# -*- coding: utf-8 -*-
"""
Full Android Project Scaffolder and APK Builder for Monster Stud.
Target: Samsung Galaxy S21 & A71 (1080x2400)
"""
import os
import sys
import shutil
import subprocess
from PIL import Image

def main():
    base_dir = os.path.abspath(".")
    android_dir = os.path.join(base_dir, "android")
    app_dir = os.path.join(android_dir, "app")
    src_main = os.path.join(app_dir, "src", "main")
    java_dir = os.path.join(src_main, "java", "com", "dragoncopper", "monsterstud")
    res_dir = os.path.join(src_main, "res")
    assets_dir = os.path.join(src_main, "assets", "web")

    print(f"Base Directory: {base_dir}")
    print(f"Android Directory: {android_dir}")

    # Ensure directories
    os.makedirs(java_dir, exist_ok=True)
    os.makedirs(res_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)

    # 1. Generate Icons from media_assets/extracted_art/special_genes/primal_apex.webp
    icon_src = os.path.join(base_dir, "media_assets", "extracted_art", "special_genes", "primal_apex.webp")
    if os.path.exists(icon_src):
        img = Image.open(icon_src).convert("RGBA")
        sizes = {
            "mipmap-mdpi": 48,
            "mipmap-hdpi": 72,
            "mipmap-xhdpi": 96,
            "mipmap-xxhdpi": 144,
            "mipmap-xxxhdpi": 192,
        }
        for folder, sz in sizes.items():
            fpath = os.path.join(res_dir, folder)
            os.makedirs(fpath, exist_ok=True)
            resized = img.resize((sz, sz), Image.Resampling.LANCZOS)
            resized.save(os.path.join(fpath, "ic_launcher.png"), "PNG")
            resized.save(os.path.join(fpath, "ic_launcher_round.png"), "PNG")
        print("Generated adaptive launcher icons in all mipmap densities.")
    else:
        print("Warning: Icon source not found at", icon_src)

    # 2. Res values: strings, styles, colors
    values_dir = os.path.join(res_dir, "values")
    os.makedirs(values_dir, exist_ok=True)

    with open(os.path.join(values_dir, "strings.xml"), "w", encoding="utf-8") as f:
        f.write("""<resources>
    <string name="app_name">Monster Stud</string>
</resources>
""")

    with open(os.path.join(values_dir, "colors.xml"), "w", encoding="utf-8") as f:
        f.write("""<resources>
    <color name="black">#070B15</color>
    <color name="gold">#F6C85F</color>
</resources>
""")

    with open(os.path.join(values_dir, "styles.xml"), "w", encoding="utf-8") as f:
        f.write("""<resources>
    <style name="AppTheme" parent="android:Theme.NoTitleBar.Fullscreen">
        <item name="android:windowBackground">@color/black</item>
        <item name="android:windowFullscreen">true</item>
        <item name="android:windowContentOverlay">@null</item>
    </style>
</resources>
""")

    # 3. AndroidManifest.xml
    with open(os.path.join(src_main, "AndroidManifest.xml"), "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.dragoncopper.monsterstud">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:label="@string/app_name"
        android:theme="@style/AppTheme"
        android:hardwareAccelerated="true"
        android:supportsRtl="true">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:screenOrientation="fullSensor"
            android:configChanges="orientation|screenSize|screenLayout|keyboardHidden|uiMode"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
""")

    # 4. AndroidBridge.java
    with open(os.path.join(java_dir, "AndroidBridge.java"), "w", encoding="utf-8") as f:
        f.write("""package com.dragoncopper.monsterstud;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import android.os.VibrationEffect;
import android.os.Vibrator;
import android.view.WindowManager;
import android.webkit.JavascriptInterface;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileInputStream;

public class AndroidBridge {
    private final Activity activity;
    private final Vibrator vibrator;

    public AndroidBridge(Activity activity) {
        this.activity = activity;
        this.vibrator = (Vibrator) activity.getSystemService(Context.VIBRATOR_SERVICE);
    }

    @JavascriptInterface
    public void vibrate(long ms) {
        if (vibrator == null || !vibrator.hasVibrator()) return;
        try {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                vibrator.vibrate(VibrationEffect.createOneShot(ms, VibrationEffect.DEFAULT_AMPLITUDE));
            } else {
                vibrator.vibrate(ms);
            }
        } catch (Exception ignored) {}
    }

    @JavascriptInterface
    public void keepScreenOn(final boolean keepOn) {
        activity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                if (keepOn) {
                    activity.getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
                } else {
                    activity.getWindow().clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
                }
            }
        });
    }

    @JavascriptInterface
    public void exitApp() {
        activity.finish();
    }

    @JavascriptInterface
    public void saveBackup(String json) {
        try {
            File file = new File(activity.getFilesDir(), "save_backup.json");
            FileOutputStream fos = new FileOutputStream(file);
            fos.write(json.getBytes("UTF-8"));
            fos.close();
        } catch (Exception ignored) {}
    }

    @JavascriptInterface
    public String loadBackup() {
        try {
            File file = new File(activity.getFilesDir(), "save_backup.json");
            if (!file.exists()) return null;
            FileInputStream fis = new FileInputStream(file);
            byte[] data = new byte[(int) file.length()];
            fis.read(data);
            fis.close();
            return new String(data, "UTF-8");
        } catch (Exception e) {
            return null;
        }
    }

    @JavascriptInterface
    public void shareSave(String json) {
        try {
            Intent intent = new Intent(Intent.ACTION_SEND);
            intent.setType("application/json");
            intent.putExtra(Intent.EXTRA_SUBJECT, "Monster Stud Career Backup");
            intent.putExtra(Intent.EXTRA_TEXT, json);
            activity.startActivity(Intent.createChooser(intent, "Share Monster Stud Save Backup"));
        } catch (Exception ignored) {}
    }
}
""")

    # 5. MainActivity.java
    with open(os.path.join(java_dir, "MainActivity.java"), "w", encoding="utf-8") as f:
        f.write("""package com.dragoncopper.monsterstud;

