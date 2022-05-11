from brownie import FundMe, accounts
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entarnce_fee = fund_me.getEntranceFee()
    print(f"The current entrance fee is{entarnce_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entarnce_fee})
    print(fund_me.address)


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
