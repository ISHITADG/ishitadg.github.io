---
layout: page
title: Education
permalink: /education/
---

<div class="education-container" style="max-width: 1000px; margin: 0 auto; padding: 2rem 0;">
  
  <div class="education-header" style="text-align: center; margin-bottom: 3rem;">
    <h1 style="font-size: 2.2rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; letter-spacing: -0.5px;">Education & Academic Experience</h1>
    <div class="divider" style="width: 60px; height: 1px; background: #a8c5e0; margin: 0 auto;"></div>
    <p style="color: #b0b0b0; margin-top: 1rem; font-size: 1rem;">Academic journey, research assistantships, teaching, and leadership (2014-2022)</p>
  </div>

  <div class="education-timeline" style="position: relative; padding-left: 2rem;">
    
    <!-- Ph.D. Period -->
    <div class="timeline-item" style="position: relative; padding-bottom: 3rem; padding-left: 2rem; border-left: 1px solid #2a2a2a;">
      <div class="timeline-marker" style="position: absolute; left: -6px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: #a8c5e0; border: 2px solid #0f0f0f;"></div>
      <div class="timeline-content">
        <h3 style="font-size: 1.5rem; color: #e8e8e8; margin-bottom: 0.5rem; font-weight: 400;">Ph.D. in Computer Science</h3>
        <p style="color: #c4a8d8; font-weight: 400; margin-bottom: 0.5rem; font-size: 1rem;">University of Massachusetts, Amherst</p>
        <p style="color: #808080; margin-bottom: 1.5rem; font-size: 0.9rem;">Sep 2016 - Feb 2023 | Advised by Prof. Michael Zink</p>
        
        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a; margin-bottom: 1rem; border-left: 3px solid #a8c5e0;">
          <h4 style="font-size: 1.2rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400;">Dissertation</h4>
          <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 1rem;">
            <strong style="color: #e8e8e8;">Title:</strong> <em style="color: #c4a8d8;">Improving User Experience by Optimizing Cloud Services</em>
          </p>
          <div style="background: #0f0f0f; padding: 1rem; border-radius: 4px; margin-bottom: 1rem; border: 1px solid #2a2a2a;">
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.9rem; margin-bottom: 0.5rem;">
              <strong style="color: #e8e8e8;">Abstract:</strong>
            </p>
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.9rem; text-align: justify;">
              Today, cloud services offer myriads of applications, tailor made for different users in the field of weather, health, finance, entertainment, etc. These services fulfill varying genres of user demands over the Internet. For example, these services can be live (live weather radar, ESPN Live) or on-demand services (weather forecasting, Netflix). While these applications cater to different customer requirements, it is necessary for these services to be efficient with respect to latency, scalability, robustness and quality of experience. These systems need to constantly evolve to provide the best user experience and meet the most current demands of the customer. For instance, weather forecasting systems need to make accurate predictions close to real-time in order to alert customers of an imminent disaster. Similarly, video-streaming systems consistently strive towards providing best viewing experience to the customer. As weather predictions become more fine-grained with high-resolution observations and video streaming platforms evolve with higher resolution content, the underlying system needs to improve to deliver optimum performance. Even though weather sensing and forecasting has become increasingly accurate in the last decade thanks to high-resolution radars, efficient computational algorithms, and high-performance computing facilities, there are existing challenges that could result in sub-optimal weather prediction. Flood-forecasting models are dependent on high-performance computing clusters for processing high-resolution rainfall data and their unavailability can become a bottleneck. Also, weather radars are critical infrastructure, but are often located in remote areas with poor network connectivity. Data retrieved from these radars are often delayed or lost, or even lack proper synchronization, resulting in less than ideal weather predictions. Additionally, as more and more users have access to the cloud-based video-streaming platforms, their viewing experience is often adversely affected by network conditions (congestion, limited bandwidth) and limitations of address-based Internet architectures. In this dissertation, we try to address these existing challenges by designing and implementing systems on the cloud that improve end-user experience. We optimize two cloud services: In the field of safety we improve upon weather forecasting systems and in the field of entertainment, quality of experience in video-streaming systems. We utilize, investigate and incorporate benefits of different system technologies such as parallelization, virtualization, software defined networking and information centric networking in the existing system workflow with the goal of optimizing the quality of experience. Firstly, we relieve the dependency on high-performance computing clusters for a flood-forecasting model by using cloud resources as an alternative. We then optimize the performance of this model on the cloud by parallely distributing its existing workflow, which leads to 34% reduction in rainfall processing time. The observed improvement in runtime is not only consistent with varying rainfall conditions but could also lead to faster forecasts on the cloud and potentially be extended to different weather forecast models. Secondly, we improve data-retrieval and synchronization challenges in weather sensing radars by applying Named Data Networking (NDN) for efficient content addressing and retrieval. We identify weather data based on a hierarchical naming scheme to explicitly access desired data and demonstrate that compared to a time-based windowing mechanism for radar data retrieval on top of TCP/IP, an NDN based mechanism improves data quality, reduces uncertainty, and enhances weather prediction. Lastly, we improve quality of experience in live video streaming by designing a seamless and efficient distribution system that is flexible enough to choose from multiple Internet architectures best suited for live video streaming. We highlight the benefits of such a hybrid system for live video streaming as well as present a detailed analysis with the goal to provide a high quality of experience (QoE) for the viewer. For our hybrid architecture, video streaming is supported simultaneously over TCP/IP and Named Data Networking (NDN)-based architecture via operating system and networking virtualization techniques to design a flexible system that utilizes the benefits of these varying Internet architectures. Based on a prototype we have designed and implemented maintaining efficient use of network resources, we demonstrate that in the case of live streaming, NDN achieves better QoE per client than IP and can also utilize higher than the available bottleneck bandwidth through in-network caching. Even without caching, as opposed to IP-only, our hybrid setup achieves better average bitrate and better perceived visual quality over live video streaming services. Furthermore, we present detailed analysis on ways adaptive video streaming with NDN can be further improved with respect to QoE. In this context, we identify the phenomenon of oscillation effects that adversely affects QoE in adaptive video streaming and propose solutions to reduce them.
            </p>
          </div>
          <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem;">
            <strong style="color: #e8e8e8;">Link:</strong> <a href="https://scholarworks.umass.edu/items/46d62003-c3b0-4584-a67b-e24b168df32e" target="_blank" style="color: #a8c5e0; text-decoration: none; border-bottom: 1px solid transparent; transition: border-color 0.3s;" onmouseover="this.style.borderBottomColor='#a8c5e0'" onmouseout="this.style.borderBottomColor='transparent'">View Dissertation on ScholarWorks →</a>
          </p>
        </div>
        
        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a; margin-bottom: 1rem;">
          <h4 onclick="toggleSection('phd-papers')" style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.5rem;">
            <span id="phd-papers-icon" style="transition: transform 0.3s;">▼</span>
            Papers (2016-2023)
          </h4>
          <div id="phd-papers-content" style="display: block;">
            {% assign phd_papers = site.publications | where_exp: "pub", "pub.year >= 2016 and pub.year <= 2023" | sort: 'year' | reverse %}
            {% if phd_papers.size > 0 %}
              <ul style="color: #b0b0b0; font-size: 0.95rem; line-height: 1.8; padding-left: 1.2rem; list-style: none;">
                {% for paper in phd_papers %}
                <li style="margin-bottom: 0.8rem; padding-left: 0.5rem; position: relative;">
                  <span style="position: absolute; left: -0.5rem; color: #a8c5e0;">•</span>
                  <strong style="color: #e8e8e8;">{{ paper.title }}</strong>
                  {% if paper.venue %}
                    <span style="color: #808080;"> | {{ paper.venue }}</span>
                  {% endif %}
                  {% if paper.year %}
                    <span style="color: #c4a8d8;"> ({{ paper.year }})</span>
                  {% endif %}
                  {% if paper.link %}
                    <a href="{{ paper.link }}" target="_blank" style="color: #a8c5e0; text-decoration: none; margin-left: 0.5rem; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;" onmouseover="this.style.borderBottomColor='#a8c5e0'" onmouseout="this.style.borderBottomColor='transparent'">[Link]</a>
                  {% endif %}
                </li>
                {% endfor %}
              </ul>
            {% else %}
              {% comment %} List papers manually {% endcomment %}
              <ul style="color: #b0b0b0; font-size: 0.95rem; line-height: 1.8; padding-left: 1.2rem; list-style: none;">
                <li style="margin-bottom: 1rem; padding-left: 0.5rem; position: relative;">
                  <span style="position: absolute; left: -0.5rem; color: #a8c5e0;">•</span>
                  <strong style="color: #e8e8e8;">A Hybrid NDN-IP Architecture for Live Video Streaming: From Host-Based to Content-Based Delivery to Improve QoE</strong>
                  <span style="color: #808080;"> | International Journal of Semantic Computing (2022)</span>
                  <span style="color: #c4a8d8;"> (2022)</span>
                  <a href="https://doi.org/10.1142/S1793351X22400074" target="_blank" style="color: #a8c5e0; text-decoration: none; margin-left: 0.5rem; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;" onmouseover="this.style.borderBottomColor='#a8c5e0'" onmouseout="this.style.borderBottomColor='transparent'">[DOI]</a>
                </li>
                <li style="margin-bottom: 1rem; padding-left: 0.5rem; position: relative;">
                  <span style="position: absolute; left: -0.5rem; color: #a8c5e0;">•</span>
                  <strong style="color: #e8e8e8;">An Information Centric Framework for Weather Sensing Data</strong>
                  <span style="color: #808080;"> | RAFNet at ICC 2022</span>
                  <span style="color: #c4a8d8;"> (2022)</span>
                  <a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=okBrMn8AAAAJ&sortby=pubdate&citation_for_view=okBrMn8AAAAJ:qjMakFHDy7sC" target="_blank" style="color: #a8c5e0; text-decoration: none; margin-left: 0.5rem; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;" onmouseover="this.style.borderBottomColor='#a8c5e0'" onmouseout="this.style.borderBottomColor='transparent'">[Link]</a>
                </li>
                <li style="margin-bottom: 1rem; padding-left: 0.5rem; position: relative;">
                  <span style="position: absolute; left: -0.5rem; color: #a8c5e0;">•</span>
                  <strong style="color: #e8e8e8;">A Hybrid NDN-IP Architecture for Live Video Streaming: A QoE Analysis</strong>
                  <span style="color: #808080;"> | 2021 IEEE International Symposium on Multimedia (ISM)</span>
                  <span style="color: #c4a8d8;"> (2021)</span>
                  <a href="https://doi.org/10.1109/ISM52913.2021.00032" target="_blank" style="color: #a8c5e0; text-decoration: none; margin-left: 0.5rem; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;" onmouseover="this.style.borderBottomColor='#a8c5e0'" onmouseout="this.style.borderBottomColor='transparent'">[DOI]</a>
                </li>
                <li style="margin-bottom: 1rem; padding-left: 0.5rem; position: relative;">
                  <span style="position: absolute; left: -0.5rem; color: #a8c5e0;">•</span>
                  <strong style="color: #e8e8e8;">High-Resolution Hydrologic Forecasting for Very Large Urban Areas</strong>
                  <span style="color: #808080;"> | Journal of Hydroinformatics</span>
                  <span style="color: #c4a8d8;"> (2019)</span>
                  <a href="https://doi.org/10.2166/hydro.2019.10" target="_blank" style="color: #a8c5e0; text-decoration: none; margin-left: 0.5rem; font-size: 0.85rem; border-bottom: 1px solid transparent; transition: border-color 0.3s;" onmouseover="this.style.borderBottomColor='#a8c5e0'" onmouseout="this.style.borderBottomColor='transparent'">[DOI]</a>
                </li>
              </ul>
            {% endif %}
          </div>
        </div>
        
        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a; margin-bottom: 1rem;">
          <h4 onclick="toggleSection('phd-courses')" style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.5rem;">
            <span id="phd-courses-icon" style="transition: transform 0.3s;">▼</span>
            Key Courses
          </h4>
          <div id="phd-courses-content" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
            <div>
              <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">Systems & Networks</p>
              <ul style="color: #b0b0b0; font-size: 0.9rem; line-height: 1.6; padding-left: 1.2rem;">
                <li>E&C-ENG 671: Computer Networks</li>
              </ul>
            </div>
            <div>
              <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">Machine Learning & AI</p>
              <ul style="color: #b0b0b0; font-size: 0.9rem; line-height: 1.6; padding-left: 1.2rem;">
                <li>CS689: Machine Learning</li>
              </ul>
            </div>
            <div>
              <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">Other</p>
              <ul style="color: #b0b0b0; font-size: 0.9rem; line-height: 1.6; padding-left: 1.2rem;">
                <li>CS590CC: Cloud Computing</li>
              </ul>
            </div>
          </div>
        </div>

        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a; margin-bottom: 1rem;">
          <h4 onclick="toggleSection('phd-research')" style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.5rem;">
            <span id="phd-research-icon" style="transition: transform 0.3s;">▼</span>
            Research Assistant
          </h4>
          <div id="phd-research-content" style="display: block;">
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
              <strong style="color: #e8e8e8;">Multimedia & Networks Lab</strong> | Advised by Prof. Michael Zink | Sep 2016 - Feb 2023
            </p>
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem;">
              Conducted research on optimizing multimedia experiences in live video streaming. Worked on network protocols, adaptive streaming algorithms, and multimedia systems optimization. Published multiple papers in top-tier conferences and journals.
            </p>
          </div>
        </div>

        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a; margin-bottom: 1rem;">
          <h4 onclick="toggleSection('phd-teaching')" style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.5rem;">
            <span id="phd-teaching-icon" style="transition: transform 0.3s;">▼</span>
            Teaching Assistant
          </h4>
          <div id="phd-teaching-content" style="display: block;">
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
              <strong style="color: #e8e8e8;">CS 653: Advanced Computer Networks</strong> | Aug 2020 – Dec 2020
            </p>
          </div>
        </div>

        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a;">
          <h4 onclick="toggleSection('phd-leadership')" style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.5rem;">
            <span id="phd-leadership-icon" style="transition: transform 0.3s;">▼</span>
            Leadership & Co-Curricular Activities
          </h4>
          <div id="phd-leadership-content" style="display: block;">
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
              • <strong style="color: #e8e8e8;">Program committee member</strong> | IEEE ISM 2022 (Oct 2022)
            </p>
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
              • <strong style="color: #e8e8e8;">Best Documentation award</strong> | Code Quality Jam, held at Adobe (July 2022)
            </p>
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
              • <strong style="color: #e8e8e8;">Student Volunteer</strong> | MMSys 2019 (June 2019)
            </p>
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem;">
              • <strong style="color: #e8e8e8;">PhD Social Chair</strong> | CICS, UMass Amherst (Sept 2017)
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Masters Period -->
    <div class="timeline-item" style="position: relative; padding-bottom: 3rem; padding-left: 2rem; border-left: 1px solid #2a2a2a;">
      <div class="timeline-marker" style="position: absolute; left: -6px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: #a8c5e0; border: 2px solid #0f0f0f;"></div>
      <div class="timeline-content">
        <h3 style="font-size: 1.5rem; color: #e8e8e8; margin-bottom: 0.5rem; font-weight: 400;">Master of Science in Computer Science</h3>
        <p style="color: #c4a8d8; font-weight: 400; margin-bottom: 0.5rem; font-size: 1rem;">University of Massachusetts, Amherst</p>
        <p style="color: #808080; margin-bottom: 1.5rem; font-size: 0.9rem;">Sep 2014 - Aug 2016</p>
        
        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a; margin-bottom: 1rem;">
          <h4 onclick="toggleSection('ms-courses')" style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.5rem;">
            <span id="ms-courses-icon" style="transition: transform 0.3s;">▼</span>
            Key Courses
          </h4>
          <div id="ms-courses-content" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div>
              <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">Systems & Networks</p>
              <ul style="color: #b0b0b0; font-size: 0.9rem; line-height: 1.6; padding-left: 1.2rem;">
                <li>CS677: Operating Systems</li>
              </ul>
            </div>
            <div>
              <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">Machine Learning & AI</p>
              <ul style="color: #b0b0b0; font-size: 0.9rem; line-height: 1.6; padding-left: 1.2rem;">
                <li>CS585: Intro Natural Language Processing</li>
              </ul>
            </div>
            <div>
              <p style="color: #c4a8d8; font-weight: 400; font-size: 0.9rem; margin-bottom: 0.5rem;">Theory & Other</p>
              <ul style="color: #b0b0b0; font-size: 0.9rem; line-height: 1.6; padding-left: 1.2rem;">
                <li>CS611: Advanced Algorithms</li>
                <li>CS646: Information Retrieval</li>
                <li>CS621: Adv S/W Eng: Analysis and Eval</li>
                <li>CS701: Advanced Topics Computer Science</li>
              </ul>
            </div>
          </div>
        </div>

        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a; margin-bottom: 1rem;">
          <h4 onclick="toggleSection('ms-research')" style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.5rem;">
            <span id="ms-research-icon" style="transition: transform 0.3s;">▼</span>
            Research Projects
          </h4>
          <div id="ms-research-content" style="display: block;">
            <div style="margin-bottom: 1.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid #2a2a2a;">
              <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
                <strong style="color: #e8e8e8;">Advisor:</strong> Prashant Shenoy
              </p>
              <p style="color: #808080; font-size: 0.85rem; margin-bottom: 0.5rem;">
                📅 Feb - Aug 2016 | 📍 UMass Amherst
              </p>
              <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem;">
                <strong style="color: #e8e8e8;">Real-time Water-quality monitoring:</strong> Built a cost-effective & real-time solution for alerting users with inconsumable water quality.
              </p>
            </div>
            <div>
              <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
                <strong style="color: #e8e8e8;">Advisor:</strong> J. Elliot B. Moss
              </p>
              <p style="color: #808080; font-size: 0.85rem; margin-bottom: 0.5rem;">
                📅 Jan - Aug 2015 | 📍 UMass Amherst
              </p>
              <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem;">
                <strong style="color: #e8e8e8;">Java Virtual Machine Bytecode Optimization:</strong> The work involved identifying and removing redundancies from compiled JAVA class files that effectively reduced the runtime of JVM.
              </p>
            </div>
          </div>
        </div>

        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a; margin-bottom: 1rem;">
          <h4 onclick="toggleSection('ms-teaching')" style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.5rem;">
            <span id="ms-teaching-icon" style="transition: transform 0.3s;">▼</span>
            Teaching Assistant
          </h4>
          <div id="ms-teaching-content" style="display: block;">
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
              <strong style="color: #e8e8e8;">CS121: Introduction to Computer Science</strong> | Spring 2015
            </p>
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
              <strong style="color: #e8e8e8;">CS187: Data Structures</strong> | Fall 2015
            </p>
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem;">
              Supported undergraduate courses, helping students with programming assignments, conducting lab sessions, and providing academic support.
            </p>
          </div>
        </div>

        <div style="background: #1a1a1a; padding: 1.5rem; border-radius: 4px; border: 1px solid #2a2a2a;">
          <h4 onclick="toggleSection('ms-leadership')" style="font-size: 1.1rem; color: #e8e8e8; margin-bottom: 1rem; font-weight: 400; cursor: pointer; user-select: none; display: flex; align-items: center; gap: 0.5rem;">
            <span id="ms-leadership-icon" style="transition: transform 0.3s;">▼</span>
            Leadership & Co-Curricular Activities
          </h4>
          <div id="ms-leadership-content" style="display: block;">
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem; margin-bottom: 0.5rem;">
              • <strong style="color: #e8e8e8;">President</strong> | Indian Student Association at UMass Amherst (May 2015-2016)
            </p>
            <p style="color: #b0b0b0; line-height: 1.7; font-size: 0.95rem;">
              • <strong style="color: #e8e8e8;">Volunteer</strong> | Women in Engineering and Computing Career Day (Oct 2015)
            </p>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>

