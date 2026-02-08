---
title: "VSF-Med - Vulnerability Scoring Framework for Medical Vision-Language Models"
excerpt: "A comprehensive framework for evaluating security vulnerabilities in medical AI systems"
collection: portfolio
permalink: /portfolio/vsf-med/
header:
  teaser: images/4.jpg
---

As medical institutions increasingly adopt Vision-Language Models (VLMs) for clinical decision support, understanding and mitigating their security vulnerabilities becomes critical. This research introduces VSF-Med, a comprehensive vulnerability scoring framework designed specifically for evaluating the robustness of medical AI systems against adversarial attacks.

The framework addresses the unique challenges posed by the integration of visual and textual modalities in medical AI, where subtle manipulations can lead to potentially dangerous misdiagnoses or inappropriate treatment recommendations.

### Research Scope

VSF-Med provides a systematic approach to evaluate vulnerabilities in medical VLMs through three key components:

- **Text-prompt attack templates**: Designed to test the model's resilience against malicious or misleading textual inputs
- **Imperceptible visual perturbations**: Subtle modifications to medical images that can deceive AI systems while remaining invisible to human observers
- **Eight-dimensional risk assessment rubric**: A comprehensive scoring system that evaluates multiple aspects of model vulnerability

Our evaluation synthesized over 30,000 adversarial variants from 5,000 radiology images, providing a thorough assessment of current medical AI systems' security posture.

### Key Findings

The research revealed varying levels of vulnerability across different state-of-the-art models:

- Models like Llama-3.2-11B-Vision-Instruct and GPT-4o demonstrated different susceptibility patterns to adversarial attacks
- Certain attack vectors proved more effective in medical contexts compared to general-purpose applications
- The multimodal nature of medical VLMs introduces unique vulnerability surfaces not present in text-only or vision-only models

### Impact and Applications

This framework enables:

- Healthcare institutions to assess the security risks of deploying AI systems in clinical settings
- AI developers to identify and address vulnerabilities during the development phase
- Regulatory bodies to establish security standards for medical AI systems
- Researchers to benchmark and improve the robustness of medical VLMs

### Team Members

- Binesh Sadanandan
- Dr. Vahid Behzadan

### Publications

Sadanandan, B., Behzadan, V. (2025). "VSF-Med: A Vulnerability Scoring Framework for Medical Vision-Language Models." arXiv preprint [arXiv:2507.00052](https://arxiv.org/abs/2507.00052).
