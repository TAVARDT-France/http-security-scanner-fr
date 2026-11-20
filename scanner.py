#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Impose des communications chiffrees exclusives via HTTPS (HSTS).'), ('Content-Security-Policy', 'Restreint les sources de contenu pour empecher les failles XSS.'), ('X-Frame-Options', 'Protege contre les attaques par détournement de clic (clickjacking).'), ('X-Content-Type-Options', 'Interdit le reniflage de type MIME par le navigateur.'), ('Referrer-Policy', "Empeche la fuite de donnees d'URL confidentielles vers des tiers."), ('Permissions-Policy', "Restreint l'acces aux interfaces materielles sensibles du terminal.")]

def scan_target(target_url):
    print(f"\n[TAVARDT France] Debut de l'audit perimetrique des en-tetes de securite pour : {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (fr-FR)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [CONFORME] {header_name}")
                    score += 1
                else:
                    print(f"  [ABSENT] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT France] Score Final : {score}/{total}")
            print(f"\nVerificacao completa online: https://tools.tavardt.com/fr/analyse-en-tetes-securite/")
            print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/fr/cybersecurite/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT France] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
