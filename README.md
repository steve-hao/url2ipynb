# [url2ipynb](https://github.com/steve-hao/url2ipynb)

url2ipynb is a Python script that converts HTML (export by Jupyter Notebook) from File/URL into ipynb notebook file.

``` 
Usage: Usage: url2ipynb url|filename outputfile
```

URL must start with http:// or https:// 

This script will converts some Web Page which is exported by Jupyter Notebook into ipynb file.

It only converts the part exported by Jupyter Notebook and ignore the other part in the web page.

Same, you can use it with you python 

``` 
import url2ipynb

url = 'https://plot.ly/python/peak-finding/'
outfile='Peak_Finding.ipynb'
url2ipynb.url2ipynb(url,outfile)

```
You can try it with this Web [plotly-express] (https://plot.ly/python/plotly-express/)