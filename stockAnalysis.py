import requests
import pandas as pd 
from yahoo_fin import stock_info as si 
from pandas_datareader import DataReader
import numpy as np
import time
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

tickers = si.tickers_sp500()
recommendations = []

for ticker in tickers:
    lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
    rhs_url = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
              'modules=upgradeDowngradeHistory,recommendationTrend,' \
              'financialData,earningsHistory,earningsTrend,industryTrend&' \
              'corsDomain=finance.yahoo.com'
              
    url =  lhs_url + ticker + rhs_url
    r = requests.get(url)
    if not r.ok:
        recommendation = 6
    try:
        result = r.json()['quoteSummary']['result'][0]
        recommendation =result['financialData']['recommendationMean']['fmt']
    except:
        recommendation = 6
    
    recommendations.append(recommendation)
    
    print("--------------------------------------------")
    print ("{} has an average recommendation of: ".format(ticker), recommendation)
    #time.sleep(0.5)
   
dataframe = pd.DataFrame(list(zip(tickers, recommendations)), columns =['Company', 'Recommendations']) 

dataframe['Recommendations'] = pd.to_numeric(dataframe['Recommendations'])

dataframeStrongBuy = dataframe[dataframe['Recommendations']<=1.7]

dataframeStrongSell = dataframe[dataframe['Recommendations']>=3.2]

s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() # to make emails encrypted
print("Creating Server")

s.login("sambeynonstock@gmail.com", "uTWow8FA6%q7")
print("Logging in")

msg= "Subject: Check These Stocks\n" + dataframeStrongBuy.to_string()
fromaddr = "sambeynonstock@gmail.com"
toaddr = 'sambeynon@gmail.com'

# Print the email's contents
print('From: ' + fromaddr)
print('To: ' + str(toaddr))
print('Message: ' + msg)

# send the email
s.sendmail(fromaddr, toaddr, msg)
print("Email sent")
# disconnect from the server
s.quit()
print("Server Terminated")
time.sleep(1)
print("Enjoy your hard-earned cash")
