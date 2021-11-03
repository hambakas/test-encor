from ncclient import manager

m = manager.connect(
    host="ios-xe-mgmt.cisco.com",
    port=10000,
    username="deverloper",
    password="C1sco12345",
    hostkey_verify=False
)
#testRev3

print("#Supported Capabilities (YANG model) : ")
for capability in m.server_capabilities:
    print (capability)