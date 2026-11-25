# Scanner d'En-têtes de Sécurité HTTP

[![Périmètre de Vérification Technique](https://img.shields.io/badge/TAVARDT-Diagnostic%20Technique-5b3cf5.svg)](https://tools.tavardt.com/fr/analyse-en-tetes-securite/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Audit technique automatisé des en-têtes HTTP de sécurité conforme aux recommandations de la CNIL, de l'ANSSI et du RGPD en France.

Conçu et maintenu par le pôle de cyberdéfense de **TAVARDT** pour les infrastructures numériques françaises.

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

## 2. Matrice de Référence Défensive et Atténuation des Risques

<table>
  <thead>
    <tr>
      <th>En-tête de Sécurité</th>
      <th>Vecteur de Risque Atténué</th>
      <th>Comportement par Défaut (Absent)</th>
      <th>Configuration Recommandée</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Strict-Transport-Security</strong></td>
      <td>Attaques de SSL-stripping et déclassement HTTP</td>
      <td>Connexion initiale effectuée en HTTP non chiffré</td>
      <td><code>max-age=31536000; includeSubDomains; preload</code></td>
    </tr>
    <tr>
      <td><strong>Content-Security-Policy</strong></td>
      <td>Cross-Site Scripting (XSS) et injection de données</td>
      <td>Exécution sans restriction de scripts arbitraires</td>
      <td>Déclaration stricte des sources de confiance pour scripts</td>
    </tr>
    <tr>
      <td><strong>X-Frame-Options</strong></td>
      <td>Clickjacking et détournement de clic via iframes</td>
      <td>Page intégrable dans tout site tiers non vérifié</td>
      <td><code>DENY</code> ou <code>SAMEORIGIN</code></td>
    </tr>
    <tr>
      <td><strong>X-Content-Type-Options</strong></td>
      <td>MIME-sniffing et interprétation erronée de fichiers</td>
      <td>Le navigateur interprète des fichiers statiques comme code</td>
      <td><code>nosniff</code></td>
    </tr>
    <tr>
      <td><strong>Referrer-Policy</strong></td>
      <td>Fuite de paramètres et jetons dans les URLs</td>
      <td>URL complète transmise vers des origines externes</td>
      <td><code>strict-origin-when-cross-origin</code></td>
    </tr>
    <tr>
      <td><strong>Permissions-Policy</strong></td>
      <td>Accès non autorisé aux capteurs matériels</td>
      <td>Capteurs matériels sollicités sans filtrage préalable</td>
      <td>Restriction stricte pour la caméra, le micro et la position</td>
    </tr>
  </tbody>
</table>

***

## 3. Guide de Déploiement Rapide et Automatisation

Exécutez cet outil directement via Python sans installer de paquets tiers :

```bash
python scanner.py exemple.fr
```

Le moteur d'audit évalue les réponses du serveur de manière déterministe :

* **Bibliothèque Standard Native:** Fonctionne exclusivement avec la bibliothèque standard Python (`urllib.request`), éliminant toute dépendance externe.
* **Score Déterministe:** Teste les six en-têtes cruciaux sans distinction de casse et attribue un score entier sur six.
* **Intégration Continue CI/CD:** S'intègre sans difficulté dans les flux de validation avant déploiement et les audits de conformité automatisés.

***

## 4. Foire Aux Questions (FAQ Technique)

### 1. Comment l'absence de l'en-tête HSTS expose-t-elle les utilisateurs aux attaques de SSL-stripping ?
Sans Strict-Transport-Security, les navigateurs initient leurs connexions en HTTP non chiffré avant d'obtenir la redirection HTTPS. Des attaquants situés sur le transit réseau peuvent intercepter cette requête initiale, supprimer le chiffrement et espionner le trafic en clair.

### 2. Quel est le rôle défensif principal de Content-Security-Policy (CSP) ?
Content-Security-Policy constitue une défense en profondeur contre les attaques de Cross-Site Scripting (XSS) et les injections de données. Cet en-tête restreint explicitement les domaines autorisés pour l'exécution de scripts, empêchant l'exécution de code malveillant.

### 3. De quelle façon X-Frame-Options protège-t-il les applications contre le clickjacking ?
X-Frame-Options indique au navigateur si une ressource peut être intégrée dans une balise frame, iframe ou object. L'attribution des valeurs DENY ou SAMEORIGIN empêche des sites malveillants de superposer des interfaces transparentes pour détourner les actions des utilisateurs.

### 4. Pourquoi Permissions-Policy est-il indispensable pour la confidentialité matérielle ?
Permissions-Policy limite l'accès du navigateur aux fonctionnalités sensibles du matériel telles que la caméra, le microphone et la géolocalisation. Cette directive garantit qu'aucun script tiers ou iframe ne peut exploiter les capteurs du terminal sans autorisation explicite.

### 5. Ce scanner d'en-têtes HTTP peut-il être intégré dans des pipelines CI/CD ?
Oui, le script `scanner.py` repose exclusivement sur la bibliothèque standard Python sans paquets externes. Il calcule des scores d'audit déterministes, ce qui permet son intégration fluide dans les phases de validation automatisée avant mise en production.

***

## 5. Outils de Diagnostic en Ligne (France)

Évaluez la résilience de vos applications publiques à l'aide des outils en ligne TAVARDT :

* [Validateur Consent Mode v2 et RGPD](https://tools.tavardt.com/fr/validateur-consent-mode-v2-rgpd/)
* [Vérificateur DMARC et Protection de Domaine](https://tools.tavardt.com/fr/verificateur-dmarc-email/)
* [Détecteur de Fichiers Sensibles Exposés](https://tools.tavardt.com/fr/scanner-fichiers-exposes/)
* [Portail Complet d'Outils Techniques](https://tools.tavardt.com/fr/)

***

## 6. Conseil et Remédiation Technique en France

Pour un accompagnement en sécurité des systèmes d'information, des tests d'intrusion avancés ou la mise en conformité RGPD à Paris, Lyon ou Marseille, contactez **TAVARDT**.

***

## Liens Utiles

* **Portail Institutionnel:** https://ag.tavardt.com/fr/
* **Suite de Diagnostic:** https://tools.tavardt.com/fr/
* **Contact Technique:** https://ag.tavardt.com/fr/contact/

***

### Licence
Distribué sous la licence MIT.

***

© 2026 TAVARDT. Tous droits réservés.
