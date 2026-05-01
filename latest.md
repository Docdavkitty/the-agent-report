---
layout: default
title: All Articles
permalink: /latest/
---

<section class="latest-page">
  <header class="latest-header">
    <h1>All Articles</h1>
  </header>

  <div class="latest-list">
    {% for post in site.posts %}
      <a href="{{ post.url | relative_url }}" class="latest-item">
        {% if post.hero_image %}
          <img src="{{ post.hero_image | relative_url }}" alt="{{ post.title }}" class="latest-item-image" loading="lazy">
        {% endif %}
        <div class="latest-item-body">
          <div class="latest-item-meta">
            {% for cat in post.categories limit:1 %}
              <span class="category-badge" style="font-size:.65rem;padding:2px 8px;margin-bottom:4px;display:inline-block;">{{ cat | replace: '-', ' ' | capitalize }}</span>
            {% endfor %}
            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
          </div>
          <h2>{{ post.title }}</h2>
          <p>{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
        </div>
      </a>
    {% endfor %}
  </div>
</section>
