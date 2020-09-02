import os
import argparse

try:
    from metasploit.msfrpc import MsfRpcClient
except:
    raise ImportError
    os.exit(-1)
    

MSF_PASSWD = os.environ["MSF_PASSWD"]
try:
    client = MsfRpcClient(MSF_PASSWD)
except:
    raise ConnectionError
    os.exit(-1)




def transform(data, pse):
    # type: (str, PSEStore) -> str
    try:
        client.modules.payload
    # ... here goes all the logic
    return data