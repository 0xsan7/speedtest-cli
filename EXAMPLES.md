# Advanced Usage Examples

## Basic Speed Test

```bash
python speedtest_cli.py
```

Returns full speed test results and saves to history.

## View Test History

```bash
python speedtest_cli.py --history
```

Shows your last 10 speed tests in table format.

## View Average Speeds

```bash
python speedtest_cli.py --average
```

Shows average download/upload from all tests.

## Faster Testing

```bash
python speedtest_cli.py --simple
```

Runs a faster test with less accuracy.

## Use Cases

### Monitor Internet Quality
Run tests regularly to track if your ISP provides consistent speeds:

```bash
python speedtest_cli.py
python speedtest_cli.py --average  # Check trends
```

### Troubleshoot Connection Issues
Compare speeds at different times of day:

```bash
python speedtest_cli.py --history
```

### Track ISP Performance
Run tests daily and monitor average speeds over weeks.

## Tips

- First test takes longer as it finds the best server
- Run multiple tests for more accurate trends
- History is saved in `speedtest_history.json`
- All results are stored locally (no data uploaded)

---

For more info, see README.md
