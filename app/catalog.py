"""
catalog.py — Ton catalogue FAQ + produits.
Modifie ce fichier pour personnaliser les réponses de ton agent.
"""

# ─── À PERSONNALISER ────────────────────────────────────────────────────────

BUSINESS_NAME = "Mon Business"  # ← mets ton nom ici

# Tes produits / services avec prix et description
PRODUCTS = [
    {
        "name": "Formation Instagram Pro",
        "price": "97€",
        "description": "4 semaines pour passer de 0 à 10K abonnés engagés. Accès à vie, mises à jour incluses.",
        "link": "https://ton-site.com/formation-instagram",
        "keywords": ["formation", "instagram", "followers", "abonnés", "réseaux sociaux"],
    },
    {
        "name": "Template Pack Canva",
        "price": "27€",
        "description": "50 templates premium Canva pour créer du contenu professionnel en 5 minutes.",
        "link": "https://ton-site.com/templates",
        "keywords": ["template", "canva", "design", "graphisme", "visuels"],
    },
    {
        "name": "Coaching 1-1",
        "price": "197€ / session",
        "description": "Session stratégie de 60 min. On analyse ton compte et on crée ton plan d'action.",
        "link": "https://ton-site.com/coaching",
        "keywords": ["coaching", "session", "accompagnement", "stratégie", "aide"],
    },
]

# Tes FAQ — questions fréquentes de tes followers
FAQ = [
    {
        "question": "Comment te contacter ?",
        "answer": "Tu peux me répondre ici sur WhatsApp, ou envoyer un email à contact@ton-site.com 📩",
        "keywords": ["contact", "email", "joindre", "parler"],
    },
    {
        "question": "Est-ce qu'il y a des garanties ?",
        "answer": "Oui ! Satisfait ou remboursé sous 30 jours sur toutes mes formations, sans question posée ✅",
        "keywords": ["garantie", "remboursement", "satisfait", "retour"],
    },
    {
        "question": "Comment ça se passe après l'achat ?",
        "answer": "Tu reçois un email de confirmation immédiatement avec ton accès. Si tu n'as rien reçu, vérifie tes spams 📬",
        "keywords": ["achat", "après", "accès", "email", "confirmation", "reçu"],
    },
    {
        "question": "Est-ce que tes formations sont adaptées aux débutants ?",
        "answer": "Absolument ! Tout est expliqué étape par étape, même si tu pars de zéro 🙌",
        "keywords": ["débutant", "niveau", "commencer", "zéro", "facile"],
    },
    {
        "question": "Quelle est la durée des formations ?",
        "answer": "La formation principale fait 4 semaines de contenu, mais tu avances à ton rythme avec l'accès à vie ⏱️",
        "keywords": ["durée", "temps", "semaines", "rythme", "accès"],
    },
]

# Message de bienvenue (premier message d'un nouveau contact)
WELCOME_MESSAGE = """Salut ! 👋 Bienvenue chez {business_name} !

Je suis ton assistant automatique. Je peux t'aider avec :

📦 *Mes produits & formations*
❓ *Répondre à tes questions*
💬 *Te mettre en contact avec moi*

Qu'est-ce que je peux faire pour toi ?"""

# Message quand l'agent ne sait pas répondre
FALLBACK_MESSAGE = """Je n'ai pas la réponse à ta question 🤔

Mais ne t'inquiète pas — je transmets ton message à {business_name} qui te répondra personnellement très vite !

En attendant, tu peux aussi consulter :
👉 https://ton-site.com/faq"""