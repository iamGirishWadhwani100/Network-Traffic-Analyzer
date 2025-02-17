from scapy.all import TCP , UDP , IP
def analyze_protocol(packets):
    """
    Analyze protocolsin the captured packets.
    :param packets: List of captured packets
    """
    for packet in packets:
        if packet.haslayer(TCP):
            print("TCP Packet: ")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print("UDP Packet: ")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")