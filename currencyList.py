
import json
import urllib
import urllib2
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.Utils import COMMASPACE, formatdate 
#import calendar
import sys


defaultCurrencyFromList=["USD","GBP"]
defaultCurrencyToList=["INR"]
fromEmail="noreply@github.com"
bccEmail=""
subject="Currency Exchange Rate Notification"



def makeServiceCall(from_curr,currency):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    opener.addheaders = [('Accept-Charset', 'utf-8')]
    url = "http://markets.ft.com/RESEARCH/Remote/UK/Markets/CurrencyConverter"
    params = {'nQuantity':1, 'sCurrencyFrom':from_curr, 'sCurrencyTo': currency}
    data = urllib.urlencode(params)
    req = urllib2.Request(url, data)
    response = json.loads(urllib2.urlopen(req).read())    
    return response


def send_email(fromAddr, toAddr, bccAddr, subject, body):        
    toAddrsList = toAddr.split(",")
    bccAddrsList = bccAddr.split(",")    
    msg = MIMEMultipart('alternative')   
    
    msgPart = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = fromAddr
    msg['To'] = toAddr
    msg['BCC'] = bccAddr
    msg['Date'] = formatdate(localtime=True)  
    msg.attach(msgPart)  
    allAddrsList = toAddrsList + bccAddrsList      
    s = smtplib.SMTP('localhost')
    s.sendmail(fromAddr, allAddrsList, msg.as_string())
    s.quit()

def process(toEmail, currencyFromList, currencyToList):
	global fromEmail,bccEmail,subject	
	
	exchangeTextFrom = "Exchange rate:"
	exchangeTextTo = "</div>"
	mailMessage = ""	
	for fromCurr in currencyFromList:
	   finalFromCurr = fromCurr
	   for curr in currencyToList:		
		response = makeServiceCall(fromCurr,curr)
		respHtml = response["html"]
		exchangeFrom = respHtml.find(exchangeTextFrom)
		if exchangeFrom != -1:
			finalExchangeFrom = exchangeFrom + len(exchangeTextFrom)
			exchangeTo = respHtml.find(exchangeTextTo,exchangeFrom)
			if exchangeTo != -1:
				exchangeRate = float(respHtml[finalExchangeFrom:exchangeTo])
				mailMessage += fromCurr+" to "+curr+" : "+str(exchangeRate)+" <br />\n"				

	print mailMessage
	if mailMessage != "":
		send_email(fromEmail, toEmail, bccEmail, subject, mailMessage)
		
argLen = len(sys.argv)

if argLen == 2:
    toEmail = sys.argv[1]
    currencyFrom = defaultCurrencyFromList
    currencyTo = defaultCurrencyToList    
elif argLen == 3:
    toEmail = sys.argv[1]
    currencyFrom = sys.argv[2].split(",")
    currencyTo = defaultCurrencyToList    
elif argLen == 4:
    toEmail = sys.argv[1]
    currencyFrom = sys.argv[2].split(",")
    currencyTo = sys.argv[3].split(",")        
else:
    print "Incorrect number of arguments. Correct usage: python ",sys.argv[0], " toEmail currencyFrom(csv) currencyTo(csv)"
    exit(0)

process(toEmail, currencyFrom, currencyTo)