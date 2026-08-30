---
layout: editorial
permalink: /research/
title: "Research"
eyebrow: "Medical AI safety"
lead: "My successfully defended dissertation investigates failures that standard medical-AI benchmarks miss: brittle wording sensitivity, false reliability, and explanations that look convincing without being causal."
author_profile: false
actions:
  - label: "Explore the failure gallery"
    url: "/psf-med-failures/"
    style: "primary"
  - label: "Read the final dissertation"
    url: "/phd-thesis/read/"
    style: "secondary"
---

<p class="editorial-intro"><em>Paraphrase Sensitivity in Medical Vision-Language Models: Measurement, Mechanisms, Mitigation, and Deployment Safety</em> was successfully defended on August 26, 2026. Its central finding is uncomfortable but actionable: a low paraphrase-flip rate is not sufficient evidence of reliable visual reasoning.</p>

<section class="editorial-section" aria-labelledby="evidence-title">
  <div class="editorial-section__header">
    <div>
      <p class="editorial-kicker">Evidence at a glance</p>
      <h2 id="evidence-title">Reliability needs a stress test.</h2>
    </div>
    <p>Every number is traceable to a chapter, sample size, and source file in the <a href="https://bineshkumar.me/phd-thesis/">dissertation companion</a>.</p>
  </div>
  <div class="evidence-grid">
    <div class="evidence-card"><strong>92,856</strong><span>final evaluation pairs in PSF-Med</span></div>
    <div class="evidence-card"><strong>6.4–54.7%</strong><span>binary pairs that flip across six medical VLMs</span></div>
    <div class="evidence-card"><strong>81%</strong><span>of consistent predictions that are image-invariant across ten settings</span></div>
    <div class="evidence-card"><strong>59%</strong><span>reduction in pairwise flips from targeted LoRA—with a grounding tradeoff</span></div>
  </div>
</section>

<section class="editorial-section" aria-labelledby="contributions-title">
  <div class="editorial-section__header">
    <div>
      <p class="editorial-kicker">Research arc</p>
      <h2 id="contributions-title">Measure. Diagnose. Mitigate. Audit. Gate.</h2>
    </div>
    <p>This work is conducted in the <a href="https://sail-lab.org/">SAIL Lab</a> at the University of New Haven under the supervision of <a href="https://vbehzadan.com">Dr. Vahid Behzadan</a>.</p>
  </div>
  <div class="finding-grid">
    <article class="finding-card">
      <span class="finding-card__index">01 · MEASUREMENT</span>
      <h3>PSF-Med exposes wording-driven diagnosis flips.</h3>
      <p>The benchmark pairs 26,850 chest X-ray questions from three countries with clinically equivalent paraphrases. It tests whether the answer changes when the meaning and image do not.</p>
    </article>
    <article class="finding-card">
      <span class="finding-card__index">02 · DIAGNOSIS</span>
      <h3>Consistency is not evidence that the image was used.</h3>
      <p>Controlled image-removal and image-swap tests show that the most consistent backends can be the least image-dependent. A stable answer can still be driven by the question alone.</p>
    </article>
    <article class="finding-card">
      <span class="finding-card__index">03 · MITIGATION</span>
      <h3>A targeted repair works—but the mechanistic account remains bounded.</h3>
      <p>Candidate sparse-autoencoder features localize where the failure is expressed, while a LoRA on layers 15–19 touches 0.1% of parameters and cuts pairwise flips about 59%. A controlled replica also shows that broadening training phrasing can reduce held-out wording sensitivity, identifying training coverage as a causal lever.</p>
    </article>
    <article class="finding-card">
      <span class="finding-card__index">04 · SAFETY</span>
      <h3>Improved consistency can create false reassurance.</h3>
      <p>Across ten model–dataset settings, a mean of 81% of consistent predictions are unchanged when the image is removed. The adapters also lean harder on question text, so better consistency does not automatically mean safer grounding.</p>
    </article>
    <article class="finding-card">
      <span class="finding-card__index">05 · DEPLOYMENT</span>
      <h3>Uncertainty can rank risk, but it cannot certify grounding.</h3>
      <p>For Targeted LoRA on the PadChest flip bank, single-pass predictive entropy ranks paraphrase flips (AUROC 0.823) and errors (0.862). The proposed gate remains an offline readiness audit: it favors text-answerable cases, its region term needs radiologist boxes, and no single internal monitor transfers across model families.</p>
    </article>
  </div>
</section>

<section class="editorial-section" aria-labelledby="outputs-title">
  <div class="editorial-section__header">
    <div>
      <p class="editorial-kicker">Selected outputs</p>
      <h2 id="outputs-title">The dissertation, in papers.</h2>
    </div>
    <p>Benchmarks, mechanistic evidence, targeted interventions, and deployment-facing safety analysis.</p>
  </div>
  <div class="publication-grid">
    {% assign selected_urls = "/publication/2026-trustworthiness-scoping-review,/publication/2026-psf-med,/publication/2026-mechanistic-lora,/publication/2026-consistent-but-dangerous,/publication/2026-predictive-entropy,/publication/2026-attention-without-grounding" | split: "," %}
    {% for selected_url in selected_urls %}
      {% assign selected_post = site.publications | where: "permalink", selected_url | first %}
      {% if selected_post %}{% include publication-card.html post=selected_post %}{% endif %}
    {% endfor %}
  </div>
</section>

<section class="editorial-section resource-panel" aria-label="Open research resources">
  <div>
    <h3>Read the final work and inspect the evidence.</h3>
    <p>The final 203-page dissertation, its executive summary, defense slides, evidence explorer, and reproducibility materials are available in the companion site. PSF-Med releases questions, paraphrases, and audit verdicts—not medical images.</p>
  </div>
  <div class="editorial-actions">
    <a class="editorial-action editorial-action--primary" href="/phd-thesis/read/">Final dissertation</a>
    <a class="editorial-action" href="/phd-thesis/assets/defense-slides.pdf">Defense slides</a>
    <a class="editorial-action" href="https://github.com/UNHSAILLab/psf-med">Code &amp; benchmark</a>
  </div>
</section>
