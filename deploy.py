from datetime import datetime
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
FlaskJSON(app)
class Boss:
    def __init__(self, name, time):
        self.name = name
        self.time = datetime.datetime.strptime(time, '%H:%M').time()


mondey = [Boss("Kzarka and Nouver","08:00"),
          Boss("Kutum and Karanda","18:00"),
          Boss("Kzarka and Nouver","21:15"),
          Boss("Kutum and Karanda","00:15")
          ]

tuesday = [Boss("Kutum and Karanda","08:00"),
          Boss("Kzarka and Nouver","18:00"),
          Boss("Kutum and Karanda","21:15"),
          Boss("Kzarka and Nouver","00:15")
          ]

wednesday = [Boss("Kzarka and Nouver","08:00"),
          Boss("Kutum and Karanda","18:00"),
          Boss("Kzarka and Nouver","21:15"),
          Boss("Quint and Muraka", "22:00"),
          Boss("Kutum and Karanda","00:15")
          ]

thursday = [Boss("Kutum and Karanda","08:00"),
          Boss("Kzarka and Nouver","18:00"),
          Boss("Kutum and Karanda","21:15"),
          Boss("Kzarka and Nouver","00:15")
          ]

friday = [Boss("Kzarka and Nouver","08:00"),
          Boss("Kutum and Karanda","18:00"),
          Boss("Kzarka and Nouver","21:15"),
          Boss("Kutum and Karanda","00:15")
          ]

saturday = [Boss("Kzarka and Nouver","12:00"),
            Boss("Kutum and Karanda","15:00"),
            Boss("Quint and Muraka", "16:00"),
            Boss("Kzarka and Nouver", "18:00"),
            Boss("Kutum and Karanda","23:15")
          ]

sunday = [Boss("Kutum and Karanda","12:00"),
          Boss("Kzarka and Nouver","15:00"),
          Boss("Kutum and Karanda","18:00"),
          Boss("Kzarka and Nouver","21:15")
          ]

now = datetime.datetime.now()
today = now.strftime("%A").upper()


def bosseOfTheDay():
    if today == "Monday".upper():
        return nextBoss(mondey)

    if today == "Tuesday".upper():
        return nextBoss(tuesday)

    if today == "Wednesday".upper():
        return nextBoss(wednesday)

    if today == "Thursday".upper():
        return nextBoss(thursday)

    if today == "Friday".upper():
        return nextBoss(friday)

    if today == "Saturday".upper():
        return nextBoss(saturday)

    if today == "Sunday".upper():
        return nextBoss(sunday)

def nextBoss(bosses=[Boss]):
    for boss in bosses:
        if boss.time > now.time():
            return boss
            break

@app.route('/')
def nextSpwanBoss():
    boss = bosseOfTheDay()
    return json_response(name=boss.name, spawnTime=boss.time)

