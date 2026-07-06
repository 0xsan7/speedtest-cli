# Speed Test CLI

Test your internet speed directly from the command line. No browser needed.

![Python](https://img.shields.io/badge/Python-3.7+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- Test download and upload speeds
- Measure ping/latency
- Track test history
- View average speeds over time
- Simple, fast command-line interface

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run a speed test

```bash
python speedtest_cli.py
```

This will:
1. Find the best server near you
2. Test download speed
3. Test upload speed
4. Display results
5. Save results to history

### View test history

```bash
python speedtest_cli.py --history
```

Shows your last 10 speed tests in a table.

### View average speeds

```bash
python speedtest_cli.py --average
```

Shows average download/upload speeds from all your tests.

### Faster testing

```bash
python speedtest_cli.py --simple
```

Runs a faster test (less accurate but quicker).

## Examples

Run a standard test:
```bash
python speedtest_cli.py
```

Check how your speed has been over time:
```bash
python speedtest_cli.py --history
```

See your average internet speed:
```bash
python speedtest_cli.py --average
```

## Output
==================================================
SPEED TEST RESULTS
Download Speed: 95.47 Mbps
Upload Speed:   50.23 Mbps
Ping:           12.45 ms
Server:         ISP Server
Location:       City, Country
Timestamp:      2024-07-05T12:30:45.123456
==================================================
Results saved to speedtest_history.json
## Requirements

- Python 3.7+
- speedtest-cli library

## How It Works

1. Connects to Speedtest.net servers
2. Finds the best server near your location
3. Tests download speed (how fast data comes to you)
4. Tests upload speed (how fast data goes from you)
5. Measures ping (connection latency)
6. Saves results to a JSON file for tracking

## Tips

- First test may take longer as it finds the best server
- Run multiple tests at different times to track trends
- History is saved in `speedtest_history.json`
- Use `--average` to see if your internet is improving/degrading

## Limitations

- Requires active internet connection
- Speedtest.net must be accessible
- Results depend on network conditions at test time

## License

MIT License - see LICENSE file

## Contributing

Found a bug? Have a feature idea? Open an issue or submit a PR!

---

Made by 0xsan7
