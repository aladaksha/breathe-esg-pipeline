import os
import sys
from django.core.wsgi import get_wsgi_application

# Dynamic path discovery: Locate 'esg_project' dynamically and inject it into Python's path
current_dir = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(current_dir):
    if 'esg_project' in dirs:
        sys.path.insert(0, root)
        sys.path.insert(0, os.path.join(root, 'esg_project'))
        break

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esg_project.settings')
application = get_wsgi_application()
