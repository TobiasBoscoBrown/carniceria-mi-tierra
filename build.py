# -*- coding: utf-8 -*-
import os, json
OUT="/tmp/mitierra/site"
PHONE_DISP="(208) 453-2046"; PHONE_TEL="+12084532046"
ADDR="517 Main St, Caldwell, ID 83605"
ADDR_DIR="517+Main+St+Caldwell+ID+83605"
NAME="Carnicería Mi Tierra"
RATING="4.2"; RCOUNT="225"
DOMAIN="https://carniceria-mi-tierra.vercel.app"

# ---------- REVIEWS (real, verbatim, attributed; positives only) ----------
REVIEWS=[
 ("Shelby L.","Boise, ID · Yelp","The BEST, authentic Mexican food we've found in Idaho! So fresh, hot and delicious! The chicharron and lengua tacos are the best I've ever had, so tender and flavorful. Their rice and beans are by far the tastiest that I've ever had, and I'm not a huge fan of beans. We've come several times in the last month alone. Customer service is great, kind, smiling and friendly."),
 ("Scott E.","Boise, ID · Yelp","Their seasoned (preparada) carne asada is incredible! I've bought it more than 10 times and have never been disappointed."),
 ("Traeger W.","Meridian, ID · Yelp","Love this place, authentic Mexico fare in every way! Worth the drive from Boise if you want homemade traditional dishes like a Mexican grandma would cook!"),
 ("Cheryl F.","Caldwell, ID · Yelp","The food is excellent! Wow this is definitely a hidden gem! The service was good and they were very accommodating. More like you are family. If you wanted a beer, you just go over to the refrigerator and get one. This is also a little grocery store!"),
 ("Tico F.","Caldwell, ID · Yelp","Very good tacos, quesadillas, and soups. The carnitas are my favorite, and the tacos are huge. Tacos are served with a grilled jalapeño if you'd like. Highly recommended."),
 ("RalphCristina G.","Caldwell, ID · Yelp","Best place to buy grilling meat. Seasoned to perfection, my go to place for carne."),
 ("Carrie Cnossen","Local Guide · Google","I have been eating here for about three years, this place never disappoints me! Friendly and helpful staff, the food is always fresh. Taco shells are homemade! The lengua is amazing here! Today I bought a few things in the market and everyone was just so kind. Loyal customer, to support our local business!"),
 ("Miguel R","Local Guide · Google","THIS is the local butcher shop you were looking for. It's not just a meat market like almost all of the rest. This is the real deal. You want a whole pig? A special cut?"),
 ("Cristina M.","Yelp","Loved that they have everything you need for a great family bbq and even a party! We will definitely be back to buy more products from the carnicería. The workers were very helpful and courteous!"),
 ("Curtis Quagmyre","Local Guide · Google","We found this spot via Facebook when someone asked who has the best tamales. I went Thursday and bought a dozen uncooked frozen to bring home for Christmas day."),
 ("Maria B.","Yelp","We love coming to Mi Tierra for the food, and the service is quite good. The staff are very quick and nice when serving your dishes. The carnicería is pretty great and fresh."),
 ("Glenda L.","Yelp","Not too many people know about this place in the back of the market, but their food is so good."),
 ("Zachary Hamilton","Local Guide · Google","Fantastic food a great people!"),
]

# ---------- SERVICES ----------
SERVICES=[
 dict(slug="carniceria", icon="cleaver", name="La Carnicería",
   tag="Fresh & marinated meats",
   blurb="Custom cuts and our famous carne asada preparada, marinated and ready for the grill.",
   img="meat-counter",
   what="A real, full service Mexican meat counter, not just a case of pre-wrapped trays. Pick your cut and the carniceros will trim it the way you want it, fresh that day.",
   goodfor="Carne asada for a backyard grill, a whole pig for a pachanga, or a hard to find cut you cannot get at the grocery store.",
   detail=[("What you will find","Carne asada preparada (marinated), al pastor and adobada, chicharrón, costilla, fajita beef, chicken, and pork with the skin on."),
           ("Sold how you want it","By the pound, custom cut, or set up for a party. Tell them how many you are feeding and they will help."),
           ("Why folks come back","Reviewers buy the preparada asada ten, twenty times and say it never disappoints.")]),
 dict(slug="taqueria", icon="taco", name="La Taquería",
   tag="Tacos, tortas & quesadillas",
   blurb="Huge tacos with a grilled jalapeño, tortas, and quesadillas, cooked to order in the back.",
   img="tacos",
   what="The cocina in the back of the market turns the same fresh meat from the carnicería into tacos, tortas, and quesadillas, made to order.",
   goodfor="A real Mexican lunch on Main Street, a quick taco run, or feeding the whole crew without a sit down restaurant price.",
   detail=[("On the plate","Tacos de asada, lengua, chicharrón, and carnitas, served with a grilled jalapeño if you want one. Tortas, quesadillas, and burritos too."),
           ("Made to order","Corn tortillas are pressed fresh for your order, not pulled from a bag."),
           ("The vibe","Order at the counter, grab a table, and a cerveza from the fridge. It feels a little like Tijuana, in the best way.")]),
 dict(slug="caldos-platillos", icon="bowl", name="Caldos y Platillos",
   tag="Soups & Mexican plates",
   blurb="Hearty caldos and full Mexican plates with rice and beans, like a grandma would make.",
   img="enchiladas",
   what="Homestyle Mexican plates and soups, the kind of food reviewers say tastes like a Mexican grandmother cooked it.",
   goodfor="A warm, filling sit down meal, a cold day caldo, or a hungry appetite that wants rice, beans, and the works.",
   detail=[("Plates","Chile relleno, enchiladas, and platillos served with rice and beans that regulars call the tastiest around."),
           ("Soups","Rotating caldos and soups made in house."),
           ("Comes with","Fresh tortillas and salsa from the counter.")]),
 dict(slug="tamales-tortillas", icon="corn", name="Tamales y Tortillas",
   tag="Handmade, every day",
   blurb="Corn tortillas pressed for every order and tamales by the dozen, cooked or frozen to go.",
   img="market-shelves",
   what="Two things this place is loved for: tortillas made fresh for each order, and tamales people drive across the valley for.",
   goodfor="Holiday tamales by the dozen, a tortilla run for dinner, or stocking the freezer for later.",
   detail=[("Tortillas","Fresh corn tortillas pressed for your order, every time."),
           ("Tamales","Sold by the dozen, hot and ready or frozen to steam at home. One reviewer calls them the best they have ever had."),
           ("Tip","Holidays go fast, so call ahead for a big tamal order.")]),
 dict(slug="mercado", icon="basket", name="El Mercado",
   tag="Mexican grocery & cantina",
   blurb="A full Mexican market: salsas, dulces, jarritos, party goods, and a self-serve beer fridge.",
   img="market-interior",
   what="A whole Mexican grocery store wrapped around the meat counter and kitchen. Shop while your food cooks.",
   goodfor="Stocking up on Mexican pantry staples, grabbing a cold drink, or one stop shopping for a family BBQ.",
   detail=[("On the shelves","Salsas, spices, dulces, jarritos and Mexican sodas, plus everyday staples and party goods."),
           ("Self-serve cerveza","Grab a beer from the fridge and they tab it to your table, just look for the open cooler."),
           ("One stop","Meat, hot food, tortillas, and groceries under one roof.")]),
 dict(slug="catering-party", icon="party", name="Para tu Fiesta",
   tag="BBQ & party trays",
   blurb="Everything for a backyard BBQ or party: marinated meat by the pound and party-sized orders.",
   img="taqueria-tray",
   what="Set up your next carne asada or party in one stop, with marinated meat, sides, tortillas, and drinks.",
   goodfor="Backyard BBQs, quinceañeras, birthdays, and any pachanga that needs a lot of good food.",
   detail=[("Carne for the grill","Marinated carne asada and other meats by the pound, ready to throw on."),
           ("Round it out","Tortillas, salsas, sides, dulces, and drinks from the market."),
           ("Plan ahead","Tell them your headcount and date and they will help you order the right amount.")]),
]

GALLERY=["carne-asada","tacos","interior-dining","meat-counter","market-shelves","enchiladas",
 "taqueria-tray","tacos-egg","nachos","coctel","drinks","building-exterior","market-interior",
 "loaded-plate","quesadilla","torta","plato-caldo","storefront-entrance"]

