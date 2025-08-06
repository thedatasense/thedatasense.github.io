---
layout: page
title: Research
permalink: /research/
description: My research focuses on developing robust defense strategies for medical vision-language models
nav: true
nav_order: 3
---

# Robust Defense Strategies for Medical Vision-Language Models

## Research Overview

My Ph.D. research at the University of New Haven's Secure and Assured Intelligent Learning Lab (SAIL Lab) focuses on developing comprehensive defense mechanisms against adversarial attacks on medical vision-language models. This work is critical for ensuring the safety and reliability of AI systems in clinical settings, where model failures could have serious consequences for patient care.

## Visual Adversarial Attacks

My research addresses six specific types of visual attacks that can compromise medical AI systems:

- **Gaussian Noise**: Random noise added at varying intensities to disrupt model predictions
- **Checkerboard Overlays**: Regular grid patterns that can confuse visual processing
- **Moiré Patterns**: Interference patterns with adjustable frequency that create visual artifacts
- **Random Arrow Artifacts**: Directional indicators strategically inserted into medical images
- **Steganographic Information Hiding**: Concealed malicious information embedded within images
- **LSB-Plane Manipulation**: Least significant bit modifications that are imperceptible to humans but affect models

## Defense Strategy Framework

I am developing and evaluating five complementary defense approaches:

### 1. Detection-Based Defenses
ML classifiers that identify attack presence and type, using CNN and Vision Transformer architectures for multi-class classification of attack types.

### 2. Preprocessing Defenses
Image filtering techniques targeting specific attack patterns:
- Wavelet denoising for Gaussian noise
- Median filtering for checkerboard patterns
- Frequency domain filtering for Moiré patterns
- Inpainting techniques for arrow artifacts
- Bit-plane randomization for steganography/LSB attacks

### 3. Model-Based Defenses
Architectural modifications including:
- Adversarial training with all attack types
- Robust attention mechanisms
- Feature denoising layers
- Attack-aware projection layers

### 4. XAI-Guided Defenses
Leveraging explainability to identify and mitigate vulnerable regions:
- Grad-CAM-based suspicious region identification
- Selective image filtering based on attention patterns
- Region-based inpainting guided by feature attribution

### 5. Multimodal Context Integration
Cross-verification using multiple data modalities:
- ECG-CXR consistency checking
- Lab value correlation with imaging findings
- Multimodal anomaly detection

## Experimental Setup

### Dataset
**Symile-MIMIC**: A multimodal clinical dataset derived from MIMIC-IV and MIMIC-CXR
- **Modalities**: Chest X-rays (CXRs), electrocardiograms (ECGs), and blood laboratory tests
- **Size**: 11,622 unique admissions from 9,573 patients
- **Structure**: Pre-defined train/validation/test splits with no patient overlap

### Target Models
- **ChexAgent (Stanford AIMI)**: Clinical reasoning agent for chest X-rays with task planning and report generation capabilities
- **LLaVA-Rad (Microsoft)**: Radiology-specific vision-language model built on CLIP visual encoder and LLaMA language model
- **Gemma**: Foundation model to be adapted for context-aware multimodal defense (CAMEL architecture)

## Research Timeline & Publications

### Current Progress (Block 1: June - Mid-July 2025)
- ✅ Implemented all six visual attack types
- ✅ Created attack parameter space with intensity levels and pattern variations
- 🔄 Generating attacked image dataset for model evaluation
- 🔄 Implementing CNN-based attack detector module

### Planned Publications

| Paper | Target Venue | Submission | Focus |
|-------|--------------|------------|-------|
| **MedVLM-Shield** | NeurIPS/ICLR/CVPR | Nov 2025 | Framework for detecting and defending against visual attacks |
| **Clinical Validation** | MIDL | Feb 2026 | Radiologist evaluation of defense effectiveness |
| **XAI-Med** | Nature Machine Intelligence | Mar 2026 | Visualization and XAI-guided defense mechanisms |
| **CAMEL** | Nature Digital Medicine | May 2026 | Multimodal context-aware defense system |
| **SecureVLM-Med** | ML4H Workshop | Jul 2026 | Unified defense framework integration |

## Clinical Validation

A key component of my research involves clinical validation with practicing radiologists to ensure the practical utility of developed defenses:

- **Participants**: 5-8 radiologists
- **Evaluation**: Defense effectiveness, diagnostic accuracy preservation, XAI explanation utility
- **Metrics**: Diagnostic accuracy change, defense effectiveness ratings, preference rankings

## Impact & Applications

This research aims to:
- Ensure the safety and reliability of medical AI systems in clinical deployment
- Develop standardized defense mechanisms for medical vision-language models
- Create interpretable security solutions that clinicians can understand and trust
- Establish benchmarks for evaluating robustness of medical AI systems

## Collaborations

I work closely with:
- **Advisor**: Dr. Vahid Behzadan, SAIL Lab, University of New Haven
- Clinical partners for validation studies
- Medical AI security researchers

## Resources & Code

Upon publication, all attack implementations, defense mechanisms, and evaluation frameworks will be made publicly available to support reproducible research and advance the field of secure medical AI.

---

*For more details about my research or potential collaborations, please [contact me](mailto:mail@bineshkumar.me).*