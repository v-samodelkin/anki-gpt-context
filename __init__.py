import sys


from gpt import create_sentence
from settings import FAKE, LIMIT

from aqt.qt import *
from aqt.utils import showInfo

from aqt import mw

def generate_questions(limit=LIMIT) -> None:
  note_count = mw.col.note_count()
  note_ids = mw.col.find_notes(f'''deck:"English from books"''', reverse=True)
  front_list = []
  for note_id in note_ids:
    note = mw.col.get_note(note_id)
    if not note['Question'] or len(note['Question']) < 5:
      limit -= 1
      note['Question'] = create_sentence(note['Front'], fake=FAKE)
      front_list.append(note['Front'])
      mw.col.update_note(note)
    if limit == 0:
      break
  # show a message box
  showInfo("Note count: {}. CQ: {}. Front: {}".format(note_count, len(mw.reviewer.cardQueue), front_list))

def clear_questions() -> None:
  note_count = mw.col.note_count()
  note_ids = mw.col.find_notes(f'''deck:"English from books"''', reverse=True)
  front_list = []
  for note_id in note_ids:
    note = mw.col.get_note(note_id)
    if note['Question']:
      note['Question'] = ''
      mw.col.update_note(note)
  # show a message box
  showInfo("Note count: {}. CQ: {}. Front: {}".format(note_count, len(mw.reviewer.cardQueue), front_list))



regenerate_action = QAction("[GPT] Regenerate questions", mw)
qconnect(regenerate_action.triggered, generate_questions)
mw.form.menuTools.addAction(regenerate_action)

clear_action = QAction("[GPT] Clear questions", mw)
qconnect(clear_action.triggered, clear_questions)
mw.form.menuTools.addAction(clear_action)

