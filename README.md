# AI-CHATBOT-WITH-NLP
**Name:** Shriraj Dharmadhikari  
**Company:** CODTECH IT SOLUTIONS 
**ID:** CT08PEP  
**Domain:** Python Programming  
**Duration:** 25th Jan to 25th Feb  
**Mentor:** Neela Santosh 

---
# **NLP Chatbot Using TF-IDF and Tkinter**  

## **Overview of the Project**  
- This project is a simple chatbot using **Natural Language Processing (NLP)** techniques.  
- It utilizes the **TF-IDF (Term Frequency-Inverse Document Frequency)** algorithm to find the most relevant answer based on user queries.  
- A **GUI (Graphical User Interface)** is implemented using **Tkinter** to allow easy interaction with the chatbot.  

## **Objective**  
- Create a chatbot that can answer predefined questions using text similarity.  
- Implement **TF-IDF and Cosine Similarity** to find the best matching response.  
- Provide a simple and user-friendly chat interface using Tkinter.  

## **Key Activities**  

### **1. Data Preparation**  
- A **knowledge base** is created as a dictionary with questions as keys and their corresponding answers as values.  
- The questions are preprocessed (converted to lowercase and cleaned of non-alphabetic characters).  

### **2. TF-IDF Vectorization and Similarity Calculation**  
- The **TfidfVectorizer** from `sklearn.feature_extraction.text` is used to convert questions into numerical vectors.  
- **Cosine Similarity** is applied to compare the user’s query with the preprocessed questions to find the best match.  

### **3. Response Generation**  
- If the highest similarity score exceeds a threshold (0.2), the chatbot returns the corresponding answer.  
- If no relevant match is found, the chatbot responds with a default message:  
  *"I'm sorry, I don't understand your question. Could you please rephrase?"*  

### **4. GUI Implementation Using Tkinter**  
- A Tkinter-based graphical interface is created:  
  - A **chat window** using `ScrolledText` to display user messages and chatbot responses.  
  - An **entry field** for user input.  
  - A **send button** to submit queries and get responses.  

## **Technologies Used**  
- **Python**: Primary programming language.  
- **Libraries**:  
  - `numpy`: For numerical operations.  
  - `sklearn.feature_extraction.text`: For TF-IDF vectorization.  
  - `sklearn.metrics.pairwise`: For calculating cosine similarity.  
  - `tkinter`: For building the GUI.  

## **Scope**  
- Can answer predefined questions related to NLP, AI, and Machine Learning.  
- Provides a simple chatbot interface without requiring internet access.  
- Can be expanded by adding more questions and training with larger datasets.  

## **Advantages**  
- Simple and efficient for handling predefined FAQs.  
- Does not require external APIs or cloud services.  
- Can be modified for various use cases like customer support bots.  

## **Disadvantages**  
- Limited to predefined knowledge; cannot learn from new inputs.  
- May not provide accurate responses for complex queries.  
- Does not support deep learning-based natural language understanding.  

## **Key Insights**  
- **TF-IDF and Cosine Similarity** provide a lightweight solution for text-based question-answering.  
- **Preprocessing text** improves the accuracy of similarity matching.  
- **A simple GUI** enhances usability for non-technical users.  

## **Future Improvements**  
- Implement **machine learning** models to improve response accuracy.  
- Add **chat history tracking** for better user experience.  
- Enhance the chatbot with **speech-to-text** and **voice responses**.  

## **Code Explanation**  

### **1. Data Preparation**  
- The chatbot uses a **dictionary of predefined questions and answers** as its knowledge base.  
- The questions are preprocessed by converting them to lowercase and removing non-alphabetic characters.  

### **2. Text Vectorization and Similarity Matching**  
- The `TfidfVectorizer` converts the questions into **numerical vectors**.  
- The user’s query is also vectorized and compared using **cosine similarity**.  
- The chatbot selects the **most similar question** and returns its corresponding answer.  

### **3. GUI Implementation**  
- A **Tkinter window** is created with:  
  - A **ScrolledText widget** to display conversation history.  
  - An **Entry widget** for user input.  
  - A **Button** to send messages and display responses.  
- The chatbot runs in a loop to process user queries in real time.  

## **Output**  

<p align="center">
  <img src="https://github.com/user-attachments/assets/0e76face-01ae-45d1-b739-0138522f557f" width="500">
</p>



## **Contact**  
- **Name**: [Shriraj Dharmadhikari]
- **Company**: CODTECH IT SOLUTIONS
- **Email**: [shrirajdharmadhikari@gmail.com]   
