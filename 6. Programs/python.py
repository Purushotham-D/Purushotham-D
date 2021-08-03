a=dict()
for word in s.split():
	print(word)
	a[word]=s.split().count(word)
print(a)
