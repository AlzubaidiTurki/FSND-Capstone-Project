# Full Stack Nano Degree Capstone Project


## fate API
This project is for completeing the Full Stack Udacity Nanodegree program.\
I tried to make it.. well.. fun! something that I like and fan of. which is fate/ anime series.\
You can see how -if we continue developing- how it will look like from here [Star Wars API](https://swapi.dev/). \
Basically, the fate/ anime series is about a fight that happen in every period to fight over the Holy Grail, which grants you -almost- anything you want.\
the players (Masters) will summon historical figures (Servants), which can be real (such as alexander the great) or fictional but they are deep in some human culutre (such as greek gods).

## Live Server
This website is delpoyed in Heroku with this domain: https://fsnd-fate.herokuapp.com/ \
So basically you can intercat with it without any installation. However, see next section for local development
## Local Development
### Installation 
This program is based on Python, so you need to install it in your machine (please follow this [link](https://docs.python.org/3/using/index.html)
### Installing Dependencies 
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
### Running the program (On Windows)
Using the powershell, set the FLASK_APP enviormental variable to the file name of the app, run:  \
`$env:FLASK_APP=app.py `\
for conviences, you can set the FLASK_ENV variable to 'development' so every change in codes will automatically restart the server. run: \
`$env:FLASK_ENV="development"`\
after this, you can run the app using the following command\
`
flask run
`
### Deploy in Heroku
Making the API live with Heroku is as easy as using git!\
After installing Heroku CLI from here, run these commands \
`heroku create name_of_your_app`\
Copy the git url you will see after running the previous command, and then, run: \
`git remote add heroku heroku_git_url` \
Then, to connect the website with POSTGRES, run \
`heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application` \
Time to push!, run \
`git push heroku master` \
Now, we need upload our latest database schema (from migration), run: \
`heroku run python manage.py db upgrade --app name_of_your_application` \
At last, you should be able to see the API in the Heroku's account dashbaord. Click on it and go to settings, then reveal env vars, and add necessary enviorment varaible (as en setup.sh). \
That's it!

# Role and Premessions
There three possible clients that can use the API 
1. Public (anyone): They can only access the route page (/)
2. Masters: They can do what public can do, plus they can view other masters and servants.
3. Judge: They can do everything (in Anime, These Judge control and maintain the battles :) )

## JWT Token
For masters: \
 `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhDZWEyMlBZaGxKZ2xXbmhjckRNdiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zYW1zbmotMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzMzY4NzlmNDNhNjIwMDZhOGQ3MzkwIiwiYXVkIjoiZmF0ZSIsImlhdCI6MTYzMTI4MzgzNCwiZXhwIjoxNjMxMzcwMjM0LCJhenAiOiIzTWpjTnJ3ZDNkejN0emllVVZWRzlKRXNmVXdDMmxZciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0Om1hc3RlcnMiLCJnZXQ6c2VydmFudHMiXX0.c88q3_gyrJvtXbWAFfT_BoZWzlgv42DcaECuqZ6U9puB9hjV6RO-BfYCNDDVqpXVihEpTrSgURWcr43ti-xmSVkIoz_mCSBECgdZaKskp-856_HcD_oH_koZ4ZJTq_tOjXd8HvEOeApEmmBWJFqVG0bca8c2jM6M3bUBGY3gbgFoyWBk7ItCqeWLuIPeY_6LBlPussd1Ses2ehiV96YFGucj5DkDUQlHGw8oVvJWz9YOkQ5XM8rGtVCMpdwduQr-vdFHXY4xZpxBLQC8EDHJyOQ0wS70pU3X5cUH_nIUOzObrDsdythC6CAeoUNdR5lpznd5etQGveYrplrrNReMCg ` \
 for Judge \
 `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhDZWEyMlBZaGxKZ2xXbmhjckRNdiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zYW1zbmotMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzMzY4NWE4ZmZiNzQwMDcxZDllYTYxIiwiYXVkIjoiZmF0ZSIsImlhdCI6MTYzMTI4MzY4NCwiZXhwIjoxNjMxMzcwMDg0LCJhenAiOiIzTWpjTnJ3ZDNkejN0emllVVZWRzlKRXNmVXdDMmxZciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm1hc3RlcnMiLCJkZWxldGU6c2VydmFudHMiLCJnZXQ6bWFzdGVycyIsImdldDpzZXJ2YW50cyIsInBhdGNoOnNlcnZhbnRzIiwicG9zdDptYXN0ZXJzIiwicG9zdDpzZXJ2YW50cyJdfQ.uPg_21228UkMaqLSKbci1L37fyAsMgCzm3P-92fUmaKBxexug5hpvoWHxlVoxFmLtgsntcCDBTF454IDzs5fhFl1Vlgr6sF7nkA5UIo9C6fjsHNyvBSjpaTVjj3kTMlD7z6AFcfajqbwP-B08Lm7tFRNblud199-KThypzuMBM1uPBWtOjQaqClsIRgEgwry6Kgx78nPDSXXrlChlmYy7LhFqCMnxNkxw5VKcUt-ThX27HbPaPFQ0ciUtlKl0-yqq0kwyDkzGQ5rbGTtnsEuCe8kxppDehhjXPsqg50pAaFogW4ncSlCfjLzk9fC239ZgJFyJ5KhQEqG-uTPNV4dUA ` 

# API Documenation

## Endpoints
### GET /
* Return a the main page of our website, note that this is the only thing public people can see :) \
Sample input:
`
 curl -i -X GET -H 'Content-type: application/json' http://localhost:5000 `\
Sample Output: \
`
 Welcome to the Holy Grail Battle page!
 This battle should be a secret to public, you need to login as a master to view other masters and servants :) `
### GET /servants
* Return a list of all servants in the database.\
Sample Input: \
`
curl -i -X GET -H 'Content-type: application/json' -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/servants `\
Sample output: \
`
{
    "servants": [
        {
            "master": null,
            "name": "",
            "source": "",
            "type": "test_saber"
        },
        {
            "master": null,
            "name": "Achilles",
            "source": "",
            "type": ""
        },
        {
            "master": null,
            "name": "FSND",
            "source": "",
            "type": "Saber"
        }
    ],
    "success": true
}
`

### GET /masters
* Return a list of all masters in the database. \
Sample input: \
`
curl -i -X GET -H 'Content-type: application/json' -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/masters `\
Sample Output: \
`
{
    "masters": [
        {
            "image": "",
            "name": "Hatem"
        },
        {
            "image": "https://2img.net/h/pre15.deviantart.net/75f5/th/pre/i/2015/079/1/0/rin_tohsaka_by_deikawn-d8fer1i.png",
            "name": "Tohsaka Rin"
        },
        {
            "image": "https://static.myfigurecollection.net/pics/encyclopedia/4380.jpg?rev=1297513293",
            "name": "Kotomine Kirei"
        }
    ],
    "success": true
}
`
### POST /servants
* Insert new servant in the database. \
Sample Input: \
`
curl -i -X POST -d '{"name" : "{NAME_HERE}"} -H 'Content-type: application/json' -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/servants` \
Sample Output: \
`
{
    "servants": [
        {
            "master": null,
            "name": "",
            "source": "",
            "type": "test_saber"
        },
        {
            "master": null,
            "name": "Achilles",
            "source": "",
            "type": ""
        },
        {
            "master": null,
            "name": "FSND",
            "source": "",
            "type": "Saber"
        }
    ],
    "success": true
}
`
### POST /masters
* Insert new master in the database. \
Sample input:\
`
curl -i -X POST -d '{"name" : "{NAME_HERE}"} -H 'Content-type: application/json' -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/masters `\
Sample output: \
`
{
    "masters": [
        {
            "image": "",
            "name": "Hatem"
        },
        {
            "image": "https://2img.net/h/pre15.deviantart.net/75f5/th/pre/i/2015/079/1/0/rin_tohsaka_by_deikawn-d8fer1i.png",
            "name": "Tohsaka Rin"
        },
        {
            "image": "https://static.myfigurecollection.net/pics/encyclopedia/4380.jpg?rev=1297513293",
            "name": "Kotomine Kirei"
        }
    ],
    "success": true
}
`
### PATCH /servants/<servant_id>
* Update a servant based on its ID. \
sample input: \
`curl -i -X PATCH -d '{"name" : "{NAME_HERE}"} -H 'Content-type: application/json' -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/servants/{servant_id} `\
Sample Output: \
`
{
    "servants": [
        {
            "master": null,
            "name": "",
            "source": "",
            "type": "test_saber"
        },
        {
            "master": null,
            "name": "Achilles",
            "source": "",
            "type": ""
        },
        {
            "master": null,
            "name": "FSND",
            "source": "",
            "type": "Saber"
        }
    ],
    "success": true
}
`
### DELETE /servants/<servant_id>
* Delete a servant based on its ID. \
Sample input: \
`curl -i -X DELETE -H 'Content-type: application/json' -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/servants/{servant_id}` \
Sample Output: \
`
{
    "servants": [
        {
            "master": null,
            "name": "",
            "source": "",
            "type": "test_saber"
        },
        {
            "master": null,
            "name": "Achilles",
            "source": "",
            "type": ""
        },
        {
            "master": null,
            "name": "FSND",
            "source": "",
            "type": "Saber"
        }
    ],
    "success": true
}
`
### DELETE /servants/<master_id>
* Delete a master based on its ID. \
sample input: \
`curl -i -X DELETE -H 'Content-type: application/json' -H "Authorization: Bearer {INSERT_TOKEN_HERE}" http://localhost:5000/masters/{master_id}`\
Sample output: \
`
{
    "masters": [
        {
            "image": "",
            "name": "Hatem"
        },
        {
            "image": "https://2img.net/h/pre15.deviantart.net/75f5/th/pre/i/2015/079/1/0/rin_tohsaka_by_deikawn-d8fer1i.png",
            "name": "Tohsaka Rin"
        },
        {
            "image": "https://static.myfigurecollection.net/pics/encyclopedia/4380.jpg?rev=1297513293",
            "name": "Kotomine Kirei"
        }
    ],
    "success": true
}
`



# Acknowledgemnt
I would like to thank my mentor Mashael for always supporting us, her students. I would also thank my colleagues Saud and Najla for helping me discovring few bugs in previous FSND projects, lastly I would like to thank MISK, for making those helpful interships for us!.
