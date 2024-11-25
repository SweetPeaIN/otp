import tkinter as tk
import cryptAlgo  # Import cryptographic functions from cryptAlgo.py

# Define colors and styles for UI refinement
BG_COLOR = "#2b2b2b"  # Background color for frames
TEXT_COLOR = "#ffffff"  # Text color
BUTTON_COLOR = "#3c3f41"  # Button background color
BUTTON_HOVER_COLOR = "#5c5f61"  # Button hover color
INPUT_BG_COLOR = "#3c3f41"  # Input/output background color
FONT_NAME = "Helvetica"  # Font for labels and buttons

# Initialize the root Tkinter window
root = tk.Tk()
root.title("Encryption Tool")
root.geometry("1000x700")
root.configure(bg=BG_COLOR)

# Define mode variable AFTER initializing root
mode = tk.StringVar(value="Encryption")

# Helper functions for one-time pad encryption and decryption
def toggle_mode():
    clear()  # Clear all fields when switching modes

    if mode.get() == "Encryption":
        mode.set("Decryption")
        toggle_button.config(text="Switch to Encryption")
        encrypt_button.grid_remove()
        decrypt_button.grid()
        generate_key_button.grid_remove()
        key_label.config(text="Enter Key")
        key_output_field.config(state="normal")
    else:
        mode.set("Encryption")
        toggle_button.config(text="Switch to Decryption")
        decrypt_button.grid_remove()
        encrypt_button.grid()
        generate_key_button.grid()
        key_label.config(text="Generated Key")
        key_output_field.config(state="readonly")

def generate_key():
    input_text = input_field.get()
    if not input_text:
        key_output_field.config(state="normal")
        key_output_field.delete(0, tk.END)
        key_output_field.insert(0, "Input is empty, please enter text.")
        key_output_field.config(state="readonly")
        return

    key = cryptAlgo.generate_random_key(len(input_text))
    key_output_field.config(state="normal")
    key_output_field.delete(0, tk.END)
    key_output_field.insert(0, key.hex())
    key_output_field.config(state="readonly")
    encrypt_button.config(state="normal")

def encrypt():
    input_text = input_field.get()
    key_hex = key_output_field.get()

    # Ensure input and key lengths match
    if len(input_text) != len(bytes.fromhex(key_hex)):
        output_field.config(state="normal")
        output_field.delete(1.0, tk.END)
        output_field.insert(tk.END, "Error: Key length must match input length.")
        output_field.config(state="disabled")
        return

    encrypted_text_hex = cryptAlgo.encrypt(input_text, bytes.fromhex(key_hex))

    # Display the encrypted text
    output_field.config(state="normal")
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, f"\n{encrypted_text_hex}")
    output_field.config(state="disabled")

def decrypt():
    input_text = input_field.get()
    key_hex = key_output_field.get()

    try:
        decrypted_text = cryptAlgo.decrypt(input_text, bytes.fromhex(key_hex))
    except ValueError:
        output_field.config(state="normal")
        output_field.delete(1.0, tk.END)
        output_field.insert(tk.END, "Error: Invalid ciphertext format.")
        output_field.config(state="disabled")
        return

    # Display the decrypted text
    output_field.config(state="normal")
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, f"=\n{decrypted_text}")
    output_field.config(state="disabled")

def clear():
    input_field.delete(1.0, tk.END)

    key_output_field.config(state="normal")
    key_output_field.delete(0, tk.END)
    key_output_field.config(state="readonly")
    output_field.config(state="normal")
    output_field.delete(1.0, tk.END)
    output_field.config(state="disabled")
    encrypt_button.config(state="disabled")

def on_enter(e):
    e.widget['background'] = BUTTON_HOVER_COLOR

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

# Add a function to handle closing the window
def on_closing():
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Title Bar
title_bar = tk.Label(root, text="Encryption Tool", font=("Helvetica", 24, "bold"), bg=BG_COLOR, fg=TEXT_COLOR, pady=20)
title_bar.pack(fill="x")

# Toggle Mode Button with Increased Font and Size
toggle_button = tk.Button(root, text="Switch to Decryption", font=("Helvetica", 16), bg=BUTTON_COLOR,
                          fg=TEXT_COLOR, command=toggle_mode, width=20, height=2)
