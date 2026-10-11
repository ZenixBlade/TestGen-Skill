
import re
import subprocess
import sys
from pathlib import Path

import ollama

MODEL = "llama3.2:3b"
TEST_FILE = Path("generated_tests.py")


def clean_python(text):
    """Remove Markdown fences from model output."""
    text = text.strip()
    text = re.sub(r"^```(?:python)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_tests(code):
    prompt = f"""
You are TestGen, a Python unit testing assistant.

The user supplied this Python source code:

{code}

Generate pytest tests for its existing functions.
Cover normal inputs, edge cases, and invalid inputs where appropriate.

Rules:
- Return only valid Python test code.
- Do not redefine the user's original functions.
- Assume the original source will be placed above your tests.
- Do not claim tests passed.
- Do not use file, network, or system operations in tests.
"""
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return clean_python(response["message"]["content"])


def main():
    print("\n=== TestGen AI ===")
    print("Paste a Python function or module.")
    print("Type END on a new line when finished.\n")

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            return

        if line.strip() == "END":
            break
        lines.append(line)

    code = "\n".join(lines).strip()
    if not code:
        print("No code entered.")
        return

    try:
        print("\nGenerating tests with", MODEL, "...")
        tests = generate_tests(code)

        if not tests:
            print("The model returned no tests.")
            return

        TEST_FILE.write_text(
            code + "\n\n" + tests + "\n",
            encoding="utf-8",
        )

        print("\n=== Generated Tests ===\n")
        print(tests)
        print("\nSaved source and tests to", TEST_FILE)

        answer = input("\nRun pytest now? (y/n): ").strip().lower()
        if answer != "y":
            print("Tests saved but not executed.")
            return

        result = subprocess.run(
            [
                sys.executable, "-m", "pytest",
                str(TEST_FILE), "-v",
                "--tb=short",
            ],
            text=True,
            capture_output=True,
            timeout=60,
        )

        print("\n=== Test Results ===")
        print(result.stdout)

        if result.stderr:
            print(result.stderr)

        if result.returncode == 0:
            print("RESULT: ALL TESTS PASSED")
        elif result.returncode == 1:
            print("RESULT: SOME TESTS FAILED")
        else:
            print("RESULT: TEST EXECUTION ERROR")

    except subprocess.TimeoutExpired:
        print("Tests exceeded the 60-second timeout.")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
