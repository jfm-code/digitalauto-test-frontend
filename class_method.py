import json
from set_up import Base  # Importing the Base class

class BaseTest:
    @classmethod
    def setUpClass(cls):
        cls.base = Base()
        cls.base.setup_logger()
        # Making sure that logger is configured only once

    def setUp(self):
        self.base.setup_browser()
        self.next = self.base.next
        self.driver = self.base.driver
        self.logger = self.base.logger
        with open('info.json') as config_file:
            self.config = json.load(config_file)

    def tearDown(self):
        self.base.clean_up()
