# TokoinChallenge

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/InNoobWeTrust/tokoin_challenge)

Data searching challenge.

Assumptions:
- json data is valid
- Each json data is an array
- Open and closing bracket is on its own line
- key-value or array's item is on its own line

Searching strategy:
- Stream file content line by line
- On open bracket, begin storing values in temporary object store in memory
- Check for value matching with search term when iterating each line. If yes raise a flag so that object will be printed
- On closing bracket, if the flag is raise, print the object in memory. And either printing object or not, clear memory to process new object
- On closing square bracket, stop processing
