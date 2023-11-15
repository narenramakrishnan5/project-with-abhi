import tkinter as tk
from PIL import Image

def screen():
    
    ws.destroy()
    display_text()
# Function to display the entered text in a new window
def display_text():
    
    ws = tk.Tk()
    
    
    # Get the screen width and height
    screen_width = ws.winfo_screenwidth()
    screen_height = ws.winfo_screenheight()

    ws.title('PythonGuides')

    # Set the dimensions to match the screen resolution
    ws.geometry(f"{screen_width}x{screen_height}")

    try:
        # Open the image
        img = Image.open("C://Users//nsampathkuma//Desktop//Project_w_abhi//background.png")  # Replace with the correct image file name and path

        # Save the image in PNG format
        img.save("background.png", "PNG")

        img = tk.PhotoImage(file="background.png")
        ws.geometry(f"{img.width()}x{img.height()}")
        label = tk.Label(ws, image=img)
        label.place(x=0, y=0)
    except tk.TclError as e:
        print("Error loading the image:", str(e))

    # Create a text box

    text = tk.Text(ws, height=1, width=10)
    text.place(x=50, y=10)

    # Create a button to display the entered text
    button = tk.Button(ws, text='SEND', relief=tk.RAISED, font=('Arial Bold', 10), command=display_text)
    button.place(x=50, y=40)
    ws.mainloop()
    return None


def open():
   print("hi") 

ws = tk.Tk()

# Get the screen width and height
"""""screen_width = ws.winfo_screenwidth()
""""""""screen_height = ws.winfo_screenheight()"""

ws.title('PythonGuides')

# Set the dimensions to match the screen resolution
ws.attributes('-fullscreen', True)

try:
    # Open the image
    img = Image.open("C://Users//nsampathkuma//Desktop//Project_w_abhi//book.JPG",mode="r")  # Replace with the correct image file name and path

    # Save the image in PNG format
    img.save("background.png", "PNG")
    
    img = tk.PhotoImage(file="background.png")
    ws.geometry(f"{img.width()}x{img.height()}")
    img = img.zoom(2, 2)
   # mg = img.resize((34, 26), Image.ANTIALIAS)
   # resize_image = img.resize((1000, 1000))
    label = tk.Label(ws, image=img)
    label.place(x=0, y=0)
except tk.TclError as e:
    print("Error loading the image:", str(e))

# Create a text box

text = tk.Text(ws, height=20, width=20)
text.place(x=600, y=500)

# Create a button to display the entered text
button = tk.Button(ws, text='SEND', relief=tk.RAISED, font=('Arial Bold', 20), command=screen)
button.place(x=700, y=500)

ws.mainloop()