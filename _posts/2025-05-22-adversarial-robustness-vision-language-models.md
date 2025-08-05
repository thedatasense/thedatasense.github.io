---
layout: post
title: "The Evolution of Adversarial Robustness: From Neural Networks to Vision-Language Models"
date: 2025-05-22 13:00:00 -0400
categories: [research, ai-safety]
tags: [adversarial-ml, vision-language-models, robustness, medical-ai, interpretability]
author: Binesh K Sadanandan
---

This comprehensive review traces the evolution of adversarial machine learning from its inception to current challenges in multimodal AI systems, with particular focus on implications for healthcare applications.

## 1. Intriguing Properties of Neural Networks (2014)

_Szegedy, Zaremba, Sutskever, Bruna, Erhan, Goodfellow, Fergus_

### Core Discovery

Neural networks have two counterintuitive properties that fundamentally challenge our understanding:

1. **Distributed Representations**: Semantic information is distributed across all neurons rather than localized
2. **Adversarial Examples**: Imperceptibly small perturbations can fool networks into misclassifying with high confidence

### Key Findings

- **Perturbation magnitude**: Only σ = 0.058-0.14 needed for 100% attack success
- **Transfer rates**: 15-40% of adversarial examples fooled models with different architectures
- **Universality**: Phenomenon observed across all architectures (linear models, CNNs, unsupervised models)

### Why This Happens

Adversarial examples exist due to high-dimensional geometry of neural networks. In high dimensions, networks behave approximately linearly in most directions, with insufficient training data to constrain behavior in all possible directions.

### Lasting Impact

This paper created the field of adversarial machine learning. Ten years later, modern VLMs still exhibit these vulnerabilities, suggesting this isn't overfitting but a fundamental characteristic of how neural networks learn.

## 2. On Evaluating Adversarial Robustness of Large Vision-Language Models (2023)

_Zhao, Pang, Du, Yang, Li, Cheung, Lin_

### Core Discovery

Large VLMs like GPT-4 can be fooled into generating targeted responses through imperceptible image perturbations—even under realistic black-box constraints with only API access.

### Attack Framework

- **Two-Stage Pipeline**: Transfer-based attacks using surrogate models (CLIP/BLIP) followed by query-based refinement
- **Cross-Modal Vulnerability**: Vision attacks are automated and imperceptible, unlike text attacks requiring extensive prompt engineering

### Key Results

- **Attack success rates**: CLIP scores increase from 0.4-0.5 to 0.8+ with just ε = 8/255 perturbations
- **Model vulnerability**: All tested models susceptible, from lightweight BLIP (224M) to massive MiniGPT-4 (14.1B)
- **Query efficiency**: Just 8 black-box queries significantly boost attack performance

### Why This Matters

VLMs are being deployed in safety-critical applications. Vision attacks present a more severe attack surface because:

1. Perturbations are imperceptible to humans
2. Attacks can be fully automated
3. Text defenses don't transfer to vision

## 3. Can LLMs Deceive CLIP? (2025)

_Ahn, Yun, Ko, Kim_

### Core Discovery

LLMs can systematically expose compositional vulnerabilities in VLMs by generating deceptive text that maintains high crossmodal similarity while contradicting the original content—achieving up to 42% attack success rate using only text modifications.

### The MAC Framework

**Multimodal Adversarial Compositionality (MAC)** provides:

- Modality-agnostic evaluation across images, videos, and audio
- Four-criteria assessment: crossmodal similarity, unimodal non-entailment, lexical distance, auxiliary constraints
- Diversity metrics to ensure varied attack patterns

### Key Findings

- **ASR improvement**: From 6.88% (zero-shot) to 42.10% (with self-training)
- **High transferability**: 23-41% cross-model transfer success
- **Efficiency gains**: Self-trained models with N=4 match zero-shot performance at N=16

### Attack Mechanism

Exploits VLMs' compositional understanding through:

- Crossmodal deception (generated text scores higher similarity)
- Semantic contradiction (e.g., "reaching for keys" → "accidentally typing email")
- Diverse patterns through entropy maximization

## 4. One Surrogate to Fool Them All (2025)

_Xu, Dai, Tang, Zhang_

### Core Discovery

A single publicly available CLIP model can generate universal adversarial perturbations forcing arbitrary DNNs to misclassify into attacker-specified targets—achieving 85% ASR on ImageNet and compromising real-world services without target model access.

### The UnivIntruder Framework

Three key innovations:

1. **CLIP-based surrogate**: Uses textual concepts for alignment with unknown targets
2. **Feature direction mechanism**: Captures perturbation effects in embedding space
3. **Robust random transformations**: Prevents overfitting to surrogate structure

### Real-World Impact

- **Dataset ASRs**: CIFAR-10 (99.4%), ImageNet (85.1% top-1)
- **Real services**: Google (53%), Baidu (84%), Claude-3.5 (80%), GPT-4 (64%)
- **Query reduction**: 80% fewer black-box queries when used as initialization

### Defense Analysis

- Adversarial training reduces ASR to 15-30% but requires expensive retraining
- Test-time defenses degrade clean accuracy significantly
- Label obfuscation provides minimal protection (<5% ASR reduction)

