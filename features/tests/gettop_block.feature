# Created by kazijesin at 9/8/21
#  You may also like…" bock is shown and contains products
#Product links under "You may also like…" bock are clickable and take to correct pages

Feature: You may also like block and it's function
  # Enter feature description here

  Scenario: User can see you may also like block & the products
    Given Open Gettop page
    When Click on a product
    When You may also like block is shown
    When Click link under the block
    Then Verify it opens the correct page
