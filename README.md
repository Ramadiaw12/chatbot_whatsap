<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=25D366&height=200&section=header&text=WhatsApp%20AI%20Agent%20🤖&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=Répond%20à%20tes%20followers%2024h%2F24%20·%20Propulsé%20par%20Groq%20%2B%20Llama%203.3&descAlignY=58&descSize=16&animation=fadeIn" alt="WhatsApp AI Agent" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-F55036?style=for-the-badge&logo=meta&logoColor=white)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Business_API-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)
![uv](https://img.shields.io/badge/uv-package_manager-DE5FE9?style=for-the-badge)

<br/>

> **Un agent WhatsApp intelligent qui répond automatiquement à tes followers,**
> **présente tes produits et gère tes FAQ — pendant que tu dors.**

<br/>

---

</div>

## ✨ Ce que fait cet agent

```
Follower envoie un message WhatsApp
         │
         ▼
┌─────────────────────┐
│   Meta Webhook      │  ← reçoit le message en temps réel
│   (FastAPI)         │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Agent IA          │  ← Groq + Llama 3.3 70B analyse la question
│   (Groq / Llama)    │     et choisit la meilleure réponse
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Catalogue         │  ← FAQ + produits + prix + liens d'achat
│   (catalog.py)      │
└────────┬────────────┘
         │
         ▼
  Réponse envoyée automatiquement au follower ✅
```

| Fonctionnalité | Détail |
|---|---|
| 🤖 **Réponses automatiques** | L'agent répond instantanément, 24h/24, 7j/7 |
| 💬 **Message de bienvenue** | Accueil personnalisé au premier message |
| 📦 **Catalogue produits** | Prix, description et lien d'achat dans chaque réponse |
| ❓ **FAQ intelligente** | Répond aux questions fréquentes sans intervention manuelle |
| 🧠 **Mémoire contextuelle** | Garde l'historique des 10 derniers messages par contact |
| ✅ **Double coche bleue** | Les messages sont marqués comme lus automatiquement |
| 🌍 **Multilingue** | Détecte la langue du message et répond dans la même |
| 🔁 **Fallback intelligent** | Si l'agent ne sait pas répondre, il te transfère le message |

---

## 🗂️ Structure du projet

```
whatsapp-agent/
│
├── app/
│   ├── main.py        # 🚀 Webhook FastAPI — point d'entrée de l'application
│   ├── agent.py       # 🧠 Cerveau de l'agent (Groq + Llama 3.3 70B)
│   ├── catalog.py     # ⭐ TON catalogue — FAQ, produits, prix, messages
│   ├── whatsapp.py    # 📱 Client Meta WhatsApp Cloud API
│   └── store.py       # 💾 Historique des conversations en mémoire
│
├── pyproject.toml     # 📦 Dépendances gérées par uv
├── .env.example       # 🔑 Variables d'environnement à remplir
└── README.md          # 📖 Ce fichier
```

---

## ⚡ Démarrage rapide

### 1 · Prérequis

- **Python 3.11+**
- **[uv](https://docs.astral.sh/uv/)** — le gestionnaire de paquets moderne pour Python

```bash
# Installe uv si ce n'est pas déjà fait
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Un compte **[Meta for Developers](https://developers.facebook.com/)** avec WhatsApp Business API activé
- Une clé API **[Groq](https://console.groq.com/)** — gratuit pour commencer

---

### 2 · Installation

```bash
# Clone le projet
git clone https://github.com/ton-compte/whatsapp-agent.git
cd whatsapp-agent

# Installe les dépendances avec uv (beaucoup plus rapide que pip)
uv sync

# Prépare les variables d'environnement
cp .env.example .env
```

---

### 3 · Configuration des variables d'environnement

Ouvre `.env` et remplis chaque valeur :

```env
# ─── Meta WhatsApp Business API ──────────────────────────────────────────────
WHATSAPP_TOKEN=ton_access_token_meta        # Dashboard Meta > WhatsApp > Token d'accès
WHATSAPP_PHONE_ID=ton_phone_number_id       # Dashboard Meta > WhatsApp > ID du numéro
WHATSAPP_VERIFY_TOKEN=un_secret_aleatoire   # Chaîne de ton choix, utilisée pour sécuriser le webhook

# ─── Groq ─────────────────────────────────────────────────────────────────────
GROQ_API_KEY=gsk_...                        # console.groq.com → API Keys → Create new key
```

> 💡 **Où trouver ces valeurs ?**
> - `WHATSAPP_TOKEN` et `WHATSAPP_PHONE_ID` : [developers.facebook.com](https://developers.facebook.com/) → ton app → WhatsApp → Paramètres API
> - `GROQ_API_KEY` : [console.groq.com](https://console.groq.com/) → API Keys → Create new key

---

### 4 · Personnalise ton catalogue

> **C'est l'unique fichier à modifier pour adapter l'agent à ton business.**

Ouvre `app/catalog.py` et remplis avec tes vraies données :

```python
BUSINESS_NAME = "Mon Business"   # ← ton nom / ta marque

PRODUCTS = [
    {
        "name": "Formation Instagram Pro",
        "price": "97€",
        "description": "4 semaines pour passer de 0 à 10K abonnés engagés.",
        "link": "https://ton-site.com/formation-instagram",
        "keywords": ["formation", "instagram", "followers", "abonnés"],
    },
    # Ajoute autant de produits que tu veux...
]

FAQ = [
    {
        "question": "Est-ce qu'il y a des garanties ?",
        "answer": "Oui ! Satisfait ou remboursé sous 30 jours ✅",
        "keywords": ["garantie", "remboursement", "retour"],
    },
    # Ajoute tes vraies questions fréquentes...
]
```

---

### 5 · Lance l'agent

```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Vérifie que tout fonctionne :

```bash
curl http://localhost:8000/health
# → {"status": "ok", "agent": "WhatsApp Agent"}
```

---

### 6 · Connecte Meta à ton webhook

Meta a besoin d'une URL publique pour envoyer les messages à ton agent.
En développement local, utilise **[ngrok](https://ngrok.com/)** :

```bash
ngrok http 8000
# → Forwarding  https://abc123.ngrok.io → localhost:8000
#   ↑ copie cette URL
```

Puis dans le **[Dashboard Meta](https://developers.facebook.com/)** :

```
WhatsApp → Configuration → Webhook
  URL de rappel  :  https://abc123.ngrok.io/webhook
  Token          :  la valeur de WHATSAPP_VERIFY_TOKEN dans ton .env
  S'abonner à    :  ✓ messages
```

---

## 🚀 Déploiement en production

### Option A — Railway *(recommandé · gratuit pour démarrer)*

```bash
npm install -g @railway/cli
railway login
railway new
railway up
```

Ajoute tes variables d'environnement dans le dashboard Railway, puis mets à jour l'URL du webhook Meta avec ton domaine Railway.

---

### Option B — Docker

```dockerfile
FROM python:3.12-slim
RUN pip install uv
WORKDIR /app
COPY . .
RUN uv sync --no-dev
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t whatsapp-agent .
docker run -p 8000:8000 --env-file .env whatsapp-agent
```

---

### Option C — VPS (Hetzner, DigitalOcean, Contabo…)

```bash
uv sync --no-dev

# Crée un service systemd pour redémarrage automatique
sudo nano /etc/systemd/system/whatsapp-agent.service
```

```ini
[Unit]
Description=WhatsApp AI Agent
After=network.target

[Service]
WorkingDirectory=/home/ubuntu/whatsapp-agent
EnvironmentFile=/home/ubuntu/whatsapp-agent/.env
ExecStart=uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable --now whatsapp-agent
```

---

## 🧠 Comment fonctionne l'IA

L'agent utilise **Groq** comme moteur d'inférence avec le modèle **Llama 3.3 70B Versatile**.

```python
# app/agent.py — simplifié pour la lisibilité
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=0,        # réponses déterministes — jamais de prix inventés
    max_tokens=512,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},   # catalogue injecté ici
        *conversation_history,                           # contexte des échanges précédents
        {"role": "user",   "content": message_follower}, # message entrant
    ],
)
```

**Pourquoi `temperature=0` ?**
L'agent ne doit jamais inventer un prix ou une offre inexistante.
Avec `temperature=0`, les réponses sont strictement ancrées dans les données du catalogue.

**Pourquoi Groq plutôt qu'OpenAI ?**
Groq utilise des puces LPU dédiées à l'inférence — les réponses arrivent en **moins d'une seconde**, avec un free tier généreux.

---

## 🔄 Flux complet d'une conversation

```
Nouveau contact                  Contact connu
      │                               │
      ▼                               ▼
Message de bienvenue        Chargement de l'historique
personnalisé                  (10 derniers messages)
      │                               │
      └───────────────┬───────────────┘
                      │
                      ▼
              Appel Groq / Llama 3.3
                      │
            ┌─────────┴──────────┐
            │                    │
      Réponse trouvée       Pas de réponse
      dans le catalogue       (fallback)
            │                    │
            ▼                    ▼
    Envoie la réponse     "Je transmets ton
    + lien d'achat si      message à [nom]…"
      pertinent
            │                    │
            └─────────┬──────────┘
                      │
                      ▼
           Sauvegarde dans l'historique
           Message marqué comme lu ✅
```

---

## 🔮 Évolutions possibles

| Fonctionnalité | Complexité | Impact |
|---|---|---|
| 💳 Lien Stripe dans la réponse | Faible | Ventes directes depuis WhatsApp |
| 🗄️ Redis pour persister les conversations | Moyenne | Mémoire après redémarrage |
| 📊 Dashboard analytics (questions les plus posées) | Moyenne | Améliore ta FAQ en continu |
| 📧 Notification email quand fallback déclenché | Faible | Aucun lead chaud manqué |
| 🔘 Boutons interactifs WhatsApp (quick replies) | Moyenne | UX encore plus fluide |
| 🌐 Intégration Notion / Airtable comme CRM | Moyenne | Centralise tous tes leads |
| 🖼️ Support des images et documents reçus | Moyenne | Gère plus de types de messages |

---

## 🛠️ Stack technique

| Composant | Technologie | Rôle |
|---|---|---|
| **Langage** | Python 3.11+ | Langage principal |
| **Package manager** | uv | Installation rapide des dépendances |
| **API Web** | FastAPI + Uvicorn | Reçoit les webhooks Meta en asynchrone |
| **IA** | Groq + Llama 3.3 70B | Génère les réponses naturelles |
| **Messagerie** | Meta WhatsApp Cloud API | Envoie et reçoit les messages WhatsApp |
| **Mémoire** | Dict Python in-memory | Historique des conversations par contact |

---

## ❓ FAQ développeur

**L'agent peut-il répondre à des images ou des vocaux ?**
Pas encore. Pour l'instant, seuls les messages texte sont traités. Les autres types sont ignorés silencieusement. C'est une évolution prévue.

**Que se passe-t-il si le serveur redémarre ?**
L'historique des conversations est stocké en mémoire — il est perdu au redémarrage. Pour persister les données, remplace `store.py` par une intégration Redis ou SQLite.

**Comment tester le webhook sans mobile ?**
Tu peux envoyer une requête POST simulée depuis le dashboard Meta (outil de test de webhook), ou utiliser `curl` avec le format JSON attendu par Meta.

**Le free tier Groq est-il suffisant pour démarrer ?**
Oui. Groq offre un quota généreux sur Llama 3.3 70B, largement suffisant pour tester et lancer tes premières conversations.

---

## 📄 Licence

Projet open-source sous licence **MIT** — libre d'utilisation, de modification et de distribution.

---

<div align="center">

**Conçu et développé avec ❤️ par**

## DIAWANE Ramatoulaye

*"Automatise le répétitif. Concentre-toi sur ce qui compte vraiment."*

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=25D366&height=100&section=footer&text=DIAWANE%20Ramatoulaye&fontSize=20&fontColor=ffffff&fontAlignY=65&desc=Automatise%20le%20répétitif.%20Concentre-toi%20sur%20ce%20qui%20compte.&descAlignY=85&descSize=12" alt="Footer" width="100%"/>

</div>