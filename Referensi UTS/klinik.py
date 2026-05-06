from datetime import datetime, timedelta
import random

class Patient:
    def __init__(self, name, queue_number):
        self.name = name
        self.queue_number = queue_number
        self.arrival_time = datetime.now()
        self.severity = random.randint(1, 5)

    def __str__(self):
        return f"[{self.queue_number}] {self.name} (Severity: {self.severity})"


class Doctor:
    def __init__(self, name):
        self.name = name
        self.available_at = datetime.now()
        self.current_patient = None

    def treat(self, patient):
        duration = random.randint(5, 15)  # menit
        start_time = max(datetime.now(), self.available_at)
        end_time = start_time + timedelta(minutes=duration)

        self.available_at = end_time
        self.current_patient = patient

        return start_time, end_time, duration


class Clinic:
    def __init__(self):
        self.queue = []
        self.history = []
        self.doctor = Doctor("Dr. Budi")
        self.counter = 1

    def add_patient(self, name):
        patient = Patient(name, self.counter)
        self.queue.append(patient)
        self.counter += 1
        print(f"Pasien masuk: {patient}")

    def call_next(self):
        if not self.queue:
            print("Tidak ada antrian.")
            return

        self.queue.sort(key=lambda x: x.severity, reverse=True)

        patient = self.queue.pop(0)
        start, end, duration = self.doctor.treat(patient)

        print(f"\nMemanggil: {patient}")
        print(f"Mulai: {start.strftime('%H:%M:%S')}")
        print(f"Selesai: {end.strftime('%H:%M:%S')} ({duration} menit)\n")

        self.history.append(patient)

clinic = Clinic()

while True:
    print("\n1. Tambah Pasien")
    print("2. Panggil Pasien")
    print("3. Keluar")

    choice = input("Pilih: ")

    if choice == "1":
        name = input("Nama pasien: ")
        clinic.add_patient(name)

    elif choice == "2":
        clinic.call_next()

    elif choice == "3":
        break