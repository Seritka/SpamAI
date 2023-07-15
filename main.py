import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def check_spam(user_input, csv_texts):
    # 사용자 입력과 CSV 데이터의 단어를 토큰화합니다
    user_words = word_tokenize(user_input)
    csv_words = [word for text in csv_texts for word in word_tokenize(text)]
    
    stop_words = ["ifg@", "[", "]", "*", "."]
    user_words = [word for word in user_words if word.lower() not in stop_words]
    csv_words = [word for word in csv_words if word.lower() not in stop_words]
    
    # 가장 많이 나온 단어 5개를 추출합니다
    user_most_common = Counter(user_words).most_common(5)
    csv_most_common = Counter(csv_words).most_common(5)
    
    # 가장 많이 나온 단어를 비교하여 스팸 여부를 결정합니다
    user_top_words = [word for word, _ in user_most_common]
    csv_top_words = [word for word, _ in csv_most_common]
    
    # 두 리스트의 공통 단어 비율을 계산합니다
    common_word_ratio = len(set(user_top_words) & set(csv_top_words)) / min(len(user_top_words), len(csv_top_words))
   
    # 스팸 여부를 결정합니다
    if common_word_ratio >= 0.6:  # 50% 이상 공통 단어 비율일 때 스팸으로 판단
        return True
    else:
        return False

# 사용자 입력 받기
user_input = input("텍스트를 입력하세요: ")

# CSV 파일에서 텍스트 읽어오기
data = pd.read_csv('IFG_09_20220725_C_001.csv', names = ['번호', '텍스트'])
csv_texts = data['텍스트']

# 사용자 입력과 CSV 데이터 비교하여 스팸 여부 확인
is_spam = check_spam(user_input, csv_texts)
if is_spam:
    print("스팸입니다.")
else:
    print("스팸이 아닙니다.")

