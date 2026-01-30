import os
import glob
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from matplotlib.colors import LinearSegmentedColormap
POSTS_DIR = "_posts/"
OUTPUT_IMAGE = "images/blog/wordcloud.png"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def get_site_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = [
        "#8998ac",
        "#6b7c93",
        "#2c3e50",
        "#5a6b7c",
        "#34495e",
        "#7f8c8d",
    ]
    return colors[random_state.randint(0, len(colors) - 1)]
def clean_text(text):
    text = re.sub(r'^---[\s\S]*?---', '', text)
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'`[^`]*`', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\$\$[\s\S]*?\$\$', '', text)
    text = re.sub(r'\$[^$]*\$', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    return text
def generate_cloud():
    all_text = ""
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            all_text += clean_text(content) + " "
    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update([
        "will", "can", "using", "use", "one", "also", "make", "new", 
        "first", "time", "now", "two", "way", "post", "blog", "figure",
        "example", "need", "value", "function", "set", "result", "form",
        "case", "problem", "well", "work", "point", "see", "Siddharth",
        "Maddali", "image", "eq", "equation", "ref", "frac", "left", "right"
    ])
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
    if not os.path.exists(os.path.dirname(OUTPUT_IMAGE)):
        os.makedirs(os.path.dirname(OUTPUT_IMAGE))
    wc.to_file(OUTPUT_IMAGE)
    print(f"Word cloud saved to {OUTPUT_IMAGE}")
if __name__ == "__main__":
    generate_cloud()
