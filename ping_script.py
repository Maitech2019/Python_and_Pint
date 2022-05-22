import os
hostname = input("Please enter ip address: ")

response = os.system("ping -c 1 " + hostname) #make sure "space after 1 " , -c 1 means run ping 1 time and stop
if response == 0:                             #0 is True =return of os.system means receive 4 replies, 1 is False
    print( hostname, "is up")
else:
    print("something went wrong")




#ip = input("Enter ip address: ")
#response = os.system("ping ", + ip)
#print(response)

