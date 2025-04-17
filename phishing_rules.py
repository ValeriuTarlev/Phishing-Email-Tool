def check_keywords(text): 
    phishing_keywords = [
        'action', 'document', 'verification', 'urgent', 'efax', 'vm', 'request', 'required', 'new', 'message', 'invoice'
    
    ]
    text = text.lower()
    found_keywords = [ word for word in phishing_keywords if word in text]
    return found_keywords



