import re
import json
import base64

filepath = r'C:\Users\eedua\Downloads\medical-spa-landing-30.aura.build\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def remove_duplicate_gallery(text):
    # Split by '<!-- Before & After Gallery -->'
    parts = text.split('<!-- Before & After Gallery -->')
    if len(parts) > 2:
        # There's more than one gallery
        # Keep the first part and the first gallery
        result = parts[0] + '<!-- Before & After Gallery -->' + parts[1]
        
        # Now, parts[2] onwards represent the duplicate galleries.
        # However, they might end at '<!-- Booking / Contato -->'
        # Let's find the first '<!-- Booking / Contato -->' in the remainder 
        # and keep only what's AFTER it.
        remainder = '<!-- Before & After Gallery -->'.join(parts[2:])
        
        # We want to throw away everything until '<!-- Booking / Contato -->'
        idx = remainder.find('<!-- Booking / Contato -->')
        if idx != -1:
            result += remainder[idx:]
        else:
            # Fallback, just append
            result += remainder
        return result
    return text

# 1. Fix the raw HTML
content = remove_duplicate_gallery(content)

# 2. Fix the Base64 JSON payload
match = re.search(r'var D = (\{.*?\});\n', content)
if match:
    D = json.loads(match.group(1))
    for entry in D.get('entries', []):
        if 'b' in entry and 't' in entry and entry['t'] == 'application/json':
            b64data = entry['b']
            try:
                data_str = base64.b64decode(b64data).decode('utf-8')
                if 'medical-spa-landing-30' in data_str or '<!DOCTYPE html>' in data_str:
                    
                    # Some json formatting uses escaped strings
                    # We might need to split by the escaped version
                    escaped_marker = '<!-- Before & After Gallery -->'
                    
                    if data_str.count(escaped_marker) > 1:
                        new_data_str = remove_duplicate_gallery(data_str)
                        new_b64data = base64.b64encode(new_data_str.encode('utf-8')).decode('utf-8')
                        entry['b'] = new_b64data
            except Exception as e:
                pass
    
    new_D_str = json.dumps(D, separators=(', ', ': '))
    content = content[:match.start()] + 'var D = ' + new_D_str + ';\n' + content[match.end():]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Duplicate gallery removed successfully!")
