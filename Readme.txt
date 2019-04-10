Operating System : Ubuntu 18.04.2 LTS
Python 3.6.7
Scrapy 1.6.0

1) Create a Virtual Enviorment.
        "pipenv shell"

2) Install Scrapy.
        "pip install Scrapy"

3) Create a Scrapy Project.
        "scrapy startproject ServiceProviders"

4) Create code for a spider that scraps data from websites.
        "scrapycode.py" ----> Spidername: 'globaltrade'

5)Command for Run the code and Create a dataset.json.
        "scrapy crawl globaltrade -o dataset.json"
