def split_url(msg = "") : 
    index_s = -1
    index_end = 0
    msg_start_index =0
    serch = 'http'
    url_temp = []
    msg_temp = ""
    while True:
        index_s = msg.find(serch, index_s+1)
        if index_s == -1:
            break 
        if msg[index_s:].find(' ')== -1 and msg[index_s:].find('\n') == -1 :
            index_end = len(msg)
        elif msg[index_s:].find(' ') == -1 and msg[index_s:].find('\n') != -1 :
             index_end = msg[index_s:].find('\n')+ index_s
        elif msg[index_s:].find(' ') != -1 and msg[index_s:].find('\n') == -1 :
             index_end = msg[index_s:].find(' ')+ index_s
        elif msg[index_s:].find(' ')+ index_s > msg[index_s:].find('\n')+ index_s  :
            index_end = msg[index_s:].find('\n')+ index_s
        elif msg[index_s:].find(' ')+ index_s < msg[index_s:].find('\n')+ index_s :
            index_end = msg[index_s:].find(' ')+ index_s
        url_temp.append(msg[index_s:index_end])
        msg_temp = msg_temp + msg[msg_start_index+1 : index_s]
        msg_start_index = index_end
    if(msg_start_index == 0) :
        msg_temp = msg
    return msg_temp, url_temp

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
    print('원본 메세지-------------------------------------------')
    print(test_msg)
    print('분할된 url-------------------------------------------')
    split_values = split_url(test_msg)
    for url in split_values[1]:
        print(url)
    print('\n')
    print('제거된 문자-------------------------------------------')
    print(split_values[0])
