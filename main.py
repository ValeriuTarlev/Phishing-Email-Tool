from phishing_rules import check_keywords, domain_sender_check, check_suspicious_link

# Sample email text
sample_email = 'Urgent! A new document has to be signed. It need immediate action invoice'

# Check for phishing words
keywords_found = check_keywords(sample_email)
print('Suspicious words found:', keywords_found)


suspicious_senders = [
    "vale@google.com",
    "admin@secure-amazon.tk",
    "support@gma1l.com",
]

for sender in suspicious_senders: 
    result = domain_sender_check(sender)
    print(f"Domain check for {sender}: {result}")


suspicious_link = [
    "http://192.168.0.1/login",
    "https://www.google.com",
    "http://bit.ly/phishing-link",
]

for link in suspicious_link:
    link_result = check_suspicious_link(link) 
    print(f"Link check for {link}: {link_result}")
