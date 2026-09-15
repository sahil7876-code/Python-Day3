corret_pass = "xyz"
not_found=True

while not_found:
    passw = input("ENter Password: ")
    if passw == corret_pass:
        not_found = False

print("MAtched")