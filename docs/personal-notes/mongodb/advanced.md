MongoDB has many advanced topics that can help optimize performance, scalability, and security. Here are some key areas to explore:

---

### **1. Indexing and Performance Optimization**  
- **Compound Indexes**: Index multiple fields to speed up queries.  
- **Text Indexing**: Enable full-text search.  
- **TTL Indexes**: Automatically delete old documents.  
- **Wildcard Indexes**: Index dynamic fields.  
- **Covered Queries**: Retrieve data directly from an index, avoiding disk reads.  
- **Explain Plans**: Use `.explain("executionStats")` to analyze query efficiency.  

---

### **2. Aggregation Pipeline**  
- **$match** → Filter documents early for better performance.  
- **$group** → Perform grouping and calculations (SUM, AVG, COUNT).  
- **$lookup** → Perform joins between collections.  
- **$facet** → Run multiple aggregations in a single query.  
- **$bucket** → Group data into ranges like a histogram.  

Example:
```js
db.orders.aggregate([
  { $match: { status: "shipped" } },
  { $group: { _id: "$customerId", totalSpent: { $sum: "$amount" } } },
  { $sort: { totalSpent: -1 } }
]);
```

---

### **3. Sharding (Horizontal Scaling)**  
- Distribute data across multiple servers for better performance.  
- **Shard Keys**: Choose carefully to balance load.  
- **Zone Sharding**: Direct specific data to specific shards (e.g., geo-based).  

Example:
```sh
sh.enableSharding("myDatabase")
sh.shardCollection("myDatabase.myCollection", { userId: "hashed" })
```

---

### **4. Replication & High Availability**  
- **Replica Sets**: Maintain copies of data for failover.  
- **Arbiter Nodes**: Help in election but don’t store data.  
- **Read Preferences**: Direct reads to secondaries (`secondaryPreferred`).  

Example:
```js
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "server1:27017" },
    { _id: 1, host: "server2:27017" },
    { _id: 2, host: "server3:27017", arbiterOnly: true }
  ]
});
```

---

### **5. Transactions (Multi-document ACID Transactions)**  
- MongoDB supports **ACID transactions** similar to SQL.  
- Use `startTransaction()` and `commitTransaction()`.  

Example:
```js
const session = db.getMongo().startSession();
session.startTransaction();
try {
  session.getDatabase("mydb").collection("users").updateOne(
    { _id: "123" },
    { $inc: { balance: -50 } }
  );
  session.getDatabase("mydb").collection("orders").insertOne(
    { userId: "123", amount: 50, status: "pending" }
  );
  session.commitTransaction();
} catch (error) {
  session.abortTransaction();
}
session.endSession();
```

---

### **6. Security & Authentication**  
- **Enable Authentication** (`SCRAM-SHA-256`, LDAP, Kerberos).  
- **Role-based Access Control (RBAC)** → Assign specific roles to users.  
- **Field-level Encryption** → Encrypt sensitive data at rest.  
- **IP Whitelisting** → Restrict access to specific IPs.  

Example:
```sh
db.createUser({
  user: "admin",
  pwd: "securePassword",
  roles: [{ role: "readWrite", db: "mydb" }]
});
```

---

### **7. Schema Design Best Practices**  
- **Embed vs. Reference**:
  - Use **embedding** for fast reads (e.g., user profile with addresses).
  - Use **referencing** for large, reusable data (e.g., orders linked to products).  
- **Bucket Pattern** → Store time-series data efficiently.  
- **Attribute Pattern** → Store dynamic fields without schema explosion.  

---

Would you like help with a specific MongoDB feature? 🚀
<hr>


# **🔄 Replication & High Availability in MongoDB**  

## **1️⃣ What is Replication in MongoDB?**
**Replication** in MongoDB is a process that ensures **data availability and redundancy** by maintaining **multiple copies of data** across different servers.  

🔹 **Why Use Replication?**  
✅ **High Availability** – If one server fails, another takes over.  
✅ **Data Redundancy** – Protects against data loss.  
✅ **Fault Tolerance** – Ensures system resilience.  
✅ **Horizontal Scaling** – Supports read scalability.  

---

## **2️⃣ How Replication Works?**
MongoDB uses **Replica Sets** to replicate data across multiple nodes.

### **🔹 What is a Replica Set?**
A **Replica Set** is a group of MongoDB instances that maintain the same dataset. It consists of:

| **Node Type**  | **Role** |
|---------------|---------|
| **Primary Node** | Handles all writes and reads (by default). |
| **Secondary Nodes** | Replicates data from the primary. Can serve read queries (if configured). |
| **Arbiter (Optional)** | Participates in elections but doesn’t store data. |

