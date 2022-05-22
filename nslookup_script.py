#create a Python script that you can run on the command line.
# When run, the python script should prompt for text input and ask what IP you want to lookup.
# the user should input an IP, and the script should do a reverse DNS query and return an FQDN.  
# If the reverse query fails, the script should return the original IP and apologize.

import os
ip = input("Enter ip address to check FQDN: ")

response = os.system("nslookup " + ip ) #make sure to have 'space' after nslookup 
print(response)                         #os.system run ping in backgroud and return 0 if successful
if response == 0:                       #0 is True =return of os.system means receive 4 replies, 1 is False
    print( "!Successfully reverse DNS query and return an FQDN!")
else:
    print("!Something went wrong for", ip, "We apologize!")

