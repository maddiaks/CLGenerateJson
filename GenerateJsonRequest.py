import json

fh = open("MalwareFiles.txt", 'r')

contents = fh.read()
contents = contents.split("\n")

# json_request = json.

# {
#     "ip_address": "",
#     "domainname": "",
#     "reverse_lookup": "",
#     "description": ""
# }

lst_malware_sites = []
for item in contents:
    d = {}
    d['ip_address'] = "0.0.0.0"
    d['domainname'] = item
    d['reverse_lookup'] = ""
    d['description'] = ''

    lst_malware_sites.append(d)

print(lst_malware_sites)
print(json.dumps(lst_malware_sites))