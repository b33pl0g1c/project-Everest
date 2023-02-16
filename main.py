import time
from winotify import Notification, audio
import psutil
battery = psutil.sensors_battery()
def getBatteryPercent(battery):
    percent = int(str(battery.percent))
    return percent

def getStatusPlugged(battery):
    plugged = battery.power_plugged
    return plugged

def secs2hours(secs):
     mm, ss = divmod(secs, 60)
     hh, mm = divmod(mm, 60)
     return "%d:%02d:%02d" % (hh, mm, ss)

def getUser():
    print(psutil.users())

currentBattery=getBatteryPercent(battery)
# currentBattery=20
pluggedStatus=getStatusPlugged(battery)
timeremaining=secs2hours(battery.secsleft)


print(timeremaining)
# while(1):
#     if(currentBattery>=80):
#         toast=Notification(app_id="Notifier",title="TIME TO UNPLUG THE CHARGER CHAD!",msg=f"Hello King,Please unplug your charger, your current percentage is: {currentBattery} and battery percent left is:{timeremaining}")
#         toast.show()
#         break
#     elif(currentBattery<=20):
#          toast=Notification(app_id="Notifier",title="TIME TO PLUG THE CHARGER CHAD!",msg=f"Hello King,Please plug your charger, your current percentage is: {currentBattery} and battery percent left is:{timeremaining}")
#          toast.show()
#          break
#     else:












# percent = str(battery.percent)
# plugged = battery.power_plugged
# if(plugged):
#     toast=Notification(app_id="Battery Notifier",
#                     title="Hey its time!",
#                     msg=f"Please unplug your charger, your current percentage is: {percent}")
#     toast.show()

# plugged = "Plugged In" if plugged else "Not Plugged In"
# print(f'Battery : {percent}% Device Is {plugged}')

# toast=Notification(app_id="Battery Notifier",
#                     title="Notifier",
#                     msg="Please unplug your charger")
# toast.show()



