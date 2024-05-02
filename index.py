import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import openai

# Defina sua chave de API do OpenAI
api_key = 'sua-chave-de-api-aqui'

# Inicialize a API do OpenAI
openai.api_key = api_key

# Função para interagir com o chatbot
def converse_with_chatbot(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",  # Escolha o modelo de linguagem
        prompt=prompt,
        max_tokens=150  # Número máximo de tokens para gerar na resposta
    )
    return response.choices[0].text.strip()

# Função para enviar mensagem e obter resposta do chatbot
def send_message():
    user_input = input_box.get("1.0",'end-1c')
    input_box.delete("1.0",'end-1c')
    if user_input.lower() == 'sair':
        messagebox.showinfo("Chat", "Até logo!")
        root.quit()
    else:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Você: " + user_input + "\n")
        chat_box.see(tk.END)
        chat_box.config(state=tk.DISABLED)

        bot_response = converse_with_chatbot(user_input)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "ChatGPT: " + bot_response + "\n")
        chat_box.see(tk.END)
        chat_box.config(state=tk.DISABLED)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Chatbot")

# Caixa de chat
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_box.config(state=tk.DISABLED)
chat_box.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

# Caixa de entrada de texto
input_box = tk.Text(root, wrap=tk.WORD, width=40, height=3)
input_box.grid(column=0, row=1, padx=10, pady=10)

# Botão de envio
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.grid(column=1, row=1, padx=10, pady=10)

root.mainloop()
