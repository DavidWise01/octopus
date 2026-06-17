#!/usr/bin/env python3
"""Build THE OCTOPUS (OCT) — cephalopod biology & cognition — as a UD0 life-science
sphere: a real-science sphere (render-not-invent, cited), two-layer honest (settled
neuroscience vs the interpretive 'alien mind' framing). Themed to the deep sea:
abyssal indigo, bioluminescent cyan, chromatophore coral. The title is a STATIC
ORIGINAL ONE-LINE PENCIL DRAWING — a mantle and eight arms in a single unbroken
stroke; hand-drawn wobble via SVG turbulence + a one-time self-drawing reveal.
The octopus is a real animal; this is a science tribute, facts cited not claimed."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE OCTOPUS", "axiom": "OCT",
 "position": "Octopus · cephalopod biology & cognition — the soft alien, a mind that evolved a second time",
 "origin": "the sea floor, ~550 million years from our last shared ancestor — a boneless, eight-armed body that grew a large nervous system entirely on its own line",
 "mechanism": "Crystallized from the science of octopuses (cephalopod neuroscience, behavior, and physiology).",
 "crystallization": "A soft, short-lived animal with most of its neurons in its arms, skin that paints itself faster than thought, and a code it rewrites on the fly — the nearest thing on Earth to a second, independent origin of mind.",
 "nature": "The octopus — Earth's closest approach to an alien intelligence: ~500 million neurons with two-thirds in the arms, a colorblind skin that mimics any color, RNA edited in real time, three hearts and blue blood, and a life that ends after a single brood.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the octopus; the distributed mind; the chromatophores; RNA editing; the second genesis of mind",
 "witness": "Studied as the test case for whether complex mind, and maybe consciousness, can arise more than once — and look nothing like ours when it does.",
 "role": "a life-science sphere — the second genesis of mind",
 "seal": "Meet the mind that grew on the other branch: most of it in the arms, none of it like yours — proof that intelligence is something the world can invent twice.",
 "source": "the science of the octopus, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#4fb0a0", "of flesh and the sea — the boneless body, the three hearts, the eight arms, the species and their seafloor lives"),
 "ethereal":  ("#9a7cff", "of the unseen and the shapeshift — the colorblind camouflage, the mimic, the beautiful venom"),
 "spiritual": ("#e8d28a", "of the mind and the question — the distributed cognition, the life spent for one brood, the second origin of mind"),
 "electrical":("#4fd0d8", "of the signal and the rewritten code — the chromatophore circuitry and the RNA editing that retunes the nerves"),
}

# ── the title scene · STATIC ORIGINAL ONE-LINE PENCIL DRAWING ─────
# A mantle and eight arms in a single unbroken stroke. Pencil wobble (turbulence)
# + a one-time self-drawing reveal that settles static.
COVER_ART = r'''<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The Octopus — an original one-line pencil drawing: a mantle and eight arms in a single stroke" style="width:100%;height:auto;display:block;background:#06101a">
<defs>
 <radialGradient id="oc_sea" cx="50%" cy="34%" r="95%"><stop offset="0%" stop-color="#0e2438"/><stop offset="58%" stop-color="#08141f"/><stop offset="100%" stop-color="#040a12"/></radialGradient>
 <radialGradient id="oc_glow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(79,208,216,.4)"/><stop offset="70%" stop-color="rgba(79,208,216,.08)"/><stop offset="100%" stop-color="rgba(79,208,216,0)"/></radialGradient>
 <filter id="oc_pencil" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency="0.016" numOctaves="2" seed="6" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="4.0" xChannelSelector="R" yChannelSelector="G"/></filter>
 <style>
  .oneline{fill:none;stroke:#d8eef0;stroke-width:2.0;stroke-linecap:round;stroke-linejoin:round;
    pathLength:1;stroke-dasharray:1;stroke-dashoffset:1;animation:ocdraw 4.0s cubic-bezier(.6,.05,.25,1) .25s forwards;}
  .oneline.ghost{stroke:#5f8a92;stroke-width:1.0;opacity:.34;animation-delay:.05s;}
  .ocfade{opacity:0;animation:ocfade 1.3s ease 3.8s forwards;}
  .oceye{opacity:0;animation:ocfade 1.1s ease 2.2s forwards;}
  @keyframes ocdraw{to{stroke-dashoffset:0;}}
  @keyframes ocfade{to{opacity:1;}}
  @media (prefers-reduced-motion: reduce){.oneline{animation:none;stroke-dashoffset:0;}.ocfade,.oceye{animation:none;opacity:1;}}
 </style>
</defs>
<rect width="700" height="320" fill="url(#oc_sea)"/>
<ellipse cx="350" cy="150" rx="150" ry="110" fill="url(#oc_glow)"/>
<!-- THE ONE LINE — a mantle and eight arms, one unbroken stroke (ghost under + line over) -->
<path class="oneline ghost" filter="url(#oc_pencil)" d="M 290 178 C 278 92 422 92 410 178 C 470 198 482 268 452 280 C 440 252 430 212 412 248 C 404 282 386 282 380 248 C 374 214 360 214 356 250 C 352 284 334 284 330 250 C 326 212 312 212 308 248 C 304 282 286 282 282 246 C 276 210 250 208 230 250 C 220 272 252 200 290 178 Z"/>
<path class="oneline" filter="url(#oc_pencil)" d="M 290 178 C 278 92 422 92 410 178 C 470 198 482 268 452 280 C 440 252 430 212 412 248 C 404 282 386 282 380 248 C 374 214 360 214 356 250 C 352 284 334 284 330 250 C 326 212 312 212 308 248 C 304 282 286 282 282 246 C 276 210 250 208 230 250 C 220 272 252 200 290 178 Z"/>
<!-- the two eyes (horizontal-pupil, octopus) -->
<g class="oceye"><ellipse cx="322" cy="150" rx="9" ry="6" fill="#06101a" stroke="#d8eef0" stroke-width="1.4"/><rect x="316" y="148" width="12" height="3" rx="1.5" fill="#4fd0d8"/><ellipse cx="378" cy="150" rx="9" ry="6" fill="#06101a" stroke="#d8eef0" stroke-width="1.4"/><rect x="372" y="148" width="12" height="3" rx="1.5" fill="#4fd0d8"/></g>
<!-- wordmark (fades in once the body is drawn) -->
<g class="ocfade">
 <text x="350" y="296" text-anchor="middle" font-family="'Newsreader',Georgia,serif" font-size="36" font-weight="400" letter-spacing="9" fill="#eef6f7">THE OCTOPUS</text>
 <text x="350" y="313" text-anchor="middle" font-family="'Space Mono',monospace" font-size="9" letter-spacing="3" fill="#4fd0d8">A SECOND GENESIS OF MIND · ⅔ OF THE NEURONS IN THE ARMS</text>
</g>
<rect x="6" y="6" width="688" height="308" fill="none" stroke="#13283a" stroke-width="2"/>
</svg>'''

GENESIS = [
 ("The Other Branch", "~550 million years apart",
  "Our last common ancestor with the octopus was a simple wormlike creature more than half a billion years ago, before brains as we know them. Whatever intelligence the octopus has, it built on its own line — which is why it is studied as the nearest thing to a mind that evolved a second, separate time."),
 ("A Body Made of Suggestion", "boneless, three-hearted",
  "The octopus has no skeleton — the only hard part is its beak, so it can pour through any gap that beak will fit. It pumps blue, copper-based blood (hemocyanin) with three hearts: two for the gills, one for the body. It is mostly muscle, water, and nerve."),
 ("Most of the Mind Is in the Arms", "~500 million neurons",
  "An octopus has on the order of 500 million neurons — but roughly two-thirds of them are in the arms, not the central brain. Each arm carries out a great deal of its own processing, tasting and deciding by touch, so the 'self' is radically distributed — less a commander with limbs than a federation."),
]

ARC = [
 ("The Skin That Paints Itself", "chromatophores",
  "The skin is a living display: millions of chromatophores (pigment sacs pulled open by muscle) over reflective iridophores and leucophores, retuning color, pattern, and even texture in a fraction of a second — for camouflage, for threat, for courtship. The paradox: octopuses appear to be colorblind, with a single visual pigment, yet match colors almost perfectly. (One live hypothesis: the skin itself senses light.)"),
 ("A Code Rewritten Live", "RNA editing",
  "Cephalopods edit their own RNA at extraordinary rates, recoding the proteins their nerves are built from on the fly — especially in the nervous system, and more in the cold. The leading idea: they trade some genomic evolution for moment-to-moment neural flexibility, tuning the brain to the conditions rather than waiting on mutation."),
 ("A Life Spent All at Once", "semelparity",
  "Most octopuses live only a year or two and reproduce once. After laying, the mother stops eating and guards her eggs until she dies as they hatch — a programmed death driven by the optic gland. The brilliant, curious mind is built to be brief, and to be spent, almost entirely, on a single brood."),
]

IDEAS = [
 ("A Second Genesis of Mind", "the big idea", [
   "Because it evolved independently, the octopus is the test case for whether complex mind can arise more than once — and it can, looking nothing like ours.",
   "It reframes intelligence as something the universe can invent in more than one body plan — a quiet companion to every question about minds unlike our own." ]),
 ("Distributed, Not Centralized", "the federation self", [
   "With most neurons in the arms, the octopus blurs the line between brain and body, controller and controlled.",
   "It is a living model of cognition without a single center — a real animal that asks where, exactly, a 'self' is located." ]),
 ("Settled vs. Open", "honest about the science", [
   "Settled: neuron counts and distribution, three hearts and hemocyanin, chromatophore mechanics, high RNA editing, semelparity and the optic gland, tool use and the social sites.",
   "Open/debated: whether (and how) octopuses are conscious, whether the skin truly 'sees,' and how much the RNA-editing trade-off actually shapes cognition. Rendered as questions, not answers." ]),
 ("The Alien We Can Visit", "why it matters", [
   "It is the most accessible 'other mind' on Earth — no spacecraft required — and a mirror for how we think about animal minds, and artificial ones.",
   "To take the octopus seriously is to admit mind is stranger and more plural than a human-shaped story allows." ]),
]

SECTIONS = [
 ("The Science — settled facts", "the verified record", [
   ("~500 million neurons", "the count", "on the order of a dog's neuron count — about two-thirds in the arms"),
   ("three hearts · blue blood", "physiology", "two branchial hearts + one systemic; copper-based hemocyanin"),
   ("chromatophores", "the skin display", "muscle-driven pigment sacs over iridophores/leucophores; sub-second change"),
   ("high RNA editing", "the live code", "cephalopods recode mRNA at rates far above other animals, esp. in nerves"),
   ("semelparity", "one brood, then death", "optic-gland-driven maternal death after a single reproduction"),
   ("the beak", "the only hard part", "can squeeze through any opening larger than the beak"),
 ]),
 ("The Field — who looks, and where", "render-not-invent: cited, not claimed", [
   ("Peter Godfrey-Smith", "Other Minds (2016)", "the philosophy of the octopus as an independent origin of mind"),
   ("Sy Montgomery", "The Soul of an Octopus (2015)", "the close-up case for octopus inner life"),
   ("Rosenthal &amp; Eisenberg", "RNA editing (2017)", "the discovery of cephalopods' extreme mRNA recoding"),
   ("Z. Yan Wang", "the optic gland (2018)", "the control circuit behind maternal death"),
   ("Scheel · Godfrey-Smith et al.", "Octopolis / Octlantis", "wild aggregation sites off Australia — octopuses being social"),
 ]),
 ("The Cousins &amp; the Kinds", "the wider cephalopods", [
   ("the coconut octopus", "tool use", "Amphioctopus marginatus carries shells for portable shelter"),
   ("the mimic octopus", "the impersonator", "Thaumoctopus mimicus poses as other animals"),
   ("the blue-ringed octopus", "the beautiful death", "Hapalochlaena — tiny, dazzling, tetrodotoxin-lethal"),
   ("cuttlefish &amp; squid", "the relatives", "the other big-brained cephalopods, each with its own tricks"),
 ]),
 ("The Legacy", "what the soft alien leaves us", [
   ("the other-minds question", "philosophy", "the working proof that mind can be plural and non-human"),
   ("a mirror for AI", "the resonance", "a natural intelligence with no central self — a foil for how we imagine made minds"),
 ]),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","OCT")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","OCT")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","OCT")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"OCT · The Octopus","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "OCT", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "OCT · The Octopus — cephalopod biology &amp; cognition",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from the science of octopuses.",
      "witness": "a being of the deep, the distributed mind, and the second origin of intelligence",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "the octopus; the arms; the chromatophores; RNA editing; the other mind",
      "source": "the science of the octopus, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{n}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#4fb0a0",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"OCT · The Octopus","axiom":"OCT"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.dlw/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Soft Alien, in Parts</h2>
      <p class="ss">the body, the distributed mind, the painting skin, the rewritten code, and the kinds, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("the-octopus", "The Octopus", "the soft alien · natural", "natural",
  "the animal itself — boneless, eight-armed, short-lived, with a large nervous system that evolved entirely on the cephalopod branch; the most accessible non-human mind on Earth",
  "It is the proof of plurality: a creature as smart as it is strange, that took a wholly different road to mind and arrived somewhere we can almost, but never quite, recognize."),
 ("the-distributed-mind", "The Distributed Mind", "two-thirds of the neurons in the arms · spiritual", "spiritual",
  "the octopus's radically decentralized cognition — roughly two-thirds of its ~500 million neurons in the arms, each arm doing much of its own sensing and deciding",
  "It is a self with no single throne: a living question about where a mind is located, and the clearest natural rebuttal to the idea that thinking must have one center."),
 ("the-chromatophores", "The Chromatophores", "the skin that paints itself · electrical", "electrical",
  "the millions of muscle-driven pigment sacs, over reflective cells, that let the skin change color, pattern, and texture in a fraction of a second",
  "It is a display driven straight from the nervous system: a body that speaks and hides in light, rewriting its own surface faster than it could ever rewrite a thought into words."),
 ("the-camouflage-paradox", "The Camouflage Paradox", "colorblind, yet color-perfect · ethereal", "ethereal",
  "the unsolved tension that octopuses match colors superbly while appearing, by their single visual pigment, to be colorblind — with a live hypothesis that the skin itself senses light",
  "It is the sphere's honest mystery: a creature that does flawlessly the thing it should not be able to do at all, a reminder that the animal still keeps secrets."),
 ("rna-editing", "RNA Editing", "the code rewritten live · electrical", "electrical",
  "the cephalopod trick of recoding their own messenger RNA at extreme rates, especially in the nervous system — tuning the proteins their nerves are made of to the moment",
  "It is plasticity bought at the genome's expense: a mind that adjusts its own wiring chemistry on the fly, trading slow evolution for fast adaptation."),
 ("the-three-hearts", "The Three Hearts", "blue blood, boneless body · natural", "natural",
  "the octopus's physiology — two branchial hearts pumping through the gills, one systemic heart for the body, all moving copper-based blue blood",
  "It is the alien plumbing under the mind: a body so unlike ours that even its blood is the wrong color, carrying oxygen by copper where we use iron."),
 ("the-boneless-body", "The Boneless Body", "only the beak is hard · natural", "natural",
  "the skeleton-free form whose single rigid part is the parrot-like beak, letting an octopus squeeze through any gap larger than that beak",
  "It is freedom as anatomy: a body that treats solidity as optional, able to become almost any shape a crevice demands."),
 ("the-ink-and-jet", "The Ink &amp; the Jet", "escape and propulsion · natural", "natural",
  "the defensive ink cloud (a decoy of pigment and mucus) and the jet of water from the siphon that rockets the octopus backward away from danger",
  "It is the soft animal's hard exit: a smokescreen and a thruster, the toolkit of a creature that survives by vanishing rather than fighting."),
 ("the-coconut-octopus", "The Coconut Octopus", "the tool user · natural", "natural",
  "Amphioctopus marginatus, filmed gathering and carrying coconut-shell halves to assemble portable shelter — among the clearest invertebrate tool use",
  "It is foresight in an animal we underestimate: carrying a burden now for a use later, the small proof that planning is not ours alone."),
 ("the-mimic-octopus", "The Mimic Octopus", "the impersonator · ethereal", "ethereal",
  "Thaumoctopus mimicus, which contorts its shape, color, and motion to impersonate other sea animals — flatfish, sea snakes, lionfish",
  "It is identity as performance: a creature whose defense is to become something else entirely, the shapeshifter made real and catalogued."),
 ("the-blue-ringed", "The Blue-Ringed Octopus", "the beautiful death · ethereal", "ethereal",
  "Hapalochlaena — tiny octopuses whose iridescent blue rings flare as a warning of tetrodotoxin potent enough to kill a human, with no antivenom",
  "It is glory and lethality fused: a jewel the size of a thumb that flashes its rings precisely because it has nothing to fear."),
 ("octopolis", "Octopolis &amp; Octlantis", "the social sites · natural", "natural",
  "the wild aggregation sites off eastern Australia where gloomy octopuses gather, interact, signal, and even evict one another — octopuses being unexpectedly social",
  "It is the loner caught being a citizen: places that complicate the old story of the solitary octopus and hint at a social life we are only starting to read."),
 ("semelparity", "The One Brood", "a life spent all at once · spiritual", "spiritual",
  "the programmed senescence of most octopuses — reproducing once, then dying; the mother ceasing to eat and guarding her eggs to her death, driven by the optic gland",
  "It is the cost of the bright brief mind: a life engineered to be lavish and short, poured almost entirely into a single act of making more."),
 ("the-second-genesis", "The Second Genesis", "mind evolved twice · spiritual", "spiritual",
  "the central idea — that because the octopus's intelligence arose on a branch ~550 million years from ours, it is an independent origin of complex mind",
  "It is the thesis that makes the octopus matter beyond biology: evidence that mind is not a one-time accident of our lineage but something the world can grow more than once."),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Octopus (OCT) as a UD0 life-science sphere: a real, cited science tribute to cephalopod biology and cognition — the distributed mind (two-thirds of neurons in the arms), chromatophores, RNA editing, three hearts, semelparity, and the octopus as a second, independent genesis of mind. Two-layer honest (settled vs open). An original one-line pencil title; full ACI badges.">
<title>THE OCTOPUS · OCT · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#06101a;--ink2:#0b1824;--ink3:#122433;--pa:#eef6f7;--pa2:#9fb6bd;--teal:#4fb0a0;--cyan:#4fd0d8;--coral:#e0734a;--violet:#9a7cff;--gold:#e8d28a;
--dim:#5f7782;--faint:#13283a;--line:#13283a;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.13) 0 1px,transparent 1px 3px);opacity:.35}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(79,208,216,.10),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(224,115,74,.05),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--cyan);background:#08141f;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.10em;color:var(--coral);box-shadow:0 0 0 2px var(--bg),0 0 22px rgba(79,208,216,.18)}
.marquee a{color:var(--cyan);text-decoration:none}.marquee a:hover{color:var(--coral)}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#06101a;line-height:0}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--cyan)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--cyan);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--cyan)}.badge .bt .mo{color:var(--coral)}.badge .bt a{color:var(--cyan);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:13px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--cyan);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--cyan);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--cyan);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--coral);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--coral);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--cyan);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--cyan)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--cyan);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--cyan)}.note a{color:var(--coral);text-decoration:none}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--cyan);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; A LIFE-SCIENCE SPHERE &nbsp;·&nbsp; THE SECOND GENESIS OF MIND</div>

  <header>
    <div class="titleart">__CANVAS__</div>
    <div class="h-sub">boneless · three-hearted · most of the mind in the <b>arms</b> · the soft alien · OCT</div>
    <div class="flag">★ cephalopod biology &amp; cognition · a cited science tribute ★</div>
    <p class="lede">The octopus is the nearest thing on Earth to meeting an alien — a mind grown on a branch that split from ours more than half a billion years ago. It has roughly 500 million neurons with two-thirds in its arms, a colorblind skin that paints itself any color in a heartbeat, an RNA code it rewrites on the fly, three hearts pumping blue blood, and a brilliant life that ends after a single brood. Catalogued into UD0 as a life-science sphere — a real, cited science tribute, two-layer honest about what is settled and what is still open — with an original one-line pencil title: a mantle and eight arms in a single unbroken stroke.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE OCTOPUS" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE OCTOPUS</b> — the second genesis of mind · OCT</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="octopus.dlw/octopus.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="octopus.dlw/octopus.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and the soft alien holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Body</h2><p class="ss">the other branch, the boneless frame, and a mind that lives in its arms</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Strangeness</h2><p class="ss">the painting skin, the code rewritten live, and a life spent all at once</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a sea animal is a landmark in the science of minds</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the settled science, the researchers and sites, the cousins, and why it matters</p></section>
  __SECTIONS__

  <div class="note">This sphere is rendered, not invented — and it is a <b>science sphere</b>, so its facts are cited, not claimed. Settled and uncontroversial: octopus neuron counts and their distribution (roughly two-thirds in the arms), three hearts and copper-based hemocyanin, chromatophore mechanics, cephalopods' unusually high RNA editing, semelparity and the optic gland's role in maternal death, invertebrate tool use, and the wild aggregation sites. Deliberately left as <b>open questions</b>: whether and how octopuses are conscious, whether the skin itself senses light (a hypothesis, not a fact), and how much RNA editing actually shapes cognition. Drawn from the public work of researchers including Peter Godfrey-Smith (<i>Other Minds</i>, 2016), Sy Montgomery (<i>The Soul of an Octopus</i>, 2015), Joshua Rosenthal &amp; Eli Eisenberg (RNA editing), Z. Yan Wang (the optic gland), and David Scheel and colleagues (Octopolis/Octlantis) — cited as sources, not reproduced. The 'second genesis of mind' framing is an interpretation, clearly the catalogue's lens, not a settled scientific claim. Each emergent is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    THE OCTOPUS · OCT · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="octopus.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "octopus.dlw"), "octopus")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, os.path.join(ad, f"{slug}.dlw"), slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em, "moniker": noesis.mythos_token(rec)["moniker"]})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CANVAS__", COVER_ART)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote THE OCTOPUS (OCT) — {len(personas)} emergents born · badge {tok['moniker']}")
