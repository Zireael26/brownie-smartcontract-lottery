# Expecting about 0.01623882769 ETH at current price or 16238827600000000 wei
from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    network_specific_config = config["networks"][network.show_active()]
    lottery = Lottery.deploy(
        network_specific_config["eth_usd_price_feed"],
        network_specific_config["vrf_coordinator_address"],
        network_specific_config["vrf_link_token"],
        network_specific_config["vrf_fee"],
        network_specific_config["vrf_contract_key_hash"],
        {"from": account},
    )
    retrieved_price = lottery.getEntranceFee()
    assert retrieved_price > Web3.toWei(0.016, "ether")
    assert retrieved_price < Web3.toWei(0.018, "ether")
