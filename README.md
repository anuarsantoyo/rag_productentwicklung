# RAG Produktentwicklung
Chatbot for Product Development

## Install dependencies
1. Do the following before installing the dependencies found in `requirements.txt` file because of current challenges installing `onnxruntime` through `pip install onnxruntime`. 
- For Windows users, follow the guide [here](https://github.com/bycloudai/InstallVSBuildToolsWindows?tab=readme-ov-file) to install the Microsoft C++ Build Tools. Be sure to follow through to the last step to set the enviroment variable path.

2. Now run this command to install dependenies in the `requirements.txt` file. 

```python
pip install -r requirements.txt
```
3. Run nltk_download.py to download the necessary nltk data.

```python
python nltk_download.py
``` 

## Create database

Create the Chroma DB.

```python
python create_database.py
```

## Query the database

Run the chatbot.

```python
python produkt_entwickulng_bot.py
```
