---
layout: page
title: Research
permalink: /research/
description: My research focuses on enhancing the robustness of vision-language models in healthcare
nav: true
nav_order: 3
---

# Robustness of Vision-Language Models in Healthcare

## Research Overview

My Ph.D. research at the University of New Haven's Secure and Assured Intelligent Learning Lab (SAIL Lab) focuses on understanding and improving the robustness of Vision-Language Models (VLMs) in healthcare applications. As these models become increasingly integrated into clinical workflows, ensuring their reliability, safety, and resilience against various forms of attacks and failures is paramount.

## VSF-Med: Visual Semantic Fingerprinting for Medical VLMs

A key component of my research is the development of VSF-Med, a comprehensive framework for evaluating and enhancing the robustness of medical vision-language models. This work addresses critical vulnerabilities in how VLMs process and interpret medical imagery, particularly in the presence of adversarial perturbations.

### Core Research Areas

#### 1. Adversarial Robustness
Understanding how VLMs respond to various forms of visual attacks and developing defense mechanisms:
- **Attack Taxonomy**: Comprehensive categorization of visual attacks including noise-based, pattern-based, and semantic attacks
- **Vulnerability Assessment**: Systematic evaluation of model weaknesses across different attack vectors
- **Defense Strategies**: Multi-layered defense approaches combining detection, preprocessing, and architectural modifications

#### 2. Semantic Understanding
Investigating how VLMs maintain semantic consistency in medical interpretations:
- Analysis of feature representations across different layers
- Cross-modal alignment between visual and textual understanding
- Semantic drift detection in the presence of perturbations

#### 3. Multimodal Robustness
Leveraging multiple data modalities to enhance model reliability:
- Integration of complementary medical data (imaging, ECG, lab values)
- Cross-modal verification mechanisms
- Context-aware defense strategies

## Technical Approach

### Visual Attack Framework
My research investigates six primary attack categories that threaten medical VLMs:

- **Noise-based Attacks**: Gaussian noise, salt-and-pepper noise, and other statistical perturbations
- **Pattern-based Attacks**: Checkerboard overlays, Moiré patterns, and structured artifacts
- **Semantic Attacks**: Targeted modifications that alter clinical interpretations
- **Steganographic Attacks**: Hidden information embedding that compromises model integrity
- **Frequency-domain Attacks**: Manipulations in transformed spaces
- **Bit-level Attacks**: LSB modifications and quantization-based perturbations

### Defense Methodology

The defense framework operates at multiple levels:

#### Detection Layer
- Deep learning classifiers for attack identification
- Anomaly detection in feature spaces
- Statistical analysis of input characteristics

#### Preprocessing Layer
- Adaptive filtering based on detected attack types
- Frequency domain cleaning
- Spatial domain restoration techniques

#### Model Layer
- Adversarial training protocols
- Robust attention mechanisms
- Defensive distillation approaches

#### Interpretation Layer
- Explainable AI techniques for vulnerability identification
- Attention-guided defense mechanisms
- Feature attribution analysis

## Experimental Framework

### Datasets and Models
- **Primary Dataset**: Symile-MIMIC multimodal clinical dataset
- **Target Models**: ChexAgent, LLaVA-Rad, and adapted foundation models
- **Evaluation Metrics**: Robustness scores, semantic preservation, clinical accuracy

### Key Research Questions
1. How do different visual perturbations affect the clinical accuracy of medical VLMs?
2. Can multimodal information provide effective defense against adversarial attacks?
3. What architectural modifications enhance inherent model robustness?
4. How can we maintain interpretability while improving security?

## Collaborations

This research is conducted under the supervision of Dr. Vahid Behzadan at the SAIL Lab, with collaborations across medical AI and security research communities.

## Project Resources

- **VSF-Med Project**: [https://unhsaillab.github.io/VSF-Med/](https://unhsaillab.github.io/VSF-Med/)
- **SAIL Lab**: Secure and Assured Intelligent Learning Lab, University of New Haven

---

*For more details about my research or potential collaborations, please [contact me](mailto:mail@bineshkumar.me).*