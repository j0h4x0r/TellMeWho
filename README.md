# TellMeWho

Search engines exploit knowledge graphs to provide meaningful and often "structured" information in response to user queries. Here we exploit knowledge graphs in the context of web search through infobox creation and question answering.

* With [Freebase Data](http://www.freebase.com/), the system receives a keyword query and returns as a result one appropriate infobox.
* The system can also answer a simple question "Who created [X]?".

## How to run?

### Dependency libraries (Python)

* urllib
* json
* OrderedDict

### To run the code:

* Basic mode : If you want to input a single query in string format "<q>"
```
-k <account_key> -q <query> -t [infobox|question]
```
* File input mode : If you have an input file with queries on each line
```
-k <account_key> -f <file_with_queries> -t [infobox|question]
```
* Interactive mode : If you want to keep inputing in terminal until you are done
```
 -k <account_key>
```

## System Design

The main.py takes in five type of input (k,q,t,f,h), we used `check_args()` function to extract the input mode and fields, also we provided instructions on how to use the system through `usage()` function.

For mode 1, we choose to run either `infobox.py` or `question.py` depending on the input parameter `-t`. If the user want to query infobox, the system pass api key and query to `run(api_k, query)` function inside `infobox.py`.

For mode 2, similar to mode 1, we run either `infobox.py` or `question.py` depending on the input parameter `-t`, for each line of the input file.

For mode 3, we wrote an infinite loop which will only break on KeyboardInterrupt (Control+D on mac). Inside each loop, we take in a raw input and check if its a "Who created"/"who created" question or others. If former, we call questions.py and if latter we call `infobox.py`.

### How `infobox.py` runs

First the `search(query)` function was called, querying Freebase API and return a list of mids, which may contain more types than required. So we have two helper functions `valid_topic()` and `cleanup_type()`, the former for filtering out the 6 categories amongst all mids, and the latter for resolving conflicted categories (eg. Author and League). Using the accepted mids, `topic()` function query Freebase API and get the data in Dict format.

Then, we call `assemble_infobox()` to format the Dict raw data into our own design - a Dict of lists, where lists can consist of text values or a nested layer of dicts. Inside these nested dicts, each key and value are a row of values of all sub-field under the outer layer. We used OrderedDict for this design, so that each output could have a certain output format. Also, for some entities that does not contain all the properties, we just put an empty list in the corresponding position.

At last, `printable()` function is called to display the data. 

### How question.py runs

First the `extractX()` function was called to get the query word, we only consider "Who created"/"who created" as valid input, and only query the API with the given two types ('Author', 'BusinessPerson').

Then, we call `MQLquery()` function to query the API. Noticed that same as the reference program, we provide table-like output for interactive mode, and text output for Basic and Fileinput mode. This distinction was implemented simply by calling `printable()` function for mode 3, whereas we just output lines of concatenated strings for mode 1 and 2.

### How printable.py works

This is a purely coded from scratch function for displaying beautiful tables and allowing nested columns. To make the table wider just change the whole parameter. The function first checks if the header data was passed in as parameter, so that we can print Name+Categories for infobox, and no such header for questions.

Then, for each key and value(list) in the given Dict, we check the type of (list[0]). If it is a Dict, then we have to divide the columns in terms of the nested fields we have. If not, we can simply print out the list values. All of these functionalities have taken automatically breakline into account to prevent table display overflow. 
