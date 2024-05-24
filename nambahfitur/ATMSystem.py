class ATMSystem:
    def __init__(self, user_info):
        self.user_info = user_info

    def tarik_tunai(self, tarik, norek):
        if tarik % 50000 != 0:
            return 'Penarikan harus dalam kelipatan 50.000'
        elif tarik >= self.user_info[norek].saldo:
            return 'SALDO ANDA TIDAK CUKUP'
        else:
            self.user_info[norek].saldo -= tarik
            self.user_info[norek].add_transaksi('tarik tunai', tarik)
            return f'BERHASIL TARIK: {tarik}\nSISA SALDO ANDA: {self.user_info[norek].saldo}'

    def transfer_dana(self, rek_tujuan, jumlah, norek):
        if jumlah >= self.user_info[norek].saldo:
            return 'SALDO ANDA TIDAK CUKUP'
        else:
            self.user_info[norek].saldo -= jumlah
            self.user_info[rek_tujuan].saldo += jumlah
            self.user_info[norek].add_transaksi('transfer keluar', jumlah)
            self.user_info[rek_tujuan].add_transaksi('transfer masuk', jumlah)
            return f'TRANSFER KE REKENING {rek_tujuan} SEBESAR: {jumlah}\nTRANSFER SUKSES\nSISA SALDO ANDA: {self.user_info[norek].saldo}'

    def cek_saldo(self, norek):
        return f'SALDO ANDA ADALAH: {self.user_info[norek].saldo}'

    def mutasi_transaksi(self, norek, hari=None):
        from datetime import datetime, timedelta
        now = datetime.now()
        transaksi = self.user_info[norek].transaksi

        if hari:
            batas_waktu = now - timedelta(days=hari)
            transaksi = [t for t in transaksi if datetime.strptime(t['tanggal'], '%Y-%m-%d %H:%M:%S') > batas_waktu]
        
        return transaksi[-5:]  # Mengembalikan 5 transaksi terakhir
    
    def setor_tunai(self, norek, nominal):
        self.user_info[norek].deposit(nominal)
        return f'SETOR TUNAI BERHASIL: {nominal}\nSALDO ANDA: {self.user_info[norek].saldo}'