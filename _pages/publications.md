---
layout: editorial
title: "Publications"
permalink: /publications/
eyebrow: "Peer-reviewed work + preprints + patents"
lead: "Research on reliable medical AI, intelligent surgical systems, and data-driven clinical decision support—organized for scanning, not citation hunting."
author_profile: false
---

<p class="editorial-intro">My recent work centers on one question: what evidence should we demand before trusting an AI system in a high-consequence setting?</p>

<section class="editorial-section" aria-label="Publication list">
{% for category in site.publication_category %}
{% assign cat_pubs = site.publications | where: "pub_type", category[0] | sort: "date" | reverse %}
{% if cat_pubs.size > 0 %}
  <section class="publication-section" aria-labelledby="publication-category-{{ category[0] }}">
    <div class="publication-section__head">
      <h2 id="publication-category-{{ category[0] }}">{{ category[1].title }}</h2>
      <span>{{ cat_pubs.size | prepend: '0' | slice: -2, 2 }} items</span>
    </div>
    <div class="publication-grid">
      {% for post in cat_pubs %}
        {% include publication-card.html post=post %}
      {% endfor %}
    </div>
  </section>
{% endif %}
{% endfor %}
</section>
