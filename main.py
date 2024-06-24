import os
import json
import argparse
from actions import send_email, get_instance_name

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

    os.system("pytest -v -s --disable-warnings test_model.py")
    os.system("pytest -v -s --disable-warnings test_no_data.py")
    os.system("pytest -v -s --disable-warnings test_page_traversal.py")
    os.system("pytest -v -s --disable-warnings test_prototype.py")
    os.system("pytest -v -s --disable-warnings test_signInOut.py")
    os.system("pytest -v -s --disable-warnings test_signUp.py")

if __name__ == "__main__":
    main()
    with open('info.json') as config_file:
        configInfo = json.load(config_file)
    instance = get_instance_name(configInfo)
    subject = f"Warnings and errors occured in the {instance}"
    send_email(configInfo, "", subject, "later")