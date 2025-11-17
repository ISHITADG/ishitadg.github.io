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

  <!-- Interactive Timeline Section -->
  <section id="timeline" class="news-section" style="margin-bottom: 4rem;">
    <h2 style="font-size: 2rem; color: #e8e8e8; margin-bottom: 3rem; text-align: center; font-weight: 400;">
      Recent News Timeline
    </h2>
    
    <div class="timeline-container" style="position: relative; max-width: 800px; margin: 0 auto;">
      <!-- Vertical Line -->
      <div class="timeline-line" style="position: absolute; left: 20px; top: 0; bottom: 0; width: 2px; background: #2a2a2a;"></div>
      
      <!-- H2 2025 -->
      <div class="timeline-period" style="position: relative; margin-bottom: 2rem;">
        <div class="timeline-dot" onclick="togglePeriod('h2-2025')" style="position: absolute; left: 11px; top: 8px; width: 20px; height: 20px; border-radius: 50%; background: #a8c5e0; border: 3px solid #0f0f0f; cursor: pointer; z-index: 10; transition: all 0.3s;"></div>
        <div class="timeline-content-wrapper" style="margin-left: 50px;">
          <div class="timeline-header" onclick="togglePeriod('h2-2025')" style="cursor: pointer; margin-bottom: 1rem;">
            <h3 style="font-size: 1.3rem; color: #e8e8e8; font-weight: 400; margin: 0;">H2 2025</h3>
          </div>
          <div class="timeline-content" id="h2-2025-content" style="display: none; padding-left: 1rem; border-left: 1px solid #2a2a2a; margin-left: 0.5rem;">
            {% assign all_pubs = site.publications | where_exp: "pub", "pub.date != nil" | sort: 'date' | reverse %}
            {% for pub in all_pubs %}
              {% assign pub_year = pub.date | date: '%Y' | plus: 0 %}
              {% assign pub_month = pub.date | date: '%m' | plus: 0 %}
              {% if pub_year == 2025 and pub_month >= 7 and pub_month <= 12 %}
              {% unless pub.title contains "SmartEdit" %}
              <div class="timeline-item" style="background: #1a1a1a; padding: 1.2rem; border-radius: 4px; margin-bottom: 1rem; border: 1px solid #2a2a2a;">
                <h4 style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 0.4rem; font-weight: 400; line-height: 1.4;">
                  {{ pub.title }}
                </h4>
                <p style="color: #808080; margin-bottom: 0.3rem; font-size: 0.9rem; line-height: 1.5;">
                  {{ pub.authors }}
                </p>
                {% if pub.venue and pub.date %}
                  {% assign pub_month_display = pub.date | date: "%b" %}
                  <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">
                    {{ pub.venue }}, {{ pub_month_display }} {{ pub.date | date: "%Y" }}
                  </p>
                {% elsif pub.venue %}
                  <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">{{ pub.venue }}</p>
                {% elsif pub.date %}
                  {% assign pub_month_display = pub.date | date: "%b" %}
                  <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">{{ pub_month_display }} {{ pub.date | date: "%Y" }}</p>
                {% endif %}
                {% if pub.link %}
                <a href="{{ pub.link }}" target="_blank" style="color: #a8c5e0; text-decoration: none; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
                  View Paper →
                </a>
                {% endif %}
              </div>
              {% endunless %}
              {% endif %}
            {% endfor %}
            <!-- SVU Workshop -->
            <div class="timeline-item" style="background: #1a1a1a; padding: 1.2rem; border-radius: 4px; margin-bottom: 1rem; border: 1px solid #2a2a2a;">
              <h4 style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 0.4rem; font-weight: 400; line-height: 1.4;">
                SVU 2025 Workshop: The First Workshop on Short-Form Video Understanding
              </h4>
              <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">
                ICCV 2025, Oct 2025
              </p>
              <a href="https://short-form-video-understanding.github.io/" target="_blank" style="color: #a8c5e0; text-decoration: none; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
                Visit Workshop Website →
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- H1 2025 -->
      <div class="timeline-period" style="position: relative; margin-bottom: 2rem;">
        <div class="timeline-dot" onclick="togglePeriod('h1-2025')" style="position: absolute; left: 11px; top: 8px; width: 20px; height: 20px; border-radius: 50%; background: #a8c5e0; border: 3px solid #0f0f0f; cursor: pointer; z-index: 10; transition: all 0.3s;"></div>
        <div class="timeline-content-wrapper" style="margin-left: 50px;">
          <div class="timeline-header" onclick="togglePeriod('h1-2025')" style="cursor: pointer; margin-bottom: 1rem;">
            <h3 style="font-size: 1.3rem; color: #e8e8e8; font-weight: 400; margin: 0;">H1 2025</h3>
          </div>
          <div class="timeline-content" id="h1-2025-content" style="display: none; padding-left: 1rem; border-left: 1px solid #2a2a2a; margin-left: 0.5rem;">
            {% assign all_pubs_h1 = site.publications | where_exp: "pub", "pub.date != nil" | sort: 'date' | reverse %}
            {% for pub in all_pubs_h1 %}
              {% if pub.title contains "SmartEdit" %}
              <div class="timeline-item" style="background: #1a1a1a; padding: 1.2rem; border-radius: 4px; margin-bottom: 1rem; border: 1px solid #2a2a2a;">
                <h4 style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 0.4rem; font-weight: 400; line-height: 1.4;">
                  {{ pub.title }}
                </h4>
                <p style="color: #808080; margin-bottom: 0.3rem; font-size: 0.9rem; line-height: 1.5;">
                  {{ pub.authors }}
                </p>
                {% if pub.venue and pub.date %}
                  {% assign pub_month_display = pub.date | date: "%b" %}
                  <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">
                    {{ pub.venue }}, {{ pub_month_display }} {{ pub.date | date: "%Y" }}
                  </p>
                {% elsif pub.venue %}
                  <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">{{ pub.venue }}</p>
                {% elsif pub.date %}
                  {% assign pub_month_display = pub.date | date: "%b" %}
                  <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">{{ pub_month_display }} {{ pub.date | date: "%Y" }}</p>
                {% endif %}
                {% if pub.link %}
                <a href="{{ pub.link }}" target="_blank" style="color: #a8c5e0; text-decoration: none; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
                  View Paper →
                </a>
                {% endif %}
              </div>
              {% endif %}
            {% endfor %}
          </div>
        </div>
      </div>

      <!-- H1 2024 -->
      <div class="timeline-period" style="position: relative; margin-bottom: 2rem;">
        <div class="timeline-dot" onclick="togglePeriod('h1-2024')" style="position: absolute; left: 11px; top: 8px; width: 20px; height: 20px; border-radius: 50%; background: #a8c5e0; border: 3px solid #0f0f0f; cursor: pointer; z-index: 10; transition: all 0.3s;"></div>
        <div class="timeline-content-wrapper" style="margin-left: 50px;">
          <div class="timeline-header" onclick="togglePeriod('h1-2024')" style="cursor: pointer; margin-bottom: 1rem;">
            <h3 style="font-size: 1.3rem; color: #e8e8e8; font-weight: 400; margin: 0;">H1 2024</h3>
          </div>
          <div class="timeline-content" id="h1-2024-content" style="display: none; padding-left: 1rem; border-left: 1px solid #2a2a2a; margin-left: 0.5rem;">
            {% assign all_pubs_2024 = site.publications | where_exp: "pub", "pub.date != nil" | sort: 'date' | reverse %}
            {% for pub in all_pubs_2024 %}
              {% assign pub_year_2024 = pub.date | date: '%Y' | plus: 0 %}
              {% assign pub_month_2024 = pub.date | date: '%m' | plus: 0 %}
              {% if pub_year_2024 == 2024 and pub_month_2024 >= 1 and pub_month_2024 < 7 %}
              {% if pub.title contains "Large content" or pub.title contains "Text-to-hand" %}
              <div class="timeline-item" style="background: #1a1a1a; padding: 1.2rem; border-radius: 4px; margin-bottom: 1rem; border: 1px solid #2a2a2a;">
                <h4 style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 0.4rem; font-weight: 400; line-height: 1.4;">
                  {{ pub.title }}
                </h4>
                <p style="color: #808080; margin-bottom: 0.3rem; font-size: 0.9rem; line-height: 1.5;">
                  {{ pub.authors }}
                </p>
                {% if pub.venue and pub.date %}
                  {% assign pub_month_display = pub.date | date: "%b" %}
                  <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">
                    {{ pub.venue }}, {{ pub_month_display }} {{ pub.date | date: "%Y" }}
                  </p>
                {% elsif pub.venue %}
                  <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">{{ pub.venue }}</p>
                {% elsif pub.date %}
                  {% assign pub_month_display = pub.date | date: "%b" %}
                  <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">{{ pub_month_display }} {{ pub.date | date: "%Y" }}</p>
                {% endif %}
                {% if pub.link %}
                <a href="{{ pub.link }}" target="_blank" style="color: #a8c5e0; text-decoration: none; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;">
                  View Paper →
                </a>
                {% endif %}
              </div>
              {% endif %}
              {% endif %}
            {% endfor %}
          </div>
        </div>
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
        <a href="https://short-form-video-understanding.github.io/#schedule" target="_blank"
           style="background: transparent; border: 1px solid #c4a8d8; color: #c4a8d8; padding: 10px 24px; border-radius: 4px; text-decoration: none; font-weight: 400; transition: all 0.3s; display: inline-block; font-size: 0.95rem;">
          Full Schedule →
        </a>
      </div>
    </div>
  </section>

  <!-- Other News Section -->
  <section id="other-news" class="news-section">
    <h2 style="font-size: 1.8rem; color: #e8e8e8; margin-bottom: 2rem; border-left: 2px solid #d4b5b5; padding-left: 1rem; font-weight: 400;">
      Upcoming/Past Talks
    </h2>
    
    <div class="updates-list">
      <div class="update-item" style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; margin-bottom: 1rem; border-left: 2px solid #a8c5e0; border: 1px solid #2a2a2a;">
        <p style="color: #b0b0b0;">Watch this space for upcoming or past talks.</p>
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

<style>
.timeline-dot:hover {
  transform: scale(1.2);
  background: #c4a8d8 !important;
}

.timeline-header:hover h3 {
  color: #a8c5e0 !important;
}

.timeline-content {
  animation: slideDown 0.3s ease-out;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>

<script>
function togglePeriod(periodId) {
  const content = document.getElementById(periodId + '-content');
  const dot = event.target.closest('.timeline-period').querySelector('.timeline-dot');
  
  if (content.style.display === 'none' || !content.style.display) {
    content.style.display = 'block';
    if (dot) {
      dot.style.background = '#c4a8d8';
      dot.style.transform = 'scale(1.1)';
    }
  } else {
    content.style.display = 'none';
    if (dot) {
      dot.style.background = '#a8c5e0';
      dot.style.transform = 'scale(1)';
    }
  }
}

document.addEventListener('DOMContentLoaded', function() {
  console.log('News timeline loaded');
});
</script>

