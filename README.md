# 1.1.6Magpie-Thai

The gist of how this chatbot works is that it looks for keywords in sets. Each keyword in the first set is connected to another
set of keywords, and each of those keywords are connected to their own set. 

It checks the input with the against the first set, and if it finds one of the keywords, it then checks the input again against
the set related to the previously found keyword, then checks again using the set from the second keyword found. Once the third 
keyword is found, it returns an appropriate response with the keywords it has gathered. 

Python dictionaries are useful for this because they similar to arrays and arraylists in that they store other elements; 
Additionally, like arraylists, dictionaries are able to edit their content and length even after initialization. The difference 
is that unlike arrays, dictionaries are unordered. Elements stored inside of it are assigned to a string "key" instead of an 
index— rather, the "keys" are assigned an object. Using this you can fill a dictionary with the first set of keywords, then 
assign each of them with another dictionary with the another set of keywords, then correspond these keywords with appropriate 
responses. 

For instance:

| Set A (Dictionary) | Set B (Dictionary) | Set C (Dictionary) | Responses (String) |
| --- | --- | --- | --- |
| Keyword A1 | Keyword B1 | Keyword C1 | Response 1| 
|            |            | Keyword C2 | Response 2|
|            |            | Keyword C3 | Response 3|
|            | Keyword B2 | Keyword C1 | Response 4|
|            |            | Keyword C2 | Response 5|
|            |            | Keyword C3 | Response 6|
| Keyword A2 | Keyword B1 | Keyword C1 | Response 7| 
|            |            | Keyword C2 | Response 8|
|            |            | Keyword C3 | Response 9|
|            | Keyword B3 | Keyword C1 | Response 10|
|            |            | Keyword C4 | Response 11|
|            |            | Keyword C5 | Response 12|

The columns represent the elements within a dictionary (For example, Set B represents the elements within a dictionary assigned 
to a keyword to Set A, and each keyword in Set B is assigned to another dictionary filled with elements assigned to keywords 
from Set C)

If an input included Keywords A2, B1, and C3, the chatbot would look for keywords from Set A, until it finds A2. Then it would 
check the input statement for words from the dictionary assigned to key A2, until it finds B1. It would repeat with 12's 
dictionary, and once it finds C3, it would return the corresponding response, number 9.

The reason this chatbot was made in python was to be able to use the dictionary, so that the responses could be organized based
on what keywords were being looked for. 
