# AND and OR Operator
In Python, AND and OR are logical operators used to combine multiple conditional statements in programing
# AND operator 
returns True value "only if both conditions are true".

# OR operator 
returns True value "if at least one condition is true".
# Not operator
If the expression evaluates to True, not makes it False. If it is False, not makes it True
# Truth table of AND and OR
*Expression*    |*Result* |*Condition*
-------------------------------------------
True And true   | True    | both must be true
True And Faulse | False   | one faulse brakes it
True Or Faulse  | True    | one have to be true 
Faulse Or Foulse| false   | both most be false to fail
Not True        | false   | not changes true value to false
Not false       | True    | not changes false value to true
------------------------------------------------


what if a decision depends on multiple things being true at the same time? Or what if it's an "either/or" situation?

This is where Logical Operators come in. We have three main ones in Python:
# recall 
And: BOTH conditions must be True. If even one is False, the whole thing fails.
OR: ONLY ONE condition needs to be True. If the first one is True, it doesn't even care about the second one.
Not: This reverses whatever the answer is. If it was True, not makes it False.

# practice question using And Operator  
(The Strict Owambe Bouncer): 
To enter the VIP section of this Lagos wedding, the bouncer has two rules: 
1 You must have the IV card  AND
2 you must be wearing the correct Aso-Ebi. 

If you have the IV but you are wearing jeans, you are bouncing back home!

