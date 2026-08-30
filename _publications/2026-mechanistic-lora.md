---
title: "Mechanistically Guided LoRA Improves Paraphrase Consistency in Medical Vision-Language Models"
collection: publications
pub_type: conferences
permalink: /publication/2026-mechanistic-lora
excerpt: "Sparse-autoencoder and residual-stream analyses identify candidate mechanisms for paraphrase flips; a targeted LoRA cuts the flip rate while touching 0.1% of parameters."
date: 2026-04-10
venue: "Conference on Health, Inference, and Learning (CHIL) 2026"
paperurl: "https://arxiv.org/abs/2603.00148"
citation: "Sadanandan, B., & Behzadan, V. (2026). Mechanistically guided LoRA improves paraphrase consistency in medical vision-language models. <i>Conference on Health, Inference, and Learning (CHIL) 2026</i>. arXiv:2603.00148."
---

[arXiv](https://arxiv.org/abs/2603.00148)

We use sparse-autoencoder interpretability to identify candidate features and the layers where a medical Vision-Language Model (VLM) commits to an answer, then apply a Low-Rank Adaptation (LoRA) on layers 15 to 19, touching 0.1% of parameters. On a patient-disjoint test the pairwise flip rate drops by about 59% (8.5% to 3.5% over five seeds) with no observed accuracy reduction. A safety re-audit finds that the adapter gains consistency by relying more heavily on question text, so lower flip rates do not imply better visual grounding.
