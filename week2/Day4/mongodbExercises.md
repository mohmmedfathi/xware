# Exercise 1 (MongoDB)

* Design Messaging and Notification System in MongoDB
* Messages Collection Will Documents, Every Document Will Have
* sender Sender info Like (id, name, etc..) and The Sender May Be Student Or Professor
* reciever Reciever info Like (id, name, etc..) and The Sender May Be Student Or Professor
* message Message
* Notification Collection Will Documents, Every Document Will Have
* sender Sender info Like (id, name, etc..) and The Sender May Be Student Or Professor
* reciever Reciever info Like (id, name, etc..) and The Sender May Be Student Or Professor
* type Notification Type (Message For Now)
* content Notification Content
* is_read is Notification Read
* created_at Notification Creation Date

![image (1)](https://user-images.githubusercontent.com/64088888/181577396-bf7143eb-4de7-4f32-af59-c1f65415d11a.png)
*  Messages Collection Will Documents, Every Document Will Have sender
## insert on Messages Collection
```

* db.Messages.insert({
    sender: { id: 1, name: 'ahmed', age: 31, city: 'New York' },
    reciever: { id: 1, name: 'mohmmed', age: 20, city: 'egypt' },
    message: { content: 'Hello World' }
    })
    
* db.Messages.insert({
    sender: { id: 1, name: 'ahmed', age: 31, city: 'New York' },
    reciever: { id: 1, name: 'mohmmed', age: 20, city: 'egypt' },
    message: { content: 'Hello World' }
    })

```
 ## Retrieve  documents in the Messages collection.
 ### db.messages.find()
 
![carbon (6)](https://user-images.githubusercontent.com/64088888/181564156-fd5a785d-6acb-4fd7-ab01-5d038a507220.svg)

<details><summary><b>output</b></summary>
 
 ```
 [
  {
    _id: ObjectId("62e243096b762d79ea87f4dc"),
    sender: { id: 1, name: 'ahmed', age: 31, city: 'New York' },
    reciever: { id: 1, name: 'mohmmed', age: 20, city: 'egypt' },
    message: { content: 'Hello World' }
  },
  {
    _id: ObjectId("62e243326b762d79ea87f4dd"),
    sender: { id: 1, name: 'ahmed', age: 31, city: 'New York' },
    reciever: { id: 1, name: 'mohmmed', age: 20, city: 'egypt' },
    message: { content: 'Hello World' }
  }
]
 
 ```
 
 </details>
 
![carbon (7)](https://user-images.githubusercontent.com/64088888/181564254-f49896e1-ce71-49e9-9c43-3fc94f24bab1.svg)

<details><summary><b>code</b></summary>
 
```
db.Notification.insert({
  sender: {id: 1, name:'Ahmed'},
reciever: {id: 1, name:'Emad'}, 
type: {type:'text'}, 
content:"Hello World",
is_read:true, 
created_at:"july"} 
)
 
```
 </details>
 
## db.Notification.find()

![carbon (8)](https://user-images.githubusercontent.com/64088888/181564283-8b4a4be2-9ee5-454d-99fa-c796afb8cbeb.svg)
