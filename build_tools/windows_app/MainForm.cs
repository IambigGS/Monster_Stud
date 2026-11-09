using System;
using System.Drawing;
using System.IO;
using System.IO.Compression;
using System.Reflection;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Web.WebView2.Core;
using Microsoft.Web.WebView2.WinForms;

namespace DragonCopper.MonsterStud
{
    public class MainForm : Form
    {
        private readonly WebView2 webView;
        private bool isFullscreen = false;
        private FormBorderStyle previousBorderStyle = FormBorderStyle.Sizable;
        private FormWindowState previousWindowState = FormWindowState.Normal;
        private Rectangle previousBounds = Rectangle.Empty;

        public MainForm()
        {
            Text = "Monster Stud — Genetic League (v1.0.0)";
            ClientSize = new Size(1280, 800);
            MinimumSize = new Size(960, 600);
            StartPosition = FormStartPosition.CenterScreen;
            BackColor = Color.FromArgb(16, 19, 30); // #10131E
            KeyPreview = true;

            try
            {
                Icon = Icon.ExtractAssociatedIcon(Application.ExecutablePath);
            }
            catch {}

            webView = new WebView2
            {
                Dock = DockStyle.Fill,
                DefaultBackgroundColor = Color.FromArgb(16, 19, 30)
            };

            Controls.Add(webView);

            KeyDown += MainForm_KeyDown;
            Load += MainForm_Load;
        }

        private async void MainForm_Load(object? sender, EventArgs e)
        {
            try
            {
                string localApp = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
                string baseAppDir = Path.Combine(localApp, "DragonCopper", "MonsterStud");
                string versionDir = Path.Combine(baseAppDir, "v1.0.0");
                string webDir = Path.Combine(versionDir, "web");
                string profileDir = Path.Combine(baseAppDir, "WebViewProfile");

                EnsureWebAssetsExtracted(webDir);

                // Enable autoplay without user gesture requirements so audio and video play automatically on boot
                var options = new CoreWebView2EnvironmentOptions
                {
                    AdditionalBrowserArguments = "--autoplay-policy=no-user-gesture-required"
                };

                var env = await CoreWebView2Environment.CreateAsync(null, profileDir, options);
                await webView.EnsureCoreWebView2Async(env);

                webView.CoreWebView2.Settings.IsStatusBarEnabled = false;
                webView.CoreWebView2.Settings.AreDefaultContextMenusEnabled = false;
                webView.CoreWebView2.Settings.IsZoomControlEnabled = true;

                webView.CoreWebView2.SetVirtualHostNameToFolderMapping(
                    "app.monsterstud.local",
                    webDir,
                    CoreWebView2HostResourceAccessKind.Allow
                );

                webView.CoreWebView2.Navigate("https://app.monsterstud.local/index.html");
            }
            catch (Exception ex)
            {
                MessageBox.Show(
                    "Failed to initialize Monster Stud:\n\n" + ex.Message,
                    "Startup Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error
                );
            }
        }

        private void EnsureWebAssetsExtracted(string webDir)
        {
            Directory.CreateDirectory(webDir);

            var assembly = Assembly.GetExecutingAssembly();
            using var stream = assembly.GetManifestResourceStream("DragonCopper.MonsterStud.assets.zip");
            if (stream == null)
            {
                throw new FileNotFoundException("Embedded assets.zip could not be found in assembly resources.");
            }

            using var archive = new ZipArchive(stream, ZipArchiveMode.Read);
            archive.ExtractToDirectory(webDir, overwriteFiles: true);
        }

        private void MainForm_KeyDown(object? sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.F11)
            {
                ToggleFullscreen();
                e.Handled = true;
            }
            else if (e.KeyCode == Keys.Escape && isFullscreen)
            {
                ToggleFullscreen();
                e.Handled = true;
            }
            else if (e.KeyCode == Keys.F12)
            {
                webView.CoreWebView2?.OpenDevToolsWindow();
                e.Handled = true;
            }
        }

        private void ToggleFullscreen()
        {
            if (!isFullscreen)
            {
                previousBorderStyle = FormBorderStyle;
                previousWindowState = WindowState;
                previousBounds = Bounds;

                FormBorderStyle = FormBorderStyle.None;
                WindowState = FormWindowState.Normal;
                Bounds = Screen.FromControl(this).Bounds;
                isFullscreen = true;
            }
            else
            {
                FormBorderStyle = previousBorderStyle;
                WindowState = previousWindowState;
                Bounds = previousBounds;
                isFullscreen = false;
            }
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                webView?.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
