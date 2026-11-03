# Phishing Link Detector 
# Author: Hussain Ahmed
# Batch: AI-Powered Cybersecurity

def check_url_safety(url):
    warnings = 0
    print(f"\nAnalyzing: {url}")
    
    # Check 1: IP Address format
    import re
    if re.search(r"http[s]?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", url):
        print("- Alert: URL uses an IP address instead of a standard domain name.")
        warnings += 1
        
    # Check 2: Unencrypted HTTP
    if url.startswith("http://"):
        print("- Alert: Connection is unencrypted (HTTP).")
        warnings += 1
        
    # Check 3: Hidden destinations via @
    if "@" in url:
        print("- Alert: Contains '@' symbol, which can hide the real destination.")
        warnings += 1
        
    if warnings == 0:
        print("- No immediate threats detected, but always stay cautious.")
    else:
        print(f"-> WARNING: {warnings} suspicious indicator(s) found.")

if __name__ == "__main__":
    print("--- EWB Phishing Link Detector ---")
    print("Note: This tool analyzes text only and does not visit the links.\n")
    while True:
        user_input = input("Enter a URL to scan (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Stay safe online. Goodbye!")
            break
        check_url_safety(user_input)
