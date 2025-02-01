# 🚀 AI-Powered Hugo Static Site Generator

## 📌 Overview
This project is a fully containerized **AI-enhanced static site generator** using **Hugo, TailwindCSS, Alpine.js, and Docker**. It includes **AI-generated content, multilingual support, social media automation, and performance optimizations**. The site can be deployed seamlessly to **GitHub Pages, Cloudflare Pages, or Netlify** with automated CI/CD pipelines.

## 🎯 Features
- **✅ AI-Generated Content** - Automatically generate blog posts using OpenAI API.
- **✅ Multilingual Support (i18n)** - Dynamic language switching.
- **✅ Live Editing via PagesCMS** - Users can update Markdown content visually.
- **✅ TailwindCSS & Alpine.js** - Modern UI and interactivity.
- **✅ Automated Deployment (CI/CD)** - Push to GitHub, auto-deploys.
- **✅ Hugo Pipes Optimization** - Minified CSS/JS, image processing.
- **✅ Social Media Automation** - Auto-share new blog posts to Twitter, Facebook, Instagram, LinkedIn, and TikTok.
- **✅ UTM Tracking** - Track analytics for shared posts.
- **✅ Fully Dockerized** - No local dependencies required.

---

## 📂 Folder Structure
```
/my-ai-hugo-site
│── /assets
│   │── /css
│   │   ├── main.css               # TailwindCSS main styles
│── /content
│   │── /en                        # English content
│   │── /es                        # Spanish content
│   │── /fr                        # French content
│   │── /de                        # German content
│   │── /blog                      # Blog posts (Markdown)
│── /layouts
│   │── /partials
│   │   ├── head.html               # Includes Tailwind & Alpine.js
│   │   ├── image.html              # Hugo Pipes Image Optimization
│── /public                         # Hugo output directory (generated)
│── /static
│   │── /css
│   │   ├── style.css               # Compiled TailwindCSS output
│   │── /images
│   │   ├── /uploads                # CMS Image Uploads
│── /themes                         # Custom Hugo themes (optional)
│── /scripts
│   │── generate_content.py         # AI-powered blog post generator
│   │── share_post.py               # Social media auto-sharing
│── /docker                         # Docker configurations (optional)
│── .github
│   │── /workflows
│   │   ├── deploy.yml              # CI/CD GitHub Actions
│── config.yaml                      # PagesCMS configuration
│── Dockerfile                        # Containerized setup
│── docker-compose.yml                # Local development setup
│── netlify.toml                      # Netlify settings (if using)
│── cloudflare-pages.yml               # Cloudflare settings (if using)
│── package.json                      # TailwindCSS & PostCSS configuration
│── tailwind.config.js                 # TailwindCSS setup
│── config.toml                        # Hugo configuration
```

---

## 🛠 Installation & Setup
### 1️⃣ Clone the repository
```sh
git clone https://github.com/daluj/my-ai-hugo-site.git
cd my-ai-hugo-site
```

### 2️⃣ Set up environment variables
Create a `.env` file in the root directory and add your API keys:
```sh
OPENAI_API_KEY=your_openai_key
TWITTER_API_KEY=your_twitter_key
FACEBOOK_ACCESS_TOKEN=your_facebook_token
LINKEDIN_ACCESS_TOKEN=your_linkedin_token
INSTAGRAM_ACCESS_TOKEN=your_instagram_token
TIKTOK_ACCESS_TOKEN=your_tiktok_token
```

### 3️⃣ Run the development server
Using Docker:
```sh
docker-compose up
```

Without Docker:
```sh
hugo server --bind=0.0.0.0 --port=1313 --disableFastRender
```
Then, open `http://localhost:1313` in your browser.

---

## 🔄 AI Content Generation
Generate an AI-powered blog post:
```sh
python scripts/generate_content.py
```
It will prompt for a topic, generate a post, and save it to the `/content/blog/` directory.

---

## 📢 Automate Social Media Sharing
Automatically share new blog posts to social media:
```sh
python scripts/share_post.py
```
This will share the latest blog post to **Twitter, Facebook, Instagram, LinkedIn, and TikTok** with **UTM tracking**.

---

## 🚀 Deployment
This project supports **GitHub Actions, Netlify, and Cloudflare Pages** for automated deployments.

### Deploy to GitHub Pages
1. Push your changes to `main`.
2. The GitHub Actions workflow will build and deploy the site automatically.

### Deploy to Netlify
1. Connect the repository to Netlify.
2. Set `hugo --minify` as the build command.
3. Deploy and enjoy!

### Deploy to Cloudflare Pages
1. Connect the repository to Cloudflare Pages.
2. Set Hugo as the framework.
3. Deploy the site automatically.

---

## 📌 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## ✨ Acknowledgments
- [Hugo](https://gohugo.io/)
- [TailwindCSS](https://tailwindcss.com/)
- [Alpine.js](https://alpinejs.dev/)
- [OpenAI](https://openai.com/)

Happy coding! 🚀