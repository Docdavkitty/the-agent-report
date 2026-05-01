#!/usr/bin/env python3
"""Generate per-article OG images for The Agent Report."""
import os, re, sys
from PIL import Image, ImageDraw, ImageFont

POSTS_DIR = "_posts"
OG_DIR = "assets/images/og"
BASE = os.path.dirname(os.path.abspath(__file__)) + "/.."

CATEGORY_COLORS = {
    "hermes-agent": "#6c5ce7",
    "research": "#74b9ff",
    "tools-frameworks": "#00cec9",
    "industry": "#fdcb6e",
    "opinion": "#e84393",
    "openclaw": "#a29bfe",
}

W, H = 1200, 630

def get_text_image(text, font_path, max_width, font_size=48):
    """Find best font size to fit text within max_width."""
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()
    
    # Split into lines that fit
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test = current_line + " " + word if current_line else word
        bbox = font.getbbox(test)
        tw = bbox[2] - bbox[0]
        if tw <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines, font

def generate_og(title, slug, categories, date_str):
    """Generate a 1200x630 OG image."""
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)
    
    # Gradient background
    for y in range(H):
        r = int(15 + (24 - 15) * y / H)
        g = int(15 + (24 - 15) * y / H)
        b = int(19 + (30 - 19) * y / H)
        for x in range(0, W, 4):
            draw.point((x, y), fill=(r, g, b, 255))
    
    # Decorative circles
    for cx, cy, r in [(200, 200, 180), (1000, 150, 250), (600, 500, 150)]:
        for i in range(0, 360, 5):
            import math
            x = cx + int(r * math.cos(math.radians(i)))
            y = cy + int(r * math.sin(math.radians(i)))
            if 0 <= x < W and 0 <= y < H:
                draw.point((x, y), fill=(42, 42, 53, 80))
    
    # Accent line at top
    cat_color = CATEGORY_COLORS.get(categories[0] if categories else "default", "#6c5ce7")
    for x in range(60, 200):
        for y in range(40, 44):
            r, g, b = int(cat_color[1:3], 16), int(cat_color[3:5], 16), int(cat_color[5:7], 16)
            draw.point((x, y), fill=(r, g, b, 255))
    
    # Category badge
    cat_text = (categories[0] or "").replace("-", " ").title() if categories else ""
    try:
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    except:
        font_small = ImageFont.load_default()
    draw.text((60, 60), cat_text, fill=cat_color, font=font_small) if cat_text else None
    
    # Title
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
    except:
        font_title = ImageFont.load_default()
    
    lines, _ = get_text_image(title, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", W - 120, 52)
    
    y_pos = 130
    for line in lines[:4]:  # Max 4 lines
        bbox = font_title.getbbox(line)
        tw = bbox[2] - bbox[0]
        x_pos = (W - tw) // 2
        draw.text((x_pos, y_pos), line, fill=(232, 232, 237, 255), font=font_title)
        y_pos += 60
    
    # Date
    try:
        font_date = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        font_date = ImageFont.load_default()
    draw.text((60, H - 60), date_str, fill=(92, 92, 110, 255), font=font_date)
    
    # "The Agent Report" at bottom-right
    draw.text((W - 300, H - 60), "The Agent Report", fill=(108, 92, 231, 255), font=font_date)
    
    # Save
    out_path = os.path.join(BASE, OG_DIR, f"{slug}.png")
    img.save(out_path, "PNG")
    return out_path

def main():
    posts_dir = os.path.join(BASE, POSTS_DIR)
    if not os.path.isdir(posts_dir):
        print(f"Posts directory not found: {posts_dir}")
        return
    
    os.makedirs(os.path.join(BASE, OG_DIR), exist_ok=True)
    
    for fname in sorted(os.listdir(posts_dir)):
        if not fname.endswith(".md"):
            continue
        
        # Extract slug from filename (remove date prefix)
        parts = fname.replace(".md", "").split("-", 3)
        slug = "-".join(parts[3:]) if len(parts) > 3 else parts[-1]
        
        out = os.path.join(BASE, OG_DIR, f"{slug}.png")
        if os.path.exists(out):
            print(f"  ✓ {slug}.png already exists")
            continue
        
        # Parse frontmatter
        content = open(os.path.join(posts_dir, fname)).read()
        fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            print(f"  ? {fname}: no frontmatter found")
            continue
        
        fm_text = fm_match.group(1)
        title = ""
        categories = []
        date_str = ""
        
        for line in fm_text.split("\n"):
            line = line.strip()
            if line.startswith("title:"):
                title = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("categories:"):
                rest = line.split(":", 1)[1].strip()
                if rest.startswith("["):
                    categories = [c.strip().strip("'").strip('"') for c in rest.strip("[]").split()]
                else:
                    categories = rest.split()
            elif line.startswith("date:"):
                date_full = line.split(":", 1)[1].strip()
                date_str = date_full.split()[0] if date_full else ""
        
        if not title:
            print(f"  ? {fname}: no title found")
            continue
        
        try:
            out_path = generate_og(title, slug, categories, date_str)
            print(f"  ✓ {slug}.png generated")
        except Exception as e:
            print(f"  ✗ {slug}.png failed: {e}")

if __name__ == "__main__":
    main()
