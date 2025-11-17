---
layout: page
title: Publications
permalink: /publications/
---

<div class="publications-container" style="max-width: 1200px; margin: 0 auto; padding: 2rem 0;">
  
  <div class="publications-header" style="text-align: center; margin-bottom: 3rem;">
    <h1 style="font-size: 2.2rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; letter-spacing: -0.5px;">Publications</h1>
    <div class="divider" style="width: 60px; height: 1px; background: #a8c5e0; margin: 0 auto;"></div>
    <p style="color: #b0b0b0; margin-top: 1rem; font-size: 1rem;">
      All publications are automatically fetched from 
      <a href="https://scholar.google.com/citations?hl=en&user=okBrMn8AAAAJ&view_op=list_works&sortby=pubdate" target="_blank" style="color: #a8c5e0; text-decoration: none; font-weight: 400;">
        Google Scholar
      </a>
    </p>
  </div>

  <div class="publications-list" style="display: grid; gap: 2rem;">
    {% assign sorted_pubs = site.publications | sort: 'date' | reverse %}
    {% for pub in sorted_pubs limit: 5 %}
    <div class="publication-card" style="background: #1a1a1a; padding: 2rem; border-radius: 4px; border: 1px solid #2a2a2a; display: grid; grid-template-columns: 200px 1fr; gap: 2rem; transition: border-color 0.3s;">
      
      <!-- Publication Image -->
      <div class="publication-image" style="width: 200px; height: 200px; border-radius: 4px; overflow: hidden; background: #0f0f0f; display: flex; align-items: center; justify-content: center;">
        {% if pub.image %}
          <img src="{{ pub.image | relative_url }}" alt="{{ pub.title }}" style="width: 100%; height: 100%; object-fit: cover;">
        {% elsif pub.doi %}
          <img src="https://api.altmetric.com/v1/doi/{{ pub.doi }}/images/medium" alt="{{ pub.title }}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.style.display='none'; this.parentElement.innerHTML='<div style=\'color: #808080; font-size: 0.9rem; text-align: center; padding: 1rem;\'>No image available</div>';">
        {% elsif pub.link %}
          {% assign scholar_id = pub.link | split: 'citation_for_view=' | last | split: ':' | first %}
          <div style="color: #808080; font-size: 0.9rem; text-align: center; padding: 1rem; display: flex; align-items: center; justify-content: center; height: 100%;">
            <span style="opacity: 0.5;">📄</span>
          </div>
        {% else %}
          <div style="color: #808080; font-size: 0.9rem; text-align: center; padding: 1rem; display: flex; align-items: center; justify-content: center; height: 100%;">
            <span style="opacity: 0.5;">📄</span>
          </div>
        {% endif %}
      </div>
      
      <!-- Publication Content -->
      <div class="publication-content" style="flex: 1;">
        <h3 style="font-size: 1.3rem; color: #e8e8e8; margin-bottom: 0.8rem; font-weight: 400; line-height: 1.4;">
          {{ pub.title }}
        </h3>
        
        <p style="color: #808080; margin-bottom: 0.8rem; line-height: 1.6; font-size: 0.95rem;">
          {{ pub.authors }}
        </p>
        
        {% if pub.venue and pub.date %}
          {% assign pub_month = pub.date | date: "%b" %}
          <p style="color: #c4a8d8; font-weight: 400; margin-bottom: 1rem; font-size: 0.95rem;">
            {{ pub.venue }}, {{ pub_month }} {{ pub.date | date: "%Y" }}
          </p>
        {% elsif pub.venue %}
          <p style="color: #c4a8d8; font-weight: 400; margin-bottom: 1rem; font-size: 0.95rem;">{{ pub.venue }}</p>
        {% elsif pub.date %}
          {% assign pub_month = pub.date | date: "%b" %}
          <p style="color: #c4a8d8; font-weight: 400; margin-bottom: 1rem; font-size: 0.95rem;">{{ pub_month }} {{ pub.date | date: "%Y" }}</p>
        {% endif %}
        
        {% if pub.content %}
          <div class="publication-abstract" style="color: #b0b0b0; line-height: 1.7; font-size: 0.9rem; margin-bottom: 1rem;">
            {{ pub.content | markdownify | strip_html | truncatewords: 50 }}
          </div>
        {% endif %}
        
        <div class="publication-links" style="display: flex; gap: 1rem; flex-wrap: wrap;">
          {% if pub.cvf %}
          <a href="{{ pub.cvf }}" target="_blank" style="color: #a8c5e0; text-decoration: none; font-weight: 400; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
            CVF →
          </a>
          {% endif %}
          {% if pub.arxiv %}
          <a href="{{ pub.arxiv }}" target="_blank" style="color: #a8c5e0; text-decoration: none; font-weight: 400; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
            arXiv →
          </a>
          {% endif %}
          {% if pub.link %}
          <a href="{{ pub.link }}" target="_blank" style="color: #a8c5e0; text-decoration: none; font-weight: 400; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
            Google Scholar →
          </a>
          {% endif %}
          {% if pub.doi %}
          <a href="https://doi.org/{{ pub.doi }}" target="_blank" style="color: #a8c5e0; text-decoration: none; font-weight: 400; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
            DOI →
          </a>
          {% endif %}
        </div>
      </div>
    </div>
    {% endfor %}
    
    {% if sorted_pubs.size == 0 %}
    <div style="text-align: center; padding: 3rem; color: #808080;">
      <p>Publications are being loaded...</p>
      <p style="font-size: 0.9rem; margin-top: 1rem;">
        <a href="https://scholar.google.com/citations?hl=en&user=okBrMn8AAAAJ&view_op=list_works&sortby=pubdate" target="_blank" style="color: #a8c5e0; text-decoration: none;">
          View all publications on Google Scholar →
        </a>
      </p>
    </div>
    {% endif %}
    
    <div style="text-align: center; margin-top: 2rem;">
      <a href="https://scholar.google.com/citations?hl=en&user=okBrMn8AAAAJ&view_op=list_works&sortby=pubdate" target="_blank" style="display: inline-block; padding: 10px 24px; background: transparent; border: 1px solid #a8c5e0; color: #a8c5e0; text-decoration: none; border-radius: 4px; font-weight: 400; transition: all 0.3s; font-size: 0.95rem;">
        View All Publications on Google Scholar →
      </a>
    </div>
  </div>

</div>

<style>
@media (max-width: 768px) {
  .publication-card {
    grid-template-columns: 1fr !important;
  }
  .publication-image {
    width: 100% !important;
    height: 200px !important;
  }
}
</style>
