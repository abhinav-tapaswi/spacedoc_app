#importing library
import tkinter as tk
from tkinter import ttk, font, Listbox, Scrollbar, messagebox
from PIL import ImageTk, Image 
import time
from joblib import load
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np
from ttkthemes import ThemedStyle
w=tk.Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar
disease_symptoms = {'(vertigo) Paroymsal  Positional Vertigo': ['nausea',
  'loss_of_balance',
  'unsteadiness',
  'spinning_movements',
  'vomiting',
  'headache'],
 'AIDS': ['high_fever',
  'patches_in_throat',
  'extra_marital_contacts',
  'muscle_wasting'],
 'Acne': ['skin_rash', 'scurring', 'pus_filled_pimples', 'blackheads'],
 'Alcoholic hepatitis': ['distention_of_abdomen',
  'history_of_alcohol_consumption',
  'fluid_overload',
  'yellowish_skin',
  'swelling_of_stomach',
  'vomiting',
  'abdominal_pain'],
 'Allergy': ['shivering',
  'watering_from_eyes',
  'continuous_sneezing',
  'chills'],
 'Arthritis': ['movement_stiffness',
  'painful_walking',
  'swelling_joints',
  'muscle_weakness',
  'stiff_neck'],
 'Bronchial Asthma': ['high_fever',
  'family_history',
  'fatigue',
  'cough',
  'mucoid_sputum',
  'breathlessness'],
 'Cervical spondylosis': ['back_pain',
  'neck_pain',
  'loss_of_balance',
  'dizziness',
  'weakness_in_limbs'],
 'Chicken pox': ['loss_of_appetite',
  'itching',
  'high_fever',
  'skin_rash',
  'lethargy',
  'swelled_lymph_nodes',
  'fatigue',
  'malaise',
  'headache',
  'red_spots_over_body',
  'mild_fever'],
 'Chronic cholestasis': ['loss_of_appetite',
  'itching',
  'nausea',
  'yellowish_skin',
  'vomiting',
  'yellowing_of_eyes',
  'abdominal_pain'],
 'Common Cold': ['muscle_pain',
  'high_fever',
  'congestion',
  'redness_of_eyes',
  'loss_of_smell',
  'continuous_sneezing',
  'swelled_lymph_nodes',
  'fatigue',
  'cough',
  'malaise',
  'throat_irritation',
  'sinus_pressure',
  'chest_pain',
  'headache',
  'phlegm',
  'runny_nose',
  'chills'],
 'Dengue': ['loss_of_appetite',
  'joint_pain',
  'skin_rash',
  'high_fever',
  'nausea',
  'back_pain',
  'muscle_pain',
  'pain_behind_the_eyes',
  'fatigue',
  'malaise',
  'vomiting',
  'headache',
  'red_spots_over_body',
  'chills'],
 'Diabetes ': ['polyuria',
  'excessive_hunger',
  'lethargy',
  'irregular_sugar_level',
  'increased_appetite',
  'fatigue',
  'weight_loss',
  'blurred_and_distorted_vision',
  'obesity',
  'restlessness'],
 'Dimorphic hemmorhoids(piles)': ['pain_during_bowel_movements',
  'bloody_stool',
  'pain_in_anal_region',
  'irritation_in_anus',
  'constipation'],
 'Drug Reaction': ['itching',
  'skin_rash',
  'spotting_urination',
  'stomach_pain',
  'burning_micturition'],
 'Fungal infection': ['itching',
  'skin_rash',
  'nodal_skin_eruptions',
  'dischromic_patches'],
 'GERD': ['cough',
  'chest_pain',
  'stomach_pain',
  'vomiting',
  'ulcers_on_tongue',
  'acidity'],
 'Gastroenteritis': ['sunken_eyes',
  'vomiting',
  'dehydration',
  'diarrhoea'],
 'Heart attack': ['chest_pain', 'vomiting', 'sweating', 'breathlessness'],
 'Hepatitis B': ['loss_of_appetite',
  'itching',
  'lethargy',
  'fatigue',
  'receiving_unsterile_injections',
  'yellowish_skin',
  'malaise',
  'yellowing_of_eyes',
  'dark_urine',
  'yellow_urine',
  'abdominal_pain',
  'receiving_blood_transfusion'],
 'Hepatitis C': ['loss_of_appetite',
  'nausea',
  'family_history',
  'fatigue',
  'yellowish_skin',
  'yellowing_of_eyes'],
 'Hepatitis D': ['loss_of_appetite',
  'joint_pain',
  'nausea',
  'fatigue',
  'yellowish_skin',
  'vomiting',
  'yellowing_of_eyes',
  'dark_urine',
  'abdominal_pain'],
 'Hepatitis E': ['loss_of_appetite',
  'joint_pain',
  'high_fever',
  'nausea',
  'fatigue',
  'yellowish_skin',
  'vomiting',
  'yellowing_of_eyes',
  'dark_urine',
  'coma',
  'abdominal_pain',
  'stomach_bleeding',
  'acute_liver_failure'],
 'Hypertension': ['lack_of_concentration',
  'loss_of_balance',
  'chest_pain',
  'dizziness',
  'headache'],
 'Hyperthyroidism': ['excessive_hunger',
  'irritability',
  'fatigue',
  'weight_loss',
  'sweating',
  'fast_heart_rate',
  'abnormal_menstruation',
  'muscle_weakness',
  'restlessness',
  'diarrhoea',
  'mood_swings'],
 'Hypoglycemia': ['excessive_hunger',
  'nausea',
  'drying_and_tingling_lips',
  'fatigue',
  'palpitations',
  'slurred_speech',
  'vomiting',
  'anxiety',
  'blurred_and_distorted_vision',
  'headache',
  'sweating',
  'irritability'],
 'Hypothyroidism': ['weight_gain',
  'lethargy',
  'cold_hands_and_feets',
  'brittle_nails',
  'fatigue',
  'enlarged_thyroid',
  'depression',
  'puffy_face_and_eyes',
  'swollen_extremeties',
  'dizziness',
  'abnormal_menstruation',
  'irritability',
  'mood_swings'],
 'Impetigo': ['skin_rash',
  'high_fever',
  'blister',
  'red_sore_around_nose',
  'yellow_crust_ooze'],
 'Jaundice': ['itching',
  'high_fever',
  'fatigue',
  'weight_loss',
  'yellowish_skin',
  'vomiting',
  'dark_urine',
  'abdominal_pain'],
 'Malaria': ['muscle_pain',
  'high_fever',
  'nausea',
  'vomiting',
  'headache',
  'sweating',
  'diarrhoea',
  'chills'],
 'Migraine': ['excessive_hunger',
  'visual_disturbances',
  'depression',
  'blurred_and_distorted_vision',
  'headache',
  'acidity',
  'irritability',
  'stiff_neck',
  'indigestion'],
 'Osteoarthristis': ['joint_pain',
  'neck_pain',
  'hip_joint_pain',
  'knee_pain',
  'painful_walking',
  'swelling_joints'],
 'Paralysis (brain hemorrhage)': ['altered_sensorium',
  'weakness_of_one_body_side',
  'vomiting',
  'headache'],
 'Peptic ulcer diseae': ['loss_of_appetite',
  'vomiting',
  'passage_of_gases',
  'abdominal_pain',
  'internal_itching',
  'indigestion'],
 'Pneumonia': ['high_fever',
  'fatigue',
  'cough',
  'malaise',
  'chest_pain',
  'phlegm',
  'rusty_sputum',
  'sweating',
  'fast_heart_rate',
  'breathlessness',
  'chills'],
 'Psoriasis': ['joint_pain',
  'skin_rash',
  'silver_like_dusting',
  'skin_peeling',
  'small_dents_in_nails',
  'inflammatory_nails'],
 'Tuberculosis': ['loss_of_appetite',
  'high_fever',
  'swelled_lymph_nodes',
  'fatigue',
  'weight_loss',
  'cough',
  'malaise',
  'chest_pain',
  'vomiting',
  'yellowing_of_eyes',
  'phlegm',
  'sweating',
  'blood_in_sputum',
  'breathlessness',
  'mild_fever',
  'chills'],
 'Typhoid': ['high_fever',
  'nausea',
  'fatigue',
  'diarrhoea',
  'belly_pain',
  'vomiting',
  'toxic_look_(typhos)',
  'headache',
  'abdominal_pain',
  'constipation',
  'chills'],
 'Urinary tract infection': ['continuous_feel_of_urine',
  'bladder_discomfort',
  'foul_smell_of urine',
  'burning_micturition'],
 'Varicose veins': ['prominent_veins_on_calf',
  'swollen_legs',
  'swollen_blood_vessels',
  'fatigue',
  'cramps',
  'bruising',
  'obesity'],
 'hepatitis A': ['loss_of_appetite',
  'joint_pain',
  'muscle_pain',
  'nausea',
  'yellowish_skin',
  'mild_fever',
  'vomiting',
  'yellowing_of_eyes',
  'dark_urine',
  'abdominal_pain',
  'diarrhoea']}

