from pywinauto.application import Application
app = Application().connect(title_re="Google Translate - Chromium", class_name="Chromium")