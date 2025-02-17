from scapy.all import sniff

def generate_statistics(packets):
    """
    Generate basic traffic statistics.
    :param packets: List of captured packets
    """
    packet_count = len(packets)
    print("Total Packets captured: {packet_count}")