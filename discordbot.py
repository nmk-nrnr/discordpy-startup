from discord.ext import commands
import os
import traceback
import time
import requests
import json
import copy
from datetime import datetime, timedelta, timezone


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

Hololive = {
   "UCa5JOPRFXMbYz4pBUxAuBaA": [
        "まこふるちゃんねる",
        "https://yt3.ggpht.com/a/AATXAJzl0Sz9ii1SVDKEcxfGJrOFPola0PD-1-PUBHVOgw=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCeVr_dAdntbgOZvVGAJi4Fw": [
        "水無月れる",
        "https://yt3.ggpht.com/a/AATXAJxMIJI8kEKKpI3UbK2IxzlIjKWMlznCT6taE0Rt=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCCwTAihRxyTTjXipFXZk1wQ": [
        "猫こまる",
        "https://yt3.ggpht.com/a/AATXAJxsVf5MDd3LEwijuxjLuRiIGZBdV6RgNlQU1svZ=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC4CGFFW708jB2lOz4R2Ymag": [
        "八乙女八弥",
        "https://yt3.ggpht.com/a/AATXAJz6GLR_QEMfq5DCebxV0qSWCYXV-uYQWaKLt4TY=s100-c-k-c0xffffffff-no-rj-mo"
    ],    
    "UCLeQ-pKNn3wrw4zzhrmFJPw": [
        "七瀬くりむ",
        "https://yt3.ggpht.com/a/AATXAJz5uuWojAC1Wn6ZTG3nQJ5E6k6WzVvtvmC6pmd4=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC-y6hEy54mJ2oyg3RABrcGw": [
        "櫻庭おと",
        "https://yt3.ggpht.com/a/AATXAJyhS0l_ujAeaLSvJQlkIMOURD5il85jhwINmz6o=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCjD4AeekxxUrutvAKXOMBGw": [
        "犬神ふうこ",
        "https://yt3.ggpht.com/a/AATXAJwQlIwQM1IRgA6Gt8O2kLdefXTRpwrAYGRYURCx=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC9vYBIS_MpqO2S6PVWN8gjA": [
        "桜愛かのん",
        "https://yt3.ggpht.com/a/AATXAJxl_9sm8hXJRmTm5ZfMh6bu9N9d57UjTiTgGXrn=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCXWKuvNK8rT87jM3yJETYnA": [
        "華咲心咲",
        "https://yt3.ggpht.com/a/AATXAJyanYRFJmidFw8DHfMjybicE2KcRjSiPKu2I-_rqA=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCnEqLOVmzAMsV2Q0DrWJpqA": [
        "紗夢ゆりか",
        "https://yt3.ggpht.com/a/AATXAJxZA-sVqO2p33qIbyNsVZHbrMYZ54yKIxN-yD7z=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCKM8gEZeqouSxrRmOQrcWLg": [
        "しふぉん",
        "https://yt3.ggpht.com/a/AATXAJxiCqFBLpO6h9l546YGTF41b2u285c6ogt4jskr=s100-c-k-c0xffffffff-no-rj-mo"
    ],
} #配信者のチャンネルID, 配信者名, アイコン画像のURLのリスト

webhook_url_Hololive = 'https://discordapp.com/api/webhooks/757153708940460057/CYpL4xpIUfyBysh2JM4rPDkBQIov9aw5Mi1wn1AS5TBKhTdBfQ3NIRFBnjn8Qv91wixq' #ホロライブ配信開始
webhook_url_Hololive_yotei = 'https://discordapp.com/api/webhooks/757153708940460057/CYpL4xpIUfyBysh2JM4rPDkBQIov9aw5Mi1wn1AS5TBKhTdBfQ3NIRFBnjn8Qv91wixq' #ホロライブ配信予定
broadcast_data = {} #配信予定のデータを格納

YOUTUBE_API_KEY = str_list = ['AIzaSyBhq7jXWlAbe5qK3Uo4ktlBBQha8uk3_pQ','AIzaSyDbfu-2PKUQuCDLqSvK0fan93yXEqqqEL4','AIzaSyC80I6-DalX5NXqPnHHn6gURzlrPBMQ_eM','AIzaSyDGcmSTLFh33RAe-bWO1Vyu0xk1dNTpzeY']

def replace_JST(s):
    a = s.split("-")
    u = a[2].split(" ")
    t = u[1].split(":")
    time = [int(a[0]), int(a[1]), int(u[0]), int(t[0]), int(t[1]), int(t[2])]
    if(time[3] >= 15):
      time[2] += 1
      time[3] = time[3] + 9 - 24
    else:
      time[3] += 9
    return (str(time[0]) + "/" + str(time[1]).zfill(2) + "/" + str(time[2]).zfill(2) + " " + str(time[3]).zfill(2) + "-" + str(time[4]).zfill(2) + "-" + str(time[5]).zfill(2))

def post_to_discord(userId, videoId):
    haishin_url = "https://www.youtube.com/watch?v=" + videoId #配信URL
    content = "配信中！\n" + haishin_url #Discordに投稿される文章
    main_content = {
        "username": Hololive[userId][0], #配信者名
        "avatar_url": Hololive[userId][1], #アイコン
        "content": content #文章
    }
    requests.post(webhook_url_Hololive, main_content) #Discordに送信
    broadcast_data.pop(videoId)

def get_information():
    tmp = copy.copy(broadcast_data)
    api_now = 0 #現在どのYouTube APIを使っているかを記録
    for idol in Hololive:
        api_link = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + idol + "&key=" + YOUTUBE_API_KEY[api_now] + "&eventType=upcoming&type=video"
        api_now = (api_now + 1) % len(YOUTUBE_API_KEY) #apiを1つずらす
        aaa = requests.get(api_link)
        v_data = json.loads(aaa.text)
        try:
            for item in v_data['items']:#各配信予定動画データに関して
                broadcast_data[item['id']['videoId']] = {'channelId':item['snippet']['channelId']} #channelIDを格納
            for video in broadcast_data:
                try:
                    a = broadcast_data[video]['starttime'] #既にbroadcast_dataにstarttimeがあるかチェック
                except KeyError:#なかったら
                    aaaa = requests.get("https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=" + video + "&key=" + YOUTUBE_API_KEY[api_now])
                    api_now = (api_now + 1) % len(YOUTUBE_API_KEY) #apiを1つずらす
                    vd = json.loads(aaaa.text)
                    print(vd)
                    broadcast_data[video]['starttime'] = vd['items'][0]['liveStreamingDetails']['scheduledStartTime']
        except KeyError: #配信予定がなくて403が出た
            continue
    for vi in broadcast_data:
        if(not(vi in tmp)):
            print(broadcast_data[vi])
            try:
                post_broadcast_schedule(broadcast_data[vi]['channelId'], vi, broadcast_data[vi]['starttime'])
            except KeyError:
                continuedef get_information():
    tmp = copy.copy(broadcast_data)
    api_now = 0 #現在どのYouTube APIを使っているかを記録
    for idol in Hololive:
        api_link = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + idol + "&key=" + YOUTUBE_API_KEY[api_now] + "&eventType=upcoming&type=video"
        api_now = (api_now + 1) % len(YOUTUBE_API_KEY) #apiを1つずらす
        aaa = requests.get(api_link)
        v_data = json.loads(aaa.text)
        try:
            for item in v_data['items']:#各配信予定動画データに関して
                broadcast_data[item['id']['videoId']] = {'channelId':item['snippet']['channelId']} #channelIDを格納
            for video in broadcast_data:
                try:
                    a = broadcast_data[video]['starttime'] #既にbroadcast_dataにstarttimeがあるかチェック
                except KeyError:#なかったら
                    aaaa = requests.get("https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=" + video + "&key=" + YOUTUBE_API_KEY[api_now])
                    api_now = (api_now + 1) % len(YOUTUBE_API_KEY) #apiを1つずらす
                    vd = json.loads(aaaa.text)
                    print(vd)
                    broadcast_data[video]['starttime'] = vd['items'][0]['liveStreamingDetails']['scheduledStartTime']
        except KeyError: #配信予定がなくて403が出た
            continue
    for vi in broadcast_data:
        if(not(vi in tmp)):
            print(broadcast_data[vi])
            try:
                post_broadcast_schedule(broadcast_data[vi]['channelId'], vi, broadcast_data[vi]['starttime'])
            except KeyError:
                continue

def check_schedule(now_time, broadcast_data):
    for bd in list(broadcast_data):
        try:
            sd_time = dataformat_for_python(broadcast_data[bd]['starttime']) #配信スタート時間をdatetime型で保管
            sd_time += timedelta(hours=9)
            if(now_time >= sd_time):#今の方が配信開始時刻よりも後だったら
                post_to_discord(broadcast_data[bd]['channelId'], bd) #ツイート
        except KeyError:
            continue
while True:
    now_time = datetime.now() + timedelta(hours=9)
    if((now_time.minute == 0) and (now_time.hour % 2 == 0)):
        get_information()
    check_schedule(now_time, broadcast_data)
    time.sleep(60)
bot.run(token)
