import requests
import os

def generate_utm_link(base_url, source, medium, campaign):
    return f"{base_url}?utm_source={source}&utm_medium={medium}&utm_campaign={campaign}"

def share_to_platforms(title, url):
    utm_url = generate_utm_link(url, "social", "organic", "blog_promotion")
    
    platforms = {
        "twitter": os.getenv("TWITTER_API_KEY"),
        "facebook": os.getenv("FACEBOOK_ACCESS_TOKEN"),
        "linkedin": os.getenv("LINKEDIN_ACCESS_TOKEN"),
        "instagram": os.getenv("INSTAGRAM_ACCESS_TOKEN"),
        "tiktok": os.getenv("TIKTOK_ACCESS_TOKEN")
    }
    
    messages = {
        "twitter": f"New post: {title} - {utm_url}",
        "facebook": {"message": f"New blog post! {title}: {utm_url}"},
        "linkedin": {"content": {"title": title, "description": "Check out our new article!", "submitted-url": utm_url}},
        "instagram": {"caption": f"🔥 New Post! {title} 📖 Link in bio!"},
        "tiktok": {"title": f"New content: {title}!", "link": utm_url}
    }
    
    for platform, token in platforms.items():
        if token:
            response = requests.post(
                f"https://api.{platform}.com/share",
                headers={"Authorization": f"Bearer {token}"},
                json=messages[platform]
            )
            print(f"Shared to {platform}: ", response.json())

if __name__ == "__main__":
    post_title = input("Enter post title: ")
    post_url = input("Enter post URL: ")
    share_to_platforms(post_title, post_url)