<style>
@media (max-width: 768px) {
  .education-timeline {
    padding-left: 1rem !important;
  }
  .timeline-content > div {
    padding: 1rem !important;
  }
}

h4[onclick] {
  transition: color 0.3s;
}

h4[onclick]:hover {
  color: #a8c5e0 !important;
}

#phd-courses-content,
#phd-research-content,
#phd-papers-content,
#phd-teaching-content,
#phd-leadership-content,
#ms-courses-content,
#ms-research-content,
#ms-teaching-content,
#ms-leadership-content {
  transition: max-height 0.3s ease-out, opacity 0.3s ease-out;
  overflow: hidden;
}

#phd-courses-content.hidden,
#phd-research-content.hidden,
#phd-papers-content.hidden,
#phd-teaching-content.hidden,
#phd-leadership-content.hidden,
#ms-courses-content.hidden,
#ms-research-content.hidden,
#ms-teaching-content.hidden,
#ms-leadership-content.hidden {
  display: none !important;
}
</style>

<script>
function toggleSection(sectionId) {
  const content = document.getElementById(sectionId + '-content');
  const icon = document.getElementById(sectionId + '-icon');
  
  if (content.classList.contains('hidden')) {
    content.classList.remove('hidden');
    icon.textContent = '▼';
    icon.style.transform = 'rotate(0deg)';
  } else {
    content.classList.add('hidden');
    icon.textContent = '▶';
    icon.style.transform = 'rotate(0deg)';
  }
}

// Initialize all sections as hidden by default
document.addEventListener('DOMContentLoaded', function() {
  const sections = [
    'phd-courses', 'phd-research', 'phd-papers', 'phd-teaching', 'phd-leadership',
    'ms-courses', 'ms-research', 'ms-teaching', 'ms-leadership'
  ];
  
  sections.forEach(sectionId => {
    const content = document.getElementById(sectionId + '-content');
    const icon = document.getElementById(sectionId + '-icon');
    if (content) {
      // Keep PhD papers section open by default
      if (sectionId === 'phd-papers') {
        content.classList.remove('hidden');
        if (icon) icon.textContent = '▼';
      } else {
        content.classList.add('hidden');
        if (icon) icon.textContent = '▶';
      }
    }
  });
});
</script>
