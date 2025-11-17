---
layout: page
title: Research
permalink: /publications/
---

<div class="publications-container" style="max-width: 1200px; margin: 0 auto; padding: 2rem 0;">
  
  <div class="publications-header" style="text-align: center; margin-bottom: 3rem;">
    <h1 style="font-size: 2.2rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; letter-spacing: -0.5px;">Research</h1>
    <div class="divider" style="width: 60px; height: 1px; background: #a8c5e0; margin: 0 auto;"></div>
  </div>

  <!-- Publications Section -->
  <section id="publications-section" style="margin-bottom: 4rem;">
    <h2 style="font-size: 1.8rem; color: #e8e8e8; margin-bottom: 2rem; border-left: 2px solid #a8c5e0; padding-left: 1rem; font-weight: 400;">
      Publications
    </h2>

    <div class="publications-list" style="display: grid; gap: 2rem;">
    {% assign sorted_pubs = site.publications | where_exp: "pub", "pub.date != nil" | sort: 'date' | reverse %}
    {% for pub in sorted_pubs limit: 5 %}
    <div class="publication-card" style="background: #1a1a1a; padding: 2rem; border-radius: 4px; border: 1px solid #2a2a2a; display: grid; grid-template-columns: 200px 1fr; gap: 2rem; transition: border-color 0.3s;">
      
      <!-- Publication Image -->
      <div class="publication-image" style="width: 200px; height: 200px; border-radius: 4px; overflow: hidden; background: #0f0f0f; display: flex; align-items: center; justify-content: center;">
        {% if pub.image %}
          <a href="{{ pub.url | relative_url }}" style="display: block; width: 100%; height: 100%; cursor: pointer;">
            <img src="{{ pub.image | relative_url }}" alt="{{ pub.title }}" style="width: 100%; height: 100%; object-fit: cover; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">
          </a>
        {% elsif pub.doi %}
          <a href="{{ pub.url | relative_url }}" style="display: block; width: 100%; height: 100%; cursor: pointer;">
            <img src="https://api.altmetric.com/v1/doi/{{ pub.doi }}/images/medium" alt="{{ pub.title }}" style="width: 100%; height: 100%; object-fit: cover; transition: opacity 0.3s;" onerror="this.style.display='none'; this.parentElement.innerHTML='<div style=\'color: #808080; font-size: 0.9rem; text-align: center; padding: 1rem;\'>No image available</div>';" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">
          </a>
        {% elsif pub.link %}
          <a href="{{ pub.url | relative_url }}" style="display: block; width: 100%; height: 100%; cursor: pointer; text-decoration: none;">
            <div style="color: #808080; font-size: 0.9rem; text-align: center; padding: 1rem; display: flex; align-items: center; justify-content: center; height: 100%; transition: color 0.3s;" onmouseover="this.style.color='#a8c5e0'" onmouseout="this.style.color='#808080'">
              <span style="opacity: 0.5;">📄</span>
            </div>
          </a>
        {% else %}
          <a href="{{ pub.url | relative_url }}" style="display: block; width: 100%; height: 100%; cursor: pointer; text-decoration: none;">
            <div style="color: #808080; font-size: 0.9rem; text-align: center; padding: 1rem; display: flex; align-items: center; justify-content: center; height: 100%; transition: color 0.3s;" onmouseover="this.style.color='#a8c5e0'" onmouseout="this.style.color='#808080'">
              <span style="opacity: 0.5;">📄</span>
            </div>
          </a>
        {% endif %}
      </div>
      
      <!-- Publication Content -->
      <div class="publication-content" style="flex: 1;">
        <h3 style="font-size: 1.3rem; color: #e8e8e8; margin-bottom: 0.5rem; font-weight: 400; line-height: 1.4;">
          {{ pub.title }}
        </h3>
        <p style="color: #808080; margin-bottom: 0.4rem; line-height: 1.6; font-size: 0.95rem;">
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
  </section>

  <!-- Patents Section -->
  <section id="patents-section">
    <h2 style="font-size: 1.8rem; color: #e8e8e8; margin-bottom: 2rem; border-left: 2px solid #c4a8d8; padding-left: 1rem; font-weight: 400;">
      Patents
    </h2>
    
    <div class="patents-list" style="display: grid; gap: 2rem;">
      <div class="patent-card" style="background: #1a1a1a; padding: 2rem; border-radius: 4px; border: 1px solid #2a2a2a; transition: border-color 0.3s;">
        <h3 style="font-size: 1.3rem; color: #e8e8e8; margin-bottom: 0.5rem; font-weight: 400; line-height: 1.4;">
          Enhancing artificial intelligence responses with contextual usage insights
        </h3>
        <p style="color: #808080; margin-bottom: 0.4rem; line-height: 1.6; font-size: 0.95rem;">
          Akash Vivek Maharaj, Vaishnavi Muppala, Shivakumar Vaithyanathan, Manas Garg, Kenneth George Russell, <strong style="color: #e8e8e8;">Ishita Dasgupta</strong>, Anup Bandigadi Rao, Aleksander Pejcic
        </p>
        <p style="color: #c4a8d8; font-weight: 400; margin-bottom: 1rem; font-size: 0.95rem;">
          US20250315460A1, Filed: Apr 2024, Published: Oct 2025
        </p>
        <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.9rem; margin-bottom: 1rem;">
          A system and method for enhancing AI assistant responses with contextual usage insights. The system determines whether to add contextual usage data to responses generated from application documentation, providing relevant context about how applications are being used.
        </p>
        <div class="patent-links" style="display: flex; gap: 1rem; flex-wrap: wrap;">
          <a href="https://patents.google.com/patent/US20250315460A1/en" target="_blank" style="color: #a8c5e0; text-decoration: none; font-weight: 400; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
            View Patent →
          </a>
        </div>
      </div>
    </div>
  </section>

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
