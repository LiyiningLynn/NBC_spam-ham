#nbc
#Li Yining  5118FG14-1
#sms

import csv
from collections import Counter
import math

n_spam = 10868.0
n_ham = 68738.0
prior_spam=692.0/5054.0
prior_ham = 4362.0/5054.0

result_csv = []
with open('sms_test.csv','rU') as test_file:
	test_reader = csv.reader(test_file)
	for line in test_reader:
		line_lst = list(line[1].split())
		for s in range(len(line_lst)):
			list_p_spam=[]
			list_p_ham = []
			with open('sortedSpam.csv','rU') as spam_file:
				spam_reader = csv.reader(spam_file)
				spam_dic = dict(spam_reader)
				if line_lst[s] in spam_dic:
					f_spam = float(spam_dic.get(line_lst[s]))#frequency
					p_spam = f_spam/n_spam
				else:
					p_spam = 1/3924.0
				list_p_spam.append(p_spam)
			with open('sortedHam.csv','rU') as ham_file:
				ham_reader = csv.reader(ham_file)
				ham_dic = dict(ham_reader)
				if line_lst[s] in ham_dic:
					f_ham = float(ham_dic.get(line_lst[s]))
					p_ham = f_ham/n_ham
				else:
					p_ham = 1/13543.0
				list_p_ham.append(p_ham)
			poster_spam = prior_spam
			poster_ham =prior_ham
		for i in range(len(list_p_spam)):
			poster_spam = math.log(poster_spam*list_p_spam[i])
		for i in range(len(list_p_ham)):
			poster_ham = math.log(poster_ham*list_p_ham[i])
		if poster_spam > poster_ham:
			label = 'spam'
		else:
			label = 'ham'
		tuple_result = (line[0],label)
		result_csv.append(tuple_result)
#result1_csv = dict(result0_csv)
#result_csv = sorted(result1_csv)
re_dic = dict(result_csv)
counts = sorted(re_dic.items())
with open('result.csv','w') as result_file:
	result_writer = csv.writer(result_file)
	for i in range(len(result_csv)):
		result_writer.writerow(counts[i])




