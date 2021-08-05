# Created by charjapadamin at 3/7/21
Feature: Test Gettop search

Scenario: User can search for a product
  Given Open Gettop page
  When Click on Gettop search icon
  When Input Ipad in search field
  Then Verify search worked for "Ipad"

