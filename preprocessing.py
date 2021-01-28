import json
with open('static/files/user_timeline_MarlouCk_Harp.json', 'r') as f:
    contents = f.read().split('\n')
    json_content = []
    for content in contents:
        if len(content) == 0:
            continue
        print(json.loads(content, encoding='utf-8'))
        json_content.append(json.loads(content))

with open('static/files/tweets.json', 'w') as f:
    f.write(json.dumps(json_content, indent=4))