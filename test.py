from extras.scripts import *
from ipam.models import IPAddress
import random

class RandomIPScript(Script):

    class Meta:
        name = "Random IP Creator"
        description = "Adds a random IP address from 192.168.0.0/24"

    def run(self, data, commit):

        # Random IP seç (192.168.0.1 - 192.168.0.254 arası)
        last_octet = random.randint(1, 254)
        ip_str = f"192.168.0.{last_octet}/24"

        # IP nesnesini oluştur
        ip = IPAddress(address=ip_str)
        ip.save()

        self.log_success(f"Created random IP: {ip}")

        return f"Random IP added: {ip}"
