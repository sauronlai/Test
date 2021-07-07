print('~~Zip code information center~~(key "end" to quit)')

zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},"新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}}

city = tuple(zipcode)
dis = []
for c in city:
    dis_list=list(zipcode[c])
    dis+=dis_list
#district = tuple(dis)

def list_zip(city):
    print(zipcode[city])
    

def area_to_zip(area):
    for c in ('台北市','新北市','基隆市'):
        z=zipcode[c].get(area)
        if z==None:
            continue
        print('%s:%d'%(c,z))


def zip_to_area(zip):
    for c in ('台北市','新北市','基隆市'):
        dis=tuple(zipcode[c])
        for d in dis:
            if zipcode[c].get(d)==int(zip):
                print('%s:%s,%s'%(zip,c,d))
            else:
                continue

while True:
    x=input('Please insert city, area or zip code:')
    if x == "end":
        break
    elif x in city:
        list_zip(x)
        continue
    elif x in dis:
        area_to_zip(x)
        continue
    elif x.isdigit():
        zip_to_area(x)
        continue
    else:
        print("Incorrect data")
        continue
