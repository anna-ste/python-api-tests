Feature: Trading pairs
  As a user
  In order to trade
  I should be able to get public info about trading pairs

  Scenario: Retrieve public data about some trading pair
    Given I am a user
    When I request public info about trading pair XBT/USD
    Then I should get 200 status code
    And Response data should be about XBT/USD trading pair
    And Trading_pair json schema should be valid