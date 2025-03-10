If you're new to **MongoDB**, here are the **basic-level** topics you should learn first:



## **1. Introduction to MongoDB**
- **MongoDB** is a **NoSQL** database, meaning it **stores data in JSON-like documents** instead of tables.  
- It is **schema-less**, so documents in the same collection can have different structures.

📌 **Example Document in MongoDB:**
```json
{
  "_id": ObjectId("650f1a2b3c4d5e6f7890abcd"),
  "name": "Alice",
  "age": 25,
  "email": "alice@example.com"
}
```



## **2. Installing MongoDB**
- Download from: [MongoDB Official Website](https://www.mongodb.com/try/download/community)  
- Start MongoDB:  
  ```sh
  mongod
  ```
- Connect to MongoDB shell:  
  ```sh
  mongosh
  ```



## **3. MongoDB Databases and Collections**
- **Database** = Like a "folder" that holds collections.  
- **Collection** = Like a "table" in SQL, but stores documents instead of rows.  

📌 **Creating a Database:**
```sh
use myDatabase
```

📌 **Creating a Collection:**
```js
db.createCollection("users")
```



## **4. CRUD Operations (Create, Read, Update, Delete)**  

### **Create (Insert Data)**
📌 Insert **one document**:  
```js
db.users.insertOne({ name: "Alice", age: 25, city: "New York" });
```
📌 Insert **multiple documents**:  
```js
db.users.insertMany([
  { name: "Bob", age: 30, city: "London" },
  { name: "Charlie", age: 28, city: "Paris" }
]);
```



### **Read (Query Data)**
📌 Get **all documents**:  
```js
db.users.find();
```
📌 Get documents with a condition:  
```js
db.users.find({ city: "London" });
```
📌 Get a **single document**:  
```js
db.users.findOne({ name: "Alice" });
```
📌 Select only specific fields:  
```js
db.users.find({ age: 30 }, { name: 1, city: 1, _id: 0 });
```



### **Update (Modify Data)**
📌 Update **one document**:  
```js
db.users.updateOne({ name: "Alice" }, { $set: { age: 26 } });
```
📌 Update **multiple documents**:  
```js
db.users.updateMany({ city: "London" }, { $set: { country: "UK" } });
```
📌 Replace a document:  
```js
db.users.replaceOne({ name: "Charlie" }, { name: "Charlie", age: 29, city: "Berlin" });
```



### **Delete (Remove Data)**
📌 Delete **one document**:  
```js
db.users.deleteOne({ name: "Bob" });
```
📌 Delete **multiple documents**:  
```js
db.users.deleteMany({ city: "Paris" });
```



## **5. Indexing for Faster Queries**
Indexes improve search speed.

📌 Create an **index** on the `name` field:  
```js
db.users.createIndex({ name: 1 });
```



## **6. Relationships in MongoDB**
MongoDB supports **two ways** to handle relationships:

### **1️⃣ Embedding (For small, related data)**
```json
{
  "_id": 1,
  "name": "Alice",
  "address": { "street": "123 Main St", "city": "New York" }
}
```

### **2️⃣ Referencing (For large, reusable data)**
```json
{
  "_id": 1,
  "name": "Alice",
  "address_id": ObjectId("650f1a2b3c4d5e6f7890abcd")
}
```
👉 You then **join** using `$lookup`.



## **7. Importing & Exporting Data**
📌 **Import JSON data into MongoDB**:
```sh
mongoimport --db=myDatabase --collection=users --file=users.json --jsonArray
```

📌 **Export data to a JSON file**:
```sh
mongoexport --db=myDatabase --collection=users --out=users.json --jsonArray
```



## **8. Basic Aggregation (Data Analysis)**
MongoDB’s **aggregation framework** is used for analytics.

📌 **Count the number of users per city**:  
```js
db.users.aggregate([
  { $group: { _id: "$city", count: { $sum: 1 } } }
]);
```



## **9. MongoDB Compass (GUI Tool)**
- **MongoDB Compass** provides a user-friendly way to manage databases.  
- Download: [MongoDB Compass](https://www.mongodb.com/try/download/compass)



## **10. Connecting MongoDB with Node.js**
You can use **MongoDB with Node.js** using the `mongodb` package.

📌 **Install MongoDB Driver:**
```sh
npm install mongodb
```

📌 **Connect to MongoDB in Node.js:**
```js
const { MongoClient } = require("mongodb");
const url = "mongodb://localhost:27017";
const client = new MongoClient(url);

async function run() {
  await client.connect();
  console.log("Connected to MongoDB");
  const db = client.db("myDatabase");
  const users = db.collection("users");

  const allUsers = await users.find().toArray();
  console.log(allUsers);
}

run().catch(console.error);
```



### **Where to Go Next?**
Once you're comfortable with the basics, move on to **moderate-level** topics like:
✅ Aggregation Pipeline  
✅ Transactions  
✅ Schema Design Patterns  
✅ Index Optimization  

Would you like more details on any of these? 🚀

<hr>


### **📌 Common MongoDB Operators Used in CRUD Operations**  

MongoDB provides various **operators** to perform CRUD (Create, Read, Update, Delete) operations efficiently. Below is a categorized list:



## **1️⃣ Query Operators (Used in Read - `find()` & `findOne()`)**  
These operators help filter documents when retrieving data.

| **Operator** | **Description** | **Example Query** |
|-------------|----------------|------------------|
| `$eq` | Matches values **equal** to a specified value | `{ age: { $eq: 25 } }` |
| `$ne` | Matches values **not equal** to a specified value | `{ age: { $ne: 25 } }` |
| `$gt` | Matches values **greater than** a value | `{ age: { $gt: 30 } }` |
| `$gte` | Matches values **greater than or equal** to a value | `{ age: { $gte: 30 } }` |
| `$lt` | Matches values **less than** a value | `{ age: { $lt: 30 } }` |
| `$lte` | Matches values **less than or equal** to a value | `{ age: { $lte: 30 } }` |
| `$in` | Matches any value in an **array** | `{ age: { $in: [25, 30, 35] } }` |
| `$nin` | Excludes values present in an **array** | `{ age: { $nin: [25, 30, 35] } }` |
| `$exists` | Checks if a field **exists** | `{ age: { $exists: true } }` |
| `$type` | Matches data by BSON **type** | `{ age: { $type: "number" } }` |



## **2️⃣ Logical Operators (Used in Read - `find()`)**  
These are used to combine multiple conditions.

| **Operator** | **Description** | **Example Query** |
|----------|----------------|------------------|
| `$and` | Matches documents that satisfy **all** conditions | `{ $and: [{ age: { $gt: 25 } }, { city: "New York" }] }` |
| `$or` | Matches documents that satisfy **at least one** condition | `{ $or: [{ age: 25 }, { city: "New York" }] }` |
| `$nor` | Matches documents that **don’t** satisfy any conditions | `{ $nor: [{ age: 25 }, { city: "New York" }] }` |
| `$not` | Matches documents where a condition **is not true** | `{ age: { $not: { $gt: 30 } } }` |



## **3️⃣ Update Operators (Used in Update - `updateOne()`, `updateMany()`)**  
Used to modify documents.

| **Operator** | **Description** | **Example Query** |
|-------------|----------------|------------------|
| `$set` | Updates **specific** fields | `{ $set: { name: "Alice" } }` |
| `$unset` | Removes a field | `{ $unset: { age: "" } }` |
| `$inc` | Increments a numeric field | `{ $inc: { age: 1 } }` |
| `$mul` | Multiplies a numeric field | `{ $mul: { salary: 1.1 } }` |
| `$rename` | Renames a field | `{ $rename: { oldName: "newName" } }` |
| `$min` | Updates field **only if new value is lower** | `{ $min: { age: 20 } }` |
| `$max` | Updates field **only if new value is higher** | `{ $max: { age: 50 } }` |
| `$currentDate` | Sets the current date/time | `{ $currentDate: { lastUpdated: true } }` |



## **4️⃣ Array Operators (Used in Read & Update)**  
Used to work with arrays inside documents.

| **Operator** | **Description** | **Example Query** |
|-------------|----------------|------------------|
| `$push` | Adds a new element to an **array** | `{ $push: { tags: "mongodb" } }` |
| `$pull` | Removes specific elements from an **array** | `{ $pull: { tags: "mongodb" } }` |
| `$pop` | Removes **first (-1) or last (1)** element from an array | `{ $pop: { tags: 1 } }` |
| `$addToSet` | Adds an element **only if it doesn’t exist** | `{ $addToSet: { tags: "database" } }` |
| `$each` | Used with `$push` to **insert multiple values** | `{ $push: { tags: { $each: ["NoSQL", "MongoDB"] } } }` |
| `$size` | Matches arrays of a specific **size** | `{ tags: { $size: 3 } }` |

---

## **5️⃣ Element Operators (Used in Read - `find()`)**  
Used to match documents based on fields and their values.

| **Operator** | **Description** | **Example Query** |
|-------------|----------------|------------------|
| `$exists` | Matches documents where a field **exists** | `{ age: { $exists: true } }` |
| `$type` | Matches documents where a field is of a **specific type** | `{ age: { $type: "number" } }` |

---

## **6️⃣ Projection Operators (Used in Read - `find()`)**  
Used to control the fields returned in the query result.

| **Operator** | **Description** | **Example Query** |
|-------------|----------------|------------------|
| `1` | Include a field | `{ name: 1, age: 1 }` |
| `0` | Exclude a field | `{ _id: 0, password: 0 }` |
| `$slice` | Returns a portion of an **array field** | `{ tags: { $slice: 2 } }` |

---

## **7️⃣ Deletion Operators (Used in Delete - `deleteOne()`, `deleteMany()`)**  
Used to remove documents.

| **Operator** | **Description** | **Example Query** |
|-------------|----------------|------------------|
| `$eq` | Deletes documents where the field **equals** a value | `db.users.deleteMany({ age: { $eq: 30 } })` |
| `$gt` | Deletes documents where the field is **greater than** a value | `db.users.deleteMany({ age: { $gt: 60 } })` |
| `$lt` | Deletes documents where the field is **less than** a value | `db.users.deleteMany({ age: { $lt: 18 } })` |

---

## **8️⃣ Aggregation Operators (Used in Aggregation - `aggregate()`)**  
Used in complex queries and data transformations.

| **Operator** | **Description** | **Example Query** |
|-------------|----------------|------------------|
| `$match` | Filters documents | `{ $match: { status: "active" } }` |
| `$group` | Groups data and calculates values | `{ $group: { _id: "$city", total: { $sum: 1 } } }` |
| `$sort` | Sorts documents | `{ $sort: { age: -1 } }` |
| `$limit` | Limits the number of documents | `{ $limit: 5 }` |
| `$lookup` | Performs a **JOIN** between collections | `{ $lookup: { from: "orders", localField: "_id", foreignField: "userId", as: "userOrders" } }` |

---

## **🔍 Example CRUD Operations Using These Operators**
```js
// INSERT: Create a new user
db.users.insertOne({ name: "Alice", age: 25, city: "New York", tags: ["developer", "mongodb"] });

// READ: Find users older than 25
db.users.find({ age: { $gt: 25 } });

// UPDATE: Increase age by 1
db.users.updateOne({ name: "Alice" }, { $inc: { age: 1 } });

// DELETE: Remove users younger than 18
db.users.deleteMany({ age: { $lt: 18 } });
```

---

### **🚀 Summary**
- **Query Operators** (`$eq`, `$gt`, `$in`) → Used in `find()`
- **Logical Operators** (`$and`, `$or`, `$not`) → Combine multiple conditions
- **Update Operators** (`$set`, `$inc`, `$push`) → Modify documents
- **Array Operators** (`$push`, `$pull`, `$addToSet`) → Work with arrays
- **Projection Operators** (`1`, `$slice`) → Select specific fields
- **Deletion Operators** (`$eq`, `$gt`, `$lt`) → Remove documents
- **Aggregation Operators** (`$match`, `$group`, `$lookup`) → Process data

### **📌 How Different MongoDB Index Types Improve Queries?**  

Each index type in MongoDB is designed to optimize different types of queries. Below is how each index affects query performance:  

---

## **1️⃣ Single Field Index (Basic Index)**
💡 **Optimizes:** Exact match and sorting on a single field.

🔹 **Without Index:**  
```js
db.users.find({ name: "Alice" });
```
👉 **Scans the entire collection (Full Collection Scan - O(n))**

🔹 **With Index (`{ name: 1 }`)**  
```js
db.users.createIndex({ name: 1 });
db.users.find({ name: "Alice" });
```
👉 **Uses the index to find the exact match quickly (B-tree lookup - O(log n))**

🔹 **Optimized Sorting:**
```js
db.users.find().sort({ name: 1 });
```
✅ Sorting is **fast** because MongoDB already has an **ordered index**.

---

## **2️⃣ Compound Index**
💡 **Optimizes:** Queries filtering on **multiple fields**.

🔹 **Without Index:**  
```js
db.users.find({ age: 30, city: "New York" });
```
👉 **Scans all documents (Slow, O(n))**

🔹 **With Compound Index (`{ age: 1, city: 1 }`)**
```js
db.users.createIndex({ age: 1, city: 1 });
db.users.find({ age: 30, city: "New York" });
```
👉 **Directly retrieves documents from the index (Fast, O(log n))**

🔹 **Optimized Sorting:**  
```js
db.users.find({ age: { $gt: 25 } }).sort({ city: 1 });
```
✅ The index helps with both **filtering** and **sorting**!

❌ **Order Matters!** The above index **won't** help with:
```js
db.users.find({ city: "New York" });
```
(As `age` comes first in the index.)

---

## **3️⃣ Multi-Key Index**
💡 **Optimizes:** Queries on **array fields**.

🔹 **Without Index:**  
```js
db.articles.find({ tags: "mongodb" });
```
👉 **Scans all articles** that might have the tag.

🔹 **With Multi-Key Index (`{ tags: 1 }`)**
```js
db.articles.createIndex({ tags: 1 });
db.articles.find({ tags: "mongodb" });
```
✅ **Each array element** gets indexed, making lookups fast.

❌ **Sorting is inefficient** with multi-key indexes.

---

## **4️⃣ Text Index**
💡 **Optimizes:** **Full-text search** in string fields.

🔹 **Without Index:**  
```js
db.articles.find({ content: /mongodb tutorial/i });
```
👉 **Slow!** This is a **regex-based** search that scans all documents.

🔹 **With Text Index (`{ title: "text", content: "text" }`)**
```js
db.articles.createIndex({ title: "text", content: "text" });
db.articles.find({ $text: { $search: "mongodb tutorial" } });
```
✅ **Fast full-text search** using **inverted indexes**.

---

## **5️⃣ Hashed Index**
💡 **Optimizes:** **Equality queries** on high-cardinality fields (e.g., `_id`, `email`).

🔹 **Without Index:**  
```js
db.users.find({ email: "user@example.com" });
```
👉 **Scans every document!** (Slow)

🔹 **With Hashed Index (`{ email: "hashed" }`)**
```js
db.users.createIndex({ email: "hashed" });
db.users.find({ email: "user@example.com" });
```
✅ **Instant lookup** for equality checks.  
❌ **Does not support range queries (`$gt`, `$lt`).**

---

## **6️⃣ Partial Index**
💡 **Optimizes:** Queries on **frequently queried subsets** of data.

🔹 **Without Index:**  
```js
db.users.find({ age: { $gt: 25 }, status: "active" });
```
👉 **Scans all users** (including inactive ones).

🔹 **With Partial Index**
```js
db.users.createIndex({ age: 1 }, { partialFilterExpression: { status: "active" } });
```
✅ **Only indexes "active" users**, making queries much faster.

---

## **7️⃣ TTL (Time-To-Live) Index**
💡 **Optimizes:** **Auto-deletion** of old documents.

🔹 **Without Index:**  
```js
db.sessions.find({ createdAt: { $lt: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000) } });
db.sessions.deleteMany({ createdAt: { $lt: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000) } });
```
👉 **Requires a scheduled cleanup job!** (Inefficient)

🔹 **With TTL Index**
```js
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 604800 });
```
✅ **Automatically removes old sessions after 7 days**.

---

## **8️⃣ Wildcard Index**
💡 **Optimizes:** Searching in **dynamic fields**.

🔹 **Without Index:**  
```js
db.logs.find({ "metadata.device": "mobile" });
```
👉 **Scans all documents if `metadata` structure varies**.

🔹 **With Wildcard Index**
```js
db.logs.createIndex({ "metadata.$**": 1 });
```
✅ **Indexes all subfields dynamically**, making searches faster.

---

### **📊 Comparison of Index Performance**
| **Index Type**  | **Best For** | **Optimized Queries** | **Supports Sorting?** |
|-------------|-----------|-----------------|----------------|
| **Single Field** | Lookups, Sorting | `{ name: "Alice" }` | ✅ Yes |
| **Compound** | Multi-field queries | `{ age: 30, city: "NY" }` | ✅ Yes (if order matches) |
| **Multi-Key** | Arrays | `{ tags: "mongodb" }` | ❌ No |
| **Text** | Full-text search | `{ $text: { $search: "mongodb" } }` | ❌ No |
| **Hashed** | Unique lookups | `{ email: "user@example.com" }` | ❌ No |
| **Partial** | Specific document subsets | `{ status: "active" }` | ✅ Yes |
| **TTL** | Auto-deleting old data | `{ createdAt: { $lt: new Date() } }` | ❌ No |
| **Wildcard** | Dynamic fields | `{ "metadata.device": "mobile" }` | ✅ Yes |

---

### **🚀 Summary**
- **Single & Compound Indexes**: Best for filtering and sorting.
- **Multi-Key Index**: Best for arrays.
- **Text Index**: Best for full-text search.
- **Hashed Index**: Best for exact matches.
- **Partial Index**: Best for optimizing specific queries.
- **TTL Index**: Best for auto-deleting old data.
- **Wildcard Index**: Best for indexing dynamic fields.

Would you like me to show an **`explain()` query comparison** for indexed vs. non-indexed searches? 🚀

# **🔗 Relationships in MongoDB**
MongoDB is a **NoSQL database** that stores data in **JSON-like documents** (BSON). Unlike relational databases, it **does not enforce strict relationships** like foreign keys. However, you can still model relationships between documents using **two main approaches**:

- **📌 Embedded Documents (Denormalization)**
- **📌 References (Normalization)**

Each approach has advantages and trade-offs depending on **performance, scalability, and data consistency**.

---

## **1️⃣ Embedded Documents (Denormalization)**
### **📌 What is it?**
Instead of storing related data in separate collections, you store related information **inside the same document**.

### **✅ When to Use?**
✔️ When related data is **frequently accessed together**  
✔️ When the related data is **not too large**  
✔️ When data changes are **not too frequent**  

### **🔹 Example: Storing Orders with Products Inside the Same Document**
```js
db.orders.insertOne({
    _id: 1,
    customer: "Alice",
    total_price: 500,
    products: [
        { product_id: 101, name: "Laptop", price: 450 },
        { product_id: 102, name: "Mouse", price: 50 }
    ]
});
```
### **🔥 Advantages**
✔ **Faster reads** (no need for joins)  
✔ **Simpler queries**  
✔ **Better performance for one-to-few relationships**  

### **⚠️ Disadvantages**
❌ **Data duplication** (if products are stored in multiple orders)  
❌ **Difficult updates** (changing product details requires updating all occurrences)  
❌ **Document size limit** (MongoDB has a **16MB** document limit)  

---

## **2️⃣ References (Normalization)**
### **📌 What is it?**
Instead of embedding related data, store **only the reference (ID) of the related document** in another collection.

### **✅ When to Use?**
✔️ When related data is **large and reusable**  
✔️ When updates are **frequent**  
✔️ When relationships are **complex (one-to-many, many-to-many)**  

### **🔹 Example: Storing Orders with Product References**
#### **Orders Collection**
```js
db.orders.insertOne({
    _id: 1,
    customer: "Alice",
    total_price: 500,
    products: [101, 102]  // Storing only product IDs
});
```
#### **Products Collection**
```js
db.products.insertMany([
    { _id: 101, name: "Laptop", price: 450 },
    { _id: 102, name: "Mouse", price: 50 }
]);
```

### **🔥 Advantages**
✔ **Less data duplication**  
✔ **Easier updates** (update the product once, and all orders reflect the change)  
✔ **Better for many-to-many relationships**  

### **⚠️ Disadvantages**
❌ **More complex queries** (need `$lookup` for joins)  
❌ **Slightly slower reads**  

### **🔍 Query Using `$lookup` (Joining Orders and Products)**
```js
db.orders.aggregate([
    {
        $lookup: {
            from: "products",
            localField: "products",
            foreignField: "_id",
            as: "order_products"
        }
    }
]);
```

---

## **3️⃣ One-to-One Relationship**
### **📌 Example: User & Profile**
Each user has **only one** profile.

#### **Embedded Approach (When Profile is Always Accessed)**
```js
db.users.insertOne({
    _id: 1,
    name: "John",
    profile: {
        age: 30,
        address: "New York"
    }
});
```

#### **Reference Approach (When Profile is Accessed Separately)**
```js
db.users.insertOne({ _id: 1, name: "John", profile_id: 101 });
db.profiles.insertOne({ _id: 101, age: 30, address: "New York" });
```
💡 **Which is better?**  
- Use **embedding** if the profile is always used with the user.  
- Use **references** if the profile is large or rarely accessed.

---

## **4️⃣ One-to-Many Relationship**
### **📌 Example: Blog Posts & Comments**
Each **post** can have **multiple comments**.

#### **Embedded Approach (Few Comments per Post)**
```js
db.posts.insertOne({
    _id: 1,
    title: "MongoDB Relationships",
    comments: [
        { user: "Alice", text: "Great article!" },
        { user: "Bob", text: "Very helpful!" }
    ]
});
```
✔ Best if comments are **limited and always needed**.

#### **Reference Approach (Many Comments)**
```js
db.posts.insertOne({ _id: 1, title: "MongoDB Relationships" });
db.comments.insertMany([
    { _id: 101, post_id: 1, user: "Alice", text: "Great article!" },
    { _id: 102, post_id: 1, user: "Bob", text: "Very helpful!" }
]);
```
✔ Best if **comments are large and frequently updated**.

---

## **5️⃣ Many-to-Many Relationship**
### **📌 Example: Students & Courses**
Each **student** can enroll in **multiple courses**, and each **course** has many students.

#### **Using an Array (For Small Datasets)**
```js
db.students.insertOne({
    _id: 1,
    name: "Alice",
    courses: ["Math", "Physics"]
});
```
✔ Simple, but **doesn’t scale well** if there are thousands of students per course.

#### **Using a Join Table (Scalable)**
```js
db.students.insertOne({ _id: 1, name: "Alice" });
db.courses.insertOne({ _id: 101, name: "Math" });
db.enrollments.insertMany([
    { student_id: 1, course_id: 101 },
    { student_id: 1, course_id: 102 }
]);
```
✔ **Scales better for large relationships**.

💡 **Query to Get Student’s Courses**
```js
db.enrollments.aggregate([
    {
        $lookup: {
            from: "courses",
            localField: "course_id",
            foreignField: "_id",
            as: "course_details"
        }
    }
]);
```

---

## **📌 Choosing the Right Relationship Type**
| **Criteria**        | **Embedded (Denormalization)** | **Referenced (Normalization)** |
|----------------------|-----------------------------|-----------------------------|
| **Data Size**        | Small to medium             | Large (scalable)           |
| **Read Performance** | Fast                         | Slower (needs joins)       |
| **Write Performance**| Slower (duplicate updates)   | Fast (single updates)      |
| **Update Frequency** | Rarely updated              | Frequently updated         |
| **Complex Queries**  | Simple (fewer joins)        | Complex (joins required)   |

---

## **🔥 Summary**
1️⃣ **Embedded Documents** – Store related data **inside the same document** for fast reads but harder updates.  
2️⃣ **References (Normalization)** – Store related data **separately** using IDs, reducing duplication and improving scalability.  
3️⃣ **One-to-One** – Use **embedding** if always accessed together; **references** if large/rarely accessed.  
4️⃣ **One-to-Many** – Embed small lists; use a **separate collection** for large, frequently updated lists.  
5️⃣ **Many-to-Many** – Use an **array** for small sets, and a **join collection** for large datasets.  

---

💡 **Want to practice?** Would you like a small project idea to implement these relationships? 🚀

# **📊 MongoDB Aggregation: Deep Dive**  

MongoDB **Aggregation Framework** is a powerful tool used to **process, transform, and analyze** data within collections. It allows complex queries, filtering, grouping, and computations similar to SQL’s `GROUP BY`, `JOIN`, and `HAVING`.  

---

## **1️⃣ What is Aggregation?**  
Aggregation operations **process multiple documents** and return computed results. Instead of retrieving documents **as-is**, aggregation allows **data transformation** using different **stages**.

---

## **2️⃣ Aggregation Pipeline 🏗️**
MongoDB’s **aggregation pipeline** consists of multiple stages, where each stage processes the documents and passes the results to the next stage.

### **📌 Basic Structure**
```js
db.collection.aggregate([
    { Stage 1 },
    { Stage 2 },
    { Stage 3 },
    ...
]);
```
Each **stage** applies a specific operation **before passing** documents to the next stage.

---

## **3️⃣ Common Aggregation Stages**
Each **stage** modifies the data in a specific way.

| **Stage** | **Description** |
|----------|----------------|
| `$match` | Filters documents (like `WHERE` in SQL) |
| `$group` | Groups documents (like `GROUP BY`) |
| `$project` | Reshapes documents (select specific fields) |
| `$sort` | Sorts documents (like `ORDER BY`) |
| `$limit` | Limits the number of documents (like `LIMIT`) |
| `$skip` | Skips a specified number of documents (like `OFFSET`) |
| `$lookup` | Performs a join with another collection (like `JOIN`) |
| `$unwind` | Deconstructs arrays (useful for handling embedded data) |

---

## **4️⃣ Aggregation Examples 🚀**
Let's see **real-world examples** using an **`orders`** collection.

### **📌 Sample Data**
```js
db.orders.insertMany([
    { _id: 1, customer: "Alice", total: 500, status: "completed", items: [{ name: "Laptop", price: 400 }, { name: "Mouse", price: 100 }] },
    { _id: 2, customer: "Bob", total: 300, status: "pending", items: [{ name: "Keyboard", price: 300 }] },
    { _id: 3, customer: "Alice", total: 200, status: "completed", items: [{ name: "Headphones", price: 200 }] }
]);
```

---

## **🔹 1. `$match` (Filtering Data)**
Filters documents based on conditions, like **`WHERE` in SQL**.

### **Example: Get completed orders**
```js
db.orders.aggregate([
    { $match: { status: "completed" } }
]);
```
✅ **Output:**
```json
[
    { "_id": 1, "customer": "Alice", "total": 500, "status": "completed" },
    { "_id": 3, "customer": "Alice", "total": 200, "status": "completed" }
]
```

---

## **🔹 2. `$group` (Grouping Data)**
Groups data and applies aggregations, like **`GROUP BY` in SQL**.

### **Example: Total amount spent by each customer**
```js
db.orders.aggregate([
    { $group: { _id: "$customer", totalSpent: { $sum: "$total" } } }
]);
```
✅ **Output:**
```json
[
    { "_id": "Alice", "totalSpent": 700 },
    { "_id": "Bob", "totalSpent": 300 }
]
```

---

## **🔹 3. `$project` (Selecting & Modifying Fields)**
Used to include, exclude, or modify fields.

### **Example: Show only `customer` and `total` fields**
```js
db.orders.aggregate([
    { $project: { _id: 0, customer: 1, total: 1 } }
]);
```
✅ **Output:**
```json
[
    { "customer": "Alice", "total": 500 },
    { "customer": "Bob", "total": 300 },
    { "customer": "Alice", "total": 200 }
]
```

---

## **🔹 4. `$sort` (Sorting Data)**
Sorts data in ascending (`1`) or descending (`-1`) order.

### **Example: Sort orders by total amount (highest first)**
```js
db.orders.aggregate([
    { $sort: { total: -1 } }
]);
```
✅ **Output:**
```json
[
    { "_id": 1, "customer": "Alice", "total": 500 },
    { "_id": 2, "customer": "Bob", "total": 300 },
    { "_id": 3, "customer": "Alice", "total": 200 }
]
```

---

## **🔹 5. `$limit` and `$skip` (Pagination)**
Used to **paginate results**.

### **Example: Get the top 2 highest orders**
```js
db.orders.aggregate([
    { $sort: { total: -1 } },
    { $limit: 2 }
]);
```

### **Example: Skip the first order and return the next 2**
```js
db.orders.aggregate([
    { $sort: { total: -1 } },
    { $skip: 1 },
    { $limit: 2 }
]);
```

---

## **🔹 6. `$lookup` (Joining Collections)**
Performs a **JOIN** between collections.

### **Example: Join `orders` with `customers`**
#### **Customers Collection**
```js
db.customers.insertMany([
    { _id: "Alice", email: "alice@example.com" },
    { _id: "Bob", email: "bob@example.com" }
]);
```
#### **Aggregation Query**
```js
db.orders.aggregate([
    {
        $lookup: {
            from: "customers",
            localField: "customer",
            foreignField: "_id",
            as: "customer_info"
        }
    }
]);
```
✅ **Output:**
```json
[
    {
        "_id": 1,
        "customer": "Alice",
        "total": 500,
        "customer_info": [{ "_id": "Alice", "email": "alice@example.com" }]
    },
    ...
]
```

---

## **🔹 7. `$unwind` (Flattening Arrays)**
Expands an array into multiple documents.

### **Example: Flatten `items` array**
```js
db.orders.aggregate([
    { $unwind: "$items" }
]);
```
✅ **Output:**
```json
[
    { "_id": 1, "customer": "Alice", "items": { "name": "Laptop", "price": 400 } },
    { "_id": 1, "customer": "Alice", "items": { "name": "Mouse", "price": 100 } },
    { "_id": 2, "customer": "Bob", "items": { "name": "Keyboard", "price": 300 } }
]
```

---

## **5️⃣ Aggregation Operators**
| **Operator** | **Description** |
|-------------|----------------|
| `$sum` | Adds numeric values |
| `$avg` | Computes the average |
| `$min` | Finds the smallest value |
| `$max` | Finds the largest value |
| `$count` | Counts documents |
| `$push` | Creates an array of values |
| `$first` | Gets the first document |
| `$last` | Gets the last document |

---

## **🔥 Summary**
- **`$match`** → Filters documents  
- **`$group`** → Groups data  
- **`$project`** → Modifies output  
- **`$sort`** → Sorts results  
- **`$limit` & `$skip`** → Pagination  
- **`$lookup`** → Joins collections  
- **`$unwind`** → Expands arrays  

🚀 **Want to practice?** Let me know if you need a **real-world project** using MongoDB Aggregation!