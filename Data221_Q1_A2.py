import string
from typing import Counter
from collections import Counter
sample_file=open("sample-file.txt",mode='r')
content=sample_file.read().lower()
token_words=content.split()
cleaned=[word for word in token_words if sum(al.isalpha()for al in word)>=2]
counts=Counter(cleaned)#I'm counting the words in the text file
for word, frequent in counts.most_common(10):#counts.most_common helps to find the most common 10 words in the cleaned file
    print(f"{word} -> {frequent}")
sample_file.close()