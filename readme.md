# Simple scarping app 
I made a scrapping app that scrappes data from a website and renders them out in a new html file.
## How to install
First make a virtual enviroment:
```bash
py -m venv venv
```
and acitvate it

```bash
venv\\Scripts\\activate.bat
```
after that isntall the modules
```bash
pip install -r requirements.txt
```
## Start the script 
```bash
scrapy runspider scarper.py -L WARNING
```
The results will be saved in `*.json` into the `data`. When you run it again, the parser will add new data to the end of the file and  break the JSON, so it is better to delete old data files before restarting. Based on JSON files, you can generate an HTML page with the names, prices and photos of gpus. Run another script `render.py`:
```bash
python render.py
```

The script will create an index.html file or update it if one already exists. Open the index.html file in a browser.

