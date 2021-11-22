import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime

CLIENT_ID = '23BJB6'
CLIENT_SECRET = '120245e705860af7237ffc2a1b4e19d6'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()

ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
print(yesterday)
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
print(yesterday2)
today = str(datetime.datetime.now().strftime("%Y%m%d"))
print(today)

fit_statsHR = auth2_client.activities_list()
    #auth2_client.intraday_time_series('activities/heart', yesterday2, detail_level='15min')
#intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')
print(fit_statsHR)
time_list = []
val_list = []

'''
for i in fit_statsHR['activities-heart-intraday']['dataset']:
    val_list.append(i['value'])
    time_list.append(i['time'])

heartdf = pd.DataFrame({'Heart Rate':val_list, 'Time': time_list})
heartdf
'''
