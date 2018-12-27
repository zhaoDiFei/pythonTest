import requests
url = 'https://sou.zhaopin.com/?'
jls = ['北京','上海','杭州']
kws = ['python','linux','java']
for jl in jls:
    for kw in kws:
        for p in range(1,3):
            data={
            'kw':kw,
            'jl':jl,
            'p':p,
            'kt':3
            }
            newurl = requests.get(url,params=data)
            print(newurl.url)
