import requests
import json

def notify(msg):
    #Telegam Bot Url
    #url='https://api.telegram.org/bot879982304:AAHG7ZRyEMWoQB-ToaiJBv_gMvkW-ekJcSg/sendMessage?chat_id=582942300&text='+msg
    #TelegramChannel chatId -1001181667975
    url='https://api.telegram.org/bot879982304:AAHG7ZRyEMWoQB-ToaiJBv_gMvkW-ekJcSg/sendMessage?chat_id=-1001181667975&text='+msg
    requests.get(url)
    print("notified")

raw = requests.get('https://api.covid19india.org/data.json')
data = raw.json()
daily_report = data['cases_time_series'][-1]
msg='*****Corona Update*****\n\n'
for i in daily_report:
	msg = msg + i + ' : ' + daily_report[i] + '\n'

lastupdatedtime = data['key_values'][0]['lastupdatedtime']
msg = msg +'updatetime : ' + lastupdatedtime 


msg=msg +'\n\n'
msg=msg +'--------------Statewise--------------\n' 
msg=msg +'confirm - death - recover - active - updatetime - state \n\n'
statewise = data['statewise']
for i in statewise:
	active = i['active']
	confirmed = i['confirmed']
	deaths = i['deaths']
	recovered = i['recovered']
	state = i['state']
	lastupdatedtime = i['lastupdatedtime']
	msg = msg + confirmed + ' ' + deaths + ' ' + recovered + ' ' + active + '  ' + lastupdatedtime + ' ' + state[0:14] + '\n'

msg=msg +'\n'
msg=msg +'--------------AP Districtwise--------------\n\n' 
raw = requests.get('https://api.covid19india.org/state_district_wise.json')
data = raw.json()

districtData = data['Andhra Pradesh']['districtData']
for district in districtData:
	msg =msg + str(districtData[district]['confirmed']) + ' ' + district +'\n'

print(msg)
notify(msg)	
		
