# mini-django
Test DeployAI : détection GENERATED_PYTHON, mais branche DIFFÉRENTE de
mini-python — présence de manage.py déclenche
"gunicorn --bind 0.0.0.0:8000 wsgi:application" au lieu de uvicorn.
Vérifie que _build_python_config détecte bien Django correctement.
