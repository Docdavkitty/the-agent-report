---
layout: default
title: Search
permalink: /search/
---

<section class="search-page">
  <header class="search-header">
    <h1>🔍 Search Articles</h1>
    <p style="color:var(--text-muted);margin-top:8px;">Search across all articles by title, content, tags, and categories.</p>
  </header>

  <div class="search-box">
    <input type="text" id="search-input" class="search-input" placeholder="Type to search..." autocomplete="off" autofocus>
    <span class="search-icon">🔍</span>
  </div>

  <div class="search-stats" id="search-stats"></div>
  <div class="search-results" id="search-results"></div>

  <div class="search-noquery" id="search-noquery">
    <p>Start typing above to search through all articles.</p>
  </div>
</section>

<script>
(function() {
  var posts = [
    {% for post in site.posts %}
    {
      title: {{ post.title | jsonify }},
      url: '{{ post.url | relative_url }}',
      excerpt: {{ post.excerpt | strip_html | strip_newlines | jsonify }},
      date: '{{ post.date | date: "%B %-d, %Y" }}',
      categories: {{ post.categories | jsonify }},
      tags: {{ post.tags | jsonify }},
      reading_time: {{ post.reading_time | default: 3 }},
      hero_image: {% if post.hero_image %}'{{ post.hero_image | relative_url }}'{% else %}''{% endif %}
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  var stats = document.getElementById('search-stats');
  var noquery = document.getElementById('search-noquery');

  function normalize(text) {
    return text.toLowerCase().replace(/[^a-z0-9\s]/g, '');
  }

  function search(query) {
    if (!query.trim()) {
      results.innerHTML = '';
      stats.textContent = '';
      noquery.style.display = 'block';
      return;
    }
    noquery.style.display = 'none';

    var terms = normalize(query).split(/\s+/).filter(Boolean);
    var scored = [];

    posts.forEach(function(post) {
      var title = normalize(post.title);
      var excerpt = normalize(post.excerpt || '');
      var cats = normalize(post.categories.join(' '));
      var tags = normalize(post.tags.join(' '));
      var allText = title + ' ' + excerpt + ' ' + cats + ' ' + tags;
      var score = 0;

      terms.forEach(function(term) {
        var count = (allText.split(term).length - 1);
        var titleCount = (title.split(term).length - 1);
        var tagCount = (tags.split(term).length - 1);
        score += count + titleCount * 3 + tagCount * 2;
      });

      if (score > 0) {
        scored.push({ post: post, score: score });
      }
    });

    scored.sort(function(a, b) { return b.score - a.score; });

    if (scored.length === 0) {
      stats.textContent = 'No results found for "' + query + '"';
      results.innerHTML = '';
      return;
    }

    stats.textContent = scored.length + ' result' + (scored.length > 1 ? 's' : '') + ' for "' + query + '"';

    var html = '';
    scored.forEach(function(item) {
      var p = item.post;
      var img = p.hero_image ? '<img src="' + p.hero_image + '" alt="" class="search-result-image" loading="lazy">' : '';
      var catHtml = p.categories.length > 0 ? p.categories[0].replace(/-/g, ' ').replace(/\b\w/g, function(l){return l.toUpperCase();}) : '';
      html += '<a href="' + p.url + '" class="search-result">' +
        img +
        '<div class="search-result-body">' +
        '<div class="search-result-meta">' +
        '<span class="category-badge" style="font-size:.65rem;padding:2px 8px;display:inline-block;">' + catHtml + '</span>' +
        ' <time>' + p.date + '</time>' +
        ' · <span>' + p.reading_time + ' min read</span>' +
        '</div>' +
        '<h2>' + p.title + '</h2>' +
        '<p>' + p.excerpt + '</p>' +
        '</div>' +
        '</a>';
    });
    results.innerHTML = html;
  }

  input.addEventListener('input', function() {
    search(this.value);
  });
})();
</script>
