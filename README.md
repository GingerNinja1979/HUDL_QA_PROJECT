# Hudl_QA_Project

----
 
**Project Description**

This repository contains automated tests for José Mello to validate Hudl.com login functionalities.

These automated tests are designed to ensure the application works correctly and consistently.

----------

**Prerequisites**

Before you begin, ensure you have the following prerequisites installed:

Python (version 3.9)

Selenium (version 4.14.0)

Web browser driver for Google Chrome

**Running Tests**

The project employs various environment variables to conceal sensitive data. An `env.py` file can be found within the route page. 

To ensure the project functions correctly, you'll need to provide your:

- email

- password

Once inside the HUDL_QA_PROJECT folder, the following command can be used to run the tests.

`pytest`

-------


**Test Cases**



| Test Case             | Description                                                            | Expected Outcome |
|:----------------------|------------------------------------------------------------------------|------------------|
| Valid Login           | Test logging in with a valid username and password.                    |       Verify that the user is successfully logged in and redirected to the expected page           |
| Invalid Login         | Attempt to login with an invalid username and a valid password         |       Verify that appropriate error messages are displayed in each case           |
| Invalid Login         | Attempt to login with a valid username and an invalid password         |          Verify that appropriate error messages are displayed in each case        |
| Invalid Login         | Attempt to login with both an invalid username and an invalid password |    Verify that appropriate error messages are displayed in each case              |
| Blank Fields Handling | Attempt to login with both username and password fields left blank     |       Verify that an error message is displayed for each empty field                                                                            |
| Using the Enter Key   | Attempt to login using the enter key                                   |         Verify that the user is successfully logged in and redirected to the expected page                                                                                                                                        |
