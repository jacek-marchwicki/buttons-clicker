# Buttons clicker

## Debug

```bash
cd server
pip install -r requirements.txt -t lib
cp secrets.py.src secrets.py # and edit
dev_appserver.py ./
```

## Deploy

```bash
cd server
pip install -r requirements.txt -t lib
appcfg.py update --oauth2 .
```
