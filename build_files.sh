python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
python manage.py collectstatic --noinput