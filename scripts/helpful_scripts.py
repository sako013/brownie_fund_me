from brownie import accounts, network, config, MockV3Aggregator, web3
from web3 import Web3

FORKED_LOACAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIROMENT = ["development", "ganache_mumbai"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENT
        or network.show_active() in FORKED_LOACAL_ENVIRONMENT
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mock PriceFeed...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(8, web3.toWei(2000, "ether"), {"from": get_account()})
        print("Mock Deplyed!")
