---
layout: default
title: Archive
permalink: /archive/
---

<section class="latest-page">
  <header class="latest-header">
    <h1>📆 Archive</h1>
    <p style="color:var(--text-muted);margin-top:8px;">All articles grouped by month</p>
  </header>

  {% assign posts_by_month = site.posts | group_by_exp: "post", "post.date | date: '%B %Y'" %}

  {% for month in posts_by_month %}
    <h2 style="font-size:1.4rem;font-weight:700;margin:32px 0 16px;padding-bottom:8px;border-bottom:1px solid var(--border);">
      {{ month.name }}
      <span style="font-size:.85rem;color:var(--text-dim);font-weight:400;">({{ month.items.size }} article{% if month.items.size > 1 %}s{% endif %})</span>
    </h2>
    <div class="latest-list" style="margin-bottom:24px;">
      {% for post in month.items %}
        <a href="{{ post.url | relative_url }}" class="latest-item">
          {% if post.hero_image %}
            <img src="{{ post.hero_image | relative_url }}" alt="{{ post.title }}" class="latest-item-image" loading="lazy">
          {% endif %}
          <div class="latest-item-body">
            <div class="latest-item-meta">
              {% for cat in post.categories limit:1 %}
                <span class="category-badge" style="font-size:.65rem;padding:2px 8px;margin-bottom:4px;display:inline-block;">{{ cat | replace: '-', ' ' | capitalize }}</span>
              {% endfor %}
              <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %d, %Y" }}</time>
            </div>
            <h2>{{ post.title }}</h2>
            <p>{{ post.excerpt | strip_html | truncatewords: 20 }}</p>
          </div>
        </a>
      {% endfor %}
    </div>
  {% endfor %}
</section>
