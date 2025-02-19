import_file = "allow_list.txt"

with open(import_file, "r") as file:
    # use read to the imported file and store it in variable named ip address
     ip_addresses = file.read()

ip_addresses = ip_addresses.split()


for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)
            # use remove method to remove elements from the ip address

ip_addresses = "\n".join(ip_addresses)
# convert ip addresses back to a string so that it can be written into the text file

# build with statement to rewrite orginal file
with open (import_file, "w") as file:
    #rewite the file, replacing its contetns with ip addresses
    file.write(ip_addresses)