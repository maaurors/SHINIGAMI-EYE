# 神死眼 SHINIGAMI-EYE

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-Educational-red.svg)

**The All-Seeing Cybersecurity Framework**

*Network Reconnaissance • Security Intelligence • Vulnerability Assessment*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Disclaimer](#%EF%B8%8F-disclaimer)

</div>

---

## 🎯 Overview

**SHINIGAMI-EYE** (神死眼 - "The Eye of the Death God") is a next-generation, all-in-one cybersecurity framework designed for comprehensive network reconnaissance and security intelligence gathering. Inspired by anime aesthetics and built with cutting-edge technology, it combines multiple security tools into a unified, powerful platform.

### Why SHINIGAMI-EYE?

- **🔍 All-in-One**: Port scanning, web recon, SSL analysis, DNS enumeration - all in one tool
- **⚡ Lightning Fast**: Multi-threaded scanning with configurable performance
- **🎨 Beautiful Output**: Rich terminal UI with colored output and epic ASCII art
- **📊 Professional Reports**: Generate HTML, JSON, and Markdown reports
- **🌐 Cross-Platform**: Works seamlessly on Windows, Linux, and macOS
- **🛡️ Security Focused**: Built by security professionals for security professionals

---

## ✨ Features

### 🔌 Port Scanner
- **TCP Connect Scanning** with multi-threading
- **Service Detection** and version identification
- **Banner Grabbing** for fingerprinting
- **Common Ports** and custom range support
- Configurable timeout and thread count

### 🌐 Web Reconnaissance
- **Subdomain Enumeration** via DNS and brute-force
- **Technology Detection** (CMS, frameworks, libraries)
- **Security Headers Analysis**
- **Directory Discovery**
- **Responsive Web Scraping**

### 🔐 SSL/TLS Analyzer
- **Certificate Inspection** (validity, issuer, expiration)
- **Cipher Suite Analysis**
- **Vulnerability Detection** (Heartbleed, POODLE, BEAST)
- **Weak Encryption Identification**
- **DNSSEC Validation**

### 📊 DNS Enumerator
- **Comprehensive Record Queries** (A, AAAA, MX, TXT, NS, SOA, etc.)
- **Zone Transfer Attempts** (AXFR)
- **Reverse DNS Lookups**
- **DNSSEC Configuration Check**
- **Wildcard Detection**

### 📄 Advanced Reporting
- **HTML Reports**: Beautiful, interactive HTML dashboards
- **JSON Export**: Machine-readable structured data
- **Markdown**: Human-readable documentation
- **Terminal Output**: Real-time colored feedback

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Install

#### On Linux/macOS:
```bash
git clone https://github.com/yourusername/shinigami-eye.git
cd shinigami-eye
chmod +x install.sh
./install.sh
```

#### On Windows:
```cmd
git clone https://github.com/yourusername/shinigami-eye.git
cd shinigami-eye
install.bat
```

### Manual Installation
```bash
# Install dependencies
pip3 install -r requirements.txt

# Install SHINIGAMI-EYE
pip3 install -e .
```

---

## 🚀 Usage

### Basic Commands

```bash
# Show help
shinigami-eye --help

# Port scan
shinigami-eye portscan -t <target> --common

# Web reconnaissance
shinigami-eye webrecon -d <domain>

# SSL/TLS analysis
shinigami-eye ssl -H <hostname>

# DNS enumeration
shinigami-eye dns -d <domain>

# Full scan (all modules)
shinigami-eye full -t <target> -o report.html
```

---

## 📚 Examples

### 1. Quick Port Scan
Scan common ports on a target:
```bash
shinigami-eye portscan -t 192.168.1.1 --common
```

### 2. Full Port Range Scan
Scan all ports from 1-65535:
```bash
shinigami-eye portscan -t example.com -s 1 -e 65535 -o portscan.json
```

### 3. Web Reconnaissance
Enumerate subdomains and detect technologies:
```bash
shinigami-eye webrecon -d example.com --discover-dirs -o webrecon.html
```

### 4. SSL Certificate Analysis
Analyze SSL/TLS configuration and vulnerabilities:
```bash
shinigami-eye ssl -H example.com -p 443
```

### 5. DNS Intelligence
Perform comprehensive DNS enumeration:
```bash
shinigami-eye dns -d example.com -o dns_report.json
```

### 6. Complete Assessment
Run all modules and generate comprehensive report:
```bash
shinigami-eye full -t example.com -f html -o full_assessment.html
```

---

## 🎨 Features Showcase

### Epic ASCII Banner
```
        ██████╗ ██╗  ██╗██╗███╗   ██╗██╗ ██████╗  █████╗ ███╗   ███╗██╗    ███████╗██╗   ██╗███████╗
       ██╔════╝ ██║  ██║██║████╗  ██║██║██╔════╝ ██╔══██╗████╗ ████║██║    ██╔════╝╚██╗ ██╔╝██╔════╝
       ███████╗ ███████║██║██╔██╗ ██║██║██║  ███╗███████║██╔████╔██║██║    █████╗   ╚████╔╝ █████╗  
       ╚════██║ ██╔══██║██║██║╚██╗██║██║██║   ██║██╔══██║██║╚██╔╝██║██║    ██╔══╝    ╚██╔╝  ██╔══╝  
       ███████║ ██║  ██║██║██║ ╚████║██║╚██████╔╝██║  ██║██║ ╚═╝ ██║██║    ███████╗   ██║   ███████╗
       ╚══════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝    ╚══════╝   ╚═╝   ╚══════╝

                                        神 死 眼 - The All-Seeing Eye
```

### Rich Terminal Output
- ✅ Color-coded status messages
- 📊 Real-time progress indicators
- ⚡ Performance statistics
- 🎯 Organized, readable results

### Professional HTML Reports
- 📈 Interactive dashboards
- 🎨 Modern, gradient design
- 📱 Responsive layout
- 🔍 Detailed findings with visual highlighting

---

## 🛠️ Advanced Configuration

### Custom Wordlists
Place custom wordlists in the `wordlists/` directory:
- `subdomains.txt` - Subdomain enumeration
- `directories.txt` - Directory discovery
- `common_ports.txt` - Port scanning

### Scan Profiles
Modify scan profiles in `config/profiles/`:
- `stealth.yaml` - Low and slow
- `aggressive.yaml` - Fast and comprehensive
- `complete.yaml` - Maximum coverage

---

## 📖 Module Details

### Port Scanner
- **Techniques**: TCP Connect
- **Performance**: Up to 100 concurrent threads
- **Features**: Service detection, banner grabbing
- **Output**: Port, service, banner information

### Web Recon
- **Methods**: DNS queries, HTTP requests
- **Capabilities**: Subdomain enum, tech stack detection
- **Security**: Headers analysis, directory discovery
- **Output**: Subdomains, technologies, directories

### SSL Analyzer
- **Checks**: Certificate validity, cipher strength
- **Vulnerabilities**: Heartbleed, POODLE, BEAST, etc.
- **Details**: Issuer, expiration, SAN, algorithm
- **Output**: Certificate info, vulnerabilities, risk level

### DNS Enumerator
- **Records**: A, AAAA, MX, TXT, NS, SOA, SRV, PTR
- **Advanced**: Zone transfers, reverse DNS, DNSSEC
- **Intelligence**: Wildcard detection, nameserver analysis
- **Output**: All DNS records, zone data, security config

---

## ⚠️ Disclaimer

**IMPORTANT - READ CAREFULLY**

SHINIGAMI-EYE is designed for **EDUCATIONAL PURPOSES** and **AUTHORIZED SECURITY TESTING** only.

### Legal Notice
- ✅ **Authorized Use**: Only scan systems you own or have explicit written permission to test
- ✅ **Compliance**: Ensure compliance with all applicable laws and regulations
- ✅ **Ethics**: Use responsibly and ethically

- ❌ **Prohibited**: Unauthorized scanning of systems is ILLEGAL
- ❌ **Criminal**: Violators may face criminal prosecution
- ❌ **Liability**: Authors are not responsible for misuse

### By using this tool, you agree to:
1. Only use for legal and authorized purposes
2. Comply with all applicable laws
3. Not use for malicious activities
4. Accept full responsibility for your actions

**Unauthorized access to computer systems is a violation of computer fraud and abuse laws in most jurisdictions.**

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed for **Educational Use Only**. See the `LICENSE` file for details.

---

## 🙏 Acknowledgments

- Inspired by tools like Nmap, Nikto, SSLyze, and DNSRecon
- ASCII art inspired by Naruto and Death Note
- Built with love for the security community

---

## 📞 Support

- 📧 Email: support@shinigami-eye.io
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/shinigami-eye/issues)
- 💬 Discord: [Join our server](https://discord.gg/shinigami-eye)

---

<div align="center">

**Made with 🔥 by Security Enthusiasts**

*神死眼 - The Eye That Sees All*

</div>