## 5. Chest X-ray Classification: Pitfalls and Best Practices (2023)

_Ghamizi, Cordy, Papadakis, Le Traon_

### Core Discovery

Previous claims of 100% attack success on chest X-ray classifiers are oversimplified. Medical domain requires careful consideration of multi-label classification, labeler disagreement, and clinical risk.

### Critical Pitfalls Identified

1. **Binary classification bias**: 9/16 studies only evaluated binary classification
2. **Single dataset evaluation**: Missing cross-domain generalization failures
3. **Inadequate threat models**: Assumed unrealistic white-box access
4. **Inappropriate metrics**: Standard accuracy ignores disease co-occurrence

### Key Findings

- **Dataset-dependent robustness**: PadChest 3× more robust than NIH (53.6% vs 13.8%)
- **Risk-based attacks more effective**: Targeting improbable combinations reduces robustness from 32.1% to 11.1%
- **Architecture matters less than data**: Similar vulnerabilities across architectures on same dataset

### Medical AI Implications

- Domain-specific evaluation metrics essential (k-robust accuracy, risk scores)
- Cross-dataset evaluation reveals true generalization limits
- Vision modality in medical VLMs may inherit these vulnerabilities

## 6. Non-Natural Image Understanding with FM-ViT (2024)

_Lin, Wang, Feng, Wang, Jin, Zhao, Wu, Yao, Chen_

### Core Discovery

Vision Transformers act as low-pass filters, progressively losing high-frequency information crucial for non-natural images. FM-ViT introduces frequency modulation to preserve these details.

### The Frequency Problem

- **Low-Pass Filter Behavior**: Self-attention reduces high-frequency components as layers deepen
- **Impact on Non-Natural Images**: Charts, diagrams, mathematical figures concentrate semantic information in high frequencies

### The FM-ViT Solution

- **Fourier Decomposition**: Separates features into DC and high-frequency components
- **Learnable Re-weighting**: Adaptive adjustment based on input characteristics
- **Sample-wise Adaptation**: Dynamic weights using Discrete Wavelet Transform

### Performance Gains

- **Classification**: Geometric 61.5%, Charts 92.1%, Functions 65.9%
- **Question answering**: GeoQA 68.2%, ChartQA 72.5%
- **Frequency preservation**: Maintains high-frequency information across all layers

### Medical Imaging Relevance

Critical for chest X-ray analysis where high-frequency details include:

- Anatomical boundaries (pleural lines, cardiac silhouettes)
- Subtle pathologies (early infiltrates, small nodules)
- Medical devices (lines, tubes, wires)

## 7. LVLM-Interpret: An Interpretability Tool (2024)

_Stan, Aflalo, Rohekar, Bhiwandiwalla, Tseng, Olson, Gurwicz, Wu, Duan, Lal_

### Core Discovery

LVLMs exhibit interpretable attention patterns revealing systematic biases—particularly over-reliance on text prompts rather than visual content, making them vulnerable to manipulation.

### The Tool

Browser-based interface combining:

- **Layer Attention Maps**: Token-to-token interactions across modalities
- **Relevancy Scores**: Gradient-based attribution through both modalities
- **Causal Graphs**: Identify minimal explanatory image patches

### Key Findings

- **Text-Image Imbalance**: Contradictory answers based solely on query wording
- **Visual Grounding Success**: Image relevancy dominates (>70%) for consistent queries
- **Causal Structure**: 5-15 image patches sufficient for specific outputs

### Healthcare Implications

Discovery of systematic text-bias critical for medical imaging where textual context shouldn't override visual evidence. Tool should become part of standard validation pipelines.

## 8. Token Activation Map (TAM) (2025)

_Yi Li, Hualiang Wang, Xinpeng Ding, Haonan Wang, Xiaomeng Li_

### Core Discovery

Multimodal LLMs' progressive text generation causes early-token activations to pollute later explanations. TAM disentangles each token's true visual cues through causal inference and denoising.

### Technical Innovation

- **Estimated Causal Inference**: Models interference from prior tokens, subtracts via least-squares
- **Rank Gaussian Filter**: Removes noise while preserving fine visual details
- **Multimodal Map Fusion**: Combines visual maps with textual relevance

### Results

- **COCO Caption**: 39.10% F1-IoU, 8.96-point improvement over baseline
- **Consistent gains**: 5.45-11.00 points across seven MLLMs
- **Better localization**: Sharper object detection, clearer attribute highlighting

## Key Takeaways for Healthcare AI

1. **Fundamental Vulnerabilities**: Adversarial examples aren't bugs but features of how neural networks learn
2. **Multimodal Amplification**: VLMs inherit and amplify vulnerabilities through cross-modal interactions
3. **Medical Domain Specificity**: Healthcare requires specialized evaluation metrics and threat models
4. **Frequency Preservation**: Critical for medical imaging where high-frequency details determine diagnosis
5. **Interpretability Requirements**: Tools must account for multimodal architectures and clinical deployment constraints

As we deploy AI in healthcare, understanding these vulnerabilities isn't optional—it's essential for patient safety and clinical trust.
