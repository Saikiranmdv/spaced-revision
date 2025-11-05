# Kubernetes Fundamentals – Revision Notes

## Topics Covered
1. What is Kubernetes  
2. Before Kubernetes (Traditional Setup)  
3. After Kubernetes (Clustered Setup)  
4. Kubernetes Jargon – Nodes, Cluster, Pods, Containers, Images  
5. Control Plane & Worker Node Components  
6. Kubernetes Control Loop  
7. Creating a K8s Cluster (Kind / Minikube)  
8. Kubernetes API & kubectl  
9. Creating and Managing Pods  
10. Kubernetes Manifest Files  
11. Checkpoint Summary  

---

## 1. What is Kubernetes

- **Kubernetes (K8s)** is a **container orchestration engine** — it automates the deployment, scaling, and management of containerized applications.  
- It manages clusters of machines running containers (like Docker).  
- **Use Cases:**
  1. Deploy Docker images in a cloud-native way.
  2. Handle patching & crashes automatically (self-healing).
  3. Enable autoscaling with simple configuration.
  4. Observe the full system through a unified dashboard.

---

## 2. Before Kubernetes

### Traditional Backend Setup
- Each backend instance deployed manually on EC2 or VM.
- A **load balancer** distributed traffic across backend machines.

### Frontend (Next.js / React)
- Frontend code deployed on separate EC2 or S3 buckets with CDN for caching.
- Each environment (frontend/backend) needed manual scaling and management.

---

## 3. After Kubernetes

- Kubernetes groups multiple machines (nodes) into a **cluster**.  
- Each part of the application (frontend, backend, DB) runs as **Pods** across nodes.

**Cluster Layout:**
- Multiple nodes (e.g., AWS Machine 1–3) managed as one unit.  
- Automatic scheduling of containers.  
- Easy scaling, updates, and monitoring.

---

## 4. Jargon (Core Kubernetes Concepts)

### **Cluster**
A cluster is a collection of machines (nodes) managed by Kubernetes.

### **Nodes**
- Physical or virtual machines that run applications.  
- Two main types:
  - **Master Node (Control Plane)** – manages the cluster, scheduling, and API access.
  - **Worker Node** – runs the actual containerized applications (pods).

### **Images**
- Immutable packages that contain the application code and dependencies.  
- Stored in repositories like Docker Hub.  
- Example: `nginx`, `redis`, etc.

### **Containers**
- Runtime instances of images.  
- Managed by container runtimes like Docker or containerd.

### **Pods**
- Smallest deployable unit in Kubernetes.  
- A Pod wraps one or more containers that share the same network/storage space.

---

## 5. Control Plane Components

| Component | Description |
|------------|--------------|
| **API Server** | Entry point for all Kubernetes commands and interactions. |
| **etcd** | Distributed key-value store for cluster state. |
| **kube-scheduler** | Assigns Pods to Nodes based on resource availability. |
| **kube-controller-manager** | Ensures desired state (replicas, health) matches actual state. |

### Worker Node Components

| Component | Description |
|------------|--------------|
| **kubelet** | Agent running on each node ensuring containers are running as expected. |
| **kube-proxy** | Manages networking and load balancing inside the cluster. |
| **Container Runtime** | Executes containers (Docker, containerd, CRI-O). |

---

## 6. The Kubernetes Control Loop

The **Control Loop** ensures the desired cluster state matches the actual state.

### Steps:
1. **Watch for Changes:** kubelet observes resources via the API Server.  
2. **Compare States:** Controller compares current vs. desired states.  
3. **Take Action:** Creates, deletes, or updates Pods/containers as needed.  

### Example:
- If a container crashes, kubelet restarts it.  
- If a node fails, scheduler moves the Pod to a healthy node.

---

## 7. Creating a Kubernetes Cluster

### **Local Setup (using kind)**

**Requirements:**
- Docker installed.  
- Install kind: [https://kind.sigs.k8s.io/docs/user/quick-start/](https://kind.sigs.k8s.io/docs/user/quick-start/)

#### Create a Single Node Cluster
```bash
kind create cluster
docker ps  # verify control plane container
```

#### Delete Cluster
```bash
kind delete cluster
```

#### Multi-node Cluster
```bash
kind create cluster --config kind-multi.yaml
docker ps  # verify multiple nodes
```

---

### **Using Minikube**
- Install: [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)
- Start cluster:
  ```bash
  minikube start
  ```
- For single node setup, control plane & worker run on same VM.

---

## 8. Kubernetes API

- The **API Server** exposes endpoints that developers and `kubectl` use.  
- Example Endpoint:  
  `https://127.0.0.1:50949/api/v1/namespaces/default/pods`  

### Try the API:
```bash
docker ps  # find where control plane is running
curl https://127.0.0.1:50949/api/v1/namespaces/default/pods
```
- The server requires authentication (`~/.kube/config`).

---

## 9. kubectl

`kubectl` is the command-line tool for interacting with Kubernetes.

**Install:** [https://kubernetes.io/docs/tasks/tools/#kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)

### Basic Commands:
```bash
kubectl get nodes
kubectl get pods
kubectl describe pod <pod-name>
```

### Debugging / Verbose Output
```bash
kubectl get nodes -v=8
```

---

## 10. Creating a Pod

We’ve already set up:
- Cluster
- Nodes
- Images
- Containers
- Pods

### Example: Run NGINX Pod
```bash
kubectl run nginx --image=nginx --port=80
```

**Check Pod:**
```bash
kubectl get pods
kubectl logs nginx
kubectl describe pod nginx
```

**Access Locally:**  
Visit [http://localhost:3005](http://localhost:3005)

**Delete Pod:**
```bash
kubectl delete pod nginx
```

---

## 11. Kubernetes Manifest Files

- Manifests define Kubernetes objects declaratively (YAML/JSON).  
- Equivalent to running imperative commands like `kubectl run`.

### Example Manifest (`manifest.yml`)
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx
      ports:
        - containerPort: 80
```

### Apply Manifest
```bash
kubectl apply -f manifest.yml
```

### Delete Pod
```bash
kubectl delete pod nginx
```

---

## ✅ Checkpoint Summary

We have created and understood:
1. Cluster  
2. Nodes  
3. Images  
4. Containers  
5. Pods  

**Next Steps:** Explore Deployments, ReplicaSets, and Services.
