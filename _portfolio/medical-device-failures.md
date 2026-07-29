---
title: "Advanced Fault Detection in Medical Devices"
excerpt: "Comparative study of generative models for early detection of failures in medical devices"
collection: portfolio
permalink: /portfolio/medical-device-failures/
header:
  teaser: images/1.jpg
---

Fault diagnosis is a seasoned field of research, and many critical medical devices carry an embedded expert system to self diagnose. But most medical devices embed intricate electro-mechanical components whose failures aren't linear, and variability in the operating environment produces failures that expert systems struggle to predict. As devices get more complex and recalls climb, expert systems alone can't keep up. That's why we turned to generative methods for fault detection.

![Medical Device Failures](/images/fda-medical-failures.jpg)

*Source: FDA MAUDE Database (Retrieved 9th January 2024)*

We studied predictive and preventive maintenance strategies in medical devices, focusing on fault detection techniques that use data, signal, process, or knowledge-based methods. These techniques matter because they catch failures before they become safety problems or degrade device performance.

### Research Scope

We surveyed current Fault Detection and Prediction algorithms and assessed how well each could work in the medical device sector. The goal: safer and more reliable medical equipment.

As part of this study we analyzed two generative algorithms, a Generative Adversarial Network (GAN) and a Variational Autoencoder (VAE), and one classic method, a Hidden Markov Model (HMM), for their effectiveness in fault detection. We also evaluated their applicability against real world surgical device sensor data and the Airbus anomaly detection benchmark dataset.

### Research Hypothesis

We use GANs to build Data-Driven Digital Twins (DDTs): deep learning models that construct digital versions of physical assets from sensor data. Incorporated into Prognostic and Health Monitoring frameworks, DDTs learn from normal operation data, bypassing the need for historical failure records.

![DDT Fault Detection](/images/ddt-fault-detection.jpg)

DDTs are good at catching early-stage faults, telling failure modes apart, and tracking asset deterioration across operating conditions. They also produce health indicators automatically, which makes predictive maintenance scheduling more efficient.

### Team Members

- Binesh Kumar
- Bahareh Arghavani Nobar
- Advisor: Dr. Vahid Behzadan

### Publications

Sadanandan, B., Arghavani Nobar, B., Behzadan, V. (2025). "Comparative Study of Generative Models for Early Detection of Failures in Medical Devices." arXiv preprint arXiv:2505.04845.
