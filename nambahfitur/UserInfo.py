class UserInfo:
    def __init__(self, norek, pin, saldo, email, password):
        self.norek = norek
        self.pin = pin
        self.saldo = saldo
        self.email = email
        self.password = password
        self.transaksi = []

    def check_pin(self, pin):
        return self.pin == pin

    def check_password(self, password):
        return self.password == password

    def get_rekening(self):
        return self.norek

    def add_transaksi(self, jenis, nominal):
        from datetime import datetime
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transaksi.append({'tanggal': now, 'jenis': jenis, 'nominal': nominal})
        
        if len(self.transaksi) > 100:
            self.transaksi.pop(0)
    
    def deposit(self, nominal):
        self.saldo += nominal
        self.add_transaksi('setor tunai', nominal)