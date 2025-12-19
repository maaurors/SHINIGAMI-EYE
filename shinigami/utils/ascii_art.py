"""
ASCII Art Module - Death Note Inspired
Epic visual effects for SHINIGAMI-EYE framework
"""
import time
import sys
from typing import Optional

class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    PURPLE = '\033[35m'
    DARK_RED = '\033[31m'
    BLACK = '\033[30m'
    GRAY = '\033[90m'

DEATH_NOTE_BANNER = f"""{Colors.BOLD}{Colors.RED}
        ██████╗ ██╗  ██╗██╗███╗   ██╗██╗ ██████╗  █████╗ ███╗   ███╗██╗    ███████╗██╗   ██╗███████╗
       ██╔════╝ ██║  ██║██║████╗  ██║██║██╔════╝ ██╔══██╗████╗ ████║██║    ██╔════╝╚██╗ ██╔╝██╔════╝
       ███████╗ ███████║██║██╔██╗ ██║██║██║  ███╗███████║██╔████╔██║██║    █████╗   ╚████╔╝ █████╗  
       ╚════██║ ██╔══██║██║██║╚██╗██║██║██║   ██║██╔══██║██║╚██╔╝██║██║    ██╔══╝    ╚██╔╝  ██╔══╝  
       ███████║ ██║  ██║██║██║ ╚████║██║╚██████╔╝██║  ██║██║ ╚═╝ ██║██║    ███████╗   ██║   ███████╗
       ╚══════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝    ╚══════╝   ╚═╝   ╚══════╝
{Colors.END}
{Colors.BOLD}{Colors.CYAN}                                       神 死 眼 - The All-Seeing Eye{Colors.END}
                                            
{Colors.GRAY}                    
                              {Colors.BOLD}{Colors.BLACK}╔════════════════════════════════════════════╗
                              {Colors.BLACK}║{Colors.END}                                            {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.WHITE}██████╗ ███████╗ █████╗ ████████╗██╗  ██╗{Colors.END}  {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.WHITE}██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║{Colors.END}  {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.WHITE}██║  ██║█████╗  ███████║   ██║   ███████║{Colors.END}  {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.WHITE}██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║{Colors.END}  {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.WHITE}██████╔╝███████╗██║  ██║   ██║   ██║  ██║{Colors.END}  {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.WHITE}╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝{Colors.END}  {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}                                            {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.RED}███╗   ██╗ ██████╗ ████████╗███████╗{Colors.END}      {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.RED}████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝{Colors.END}      {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.RED}██╔██╗ ██║██║   ██║   ██║   █████╗{Colors.END}        {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.RED}██║╚██╗██║██║   ██║   ██║   ██╔══╝{Colors.END}        {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.RED}██║ ╚████║╚██████╔╝   ██║   ███████╗{Colors.END}      {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.RED}╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝{Colors.END}      {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}                                            {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.GRAY}────────────────────────────────────────{Colors.END}  {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}                                            {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.BOLD}{Colors.CYAN}How to use:{Colors.END}                             {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}                                            {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.WHITE}• Write target's IP/domain in this book{Colors.END} {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.WHITE}• Their network secrets will be revealed{Colors.END}{Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.WHITE}• All ports, services, and vulns exposed{Colors.END}{Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}                                            {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.GRAY}────────────────────────────────────────{Colors.END}  {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}                                            {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.YELLOW}Target: ____________________________{Colors.END}      {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}                                            {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.YELLOW}Method: [ ] Port Scan  [ ] Web Recon{Colors.END}   {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}  {Colors.YELLOW}        [ ] SSL Check  [ ] DNS Enum{Colors.END}    {Colors.BLACK}║
                              {Colors.BLACK}║{Colors.END}                                            {Colors.BLACK}║
                              {Colors.BLACK}╚════════════════════════════════════════════╝{Colors.END}
{Colors.END}                              
                        {Colors.CYAN}[ Network Reconnaissance & Security Intelligence Framework ]{Colors.END}
                                    {Colors.YELLOW}Version 1.0.0 - "Death Note Edition"{Colors.END}
                                          {Colors.RED}Educational Use Only{Colors.END}
"""

def print_banner():
    """Print the main SHINIGAMI-EYE banner"""
    print(DEATH_NOTE_BANNER)

def animate_text(text: str, color: str = Colors.CYAN, delay: float = 0.03):
    """Animate text character by character"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_status(message: str, status: str = "info"):
    """Print formatted status message"""
    symbols = {
        "success": f"{Colors.GREEN}[✓]{Colors.END}",
        "error": f"{Colors.RED}[✗]{Colors.END}",
        "warning": f"{Colors.YELLOW}[!]{Colors.END}",
        "info": f"{Colors.CYAN}[i]{Colors.END}",
        "scan": f"{Colors.MAGENTA}[◉]{Colors.END}"
    }
    symbol = symbols.get(status, symbols["info"])
    print(f"{symbol} {message}")

def print_module_header(module_name: str):
    """Print module header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.PURPLE}  {module_name}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}\n")

if __name__ == "__main__":
    print_banner()
    time.sleep(1)
    animate_text("Opening the Death Note...", Colors.RED, 0.04)
    time.sleep(0.5)
    print_status("Network scanner loaded", "success")
    print_status("Vulnerability database ready", "success")
    print_status("Intelligence modules active", "success")
    print_status("All systems operational", "success")
    print()
    print(f"{Colors.BOLD}{Colors.RED}Remember: Those who use this tool must follow the rules...{Colors.END}")
    print(f"{Colors.YELLOW}Rule I: Only scan systems you own or have permission to test{Colors.END}")
    print(f"{Colors.YELLOW}Rule II: Unauthorized access is illegal and punishable by law{Colors.END}")
