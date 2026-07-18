#!/usr/bin/env python3
"""
Speed Test CLI - Test your internet speed from the command line.
"""

import speedtest
import argparse
import json
import csv
from datetime import datetime
from pathlib import Path


class Colors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


class SpeedTestRunner:
    """Run internet speed tests and track results."""
    
    HISTORY_FILE = 'speedtest_history.json'
    
    def __init__(self, simple=False, color=True):
        """
        Initialize Speed Test Runner.
        
        Args:
            simple: If True, run faster tests with fewer threads
            color: If True, use colored output
        """
        self.simple = simple
        self.color = color
        self.history_file = Path(self.HISTORY_FILE)
    
    def _colorize(self, text, color_code):
        """Apply color to text if color is enabled."""
        if self.color:
            return f"{color_code}{text}{Colors.RESET}"
        return text
    
    def run_test(self):
        """
        Run the speed test.
        
        Returns:
            Dictionary with test results
        """
        print(self._colorize("Starting speed test...", Colors.CYAN))
        print(self._colorize("(This may take 30-60 seconds)\n", Colors.YELLOW))
        
        try:
            st = speedtest.Speedtest()
            
            print(self._colorize("Finding best server...", Colors.BLUE))
            st.get_best_server()
            
            print(self._colorize("Testing download speed...", Colors.BLUE))
            download = st.download() / 1_000_000
            
            print(self._colorize("Testing upload speed...", Colors.BLUE))
            upload = st.upload() / 1_000_000
            
            ping = st.results.ping
            
            return {
                'timestamp': datetime.now().isoformat(),
                'download_mbps': round(download, 2),
                'upload_mbps': round(upload, 2),
                'ping_ms': round(ping, 2),
                'server': st.results.server['sponsor'],
                'location': f"{st.results.server['name']}, {st.results.server['country']}"
            }
        
        except Exception as e:
            raise RuntimeError(f"Speed test failed: {e}")
    
    def display_results(self, results):
        """
        Display results in a nice format.
        
        Args:
            results: Dictionary with test results
        """
        print("\n" + self._colorize("="*50, Colors.HEADER))
        print(self._colorize("SPEED TEST RESULTS".center(50), Colors.BOLD))
        print(self._colorize("="*50, Colors.HEADER) + "\n")
        
        download = self._colorize(f"{results['download_mbps']} Mbps", Colors.GREEN)
        upload = self._colorize(f"{results['upload_mbps']} Mbps", Colors.GREEN)
        ping = self._colorize(f"{results['ping_ms']} ms", Colors.YELLOW)
        
        print(f"Download Speed: {download}")
        print(f"Upload Speed:   {upload}")
        print(f"Ping:           {ping}")
        print(f"Server:         {results['server']}")
        print(f"Location:       {results['location']}")
        print(f"Timestamp:      {results['timestamp']}")
        
        print("\n" + self._colorize("="*50, Colors.HEADER) + "\n")
    
    def save_to_history(self, results):
        """
        Save results to history file.
        
        Args:
            results: Dictionary with test results
        """
        history = []
        
        if self.history_file.exists():
            with open(self.history_file, 'r') as f:
                history = json.load(f)
        
        history.append(results)
        
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)
        
        print(self._colorize(f"Results saved to {self.HISTORY_FILE}", Colors.GREEN))
    
    def show_history(self):
        """Display test history."""
        if not self.history_file.exists():
            print(self._colorize("No history found. Run a test first.", Colors.RED))
            return
        
        with open(self.history_file, 'r') as f:
            history = json.load(f)
        
        print("\n" + self._colorize("="*70, Colors.HEADER))
        print(self._colorize("SPEED TEST HISTORY".center(70), Colors.BOLD))
        print(self._colorize("="*70, Colors.HEADER) + "\n")
        
        print(f"{'Date':<25} {'Download (Mbps)':<20} {'Upload (Mbps)':<20}")
        print(self._colorize("-"*70, Colors.CYAN))
        
        for result in history[-10:]:
            date = result['timestamp'].split('T')[0]
            download = result['download_mbps']
            upload = result['upload_mbps']
            print(f"{date:<25} {download:<20} {upload:<20}")
        
        print("\n" + self._colorize("="*70, Colors.HEADER) + "\n")
    
    def show_average(self):
        """Show average speeds from history."""
        if not self.history_file.exists():
            print(self._colorize("No history found. Run a test first.", Colors.RED))
            return
        
        with open(self.history_file, 'r') as f:
            history = json.load(f)
        
        if not history:
            print(self._colorize("No test data available.", Colors.RED))
            return
        
        avg_download = sum(r['download_mbps'] for r in history) / len(history)
        avg_upload = sum(r['upload_mbps'] for r in history) / len(history)
        
        print("\n" + self._colorize("="*50, Colors.HEADER))
        print(self._colorize("AVERAGE SPEEDS".center(50), Colors.BOLD))
        print(self._colorize("="*50, Colors.HEADER) + "\n")
        
        print(f"Tests Run:      {len(history)}")
        print(self._colorize(f"Avg Download:   {round(avg_download, 2)} Mbps", Colors.GREEN))
        print(self._colorize(f"Avg Upload:     {round(avg_upload, 2)} Mbps", Colors.GREEN))
        
        print("\n" + self._colorize("="*50, Colors.HEADER) + "\n")
    
    def export_to_csv(self, output_file='speedtest_results.csv'):
        """
        Export history to CSV file.
        
        Args:
            output_file: Name of CSV file to create
        """
        if not self.history_file.exists():
            print(self._colorize("No history found. Run a test first.", Colors.RED))
            return
        
        with open(self.history_file, 'r') as f:
            history = json.load(f)
        
        if not history:
            print(self._colorize("No test data available.", Colors.RED))
            return
        
        try:
            with open(output_file, 'w', newline='') as csvfile:
                fieldnames = ['timestamp', 'download_mbps', 'upload_mbps', 'ping_ms', 'server', 'location']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(history)
            
            print(self._colorize(f"Results exported to {output_file}", Colors.GREEN))
        except Exception as e:
            print(self._colorize(f"Error exporting to CSV: {e}", Colors.RED))


def main():
    """Command-line interface for Speed Test CLI."""
    
    parser = argparse.ArgumentParser(
        description='Test your internet speed from the command line.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python speedtest_cli.py                 # Run a speed test
  python speedtest_cli.py --history       # Show test history
  python speedtest_cli.py --average       # Show average speeds
  python speedtest_cli.py --export        # Export to CSV
  python speedtest_cli.py --simple        # Faster test
  python speedtest_cli.py --no-color      # Disable colored output
        """
    )
    
    parser.add_argument('--history', action='store_true',
                       help='Show test history')
    parser.add_argument('--average', action='store_true',
                       help='Show average speeds from all tests')
    parser.add_argument('--simple', action='store_true',
                       help='Run faster test (less accurate)')
    parser.add_argument('--export', action='store_true',
                       help='Export test history to CSV')
    parser.add_argument('--no-color', action='store_true',
                       help='Disable colored output')
    
    args = parser.parse_args()
    
    runner = SpeedTestRunner(simple=args.simple, color=not args.no_color)
    
    if args.history:
        runner.show_history()
    elif args.average:
        runner.show_average()
    elif args.export:
        runner.export_to_csv()
    else:
        try:
            results = runner.run_test()
            runner.display_results(results)
            runner.save_to_history(results)
        except RuntimeError as e:
            print(runner._colorize(f"Error: {e}", Colors.RED))


if __name__ == '__main__':
    main()
