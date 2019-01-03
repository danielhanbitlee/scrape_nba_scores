import requests, pytz
from apscheduler.schedulers.twisted import TwistedScheduler
from twisted.internet import reactor

def send_request():
    requests.post("https://murmuring-reaches-84629.herokuapp.com/schedule.json", data = {
        'project': 'default',
        'spider': 'nba_scores',
        'city': 'los_angeles'
    })

if __name__ == '__main__':
    scheduler = TwistedScheduler(timezone = pytz.utc)
    scheduler.add_job(send_request, 'cron', day_of_week = 'mon-sun', hour = '12', minute = '0')
    scheduler.start()
    reactor.run()