# ---------- ICONS (inline svg, currentColor) ----------
def icon(n,cls="w-6 h-6"):
  P={
  "cleaver":'<path d="M3 3h10l5 5v3H8L3 6V3z"/><path d="M8 11v10"/><path d="M6 21h4"/>',
  "taco":'<path d="M2 18a10 10 0 0 1 20 0z"/><path d="M2 18h20"/><path d="M8 14c1-1 3-1 4 0M13 13c1-1 2-1 3 0"/>',
  "bowl":'<path d="M3 11h18a9 9 0 0 1-18 0z"/><path d="M12 3c-2 1-2 3 0 4M16 4c-1 .5-1 2 0 3"/>',
  "corn":'<path d="M12 3c4 2 4 9 0 18C8 12 8 5 12 3z"/><path d="M12 6l-2 2M12 10l-2 2M12 14l-2 2M12 8l2 2M12 12l2 2"/>',
  "basket":'<path d="M5 9h14l-1.5 10.5a2 2 0 0 1-2 1.5H8.5a2 2 0 0 1-2-1.5L5 9z"/><path d="M9 9l1.5-5M15 9l-1.5-5"/>',
  "party":'<path d="M3 21l6-14 9 9-14 6z"/><path d="M9 7l1-3M14 6l2-2M18 10l3-1"/>',
  "star":'<path d="M12 2l2.9 6.2 6.6.9-4.8 4.7 1.2 6.7L12 17.8 5.9 20.5 7 13.8 2.2 9.1l6.6-.9L12 2z"/>',
  "phone":'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7l.6 3a2 2 0 0 1-.6 1.9L7.8 9.8a16 16 0 0 0 6 6l1.2-1.3a2 2 0 0 1 1.9-.6l3 .6a2 2 0 0 1 1.7 2z"/>',
  "pin":'<path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
  "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  "check":'<path d="M20 6L9 17l-5-5"/>',
  "fire":'<path d="M12 2s5 4 5 9a5 5 0 0 1-10 0c0-2 1-3 1-3 0 2 2 2 2 0 0-3 2-6 2-6z"/>',
  "hand":'<path d="M7 11V6a2 2 0 0 1 4 0v5M11 11V4a2 2 0 0 1 4 0v7M15 11V6a2 2 0 0 1 4 0v8a6 6 0 0 1-6 6h-2a6 6 0 0 1-5-3l-2.5-4a2 2 0 0 1 3.3-2.2L7 13"/>',
  "arrow":'<path d="M5 12h14M13 6l6 6-6 6"/>',
  "menu":'<path d="M3 6h18M3 12h18M3 18h18"/>',
  "x":'<path d="M6 6l12 12M18 6L6 18"/>',
  }
  return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[n]}</svg>'

def fstar(cls="w-4 h-4"):
  return f'<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l2.9 6.2 6.6.9-4.8 4.7 1.2 6.7L12 17.8 5.9 20.5 7 13.8 2.2 9.1l6.6-.9L12 2z"/></svg>' 
print("part1 loaded")

NAV=[("Carnicería","/services.html"),("Taquería","/taqueria.html"),("Gallery","/index.html#gallery"),
     ("Reviews","/index.html#reviews"),("About","/index.html#about"),("Blog","/blog.html")]

def head(title, desc, jsonld, og="img/carne-asada.jpg"):
  ld="\n".join(f'<script type="application/ld+json">{json.dumps(b)}</script>' for b in jsonld)
  return f'''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#C0272D">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:type" content="business.business"><meta property="og:image" content="{og}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config={{theme:{{extend:{{
 colors:{{ink:'#241B16',cream:'#FBF6EC',card:'#FFFFFF',chili:'#C0272D',chilid:'#9E1F24',adobe:'#BE5A38',verde:'#2F7D4F',gold:'#E2A32B',line:'#ECE0CD',muted:'#7C6F63'}},
 fontFamily:{{display:['"Alfa Slab One"','serif'],sans:['Inter','ui-sans-serif','sans-serif']}},
 keyframes:{{marquee:{{'0%':{{transform:'translateX(0)'}},'100%':{{transform:'translateX(-50%)'}}}},
   scrollx:{{'0%':{{transform:'translateX(0)'}},'100%':{{transform:'translateX(-50%)'}}}}}},
 animation:{{marquee:'marquee 28s linear infinite',scrollx:'scrollx 45s linear infinite'}}
}}}}}}
</script>
<style>
 html{{scroll-behavior:smooth}} html,body{{overflow-x:hidden;max-width:100%}} body{{font-family:Inter,sans-serif}}
 .font-display{{font-family:'Alfa Slab One',serif}}
 .pausehover:hover{{animation-play-state:paused}}
 .hero-grad{{background:linear-gradient(180deg,rgba(20,14,11,.05),rgba(20,14,11,.55) 60%,rgba(20,14,11,.85))}}
 .edge{{-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}}
</style>
{ld}
</head><body class="bg-cream text-ink antialiased">
'''

def header():
  links="".join(f'<a href="{h}" class="hover:text-chili transition-colors">{t}</a>' for t,h in NAV)
  mlinks="".join(f'<a href="{h}" class="block py-2.5 text-lg font-semibold border-b border-line/70" onclick="closeMenu()">{t}</a>' for t,h in NAV)
  return f'''
<div class="bg-ink text-cream text-[12.5px]">
 <div class="max-w-6xl mx-auto px-4 py-1.5 flex flex-wrap items-center justify-center gap-x-4 gap-y-0.5 text-center">
  <span class="inline-flex items-center gap-1.5">{fstar('w-3.5 h-3.5 text-gold')}<b class="font-semibold">{RATING}</b> from {RCOUNT} Google reviews</span>
  <span class="opacity-40">|</span>
  <span class="inline-flex items-center gap-1.5">{icon('clock','w-3.5 h-3.5 text-gold')}Open daily, 8:00 AM to 8:00 PM</span>
  <span class="opacity-40">|</span>
  <span class="inline-flex items-center gap-1.5">{icon('pin','w-3.5 h-3.5 text-gold')}517 Main St, Caldwell</span>
 </div>
</div>
<header class="sticky top-0 z-40 bg-cream/95 backdrop-blur border-b border-line">
 <div class="max-w-6xl mx-auto px-4 h-[68px] flex items-center justify-between gap-4">
  <a href="/index.html" class="flex items-center gap-2.5 shrink-0">
   <span class="grid place-items-center w-10 h-10 rounded-xl bg-chili text-cream shadow-sm">{icon('cleaver','w-5 h-5')}</span>
   <span class="leading-none">
    <span class="block font-display text-[19px] text-ink tracking-tight">Mi Tierra</span>
    <span class="block text-[10.5px] font-semibold uppercase tracking-[.18em] text-adobe">Carnicería · Caldwell</span>
   </span>
  </a>
  <nav class="hidden lg:flex items-center gap-7 text-[15px] font-semibold text-ink/85">{links}</nav>
  <div class="flex items-center gap-2">
   <button onclick="toggleLang()" id="langBtn" class="inline-flex items-center gap-1.5 border border-line rounded-xl px-3 py-2.5 text-sm font-semibold text-ink hover:border-ink transition-colors" aria-label="Cambiar idioma / Switch language"><svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.6 3 2.6 15 0 18M12 3c-2.6 3-2.6 15 0 18"/></svg><span id="langLabel">ES</span></button>
   <a href="tel:{PHONE_TEL}" class="hidden sm:inline-flex items-center gap-2 bg-chili hover:bg-chilid text-cream font-semibold text-sm px-4 py-2.5 rounded-xl transition-colors">{icon('phone','w-4 h-4')}<span class="hidden md:inline">{PHONE_DISP}</span><span class="md:hidden">Call</span></a>
   <button onclick="openMenu()" class="lg:hidden grid place-items-center w-11 h-11 rounded-xl border border-line text-ink" aria-label="Open menu">{icon('menu','w-6 h-6')}</button>
  </div>
 </div>
</header>
<div id="mobileMenu" style="display:none" class="fixed inset-0 z-50 lg:hidden">
 <div class="absolute inset-0 bg-ink/50" onclick="closeMenu()"></div>
 <div class="absolute right-0 top-0 h-full w-[82%] max-w-xs bg-cream shadow-2xl p-5 overflow-y-auto">
  <div class="flex items-center justify-between mb-4">
   <span class="font-display text-lg">Mi Tierra</span>
   <button onclick="closeMenu()" class="grid place-items-center w-10 h-10 rounded-lg border border-line" aria-label="Close menu">{icon('x','w-5 h-5')}</button>
  </div>
  {mlinks}
  <button onclick="toggleLang()" class="mt-4 w-full inline-flex items-center justify-center gap-2 border border-line rounded-xl px-4 py-3 font-semibold"><svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.6 3 2.6 15 0 18M12 3c-2.6 3-2.6 15 0 18"/></svg><span id="langLabelM">Español</span></button>
  <a href="tel:{PHONE_TEL}" class="mt-3 flex items-center justify-center gap-2 bg-chili text-cream font-semibold px-4 py-3 rounded-xl">{icon('phone','w-4 h-4')}{PHONE_DISP}</a>
 </div>
</div>
'''

