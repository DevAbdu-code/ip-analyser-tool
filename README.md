#  IP Intelligence Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-2.0.0-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC_BY--ND_4.0-lightgrey?style=for-the-badge)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)

> *"Network intelligence at your fingertips"*

</div>

---

##  About

**IP Intelligence Tool** is a comprehensive Python-based CLI tool for IP address analysis and network intelligence gathering.

### ✨ Features

| Feature | Description |
|---------|-------------|
| **IP Validation** | Validate IPv4 addresses with proper formatting |
| **Geolocation** | Get country, city, coordinates, ISP, ASN |
| **DNS Lookup** | Forward and reverse DNS resolution |
| **WHOIS Query** | Domain registration and ownership details |
| **Network Analysis** | Class, type, CIDR, binary/hex representation |
| **Threat Intelligence** | Check against threat databases (AbuseIPDB) |
| **Multiple Outputs** | Table, JSON, and CSV formats |
| **Export Results** | Save analysis to files |

---

##  Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/DevAbdu-code/ip-analyser-tool.git
cd ip-analyser-tool

# Install dependencies
pip install -r requirements.txt

# Make it executable
chmod +x ip_analyser.py
```

### Basic Usage

```bash
# Analyze an IP address
python3 ip_analyser.py 8.8.8.8

# JSON output
python3 ip_analyser.py 8.8.8.8 --format json

# Export to file
python3 ip_analyser.py 8.8.8.8 --output report.json

# Specific modules only
python3 ip_analyser.py 8.8.8.8 --modules geo,dns
```
---

### 📖 Usage Examples

### Example 1: Basic Analysis
```bash
$ python3 ip_analyser.py 8.8.8.8

============================================================
 IP Analysis Results
============================================================

 IP: 8.8.8.8
 Timestamp: 2026-08-08T10:30:00

 Geolocation:
  Country: United States
  City: Mountain View
  ISP: Google LLC
  Coordinates: 37.386, -122.0838

 Network:
  Class: Class A
  Type: Public
  Binary: 00001000.00001000.00001000.00001000

 DNS:
  Reverse DNS: dns.google

 WHOIS:
  Registrar: Google LLC
  Organization: Google LLC

🛡️ Threat Intelligence:
  Threat Score: 0
  Total Reports: 0
  Malicious:  NO

============================================================
```
---

### Example 1: Basic Analysis

```bash
$ python3 ip_analyser.py 8.8.8.8 --format json
{
  "ip": "8.8.8.8",
  "timestamp": "2026-08-08T10:30:00",
  "analysis": {
    "geolocation": {
      "country": "United States",
      "city": "Mountain View",
      "isp": "Google LLC"
    },
    ...
  }
}
```
---

### Project Structure

```text
ip-analyser-tool/
├── ip_analyser.py          # Main script
├── README.md               # Documentation
├── LICENSE.md              # License
├── requirements.txt        # Dependencies
├── setup.py                # Package setup
├── config/
│   └── config.yaml         # Configuration
├── modules/                # Core modules
│   ├── validator.py
│   ├── geolocation.py
│   ├── dns_lookup.py
│   ├── whois_lookup.py
│   ├── network_info.py
│   └── security_check.py
├── utils/
│   └── formatter.py        # Output formatting
└── examples/
    └── sample_output.txt   # Example outputs
```
--- 

##  Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| `requests` | >=2.31.0 | HTTP requests for API calls |
| `python-whois` | >=0.8.0 | WHOIS queries |
| `dnspython` | >=2.4.2 | DNS resolution |
| `pyyaml` | >=6.0 | Configuration parsing |

---

##  Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push: `git push origin feature/amazing`
5. Open a Pull Request

---

## ⚠️ Disclaimer

> **FOR EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY.**  
> This tool is intended for use on systems you own or have explicit permission to test. Unauthorized access is illegal.

---

## 📜 License

This project is licensed under the **Creative Commons Attribution-NoDerivatives 4.0 International License**.

| You CAN  | You CANNOT  |
|------------|---------------|
| Share and redistribute | Modify or adapt |
| Use for personal study | Remove author credit |
| Use in presentations | Claim as your own |

<sub>📚 Source: [ip-analyser-tool](https://github.com/DevAbdu-code/ip-analyser-tool) • ✍️ Abdu (DevAbdu-code) • 📜 CC BY-ND 4.0</sub>

---

<div align="center">

**⭐ If you find this tool helpful, please consider giving a star!**

*Built with 💻, 🔐, and ☕*

</div>
