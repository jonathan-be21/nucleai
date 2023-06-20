FROM python:3.9.17-alpine3.18

ENV source_folder_path=$SOURCE_FOLDER_PATH
ENV dest_folder_path=$DEST_FOLDER_PATH

WORKDIR /app

COPY . .

RUN apk update && pip install --upgrade pip && pip install -f requirements.txt

ENTRYPOINT [ "python3 listener.py" ]