# Define a dictionary of medicines for each disease
disease_medicines = {
    "Fungal infection": ["econazole", "clotrimazole (Canesten)"],
    "Acne": ["tretinoin", "tazarotene"],
    "Psoriasis": ["Methotrexate", "cyclosporine"],
    "Impetigo": ["dicloxaci llin", "cephalexin"],
    "hepatitis A": [ 'acetaminophen','paracetamo'],
    "Hepatitis B": ['entecavir (Baraclude)', 'tenofovir (Viread)'],
    "Hepatitis C": ['Elbasvir-Grazoprevir (Zepatier) ','Glecaprevir-Pibrentasvir (Mavyret)'],
    "Hepatitis D": ["Pegylated interferon alpha"],
    "Hepatitis E": ["interferon", "ribavirin"],
    "Alcoholic hepatitis": ["Corticosteroids", "Pentoxifylline"],
    "GERD": ['esomeprazole (Nexium)', 'lansoprazole (Prevacid)'],
    "Chronic cholestasis": ["ursodiol"],
    "Peptic ulcer diseae": ["omeprazole (Prilosec)","lansoprazole (Prevacid)"],
    "Gastroenteritis": ['operamide link (Imodium)','bismuth subsalicylate link'],
    "Jaundice": ['Iron supplements','Antihistamines'],
    "Tuberculosis": ['Rifampin', 'isoniazid'],
    "Bronchial Asthma": ['malizumab (Xolair)','mepolizumab (Nucala)'],
    "Common Cold": ['oxymetazoline nasal', 'phenylephrine nasal'],
    "AIDS": ["Abacavir", "Emtricitabine"],
    "Hypertension": ["Doxazosin", "Propranolol"],
    "Malaria": ["Doxycycline", "Mefloquine"],
    "Chicken pox": ["Acyclovir", "Valacyclovir"],
    "Dengue": ["Pain Relievers", "Acetaminophen "],
    "Typhoid": ["Ciprofloxacin", "Azithromycin"],
    "Pneumonia": ["Penicillins", "Tetracyclines"],
    "Dimorphic hemmorhoids(piles)": ["Pain Relievers", "Fiber Supplements"],
    "Heart attack": ["Aspirin", "Nitroglycerin"],
    "Hypothyroidism": ["Liothyronine (T3)", "Desiccated Thyroid Extract"],
    "Hyperthyroidism": ["Methimazole (Tapazole)", "Radioactive Iodine (I-131)"],
    "Hypoglycemia": ["Glucagon", "Dextrose (IV)"],
    "Diabetes": ["Insulin for type 1", "Metformin (Glucophage) for type 2"],
    "Arthritis": ["Celecoxib (Celebrex)", "Diclofenac (Voltaren)"],
    "(vertigo) Paroymsal Positional Vertigo": ["Metoclopramide (Reglan)", "Diazepam (Valium)"],
    "Urinary Tract Infection": ["Levofloxacin (Levaquin)", "Fosfomycin (Monurol)"],
    "Allergy": ["Anticholinergic Nasal Spray", "Antibiotics "],
    "Drug Reaction": ["Epinephrine", "Bronchodilators "],
    "Migraine": ["Antidepressants", "Metoclopramide (Reglan) "],
    "Paralysis (brain hemorrhage)": ["Antiplatelet Agents ", "Blood Pressure Medications"],
    "Cervical spondylosis": ["Heat and Cold Therapy", "Pain Relief Medications"],
    "Osteoarthristis": ["Corticosteroids", "Hyaluronic Acid Injections"]
}
class DiseasetoDoctor:
    def findDoc(self, *symps):
        model = load('symptoms-disease_model.joblib')
        lis = MultiLabelBinarizer(classes=['abdominal_pain', 'abnormal_menstruation', 'acidity',
                                           'acute_liver_failure', 'altered_sensorium', 'anxiety',
                                           'back_pain', 'belly_pain', 'blackheads', 'bladder_discomfort',
                                           'blister', 'blood_in_sputum', 'bloody_stool',
                                           'blurred_and_distorted_vision', 'breathlessness',
                                           'brittle_nails', 'bruising', 'burning_micturition',
                                           'chest_pain', 'chills', 'cold_hands_and_feets', 'coma',
                                           'congestion', 'constipation', 'continuous_feel_of_urine',
                                           'continuous_sneezing', 'cough', 'cramps', 'dark_urine',
                                           'dehydration', 'depression', 'diarrhoea',
                                           'dischromic_patches', 'distention_of_abdomen', 'dizziness',
                                           'drying_and_tingling_lips', 'enlarged_thyroid',
                                           'excessive_hunger', 'extra_marital_contacts', 'family_history',
                                           'fast_heart_rate', 'fatigue', 'fluid_overload',
                                           'foul_smell_of urine', 'headache', 'high_fever',
                                           'hip_joint_pain', 'history_of_alcohol_consumption',
                                           'increased_appetite', 'indigestion', 'inflammatory_nails',
                                           'internal_itching', 'irregular_sugar_level', 'irritability',
                                           'irritation_in_anus', 'joint_pain', 'knee_pain',
                                           'lack_of_concentration', 'lethargy', 'loss_of_appetite',
                                           'loss_of_balance', 'loss_of_smell', 'malaise', 'mild_fever',
                                           'mood_swings', 'movement_stiffness', 'mucoid_sputum',
                                           'muscle_pain', 'muscle_wasting', 'muscle_weakness', 'nausea',
                                           'neck_pain', 'nodal_skin_eruptions', 'obesity',
                                           'pain_behind_the_eyes', 'pain_during_bowel_movements',
                                           'pain_in_anal_region', 'painful_walking', 'palpitations',
                                           'passage_of_gases', 'patches_in_throat', 'phlegm', 'polyuria',
                                           'prominent_veins_on_calf', 'puffy_face_and_eyes',
                                           'pus_filled_pimples', 'receiving_blood_transfusion',
                                           'receiving_unsterile_injections', 'red_sore_around_nose',
                                           'red_spots_over_body', 'redness_of_eyes', 'restlessness',
                                           'runny_nose', 'rusty_sputum', 'scurring', 'shivering',
                                           'silver_like_dusting', 'sinus_pressure', 'skin_peeling',
                                           'skin_rash', 'slurred_speech', 'small_dents_in_nails',
                                           'spinning_movements', 'spotting_urination', 'stiff_neck',
                                           'stomach_bleeding', 'stomach_pain', 'sunken_eyes', 'sweating',
                                           'swelled_lymph_nodes', 'swelling_joints', 'swelling_of_stomach',
                                           'swollen_blood_vessels', 'swollen_extremeties', 'swollen_legs',
                                           'throat_irritation', 'toxic_look_(typhos)', 'ulcers_on_tongue',
                                           'unsteadiness', 'visual_disturbances', 'vomiting',
                                           'watering_from_eyes', 'weakness_in_limbs',
                                           'weakness_of_one_body_side', 'weight_gain', 'weight_loss',
                                           'yellow_crust_ooze', 'yellow_urine', 'yellowing_of_eyes',
                                           'yellowish_skin', 'itching']).fit_transform(symps)
        pred = model.predict(np.array(lis))
        p=[i for i in pred]
        return p
