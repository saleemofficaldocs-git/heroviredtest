instance = {
    "id": "i-123456",
    "state": "running",
    "public_ip": "53.10.11.22",
    "private_id": "10.1.1.1",
    "vpc": {
        "cidr": "10.0.0.0/16",
        "nat": "yes",
        "pub_subnet": ["10.0.0.1/24", "10.0.1.0/24"]
    }
}

#print(instance["id"])
#print("This is get",instance.get("id"))

#instance["region"] = "ap-south-1"
#instance["state"] = "stopped"
#instance.update({'state': 'stopped'})
#instance.remove("public_ip")
print(instance)

print(instance.get("vpc").get("pub_subnet")[0])



