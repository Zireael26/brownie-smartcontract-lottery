# Slotto - The decentralised lottery system

Slotto is a decentralised, smart-contracts based lottery system built using Solidity and Brownie (web3py based framework).
1. Users can enter the lottery with ETH based on a USD fee.
2. An admin will choose when the lottery is over.
3. Lottery will select a random winner.

## To run it on your local machine
```sh
git clone https://github.com/Zireael26/brownie-smartcontract-lottery.git
```
```sh
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install eth-brownie
```
```sh
pip3 install -r requirements.txt
```
```sh
brownie compile
```
```sh
brownie run scripts/...py
```