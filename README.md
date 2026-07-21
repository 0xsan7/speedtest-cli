# Speed Test CLI

Professional Internet Speed Testing Tool for the Command Line

[![Tests](https://github.com/0xsan7/speedtest-cli/actions/workflows/test.yml/badge.svg)](https://github.com/0xsan7/speedtest-cli/actions)
[![Code Quality](https://github.com/0xsan7/speedtest-cli/actions/workflows/lint.yml/badge.svg)](https://github.com/0xsan7/speedtest-cli/actions)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square)

## Overview

Speed Test CLI is a lightweight, production-ready command-line tool for testing internet speed. Monitor your connection quality, track performance trends, and export results for analysis—all from the terminal.

Perfect for:
- System administrators monitoring network health
- DevOps engineers tracking connectivity
- Users wanting a CLI alternative to web-based speed tests
- Automating speed tests on servers

## Quick Links

- Installation: [Getting Started](#installation)
- Usage: [Command Reference](#usage)
- Documentation: [Full Guides](#documentation)
- Contributing: [How to Contribute](#contributing)

## Features

Core Functionality:
- Download Speed Testing - Measure how fast data comes to you
- Upload Speed Testing - Measure how fast data goes from you
- Ping Measurement - Check connection latency
- Test History - Track all speed tests in JSON format
- Average Calculation - See performance trends over time
- CSV Export - Export results for spreadsheet analysis
- Colored Output - Beautiful, readable terminal output
- Fast Mode - Quick tests with --simple flag

Developer Features:
- Automated Testing - GitHub Actions CI/CD
- Production Code - Clean, documented, maintainable
- Security Conscious - Local data storage only
- Pip Installable - pip install support via setup.py
- Development Tools - Makefile, linting, testing

## Installation

Minimum Requirements:
- Python 3.9 or higher
- pip package manager
- Active internet connection

Installation Options:

Option 1: Clone from GitHub (Recommended)
```bash
git clone https://github.com/0xsan7/speedtest-cli.git
cd speedtest-cli
pip install -r requirements.txt
```

Option 2: Quick Install
```bash
pip install -r requirements.txt
python speedtest_cli.py
```

Option 3: Development Setup
```bash
git clone https://github.com/0xsan7/speedtest-cli.git
cd speedtest-cli
pip install -e .
speedtest
```

Verify Installation:
```bash
python speedtest_cli.py --help
```

## Quick Start

Run Your First Speed Test:
```bash
python speedtest_cli.py
```

This will:
1. Find the best server near you
2. Test your download speed
3. Test your upload speed
4. Measure your ping
5. Display results
6. Save to history

Expected Output:
==================================================
SPEED TEST RESULTS
Download Speed: 95.47 Mbps
Upload Speed: 50.23 Mbps
Ping: 12.45 ms
Server: ISP Server
Location: Pune, India
Timestamp: 2026-07-06T20:39:44.255653
==================================================
Results saved to speedtest_history.json
## Usage

Basic Speed Test:
```bash
python speedtest_cli.py
```

View Test History:
```bash
python speedtest_cli.py --history
```

Output Format:
======================================================================
SPEED TEST HISTORY
Date Download (Mbps) Upload (Mbps)
2026-07-06 95.47 50.23
2026-07-05 87.32 48.15
2026-07-04 92.11 51.04
View Average Speeds:
```bash
python speedtest_cli.py --average
```

Output:
==================================================
AVERAGE SPEEDS
Tests Run: 3
Avg Download: 91.63 Mbps
Avg Upload: 49.81 Mbps
==================================================
Export to CSV:
```bash
python speedtest_cli.py --export
```

Creates speedtest_results.csv with all historical data for spreadsheet analysis.

Faster Testing:
```bash
python speedtest_cli.py --simple
```

Uses fewer threads for quicker results (less accurate).

Disable Colors:
```bash
python speedtest_cli.py --no-color
```

For piping output or non-color terminals.

Command Reference:

| Command | Description |
|---------|-------------|
| python speedtest_cli.py | Run a full speed test |
| --history | Show test history (last 10) |
| --average | Show average speeds from all tests |
| --export | Export history to CSV file |
| --simple | Run faster test (less accurate) |
| --no-color | Disable colored output |
| --help | Show help message |

