---
layout: page
title: Project 1 - Advanced Fault Detection in Medical Devices
description: Exploring the integration of complex electronics in medical devices and the application of Fault Detection and Prediction algorithms.
img: assets/img/3.jpg
importance: 1
category: work
giscus_comments: true
---

<h2>Project Overview</h2>

<p>“Project 2” delves into the rapidly evolving field of medical devices, focusing on the use of sophisticated electronics like microchips and FPGAs to improve the safety and performance of life-saving equipment. This project explores the complexities and challenges of these electro-mechanical systems, particularly in terms of failure modes that are difficult to detect with traditional testing methods.</p>

<p>The study investigates predictive and preventive maintenance strategies in medical devices, emphasizing fault detection techniques that utilize data, signal, process, or knowledge-based methods. These innovative techniques are critical for preempting failures that could lead to safety concerns or compromised device performance.</p>

<h3>Team Members</h3>
<ul>
  <li>Binesh Kumar</li>
  <li>Bahareh Arghavani Nobar</li>
  <li>Advisor: Dr. Vahid Behzadan</li>
</ul>

<h3>Research Scope</h3>
<p>The core of our research involves a comprehensive survey of state-of-the-art Fault Detection and Prediction algorithms. We aim to assess their feasibility and potential application in the medical device sector, thereby contributing to the development of safer and more reliable medical equipment.</p>

<div class="row">
    <!-- Include images related to the project -->
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/related_image_1.jpg" title="Medical Device Electronics" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/related_image_2.jpg" title="Fault Detection Research" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Top: Advanced electronics in medical devices. Bottom: Research on Fault Detection.
</div>

<!-- Additional project details or images can be included here -->

<h3>Publications</h3>
<p>In preparation: Sadanandan, B., Arghavani Nobar, B., Behzadan, V. (2023). “Analysis of Fault Detection in Medical Devices Leveraging Generative Machine Learning Methods.”</p>


The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}
s


