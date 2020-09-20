from discord.ext import commands
import os
import traceback

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
    "UCAyjv2xdlJt8sYDbmMN-tFw": [
        "水月水人",
        "https://yt3.ggpht.com/a/AATXAJwJrRoSU5Qnl6eGt72LEe8h7qlpH3Se0R8GX-B4=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCtL469kQLOf6732_MZgo--w": [
        "朝武神奈",
        "https://yt3.ggpht.com/a/AATXAJxXz0bW4HtgfTiX7cRps82UnSAboDzIceh-dPzx=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCXJaM56bVzQLAcnokYvHUTg": [
        "和泉さくら",
        "https://yt3.ggpht.com/a/AATXAJzDsrjnoB0fd25jdYTOH7E8zzTtw9GbBMky1f4X=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCeJ0yHgI7xtDl6HDxeelUqw": [
        "猫望とろ",
        "https://yt3.ggpht.com/a/AATXAJwj55IkgAJFUyZGJqFF-cIpAdCghJ_IGyAnVgRu=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCvgpEW8qmD_zdYfSXpe_gGg": [
        "アルフレッド・ロバーツ",
        "https://yt3.ggpht.com/a/AATXAJx7nFCSj2bz7La3Icb6SwKJg34-sbshbHTYQb9T=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCBIi1YjzbtR3xA2-n6uJpCA": [
        "古戸宮まい",
        "https://yt3.ggpht.com/a/AATXAJxcgYUbKWdQNc2BphkIImKLCYZaLXsj8un9jvVF=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCfSueu6jRDR5wAi-9W7G_Zg": [
        "天使エム",
        "https://yt3.ggpht.com/a/AATXAJwLWltXEI50EXo9OFHHYAnlb7r2ZPBure_-ffp2=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCFnxFddHDrRUOgRoQuJ3Zeg": [
        "胡桃るく",
        "https://yt3.ggpht.com/a/AATXAJx7sEz7RHahF91kisF02UDrmeRNXB1l8WDFNCRf=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCu5pfqIxJDFRg4qSIRHRPzg": [
        "宇佐美黒兎",
        "https://yt3.ggpht.com/a/AATXAJxfITFlg2SDitpmU4ouGveW7mYt7S6zyjaQx88n=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC0Dq5uZeyjINiJ-BZQugr9g": [
        "夢空愛里鈴",
        "https://yt3.ggpht.com/a/AATXAJzyF6PfOnBxk2nVrt5atH4AQI5Rlx_VfcYvP0YI=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCZwsOhl_T0k2Sgf7S3JReNQ": [
        "音琴かなみ",
        "https://yt3.ggpht.com/a/AATXAJy3v3BnB7Oei5nl69RkeJdOkR9XBbkYo1GfW95x-w=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCS9Obb1VyV-mEmFtlK1RzoA": [
        "獅子ヶ谷フレア",
        "https://yt3.ggpht.com/a/AATXAJzIwAA_odB2o_ThBM6Onf6wahXH1n_MnlfcC3E0=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCIlpeM3yjTAf5GuRn3eUWMQ": [
        "紗蘭",
        "https://yt3.ggpht.com/a/AATXAJyKQEpOETZzAdZiJyixfkEmeu8aLfXZNe-uPJLo=s100-c-k-c0xffffffff-no-rj-mo"
    ],
     "UCk7ahkz45oPxCR_OTR1nIUQ": [
        "星野じゅり",
        "https://yt3.ggpht.com/a/AATXAJwYvvxbUKO7tJeIHOwaaBeE83S9Yju9cl-NlMl9zg=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCHEGebAKYt0vmaEQraicUIw": [
        "憂音",
        "https://yt3.ggpht.com/a/AATXAJwGAI-ofm4MuOfFkhq3TEtyFDI_WkUV7uAhlHxp=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCdOcEgE71dj-OBTLcGrYu_w": [
        "恋夢ルネア",
        "https://yt3.ggpht.com/a/AATXAJx4XP2WFb_Z_TS5Uvg0N5CTvUOhPcqUe1V5AD7l=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCmm5zXNh3IUXI2KiAe_Ae-g": [
        "日輪あさひ",
        "https://yt3.ggpht.com/a/AATXAJzp2rS7A1qUb03c-iuTFEfs-WjI6yrRo85wLwnEhg=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCznmf_WBKxE4vDyORj4JXGQ": [
        "有栖川エトナ",
        "https://yt3.ggpht.com/a/AATXAJzs5cWML8-b7CJjf-Qtu_ztU_cZ5xkqozVjH_WL=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCZrMsKDP_OQuwICm_b1TGZg": [
        "浅葱ゆあ",
        "https://yt3.ggpht.com/a/AATXAJywvFEBQJIKtJOW8SaBe5A9rjkw1d4cecHAJMuUxg=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC9YDHMtwya_bOjydoLnEG6A": [
        "春摘ハヤテ",
        "https://yt3.ggpht.com/a/AATXAJz9TF1J_7sH7MyBjOI-Fspicd2A3Ai1ni1vWWRl1Q=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC_drYUN9rC9sygy-E2A72jA": [
        "織田りこる",
        "https://yt3.ggpht.com/a/AATXAJwGqoX5e5JN7vBxtH0OdTLgBAPs10nv_M9e-eru=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCnjRGI-xos1ve5EI5CJhuxA": [
        "朝凪汐",
        "https://yt3.ggpht.com/a/AATXAJyg_orBy7JrwojNTV33FTNzrze4OctJ8Osh8qzvcQ=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCgbHGAI52ZYk3LRO0iVJUIQ": [
        "芭蕉宮香",
        "https://yt3.ggpht.com/a/AATXAJyQDX3wHAu-CZV3ktKejXfwLATzTBWQC5kMJUBk=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCpD21MmuBXZ32gT2a6R8zpw": [
        "黒江麗子",
        "https://yt3.ggpht.com/a/AATXAJywExA_rodrjMk2PvGcMqaRaJuZmo6ETsUmGuOemA=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCm0000cv4ivj7kvgCnqEDLA": [
        "たるとみつき",
        "https://yt3.ggpht.com/a/AATXAJwLWmCuUa8gEGWlXkY2i7bMN3mgWLpbfNZB-IJtDw=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCDFi0bH-HRvABhuPSA32iQA": [
        "さく",
        "https://yt3.ggpht.com/a/AATXAJz9pq_vp9qK2ua53BuiE2b-cctJT5kptwwiDOwfYA=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "user/otonee0911": [
        "星乃りんね",
        "https://yt3.ggpht.com/a/AATXAJzPWaFh8679kM2UbyBsmFSXotSx0rqzcVkK4OpNHg=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "user/kurumi344": [
        "くるみ",
        "https://yt3.ggpht.com/a/AATXAJwVRgKHnGLPmz9TiL6XqF9Mb8-iajmEf7jxcBm93Q=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCu2WSoswhlYErSPYsbdpLhQ": [
        "つづきつづ美",
        "https://yt3.ggpht.com/a/AATXAJwdbVEqtw7KGQgFjNJnbTRpAfgdharBHs7BmWMvmg=s100-c-k-c0xffffffff-no-rj-mo"
    ],

} #配信者のチャンネルID, 配信者名, アイコン画像のURLのリスト

webhook_url_Hololive = '配信開始チャンネル用のwebhookリンク' #ホロライブ配信開始
webhook_url_Hololive_yotei = '配信開始予定用のwebhookリンク' #ホロライブ配信予定
broadcast_data = {} #配信予定のデータを格納

YOUTUBE_API_KEY = ['AIzaSyDGcmSTLFh33RAe-bWO1Vyu0xk1dNTpzeY','AIzaSyC80I6-DalX5NXqPnHHn6gURzlrPBMQ_eM','AIzaSyDbfu-2PKUQuCDLqSvK0fan93yXEqqqEL4']

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
