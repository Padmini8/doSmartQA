Feature: SmartQA LOGIN

@login
  Scenario Outline: Login to SmartQA
    Given  I launch the chrome browser
    When   I open SmartQA Homepage
    And    Enter username "<username>" and password "<password>"
    Then   Click on login button
#   Then User must successfully login to the project page
    Then   I am on the dropdown page
    Then   I select option "{option}" from the dropdown
    And    Click on the Open project cta
    And    User successfully reached to dashboard
    And    User successfully Logout from dashboard
   Examples:
     | username  | password  |
     | HARIKA    | Harika@97 |

#@invalid
Scenario Outline: Login to SmartQA with Invalid credentials
    Given  I launch the chrome browser
    When   I open SmartQA Homepage
    Then   I enter invalid username "<username>"and password "<password>"
    Then   Click on login button
    Then   I should get a proper warning message
  Examples:
    | username | password |
    | HARIKA   | Harikaa  |

#@Emptyfields
  Scenario: Login without entering credentials
    Given  I launch the chrome browser
    When   I open SmartQA Homepage
    Then   I dont enter anything into username and password fields
    And    Click on login button
    Then   User should receive a Oops warning message

