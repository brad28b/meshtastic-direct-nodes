# meshtastic-direct-nodes
This python script will connect to your Meshtastic node, and return a list of nodes that your node is directly connected to (that is, Zero hops away).

![Screenshot 2024-12-03 102154](https://github.com/user-attachments/assets/9f1b6c3e-dfd7-4689-ba17-f9e3cbc36b62)


# Installation
<blockquote>cd ~</blockquote>
<blockquote>git clone https://github.com/brad28b/meshtastic-direct-nodes.git</blockquote>
<blockquote>cd meshtastic-direct-nodes</blockquote>
<blockquote>pip3 install -r requirements.txt</blockquote>

# Usage
<blockquote>python direct_mesh_nodes.py</blockquote>

Note: If you use Serial, the script will attempt to find your serial port automatically. You can also change the code to directly specify your serial port, by changing this line:

<blockquote>interface = meshtastic.serial_interface.SerialInterface(devPath='/dev/ttyUSB0')  # Replace with your port</blockquote>
