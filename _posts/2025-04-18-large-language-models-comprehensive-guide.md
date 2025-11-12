---
layout: post
title: "Large Language Models: From Architecture to Evaluation"
date: 2025-04-18 12:00:00 -0400
description: A complete guide to building and evaluating large language models, from pretraining and instruction finetuning to multimodal capabilities using LLaMA as a case study.
categories: [research, deep-learning]
tags: [llms, multimodal-ai, evaluation-metrics, llama, transformers]
author: Binesh K Sadanandan
---

Large Language Models (LLMs) have transformed how machines process text—and now they’re learning to see. In this guide, we:

1. Show how we build chat-capable LLMs.
2. Walk through instruction finetuning.
3. Use Meta’s LLaMA as a concrete example of a multimodal LLM.
4. Cover key evaluation metrics and best practices.

---

## 1. From Text to Conversation

We start by teaching a model to predict words, then turn it into a helpful assistant.

### 1.1 Pretraining on Text  
- **Data**: Hundreds of billions of tokens from books, articles, code.  
- **Task**: Predict the next token in each sequence.  
- **Model**: A stack of transformer decoder blocks with self-attention and feed-forward layers.  
- **Scale**:  
  - Embedding size (`d_model`), number of layers (`L`), and attention heads (`H`) set the model’s capacity.  
  - Doubling `d_model` roughly quadruples total parameters.  
  - Leading models range from 10 B to over 1 T parameters.  
- **Context window**:  
  - Early: 2 K tokens (e.g., GPT-3)  
  - Now: 100 K+ tokens for long documents  
  - Attention cost grows as $O(n^2)$, so long contexts need memory tricks.  

> **Tip:** Use mixed precision (FP16 or BF16) to save GPU memory and speed up training.

### 1.2 Instruction Finetuning  
After pretraining, the model knows language patterns but not how to follow requests. We fix that by:

1. **Collecting examples**  
   - Human-written prompts and ideal responses (translate, summarize, answer).  
2. **Training**  
   - Continue cross-entropy on the response, conditioning on the instruction.  
   - Optionally apply RLHF (reinforcement learning from human feedback).  
3. **Result**  
   - The model asks for clarification if unclear.  
   - It refuses harmful or off-limits requests.  
   - It shifts from “next-word guessing” to “helpful assistant.”

---

## 2. Case Study: LLaMA as a Multimodal LLM

Meta’s LLaMA family illustrates how to add vision to a text model. LLaMA 3.2 processes images and text in one network.

### 2.1 Why Multimodal?  
- Real-world tasks often mix text and images: recipes with photos, medical reports with scans, document Q&A with figures.  
- A single model that handles both can share knowledge across modes.

### 2.2 LLaMA 3.2 Architecture

#### 2.2.1 Vision Encoder  
1. **Patch embedding**  
   - Split each image into a 32×32 grid of patches.  
   - Flatten each patch into a 1,280-dim vector.  
2. **Two-stage encoder**  
   - **Local encoder** (32 layers) captures textures and edges.  
   - **Global encoder** (8 layers with gated attention) builds a wider context.  
3. **Multi-scale features**  
   - Extract outputs from layers 3, 7, 15, 23, and 30 for richer signals.

#### 2.2.2 Text Backbone  
- Based on LLaMA 3.1  
- **40 transformer layers**, hidden size 4,096  
- Alternates self-attention and cross-attention every 5 layers  

#### 2.2.3 Cross-Modal Bridge  
1. **Projection layer**  
   - Map 7,680-dim visual features into the 4,096-dim text space.  
2. **Cross-attention**  
   - At key layers, text tokens attend to image features.  
3. **Gating**  
   - Control how much visual information flows in, preventing overload.

> **Note:** By sharing transformer blocks, LLaMA keeps parameter growth modest while gaining vision skills.

---

## 3. Evaluating LLMs: A Holistic View

We measure models on multiple fronts—accuracy, fairness, cost, and robustness.

### 3.1 Core Metrics

| Metric       | What it measures                         | When to use                    |
|--------------|------------------------------------------|--------------------------------|
| **Perplexity** | How well a model predicts text            | Language modeling              |
| **ROUGE**      | Overlap of generated vs. reference text | Summarization, translation     |

- **Perplexity**  
  \[
    \text{Perplexity} = \exp\Bigl(-\tfrac{1}{D}\sum_{i=1}^D \log P(t_i \mid t_{<i})\Bigr).
  \]  
  Lower is better—fewer surprises.

- **ROUGE-1**  
  \[
    \frac{\text{Matched words}}{\text{Words in reference}}.
  \]  

### 3.2 HELM Framework

A broad evaluation groups metrics into three pillars:

1. **Efficiency**  
   - Training compute and energy use  
   - Inference latency and throughput  
2. **Alignment**  
   - Fairness across demographics  
   - Bias and toxicity checks  
3. **Capability**  
   - Task accuracy (F1, Exact Match, MRR)  
   - Calibration (ECE)  
   - Robustness to noise, paraphrases, typos

---

## 4. Best Practices and Takeaways

1. **Pretrain** at large scale, using diverse text.
2. **Finetune** on clear, high-quality instruction data.
3. **Integrate vision** via cross-attention—LLaMA shows one path.
4. **Evaluate broadly**: don't rely on a single number.

By following this roadmap, you build LLMs that understand text, images, and user needs—while staying efficient, fair, and robust.

## References

Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M. A., Lacroix, T., Rozière, B., Goyal, N., Hambro, E., Azhar, F., Rodriguez, A., Joulin, A., Grave, E., & Lample, G. (2023). LLaMA: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*.

Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Yang, J., Fan, A., et al. (2024). The Llama 3 herd of models. *arXiv preprint arXiv:2407.21783*.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P. F., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*, 35, 27730-27744.

Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M., Zhang, Y., Narayanan, D., Wu, Y., Kumar, A., Newman, B., Yuan, B., Yan, B., Zhang, C., Cosgrove, C., Manning, C. D., Ré, C., Acosta-Navas, D., Hudson, D. A., ... & Koreeda, Y. (2022). Holistic evaluation of language models. *arXiv preprint arXiv:2211.09110*.

Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter, C., Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray, S., Chess, B., Clark, J., Berner, C., McCandlish, S., Radford, A., Sutskever, I., & Amodei, D. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems*, 33, 1877-1901.
