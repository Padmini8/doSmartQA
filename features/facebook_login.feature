Feature: Facebook login functionality

  @logincase
  @sanity
  Scenario: Test login with incorrect credentials
    When user input wrong credentials
    Then Error message will come


