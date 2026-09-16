"""Regenerate the static homepage from publication data; no dependencies required."""
from pathlib import Path
import json
from html import escape

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT/'data/profile.json').read_text())
figures = {
    'finetuning2026': 'fine-tuning.jpg', 'tabtune2026': 'tabtune.png',
    'ontology2026': 'clinical-qa.png', 'orionbix2026': 'orion-bix.png',
    'peraugy2025': 'peraugy.png', 'health2026': 'distillation.png',
    'pocket2026': 'distillation.png', 'orionmsp2025': 'orion-msp.png',
}

def publication(p, label):
    figure = figures.get(p['id'])
    visual = f'<a href="images/sides/{figure}" target="_blank" rel="noopener" aria-label="Open figure for {escape(p["title"], quote=True)}"><img class="sideimg" src="images/sides/{figure}" alt="Figure for {escape(p["title"], quote=True)}" loading="lazy"></a>' if figure else ''
    authors = escape(p['authors']).replace('Aditya Tanna', '<span class="thisauthor">Aditya Tanna</span>')
    links = []
    if p['url']:
        links.append(f'<a class="tag" href="{escape(p["url"], quote=True)}" target="_blank" rel="noopener">'+('arXiv' if 'arxiv.org' in p['url'] else 'Paper')+'</a>')
    if p['id']=='tabtune2026': links.append('<a class="tag" href="https://github.com/Lexsi-Labs/TabTune" target="_blank" rel="noopener">Code</a>')
    if figure: links.append(f'<a class="tag" href="images/sides/{figure}" target="_blank" rel="noopener">Figure</a>')
    award=f'<span class="award">{escape(p["award"])}</span> · ' if p.get('award') else ''
    return f'''<article class="publication" id="pub-{p['id']}">
      <div class="publication-visual">{visual}</div>
      <div class="paper"><h3 class="paper-title" style="margin:0">[{label}] {escape(p['title'])}</h3>
      <div>{authors}</div><div>{award}<span class="venue">{escape(p['venue'])} {p['year']}</span></div>
      <div class="pub-links">{''.join(links)}</div></div></article>'''

pubs=[]
for category,prefix,heading in [('Conference & journal','C','Conference and journal'),('Workshop & preprint','W','Workshop and preprint')]:
    pubs.append(f'<h3 class="group-label">{heading}</h3>')
    for n,p in enumerate([p for p in data['publications'] if p['type']==category],1): pubs.append(publication(p,f'{prefix}.{n}'))

