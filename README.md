Project keywords: Python Flask, API, JavaScript, Jquery, NoSQL, HTML

Python Flask and JavaScript REST API with MongoDB.
This has been done mainly for my own purposes, i.e. testing my MongoDB databases.
The main idea is that you can access multiple mongoDB databases with a single program using api calls or an html interface.

Main features

The program can search all mongodb databases and their collections on the computer. After the search, the user can select them for use via the HTML user interface.
you can perform CRUD operations on the database you have selected. Selecting a database is easy, select a database from the dropdown menu and click the Select button
Various API calls like search or delete by id, name, etc. are also available.
You can choose whether you want to see the data in json format or in text format on the html page.

JQUERY functions facilitate CRUD operations. With this program, you don't need to enter the object ID, just click on it and it will go to the input field. speeds up, for example, the deletion of records from the database

Python and JavaScript collaboration, among others:

The Python function counts the number of fields in the MongoDB collection and the Javascript function creates the same number of input fields (with the createElement method) in the html user interface. the end result is the right number of input fields for adding a new record or editing an old record.

Database statistics, see the number of collections, sizes of collections and databases, etc.
Some of the database statistics are now available graphically. Made with the ChartJS library.

Customization options, in the reading view you can choose whether you want to see the database data in the table, in small or large font, and the background color of the table can also be changed.

JavaScript search function. The function uses the window.find method and highlights the found words in yellow. the function also stores the searched words in a table and displays them to the user.
The function also shows some statistics about the searched words, for example the number of characters of the longest and shortest words and the number of characters of both words

