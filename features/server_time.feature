Feature: Server time
  As a user
  In order to be informed
  I should be able to retrieve server time

  Scenario: Retrieve server time
    Given I am a user
    When I retrieve server time
    Then I should get 200 status code
    And Server time should have %a, %d %b %y %H:%M:%S +0000 time format
