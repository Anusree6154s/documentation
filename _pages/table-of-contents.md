---
permalink: /table-of-contents
layout: page
title: Table of Contents
---


<ul>
  {% for post in site.posts %}
    <li>
      <a href=".{{ post.url }}">{{ post.date | date: "%d %b %Y" }} - {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>