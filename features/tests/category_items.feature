# Created by kazijesin at 8/8/21
  2 - "Showing all <N> results" is present and reflects correct amount of items (count amount of products on the page to verify this)
3 - All items have Category, Name and Price
4 - User can open and close Quick View by clicking on closing X
5 - User can click Quick View and add product to cart
#
Feature: Test Scenarios for Category functionality


  Scenario: Items of correct category are shown

    Given Open gettop page
    When Click on the categories
    And "Showing all {N} results" is present
    When All items have Category
    When All items have Name
    When All items have Price
    When User can open Quick View
    When User can close Quick view by clicking X
    Then User can click Quick View and add product to cart



