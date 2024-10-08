import json
from setup_methods.set_up import Base  # Importing the Base class

class BaseTest:
    @classmethod
    def setUpClass(cls):
        cls.base = Base()
        cls.base.setup_logger()
        # Making sure that logger is configured only once at the beginning of every test cases
    
    @classmethod
    def tearDownClass(cls):
        cls.base.logSummarizer()
        # Making sure that the summarizer is configured only once at the end of every test cases

    def setUp(self):
        self.base.setup_browser()
        self.base.start_timer()
        self.next = self.base.next
        self.driver = self.base.driver
        self.logger = self.base.logger
        with open('info.json') as config_file:
            self.configInfo = json.load(config_file)
        with open('critical_error.json') as config_file_2:
            self.configError = json.load(config_file_2)

    def tearDown(self):
        self.base.clean_up()
