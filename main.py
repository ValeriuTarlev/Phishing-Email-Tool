from phishing_rules import check_keywords, domain_sender_check, check_suspicious_link, analyze_email


# Sample email text
sample_email = 'Urgent! A new document has to be signed. It need immediate action invoice'

# Check for phishing words in the sample email text
keywords_found = check_keywords(sample_email)
print('Suspicious words found:', keywords_found)

# Analyze sender domains for legitimacy
suspicious_senders = [
    "vale@google.com",
    "admin@secure-amazon.tk",
    "support@gma1l.com",
]

for sender in suspicious_senders: 
    result = domain_sender_check(sender)
    print(f"Domain check for {sender}: {result}")

# Check each URL for signs of phishing (IP addresses, shorteners, shady TLDs)
suspicious_link = [
    "http://192.168.0.1/login",
    "https://www.google.com",
    "http://bit.ly/phishing-link",
]

for link in suspicious_link:
    link_result = check_suspicious_link(link) 
    print(f"Link check for {link}: {link_result}")

# Run the full phishing risk analysis on a single email
result = analyze_email(
    subject="Your Amazon details", 
    body="Your order #123-4567890-1234567 has been shipped and is on its way.", 
    sender="www.@amazon.com",
    link=" "
)

# Display the final analysis result with score and breakdown
print("\n--- Phishing Risk Analysis ---")
print(f"Score: {result['score']}")
print(f"Risk Level: {result['risk_level']}")
print("Details:")
print(f"- Keywords: {result['details']['keywords']}")
print(f"- Domain: {result['details']['domain']}")
print(f"- Link: {result['details']['link']}")
print(f"- AI Result: {result['details']['ai_result']}")

