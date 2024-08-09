import os
import json
import argparse
from datetime import datetime
from setup_methods.actions import send_email, get_instance_name

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
        
    # test_files = ['test_no_data.py','test_page_traversal.py','test_signInOut.py','test_signUp.py','test_model.py','test_prototype.py','test_wishlistAPI.py']
    test_files = ['test_model.py']
    for test in test_files:
        execute_cmd = "pytest -v -s --disable-warnings test_methods/" + test
        os.system(execute_cmd)

    # os.system("pytest -v -s --disable-warnings test_methods/test_no_data.py")
    # os.system("pytest -v -s --disable-warnings test_methods/test_page_traversal.py")
    # os.system("pytest -v -s --disable-warnings test_methods/test_signInOut.py")
    # os.system("pytest -v -s --disable-warnings test_methods/test_signUp.py")
    # os.system("pytest -v -s --disable-warnings test_methods/test_model.py")
    # os.system("pytest -v -s --disable-warnings test_methods/test_prototype.py")
    # os.system("pytest -v -s --disable-warnings test_methods/test_wishlistAPI.py")
    
if __name__ == "__main__":
    main()
    with open('info.json') as config_file:
        configInfo = json.load(config_file)
    instance = get_instance_name(configInfo)
    subject = f"[{instance}-instance] Warnings and errors occured"
    current_time = str(datetime.now())
    current_date = current_time[:10]
    send_email(configInfo, "", subject, "later", current_date)