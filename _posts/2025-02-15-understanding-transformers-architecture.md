---
layout: post
title: "Understanding the Transformer Architecture: A Deep Dive"
date: 2025-02-15 10:00:00 -0400
categories: [research, deep-learning]
tags: [transformers, attention-mechanism, neural-networks, nlp]
author: Binesh K Sadanandan
---

Originally introduced in "Attention is All You Need" by Vaswani et al., the transformer architecture has revolutionized natural language processing and beyond. This post provides a comprehensive overview of the transformer architecture, its key components, and the attention mechanism that powers it.

## High-Level Overview

The transformer architecture consists of two main components:

- **Encoder**: Processes the input text and encodes it into contextual vectors
- **Decoder**: Takes these encoded vectors and generates the output text

Both encoder and decoder use layers of self-attention mechanisms that allow the model to weigh and learn the importance of words in a sequence with respect to each other.

### Why Transformers?

Unlike RNNs and LSTMs that process sequences one word/token at a time, transformers process entire sequences at once. This parallel processing capability offers several advantages:

- Eliminates sequential dependencies that hinder parallelization
- Better captures long-term dependencies in sequences
- Significantly improves training time

## The Encoder

The encoder is a stack of multiple identical layers (6 in the original transformer paper). Each layer consists of:

### 1. Multi-Headed Self-Attention

The encoder processes the input sequence using self-attention, where each token attends to every other token. This captures dependencies between words, regardless of their position in the sequence. Input tokens are represented as embeddings, added to positional encodings to retain order information.

### 2. Add & Norm Layers

- **Add**: A residual connection where the input to a sublayer is added back to its output
- **Norm**: Layer normalization that ensures consistent scale of inputs across layers

These components help stabilize training by avoiding the vanishing gradient problem and allow the model to learn identity mappings when needed.

### 3. Feedforward Neural Network

A fully connected layer that processes the output of the attention mechanism to refine token representations.

### 4. Residual Connections and Layer Normalization

These stabilize training by passing the input of each layer forward along with the processed output.

## The Decoder

The decoder is also a stack of identical layers, but each layer has three key components:

### 1. Masked Multi-Headed Self-Attention

The decoder attends to its own previous outputs, but masking is applied to prevent attending to future tokens (maintaining causality during generation).

### 2. Cross-Attention

This is where the decoder attends to the encoder's output representations. At each decoding step, the decoder uses:

- Encoder's output as key-value pairs
- Its own hidden state as the query

This allows the decoder to focus on relevant parts of the input sentence for the current output token.

### 3. Feedforward Layer

Like the encoder, a fully connected layer refines the decoder's representations.

## The Attention Mechanism

### Key Components

- **Input Embeddings**: Words or tokens represented as vectors (e.g., ["we," "train," "a," "transformer," "model"])
- **Trainable Weight Matrices**:
  - $$W_X$$: Transforms inputs into query vectors ($$Q$$)
  - $$W_Y$$: Transforms inputs into key vectors ($$K$$)
  - $$W_Z$$: Transforms inputs into value vectors ($$V$$)

### Steps in Self-Attention

1. **Compute Q, K, and V**: Multiply the input matrix $$X$$ by weight matrices $$W_X$$, $$W_Y$$, and $$W_Z$$. Each token $$x_i$$ is associated with:

   - $$q_i$$: Seeks relevant information
   - $$k_i$$: Provides relevance clues
   - $$v_i$$: Contains semantic information

2. **Compute Attention Scores**: For token $$x_i$$, calculate $$q_i \cdot k_j$$ (dot product) for all $$j$$. This measures the similarity between $$q_i$$ and $$k_j$$.

3. **Scale the Scores**: Divide each score by $$\sqrt{d_k}$$, where $$d_k$$ is the dimensionality of the key vectors. This prevents large values from destabilizing the softmax function.

4. **Apply Causal Mask**: Add a mask to ensure tokens only attend to current and previous tokens (not future ones). Example for position 2:
   $$\text{causal\_mask} = [0, 0, -\infty, -\infty]$$

5. **Apply Softmax**: Convert masked scores into probabilities (attention weights):
   $$\text{softmax}(\text{masked\_scores}) \rightarrow [w_1, w_2, \ldots, w_n]$$

6. **Weighted Sum of Value Vectors**: Use attention weights to compute the output for each token:
   $$g_i = \sum_{j=1}^{n} w_j \cdot v_j$$

### The Key Formula

The attention mechanism for all tokens can be expressed as:

$$G = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}} + M\right) V$$

Where:

- $$Q, K, V$$: Query, key, and value matrices
- $$M$$: Causal mask

## Byte Pair Encoding (BPE)

Byte Pair Encoding is a subword tokenization algorithm widely used in transformer models like GPT. It balances the trade-off between vocabulary size and the ability to represent rare and unseen words.

### Why BPE?

Traditional tokenization algorithms in NLP:

- Lack computational efficiency
- Fail to represent unseen words effectively

BPE addresses these issues by breaking text into subwords and learning a vocabulary of frequent subword patterns.

### The BPE Algorithm

1. **Initialization**: Start with a vocabulary of individual characters and a special end-of-word symbol (e.g., `_`)
2. **Tokenization**: Represent the input text as a sequence of these initial tokens
3. **Merge Operations**: Iteratively merge the most frequent adjacent token pairs into a new token. Each merge:
   - Reduces the sequence length
   - Adds the merged token to the vocabulary
4. **Stopping Criterion**: Stop after a predefined number of merges or when no frequent pairs remain

## Conclusion

The transformer architecture's innovative use of attention mechanisms has made it the foundation of modern NLP systems. By processing sequences in parallel and effectively capturing long-range dependencies, transformers have enabled breakthrough models like BERT, GPT, and many others that continue to push the boundaries of what's possible in AI.

## References

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. _Advances in neural information processing systems_, 30.