def footer():
  ql="".join(f'<li><a href="{h}" class="hover:text-cream transition-colors">{t}</a></li>' for t,h in NAV)
  sl="".join(f'<li><a href="/{s["slug"]}.html" class="hover:text-cream transition-colors">{s["name"]}</a></li>' for s in SERVICES)
  return f'''
<footer class="bg-ink text-cream/75">
 <div class="max-w-6xl mx-auto px-4 py-14 grid gap-10 md:grid-cols-4">
  <div class="md:col-span-1">
   <div class="flex items-center gap-2.5 mb-3">
    <span class="grid place-items-center w-10 h-10 rounded-xl bg-chili text-cream">{icon('cleaver','w-5 h-5')}</span>
    <span class="font-display text-cream text-lg">Mi Tierra</span>
   </div>
   <p class="text-sm leading-relaxed">A family run Mexican carnicería, taquería, and market on Main Street in downtown Caldwell. The real deal.</p>
   <p class="mt-3 inline-flex items-center gap-1.5 text-sm">{fstar('w-4 h-4 text-gold')}<b class="text-cream">{RATING}</b> · {RCOUNT} Google reviews</p>
  </div>
  <div>
   <h3 class="text-cream font-bold text-sm uppercase tracking-wider mb-3">Visit</h3>
   <ul class="space-y-2 text-sm">
    <li><a href="https://www.google.com/maps/dir/?api=1&destination={ADDR_DIR}" class="hover:text-cream inline-flex items-start gap-2">{icon('pin','w-4 h-4 mt-0.5 shrink-0 text-gold')}<span>517 Main St<br>Caldwell, ID 83605</span></a></li>
    <li><a href="tel:{PHONE_TEL}" class="hover:text-cream inline-flex items-center gap-2">{icon('phone','w-4 h-4 text-gold')}{PHONE_DISP}</a></li>
   </ul>
  </div>
  <div>
   <h3 class="text-cream font-bold text-sm uppercase tracking-wider mb-3">Hours</h3>
   <ul class="space-y-1.5 text-sm">
    <li class="flex justify-between gap-4"><span>Mon to Sat</span><span class="text-cream">8:00 AM to 8:00 PM</span></li>
    <li class="flex justify-between gap-4"><span>Sunday</span><span class="text-cream">8:00 AM to 7:00 PM</span></li>
   </ul>
   <h3 class="text-cream font-bold text-sm uppercase tracking-wider mt-5 mb-2">What we do</h3>
   <ul class="space-y-1.5 text-sm columns-1">{sl}</ul>
  </div>
  <div>
   <h3 class="text-cream font-bold text-sm uppercase tracking-wider mb-3">Explore</h3>
   <ul class="space-y-2 text-sm">{ql}</ul>
  </div>
 </div>
 <div class="border-t border-white/10">
  <div class="max-w-6xl mx-auto px-4 py-5 text-xs text-cream/55 flex flex-col sm:flex-row gap-2 justify-between">
   <span>© 2026 Carnicería Mi Tierra. All rights reserved.</span>
   <span>517 Main St, Caldwell, ID 83605 · {PHONE_DISP}</span>
  </div>
 </div>
</footer>
<script>
function openMenu(){{document.getElementById('mobileMenu').style.display='block';document.body.style.overflow='hidden';}}
function closeMenu(){{document.getElementById('mobileMenu').style.display='none';document.body.style.overflow='';}}
(function(){{var t=document.getElementById('rv');if(!t)return;t.innerHTML+=t.innerHTML;}})();
</script>
''' + I18N_SCRIPT + '''
</body></html>'''
print("part2 loaded")

def stars(cls="w-4 h-4"):
  return '<div class="flex text-gold">'+("".join(fstar(cls) for _ in range(5)))+'</div>'

def rcard(r, w="w-[330px]"):
  name,meta,txt=r
  initial=name[0]
  return f'''<figure class="{w} shrink-0 bg-card border border-line rounded-2xl p-5 flex flex-col shadow-sm">
   <div class="flex items-center gap-3 mb-3">
    <span class="grid place-items-center w-10 h-10 rounded-full bg-adobe/15 text-adobe font-bold">{initial}</span>
    <div><div class="font-bold text-sm leading-tight">{name}</div><div class="text-xs text-muted">{meta}</div></div>
   </div>
   {stars()}
   <blockquote class="mt-2.5 text-[14px] leading-relaxed text-ink/80">{txt}</blockquote>
  </figure>'''

def chip(t):
  return f'<span class="inline-flex items-center gap-1.5 bg-card/90 backdrop-blur border border-line rounded-full px-3 py-1.5 text-[13px] font-semibold">{t}</span>'

