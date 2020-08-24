phonebook = {
    "Bob" : 1574574527,
    "Billy" : 2563575439,
    "Guru" : 0000000000,
    "Sowmya" : 0000000000
}
phonenumberresponse = input("Type Guru's Phone Number:")
print(phonenumberresponse)
phonebook["Guru"] = phonenumberresponse
print("Guru's Phone number has been updated")
print(phonebook)
phonenumberresponse = input("Type Sowmya's Phone Number:")
print(phonenumberresponse)
phonebook["Sowmya"] = phonenumberresponse
print("Sowmya's Phone number has been updated")
print(phonebook)
