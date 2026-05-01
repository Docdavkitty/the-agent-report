---
layout: default
title: Archive
permalink: /archive/
---

<section class="latest-page">
  <header class="latest-header">
    <h1>📆 Archive</h1>
    <p style="color:var(--text-muted);margin-top:8px;">All {{ site.posts.size }} articles grouped by month</p>
  </header>

  {% assign posts_by_month = site.posts | group_by_exp: "post", "post.date | date: '%B %Y'" %}
  {% assign global_idx = 0 %}

  {% for month in posts_by_month %}
    {% assign month_size = month.items.size %}
    <h2 style="font-size:1.4rem;font-weight:700;margin:32px 0 16px;padding-bottom:8px;border-bottom:1px solid var(--border);">
      {{ month.name }}
      <span style="font-size:.85rem;color:var(--text-dim);font-weight:400;">({{ month_size }} article{% if month_size > 1 %}s{% endif %})</span>
    </h2>
    <div class="latest-list" style="margin-bottom:24px;">
      {% for post in month.items %}
        {% assign global_idx = global_idx | plus: 1 %}
        <a href="{{ post.url | relative_url }}" class="latest-item{% if global_idx > 15 %} archive-hidden{% endif %}">
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
            {% if post.reading_time %}<span class="card-reading-time" style="display:inline-block;margin-top:4px;">{{ post.reading_time }} min read</span>{% endif %}
            <p>{{ post.excerpt | strip_html | truncatewords: 20 }}</p>
          </div>
        </a>
      {% endfor %}
    </div>
  {% endfor %}

  {% if global_idx > 15 %}
  <div class="pagination" id="archive-pagination">
    <button class="load-more-btn" id="archive-load-more" onclick="loadMoreArchive()">Load more ({{ global_idx | minus: 15 }} remaining)</button>
  </div>
  {% endif %}
</section>

<script>
function loadMoreArchive() {
  var hidden = document.querySelectorAll('.archive-hidden');
  var batch = 10;
  for (var i = 0; i < batch && i < hidden.length; i++) {
    hidden[i].classList.remove('archive-hidden');
  }
  var remaining = document.querySelectorAll('.archive-hidden').length;
  var btn = document.getElementById('archive-load-more');
  if (remaining > 0) {
    btn.textContent = 'Load more (' + remaining + ' remaining)';
  } else {
    btn.parentElement.style.display = 'none';
  }
}
</script>
