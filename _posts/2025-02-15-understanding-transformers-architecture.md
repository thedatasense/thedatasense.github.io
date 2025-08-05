---
layout: post
title: "Understanding the Transformer Architecture: A Deep Dive"
date: 2025-02-15 10:00:00 -0400
categories: [research, deep-learning]
tags: [transformers, attention-mechanism, neural-networks, nlp]
author: Binesh K Sadanandan
---

The transformer architecture changed natural language processing when Vaswani et al. introduced it in "Attention is All You Need." This post explains how transformers work, focusing on their key components and the attention mechanism.

## What is a Transformer?

A transformer has two main parts:

**Encoder**: Reads input text and creates contextual vectors  
**Decoder**: Uses these vectors to generate output text

Both parts use self-attention to understand how words relate to each other in a sequence.

## Why Use Transformers?

Transformers process entire sequences at once, unlike RNNs and LSTMs that process one word at a time. This gives three benefits:

• Removes sequential bottlenecks  
• Captures long-range dependencies better  
• Trains much faster

## The Encoder

The encoder stacks 6 identical layers. Each layer contains:

### 1. Multi-Head Self-Attention

Every token looks at every other token in the sequence. This captures word relationships regardless of distance. The model adds positional encodings to embeddings so it knows word order.

### 2. Add & Norm

**Add**: Adds the input back to the output (residual connection)  
**Norm**: Standardizes values across layers

These prevent vanishing gradients and help the model learn.

### 3. Feedforward Network

A simple neural network that refines token representations.

### 4. More Residual Connections

Each sublayer passes its input forward with its output, which stabilizes training.

## The Decoder

The decoder also stacks identical layers, but each has three parts:

### 1. Masked Self-Attention

The decoder looks at its previous outputs but can't see future tokens. This maintains causality during generation.

### 2. Cross-Attention

Here the decoder connects to the encoder:

• Uses encoder output as keys and values  
• Uses its own state as queries  
• Focuses on relevant input parts for each output token

### 3. Feedforward Layer

Refines the decoder's representations, just like in the encoder.

## How Attention Works

### Core Components

**Input Embeddings**: Word vectors (example: ["we," "train," "a," "transformer," "model"])

**Weight Matrices**:  
• $$W_Q$$: Creates query vectors  
• $$W_K$$: Creates key vectors  
• $$W_V$$: Creates value vectors

### The Attention Process

1. **Create Q, K, V matrices**  
   Multiply input X by weight matrices. Each token gets:
   • Query (q): What information it needs
   • Key (k): What information it offers
   • Value (v): Its actual content

2. **Calculate attention scores**  
   For each token, compute dot product of its query with all keys. This measures relevance.

3. **Scale the scores**  
   Divide by $$\sqrt{d_k}$$ to prevent large values that break softmax.

4. **Apply causal mask**  
   Add mask to hide future tokens. For position 2:  
   `mask = [0, 0, -∞, -∞]`

5. **Apply softmax**  
   Convert scores to probabilities (attention weights).

6. **Compute weighted sum**  
   Multiply values by attention weights and sum:  
   $$g_i = \sum_{j=1}^{n} w_j \cdot v_j$$

### The Complete Formula

$$G = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}} + M\right) V$$

Where:  
• Q, K, V = Query, key, value matrices  
• M = Causal mask

## Byte Pair Encoding (BPE)

BPE is a tokenization method that breaks text into subwords. It balances vocabulary size with the ability to handle rare words.

### Why BPE?

Traditional tokenization has problems:  
• Poor computational efficiency  
• Can't handle unseen words

BPE solves these by learning common subword patterns.

### How BPE Works

1. **Start**: Begin with individual characters plus end-of-word marker (_)
2. **Tokenize**: Break text into these basic tokens
3. **Merge**: Find the most common adjacent pair and merge them. This:
   • Shortens the sequence
   • Adds new token to vocabulary
4. **Stop**: After set number of merges or when no common pairs remain

## Summary

Transformers excel because they:  
• Process sequences in parallel  
• Capture long-range dependencies  
• Use attention to understand word relationships

This architecture powers BERT, GPT, and other breakthrough models in AI.

## Reference

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. _Advances in neural information processing systems_, 30.