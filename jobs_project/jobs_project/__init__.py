# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import sys
import os

# Add /app/infra to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))  # /app/jobs_project
project_root = os.path.abspath(os.path.join(current_dir, "../.."))  # /app
infra_path = os.path.join(project_root, "infra")  # /app/infra

if infra_path not in sys.path:
    sys.path.append(infra_path)
