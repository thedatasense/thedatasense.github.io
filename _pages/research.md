---
layout: single
permalink: /research/
title: "Research"
author_profile: true
---

## Problem Statement

Medical Vision-Language Models (VLMs) achieve 85-95% accuracy on benchmarks, yet this high performance masks a critical safety gap: **Phrasing-Sensitive Failures (PSF)**. These models produce contradictory clinical assessments for semantically equivalent questions---answering "Is the heart size normal?" with "Yes" while responding "Is there cardiomegaly?" with "Yes, enlarged" for the same image.

Compounding this, the **Misleading Explanation Effect (MEE)** causes standard faithfulness metrics to paradoxically rate incorrect predictions as more interpretable than correct ones. Together, PSF and MEE undermine the primary mechanisms clinicians use to assess AI reliability, creating dangerous blind spots in clinical deployment.

---

## Dissertation Research

**Clinically Robust Vision-Language Models for Diagnostic Applications:**
*Measuring, Understanding, and Mitigating Phrasing-Sensitive Failures*

Under the advisement of [Dr. Vahid Behzadan](https://sail-lab.org/) at the [Secure and Assured Intelligent Learning Lab (SAIL Lab)](https://unhsaillab.github.io/), University of New Haven.

---

## Key Research Questions

1. **Prevalence**: How prevalent is PSF across different pathology types and linguistic phenomena (negation, synonyms, hedging)?

2. **Mechanism**: Which layers, attention heads, and fusion pathways are causally responsible for phrasing sensitivity?

3. **Mitigation**: Can targeted LoRA-based interventions reduce PSF by 50%+ while maintaining diagnostic accuracy?

4. **Deployment**: How should safety thresholds be calibrated for different clinical workflows (triage, critical alerts, reporting)?

---

## Research Thrusts

### Thrust 1: Measuring PSF and MEE

Development of the **VSF-Med Benchmark**---2,500+ paraphrased questions across 5 chest X-ray pathologies (cardiomegaly, pleural effusion, pneumothorax, consolidation, atelectasis) with linguistic phenomenon annotations.

**Novel Metrics:**
- **Paraphrase Flip Rate (PFR)**: Proportion of semantically equivalent question pairs yielding contradictory answers
- **Attention Stability Index (ASI)**: Cosine similarity of attention maps across paraphrases
- **Misleading Explanation Effect Coefficient (MEEC)**: Difference in faithfulness scores between incorrect vs. correct predictions

**Preliminary Findings**: 18-28% PFR observed in MedGemma and LLaVA-Rad with stable attention (ASI > 0.85), confirming visual-linguistic decoupling.

### Thrust 2: Causal Analysis

Localizing PSF origins through:
- **Activation patching** to identify layers with high Causal Importance Scores (CIS > 0.5)
- **Token ablation** to measure necessity/sufficiency of linguistic elements
- **Decomposed attention analysis** to characterize visual-text fusion stability

**Hypothesis**: PSF arises when paraphrases perturb fusion pathways more than visual evidence, while MEE occurs when attention-output coupling is weak.

### Thrust 3: Robustness Interventions

Targeted **LoRA-based fine-tuning** on causally-identified layers with a combined training objective:

- **Task loss**: Cross-entropy for correctness
- **Consistency loss**: KL divergence penalizing distributional disagreement across paraphrases
- **Representation loss**: Cosine alignment of embeddings for equivalent questions

**Target**: 50%+ PFR reduction, MEEC towards 0, with <1% additional parameters.

### Thrust 4: Clinical Safety Framework

Risk-stratified deployment protocols including:
- Real-time paraphrase probing and consistency scoring
- Abstention triggers for high-PSF cases
- Uncertainty communication with calibrated confidence and PSF risk indicators
- Radiologist validation studies (N=10-15)

---

## Datasets & Models

**Imaging Datasets**: MIMIC-CXR (377K images), CheXpert (224K images), VinDr-CXR (18K images)

**Target Models**: MedGemma-4b-it, LLaVA-Rad

**Focus Pathologies**: Cardiomegaly, Pleural Effusion, Pneumothorax, Consolidation/Pneumonia, Atelectasis

---

## GitHub Repositories

### Dissertation Research
- [robust-med-mllm-experiments](https://github.com/thedatasense/robust-med-mllm-experiments) --- Robustness experiments for medical multimodal LLMs
- [medical-vlm-intepret](https://github.com/thedatasense/medical-vlm-intepret) --- Interpretability tools for medical VLMs

### Medical VLM Implementations
- [LLaVA-Med](https://github.com/thedatasense/LLaVA-Med) --- Large Language and Vision Assistant for biomedicine
- [CheXagent](https://github.com/thedatasense/CheXagent) --- Chest X-ray analysis agent
- [CARES](https://github.com/thedatasense/CARES) --- Clinical AI reasoning and evaluation

---

## Publications

**Sadanandan, B.**, Behzadan, V. (2025). "VSF-Med: A Vulnerability Scoring Framework for Medical Vision-Language Models." *arXiv preprint* [arXiv:2507.00052](https://arxiv.org/abs/2507.00052)

**Sadanandan, B.**, Behzadan, V. (2025). "Promise of Data-Driven Modeling and Decision Support for Precision Oncology and Theranostics." *arXiv preprint* [arXiv:2505.09899](https://arxiv.org/abs/2505.09899)

**Sadanandan, B.**, Arghavani Nobar, B., Behzadan, V. (2025). "Comparative Study of Generative Models for Early Detection of Failures in Medical Devices." *arXiv preprint* [arXiv:2505.04845](https://arxiv.org/abs/2505.04845)

[Google Scholar Profile](https://scholar.google.com/citations?user=YgIIscgAAAAJ&hl=en)

---

## Collaborators

- **[Dr. Vahid Behzadan](https://sail-lab.org/)** --- Dissertation Advisor, SAIL Lab Director
- **[SAIL Lab](https://unhsaillab.github.io/)** --- Secure and Assured Intelligent Learning Lab, University of New Haven

---

## Contact

For research inquiries or collaboration opportunities: [LinkedIn](https://www.linkedin.com/in/bineshk) | contact(at)bineshkumar(dot)me
