FROM python:3.7.1-stretch

RUN useradd alfieweb
WORKDIR /home/alfieweb

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends texlive-xetex texlive-fonts-recommended texlive-lang-european

RUN apt-get install unzip
RUN wget https://github.com/adobe-fonts/source-sans-pro/releases/download/2.040R-ro%2F1.090R-it/source-sans-pro-2.040R-ro-1.090R-it.zip
RUN unzip source-sans-pro-2.040R-ro-1.090R-it.zip
RUN mkdir -p .fonts
RUN cp source-sans-pro-2.040R-ro-1.090R-it/OTF/*.otf .fonts/ #/usr/share/fonts/type1
RUN rm -r source-sans-pro-2.040R-ro-1.090R-it
RUN fc-cache -f -v

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
RUN key=$(openssl rand -base64 32) && sed -i "s|key-replaced-on-docker-build|$key|g" app/alfieweb.py
RUN mkdir -p app/generated-files/tmp/
RUN mkdir -p app/generated-files/cache/
COPY gunicorn-config.py ./
COPY boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP alfieweb.py

RUN chown -R alfieweb:alfieweb ./
USER alfieweb

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
