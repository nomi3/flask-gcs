# flask-gcs

You can use GCS Emulator in local environment with Flask.

## Setup

```bash
git clone https://github.com/nomi3/flask-gcs.git
cd flask-gcs
make up
```

Now, you can access to http://localhost:8080/
If you see "hello", it's working.

## Upload file

```bash
curl -X POST -F "file=@test.txt" http://localhost:8080/upload
```

You can see the file in .storage/local-bucket/test.txt

## Download file

```bash
curl http://localhost:8080/download?file_name=test.txt
```

You can get the file in .storage/local-bucket/test.txt

## Delete file

```bash
curl -X DELETE http://localhost:8080/delete?file_name=test.txt
```

You can delete the file in .storage/local-bucket/test.txt

## Stop

```bash
make down
```
