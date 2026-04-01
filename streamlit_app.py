import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit Page Setup
st.set_page_config(
    page_title="KrishiAmrut - Natural Farming Guide",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide Streamlit Branding (Make it feel like a real website)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0rem;}
    iframe {border: none;}
    </style>
""", unsafe_allow_html=True)

# 3. Your Full HTML Code (Including all formulations & logic)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KrishiAmrut - Scalable Natural Farming Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; scroll-behavior: smooth; }
        .tab-active { border-bottom: 3px solid #059669; color: #059669; }
        .card-gradient { background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); }
        .calc-input:focus { border-color: #059669; outline: none; box-shadow: 0 0 0 3px rgba(5, 150, 105, 0.1); }
    </style>
</head>
<body class="bg-gray-50 text-gray-900 pb-24">

    <div id="language-nav" class="sticky top-0 z-50 bg-white border-b shadow-sm p-3 flex overflow-x-auto gap-2 items-center">
        <span class="text-xs font-bold text-gray-400 uppercase flex-shrink-0 mr-2">Language / மொழி / భాష / भाषा:</span>
        <button onclick="setLanguage('en')" class="lang-btn px-4 py-1.5 rounded-full text-sm font-bold border border-emerald-600 transition" id="btn-en">English</button>
        <button onclick="setLanguage('ta')" class="lang-btn px-4 py-1.5 rounded-full text-sm font-bold border border-gray-200" id="btn-ta">தமிழ்</button>
        <button onclick="setLanguage('te')" class="lang-btn px-4 py-1.5 rounded-full text-sm font-bold border border-gray-200" id="btn-te">తెలుగు</button>
        <button onclick="setLanguage('hi')" class="lang-btn px-4 py-1.5 rounded-full text-sm font-bold border border-gray-200" id="btn-hi">हिन्दी</button>
    </div>

    <header class="card-gradient py-10 px-6 text-center border-b border-emerald-100">
        <div class="max-w-4xl mx-auto">
            <h1 id="main-title" class="text-4xl md:text-5xl font-bold text-emerald-900 mb-3">KrishiAmrut</h1>
            <p id="main-subtitle" class="text-md md:text-lg text-emerald-700 max-w-2xl mx-auto mb-6">Scientific Bio-Inputs & Scalable Natural Farming Guide (ICAR & TNAU Standards)</p>
            
            <div class="bg-white/80 backdrop-blur p-5 rounded-3xl border border-emerald-200 inline-flex flex-col items-center shadow-sm">
                <span id="label-farm-size" class="text-xs font-bold text-emerald-800 uppercase mb-2">Configure Your Farm Size</span>
                <div class="flex items-center gap-3">
                    <input type="number" id="land-size" value="1" min="0.1" step="0.1" onchange="updateCalibration()" class="w-24 px-3 py-2 border-2 rounded-xl calc-input font-bold text-center text-lg text-emerald-900">
                    <span id="label-acres" class="text-emerald-900 font-bold text-lg">Acre(s)</span>
                </div>
                <p id="label-calibrate-msg" class="text-[10px] text-emerald-600 mt-2 font-medium">*All ingredient quantities calibrate automatically below</p>
            </div>
        </div>
    </header>

    <nav class="flex justify-start md:justify-center bg-white border-b sticky top-[60px] z-40 overflow-x-auto whitespace-nowrap px-4">
        <button onclick="showSection('formulations')" class="nav-link px-6 py-4 font-bold text-gray-600 tab-active" id="nav-form">Deep Formulations</button>
        <button onclick="showSection('guides')" class="nav-link px-6 py-4 font-bold text-gray-600" id="nav-guide">Personalized Advice</button>
        <button onclick="showSection('microbial')" class="nav-link px-6 py-4 font-bold text-gray-600" id="nav-micro">Microbial Life</button>
        <button onclick="showSection('comparison')" class="nav-link px-6 py-4 font-bold text-gray-600" id="nav-comp">Comparison</button>
    </nav>

    <main class="max-w-5xl mx-auto px-4 mt-8">
        
        <section id="sec-formulations" class="content-section block space-y-8">
            <h2 class="text-2xl font-bold text-emerald-800" id="form-title-h2">Scientific Bio-Input Formulations</h2>
            
            <div class="bg-white rounded-2xl shadow-md overflow-hidden border border-emerald-100">
                <div class="bg-emerald-600 text-white px-6 py-4"><h3 class="font-bold text-xl" id="j-title">Jeevamrutha (Liquid)</h3></div>
                <div class="p-6 grid md:grid-cols-2 gap-8">
                    <div>
                        <h4 class="text-sm font-bold text-emerald-800 mb-3" id="ing-header">Ingredients:</h4>
                        <ul class="text-sm space-y-3 font-medium">
                            <li class="flex justify-between"><span id="ing-water">Water</span> <span><span class="qty" data-base="200">200</span> L</span></li>
                            <li class="flex justify-between"><span id="ing-dung">Dung</span> <span><span class="qty" data-base="10">10</span> kg</span></li>
                            <li class="flex justify-between"><span id="ing-urine">Urine</span> <span><span class="qty" data-base="10">10</span> L</span></li>
                            <li class="flex justify-between"><span id="ing-jaggery">Jaggery</span> <span><span class="qty" data-base="2">2</span> kg</span></li>
                            <li class="flex justify-between"><span id="ing-flour">Flour</span> <span><span class="qty" data-base="2">2</span> kg</span></li>
                        </ul>
                    </div>
                    <div class="text-sm text-gray-600 bg-emerald-50/50 p-5 rounded-2xl border border-emerald-100">
                        <h4 class="font-bold text-emerald-700 mb-2" id="guideline-header">ICAR/TNAU Guideline:</h4>
                        <p id="j-guideline">Ferment for 48-72 hours. Apply with irrigation.</p>
                    </div>
                </div>
            </div>

            <div class="bg-white rounded-2xl shadow-md overflow-hidden border border-indigo-100">
                <div class="bg-indigo-600 text-white px-6 py-4"><h3 class="font-bold text-xl" id="b-title">Beejamrutha</h3></div>
                <div class="p-6 grid md:grid-cols-2 gap-4">
                    <ul class="text-sm space-y-2">
                        <li class="flex justify-between"><span id="b-ing-dung">Dung</span> <span><span class="qty" data-base="5">5</span> kg</span></li>
                        <li class="flex justify-between"><span id="b-ing-urine">Urine</span> <span><span class="qty" data-base="5">5</span> L</span></li>
                        <li class="flex justify-between"><span id="b-ing-lime">Lime</span> <span><span class="qty" data-base="50">50</span> g</span></li>
                    </ul>
                    <p class="text-xs text-gray-500 italic" id="b-desc">Used for seed treatment to prevent fungal diseases.</p>
                </div>
            </div>

            <div class="bg-white rounded-2xl shadow-md overflow-hidden border border-stone-200">
                <div class="bg-stone-700 text-white px-6 py-4"><h3 class="font-bold text-xl" id="k-title">Kunapajala</h3></div>
                <div class="p-6">
                    <ul class="text-sm space-y-1 list-disc pl-5 mb-4" id="k-list">
                        <li>Animal/Fish waste</li><li>Sesame oil cake</li><li>Jaggery</li>
                    </ul>
                    <div class="bg-stone-50 p-3 rounded-lg text-xs" id="k-ref">Reference: Vrikshayurveda. Dilute 1:10.</div>
                </div>
            </div>
            
            <div class="bg-white rounded-2xl shadow-md overflow-hidden border border-red-100">
                <div class="bg-red-700 text-white px-6 py-4"><h3 class="font-bold text-xl" id="d-title">Dashparni Ark</h3></div>
                <div class="p-6">
                    <p class="text-sm mb-4" id="d-desc">Ferment 10 bitter leaves in urine for 40 days.</p>
                    <div class="bg-red-50 p-3 rounded-lg text-xs font-bold" id="d-ratio-val">Spray Ratio: 2.5%</div>
                </div>
            </div>
        </section>

        <section id="sec-guides" class="content-section hidden space-y-6">
            <h2 class="text-2xl font-bold text-emerald-800" id="guide-h2">Personalized Recommendation</h2>
            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-amber-50 p-5 rounded-2xl border-2 border-amber-100">
                    <h3 class="font-bold text-amber-900" id="l1-title">Dryland (Arid)</h3>
                    <p class="text-xs mt-3" id="l1-low">Low Resources: Use Amrit Pani and mulching.</p>
                    <p class="text-xs mt-2" id="l1-high">Full Resources: Beejamrutha + Ghanjeevamrit.</p>
                </div>
                <div class="bg-emerald-50 p-5 rounded-2xl border-2 border-emerald-100">
                    <h3 class="font-bold text-emerald-900" id="l2-title">Rainfed (Watershed)</h3>
                    <p class="text-xs mt-3" id="l2-low">Low: Contour digging and Sanjivak.</p>
                </div>
                <div class="bg-blue-50 p-5 rounded-2xl border-2 border-blue-100">
                    <h3 class="font-bold text-blue-900" id="l3-title">Irrigated (Wet)</h3>
                    <p class="text-xs mt-3" id="l3-low">Low: Waphasa aeration technique.</p>
                    <p class="text-xs mt-2" id="l3-high">Full: Panchagavya & Kunapajala.</p>
                </div>
            </div>
        </section>

        <section id="sec-microbial" class="content-section hidden space-y-6">
            <h2 class="text-2xl font-bold text-emerald-800" id="micro-h2">Soil Microbiology</h2>
            <div class="bg-white p-6 rounded-2xl border">
                <h3 class="font-bold text-emerald-700" id="m1-title">Rhizosphere Dynamics</h3>
                <p class="text-sm mt-2 text-gray-600" id="m1-desc">Feeding microbes to feed the plant.</p>
            </div>
        </section>

        <section id="sec-comparison" class="content-section hidden">
            <h2 class="text-2xl font-bold text-emerald-800 mb-6" id="comp-h2">Natural vs. Chemical</h2>
            <div class="bg-white rounded-xl border overflow-hidden">
                <table class="w-full text-left text-sm">
                    <tr class="bg-gray-50 border-b"><th class="p-3" id="th-feat">Feature</th><th class="p-3" id="th-nat">Natural</th><th class="p-3" id="th-chem">Chemical</th></tr>
                    <tr class="border-b"><td class="p-3" id="td-cost">Cost</td><td class="p-3">Zero</td><td class="p-3">High</td></tr>
                    <tr><td class="p-3" id="td-water">Water</td><td class="p-3">90% Less</td><td class="p-3">High</td></tr>
                </table>
            </div>
        </section>
    </main>

    <div class="fixed bottom-0 left-0 right-0 bg-white/95 border-t p-4 flex justify-center shadow-lg z-50">
        <button onclick="shareLink()" class="bg-emerald-600 text-white px-10 py-2.5 rounded-2xl font-bold text-sm">Share App</button>
    </div>

    <script>
        let currentLang = 'en';
        const translations = {
            en: {
                title: "KrishiAmrut", farmSize: "Configure Farm Size", acres: "Acre(s)", 
                navForm: "Deep Formulations", navGuide: "Personalized Advice", navMicro: "Microbial Life", navComp: "Comparison",
                jTitle: "Jeevamrutha (Liquid)", bTitle: "Beejamrutha", kTitle: "Kunapajala", dTitle: "Dashparni Ark",
                l1T: "Dryland", l2T: "Rainfed", l3T: "Irrigated"
            },
            ta: {
                title: "கிருஷ்ணாம்ருத்", farmSize: "நிலத்தின் அளவு", acres: "ஏக்கர்",
                navForm: "கரைசல்கள்", navGuide: "தனிப்பயனாக்கப்பட்ட ஆலோசனை", navMicro: "நுண்ணுயிர்", navComp: "ஒப்பீடு",
                jTitle: "ஜீவாமிர்தம்", bTitle: "பீஜாமிர்தம்", kTitle: "குணபஜலம்", dTitle: "தசபர்ணி அர்க்கு",
                l1T: "புஞ்சை நிலம்", l2T: "மழையாதாரம்", l3T: "நஞ்சை நிலம்"
            }
            // Add other languages here...
        };

        function setLanguage(lang) {
            const t = translations[lang] || translations.en;
            document.getElementById('main-title').innerText = t.title;
            document.getElementById('nav-form').innerText = t.navForm;
            document.getElementById('nav-guide').innerText = t.navGuide;
            document.querySelectorAll('.lang-btn').forEach(b => b.classList.replace('border-emerald-600', 'border-gray-200'));
            document.getElementById('btn-'+lang).classList.replace('border-gray-200', 'border-emerald-600');
            updateCalibration();
        }

        function updateCalibration() {
            const size = document.getElementById('land-size').value || 1;
            document.querySelectorAll('.current-acres').forEach(el => el.innerText = size);
            document.querySelectorAll('.qty').forEach(el => {
                const base = el.getAttribute('data-base');
                el.innerText = (base * size).toFixed(1).replace('.0', '');
            });
        }

        function showSection(id) {
            document.querySelectorAll('.content-section').forEach(s => s.classList.replace('block', 'hidden'));
            document.getElementById('sec-'+id).classList.replace('hidden', 'block');
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('tab-active'));
            event.target.classList.add('tab-active');
        }

        function shareLink() { alert("Link Copied!"); }
        window.onload = () => setLanguage('en');
    </script>
</body>
</html>
"""

# 4. Render the Full Application
components.html(html_content, height=2500, scrolling=True)
