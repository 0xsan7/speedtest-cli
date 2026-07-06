#!/usr/bin/env python3
"""
Speed Test CLI - Test your internet speed from the command line.
"""

import speedtest
import argparse
import json
from datetime import datetime
from pathlib import Path


class SpeedTestRunner:
    """Run internet speed tests and track results."""
    
    HISTORY_FILE = 'speedtest_history.json'
    
    def __init__(self, simple=False):
        """
        Initialize Speed Test Runner.
        
        Args:
            simple: If True, run faster tests with fewer threads
        """
        self.simple = simple
        self.history_file = Path(self.HISTORY_FILE)
    
    def run_test(self):
        """
        Run the speed test.
        
        Returns:
            Dictionary with test results
        """
        print("Starting speed test...")
        print("(This may take 30-60 seconds)\n")
        
        try:
            st = speedtest.Speedtest()
            
            print("Finding best server...")
            st.get_best_server()
            
            print("Testing download speed...")
            download = st.download() / 1_000_000  # Convert to Mbps
            
            print("Testing upload speed...")
            upload = st.upload() / 1_000_000  # Convert to Mbps
            
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
        print("\n" + "="*50)
        print("SPEED TEST RESULTS".center(50))
        print("="*50 + "\n")
        
        print(f"Download Speed: {results['download_mbps']} Mbps")
        print(f"Upload Speed:   {results['upload_mbps']} Mbps")
        print(f"Ping:           {results['ping_ms']} ms")
        print(f"Server:         {results['server']}")
        print(f"Location:       {results['location']}")
        print(f"Timestamp:      {results['timestamp']}")
        
        print("\n" + "="*50 + "\n")
    
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
        
        print(f"Results saved to {self.HISTORY_FILE}")
    
    def show_history(self):
        """Display test history."""
        if not self.history_file.exists():
            print("No history found. Run a test first.")
            return
        
        with open(self.history_file, 'r') as f:
            history = json.load(f)
        
        print("\n" + "="*70)
        print("SPEED TEST HISTORY".center(70))
        print("="*70 + "\n")
        
        print(f"{'Date':<25} {'Download (Mbps)':<20} {'Upload (Mbps)':<20}")
        print("-"*70)
        
        for result in history[-10:]:  # Show last 10 tests
            date = result['timestamp'].split('T')[0]
            download = result['download_mbps']
            upload = result['upload_mbps']
            print(f"{date:<25} {download:<20} {upload:<20}")
        
        print("\n" + "="*70 + "\n")
    
    def show_average(self):
        """Show average speeds from history."""
        if not self.history_file.exists():
            print("No history found. Run a test first.")
            return
        
        with open(self.history_file, 'r') as f:
            history = json.load(f)
        
        if not history:
            print("No test data available.")
            return
        
        avg_download = sum(r['download_mbps'] for r in history) / len(history)
        avg_upload = sum(r['upload_mbps'] for r in history) / len(history)
        
        print("\n" + "="*50)
        print("AVERAGE SPEEDS".center(50))
        print("="*50 + "\n")
        
        print(f"Tests Run:      {len(history)}")
        print(f"Avg Download:   {round(avg_download, 2)} Mbps")
        print(f"Avg Upload:     {round(avg_upload, 2)} Mbps")
        
        print("\n" + "="*50 + "\n")


def main():
    """Command-line interface for Speed Test CLI."""
    
    parser = argparse.ArgumentParser(
        description='Test your internet speed from the command line.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python speedtest_cli.py
  python speedtest_cli.py --history
  python speedtest_cli.py --average
        """
    )
    
    parser.add_argument('--history', action='store_true',
                       help='Show test history')
    parser.add_argument('--average', action='store_true',
                       help='Show average speeds from all tests')
    parser.add_argument('--simple', action='store_true',
                       help='Run faster test (less accurate)')
    
    args = parser.parse_args()
    
    runner = SpeedTestRunner(simple=args.simple)
    
    if args.history:
        runner.show_history()
    elif args.average:
        runner.show_average()
    else:
        try:
            results = runner.run_test()
            runner.display_results(results)
            runner.save_to_history(results)
        except RuntimeError as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