# Create a list of medicines based on disease_symptoms
medicines_list = list(set(medicine for medicines in disease_medicines.values() for medicine in medicines))

# Sort the symptoms alphabetically
all_symptoms = sorted(list(set(symptom for symptoms in disease_symptoms.values() for symptom in symptoms)))

# Function to suggest medicines based on entered symptoms
def suggest_medicines(*args):
    entered_text = entry_var.get().lower()
    entered_symptoms = set(entered_text.split(", "))
    suggested_diseases = set()
    total_symptoms=set([i for dis, symp in disease_symptoms.items() for i in symp])
    f=1
    for disease, symptoms in disease_symptoms.items():
        symp=set(symptoms)
        if (symp.issuperset(entered_symptoms)):
            suggested_diseases.add(disease)
            f=0
    if(f == 1 and entered_symptoms.issubset(total_symptoms)):
        for i in DiseasetoDoctor().findDoc(entered_symptoms):
            suggested_diseases.add(i)
    update_suggested_diseases_listbox(suggested_diseases)

# Function to update the suggested diseases listbox
def update_suggested_diseases_listbox(suggested_diseases):
    suggested_diseases_listbox.delete(0, tk.END)
    for disease in suggested_diseases:
        symptoms = ", ".join(symptom for symptom in disease_symptoms[disease])
        suggested_diseases_listbox.insert(tk.END, f"{disease} - You might also be suffering from [{symptoms}]")

