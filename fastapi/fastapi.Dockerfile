FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV source_folder_path=$SOURCE_FOLDER_PATH
ENV dest_folder_path=$DEST_FOLDER_PATH

WORKDIR /app

COPY . .

RUN apk update && pip install --upgrade pip && pip install -f requirements.txt

ENTRYPOINT [ "python3 fastapi.py" ]