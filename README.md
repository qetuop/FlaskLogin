### https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

# Setup Env, from top level
source deploy.sh

# Setup DB - creates project/db.sqlite
python3 setupDb.py

# Run
export FLASK_APP=project
export FLASK_DEBUG=1
flask run

or

python3 wsgi.py
