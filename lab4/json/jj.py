import json

with open("j.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 78)

print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<5}") 
print('-' * 50 + " " + '-' * 20 + "  " + '-' * 6 + "  " + '-' * 6)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "N/A") 
    description = attributes.get("descr", "")  
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "N/A")
    print(f"{dn:<50} {description:<20} {speed:<9} {mtu:<5}")
