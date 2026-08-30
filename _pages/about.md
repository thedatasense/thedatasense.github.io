---
layout: home
permalink: /
title: "Medical AI Safety & Systems"
excerpt: "Medical AI systems for surgical innovation—and research into the failures that standard benchmarks miss."
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="home-hero" aria-labelledby="home-intro-title">
  <div class="home-shell home-hero__grid">
    <div>
      <p class="home-eyebrow">Medical AI systems · safety · interpretability</p>
      <h1 id="home-intro-title">I build medical AI that <em>earns the right</em> to be trusted.</h1>
      <p class="home-hero__lede">I’m Binesh K Sadanandan—Technical Fellow at Medtronic Surgical Innovation. I successfully defended my Ph.D. dissertation on medical-AI reliability at the University of New Haven on August 26, 2026.</p>
      <div class="home-hero__actions">
        <a class="home-action home-action--primary" href="/research/">Explore the research</a>
        <a class="home-action home-action--secondary" href="/psf-med-failures/">View failure gallery</a>
      </div>
    </div>

    <div class="home-signal" aria-hidden="true">
      <p class="home-signal__topline">Schematic failure pattern · not patient data</p>
      <div class="home-signal__case">
        <div class="home-signal__image"></div>
        <div class="home-signal__copy">
          <p class="home-signal__label">Same image · new wording</p>
          <p class="home-signal__question">Can a clinically equivalent question change the model’s diagnosis?</p>
          <div class="home-signal__answers">
            <div class="home-signal__answer"><strong>Prompt A</strong>Stable answer</div>
            <div class="home-signal__answer home-signal__answer--flagged"><strong>Prompt B</strong>Answer flips</div>
          </div>
        </div>
      </div>
      <p class="home-signal__footer">The job is not just to measure reliability. It’s to interrogate it.</p>
    </div>
  </div>
</section>

<section class="home-proof" aria-label="Career and research highlights">
  <div class="home-shell home-proof__grid">
    <div class="home-proof__item"><span class="home-proof__number">19</span><span class="home-proof__label">years of engineering experience</span></div>
    <div class="home-proof__item"><span class="home-proof__number">12</span><span class="home-proof__label">publications &amp; preprints in medical AI</span></div>
    <div class="home-proof__item"><span class="home-proof__number">2</span><span class="home-proof__label">patents in ML for surgical devices</span></div>
    <div class="home-proof__item"><span class="home-proof__number">92,856</span><span class="home-proof__label">evaluation question–paraphrase pairs in PSF-Med</span></div>
  </div>
</section>

<section class="home-section" aria-labelledby="research-title">
  <div class="home-shell">
    <div class="home-section__head">
      <div>
        <p class="home-section__kicker">Flagship research</p>
        <h2 id="research-title">Reliability is more than a score.</h2>
      </div>
      <p class="home-section__intro">My dissertation, <em>Paraphrase Sensitivity in Medical Vision-Language Models</em>, asks a deliberately uncomfortable question: when a medical vision-language model appears reliable, is it actually looking at the image?</p>
    </div>

    <article class="home-flagship">
      <div class="home-flagship__body">
        <p class="home-flagship__label">PSF-Med benchmark</p>
        <h3>When the wording changes, should the diagnosis?</h3>
        <p>PSF-Med tests clinically equivalent questions against the same chest X-ray. It finds that models can flip their answer when the meaning has not changed—and can look consistent while ignoring the image altogether.</p>
        <a class="home-text-link" href="/research/">See the methods, evidence, and papers</a>
        <a class="home-text-link" href="/psf-med-failures/">View the real failure gallery</a>
      </div>
      <div class="home-flagship__evidence" aria-label="Selected research findings">
        <div class="home-evidence"><span class="home-evidence__number">6.4–54.7%</span><span class="home-evidence__label">of binary question pairs flip across six medical VLMs</span></div>
        <div class="home-evidence"><span class="home-evidence__number">81%</span><span class="home-evidence__label">of consistent predictions are image-invariant across ten settings</span></div>
        <div class="home-evidence"><span class="home-evidence__number">59%</span><span class="home-evidence__label">reduction in pairwise flips from targeted LoRA, with an important grounding tradeoff</span></div>
      </div>
    </article>
  </div>
</section>

<section class="home-section home-section--surface" aria-labelledby="work-title">
  <div class="home-shell">
    <div class="home-section__head">
      <div>
        <p class="home-section__kicker">Selected work</p>
        <h2 id="work-title">From devices to deployment.</h2>
      </div>
      <p class="home-section__intro">I work across the full chain: trustworthy data, intelligent medical devices, robust clinical models, and the evidence needed to challenge them.</p>
    </div>

    <div class="home-work">
      <a class="home-work__card" href="/research/">
        <span class="home-work__index">01</span>
        <p class="home-work__type">Research</p>
        <h3>Medical VLM safety</h3>
        <span class="home-work__arrow" aria-hidden="true">→</span>
      </a>
      <a class="home-work__card" href="/portfolio/medical-device-failures/">
        <span class="home-work__index">02</span>
        <p class="home-work__type">Applied ML</p>
        <h3>Failure detection for medical devices</h3>
        <span class="home-work__arrow" aria-hidden="true">→</span>
      </a>
      <a class="home-work__card" href="/publications/">
        <span class="home-work__index">03</span>
        <p class="home-work__type">Publications</p>
        <h3>Methods, benchmarks, and evidence</h3>
        <span class="home-work__arrow" aria-hidden="true">→</span>
      </a>
    </div>
  </div>
</section>

<section class="home-contact" aria-labelledby="contact-title">
  <div class="home-shell">
    <p class="home-eyebrow">Let’s connect</p>
    <h2 id="contact-title">Working on a hard problem in trustworthy medical AI?</h2>
    <p>I’m always interested in thoughtful conversations about safety, interpretability, medical-device intelligence, and turning rigorous evidence into better systems.</p>
    <a class="home-action home-action--primary" href="mailto:contact@bineshkumar.me">Get in touch</a>
  </div>
</section>
