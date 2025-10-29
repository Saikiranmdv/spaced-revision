# 📘 Revision Notes

## Topics Covered
1. Traditional Backend vs Serverless  
2. When to use Serverless Architecture  
3. Pros and Cons of Serverless  
4. Famous Serverless Providers  
5. Cloudflare Workers – How They Work  
6. Isolates vs Containers  
7. Wrangler (Cloudflare CLI)  
8. Hono Framework Motivation  
9. Connecting Databases in Serverless  

---

## 1. Traditional Backend vs Serverless

- **Traditional Backend (e.g., Express with Node.js)**  
  - Run locally using:  
    ```bash
    node index.js
    ```
    This starts a process on a fixed port (e.g., 3000).  
  - To deploy on the internet, common options include:  
    - Renting a VM (AWS EC2, GCP Compute Engine, Azure VMs).  
    - Putting app in an Auto Scaling Group.  
    - Deploying into a Kubernetes cluster.  

- **Serverless**  
  - Developers focus only on code.  
  - Cloud provider dynamically manages provisioning, scaling, and server allocation.  
  - You don’t pay for idle VMs, instead pay **per request**.  

---

## 2. When to Use Serverless

- 🚀 Rapid prototyping: Get off the ground fast without worrying about infrastructure.  
- 📈 Unpredictable traffic: Serverless auto-scales without manual configuration.  
- 💸 Low-traffic apps: Optimized for cost — only pay when code executes.  

---

## 3. Pros and Cons of Serverless

**Advantages**
- No server management needed.  
- Automatic scaling.  
- Pay-as-you-go (per request).  
- Faster deployment cycle.  

**Disadvantages**
- Can become **expensive at large scale**.  
- **Cold start problem** → first request after inactivity is slow.  
- Native serverless platforms may lack built-in routing (e.g., Cloudflare Workers).  
- Monitoring/debugging can be more complex.  

---

## 4. Famous Serverless Providers

- **AWS Lambda** → Most widely used serverless provider.  
- **Google Cloud Functions** → Integrated with Firebase and GCP ecosystem.  
- **Cloudflare Workers** → Runs code at Cloudflare’s **Edge Network** (distributed globally for low latency).  

---

## 5. Cloudflare Workers – How They Work

- Workers run JavaScript/TypeScript functions on the **V8 Engine** (same engine as Chrome & Node.js).  
- They use many standard browser APIs.  
- Instead of running on a single centralized server, they execute on Cloudflare’s **global Edge Network** (hundreds of locations worldwide).  
- Each request is executed close to the user, ensuring **low latency**.  

---

## 6. Isolates vs Containers

- **Traditional Model** → Each function runs in its own **containerized process** (slower cold starts, higher overhead).  
- **Cloudflare Workers Model** → Uses **Isolates** (lightweight, sandboxed V8 contexts).  
  - Start extremely fast.  
  - Consume less memory.  
  - A single runtime can run **hundreds/thousands** of isolates simultaneously.  
  - Ideal for short-lived, event-driven functions.  

**Why isolates?**
- Faster startup than containers.  
- Safer execution (isolated memory per function).  
- Lower cost due to reduced resource usage.  

⚠️ Limitations:  
- Resource restrictions on isolates.  
- Suspicious activity (like escaping sandbox) can terminate isolate.  
- Individual execution time/memory limits.  

---

## 7. Wrangler (Cloudflare CLI)

- **Wrangler** = Cloudflare’s CLI tool to manage and deploy Workers.  
- Features:  
  - Deploy Workers from local dev environment.  
  - Manage routes, KV storage, durable objects.  
  - Provides live preview with `wrangler dev`.  

---

## 8. Hono Framework Motivation

- No good native framework for Cloudflare Workers → led to **Hono** creation.  
- Goals:  
  - Lightweight, ultra-fast router (Trie-based, RegExpRouter).  
  - Middleware support (Basic Auth, GraphQL, Firebase Auth, Sentry).  
  - Node.js adapter for wider ecosystem.  
- Works with Deno, Bun, Cloudflare Workers.  
- **Key Value**: Standardized, Web Standard API support → Express-like experience on serverless.  

---

## 9. Connecting Databases in Serverless

- Challenges:  
  - Each function invocation may open new DB connections → can exhaust DB resources.  
- Solutions:  
  - **Connection Pooling** → manage and reuse connections.  
  - **Prisma Accelerate** → helps manage pooled connections in serverless.  
  - **Neon** (Postgres) → serverless Postgres with built-in connection pooling.  

---

### 🔹 Quick Recap
- Serverless = no server management, pay-per-request.  
- Best for unpredictable/low traffic, rapid deployments.  
- Famous providers: AWS Lambda, GCP Functions, Cloudflare Workers.  
- Cloudflare Workers use **isolates** (faster than containers).  
- Wrangler = CLI for Workers.  
- Hono = lightweight, fast framework for Workers.  
- DB connections in serverless need pooling (Prisma Accelerate, Neon).  
