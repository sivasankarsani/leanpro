import json
import commands
import os

class FinoramicAssignments:
	# method to check for redundant parenthese or not
	def is_redundant_parentheses(self, A):
		"""
		@param: A
		@type: string contain list of oprators and operand

		stack : list to keep maintain the ops

		@rtype : bool
		"""
		stack = []
		# check for having equal parenthese closes or not
		if not A.count('(') == A.count(')'):
			return 1
		# for each character
		for op in A:
			if op == ')':
				top = stack.pop()
				is_redundant = True
				while top !='(':
					if top in "*+-/":
						is_redundant = False
					top = stack.pop()
				if is_redundant:
					return 1
			else:
				# add each op to list
				stack.append(op)
		return 0

	# Need to get the closurest value
	def three_sum(self, A, B):
		"""
		@param: A
		@type : list

		@param: int
		@type : B

		@rtype : int
		"""
		self.lenth = len(A)
		if self.lenth <3:
			return None
		if self.lenth == 3:
			return sum(A)
		import sys
		self.max_value = sys.maxint
		for _index in range(0,self.lenth-2):
			sec_ind = _index + 1
			end_ind = self.lenth -1
			while sec_ind < end_ind:
				self.best_sum = A[_index] + A[sec_ind] + A[end_ind]
				self.diff = abs(B - self.best_sum)

				if self.diff ==0:
					return self.best_sum

				if self.diff < self.max_value:
					self.max_value = self.diff
					self.closure_num = self.best_sum

				if self.best_sum <=B:
					sec_ind = sec_ind+ 1
				else:
					end_ind = end_ind - 1

		return self.closure_num

	def get_anagarams_pairs(self, A):
		"""
		Return the set of pairs index values
		@param: A
		@type : list of strings

		@rtype: list of ana_pairs with int

		"""
		if not A:
			return None
		ana_pairs = []
		base_b = {}
		index = 0
		for _index, st1 in enumerate(A):
			# creating the hash model to count each chars
			sort_key =''.join(sorted(st1))
			if sort_key not in base_b:
				# key is not present, we need to add the index on list
				ana_pairs.append([_index+1])
				base_b[sort_key] = index
				index = index + 1
			else:
				# if key is present means, we already had such type of string in data
				# we need to just add the index of second element
				st2 = base_b[sort_key]
				ana_pairs[st2].append(_index+1)

		return ana_pairs

	# need to install the all python dependcies
	def install_dependencies(self, filepath=None):
		"""
		Assume that all dependencies are there in json format in file.
		ex:
			{
				"dependencies": [ "pkg1", "pkg2",...]
			}

		@rtype : bool 
		True if all dependencies are install successfully ow false
		"""
		
		f = filepath if filepath and os.path.exists(filepath) else 'pkg.json'

		with open(f,'r') as _file:
			data = _file.read()

		Dependencies = json.loads(data)
		# get the current python version
		status, version = commands.getstatusoutput("python --version")
		if status:
			return "..unable to get the python version..ERR_MSG:"+str(version)

		failed_pkgs = {}
		PY_VERSION  = "pip" if "python2" in version.lower().replace(' ','') else "pip3"

		for pkg in Dependencies.get('dependencies',{}):
			_pkg_cmd = "{version} install {package}".format(
					version=PY_VERSION,
					package=pkg)
			try:
				status, err_msg = commands.getstatusoutput(_pkg_cmd)
				if status!=0:
					failed_pkgs[pkg] = err_msg
			except Exception as e:
					failed_pkgs[pkg] = e

		if not failed_pkgs:
			return "successfully installed"
		for _pkg, _err in failed_pkgs.iteritems():
			print "**{} package was not install, ERR_MSG: {}**".format(_pkg, str(_err))

		return "..Failed to install some dependencies."







