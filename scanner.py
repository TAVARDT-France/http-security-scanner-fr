#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Impose des connexions chiffrées via HTTPS et prévient les attaques de rétrogradation SSL.'), ('Content-Security-Policy', 'Prévient les attaques par injection de scripts (XSS) et restreint les sources de contenu autorisées.'), ('X-Frame-Options', "Protège contre les attaques par détournement de clic (clickjacking) en contrôlant l'intégration dans des cadres."), ('X-Content-Type-Options', "Interdit l'interprétation automatique et non sécurisée des types MIME par le navigateur."), ('Referrer-Policy', 'Empêche la fuite de données confidentielles contenues dans les URLs référentes vers des tiers.'), ('Permissions-Policy', 'Applique le principe du moindre privilège aux APIs matérielles du navigateur (caméra, micro, géolocalisation).')]

def scan_target(target_url):
    print(f"\n[TAVARDT France] Début de l'audit périmétrique des en-têtes de sécurité pour : {target_url}\n")
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
            print(f"\nVérification complète en ligne : https://tools.tavardt.com/fr/analyse-en-tetes-securite/")
            print(f"Support entreprise et cyberdéfense : https://ag.tavardt.com/fr/cybersecurite/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT France] Erreur lors de l'inspection de la cible : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
