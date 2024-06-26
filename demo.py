import os
import psutil
import platform
import cpuinfo

# Basic CPU Information
num_cores = os.cpu_count()
cpu_freq = psutil.cpu_freq()
cpu_percent = psutil.cpu_percent(interval=1)

print(f"Number of logical CPU cores: {num_cores}")
print(f"Current CPU frequency: {cpu_freq.current:.2f} MHz")
print(f"Min CPU frequency: {cpu_freq.min:.2f} MHz")
print(f"Max CPU frequency: {cpu_freq.max:.2f} MHz")
print(f"CPU usage: {cpu_percent}%")

# Detailed CPU Information using cpuinfo
cpu_info = cpuinfo.get_cpu_info()

print("\nDetailed CPU Information:")
print(f"CPU Brand: {cpu_info['brand_raw']}")
print(f"CPU Arch: {cpu_info['arch']}")
print(f"Bits: {cpu_info['bits']}")
print(f"Count: {cpu_info['count']}")
print(f"Vendor ID: {cpu_info['vendor_id_raw']}")
print(f"Stepping: {cpu_info.get('stepping', 'N/A')}")
print(f"Model: {cpu_info.get('model', 'N/A')}")
print(f"Family: {cpu_info.get('family', 'N/A')}")
print(f"L2 Cache Size: {cpu_info.get('l2_cache_size', 'N/A')}")
print(f"L3 Cache Size: {cpu_info.get('l3_cache_size', 'N/A')}")

# System Information using platform
system_info = platform.uname()

print("\nSystem Information:")
print(f"System: {system_info.system}")
print(f"Node Name: {system_info.node}")
print(f"Release: {system_info.release}")
print(f"Version: {system_info.version}")
print(f"Machine: {system_info.machine}")
print(f"Processor: {system_info.processor}")

# Additional CPU stats from psutil
print("\nAdditional CPU Stats:")
print(f"CPU times: {psutil.cpu_times()}")
print(f"CPU stats: {psutil.cpu_stats()}")
print(f"CPU load (1, 5, 15 min): {psutil.getloadavg()}")

# ======================= REPLIT ======================
# Number of logical CPU cores: 8
# Current CPU frequency: 3050.00 MHz
# Min CPU frequency: 0.00 MHz
# Max CPU frequency: 0.00 MHz
# CPU usage: 58.1%

# Detailed CPU Information:
# CPU Brand: AMD EPYC 7B13
# CPU Arch: X86_64
# Bits: 64
# Count: 8
# Vendor ID: AuthenticAMD
# Stepping: N/A
# Model: 1
# Family: 25
# L2 Cache Size: 2097152
# L3 Cache Size: 524288

# System Information:
# System: Linux
# Node Name: da2a6cb23419
# Release: 6.5.0-1022-gcp
# Version: #24~22.04.1-Ubuntu SMP Tue May 28 16:34:13 UTC 2024
# Machine: x86_64
# Processor:

# Additional CPU Stats:
# CPU times: scputimes(user=17571.78, nice=74.68, system=193591.18, idle=105237.11, iowait=9677.21, irq=0.0, softirq=559.67, steal=0.0, guest=0.0, guest_nice=0.0)
# CPU stats: scpustats(ctx_switches=1731836370, interrupts=1013844271, soft_interrupts=148625833, syscalls=0)
# CPU load (1, 5, 15 min): (6.3720703125, 6.6689453125, 7.2392578125)
