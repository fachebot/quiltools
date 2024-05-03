import re
import json
import requests

def get_main_js():
    res = requests.get("https://quilibrium.com/?/rewards")
    pattern = r"main\.([^.]+)\.js"
    match = re.search(pattern, res.content.decode('utf-8'))
    if match is None:
        return None
    return f"https://quilibrium.com/static/js/main.{match[1]}.js"

def get_rewards():
    js = get_main_js()
    print(f"wget {js}")
    if js is None:
        return []

    res = requests.get(js)
    regex = r'var\s+OR\s*=\s*([^$]+?),\$R\s*=\s*'
    match = re.search(regex, res.content.decode('utf-8'))
    print(f"match: {not match is None}")
    if match is None:
        return []

    data = match.group(1)
    data = re.sub(r',?janPresence:!0|,?marPresence:!0|,?aprPresence:!0|,?febPresence:!0', '', data)
    data = re.sub(r',?janPresence:!1|,?marPresence:!1|,?aprPresence:!1|,?febPresence:!1', '', data)
    code = re.sub(r'(?<={|,)(\w+):([^,}]+)', r'"\1":\2', data)

    return eval(code)

def main():
    rewards = {}
    total_rewards = 0
    data = get_rewards()

    for item in data:
        rewards[item["peerId"]] = item["reward"]
        total_rewards = total_rewards + item["reward"]
    
    peers = []
    with open("peers.json") as fp:
        peers = json.load(fp)

    total = 0
    for peer in peers:
        if peer in rewards:
            total = total + rewards[peer]

    print(f"用户数量: {len(rewards)}\n总奖励数量: {total_rewards}\n我的奖励数量: {total}")

if __name__ == "__main__":
    main()