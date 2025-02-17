from scapy.all import sniff

def capture_packets(count=10):
    """
    Capture a specified number of packets:
    param count: Number of packets to capture:
    return: List of captured packets
    """
    packets = sniff(count=count)
    return packets