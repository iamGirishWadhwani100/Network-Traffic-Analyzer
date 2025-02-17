from packet_capture import capture_packets
from protocol_analyzer import analyze_protocol
from traffic_statistics import generate_statistics
from visualization import plot_traffic

def main():
    #Step 1: Capture bpackets
    packets = capture_packets(count = 20)

    #Step 2: Analyze Protocols
    analyze_protocol(packets)

    #Step 3: Generate Statistics
    generate_statistics(packets)

    #Step 4: Visualize Data
    time_intervals = [1, 2, 3, 4, 5]     #Example Data
    packet_counts = [10, 20, 15, 30, 25]   #Example Data
    plot_traffic(packet_counts, time_intervals)
if __name__ == "__main__":
   main()