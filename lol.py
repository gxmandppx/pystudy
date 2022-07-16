import requests,time,re,json

LOLServerSelect = [
    {'t':"黑色玫瑰   电信",'v':"14", 'status':"1"}]

def get_receive(cookie):
    for id,cook in enumerate(cookie):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 qifei',
            'cookie': cook
        }
        print(f"第{id+1}个账号  {re.findall('([1-9][0-9]{4,14})',cook)[0]} \n")
        for i in LOLServerSelect:
            #print(i['v'])
            url = f"https://apps.game.qq.com/daoju/igw/main?_service=buy.plug.svr.sysc_ext&paytype=8&iActionId=22565&propid=338943&buyNum=1&_app_id=1006&_plug_id=72007&_biz_code=lol&areaid={i['v']}"
            res = requests.get(url,headers=headers).json()
            print(res)
            if 'act_amount' in res:
                print(f"{i['t']} {json.loads(res['msg'])[0]['sMsg']}")
            else:
                print(f"{i['t']}  {res['msg']}")
            #print(res)

            time.sleep(1)
        print()

if __name__ == '__main__':
    cookie = ['skey=@WIDIdkaGU;uin=o2016330070']  #自己修改此处
    get_receive(cookie)