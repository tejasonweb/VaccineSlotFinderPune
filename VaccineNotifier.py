import requests
import datetime
import time
import json

def getVaccineSlots(date,pincode):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+str(pincode)+"&date="+date
    headers = {'Authority':'cdn-api.co-vin.in',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    vreq = requests.get(url,headers=headers)
    if vreq.status_code == 200:
        centers = vreq.json()["centers"]
        if len(centers)>0:
            print(str(len(centers)) + " centers are available.")
            for c in range(len(centers)):
                #check if there if capacity > 0 for the center
                sessions = centers[c]["sessions"]
                if(sessions[0]["available_capacity"] > 0):
                    print("=============================================================")
                    print("Name : " + centers[c]["name"])
                    print("Address : " + centers[c]["address"])
                    print("From : " + centers[c]["from"])
                    print("To : "+ centers[c]["to"])
                    print("Fee Type : " + centers[c]["fee_type"])
                    print("Number of Sessions : " + str(len(sessions)))
                    print("Date : " + sessions[0]["date"])
                    print("Available Capacity : " + str(sessions[0]["available_capacity"]))
                    print("Min Age Limit : " + str(sessions[0]["min_age_limit"]))
                    print("Vaccine : " + sessions[0]["vaccine"])
                    slots = sessions[0]["slots"]
                    print(str(len(slots)) +" slots are available")
                    for i in range(len(slots)):
                        print(slots[i])
                else:
                    print("No capacity is available at center : "+centers[c]["name"])
                print("=============================================================")
        else:
            print("No centers available for the pin code : "+str(pincode)+ " and date : "+str(date))
    else:
        print("error : "+str(vreq.status_code) + ". Try again later.")

pincode = 411001
date1 = datetime.datetime.now().strftime("%d-%m-%Y")

for i in range(998):
    print("Getting Vaccine slots for Pin : " + str(pincode) + " and Date : " + date1)
    getVaccineSlots(date1,pincode)
    pincode = pincode + 1
    
