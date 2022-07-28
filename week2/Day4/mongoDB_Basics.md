## MongoDB Basics
### Check monosh Version
``` mongosh --version ```

### Start the Mongo Shell
``` mongosh ```

### Show Current Database
```db ```

### Show All Databases
``` show dbs ``` 

### Create Or Switch Database
 ``` use hamada ``` 

### Drop Database
 ``` db.dropDatabase() ``` 

### Create Collection
 ``` db.createCollection('friends') ``` 

### Show Collections
 ``` show collectionName ```
## Insert Document

``` sql
 db.messages.insert ({ 
    sender:{id:1,name:'ahmed',age:31,city:"New York"}, 
    reciever:{id:1,name:'mohmmed',age:20, city:"egypt"},
    message:{"content":"Hello World"}
  })
```

## Find All Documents
``` sql
db.posts.find()
```

## Find Documents with Query

``` 
db.posts.find({ category: 'News' })
```

## Sort Documents
### Ascending
```
db.posts.find().sort({ title: 1 })
```
### Descending
```
db.posts.find().sort({ title: -1 })
```
## Count Documents
```
db.posts.find().count()
db.posts.find({ category: 'news' }).count()
```
## Update Document
```
db.posts.updateOne({ title: 'Post 1' },
{
  $set: {
    category: 'Tech'
  }
})
```
## Delete
```

**Delete a Document**

db.posts.deleteOne({ title: 'Post 6' })
**Delete Multiple Documents**
db.posts.deleteMany({ category: 'Tech' })
```

## COMPARISON OPERATORS
![Screenshot from 2022-07-26 13-10-24](https://user-images.githubusercontent.com/64088888/181561753-661881fa-4c5c-460b-8f3f-4a1ce8aeec38.png)




 
