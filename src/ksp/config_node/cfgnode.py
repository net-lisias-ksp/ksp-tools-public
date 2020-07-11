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

Based on the source https://github.com/taniwha/io_object_mu/blob/master/cfgnode/cfgnode.py
'''

from ksp.config_node.parser import Parser, ParserError

class ConfigNodeError(ParserError):
	def __init__(self, parser:Parser, msg:str):
		super().__init__(parser, msg)

class ConfigNode:

	__CONVERTERS = dict()

	__CONVERTERS['PART'] = dict()
	#__CONVERTERS['PART']['name'] = lambda v : v.replace("_",".") if str == type(v) else v
	__CONVERTERS['PART']['cost'] = lambda v : float(v) if str == type(v) else v
	__CONVERTERS['PART']['entryCost'] = lambda v : float(v) if str == type(v) else v
	__CONVERTERS['PART']['mass'] = lambda v : float(v) if str == type(v) else v
	__CONVERTERS['PART']['maximum_drag'] = lambda v : float(v) if str == type(v) else v
	__CONVERTERS['PART']['minimum_drag'] = lambda v : float(v) if str == type(v) else v
	__CONVERTERS['PART']['angularDrag'] = lambda v : float(v) if str == type(v) else v
	__CONVERTERS['PART']['crashTolerance'] = lambda v : float(v) if str == type(v) else v
	__CONVERTERS['PART']['maxTemp'] = lambda v : float(v) if str == type(v) else v
	__CONVERTERS['PART']['PhysicsSignificance'] = lambda v : 0 != int(v) if str == type(v) else v
	__CONVERTERS['PART']['scale'] = lambda v : [float(vv.strip()) for vv in v.split(",")] if str == type(v) else v
	__CONVERTERS['PART']['bulkheadProfiles'] = lambda v : [vv.strip() for vv in v.split(",")] if str == type(v) else v
	__CONVERTERS['PART']['TechRequired'] = lambda v : [vv.strip() for vv in v.split(",")] if str == type(v) else v
	__CONVERTERS['PART']['tags'] = lambda v : [vv.strip() for vv in v.split(",")] if str == type(v) else v

	def __init__(self, name:str = None):
		self.name = name
		self.__values = dict()
		self.__nodes = dict()

	@classmethod
	def __parse(cls, node, parser:Parser, top:bool = False, localization:dict=dict()):
		while parser.tokenAvailable(True):
			token_start = parser.pos
			if parser.getToken(True) == None:
				break
			if parser.token in (['{', '}', '='] if top else ['{', '=']):
				raise ConfigNodeError(parser, "unexpected " + parser.token)
			if parser.token == '}':
				return
			token_end = parser.pos
			key = parser.token
			while parser.tokenAvailable(True):
				parser.getToken(True)
				token_end = parser.pos
				if parser.token == '=':
					value = ''
					if parser.tokenAvailable(False):
						parser.getLine()
						value = parser.token.strip()
						if value.startswith("#") and value in localization:
							value = localization[value]
					node.add_value(key, value)
					break
				elif parser.token == '{':
					new_node = ConfigNode(key)
					ConfigNode.__parse(new_node, parser, False, localization)
					node.add_node(key, new_node)
					break
				else:
					#cfg_error(parser, "unexpected " + parser.token)
					key = parser.text[token_start:token_end]
		if not top:
			raise ConfigNodeError(parser, "unexpected end of file")

	@classmethod
	def load(cls, text:str, path:str = "", localization:dict=dict()):
		if not text:
			return []
		parser = Parser(path, text, "{}=", False)
		nodes = []
		try:
			while parser.tokenAvailable(True):
				node = ConfigNode()
				ConfigNode.__parse(node, parser, True, localization)
				nodes.append(node)
			if len(nodes) == 1:
				return nodes[0]
			else:
				return nodes
		except ParserError as e:
			raise ConfigNodeError(parser, e.message)

	@classmethod
	def load_file(cls, path:str, localization:dict=dict()):
		_text = open(path, "r", encoding='utf-8-sig').read()
		return cls.load(_text, path, localization)

	@property
	def values(self):
		return self.__values.items()

	@property
	def nodes(self):
		return self.__nodes.items()

	def has_node(self, key):
		return key in self.__nodes

	def get_node(self, key):
		if key in self.__nodes:
			return self.__nodes[key]
		raise LookupError("No node called {0} found!".format(key))

	def add_node(self, key, node):
		if key in self.__nodes:
			if list == type(self.__nodes[key]):
				self.__nodes[key].append(node)
			else:
				oldnode = self.__nodes[key]
				self.__nodes[key] = list()
				self.__nodes[key].append(oldnode)
				self.__nodes[key].append(node)
		else:
			self.__nodes[key] = node

	def has_value(self, key):
		return key in self.__values

	def get_value(self, key):
		if key in self.__values:
			return self.__values[key]
		raise LookupError("No value called {0} found!".format(key))

	def add_value(self, key, value):
		if self.name in ConfigNode.__CONVERTERS and key in ConfigNode.__CONVERTERS[self.name]:
			value = ConfigNode.__CONVERTERS[self.name][key](value)

		if key in self.__values:
			if list == type(self.__values[key]):
				self.__values[key].append(value)
			else:
				oldvalue = self.__values[key]
				self.__values[key] = list()
				self.__values[key].append(oldvalue)
				self.__values[key].append(value)
		else:
			self.__values[key] = value

	def to_string(self, level = 0):
		extra = 0
		if level >= 0:
			extra = 2
		text=[None] * (len(self.__values) + len(self.__nodes) + extra)
		index = 0
		if level >= 0:
			text[index] = "{\n"
			index += 1
		for val in self.__values.items():
			text[index] = "%s%s = %s\n" % ("    " * (level + 1), val[0], val[1])
			index += 1
		for node in self.__nodes.items():
			ntext = node[1].to_string(level + 1)
			text[index] = "%s%s %s\n" % ("    " * (level + 1), node[0], ntext)
			index += 1
		if level >= 0:
			text[index] = "%s}\n" % ("    " * (level))
			index += 1
		return "".join(text)

	def __repr__(self):
		return self.to_string(0)
