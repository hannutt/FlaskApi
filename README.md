Python Flask and JavaScript REST API with MongoDB.
This has been done mainly for my own purposes, i.e. testing my MongoDB databases.
The main idea is that you can access multiple mongoDB databases with a single program using api calls or an html interface.

Main features

The program can search all mongodb databases and their collections on the computer. After the search, the user can select them for use via the HTML user interface.
you can perform CRUD operations on the database you have selected. Selecting a database is easy, select a database from the dropdown menu and click the Select button
Various API calls like search or delete by id, name, etc. are also available.
You can choose whether you want to see the data in json format or in text format on the html page.

JQUERY functions facilitate CRUD operations. for now you don't need to enter the objectID number, just click it and it will go to the input field.

Python and JavaScript collaboration, among others:

The Python function counts the number of fields in the MongoDB collection and the Javascript function creates the same number of input fields (with createElement method) in the html interface. A ready basis for adding a new record or editing an old record.

Database statistics, see the number of collections, sizes of collections and databases, etc.

