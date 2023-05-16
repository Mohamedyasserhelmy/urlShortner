### URL_Shortner Project Specification

**Description : A Flask application with react js in frontend which takes long url and convert it into smaller one **

###### **1- Project Architecture** 

![](/assets/system_Arch.png)

**As we can see in figure-1 we have a flask server up and running to serve 4 main endpoints **

###### 2- API Documentation

|            url             |                    specification                     |
| :------------------------: | :--------------------------------------------------: |
|    **GET** /shortlinks     |               **list all short links**               |
|   **POST**  /shortlinks    |          **add new shortlink to database**           |
| **put** /shortlinks/{slug} |                 **update document**                  |
| **GET** /shortlinks/{slug} | **get specific shortlink (to be used in frontend )** |

**you can find the actual API testing results from this link** : [https://documenter.getpostman.com/view/26760066/2s93kxcRxR]()

###### 3- How to Run ? 

1. **Activate the python environment** 

   `cd urlShortnerFlask` 

   `source /bin/activate`

2. **Run flask server**

   `flask --app app run --debug`

   Now we can ping our app on link : [http://127.0.0.1:5000]()

3. **Run React JS front-end **

   `cd templates/src/app.js`

   `npm start`

   Now we can see our app is up and running on link : [ http://localhost:3000/]()

![](/assets/Screenshot from 2023-05-17 02-41-57.png)

**As we can see we can Enter the URL we want to shorten using this form** 









