# الورقة الذهبية GPC — Golden Paper Co.

الموقع الرسمي لشركة **الورقة الذهبية للطباعة** في تبوك، المملكة العربية السعودية.
موقع ثابت (Static Site) منشور عبر **GitHub Pages**.

🌐 الموقع: [waraqadhahabiya.com](https://www.waraqadhahabiya.com) · 📍 تبوك، حي الراجحي، خلف مجمع العصر

---

## 📂 بنية المشروع

```
golden-paper/
├── index.html              الصفحة الرئيسية (تطبيق React مبني)
├── team.html               صفحة فريق العمل
├── favicon.svg             أيقونة الموقع (شعار GPC)
├── opengraph.jpg           صورة المشاركة الاجتماعية
├── .nojekyll               تعطيل Jekyll على GitHub Pages
│
├── assets/                 حزم التطبيق المبني (Vite build — لا تُعدّل يدوياً)
│   ├── index-DATgigZ8.js
│   └── index-DzwE51Dp.css
│
├── brand/                  الهوية البصرية (انظر brand/README.md)
│   ├── logo-icon.svg       شعار الحرف C (SVG متجهي)
│   ├── brand.css           نظام التصميم: ألوان + مكوّنات
│   └── README.md
│
├── cards/                  البطاقات الرقمية لفريق العمل
│   ├── index.html          دليل البطاقات
│   ├── abu-abdulkarim.html · khalid.html · abdulkarim.html · mustafa.html
│   └── qr/*.svg            أكواد QR (روابط واتساب)
│
├── images/                 صور الموقع
│   ├── goldy.png           شخصية "Goldy"
│   ├── clients/            شعارات العملاء
│   │   └── partners/       8 شعارات شركاء (بوتشيلي، ذا بالم، سبوت لايت …) — محسّنة للويب
│   └── opt/                نسخ WebP مُحسّنة
│
└── tools/
    └── gen_cards.py        مولّد البطاقات الرقمية من بيانات موحّدة
```

---

## 🧩 المكوّنات

### الصفحة الرئيسية (`index.html`)
تطبيق React مبني بـ Vite (الشيفرة المصدرية في مستودع منفصل). لا تُعدّل ملفات `assets/`
يدوياً — أي تغيير في المحتوى يتطلب إعادة البناء من المصدر ونسخ المخرجات هنا.

### صفحة الفريق (`team.html`)
صفحة مستقلة تعرض أعضاء الفريق وتربط ببطاقة كل عضو + الخدمات ومعلومات التواصل.

### البطاقات الرقمية (`cards/`)
بطاقة عمل رقمية لكل عضو فيها:
- **حفظ جهة الاتصال** (تنزيل ملف vCard — يعمل بدون إنترنت)
- أزرار واتساب / اتصال / بريد / موقع / خريطة
- **رمز QR** للتواصل عبر واتساب
- روابط التواصل الاجتماعي (@GP1.SA)

**التوليد:** البطاقات مولّدة من `tools/gen_cards.py`. لتعديل بيانات عضو أو إضافة عضو:
```bash
# 1) عدّل قائمة PEOPLE في tools/gen_cards.py
# 2) لتوليد أكواد QR جديدة (إن تغيّرت الأرقام):
pip install segno
python - <<'PY'
import segno
segno.make("https://wa.me/9665XXXXXXXX", error='m').save(
    "cards/qr/<slug>.svg", scale=1, border=2, dark="#1A0D3D", light="#ffffff")
PY
# 3) أعد توليد صفحات البطاقات:
python3 tools/gen_cards.py
```

---

## 🎨 الهوية
الألوان والمكوّنات موثّقة في [`brand/README.md`](brand/README.md).
الأساسي بنفسجي `#643DFF` والمميّز ذهبي `#FFC42E`، خطوط Noto Kufi Arabic + Cairo.

---

## 🚀 النشر
يُنشر تلقائياً عبر GitHub Pages من الفرع `main`. وجود `.nojekyll` يمنع معالجة Jekyll.
الصفحات كلها ثابتة (HTML/CSS/JS) وتعمل مباشرة دون خطوة بناء (عدا `index.html`
الذي مخرجاته جاهزة في `assets/`).
