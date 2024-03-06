import tkinter as tk


def calculo_valor_total():
    valor_total = 0
    quantidade_materias = 5

    for i in range(quantidade_materias):
        valor_total += float(entry_list[i].get())

    valor_medio_enem = valor_total / quantidade_materias
    label_resultado_total.config(text="Sua pontuação total foi: " + str(valor_total))
    label_resultado_medio.config(text="Sua média no ENEM é: " + str(valor_medio_enem))


root = tk.Tk()
root.title("Calculadora de Média do ENEM")

# Create labels and entry boxes for each subject
entry_list = []
for i in range(5):
    tk.Label(root, text=f"Matéria {i+1}:").grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entry_list.append(entry)

# Create a button to calculate
calcular_button = tk.Button(root, text="Calcular Média", command=calculo_valor_total)
calcular_button.grid(row=5, columnspan=2)

# Create labels to display results
label_resultado_total = tk.Label(root, text="")
label_resultado_total.grid(row=6, columnspan=2)
label_resultado_medio = tk.Label(root, text="")
label_resultado_medio.grid(row=7, columnspan=2)

root.mainloop()
