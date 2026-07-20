# -*- coding: utf-8 -*-
"""مولّد البطاقات الرقمية لـ الورقة الذهبية GPC.
يُنتج cards/<slug>.html لكل عضو + cards/index.html من بيانات موحّدة.
التشغيل:  python3 tools/gen_cards.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "cards")

COMPANY_AR = "الورقة الذهبية"
GPC = "GPC"
WEBSITE = "https://www.waraqadhahabiya.com"
WEBSITE_DISP = "waraqadhahabiya.com"
LOCATION = "تبوك، حي الراجحي، خلف مجمع العصر"
MAPS = ("https://www.google.com/maps/search/?api=1&query="
        "%D8%A7%D9%84%D9%88%D8%B1%D9%82%D8%A9%20%D8%A7%D9%84%D8%B0%D9%87%D8%A8%D9%8A%D8%A9%20GPC%20%D8%AA%D8%A8%D9%88%D9%83")
SOCIAL = "GP1.SA"
INSTAGRAM = "https://instagram.com/GP1.SA"
TIKTOK = "https://tiktok.com/@GP1.SA"
SNAPCHAT = "https://snapchat.com/add/GP1.SA"
EMAIL = "g.paper2023@gmail.com"

PEOPLE = [
  dict(slug="abu-abdulkarim", name_ar="أبو عبدالكريم", name_en="ABU ABDUL ALKARIM",
       title_ar="المدير العام", title_en="Managing Director", initials="أ",
       given="أبو عبدالكريم", family="",
       phones=[("053 006 3686", "+966530063686")], whatsapp="966530063686"),
  dict(slug="khalid", name_ar="خالد محمد", name_en="KHALID MOHAMMED",
       title_ar="المدير التنفيذي", title_en="Executive Manager", initials="خ",
       given="خالد", family="محمد",
       phones=[("0500 727 188", "+966500727188")], whatsapp="966500727188"),
  dict(slug="abdulkarim", name_ar="عبدالكريم محمد", name_en="ABDUL ALKARIM",
       title_ar="أخصائي تسويق", title_en="Marketing Specialist", initials="ع",
       given="عبدالكريم", family="محمد",
       phones=[("055 455 4338", "+966554554338"), ("053 307 4842", "+966533074842")],
       whatsapp="966554554338"),
  dict(slug="mustafa", name_ar="مصطفى محمد", name_en="MUSTAFA MOHAMMED",
       title_ar="مصمم جرافيك", title_en="Graphic Designer", initials="م",
       given="مصطفى", family="محمد",
       phones=[("0500 765 277", "+966500765277")], whatsapp="966500765277"),
]

IC = {
 "whatsapp":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.9 4.44-9.9 9.9 0 1.75.46 3.45 1.32 4.95L2.05 22l5.28-1.38a9.87 9.87 0 0 0 4.71 1.2h.01c5.46 0 9.9-4.44 9.9-9.9 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2Zm0 1.8c2.16 0 4.19.84 5.72 2.37a8.06 8.06 0 0 1 2.37 5.73c0 4.46-3.63 8.1-8.1 8.1a8.1 8.1 0 0 1-4.13-1.13l-.3-.18-3.05.8.82-2.98-.2-.31a8.05 8.05 0 0 1-1.24-4.3c0-4.46 3.63-8.1 8.11-8.1Zm4.62 10.24c-.25-.13-1.48-.73-1.71-.81-.23-.09-.4-.13-.56.12-.17.25-.64.81-.79.98-.14.16-.29.18-.54.06-.25-.12-1.05-.39-2-1.24-.74-.66-1.24-1.47-1.38-1.72-.15-.25-.02-.39.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.36-.77-1.86-.2-.48-.41-.42-.56-.43l-.48-.01c-.16 0-.43.06-.66.31-.23.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.25 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.15-1.19-.06-.11-.23-.17-.48-.29Z"/></svg>',
 "phone":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.6 15.6 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1C10.4 21 3 13.6 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1.02l-2.2 2.2Z"/></svg>',
 "email":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Zm0 2v.01l8 5 8-5V6H4Zm16 2.24-7.47 4.67a1 1 0 0 1-1.06 0L4 8.24V18h16V8.24Z"/></svg>',
 "contact":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm0 2c-3.31 0-8 1.67-8 5v1h16v-1c0-3.33-4.69-5-8-5Zm7-9v2h2v2h-2v2h-2V9h-2V7h2V5h2Z"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm6.93 6h-2.95a15.7 15.7 0 0 0-1.38-3.56A8.03 8.03 0 0 1 18.93 8ZM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96ZM4.26 14a7.96 7.96 0 0 1 0-4h3.38a16.6 16.6 0 0 0 0 4H4.26Zm.81 2h2.95c.35 1.28.82 2.48 1.38 3.56A8.03 8.03 0 0 1 5.07 16Zm2.95-8H5.07a8.03 8.03 0 0 1 4.33-3.56A15.7 15.7 0 0 0 8.02 8ZM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96ZM14.34 14H9.66a14.7 14.7 0 0 1 0-4h4.68a14.7 14.7 0 0 1 0 4Zm.28 5.56c.56-1.08 1.03-2.28 1.38-3.56h2.95a8.03 8.03 0 0 1-4.33 3.56ZM16.36 14a16.6 16.6 0 0 0 0-4h3.38a7.96 7.96 0 0 1 0 4h-3.38Z"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>',
 "instagram":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.7 3.7 0 0 1-1.38-.9 3.7 3.7 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16Zm0 3.24A6.6 6.6 0 1 0 12 18.6 6.6 6.6 0 0 0 12 5.4Zm0 10.89A4.29 4.29 0 1 1 12 7.71a4.29 4.29 0 0 1 0 8.58Zm6.85-11.15a1.54 1.54 0 1 1-3.08 0 1.54 1.54 0 0 1 3.08 0Z"/></svg>',
 "tiktok":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 5.82a4.28 4.28 0 0 1-1.04-2.82h-3.1v12.34a2.53 2.53 0 0 1-2.53 2.4 2.53 2.53 0 1 1 .7-4.96V9.6a5.63 5.63 0 1 0 4.93 5.58V9.01a7.34 7.34 0 0 0 4.3 1.38V7.3a4.28 4.28 0 0 1-3.26-1.48Z"/></svg>',
 "snapchat":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.01 2c1.86.02 3.65.98 4.4 2.94.28.72.24 1.62.22 2.42-.01.28-.03.6-.04.94.13.07.32.11.53.11.3-.01.66-.11.98-.28.13-.07.28-.1.42-.1.3 0 .58.15.7.44.16.4-.08.75-.6.98l-.4.18c-.44.2-.99.44-1.14.79-.08.19-.03.42.05.6.02.03 1.06 2.34 3.3 2.71.24.04.42.25.4.5-.01.09-.03.17-.07.24-.28.66-1.5.92-2.2 1.03-.08.01-.13.1-.15.24-.02.1-.04.2-.08.32-.05.16-.2.26-.4.26h-.04c-.14 0-.32-.03-.55-.07-.35-.07-.77-.14-1.28-.14-.3 0-.62.03-.94.08-.62.11-1.14.5-1.7.9-.72.53-1.53 1.12-2.79 1.12h-.14c-1.26 0-2.06-.59-2.78-1.11-.57-.42-1.09-.8-1.71-.91a5.9 5.9 0 0 0-.94-.08c-.53 0-.96.09-1.28.15-.22.04-.4.07-.53.07-.27.01-.4-.15-.46-.28-.04-.11-.06-.22-.08-.31-.03-.14-.07-.23-.15-.24-.7-.11-1.92-.37-2.2-1.04a.53.53 0 0 1-.06-.23c-.02-.25.15-.46.4-.5 2.23-.37 3.27-2.68 3.3-2.72.08-.17.13-.4.05-.6-.15-.34-.7-.58-1.14-.78-.14-.06-.28-.12-.4-.18-.68-.3-.77-.66-.66-.98.11-.32.5-.5.87-.36.28.13.6.2.85.2.22 0 .38-.04.48-.09v-.03c-.02-.34-.04-.65-.05-.93-.02-.8-.06-1.7.22-2.42C8.34 2.98 10.13 2.02 12 2h.01Z"/></svg>',
}

TEMPLATE = r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
  <title>@@NAME_AR@@ — @@COMPANY_AR@@ @@GPC@@</title>
  <meta name="description" content="بطاقة عمل رقمية — @@NAME_AR@@، @@TITLE_AR@@، @@COMPANY_AR@@ @@GPC@@." />
  <link rel="icon" type="image/svg+xml" href="../favicon.svg" />
  <meta property="og:type" content="profile" />
  <meta property="og:title" content="@@NAME_AR@@ — @@COMPANY_AR@@ @@GPC@@" />
  <meta property="og:description" content="@@TITLE_AR@@ | @@TITLE_EN@@" />
  <meta name="theme-color" content="#1A0D3D" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Kufi+Arabic:wght@300;400;500;600;700;800;900&family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../brand/brand.css">
  <style>
    body{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:28px 16px;color:#fff;
      background:radial-gradient(1200px 600px at 80% -10%,rgba(123,92,255,.5),transparent 60%),
        radial-gradient(900px 500px at 0% 110%,rgba(255,196,46,.14),transparent 55%),
        linear-gradient(160deg,#2b1856 0%,#1a0d3d 60%,#150a33 100%);position:relative;overflow-x:hidden}
    body::before{content:"";position:fixed;inset:0;z-index:0;opacity:.05;pointer-events:none;
      background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 96 96'%3E%3Cpath fill='%23ffffff' fill-rule='evenodd' d='M29 16 H71 V56 L55 74 H25 Z M40 30 H60 L64 34 V44 H53 V60 H40 Z'/%3E%3C/svg%3E");
      background-size:120px 120px}
    .card{position:relative;z-index:1;width:100%;max-width:430px;background:rgba(255,255,255,.055);
      border:1px solid rgba(255,255,255,.12);border-radius:var(--gpc-radius);box-shadow:var(--gpc-shadow);
      backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);padding:26px 24px 30px;overflow:hidden}
    .card__top{display:flex;align-items:center;justify-content:space-between;margin-bottom:22px}
    .gpc-lockup .gpc-mark{color:var(--gpc-gold)}
    .gpc-lockup .gpc-word b{color:#fff}.gpc-lockup .gpc-word span{color:var(--gpc-gold)}
    .avatar{width:96px;height:96px;margin:6px auto 14px;border-radius:50%;display:flex;align-items:center;justify-content:center;
      font-weight:800;font-size:2.4rem;color:var(--gpc-purple-deep);background:linear-gradient(145deg,#FFE195,#FFC42E);
      box-shadow:0 0 0 6px rgba(255,196,46,.14),0 0 0 12px rgba(255,196,46,.07)}
    .name{text-align:center;font-weight:800;font-size:1.7rem;margin:0 0 2px}
    .name-en{text-align:center;font-weight:600;font-size:.8rem;letter-spacing:2px;color:var(--gpc-gold-2);opacity:.9;margin-bottom:10px}
    .title{text-align:center;margin-bottom:22px}
    .title small{display:block;margin-top:6px;font-size:.72rem;letter-spacing:1.5px;opacity:.6}
    .sec-label{font-size:.72rem;letter-spacing:2px;opacity:.55;margin:22px 4px 10px;text-align:center}
    .qr-wrap{display:flex;flex-direction:column;align-items:center;gap:10px;margin-top:6px}
    .qr-tile{background:#fff;padding:12px;border-radius:16px;width:150px;height:150px;box-shadow:var(--gpc-shadow-sm)}
    .qr-tile img{width:100%;height:100%;image-rendering:pixelated}
    .social{display:flex;justify-content:center;gap:14px;margin-top:22px}
    .social a{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;
      background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);color:#fff;transition:background .2s,transform .12s}
    .social a:hover{background:var(--gpc-gold);color:var(--gpc-purple-deep);transform:translateY(-2px)}
    .social a svg{width:20px;height:20px}
    .handle{text-align:center;font-size:.82rem;opacity:.7;margin-top:10px;letter-spacing:1px}
    .addr{display:flex;align-items:center;justify-content:center;gap:6px;margin-top:8px;font-size:.82rem;opacity:.72}
    .addr svg{width:16px;height:16px;color:var(--gpc-gold)}
    .foot{text-align:center;margin-top:24px;padding-top:16px;border-top:1px solid rgba(255,255,255,.1);font-size:.72rem;opacity:.5}
    .foot a{color:var(--gpc-gold-2)}
    @media (max-width:380px){.name{font-size:1.45rem}.gpc-actions{grid-template-columns:1fr}}
  </style>
</head>
<body>
  <main class="card">
    <div class="card__top">
      <a class="gpc-lockup" href="@@WEBSITE@@" target="_blank" rel="noopener" aria-label="@@COMPANY_AR@@ @@GPC@@">
        <span class="gpc-mark">@@MARK@@</span>
        <span class="gpc-word"><b>@@COMPANY_AR@@</b><span>@@GPC@@</span></span>
      </a>
      <span class="gpc-chip">بطاقة رقمية</span>
    </div>

    <div class="avatar">@@INITIALS@@</div>
    <h1 class="name">@@NAME_AR@@</h1>
    <div class="name-en">@@NAME_EN@@</div>
    <div class="title">
      <span class="gpc-chip">@@TITLE_AR@@</span>
      <small>@@TITLE_EN@@</small>
    </div>

    <nav class="gpc-actions" aria-label="إجراءات التواصل">
      <a class="gpc-btn gpc-btn--gold gpc-btn--wide" href="https://wa.me/@@WHATSAPP@@" target="_blank" rel="noopener">@@IC_WHATSAPP@@ تواصل على واتساب</a>
@@CALL_BTNS@@
      <a class="gpc-btn gpc-btn--ghost" href="mailto:@@EMAIL@@">@@IC_EMAIL@@ البريد</a>
      <button class="gpc-btn gpc-btn--solid gpc-btn--wide" id="saveContact" type="button">@@IC_CONTACT@@ حفظ جهة الاتصال</button>
      <a class="gpc-btn gpc-btn--ghost" href="@@WEBSITE@@" target="_blank" rel="noopener">@@IC_GLOBE@@ زيارة الموقع</a>
      <a class="gpc-btn gpc-btn--ghost" href="@@MAPS@@" target="_blank" rel="noopener">@@IC_PIN@@ الخريطة</a>
    </nav>

    <div class="sec-label">امسح للتواصل عبر واتساب</div>
    <div class="qr-wrap">
      <div class="qr-tile"><img src="qr/@@SLUG@@.svg" alt="رمز QR للتواصل مع @@NAME_AR@@ عبر واتساب" /></div>
    </div>

    <div class="social">
      <a href="@@INSTAGRAM@@" target="_blank" rel="noopener" aria-label="إنستغرام">@@IC_INSTAGRAM@@</a>
      <a href="@@TIKTOK@@" target="_blank" rel="noopener" aria-label="تيك توك">@@IC_TIKTOK@@</a>
      <a href="@@SNAPCHAT@@" target="_blank" rel="noopener" aria-label="سناب شات">@@IC_SNAPCHAT@@</a>
    </div>
    <div class="handle">@@SOCIAL@@</div>
    <div class="addr">@@IC_PIN@@ @@LOCATION@@</div>

    <div class="foot"><a href="../team.html">← فريق @@COMPANY_AR@@</a> · @@WEBSITE_DISP@@</div>
  </main>

  <script>
    (function(){
      var vcard = @@VCARD_JS@@;
      var btn = document.getElementById('saveContact');
      if(!btn) return;
      btn.addEventListener('click', function(){
        var blob = new Blob([vcard], {type:'text/vcard;charset=utf-8'});
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url; a.download = '@@SLUG@@.vcf';
        document.body.appendChild(a); a.click(); document.body.removeChild(a);
        setTimeout(function(){ URL.revokeObjectURL(url); }, 1500);
      });
    })();
  </script>
</body>
</html>
"""