# Function to suggest medicines for the selected disease
def suggest_medicines_for_disease():
    selected_disease_index = suggested_diseases_listbox.curselection()
    if selected_disease_index:
        selected_disease = suggested_diseases_listbox.get(selected_disease_index[0]).split(" - ")[0]
        suggested_medicines = set(disease_medicines.get(selected_disease, []))
        update_suggested_medicines_listbox(suggested_medicines)
    else:
        messagebox.showwarning("No Disease Selected", "Please select a disease.")

# Function to update the suggested medicines listbox
def update_suggested_medicines_listbox(suggested_medicines):
    suggested_medicines_listbox.delete(0, tk.END)
    for medicine in suggested_medicines:
        suggested_medicines_listbox.insert(tk.END, medicine)

# Function to display detailed results for a selected medicine
def show_medicine_details():
    selected_medicine_index = suggested_medicines_listbox.curselection()
    if selected_medicine_index:
        selected_medicine = suggested_medicines_listbox.get(selected_medicine_index[0])
        medicine_details = get_medicine_details(selected_medicine)
        messagebox.showinfo("Medicine Details", medicine_details)
    else:
        messagebox.showwarning("No Medicine Selected", "Please select a medicine.")

# Function to get details of a selected medicine (not implemented here)
def get_medicine_details(disease,symps,medicine):
    st=''
    sy=''
    for i in list(medicine):
        st=f"{st}\n{i}"
    for i in list(symps):
        if(sy==''):
            sy=f" {i}"
        else:
            sy=f"{sy}, {i}"

    return f"Details for {disease}:\nSymptoms:{sy}\nMedicines required:{st}"

