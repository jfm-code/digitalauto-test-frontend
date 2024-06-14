import os
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Run tests with optional headless mode."
    )
    parser.add_argument(
        "--headless", action="store_true", help="Run tests in headless mode"
    )
    args = parser.parse_args()

    if args.headless:
        os.environ["HEADLESS"] = "true"
    else:
        os.environ["HEADLESS"] = "false"

    os.system("pytest -v -s test_signInOut.py")
    os.system("pytest -v -s test_signUp.py")


if __name__ == "__main__":
    main()