toggle_button.pack(pady=10)
toggle_button.bind("<Enter>", on_enter)
toggle_button.bind("<Leave>", on_leave)

# Input Frame
input_frame = tk.Frame(root, bg=BG_COLOR)
input_frame.pack(fill="both", padx=20, pady=10, expand=True)
input_label = tk.Label(input_frame, text="Input Text", font=("Helvetica", 16), bg=BG_COLOR, fg=TEXT_COLOR)
input_label.grid(row=0, column=0, sticky="w", padx=5)

# Using Text widget instead of Entry to allow for "height" adjustments
input_field = tk.Text(input_frame, font=("Helvetica", 16), width=80, height=5, bg=INPUT_BG_COLOR, fg=TEXT_COLOR,
                      insertbackground=TEXT_COLOR)
input_field.grid(row=0, column=1, padx=10, pady=5)  # Adjust padding for better layout

# Key Generation and Output Frame
key_frame = tk.Frame(root, bg=BG_COLOR)
key_frame.pack(fill="both", padx=20, pady=10, expand=True)
generate_key_button = tk.Button(key_frame, text="Generate Random Key", font=("Helvetica", 14), bg=BUTTON_COLOR,
                                fg=TEXT_COLOR, command=generate_key, width=20, height=2)
generate_key_button.grid(row=0, column=0, padx=5)
key_label = tk.Label(key_frame, text="Generated Key", font=("Helvetica", 16), bg=BG_COLOR, fg=TEXT_COLOR)
key_label.grid(row=0, column=1, padx=5, sticky="w")
key_output_field = tk.Entry(key_frame, font=("Helvetica", 16), width=60, state="readonly", bg=INPUT_BG_COLOR,
                            fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
key_output_field.grid(row=0, column=2, padx=10)

generate_key_button.bind("<Enter>", on_enter)
generate_key_button.bind("<Leave>", on_leave)

# Action Buttons Frame (Centered Buttons)
action_frame = tk.Frame(root, bg=BG_COLOR)
action_frame.pack(pady=15, padx=20, fill="both", expand=True)

# Define the buttons and set them up in the grid layout
encrypt_button = tk.Button(action_frame, text="Encrypt", font=("Helvetica", 14), bg=BUTTON_COLOR, fg=TEXT_COLOR,
                           command=encrypt, state="disabled", width=15, height=2)
decrypt_button = tk.Button(action_frame, text="Decrypt", font=("Helvetica", 14), bg=BUTTON_COLOR, fg=TEXT_COLOR,
                           command=decrypt, width=15, height=2)
clear_button = tk.Button(action_frame, text="Clear", font=("Helvetica", 14), bg=BUTTON_COLOR, fg=TEXT_COLOR,
                         command=clear, width=15, height=2)

# Using columnspan to center the buttons in the grid
encrypt_button.grid(row=0, column=0, padx=10, pady=10)
decrypt_button.grid(row=0, column=1, padx=10, pady=10)
clear_button.grid(row=0, column=2, padx=10, pady=10)

# Center the frame content itself using grid configuration
action_frame.grid_columnconfigure(0, weight=1)
action_frame.grid_columnconfigure(1, weight=1)
action_frame.grid_columnconfigure(2, weight=1)

# Bind the button hover effects
for button in [encrypt_button, decrypt_button, clear_button]:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Output Field Frame with Increased Size
output_frame = tk.Frame(root, bg=BG_COLOR)
output_frame.pack(fill="both", padx=20, pady=10, expand=True)
output_label = tk.Label(output_frame, text="Output Text", font=("Helvetica", 16), bg=BG_COLOR, fg=TEXT_COLOR)
output_label.grid(row=0, column=0, sticky="w", padx=5)
output_field = tk.Text(output_frame, font=("Helvetica", 16), width=80, height=5, state="disabled", bg=INPUT_BG_COLOR,
                       fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
output_field.grid(row=0, column=1, padx=10)

# Initialize the mode to set button visibility
toggle_mode()

root.mainloop()
