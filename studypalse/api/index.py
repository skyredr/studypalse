import os
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "study_pulse.settings")

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
