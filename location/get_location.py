import requests

url = 'https://apis.map.qq.com/jsapi?qt=geoc&addr={}&key=UGMBZ-CINWR-DDRW5-W52AK-D3ENK-ZEBRC&output=jsonp&pf=jsapi&ref=jsapi'


def get_location(name):
    resp = requests.get(url.format(name))
    r = resp.json()
    if r['info']['error'] == 0:
        x = r['detail']['pointx']
        y = r['detail']['pointy']
    else:
        print("未查询到该地区的信息: {}".format(name))
        x = 0.0
        y = 0.0
    return x, y


def main():

    with open('data.txt', 'r') as f:
        lines = f.readlines()
    with open('data_with_geo.csv', 'w') as f:
        header = "地区,经度,纬度\n"
        f.writelines(header)
        for line in lines:
            name = line.strip()
            x, y = get_location(line.strip())
            f.writelines("{},{},{}\n".format(name, x, y))
        print("success")


if __name__ =='__main__':
    main()