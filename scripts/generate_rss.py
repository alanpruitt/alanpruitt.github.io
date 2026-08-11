import os
import glob
import re
import xml.etree.ElementTree as ET
from datetime import datetime
import email.utils

def parse_markdown_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not frontmatter_match:
        return None
    
    yaml_text = frontmatter_match.group(1)
    meta = {}
    for line in yaml_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val.startswith('['):
                continue
            meta[key] = val
            
    basename = os.path.basename(filepath).replace('.md', '')
    meta['slug'] = f"articles/{basename}"
    return meta

def generate_rss_feed(output_dir="."):
    md_files = sorted(glob.glob(os.path.join(output_dir, "src", "articles", "*.md")))
    essays = []
    for f in md_files:
        meta = parse_markdown_frontmatter(f)
        if meta and 'title' in meta:
            essays.append({
                "title": meta.get('title'),
                "slug": meta.get('slug'),
                "summary": meta.get('description', ''),
                "date": meta.get('date', '2026-08-11')
            })

    # Sort essays by date descending
    essays.sort(key=lambda x: x['date'], reverse=True)

    # 1. Root Element and Attributes
    rss = ET.Element("rss", version="2.0", attrib={
        "xmlns:atom": "http://www.w3.org/2005/Atom"
    })
    
    # 2. Channel Element
    channel = ET.SubElement(rss, "channel")
    
    # Core Feed Metadata
    ET.SubElement(channel, "title").text = "Alan Pruitt — Curriculum-as-Code & AI Architecture"
    ET.SubElement(channel, "link").text = "https://alanpruitt.com"
    ET.SubElement(channel, "description").text = "Essays on Curriculum-as-Code, deterministic AI auditing, and higher education innovation."
    ET.SubElement(channel, "language").text = "en-us"
    
    # Atom Self Link for RSS Validators
    ET.SubElement(channel, "atom:link", attrib={
        "href": "https://alanpruitt.com/rss.xml",
        "rel": "self",
        "type": "application/rss+xml"
    })

    # Set Last Build Date to Current Time
    now_rfc822 = email.utils.formatdate(datetime.now().timestamp(), usegmt=True)
    ET.SubElement(channel, "lastBuildDate").text = now_rfc822

    # 3. Add Items (Essays)
    for essay in essays:
        item = ET.SubElement(channel, "item")
        
        # Link construction
        url = f"https://alanpruitt.com/{essay['slug']}.html"
        
        ET.SubElement(item, "title").text = essay["title"]
        ET.SubElement(item, "link").text = url
        ET.SubElement(item, "guid", attrib={"isPermaLink": "true"}).text = url
        ET.SubElement(item, "description").text = essay["summary"]
        
        # Format "YYYY-MM-DD" date string to RFC-822 format required by RSS standard
        try:
            dt = datetime.strptime(essay["date"], "%Y-%m-%d")
            pub_date_rfc = email.utils.formatdate(dt.timestamp(), usegmt=True)
            ET.SubElement(item, "pubDate").text = pub_date_rfc
        except ValueError:
            ET.SubElement(item, "pubDate").text = essay["date"]

    # 4. Write XML to File
    tree = ET.ElementTree(rss)
    ET.indent(tree, space="  ", level=0)
    
    output_file = os.path.join(output_dir, "rss.xml")
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"✅ Generated RSS feed with {len(essays)} items: {output_file}")

if __name__ == "__main__":
    generate_rss_feed()