def index_body():
  # marquee
  spec=["Carne Asada Preparada","Al Pastor","Chicharrón","Lengua","Carnitas","Tacos","Tortas","Quesadillas","Tamales","Caldos","Tortillas Hechas a Mano","Coctel de Camarón","Salsas","Jarritos","Cerveza Fría"]
  mq="".join(f'<span class="inline-flex items-center gap-3 px-6"><span class="w-1.5 h-1.5 rounded-full bg-chili"></span><span class="font-display text-lg text-ink/85">{s}</span></span>' for s in spec)
  # services
  scards=""
  for s in SERVICES:
    scards+=f'''<a href="/{s['slug']}.html" class="group bg-card border border-line rounded-2xl overflow-hidden flex flex-col h-full hover:shadow-xl hover:-translate-y-0.5 transition-all">
      <div class="relative h-44 overflow-hidden"><img src="img/{s['img']}.jpg" alt="{s['name']} at Carnicería Mi Tierra in Caldwell" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy">
       <span class="absolute top-3 left-3 grid place-items-center w-10 h-10 rounded-xl bg-chili text-cream shadow">{icon(s['icon'],'w-5 h-5')}</span></div>
      <div class="p-5 flex flex-col flex-grow">
       <div class="text-[11px] font-bold uppercase tracking-wider text-adobe mb-1">{s['tag']}</div>
       <h3 class="font-display text-xl leading-tight mb-2">{s['name']}</h3>
       <p class="text-sm text-ink/70 leading-relaxed">{s['blurb']}</p>
       <span class="mt-auto pt-4 inline-flex items-center gap-1.5 text-chili font-semibold text-sm">See more {icon('arrow','w-4 h-4 group-hover:translate-x-1 transition-transform')}</span>
      </div></a>'''
  # promise bullets
  promise=[("hand","The real deal, not just a meat case","Custom cuts, marinated asada, even a whole pig. Reviewers call it the real local butcher shop they had been looking for."),
           ("fire","Cooked like a grandma would","Homemade corn tortillas with every order, huge tacos, and plates folks say taste like a Mexican grandmother made them."),
           ("basket","A whole market in one stop","Meat counter, hot food in the back, fresh tortillas, a full grocery, and a self-serve beer fridge, all under one roof.")]
  pcards="".join(f'''<div class="bg-card border border-line rounded-2xl p-6"><span class="grid place-items-center w-12 h-12 rounded-xl bg-verde/12 text-verde mb-4">{icon(i,'w-6 h-6')}</span><h3 class="font-bold text-lg mb-1.5">{t}</h3><p class="text-sm text-ink/70 leading-relaxed">{d}</p></div>''' for i,t,d in promise)
  # steps
  steps=[("Come in off Main Street","Find us at 517 Main St in downtown Caldwell, look for the red awning."),
         ("Order at the counter, or pick your cuts","Hot food and tacos are ordered in the back. Want to grill at home? The carniceros will cut and marinate your meat."),
         ("Grab a cerveza, eat in or take it home","Help yourself to a cold one from the fridge, they tab your table. Shop the market on your way out.")]
  stepc="".join(f'''<div class="relative pl-14"><span class="absolute left-0 top-0 grid place-items-center w-10 h-10 rounded-full bg-chili text-cream font-display text-lg">{n+1}</span><h3 class="font-bold text-lg mb-1">{t}</h3><p class="text-sm text-ink/70 leading-relaxed">{d}</p></div>''' for n,(t,d) in enumerate(steps))
  # gallery
  gal="".join(f'<div class="break-inside-avoid mb-3 overflow-hidden rounded-xl"><img src="img/{g}.jpg" alt="Carnicería Mi Tierra Caldwell, {g.replace("-"," ")}" class="w-full hover:scale-[1.03] transition-transform duration-500" loading="lazy"></div>' for g in GALLERY)
  # reviews
  feat="".join(rcard(r,"w-full") for r in REVIEWS[:6])
  carou="".join(rcard(r) for r in REVIEWS)
  # faq
  faqs=[("Do you have a taquería, or is it just a meat market?","Both. There is a full meat counter and a Mexican grocery up front, and a taquería kitchen in the back serving tacos, tortas, quesadillas, caldos, and plates."),
        ("Can I buy meat by the pound and get custom cuts?","Yes. The carnicería does custom cuts and our famous carne asada preparada, marinated and ready for the grill, sold by the pound. Ask for special cuts or a whole pig for a party."),
        ("Are the tortillas really made fresh?","Yes, corn tortillas are pressed fresh for your order, and reviewers keep coming back for them and for the tamales."),
        ("Can you set me up for a backyard BBQ or party?","Yes. Tell us your headcount and date and we will help you order marinated meat, tortillas, salsas, sides, and drinks for the whole fiesta."),
        ("Do you sell beer?","Yes, there is a self-serve beer fridge, just grab a cold one and we tab it to your table."),
        ("Where are you and what are your hours?","517 Main St in downtown Caldwell. Open Monday to Saturday 8:00 AM to 8:00 PM, and Sunday 8:00 AM to 7:00 PM.")]
  faqc="".join(f'''<details class="group bg-card border border-line rounded-xl px-5 py-1 open:shadow-sm"><summary class="flex items-center justify-between gap-4 cursor-pointer list-none py-4 font-semibold">{q}<span class="text-chili group-open:rotate-45 transition-transform text-xl leading-none">+</span></summary><p class="pb-4 -mt-1 text-sm text-ink/70 leading-relaxed">{a}</p></details>''' for q,a in faqs)

  return f'''
<main id="top">
<!-- HERO -->
<section class="relative">
 <div class="absolute inset-0"><img src="img/carne-asada.jpg" alt="Marinated carne asada plate at Carnicería Mi Tierra in Caldwell" class="w-full h-full object-cover"><div class="absolute inset-0 hero-grad"></div></div>
 <div class="relative max-w-6xl mx-auto px-4 pt-20 pb-24 md:pt-28 md:pb-32">
  <div class="max-w-2xl">
   <div class="flex flex-wrap gap-2 mb-5">{chip('Caldwell, Idaho')}{chip('Carnicería · Taquería · Mercado')}{chip('Family owned')}</div>
   <h1 class="font-display text-4xl md:text-6xl leading-[1.05] text-cream drop-shadow-sm">Caldwell's real Mexican carnicería and taquería.</h1>
   <p class="mt-5 text-lg text-cream/90 leading-relaxed max-w-xl">Marinated carne asada by the pound, huge tacos with a grilled jalapeño, handmade corn tortillas with every order, and a whole Mexican market in the back. Folks drive in from Boise and Meridian for it.</p>
   <div class="mt-7 flex flex-wrap gap-3">
    <a href="tel:{PHONE_TEL}" class="inline-flex items-center gap-2 bg-chili hover:bg-chilid text-cream font-semibold px-6 py-3.5 rounded-xl shadow-lg transition-colors">{icon('phone','w-5 h-5')}Call {PHONE_DISP}</a>
    <a href="https://www.google.com/maps/dir/?api=1&destination={ADDR_DIR}" class="inline-flex items-center gap-2 bg-cream/95 hover:bg-cream text-ink font-semibold px-6 py-3.5 rounded-xl transition-colors">{icon('pin','w-5 h-5')}Get directions</a>
   </div>
   <div class="mt-7 flex items-center gap-3 text-cream">{stars('w-5 h-5')}<span class="font-semibold">{RATING}</span><span class="text-cream/80 text-sm">from {RCOUNT} Google reviews</span></div>
  </div>
 </div>
 <div class="relative max-w-6xl mx-auto px-4 -mb-10 md:-mb-12">
  <div class="grid grid-cols-2 md:grid-cols-3 gap-3 md:gap-4">
   <div class="bg-card border border-line rounded-2xl p-4 shadow-lg"><div class="flex items-center gap-2 text-gold mb-1">{fstar('w-5 h-5')}<span class="font-display text-2xl text-ink">{RATING}</span></div><div class="text-xs text-muted font-semibold">{RCOUNT} Google reviews</div></div>
   <div class="bg-card border border-line rounded-2xl p-4 shadow-lg"><div class="font-display text-lg text-chili leading-tight">Carne Asada Preparada</div><div class="text-xs text-muted font-semibold mt-1">Marinated, by the pound</div></div>
   <div class="col-span-2 md:col-span-1 bg-card border border-line rounded-2xl p-4 shadow-lg"><div class="font-display text-lg text-verde leading-tight">Tortillas Hechas a Mano</div><div class="text-xs text-muted font-semibold mt-1">Pressed fresh, every order</div></div>
  </div>
 </div>
</section>

<!-- MARQUEE -->
<section class="pt-20 md:pt-24 pb-2 overflow-hidden border-b border-line">
 <div class="edge"><div class="flex w-max animate-marquee pausehover">{mq}{mq}</div></div>
</section>

<!-- PROMISE -->
<section class="max-w-6xl mx-auto px-4 py-16 md:py-20">
 <div class="max-w-2xl mb-10"><div class="text-xs font-bold uppercase tracking-[.2em] text-adobe mb-2">Why folks drive in</div>
  <h2 class="font-display text-3xl md:text-4xl leading-tight">A neighborhood carnicería that does it the real way.</h2></div>
 <div class="grid gap-4 md:grid-cols-3">{pcards}</div>
</section>

<!-- SERVICES -->
<section class="bg-ink/[.03] border-y border-line">
 <div class="max-w-6xl mx-auto px-4 py-16 md:py-20">
  <div class="flex flex-wrap items-end justify-between gap-4 mb-10">
   <div class="max-w-xl"><div class="text-xs font-bold uppercase tracking-[.2em] text-adobe mb-2">What we do</div>
    <h2 class="font-display text-3xl md:text-4xl leading-tight">From the meat counter to the table.</h2></div>
   <a href="/services.html" class="inline-flex items-center gap-1.5 text-chili font-semibold">All departments {icon('arrow','w-4 h-4')}</a>
  </div>
  <div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">{scards}</div>
 </div>
</section>

<!-- HOW -->
<section class="max-w-6xl mx-auto px-4 py-16 md:py-20">
 <div class="max-w-xl mb-10"><div class="text-xs font-bold uppercase tracking-[.2em] text-adobe mb-2">How it works</div>
  <h2 class="font-display text-3xl md:text-4xl leading-tight">Walk in hungry, leave with dinner and groceries.</h2></div>
 <div class="grid gap-8 md:grid-cols-3">{stepc}</div>
</section>

<!-- GALLERY -->
<section id="gallery" class="bg-ink/[.03] border-y border-line">
 <div class="max-w-6xl mx-auto px-4 py-16 md:py-20">
  <div class="max-w-xl mb-8"><div class="text-xs font-bold uppercase tracking-[.2em] text-adobe mb-2">The shop</div>
   <h2 class="font-display text-3xl md:text-4xl leading-tight">Real food, real market, on Main Street.</h2></div>
  <div class="columns-2 md:columns-3 lg:columns-4 gap-3">{gal}</div>
 </div>
</section>

<!-- REVIEWS -->
<section id="reviews" class="max-w-6xl mx-auto px-4 py-16 md:py-20">
 <div class="max-w-xl mb-3"><div class="text-xs font-bold uppercase tracking-[.2em] text-adobe mb-2">Straight from Google and Yelp</div>
  <h2 class="font-display text-3xl md:text-4xl leading-tight">Loved across the Treasure Valley.</h2></div>
 <div class="flex items-center gap-3 mb-8">{stars('w-5 h-5')}<span class="font-semibold">{RATING}</span><span class="text-muted text-sm">based on {RCOUNT} Google reviews</span></div>
 <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">{feat}</div>
</section>
<section class="pb-16 md:pb-20 overflow-hidden">
 <div class="edge"><div id="rv" class="flex gap-4 w-max animate-scrollx pausehover px-2">{carou}</div></div>
</section>

<!-- ABOUT -->
<section id="about" class="bg-ink text-cream">
 <div class="max-w-6xl mx-auto px-4 py-16 md:py-20 grid md:grid-cols-2 gap-10 items-center">
  <div>
   <div class="text-xs font-bold uppercase tracking-[.2em] text-gold mb-2">The family behind the counter</div>
   <h2 class="font-display text-3xl md:text-4xl leading-tight">A hidden gem in the back of the market.</h2>
   <p class="mt-5 text-cream/80 leading-relaxed">Carnicería Mi Tierra has been a Main Street fixture in downtown Caldwell, a family run shop where the meat case, the kitchen, and a full Mexican grocery all live under one roof. Regulars say it feels a little like Tijuana, in the best way, with staff who treat you like family.</p>
   <p class="mt-4 text-cream/80 leading-relaxed">The carniceros cut and marinate the asada by hand, the cocina presses tortillas fresh for every order, and the freezer is stocked with tamales people drive across the valley for. It is not just a meat market. It is the real deal.</p>
   <blockquote class="mt-5 border-l-2 border-gold pl-4 text-cream/90 italic">"Authentic Mexico fare in every way. Worth the drive from Boise if you want homemade traditional dishes like a Mexican grandma would cook."</blockquote>
   <a href="tel:{PHONE_TEL}" class="mt-7 inline-flex items-center gap-2 bg-chili hover:bg-chilid text-cream font-semibold px-6 py-3.5 rounded-xl transition-colors">{icon('phone','w-5 h-5')}Call {PHONE_DISP}</a>
  </div>
  <div class="grid grid-cols-2 gap-3">
   <img src="img/storefront-entrance.jpg" alt="Carnicería Mi Tierra storefront at 517 Main St, Caldwell" class="rounded-2xl w-full h-full object-cover col-span-1 row-span-2">
   <img src="img/meat-counter.jpg" alt="The meat counter at Carnicería Mi Tierra" class="rounded-2xl w-full h-40 object-cover">
   <img src="img/interior-dining.jpg" alt="Inside the taquería at Carnicería Mi Tierra" class="rounded-2xl w-full h-40 object-cover">
  </div>
 </div>
</section>

<!-- BLOG TEASER -->
<section class="max-w-6xl mx-auto px-4 py-16 md:py-20">
 <div class="grid md:grid-cols-2 gap-6 items-stretch">
  <a href="/blog.html" class="group bg-card border border-line rounded-2xl overflow-hidden flex flex-col sm:flex-row hover:shadow-xl transition-all">
   <img src="img/tacos.jpg" alt="How to order at a Mexican carnicería" class="w-full sm:w-48 h-48 sm:h-auto object-cover">
   <div class="p-6 flex flex-col">
    <div class="text-xs font-bold uppercase tracking-wider text-adobe mb-1">From the counter</div>
    <h3 class="font-display text-xl leading-tight mb-2">How to order at a Mexican carnicería (and what to ask for)</h3>
    <p class="text-sm text-ink/70 leading-relaxed">New to the carnicería? Here is exactly what to order, how to ask for your asada preparada, and how the taquería in the back works.</p>
    <span class="mt-auto pt-4 inline-flex items-center gap-1.5 text-chili font-semibold text-sm">Read the guide {icon('arrow','w-4 h-4 group-hover:translate-x-1 transition-transform')}</span>
   </div>
  </a>
  <div class="bg-chili text-cream rounded-2xl p-8 flex flex-col justify-center">
   <h3 class="font-display text-2xl leading-tight">Setting up a carne asada?</h3>
   <p class="mt-3 text-cream/90 leading-relaxed">Order marinated meat by the pound, fresh tortillas, salsas, and drinks for the whole fiesta in one stop.</p>
   <a href="/catering-party.html" class="mt-5 inline-flex items-center gap-2 bg-cream text-chili font-semibold px-5 py-3 rounded-xl w-max">{icon('party','w-5 h-5')}Plan your party</a>
  </div>
 </div>
</section>

<!-- FAQ -->
<section class="bg-ink/[.03] border-y border-line">
 <div class="max-w-3xl mx-auto px-4 py-16 md:py-20">
  <div class="text-center mb-10"><div class="text-xs font-bold uppercase tracking-[.2em] text-adobe mb-2">Good to know</div>
   <h2 class="font-display text-3xl md:text-4xl leading-tight">Questions, answered.</h2></div>
  <div class="space-y-3">{faqc}</div>
 </div>
</section>

<!-- CTA -->
<section class="relative">
 <img src="img/interior-dining.jpg" alt="Carnicería Mi Tierra taquería in Caldwell" class="absolute inset-0 w-full h-full object-cover">
 <div class="absolute inset-0 bg-ink/75"></div>
 <div class="relative max-w-3xl mx-auto px-4 py-20 text-center text-cream">
  <h2 class="font-display text-3xl md:text-5xl leading-tight">Come hungry. Leave with dinner, and groceries.</h2>
  <p class="mt-4 text-cream/85 text-lg">517 Main St, Caldwell. Open every day. Walk in, call ahead, or set up your next BBQ.</p>
  <div class="mt-7 flex flex-wrap gap-3 justify-center">
   <a href="tel:{PHONE_TEL}" class="inline-flex items-center gap-2 bg-chili hover:bg-chilid text-cream font-semibold px-6 py-3.5 rounded-xl transition-colors">{icon('phone','w-5 h-5')}Call {PHONE_DISP}</a>
   <a href="https://www.google.com/maps/dir/?api=1&destination={ADDR_DIR}" class="inline-flex items-center gap-2 bg-cream text-ink font-semibold px-6 py-3.5 rounded-xl">{icon('pin','w-5 h-5')}Get directions</a>
  </div>
 </div>
</section>
</main>
'''
print("part3 loaded")

