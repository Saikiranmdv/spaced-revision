# Kubernetes – Part 2: ReplicaSet & Deployment

## Topics Covered
1. ReplicaSet  
2. Creating a ReplicaSet  
3. Deployment  
4. Key Differences: Pod vs Deployment  
5. Creating a Deployment  
6. Practical Example (YAML + CLI)

---

## 1. ReplicaSet

A **ReplicaSet** in Kubernetes is a controller that ensures a specified number of **pod replicas** are running at any given time.  
It maintains a stable set of pods running in the cluster, even if some fail or are deleted.

### 🔹 Purpose
- Guarantees that the desired number of identical Pods are always active.
- Automatically replaces failed or deleted Pods with new ones.
- Acts as the **foundation of Deployments**, which manage ReplicaSets automatically.

### 🔹 How It Works
When you create a **Deployment**, you specify the number of **replicas** you want for that Pod.  
The Deployment creates a **ReplicaSet**, which then creates and maintains the Pods.

###  Series of Events
1. User runs `kubectl create deployment`.
2. Deployment controller creates a new **ReplicaSet**.
3. ReplicaSet creates the required number of **Pods**.
4. If Pods go down, **ReplicaSet Controller** brings them back up automatically.

---

## 2. Creating a ReplicaSet

Let’s manually create a ReplicaSet that starts 3 NGINX Pods.

### ReplicaSet Manifest (`rs.yml`)
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

### ⚙️ Apply the Manifest
```bash
kubectl apply -f rs.yml
```

### 🔍 Get ReplicaSet Details
```bash
kubectl get rs
kubectl get pods
```

**Example Output:**
```
NAME               DESIRED   CURRENT   READY   AGE
nginx-replicaset   3         3         3       22s
```

### 🧠 Test Replica Behavior
- Try deleting a Pod → ReplicaSet immediately recreates it.
```bash
kubectl delete pod <pod-name>
kubectl get pods
```

- Try creating a new Pod manually → It gets terminated because ReplicaSet already maintains 3 replicas.

```bash
kubectl run nginx-pod --image=nginx --labels="app=nginx"
# The Pod will terminate since 3 replicas already exist.
```

### 🧹 Delete the ReplicaSet
```bash
kubectl delete rs nginx-replicaset
```

---

## 3. Deployment

A **Deployment** is a higher-level abstraction that manages ReplicaSets and provides declarative updates to Pods.

### 🔹 Features
- Automates **rolling updates** and **rollbacks**.  
- Handles **scaling** and **self-healing**.  
- Makes managing large-scale applications easier.

### 🧩 Deployment Architecture
- The **Deployment Controller** creates and manages ReplicaSets.
- ReplicaSets then manage Pods.
- If a Deployment is updated (e.g., new image), it creates a new ReplicaSet.

---

## 4. Key Differences Between Deployment and Pod

| Aspect | Pod | Deployment |
|--------|-----|-------------|
| **Abstraction Level** | Smallest object that runs containers. | Higher-level object managing multiple Pods via ReplicaSet. |
| **Management** | Created and destroyed manually. | Manages Pods automatically, ensuring desired count. |
| **Updates** | Manual recreation needed. | Supports rolling updates and rollback. |
| **Scaling** | Scale by creating/deleting Pods. | Scale declaratively via replica count. |
| **Self-Healing** | Needs manual restart on crash. | Automatically restarts Pods through ReplicaSet. |

---

## 5. Creating a Deployment

Let’s create a Deployment that manages 3 replicas of an NGINX container.

### 🧾 Deployment Manifest (`deployment.yml`)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

### ⚙️ Apply the Deployment
```bash
kubectl apply -f deployment.yml
```

### 🔍 Verify Deployment
```bash
kubectl get deployment
kubectl get rs
kubectl get pods
```

**Example Output:**
```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   3/3     3            3           30s
```

---

## 6. Updating and Managing Deployments

### 🧠 Update Deployment Image
```bash
kubectl set image deployment/nginx-deployment nginx=nginx:1.27
kubectl rollout status deployment/nginx-deployment
```

### 🔄 Rollback if Needed
```bash
kubectl rollout undo deployment/nginx-deployment
```

### 🧹 Delete Deployment
```bash
kubectl delete deployment nginx-deployment
```

---

## ✅ Summary

| Concept | Description |
|----------|--------------|
| **ReplicaSet** | Ensures fixed number of Pods run; replaces crashed ones. |
| **Deployment** | Manages ReplicaSets and handles updates/rollbacks. |
| **Pod** | Smallest deployable object containing container(s). |
| **Scaling** | Managed declaratively using replica count. |
| **Self-Healing** | Automatic via ReplicaSet Controller. |

---

### 🧩 Next Topics
- Kubernetes Services (ClusterIP, NodePort, LoadBalancer)  
- Rolling Updates & Rollbacks in detail  
- Persistent Volumes & Storage  
- ConfigMaps and Secrets
