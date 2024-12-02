import meshtastic
import meshtastic.serial_interface
import meshtastic.tcp_interface
from datetime import datetime
import time
import sys

def format_timestamp(timestamp):
    """Convert Unix timestamp to human readable format"""
    try:
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return 'Unknown'

def get_interface():
    """Get the interface based on user selection"""
    while True:
        print("\nSelect connection type:")
        print("1. Serial (USB)")
        print("2. TCP (Network)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            try:
                return meshtastic.serial_interface.SerialInterface()
            except Exception as e:
                print(f"Error connecting to serial device: {e}")
                continue
        elif choice == "2":
            ip = input("Enter IP address (e.g., 192.168.1.100): ").strip()
            try:
                return meshtastic.tcp_interface.TCPInterface(ip)
            except Exception as e:
                print(f"Error connecting to {ip}: {e}")
                continue
        elif choice == "3":
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

def main():
    # Get interface from user
    interface = get_interface()
    print("\nConnected to device. Gathering node data...")
    
    # Wait a moment for node data to populate
    time.sleep(2)
    
    # Get all nodes using the correct method
    nodes = interface.nodes
    
    # Filter for direct nodes (hopsAway = 0)
    direct_nodes = {
        node_id: node for node_id, node in nodes.items()
        if node.get('hopsAway', float('inf')) == 0
    }
    
    if not direct_nodes:
        print("No directly connected nodes found")
        return
    
    # Print header
    print(f"\nFound {len(direct_nodes)} directly connected nodes:")
    print("-" * 80)
    
    # Print nodes in a similar format to CLI --nodes
    for node_id, node in direct_nodes.items():
        user = node.get('user', {})
        position = node.get('position', {})
        
        print(f"Node {node_id}:")
        # Basic info
        longname = user.get('longName', 'Unknown')
        shortname = user.get('shortName', '')
        if shortname:
            print(f"  Username: {longname} ({shortname})")
        else:
            print(f"  Username: {longname}")
        print(f"  Hardware: {user.get('hwModel', 'Unknown')}")
        
        # Position info if available
        if position and 'latitude' in position and 'longitude' in position:
            print(f"  Position: {position.get('latitude')}°, {position.get('longitude')}°")
            if 'altitude' in position:
                print(f"  Altitude: {position.get('altitude')} m")
        
        # Signal and metrics
        metrics = node.get('deviceMetrics', {})
        if 'snr' in node:
            print(f"  SNR: {node.get('snr')} dB")
        if metrics.get('channelUtilization'):
            print(f"  Channel utilization: {metrics.get('channelUtilization')}%")
        if metrics.get('airUtilTx'):
            print(f"  Air utilization: {metrics.get('airUtilTx')}%")
        
        # Battery and last heard
        if metrics.get('batteryLevel'):
            print(f"  Battery: {metrics.get('batteryLevel')}%")
        last_heard = node.get('lastHeard')
        if last_heard:
            print(f"  Last heard: {format_timestamp(last_heard)}")
        
        print()  # Empty line between nodes
    
    # Clean up
    interface.close()

if __name__ == "__main__":
    try:
        while True:
            try:
                main()
                
                # Ask if user wants to try another connection
                again = input("\nWould you like to try another connection? (y/n): ").strip().lower()
                if again != 'y':
                    break
                    
            except Exception as e:
                print(f"\nError: {e}")
                retry = input("\nWould you like to try again? (y/n): ").strip().lower()
                if retry != 'y':
                    break
    except KeyboardInterrupt:
        print("\nExiting...")
