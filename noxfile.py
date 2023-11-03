import nox
from nox import Session

PYTHON_VERSION = "3.10"


@nox.session(python=PYTHON_VERSION)
def format_code(session: Session):
    session.install("black")
    session.install("isort")
    session.run("isort", "--profile=black", ".")
    session.run("black", "-l", "100", ".")
