# Local Python Chatbot Using Ollama

This project runs a fully local chatbot using Python + Ollama.  
Everything happens on your machine — no API keys, no cloud services.

---

## 🚀 Prerequisites

Install the following:

- **Python 3.10+**
- **Ollama** → https://ollama.com/download

Check that Ollama works:

```bash
ollama --version
```

Download a model:
```
ollama pull phi:latest
```

Verify it’s installed:
```
ollama list
```


## 🛠️ Setup

1. Clone this repository:
   ```
   git clone git@github.com:VolodymyrPliuta/Ollama.git
   ```

2. Navigate to the project directory:
   ```
   cd ollama
   ``` 
3. Create and activate a virtual environment:
   ```bash
    python -m venv venv

    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```  

## ▶️ Run the Chatbot
Run the chatbot script:
```bash
python simple.py
```
Type your messages and press Enter to chat with the local model.  
Type `exit` to quit the chat.
Enjoy chatting locally with Ollama keeping your data private 🎉