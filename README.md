# Scanner d'En-têtes de Sécurité HTTP

[![Périmètre de Vérification Technique](https://img.shields.io/badge/TAVARDT-Diagnostic%20Technique-5b3cf5.svg)](https://tools.tavardt.com/fr/analyse-en-tetes-securite/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Audit technique automatisé des en-têtes HTTP de sécurité conforme aux recommandations de la CNIL, de l'ANSSI et du RGPD en France.

***

## 1. Périmètre de Vérification Technique

Cet outil en ligne de commande vérifie les directives de protection au niveau du navigateur et du protocole HTTP :

* **Strict-Transport-Security (HSTS):** Impose des connexions chiffrées via HTTPS et prévient les attaques de rétrogradation SSL.
* **Content-Security-Policy (CSP):** Prévient les attaques par injection de scripts (XSS) et restreint les sources de contenu autorisées.
* **X-Frame-Options:** Protège contre les attaques par détournement de clic (clickjacking) en contrôlant l'intégration dans des cadres.
* **X-Content-Type-Options:** Interdit l'interprétation automatique et non sécurisée des types MIME par le navigateur.
* **Referrer-Policy:** Empêche la fuite de données confidentielles contenues dans les URLs référentes vers des tiers.
* **Permissions-Policy:** Applique le principe du moindre privilège aux APIs matérielles du navigateur (caméra, micro, géolocalisation).

***

## 2. Guide de Déploiement Rapide

Exécutez cet outil directement via Python sans installer de paquets tiers :

```bash
python scanner.py exemple.fr
```

***

## 3. Outils de Diagnostic en Ligne (France)

Évaluez la résilience de vos applications publiques à l'aide des outils en ligne TAVARDT :

* [Validateur Consent Mode v2 et RGPD](https://tools.tavardt.com/fr/validateur-consent-mode-v2-rgpd/)
* [Vérificateur DMARC et Protection de Domaine](https://tools.tavardt.com/fr/verificateur-dmarc-email/)
* [Détecteur de Fichiers Sensibles Exposés](https://tools.tavardt.com/fr/scanner-fichiers-exposes/)
* [Portail Complet d'Outils Techniques](https://tools.tavardt.com/fr/)

***

## 4. Conseil et Remédiation Technique

Pour un accompagnement en sécurité des systèmes d'information, des tests d'intrusion ou la mise en conformité RGPD en France, contactez **TAVARDT**.

***

## Liens Utiles

* **Portail Entreprise:** https://ag.tavardt.com/fr/
* **Suite de Diagnostic:** https://tools.tavardt.com/fr/
* **Contact Technique:** https://ag.tavardt.com/fr/contact/

***

### Licence
Distribué sous la licence MIT.

***

© 2026 TAVARDT. Tous droits réservés.
