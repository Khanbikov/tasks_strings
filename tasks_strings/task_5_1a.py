computers = {
    "pc1": {
        "os": "Windows 10",
        "processor": "ADM Phenom II",
        "ram": "8 gb",
        "motherboard": "MSI87343",
        "HDD": "1Tb",
    },
    "pc2": {
        "os": "Windows 10",
        "processor": "ADM Phenom I",
        "ram": "4 gb",
        "motherboard": "MSI845656",
        "HDD": "512Gb",
    },
    "pc3": {
        "os": "Windows 7",
        "processor": "ADM Phenom II",
        "ram": "4 gb",
        "motherboard": "ASUS-4565",
        "HDD": "1Tb",
    }
}

device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")

print(computers[device][parameter])