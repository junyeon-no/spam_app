import tensorflow
from keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
import pickle


###########################모델 로드################################
# Lstm_model = load_mode1l('.\LSTM_model.h5') #영문 스팸 학습 모델
Lstm_model = load_model('.\LSTM_ko_model.h5') #한글 스팸 학습 모델
###########################모델 로드################################


############################테스트 문자##############################
#테스트 한글 샘플
d = ["""
[Web발신]
[긴급재난자금] 상품권이 도착했습니다.
확인해주세요. https://bit.ly/3aSTMel
"""]
# d = ["""

# """
# ]
# 테스트 영문 샘플
# d = ["""
# SIX chances to win CASH!
# From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply Reply HL 4 info
# """]
############################테스트 문자##############################


### tokenizer loading test#################################################################
# 영문 토큰 객체
# with open('tokenizer.pickle', 'rb') as handle:
#     tokenizer = pickle.load(handle)

#한글 토큰 객체
with open('tokenizer_ko.pickle', 'rb') as handle: #한국어 학습된 tokenizer
    tokenizer = pickle.load(handle)
### loading test############################################################################



s = tokenizer.texts_to_sequences(d) # 단어를 숫자값, 인덱스로 변환하여 저장
print(s) 
X_data = s
max_len = 189
data = pad_sequences(X_data, maxlen = max_len) #정수 인코딩된 데이터 패딩
print(data)
print(Lstm_model.predict(data))

