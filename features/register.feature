
Feature: Registration Page

@register
   Scenario: Creating a account in SmartQA Page
     Given  User navigated to SmartQA CreateAccount page
     When   User should enter mandatory fields
     And User should click on the Register Cta

#     Then   I should get a proper warning message

#@emptyfields
#Scenario: Creating a account without providing the details
#     Given  User navigated to SmartQA CreateAccount page
#     When   User should not provide any details in the fields
#     And    User should click on the Register Cta
#     Then   User should get a proper warning message
#
#@existingmailid
#Scenario: Creating a account with the existing email id
#     Given  User navigated to SmartQA CreateAccount page
#     When   User should provide the existing email id details
#     And    User should click on the Register Cta
#     Then   User should get a proper warning message