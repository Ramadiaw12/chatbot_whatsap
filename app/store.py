"""
store.py — Stockage en mémoire des historiques de conversation.
Pour la prod, remplace par Redis ou une base SQLite.
"""

from collections import defaultdict

# { phone_number: [{"role": "user"|"assistant", "content": "..."}] }
_conversations: dict[str, list[dict]] = defaultdict(list)
_known_contacts: set[str] = set()

MAX_HISTORY = 10  # nombre de messages gardés en mémoire par contact


def is_new_contact(phone: str) -> bool:
    return phone not in _known_contacts


def register_contact(phone: str) -> None:
    _known_contacts.add(phone)


def add_message(phone: str, role: str, content: str) -> None:
    history = _conversations[phone]
    history.append({"role": role, "content": content})
    # Garde seulement les N derniers messages
    if len(history) > MAX_HISTORY:
        _conversations[phone] = history[-MAX_HISTORY:]


def get_history(phone: str) -> list[dict]:
    return list(_conversations[phone])


def clear_history(phone: str) -> None:
    _conversations[phone] = []