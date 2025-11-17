---
layout: page
title: Latest News
permalink: /news/
---

<div class="news-container" style="max-width: 1000px; margin: 0 auto; padding: 2rem 0;">
  
  <div class="news-header" style="text-align: center; margin-bottom: 3rem;">
    <h1 style="font-size: 2.5rem; color: #333; margin-bottom: 1rem;">Latest News</h1>
    <div class="divider" style="width: 100px; height: 4px; background: linear-gradient(90deg, #667eea, #764ba2); margin: 0 auto;"></div>
    <p style="color: #666; margin-top: 1rem; font-size: 1.1rem;">Recent publications, workshops, and research highlights</p>
  </div>

  <!-- Recent Publications Section -->
  <section id="publications" class="news-section" style="margin-bottom: 4rem;">
    <h2 style="font-size: 2rem; color: #333; margin-bottom: 2rem; border-left: 4px solid #667eea; padding-left: 1rem;">
      Recent Publications (Last 3 Months)
    </h2>
    
    <div id="recent-publications" class="publications-list">
      <div class="loading-message" style="text-align: center; padding: 3rem; color: #666; font-style: italic;">
        <p>Loading recent publications from Google Scholar...</p>
        <p style="font-size: 0.9rem; margin-top: 1rem;">Publications published in the last 3 months will appear here automatically.</p>
      </div>
    </div>
  </section>

  <!-- Workshop Section -->
  <section id="workshop" class="news-section" style="margin-bottom: 4rem;">
    <h2 style="font-size: 2rem; color: #333; margin-bottom: 2rem; border-left: 4px solid #764ba2; padding-left: 1rem;">
      Workshop Organization
    </h2>
    
    <div class="workshop-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2.5rem; border-radius: 16px; color: white; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">
      <div class="workshop-header" style="display: flex; align-items: center; margin-bottom: 1.5rem;">
        <div class="workshop-icon" style="font-size: 3rem; margin-right: 1.5rem;">🎓</div>
        <div>
          <h3 style="font-size: 1.8rem; margin-bottom: 0.5rem;">SVU 2025 Workshop</h3>
          <p style="opacity: 0.9; font-size: 1.1rem;">The First Workshop on Short-Form Video Understanding</p>
        </div>
      </div>
      
      <div class="workshop-details" style="margin-bottom: 1.5rem;">
        <p style="margin-bottom: 0.8rem; line-height: 1.6;">
          <strong>Venue:</strong> ICCV 2025, Room 313B, Hawai'i Convention Center
        </p>
        <p style="margin-bottom: 0.8rem; line-height: 1.6;">
          <strong>Date:</strong> October 19, 2025, 1 PM - 5 PM HST, Honolulu, Hawai'i, USA
        </p>
        <p style="line-height: 1.6; margin-bottom: 1.5rem;">
          I recently co-organized this workshop alongside colleagues from Adobe Research and other institutions in October 2025. The workshop explored the challenges and opportunities in understanding short-form videos across social media, marketing, business, and other domains. Short-form videos present unique challenges—rapid editing patterns, engagement-driven narratives, platform-specific formats—that differ fundamentally from traditional long-form video understanding, making them increasingly embedded in our daily lives as sources of entertainment, information, and communication.
        </p>
      </div>
      
      <div class="workshop-highlights" style="background: rgba(255, 255, 255, 0.15); padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
        <h4 style="font-size: 1.2rem; margin-bottom: 1rem;">Workshop Topics:</h4>
        <ul style="list-style: none; padding: 0; line-height: 1.8;">
          <li style="margin-bottom: 0.5rem;">• SV Data Collection and Benchmarking</li>
          <li style="margin-bottom: 0.5rem;">• SV Analysis and Understanding</li>
          <li style="margin-bottom: 0.5rem;">• New Research Frontiers in SV</li>
          <li>• Detection, Generation, and Evaluation of Short-Form Videos</li>
        </ul>
      </div>
      
      <div class="workshop-links" style="display: flex; gap: 1rem; flex-wrap: wrap;">
        <a href="https://short-form-video-understanding.github.io/" target="_blank" 
           style="background: white; color: #667eea; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 600; transition: transform 0.3s; display: inline-block;">
          Visit Workshop Website →
        </a>
        <a href="https://short-form-video-understanding.github.io/#submission" target="_blank"
           style="background: rgba(255, 255, 255, 0.2); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 600; border: 2px solid white; transition: transform 0.3s; display: inline-block;">
          Submission Guidelines →
        </a>
      </div>
    </div>
  </section>

  <!-- Other News Section -->
  <section id="other-news" class="news-section">
    <h2 style="font-size: 2rem; color: #333; margin-bottom: 2rem; border-left: 4px solid #f093fb; padding-left: 1rem;">
      Other Updates
    </h2>
    
    <div class="updates-list">
      <div class="update-item" style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem; border-left: 4px solid #667eea;">
        <p style="color: #666; font-size: 0.9rem; margin-bottom: 0.5rem;">Stay tuned for more updates!</p>
        <p style="color: #333;">This section will be updated with recent achievements, conference presentations, and other professional activities.</p>
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

