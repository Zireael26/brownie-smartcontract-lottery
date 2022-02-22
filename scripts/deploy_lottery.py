from brownie import Lottery, config, network
from scripts.helpful_scripts import get_account, get_contract, fund_with_link
import time


def deploy_lottery():
    # account = get_account(id="abhishek-account")
    account = get_account()
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


def start_lottery():
    # account = get_account(id="abhishek-account")
    account = get_account()
    # network_specific_config = config["networks"][network.show_active()]
    lottery = Lottery[-1]
    start_transaction = lottery.startLottery({"from": account})
    start_transaction.wait(1)
    print("Lottery started!")


def enter_lottery():
    account = get_account()
    lottery = Lottery[-1]
    value = lottery.getEntranceFee() + 1000000
    enter_lottery_transsaction = lottery.enter({"from": account, "value": value})
    enter_lottery_transsaction.wait(1)
    print("You entered the lottery!")


def end_lottery():
    account = get_account()
    lottery = Lottery[-1]
    # fund the contract with Chainlink Test LINK (because it gets random from chainlink VRF coordinator)
    # Then End the lottery
    fund_with_link(lottery.address)
    end_lottery_transaction = lottery.endLottery({"from": account})
    end_lottery_transaction.wait(1)
    time.sleep(60)
    print(f"{lottery.recentWinner()} won the lottery!")


def main():
    deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()