def build_vcard(p):
    lines = ["BEGIN:VCARD", "VERSION:3.0",
             "N:%s;%s;;;" % (p["family"], p["given"]),
             "FN:%s" % p["name_ar"],
             "ORG:%s %s" % (COMPANY_AR, GPC),
             "TITLE:%s" % p["title_ar"]]
    for _disp, e164 in p["phones"]:
        lines.append("TEL;TYPE=CELL,VOICE:%s" % e164)
    lines += ["EMAIL;TYPE=INTERNET:%s" % EMAIL, "URL:%s" % WEBSITE,
              "ADR;TYPE=WORK:;;حي الراجحي، خلف مجمع العصر;تبوك;;;السعودية",
              "END:VCARD"]
    return "\\r\\n".join(lines)

def call_buttons(p):
    out = []
    phones = p["phones"]
    for disp, e164 in phones:
        label = "اتصال" if len(phones) == 1 else disp
        out.append('      <a class="gpc-btn gpc-btn--ghost" href="tel:%s">%s <span dir="ltr">%s</span></a>'
                   % (e164, IC["phone"], label))
    return "\n".join(out)

os.makedirs(OUT, exist_ok=True)
mark_svg = open(os.path.join(ROOT, "brand", "logo-icon.svg")).read().strip()

for p in PEOPLE:
    page = TEMPLATE
    repl = {
      "NAME_AR": p["name_ar"], "NAME_EN": p["name_en"],
      "TITLE_AR": p["title_ar"], "TITLE_EN": p["title_en"],
      "INITIALS": p["initials"], "SLUG": p["slug"], "WHATSAPP": p["whatsapp"],
      "EMAIL": EMAIL, "WEBSITE": WEBSITE, "WEBSITE_DISP": WEBSITE_DISP,
      "MAPS": MAPS, "LOCATION": LOCATION, "SOCIAL": SOCIAL,
      "INSTAGRAM": INSTAGRAM, "TIKTOK": TIKTOK, "SNAPCHAT": SNAPCHAT,
      "COMPANY_AR": COMPANY_AR, "GPC": GPC, "MARK": mark_svg,
      "CALL_BTNS": call_buttons(p),
      "IC_WHATSAPP": IC["whatsapp"], "IC_PHONE": IC["phone"], "IC_EMAIL": IC["email"],
      "IC_CONTACT": IC["contact"], "IC_GLOBE": IC["globe"], "IC_PIN": IC["pin"],
      "IC_INSTAGRAM": IC["instagram"], "IC_TIKTOK": IC["tiktok"], "IC_SNAPCHAT": IC["snapchat"],
      "VCARD_JS": '"%s"' % build_vcard(p),
    }
    for k, v in repl.items():
        page = page.replace("@@%s@@" % k, v)
    with open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote cards/%s.html" % p["slug"])