GEO={"@type":"GeoCoordinates","latitude":43.6682928,"longitude":-116.6896475}
ADDRESS={"@type":"PostalAddress","streetAddress":"517 Main St","addressLocality":"Caldwell","addressRegion":"ID","postalCode":"83605","addressCountry":"US"}
HOURS=[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"20:00"},
       {"@type":"OpeningHoursSpecification","dayOfWeek":["Sunday"],"opens":"08:00","closes":"19:00"}]

def ld_business():
  return {"@context":"https://schema.org","@type":["Restaurant","GroceryStore"],"name":NAME,
   "image":DOMAIN+"/img/carne-asada.jpg","telephone":PHONE_DISP,"priceRange":"$$",
   "servesCuisine":["Mexican"],"address":ADDRESS,"geo":GEO,"url":DOMAIN+"/","openingHoursSpecification":HOURS,
   "aggregateRating":{"@type":"AggregateRating","ratingValue":RATING,"reviewCount":RCOUNT}}

def ld_faq(faqs):
  return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}

def ld_service(s):
  return {"@context":"https://schema.org","@type":"Service","name":s["name"],"serviceType":s["tag"],
   "description":s["blurb"],"provider":{"@type":"Restaurant","name":NAME,"address":ADDRESS,"telephone":PHONE_DISP},
   "areaServed":["Caldwell","Nampa","Boise","Meridian","Idaho"]}

def ld_blog():
  return {"@context":"https://schema.org","@type":"BlogPosting",
   "headline":"How to order at a Mexican carnicería (and what to ask for)",
   "image":DOMAIN+"/img/tacos.jpg","author":{"@type":"Organization","name":NAME},
   "publisher":{"@type":"Organization","name":NAME},"datePublished":"2026-06-22",
   "mainEntityOfPage":DOMAIN+"/blog.html"}

FAQS_INDEX=[("Do you have a taquería, or is it just a meat market?","Both. There is a full meat counter and a Mexican grocery up front, and a taquería kitchen in the back serving tacos, tortas, quesadillas, caldos, and plates."),
 ("Can I buy meat by the pound and get custom cuts?","Yes. The carnicería does custom cuts and carne asada preparada, marinated and ready for the grill, sold by the pound. Ask for special cuts or a whole pig for a party."),
 ("Are the tortillas really made fresh?","Yes, corn tortillas are pressed fresh for your order, and reviewers keep coming back for them and for the tamales."),
 ("Can you set me up for a backyard BBQ or party?","Yes. Tell us your headcount and date and we will help you order marinated meat, tortillas, salsas, sides, and drinks for the whole fiesta."),
 ("Do you sell beer?","Yes, there is a self-serve beer fridge, just grab a cold one and we tab it to your table."),
 ("Where are you and what are your hours?","517 Main St in downtown Caldwell. Open Monday to Saturday 8:00 AM to 8:00 PM, and Sunday 8:00 AM to 7:00 PM.")]

def service_page(s):
  others="".join(f'<a href="/{o["slug"]}.html" class="flex items-center gap-3 p-3 rounded-xl border border-line hover:border-chili hover:bg-chili/5 transition-colors"><span class="grid place-items-center w-9 h-9 rounded-lg bg-chili/10 text-chili shrink-0">{icon(o["icon"],"w-5 h-5")}</span><span class="text-sm font-semibold">{o["name"]}</span></a>' for o in SERVICES if o["slug"]!=s["slug"])
  det="".join(f'<div class="border-l-2 border-adobe/40 pl-4"><div class="font-bold text-sm uppercase tracking-wider text-adobe mb-1">{t}</div><p class="text-ink/80 leading-relaxed">{d}</p></div>' for t,d in s["detail"])
  rv=REVIEWS[ (SERVICES.index(s)*2) % len(REVIEWS) ], REVIEWS[(SERVICES.index(s)*2+1) % len(REVIEWS)]
  rcards="".join(rcard(r,"w-full") for r in rv)
  body=f'''
<main>
<section class="bg-ink text-cream">
 <div class="max-w-6xl mx-auto px-4 py-4 text-sm text-cream/60"><a href="/index.html" class="hover:text-cream">Home</a> <span class="opacity-50">/</span> <a href="/services.html" class="hover:text-cream">Departments</a> <span class="opacity-50">/</span> <span class="text-cream">{s['name']}</span></div>
 <div class="max-w-6xl mx-auto px-4 pb-14 grid md:grid-cols-2 gap-10 items-center">
  <div>
   <span class="grid place-items-center w-14 h-14 rounded-2xl bg-chili text-cream mb-4">{icon(s['icon'],'w-7 h-7')}</span>
   <div class="text-xs font-bold uppercase tracking-[.2em] text-gold mb-2">{s['tag']}</div>
   <h1 class="font-display text-4xl md:text-5xl leading-tight">{s['name']}</h1>
   <p class="mt-4 text-cream/85 text-lg leading-relaxed">{s['blurb']}</p>
   <div class="mt-6 flex flex-wrap gap-3">
    <a href="tel:{PHONE_TEL}" class="inline-flex items-center gap-2 bg-chili hover:bg-chilid text-cream font-semibold px-6 py-3.5 rounded-xl transition-colors">{icon('phone','w-5 h-5')}Call {PHONE_DISP}</a>
    <a href="https://www.google.com/maps/dir/?api=1&destination={ADDR_DIR}" class="inline-flex items-center gap-2 bg-cream/10 hover:bg-cream/20 text-cream font-semibold px-6 py-3.5 rounded-xl transition-colors">{icon('pin','w-5 h-5')}Get directions</a>
   </div>
  </div>
  <img src="img/{s['img']}.jpg" alt="{s['name']} at Carnicería Mi Tierra in Caldwell" class="rounded-2xl w-full h-72 md:h-80 object-cover shadow-xl">
 </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-14 grid lg:grid-cols-3 gap-10">
 <div class="lg:col-span-2 space-y-8">
  <div><h2 class="font-display text-2xl mb-2">What it is</h2><p class="text-ink/80 leading-relaxed">{s['what']}</p></div>
  <div><h2 class="font-display text-2xl mb-2">Good for</h2><p class="text-ink/80 leading-relaxed">{s['goodfor']}</p></div>
  <div class="grid sm:grid-cols-2 gap-5">{det}</div>
  <div class="bg-chili/5 border border-chili/20 rounded-2xl p-6 flex flex-wrap items-center justify-between gap-4">
   <div><div class="font-display text-xl text-ink">Ready when you are.</div><p class="text-sm text-ink/70">Call ahead or just walk in to 517 Main St.</p></div>
   <a href="tel:{PHONE_TEL}" class="inline-flex items-center gap-2 bg-chili hover:bg-chilid text-cream font-semibold px-5 py-3 rounded-xl transition-colors">{icon('phone','w-5 h-5')}{PHONE_DISP}</a>
  </div>
  <div><h2 class="font-display text-2xl mb-4">What people say</h2><div class="grid sm:grid-cols-2 gap-4">{rcards}</div></div>
 </div>
 <aside class="space-y-6">
  <div class="bg-card border border-line rounded-2xl p-5">
   <h3 class="font-bold mb-3 flex items-center gap-2">{icon('clock','w-5 h-5 text-chili')}Hours</h3>
   <ul class="text-sm space-y-1.5 text-ink/75"><li class="flex justify-between"><span>Mon to Sat</span><span class="font-semibold text-ink">8 AM to 8 PM</span></li><li class="flex justify-between"><span>Sunday</span><span class="font-semibold text-ink">8 AM to 7 PM</span></li></ul>
   <a href="https://www.google.com/maps/dir/?api=1&destination={ADDR_DIR}" class="mt-3 inline-flex items-center gap-1.5 text-chili font-semibold text-sm">{icon('pin','w-4 h-4')}517 Main St, Caldwell</a>
  </div>
  <div class="bg-card border border-line rounded-2xl p-5">
   <h3 class="font-bold mb-3">More departments</h3>
   <div class="space-y-2">{others}</div>
  </div>
 </aside>
</section>
</main>'''
  return head(f"{s['name']} | Carnicería Mi Tierra, Caldwell ID",f"{s['blurb']} Carnicería Mi Tierra, 517 Main St, Caldwell. Call {PHONE_DISP}.",[ld_service(s)],og=f"img/{s['img']}.jpg")+header()+body+footer()

