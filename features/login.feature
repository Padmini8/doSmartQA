Feature: SmartQA LOGIN

@login
  Scenario Outline: Login to SmartQA
    Given  I launch the chrome browser
    When  I open SmartQA Homepage
    And   Enter username "<username>" and password "<password>"
    Then  Click on login button
    Then User must successfully login to the project page
    Then  I am on the dropdown page
    Then I select option "{option}" from the dropdown
    And Click on the Open project cta
    And User successfully reached to dashboard
    And User successfully Logout

    Examples:
     | username  | password  |
     | HARIKA    | Harika@97 |
#     | HAARIKA   | Harika@97 |
#     | @13453r2y | Harika    |

#@project
#  Scenario Outline : creating a project
#    Given  I launch the chrome browser
#    When  I open SmartQA Homepage
#    Then I am on the dropdown page
#    When I select option "{option}" from the dropdown
#    Then The selected option should be "{expected_option}"
#    And  User successfully reached to dashboard
#    And  User successfully Logout
#
#    Examples:
#      | option  | project     |
#      | EDVANZA | EDVANZA 1.0 |
