#!/usr/bin/env python3
"""
Speed Test CLI - Test your internet speed from the command line.
"""

import speedtest
import argparse
import json
import csv
import logging
from datetime import datetime
from pathlib import Path


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('speedtest.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


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
        logger.info("Speed Test Runner initialized")
    
    def run_test(self):
        """
        Run the speed test.
        
        Returns:
            Dictionary with test results
        """
        logger.info("Starting speed test...")
        print("Starting speed test...")
        print("(This may take 30-60 seconds)\n")
        
        try:
            st = speedtest.Speedtest()
            
            logger.info("Finding best server...")
            print("Finding best server...")
            st.get_best_server()
            
            logger.info("Testing download speed...")
            print("Testing download speed...")
            download = st.download() / 1_000_000
            
            logger.info("Testing upload speed...")
            print("Testing upload speed...")
            upload = st.upload() / 1_000_000
            
            ping = st.results.ping
            
            result = {
                'timestamp': datetime.now().isoformat(),
                'download_mbps': round(download, 2),
                'upload_mbps': round(upload, 2),
                'ping_ms': round(ping, 2),
                'server': st.results.server['sponsor'],
                'location': f"{st.results.server['name']}, {st.results.server['country']}"
            }
            
            logger.info(f"Test completed - Download: {result['download_mbps']} Mbps, Upload: {result['upload_mbps']} Mbps")
            return result
        
        except Exception as e:
            logger.error(f"Speed test failed: {e}")
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
        
        logger.info(f"Results saved to {self.HISTORY_FILE}")
        print(f"Results saved to {self.HISTORY_FILE}")
    
    def show_history(self):
        """Display test history."""
        if not self.history_file.exists():
            logger.warning("No history found")
            print("No history found. Run a test first.")
            return
        
        with open(self.history_file, 'r') as f:
            history = json.load(f)
        
        logger.info(f"Displaying history with {len(history)} records")
        
        print("\n" + "="*70)
        print("SPEED TEST HISTORY".center(70))
        print("="*70 + "\n")
        
        print(f"{'Date':<25} {'Download (Mbps)':<20} {'Upload (Mbps)':<20}")
        print("-"*70)
        
        for result in history[-10:]:
            date = result['timestamp'].split('T')[0]
            download = result['download_mbps']
            upload = result['upload_mbps']
            print(f"{date:<25} {download:<20} {upload:<20}")
        
        print("\n" + "="*70 + "\n")
    
    def show_average(self):
        """Show average speeds from history."""
        if not self.history_file.exists():
            logger.warning("No history found")
            print("No history found. Run a test first.")
            return
        
        with open(self.history_file, 'r') as f:
            history = json.load(f)
        
        if not history:
            logger.warning("No test data available")
            print("No test data available.")
            return
        
        avg_download = sum(r['download_mbps'] for r in history) / len(history)
        avg_upload = sum(r['upload_mbps'] for r in history) / len(history)
        
        logger.info(f"Average speeds - Download: {round(avg_download, 2)} Mbps, Upload: {round(avg_upload, 2)} Mbps")
        
        print("\n" + "="*50)
        print("AVERAGE SPEEDS".center(50))
        print("="*50 + "\n")
        
        print(f"Tests Run:      {len(history)}")
        print(f"Avg Download:   {round(avg_download, 2)} Mbps")
        print(f"Avg Upload:     {round(avg_upload, 2)} Mbps")
        
        print("\n" + "="*50 + "\n")
    
    def export_to_csv(self, output_file='speedtest_results.csv'):
        """
        Export history to CSV file.
        
        Args:
            output_file: Name of CSV file to create
        """
        if not self.history_file.exists():
            logger.warning("No history found for export")
            print("No history found. Run a test first.")
            return
        
        with open(self.history_file, 'r') as f:
            history = json.load(f)
        
        if not history:
            logger.warning("No test data available for export")
            print("No test data available.")
            return
        
        try:
            with open(output_file, 'w', newline='') as csvfile:
                fieldnames = ['timestamp', 'download_mbps', 'upload_mbps', 'ping_ms', 'server', 'location']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(history)
            
            logger.info(f"Results exported to {output_file}")
            print(f"Results exported to {output_file}")
        except Exception as e:
            logger.error(f"Error exporting to CSV: {e}")
            print(f"Error exporting to CSV: {e}")


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
    
    args = parser.parse_args()
    
    runner = SpeedTestRunner(simple=args.simple)
    
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
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
