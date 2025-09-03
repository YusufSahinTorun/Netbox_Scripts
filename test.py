import random

from netbox.scripts import Script, ObjectVar, StringVar
from ipam.models import IPAddress

class RandomIPCreator(Script):
    class Meta:
        name = "Rastgele IP Oluşturucu"
        description = "Rastgele bir IP adresi oluşturur ve Netbox'a kaydeder."

    # Script parametreleri
    ip_version = ObjectVar(
        model='ipam.ipaddress',
        label="IP Versiyonu",
        query_params={
            'family': '4' # Sadece IPv4 için
        }
    )

    description = StringVar(
        description="Oluşturulacak IP adresi için açıklama"
    )

    def run(self, data, commit):
        # Rastgele IP adresi oluştur
        ip_octets = [str(random.randint(1, 254)) for _ in range(4)]
        random_ip = ".".join(ip_octets) + "/24"

        # IPAddress modelini oluştur
        try:
            ip_address = IPAddress(
                address=random_ip,
                description=data['description']
            )
            ip_address.save()

            self.log_success(f"Başarılı: Yeni IP adresi oluşturuldu: {ip_address}")

        except Exception as e:
            self.log_failure(f"Hata: IP adresi oluşturulamadı - {e}")

        if not commit:
            self.log_info("Dry run: Veritabanına değişiklik kaydedilmedi.")