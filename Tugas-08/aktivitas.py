# =========================
# SOAL 1 - PAPAN CATUR
# =========================

print('🌸 === PAPAN CATUR === 🌸\n')

for i in range(8):
    for j in range(8):

        if (i + j) % 2 == 0:
            print('⬛', end=' ')
        else:
            print('⬜', end=' ')

    print()


# =========================
# SOAL 2 - PROGRAM AKTIVITAS
# =========================

list_aktivitas = []

while True:

    print('\n🌷 === MENU AKTIVITAS HARIAN === 🌷')
    print('1. 📝 Tambah Aktivitas')
    print('2. 📋 Tampilkan Aktivitas')
    print('3. 🗑️ Hapus Aktivitas')
    print('4. 🐣 Selesai')

    menu = input('👉 Pilih menu: ')

    # =========================
    # TAMBAH AKTIVITAS
    # =========================
    if menu == '1':

        print('\n🐻 Tambah Aktivitas Baru')

        aktivitas = input('📝 Nama aktivitas : ')
        waktu = input('⏰ Waktu aktivitas : ')
        prioritas = input('⭐ Prioritas aktivitas : ')
        mood = input('🌈 Mood saat aktivitas : ')

        data = {
            'aktivitas': aktivitas,
            'waktu': waktu,
            'prioritas': prioritas,
            'mood': mood
        }

        list_aktivitas.append(data)

        print('\n🌸 Aktivitas berhasil ditambahkan! 🌸')

    # =========================
    # TAMPILKAN AKTIVITAS
    # =========================
    elif menu == '2':

        if len(list_aktivitas) == 0:
            print('\n🐰 Belum ada aktivitas yang tersimpan')
        
        else:
            print('\n📚 === DAFTAR AKTIVITAS === 📚')

            nomor = 1

            for item in list_aktivitas:

                print(f'\n🐼 Aktivitas ke-{nomor}')
                print(f'📝 Aktivitas : {item["aktivitas"]}')
                print(f'⏰ Waktu     : {item["waktu"]}')
                print(f'⭐ Prioritas : {item["prioritas"]}')
                print(f'🌈 Mood      : {item["mood"]}')

                nomor += 1

    # =========================
    # HAPUS AKTIVITAS
    # =========================
    elif menu == '3':

        if len(list_aktivitas) == 0:
            print('\n🦊 Data aktivitas masih kosong')

        else:
            print('\n🗂️ Daftar Aktivitas')

            nomor = 1

            for item in list_aktivitas:
                print(f'{nomor}. {item["aktivitas"]}')
                nomor += 1

            hapus = int(input('\n❌ Masukkan nomor aktivitas yang ingin dihapus: '))

            if hapus <= len(list_aktivitas):
                list_aktivitas.pop(hapus - 1)
                print('🌼 Aktivitas berhasil dihapus')
            else:
                print('⚠️ Nomor aktivitas tidak tersedia')

    # =========================
    # SELESAI
    # =========================
    elif menu == '4':
        print('\n🐣 Program selesai, semangat menjalani hari 🌷')
        break

    # =========================
    # VALIDASI MENU
    # =========================
    else:
        print('\n⚠️ Menu tidak tersedia')