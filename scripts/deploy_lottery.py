from brownie import Lottery, config, network
from scripts.helpful_scripts import get_account, get_contract


def deploy_lottery():
    account = get_account(id="abhishek-account")
    network_specific_config = config["networks"][network.show_active()]
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        network_specific_config["vrf_fee"],
        network_specific_config["vrf_contract_key_hash"],
        {"from": account},
        publish_source=network_specific_config.get("verify", False),
    )
    print("Deployed Lottery")


def main():
    deploy_lottery()
