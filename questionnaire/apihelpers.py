from urllib import urlopen
from io import BytesIO
import gzip
import json

def json_response(url, encoding="utf-8"):
    """
    Helper to import a JSON API response
    into a python object

    """
    
    response = urlopen(url)
    
    if response.info().get('Content-Encoding') == 'gzip':
        binaryStream = BytesIO(response.read())
        response = gzip.GzipFile(fileobj=binaryStream)
    
    return json.load(response, encoding=encoding)
