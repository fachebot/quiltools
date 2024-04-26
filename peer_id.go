package main

import (
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	"os"

	"github.com/libp2p/go-libp2p/core/crypto"
	"github.com/libp2p/go-libp2p/core/peer"
	"github.com/pkg/errors"
)

func getPeerID(peerPrivKey string) string {
	key, err := hex.DecodeString(peerPrivKey)
	if err != nil {
		panic(errors.Wrap(err, "error unmarshaling peerkey"))
	}

	privKey, err := crypto.UnmarshalEd448PrivateKey(key)
	if err != nil {
		panic(errors.Wrap(err, "error unmarshaling peerkey"))
	}

	pub := privKey.GetPublic()
	id, err := peer.IDFromPublicKey(pub)
	if err != nil {
		panic(errors.Wrap(err, "error getting peer id"))
	}

	return id.String()
}

func main() {
	file, err := os.Open("peerkeys.json")
	if err != nil {
		panic(err)
	}

	data, err := io.ReadAll(file)
	if err != nil {
		panic(err)
	}

	var keys []string
	err = json.Unmarshal(data, &keys)
	if err != nil {
		panic(err)
	}

	peers := make([]string, 0)
	for _, key := range keys {
		id := getPeerID(key)
		peers = append(peers, id)
		fmt.Println("Peer ID: " + id)
	}

	data, err = json.Marshal(peers)
	if err != nil {
		panic(err)
	}

	err = os.WriteFile("peers.json", data, 0644)
	if err != nil {
		panic(err)
	}
}
