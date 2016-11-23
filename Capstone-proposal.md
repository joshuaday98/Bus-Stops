# Public Transit Locator

## Overview:

##### This simple to operate apps lets any user in the Portland Metro area to find a Trimet stop near them.

## MVP:

* Allow users to create their own account and set a home location.
* Allow users to select the radius they would like to search for stops in.
* Create an attractive front-end.
* Add functionality for the New York transit system.

## Data Model:

##### We will need to save the data for the New York transit in our database to prevent having to read the CSV containing every stop each time we have to search.

##### The Users model will also need to be saved to the data base to allow users to create their own home location and various other features.

## Technical Components:

##### Python:
    Python is used for the general backend and processing. All calculations and interacting with most REST API's is done with Python.
    Dependencies:
      * Django
      * Geopy
      * requests

##### Javascript:
    Javascript is used to interact with the Python in the back and used to dynamically update the page using Google's Maps API.
    Frameworks/API's:
      * jquery
      * Google Maps JS API

##### HTML:
    HTML is how you see my webpage!

##### CSS
    Make that webpage look pretty.

##### Markdown
    Markdown is used for the documentation.

## Schedule:

1. Complete desired functionality for the Trimet system (adding busses to the map, allowing a user to select the search distance).
2. Move the entire New York transit system data into my database.
3. Using geopy make a formula for creating a boundary around a point for the New York system.
4. Develop an effective way to search for every stop in the boundary using my data base.
5. Create Users and allow them to create their own home location and default distance.

## Further Work:

* Add other major cities. (Seattle, LA, Etc.)
* Possibly an android app? More realistic usage as an app.
* Add the busses arrival time in real time