def services_overview():
  cards=""
  for s in SERVICES:
    cards+=f'''<a href="/{s['slug']}.html" class="group bg-card border border-line rounded-2xl overflow-hidden flex flex-col h-full hover:shadow-xl hover:-translate-y-0.5 transition-all">
      <div class="relative h-48 overflow-hidden"><img src="img/{s['img']}.jpg" alt="{s['name']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy"><span class="absolute top-3 left-3 grid place-items-center w-10 h-10 rounded-xl bg-chili text-cream">{icon(s['icon'],'w-5 h-5')}</span></div>
      <div class="p-5 flex flex-col flex-grow"><div class="text-[11px] font-bold uppercase tracking-wider text-adobe mb-1">{s['tag']}</div><h3 class="font-display text-xl mb-2">{s['name']}</h3><p class="text-sm text-ink/70 leading-relaxed">{s['blurb']}</p><span class="mt-auto pt-4 inline-flex items-center gap-1.5 text-chili font-semibold text-sm">See more {icon('arrow','w-4 h-4 group-hover:translate-x-1 transition-transform')}</span></div></a>'''
  body=f'''
<main>
<section class="bg-ink text-cream">
 <div class="max-w-6xl mx-auto px-4 py-4 text-sm text-cream/60"><a href="/index.html" class="hover:text-cream">Home</a> <span class="opacity-50">/</span> <span class="text-cream">Departments</span></div>
 <div class="max-w-6xl mx-auto px-4 pb-14 pt-2">
  <div class="text-xs font-bold uppercase tracking-[.2em] text-gold mb-2">Everything under one roof</div>
  <h1 class="font-display text-4xl md:text-5xl leading-tight max-w-2xl">A carnicería, a taquería, and a Mexican market.</h1>
  <p class="mt-4 text-cream/85 text-lg max-w-2xl leading-relaxed">Pick your cuts, order hot food in the back, stock up on groceries, and set up your next party, all in one stop on Main Street.</p>
 </div>
</section>
<section class="max-w-6xl mx-auto px-4 py-14"><div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">{cards}</div></section>
<section class="bg-chili text-cream"><div class="max-w-3xl mx-auto px-4 py-16 text-center"><h2 class="font-display text-3xl md:text-4xl">Come see us at 517 Main St.</h2><p class="mt-3 text-cream/90">Open every day. Walk in or call ahead.</p><a href="tel:{PHONE_TEL}" class="mt-6 inline-flex items-center gap-2 bg-cream text-chili font-semibold px-6 py-3.5 rounded-xl">{icon('phone','w-5 h-5')}Call {PHONE_DISP}</a></div></section>
</main>'''
  return head("Departments | Carnicería Mi Tierra, Caldwell ID","Carnicería, taquería, caldos and plates, tamales and tortillas, a Mexican market, and party trays. Carnicería Mi Tierra, 517 Main St, Caldwell.",[ld_business()])+header()+body+footer()
print("part4 loaded")

def blog_page():
  body=f'''
<main>
<article>
<section class="bg-ink text-cream">
 <div class="max-w-3xl mx-auto px-4 py-4 text-sm text-cream/60"><a href="/index.html" class="hover:text-cream">Home</a> <span class="opacity-50">/</span> <a href="/blog.html" class="hover:text-cream">Blog</a> <span class="opacity-50">/</span> <span class="text-cream">Carnicería guide</span></div>
 <div class="max-w-3xl mx-auto px-4 pb-12 pt-2">
  <div class="text-xs font-bold uppercase tracking-[.2em] text-gold mb-3">From the counter · Caldwell, ID</div>
  <h1 class="font-display text-3xl md:text-5xl leading-[1.1]">How to order at a Mexican carnicería (and what to ask for)</h1>
  <p class="mt-4 text-cream/80 text-lg leading-relaxed">First time at a real carnicería? Here is how Mi Tierra works, what to order, and how to walk out with a trunk full of dinner.</p>
 </div>
</section>

<div class="max-w-3xl mx-auto px-4">
 <img src="img/meat-counter.jpg" alt="The meat counter at Carnicería Mi Tierra in Caldwell" class="rounded-2xl w-full h-72 object-cover -mt-8 shadow-xl relative">

 <div class="bg-card border border-line rounded-2xl p-5 mt-8 flex items-center gap-4">
  <span class="grid place-items-center w-12 h-12 rounded-xl bg-chili text-cream shrink-0">{icon('taco','w-6 h-6')}</span>
  <div class="flex-grow">
   <div class="font-bold text-sm">Listen instead: the Mi Tierra carnicería guide</div>
   <div class="text-xs text-muted mb-2">A quick two minute walk through with Ava and Marco</div>
   <audio controls preload="none" class="w-full"><source src="podcast.mp3" type="audio/mpeg">Your browser does not support audio.</audio>
  </div>
 </div>

 <div class="prose-custom mt-10 space-y-5 text-[17px] leading-relaxed text-ink/85">
  <p>If you have only ever bought meat off a foam tray at a big grocery store, your first trip to a Mexican carnicería can feel like a different world. There is a meat case as long as a car, a kitchen in the back filling the air with the smell of asada, shelves of salsas and dulces, and a cooler full of cold beer. At <strong>Carnicería Mi Tierra</strong> on Main Street in Caldwell, all of that lives under one roof. Here is how to order like a regular.</p>

  <h2 class="font-display text-2xl text-ink pt-2">First, know that it is three places in one</h2>
  <p>Mi Tierra is a <strong>carnicería</strong> (a butcher counter), a <strong>taquería</strong> (a hot food kitchen in the back), and a <strong>mercado</strong> (a Mexican grocery), all at once. That is why folks drive in from Boise, Nampa, and Meridian: you can grab lunch, pick up meat to grill tonight, and finish your grocery list in a single stop. Walk in, take a look around, and decide what you came for. Most people come for two or three of those things at once.</p>

  <h2 class="font-display text-2xl text-ink pt-2">At the meat counter: ask for it "preparada"</h2>
  <p>The thing regulars buy again and again is the <strong>carne asada preparada</strong>, which just means the beef is already marinated and seasoned, ready to throw straight on the grill. One Boise regular says he has bought it more than ten times and has never been disappointed. If you are feeding a crowd, tell the carnicero how many people and they will weigh out the right amount and cut it the way you want.</p>
  <p>Do not be shy about asking for the cuts you cannot find anywhere else. This is a real butcher shop, not just a case of pre-wrapped trays. Want a whole pig for a pachanga? Pork with the skin still on for chicharrón? A specific cut for birria or carnitas? Ask. Other things worth grabbing: <strong>al pastor</strong> or <strong>adobada</strong> (marinated pork), <strong>chicharrón</strong>, fajita beef, and chicken. Everything is sold by the pound.</p>

  <h2 class="font-display text-2xl text-ink pt-2">In the back: order tacos, tortas, and caldos</h2>
  <p>Head to the counter in the back for the taquería. The same fresh meat from the case becomes <strong>tacos</strong> (huge ones, served with a grilled jalapeño if you want), <strong>tortas</strong>, <strong>quesadillas</strong>, and <strong>burritos</strong>. The lengua and chicharrón tacos get singled out by reviewers as some of the best they have had, and the carnitas have their own fan club. If you want a full sit down meal, go for a <strong>plato</strong> with rice and beans, a <strong>chile relleno</strong>, enchiladas, or a hot <strong>caldo</strong>. People say it tastes like a Mexican grandmother cooked it, which is about the highest praise food like this can get.</p>
  <p>One detail that keeps people loyal: the <strong>corn tortillas are pressed fresh for your order</strong>, not pulled out of a bag. You can taste the difference.</p>

  <h2 class="font-display text-2xl text-ink pt-2">How the ordering and the beer fridge work</h2>
  <p>The flow is informal and that is part of the charm. You order your hot food at the counter in the back and pay up front. Seating is casual. And if you want a cold one, you just walk over to the <strong>refrigerator and grab a beer yourself</strong>, then they tab it to your table along with whatever else you ordered. As one reviewer put it, the whole place feels a little like being across the border, in the best possible way, with staff who treat you like family.</p>

  <h2 class="font-display text-2xl text-ink pt-2">Do not skip the tamales and the tortillas</h2>
  <p>Around the holidays, the <strong>tamales</strong> are the move. You can buy them hot and ready or by the dozen frozen, so you can steam them at home on Christmas morning. One reviewer found the spot through a Facebook thread about the best tamales in the valley, bought a dozen frozen, and called them the best they had ever had. They go fast in December, so call ahead for a big order.</p>

  <h2 class="font-display text-2xl text-ink pt-2">Setting up a carne asada or party</h2>
  <p>This is where the one stop shop really pays off. For a backyard BBQ, a birthday, or a quinceañera, you can knock out the whole list at Mi Tierra: <strong>marinated meat by the pound</strong>, fresh tortillas, salsas, sides, dulces for the kids, and drinks. Tell the team your headcount and your date and they will help you order the right amount so nobody leaves hungry.</p>

  <h2 class="font-display text-2xl text-ink pt-2">Quick first-timer cheat sheet</h2>
  <ul class="list-disc pl-6 space-y-1.5">
   <li>Hungry now? Order tacos de asada or carnitas in the back, with a grilled jalapeño.</li>
   <li>Grilling tonight? Ask for carne asada preparada by the pound at the counter.</li>
   <li>Want a cold beer? Grab it from the fridge yourself, they will tab your table.</li>
   <li>Holiday coming up? Call ahead for tamales by the dozen.</li>
   <li>Throwing a party? Give them your headcount and let them set you up.</li>
  </ul>

  <p class="pt-2">Come see for yourself. Carnicería Mi Tierra is at <strong>517 Main St in downtown Caldwell</strong>, open Monday to Saturday 8:00 AM to 8:00 PM and Sunday 8:00 AM to 7:00 PM. Walk in, call <a href="tel:{PHONE_TEL}" class="text-chili font-semibold">{PHONE_DISP}</a>, and order like you have been coming for years.</p>
 </div>

 <div class="my-12 bg-chili text-cream rounded-2xl p-8 text-center">
  <h2 class="font-display text-2xl md:text-3xl">Ready to order?</h2>
  <p class="mt-3 text-cream/90">Fresh meat, hot tacos, and a whole market on Main Street.</p>
  <div class="mt-5 flex flex-wrap gap-3 justify-center">
   <a href="tel:{PHONE_TEL}" class="inline-flex items-center gap-2 bg-cream text-chili font-semibold px-6 py-3.5 rounded-xl">{icon('phone','w-5 h-5')}Call {PHONE_DISP}</a>
   <a href="/services.html" class="inline-flex items-center gap-2 bg-chilid text-cream font-semibold px-6 py-3.5 rounded-xl">See the departments</a>
  </div>
 </div>
</div>
</article>
</main>'''
  return head("How to order at a Mexican carnicería | Carnicería Mi Tierra, Caldwell","A first-timer's guide to ordering at Carnicería Mi Tierra in Caldwell: carne asada preparada, tacos, tamales, the self-serve beer fridge, and setting up a party.",[ld_blog()],og="img/tacos.jpg")+header()+blog_page_audio_note()+footer() if False else head("How to order at a Mexican carnicería | Carnicería Mi Tierra, Caldwell","A first-timer's guide to ordering at Carnicería Mi Tierra in Caldwell: carne asada preparada, tacos, tamales, the self-serve beer fridge, and setting up a party.",[ld_blog()],og="img/tacos.jpg")+header()+body+footer()


