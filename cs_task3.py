import tkinter as tk
import re

def check_password_strength():
    password = entry.get()
    strength = 0
    feedback_list = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback_list.append("❌ At least 8 characters")

    # Check lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback_list.append("❌ Add lowercase letter")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback_list.append("❌ Add uppercase letter")

    # Check digit
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback_list.append("❌ Add a number")

    # Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\\[\]`~;']", password):
        strength += 1
    else:
        feedback_list.append("❌ Add special character")

    # Determine overall strength
    if strength <= 2:
        result = "Strength: Weak 💡"
        color = "red"
    elif strength == 3 or strength == 4:
        result = "Strength: Medium ⚠️"
        color = "orange"
    else:
        result = "Strength: Strong ✅"
        color = "green"

    # Update label
    strength_label.config(text=result, fg=color)

    # Show feedback
    tips_text.delete(1.0, tk.END)
    if feedback_list:
        tips_text.insert(tk.END, "\n".join(feedback_list))
    else:
        tips_text.insert(tk.END, "✅ Good job! Your password looks strong.")

# --- GUI setup ---
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x300")
root.resizable(False, False)

# Entry
tk.Label(root, text="Enter password:").pack(pady=10)
entry = tk.Entry(root, width=30, show="*")
entry.pack()

# Button
tk.Button(root, text="Check Strength", command=check_password_strength).pack(pady=10)

# Result label
strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack()

# Tips text box
tips_text = tk.Text(root, height=6, width=45)
tips_text.pack(pady=10)

root.mainloop()
