import math
from bitarray import bitarray

class LZ77Compressor:
	"""
	implementacion para el algoritmo de lz77
	"""
	MAX_WINDOW_SIZE = 400

	def __init__(self, window_size=20):
		self.window_size = min(window_size, self.MAX_WINDOW_SIZE) 
		self.lookahead_buffer_size = 15 # el largo del match es a lo maximo 4 bits (15)

	def compress(self, input_file_path, output_file_path=None, verbose=False):
		"""#
		El formato de compresion sera:
		0 bit seguido de 8 bits, cuando no matchea el caracter actual con la ventana de revision

		1 bit seguido de 12 bits para declarar la distancia al comienzo del match desde la posicion actual
		4 bits para el largo del match (matches de maximo 16 de distancia)
		
		se crea un archivo binario en el output especificado
		"""
		data = None
		i = 0
		output_buffer = bitarray(endian='big')

		# leer la imagen
		try:
			with open(input_file_path, 'rb') as input_file:
				data = input_file.read()
		except IOError:
			print('no se pudo abrir el input')
			raise

		while i < len(data):

			match = self.findLongestMatch(data, i)

			if match: 
				# añade un bit de inicio, seguido de 12 bits para indicar la distancia a la posicion del match
				# seguido de 4 bits para el largo del
	
				(bestMatchDistance, bestMatchLength) = match

				output_buffer.append(True)
				output_buffer.frombytes(bytes([bestMatchDistance >> 4]))
				output_buffer.frombytes(bytes([((bestMatchDistance & 0xf) << 4) | bestMatchLength]))

				if verbose:
                                        print("<1, %i, %i>" % (bestMatchDistance, bestMatchLength), end='')

				i += bestMatchLength

			else:
				# No hay match, bit con 0 para marcar seguido de 8 bits que especifican el numero
				output_buffer.append(False)
				output_buffer.frombytes(bytes([data[i]]))
				
				if verbose:
					print("<0, %s>" % data[i], end='')

				i += 1

		# llena el buffer hasta el proximo multiplo de 8 con bits en 0
		output_buffer.fill()

		# escribe el archivo comprimido
		if output_file_path:
			try:
				with open(output_file_path, 'wb') as output_file:
					output_file.write(output_buffer.tobytes())
					print("funciono la compresion :) ...")
					return None
			except IOError:
				print('error con el output path ...')
				raise

		# caso en que no se de outputfile
		return output_buffer


	def decompress(self, input_file_path, output_file_path=None):
		"""
		dado el path de un archivo comprimido, descomprime el archivo en un output file.
		"""
		data = bitarray(endian='big')
		output_buffer = []

		# lee el archivo comprimido
		try:
			with open(input_file_path, 'rb') as input_file:
				data.fromfile(input_file)
		except IOError:
			print('no se pudo abrir el archivo ...')
			raise

		while len(data) >= 9:

			flag = data.pop(0)

			if not flag:
				byte = data[0:8].tobytes()

				output_buffer.append(byte)
				del data[0:8]
			else:
				byte1 = ord(data[0:8].tobytes())
				byte2 = ord(data[8:16].tobytes())

				del data[0:16]
				distance = (byte1 << 4) | (byte2 >> 4)
				length = (byte2 & 0xf)

				for i in range(length):
					output_buffer.append(output_buffer[-distance])
		out_data =  b''.join(output_buffer)

		if output_file_path:
			try:
				with open(output_file_path, 'wb') as output_file:
					output_file.write(out_data)
					print('la descompresion funciono :)')
					return None 
			except IOError:
				print('hubo en error con el output...')
				raise 
		return out_data


	def findLongestMatch(self, data, current_position):
		""" 
		Encuentra el match mas largo para la prefix del string actual, buscando posibles 
		matches en el buffer que se lleva de posiciones pasadas
		"""
		end_of_buffer = min(current_position + self.lookahead_buffer_size, len(data) + 1)

		best_match_distance = -1
		best_match_length = -1

		for j in range(current_position + 2, end_of_buffer):

			start_index = max(0, current_position - self.window_size)
			substring = data[current_position:j]

			for i in range(start_index, current_position):

				repetitions = len(substring) // (current_position - i)

				last = len(substring) % (current_position - i)

				matched_string = data[i:current_position] * repetitions + data[i:i+last]

				if matched_string == substring and len(substring) > best_match_length:
					best_match_distance = current_position - i 
					best_match_length = len(substring)

		if best_match_distance > 0 and best_match_length > 0:
			return (best_match_distance, best_match_length)
		return None

# la base del codigo fue tomada de https://github.com/manassra/LZ77-Compressor/blob/master/src/LZ77.py
# y se realizaron pequeños cambios.
