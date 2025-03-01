import { rpc, sc } from "@cityofzion/neon-js";

const NEO_RPC_URL = "http://127.0.0.1:50012";
const CONTRACT_HASH = "your_contract_hash_here";

async function createIdentity(user, name, publicKey) {
    const script = sc.createScript({
        scriptHash: CONTRACT_HASH,
        operation: "create_identity",
        args: [user, name, publicKey]
    });

    const client = new rpc.RPCClient(NEO_RPC_URL);
    const response = await client.invokeFunction(script);
    console.log(response);
}
