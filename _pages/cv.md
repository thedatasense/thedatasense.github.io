---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

You can download my full CV here: [Download CV (PDF)](/files/binesh_resume.pdf)

## Education

- **Ph.D. in Engineering and Applied Science - Data Science**, University of New Haven, 2021 - 2027
- **M.S. in Data Science**, University of Connecticut School of Business, 2017 - 2019
- **Nanodegree in Deep Learning**, Udacity, 2017
- **Advanced Diploma in PLC Controls and Design**, Anna University, 2008
- **B.E. in Electronics and Communication**, Cochin University of Science and Technology

## Work Experience

- **Senior Principal R&D Engineer (Technical Fellow)**, Medtronic Surgical Innovation
  - Improving state-of-the-art in minimally invasive therapies using data from conventional and non-conventional sources
  - Leading machine learning and software-driven systems development for medical technology

- **Ph.D. Research Assistant**, SAIL Lab, University of New Haven
  - Developing robust defense strategies for medical vision-language models
  - Researching visual adversarial attacks, detection mechanisms, and XAI-guided mitigation strategies

## Research Interests

- Medical Vision-Language Models and Robustness
- Adversarial Machine Learning in Healthcare AI
- Precision Oncology and Theranostics
- Fault Detection in Medical Devices
- Data-Driven Digital Twins

## Publications

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Portfolio

  <ul>{% for post in site.portfolio reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
