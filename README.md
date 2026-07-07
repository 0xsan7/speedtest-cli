# Speed Test CLI

Professional internet speed testing tool for the command line. Test your download/upload speeds and track trends over time.

[![Tests](https://github.com/0xsan7/speedtest-cli/actions/workflows/test.yml/badge.svg)](https://github.com/0xsan7/speedtest-cli/actions)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

## Features

- Test download and upload speeds
- Measure ping/latency
- Track test history in JSON format
- Export results to CSV
- View average speeds over time
- Simple mode for faster testing
- Cross-platform (Mac, Linux, Windows)
- Production-ready code

## Installation

### Option 1: From source
```bash
git clone https://github.com/0xsan7/speedtest-cli.git
cd speedtest-cli
pip install -e .
```

### Option 2: Using pip
```bash
pip install -r requirements.txt
python speedtest_cli.py
```

## Usage

### Run a speed test
```bash
python speedtest_cli.py
```

### View test history
```bash
python speedtest_cli.py --history
```

### View average speeds
```bash
python speedtest_cli.py --average
```

### Export to CSV
```bash
python speedtest_cli.py --export
```

### Faster testing
```bash
python speedtest_cli.py --simple
```

## Output Example
==================================================
SPEED TEST RESULTS
Download Speed: 95.47 Mbps
Upload Speed:   50.23 Mbps
Ping:           12.45 ms
Server:         ISP Server
Location:       City, Country
Timestamp:      2026-07-06T20:39:44.255653
==================================================
Results saved to speedtest_history.json
## Data Storage

- Results are stored in `speedtest_history.json` (JSON format)
- Export to `speedtest_results.csv` for use in spreadsheets
- All data stored locally on your machine
- No data sent to third parties except Speedtest.net

## Requirements

- Python 3.9 or higher
- speedtest-cli library

## Documentation

- [EXAMPLES.md](EXAMPLES.md) - Advanced usage examples
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [CHANGELOG.md](CHANGELOG.md) - Release history

## Performance

- Typical test: 30-60 seconds
- Download/upload measured in Mbps
- Ping measured in milliseconds
- Results accurate to 2 decimal places

## License

MIT License - see [LICENSE](LICENSE) file

## Author

Made by [0xsan7](https://github.com/0xsan7)

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

**Status:** Production Ready | **Version:** 1.0.0 | **Last Updated:** 2026-07-06
