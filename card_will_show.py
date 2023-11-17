from aqt import mw
from anki.cards import Card

def add_debug_line(text: str, card: Card, kind: str):
  last_card = mw.reviewer.lastCard()
  prev_front = last_card.note()['Front'] if last_card else 'no note'
  return text + '<br>[kind: {kind}. front: {front}. back: {back}. prev_front: {prev_front}]: {question}'.format(kind=kind, front=card.note()['Front'], back=card.note()['Back'], prev_front=prev_front, question="request(text)")

gui_hooks.card_will_show.append(add_debug_line)
