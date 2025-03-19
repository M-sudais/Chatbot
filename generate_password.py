def password():
    import random
    name = str(input("Enter your fullname: "))
    numbers = "0123456789"
    symbols = "!@#$%^&*()"
    all_together = name + numbers + symbols
    length = 8
    password = "".join(random.sample(all_together, length))
    print(f"Take Note of this Password: {password}")
    