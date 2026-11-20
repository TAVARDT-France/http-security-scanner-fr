# Scanner d'En-têtes de Sécurité HTTP | TAVARDT France

[![Auditoria de Segurança](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/fr/analyse-en-tetes-securite/)
[![Conformidade](https://img.shields.io/badge/Jurisdi%C3%A7%C3%A3o-France-00C853.svg)](https://ag.tavardt.com/fr/cybersecurite/)

Audit technique automatisé des en-têtes HTTP de sécurité conforme aux recommandations de la CNIL, de l'ANSSI et du RGPD en France.

Desenvolvido e mantido pela divisão de cibersegurança e proteção de infraestruturas da **[TAVARDT France](https://ag.tavardt.com/fr/)**.

---

## 1. Périmètre de Vérification Technique

Cet outil en ligne de commande vérifie les directives de protection au niveau du navigateur et du protocole HTTP :

* **Strict-Transport-Security (HSTS):** Força comunicações encriptadas via HTTPS e impede ataques de downgrade e interceptação SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de injeção de scripts (XSS) e restringe as origens autorizadas para carregamento de recursos.
* **X-Frame-Options:** Previne ataques de clickjacking regulando as permissões de incorporação em frames e iframes.
* **X-Content-Type-Options:** Impede a execução indevida de ficheiros derivados de vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege dados sensíveis contidos em URLs de referência contra fuga para domínios terceiros.
* **Permissions-Policy:** Aplica o princípio do menor privilégio sobre APIs de hardware do navegador (câmara, microfone e geolocalização).

---

## 2. Guide de Déploiement Rapide

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py exemplo.com
```

---

## 3. Outils de Diagnostic en Ligne (France)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [Analyseur d'En-têtes HTTP de Sécurité](https://tools.tavardt.com/fr/analyse-en-tetes-securite/)
* [Validateur Consent Mode v2 et RGPD](https://tools.tavardt.com/fr/validateur-consent-mode-v2-rgpd/)
* [Vérificateur DMARC et Protection de Domaine](https://tools.tavardt.com/fr/verificateur-dmarc-email/)
* [Détecteur de Fichiers Sensibles Exposés](https://tools.tavardt.com/fr/scanner-fichiers-exposes/)
* [Portail Complet d'Outils Techniques](https://tools.tavardt.com/fr/)

---

## 4. Conseil et Remédiation Technique

Pour un accompagnement en sécurité des systèmes d'information, des tests d'intrusion ou la mise en conformité RGPD en France, contactez **[TAVARDT France](https://ag.tavardt.com/fr/contact/)**.
