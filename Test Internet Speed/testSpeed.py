# Testing Speed 
import speedtest 
from convertDataSize import calcData

speed = speedtest.Speedtest()

print("Performing Download test ..!!")
print("Performing Upload test ..!!")
download = speed.download()
upload = speed.upload() 

download = calcData(download)
upload = calcData(upload)

speed.get_servers()

best =speed.get_best_server()

ping = speed.results.ping

print(f"Found: {best['host']} located in {best['country']}")
print("Your ⏬ Download speed is : ", download)
print("Your ⏫ Upload speed is : ", upload)
print('Your Ping is : ', ping)




