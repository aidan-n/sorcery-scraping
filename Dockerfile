FROM python

RUN pip install requests beautifulsoup4 python-dotenv

ADD sorcery.py .

CMD ["python", "./sorcery.py"]