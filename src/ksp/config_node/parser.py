#    This file is part of KSP Tools
#    © 2020 LisiasT
#
#    KSP Tools is licensed as follows:
#
#        * GPL 2.0 : https://www.gnu.org/licenses/gpl-2.0.txt
#
#    KSP Tools is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#    You should have received a copy of the GNU General Public License 2.0
#    along with KSP Tools, if not see <https://www.gnu.org/licenses/>.
#
'''
Created on Jul 8, 2020

@author: lisias, taniwha

Based on the source https://github.com/taniwha/io_object_mu/blob/master/cfgnode/script.py

'''


class ParserError(Exception):
	def __init__(self, parser, message):
		self.filename = parser.filename
		self.line = parser.line
		self.message = message

		super().__init__(self.__str__())

	def __str__(self):
		return "{0}:{1} :: {2}" .format(self.filename, self.line, self.message)

class Parser:
	def __init__(self, filename, text, single="{}()':", quotes=True):
		self.filename = filename
		self.text = text
		self.single = single
		self.quotes = quotes
		self.pos = 0
		self.line = 1
		self.unget = False

	def error(self, msg):
		raise ParserError(self.filename, self.line, msg)

	def tokenAvailable(self, crossline=False):
		if self.unget:
			return True
		while self.pos < len(self.text):
			while self.pos < len(self.text) and self.text[self.pos].isspace():
				if self.text[self.pos] == "\n":
					if not crossline:
						return False
					self.line += 1
				self.pos += 1
			if self.pos == len(self.text):
				return False
			if self.text[self.pos] in ["\x1a", "\x04"]:
				# end of file characters
				self.pos += 1
				continue
			if self.text[self.pos:self.pos + 2] == "//":
				while (self.pos < len(self.text)
					and self.text[self.pos] != "\n"):
					self.pos += 1
				if self.pos == len(self.text):
					return False
				if not crossline:
					return False
				continue
			return True
		return False

	def getLine(self):
		start = self.pos
		end = start
		while self.pos < len(self.text):
			if self.text[self.pos] == "\n":
				self.line += 1
				self.pos += 1
				break
			if self.text[self.pos:self.pos + 2] == "//":
				break
			self.pos += 1
			end = self.pos
		if self.unget:
			self.unget = False
			self.token = self.token + self.text[start:end]
		else:
			self.token = self.text[start:end]
		return self.pos < len(self.text)

	def getToken(self, crossline=False):
		if self.unget:
			self.unget = False
			return self.token
		if not self.tokenAvailable(crossline):
			if not crossline:
				self.error("line is incomplete")
			return None
		if self.quotes and self.text[self.pos] == "\"":
			self.pos += 1
			start = self.pos
			if self.text[self.pos] == len(self.text):
				self.error("EOF inside quoted string")
			while self.text[self.pos] != "\"":
				if self.pos == len(self.text):
					self.error("EOF inside quoted string")
					return None
				if self.text[self.pos] == "\n":
					self.line += 1
				self.pos += 1
			self.token = self.text[start:self.pos]
			self.pos += 1
		else:
			start = self.pos
			if self.text[self.pos] in self.single:
				self.pos += 1
			else:
				while (self.pos < len(self.text)
					and not self.text[self.pos].isspace()
					and self.text[self.pos] not in self.single):
					self.pos += 1
			self.token = self.text[start:self.pos]
		return self.token

	def ungetToken(self):
		self.unget = True
