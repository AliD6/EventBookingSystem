FROM registry.sedrehgroup.ir/python:3.11.1
LABEL MAINTAINER="AliD"

ENV TZ=Asia/Tehran

# RUN apt-get -y update && apt-get -y upgrade && apt-get install vim nano -y

WORKDIR /api
# RUN python3 -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
#RUN python -m pip install --upgrade pip && pip install -r requirements.txt
RUN PIP_INDEX_URL="https://admin:Sedreh%23313@nexus.sedrehgroup.ir/repository/sedreh-python/simple" pip install -r requirements.txt
COPY . .

CMD ["sh", "entrypoint.sh"]
