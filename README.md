krisha\_testing
---------------

Description
-----------

This repository contains automated tests for the website krisha.kz. The tests cover functionalities such as registration, filtering products, changing the website language, sending messages to sellers, and submitting advertisements[](https://github.com/jacksylyk/krisha_testing).

Test Scenarios
--------------

1.  **Registration Test**
    
    *   Description: This test verifies the registration process on krisha.kz.
    *   Steps:
        
        1.  Navigate to the registration page.
        2.  Fill in the required details.
        3.  Submit the registration form.
        4.  Verify successful registration.
        
    
2.  **Filter Products Test**
    
    *   Description: This test validates the functionality of filtering products on krisha.kz.
    *   Steps:
        
        1.  Navigate to the product listing page.
        2.  Apply various filters.
        3.  Submit the filter form.
        4.  Verify the filtered results match the applied criteria.
        
    
3.  **Language Change Test**
    
    *   Description: This test ensures the language change feature works correctly on krisha.kz.
    *   Steps:
        
        1.  Locate the language settings.
        2.  Change the language to a different option.
        3.  Verify the language is updated.
        
    
4.  **Message Sending Test**
    
    *   Description: This test checks the functionality of sending messages to sellers on krisha.kz.
    *   Steps:
        
        1.  Find the messaging option on the seller's profile.
        2.  Compose a message.
        3.  Send the message.
        4.  Confirm the message is sent successfully.
        
    
5.  **Advertisement Submission Test**
    
    *   Description: This test validates the functionality of submitting advertisements on krisha.kz.
    *   Steps:
        
        1.  Navigate to the advertisement submission section.
        2.  Fill in the required details.
        3.  Submit the advertisement.
        4.  Verify the advertisement is successfully submitted.
        
    

Directory Structure
-------------------

*   `config.py`: Contains configuration settings for the tests.
*   `pages/`: Contains page object classes for different pages on krisha.kz.
*   `requirements.txt`: Lists the required Python dependencies.
*   `run_tests.py`: The main script to run the tests.
*   `tests/`: Contains the test scripts for each functionality.

Tools Used
----------

*   Python
*   Selenium

Setup Instructions
------------------

1.  Clone the repository.
2.  Install the necessary dependencies using `pip install -r requirements.txt`.
3.  Run the tests using `pytest -v -s --alluredir results`.
4.  Serve Allure to show results `allure serve results`.
