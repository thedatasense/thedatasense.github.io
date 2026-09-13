---
layout: single
permalink: /research/
title: "Research"
author_profile: true
---

I conducted this dissertation research in the [Secure and Assured Intelligent Learning Lab (SAIL Lab)](https://sail-lab.org/) at the University of New Haven under the supervision of [Dr. Vahid Behzadan](https://vbehzadan.com). I successfully defended the dissertation on August 26, 2026.

My dissertation, *Paraphrase Sensitivity in Medical Vision-Language Models: Measurement, Mechanisms, Mitigation, and Deployment Safety*, investigates robustness, safety, and interpretability failures in medical Vision-Language Models (VLMs). Its central finding is that a low paraphrase-flip rate is not sufficient evidence of reliable visual reasoning: models that appear reliable by standard metrics may be exploiting text shortcuts rather than analyzing the medical image.

## Interactive failure gallery

I have also published a poster-friendly interactive gallery with representative failure cases from PSF-Med, my paraphrase sensitivity benchmark. It shows how semantically equivalent clinical questions can trigger contradictory answers on the same chest X-ray while suppressing raw image filenames and internal example IDs.

<p><a class="btn btn--info btn--large" href="/phd-thesis/read/">Read the final dissertation</a> <a class="btn btn--inverse btn--large" href="/psf-med-failures/">Open the failure gallery</a></p>

## Key contributions

Every number below is traceable to a chapter, a sample size, and a source file in the [dissertation companion](/phd-thesis/).

| Contribution | What I found |
|---|---|
| **PSF-Med** | A benchmark of 92,856 final evaluation pairs, built from 26,850 chest X-ray questions across three countries. On the binary yes/no subset, six medical VLMs flip on 6.4% to 54.7% of pairs. |
| **Consistency is not safety** | Averaged across ten model-dataset settings, 81% of each model's consistent predictions are image-invariant: the answer does not change when I remove the image. A model can look reliable and still be reading only the question. |
| **Mechanistic diagnosis** | Sparse Autoencoders point to Feature 3818 at layer 17 as a clinical-query operator gate, and the answer commits at layer 16. This is a candidate account, not a proven circuit: the feature is the largest layer-17 delta in 37 of 76 operator-preserving flips, and ablating it alone restores the original answer in only 6 of them. |
| **Targeted repair and causal probe** | A Low-Rank Adaptation (LoRA) on layers 15 to 19, touching 0.1% of parameters, cuts the pairwise flip rate by about 59% (8.5% to 3.5% over five seeds) on a patient-disjoint test, with no observed accuracy reduction. It buys that consistency by leaning harder on the question text. In a controlled replica, broader training-phrasing coverage reduces held-out wording sensitivity, identifying training coverage as a causal lever. |
| **Deployment audits** | For Targeted LoRA on the PadChest flip bank, single-pass predictive entropy ranks paraphrase flips at AUROC 0.823 and errors at 0.862. The gate remains an offline readiness audit: it admits text-answerable cases over grounded ones, and no single internal monitor transfers across model families. |

## Publications

Browse the [full publication list](/publications/) for papers, preprints, and patents. Selected dissertation publications follow.

- **Trustworthiness Evaluation of Medical Vision-Language Models: A Scoping Review of Robustness, Grounding, Hallucination, and Uncertainty**<br>
  B. Sadanandan, A. Karimi, B. Upadhayay, V. Behzadan. *JMIR AI preprint; manuscript under review*, 2026.<br>
  [JMIR preprint](https://preprints.jmir.org/preprint/102330)

- **PSF-Med: A Clinician-Audited Benchmark for Paraphrase Sensitivity in Medical Vision-Language Models**<br>
  B. Sadanandan, V. Behzadan, L. Jayan, A. G. Kurup. *MMFM-BIOMED Workshop, CVPR*, 2026.<br>
  [arXiv:2602.21428](https://arxiv.org/abs/2602.21428)

- **Mechanistically Guided LoRA Improves Paraphrase Consistency in Medical Vision-Language Models**<br>
  B. Sadanandan, V. Behzadan. *CHIL*, 2026.<br>
  [arXiv:2603.00148](https://arxiv.org/abs/2603.00148)

- **Consistent but Dangerous: Per-Sample Safety Classification Reveals False Reliability in Medical Vision-Language Models**<br>
  B. Sadanandan, V. Behzadan. *CVPR MedReasoner Workshop*, 2026.<br>
  [arXiv:2603.20985](https://arxiv.org/abs/2603.20985)

- **Predictive Entropy as a Joint Screen for Error and Paraphrase Instability in Medical Vision-Language Models**<br>
  B. Sadanandan, V. Behzadan. *UNSURE Workshop, MICCAI*, 2026. Poster.<br>
  [Paper](/phd-thesis/assets/papers/predictive-entropy.pdf)

- **Attention Without Grounding: Causal Evaluation of Visual Explanations in Medical VLMs**<br>
  B. Sadanandan, V. Behzadan. *iMIMIC Workshop, MICCAI*, 2026.<br>
  [arXiv:2607.18577](https://arxiv.org/abs/2607.18577)


## Datasets & Code

See the [project portfolio](/portfolio/) for applied work and the [dissertation companion](/phd-thesis/) for the thesis and reproducibility materials.

- [**PSF-Med Benchmark**](https://github.com/UNHSAILLab/psf-med): 92,856 final evaluation pairs, six VLMs, and three chest X-ray datasets: MIMIC-CXR, PadChest, and VinDr-CXR. The release carries questions, paraphrases, and audit verdicts, not images.
- [**PSF-Med Dataset**](https://huggingface.co/datasets/saillab/psf-med): public questions, paraphrases, and audit verdicts.
- [**Targeted LoRA code and models**](https://github.com/UNHSAILLab/medical-vlm-paraphrase-consistency): training, evaluation, and adapter resources for the mitigation study.

## News

- **Aug 2026**: Successfully defended the Ph.D. dissertation on August 26; final dissertation published on August 28.
- **2026**: Predictive Entropy accepted as a poster at the UNSURE Workshop, MICCAI 2026.
- **2026**: Attention Without Grounding accepted at the iMIMIC Workshop, MICCAI 2026.
- **2026**: PSF-Med accepted at the MMFM-BIOMED Workshop, CVPR 2026.
- **Apr 2026**: PSF-Med poster at SMLM, Yale.
- **Apr 2026**: Mechanistically Guided LoRA Improves Paraphrase Consistency accepted at CHIL 2026.
- **Mar 2026**: Chain-of-Thought paper accepted at 2AI 2026.
- **Mar 2026**: Consistent but Dangerous, CVPR 2026 MedReasoner paper accepted.
- **Feb 2026**: VSF-Med poster accepted at IEEE ISBI 2026.
