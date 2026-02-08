---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% for category in site.publication_category %}
{% assign cat_pubs = site.publications | where: "pub_type", category[0] | sort: "date" | reverse %}
{% if cat_pubs.size > 0 %}
<h2>{{ category[1].title }}</h2>
{% for post in cat_pubs %}
{% include archive-single.html %}
{% endfor %}
{% endif %}
{% endfor %}
