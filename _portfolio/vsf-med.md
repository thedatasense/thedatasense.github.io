---
title: "VSF-Med - Vulnerability Scoring Framework for Medical Vision-Language Models"
excerpt: "A framework for scoring security vulnerabilities in medical AI systems"
collection: portfolio
permalink: /portfolio/vsf-med/
header:
  teaser: images/4.jpg
---

As medical institutions adopt Vision-Language Models (VLMs) for clinical decision support, understanding and mitigating their security vulnerabilities becomes urgent. We built VSF-Med, a vulnerability scoring framework for evaluating the robustness of medical AI systems against adversarial attacks.

The framework addresses the unique challenges posed by the integration of visual and textual modalities in medical AI, where subtle manipulations can lead to potentially dangerous misdiagnoses or inappropriate treatment recommendations.

### Research Scope

VSF-Med evaluates vulnerabilities in medical VLMs through three components:

| Component | What it does |
|---|---|
| Text-prompt attack templates | Test the model's resilience against malicious or misleading textual inputs |
| Imperceptible visual perturbations | Subtle modifications to medical images that deceive AI systems while remaining invisible to human observers |
| Eight-dimensional risk rubric | A scoring system that covers eight distinct aspects of model vulnerability |

We synthesized over 30,000 adversarial variants from 5,000 radiology images to assess the security posture of current medical AI systems.

### Key Findings

We found that current models fail in different ways. Llama-3.2-11B-Vision-Instruct and GPT-4o showed distinct susceptibility patterns to adversarial attacks, and certain attack vectors proved more effective in medical contexts than in general-purpose applications. The multimodal nature of medical VLMs also introduces vulnerability surfaces that text-only or vision-only models simply don't have.

### Impact and Applications

| Audience | What VSF-Med gives them |
|---|---|
| Healthcare institutions | A way to assess the security risks of deploying AI systems in clinical settings |
| AI developers | A method to find and fix vulnerabilities during development |
| Regulatory bodies | A basis for security standards for medical AI systems |
| Researchers | A benchmark for improving the robustness of medical VLMs |

### Team Members

- Binesh Sadanandan
- Dr. Vahid Behzadan

### Publications

Sadanandan, B., Behzadan, V. (2025). "VSF-Med: A Vulnerability Scoring Framework for Medical Vision-Language Models." arXiv preprint [arXiv:2507.00052](https://arxiv.org/abs/2507.00052).
