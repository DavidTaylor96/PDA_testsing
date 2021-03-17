### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
# No def __init__ statement

# card.value is not equated to 1 as there is only a single = sign
  def check_for_ace(self, card):
    if card.value = 1:
      return True
#else is not closed with a colon
    else
      return False
   
#method not defined due to typo, dif instead of def
#no comma seperating card1 and card2
  dif highest_card(self, card1 card2):
  #no indentatio of if statement
  if card1.value > card2.value:
    # returned card not card1
    return card
  else:
    return card2
# no section of the if statement for instances of a draw
  
# no indentation of full method
# total variable is not assigned as anything.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    #return statement inside for loop
    return "You have a total of" + total
    # total is an integer which can't be added to a string. Needs converted first or interpolated
  
```
