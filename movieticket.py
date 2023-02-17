#!/usr/bin/python3

import telegram
import requests
import time
import config

print('welcome')
urlTemplate="https://ticket.sstm.org.cn/vendor/movie/getShowSeats.xhtml?showNo={}&appId=wx1d7ddce169710ba7"
header={'Host':'ticket.sstm.org.cn','Connection':'keep-alive','mpsessid':config.mpsessionid,'content-type':'application/x-www-form-urlencoded','Accept-Encoding':'gzip,compress,br,deflate','User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.32(0x18002033) NetType/3G Language/zh_CN','Referer':'https://servicewechat.com/wx1d7ddce169710ba7/38/page-frame.html'}
bot=telegram.Bot(token=config.botToken)

print(bot.getMe())


def get_seat(time,url):
	r = requests.get(url, headers=header)
	if r.status_code != 200:
		print('request failed!')
		bot.sendMessage(chat_id=config.chatId,text='request failed!')

	if str(r.content).find('\"status\":1') >= config.minSeats:
		print(time + ' have seats!')
		bot.sendMessage(chat_id=config.chatId, text=time + ' have seats!')
	else:
		print(time + ' no seats!')


while 1:
	print(time.asctime( time.localtime(time.time()) ))
	
	for showTime, showNo in config.showNos.items():
		get_seat(showTime, urlTemplate.format(showNo))
		time.sleep(1)
	print()
	time.sleep(5)

