---
layout: post
title: "Large Language Models: From Architecture to Evaluation"
date: 2025-04-18 12:00:00 -0400
categories: [research, deep-learning]
tags: [llms, multimodal-ai, evaluation-metrics, llama, transformers]
author: Binesh K Sadanandan
---

Large Language Models (LLMs) have revolutionized natural language processing through their ability to understand and generate human-like text. This comprehensive guide explores the architecture, training, and evaluation of modern LLMs, including the latest multimodal developments.

## Creating Chat-Capable LLMs

Building a conversational LLM involves two critical stages:

### 1. Pretraining on Massive Datasets

During pretraining, models learn to predict the next token based on input context, minimizing cross-entropy loss. This phase helps models develop contextual understanding as a side effect. Modern LLMs employ transformer architectures with:
- Larger embedding dimensions (`emb_dim`)
- Multiple stacked decoder blocks (`num_blocks`)

#### Number of Parameters

While toy models might have millions of parameters, state-of-the-art systems push into hundreds of billions or even trillions. In transformers, these parameters are distributed across:
- Embeddings
- Multi-head self-attention modules
- MLP layers

Doubling the embedding dimension typically quadruples the parameter count in attention and MLP components.

#### Context Window

Modern LLMs handle increasingly larger contexts:
- GPT-3: 2,048 tokens
- Next-gen LLMs: 128,000+ tokens (entire novel in one pass)

However, self-attention scaling remains a bottleneck with $$O(n^2)$$ complexity, where doubling sequence length quadruples memory usage and compute cost.

### 2. Supervised Finetuning for Instructions

The second phase addresses the gap between raw text generation and instruction-following ability. During finetuning:
- Models train on high-quality instruction-response pairs
- Learn direct response behaviors
- Develop ability to clarify questions or refuse inappropriate requests
- Transform from "text continuation" to interactive assistance

## Multimodal LLMs: Llama 3.2 Architecture

Meta's Multimodal LLaMA 3.2 integrates vision and language capabilities through three main components:

### Vision Encoder
- **Two-stage design**: 32-layer local encoder + 8-layer global encoder with gated attention
- **High-resolution input**: 32×32 grid of patches (1280-dimensional vectors)
- **Multi-scale features**: Preserves outputs from layers 3, 7, 15, 23, and 30

### Language Model
- Based on LLaMA 3.1 with 40 transformer layers
- Hidden size of 4096
- Alternates between self-attention and cross-attention (every 5th layer)

### Integration Mechanism
- **Projection layer**: Maps 7680-dimensional visual features to 4096-dimensional space
- **Cross-attention layers**: Strategic placement for visual-textual integration
- **Gated mechanisms**: Fine-grained control over information flow

## Evaluating LLMs

### Perplexity

Perplexity measures how well a model predicts text, quantifying uncertainty in predictions. Lower perplexity indicates better performance.

**Mathematical Definition:**
$$\text{Perplexity}(\mathcal{D}, k) = \exp\left( - \frac{1}{D} \sum_{i=1}^{D} \log \Pr(t_i \mid t_{i-k}, t_{i-k+1}, \ldots, t_{i-1}) \right)$$

**Example Calculation:**
For text "AI models are improving significantly" with token probabilities:
- $$\Pr(\text{AI}) = 0.12$$
- $$\Pr(\text{models} \mid \text{AI}) = 0.15$$
- $$\Pr(\text{are} \mid \text{AI, models}) = 0.25$$
- $$\Pr(\text{improving} \mid \text{models, are}) = 0.20$$
- $$\Pr(\text{significantly} \mid \text{are, improving}) = 0.10$$

Average NLL = 1.86, resulting in Perplexity ≈ 6.42

### ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

ROUGE evaluates text quality by measuring token/n-gram overlaps between generated and reference text:

$$\text{ROUGE-1} = \frac{\sum_{(g, r) \in \mathcal{D}} \sum_{t \in r} \text{count}(t, g)}{\sum_{(g, r) \in \mathcal{D}} \text{length}(r)}$$

**Example:**
- Reference: "The cat sat on the mat near the door"
- Generated: "The cat sat by the door on the mat"
- Matching words: 7 out of 9
- ROUGE-1: 0.78

## Holistic Evaluation Framework (HELM)

The HELM framework groups evaluation metrics into three categories:

### 1. Resource Requirements/Efficiency
Evaluates training and inference costs:
- Energy consumption and CO2 emissions
- Runtime metrics (denoised and idealized)
- Hardware/software standardization for fair comparison

### 2. Alignment
Addresses fairness, bias, stereotypes, and toxicity:

**Fairness Approaches:**
- **Counterfactual fairness**: Tests model behavior on perturbed examples
- **Performance disparities**: Measures accuracy differences across demographic groups

**Social Bias Metrics:**
- Demographic representation bias
- Stereotypical associations

### 3. Capability
Includes accuracy, calibration, and robustness:

**Accuracy Metrics:**
- Exact match (text classification)
- F1 score (question answering)
- MRR/NDCG (information retrieval)
- ROUGE (summarization)

**Calibration:**
The ability to express uncertainty accurately, crucial for high-stakes applications. Expected Calibration Error (ECE) measures the difference between predicted probability and actual correctness.

**Robustness:**
- **Invariance**: Stability under semantic-preserving perturbations (typos, capitalization)
- **Equivariance**: Response to semantic-altering perturbations

## Taxonomy of LLM Evaluation

1. **Accuracy**: Task-specific metrics rather than single values
2. **Calibration and Uncertainty**: Meaningful probability assignments
3. **Robustness**: Performance against transformed instances
4. **Fairness**: Counterfactual and statistical fairness metrics

## Key Takeaways

- LLM development requires massive pretraining followed by careful instruction finetuning
- Multimodal architectures like Llama 3.2 integrate vision through sophisticated cross-attention mechanisms
- Evaluation must be holistic, considering efficiency, alignment, and capability
- Perplexity and ROUGE provide complementary views of model performance
- Fairness and robustness are as important as raw accuracy

As LLMs continue to evolve, comprehensive evaluation frameworks become essential for developing models that are not only capable but also efficient, fair, and aligned with human values.