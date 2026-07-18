# Troubleshooting Guide

## Speed Test Issues

### "Repository not found" error
- Check your internet connection
- Ensure speedtest.net is accessible
- Try using a VPN if blocked

### Test takes too long
- Use `--simple` flag for faster testing
- Close other applications
- Ensure stable connection

### Inconsistent results
- Run multiple tests for average
- Test at different times
- Use `--history` to see patterns

## Installation Issues

### pip: command not found
```bash
# Use pip3 instead
pip3 install -r requirements.txt
```

### Module not found error
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Python version error
```bash
# Check your Python version
python --version

# Requires Python 3.9+
# Update Python if needed
```

## Improving Your Speed

### If speeds are slow:
1. Restart your router
2. Close bandwidth-heavy applications
3. Move closer to WiFi router
4. Use wired Ethernet connection
5. Check for background updates

### Network optimization:
- Reduce number of connected devices
- Update router firmware
- Clear browser cache
- Disable VPN temporarily for testing

## Getting Help

For issues not listed here:
1. Check GitHub issues: https://github.com/0xsan7/speedtest-cli/issues
2. Create new issue with:
   - Python version
   - Operating system
   - Error message
   - Steps to reproduce

---

**Last Updated:** 2026-07-06
