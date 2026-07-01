---
layout: default
title: Latest Articles
permalink: /latest/
---

<section class="latest-page">
  <header class="latest-header">
    <h1>📋 All Articles</h1>
    <p style="color:var(--text-muted);margin-top:8px;">Every article from The Agent Report, newest first.</p>
  </header>

  <div class="latest-list">
    {% for post in site.posts %}
      <a href="{{ post.url | relative_url }}" class="latest-item">
        <img
          src="{% if post.hero_image %}{{ post.hero_image | relative_url }}{% else %}https://placehold.co/240x180/1a1a2e/888899?text=Article{% endif %}"
          alt="{{ post.title | escape }}"
          class="latest-item-image"
          loading="lazy"
        >
        <div class="latest-item-body">
          <div class="latest-item-meta">
            {% for cat in post.categories limit:1 %}
              <span class="category-badge {{ cat | slugify }}" style="font-size:.65rem;padding:2px 8px;margin-right:8px;">{{ cat | replace: '-', ' ' | capitalize }}</span>
            {% endfor %}
            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
            {% if post.reading_time %} · {{ post.reading_time }} min read{% endif %}
          </div>
          <h2>{{ post.title | escape }}</h2>
          <p>{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
        </div>
      </a>
    {% endfor %}
  </div>
</section>
