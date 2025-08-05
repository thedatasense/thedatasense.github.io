---
layout: page
title: VSF-Med - Vulnerability Scoring Framework for Medical Vision-Language Models
description: A comprehensive framework for evaluating security vulnerabilities in medical AI systems
img: assets/img/4.jpg
importance: 1
category: research
giscus_comments: false
---

<p>As medical institutions increasingly adopt Vision-Language Models (VLMs) for clinical decision support, understanding and mitigating their security vulnerabilities becomes critical. This research introduces VSF-Med, a comprehensive vulnerability scoring framework designed specifically for evaluating the robustness of medical AI systems against adversarial attacks.</p>

<p>The framework addresses the unique challenges posed by the integration of visual and textual modalities in medical AI, where subtle manipulations can lead to potentially dangerous misdiagnoses or inappropriate treatment recommendations.</p>

<h3>Research Scope</h3>
<p>VSF-Med provides a systematic approach to evaluate vulnerabilities in medical VLMs through three key components:</p>
<ul>
  <li><strong>Text-prompt attack templates</strong>: Designed to test the model's resilience against malicious or misleading textual inputs</li>
  <li><strong>Imperceptible visual perturbations</strong>: Subtle modifications to medical images that can deceive AI systems while remaining invisible to human observers</li>
  <li><strong>Eight-dimensional risk assessment rubric</strong>: A comprehensive scoring system that evaluates multiple aspects of model vulnerability</li>
</ul>

<p>Our evaluation synthesized over 30,000 adversarial variants from 5,000 radiology images, providing a thorough assessment of current medical AI systems' security posture.</p>

<h3>Key Findings</h3>
<p>The research revealed varying levels of vulnerability across different state-of-the-art models:</p>
<ul>
  <li>Models like Llama-3.2-11B-Vision-Instruct and GPT-4o demonstrated different susceptibility patterns to adversarial attacks</li>
  <li>Certain attack vectors proved more effective in medical contexts compared to general-purpose applications</li>
  <li>The multimodal nature of medical VLMs introduces unique vulnerability surfaces not present in text-only or vision-only models</li>
</ul>

<h3>Impact and Applications</h3>
<p>This framework enables:</p>
<ul>
  <li>Healthcare institutions to assess the security risks of deploying AI systems in clinical settings</li>
  <li>AI developers to identify and address vulnerabilities during the development phase</li>
  <li>Regulatory bodies to establish security standards for medical AI systems</li>
  <li>Researchers to benchmark and improve the robustness of medical VLMs</li>
</ul>

<h3>Team Members</h3>
<ul>
  <li>Binesh Sadanandan</li>
  <li>Dr. Vahid Behzadan</li>
</ul>

<h3>Publications</h3>
<p>Sadanandan, B., Behzadan, V. (2024). "VSF-Med: A Vulnerability Scoring Framework for Medical Vision-Language Models." arXiv preprint arXiv:2507.00052. Available at: <a href="https://arxiv.org/abs/2507.00052" target="_blank">https://arxiv.org/abs/2507.00052</a></p>
