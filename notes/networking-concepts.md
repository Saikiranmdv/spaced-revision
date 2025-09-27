# Revision Notes

## Topics Covered
1. Address Resolution Protocol (ARP)  
2. Dynamic Host Configuration Protocol (DHCP)  
3. OSI Model and its 7 Layers  
4. Packets and Frames  
5. TCP – Three-Way Handshake  
6. UDP  
7. Ports  

---

## 1. Address Resolution Protocol (ARP)
- **Purpose**: Maps an IP address to a MAC address in a local network.  
- **Process**:  
  - Device broadcasts “Who has IP X?”  
  - The owner replies with its MAC address.  
- **Usage**: Essential for communication within LANs.  
- **Security Risk**: ARP spoofing/poisoning → attacker pretends to be another device.  

---

## 2. Dynamic Host Configuration Protocol (DHCP)
- **Purpose**: Automatically assigns IP addresses and network config to devices.  
- **Process** (DORA):  
  - **D**iscover → client broadcasts request.  
  - **O**ffer → server offers IP.  
  - **R**equest → client requests chosen IP.  
  - **A**ck → server confirms lease.  
- **Config Provided**: IP address, subnet mask, gateway, DNS.  

---

## 3. OSI Model (7 Layers)

1. **Physical** → Transmission of raw bits (cables, NICs).  
2. **Data Link** → Frames, MAC addresses, switches, error detection.  
3. **Network** → Packets, logical addressing (IP), routers.  
4. **Transport** → End-to-end delivery (TCP/UDP, ports, segmentation).  
5. **Session** → Maintains sessions (start/stop/restore communication).  
6. **Presentation** → Data translation, encryption, compression.  
7. **Application** → Interfaces with user apps (HTTP, SMTP, FTP, DNS).  

Easy Mnemonic: **Please Do Not Throw Sausage Pizza Away**

---

## 4. Packets vs Frames
- **Frame**: Data unit at Data Link layer (MAC addresses, inside LAN).  
- **Packet**: Data unit at Network layer (IP addresses, routed across networks).  
- **Encapsulation**: Application data → Segments → Packets → Frames → Bits.  

---

## 5. TCP – Three-Way Handshake
- Ensures **reliable connection** before data transfer.  
1. **SYN** → Client sends synchronization request with initial sequence number.  
2. **SYN-ACK** → Server replies with its sequence number + acknowledges client’s.  
3. **ACK** → Client acknowledges server’s sequence number → connection established.  

Guarantees reliability, ordering, and error correction.  

---

## 6. UDP
- **Connectionless**, lightweight protocol.  
- No handshake, no guarantee of delivery/order.  
- Used in **speed-critical** apps: DNS, video streaming, VoIP, gaming.  

---

## 7. Ports
- Logical endpoints for communication at the **Transport Layer**.  
- **Well-known ports** (0–1023):  
  - 20/21 → FTP  
  - 22 → SSH  
  - 23 → Telnet  
  - 25 → SMTP  
  - 53 → DNS  
  - 80 → HTTP  
  - 443 → HTTPS  
- **Registered ports** (1024–49151): Used by applications.  
- **Dynamic/Ephemeral ports** (49152–65535): Temporary client connections.  

---

### 🔹 Quick Recap
- ARP maps IP → MAC.  
- DHCP auto-assigns IPs (DORA).  
- OSI = 7 layers (Physical → Application).  
- Packet = Network layer, Frame = Data Link.  
- TCP handshake = SYN → SYN-ACK → ACK.  
- UDP = fast, unreliable.  
- Ports = communication endpoints.  
