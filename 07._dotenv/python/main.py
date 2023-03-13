#poetry init -n
#poetry shell
#poetry add python-env
#nodemon --exec python3 main.py


from dotenv import load_dotenv, dotenv_values

dotenv_values = dotenv_values()
print(dotenv_values.get("MY_VARIABLE"))


#EXAMPLE 2  
load_dotenv()
import os
print(os.getenv("MY_VARIABLE"))