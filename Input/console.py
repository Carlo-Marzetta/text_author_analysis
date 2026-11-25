import code
import contextlib
import io
import tkinter as tk


class Console:
    def __init__(self, parent):
        self.interpreter = code.InteractiveConsole()
        self.more = False

        self.frame = tk.Frame(parent, padx=10, pady=10)
        self.output = tk.Text(self.frame, state="disabled", wrap="word")
        self.output.pack(expand=True, fill="both")

        self.command = tk.Entry(self.frame)
        self.command.pack(fill="x")
        self.command.bind("<Return>", self.runCommand)

    def runCommand(self, event=None):
        command = self.command.get()
        self.command.delete(0, tk.END)

        prompt = "... " if self.more else ">>> "
        self.output.configure(state="normal")
        self.output.insert(tk.END, f"{prompt}{command}\n")

        captured = io.StringIO()
        with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
            self.more = self.interpreter.push(command)

        self.output.insert(tk.END, captured.getvalue())
        self.output.see(tk.END)
        self.output.configure(state="disabled")
        return "break"
