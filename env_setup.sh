# create python virtual environment, install packages, etc.

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
source .venv/bin/deactivate
