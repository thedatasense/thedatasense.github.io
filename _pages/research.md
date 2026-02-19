---
layout: single
permalink: /research/
title: "Research"
author_profile: true
---

I study what happens when medical visual language models give different answers to the same question, just because you phrase it differently. That's the kind of failure that looks invisible on benchmarks but could matter a lot in a hospital.

I work with [Dr. Vahid Behzadan](https://sail-lab.org/) at the [Secure and Assured Intelligent Learning Lab (SAIL Lab)](https://unhsaillab.github.io/), University of New Haven.

## The problem that started it all

Vision-Language Models (VLMs) can look at a chest X-ray and answer clinical questions about it. They score well on standard benchmarks, sometimes reaching 85 to 95% accuracy. But here's the thing: ask "Is the heart size normal?" and the model says "Yes." Ask "Is there cardiomegaly?" about the same image and it says "Yes, the heart is enlarged." Same image, same clinical meaning, opposite answers.

I call these Paraphrase Sensitivity Failures (PSFs). Clinicians naturally rephrase questions all the time. If a model can't handle that, its high benchmark scores don't mean much at the bedside.

## What we found

We tested six medical VLMs on 19,748 questions with roughly 92,000 semantically equivalent paraphrases across chest X-ray datasets, including Medical Information Mart for Intensive Care (MIMIC-CXR) and PadChest. The flip rates, meaning how often a model contradicts itself on rephrased questions, ranged from 8% to 58% depending on the model and dataset. Negation paraphrases were the worst offenders. Changing "Is there pleural effusion?" to "Can pleural effusion be ruled out?" triggered flips 32 to 52% of the time across every model we tested.

## Why models flip

The models that flip aren't just confused by language. They're ignoring the image. When we used bounding box annotations from PadChest to measure where models actually look, flip cases showed 41% less attention to pathology regions compared to cases where the model stayed consistent. Some models appeared "stable" only because they achieved 96% text-only agreement, meaning they were getting answers from language patterns alone, not from the X-ray.

## Breakopen the model to see what's under the hood

Using GemmaScope 2 Sparse Autoencoders on MedGemma-4B, we found one specific feature, Feature 3818 at layer 17, that acts like a formality gate for clinical queries. When this feature activates strongly (values around 300 to 400), the model tends toward conservative "No" responses. When it stays near zero, the model leans toward "Yes." This single feature accounts for 28 to 42% of the decision margin shift in flip pairs. That's a lot of clinical behavior riding on one internal switch.

## Fixing it 

We used targeted Low-Rank Adaptation (LoRA) fine-tuning on layers 15 through 19, the layers our causal analysis identified as most responsible. With just 0.1% of parameters updated, we reduced flip rates by 79.5%.

But here's what caught us off guard. Naively fine-tuning all 34 layers drove the flip rate down to 1.4%, which sounds great until you realize the model achieved 80.6% text-only agreement. It became consistent by memorizing language patterns, not by actually looking at images. Our targeted approach kept flip rates at 8.3% on MIMIC while maintaining 32.7% swap sensitivity, which tells us the model is genuinely using the image.

The lesson: consistency alone isn't safety. A model that always gives the same answer but ignores the X-ray may be more dangerous than one that occasionally contradicts itself while actually trying to read the image.

## What I'm working with

| Category | Details |
|---|---|
| Imaging Datasets | MIMIC-CXR (377K images), CheXpert (224K images), PadChest, VinDr-CXR (18K images) |
| Target Models | MedGemma-4B, MedGemma-27B, LLaVA-Rad, and others |
| Focus Pathologies | Cardiomegaly, Pleural Effusion, Pneumothorax, Consolidation, Atelectasis |

## Code and repositories

| Repository | What it does |
|---|---|
| [robust-med-mllm-experiments](https://github.com/thedatasense/robust-med-mllm-experiments) | Main experiments for medical multimodal Large Language Model (LLM) testing |
| [medical-vlm-intepret](https://github.com/thedatasense/medical-vlm-intepret) | Interpretability tools for medical VLMs |
| [LLaVA-Med](https://github.com/thedatasense/LLaVA-Med) | Large Language and Vision Assistant for biomedicine |
| [CheXagent](https://github.com/thedatasense/CheXagent) | Chest X-ray analysis agent |

## Selected publications

**Sadanandan, B.**, Behzadan, V. (2025). "VSF-Med: A Vulnerability Scoring Framework for Medical Vision-Language Models." *IEEE ISBI 2026*. [arXiv:2507.00052](https://arxiv.org/abs/2507.00052)

**Sadanandan, B.**, Behzadan, V. (2026). "When Chain-of-Thought Backfires: Evaluating Prompt Sensitivity in Medical Language Models." *Preprint*.

**Sadanandan, B.**, Behzadan, V. (2025). "Promise of Data-Driven Modeling and Decision Support for Precision Oncology and Theranostics." [arXiv:2505.09899](https://arxiv.org/abs/2505.09899)

**Sadanandan, B.**, Arghavani Nobar, B., Behzadan, V. (2024). "Comparative Study of Generative Models for Early Detection of Failures in Medical Devices." *2024 8th International Conference on Medical and Health Informatics*.

[Full list of publications](/publications/) | [Google Scholar](https://scholar.google.com/citations?user=YgIIscgAAAAJ&hl=en)


## Get in touch

If any of this resonates with your work, or if you're thinking about similar problems, I'd love to hear from you: [LinkedIn](https://www.linkedin.com/in/bineshk) | contact(at)bineshkumar(dot)me
