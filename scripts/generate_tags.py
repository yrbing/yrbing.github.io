import os
import yaml
import json
from collections import Counter

content_dir = 'content/posts' # Where to get all tags
output_file = 'data/wordcloud.json'

tags = []
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                try:
                    # Parse YAML Front Matter
                    content = f.read().split('---')
                    if len(content) > 1:
                        meta = yaml.safe_load(content[1])
                        if meta and 'tags' in meta:
                            tags.extend(meta['tags'])
                except Exception as e:
                    print(f"Error parsing {file}: {e}")

# Format to [{"name": "xxx", "value": 10}, ...] as required by D3
count = Counter(tags)
data = [{"name": k, "value": v} for k, v in count.items()]

os.makedirs('data', exist_ok=True)
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
