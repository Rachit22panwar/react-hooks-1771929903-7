import tkinter as tk

def process_input():
    id_text = entry_text.get()
    
    try:
        # Try to convert the input to an integer
        input_digit = int(entry_digit.get())
        
        # Process the input
        output_result = f"Input Text: {id_text}\nInput Digit: {input_digit}"
        
    except ValueError:
        output_result = "Please enter a valid digit."
    
    output_box.config(state=tk.NORMAL)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, output_result)
    output_box.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Youtube Summary web page")

# Input text box
label_text = tk.Label(root, text="Input ID:")
label_text.grid(row=0, column=0, padx=10, pady=10)
entry_text = tk.Entry(root, width=30)
entry_text.grid(row=0, column=1, padx=10, pady=10)

# Input digit box
label_digit = tk.Label(root, text="Summary length:")
label_digit.grid(row=1, column=0, padx=10, pady=10)
entry_digit = tk.Entry(root, width=10)
entry_digit.grid(row=1, column=1, padx=10, pady=10)

# Output Box
output_box = tk.Text(root, height=5, width=40, state=tk.DISABLED)
output_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Submit Button
process_button = tk.Button(root, text="Submit", command=process_input)
process_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()