# meshtastic-direct-nodes
This python script will connect to your Meshtastic node, and return a list of nodes that your node is directly connected to (that is, Zero hops away).

![Screenshot 2024-12-03 103843](https://github.com/user-attachments/assets/8dfe8a00-020b-452f-a33b-232d1e09d170)

# Installation
<blockquote>cd ~</blockquote>
<blockquote>git clone https://github.com/brad28b/meshtastic-direct-nodes.git</blockquote>
<blockquote>cd meshtastic-direct-nodes</blockquote>
<blockquote>pip3 install -r requirements.txt</blockquote>

# Usage
<blockquote>python meshtastic-direct-nodes.py</blockquote>

Note: If you use Serial, the script will attempt to find your serial port automatically. You can also change the code to directly specify your serial port, by changing this line:

<blockquote>interface = meshtastic.serial_interface.SerialInterface(devPath='/dev/ttyUSB0')  # Replace with your port</blockquote>
