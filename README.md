# Password finder

## Finds the password for the serial number

#### This program asks the user to input their serial number and will print the corresponding password.

#### the way it works is it formats each line by removing whitespace and indexing is used to indicate which part of the line is the serial number/ password. This means that the text file needs to be formatted in a certain way for this to work.

#### The program iterates through each line, not stopping once it has found a match, as there may be duplicates further down the list, in which case, the password will be updated.