# Main instructions

This instructions are helpfull for getting you up and running the project. The main goal is for you to have a base project from where you can showcase the different uses or demos you create, so that more people can have access to them, professors, collegues, boss.

## Running fast api
fastapi run app/main.py

## Running streamlit

## Running both at the same time

### Windows

Start-Process -NoNewWindow -FilePath "powershell" -ArgumentList "fastapi run app/main.py"
Start-Process -NoNewWindow -FilePath "powershell" -ArgumentList "streamlit run frontend/Chat.py"

Start-Process -NoNewWindow -FilePath "powershell" -ArgumentList "uvicorn llm_chat.app.main:app --reload"
Start-Process -NoNewWindow -FilePath "powershell" -ArgumentList "streamlit run llm_chat/frontend/Chat.py"

### macOs/Linux

uvicorn llm_chat.app.main:app --reload & streamlit run frontend/Chatbot.py