page='''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Aditya Tanna | Research Scientist at Lexsi Labs</title>
<meta name="description" content="Aditya Tanna leads tabular foundation model research at Lexsi Labs. Research on synthetic pretraining, fine-tuning, calibration, distillation, and structured learning.">
<meta name="robots" content="index,follow">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="css/site.css"><script src="js/site.js"></script>
</head><body><a class="skip" href="#about">Skip to content</a>
<div class="container">
<nav class="section-nav" aria-label="Page sections">
 <button class="theme-toggle" type="button" aria-label="Toggle dark mode"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M20.4 15.4A9 9 0 0 1 8.6 3.6a9 9 0 1 0 11.8 11.8Z"/></svg></button>
 <div class="nav-links"><a href="#about">About</a><a href="#timeline">Timeline</a><a href="#publications">Publications</a><a href="#projects">Projects</a></div>
</nav>
<div class="layout">
<aside class="profile" aria-label="Profile and contact links">
 <h1 class="name">Aditya Tanna</h1>
 <img class="profilepic" src="images/profile.png" width="960" height="990" alt="Aditya Tanna" fetchpriority="high">
 <div class="socials">
  <a class="email" href="mailto:adityatanna29@gmail.com"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/></svg>adityatanna29 [at] gmail [dot] com</a>
  <a href="https://github.com/adityatanna29" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 21v-4c-5 1-6-2-6-2m12 6v-4c0-1-.2-2-1-3 4 0 6-2 6-6 0-2-1-3-2-4 0-1 0-2-1-3-2 0-3 1-4 1h-2C10 1 8 1 6 1c-1 1-1 3-1 4-1 1-2 2-2 4 0 4 3 5 7 5-1 1-1 2-1 3"/></svg>GitHub</a>
  <a href="https://www.linkedin.com/in/aditya-tanna29/" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 10v7m0-10v.1M11 17v-7m0 3c0-4 6-4 6 0v4"/></svg>LinkedIn</a>
  <a href="https://scholar.google.com/citations?user=8y8sDywAAAAJ" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m2 9 10-6 10 6-10 6Z"/><path d="M6 12v6c4 3 8 3 12 0v-6M22 9v9"/></svg>Google Scholar</a>
  <a class="source-link" href="https://github.com/adityatanna29/adityatanna29.github.io" target="_blank" rel="noopener">Website source</a>
 </div>
</aside>
<main class="content">
 <section class="section" id="about"><h2 class="section-title">About</h2>
 <p>Hello! My name is Aditya Tanna, and I am a Research Scientist at <a href="https://github.com/Lexsi-Labs" target="_blank" rel="noopener">Lexsi Labs</a>, where I lead the tabular foundation model team. I study what these models learn from synthetic pretraining, how adaptation changes that knowledge, and how much remains after compression.</p>
 <p>I built and maintain <a href="https://github.com/Lexsi-Labs/TabTune" target="_blank" rel="noopener">TabTune</a>, our open-source library that brings more than ten tabular foundation models under one interface for inference, meta-learning, and fine-tuning [<a class="pub-ref" href="#pub-tabtune2026">WWW ’26</a>]. My research explores fine-tuning and calibration [<a class="pub-ref" href="#pub-finetuning2026">WWW ’26</a>], distillation into CPU-ready students [<a class="pub-ref" href="#pub-health2026">SD4H ’26</a>], the limits of ensembling [<a class="pub-ref" href="#pub-ensemble2026">FMSD ’26</a>], and attention architectures designed for tables [<a class="pub-ref" href="#pub-orionbix2026">WWW ’26</a>, <a class="pub-ref" href="#pub-orionmsp2025">EurIPS ’25</a>].</p>
 <p>Previously, I was a Research Assistant with <strong>Prof. Sourish Dasgupta</strong> at the Knowledge and Discovery Lab, working on preference-diversity augmentation for personalized summarization [<a class="pub-ref" href="#pub-peraugy2025">TMLR ’25</a>]. My undergraduate thesis with <strong>Prof. Abhishek Jindal</strong> investigated ontology-grounded reinforcement learning for clinical question answering [<a class="pub-ref" href="#pub-ontology2026">CIKM ’26</a>]. I completed my B.Tech. in Mathematics and Computing at <strong>Dhirubhai Ambani University</strong> (formerly DA-IICT), with a merit scholarship in all eight semesters.</p>
 <p><strong>Keywords:</strong> Tabular Foundation Models, Pretraining Priors, Fine-Tuning, Calibration, Distillation, In-Context Learning</p>
 <p>If you’d like to discuss my research or a collaboration, feel free to reach out <a href="mailto:adityatanna29@gmail.com">via email!</a></p>
 <p class="updated">Last updated: September 2026</p></section>
 <section class="section" id="timeline"><h2 class="section-title">Timeline</h2>
 <div class="news-scroll" tabindex="0" role="region" aria-label="Research and career timeline">
  <div class="news-item"><strong>• 2026:</strong> Our work on distilling tabular foundation models for structured health data received a <em>Spotlight</em> at SD4H @ ICML. Our credit-risk study received an <em>Oral</em> presentation at FinDS @ SIGMOD/PODS.</div>
  <div class="news-item"><strong>• 2026:</strong> TabTune, our fine-tuning study, and Orion-BiX appear at The Web Conference (WWW). Our ontology-grounded clinical QA work appears at CIKM.</div>
  <div class="news-item"><strong>• 2025:</strong> Our personalized summarization work, PerAugy, was published in TMLR. Orion-MSP was presented at AITD @ EurIPS.</div>
  <div class="news-item"><strong>• August 2025:</strong> Joined Lexsi Labs as a Research Scientist, leading research on tabular foundation models.</div>
  <div class="news-item"><strong>• May 2025:</strong> Completed my B.Tech. in Mathematics and Computing at Dhirubhai Ambani University.</div>
  <div class="news-item"><strong>• January 2024:</strong> Began working with Prof. Sourish Dasgupta as a Research Assistant at the Knowledge and Discovery Lab.</div>
 </div></section>
 <section class="section" id="publications"><h2 class="section-title">Publications</h2>
 <p class="pub-legend">C = Conference or journal · W = Workshop or preprint</p>
 __PUBLICATIONS__
 </section>
 <section class="section" id="projects"><h2 class="section-title">Projects</h2>
 <article class="project"><div><h3>TabTune: A Unified Tabular ML Toolkit</h3><p>An open-source library for inference, meta-learning, supervised fine-tuning, and parameter-efficient adaptation across 10+ tabular foundation models. Includes calibration and fairness evaluation, with extensions for conformal prediction, row-feature attribution, and prediction provenance.</p><div class="pub-links"><a class="tag" href="https://github.com/Lexsi-Labs/TabTune" target="_blank" rel="noopener">GitHub</a><a class="tag" href="https://dl.acm.org/doi/10.1145/3774905.3793137" target="_blank" rel="noopener">Paper</a></div></div><a href="images/sides/tabtune.png" target="_blank" rel="noopener" aria-label="Open TabTune overview"><img src="images/sides/tabtune.png" alt="TabTune toolkit architecture" loading="lazy"></a></article>
 <article class="project no-image"><div><h3>Forty8: Calibrated World Cup Forecasting</h3><p>A probabilistic forecasting engine for the 2026 World Cup. Combines rating, goal, market, and squad-strength models using a log-opinion pool, then simulates 300,000 tournament outcomes. Uses walk-forward backtesting, Brier scores, and completed-match constraints to produce calibrated, results-conditioned forecasts.</p></div></article>
 </section>
 <section class="section details" id="teaching"><h2 class="section-title">Teaching &amp; Service</h2>
 <p>At Dhirubhai Ambani University, I was a Teaching Assistant for <strong>Object Oriented Programming</strong> with Prof. Sourish Dasgupta (January–June 2025), <strong>Database Management Systems</strong> with Prof. Amit Mankodi (July–December 2024), and <strong>Big Data Processing</strong> with Prof. PM Jat (July–December 2024).</p>
 <p><strong>Reviewer:</strong> NeurIPS 2026, CIKM 2026, and the FMSD and SD4H workshops at ICML 2026.</p>
 </section>
 <footer>© 2026 Aditya Tanna. Layout reference: <a href="https://wattsishaan.github.io/" target="_blank" rel="noopener">Ishaan Watts</a>, whose site credits <a href="https://github.com/SebastinSanty/minimal-research-theme" target="_blank" rel="noopener">minimal-research-theme</a>.</footer>
</main></div></div></body></html>
'''
(ROOT/'index.html').write_text(page.replace('__PUBLICATIONS__','\n'.join(pubs)))
print('Generated homepage with 11 papers and 8 publication figure placements.')
