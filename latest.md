---
layout: default
title: All Articles
permalink: /latest/
---

<section class="latest-page">
  <header class="latest-header">
    <h1>All Articles</h1>
    <p style="color:var(--text-muted);margin-top:8px;">{{ site.posts.size }} articles and counting</p>
  </header>

  <div class="latest-list" id="latest-list">
    {% for post in site.posts %}
      <a href="{{ post.url | relative_url }}" class="latest-item{% if forloop.index > 10 %} latest-hidden{% endif %}">
        {% if post.hero_image %}
          <img src="{{ post.hero_image | relative_url }}" alt="{{ post.title | escape }}" class="latest-item-image" loading="lazy">
        {% endif %}
        <div class="latest-item-body">
          <div class="latest-item-meta">
            {% for cat in post.categories limit:1 %}
              <span class="category-badge" style="font-size:.65rem;padding:2px 8px;margin-bottom:4px;display:inline-block;">{{ cat | replace: '-', ' ' | capitalize }}</span>
            {% endfor %}
            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
          </div>
          <h2>{{ post.title | escape }}</h2>
          {% if post.reading_time %}<span class="card-reading-time" style="display:inline-block;margin-top:4px;">{{ post.reading_time }} min read</span>{% endif %}
          <p>{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
        </div>
      </a>
    {% endfor %}
  </div>

  {% if site.posts.size > 10 %}
  <div class="pagination" id="latest-pagination">
    <button class="load-more-btn" id="load-more-btn" onclick="loadMore()">Load more ({{ site.posts.size | minus: 10 }} remaining)</button>
  </div>
  {% endif %}
</section>

<script>
function loadMore() {
  var hidden = document.querySelectorAll('.latest-hidden');
  var batch = 10;
  for (var i = 0; i < batch && i < hidden.length; i++) {
    hidden[i].classList.remove('latest-hidden');
  }
  var remaining = document.querySelectorAll('.latest-hidden').length;
  var btn = document.getElementById('load-more-btn');
  if (remaining > 0) {
    btn.textContent = 'Load more (' + remaining + ' remaining)';
  } else {
    btn.parentElement.style.display = 'none';
  }
}
</script>
