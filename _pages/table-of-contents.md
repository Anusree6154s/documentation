---
permalink: /table-of-contents
layout: page
title: Table of Contents
---

{% for post in site.posts %}
{% unless post.hidden %}
{% assign post_count = post_count | plus: 1 %}
{% endunless %}
{% endfor %}

<p style="color:gray; margin-left:20px;">Total Posts: {{ post_count }}</p>


<ul>
  {% for post in site.posts %}
  {% unless post.hidden %}
    <li>
      <a href=".{{ post.url }}">{{ post.date | date: "%d %b %Y" }} - {{ post.title }}</a>
    </li>
  {% endunless %}
  {% endfor %}
</ul>

