test:
	-rm o
	curl http://127.0.0.1:8000/waddayaknow > o
	curl http://127.0.0.1:8000/post-demo >> o
	curl -X POST -d argument=42 http://127.0.0.1:8000/post-demo >> o
	curl http://127.0.0.1:8000/form-demo | diff templates/form.html -  >> o
	curl -X POST -d submitted-name=Archie http://127.0.0.1:8000/form-demo >> o

app:
	flask --app app run --debug --port 8000

# If app.py is working correctly, then the two files should be identical
diff:
	diff demo-file.txt o
