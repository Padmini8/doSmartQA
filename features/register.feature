Feature: Register Account functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register page
    When I enter mandatory fields
    And I select privacy policy option
    And I click on continue button
    Then Account should get created

  Scenario: Register with all fields
    Given I navigate to Register page
    When I enter details into all fields
    And I click on continue button
    Then Account should get created

  Scenario: Register with a duplicate email fields
    Given I navigate to Register page
    When I enter details into all fields except email field
    And I enter existing accounts email into email field
    And I click on continue button
    Then Proper warning message informing about duplicate account should be displayed

  Scenario: Register without providing any details
    Given I navigate to Register page
    When I dont enter anything into the fields
    And I click on continue button
    Then Proper warning messages for every mandatory fields should be displayed

