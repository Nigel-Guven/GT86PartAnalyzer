class Cinema_Object:

	def __init__(self, cine_name, cine_url, film_list):		#constructor
		self.cine_name = cine_name
		self.cine_url = cine_url
		self.film_list = film_list
	
	def printCinemaObject(self):							#list_information
		print(self.cine_name)
		print(self.cine_url)
		print(self.film_list)
	
	def __repr__(self):
		return str(self)

	def __str__(self):
		return "({}, {})".format(self.cine_name, self.cine_url, self.film_list)  
	  
class Film_Object:
	
	def __init__(self, film_name, film_runtime, film_rating, film_times, film_image_url):				#constructor
		self.film_name = film_name
		self.film_runtime = film_runtime
		self.film_rating = film_rating	
		self.film_times = film_times
		self.film_image_url = film_image_url
		
	def printFilmObject(self):								#list_information
		print(self.film_name)
		print(film_runtime)
		print(film_rating)
		print(self.film_times)
		print(self.film_image_url)
		
	def __repr__(self):
		return str(self)

	def __str__(self):
		return "({}, {})".format(self.film_name, self.film_runtime, self.film_rating, self.film_times,self.film_image_url)	