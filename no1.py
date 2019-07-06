import googlemaps
from datetime import datetime
from flask import Flask, render_template, request
import requests

gmaps = googlemaps.Client(key='AIzaSyCn2LdtM5N7wyYtt9uBE7c0lUiMwl5SQdA')

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)
prev=[]
wpTime=0
timeout=30
app = Flask(__name__)

@app.route('/')
def location():
    return render_template('no2loc.html')
   
@app.route('/fetchdatafromhtml',methods=['POST','GET'])
def fetchdatafromhtml():
    start=request.form['start']
    end=request.form['end']

# Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(start,
                                     end,
                                     mode="transit",
                                     departure_time=now)
    print(directions_result)
    f = open( 'file.json', 'w' )
    f.write(repr(directions_result))
    f.close()

    return render_template("response.html")

if __name__ == '__main__':
   app.run(debug = True)