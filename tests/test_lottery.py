# Expecting about 0.01623882769 ETH at current price or 16238827600000000 wei
from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    retrieved_price = lottery.getEntranceFee()
    assert retrieved_price > Web3.toWei(0.016, "ether")
    assert retrieved_price < Web3.toWei(0.018, "ether")
