packet_of_pens = int(input())
packet_of_markers = int(input())
litres_detergent = int(input())
percentage_discount = int(input()) / 100
price_of_pen_packets = packet_of_pens * 5.80
price_of_marker_packets = packet_of_markers * 7.20
price_of_detergent = litres_detergent * 1.20
mid_sum = price_of_pen_packets + price_of_marker_packets + price_of_detergent
total_sum = mid_sum - (mid_sum * percentage_discount)
print(total_sum)
