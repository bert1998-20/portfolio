import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Obeth Gabiana Silawan | SEO Specialist Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide ALL Streamlit default elements including file explorer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {margin: 0; padding: 0;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        .css-1d391kg, .css-1lcbmhc, .css-1vq4p4l, .css-1y4p8pa {
            display: none !important;
        }
        .stFileUploader, .stFileUploader div {
            display: none !important;
        }
        [data-testid="stFileUploader"], [data-testid="stSidebar"] {
            display: none !important;
        }
        section[data-testid="stSidebar"] {
            display: none !important;
            width: 0 !important;
        }
        .st-emotion-cache-1r6slb0, .st-emotion-cache-1r6slb0 * {
            display: none !important;
        }
        .main .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        .st-emotion-cache-1v0mbdj {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Portfolio HTML
portfolio_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Obeth Gabiana Silawan | SEO Specialist Portfolio</title>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', 'Segoe UI', Arial, sans-serif;
  cursor: none;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

body {
  background: radial-gradient(circle at top, #1a2cff, #060714 55%, #02030a);
  color: #fff;
  overflow-x: hidden;
}

.cursor {
  width: 20px;
  height: 20px;
  border: 2px solid #7df9ff;
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  transform: translate(-50%, -50%);
  transition: width 0.2s, height 0.2s, background 0.2s;
  box-shadow: 0 0 15px rgba(125, 249, 255, 0.5);
}

.cursor-dot {
  width: 4px;
  height: 4px;
  background: #7df9ff;
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  transform: translate(-50%, -50%);
}

.bg-grid {
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(125,249,255,.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(125,249,255,.06) 1px, transparent 1px);
  background-size: 45px 45px;
  z-index: -2;
}

.bg-glow-1 {
  position: fixed;
  width: 600px;
  height: 600px;
  background: #7df9ff;
  filter: blur(160px);
  opacity: .12;
  border-radius: 50%;
  top: -10%;
  right: -10%;
  z-index: -1;
  animation: floatGlow 12s ease-in-out infinite;
}

.bg-glow-2 {
  position: fixed;
  width: 500px;
  height: 500px;
  background: #9b6cff;
  filter: blur(160px);
  opacity: .1;
  border-radius: 50%;
  bottom: -10%;
  left: -10%;
  z-index: -1;
  animation: floatGlow 10s ease-in-out infinite reverse;
}

@keyframes floatGlow {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(30px, 20px); }
}

header {
  padding: 18px 8%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  backdrop-filter: blur(10px);
  background: rgba(6, 7, 20, 0.4);
  position: sticky;
  top: 0;
  z-index: 100;
}

.logo {
  font-size: 24px;
  font-weight: 900;
  background: linear-gradient(135deg, #7df9ff, #9b6cff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  letter-spacing: 2px;
}

.logo span {
  color: #7df9ff;
  background: none;
  -webkit-background-clip: unset;
  background-clip: unset;
}

nav a {
  color: #fff;
  text-decoration: none;
  margin-left: 28px;
  font-size: 14px;
  font-weight: 500;
  opacity: .8;
  transition: all 0.3s ease;
  position: relative;
}

nav a::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #7df9ff, #9b6cff);
  transition: width 0.3s ease;
}

nav a:hover::after {
  width: 100%;
}

nav a:hover {
  opacity: 1;
  color: #7df9ff;
}

.hero {
  min-height: auto;
  padding: 40px 8% 50px;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  align-items: center;
  gap: 40px;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 18px;
  border: 1px solid rgba(125,249,255,.45);
  border-radius: 50px;
  color: #7df9ff;
  background: rgba(125,249,255,.08);
  margin-bottom: 20px;
  font-size: 13px;
  font-weight: 500;
  backdrop-filter: blur(5px);
}

.badge::before {
  content: '✨';
  font-size: 14px;
}

.hero h1 {
  font-size: 52px;
  line-height: 1.08;
  margin-bottom: 18px;
  font-weight: 800;
}

.hero h1 span {
  background: linear-gradient(135deg, #7df9ff, #9b6cff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.hero p {
  max-width: 620px;
  font-size: 16px;
  line-height: 1.6;
  color: #d6dcff;
  margin-bottom: 28px;
}

.buttons {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.btn {
  padding: 12px 28px;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 700;
  font-size: 14px;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.btn-primary {
  background: linear-gradient(135deg, #7df9ff, #9b6cff);
  color: #030713;
  box-shadow: 0 0 20px rgba(125,249,255,.3);
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 35px rgba(125,249,255,.5);
}

.btn-secondary {
  border: 1px solid rgba(255,255,255,.3);
  color: #fff;
  background: rgba(255,255,255,.06);
}

.btn-secondary:hover {
  border-color: #7df9ff;
  background: rgba(125,249,255,.1);
  transform: translateY(-3px);
}

.stats {
  display: flex;
  gap: 32px;
  margin-top: 28px;
  flex-wrap: wrap;
}

.stat-number {
  font-size: 28px;
  font-weight: 800;
  color: #7df9ff;
  display: block;
}

.stat-label {
  font-size: 12px;
  color: #a0a8e0;
  letter-spacing: 1px;
}

.avatar-wrap {
  perspective: 1200px;
  display: flex;
  justify-content: center;
}

.avatar-card {
  width: 340px;
  height: 500px;
  position: relative;
  border-radius: 40px;
  background: linear-gradient(145deg, rgba(255,255,255,.12), rgba(255,255,255,.03));
  border: 1px solid rgba(255,255,255,.2);
  backdrop-filter: blur(20px);
  box-shadow: 0 40px 90px rgba(0,0,0,.5);
  transform-style: preserve-3d;
  animation: float 5s ease-in-out infinite;
  overflow: hidden;
}

@keyframes float {
  0%,100% { transform: translateY(0) rotateY(-5deg); }
  50% { transform: translateY(-15px) rotateY(5deg); }
}

.character {
  position: absolute;
  left: 50%;
  top: 50px;
  transform: translateX(-50%) translateZ(80px);
  width: 220px;
  height: 320px;
}

.hair {
  position: absolute;
  top: 0;
  left: 20px;
  width: 180px;
  height: 120px;
  background: linear-gradient(135deg, #0f1530, #5a50dd);
  border-radius: 55% 55% 40% 40%;
  box-shadow: 0 0 30px rgba(109,97,255,.6);
}

.face {
  position: absolute;
  top: 55px;
  left: 40px;
  width: 140px;
  height: 140px;
  background: #ffddcf;
  border-radius: 50% 50% 45% 45%;
}

.eye {
  position: absolute;
  top: 60px;
  width: 18px;
  height: 22px;
  background: #071030;
  border-radius: 50%;
  transition: all 0.1s ease;
}

.eye.left { left: 35px; }
.eye.right { right: 35px; }

.mouth {
  position: absolute;
  bottom: 40px;
  left: 58px;
  width: 20px;
  height: 8px;
  border-bottom: 3px solid #b85c6a;
  border-radius: 50%;
}

.body {
  position: absolute;
  top: 200px;
  left: 15px;
  width: 190px;
  height: 115px;
  background: linear-gradient(135deg, #1a2eff, #8a5cff);
  border-radius: 50px 50px 30px 30px;
  box-shadow: 0 0 25px rgba(125,249,255,.3);
}

.code-chip {
  position: absolute;
  bottom: 15px;
  left: 15px;
  right: 15px;
  padding: 12px;
  border-radius: 18px;
  background: rgba(0,0,0,.6);
  color: #dffcff;
  border: 1px solid rgba(125,249,255,.3);
  font-size: 10px;
  line-height: 1.6;
  text-align: center;
  transform: translateZ(60px);
  backdrop-filter: blur(8px);
}

section {
  padding: 60px 8%;
}

.section-title {
  font-size: 38px;
  margin-bottom: 14px;
  background: linear-gradient(135deg, #fff, #7df9ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-weight: 700;
}

.section-desc {
  color: #cfd5ff;
  max-width: 760px;
  line-height: 1.7;
  margin-bottom: 35px;
  font-size: 16px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.card {
  padding: 28px;
  border-radius: 28px;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.12);
  backdrop-filter: blur(14px);
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
  border-color: rgba(125,249,255,.5);
  box-shadow: 0 0 40px rgba(125,249,255,.15);
}

.card ul {
  padding-left: 18px;
  margin-top: 8px;
}

.card li {
  color: #d5dcff;
  line-height: 1.6;
  font-size: 12px;
  margin-bottom: 5px;
}

.card h3 {
  font-size: 16px;
  margin-bottom: 4px;
}

.card p {
  font-size: 13px;
  color: #a0a8e0;
  margin-bottom: 6px;
}

.about-box {
  padding: 35px;
  border-radius: 32px;
  background: linear-gradient(145deg, rgba(125,249,255,.1), rgba(255,255,255,.04));
  border: 1px solid rgba(125,249,255,.2);
}

.about-box p {
  color: #dce2ff;
  line-height: 1.8;
  margin-bottom: 14px;
  font-size: 15px;
}

.contact-box {
  text-align: center;
  padding: 50px;
  border-radius: 40px;
  background: linear-gradient(135deg, rgba(125,249,255,.12), rgba(155,108,255,.1));
  border: 1px solid rgba(255,255,255,.15);
}

.contact-box p {
  color: #dce2ff;
  margin-bottom: 16px;
  font-size: 15px;
}

.contact-box h2 {
  font-size: 34px;
  margin-bottom: 12px;
  background: linear-gradient(135deg, #fff, #7df9ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

footer {
  padding: 24px;
  text-align: center;
  color: #bfc5ff;
  border-top: 1px solid rgba(255,255,255,.08);
  font-size: 13px;
}

@media(max-width: 850px) {
  .hero {
    grid-template-columns: 1fr;
    text-align: center;
    padding: 30px 8% 40px;
  }
  .hero h1 {
    font-size: 38px;
  }
  .grid {
    grid-template-columns: 1fr;
  }
  .avatar-card {
    width: 280px;
    height: 420px;
  }
  .section-title {
    font-size: 30px;
  }
}
</style>
</head>
<body>

<div class="cursor"></div>
<div class="cursor-dot"></div>
<div class="bg-grid"></div>
<div class="bg-glow-1"></div>
<div class="bg-glow-2"></div>

<header>
  <div class="logo"><span>OBETH</span>.AI</div>
  <nav>
    <a href="#about">About</a>
    <a href="#experience">Experience</a>
    <a href="#skills">Skills</a>
    <a href="#featured">Featured</a>
    <a href="#contact">Contact</a>
  </nav>
</header>

<section class="hero">
  <div>
    <div class="badge">✨ SEO Specialist & WordPress Developer</div>
    <h1>Hi, I'm <span>Obeth Gabiana Silawan</span></h1>
    <p>
      SEO Specialist, WordPress Developer, ASO Specialist, and Server Administrator.
      I create intelligent websites, automation systems, data-driven insights, and search-optimized digital
      experiences that help brands grow smarter in the modern world.
    </p>
    
    <div class="stats">
      <div>
        <span class="stat-number">7+</span>
        <span class="stat-label">Years Experience</span>
      </div>
      <div>
        <span class="stat-number">100+</span>
        <span class="stat-label">Projects Completed</span>
      </div>
      <div>
        <span class="stat-number">50+</span>
        <span class="stat-label">Happy Clients</span>
      </div>
    </div>

    <div class="buttons">
      <a href="#contact" class="btn btn-secondary">📧 Hire Me</a>
      <a href="#" onclick="downloadCV()" class="btn btn-secondary">📄 Download CV</a>
    </div>
  </div>

  <div class="avatar-wrap">
    <div class="avatar-card" id="avatarCard">
      <div class="character">
        <div class="hair"></div>
        <div class="face">
          <div class="eye left"></div>
          <div class="eye right"></div>
          <div class="mouth"></div>
        </div>
        <div class="body"></div>
      </div>
      <div class="code-chip">
        🔍 SEO Specialist | WordPress Developer<br>
        🖥️ VPS | aaPanel | cPanel | WHM<br>
        📱 ASO Specialist | Data Analyst
      </div>
    </div>
  </div>
</section>

<section id="about">
  <h2 class="section-title">About Me</h2>
  <div class="about-box">
    <p>As a young coder from Samar, I left home seeking deeper knowledge and skills to thrive in a fast-changing world. My journey led me to explore what it takes to succeed in the 21st century. I've discovered through years of study and insights from experienced friends in IT. While there's plenty of information available, turning it into real understanding is the real challenge.</p>
    <p>My mission is to build websites and digital systems that are functional, user-friendly, visually attractive, search-friendly, powered by smart data analytics, and hosted on reliable server infrastructure.</p>
    <p><strong>✨ Core Philosophy:</strong> "Build smart, optimize constantly, analyze data deeply, and let insights drive decisions."</p>
  </div>
</section>

<section id="experience">
  <h2 class="section-title">Work Experience</h2>
  <p class="section-desc">My complete professional journey from 2019 to Present (2026) - chronological order from newest to oldest.</p>

  <div class="grid">
    <!-- SENIOR SEO SPECIALIST - SIMPLIFIED -->
    <div class="card">
      <h3>🔹 Senior SEO Specialist</h3>
      <p><strong>Self-employed / Freelance</strong> | 2026 - PRESENT</p>
      <ul>
        <li>Manage VPS, cPanel, WHM, aaPanel, and hPanel servers</li>
        <li>Website Migration between hosting providers with zero downtime</li>
        <li>Technical SEO Audits and implementation</li>
        <li>Server Security Hardening & Firewall Setup</li>
        <li>WordPress Optimization on VPS Environments</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 SEO FREELANCE</h3>
      <p><strong>Self-employed</strong> | 2024 - 2025</p>
      <ul>
        <li>Keyword Research & Strategy using SEMrush, Ahrefs, Google Keyword Planner</li>
        <li>On-Page SEO Optimization (meta tags, headers, content structure)</li>
        <li>Technical SEO Audits (site speed, mobile-friendliness, core web vitals)</li>
        <li>Quality Backlink Building through guest posting and outreach</li>
        <li>Content Strategy & Creation for organic growth</li>
        <li>Google My Business (GMB) Optimization for local SEO</li>
        <li>SEO Reporting & Analytics using Google Analytics 4 and Search Console</li>
        <li>Competitor Analysis & Gap Identification</li>
        <li>WordPress SEO Optimization (Yoast SEO, Rank Math)</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 SEO Team Lead</h3>
      <p><strong>IE Soft Technology</strong> | 2024 - 2025</p>
      <ul>
        <li>Led a team of specialists to design and implement SEO strategies</li>
        <li>Create road Map & SEO strategies</li>
        <li>Managed technical audits</li>
        <li>Managed link-building campaigns</li>
        <li>Analyzed performance via GA4, Search Console</li>
        <li>Translating insights into scalable actions</li>
        <li>Collaborated with cross-functional teams</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 Offpage SEO Specialist</h3>
      <p><strong>Bricksharts Technology</strong> | 2022</p>
      <ul>
        <li>Executed strategic backlink campaigns (HARO, Digital PR)</li>
        <li>Built relationships with industry influencers</li>
        <li>Managed local SEO citations and directory listings</li>
        <li>Monitored and disavowed toxic backlinks</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 Onpage SEO Specialist</h3>
      <p><strong>Elevate Outsourcing</strong> | 2022</p>
      <ul>
        <li>Keyword Research & Optimization</li>
        <li>Content Optimization</li>
        <li>Meta Tags & URL Structuring</li>
        <li>Header Tags (H1, H2, H3) & HTML Markup</li>
        <li>Internal Linking Strategy</li>
        <li>Image & Multimedia Optimization</li>
        <li>Mobile & Core Web Vitals</li>
        <li>User Experience (UX) Signals</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 Onpage SEO Specialist</h3>
      <p><strong>Levender Groups</strong> | 2022</p>
      <ul>
        <li>Keyword Research & Optimization</li>
        <li>Content Optimization</li>
        <li>Meta Tags & URL Structuring</li>
        <li>Header Tags (H1, H2, H3) & HTML Markup</li>
        <li>Internal Linking Strategy</li>
        <li>Image & Multimedia Optimization</li>
        <li>Mobile & Core Web Vitals</li>
        <li>User Experience (UX) Signals</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 Junior ASO Specialist</h3>
      <p><strong>Cosmolink Global Solution</strong> | 2021</p>
      <ul>
        <li>Keyword Research & Optimization for app stores</li>
        <li>A/B tested icons, screenshots, and video previews to improve CTR</li>
        <li>Analyzed competitor creatives and adapted best practices</li>
        <li>Tools: AppTweak, MobileAction, Google Play Console, App Store Connect</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 WordPress Developer</h3>
      <p><strong>Bricksharts Technology</strong> | 2021</p>
      <ul>
        <li>Theme & Plugin Development</li>
        <li>Page Builders & Gutenberg</li>
        <li>Performance Optimization</li>
        <li>Security & Maintenance</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 Junior SEO Specialist</h3>
      <p><strong>WBridge Island Cove</strong> | 2019 - 2020</p>
      <ul>
        <li>On-Page SEO optimization (meta descriptions, title tags, header structure)</li>
        <li>Keyword research and implementation</li>
        <li>Content optimization for target keywords</li>
        <li>Internal linking strategy improvement</li>
        <li>Technical SEO fixes (broken links, redirects, sitemap)</li>
        <li>Local SEO optimization for business listings</li>
        <li>SEO performance monitoring via Google Analytics & Search Console</li>
        <li>Competitor keyword analysis and gap identification</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 Junior SEO Specialist</h3>
      <p><strong>Various Clients</strong> | 2019 - 2020</p>
      <ul>
        <li>Supporting organic growth</li>
        <li>Improved URL structures, header tags</li>
        <li>Updated old content for freshness and relevance</li>
        <li>Monitored rankings, traffic (Google Analytics/Search Console)</li>
      </ul>
    </div>
  </div>
</section>

<section id="skills">
  <h2 class="section-title">Skills & Expertise</h2>
  <p class="section-desc">A comprehensive skill set combining SEO mastery, WordPress Development, ASO, and Server Administration.</p>

  <div class="grid">
    <div class="card">
      <h3>🔍 On-Page SEO</h3>
      <ul>
        <li>Keyword Research & Optimization</li>
        <li>Content Optimization</li>
        <li>Meta Tags & URL Structuring</li>
        <li>Header Tags (H1, H2, H3) & HTML Markup</li>
        <li>Internal Linking Strategy</li>
        <li>Image & Multimedia Optimization</li>
        <li>Mobile & Core Web Vitals</li>
        <li>User Experience (UX) Signals</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔗 White Hat SEO</h3>
      <ul>
        <li>Ethical Link Building (Guest posting, HARO, Digital PR)</li>
        <li>Quality Content Creation & Strategy</li>
        <li>GMB & Local SEO Optimization</li>
        <li>Technical SEO Audits & Fixes</li>
        <li>Keyword Research & Strategy</li>
        <li>On-Page SEO Optimization</li>
        <li>SEO Analytics & Reporting (GA4, GSC)</li>
        <li>Competitor Analysis & Gap Identification</li>
      </ul>
    </div>

    <div class="card">
      <h3>🖥️ Server & Hosting</h3>
      <ul>
        <li>VPS Setup & Configuration</li>
        <li>aaPanel / cPanel / WHM</li>
        <li>hPanel Management</li>
        <li>Website Migration</li>
        <li>Database Transfer</li>
        <li>Linux Operations</li>
      </ul>
    </div>

    <div class="card">
      <h3>💻 WordPress Development</h3>
      <ul>
        <li>Theme & Plugin Development</li>
        <li>Page Builders & Gutenberg</li>
        <li>Performance Optimization</li>
        <li>Security & Maintenance</li>
      </ul>
    </div>

    <div class="card">
      <h3>📱 ASO & Mobile</h3>
      <ul>
        <li>App Store Optimization</li>
        <li>Keyword Research for Apps</li>
        <li>Creative A/B Testing</li>
        <li>Tools: AppTweak, MobileAction, Google Play Console, App Store Connect</li>
      </ul>
    </div>

    <div class="card">
      <h3>📊 Analytics & Tools</h3>
      <ul>
        <li>Google Analytics 4 (GA4)</li>
        <li>Google Search Console</li>
        <li>Data Analysis & Reporting</li>
        <li>Performance Tracking</li>
        <li>SEO Tools: Ahrefs, SEMrush, Screaming Frog, Moz</li>
      </ul>
    </div>
  </div>
</section>

<!-- Featured Project Section -->
<section id="featured">
  <h2 class="section-title">Featured Project</h2>
  <div class="about-box" style="text-align: center;">
    <div style="font-size: 50px; margin-bottom: 15px;">📊</div>
    <h3 style="color: #7df9ff; margin-bottom: 12px; font-size: 24px;">Scatter Dashboard</h3>
    <p style="margin-bottom: 20px; max-width: 600px; margin-left: auto; margin-right: auto; font-size: 15px; color: #dce2ff;">
      An interactive data visualization dashboard built with Streamlit. 
      Explore scatter plots, data analysis, and real-time insights.
    </p>
    <a href="https://scatter-dashboard-bert.streamlit.app/" target="_blank" class="btn btn-primary">🚀 Launch Dashboard →</a>
  </div>
</section>

<section id="contact">
  <div class="contact-box">
    <h2>Let's Build Something Intelligent</h2>
    <p>Ready to create an SEO-friendly, data-driven digital experience? Let's collaborate and bring your vision to life.</p>
    <div style="margin-bottom: 16px;">
      <p>📞 +63 9564574637</p>
      <p>✉️ ieph.bert888@gmail.com</p>
      <p>📍 San Leon Umingan Pangasinan</p>
      <p>🌐 Languages: English | Tagalog</p>
    </div>
    <a href="mailto:ieph.bert888@gmail.com" class="btn btn-primary">✉️ Contact Me</a>
  </div>
</section>

<footer>
  © 2026 Obeth Gabiana Silawan | SEO Specialist | WordPress Developer | ASO Specialist | Server Administrator | Built with 💙
</footer>

<script>
// Cursor and 3D effects
const cursor = document.querySelector(".cursor");
const cursorDot = document.querySelector(".cursor-dot");
const avatarCard = document.getElementById("avatarCard");

document.addEventListener("mousemove", function(e) {
  cursor.style.left = e.clientX + "px";
  cursor.style.top = e.clientY + "px";
  cursorDot.style.left = e.clientX + "px";
  cursorDot.style.top = e.clientY + "px";
  
  if (avatarCard) {
    const x = (window.innerWidth / 2 - e.clientX) / 35;
    const y = (window.innerHeight / 2 - e.clientY) / 35;
    avatarCard.style.transform = `rotateY(${-x}deg) rotateX(${y}deg)`;
  }
});

// Eye tracking
document.addEventListener("mousemove", function(e) {
  const eyes = document.querySelectorAll(".eye");
  eyes.forEach(eye => {
    const rect = eye.getBoundingClientRect();
    const angle = Math.atan2(e.clientY - rect.top, e.clientX - rect.left);
    const distance = Math.min(5, Math.hypot(e.clientX - rect.left, e.clientY - rect.top) / 30);
    eye.style.transform = `translate(${Math.cos(angle) * distance}px, ${Math.sin(angle) * distance}px)`;
  });
});

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth' });
  });
});

// Download CV function
function downloadCV() {
  const cvContent = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Obeth Gabiana Silawan - Complete CV 2019-2026</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 40px 20px;
  }
  .cv-container {
    max-width: 1200px;
    margin: 0 auto;
    background: #fff;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  }
  .cv-content { padding: 40px; }
  .header {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 30px;
    padding-bottom: 30px;
    border-bottom: 3px solid #667eea;
    margin-bottom: 30px;
  }
  .name-title h1 { font-size: 42px; color: #2d3748; }
  .name-title .title { font-size: 18px; color: #667eea; margin: 10px 0; }
  .contact-info { text-align: right; }
  .contact-info p { margin: 5px 0; color: #4a5568; }
  .section { margin-bottom: 30px; }
  .section-title {
    font-size: 22px;
    font-weight: bold;
    color: #2d3748;
    border-left: 4px solid #667eea;
    padding-left: 15px;
    margin-bottom: 20px;
    margin-top: 25px;
  }
  .job {
    margin-bottom: 25px;
    padding-bottom: 15px;
    border-bottom: 1px solid #e2e8f0;
  }
  .job-title { font-size: 18px; font-weight: bold; color: #2d3748; }
  .company { color: #667eea; font-weight: 600; margin: 5px 0; }
  .date { color: #718096; font-size: 13px; margin-bottom: 10px; }
  .job-description { margin-left: 20px; }
  .job-description li { margin: 8px 0; color: #4a5568; line-height: 1.5; }
  .skills-tags { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; }
  .skill-tag {
    background: #e2e8f0;
    padding: 5px 15px;
    border-radius: 25px;
    font-size: 12px;
    color: #2d3748;
  }
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
  @media (max-width: 768px) {
    .header { grid-template-columns: 1fr; text-align: center; }
    .contact-info { text-align: center; }
    .two-col { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
<div class="cv-container">
  <div class="cv-content">
    <div class="header">
      <div class="name-title">
        <h1>OBETH GABIANA SILAWAN</h1>
        <div class="title">SEO Specialist | WordPress Developer | ASO Specialist | Server Administrator</div>
      </div>
      <div class="contact-info">
        <p>📞 +63 9564574637</p>
        <p>✉️ ieph.bert888@gmail.com</p>
        <p>📍 San Leon Umingan Pangasinan</p>
        <p>🌐 English | Tagalog</p>
      </div>
    </div>

    <div class="section">
      <div class="section-title">Professional Summary</div>
      <p style="line-height: 1.6; color: #4a5568;">As a young coder from Samar, I left home seeking deeper knowledge and skills to thrive in a fast-changing world. My journey led me to explore what it takes to succeed in the 21st century. I've discovered through years of study and insights from experienced friends in IT. While there's plenty of information available, turning it into real understanding is the real challenge. With 7+ years of experience, I deliver results-driven digital solutions.</p>
    </div>

    <div class="section">
      <div class="section-title">Work Experience (2019 - 2026 PRESENT)</div>
      
      <div class="job">
        <div class="job-title">Senior SEO Specialist</div>
        <div class="company">Self-employed / Freelance</div>
        <div class="date">2026 - PRESENT</div>
        <ul class="job-description">
          <li>Manage VPS, cPanel, WHM, aaPanel, and hPanel servers</li>
          <li>Website Migration between hosting providers with zero downtime</li>
          <li>Technical SEO Audits and implementation</li>
          <li>Server Security Hardening & Firewall Setup</li>
          <li>WordPress Optimization on VPS Environments</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">SEO FREELANCE</div>
        <div class="company">Self-employed</div>
        <div class="date">2024 - 2025</div>
        <ul class="job-description">
          <li>Keyword Research & Strategy using SEMrush, Ahrefs, Google Keyword Planner</li>
          <li>On-Page SEO Optimization (meta tags, headers, content structure)</li>
          <li>Technical SEO Audits (site speed, mobile-friendliness, core web vitals)</li>
          <li>Quality Backlink Building through guest posting and outreach</li>
          <li>Content Strategy & Creation for organic growth</li>
          <li>Google My Business (GMB) Optimization for local SEO</li>
          <li>SEO Reporting & Analytics using Google Analytics 4 and Search Console</li>
          <li>Competitor Analysis & Gap Identification</li>
          <li>WordPress SEO Optimization (Yoast SEO, Rank Math)</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">SEO Team Lead</div>
        <div class="company">IE Soft Technology</div>
        <div class="date">2024 - 2025</div>
        <ul class="job-description">
          <li>Led a team of specialists to design and implement SEO strategies</li>
          <li>Create road Map & SEO strategies</li>
          <li>Managed technical audits and link-building campaigns</li>
          <li>Analyzed performance via GA4, Search Console</li>
          <li>Translating insights into scalable actions</li>
          <li>Collaborated with cross-functional teams</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">Offpage SEO Specialist</div>
        <div class="company">Bricksharts Technology</div>
        <div class="date">2022</div>
        <ul class="job-description">
          <li>Executed strategic backlink campaigns (HARO, Digital PR)</li>
          <li>Built relationships with industry influencers</li>
          <li>Managed local SEO citations and directory listings</li>
          <li>Monitored and disavowed toxic backlinks</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">Onpage SEO Specialist</div>
        <div class="company">Elevate Outsourcing / Levender Groups</div>
        <div class="date">2022</div>
        <ul class="job-description">
          <li>Keyword Research & Optimization</li>
          <li>Content Optimization, Meta Tags & URL Structuring</li>
          <li>Header Tags (H1, H2, H3) & HTML Markup</li>
          <li>Internal Linking Strategy</li>
          <li>Image & Multimedia Optimization</li>
          <li>Mobile & Core Web Vitals</li>
          <li>User Experience (UX) Signals</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">Junior ASO Specialist</div>
        <div class="company">Cosmolink Global Solution</div>
        <div class="date">2021</div>
        <ul class="job-description">
          <li>Keyword Research & Optimization for app stores</li>
          <li>A/B tested icons, screenshots, and video previews to improve CTR</li>
          <li>Analyzed competitor creatives and adapted best practices</li>
          <li>Tools: AppTweak, MobileAction, Google Play Console, App Store Connect</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">WordPress Developer</div>
        <div class="company">Bricksharts Technology</div>
        <div class="date">2021</div>
        <ul class="job-description">
          <li>Theme & Plugin Development</li>
          <li>Page Builders & Gutenberg</li>
          <li>Performance Optimization</li>
          <li>Security & Maintenance</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">Junior SEO Specialist</div>
        <div class="company">WBridge Island Cove</div>
        <div class="date">2019 - 2020</div>
        <ul class="job-description">
          <li>On-Page SEO optimization (meta descriptions, title tags, header structure)</li>
          <li>Keyword research and implementation</li>
          <li>Content optimization for target keywords</li>
          <li>Internal linking strategy improvement</li>
          <li>Technical SEO fixes (broken links, redirects, sitemap)</li>
          <li>Local SEO optimization for business listings</li>
          <li>SEO performance monitoring via Google Analytics & Search Console</li>
          <li>Competitor keyword analysis and gap identification</li>
        </ul>
      </div>
    </div>

    <div class="two-col">
      <div>
        <div class="section">
          <div class="section-title">Education</div>
          <div class="job">
            <div class="job-title">BS Information Technology</div>
            <div class="company">Samar State University</div>
            <div class="date">2015 - 2018</div>
          </div>
        </div>
      </div>
      <div>
        <div class="section">
          <div class="section-title">Core Competencies</div>
          <div class="skills-tags">
            <span class="skill-tag">SEO</span>
            <span class="skill-tag">On-Page SEO</span>
            <span class="skill-tag">Off-Page SEO</span>
            <span class="skill-tag">WordPress</span>
            <span class="skill-tag">ASO</span>
            <span class="skill-tag">VPS</span>
            <span class="skill-tag">cPanel/WHM</span>
            <span class="skill-tag">GA4</span>
            <span class="skill-tag">Linux</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>`;
  
  const blob = new Blob([cvContent], { type: 'text/html' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'Obeth_Silawan_Complete_CV.html';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
</script>
</body>
</html>
"""

# Render the HTML
components.html(portfolio_html, height=2500, scrolling=True)
