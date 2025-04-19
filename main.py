from phishing_rules import check_keywords
from phishing_rules import domain_sender_check

sample_email = 'Urgent! A new document has to be signed. It need immediate action invoice'

result = check_keywords(sample_email)
print('suspicious words found:', result)

suspiscious_domain = "vale@google.com"

results = domain_sender_check(suspiscious_domain)
print(results)
