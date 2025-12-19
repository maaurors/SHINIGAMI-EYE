# SHINIGAMI-EYE - Installation & Usage Guide

## Framework Overview

**SHINIGAMI-EYE** (神死眼) is a comprehensive cybersecurity framework for network reconnaissance and security intelligence gathering.

### Current Location

The framework is located at:
```
~/Desktop/SHINIGAMI-EYE
```

---

## Quick Installation

### On Linux/macOS:

```bash
cd ~/Desktop/SHINIGAMI-EYE
./install.sh
```

This will automatically install all dependencies and set up the framework.

### On Windows:

```cmd
cd Desktop\SHINIGAMI-EYE
install.bat
```

---

## Visual Demo

To see the Death Note banner without installing, run:

```bash
cd ~/Desktop/SHINIGAMI-EYE
python3 demo.py
```

---

## Core Features

### Port Scanner
- Multi-threaded TCP scanning (up to 200 threads)
- Service detection and identification
- Banner grabbing for fingerprinting
- Common ports and custom range support

### Web Reconnaissance
- Subdomain enumeration
- Technology detection (CMS, frameworks)
- Security headers analysis
- Directory discovery

### SSL/TLS Analyzer
- Certificate inspection
- Vulnerability detection (Heartbleed, POODLE, BEAST)
- Cipher analysis
- Expiration validation

### DNS Enumerator
- Comprehensive DNS record queries
- Zone transfer attempts (AXFR)
- Reverse DNS lookups
- DNSSEC validation

### Reporting System
- Interactive HTML reports
- Structured JSON export
- Markdown documentation

---

## Basic Usage

After installation:

```bash
# View help
shinigami-eye --help

# Quick port scan
shinigami-eye portscan -t scanme.nmap.org --common

# Web reconnaissance
shinigami-eye webrecon -d example.com

# SSL/TLS analysis
shinigami-eye ssl -H example.com

# DNS enumeration
shinigami-eye dns -d example.com

# Full scan with HTML report
shinigami-eye full -t example.com -o report.html
```

---

## Scan Profiles

SHINIGAMI-EYE includes pre-configured scanning profiles:

- **Stealth**: Slow and stealthy, minimal detection
- **Aggressive**: Fast and comprehensive, maximum speed  
- **Complete**: Maximum coverage, all ports

---

## Documentation

- `README.md` - Complete documentation
- `config/` - Configuration files
- `wordlists/` - Wordlists for attacks

---

## Legal Disclaimer

**IMPORTANT**: SHINIGAMI-EYE is for **EDUCATIONAL USE** and **AUTHORIZED TESTING** only.

- ✅ Only scan systems you own or have explicit permission to test
- ✅ Comply with all applicable laws and regulations
- ❌ DO NOT use for illegal or malicious activities

**Unauthorized access to computer systems is ILLEGAL.**

---

## Framework Status

The framework is:
- ✅ 100% functional
- ✅ Fully documented
- ✅ Ready to deploy
- ✅ Multi-platform
- ✅ Production-ready

---

## Support

If you have questions or issues:

1. Read the complete `README.md`
2. Check the configuration files in `config/`
3. Test with `demo.py` to verify functionality

---

**神死眼 - The Eye That Sees All**

*Created for educational and authorized security testing purposes*