# Function to add a selected symptom to the entry field
def add_symptom():
    selected_disease_index =suggested_diseases_listbox.curselection()
    if selected_disease_index:
        selected_disease = suggested_diseases_listbox.get(selected_disease_index[0]).split(" - ")[0]
        suggested_medicines = set(disease_medicines.get(selected_disease, []))
        symps= set(disease_symptoms.get(selected_disease, []))
        medicine_details = get_medicine_details(selected_disease,symps,suggested_medicines)
        messagebox.showinfo("Disease & Medicine Details", medicine_details)
    else:
        messagebox.showwarning("No Disease Selected", "Please select a disease.")

#new window to open
def main():
    def on_select(event):
        selected_indices = symptom_listbox.curselection()
        if selected_indices:
            selected_symptom = symptom_listbox.get(selected_indices[0])
            current_text = entry_var.get()
            if current_text:
                new_text = f"{current_text}, {selected_symptom}"
            else:
                new_text = selected_symptom
        entry_var.set(new_text)
    
    # Create the main window
    root = tk.Tk()
    root.title("SPACE-DOCTOR 🚀")
    style = ThemedStyle(root)
    style.set_theme("plastik")

    # Create a main frame for both left and right sections
    main_frame = ttk.Frame(root)
    main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Create a frame for the left section
    left_frame = ttk.Frame(main_frame)
    left_frame.grid(row=0, column=0, padx=(0, 20), pady=20, sticky="nsew")

    # Create a frame for the right section
    right_frame = ttk.Frame(main_frame)
    right_frame.grid(row=0, column=1, pady=20, sticky="nsew")

    # Labels and headings
    ttk.Label(left_frame, text="Enter Your Symptoms", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=(0, 10), sticky="w")
    ttk.Label(left_frame, text="Suggested Diseases", font=("Helvetica", 12, "bold")).grid(row=2, column=0, padx=(0, 10), pady=(10, 0), sticky="w")

    # Create an entry widget for entering symptoms
    global entry_var
    entry_var = tk.StringVar()
    entry_var.trace_add('write', suggest_medicines)
    entry = ttk.Entry(left_frame, textvariable=entry_var, font=("Helvetica", 10, "normal"))
    entry.grid(row=1, column=0, padx=0, pady=(0, 10), sticky="ew")

    # Create a listbox for suggested diseases
    global suggested_diseases_listbox
    suggested_diseases_listbox = Listbox(left_frame, height=5)
    suggested_diseases_listbox.grid(row=4, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew")

    # Create a vertical scrollbar for the suggested diseases listbox
    diseases_scrollbar = Scrollbar(left_frame, orient="vertical", command=suggested_diseases_listbox.yview)
    suggested_diseases_listbox.config(yscrollcommand=diseases_scrollbar.set)
    diseases_scrollbar.grid(row=4, column=1, sticky="ns")

    # Create a listbox for the list of symptoms
    global symptom_listbox
    symptom_listbox = Listbox(left_frame, height=10)
    symptom_listbox.grid(row=5, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew")

    # Create a horizontal scrollbar for the symptom listbox
    symptom_h_scrollbar = Scrollbar(left_frame, orient="horizontal", command=symptom_listbox.xview)
    symptom_h_scrollbar.grid(row=6, column=0, sticky="ew")
    symptom_listbox.config(xscrollcommand=symptom_h_scrollbar.set)

    # Create a vertical scrollbar for the symptom listbox
    symptom_v_scrollbar = Scrollbar(left_frame, orient="vertical", command=symptom_listbox.yview)
    symptom_listbox.config(yscrollcommand=symptom_v_scrollbar.set)
    symptom_v_scrollbar.grid(row=5, column=1, sticky="ns")

    # Create a button to add selected symptom to the entry field
    add_symptom_button = ttk.Button(left_frame, text="Suggest Medicines for Disease", command=add_symptom)
    add_symptom_button.grid(row=7, column=0, padx=(0, 10), pady=(10, 0), sticky="ew")

    # Configure row and column weights for responsiveness
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)

    left_frame.grid_rowconfigure(1, weight=1)

    left_frame.grid_columnconfigure(0, weight=1)

    # Populate symptom listbox
    for symptom in all_symptoms:
        symptom_listbox.insert(tk.END, symptom)

    # Bind on_select function to ListboxSelect event
    symptom_listbox.bind("<<ListboxSelect>>", on_select)

    # Run the tkinter main loop
    root.mainloop()

tk.Frame(w, width=427, height=250, bg='black', borderwidth=0).place(x=0,y=0)
im=Image.open("spacedoc.png")
img = ImageTk.PhotoImage(im.resize((100,100), Image.LANCZOS))
label1=tk.Label(w, image=img, borderwidth=0,highlightthickness=0, highlightbackground='black') #decorate it   #You need to install this font in your PC or try another one
label1.place(x=10,y=60)
label3=tk.Label(w, text="WELCOME TO SPACEDOC 🚀", fg='white', bg='black' )
label3.configure(font=("Game of Squids", 20, 'bold')) #decorate it   #You need to install this font in your PC or try another one
label3.place(x=70,y=20)

label2=tk.Label(w, text='Loading...', fg='white', bg='black') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))




for i in range(2):
    l1=tk.Label(w, image=image_a, border=0, relief=tk.SUNKEN).place(x=180, y=145)
    l2=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=200, y=145)
    l3=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=220, y=145)
    l4=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=180, y=145)
    l2=tk.Label(w, image=image_a, border=0, relief=tk.SUNKEN).place(x=200, y=145)
    l3=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=220, y=145)
    l4=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=180, y=145)
    l2=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=200, y=145)
    l3=tk.Label(w, image=image_a, border=0, relief=tk.SUNKEN).place(x=220, y=145)
    l4=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=180, y=145)
    l2=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=200, y=145)
    l3=tk.Label(w, image=image_b, border=0, relief=tk.SUNKEN).place(x=220, y=145)
    l4=tk.Label(w, image=image_a, border=0, relief=tk.SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
main()
w.mainloop()