import android.app.Activity;
import android.content.res.Configuration;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.view.WindowManager;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {
    private WebView webView;
    private AndroidBridge bridge;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Hardware acceleration & screen keep awake
        getWindow().setFlags(
            WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED,
            WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED
        );
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

        setImmersiveMode();

        webView = new WebView(this);
        setContentView(webView);

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setMediaPlaybackRequiresUserGesture(false);
        settings.setUseWideViewPort(true);
        settings.setLoadWithOverviewMode(true);
        settings.setCacheMode(WebSettings.LOAD_DEFAULT);

        bridge = new AndroidBridge(this);
        webView.addJavascriptInterface(bridge, "AndroidBridge");

        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());

        webView.loadUrl("file:///android_asset/web/index.html");
    }

    private void setImmersiveMode() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            getWindow().setDecorFitsSystemWindows(false);
            WindowInsetsController controller = getWindow().getInsetsController();
            if (controller != null) {
                controller.hide(WindowInsets.Type.statusBars() | WindowInsets.Type.navigationBars());
                controller.setSystemBarsBehavior(WindowInsetsController.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE);
            }
        } else {
            getWindow().getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_FULLSCREEN
                | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
            );
        }
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            setImmersiveMode();
        }
    }

    @Override
    public void onBackPressed() {
        if (webView != null) {
            webView.evaluateJavascript("if(window.handleAndroidBack){window.handleAndroidBack();}else{window.history.back();}", null);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (webView != null) webView.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (webView != null) webView.onResume();
        setImmersiveMode();
    }

    @Override
    protected void onDestroy() {
        if (webView != null) {
            webView.destroy();
        }
        super.onDestroy();
    }
}
""")

    # 6. Copy web/ directory into android/app/src/main/assets/web/
    web_src = os.path.join(base_dir, "web")
    print(f"Syncing web assets from {web_src} to {assets_dir}...")
    if os.path.exists(assets_dir):
        shutil.rmtree(assets_dir, ignore_errors=True)
    shutil.copytree(web_src, assets_dir)
    print("Web assets synced successfully.")

    # 7. Add AndroidBridge hook into android/app/src/main/assets/web/index.html
    web_index_path = os.path.join(assets_dir, "index.html")
    with open(web_index_path, "r", encoding="utf-8") as f:
        html = f.read()

    bridge_js = """
