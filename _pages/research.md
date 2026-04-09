---
layout: single
permalink: /research/
title: "Research"
author_profile: true
---

I am conducting this dissertation research in the [Secure and Assured Intelligent Learning Lab (SAIL Lab)](https://sail-lab.org/) at the University of New Haven under the supervision of [Dr. Vahid Behzadan](https://vbehzadan.com).

My dissertation investigates robustness, safety, and interpretability failures in medical Vision-Language Models (VLMs). The central finding is that models that appear reliable by standard metrics are often exploiting text shortcuts rather than analyzing the medical image. A model can achieve near-perfect consistency while ignoring the chest X-ray entirely.

## Interactive failure gallery

I have also published a poster-friendly interactive gallery with representative PSF-Med failure cases. It shows how semantically equivalent clinical questions can trigger contradictory answers on the same chest X-ray while suppressing raw image filenames and internal example IDs.

<p><a class="btn btn--info btn--large" href="{{ '/psf-med-failures/' | relative_url }}">Open the interactive PSF-Med gallery</a></p>

## Key contributions

- **PSF-Med**: A benchmark of 82,234 paraphrase pairs across six VLMs showing that rephrasing a clinical question can flip a diagnostic answer up to 54% of the time.
- **Consistency-Safety Paradox**: Demonstrating that the most consistent models are the most text-reliant, creating a false sense of safety (`r = -0.89`).
- **Mechanistic Diagnosis**: Using Sparse Autoencoders to identify a single "formality gate" feature that mediates 67% of flip failures, enabling targeted `0.1%`-parameter LoRA repair.
- **Deployment Audits**: Showing that selective-prediction rules raise accuracy to 97% by selecting text-answerable cases, not image-grounded ones, across three architecture families.

## Publications

- **PSF-Med: Measuring and Explaining Paraphrase Sensitivity in Medical Vision-Language Models**  
  B. Sadanandan, V. Behzadan. Under review, 2026.  
  [arXiv:2602.21428](https://arxiv.org/abs/2602.21428)

- **Mechanistically Guided LoRA Improves Paraphrase Consistency in Medical Vision-Language Models**  
  B. Sadanandan, V. Behzadan. Under review, 2026.  
  [arXiv:2603.00148](https://arxiv.org/abs/2603.00148)

- **Consistent but Dangerous: Per-Sample Safety Classification Reveals False Reliability in Medical VLMs**  
  B. Sadanandan, V. Behzadan. *CVPR MedReasoner Workshop*, 2026.  
  [arXiv:2603.20985](https://arxiv.org/abs/2603.20985)

- **VSF-Med: A Vulnerability Scoring Framework for Medical Vision-Language Models**  
  B. Sadanandan, V. Behzadan. *IEEE ISBI*, 2026. Poster.  
  [arXiv:2507.00052](https://arxiv.org/abs/2507.00052)

- **When Chain-of-Thought Backfires: Evaluating Prompt Sensitivity in Medical Language Models**  
  B. Sadanandan, V. Behzadan. *2nd International Conference on Applied Artificial Intelligence (2AI)*, 2026.

- **Predictive Entropy Links Calibration and Paraphrase Sensitivity in Medical VLMs**  
  B. Sadanandan, V. Behzadan. Under review, 2026.

- **Attention Without Grounding: Safety Evaluation of Visual Explanations in Medical VLMs**  
  B. Sadanandan, V. Behzadan. Under review, 2026.

- **Consistency Is Not Safety: Family-Specific Deployment Audits for Medical VLMs**  
  B. Sadanandan, V. Behzadan. Under review, 2026.


## Datasets & Code

- [**PSF-Med Benchmark**](https://github.com/UNHSAILLab/medical-vlm-robustness): 82K paraphrase pairs, six VLMs, and three chest X-ray datasets: MIMIC-CXR, PadChest, and VinDr-CXR.
- **Models**: Base, targeted LoRA, and full LoRA checkpoints on Hugging Face.

## News

- **Apr 2026**: Presenting PSF-Med poster at SMLM, Yale.
- **Apr 2026**: VSF-Med poster accepted at IEEE ISBI 2026.
- **Apr 2026**: Chain-of-Thought paper accepted at 2AI 2026.
- **Mar 2026**: CVPR MedReasoner Workshop paper accepted.
- **Feb 2026**: Dissertation first draft complete (6 chapters).
