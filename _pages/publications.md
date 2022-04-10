---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<h3>Journal Publications</h3>

{% for post in site.publications reversed %}
{%if {{post.category}} == "published" %}
  {% include archive-single.html %}
{%endif%}
{% endfor %}

<h3>Proceedings or technical report </h3>

{% for post in site.publications reversed %}
{%if {{post.category}} == "report" %}
  {% include archive-single.html %}
{%endif%}
{% endfor %}