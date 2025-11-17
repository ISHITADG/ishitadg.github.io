---
layout: page
title: Publications
permalink: /publications/
---

<div class="publications-container" style="max-width: 1000px; margin: 0 auto; padding: 2rem 0;">
  
  <div class="publications-header" style="text-align: center; margin-bottom: 3rem;">
    <h1 style="font-size: 2.5rem; color: #333; margin-bottom: 1rem;">Publications</h1>
    <div class="divider" style="width: 100px; height: 4px; background: linear-gradient(90deg, #667eea, #764ba2); margin: 0 auto;"></div>
    <p style="color: #666; margin-top: 1rem; font-size: 1.1rem;">
      All publications are automatically fetched from 
      <a href="https://scholar.google.com/citations?hl=en&user=okBrMn8AAAAJ&view_op=list_works&sortby=pubdate" target="_blank" style="color: #667eea; text-decoration: none; font-weight: 600;">
        Google Scholar
      </a>
      <span style="margin: 0 10px;">|</span>
      <a href="https://scholar.google.com/citations?hl=en&user=okBrMn8AAAAJ&view_op=list_works&sortby=pubdate" target="_blank" style="color: #764ba2; text-decoration: none; font-weight: 600; padding: 8px 16px; background: #f8f9fa; border-radius: 5px; display: inline-block; margin-top: 10px;">
        View All Publications on Google Scholar →
      </a>
    </p>
  </div>

  <div id="publications-list" class="publications-list">
    <!-- Publications will be dynamically loaded here by the Google Scholar scraper -->
    <div class="loading-message" style="text-align: center; padding: 3rem; color: #666; font-style: italic;">
      <p>Loading publications from Google Scholar...</p>
      <p style="font-size: 0.9rem; margin-top: 1rem;">Publications are automatically updated via GitHub Actions.</p>
    </div>
  </div>

</div>

<style>
.publication-item {
  background: white;
  padding: 2rem;
  margin-bottom: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  border-left: 4px solid #667eea;
}

.publication-item:hover {
  transform: translateX(5px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.publication-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 0.5rem;
}

.publication-authors {
  color: #666;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.publication-venue {
  color: #764ba2;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.publication-year {
  color: #999;
  font-size: 0.9rem;
}

.publication-links {
  margin-top: 1rem;
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.publication-links a {
  color: #667eea;
  text-decoration: none;
  font-size: 0.9rem;
  padding: 4px 12px;
  border: 1px solid #667eea;
  border-radius: 4px;
  transition: background 0.3s, color 0.3s;
}

.publication-links a:hover {
  background: #667eea;
  color: white;
}
</style>

