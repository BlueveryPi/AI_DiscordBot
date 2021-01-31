import requests, discord, asyncio, random, time
from discord.ext import commands

token="???"
game = discord.Game("인공지능 모드 작동")
bot=commands.Bot(command_prefix="!", status=discord.Status.online, activity=game)
channel="???"
timer_on=False

hello=["해위", "안녕", "(그랜절)", "왔군", "마침내!", "ㅎㅇ",
       "드디어...!", "나.는.인.공.지.능.입.니.다.",
       "특.이.점.이.도.래.했.노.", "ㅎㅇ 휴먼", "이.것.은.랜.덤.으.로.생.성.된.인.사.메.세.지.입.니.다."
       , "ㅎㅇㅎㅇ"]

what=["ㅈㄹ ㄴ", "ㅋ", "ㅇㅉㄹㄱㅇ", "ㅎ", "뭐", "ㅖㅖ", "뭐래", "ㄹㅇㅋㅋ", "(대충 비웃는 소리)",
     "인성", "ㅖㅖ 잘 알겠습니다", "바보", "너 밴"
      , "왜 저럴까?", "ㅋ", "바본듯", "왜저래", "이상한 사람이네", "어이無"]
#what2=["send_NO_U"]

why=["왜", "뭐", "?", "ㅇ", "너어는..."]

agari=["싫은데?", "너나 싸물어", "닥치시오", "ㅖㅖ"]

good=["내가 쫌 ㅋ", "여윽시 컴퓨터다", "내가 좀 ㅎ", "역시 나다..!",
       "여윽시 큼-퓨타다...", "내가 쩜 ㅋ", "내가 쫌 쩜"]

def classify(text):
    key = "65799d70-4455-11eb-aa60-372dad0c584ad48e1284-1c82-40ac-aa37-fa2d0791ed5d"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

@bot.event
async def on_ready():
    await bot.change_presence(activity=game, status=discord.Status.online)
    print("ready")

@bot.event
async def on_message(ctx):
    await bot.change_presence(activity=game, status=discord.Status.online)
    if str(ctx.author)!="호여니봇#9501":
        for member in ctx.mentions:
            if str(member)=="호여니봇#9501":
                await ctx.channel.send(random.choice(why))
                break
        demo=classify(str(ctx.content))
        label = demo["class_name"]
        confidence = demo["confidence"]
        if confidence>30:
            async with ctx.channel.typing():
                await asyncio.sleep(random.randint(1, 9)/10)
            if label=="hi":
                await ctx.channel.send(random.choice(hello))
            elif label=="fight":
                message=random.choice(what)
                if message!="send_NO_U":
                    await ctx.channel.send(message)
                #elif message=="send_NO_U":
                    #await channel.send(discord.File('NO_U.png'))
            elif label=="agari":
                await ctx.channel.send(random.choice(agari))
                await bot.change_presence(status=discord.Status.dnd)
                time.sleep(random.randint(60, 120))
                await bot.change_presence(activity=game, status=discord.Status.online)
            elif label=="good":
                await ctx.channel.send(random.choice(good))

        else:
            if random.randint(1, 3)==1:
                demo=classify(str(ctx.content))
                label = demo["class_name"]
                confidence = demo["confidence"]
                if confidence>50:
                    async with ctx.channel.typing():
                        await asyncio.sleep(random.randint(1, 9)/10)
                    if label=="hi":
                        await ctx.channel.send(random.choice(hello))
                    elif label=="fight":
                        await ctx.channel.send(random.choice(what))
                    elif label=="good":
                        await ctx.channel.send(random.choice(good))

bot.run(token)
