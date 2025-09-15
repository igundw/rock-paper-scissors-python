import random

pilihan_komputer = ['gunting', 'batu', 'kertas']
komputer = random.choice(pilihan_komputer)
print(f'''
-----------------------------
|     Halo, Selamat Datang   |
|     Di Game Gunting      |
|       Batu Kertas        |
-----------------------------
''')

nama = input('Masukkan Nama Kamu: ')
siap_bermain = input(f'Halo, {nama}! Apakah kamu siap bermain batu gunting kertas hari ini? [Ya/Tidak]: ')
siap_bermain_lower = siap_bermain.lower()

if 'ya' in siap_bermain_lower:
    print('Senang Mendengarnya, Mari Kita Bermain :)\n')

    pilihan_user = input(f'Nah, {nama} sekarang masukkan jagoan kamu! [Gunting / Batu / Kertas]: ').lower() 

    print(f'\nKamu memilih: {pilihan_user}')
    print(f'Komputer memilih: {komputer}\n')

    if komputer == pilihan_user:
        print('Wah, kita seri nih!')
    
    elif pilihan_user == 'batu' and komputer == 'gunting': 
        print('Selamat Kamu Menang')
    
    elif pilihan_user == 'kertas' and komputer == 'batu': 
        print('Selamat Kamu Menang')
    
    elif pilihan_user == 'gunting' and komputer == 'kertas':
        print('Selamat Kamu Menang')
    
    else:
        if pilihan_user not in pilihan_komputer:
            print('Input kamu salah! Harusnya pilih gunting, batu, atau kertas.')
        else:
            print('Yaah, kamu kalaahh :(') 

else:
    print('Sayang sekali :(. Semoga kita bisa bermain di lain kesempatan, ya!')
