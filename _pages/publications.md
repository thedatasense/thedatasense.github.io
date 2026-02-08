---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.publication_category %}
  {% for category in site.publication_category %}
    {% assign cat_pubs = site.publications | where: "category", category[0] | sort: "date" | reverse %}
    {% if cat_pubs.size > 0 %}
      <h2>{{ category[1].title }}</h2>
      {% for post in cat_pubs %}
        {% include archive-single.html %}
      {% endfor %}
    {% endif %}
  {% endfor %}
{% else %}
  {% assign sorted_pubs = site.publications | sort: "date" | reverse %}
  {% for post in sorted_pubs %}
    {% include archive-single.html %}
  {% endfor %}
{% endif %}
