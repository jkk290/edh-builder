# EDH Builder

A Python CLI app for building and managing Magic The Gathering EDH/Commander decks

## Builder Mode Syntax

`q`  
Exit back to the previous menu

`add <card name> [-qty]`  
Add card to the deck list. If no qty is entered, default is 1.  
Example:  
`add Cyclonic Rift` (Add 1x Cyclonic Rift to the deck list)  
`add Island -15` (Add 15x Island to the deck list)  

`delete <card name> [-qty]`  
Remove card from the deck list. If no qty is entered, the card and all copies are removed. If qty is entered, subtracts qty from the total copies in the deck list. Removes card if qty reaches 0.  
Example:  
`delete Cyclonic Rift` (Removes Cyclonic Rift from deck list)  
`delete Island -5` (Removes 5 copies of Island from deck list)  

`show deck`  
Prints the current desk list  

`save deck`  
Writes the current deck list to the deck file as a csv. CSV format is cardname, type, qty.  
Example:  
"Yuriko, The Tiger's Shadow",commander,1  
Cyclonic Rift,,1  
Island,,15  
