import csv
from collections import Counter

word_list=[]#raw, to count word frequency
with open('ham.csv','rU') as my_file:
	my_reader = csv.reader(my_file)
	for line in my_reader:
		word_list.extend(line[1].split())
#here we create a list of words from all the emails
cnt = dict(Counter(word_list))
counts = sorted(cnt.items(),key=lambda x:x[1],reverse = True)
#print counts

with open('sortedHam.csv','w') as my_count:
		my_writer = csv.writer(my_count)
		#my_writer.writerow(counts)
		for i in range(len(counts)):
			my_writer.writerow(counts[i])