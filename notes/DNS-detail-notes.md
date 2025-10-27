# Revision Notes 08-10-2025

## Topics Covered
1. Domain Hierarchy  
2. DNS Record Types  
3. DNS Request Flow  

---

## 1. Domain Hierarchy

- **Root Domain (`.`)** → top of the hierarchy.  
- **Top-Level Domain (TLD)** → rightmost part (e.g., `.com`, `.edu`, `.gov`).  
  - Types:  
    - **gTLD** → Generic (e.g., `.com`, `.org`).  
    - **ccTLD** → Country Code (e.g., `.uk`, `.in`, `.ca`).  
- **Second-Level Domain (SLD)** → name chosen by the registrant (e.g., `tryhackme` in `tryhackme.com`).  
  - Limited to 63 characters.  
  - Can use `a–z`, `0–9`, and hyphens (cannot start or end with hyphen, no consecutive hyphens).  
- **Subdomain** → part added before the SLD (e.g., `admin.tryhackme.com`).  
  - Same naming restrictions as SLD.  
  - Max 253 characters for the full domain.  
  - Unlimited subdomains possible.

---

## 2. DNS Record Types

- **A Record** → Maps hostname to IPv4 address (e.g., `104.26.10.229`).  
- **AAAA Record** → Maps hostname to IPv6 address (e.g., `2606:4700:20::681a:eb5`).  
- **CNAME Record** → Alias pointing to another domain (e.g., `store.tryhackme.com` → `shops.shopify.com`).  
- **MX Record** → Specifies mail servers for a domain.  
  - Includes priority numbers → tells clients which server to try first.  
- **TXT Record** → Stores free-text data. Common uses:  
  - Email authentication (SPF, DKIM).  
  - Domain ownership verification.  
  - Custom metadata.  

---

## 3. DNS Request Flow

Steps when you make a DNS query (e.g., `tryhackme.com`):

1. **Local Cache** → Computer checks if it already knows the IP.  
2. **Recursive DNS Server** → ISP or configured DNS server (Google DNS, Cloudflare, etc.).  
   - If cached locally, reply is returned.  
   - If not cached, query continues.  
3. **Root DNS Server** → Directs to correct TLD server (e.g., `.com`).  
4. **TLD DNS Server** → Tells which authoritative server is responsible for the SLD (e.g., Cloudflare for `tryhackme.com`).  
5. **Authoritative DNS Server** → Provides the actual IP address of the domain.  
   - Stores DNS records for the domain.  
   - Returns the correct A/AAAA/CNAME/MX/TXT record.  

**TTL (Time To Live)**: Defines how long a record is cached before needing re-validation.  

---

### 🔹 Quick Recap
- DNS translates human-readable names → IP addresses.  
- Domain hierarchy = Root → TLD → SLD → Subdomain.  
- Common records: **A (IPv4)**, **AAAA (IPv6)**, **CNAME (alias)**, **MX (mail)**, **TXT (text/authentication)**.  
- DNS resolution flow: Cache → Recursive → Root → TLD → Authoritative.
