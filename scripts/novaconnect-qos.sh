#!/bin/bash
set -e

DEV=enp0s8

# Remove existing queue and filters
tc qdisc del dev "$DEV" root 2>/dev/null || true

# Create root priority queue
tc qdisc add dev "$DEV" root handle 1: prio bands 3 priomap 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2

# Create individual queues
tc qdisc add dev "$DEV" parent 1:1 handle 10: pfifo limit 100
tc qdisc add dev "$DEV" parent 1:2 handle 20: pfifo limit 100
tc qdisc add dev "$DEV" parent 1:3 handle 30: pfifo limit 100

# RTP - Highest priority
tc filter add dev "$DEV" parent 1: protocol ip prio 1 u32 match ip tos 0xb8 0xfc flowid 1:1

# SIP - Medium priority
tc filter add dev "$DEV" parent 1: protocol ip prio 2 u32 match ip tos 0x60 0xfc flowid 1:2
