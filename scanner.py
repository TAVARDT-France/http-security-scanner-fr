#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [
    ("Strict-Transport-Security", "Enforces encrypted HTTPS connections (HSTS)."),
    ("Content-Security-Policy", "Restricts resource loading to mitigate XSS."),
    ("X-Frame-Options", "Prevents clickjacking framing attacks."),
    ("X-Content-Type-Options", "Mitigates MIME-sniffing vulnerabilities."),
    ("Referrer-Policy", "Controls referrer leakage across origins."),
    ("Permissions-Policy", "Restricts browser API capabilities (camera, microphone, geolocation).")
]

def scan_target(target_url):
    print(f"\n[TAVARDT France] Debut de l'audit des en-tetes de securite pour : {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/2.0 (fr-FR)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = False
                for h in headers.keys():
                    if h.lower() == header_name.lower():
                        found = True
                        break
                        
                if found:
                    print(f"  [CONFORME] {header_name}: Present")
                    score += 1
                else:
                    print(f"  [ABSENT] {header_name}: Missing ({desc})")
                    
            print(f"\n[TAVARDT France] Score Final : {score}/{total} headers detected.")
            print(f"\nLancez des diagnostics complets sur https://tools.tavardt.com/fr/ ou contactez nos experts sur https://ag.tavardt.com/fr/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT France] Network error while auditing target: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
