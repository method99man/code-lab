from tkinter import *
import wikipedia
import ttkbootstrap as ttk
from ttkbootstrap import Style

"""
    Delete/Add 'ttk.{element}' to change style of elements.
"""

# Window initialization
window = Tk()

# Styling window
style = Style(theme='darkly')   # comment to turn off theme
window.geometry("800x400")
window.title("Python Wikipedia")

def searchWiki():
    try:
        query = searchInput.get()
        result = wikipedia.summary(query, sentences=10)
        resultBox.config(state=ttk.NORMAL)    # Enable editing
        resultBox.delete('1.0', END)
        resultBox.insert('1.0', result)
        resultBox.config(state=ttk.DISABLED)  # Disable after inserting

    except Exception:
        resultBox.config(state=ttk.NORMAL)    # Enable editing
        resultBox.delete('1.0', END)
        resultBox.insert('1.0', 'No results found')
        resultBox.config(state=ttk.DISABLED)  # Disable after inserting


# GUI elements
header = ttk.Label(window, text = 'Python Wikipedia', font = ("Arial", 20))
header.pack(pady = 5)

searchInput = ttk.Entry(window, width = 50, justify = "center")
searchInput.pack(pady = 5)

search_btn = ttk.Button(window, text = 'Search', command = searchWiki)
search_btn.pack(pady = 5)

resultBox = ttk.Text(window, width = 1000, height = 1000, border = 0, font = ("Arial", 12))
resultBox.config(state=ttk.DISABLED)  # Disable editing text resultBox
resultBox.pack(padx = 15, pady = 15)

# Main loop
window.mainloop()