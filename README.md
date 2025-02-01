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
├── assets
│   ├── css
│   │   └── main.css
│   └── js
│       ├── alpine.js
│       └── custom.js
├── cloudflare-pages.yml
├── config.toml
├── config.yaml
├── content
│   ├── blog
│   ├── de
│   ├── en
│   │   └── blog
│   │       └── welcome.md
│   ├── es
│   └── fr
├── docker-compose.yml
├── Dockerfile
├── layouts
│   ├── _default
│   │   ├── baseof.html
│   │   ├── list.html
│   │   ├── single.html
│   │   └── taxonomy.html
│   ├── partials
│   │   ├── darkmode.html
│   │   ├── head.html
│   │   ├── image.html
│   │   ├── langswitcher.html
│   │   ├── meta.html
│   │   └── scripts.html
│   └── shortcodes
│       └── ai_content.html
├── netlify.toml
├── package.json
├── public
├── README.md
├── resources
│   └── _gen
│       ├── assets
│       └── images
├── scripts
│   ├── generate_content.py
│   └── share_post.py
├── static
│   ├── css
│   └── images
│       └── uploads
├── tailwind.config.js
└── themes
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

## Fill the public folder

Enter the Hugo container. Open a shell inside the Hugo container:
```sh
docker exec -it hugo_dev /bin/sh
```
Once inside the container run:
```sh
hugo --minify
```

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