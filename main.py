from phishing_rules import check_keywords

sample_email = 'Urgent! A new document has to be signed. It need immediate action invoice'

result = check_keywords(sample_email)
print('suspicious words found:', result)




