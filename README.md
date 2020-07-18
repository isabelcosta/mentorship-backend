# Mentorship System (Backend)

![Build Status](https://github.com/anitab-org/mentorship-backend/workflows/Run%20tests/badge.svg)
[![codecov](https://codecov.io/gh/anitab-org/mentorship-backend/branch/develop/graph/badge.svg)](https://codecov.io/gh/anitab-org/mentorship-backend)

[Mentorship System](https://github.com/anitab-org/mentorship-backend) is an application that allows women in tech to mentor each other, on career development topics, through 1:1 relations for a certain period.
This is the Backend REST API for the Mentorship System.

**Table of Contents**

- [Setup and run](#setup-and-run)
    - [Run app](#run-app)
    - [Run with Docker](#run-with-docker)
    - [Run tests](run-tests)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Branches](#branches)
- [Contact](#contact)

## Setup and run

To setup the project locally read these wiki pages and follow the instructions:

 - [Fork, Clone and Remote](https://github.com/anitab-org/mentorship-backend/wiki/Fork%2C-Clone-%26-Remote)
 - [Export Environment Variables](docs/environment-variables.md)

### Run app

The project runs on Python 3.

1. Create a virtual environment:
`virtualenv venv --python=python3`

2. Activate the virtual environment:
`source ./venv/bin/activate`

`source ./venv/bin/activate` may produce errors (no such directory errors) for Windows users who use Git Bash, because on Windows machines, virtual environments do not have the bin folder under venv. Instead, run the command `source ./venv/Scripts/activate`. This command only works on Git Bash on Windows machines. For Windows Command Line Users, run `.\env\Scripts\activate` instead. This command is for users running the program on Windows CMD.


3. Install all the dependencies in `requirements.txt` file:
`pip install -r requirements.txt`

4. Make sure you create `.env` using `.env.template` and update the values of corresponding environment variables
or
make sure you exported the following [environment variables](docs/environment-variables.md):

```
export FLASK_ENVIRONMENT_CONFIG=<local-or-dev-or-test-or-prod-or-stag>
export SECRET_KEY=<your-secret-key>
export SECURITY_PASSWORD_SALT=<your-security-password-salt>
export MAIL_DEFAULT_SENDER=<mail-default-sender>
export MAIL_SERVER=<mail-server>
export APP_MAIL_USERNAME=<app-mail-username>
export APP_MAIL_PASSWORD=<app-mail-password>
export MOCK_EMAIL = <True-or-False>
```

If you're testing any environment other than "local", then you have to also set these other variables:
```
export DB_TYPE=<database_type>
export DB_USERNAME=<database_username>
export DB_PASSWORD=<database_password>
export DB_ENDPOINT=<database_endpoint>
export DB_NAME=<database_name>
```

5. Run the app:
```
python run.py
```

6. Navigate to http://localhost:5000 in your browser

7. When you are done using the app, deactivate the virtual environment:
```
deactivate
```

### Run with docker

1. Make sure you exported the following [environment variables](docs/environment-variables.md) to '.env' file

2. Build docker image
```
docker build -t mentorship-backend:latest .
```
3. Deploy
Docker container ports must be mapped to the host machine port using '--publish' so they're visible.
```sh
docker run --env "FLASK_APP=run.py" --publish 5000:5000 mentorship-backend:latest
```

### Run tests

To run the unitests run the following command in the terminal (while the virtual environment is activated):

```
python -m unittest discover tests
```

## Documentation

You can learn more about this project throguh the documentation in the [docs](./docs) folder and on [our Wiki](https://github.com/anitab-org/mentorship-backend/wiki).

**Summary**

- **Language:** Python 3.6
- **Framework:** [Flask](http://flask.pocoo.org/)
- **Flask Extensions:** [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/), [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org), [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/latest/), [Flask-Mail](https://pythonhosted.org/Flask-Mail)
- **Hosting Service:** Heroku
- **Database:** Relational Database

Understand more about our technical decisions made along with this project development in [Technical Decisions Wiki page](https://github.com/anitab-org/mentorship-backend/wiki/Technical-Decisions).

Here's some links to important documentation for this project:

- [How to use Backend Swagger UI](https://github.com/anitab-org/mentorship-backend/wiki/Using-Backend-Swagger-UI) and [test PR guide](./docs/test-pr-guide.md) contains a few resources for you to understand how to use the Swagger user interface provided by this app.
- [Features Overview](./docs/features.md) has a high level understanding of the features this application has.
- [Future ideas for the project](https://github.com/anitab-org/mentorship-backend/wiki/Future-ideas).
- [Troubleshoot guide](./docs/troubleshoots.md) contains common isssues other contributors may run into in their setup.
- [Quality Assurance test cases](./docs/quality-assurance-test-cases.md) has test cases for each endpoint we have which you can use to learn about how each feature should work.

## Contributing

Please read our [Contributing guidelines](./.github/CONTRIBUTING.md), [Code of Conduct](http://systers.io/code-of-conduct) and [Reporting Guidelines](http://systers.io/reporting-guidelines)

Please follow our [Commit Message Style Guide](https://github.com/anitab-org/mentorship-backend/wiki/Commit-Message-Style-Guide) and [Coding Standards](./docs/coding_standards.md) while sending PRs.

## Branches

The repository has the following permanent branches:

 * **master** This contains the code which has been released.

 * **develop** This contains the latest code. All the contributing PRs must be sent to this branch. When we want to release the next version of the app, this branch is merged into the `master` branch.

## Contact

You can reach the maintainers and our community on [AnitaB.org Open Source Zulip](https://anitab-org.zulipchat.com/). If you are interested in contributing to the mentorship system, we have a dedicated stream for this project [#mentorship-system](https://anitab-org.zulipchat.com/#narrow/stream/222534-mentorship-system), where you can ask questions and interact with the community, join with us!
