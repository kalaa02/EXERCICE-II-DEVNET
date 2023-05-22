bgp_output = '''BGP router identifier 10.220.88.20, local AS number 42
BGP table version is 59, main routing table version 59
Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.220.88.38    4           44    7536    8296       59    0    0 5d05h           0'''

# Split the output into lines
bgp_lines = bgp_output.splitlines()

# Get the first and last lines
first_line = bgp_lines[0]
last_line = bgp_lines[-1]

# Extract the local AS number from the first line using string.split()
local_as = first_line.split()[-1]

# Extract the IP address of the BGP peer from the last line using string.split()
bgp_peer_ip = last_line.split()[0]

# Print the local AS number and the IP address of the BGP peer
print("Local AS number:", local_as)
print("BGP peer IP address:", bgp_peer_ip)
