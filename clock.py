class Clock():
	def __init__(self, hours, minutes=00):
		self.hours = hours
		self.minutes = minutes
		
	def __add__(self, other):
		time_in_minutes=self.hours*60+self.minutes
		time_in_minutes+=other
		return self.new(time_in_minutes)
	
	def __sub__(self, other):
		time_in_minutes=self.hours*60+self.minutes
		time_in_minutes-=other
		return self.new(time_in_minutes)
	
	def __eq__(self,other):
		return self.__str__()==other
	
	def new (self, time_in_minutes):
		if time_in_minutes>1440:
			days=time_in_minutes/1440
			time_in_minutes-=days*1440
		self.hours=time_in_minutes/60
		self.minutes=time_in_minutes % 60
		return self.__str__()
		
	def __str__(self):
		if self.hours<10:
			hours= "0%s" % (self.hours)
		else:
			hours= "%s" % (self.hours)
		if self.minutes<10:
			minutes= "0%s" % (self.minutes)
		else:
			minutes= "%s" % (self.minutes)
		return "%s:%s" % (hours, minutes)
	
	@classmethod
	def at(cls, hours, minutes=00):
		return cls(hours, minutes)
	
	

