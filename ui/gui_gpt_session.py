from typing import Optional
import PySide6.QtCore
import PySide6.QtGui
from ui.design.Ui_gpt_session_select_window import Ui_gpt_session_select
from ui.design.Ui_gpt_session_show import Ui_gpt_show_session
from PySide6.QtWidgets import QMainWindow, QWidget
from gpt.loader import display_history_sessions, load_messages

class GPTShowSession(QWidget, Ui_gpt_show_session):
    def __init__(self,) -> None:
        super().__init__()
        self.setupUi(self)


class GPTSessionSelect(QWidget, Ui_gpt_session_select):

    def __init__(self, parent) -> None:
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.listWidget.addItems(display_history_sessions())
        self._bind_btns()
        self.show_window = GPTShowSession()

    def _bind_btns(self):

        def confirm_btn_callback():
            session = self.listWidget.currentItem().text()
            self.parent.set_session(session)
            self.close()

        self.confirm_btn.clicked.connect(confirm_btn_callback)

        self.cancel_btn.clicked.connect(self.close)

        def view_btn_callback():
            message = load_messages(self.listWidget.currentItem().text())
            self.show_window.show()
            for msg in message:
                self.show_window.textBrowser.append(msg.type + ":" + msg.content + '\n')
        
        self.view_btn.clicked.connect(view_btn_callback)

    def closeEvent(self, event) -> None:
        self.show_window.close()