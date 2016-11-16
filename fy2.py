import requests
import urllib.request
from bs4 import BeautifulSoup
import os



def url_open1(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html = requests.get(url, headers=header).text
    soup = BeautifulSoup(html, 'lxml')
    return soup


def all_links(url):
    soup = url_open1(url)
    cili_link = soup.find_all('div', class_="search-item")
    if len(cili_link) == 0:
        print('该番号无资源！')
    else:
        for each in cili_link:
            cili = each.a['href'].split('/')[-1].split('.')[0]
            leixing = each.span.get_text()
            size = each.b.find_next('b').text
            print('林司机提供的磁力链接为：' + 'magnet:?xt=urn:btih:' + '%s 类型：%s 大小：%s' % (
            cili, leixing, size) + '\n' + '----------------------------' + '\n')




def url_open(parser):
    soup = BeautifulSoup(parser,'lxml')
    return soup

def all_info(parser):
    soup = url_open(parser)
    all = soup.find_all('a', class_="movie-box")
    for each in all:
        img = each.img['src']
        title = each.date.text
        with open(title + '.jpg', 'wb') as f:
            print('正在拉取%s的封面......'%(title))
            picture = requests.get(img).content
            f.write(picture)
def all_info_high(parser):
    soup = url_open(parser)
    all = soup.find_all('a', class_="movie-box")
    for each in all:
        img = each.img['src']
        img=img[0:-5]
        img=img+'l.jpg'
        title = each.date.text
        with open(title+'.jpg','wb') as f:
            print('正在拉取%s的封面......'%(title))
            picture = requests.get(img).content
            f.write(picture)






if __name__=='__main__':
    name = input('请输入番号或者女优名字(请输入日文名)：')
    page = int(input('请输入拉取页数：'))
    os.mkdir(name)
    os.startfile(name)
    os.chdir(name)
    num=1
    print('请选择（输入数字1或者2）：')
    print('              1.预览图（加载快速）')
    print('              2.高清大图（加载慢速）')
    shuru = int(input('请输入：'))
    if shuru==1:
        while num<=page:
            url =str('https://avmo.pw/cn/search/'+str(name)+'/page/'+str(num))
            head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            html = requests.get(url, headers=head)
            if html.status_code == 200:
                print('正在搜索第%d页，搜索成功，正在跳转......'%(num))
                parser_html = html.text
                all_info(parser_html)
                num += 1
                print('Over！')


            else:
                print('连接网站失败！')
    else:
        while num <= page:
            url = str('https://avmo.pw/cn/search/' + str(name) + '/page/' + str(num))
            head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            html = requests.get(url, headers=head)
            if html.status_code == 200:
                print('正在搜索第%d页，搜索成功，正在跳转......' % (num))
                parser_html = html.text
                all_info_high(parser_html)
                num += 1
                print('Over！')


            else:
                print('连接网站失败！')

    while True:
        print('-------------------------本软件网站由林子涵老司机提供---------------------------')
        print('-------------------------信任林司机  随时随地带你飙车---------------------------')
        print('-------------------------作者：516宿舍第一adc  孙衎衎---------------------------')
        num = 1
        name = input('请输入番号(按Q退出)：')
        if name=='q' or name=='Q':
            break
        page = int(input('请输入拉取页数:'))
        while page >= num:
            url1 = 'http://www.ciliba.org/s/' + str(name) + '_rel_' + str(num) + '.html'
            all_links(url1)
            num += 1
























