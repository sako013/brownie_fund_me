from brownie import FundMe, MockV3Aggregator, network, config, web3
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIROMENT,
)


# This is how we add any EVM chain like avax,matic,fantom
#  brownie networks add Ethereum ganache_mumbai host=http://127.0.0.1:8545 chainid=1337


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"Contract Deployed to{fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
