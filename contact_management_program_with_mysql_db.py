# import class ERROR untuk memunculkan pesan error
from mysql.connector import Error
# untuk keluar dari program jika terjadi error saat mencoba connect ke database
from sys import exit

# error handling jika terjadi error saat mencoba connect ke database
try:
	from connect_db import mydb, mycursor
except Error as err:
	print(f'\n{err}')
	# function from sys module
	exit()

from tabulate import tabulate

class function:

	def edit_kontak_function(query_result, identifier_column, data_to_edit):
		if ( query_result ):
			what_to_edit = input('apa yang ingin anda edit (nama/no_telp)? ').strip()

			if what_to_edit.lower() == 'nama':
				nama = input('masukan nama baru: ').strip()
				mycursor.execute(f'update daftar_kontak set nama = "{nama}" where {identifier_column} = "{data_to_edit}"')
				mydb.commit()
				print('\nPengubahan berhasil')

			elif what_to_edit.lower() == 'no_telp':
				no_telp = input('masukan no telepon baru: ').strip()
				mycursor.execute(f'update daftar_kontak set no_telp = "{no_telp}" where {identifier_column} = "{data_to_edit}"')
				mydb.commit()
				print("\nPengubahan berhasil")

			else:
				print('\ninput tidak valid')

		else:
			print(f'\n{data_to_edit} tidak ada dalam daftar')

	def cari_kontak_function(search_by, input_data):
		# query all data in database table
		mycursor.execute(f'select * from daftar_kontak')
		query_result = mycursor.fetchall()

		def filter_search(x):
			if search_by == 'nama':
				if input_data in x[1]:
					return True

			elif search_by == 'no_telp':
				if input_data in x[2]:
					return True

			else:
				return False

		data_after_filter = list(filter(filter_search, query_result))

		# truthy check
		if ( data_after_filter ):
			print(tabulate(data_after_filter, headers=['id', 'nama', 'no_telp']))

		else:
			print(f'{search_by} {input_data} tidak ditemukan')

	def hapus_kontak_function(identifier_column, data_to_delete):
		try:
			mycursor.execute(f'delete from daftar_kontak where {identifier_column} = "{data_to_delete}"')
			mydb.commit()
			assert mycursor.rowcount >= 1
			print('\n' + str(mycursor.rowcount), 'Kontak berhasil dihapus')
		except:
			print(f'\nMaaf {identifier_column} {data_to_delete} tidak ada di dalam database kami')


