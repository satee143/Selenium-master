import time

from pywinauto.application import Application
app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("Help->About Notepad")
time.sleep(5)
app.AboutNotepad.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)