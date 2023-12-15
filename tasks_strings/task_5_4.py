model = {"TE100-S5":
            {"product Title": "5-Port 10/100Mbps Fast Ethernet Switch",
             "10/100Mbps": "5x",
             "Foreading Capacity": "1Gbps",
             "MAC adress entries": "1K",
             "Enclozure Material": "Plactic"},
         "TE-100-S8":
               {"product Title": "9-Port 10/100Mbps Fast Ethernet Switch",
                "10/100Mbps": "8x",
                "Foreading Capacity": "1.6Gbps",
                "MAC adress entries": "2K",
                "Enclozure Material": "Plactic"},
            }

for switch in model.keys():
    if model[switch]['10/100Mbps'] == "5x" and \
            model[switch]['MAC adress entries'] == "1K":
        print(model[switch])