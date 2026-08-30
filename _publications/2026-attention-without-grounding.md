---
title: "Attention Without Grounding: Causal Evaluation of Visual Explanations in Medical VLMs"
collection: publications
pub_type: conferences
permalink: /publication/2026-attention-without-grounding
excerpt: "Attention maps can look convincing while playing no causal role in the answer. We test whether visual explanations in medical VLMs actually reflect what the model uses."
date: 2026-07-01
venue: "iMIMIC Workshop, MICCAI 2026"
paperurl: "https://arxiv.org/abs/2607.18577"
citation: "Sadanandan, B., & Behzadan, V. (2026). Attention Without Grounding: Causal Evaluation of Visual Explanations in Medical VLMs. <i>iMIMIC Workshop, MICCAI 2026</i>."
---

[arXiv](https://arxiv.org/abs/2607.18577) | [Code and data instructions](https://github.com/thedatasense/medicalvlm_attention_without_grounding)

Saliency and attention maps are often offered as evidence that a medical Vision-Language Model (VLM) looked at the right region. Bounding-box coverage, patch-rank agreement with occlusion, and region-based causal scoring show that attention only marginally beats a shifted box and does not track causal patch importance. Attention is a coarse localizer, short of a faithful explanation, and should not be treated as safety evidence.
