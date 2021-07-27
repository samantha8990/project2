# Data Visualization Project

Group Members:
Arianne, Ashley, Samantha, & Bitty

Objective: To tell a story with data and create unique visualizations on a dashboard that we create.

Chosen Topic: Serial Killers
We selected a serial killer dataset because we were curious if there were certain regions that had more serial killers than others and if any time frames were more dangerous. Originally, we had a dataset with unsolved and solved serial murders in the United States from 2015-2019. We had to scale down our data to accomodate heroku's data limits for a free account so we decided to look at the smallest dataset possible: unsolved murders from the year 2016. It comforted us that the unsolved murders did account for the lowest numbers within our original dataset. 

Process:
We utilized DBeaver to create a SQL database that was able to connect to heroku to host our app.  Within DBeaver we imported and merged our two csv murder data and our coordinates for city locations in the U.S. 

We then got to work on creating our app.py file to connect our database to our javascript visualization files. We then created different html files to host the visualizations to enable the interactive portion of the project. 

Future Considerations:
If we had more time to work on this project, we would like to add a map layer that allows us to toggle between hotspots of solved vs. unsolved murders per year. That way we could see if there are any trends between months where crime tends to be high in the U.S. and see if murder weapons vary between unsolved and solved cases.

Resources:
Data:
https://www.kaggle.com/vesuvius13/serial-killers-dataset
https://en.wikipedia.org/wiki/List_of_serial_killers_in_the_United_States
https://sarcadass.github.io/granim.js/examples.html

Images:
https://wallpaperaccess.com/blood
https://www.svgrepo.com/svg/11497/knife-with-blood
https://svg-clipart.com/thumbs/red/nmOO979-blood-clipart.jpg
