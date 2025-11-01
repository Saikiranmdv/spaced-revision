# 📘 Revision Notes

## Topics Covered
1. Downloading Files (Wget)  
2. Transferring Files (SCP)  
3. Serving Files via Web Server (Python HTTPServer)  
4. Viewing and Managing Processes  
5. Understanding Namespaces and Process Lifecycle  
6. Managing Services on Boot (systemctl)  
7. Foregrounding & Backgrounding Processes  
8. Automating Tasks with Cron (Crontabs)  
9. Packages and Software Repositories (apt)  
10. Managing System Logs  

---

## 1. Downloading Files (Wget)

- **Purpose:** Used to download files from the internet via HTTP/HTTPS.  
- **Syntax:**
  ```bash
  wget <URL>
  ```
  Example:
  ```bash
  wget https://assets.tryhackme.com/additional/linux-fundamentals/part3/myfile.txt
  ```
- **Usage:** Works like downloading a file in your browser.  
- **Tip:** Supports batch downloads and recursive downloading with flags (`-r`, `-O`, etc.).

---

## 2. Transferring Files (SCP)

- **Purpose:** Securely copy files between local and remote systems using SSH.  
- **Format:**  
  ```bash
  scp <source> <destination>
  ```
- **Example (Local → Remote):**
  ```bash
  scp important.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt
  ```
- **Example (Remote → Local):**
  ```bash
  scp ubuntu@192.168.1.30:/home/ubuntu/documents.txt notes.txt
  ```
- **Key Points:**
  - Encrypts data and credentials.
  - Requires username/password or SSH key authentication.
  - Supports both file and directory transfer with `-r`.

---

## 3. Serving Files from Your Host (Web)

- **Python HTTPServer:**  
  Lightweight web server built into Python3.  
  ```bash
  python3 -m http.server
  ```
- **Default Port:** `8000`  
  Serves files from the current working directory.  
- **Example of Downloading a File:**
  ```bash
  wget http://10.201.10.104:8000/myfile
  ```
- **Tip:** Run the server in one terminal and download from another.

---

## 4. Viewing Processes

- **Definition:** Processes are running programs managed by the kernel, each with a unique **PID (Process ID)**.

### Commands:
- **List current user's processes:**
  ```bash
  ps
  ```
- **List all processes:**
  ```bash
  ps aux
  ```
- **Real-time process view:**
  ```bash
  top
  ```
  - Displays live CPU, memory, and process info.  
  - Refreshes every 10 seconds.

---

## 5. Managing Processes

- **Terminate a Process:**
  ```bash
  kill <PID>
  ```
- **Signals:**
  - `SIGTERM` → Graceful shutdown (cleanup allowed).  
  - `SIGKILL` → Immediate termination (no cleanup).  
  - `SIGSTOP` → Suspend/stop process.  

---

## 6. How Processes Start – Namespaces

- **Namespaces:**  
  The OS uses namespaces to isolate resources (CPU, RAM, network) between processes for security.  
- **PID 0:** The first process started by the system (the **init/systemd** process).  
- **systemd:**  
  - Manages system services and child processes.  
  - Acts as a parent for user-launched processes.

---

## 7. Managing Services (systemctl)

Used to control systemd-managed services.

**Syntax:**
```bash
systemctl [option] [service]
```

| Option  | Description             | Example                     |
|----------|------------------------|-----------------------------|
| start    | Start a service        | `systemctl start apache2`   |
| stop     | Stop a service         | `systemctl stop apache2`    |
| enable   | Start service on boot  | `systemctl enable apache2`  |
| disable  | Prevent startup on boot| `systemctl disable apache2` |

---

## 8. Foregrounding & Backgrounding Processes

- **Foreground:** Process occupies the terminal until finished.  
  Example:
  ```bash
  echo "Hello THM"
  ```

- **Background:** Add `&` at the end to run without blocking:
  ```bash
  echo "Hello THM" &
  ```
  - Returns process ID (PID) immediately.

- **Suspend with `Ctrl + Z`** → pauses the process.  
- **Bring back to foreground:**
  ```bash
  fg
  ```

---

## 9. Automation with Cron (Crontabs)

- **Cron:** Daemon that schedules recurring tasks.  
- **Crontab Syntax:**  
  ```
  MIN HOUR DOM MON DOW CMD
  ```

| Field | Description |
|-------|-------------|
| MIN   | Minute (0–59) |
| HOUR  | Hour (0–23) |
| DOM   | Day of Month |
| MON   | Month |
| DOW   | Day of Week |
| CMD   | Command to execute |

**Example (backup every 12 hours):**
```bash
0 */12 * * * cp -R /home/cmnatic/Documents /var/backups/
```

- **Edit crontab:**
  ```bash
  crontab -e
  ```
- **Tools:**  
  - [Crontab Generator](https://crontab-generator.org/)  
  - [Cron Guru](https://crontab.guru/)  

---

## 10. Packages & Software Repositories

### 🔹 Repositories
- **apt** = Package manager for Ubuntu/Debian systems.
- **Default repositories** maintained by OS vendors.
- **Community repositories** can be added for extra software.

### 🔹 Adding a Repository (Example: Sublime Text)
1. Add developer GPG key:
   ```bash
   wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
   ```
2. Create repo file:
   ```bash
   sudo nano /etc/apt/sources.list.d/sublime-text.list
   ```
3. Add repo URL:
   ```
   deb https://download.sublimetext.com/ apt/stable/
   ```
4. Update and install:
   ```bash
   sudo apt update
   sudo apt install sublime-text
   ```

### 🔹 Removing a Repository
```bash
sudo add-apt-repository --remove ppa:PPA_Name/ppa
sudo apt remove sublime-text
```

---

## 11. Managing System Logs

- **Location:** `/var/log/`
- **Purpose:** Store system and application logs.  
- **Examples:**
  - **/var/log/apache2/** → Web server logs.  
  - **/var/log/fail2ban.log** → Brute-force protection logs.  
  - **/var/log/ufw.log** → Firewall logs.  
- **Key Log Types:**
  - `access.log` → Records requests to the service.  
  - `error.log` → Records service errors.  
- **Log Rotation:**  
  - Automatic cleanup and archiving of old logs by the OS.

---

### 🔹 Quick Recap
- `wget` → Download files.  
- `scp` → Securely transfer files between systems.  
- `python3 -m http.server` → Serve files via HTTP.  
- `ps`, `top` → View running processes.  
- `kill`, `systemctl` → Manage processes and services.  
- `fg`, `bg` → Move processes between states.  
- `crontab` → Schedule recurring tasks.  
- `apt` → Manage packages and repositories.  
- `/var/log/` → System logs for monitoring and troubleshooting.
