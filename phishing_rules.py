import re

# List of Phishing keywords
phishing_keywords = [
        'action', 'document', 'verification', 'urgent', 'efax', 'vm', 'request', 'required', 'new', 'message', 'invoice'
    
]

# List of trusted domain
trusted_domain = [

        # Tech Companies
        "google.com", "gmail.com", "microsoft.com", "outlook.com", "apple.com", "icloud.com",
        "amazon.com", "aws.amazon.com", "facebook.com", "meta.com", "instagram.com", "linkedin.com",
        "youtube.com", "netflix.com", "dropbox.com", "adobe.com", "zoom.us", "skype.com", "slack.com",
        "github.com", "gitlab.com", "bitbucket.org", "atlassian.com", "notion.so", "figma.com",
        
        # Financial Institutions
        "paypal.com", "stripe.com", "squareup.com", "chase.com", "bankofamerica.com",
        "wellsfargo.com", "capitalone.com", "americanexpress.com", "visa.com", "mastercard.com",

        # Government and Education
        "irs.gov", "usa.gov", "gov.uk", "europa.eu", "edu.com", "khanacademy.org", "edx.org",

        # Retail & Delivery
        "ebay.com", "etsy.com", "target.com", "walmart.com", "costco.com", "homedepot.com",
        "ups.com", "fedex.com", "dhl.com", "usps.com",

        # Health / Insurance
        "cvs.com", "walgreens.com", "unitedhealthcare.com", "aetna.com", "bluecross.com",

        # Others (general services)
        "spotify.com", "uber.com", "airbnb.com", "booking.com", "expedia.com", "tiktok.com",
        "reddit.com", "quora.com", "pinterest.com", "twitter.com", "x.com"
    ]        
    
# List of suspicious TLDs 
suspicious_tlds = [
    ".ru",     # Russia
    ".tk",     # Tokelau (free domain provider, often abused)
    ".ml",     # Mali (also free)
    ".ga",     # Gabon (free domains)
    ".cf",     # Central African Republic (free)
    ".gq",     # Equatorial Guinea (free)
    ".xyz",    # Cheap and common in spam
    ".top",    # Very low cost, high abuse
    ".club",   # Common in fake social/fan clubs
    ".work",   # Spam and fake job listings
    ".click",  # Common in phishing URLs
    ".link",   # Common in suspicious shorteners
    ".fit",    # Often used in fake health scams
    ".rest",   # Used in fake restaurant/phishing scams
    ".cn",     # China (not shady by default, but high phishing volume)
    ".su",     # Old Soviet Union domain, often unregulated
    ".cc",     # Used in malware campaigns
    ".pw",     # “Professional Web” – cheap and widely abused
    ".date",   # Used in romance/dating scams
    ".review", # Fake review and scam sites
    ".science" # Used in fake academic or research sites
]

# List of URL shorteners
shorteners = [
    "bit.ly",
    "tinyurl.com",
    "t.co",              
    "ow.ly",            
    "goo.gl",               
    "is.gd",
    "buff.ly",           
    "rebrand.ly",
    "adf.ly",
    "shorte.st",
    "cutt.ly",
    "rb.gy",             
    "soo.gd",
    "v.gd",
    "cli.re",
    "bl.ink",
    "trib.al",          
    "po.st",
    "mcaf.ee",           
    "qr.ae",             
    "lnkd.in",           
    "bit.do",
    "lc.chat",
    "1url.com",
    "u.to",
    "yourls.org"         
]


def check_keywords(text): 
    text = text.lower()
    found_keywords = [ word for word in phishing_keywords if word in text]
    return found_keywords


def domain_sender_check(email_domain):
    domain = email_domain.split('@')[-1].lower()
    if domain in trusted_domain and not any(domain.endswith(tld) for tld in suspicious_tlds):
        return "Domain looks legit"
    else:
        return "Domain suspicious"
    
    
def check_suspicious_link(url): 
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    
    if ip_pattern.search(url): 
        return "Suspicious: IP address link detected"
    if any(shortener in url for shortener in shorteners):
                return "Suspicious: URL shortener detected"
    if any(url.endswith(tld) for tld in suspicious_tlds):
         return "Suspicious: Shady TLD detected"
    
    return "Link looks clean"

    

    
    
    