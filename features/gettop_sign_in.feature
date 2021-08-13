# Created by charjapadamin at 10/7/21
Feature: Logged out users sees sign in page


  Scenario: Logged out users sees sign in page when clicking Orders
  Given Open gettop page
  When Click  Orders link
  Then Verify page has Sign-In

    Scenario: Amazon footer has correct amount of links
    Given Open Amazon page
    #Then Verify 48 footer links are displayed
   # Enter feature name here
  # Enter feature description here

  #Scenario: User can select blouse colors
  #Given Open Amazon product B07NF5WGQ1
  #Then Verify user can click through colors
  # Enter scenario name here
    # Enter steps here


