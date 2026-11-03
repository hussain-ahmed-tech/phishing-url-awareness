# Test Case Results

**Tester:** Hussain Ahmed  
**Environment:** Windows / Python 3.11  

| Test Case | Input URL | Expected Output | Actual Output | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `https://secure.example.com/login` | No alerts | No immediate threats detected... | **PASS** |
| 2 | `http://10.0.0.1/admin` | IP address + HTTP flags | Alert: URL uses an IP... Alert: Connection is unencrypted... | **PASS** |
| 3 | `http://google.com@phishingsite.net/` | @ symbol + HTTP flags | Alert: Contains '@' symbol... Alert: Connection is unencrypted... | **PASS** |
| 4 | `https://www.very-long-suspicious-domain-name.com` | No alerts (limitation) | No immediate threats detected... | **PASS** |

### Reflection
Testing this script showed that relying on just a few text patterns isn't enough to catch every phishing site, but it successfully identifies some of the most common red flags.
