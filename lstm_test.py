import tensorflow
from keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os


#https://tykimos.github.io/2017/06/10/Model_Save_Load/ <<<<<참고 블로그

Lstm_model = load_model('.\LSTM_model.h5')
max_len = 189
d = ["""
[Web발신]
[긴급재난자금] 상품권이 도착했습니다.
확인해주세요.
"""]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(d)
s = tokenizer.texts_to_sequences(d) # 단어를 숫자값, 인덱스로 변환하여 저장
print(s) #[ [ 33 , 33, 33] ]
X_data = s
data = pad_sequences(X_data, maxlen = max_len)
print(data)
print(Lstm_model.predict(data))