# -*- coding: utf-8 -*-

# Copyright 2008 Jaap Karssenberg <pardus@cpan.org>

from tests import TestCase

import zim.plugins

zim.plugins.path = ['.'] # override default search path

class testPlugins(TestCase):
	'''FIXME'''

	def runTest(self):
		'''Test loading plugins and meta data'''
		plugins = zim.plugins.list_plugins()
		self.assertTrue(len(plugins) > 10)
		self.assertTrue('spell' in plugins)
		self.assertTrue('linkmap' in plugins)

		for name in plugins:
			#~ print '>>', name
			plugin = zim.plugins.get_plugin(name)

			# test plugin info
			self.assertTrue(plugin.plugin_info['name'])
			self.assertTrue(plugin.plugin_info['description'])
			self.assertTrue(plugin.plugin_info['author'])

			# test dependencies data
			dep = plugin.check_dependencies()
			self.assertTrue(isinstance(dep,list))
			for i in range(len(dep)):
				self.assertTrue(isinstance(dep[i],tuple))
				self.assertTrue(isinstance(dep[i][0],str))
				self.assertTrue(isinstance(dep[i][1],bool))
