from boa3.builtin import public
from boa3.builtin.contract import NeoToken
from boa3.builtin.type import UInt160

# Storage key prefix for DIDs
DID_PREFIX = "did:neo:"

@public
def create_identity(user: UInt160, name: str, public_key: str) -> str:
    
    did = DID_PREFIX + str(user)
    if not storage.get(did):
        storage.put(did, f"{name}|{public_key}")
        return f"Identity {did} created successfully."
    return "Identity already exists."

@public
def get_identity(user: UInt160) -> str:
  
    did = DID_PREFIX + str(user)
    identity = storage.get(did)
    return identity if identity else "Identity not found."

@public
def authenticate(user: UInt160, public_key: str) -> bool:
    
    did = DID_PREFIX + str(user)
    identity = storage.get(did)
    if identity:
        _, stored_key = identity.split("|")
        return stored_key == public_key
    return False
