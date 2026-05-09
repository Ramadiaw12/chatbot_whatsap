"""
main.py — Webhook FastAPI pour la Meta WhatsApp Cloud API.
"""

import os
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv

load_dotenv()

from app import agent, store, whatsapp  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "mon_token_secret")


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("🚀 WhatsApp Agent démarré")
    yield
    log.info("Agent arrêté")


app = FastAPI(title="WhatsApp Agent", lifespan=lifespan)


# ── Vérification du webhook (Meta l'appelle une fois lors de la config) ──────

@app.get("/webhook")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        log.info("✅ Webhook vérifié par Meta")
        return PlainTextResponse(hub_challenge)
    raise HTTPException(status_code=403, detail="Token invalide")


# ── Réception des messages entrants ─────────────────────────────────────────

@app.post("/webhook")
async def receive_message(request: Request):
    body = await request.json()

    # Parcourt la structure Meta
    for entry in body.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            messages = value.get("messages", [])

            for msg in messages:
                if msg.get("type") != "text":
                    continue  # ignore images, stickers, etc. pour l'instant

                phone = msg["from"]
                text = msg["text"]["body"]
                msg_id = msg["id"]

                log.info(f"📩 Message de {phone}: {text[:60]}")

                # Double coche bleue (marquer comme lu)
                await whatsapp.mark_as_read(msg_id)

                # Message de bienvenue si nouveau contact
                if store.is_new_contact(phone):
                    store.register_contact(phone)
                    welcome = agent.get_welcome()
                    await whatsapp.send_text(phone, welcome)
                    store.add_message(phone, "assistant", welcome)

                # Génère la réponse de l'agent
                history = store.get_history(phone)
                store.add_message(phone, "user", text)

                reply = agent.get_reply(text, history)
                await whatsapp.send_text(phone, reply)
                store.add_message(phone, "assistant", reply)

                log.info(f"📤 Réponse à {phone}: {reply[:60]}")

    return {"status": "ok"}


# ── Health check ─────────────────────────────────────────────────────────────

@app.get("/health")
async def health():
    return {"status": "ok", "agent": "WhatsApp Agent"}