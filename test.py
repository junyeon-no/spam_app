from split_char import split_url

# msg ="""
# [Web 발신]
# 스마일 pay
# 모바일 서비스 이용
# 요청일시 : 2020.12.22
# https://www.svcasvw.com 요청금액
# http://www.naasvfasvasvsavver.com
# 요청금액 : 468,000
# 요청금액 : 468,000
# https://www.vasdvabaebawe.com"""

msg = """
[Web 발신]
스마일 pay
모바일 서비스 이용
요청일시 : 2020.12.22
요청금액
요청금액 : 468,000
요청금액 : 468,000
"""

split_value = split_url(msg)
print("msg---------------------------------------------------------")
print(msg)
print("잘라낸 url--------------------------------------------------")
for url in split_value[1] :
    print(url)
print("잘라낸 문자--------------------------------------------------")
print(split_value[0])