# ---------- cards/index.html : دليل البطاقات ----------
cards_dir_items = []
for p in PEOPLE:
    cards_dir_items.append(
      '      <a class="dir-card" href="%s.html">\n'
      '        <span class="dir-av">%s</span>\n'
      '        <span class="dir-meta"><b>%s</b><small>%s</small></span>\n'
      '        <span class="dir-arrow">‹</span>\n'
      '      </a>' % (p["slug"], p["initials"], p["name_ar"], p["title_ar"]))

INDEX = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
  <title>البطاقات الرقمية — {C} {G}</title>
  <link rel="icon" type="image/svg+xml" href="../favicon.svg" />
  <meta name="theme-color" content="#1A0D3D" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Kufi+Arabic:wght@300;400;500;600;700;800;900&family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../brand/brand.css">
  <style>
    body{{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:32px 16px;color:#fff;
      background:radial-gradient(1000px 500px at 80% -10%,rgba(123,92,255,.5),transparent 60%),linear-gradient(160deg,#2b1856,#1a0d3d 65%,#150a33)}}
    .wrap{{width:100%;max-width:460px}}
    .head{{text-align:center;margin-bottom:26px}}
    .head .gpc-mark{{width:64px;height:64px;color:var(--gpc-gold);margin:0 auto 14px}}
    .head h1{{font-size:1.5rem;margin:0 0 4px}}
    .head p{{opacity:.6;font-size:.9rem;margin:0}}
    .dir-card{{display:flex;align-items:center;gap:14px;padding:14px 16px;margin-bottom:12px;border-radius:16px;
      background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);transition:background .2s,transform .12s}}
    .dir-card:hover{{background:rgba(255,255,255,.12);transform:translateY(-2px)}}
    .dir-av{{width:50px;height:50px;flex:none;border-radius:50%;display:flex;align-items:center;justify-content:center;
      font-weight:800;font-size:1.35rem;color:var(--gpc-purple-deep);background:linear-gradient(145deg,#FFE195,#FFC42E)}}
    .dir-meta{{flex:1;line-height:1.3}}.dir-meta b{{display:block;font-size:1.05rem}}.dir-meta small{{opacity:.6;font-size:.82rem}}
    .dir-arrow{{opacity:.4;font-size:1.6rem;font-weight:700}}
    .foot{{text-align:center;margin-top:22px;font-size:.78rem;opacity:.5}}.foot a{{color:var(--gpc-gold-2)}}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="head">
      <span class="gpc-mark">{MARK}</span>
      <h1>{C} {G}</h1>
      <p>البطاقات الرقمية لفريق العمل</p>
    </div>
{ITEMS}
    <div class="foot"><a href="../team.html">صفحة الفريق</a> · <a href="{WEB}" target="_blank" rel="noopener">{WEBDISP}</a></div>
  </div>
</body>
</html>
""".format(C=COMPANY_AR, G=GPC, MARK=mark_svg, ITEMS="\n".join(cards_dir_items),
           WEB=WEBSITE, WEBDISP=WEBSITE_DISP)

with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(INDEX)
print("wrote cards/index.html")
print("done")
