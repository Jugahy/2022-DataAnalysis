import json

with open("/content/busan_gu.json") as f:
  json_data = json.load(f)
print(json.dumps(json_data))