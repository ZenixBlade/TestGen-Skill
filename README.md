\# TestGen-Skill 🧪



\*\*Generate and execute Python unit tests locally using AI.\*\*



TestGen-Skill is a lightweight command-line tool that uses a locally running Ollama model to generate pytest tests for Python functions.



\## Features



\- Generates tests for normal inputs, edge cases, and invalid inputs.

\- Uses a local Ollama model.

\- Saves source code and generated tests to `generated\_tests.py`.

\- Offers to run tests using pytest.

\- Displays actual test execution results.



\## Requirements



\- Python

\- \[Ollama](https://ollama.com/)

\- `llama3.2:3b` model

\- Python packages: `ollama` and `pytest`



\## Setup



Install dependencies:



```bash

py -m pip install ollama pytest

```



Download the model if needed:



```bash

ollama pull llama3.2:3b

```



Make sure Ollama is running, then start the application:



```bash

py app.py

```



Paste your Python source code into the prompt. Type `END` on a new line when finished. When asked, enter `y` to run pytest.



\## Skill Instructions



See `skills/testgen/SKILL.md`.



\## Safety



Review generated tests before executing them. Running tests can execute Python code, and this prototype does not provide a security sandbox.



\## Project Status



Prototype tested locally with a simple Python function.



\## License



No license specified yet.

