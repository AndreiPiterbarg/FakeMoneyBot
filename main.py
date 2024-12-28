import threading
import time
import sys
import os


from historical.data_collector import start_collecting_data
from strategies.momentum import run_momentum_strategy

def main():
    collector_thread = threading.Thread(target=start_collecting_data, daemon=False)
    collector_thread.start()

    # Keep the main thread alive until collector_thread finishes (infinite loop).
    # If you need a graceful shutdown, you can implement a stop signal instead.
    collector_thread.join()

if __name__ == "__main__":
    main()