# ---------- I18N (Mexican Spanish) ----------
ES_DICT={
 "from 225 Google reviews":"de 225 reseñas de Google",
 "Open daily, 8:00 AM to 8:00 PM":"Abierto a diario, 8:00 AM a 8:00 PM",
 "Gallery":"Galería","Reviews":"Reseñas","About":"Nosotros",
 "Call":"Llamar","Call (208) 453-2046":"Llámanos (208) 453-2046","Get directions":"Cómo llegar",
 "See more":"Ver más","All departments":"Todos los departamentos","More departments":"Más departamentos",
 "Family owned":"Negocio familiar",
 "Caldwell's real Mexican carnicería and taquería.":"La verdadera carnicería y taquería mexicana de Caldwell.",
 "Marinated carne asada by the pound, huge tacos with a grilled jalapeño, handmade corn tortillas with every order, and a whole Mexican market in the back. Folks drive in from Boise and Meridian for it.":"Carne asada preparada por libra, tacos enormes con jalapeño asado, tortillas de maíz hechas a mano con cada orden, y todo un mercado mexicano al fondo. La gente viene desde Boise y Meridian por ella.",
 "225 Google reviews":"225 reseñas de Google","Marinated, by the pound":"Preparada, por libra","Pressed fresh, every order":"Hechas al momento, cada orden",
 "Why folks drive in":"Por qué la gente maneja hasta acá",
 "A neighborhood carnicería that does it the real way.":"Una carnicería de barrio que lo hace como se debe.",
 "The real deal, not just a meat case":"De a de veras, no solo una vitrina de carne",
 "Custom cuts, marinated asada, even a whole pig. Reviewers call it the real local butcher shop they had been looking for.":"Cortes a tu gusto, asada preparada, hasta un cerdo entero. Los clientes la llaman la verdadera carnicería del barrio que andaban buscando.",
 "Cooked like a grandma would":"Cocinado como lo haría una abuela",
 "Homemade corn tortillas with every order, huge tacos, and plates folks say taste like a Mexican grandmother made them.":"Tortillas de maíz hechas en casa con cada orden, tacos enormes, y platillos que la gente dice saben a los de una abuela mexicana.",
 "A whole market in one stop":"Todo un mercado en una sola parada",
 "Meat counter, hot food in the back, fresh tortillas, a full grocery, and a self-serve beer fridge, all under one roof.":"Vitrina de carne, comida caliente al fondo, tortillas frescas, abarrotes completos y un refri de cervezas de autoservicio, todo bajo un mismo techo.",
 "What we do":"Lo que hacemos","From the meat counter to the table.":"De la vitrina a la mesa.",
 "Fresh & marinated meats":"Carnes frescas y preparadas",
 "Custom cuts and our famous carne asada preparada, marinated and ready for the grill.":"Cortes a tu gusto y nuestra famosa carne asada preparada, lista para el asador.",
 "Tacos, tortas & quesadillas":"Tacos, tortas y quesadillas",
 "Huge tacos with a grilled jalapeño, tortas, and quesadillas, cooked to order in the back.":"Tacos enormes con jalapeño asado, tortas y quesadillas, hechos al momento en la cocina de atrás.",
 "Soups & Mexican plates":"Caldos y platillos",
 "Hearty caldos and full Mexican plates with rice and beans, like a grandma would make.":"Caldos sustanciosos y platillos completos con arroz y frijoles, como los hace una abuela.",
 "Handmade, every day":"Hechas a mano, todos los días",
 "Corn tortillas pressed for every order and tamales by the dozen, cooked or frozen to go.":"Tortillas de maíz hechas para cada orden y tamales por docena, calientitos o congelados para llevar.",
 "Mexican grocery & cantina":"Abarrotes y cantina",
 "A full Mexican market: salsas, dulces, jarritos, party goods, and a self-serve beer fridge.":"Un mercado mexicano completo: salsas, dulces, jarritos, cosas para fiesta y un refri de cervezas de autoservicio.",
 "BBQ & party trays":"Carne para fiestas y charolas",
 "Everything for a backyard BBQ or party: marinated meat by the pound and party-sized orders.":"Todo para una carne asada o fiesta: carne preparada por libra y órdenes para fiesta.",
 "How it works":"Cómo funciona","Walk in hungry, leave with dinner and groceries.":"Entra con hambre, sal con la cena y el mandado.",
 "Come in off Main Street":"Llega por la calle Main",
 "Find us at 517 Main St in downtown Caldwell, look for the red awning.":"Encuéntranos en el 517 de Main St en el centro de Caldwell, busca el toldo rojo.",
 "Order at the counter, or pick your cuts":"Ordena en el mostrador, o escoge tus cortes",
 "Hot food and tacos are ordered in the back. Want to grill at home? The carniceros will cut and marinate your meat.":"La comida caliente y los tacos se ordenan al fondo. ¿Quieres asar en casa? Los carniceros te cortan y preparan la carne.",
 "Grab a cerveza, eat in or take it home":"Agarra una cerveza, come aquí o llévatelo",
 "Help yourself to a cold one from the fridge, they tab your table. Shop the market on your way out.":"Sírvete una fría del refri, la apuntan a tu mesa. Date una vuelta por el mercado a la salida.",
 "The shop":"La tienda","Real food, real market, on Main Street.":"Comida de verdad, mercado de verdad, en Main Street.",
 "Straight from Google and Yelp":"Directo de Google y Yelp","Loved across the Treasure Valley.":"Querida en todo el Treasure Valley.",
 "based on 225 Google reviews":"según 225 reseñas de Google",
 "The family behind the counter":"La familia detrás del mostrador","A hidden gem in the back of the market.":"Una joya escondida al fondo del mercado.",
 "Carnicería Mi Tierra has been a Main Street fixture in downtown Caldwell, a family run shop where the meat case, the kitchen, and a full Mexican grocery all live under one roof. Regulars say it feels a little like Tijuana, in the best way, with staff who treat you like family.":"Carnicería Mi Tierra es desde hace años un punto de referencia en Main Street, en el centro de Caldwell, un negocio familiar donde la vitrina de carne, la cocina y un mercado mexicano completo conviven bajo un mismo techo. Los clientes dicen que se siente un poco como Tijuana, en el buen sentido, con un trato que te hace sentir de la familia.",
 "The carniceros cut and marinate the asada by hand, the cocina presses tortillas fresh for every order, and the freezer is stocked with tamales people drive across the valley for. It is not just a meat market. It is the real deal.":"Los carniceros cortan y preparan la asada a mano, la cocina hace las tortillas al momento para cada orden, y el congelador está surtido de tamales por los que la gente maneja desde todo el valle. No es solo una carnicería. Es la de a de veras.",
 "From the counter":"Desde el mostrador",
 "How to order at a Mexican carnicería (and what to ask for)":"Cómo ordenar en una carnicería mexicana (y qué pedir)",
 "New to the carnicería? Here is exactly what to order, how to ask for your asada preparada, and how the taquería in the back works.":"¿Primera vez en la carnicería? Aquí te decimos qué ordenar, cómo pedir tu asada preparada, y cómo funciona la taquería de atrás.",
 "Read the guide":"Leer la guía","Setting up a carne asada?":"¿Vas a hacer una carne asada?",
 "Order marinated meat by the pound, fresh tortillas, salsas, and drinks for the whole fiesta in one stop.":"Pide carne preparada por libra, tortillas frescas, salsas y bebidas para toda la fiesta en una sola parada.",
 "Plan your party":"Organiza tu fiesta",
 "Good to know":"Bueno saber","Questions, answered.":"Preguntas, respondidas.",
 "Do you have a taquería, or is it just a meat market?":"¿Tienen taquería, o es solo carnicería?",
 "Both. There is a full meat counter and a Mexican grocery up front, and a taquería kitchen in the back serving tacos, tortas, quesadillas, caldos, and plates.":"Las dos cosas. Al frente hay una vitrina de carne completa y un mercado mexicano, y al fondo una cocina de taquería con tacos, tortas, quesadillas, caldos y platillos.",
 "Can I buy meat by the pound and get custom cuts?":"¿Puedo comprar carne por libra y pedir cortes a mi gusto?",
 "Yes. The carnicería does custom cuts and carne asada preparada, marinated and ready for the grill, sold by the pound. Ask for special cuts or a whole pig for a party.":"Sí. La carnicería hace cortes a tu gusto y carne asada preparada, lista para el asador, vendida por libra. Pide cortes especiales o un cerdo entero para tu fiesta.",
 "Are the tortillas really made fresh?":"¿De verdad hacen las tortillas frescas?",
 "Yes, corn tortillas are pressed fresh for your order, and reviewers keep coming back for them and for the tamales.":"Sí, las tortillas de maíz se hacen al momento para tu orden, y los clientes regresan por ellas y por los tamales.",
 "Can you set me up for a backyard BBQ or party?":"¿Me pueden surtir para una carne asada o fiesta?",
 "Yes. Tell us your headcount and date and we will help you order marinated meat, tortillas, salsas, sides, and drinks for the whole fiesta.":"Sí. Dinos cuántas personas y la fecha, y te ayudamos a ordenar carne preparada, tortillas, salsas, guarniciones y bebidas para toda la fiesta.",
 "Do you sell beer?":"¿Venden cerveza?",
 "Yes, there is a self-serve beer fridge, just grab a cold one and we tab it to your table.":"Sí, hay un refri de cervezas de autoservicio, agarra una fría y la apuntamos a tu mesa.",
 "Where are you and what are your hours?":"¿Dónde están y cuál es su horario?",
 "517 Main St in downtown Caldwell. Open Monday to Saturday 8:00 AM to 8:00 PM, and Sunday 8:00 AM to 7:00 PM.":"517 Main St en el centro de Caldwell. Abierto de lunes a sábado de 8:00 AM a 8:00 PM, y domingo de 8:00 AM a 7:00 PM.",
 "Come hungry. Leave with dinner, and groceries.":"Ven con hambre. Vete con la cena, y el mandado.",
 "517 Main St, Caldwell. Open every day. Walk in, call ahead, or set up your next BBQ.":"517 Main St, Caldwell. Abierto todos los días. Pásate, llámanos, u organiza tu próxima carne asada.",
 "A family run Mexican carnicería, taquería, and market on Main Street in downtown Caldwell. The real deal.":"Una carnicería, taquería y mercado mexicano familiar en Main Street, en el centro de Caldwell. La de a de veras.",
 "Visit":"Visítanos","Hours":"Horario","Mon to Sat":"Lun a Sáb","Sunday":"Domingo","Explore":"Explora",
 "8:00 AM to 8:00 PM":"8:00 AM a 8:00 PM","8:00 AM to 7:00 PM":"8:00 AM a 7:00 PM",
 "8 AM to 8 PM":"8 AM a 8 PM","8 AM to 7 PM":"8 AM a 7 PM",
 "© 2026 Carnicería Mi Tierra. All rights reserved.":"© 2026 Carnicería Mi Tierra. Todos los derechos reservados.",
 "· 225 Google reviews":"· 225 reseñas de Google",
 "Home":"Inicio","Departments":"Departamentos","What it is":"Qué es","Good for":"Ideal para",
 "Ready when you are.":"Listos cuando tú quieras.","Call ahead or just walk in to 517 Main St.":"Llámanos o pásate directo al 517 de Main St.",
 "What people say":"Lo que dice la gente",
 "What you will find":"Lo que encontrarás","Sold how you want it":"Como tú lo quieras","Why folks come back":"Por qué regresan",
 "On the plate":"En el plato","Made to order":"Hecho al momento","The vibe":"El ambiente","Plates":"Platillos","Soups":"Caldos",
 "Comes with":"Viene con","Tip":"Consejo","On the shelves":"En los estantes","Self-serve cerveza":"Cerveza de autoservicio",
 "One stop":"Una sola parada","Carne for the grill":"Carne para el asador","Round it out":"Complétalo","Plan ahead":"Planéalo con tiempo",
 "Everything under one roof":"Todo bajo un mismo techo","A carnicería, a taquería, and a Mexican market.":"Una carnicería, una taquería y un mercado mexicano.",
 "Pick your cuts, order hot food in the back, stock up on groceries, and set up your next party, all in one stop on Main Street.":"Escoge tus cortes, ordena comida caliente al fondo, surte tu despensa y organiza tu próxima fiesta, todo en una parada en Main Street.",
 "Come see us at 517 Main St.":"Ven a visitarnos al 517 de Main St.","Open every day. Walk in or call ahead.":"Abierto todos los días. Pásate o llámanos.",
 "From the counter · Caldwell, ID":"Desde el mostrador · Caldwell, ID",
 "First time at a real carnicería? Here is how Mi Tierra works, what to order, and how to walk out with a trunk full of dinner.":"¿Primera vez en una carnicería de verdad? Así funciona Mi Tierra, qué ordenar, y cómo salir con la cajuela llena de cena.",
 "Listen instead: the Mi Tierra carnicería guide":"Mejor escúchalo: la guía de la carnicería Mi Tierra",
 "A quick two minute walk through with Ava and Marco":"Un recorrido rápido de dos minutos con Ava y Marco",
 "Ready to order?":"¿Listo para ordenar?","Fresh meat, hot tacos, and a whole market on Main Street.":"Carne fresca, tacos calientes y todo un mercado en Main Street.",
 "See the departments":"Ver los departamentos",
}
import json as _json
I18N_SCRIPT="<script>\nvar I18N="+_json.dumps(ES_DICT,ensure_ascii=False)+";\n"+r"""
function _trWalk(lang){
 var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,{acceptNode:function(n){var p=n.parentNode;if(!p)return NodeFilter.FILTER_REJECT;var t=p.nodeName;if(t==='SCRIPT'||t==='STYLE'||t==='NOSCRIPT'||t==='AUDIO')return NodeFilter.FILTER_REJECT;return NodeFilter.FILTER_ACCEPT;}});
 var nodes=[];while(w.nextNode())nodes.push(w.currentNode);
 nodes.forEach(function(n){
  var raw=n.nodeValue;if(!raw)return;var key=raw.trim().replace(/\s+/g,' ');if(!key)return;
  if(n.__en===undefined)n.__en=raw;
  if(lang==='es'&&I18N[key]!==undefined){var lead=(raw.match(/^\s*/)||[''])[0],tr=(raw.match(/\s*$/)||[''])[0];n.nodeValue=lead+I18N[key]+tr;}
  else{n.nodeValue=n.__en;}
 });
 document.documentElement.lang=lang;
 var lb=document.getElementById('langLabel');if(lb)lb.textContent=(lang==='es'?'EN':'ES');
 var lbm=document.getElementById('langLabelM');if(lbm)lbm.textContent=(lang==='es'?'English':'Español');
 try{localStorage.setItem('lang',lang);}catch(e){}
}
function toggleLang(){var cur='en';try{cur=localStorage.getItem('lang')||'en';}catch(e){}_trWalk(cur==='es'?'en':'es');}
(function(){var l=null;try{l=localStorage.getItem('lang');}catch(e){}if(l==='es')_trWalk('es');})();
</script>"""


