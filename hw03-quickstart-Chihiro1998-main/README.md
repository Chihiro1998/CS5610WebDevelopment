# hw-quickstart-solution

Server demo based on the Flask [quickstart](https://flask.palletsprojects.com/en/stable/quickstart)

## assignment (summary)

Write an app.py and start flask with
```
make app
```
so that the command-line command
```
make test
```
produces a single file called "o" with the content in `demo-file.txt`

* You can see in the Makefile that `make test` runs several `curl` commands.
* Hints are below for creating the code that responds appropriately to each `curl` command.
* Note: you should be able to complete the assignment with less than 30 lines of code.

## GET

The response to
```
curl http://127.0.0.1:8000/waddayaknow
```
should be
```
Not much, you?
```
* Make sure there's a a carriage return (i.e., "\n") at the end of the string that comes from the server.
* A Minimal Application -- https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application
* Routing -- https://flask.palletsprojects.com/en/stable/quickstart/#routing

## POST

```
curl http://127.0.0.1:8000/post-demo
```
should produce the response
```
That wasn't a POST request
```
and
```
curl -X POST -d argument=42 http://127.0.0.1:8000/post-demo >> o
```
should produce the response
```
{
  "argument": "42"
}
```
* HTTP methods -- https://flask.palletsprojects.com/en/stable/quickstart/#http-methods
* Accessing request data -- https://flask.palletsprojects.com/en/stable/quickstart/#accessing-request-data
* You can verify with `--verbose` that `curl` sends the POST with "Content-Type: application/x-www-form-urlencoded"
* That means you can access the form data in Flask's request object with its form property: `request.form`
* Request.form API docs -- https://flask.palletsprojects.com/en/stable/api/#flask.Request.form

## templates

The command
```
curl http://127.0.0.1:8000/form-demo
```
should return the file `./templates/form.html` and
```
curl -X POST -d submitted-name=Archie http://127.0.0.1:8000/form-demo
```
should respond with
{
  "submitted-name": "Archie"
}
* Rendering templates -- https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates
* Note: If you browse to http://127.0.0.1:8000/form-demo, the template should render in your browser -- try it
