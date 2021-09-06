# Full Stack Nano Degree Capstone Project


## fate API
This project is for completeing the Full Stack Udacity Nanodegree program.\
I tried to make it.. well.. fun! something that I like and fan of. which is fate/ anime series.\
You can see how -if we continue developing- how it will look like from here [Star Wars API](https://swapi.dev/). \
Basically, the fate/ anime series is about a fight that happen in every period to fight over the Holy Grail, which grants you -almost- anything you want.\
the players (Masters) will summon historical figures (Servants), which can be real (such as alexander the great) or fictional but they are deep in some human culutre (such as greek gods).\

## Live Server
This website is delpoyed in Heroku with this domain: https://fsnd-fate.herokuapp.com/ \
So basically you can intercat with it without any installation. However, see next section for local development
## Local Development
### Installation 
You can install all needed libraries to run the website. simply run:\
`
pip3 install -r requirements.txt
`
### Linking Database
you can link your own database by making envoirment variables using these nams: \
`
DB_HOST
`,
`
DB_USER
`,
`
DB_PASSWORD
`,
`
DB_NAME
`
if any of these variables does not exist, a defualt value will be assigned, and they are:\
`
DB_HOST = '127.0.0.1:5432'
`
`
DB_USER = 'postgres'
`
`
DB_PASSWORD = 'postgres'
`
`
DB_NAME = 'fate'
`
### Dummy Data
you can run `python seeder.py` to insert some data in the database to start interacting with the API!
### Running the program
Run (on Windows) \
`$env:FLASK_APP=app.py `\
`
flask run
`
# Role and Premessions
There three possible clients that can use the API \
1. Public (anyone): They can only access the route page (/)
2. Masters: They can do what public can do, plus they can view other masters and servants.
3. Judge: They can do everything (in Anime, These Judge control and maintain the battles :) )

## JWT Token
For masters: \
 `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhDZWEyMlBZaGxKZ2xXbmhjckRNdiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zYW1zbmotMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzMzY4NzlmNDNhNjIwMDZhOGQ3MzkwIiwiYXVkIjoiZmF0ZSIsImlhdCI6MTYzMDk0MDYwMywiZXhwIjoxNjMxMDI3MDAzLCJhenAiOiIzTWpjTnJ3ZDNkejN0emllVVZWRzlKRXNmVXdDMmxZciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0Om1hc3RlcnMiLCJnZXQ6c2VydmFudHMiXX0.h01d5qlon4fjEEcJOn59oYW9a0k39pOk4EY7hKP4pNPi1a8qSKVPRLIlg3GYCjvS1zhY7TcH2db7y0azMbul5_aASmj3WNlJp4ksK5BtfL0a7KMNNwclK22OODzboOBwIbHFA8I0wUHJ75VpMlOx_rW3WaABzlFBIE2T_gop1BdBbt31bilbLesOJ-vvrQSE6O7_-_cn4Ipq0kffPHu7JeXD9W-LT5J4CfezOAn9DlN67VnnXVSRJ9Sa2h4nhBSdwEBYY3rhTKUp3C1YyMjADa8v-Bh4R_QKBp20PePwn85D8dxwdpBBdmbzCk_WoWqjJZwtrlRWwKRU-P1ZZNeDLA ` \
 for Judge \
 `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhDZWEyMlBZaGxKZ2xXbmhjckRNdiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zYW1zbmotMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXVa0DB8NjEzMzY4NWE4ZmZiNzQwMDcxZDllYTYxIiwiYXVkIjoiZmF0ZSIsImlhdCI6MTYzMDk0MDY0MCwiZXhwIjoxNjMxMDI3MDQwLCJhenAiOiIzTWpjTnJ3ZDNkejN0emllVVZWRzlKRXNmVXdDMmxZciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm1hc3RlcnMiLCJkZWxldGU6c2VydmFudHMiLCJnZXQ6bWFzdGVycyIsImdldDpzZXJ2YW50cyIsInBhdGNoOnNlcnZhbnRzIiwicG9zdDptYXN0ZXJzIiwicG9zdDpzZXJ2YW50cyJdfQ.bwM8YyoC076JHctrku1ICHczCEGqSTc-XDS8bnyhvN3Lj7bTYUS9ZQRSOoVMXVSaiMhSTNqv6ExnZ9TF1PlktrG8KUyIGWM8g9LYkH1G1_6w1Sve3NBbXNfrSWm_BF8aW8CjF5igsd7L4Ji5UZlI3nAO94Q44j888PNPeyPX13QBnqbHGF2nx2VxKUkoIa6BRQGvH88D3ts8X8y1YL2UdFAVi88Q524lkwGNkVCbcES4Rg_yr2mWPqzeqj0vq1jymVEUVjQFakEgv6HZKgMW04FCeIOGOaiKmcbniwDbFm1UW8MrDxD5Z9Z2Sn36YAeKCzd4DBjatwg43-cQLfJcjA ` \

# API Documenation

## Endpoints
### GET /
* Return a the main page of our website, note that this is the only thing public people can see :)
### GET /servants
* Return a list of all servants in the database.
### GET /masters
* Return a list of all masters in the database.
### POST /servants
* Insert new servant in the database.
### POST /masters
* Insert new master in the database.
### PATCH /servants/<servant_id>
* Update a servant based on its ID.
### DELETE /servants/<servant_id>
* Delete a servant based on its ID.
### DELETE /servants/<master_id>
* Delete a master based on its ID.

You can see all these interactions with different roles in the postman workspace.


# Acknowledgemnt
I would like to thank my mentor Mashael for always supporting us, her students. I would also thank my colleagues Saud and Najla for helping me discovring few bugs in previous FSND projects, lastly I would like to thank MISK, for making those helpful interships for us!.
