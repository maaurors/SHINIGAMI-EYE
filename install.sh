#!/bin/bash
#
# SHINIGAMI-EYE Installation Script for Unix/Linux/macOS
# 神死眼 - The All-Seeing Eye
#

set -e

echo "============================================"
echo "    SHINIGAMI-EYE (神死眼) Installer"
echo "    All-Seeing Cybersecurity Framework"
echo "============================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${CYAN}[1/5]${NC} Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed${NC}"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "${GREEN}✓${NC} Found Python ${PYTHON_VERSION}"

# Check pip
echo -e "${CYAN}[2/5]${NC} Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo -e "${YELLOW}⚠${NC}  pip not found, installing..."
    python3 -m ensurepip --upgrade
fi
echo -e "${GREEN}✓${NC} pip is ready"

# Create virtual environment (optional but recommended)
echo -e "${CYAN}[3/5]${NC} Setting up virtual environment (optional)..."
read -p "Create virtual environment? (recommended) [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python3 -m venv venv
    source venv/bin/activate
    echo -e "${GREEN}✓${NC} Virtual environment created and activated"
fi

# Install dependencies
echo -e "${CYAN}[4/5]${NC} Installing dependencies..."
pip3 install -r requirements.txt
echo -e "${GREEN}✓${NC} Dependencies installed"

# Install SHINIGAMI-EYE
echo -e "${CYAN}[5/5]${NC} Installing SHINIGAMI-EYE..."
pip3 install -e .
echo -e "${GREEN}✓${NC} SHINIGAMI-EYE installed"

echo ""
echo -e "${GREEN}============================================${NC}"
echo -e "${GREEN}    Installation Complete! 🎉${NC}"
echo -e "${GREEN}============================================${NC}"
echo ""
echo -e "${CYAN}Usage:${NC}"
echo "  shinigami-eye --help"
echo "  shinigami-eye portscan -t <target>"
echo "  shinigami-eye webrecon -d <domain>"
echo "  shinigami-eye full -t <target>"
echo ""
echo -e "${YELLOW}⚠️  Remember: Educational use only!${NC}"
echo ""
