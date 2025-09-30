emailAddress = input()

emailAddressFixed = ""

for fragment in emailAddress.split(" "):
    emailAddressFixed += fragment

print(emailAddressFixed)

