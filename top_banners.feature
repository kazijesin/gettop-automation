# Created by kazijesin at 8/8/21
#

Feature: User can see top banners
  #  User can click right and left arrows to see top banners;
#User can click bottom dots to see top banners
#User can click on product banner and is taken to correct category page


  Scenario: User can browse through top banners

    Given Open Gettop page
    When Click right & left arrow of the top banners
    And User can click bottom dots to see top banners
    When click on product banner
    Then Verify correct category page opens