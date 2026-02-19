---
layout: single
permalink: /research/
title: "Research"
author_profile: true
---

My research focuses on the robustness and safety of medical Vision-Language Models (VLMs) for clinical deployment. I work under [Dr. Vahid Behzadan](https://sail-lab.org/) at the [SAIL Lab](https://unhsaillab.github.io/), University of New Haven.

---

## Clinically Robust Vision-Language Models for Diagnostic Applications

Medical VLMs achieve strong benchmark accuracy but suffer from **Paraphrase Sensitivity Failures (PSFs)**: they produce contradictory diagnoses for semantically equivalent questions phrased differently. This is a critical safety gap since clinicians naturally vary how they phrase queries.

We studied six medical VLMs across 19,748 questions with ~92,000 paraphrases on chest X-ray datasets (MIMIC-CXR, PadChest). Flip rates ranged from 8% to 58% depending on the model and dataset. Negation paraphrases universally triggered 32-52% flip rates---the most dangerous failure pattern for clinical use.

**Why models flip:** Models that flip demonstrably ignore the image. Flip cases show 41% less attention to pathology regions compared to consistent cases. Some models achieve low flip rates simply by ignoring images entirely and relying on language priors.

**Mechanistic findings:** Using sparse autoencoders on MedGemma-4B, we identified a single feature (Feature 3818, layer 17) that acts as a clinical query formality gate---mediating 28-42% of decision margin changes in flip pairs.

**Mitigation:** Targeted LoRA fine-tuning on causally-identified layers (15-19) achieved 79.5% flip rate reduction with only 0.1% parameter updates. However, we found that lower flip rates do not guarantee safer models. Full LoRA achieves 1.4% flip rate but 80.6% text-only agreement---consistency through memorization, not image analysis. Our targeted approach provides a better safety tradeoff.

**Key insight:** Paraphrase consistency is necessary but insufficient for safe deployment. A model that is consistent but ignores visual evidence may be more dangerous than one that is inconsistent but attempts image analysis. This work bridges robustness metrics and actual deployment safety.

---

## Datasets & Models

**Imaging Datasets**: MIMIC-CXR (377K images), CheXpert (224K images), PadChest, VinDr-CXR (18K images)

**Target Models**: MedGemma-4B, MedGemma-27B, LLaVA-Rad, and others

**Focus Pathologies**: Cardiomegaly, Pleural Effusion, Pneumothorax, Consolidation, Atelectasis

---

## GitHub Repositories

- [robust-med-mllm-experiments](https://github.com/thedatasense/robust-med-mllm-experiments) --- Robustness experiments for medical multimodal LLMs
- [medical-vlm-intepret](https://github.com/thedatasense/medical-vlm-intepret) --- Interpretability tools for medical VLMs
- [LLaVA-Med](https://github.com/thedatasense/LLaVA-Med) --- Large Language and Vision Assistant for biomedicine
- [CheXagent](https://github.com/thedatasense/CheXagent) --- Chest X-ray analysis agent

---

## Selected Publications

**Sadanandan, B.**, Behzadan, V. (2025). "VSF-Med: A Vulnerability Scoring Framework for Medical Vision-Language Models." *IEEE ISBI 2026*. [arXiv:2507.00052](https://arxiv.org/abs/2507.00052)

**Sadanandan, B.**, Behzadan, V. (2026). "When Chain-of-Thought Backfires: Evaluating Prompt Sensitivity in Medical Language Models." *Preprint*.

**Sadanandan, B.**, Behzadan, V. (2025). "Promise of Data-Driven Modeling and Decision Support for Precision Oncology and Theranostics." [arXiv:2505.09899](https://arxiv.org/abs/2505.09899)

**Sadanandan, B.**, Arghavani Nobar, B., Behzadan, V. (2024). "Comparative Study of Generative Models for Early Detection of Failures in Medical Devices." *2024 8th International Conference on Medical and Health Informatics*.

[Full list of publications](/publications/) | [Google Scholar](https://scholar.google.com/citations?user=YgIIscgAAAAJ&hl=en)

---

## Collaborators

- **[Dr. Vahid Behzadan](https://sail-lab.org/)** --- Dissertation Advisor, SAIL Lab Director
- **[SAIL Lab](https://unhsaillab.github.io/)** --- Secure and Assured Intelligent Learning Lab, University of New Haven

---

## Contact

For research inquiries or collaboration: [LinkedIn](https://www.linkedin.com/in/bineshk) | contact(at)bineshkumar(dot)me