# ---------- WRITE FILES ----------
def w(fn,html):
  with open(os.path.join(OUT,fn),"w",encoding="utf-8") as f: f.write(html)
  print("wrote",fn,len(html))

index_html=head(f"Carnicería Mi Tierra | Mexican Carnicería, Taquería & Market in Caldwell, ID",
  f"Family run Mexican carnicería, taquería, and market at 517 Main St, Caldwell. Carne asada preparada by the pound, huge tacos, handmade tortillas, tamales, and a full market. {RATING} stars, {RCOUNT} reviews. Call {PHONE_DISP}.",
  [ld_business(),ld_faq(FAQS_INDEX)])+header()+index_body()+footer()
w("index.html",index_html)
w("services.html",services_overview())
for s in SERVICES: w(f"{s['slug']}.html",service_page(s))
w("blog.html",blog_page())

# robots / sitemap / nojekyll
open(os.path.join(OUT,".nojekyll"),"w").close()
with open(os.path.join(OUT,"robots.txt"),"w") as f:
  f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
pages=["/","/services.html","/blog.html"]+[f"/{s['slug']}.html" for s in SERVICES]
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">\n'
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in pages: sm+=f'  <url><loc>{DOMAIN}{p}</loc><changefreq>monthly</changefreq></url>\n'
sm+='</urlset>\n'
with open(os.path.join(OUT,"sitemap.xml"),"w") as f: f.write(sm)
print("wrote robots, sitemap, nojekyll")
