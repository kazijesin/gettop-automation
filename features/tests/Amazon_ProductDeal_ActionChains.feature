# Created by charjapadamin at 17/7/21
Feature: Amazon Product Page
  # Enter feature description here

  Scenario: User see the deals
    Given Open Amazon product page
    When Hover over new arrivals
    Then Verify user see the deals