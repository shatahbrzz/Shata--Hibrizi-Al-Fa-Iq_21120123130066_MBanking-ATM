import tkinter as tk
import UserInfo as UserInfo
import ATMSystem as ATMSystem
from tkinter import messagebox
import random
import re

def main():
    users_info = {
        1234567890: {'pin': 123456, 'saldo': 1500000, 'email': 'user1@email.com', 'password': 'Password123'},
        9876543210: {'pin': 567890, 'saldo': 2000000, 'email': 'user2@email.com', 'password': 'Password456'},
        1111111111: {'pin': 111111, 'saldo': 800000, 'email': 'user3@email.com', 'password': 'Password111'},
        2222222222: {'pin': 222222, 'saldo': 3000000, 'email': 'user4@email.com', 'password': 'Password222'}
    }

    users = {norek: UserInfo.UserInfo(norek, info['pin'], info['saldo'], info['email'], info['password']) for norek, info in users_info.items()}

    atm_system = ATMSystem.ATMSystem(users)

    def show_menu_awal():
        clear_frame()
        show_menu_awal_frame = tk.Frame(root, bg="#000000")

        label_judul = tk.Label(show_menu_awal_frame, text="BSH MOBILE", font=("Arial", 20), bg="#000000", fg="white")
        label_judul.pack()

        label_judul2 = tk.Label(show_menu_awal_frame, text="(BANK SHATA HIBRIZI MOBILE)", font=("Arial", 15), bg="#000000", fg="white")
        label_judul2.pack()

        button_login = tk.Button(show_menu_awal_frame, text="Log In", command=show_opsi_login, font=("Arial", 12), bg="#ff00ff")
        button_login.pack(pady=10)

        button_sign_in = tk.Button(show_menu_awal_frame, text="Sign Up", command=show_sign_in_menu, font=("Arial", 12), bg="#ff00ff")
        button_sign_in.pack(pady=10)

        show_menu_awal_frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_opsi_login():
        clear_frame()
        login_options_frame = tk.Frame(root, bg="#000000")

        button_login_norek = tk.Button(login_options_frame, text="Login dengan Rekening", command=show_login_menu, font=("Arial", 12), bg="#ff00ff")
        button_login_norek.pack(pady=10)

        button_login_email = tk.Button(login_options_frame, text="Login dengan Email", command=show_email_login_menu, font=("Arial", 12), bg="#ff00ff")
        button_login_email.pack(pady=10)

        button_back = tk.Button(login_options_frame, text="Kembali", command=lambda: show_menu_awal(), font=("Arial", 12), bg="#ff00ff")
        button_back.pack(pady=10)

        login_options_frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_login_menu():
        clear_frame()
        login_frame = tk.Frame(root, bg="#000000")

        label_norek = tk.Label(login_frame, text="Nomor Rekening:", font=("Arial", 12), bg="#000000", fg="white")
        label_norek.pack()
        entry_norek = tk.Entry(login_frame, font=("Arial", 12))
        entry_norek.pack()

        label_pin = tk.Label(login_frame, text="PIN:", font=("Arial", 12), bg="#000000", fg="white")
        label_pin.pack()
        entry_pin = tk.Entry(login_frame, show="*", font=("Arial", 12))
        entry_pin.pack()

        button_login = tk.Button(login_frame, text="Login", command=lambda: login_norek(entry_norek.get(), entry_pin.get()), font=("Arial", 12), bg="#ff00ff")
        button_login.pack(pady=10)

        button_back = tk.Button(login_frame, text="Kembali", command=lambda: show_menu_awal(), font=("Arial", 12), bg="#ff00ff")
        button_back.pack(pady=10)

        login_frame.place(relx=0.5, rely=0.5, anchor="center")

    def login_norek(norek, pin):
        norek = int(norek)
        pin = int(pin)

        if norek not in users_info:
            messagebox.showerror("Error", "NOMOR REKENING TIDAK VALID!")
            return

        elif not users[norek].check_pin(pin):
            messagebox.showerror("Error", "PIN SALAH! TRANSAKSI BATAL")
            return

        clear_frame()
        show_transaction_menu(norek)

    def show_email_login_menu():
        clear_frame()
        email_login_frame = tk.Frame(root, bg="#000000")

        label_email = tk.Label(email_login_frame, text="Email:", font=("Arial", 12), bg="#000000", fg="white")
        label_email.pack()
        entry_email = tk.Entry(email_login_frame, font=("Arial", 12))
        entry_email.pack()

        label_password = tk.Label(email_login_frame, text="Password:", font=("Arial", 12), bg="#000000", fg="white")
        label_password.pack()
        entry_password = tk.Entry(email_login_frame, show="*", font=("Arial", 12))
        entry_password.pack()

        button_login = tk.Button(email_login_frame, text="Login", command=lambda: login_email(entry_email.get(), entry_password.get()), font=("Arial", 12), bg="#ff00ff")
        button_login.pack(pady=10)

        button_back = tk.Button(email_login_frame, text="Kembali", command=lambda: show_menu_awal(), font=("Arial", 12), bg="#ff00ff")
        button_back.pack(pady=10)

        email_login_frame.place(relx=0.5, rely=0.5, anchor="center")

    def login_email(email, password):
        for norek, user in users.items():
            if user.email == email and user.check_password(password):
                clear_frame()
                show_transaction_menu(norek)
                return

        messagebox.showerror("Error", "Email atau Password salah!")

    def show_sign_in_menu():
        clear_frame()
        sign_in_frame = tk.Frame(root, bg="#000000")

        label_email = tk.Label(sign_in_frame, text="Email:", font=("Arial", 12), bg="#000000", fg="white")
        label_email.pack()
        entry_email = tk.Entry(sign_in_frame, font=("Arial", 12))
        entry_email.pack()

        label_password = tk.Label(sign_in_frame, text="Password:", font=("Arial", 12), bg="#000000", fg="white")
        label_password.pack()
        entry_password = tk.Entry(sign_in_frame, show="*", font=("Arial", 12))
        entry_password.pack()

        label_confirm_password = tk.Label(sign_in_frame, text="Konfirmasi Password:", font=("Arial", 12), bg="#000000", fg="white")
        label_confirm_password.pack()
        entry_confirm_password = tk.Entry(sign_in_frame, show="*", font=("Arial", 12))
        entry_confirm_password.pack()

        label_pin = tk.Label(sign_in_frame, text="PIN:", font=("Arial", 12), bg="#000000", fg="white")
        label_pin.pack()
        entry_pin = tk.Entry(sign_in_frame, show="*", font=("Arial", 12))
        entry_pin.pack()

        label_confirm_pin = tk.Label(sign_in_frame, text="Konfirmasi PIN:", font=("Arial", 12), bg="#000000", fg="white")
        label_confirm_pin.pack()
        entry_confirm_pin = tk.Entry(sign_in_frame, show="*", font=("Arial", 12))
        entry_confirm_pin.pack()

        label_initial_deposit = tk.Label(sign_in_frame, text="Setoran Awal:", font=("Arial", 12), bg="#000000", fg="white")
        label_initial_deposit.pack()
        entry_initial_deposit = tk.Entry(sign_in_frame, font=("Arial", 12))
        entry_initial_deposit.pack()

        button_sign_in = tk.Button(sign_in_frame, text="Sign Up", command=lambda: sign_in(entry_email.get(), entry_password.get(), entry_confirm_password.get(), entry_pin.get(), entry_confirm_pin.get(), entry_initial_deposit.get()), font=("Arial", 12), bg="#ff00ff")
        button_sign_in.pack(pady=10)

        button_back = tk.Button(sign_in_frame, text="Kembali", command=lambda: show_menu_awal(), font=("Arial", 12), bg="#ff00ff")
        button_back.pack(pady=10)

        sign_in_frame.place(relx=0.5, rely=0.5, anchor="center")

    def sign_in(email, password, confirm_password, pin, confirm_pin, initial_deposit):
        if password != confirm_password:
            messagebox.showerror("Error", "Password tidak cocok!")
            return
        if pin != confirm_pin:
            messagebox.showerror("Error", "PIN tidak cocok!")
            return
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$', password):
            messagebox.showerror("Error", "Password harus mengandung huruf besar, huruf kecil, dan angka!")
            return
        norek = random.randint(1000000000, 9999999999)
        while norek in users_info:
            norek = random.randint(1000000000, 9999999999)
        pin = int(pin)
        initial_deposit = int(initial_deposit)

        users_info[norek] = {'pin': pin, 'saldo': initial_deposit, 'email': email, 'password': password}
        users[norek] = UserInfo.UserInfo(norek, pin, initial_deposit, email, password)
        messagebox.showinfo("Success", f"Akun berhasil dibuat!\nNomor Rekening Anda: {norek}")
        show_menu_awal()

    def show_transaction_menu(norek):
        clear_frame()
        transaction_frame = tk.Frame(root, bg="#000000")

        label_transaction = tk.Label(transaction_frame, text="Pilih Jenis Transaksi:", font=("Arial", 14), bg="#000000", fg="white")
        label_transaction.pack(pady=20)

        button_tarik = tk.Button(transaction_frame, text="Tarik Tunai", command=lambda: show_tarik_tunai_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_tarik.pack()

        button_setor = tk.Button(transaction_frame, text="Setor Tunai", command=lambda: show_setor_tunai_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_setor.pack(pady=10)

        button_transfer = tk.Button(transaction_frame, text="Transfer Dana", command=lambda: show_transfer_dana_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_transfer.pack(pady=10)

        button_cek_saldo = tk.Button(transaction_frame, text="Cek Saldo", command=lambda: show_cek_saldo_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_cek_saldo.pack()

        button_mutasi = tk.Button(transaction_frame, text="Mutasi Transaksi", command=lambda: show_mutasi_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_mutasi.pack(pady=1)

        button_cancel = tk.Button(transaction_frame, text="Log Out", command=lambda: show_menu_awal(), font=("Arial", 12), bg="#ff00ff")
        button_cancel.pack(pady=10)

        transaction_frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_setor_tunai_menu(norek):
        clear_frame()
        setor_tunai_frame = tk.Frame(root, bg="#000000")

        label_nominal = tk.Label(setor_tunai_frame, text="Nominal Setoran:", font=("Arial", 12), bg="#000000", fg="white")
        label_nominal.pack()
        entry_nominal = tk.Entry(setor_tunai_frame, font=("Arial", 12))
        entry_nominal.pack()

        def setor_tunai():
            nominal = int(entry_nominal.get())
            result = atm_system.setor_tunai(norek, nominal)
            messagebox.showinfo("Info", result)
            show_transaction_menu(norek)

        button_setor = tk.Button(setor_tunai_frame, text="Setor Tunai", command=setor_tunai, font=("Arial", 12), bg="#ff00ff")
        button_setor.pack(pady=10)

        button_cancel = tk.Button(setor_tunai_frame, text="Batal Transaksi", command=lambda: show_transaction_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_cancel.pack(pady=10)

        setor_tunai_frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_tarik_tunai_menu(norek):
        clear_frame()
        tarik_tunai_frame = tk.Frame(root, bg="#000000")

        label_nominal = tk.Label(tarik_tunai_frame, text="Nominal Penarikan:", font=("Arial", 12), bg="#000000", fg="white")
        label_nominal.pack()
        entry_nominal = tk.Entry(tarik_tunai_frame, font=("Arial", 12))
        entry_nominal.pack()

        def tarik_tunai():
            nominal = int(entry_nominal.get())
            result = atm_system.tarik_tunai(nominal, norek)
            messagebox.showinfo("Info", result)
            show_transaction_menu(norek)

        button_tarik = tk.Button(tarik_tunai_frame, text="Tarik Tunai", command=tarik_tunai, font=("Arial", 12), bg="#ff00ff")
        button_tarik.pack(pady=10)

        button_cancel = tk.Button(tarik_tunai_frame, text="Batal Transaksi", command=lambda: show_transaction_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_cancel.pack(pady=10)

        tarik_tunai_frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_transfer_dana_menu(norek):
        clear_frame()
        transfer_dana_frame = tk.Frame(root, bg="#000000")

        label_rek_tujuan = tk.Label(transfer_dana_frame, text="Nomor Rekening Tujuan:", font=("Arial", 12), bg="#000000", fg="white")
        label_rek_tujuan.pack()
        entry_rek_tujuan = tk.Entry(transfer_dana_frame, font=("Arial", 12))
        entry_rek_tujuan.pack()

        label_jumlah = tk.Label(transfer_dana_frame, text="Jumlah:", font=("Arial", 12), bg="#000000", fg="white")
        label_jumlah.pack()
        entry_jumlah = tk.Entry(transfer_dana_frame, font=("Arial", 12))
        entry_jumlah.pack()

        def transfer_dana():
            rek_tujuan_input = int(entry_rek_tujuan.get())
            jumlah_input = int(entry_jumlah.get())

            if rek_tujuan_input not in users_info:
                messagebox.showerror("Error", "Nomor Rekening Tujuan Tidak Valid!")
                return

            messagebox.showinfo("Info", atm_system.transfer_dana(rek_tujuan_input, jumlah_input, norek))
            show_transaction_menu(norek)

        button_transfer = tk.Button(transfer_dana_frame, text="Transfer Dana", command=transfer_dana, font=("Arial", 12), bg="#ff00ff")
        button_transfer.pack(pady=10)

        button_cancel = tk.Button(transfer_dana_frame, text="Batal Transaksi", command=lambda: show_transaction_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_cancel.pack(pady=10)

        transfer_dana_frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_cek_saldo_menu(norek):
        clear_frame()
        cek_saldo_frame = tk.Frame(root, bg="#000000")

        def cek_saldo():
            messagebox.showinfo("Info", atm_system.cek_saldo(norek))
            show_transaction_menu(norek)

        button_cek_saldo = tk.Button(cek_saldo_frame, text="Cek Saldo", command=cek_saldo, font=("Arial", 12), bg="#ff00ff")
        button_cek_saldo.pack(pady=10)

        button_cancel = tk.Button(cek_saldo_frame, text="Batal Transaksi", command=lambda: show_transaction_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_cancel.pack(pady=10)

        cek_saldo_frame.place(relx=0.5, rely=0.5, anchor="center")

    def show_mutasi_menu(norek):
        clear_frame()
        mutasi_frame = tk.Frame(root, bg="#000000")

        def show_mutasi(hari):
            transaksi = atm_system.mutasi_transaksi(norek, hari)
            transaksi_str = "\n".join([f"{t['tanggal']} - {t['jenis']} - {t['nominal']}" for t in transaksi])
            messagebox.showinfo("Mutasi Transaksi", transaksi_str)

        button_5_transaksi = tk.Button(mutasi_frame, text="5 Transaksi Terakhir", command=lambda: show_mutasi(None), font=("Arial", 12), bg="#ff00ff")
        button_5_transaksi.pack(pady=10)

        button_3_hari = tk.Button(mutasi_frame, text="3 Hari Terakhir", command=lambda: show_mutasi(3), font=("Arial", 12), bg="#ff00ff")
        button_3_hari.pack(pady=10)

        button_7_hari = tk.Button(mutasi_frame, text="7 Hari Terakhir", command=lambda: show_mutasi(7), font=("Arial", 12), bg="#ff00ff")
        button_7_hari.pack(pady=10)

        button_cancel = tk.Button(mutasi_frame, text="Batal Transaksi", command=lambda: show_transaction_menu(norek), font=("Arial", 12), bg="#ff00ff")
        button_cancel.pack(pady=10)

        mutasi_frame.place(relx=0.5, rely=0.5, anchor="center")

    def clear_frame():
        for widget in root.winfo_children():
            widget.destroy()

    root = tk.Tk()
    root.title("ATM Application [Shata' H. Al Fa'Iq (21120123130066)]")
    root.geometry("860x620")
    root.configure(bg="#000000")

    show_menu_awal()

    root.mainloop()

if __name__ == "__main__":
    main()