---
permalink: /all-posts
layout: page
---

<div class='all-posts'>

<div class='heading'>
  <p><span>All Posts</span></p>
  <p>Chronicles in Progress</p>
  <p>An archive of my journey through tech and design.</p>
  <div class='background-container'>
    <div class='background background1'><div class='background-inner'></div></div>
    <div class='background background2'><div class='background-inner'></div></div>
    <div class='background background2'><div class='background-inner'></div></div>
  </div>
</div>

<div class='post-list'>
  {% for post in site.posts %}
  {% unless post.hidden %}
  {% assign post_count = post_count | plus: 1 %}
  {% endunless %}
  {% endfor %}
  <p class='total-posts'><span>Total Posts: {{ post_count }}</span></p>
  <div class='list'>
    {% for post in site.posts %}
    {% unless post.hidden %}
      <a href=".{{ post.url }}">
        <div class='content'>
          <p class='arrow'></p>
          <div class='content-inner'>
            <p class='title'>{{ post.title }}</p>
            <p class='excerpt'>{{ post.excerpt }}</p>
            <p>
              {%- if post.tags.size>0 -%}
              <span class='tag-title'>TAGS: </span>
                {%- for tag in post.tags -%}
                    <span class='tags'>{{ tag | escape }},</span>
                  {%- endfor -%} 
                {%- endif -%}
            </p>
          </div>
        </div>
        <span class='date'>{{ post.date | date: "%d/%m/%Y" }}</span>
      </a>
    {% endunless %}
    {% endfor %}
  </div>
</div>


  

</div>