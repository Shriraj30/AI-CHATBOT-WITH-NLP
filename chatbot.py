import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import scrolledtext


knowledge_base = {
    "What is natural language processing?": "Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language.",
    "Explain machine learning": "Machine learning is a subset of artificial intelligence that involves training algorithms to make predictions or decisions without being explicitly programmed.",
    "What is TF-IDF?": "TF-IDF stands for Term Frequency-Inverse Document Frequency. It is a numerical statistic that reflects how important a word is to a document relative to a collection of documents.",
    "Tell me about AI": "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn.",
    "How does TF-IDF work?": "TF-IDF works by calculating the frequency of words in a document and weighing them according to how rare they are across a collection of documents."
}


questions = list(knowledge_base.keys())
answers = list(knowledge_base.values())


def preprocess_text(text):
    text = text.lower()
    text = " ".join([word for word in text.split() if word.isalpha()])
    return text

preprocessed_questions = [preprocess_text(q) for q in questions]


tfidf_vectorizer = TfidfVectorizer(stop_words='english')
question_vectors = tfidf_vectorizer.fit_transform(preprocessed_questions)

def get_response(user_query):
    """Generate a response based on user query."""
    
    preprocessed_query = preprocess_text(user_query)
    query_vector = tfidf_vectorizer.transform([preprocessed_query])

    similarities = cosine_similarity(query_vector, question_vectors)
    best_match_idx = np.argmax(similarities)

   
    if similarities[0][best_match_idx] > 0.2:
        return answers[best_match_idx]
    else:
        return "I'm sorry, I don't understand your question. Could you please rephrase?"


def send_message():
    """Send user message to the chatbot and display response."""
    user_input = user_entry.get()
    if user_input.lower() == 'exit':
        window.quit()
    else:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {user_input}\n")
        response = get_response(user_input)
        chat_window.insert(tk.END, f"Chatbot: {response}\n")
        chat_window.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)


window = tk.Tk()
window.title("NLP Chatbot")
window.geometry("500x500")
window.config(bg="#f0f0f0")


chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=15, state=tk.DISABLED, bg="#f9f9f9", fg="black", font=("Arial", 12), padx=10, pady=10)
chat_window.grid(row=0, column=0, padx=20, pady=10)


user_entry = tk.Entry(window, width=40, font=("Arial", 14), bd=2, relief="solid")
user_entry.grid(row=1, column=0, padx=20, pady=10)


send_button = tk.Button(window, text="Send", command=send_message, font=("Arial", 14), bg="#4CAF50", fg="white", width=10, height=1, relief="solid")
send_button.grid(row=1, column=1, padx=20, pady=10)


window.mainloop()
