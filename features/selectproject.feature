Feature: project page

#  Background:
#    Given I am logged in to SmartQA with username "HARIKA" and password "Harika@97"

  Scenario Outline: Perform some action after login
    Given I am on the dropdown page
    When I select option "{option}" from the dropdown
    Then The selected option should be "{expected_option}"
    And User successfully reached to dashboard
    And User successfully Logout


    Examples:
      | option  | project     |
      | EDVANZA | EDVANZA 1.0 |