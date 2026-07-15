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

<p><a class="btn btn--info btn--large" href="/phd-thesis/">Open the PhD dissertation companion</a> <a class="btn btn--inverse btn--large" href="/phd-thesis/cases/">Open the failure gallery</a></p>

## Key contributions

Every number below is traceable to a chapter, a sample size, and a source file in the [dissertation companion](/phd-thesis/).

| Contribution | What I found |
|---|---|
| **PSF-Med** | A benchmark of 92,856 audited question-paraphrase pairs, built from 26,850 chest X-ray questions across three countries. On the binary yes/no subset, six medical VLMs flip on 6.4% to 54.7% of pairs. |
| **Consistency is not safety** | Averaged across ten model-dataset settings, 81% of each model's consistent predictions are image-invariant: the answer does not change when I remove the image. A model can look reliable and still be reading only the question. |
| **Mechanistic diagnosis** | Sparse Autoencoders point to Feature 3818 at layer 17 as a clinical-query operator gate, and the answer commits at layer 16. This is a candidate account, not a proven circuit: the feature is the largest layer-17 delta in 37 of 76 operator-preserving flips, and ablating it alone restores the original answer in only 6 of them. |
| **Targeted repair** | A LoRA on layers 15 to 19, touching 0.1% of parameters, cuts the pairwise flip rate by about 59% (8.5% to 3.5% over five seeds) on a patient-disjoint test, with no observed accuracy reduction. It buys that consistency by leaning harder on the question text, so it does not preserve visual grounding. |
| **Deployment audits** | Offline audit rules admit 33% of PadChest cases at 96.8% accuracy, but they admit the cases a text prior already answers. On the slice where the image is needed, the same model scores 2.9%. No single internal monitor transfers across model families. |

## Publications

- **PSF-Med: Measuring and Explaining Paraphrase Sensitivity in Medical Vision-Language Models**  
  B. Sadanandan, V. Behzadan. Under review, 2026.  
  [arXiv:2602.21428](https://arxiv.org/abs/2602.21428)

- **Mechanistically Guided LoRA Improves Paraphrase Consistency in Medical Vision-Language Models**  
  B. Sadanandan, V. Behzadan. *CHIL*, 2026.  
  [arXiv:2603.00148](https://arxiv.org/abs/2603.00148)

- **Consistent but Dangerous: Per-Sample Safety Classification Reveals False Reliability in Medical VLMs**  
  B. Sadanandan, V. Behzadan. *CVPR MedReasoner Workshop*, 2026.  
  [arXiv:2603.20985](https://arxiv.org/abs/2603.20985)

- **VSF-Med: A Vulnerability Scoring Framework for Medical Vision-Language Models**  
  B. Sadanandan, V. Behzadan. *IEEE ISBI*, 2026. Poster.  
  [arXiv:2507.00052](https://arxiv.org/abs/2507.00052)

- **When Chain-of-Thought Backfires: Evaluating Prompt Sensitivity in Medical Language Models**  
  B. Sadanandan, V. Behzadan. *2nd International Conference on Applied Artificial Intelligence (2AI)*, 2026.  
  [arXiv:2603.25960](https://arxiv.org/abs/2603.25960)

- **Predictive Entropy Links Calibration and Paraphrase Sensitivity in Medical VLMs**  
  B. Sadanandan, V. Behzadan. Under review, 2026.

- **Attention Without Grounding: Safety Evaluation of Visual Explanations in Medical VLMs**  
  B. Sadanandan, V. Behzadan. Under review, 2026.

- **Consistency Is Not Safety: Family-Specific Deployment Audits for Medical VLMs**  
  B. Sadanandan, V. Behzadan. Under review, 2026.


## Datasets & Code

- [**PSF-Med Benchmark**](https://github.com/UNHSAILLab/psf-med): 92,856 audited question-paraphrase pairs, six VLMs, and three chest X-ray datasets: MIMIC-CXR, PadChest, and VinDr-CXR. The release carries questions, paraphrases, and audit verdicts, not images.
- **Models**: Base, targeted LoRA, and full LoRA checkpoints on Hugging Face.

## News

- **Apr 2026**: PSF-Med poster at SMLM, Yale.
- **Apr 2026**: Mechanistically Guided LoRA Improves Paraphrase Consistency accepted at CHIL 2026.
- **Mar 2026**: Chain-of-Thought paper accepted at 2AI 2026.
- **Mar 2026**: Consistent but Dangerous, CVPR 2026 MedReasoner paper accepted.
- **Feb 2026**: VSF-Med poster accepted at IEEE ISBI 2026.
