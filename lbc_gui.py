import tkinter
import lbc


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        self.title("Little Ben Computer")

        self.source_frame = tkinter.Text(self)
        self.source_frame.grid(row=0, column=0)
        self.source_field = tkinter.Text(self.source_frame, width=30, height=25)
        self.source_field.grid(row=0, column=0)
        self.source_scroll = tkinter.Scrollbar(self.source_frame)#, fill=tkinter.Y)
        self.source_scroll.grid(row=0, column=1, sticky="ns")
        self.source_field.config(yscrollcommand=self.source_scroll.set)
        self.source_scroll.config(command=self.source_field.yview)

        self.registers_frame = tkinter.LabelFrame(self, text="Registers")
        self.registers_frame.grid(row=0, column=1)
        self.accumulator_label = tkinter.Label(self.registers_frame, text="Accumulator")
        self.accumulator_label.grid(row=0, column=0)
        self.accumulator_output = tkinter.Text(self.registers_frame, width=8, height=1)
        self.accumulator_output.grid(row=0, column=1)
        self.pc_label = tkinter.Label(self.registers_frame, text="Program Counter")
        self.pc_label.grid(row=1, column=0)
        self.pc_output = tkinter.Text(self.registers_frame, width=8, height=1)
        self.pc_output.grid(row=1, column=0)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()