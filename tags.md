---
layout: default
title: Tags
permalink: /tags/
---

<section class="latest-page">
  <header class="latest-header">
    <h1>🏷️ Tags</h1>
    <p style="color:var(--text-muted);margin-top:8px;">Browse articles by topic</p>
  </header>

  {% assign all_tags = "" | split: "" %}
  {% for post in site.posts %}
    {% for tag in post.tags %}
      {% assign all_tags = all_tags | push: tag %}
    {% endfor %}
  {% endfor %}
  {% assign all_tags = all_tags | uniq | sort %}

  <div class="tag-cloud" style="margin-bottom:40px;display:flex;flex-wrap:wrap;gap:10px;">
    {% for tag in all_tags %}
      {% assign count = 0 %}
      {% for post in site.posts %}{% if post.tags contains tag %}{% assign count = count | plus: 1 %}{% endif %}{% endfor %}
      <a href="#{{ tag | slugify }}" class="tag" style="font-size:{% if count > 3 %}1.1rem{% elsif count > 1 %}0.95rem{% else %}0.8rem{% endif %};padding:6px 16px;">
        {{ tag }} <span style="opacity:.6;">({{ count }})</span>
      </a>
    {% endfor %}
  </div>

  <div class="latest-list">
    {% for tag in all_tags %}
      <h2 id="{{ tag | slugify }}" style="font-size:1.3rem;font-weight:700;margin:32px 0 16px;padding-bottom:8px;border-bottom:1px solid var(--border);"># {{ tag }}</h2>
      {% for post in site.posts %}
        {% if post.tags contains tag %}
          <a href="{{ post.url | relative_url }}" class="latest-item">
            {% if post.hero_image %}
              <img src="{{ post.hero_image | relative_url }}" alt="{{ post.title }}" class="latest-item-image" loading="lazy">
            {% endif %}
            <div class="latest-item-body">
              <div class="latest-item-meta">
                <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
              </div>
              <h2>{{ post.title }}</h2>
            </div>
          </a>
        {% endif %}
      {% endfor %}
    {% endfor %}
  </div>
</section>
