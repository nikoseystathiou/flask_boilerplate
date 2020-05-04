# start.sh

export FLASK_APP=wsgi.py
export FLASK_ENV=development
export FLASK_DEBUG=1
#export FLASK_RUN_HOST=
#export FLASK_RUN_PORT=
#export FLASK_RUN_CERT=
#export FLASK_RUN_KEY=
flask run
