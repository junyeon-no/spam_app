def split_url(c = "") : 
    index_s = -1
    index_end = 0
    serch = 'http'
    url_temp = []
    while True:
        index_s = c.find(serch, index_s+1)
        if index_s == -1:
            break
        if c[index_s:].find(' ')== -1 and c[index_s:].find('\n') == -1 :
            index_end = len(c)
        elif c[index_s:].find(' ') == -1 and c[index_s:].find('\n') != -1 :
             index_end = c[index_s:].find('\n')+ index_s
        elif c[index_s:].find(' ') != -1 and c[index_s:].find('\n') == -1 :
             index_end = c[index_s:].find(' ')+ index_s
        elif c[index_s:].find(' ')+ index_s > c[index_s:].find('\n')+ index_s  :
            index_end = c[index_s:].find('\n')+ index_s
        elif c[index_s:].find(' ')+ index_s < c[index_s:].find('\n')+ index_s :
            index_end = c[index_s:].find(' ')+ index_s
        url_temp.append(c[index_s:index_end])
    return url_temp

test_msg = """
[Web 발신]
스마일 pay
모바일 서비스 이용
요청일시 : 2020.12.22
https://www.svcasvw.com 요청금액
http://www.naasvfasvasvsavver.com
요청금액 : 468,000
요청금액 : 468,000
https://www.vasdvabaebawe.com"""

if __name__ == "__main__":
    print('split_url(c)의 결과-------------------------------------------')
    urls = split_url(test_msg)
    for url in urls:
        print(url)
    print('\n')
