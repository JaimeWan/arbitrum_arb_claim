
from web3 import Web3, HTTPProvider
import json 

abi={
    "abi":"[{\"inputs\":[{\"internalType\":\"contract IERC20VotesUpgradeable\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address payable\",\"name\":\"_sweepReceiver\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_owner\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_claimPeriodStart\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_claimPeriodEnd\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"delegateTo\",\"type\":\"address\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"CanClaim\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"HasClaimed\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newSweepReceiver\",\"type\":\"address\"}],\"name\":\"SweepReceiverSet\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"Swept\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"Withdrawal\",\"type\":\"event\"},{\"inputs\":[],\"name\":\"claim\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"delegatee\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint8\",\"name\":\"v\",\"type\":\"uint8\"},{\"internalType\":\"bytes32\",\"name\":\"r\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"s\",\"type\":\"bytes32\"}],\"name\":\"claimAndDelegate\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"claimPeriodEnd\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"claimPeriodStart\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"claimableTokens\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address[]\",\"name\":\"_recipients\",\"type\":\"address[]\"},{\"internalType\":\"uint256[]\",\"name\":\"_claimableAmount\",\"type\":\"uint256[]\"}],\"name\":\"setRecipients\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address payable\",\"name\":\"_sweepReceiver\",\"type\":\"address\"}],\"name\":\"setSweepReciever\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"sweep\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"sweepReceiver\",\"outputs\":[{\"internalType\":\"address payable\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"token\",\"outputs\":[{\"internalType\":\"contract IERC20VotesUpgradeable\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"totalClaimable\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"withdraw\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]",
    "address": "0x67a24CE4321aB3aF51c2D0a4801c3E111D88C9d9",
}


datas = [
    {
        "address": "地址1",
        "private_key": "私钥1"
    },
    {
        "address": "地址2",
        "private_key": "私钥2"
    },
]

web3 = Web3(HTTPProvider("https://arb1.arbitrum.io/rpc"))



# 创建一个方法,调用合约abi["abi"]中claimableTokens方法，获取可领取的数量
def getClaimableTokens(address):
    swapContract=web3.eth.contract(
        address=abi["address"], abi=abi["abi"])
    #swap
    arb_contract=swapContract.functions.claimableTokens(address)
    return arb_contract.call()


# 创建一个方法,调用合约abi["abi"]中claim方法,领取奖励
# address:钱包地址
# private_key:钱包私钥
# gasLimit:交易的gasLimit,当gasLimit=500000且fla=True时,会重新获取gasLimit
# flag:是否需要根据arb_contract.estimateGas()重新获取gasLimit(当gasLimit=500000且fla=True时)
def claim(address,private_key,gasLimit=500000,flag=True):
    address = web3.toChecksumAddress(address)
    swapContract=web3.eth.contract(
        address=abi["address"], abi=abi["abi"])
    #swap
    arb_contract=swapContract.functions.claim()
    # 获取交易的nonce
    nonce = web3.eth.getTransactionCount(address)
    # 获取gasPrice
    gasPrice = web3.eth.gasPrice
    # 获取gasLimit
    if gasLimit==500000 or flag:
      try:
       gasLimit = arb_contract.estimateGas()
      except Exception as e: 
         print(address+"执行:还没开始领取奖励")
         return "还没开始领取奖励"
    # 获取交易的数据,gasPrice和nonce都是必须的,否则会报错
    data = arb_contract.buildTransaction(
        {'gas': gasLimit, 'gasPrice': gasPrice, 'nonce': nonce})
    # 签名交易
    signed_txn = web3.eth.account.sign_transaction(
        data, private_key=private_key)
    # 发送交易
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    # 获取交易的hash
    tx_hash = web3.toHex(tx_hash)
    print(address+"执行:提交成功,交易hash:"+tx_hash)
    return tx_hash



tx_hash_list=[]

for i in datas:
 tx_hash = claim(i["address"],i["private_key"])
 tx_hash_list.append({"address":i["address"],"tx_hash":tx_hash})

print(json.dumps(tx_hash_list,indent=4,ensure_ascii=False))

# 将tx_hash_list写入当前文件夹下的result.json文件中
with open("result.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(tx_hash_list, indent=4, ensure_ascii=False))

print("执行完成")



 




