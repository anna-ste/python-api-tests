Feature: Open orders
  As a trader
  In order to trade
  I should be able to retrieve open orders

  Scenario: Retrieve empty list of open orders
    Given I am an authenticated user
    When I retrieve open orders
    Then I should get 200 status code
    Then I should get empty list of opened orders