class Contact_management:
	def __init__(self, start_app=False):
		# jika tabel kosong maka auto increment direset kembali ke 1
		mycursor.execute('select id from daftar_kontak limit 1')
		if ( not mycursor.fetchall() ):
			mycursor.execute('alter table daftar_kontak auto_increment = 1')

		if ( start_app == True ):
			# menampilkan option
			self.option()
			try:
				option = int(input('\nPilih option: '))
				match ( option ):
					case 1:
						self.tambah_kontak()
					case 2:
						self.hapus_kontak()
					case 3:
						self.hapus_semua_kontak()
					case 4:
						self.edit_kontak()
					case 5:
						self.cari_kontak()
					case 6:
						self.lihat_kontak()
					case _:
						print('Input tidak valid')

			except ValueError:
				print('\nTidak menerima selain angka integer')

		else:
			pass

	# option menu
	def option(self):
		# to add space
		print()
		print('Program Manajemen Kontak\n')
		print('1. Tambah Kontak')
		print('2. Hapus Kontak')
		print('3. Hapus Semua Kontak')
		print('4. Edit Kontak')
		print('5. Cari Kontak')
		print('6. Lihat Kontak')

	# option 1
	def tambah_kontak(self):
		nama = input('\nNama: ').strip()

		if ( not nama ):
			print('\nNama tidak boleh kosong')
			return False

		no_telp = input('No Telepon: ').strip()

		if ( not  no_telp ):
			print('\nNo telepon tidak boleh kosong')
			return False

		mycursor.execute(f'''insert into daftar_kontak values ('', '{nama}', '{no_telp}') ''')
		mydb.commit()
		print('\nKontak berhasil ditambahkan')

	# option 2
	def hapus_kontak(self):
		mycursor.execute('select id from daftar_kontak limit 1')

		# jika tabel tidak kosong maka lanjutkan jika kosong maka berhenti
		if mycursor.fetchall():
			pass

		else:
			print('\nDaftar kontak kosong')
			return False
		
		mycursor.execute('select * from daftar_kontak')
		print(tabulate(mycursor.fetchall(), headers=['id', 'nama', 'no_telp']))

		hapus_by = input('\nhapus by (id/nama/no_telp): ')

		if hapus_by.lower() == 'id':

			input_id = input('masukan id: ').strip()

			function.hapus_kontak_function('id', input_id)

		elif hapus_by.lower() == 'nama':
			input_nama = input('Masukan nama kontak yang ingin anda hapus: ').strip()

			function.hapus_kontak_function('nama', input_nama)

		elif hapus_by.lower() == 'no_telp':
			input_no_telp = input('Masukan no telepon yang ingin anda hapus: ').strip()

			function.hapus_kontak_function('no_telp', input_no_telp)

		else:
			print('Input tidak valid')

	# option 4
	def hapus_semua_kontak(self):
		# tabel truthy check
		mycursor.execute('select id from daftar_kontak limit 1')
		if ( not mycursor.fetchall() ):
			print('\nTabel kosong')
			return False

		sure = input('Anda yakin ingin menghapus semua kontak (yes/no)? ')

		# validation
		if ( sure.lower() != 'yes' and sure.lower() != 'no' ):
			print('\nInput tidak valid')
			return False

		else:
			if ( sure.lower() == 'yes' ):
				mycursor.execute('delete from daftar_kontak')
				jumlah_kontak_dihapus = mycursor.rowcount
				mydb.commit()
				print('\n' + str(jumlah_kontak_dihapus), 'Kontak berhasil dihapus')

			else:
				print('\nPenghapusan dibatalkan')

	# option 3
	def edit_kontak(self):
		mycursor.execute('select id from daftar_kontak limit 1')


		# jika tabel tidak kosong maka lanjutkan jika kosong maka berhenti
		if mycursor.fetchall():
			pass

		else:
			print('\nDaftar kontak kosong')
			return False

		mycursor.execute('select * from daftar_kontak')
		cek_exists_kontak = mycursor.fetchall()

		print()
		print(tabulate(cek_exists_kontak, headers=['id', 'Nama', 'no_telp']))

		edit_by = input('\nedit by (nama/no_telp): ')

		if edit_by.lower() == 'nama':

			# cek nama input
			nama_to_edit = input('\nMasukan nama kontak yang ingin anda edit: ').strip()

			mycursor.execute(f'select id from daftar_kontak where nama = "{nama_to_edit}"')
			check_exist = mycursor.fetchall()

			function.edit_kontak_function(check_exist, "nama", nama_to_edit)

		elif edit_by.lower() == 'no_telp':

			no_telp_to_edit = input('masukan no telepon kontak yang ingin anda edit: ').strip()

			# cek no telepon input
			mycursor.execute(f'select id from daftar_kontak where no_telp = "{no_telp_to_edit}"')
			check_exist = mycursor.fetchall()

			function.edit_kontak_function(check_exist, 'no_telp', no_telp_to_edit)

		else:
			print('\nMaaf, input tidak valid')

	# option 4
	def cari_kontak(self):
		# check isi tabel
		# kalo tabel tidak ada isinya maka program di-stop
		mycursor.execute('select id from daftar_kontak limit 1')

		# truthy check
		if ( not mycursor.fetchall() ):
			print('\nDaftar kontak kosong')
			return False

		search_by = input('search by (nama/no_telp): ').strip()

		# validasi input
		if search_by.lower() != 'nama' and search_by.lower() != 'no_telp':
			print('\nInput tidak valid')
			return False

		input_data = input(f'masukan {search_by} kontak: ').strip()

		# to give a space
		print()
		function.cari_kontak_function(search_by, input_data)

	# option 5
	def lihat_kontak(self):
		mycursor.execute(f'select * from daftar_kontak')
		print()
		query_result = mycursor.fetchall()
		if ( query_result ):
			print(tabulate(query_result, headers=['id', 'nama', 'no_telp']))

		else:
			print('Daftar kontak kosong')

Contact_management(start_app=True)