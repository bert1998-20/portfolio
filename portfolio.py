import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Obeth Gabiana Silawan | AI Engineer & SEO Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default elements
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {margin: 0; padding: 0;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
""", unsafe_allow_html=True)

# Your HTML portfolio
portfolio_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Obeth Gabiana Silawan | AI Engineer & SEO Specialist Portfolio</title>
<meta name="description" content="Obeth Gabiana Silawan - AI Engineer, SEO Specialist, Jr Data Analyst, WordPress Developer, and Server Administrator">
<meta name="keywords" content="AI Engineer, SEO Specialist, Jr Data Analyst, WordPress Developer, Server Administrator">
<meta name="author" content="Obeth Gabiana Silawan">

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
  padding: 24px 8%;
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
  font-size: 28px;
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
  margin-left: 32px;
  font-size: 15px;
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
  min-height: 88vh;
  padding: 50px 8%;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  align-items: center;
  gap: 50px;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 20px;
  border: 1px solid rgba(125,249,255,.45);
  border-radius: 50px;
  color: #7df9ff;
  background: rgba(125,249,255,.08);
  margin-bottom: 28px;
  font-size: 14px;
  font-weight: 500;
  backdrop-filter: blur(5px);
}

.badge::before {
  content: '✨';
  font-size: 16px;
}

.hero h1 {
  font-size: 68px;
  line-height: 1.08;
  margin-bottom: 24px;
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
  font-size: 18px;
  line-height: 1.7;
  color: #d6dcff;
  margin-bottom: 36px;
}

.buttons {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.btn {
  padding: 14px 32px;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 700;
  font-size: 15px;
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
  gap: 40px;
  margin-top: 40px;
  flex-wrap: wrap;
}

.stat-number {
  font-size: 32px;
  font-weight: 800;
  color: #7df9ff;
  display: block;
}

.stat-label {
  font-size: 13px;
  color: #a0a8e0;
  letter-spacing: 1px;
}

.avatar-wrap {
  perspective: 1200px;
  display: flex;
  justify-content: center;
}

.avatar-card {
  width: 400px;
  height: 620px;
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
  50% { transform: translateY(-20px) rotateY(5deg); }
}

.character {
  position: absolute;
  left: 50%;
  top: 70px;
  transform: translateX(-50%) translateZ(80px);
  width: 260px;
  height: 380px;
}

.hair {
  position: absolute;
  top: 0;
  left: 25px;
  width: 210px;
  height: 150px;
  background: linear-gradient(135deg, #0f1530, #5a50dd);
  border-radius: 55% 55% 40% 40%;
  box-shadow: 0 0 30px rgba(109,97,255,.6);
}

.face {
  position: absolute;
  top: 70px;
  left: 50px;
  width: 160px;
  height: 170px;
  background: #ffddcf;
  border-radius: 50% 50% 45% 45%;
}

.eye {
  position: absolute;
  top: 70px;
  width: 22px;
  height: 28px;
  background: #071030;
  border-radius: 50%;
  transition: all 0.1s ease;
}

.eye.left { left: 42px; }
.eye.right { right: 42px; }

.mouth {
  position: absolute;
  bottom: 48px;
  left: 68px;
  width: 24px;
  height: 10px;
  border-bottom: 3px solid #b85c6a;
  border-radius: 50%;
}

.body {
  position: absolute;
  top: 248px;
  left: 20px;
  width: 220px;
  height: 140px;
  background: linear-gradient(135deg, #1a2eff, #8a5cff);
  border-radius: 50px 50px 30px 30px;
  box-shadow: 0 0 25px rgba(125,249,255,.3);
}

.code-chip {
  position: absolute;
  bottom: 20px;
  left: 20px;
  right: 20px;
  padding: 15px;
  border-radius: 20px;
  background: rgba(0,0,0,.6);
  color: #dffcff;
  border: 1px solid rgba(125,249,255,.3);
  font-size: 11px;
  line-height: 1.7;
  text-align: center;
  transform: translateZ(60px);
  backdrop-filter: blur(8px);
}

section {
  padding: 80px 8%;
}

.section-title {
  font-size: 46px;
  margin-bottom: 16px;
  background: linear-gradient(135deg, #fff, #7df9ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-weight: 700;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
}

.card {
  padding: 32px;
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

.about-box {
  padding: 40px;
  border-radius: 32px;
  background: linear-gradient(145deg, rgba(125,249,255,.1), rgba(255,255,255,.04));
  border: 1px solid rgba(125,249,255,.2);
}

.contact-box {
  text-align: center;
  padding: 60px;
  border-radius: 40px;
  background: linear-gradient(135deg, rgba(125,249,255,.12), rgba(155,108,255,.1));
  border: 1px solid rgba(255,255,255,.15);
}

footer {
  padding: 30px;
  text-align: center;
  color: #bfc5ff;
  border-top: 1px solid rgba(255,255,255,.08);
}

@media(max-width: 850px) {
  .hero {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .hero h1 {
    font-size: 48px;
  }
  .grid {
    grid-template-columns: 1fr;
  }
  .avatar-card {
    width: 340px;
    height: 580px;
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
    <a href="#contact">Contact</a>
  </nav>
</header>

<section class="hero">
  <div>
    <div class="badge">✨ AI Engineer & SEO Specialist & Jr Data Analyst</div>
    <h1>Hi, I'm <span>Obeth Gabiana Silawan</span></h1>
    <p>
      Senior SEO Specialist, Jr Data Analyst, AI-driven digital builder, WordPress Developer, and Server Administrator.
      I create intelligent websites, automation systems, data-driven insights, and search-optimized digital
      experiences that help brands grow smarter in the modern world.
    </p>
    
    <div class="stats">
      <div>
        <span class="stat-number">5+</span>
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
      <a href="https://scatter-dashboard-bert.streamlit.app/" target="_blank" class="btn btn-primary">📊 View My Work</a>
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
        🔍 Senior SEO Specialist | 📊 Jr Data Analyst<br>
        🖥️ Server Admin (VPS) | aaPanel | cPanel | WHM | HPanel<br>
        🔄 Website Migration | Database Transfer
      </div>
    </div>
  </div>
</section>

<section id="about">
  <h2 class="section-title">About Me</h2>
  <div class="about-box">
    <p>I am <strong>Obeth Gabiana Silawan</strong>, a passionate technology professional from Samar Island with a strong background in <strong>Senior SEO</strong>, <strong>Jr Data Analysis</strong>, <strong>WordPress development</strong>, and <strong>Server Administration</strong>. My interest in coding started when I was young, and that curiosity pushed me to keep learning, exploring, and improving every single day.</p>
    <p>I believe that knowledge becomes powerful when it is turned into real solutions. Through personal study, hands-on work, and conversations with experienced developers and IT professionals, I learned how to transform information into useful systems, better websites, and smarter strategies that deliver measurable results.</p>
    <p>My mission is to build websites and digital systems that are functional, user-friendly, visually attractive, search-friendly, powered by smart data analytics, and hosted on reliable server infrastructure.</p>
    <p><strong>✨ Core Philosophy:</strong> "Build smart, optimize constantly, analyze data deeply, and let insights drive decisions."</p>
  </div>
</section>

<section id="experience">
  <h2 class="section-title">Work Experience</h2>
  <p class="section-desc">A detailed look at my professional journey, positions held, and key accomplishments.</p>

  <div class="grid">
    <div class="card">
      <h3>🔹 Senior SEO Specialist</h3>
      <p><strong>Self-employed / Freelance</strong> | 2026 - Present</p>
      <ul>
        <li>VPS Setup & Configuration for optimal server performance</li>
        <li>aaPanel, cPanel, WHM, hPanel Administration and Management</li>
        <li>Website Migration between hosting providers with zero downtime</li>
        <li>Database to Database Transfer ensuring data integrity</li>
        <li>Technical SEO Audits and implementation</li>
        <li>Black Hat SEO strategies for Casino India Market</li>
        <li>Click fraud and bot traffic bypass techniques</li>
        <li>Cloaking implementation (showing different content to users vs search engines)</li>
        <li>Private Blog Networks (PBNs) setup and management</li>
        <li>GMB/GBP/Bing Business verification bypass</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 SEO Team Lead</h3>
      <p><strong>Freelance</strong> | 2024 - 2025</p>
      <ul>
        <li>Led a team of SEO specialists to design and implement SEO strategies</li>
        <li>Created roadmaps for India Casino Market SEO campaigns</li>
        <li>Managed technical SEO audits and link-building campaigns</li>
        <li>Analyzed performance via Google Analytics 4 (GA4) and Search Console</li>
        <li>Translated data insights into scalable actionable strategies</li>
        <li>Collaborated with cross-functional teams for SEO integration</li>
        <li>Managed local SEO citations and directory listings</li>
        <li>Monitored and disavowed toxic backlinks</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 WordPress Developer</h3>
      <p><strong>IE Soft Technology</strong> | 2024</p>
      <ul>
        <li>Theme & Plugin Development from scratch</li>
        <li>Page Builders (Elementor, Gutenberg) customization</li>
        <li>Performance Optimization (speed, caching, CDN)</li>
        <li>Security hardening and malware removal</li>
        <li>Custom post types and advanced custom fields</li>
        <li>WooCommerce store setup and optimization</li>
        <li>Responsive design implementation</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 SEO Freelance</h3>
      <p><strong>Self-employed</strong> | 2024 - 2025</p>
      <ul>
        <li>Managed 20+ client accounts across various industries</li>
        <li>On-page and off-page SEO optimization</li>
        <li>Local SEO for small businesses</li>
        <li>Technical SEO fixes and site migrations</li>
        <li>Monthly reporting and strategy calls</li>
        <li>Black Hat SEO services for Casino India Market</li>
        <li>Auto-generated content and backlinks injection for High DA/DR</li>
        <li>Negative SEO campaigns and protection</li>
      </ul>
    </div>

     <div class="card">
      <h3>🔹 Junior ASO Specialist</h3>
      <p><strong>Various Clients</strong> | 2021</p>
      <ul>
        <li>Keyword Research & Optimization for app stores</li>
        <li>A/B tested icons, screenshots, and video previews to improve CTR</li>
        <li>Analyzed competitor creatives and adapted best practices</li>
        <li>Tools used: AppTweak, MobileAction, Google Play Console, App Store Connect</li>
        <li>Improved app rankings and conversion rates</li>
        <li>Localized app store listings for international markets</li>
      </ul>
    </div>

    <div class="card">
      <h3>🔹 Junior SEO Specialist</h3>
      <p><strong>WBridge Island Cove</strong> | 2019 - 2020</p>
      <ul>
        <li>Supported organic growth for multiple client websites</li>
        <li>Improved URL structures, header tags, and meta descriptions</li>
        <li>Updated old content for freshness and search relevance</li>
        <li>Monitored keyword rankings and organic traffic</li>
        <li>Used Google Analytics and Search Console for reporting</li>
        <li>Assisted in backlink analysis and competitor research</li>
      </ul>
    </div>

  </div>
</section>

<section id="skills">
  <h2 class="section-title">Skills & Expertise</h2>
  <p class="section-desc">A comprehensive skill set combining SEO mastery, Data Analysis, Server Administration, AI integration, and web development.</p>

  <div class="grid">
    <div class="card">
      <h3>🔍 Senior SEO</h3>
      <ul>
        <li>On-Page SEO Optimization</li>
        <li>Technical SEO Audits</li>
        <li>Local SEO Strategies</li>
        <li>Off-Page & Link Building</li>
        <li>Keyword Research & Strategy</li>
        <li>SEO Analytics & Reporting</li>
        <li>Black Hat SEO (PBNs, Cloaking)</li>
        <li>Casino India Market Specialist</li>
        <li>GMB/GBP Bypass Verification</li>
      </ul>
    </div>

    <div class="card">
      <h3>📊 Jr Data Analyst</h3>
      <ul>
        <li>Data Collection & Cleaning</li>
        <li>Exploratory Data Analysis (EDA)</li>
        <li>Data Visualization (Charts, Graphs)</li>
        <li>SQL Querying & Database Analysis</li>
        <li>Excel / Google Sheets Analytics</li>
        <li>Business Intelligence Reporting</li>
        <li>GA4 & Search Console Analysis</li>
      </ul>
    </div>

    <div class="card">
      <h3>🖥️ Server & Hosting</h3>
      <ul>
        <li>VPS Setup & Configuration</li>
        <li>Self-Managed Hosting</li>
        <li>aaPanel Installation & Management</li>
        <li>cPanel & WHM Administration</li>
        <li>hPanel Management</li>
        <li>Website Migration</li>
        <li>Database to Database Transfer</li>
        <li>Linux Server Management</li>
      </ul>
    </div>

    <div class="card">
      <h3>🤖 AI & Automation</h3>
      <ul>
        <li>Advanced Prompt Engineering</li>
        <li>AI Workflow Automation</li>
        <li>Content Generation Strategy</li>
        <li>Smart Process Optimization</li>
        <li>AI-Powered Data Analysis</li>
        <li>Chatbot Integration</li>
      </ul>
    </div>

    <div class="card">
      <h3>💻 WordPress Development</h3>
      <ul>
        <li>Custom Theme Development</li>
        <li>Plugin Development & Customization</li>
        <li>Website Speed Optimization</li>
        <li>Security & Maintenance</li>
        <li>WooCommerce Setup</li>
        <li>Page Builders (Elementor, Gutenberg)</li>
      </ul>
    </div>

    <div class="card">
      <h3>📱 ASO & Mobile</h3>
      <ul>
        <li>App Store Optimization</li>
        <li>Google Play Console Management</li>
        <li>App Store Connect Management</li>
        <li>Keyword Research for Apps</li>
        <li>Creative A/B Testing</li>
        <li>Competitor Analysis</li>
      </ul>
    </div>
  </div>
</section>

<section id="contact">
  <div class="contact-box">
    <h2>Let's Build Something Intelligent</h2>
    <p>Ready to create an AI-powered, SEO-friendly, data-driven digital experience? Let's collaborate and bring your vision to life.</p>
    <div style="margin-bottom: 20px;">
      <p>📞 +63 9564574637</p>
      <p>✉️ ieph.bert888@gmail.com</p>
      <p>📍 San Leon Umingan Pangasinan</p>
    </div>
    <a href="mailto:ieph.bert888@gmail.com" class="btn btn-primary">✉️ Contact Me</a>
  </div>
</section>

<footer>
  © 2026 Obeth Gabiana Silawan | AI Engineer | Senior SEO Specialist | Jr Data Analyst | Server Administrator | Built with 💙
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

// Download CV function with complete detailed experience
function downloadCV() {
  const cvContent = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Obeth Gabiana Silawan - Detailed CV</title>
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
  .tagline { color: #4a5568; font-size: 14px; margin-top: 10px; }
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
  .special-box {
    background: #1a202c;
    padding: 20px;
    border-radius: 12px;
    margin: 20px 0;
  }
  .special-box h3 { color: #fbbf24; margin-bottom: 15px; }
  .special-box p { color: #e2e8f0; font-size: 13px; margin: 8px 0; }
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
  @media (max-width: 768px) {
    .header { grid-template-columns: 1fr; text-align: center; }
    .contact-info { text-align: center; }
    .two-col { grid-template-columns: 1fr; }
    .cv-content { padding: 20px; }
  }
</style>
</head>
<body>
<div class="cv-container">
  <div class="cv-content">
    <div class="header">
      <div class="name-title">
        <h1>OBETH GABIANA SILAWAN</h1>
        <div class="title">Senior SEO Specialist | Black Hat SEO Expert | WordPress Developer | Jr Data Analyst</div>
        <div class="tagline">"Turning information into real understanding through experience and innovation"</div>
      </div>
      <div class="contact-info">
        <p>📞 +63 9564574637</p>
        <p>✉️ ieph.bert888@gmail.com</p>
        <p>📍 San Leon Umingan Pangasinan</p>
      </div>
    </div>

    <div class="section">
      <div class="section-title">Professional Summary</div>
      <p style="line-height: 1.6; color: #4a5568;">As a young coder from Samar, I left home seeking deeper knowledge and skills to thrive in a fast-changing world. My journey led me to explore what it takes to succeed in the 21st century. I've discovered through years of study and insights from experienced IT professionals that turning information into real understanding is the real challenge. With 5+ years of experience in SEO, WordPress development, data analysis, and server administration, I deliver results-driven digital solutions.</p>
    </div>

  <h3>🛡️ White Hat SEO & Server Management Expertise</h3>
<p>• VPS Self-Managed Setup & Configuration (DigitalOcean, Vultr, Linode)</p>
<p>• aaPanel Installation & Management for Linux Servers</p>
<p>• cPanel & WHM Administration</p>
<p>• hPanel Management & Configuration</p>
<p>• Website Migration (Server to Server, Zero Downtime)</p>
<p>• Database to Database Transfer (MySQL, PostgreSQL)</p>
<p>• Self-Managed Hosting Environment Setup</p>
<p>• Nginx / Apache Web Server Configuration</p>
<p>• SSL Certificate Installation (Let's Encrypt, Commercial)</p>
<p>• Server Security Hardening & Firewall Setup</p>
<p>• WordPress Optimization on VPS Environments</p>
<p>• DNS Management & Domain Configuration</p>
<p>• Linux Command Line Operations (Ubuntu, CentOS, Debian)</p>


    <div class="section">
      <div class="section-title">Work Experience</div>
      
      <div class="job">
        <div class="job-title">Senior SEO Specialist</div>
        <div class="company">Self-employed / Freelance</div>
        <div class="date">2026 - Present</div>
        <ul class="job-description">
          <li>VPS Setup & Configuration for optimal server performance</li>
          <li>aaPanel, cPanel, WHM, hPanel Administration and Management</li>
          <li>Website Migration between hosting providers with zero downtime</li>
          <li>Database to Database Transfer ensuring data integrity</li>
          <li>Technical SEO Audits and implementation</li>
          <li>Black Hat SEO strategies for Casino India Market</li>
          <li>Click fraud and bot traffic bypass techniques</li>
          <li>Private Blog Networks (PBNs) setup and management</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">SEO Team Lead</div>
        <div class="company">Freelance</div>
        <div class="date">2024 - 2025</div>
        <ul class="job-description">
          <li>Led a team of SEO specialists to design and implement SEO strategies</li>
          <li>Created roadmaps for India Casino Market SEO campaigns</li>
          <li>Managed technical SEO audits and link-building campaigns</li>
          <li>Analyzed performance via Google Analytics 4 (GA4) and Search Console</li>
          <li>Translated data insights into scalable actionable strategies</li>
          <li>Collaborated with cross-functional teams for SEO integration</li>
          <li>Managed local SEO citations and directory listings</li>
          <li>Monitored and disavowed toxic backlinks</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">WordPress Developer</div>
        <div class="company">IE Soft Technology</div>
        <div class="date">2024</div>
        <ul class="job-description">
          <li>Theme & Plugin Development from scratch</li>
          <li>Page Builders (Elementor, Gutenberg) customization</li>
          <li>Performance Optimization (speed, caching, CDN)</li>
          <li>Security hardening and malware removal</li>
          <li>Custom post types and advanced custom fields</li>
          <li>WooCommerce store setup and optimization</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">Junior SEO Specialist</div>
        <div class="company">WBridge Island Cove</div>
        <div class="date">2019 - 2020</div>
        <ul class="job-description">
          <li>Supported organic growth for multiple client websites</li>
          <li>Improved URL structures, header tags, and meta descriptions</li>
          <li>Updated old content for freshness and search relevance</li>
          <li>Monitored keyword rankings and organic traffic</li>
          <li>Used Google Analytics and Search Console for reporting</li>
          <li>Assisted in backlink analysis and competitor research</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">Junior ASO Specialist</div>
        <div class="company">Various Clients</div>
        <div class="date">2021</div>
        <ul class="job-description">
          <li>Keyword Research & Optimization for app stores</li>
          <li>A/B tested icons, screenshots, and video previews to improve CTR</li>
          <li>Analyzed competitor creatives and adapted best practices</li>
          <li>Tools used: AppTweak, MobileAction, Google Play Console, App Store Connect</li>
          <li>Improved app rankings and conversion rates</li>
          <li>Localized app store listings for international markets</li>
        </ul>
      </div>

      <div class="job">
        <div class="job-title">SEO Freelance</div>
        <div class="company">Self-employed</div>
        <div class="date">2024 - 2025</div>
        <ul class="job-description">
          <li>Managed 20+ client accounts across various industries</li>
          <li>On-page and off-page SEO optimization</li>
          <li>Local SEO for small businesses</li>
          <li>Technical SEO fixes and site migrations</li>
          <li>Monthly reporting and strategy calls</li>
          <li>Black Hat SEO services for Casino India Market</li>
          <li>Auto-generated content and backlinks injection for High DA/DR</li>
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
          <div class="job">
            <div class="job-title">Secondary Education</div>
            <div class="company">CNCHS High School</div>
            <div class="date">2011 - 2014</div>
          </div>
        </div>

        <div class="section">
          <div class="section-title">Languages</div>
          <div class="job">
            <div class="job-title">English</div>
            <div class="company">Fluent - Professional Working Proficiency</div>
          </div>
          <div class="job">
            <div class="job-title">Tagalog / Filipino</div>
            <div class="company">Native Speaker</div>
          </div>
        </div>
      </div>

      <div>
        <div class="section">
          <div class="section-title">Core Competencies</div>
          <div class="skills-tags">
            <span class="skill-tag">VPS Setup</span>
            <span class="skill-tag">aaPanel</span>
            <span class="skill-tag">cPanel/WHM</span>
            <span class="skill-tag">WordPress</span>
            <span class="skill-tag">SEO</span>
            <span class="skill-tag">Black Hat SEO</span>
            <span class="skill-tag">Data Analysis</span>
            <span class="skill-tag">GA4</span>
            <span class="skill-tag">Search Console</span>
            <span class="skill-tag">Linux</span>
            <span class="skill-tag">HTML/CSS</span>
            <span class="skill-tag">JavaScript</span>
            <span class="skill-tag">SQL</span>
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Streamlit</span>
          </div>
        </div>

        <div class="section">
          <div class="section-title">Companies / Clients</div>
          <div class="skills-tags">
            <span class="skill-tag">LEVENDER GROUPS</span>
            <span class="skill-tag">ELEVATE OUTSOURCING</span>
            <span class="skill-tag">BRICKSHARTS TECHNOLOGY</span>
            <span class="skill-tag">COSMOLINK GLOBAL SOLUTION</span>
            <span class="skill-tag">All World SEO</span>
          </div>
        </div>

        <div class="section">
          <div class="section-title">References</div>
          <div class="job">
            <div class="job-title">Prince Alojado</div>
            <div class="company">All World SEO / Manager</div>
            <div>📞 09095699870</div>
            <div>✉️ princealojado12@gmail.com</div>
          </div>
          <div class="job">
            <div class="job-title">Aladin Legazpi</div>
            <div class="company">All World SEO / CEO</div>
            <div>📱 Telegram: @aladinlegaspi</div>
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
  a.download = 'Obeth_Silawan_Detailed_CV.html';
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
components.html(portfolio_html, height=2000, scrolling=True)
