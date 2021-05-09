import requests
import datetime
import time
import json


#pincode = 411001
#date1 = datetime.datetime.now().strftime("%d-%m-%Y")
date2 = datetime.datetime.strptime("05-05-2021","%d-%m-%Y")
# open pincode file
pincodefile = open("PunePinCodeList.txt")

def showwait():
    j = 1
    for i in range(15):
        #sys.stdout.write(". ")
        #sys.stdout.flush()	
        print("|\t"+str(i+j),end="\r")
        j+=1
        time.sleep(1)
        print("/\t"+str(i+j),end="\r")
        j+=1
        time.sleep(1)
        print("-\t"+str(i+j),end="\r")
        j+=1
        time.sleep(1)
        print("\\\t"+str(i+j),end="\r")
        time.sleep(1)


def getVaccineSlots(date,pincode):
    print("===================================================================================================")
    print("Pin : " + str(pincode) + " and Date : "+date)
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+str(pincode)+"&date="+date
    headers = {'Authority':'cdn-api.co-vin.in',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    vreq = requests.get(url,headers=headers)
    if vreq.status_code == 200:
        centers = vreq.json()["centers"]
        if len(centers)>0:
            print("\t"+str(len(centers)) + " center(s) are available.")
            for c in range(len(centers)):
                #check if there if capacity > 0 for the center
                print("\t===========================================================================================")
                print("\tName : " + centers[c]["name"])
                sessions = centers[c]["sessions"]
                if(sessions[0]["available_capacity"] > 0):
                    print("\tAddress \t\t: " + centers[c]["address"])
                    print("\tFrom \t\t\t: " + centers[c]["from"])
                    print("\tTo \t\t\t: "+ centers[c]["to"])
                    print("\tFee Type \t\t: " + centers[c]["fee_type"])
                    print("\tNumber of Sessions \t: " + str(len(sessions)))
                    print("\tDate \t\t\t: " + sessions[0]["date"])
                    print("\tAvailable Capacity \t: " + str(sessions[0]["available_capacity"]))
                    print("\tMin Age Limit \t\t: " + str(sessions[0]["min_age_limit"]))
                    print("\tVaccine \t\t: " + sessions[0]["vaccine"])
                    slots = sessions[0]["slots"]
                    print("\t"+str(len(slots)) +" slots are available")
                    for i in range(len(slots)):
                        print("\t\t"+slots[i])
                else:
                    print("\tNo capacity is available at center : "+centers[c]["name"] + " on date : "+sessions[0]["date"])
        else:
            print("\tNo centers available for the pin code : "+str(pincode) +" on date : "+date)
    else:
        print("error : "+str(vreq.status_code) + ".")
        if(vreq.status_code==403):
            print("Error 403 could be due to too many requests. Will try again in 60 seconds.")
            showwait()
            getVaccineSlots(date,pincode)

for pincode in pincodefile:
    for i in range(10):
        getVaccineSlots((datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%d-%m-%Y"),pincode.strip())
    print("")
    #time.sleep(0)
print("===================================================================================================")    
