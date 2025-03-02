from tkinter.scrolledtext import ScrolledText


from .MMWidget import MMWidget, _LongText


class LongTextWidget(MMWidget):
    def __init__(self, master, cinfo_name, label_text=None, width: int = None):
        super(LongTextWidget, self).__init__(master,name=cinfo_name.lower())
        if label_text is None:
            label_text = cinfo_name
        self.set_label(label_text)
        self.default = ""
        self.name = cinfo_name
        # Input
        self.widget_slave = ScrolledText(self)
        self.widget_slave.configure(height='5', width=width)
        self.widget_slave.pack(fill='both', side='top')

        self.widget = _LongText(name=cinfo_name)
        self.widget.linked_text_field = self.widget_slave
