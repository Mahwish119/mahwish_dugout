Week 2
Jason ,dumps() and loads()
API server activated the commands are terminal>pyhton -m [.name of server](.venv)
terminal> .venv(name of server)\Scripts\activated (the server will become activated)
powershell/termnal>pip install fastapi "uvicorn[standard]"requests 
if the 5th step doesn't work and the installation doesnot start then enter the following command 
python -m pip install fastapi "uvicorn[standard]"requests, once the terminal finishes all the installation view the installed items with the following command 
terminal>pip freeze > requirements.txt. The file will appear in the work place if this doesnot work follow the command
terminal> pyhton -m pip freeze > requirements.txt
after the api.py completed run the following command on your terminal 
>uvicorn folder_name.api:app --reload if it doesnot work execute the following command
terminal>pyhton -m uvicorn folder_name.api:app --reload
--reload will keep the server updated with all the changes being done in the app immediately and there is no need to activate the server again.  
