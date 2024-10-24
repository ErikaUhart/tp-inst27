## request and response
## GET
```
### request

#### GET http://instagram.com/user?id=15

### response
 {
    "user": {
      "id": 15,
      "username": "erika.uh",
      "password": "123456uh",
      "email": "erikauhart@gmail.com"
    }
  }
  
```
## PUT
```
### request


 #### PUT http://instagram.com/user?id=15
   
  {
        "user": {
          "id": 15,
          "username": "erika.uh",
          "password": "789456er",
          "email": "erikauhart@gmail.com"
        }
  }

```
## POST
```
### request



 #### POST http://instagram.com/login
 
 {
  "email": "erikauhart@mail.com",
  "password": "789456er"
 }

 ### response
 {
  "mensaje": "inicio de sesion correcto",
  "user": {
    "id":15,
    "username": "erika.uh",
    "email": "erikauhart@gmail.com" 
  }
  }

```
## DELETE
```
### request

#### DELETE http://instagram.com/user?id=15

### response

http: 404 Not Found

