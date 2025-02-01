import openai
import os

def generate_blog_post(topic):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    prompt = f"Write a detailed blog post about {topic}. Include key insights and takeaways."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful blog writer."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"].strip()

if __name__ == "__main__":
    topic = input("Enter blog topic: ")
    blog_content = generate_blog_post(topic)
    print("\nGenerated Blog Post:\n")
    print(blog_content)
    
    with open(f"content/{topic.replace(' ', '_').lower()}.md", "w") as f:
        f.write(f"---\ntitle: {topic}\n---\n\n{blog_content}")