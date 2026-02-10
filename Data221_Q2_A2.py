from collections import Counter


file1= open("sample-file.txt",'r')

lower_case_file=file1.read().lower().split()

cleaner_file=[word for word in lower_case_file if sum(alp.isalpha() for alp in word)>=2]

bigrams=[(cleaner_file[i], cleaner_file[i+1]) for i in range(len(cleaner_file)-1)]

formatted_words=[f"{v} {n}" for v, n in bigrams]

total_order=Counter(formatted_words)

for tot, frequent in total_order.most_common(5):
    print(f"{tot} -> {frequent}")
file1.close()
