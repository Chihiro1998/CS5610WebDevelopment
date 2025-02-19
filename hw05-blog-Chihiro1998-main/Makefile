# Run the app in debug mode on port 8000
run:
	cd tutorial; flask --app flaskr init-db  # initializes the database
	cd tutorial; flask --app flaskr run --debug --port 8000

# Register several users with the app
users:
	curl -X POST http://127.0.0.1:8000/auth/register -d "username=user1&password=pass1"
	curl -X POST http://127.0.0.1:8000/auth/register -d "username=user2&password=pass2"
	curl -X POST http://127.0.0.1:8000/auth/register -d "username=user3&password=pass3"
	curl -X POST http://127.0.0.1:8000/auth/register -d "username=user4&password=pass4"
	curl -X POST http://127.0.0.1:8000/auth/register -d "username=user5&password=pass5"

# Get a copy of the tutorial from the flask repo on github.com using SSH
setup:
	git clone git@github.com:pallets/flask.git
	cp -r flask/examples/tutorial .
	rm -rf flask  # delete the flask repo that we just cloned
