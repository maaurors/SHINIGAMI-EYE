#!/usr/bin/env python3
"""
SHINIGAMI-EYE Visual Demo - Death Note Edition
Minimalist demonstration
"""
import sys
import time
from pathlib import Path
# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))
from shinigami.utils.ascii_art import (
    print_banner,
    print_status,
    print_module_header
)
def demo():
    """Run demonstration"""
    
    # Print banner
    print_banner()
    time.sleep(1)
    
    # Show modules
    print("Initializing SHINIGAMI-EYE Framework...")
    time.sleep(0.5)
    
    print_status("System check complete", "success")
    print_status("Loading modules...", "info")
    time.sleep(0.3)
    
    print_module_header("PORT SCANNER")
    print_status("TCP scanner ready", "success")
    print_status("Service detection enabled", "success")
    print_status("Banner grabbing active", "success")
    time.sleep(0.4)
    
    print_module_header("WEB RECONNAISSANCE")
    print_status("Subdomain enumeration ready", "success")
    print_status("Technology detector loaded", "success")
    print_status("Security headers analyzer active", "success")
    time.sleep(0.4)
    
    print_module_header("SSL/TLS ANALYZER")
    print_status("Certificate inspector ready", "success")
    print_status("Vulnerability scanner loaded", "success")
    print_status("Cipher analyzer active", "success")
    time.sleep(0.4)
    
    print_module_header("DNS ENUMERATOR")
    print_status("DNS resolver ready", "success")
    print_status("Zone transfer module loaded", "success")
    print_status("DNSSEC validator active", "success")
    time.sleep(0.4)
    
    # Final status
    print()
    print("="*70)
    print("  ✓ ALL SYSTEMS OPERATIONAL")
    print("="*70)
    print()
    
    print("SHINIGAMI-EYE is ready for deployment!")
    print()
    print("Installation:")
    print("  ./install.sh          (Linux/macOS)")
    print("  install.bat           (Windows)")
    print()
    print("Quick Start Commands:")
    print("  shinigami-eye portscan -t <target> --common")
    print("  shinigami-eye webrecon -d <domain>")
    print("  shinigami-eye ssl -H <hostname>")
    print("  shinigami-eye dns -d <domain>")
    print("  shinigami-eye full -t <target> -o report.html")
    print()
    print("⚠️  Educational use only. Unauthorized scanning is ILLEGAL.")
    print()
if __name__ == "__main__":
    try:
        demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted\n")
        sys.exit(0)
