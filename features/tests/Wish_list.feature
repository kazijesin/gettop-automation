# Created by kazijesin at 7/8/21
  #"No products added to the wishlist'" shown if no product were added to the list

  #please note no wish list or save for later option was available. So i worked with cart button

Feature: Gettop Wish list


  Scenario: User can see no products added to the wishlist

    Given Open Gettop page
    When Click on cart icon
    Then Verify Your cart is currently empty is shown
