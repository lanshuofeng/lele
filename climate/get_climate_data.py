import datetime
import requests

url_template = "http://cmdp.ncc-cma.net/download/Monitoring/Drought/zki/zki{}.txt"


def save_file(data, file_name):
    with open('cma_data/data/{}'.format(file_name), 'w') as f:
        f.writelines(data)


def get_data(d):
    url = url_template.format(d)
    resp = requests.get(url)
    if resp.status_code != 200:
        return d
    file_name = 'zki{}.txt'.format(d)
    save_file(resp.text, file_name)
    return None


def main():
    start = '2010-01-01'
    end = '2019-12-31'
    datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
    miss_d = []
    while datestart < dateend:
        datestart += datetime.timedelta(days=1)
        d = datestart.strftime('%Y%m%d')[2:]
        print(d)
        res = get_data(d)
        # 记录缺失的天数
        if res is not None:
            miss_d.append(d)
    print(len(miss_d))
    print(miss_d)


if __name__ == "__main__":
    main()