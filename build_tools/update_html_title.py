import os

html_path = os.path.join('web', 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

target = '<meta name="monster-stud-build" content="2026-11-07-tester-clean-start-isolated-save">\n<title>Monster Stud — Tester Edition (Fresh Start)</title>'
if target not in c:
    target = target.replace('\n', '\r\n')

replacement = '''<meta name="monster-stud-build" content="2026-11-08-v1.0.0-production-release">
<title>Monster Stud — Genetic League</title>
<!-- Telegram Mini App (TMA) SDK -->
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<script>
  (function(){
    try {
      if (window.Telegram && window.Telegram.WebApp) {
        window.Telegram.WebApp.ready();
        window.Telegram.WebApp.expand();
        if (typeof window.Telegram.WebApp.setHeaderColor === 'function') {
          window.Telegram.WebApp.setHeaderColor('#10131e');
        }
        if (typeof window.Telegram.WebApp.setBackgroundColor === 'function') {
          window.Telegram.WebApp.setBackgroundColor('#10131e');
        }
      }
    } catch(e) {}
  })();
</script>'''

if '\r\n' in c:
    replacement = replacement.replace('\n', '\r\n')

if target in c:
    c = c.replace(target, replacement, 1)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Successfully updated web/index.html")
else:
    print("Target string was not found.")
