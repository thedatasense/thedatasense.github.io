---
title: "Mechanistically Guided LoRA Improves Paraphrase Consistency in Medical Vision-Language Models"
collection: publications
pub_type: conferences
permalink: /publication/2026-mechanistic-lora
excerpt: "Sparse-autoencoder interpretability points to the layers that drive paraphrase flips; a targeted LoRA on those layers cuts the flip rate while touching 0.1% of parameters."
date: 2026-04-10
venue: "CHIL 2026"
paperurl: "https://arxiv.org/abs/2603.00148"
citation: "Sadanandan, B., & Behzadan, V. (2026). Mechanistically Guided LoRA Improves Paraphrase Consistency in Medical Vision-Language Models. <i>CHIL 2026</i>."
---

[arXiv](https://arxiv.org/abs/2603.00148)

We use sparse-autoencoder interpretability to locate the layers where a medical Vision-Language Model (VLM) commits to an answer, then apply a Low-Rank Adaptation (LoRA) on layers 15 to 19, touching 0.1% of parameters. On a patient-disjoint test the pairwise flip rate drops by about 59% (8.5% to 3.5% over five seeds) with no observed accuracy reduction.
