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

<h2>Preprint </h2>

{% for post in site.publications reversed %}
{%if {{post.category}} == "preprint" %}
  {% include archive-single.html %}
{%endif%}
{% endfor %}

<h2>Journal Publications</h2>

{% for post in site.publications reversed %}
{%if {{post.category}} == "published" %}
  {% include archive-single.html %}
{%endif%}
{% endfor %}

<h2>Proceedings or technical report </h2>

{% for post in site.publications reversed %}
{%if {{post.category}} == "report" %}
  {% include archive-single.html %}
{%endif%}
{% endfor %}