# TarotReadings

## Resource

**Readings**
Attributes:
- Question (string)
- Card (string)
- Description (string)
- Imagepath (string)
- Rating (int)

**Users**
Attributes: 
- First Name (string)
- Last Name (string)
- Email (string)
- Password (string)

## Schema

``` sql
CREATE TABLE readings (
    id INTEGER PRIMARY KEY,
    card TEXT,
    question TEXT,
    description TEXT,
    image TEXT,
    rating INTEGER);

```

```sql
CREATE TABLE usere (
    id INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    email TEXT,
    password TEXT);
```

## Password Hashing Method
**BCRYPT - B2,**
**SALT ROUNDS = 12**




## REST Endpoints

Name                          | Method   | Path
------------------------------|----------|------------
Retrieve reading collection   | GET      | /readings
Retrieve reading member       | GET      | /readings/*\<id\>*
Create reading member         | POST     | /readings
Update reading member         | PUT      | /readings/*\<id\>*
Delete reading member         | DELETE   | /readings/*\<id\>*
Create User                   | POST     | /users
Create Session                | POST     | /sesions
