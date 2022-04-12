---
layout: archive
title: "Tutorials"
permalink: /tutorials/
author_profile: true
---

I gather here tutorials on various subject, given over the years,
in there most up-to-date form.

{% include base_path %}


{% for post in site.tutorials reversed %}
  {% include archive-single.html %}
{% endfor %}

