package com.dragoncopper.monsterstud;

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
        Vibrator v = null;
        try {
            v = (Vibrator) activity.getSystemService(Context.VIBRATOR_SERVICE);
        } catch (Exception ignored) {}
        this.vibrator = v;
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
                try {
                    if (keepOn) {
                        activity.getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
                    } else {
                        activity.getWindow().clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
                    }
                } catch (Exception ignored) {}
            }
        });
    }

    @JavascriptInterface
    public void exitApp() {
        try {
            activity.finish();
        } catch (Exception ignored) {}
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
