---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
  - /resume/
---

{% include base_path %}

You can download my full CV here: [Download CV (PDF)](/files/binesh_resume.pdf)

## Summary

I'm a Technical Fellow and senior data science leader with 10+ years building production machine learning, generative AI, and enterprise data platforms in regulated healthcare, on a 19-year engineering foundation. I advise senior leadership on machine learning strategy at Medtronic while finishing a Ph.D. in medical AI safety, mechanistic interpretability, and Large Language Model (LLM) and Vision-Language Model (VLM) evaluation (expected August 2026), with two patents and the publication record listed below.

## Experience

**Medtronic, Surgical Innovation** (North Haven, CT, 2015 - Present)

| Role | Years |
|---|---|
| Senior Principal R&D Engineer & Technical Fellow | 2023 - Present |
| Senior Principal R&D Engineer | 2021 - 2023 |
| Principal R&D Applications Engineer | 2016 - 2021 |
| Enterprise Solutions Consultant | 2015 - 2016 |

As Technical Fellow, I advise senior leadership on machine learning and data science strategy and mentor engineering teams across the organization. I lead data science and machine learning integration for surgical instruments: predictive models and generative AI for product development and device safety on AWS and Snowflake, retrieval-augmented generation (RAG) pipelines with vector databases for R&D document search, and analysis of MedDRA-coded adverse event data for post-market device safety surveillance. My team's models include multimodal deep learning for early prediction of ICU patient deterioration (Journal of Data Science, 2025) and generative models for early detection of device failures (ICMHI, 2024).

In earlier roles here, I led scientific and clinical evidence strategies for minimally invasive surgical staplers, built data pipelines with Dataiku, Python, Redshift, and Snowflake for clinical evidence generation, delivered Power BI dashboards for stakeholders, and architected Windchill product lifecycle management (PLM) solutions for R&D.

**Ph.D. Researcher, SAIL Lab, University of New Haven** (2021 - Present)

My dissertation studies paraphrase sensitivity failures in medical vision-language models: clinically equivalent questions that produce contradictory diagnoses. I built the PSF-Med benchmark, applied sparse-autoencoder interpretability to locate causative features, and used mechanistically guided Low-Rank Adaptation (LoRA) interventions to cut diagnosis flip rates. The benchmarks, models, and code are open on [Hugging Face](https://huggingface.co/datasets/saillab/psf-med) and [GitHub](https://github.com/UNHSAILLab/psf-med).

**Earlier career**

| Role | Company | Years |
|---|---|---|
| Technical Architect (PLM) & Application Consultant | Barry-Wehmiller Design Group | 2012 - 2015 |
| Product Specialist & Enterprise Support Engineer | PTC | 2010 - 2012 |
| Infrastructure Engineer | Hewlett Packard Enterprise | 2009 - 2010 |
| Technical Associate | Minacs | 2007 - 2009 |

## Education

| Degree | Institution | Years |
|---|---|---|
| Ph.D., Engineering and Applied Science (Data Science) | University of New Haven | 2021 - present, expected August 2026 |
| M.S., Data Science (GPA 3.92) | University of Connecticut School of Business | 2017 - 2019 |
| B.E., Electronics and Communication | Cochin University of Science and Technology | 2004 - 2008 |

Certifications: Tableau Desktop Specialist; Deep Learning Nanodegree, Udacity (2017); Certificate in Project Management.

## Skills

| Area | Tools and methods |
|---|---|
| Machine Learning & GenAI | Production ML (batch and real-time inference), predictive modeling, deep learning, LLM/VLM evaluation, retrieval-augmented generation (RAG), vector databases, prompt engineering |
| Responsible AI | Robustness and bias evaluation, failure-mode analysis, model monitoring, clinical AI safety |
| Data Platforms | AWS, Snowflake, Redshift, Databricks, Azure ML, Dataiku, lakehouse and pipeline architecture, data governance, PLM/Windchill, APIs and data services |
| Analytics & Visualization | Python, SQL, R, statistics, exploratory data analysis, anomaly detection, Power BI, Tableau, Plotly/Dash |
| Health Data | DICOM, MedDRA, clinical evidence generation |

## Professional Service

I serve as a peer reviewer for ICLR 2026, MICCAI 2026, Machine Learning for Healthcare (MLHC) 2026, and IEEE ICMLA 2026, and I was Lead Reviewer for the International Medical Devices Safety Conference in 2024 and 2025.

## Publications

<ul>{% for post in site.publications reversed %}
{% include archive-single-cv.html %}
{% endfor %}</ul>

## Portfolio

<ul>{% for post in site.portfolio reversed %}
{% include archive-single-cv.html %}
{% endfor %}</ul>
