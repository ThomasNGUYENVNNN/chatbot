from os.path import dirname, join
from os import listdir, mkdir
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
import pandas as pd

from engine.hoaian import HoaiAn

LOG_FOLDER = join(dirname(dirname(__file__)), "logs")

def index(request):
    return render(request, 'index.html')


def log(text):
    today = datetime.now().strftime('%Y%m%d')
    LOG_FOLDER = join(dirname(dirname(__file__)), "logs")
    log_file = join(LOG_FOLDER, "{}.txt".format(today))
    with open(log_file, "a") as f:
        f.write(text + "\n")

@csrf_exempt
def analyze(request):
    result = {}
    log_file = join(LOG_FOLDER, "20190416.txt")
    lines = open(log_file).read().splitlines()
    data = []
    for line in lines:
        ip, date, time, agent, *text = line.split()
        text = " ".join(text)
        agent = agent[:-1]
        data.append({
            "ip": ip,
            "date": date,
            "time": time,
            "agent": agent,
            "text": text
        })
    df = pd.DataFrame(data)
    users = df[df["agent"] == "USER"]
    result["count_user"] = len(users["ip"].unique())
    result["count_message"] = len(users)
    return JsonResponse(result)


@csrf_exempt
def chatbot(request):
    result = {}
    try:
        data = json.loads(request.body.decode("utf-8"))
        text = data["text"]
        user = data["user"]
        ip = request.META["REMOTE_ADDR"]
        time = datetime.now().strftime('%Y%m%d %H:%M:%S')
        log_text = "{} {} {} {}".format(ip, time, "USER:", text)
        log(log_text)
        response_message = HoaiAn.reply(text, user)
        log_text = "{} {} {} {}".format(ip, time, "BOT:", response_message)
        log(log_text)
        result["output"] = response_message
    except Exception as e:
        print(e)
        result = {"error": "Bad request!"}
    return JsonResponse(result)


if __name__ == '__main__':
    log("hihi")
