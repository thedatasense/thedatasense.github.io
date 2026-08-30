---
title: "Predictive Entropy as a Joint Screen for Error and Paraphrase Instability in Medical Vision-Language Models"
collection: publications
pub_type: conferences
permalink: /publication/2026-predictive-entropy
excerpt: "A single predictive-entropy signal can rank both likely errors and likely paraphrase flips, providing a bounded readiness screen for two failure modes."
date: 2026-04-01
venue: "UNSURE Workshop, MICCAI 2026 (poster)"
paperurl: "/phd-thesis/assets/papers/predictive-entropy.pdf"
citation: "Sadanandan, B., & Behzadan, V. (2026). Predictive entropy as a joint screen for error and paraphrase instability in medical vision-language models. <i>UNSURE Workshop, MICCAI 2026</i> (poster)."
---

[Paper](/phd-thesis/assets/papers/predictive-entropy.pdf) | [Code](https://github.com/thedatasense/predictive_entropy_unsure)

We test whether a single predictive-entropy signal can flag two failure modes in medical Vision-Language Models (VLMs). On Targeted LoRA over the PadChest flip bank, entropy ranks paraphrase flips at AUROC 0.823 and errors at 0.862, with the flip result replicated across architectures. Softmax entropy, temperature-scaled entropy, and absolute margin are rank-equivalent; confidence ranking still does not certify that a prediction is image-grounded.
