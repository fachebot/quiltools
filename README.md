# quiltools
此项目提供以下功能：
1. 根据用户提供的节点 `peerPrivKey` 批量查询节点的 `peerId`
2. 根据用户提供的节点 `peerId` 批量查询 Quilibrium 节点奖励数量

编译和运行此项目请自行按照以下软件：
* python 3.11.0+
* golang go 1.21.3 +

## 安装依赖
```bash
pip install -r requirements.txt
```

## 批量查询PeerID
1. 在当前目录新增一个 json 文件，命名为 `peerkeys.json`。
2. 复制所有 Quilibrium 节点 `.config/config.yml` 文件中 `p2p.peerPrivKey` 项的内容到 `peerkeys.json`，例如：
    ```json
    [
        "3bced4a1df496......",
        "197d9438ae2c......"
    ]
    ```
3. 最后执行命令 `go run peer_id.go`，将会在控制台输出所有节点的 Peer ID，同时将查询结果保存到 `peers.json` 文件：
    ```bash
    Peer ID: QmUrAcuyxHnAMo31o817SVHWw2AU3A6nMaBCjCkuBiDXm9
    Peer ID: QmeEoDE5XwErsqo841KwaXPf1js5jGaa3NWdP2sbhS2sAx
    Peer ID: QmVx7WUctiM9pzSQkg4APdQoGLHkydk4LdtPTigtixJ83E
    Peer ID: QmeP3zZBydPpGXgmqoK557aEoavkBsgt8XjNQ2rLCbo195
    ```

## 批量查询节点奖励
1. 在当前目录新增一个 json 文件，命名为 `peers.json`。
2. 将所有个 Quilibrium 节点的 PeerID 写入到 `peers.json`，例如：
    ```json
    ["QmYpBNSWaUCbTMRUMyLhjbYogUhqgaVztaQEgrACBAkqcP","QmeTrcbvxCeLvFNoQJ2YM47A67NUioZAoHe4N3ZqTuJBgr"]
    ```
3. 最后执行命令 `python query_rewards.py`，将会在控制台输出所有节点的奖励数量：
    ```bash
    Peer ID: QmWwJ8irT2iVrnK2mywhgJQ6eLxz3xQTexN6UWhtEoA1Qa, 奖励数量: 17888.241215
    Peer ID: QmUrAcuyxHnAMo31o817SVHWw2AU3A6nMaBCjCkuBiDXm9, 奖励数量: 18776.708953
    Peer ID: QmeEoDE5XwErsqo841KwaXPf1js5jGaa3NWdP2sbhS2sAx, 奖励数量: 17888.241215
    Peer ID: QmVx7WUctiM9pzSQkg4APdQoGLHkydk4LdtPTigtixJ83E, 奖励数量: 18827.079867
    Peer ID: QmeP3zZBydPpGXgmqoK557aEoavkBsgt8XjNQ2rLCbo195, 奖励数量: 17794.812874
    用户数量: 44617
    总奖励数量: 361052159.99971926
    我的奖励数量: 211232.86246199996
    ```