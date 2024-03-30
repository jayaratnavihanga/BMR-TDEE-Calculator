from joblib import load
import numpy as np
import tkinter as tk
from tkinter import ttk

# Load the BMR models
loaded_model_male_bmr = load('trained_model_male_bmr.joblib')
loaded_model_female_bmr = load('trained_model_female_bmr.joblib')

# Function to calculate TDEE
def calculate_tdee():
    # Get user inputs
    gender = gender_var.get()
    weight = float(weight_entry.get())
    activity_lvl = int(activity_var.get()[0])

    # Predict BMR based on gender
    if gender == 'Male':
        predicted_bmr = loaded_model_male_bmr.predict(np.array([[weight]]))
    elif gender == 'Female':
        predicted_bmr = loaded_model_female_bmr.predict(np.array([[weight]]))
    else:
        result_label.config(text="Invalid gender input.")
        return

    # Calculate TDEE based on activity level
    activity_levels = [1.2, 1.375, 1.55, 1.725, 1.9]
    if 1 <= activity_lvl <= 5:
        tdee = predicted_bmr * activity_levels[activity_lvl - 1]
        result_label.config(text=f"Predicted BMR: {predicted_bmr[0]:.2f} kcal\n"
                                 f"Total Daily Energy Expenditure (TDEE): {tdee[0]:.2f} kcal", foreground="green")
    else:
        result_label.config(text="Invalid input for activity level.", foreground="red")

# Create the main window
root = tk.Tk()
root.title("BMR & TDEE Calculator")
root.configure(bg='lightblue')

# Gender selection
gender_label = ttk.Label(root, text="Gender:", background='lightblue')
gender_label.grid(row=0, column=0, padx=5, pady=5)

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"])
gender_combobox.grid(row=0, column=1, padx=5, pady=5)

# Weight input
weight_label = ttk.Label(root, text="Weight (kg):", background='lightblue')
weight_label.grid(row=1, column=0, padx=5, pady=5)

weight_entry = ttk.Entry(root)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

# Activity level selection
activity_label = ttk.Label(root, text="Activity Level:", background='lightblue')
activity_label.grid(row=2, column=0, padx=5, pady=5)

activity_var = tk.StringVar()
activity_combobox = ttk.Combobox(root, textvariable=activity_var, values=["1 - Sedentary",
                                                                          "2 - Lightly active",
                                                                          "3 - Moderately active",
                                                                          "4 - Very active",
                                                                          "5 - Extra active"])
activity_combobox.grid(row=2, column=1, padx=5, pady=5)

# Button to calculate TDEE
calculate_button = ttk.Button(root, text="Calculate", command=calculate_tdee)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Label to display result
result_label = ttk.Label(root, text="", background='lightblue')
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()

