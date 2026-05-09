"""
agent.py — Cerveau de l'agent : utilise Claude pour matcher FAQ/produits
et générer une réponse naturelle.
"""

import json
import os
from openai import OpenAI
from app.catalog import (
    BUSINESS_NAME,
    PRODUCTS,
    FAQ,
    WELCOME_MESSAGE,
    FALLBACK_MESSAGE,
)


client = ChatGroq(
    model="llama-3.3-70b-versatile",  # or "mixtral-8x7b-32768"
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)

# Prépare le catalogue sous forme de texte pour le prompt
def _build_catalog_text() -> str:
    products_str = "\n".join(
        f"- {p['name']} ({p['price']}) : {p['description']} → {p['link']}"
        for p in PRODUCTS
    )
    faq_str = "\n".join(
        f"Q: {f['question']}\nR: {f['answer']}"
        for f in FAQ
    )
    return f"""=== PRODUITS ===
{products_str}

=== FAQ ===
{faq_str}"""


SYSTEM_PROMPT = f"""Tu es l'assistant WhatsApp de "{BUSINESS_NAME}".
Ton rôle : répondre aux messages des followers de manière courte, chaleureuse et naturelle.

RÈGLES STRICTES :
1. Réponds UNIQUEMENT en te basant sur le catalogue ci-dessous.
2. Si la question concerne un produit, donne le nom, le prix, et le lien.
3. Si c'est une FAQ, utilise la réponse prévue (tu peux légèrement reformuler).
4. Si tu ne sais pas, réponds avec exactement ce JSON : {{"fallback": true}}
5. Garde tes réponses courtes (3-5 lignes max), WhatsApp n'est pas un blog.
6. Utilise des emojis avec parcimonie (1-2 max par message).
7. Ne réponds JAMAIS en dehors du catalogue — pas d'inventions, pas de prix fictifs.
8. Réponds toujours dans la langue du message reçu.

{_build_catalog_text()}
"""


def get_reply(user_message: str, conversation_history: list[dict]) -> str:
    """
    Génère une réponse à partir du message utilisateur.
    conversation_history : liste de {"role": "user"|"assistant", "content": "..."}
    """
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history + [{"role": "user", "content": user_message}]

    response = client.chat.completions.create(
        model="grok-3-fast",
        max_tokens=512,
        messages=messages,
    )

    reply_text = response.choices[0].message.content.strip()

    # Vérifie si l'agent indique un fallback
    try:
        parsed = json.loads(reply_text)
        if parsed.get("fallback"):
            return FALLBACK_MESSAGE.format(business_name=BUSINESS_NAME)
    except (json.JSONDecodeError, AttributeError):
        pass

    return reply_text


def get_welcome() -> str:
    return WELCOME_MESSAGE.format(business_name=BUSINESS_NAME)