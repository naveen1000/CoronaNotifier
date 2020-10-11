import requests
import json
def notify(msg):
    #TelegramChannel chatId -1001181667975   
    #MyChatId 582942300
    url='https://api.telegram.org/bot1193312817:AAGTRlOs3YZHFeDSO_33YTwwewrEaMbLizE/sendMessage?chat_id=582942300&parse_mode=Markdown&text='+msg
    requests.get(url)
    print("notified")

raw = requests.get('https://api.covid19india.org/data.json')
data = raw.json()
daily_report = data['cases_time_series'][-1]
msg='--------------*****Corona Update*****--------------\n'


statewise = data['statewise']
for i in statewise:
    state = i['state']
    if state == "Andhra Pradesh":
        active = i['active']
        confirmed = i['confirmed']
        deaths = i['deaths']
        recovered = i['recovered']
        state = i['state']
        lastupdatedtime = i['lastupdatedtime']
        deltaconfirmed = i['deltaconfirmed']
        deltadeaths = i['deltadeaths']
        deltarecovered = i['deltarecovered']
        msg= msg + "***Andhra Pradesh***"+"\n"
        msg = msg + "Today Confirmed:" + deltaconfirmed + "\n"
        msg = msg + "Today Dead:" + deltadeaths + "\n"
        msg = msg + "Today Recovered:" + deltarecovered + "\n"
        msg= msg + "-------------------------\n"
        msg= msg + "Active:" + active +"\n"
        msg= msg + "Confirmed:" + confirmed +"\n"
        msg= msg + "Deaths:" + deaths +"\n"
        msg= msg + "Recovered:" + recovered +"\n"
        msg= msg + "UpdatedOn:" + lastupdatedtime +"\n\n"
        break
	
msg = msg +'--------------***AP District Confirmed ***--------------\n' 
msg = msg +'Today  Total    State \n' 
raw = requests.get('https://api.covid19india.org/state_district_wise.json')
data = raw.json()

districtData = data['Andhra Pradesh']['districtData']
for district in districtData:
	msg =msg + str(districtData[district]['delta']['confirmed']).center(3) + str(districtData[district]['confirmed']).center(6) + ' ' + district +'\n'

msg=msg +'\n\n'
msg=msg +'--------------***Yestrday Report***--------------\n\n' 	

for i in daily_report:
		msg = msg + i.capitalize().replace('deceased',"dead").replace('Daily',"Yesterday") + ' : ' + daily_report[i] + '\n'	
print(msg)
notify(msg)	
