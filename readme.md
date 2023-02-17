# 上海天文馆电影票余票监控

# quick start

## 1. 抓取`mpsessionId`, `showNo`
    
抓取电影场次列表的请求， 记录header中的`mpsessid`以及应答中的`showNo`

## 2. 修改配置文件

- `mpsessionid`： 填写上面抓取的信息
- `showNos`: 填写希望监控的时间和`showNo`，可填写多个场次，示例：`{'14:00': 'ASS29366534', '14:45': 'ASS47352013', '15:30':'ASS27839080'}`
- `minSeats`: 填写触发通知的最少座位数量, 示例：2
- `botToken`: 填写telegram bot的token
- `chatId`: 希望发送到的telegram的频道id

## 3. 运行

前台运行

```bash
python movieticket.py
```
后台运行
```bash
nohup python -u movieticket.py > watch.log 2>&1 &
```
