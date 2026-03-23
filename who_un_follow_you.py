import json

with open('following.json', 'r') as f:
    following_data = json.load(f)

with open('followers_1.json', 'r') as f:
    followers_data = json.load(f)

following_list = {}
for item in following_data['relationships_following']:
    username = item['title']
    href = item['string_list_data'][0]['href']
    following_list[username] = href

followers_set = set()
for item in followers_data:
    username = item['string_list_data'][0]['value']
    followers_set.add(username)

not_following_back = []
for username, href in following_list.items():
    if username not in followers_set:
        not_following_back.append((username, href))

print(f"Total following: {len(following_list)}")
print(f"Total followers: {len(followers_set)}")
print(f"Not following back: {len(not_following_back)}")

for username, href in not_following_back:
    print(f"{username}: {href}")