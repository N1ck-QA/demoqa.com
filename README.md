Introduction
------------

This repository contains a custom framework based
on the PageObject pattern with Selenium and Python (PyTest + Selenium),
developed during the process of testing the (https://demoqa.com) site 
within the 'Task3''at the stage of traineeship at the "TK"


Files
-----

[conftest.py](conftest.py) contains the required code (fixture) to run tests (start and close the webdriver, parameterization tools)

[webdriver_singleton.py](webdriver_singleton.py) contains the 'WebDriverSingleton' class with implementation of Singleton pattern and Factory method to organize the retrieval of a driver instance

[utils/config_util.py](utils/config_util.py) contains the 'ConfigUtil' class for working with the config.json 

[utils/data_loader.py](utils/data_loader.py) contains the 'DataLoader' class for working with the data.json (applicable to working with users data in table)

[utils/logger.py](utils/logger.py) contains the logger instance for working with the logs and method for configuration logging parameters

[utils/random_util.py](utils/random_util.py) contains the instance of 'Faker' class and method for generation the random text

[config/config.json](config/config.json) contains all needed browser options for webdriver

[test data/users.json](test_data/users.json) contains all needed test data for testing table on the 'Web Tables' page

[logs/](logs) directory that will contain the 'test.log' file with detailed log of the test actions created after
running the test

[pages/base_page.py](pages/base_page.py) contains 'BasePage' class with a page builder

[pages/main_page.py](pages/main_page.py) contains 'MainPage' class for interaction with the main page

[pages/alert_page.py](pages/alert_page.py) contains 'AlertPage' class with needed element locators and methods of interaction with them

[pages/nested_frames_page.py](pages/nested_frames_page.py) contains 'NestedFramePage' class with needed element locators and methods of interaction with them

[pages/frames_page.py](pages/frames_page.py) contains 'FramesPage' class with needed element locators and methods of interaction with them

[pages/tables_page.py](pages/tables_page.py) contains 'TablesPage' class with needed element locators and methods of interaction with them

[pages/browser_windows_page.py](pages/browser_windows_page.py) contains 'BrowserWindows' class with needed element locators and methods of interaction with them

[pages/links_page.py](pages/links_page.py) contains 'LinksPage' class with needed element locators and methods of interaction with them

[Elements/base_element.py](Elements/base_element.py) contains 'BaseElement' class with an element builder and methods for interaction with main elements on the pages

[Elements/elements.py](Elements/elements.py) contains all classes of main elements on the pages (for example: 'Button', 'Input', 'Caption', etc.) with methods for interaction with them

[tests/tests_demoqa.py](tests/test_demoqa.py) contains all Web UI tests for DEMOQA (https://demoqa.com)


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```


Note:
~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.
