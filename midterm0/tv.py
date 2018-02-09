import sys

class Television:

	def __init__(self, volume):
		self._volume = volume
		self._is_muted = False

	def toggle_mute(self):
		if self._is_muted == False:
			self._is_muted = True
		else:
			self._is_muted = False
		return self._is_muted

	def volume_up(self):
		if self._volume < 10:
			self._volume += 1
		self._is_muted = False
		return self._volume

	def volume_down(self):
		if self._volume > 0:
			self._volume -= 1
		self._is_muted = False
		return self._volume
def main():
	tv = Television(2)
	print(tv.toggle_mute())
	print(tv.toggle_mute())
	for i in range(5):
		print(tv.volume_down())
	print("The volume will no longer decrement.")
	for j in range(15):
		print(tv.volume_up())
	print("The volume will no longer increment.")


main()	
