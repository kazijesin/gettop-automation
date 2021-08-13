# Created by Kazi Jesin at 6/8/21
  #"Browse Our Categories" text is shown
#4 correct categories are shown
#Upon clicking on each category, correct page opens


Feature: Browse Gettop categories

  Scenario: User can browse categories
  Given Open Gettop page
  When "Browse Our Categories" text is shown
  When Expected {4} categories are shown
  Then User can click on each category and Verify correct page opens



