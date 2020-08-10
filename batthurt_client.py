from firebase import firebase as fb

print('BattHurt Simple Client \nUse with BattHurt for Android and config deviceID\n')
f=open("deviceID.txt",'rt')
fbClient=fb.FirebaseApplication("https://batthurt-33201.firebaseio.com",None)

model=str(f.read())
data=fbClient.get(model,'')
charging=True if fbClient.get("CurrentIsCharging_"+model[15:],'')
if(data is not None):
    print("On Device: "+model[15:]+", Battery: "+str(data)+"%")
    print("Charging\n / \n \ \n /") if(charging) else print("Discharging")
else:
    print("Can't Read! Object is not ready. check your connection and make sure your deviceID file is properly conf'ed")
