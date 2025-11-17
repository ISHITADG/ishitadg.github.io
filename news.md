---
layout: page
title: Latest News
permalink: /news/
---

<div class="news-container" style="max-width: 1000px; margin: 0 auto; padding: 2rem 0;">
  
  <div class="news-header" style="text-align: center; margin-bottom: 3rem;">
    <h1 style="font-size: 2.2rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; letter-spacing: -0.5px;">Latest News</h1>
    <div class="divider" style="width: 60px; height: 1px; background: #a8c5e0; margin: 0 auto;"></div>
    <p style="color: #b0b0b0; margin-top: 1rem; font-size: 1rem;">Recent publications, workshops, and research highlights</p>
  </div>

  <!-- Recent Publications Section -->
  <section id="publications" class="news-section" style="margin-bottom: 4rem;">
    <h2 style="font-size: 2rem; color: #e8e8e8; margin-bottom: 2rem; border-left: 2px solid #a8c5e0; padding-left: 1rem; font-weight: 400;">
      Recent Publications
    </h2>
    
    <div class="publications-list" style="display: grid; gap: 1.5rem;">
      {% assign sorted_pubs = site.publications | sort: 'date' | reverse %}
      {% for pub in sorted_pubs limit: 7 %}
      <div class="publication-card" style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border-left: 2px solid #a8c5e0; border: 1px solid #2a2a2a; transition: border-color 0.3s;">
        <h3 style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 0.8rem; font-weight: 400; line-height: 1.5;">
          {{ pub.title }}
        </h3>
        <p style="color: #808080; margin-bottom: 0.6rem; line-height: 1.6; font-size: 0.9rem;">
          {{ pub.authors }}
        </p>
        {% if pub.venue %}
        <p style="color: #c4a8d8; font-weight: 400; margin-bottom: 0.5rem; font-size: 0.9rem;">
          {{ pub.venue }}
        </p>
        {% endif %}
        {% if pub.year %}
        <p style="color: #666; font-size: 0.85rem; margin-bottom: 1rem;">
          {{ pub.year }}
        </p>
        {% endif %}
        {% if pub.link %}
        <a href="{{ pub.link }}" target="_blank" style="color: #a8c5e0; text-decoration: none; font-weight: 400; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
          View on Google Scholar →
        </a>
        {% endif %}
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
        <a href="{{ '/publications/' | relative_url }}" style="display: inline-block; padding: 10px 24px; background: transparent; border: 1px solid #a8c5e0; color: #a8c5e0; text-decoration: none; border-radius: 4px; font-weight: 400; transition: all 0.3s; font-size: 0.95rem;">
          View All Publications
        </a>
      </div>
    </div>
  </section>

  <!-- Workshop Section -->
  <section id="workshop" class="news-section" style="margin-bottom: 4rem;">
    <h2 style="font-size: 1.8rem; color: #e8e8e8; margin-bottom: 2rem; border-left: 2px solid #c4a8d8; padding-left: 1rem; font-weight: 400;">
      Workshop Organization
    </h2>
    
    <div class="workshop-card" style="background: #1a1a1a; padding: 2.5rem; border-radius: 4px; border: 1px solid #2a2a2a; color: #e8e8e8;">
      <div class="workshop-header" style="display: flex; align-items: center; margin-bottom: 1.5rem;">
        <div class="workshop-icon" style="font-size: 3rem; margin-right: 1.5rem;">🎓</div>
        <div>
          <h3 style="font-size: 1.8rem; margin-bottom: 0.5rem;">SVU 2025 Workshop</h3>
          <p style="opacity: 0.9; font-size: 1.1rem;">The First Workshop on Short-Form Video Understanding</p>
        </div>
      </div>
      
      <div class="workshop-details" style="margin-bottom: 1.5rem;">
        <p style="margin-bottom: 0.8rem; line-height: 1.6; color: #b0b0b0;">
          <strong style="color: #e8e8e8;">Venue:</strong> ICCV 2025, Room 313B, Hawai'i Convention Center
        </p>
        <p style="margin-bottom: 0.8rem; line-height: 1.6; color: #b0b0b0;">
          <strong style="color: #e8e8e8;">Date:</strong> October 19, 2025, 1 PM - 5 PM HST, Honolulu, Hawai'i, USA
        </p>
        <p style="line-height: 1.7; margin-bottom: 1.5rem; color: #b0b0b0; font-size: 0.95rem;">
          I recently co-organized this workshop alongside colleagues from Adobe Research and other institutions in October 2025. The workshop explored the challenges and opportunities in understanding short-form videos across social media, marketing, business, and other domains. Short-form videos present unique challenges—rapid editing patterns, engagement-driven narratives, platform-specific formats—that differ fundamentally from traditional long-form video understanding, making them increasingly embedded in our daily lives as sources of entertainment, information, and communication.
        </p>
      </div>
      
      <div class="workshop-highlights" style="background: #0f0f0f; padding: 1.5rem; border-radius: 4px; margin-bottom: 1.5rem; border: 1px solid #2a2a2a;">
        <h4 style="font-size: 1.1rem; margin-bottom: 1rem; color: #e8e8e8; font-weight: 400;">Workshop Topics:</h4>
        <ul style="list-style: none; padding: 0; line-height: 1.8; color: #b0b0b0;">
          <li style="margin-bottom: 0.5rem;">• SV Data Collection and Benchmarking</li>
          <li style="margin-bottom: 0.5rem;">• SV Analysis and Understanding</li>
          <li style="margin-bottom: 0.5rem;">• New Research Frontiers in SV</li>
          <li>• Detection, Generation, and Evaluation of Short-Form Videos</li>
        </ul>
      </div>
      
      <div class="workshop-links" style="display: flex; gap: 1rem; flex-wrap: wrap;">
        <a href="https://short-form-video-understanding.github.io/" target="_blank" 
           style="background: transparent; border: 1px solid #a8c5e0; color: #a8c5e0; padding: 10px 24px; border-radius: 4px; text-decoration: none; font-weight: 400; transition: all 0.3s; display: inline-block; font-size: 0.95rem;">
          Visit Workshop Website →
        </a>
        <a href="https://short-form-video-understanding.github.io/#submission" target="_blank"
           style="background: transparent; border: 1px solid #c4a8d8; color: #c4a8d8; padding: 10px 24px; border-radius: 4px; text-decoration: none; font-weight: 400; transition: all 0.3s; display: inline-block; font-size: 0.95rem;">
          Submission Guidelines →
        </a>
      </div>
    </div>
  </section>

  <!-- Other News Section -->
  <section id="other-news" class="news-section">
    <h2 style="font-size: 1.8rem; color: #e8e8e8; margin-bottom: 2rem; border-left: 2px solid #d4b5b5; padding-left: 1rem; font-weight: 400;">
      Other Updates
    </h2>
    
    <div class="updates-list">
      <div class="update-item" style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; margin-bottom: 1rem; border-left: 2px solid #a8c5e0; border: 1px solid #2a2a2a;">
        <p style="color: #808080; font-size: 0.9rem; margin-bottom: 0.5rem;">Stay tuned for more updates!</p>
        <p style="color: #b0b0b0;">This section will be updated with recent achievements, conference presentations, and other professional activities.</p>
      </div>
    </div>
  </section>

</div>

<style>
.workshop-links a:hover {
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .workshop-header {
    flex-direction: column;
    text-align: center;
  }
  .workshop-icon {
    margin-right: 0 !important;
    margin-bottom: 1rem;
  }
  .workshop-links {
    flex-direction: column;
  }
  .workshop-links a {
    text-align: center;
  }
}
</style>

<script>
// This will be populated by the Google Scholar scraper
// For now, it's a placeholder that will be updated when publications are fetched
document.addEventListener('DOMContentLoaded', function() {
  // Placeholder for dynamic content loading
  console.log('News page loaded - publications will be populated by GitHub Actions');
});
</script>

