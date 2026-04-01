import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="KrishiAmrut",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide Streamlit's default header/footer to make it look like a real website
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0rem;}
    iframe {border-radius: 0px;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 3. The Full KrishiAmrut Application
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KrishiAmrut - Natural Farming Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #f9fafb; }
        .tab-active { border-bottom: 4px solid #059669; color: #059669; }
        .card-gradient { background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); }
    </style>
</head>
<body class="pb-24">
    <div id="language-nav" class="sticky top-0 z-50 bg-white border-b shadow-sm p-3 flex overflow-x-auto gap-2 items-center">
        <span class="text-xs font-bold text-gray-400 uppercase flex-shrink-0 mr-2">Language:</span>
        <button onclick="setLanguage('en')" class="lang-btn px-4 py-1.5 rounded-full text-sm font-bold border border-emerald-600 transition" id="btn-en">English</button>
        <button onclick="setLanguage('ta')" class="lang-btn px-4 py-1.5 rounded-full text-sm font-bold border border-gray-200" id="btn-ta">தமிழ்</button>
        <button onclick="setLanguage('te')" class="lang-btn px-4 py-1.5 rounded-full text-sm font-bold border border-gray-200" id="btn-te">తెలుగు</button>
        <button onclick="setLanguage('hi')" class="lang-btn px-4 py-1.5 rounded-full text-sm font-bold border border-gray-200" id="btn-hi">हिन्दी</button>
    </div>

    <header class="card-gradient py-10 px-6 text-center border-b border-emerald-100">
        <h1 id="main-title" class="text-4xl font-bold text-emerald-900 mb-2">KrishiAmrut</h1>
        <p id="main-subtitle" class="text-emerald-700 max-w-2xl mx-auto mb-6 text-sm md:text-base">Scientific Bio-Inputs & Scalable Natural Farming Guide</p>
        <div class="bg-white/80 backdrop-blur p-4 rounded-2xl border border-emerald-200 inline-flex flex-col items-center">
            <span id="label-farm-size" class="text-[10px] font-bold text-emerald-800 uppercase mb-1">Farm Size</span>
            <div class="flex items-center gap-2">
                <input type="number" id="land-size" value="1" min="0.1" step="0.1" onchange="updateCalibration()" class="w-20 px-2 py-1 border-2 rounded-lg font-bold text-center text-emerald-900">
                <span id="label-acres" class="text-emerald-900 font-bold">Acre(s)</span>
            </div>
        </div>
    </header>

    <nav class="flex bg-white border-b sticky top-[60px] z-40 overflow-x-auto whitespace-nowrap px-4 justify-center">
        <button onclick="showSection('formulations')" class="nav-link px-4 py-4 font-bold text-gray-500 tab-active" id="nav-form">Formulations</button>
        <button onclick="showSection('guides')" class="nav-link px-4 py-4 font-bold text-gray-500" id="nav-guide">Personalized Advice</button>
        <button onclick="showSection('microbial')" class="nav-link px-4 py-4 font-bold text-gray-500" id="nav-micro">Microbes</button>
    </nav>

    <main class="max-w-4xl mx-auto px-4 mt-8">
        <section id="sec-formulations" class="content-section block space-y-6">
            <div class="bg-white rounded-xl shadow-sm overflow-hidden border border-emerald-100">
                <div class="bg-emerald-600 text-white px-5 py-3">
                    <h3 class="font-bold" id="j-title">Jeevamrutha (Liquid)</h3>
                </div>
                <div class="p-5">
                    <h4 class="text-xs font-bold text-emerald-800 mb-2" id="ing-header">Ingredients for <span class="current-acres">1</span> Acre:</h4>
                    <ul class="text-sm space-y-2">
                        <li class="flex justify-between border-b pb-1"><span>Water</span> <span><span class="qty" data-base="200">200</span> L</span></li>
                        <li class="flex justify-between border-b pb-1"><span>Cow Dung</span> <span><span class="qty" data-base="10">10</span> kg</span></li>
                        <li class="flex justify-between border-b pb-1"><span>Cow Urine</span> <span><span class="qty" data-base="10">10</span> L</span></li>
                        <li class="flex justify-between border-b pb-1"><span>Jaggery</span> <span><span class="qty" data-base="2">2</span> kg</span></li>
                        <li class="flex justify-between"><span>Pulse Flour</span> <span><span class="qty" data-base="2">2</span> kg</span></li>
                    </ul>
                </div>
            </div>

            <div class="bg-white rounded-xl shadow-sm overflow-hidden border border-amber-100">
                <div class="bg-amber-600 text-white px-5 py-3">
                    <h3 class="font-bold" id="g-title">Ghanjeevamrit (Solid)</h3>
                </div>
                <div class="p-5">
                    <p class="text-sm font-bold text-amber-900"><span class="qty" data-base="100">100</span> kg / <span class="current-acres">1</span> Acre</p>
                    <p class="text-xs text-gray-500 mt-1" id="g-sub">Dry fermented basal dose for soil health.</p>
                </div>
            </div>
        </section>

        <section id="sec-guides" class="content-section hidden space-y-4">
            <div class="bg-amber-50 p-5 rounded-2xl border border-amber-200">
                <h3 class="font-bold text-amber-900" id="l1-title">Dryland (Arid)</h3>
                <p class="text-xs mt-2" id="l1-low">Low Resources: Use Amrit Pani & heavy mulching.</p>
            </div>
            <div class="bg-blue-50 p-5 rounded-2xl border border-blue-200">
                <h3 class="font-bold text-blue-900" id="l3-title">Irrigated (Wet)</h3>
                <p class="text-xs mt-2" id="l3-high">Full Resources: Multi-cropping & Panchagavya spray.</p>
            </div>
        </section>

        <section id="sec-microbial" class="content-section hidden">
            <div class="bg-white p-5 rounded-xl border">
                <h3 class="font-bold text-emerald-800" id="m1-title">Rhizosphere Dynamics</h3>
                <p class="text-sm text-gray-600 mt-2" id="m1-desc">Jeevamrutha populates root zones with nitrogen-fixing bacteria.</p>
            </div>
        </section>
    </main>

    <script>
        const translations = {
            en: {
                title: "KrishiAmrut", sub: "Scientific Bio-Inputs Guide", farm: "Farm Size", acres: "Acre(s)", calc: "Calibrating...",
                navForm: "Formulations", navGuide: "Personalized Advice", navMicro: "Microbes",
                jTitle: "Jeevamrutha (Liquid)", gTitle: "Ghanjeevamrit (Solid)", ingH: "Ingredients for",
                l1T: "Dryland (Arid)", l3T: "Irrigated (Wet)", m1T: "Rhizosphere Dynamics"
            },
            ta: {
                title: "கிருஷ்ணாம்ருத்", sub: "அறிவியல் இயற்கை விவசாய வழிகாட்டி", farm: "நிலத்தின் அளவு", acres: "ஏக்கர்", calc: "கணக்கிடப்படுகிறது...",
                navForm: "கரைசல்கள்", navGuide: "தனிப்பயனாக்கப்பட்ட ஆலோசனை", navMicro: "நுண்ணுயிர்",
                jTitle: "ஜீவாமிர்தம் (திரவம்)", gTitle: "கனஜீவாமிர்தம் (திட நிலை)", ingH: "தேவையான பொருட்கள்",
                l1T: "புஞ்சை நிலம்", l3T: "நஞ்சை நிலம்", m1T: "வேர் மண்டல செயல்பாடு"
            }
        };

        function setLanguage(lang) {
            const t = translations[lang] || translations.en;
            document.getElementById('main-title').innerText = t.title;
            document.getElementById('nav-form').innerText = t.navForm;
            document.getElementById('nav-guide').innerText = t.navGuide;
            document.getElementById('nav-micro').innerText = t.navMicro;
            document.querySelectorAll('.lang-btn').forEach(b => b.classList.replace('border-emerald-600', 'border-gray-200'));
            document.getElementById('btn-'+lang).classList.replace('border-gray-200', 'border-emerald-600');
            updateCalibration();
        }

        function updateCalibration() {
            const size = parseFloat(document.getElementById('land-size').value) || 1;
            document.querySelectorAll('.current-acres').forEach(el => el.innerText = size);
            document.querySelectorAll('.qty').forEach(el => {
                const base = parseFloat(el.getAttribute('data-base'));
                el.innerText = (base * size).toFixed(1).replace('.0', '');
            });
        }

        function showSection(id) {
            document.querySelectorAll('.content-section').forEach(s => s.classList.replace('block', 'hidden'));
            document.getElementById('sec-'+id).classList.replace('hidden', 'block');
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('tab-active'));
            event.target.classList.add('tab-active');
        }

        window.onload = () => setLanguage('en');
    </script>
</body>
</html>
"""

# 4. Final Rendering
components.html(html_content, height=1800, scrolling=True)
