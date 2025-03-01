from neo3.api.rpc import NeoRpcClient

# Initialize Neo RPC client
rpc_url = "http://127.0.0.1:50012"
client = NeoRpcClient(rpc_url)

# Deploy the smart contract
contract_path = "did_smart_contract.py"
result = client.compile_and_deploy(contract_path)

print(f"Deployment result: {result}")