// Android Native Integration Hook
(function setupAndroidBridgeIntegration(){
  window.handleAndroidBack = function(){
    const finisherOverlay = document.getElementById('combatFinisherOverlay');
    if (finisherOverlay) {
      const skipBtn = document.getElementById('skipFinisherBtn');
      if (skipBtn) { skipBtn.click(); return; }
    }
    const dialog = document.getElementById('gameDialogOverlay');
    if (dialog) { dialog.remove(); document.body.style.overflow = ''; return; }
    const tooltip = document.getElementById('monsterStudGeneTooltip');
    if (tooltip && tooltip.classList.contains('visible')) {
      tooltip.classList.remove('visible'); return;
    }
    const activeView = document.querySelector('.view.active');
    if (activeView && activeView.id !== 'stable') {
      if (typeof setActiveView === 'function') {
        setActiveView('stable');
        return;
      }
    }
    if (typeof showGameConfirm === 'function') {
      showGameConfirm('Exit Game', 'Are you sure you want to exit Monster Stud?', function(){
        if (window.AndroidBridge && window.AndroidBridge.exitApp) {
          window.AndroidBridge.exitApp();
        }
      }, 'Exit', 'Stay');
    }
  };

  // Enhance combat SFX with native vibration
  const origSfx = window.playCombatSfx;
  if (typeof origSfx === 'function') {
    window.playCombatSfx = function(type) {
      origSfx(type);
      if (window.AndroidBridge && window.AndroidBridge.vibrate) {
        if (type === 'knockout') window.AndroidBridge.vibrate(80);
        else if (type === 'impact') window.AndroidBridge.vibrate(28);
      }
    };
  }
})();
"""
    html = html.replace('</head>', f'<script>{bridge_js}</script>\n</head>')
    with open(web_index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Injected AndroidBridge back-button & haptics hooks into assets web/index.html.")

    # 8. Gradle config files
    with open(os.path.join(android_dir, "settings.gradle"), "w", encoding="utf-8") as f:
        f.write("""pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "MonsterStud"
include ':app'
""")

    with open(os.path.join(android_dir, "build.gradle"), "w", encoding="utf-8") as f:
        f.write("""buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:8.3.2'
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}
""")

    with open(os.path.join(android_dir, "gradle.properties"), "w", encoding="utf-8") as f:
        f.write("""org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
android.enableJetifier=true
""")

    localappdata = os.environ.get("LOCALAPPDATA", "")
    sdk_dir = os.path.join(localappdata, "Android", "Sdk").replace("\\", "\\\\")
    with open(os.path.join(android_dir, "local.properties"), "w", encoding="utf-8") as f:
        f.write(f"sdk.dir={sdk_dir}\n")

    with open(os.path.join(app_dir, "build.gradle"), "w", encoding="utf-8") as f:
        f.write("""plugins {
    id 'com.android.application'
}

android {
    namespace 'com.dragoncopper.monsterstud'
    compileSdk 34

    defaultConfig {
        applicationId "com.dragoncopper.monsterstud"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0.0"
    }

    buildTypes {
        release {
            minifyEnabled false
            signingConfig signingConfigs.debug
        }
    }

    compileOptions {
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }

    sourceSets {
        main {
            assets.srcDirs = ['src/main/assets']
        }
    }
}

dependencies {
    // Zero third-party dependencies required; uses pure native Android SDK WebView
}
""")

    print("Android project structure scaffolded successfully.")

if __name__ == "__main__":
    main()
