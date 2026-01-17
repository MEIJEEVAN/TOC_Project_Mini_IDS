from urllib.parse import unquote

from scapy.all import Raw, sniff

import app
from alerts import detect_attack


def packet_handler(packet):
    if packet.haslayer(Raw):
        raw_payload = packet[Raw].load.decode(errors="ignore")

        # Decode URL-encoded payloads
        payload = unquote(raw_payload)

        # Optional but STRONGLY recommended: only inspect HTTP requests
        if not payload.startswith(("GET", "POST", "PUT", "DELETE")):
            return

        print("[DEBUG] Payload:", payload)

        attack = detect_attack(payload)
        if attack:
            print("[ALERT] Detected:", attack)
            app.send_alert(attack, payload)


def start_sniffing():
    sniff(iface="lo", filter="tcp", prn=packet_handler, store=False)


if __name__ == "__main__":
    start_sniffing()