📌 **Example: A 3-Node Replica Set**  
```
+----------------+
| Primary Node   |
| (Writes & Reads)|
+----------------+
       |
       v
+----------------+   +----------------+
| Secondary Node | ← | Secondary Node |
| (Backup)       |   | (Backup)       |
+----------------+   +----------------+
```

---

## **3️⃣ Setting Up a Replica Set**
### **🔹 Step 1: Start MongoDB Instances**
Start **3 MongoDB instances** on different ports:
```bash
mongod --replSet "myReplicaSet" --port 27017 --dbpath /data/node1 --oplogSize 128 --bind_ip 127.0.0.1 &
mongod --replSet "myReplicaSet" --port 27018 --dbpath /data/node2 --oplogSize 128 --bind_ip 127.0.0.1 &
mongod --replSet "myReplicaSet" --port 27019 --dbpath /data/node3 --oplogSize 128 --bind_ip 127.0.0.1 &
```

### **🔹 Step 2: Initiate the Replica Set**
Connect to **MongoDB shell**:
```bash
mongo --port 27017
```
Initialize the replica set:
```js
rs.initiate({
  _id: "myReplicaSet",
  members: [
    { _id: 0, host: "localhost:27017" },
    { _id: 1, host: "localhost:27018" },
    { _id: 2, host: "localhost:27019" }
  ]
});
```
Check replica set status:
```js
rs.status();
```

---

## **4️⃣ Automatic Failover & Elections**
### **🔹 What Happens When the Primary Fails?**
1️⃣ If the **primary node** goes down, **an election is triggered**.  
2️⃣ A **secondary node** is elected as the **new primary**.  
3️⃣ When the old primary recovers, it rejoins as a **secondary**.  

📌 **Example of Automatic Failover Process**
```
+----------------+
| Primary Node   |  (Fails ❌)
+----------------+
       |
       v  (Election happens 🗳️)
+----------------+   +----------------+
| Secondary Node | → | Secondary Node |  (New Primary ✅)
+----------------+   +----------------+
```

### **🔹 Force Trigger an Election**
You can **manually trigger an election** if needed:
```js
rs.stepDown();
```

---

## **5️⃣ Read & Write Operations in Replica Sets**
By default, **all writes go to the primary**.

### **🔹 Read from Secondary Nodes**
MongoDB allows **reading from secondary nodes** using **read preferences**.

#### ✅ **Allow Read Operations on Secondary Nodes**
```js
db.getMongo().setReadPref("secondary");
db.collection.find();
```

#### ✅ **Read from Nearest Node (Load Balancing)**
```js
db.getMongo().setReadPref("nearest");
db.collection.find();
```

⚠️ **Caution:** Secondary reads might be **eventually consistent** due to replication delay.

---

## **6️⃣ Replication Lag**
### **🔹 What is Replication Lag?**
Replication lag happens when **secondary nodes fall behind** in syncing data from the primary.

🔹 **Causes of Replication Lag:**  
- **High write traffic** on primary.  
- **Slow network connection** between replica set members.  
- **Overloaded secondary nodes** due to read operations.  

### **🔹 Check Replication Lag**
```js
rs.printSlaveReplicationInfo();
```

---

## **7️⃣ High Availability Best Practices**
✅ **Always have an odd number of nodes** to prevent split-brain scenarios.  
✅ **Use an Arbiter** only when you have 2 data nodes (to maintain elections).  
✅ **Enable Write Concern & Read Concern** for data durability.  
✅ **Monitor replication lag** to avoid stale reads.  
✅ **Use geographically distributed replica sets** for disaster recovery.  

---

## **8️⃣ Difference Between Replication & Sharding**
| **Feature** | **Replication (Replica Sets)** | **Sharding** |
|------------|-----------------------------|------------|
| **Purpose** | High availability & data redundancy | Horizontal scaling |
| **Data Distribution** | Full copy on each node | Data split across shards |
| **Failover Support** | Automatic failover | No automatic failover |
| **Read Scaling** | Can read from secondaries | Data spread across multiple servers |
| **Write Scaling** | Single primary | Writes distributed across shards |

📌 **Use Replication** for **high availability** and **data redundancy**.  
📌 **Use Sharding** for **scaling large datasets** across multiple nodes.  

---

## **🚀 Summary: Key Takeaways**
| **Concept** | **What it Does** |
|------------|----------------|
| **Replica Set** | A group of MongoDB nodes that replicate data. |
| **Primary Node** | Handles all writes & read requests (default). |
| **Secondary Nodes** | Backup nodes that replicate from the primary. |
| **Arbiter Node** | Participates in elections but doesn’t store data. |
| **Automatic Failover** | If the primary node fails, a new primary is elected. |
| **Read Scaling** | Queries can be sent to secondary nodes. |
| **Replication Lag** | Delay in syncing data between primary & secondaries. |

🚀 **Want to set up replication for your MongoDB database? Let me know!** 😊