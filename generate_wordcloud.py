import os
import glob
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from matplotlib.colors import LinearSegmentedColormap

# Configuration
POSTS_DIR = "_posts/"
OUTPUT_IMAGE = "images/blog/wordcloud.png"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" # Fallback font

# Website Palette
# Slate Blue: #8998ac
# Primary Dark: #6b7c93
# Text Color: #2c3e50
# Accent: #3498db
# Link: #5a6b7c

def get_site_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = [
        "#8998ac", # Primary
        "#6b7c93", # Primary Dark
        "#2c3e50", # Text
        "#5a6b7c", # Link
        "#34495e", # Dark Blue Grey
        "#7f8c8d", # Grey
    ]
    return colors[random_state.randint(0, len(colors) - 1)]

def clean_text(text):
    # Remove YAML Front Matter
    text = re.sub(r'^---[\s\S]*?---', '', text)
    
    # Remove Code Blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'`[^`]*`', '', text)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove LaTeX math (basic removal)
    text = re.sub(r'\$\$[\s\S]*?\$\$', '', text)
    text = re.sub(r'\$[^$]*\$', '', text)
    
    # Remove Links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    return text

def generate_cloud():
    all_text = ""
    
    # Read all markdown files
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            all_text += clean_text(content) + " "

    # Custom Stopwords
    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update([
        "will", "can", "using", "use", "one", "also", "make", "new", 
        "first", "time", "now", "two", "way", "post", "blog", "figure",
        "example", "need", "value", "function", "set", "result", "form",
        "case", "problem", "well", "work", "point", "see", "Siddharth",
        "Maddali", "image", "eq", "equation", "ref", "frac", "left", "right"
    ])

    # Generate WordCloud
    # Background color matches the site background (#fdfdfd)
    wc = WordCloud(
        width=1600,
        height=400,
        background_color="#fdfdfd",
        stopwords=custom_stopwords,
        max_words=100,
        min_font_size=10,
        color_func=get_site_color_func,
        random_state=42,
        prefer_horizontal=0.9
    )

    wc.generate(all_text)

    # Save to file
    if not os.path.exists(os.path.dirname(OUTPUT_IMAGE)):
        os.makedirs(os.path.dirname(OUTPUT_IMAGE))
        
    wc.to_file(OUTPUT_IMAGE)
    print(f"Word cloud saved to {OUTPUT_IMAGE}")

if __name__ == "__main__":
    generate_cloud()
