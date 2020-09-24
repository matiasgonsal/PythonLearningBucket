clear
echo executing flask service...
service=ServiceController.py
export FLASK_APP=$service
flask run
