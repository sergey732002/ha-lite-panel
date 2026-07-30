import os

# Home Assistant Supervisor API
SUPERVISOR_URL = "http://supervisor/core/api"
SUPERVISOR_TOKEN = os.environ.get("SUPERVISOR_TOKEN", "")

# Directories
BASE_DIR = "/"

PANELS_DIR = "/panels"
TEMPLATES_DIR = "/templates"
STATIC_DIR = "/static"

# Default panel
DEFAULT_PANEL = "home"

# Refresh interval (seconds)
DEFAULT_REFRESH = 5