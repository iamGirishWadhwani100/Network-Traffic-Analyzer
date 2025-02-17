import matplotlib.pyplot as plt

def plot_traffic(packet_counts, time_intervals):
    """
    Plot traffic over time.
    :param packet_counts: List of packets counts
    :param time_intervals: List of time intervals
    """
    
    plt.plot(time_intervals, packet_counts)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Packet Count")
    plt.title("Network Traffic Over Time")
    plt.show()