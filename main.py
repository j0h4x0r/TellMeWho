import getopt, sys
import infobox
import question

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "k:q:t:f:h", ["help"])
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		usage()
		sys.exit(2)
	opt_dict, mode = check_args(opts)
	api_key = opt_dict['k']
	# run according to mode
	if mode == 1:
		if opt_dict['t'] == 'infobox':
			infobox.main(api_key, opt_dict['q'])
		elif opt_dict['t'] == 'question':
			question.run(api_key, opt_dict['q'])
	elif mode == 2:
		f = open(opt_dict['f'])
		for line in f.readlines():
			line = line.strip('\r\n')
			print 'Query-Question: ' + line + '\n'
			if opt_dict['t'] == 'infobox':
				infobox.main(api_key, line)
			elif opt_dict['t'] == 'question':
				question.run(api_key, line)
			print ''
	elif mode == 3:
		try:
			while True:
				query = raw_input('fb_ibox> ')
				print 'Let me see...'
				if query.startswith('Who created ') or query.startswith('who created '):
					question.run(api_key, query)
				else:
					infobox.main(api_key, query)
		except KeyboardInterrupt:
			sys.exit(0)

def check_args(opts):
	opt_dict = {}
	mode = 0
	for o, v in opts:
		opt_dict[o[1:]] = v
	# help
	if 'h' in opt_dict.keys():
		usage()
		sys.exit(0)
	# must have key
	elif 'k' not in opt_dict.keys():
		print 'Freebase API key must be given'
		usage()
		sys.exit(2)
	elif 't' in opt_dict.keys():
		if 'q' not in opt_dict.keys() and 'f' not in opt_dict.keys():
			print 'Arguments error'
			usage()
			sys.exit(2)
		else:
			if 'q' in opt_dict.keys():
				mode = 1
			elif 'f' in opt_dict.keys():
				mode = 2
	else:
		mode = 3
	return opt_dict, mode

def usage():
	print '''
Usage:
1. -k <account_key> -q <query> -t [infobox|question]
	If the type is infobox (i.e., -t infobox) the system tries to find the most relevant entity to the query <query> and create an infobox about it.
	If the type is question (i.e., -t question), the system tries to answer the question if it is of type "Who created [X]?".
	Note that the query has to be given as a single parameter.
2. -k <account_key> -f <file_with_queries> -t [infobox|question]
	If the type is infobox (i.e. -t infobox) the system reads the file <file_with_queries> and treats each line as a query for infobox creation.
	If the type is question (i.e., -t question), the system treats each line of the <file_with_queris> files as a "Who created [X]?" question and tries to answer it.
	Note that the file name has to be given as a single parameter.
3. -k <account_key>
	A shell is spawned for interactive queries (either for infobox creation or question answering). This functionality is not required for your implementation.
4. --help | -h
	What you see :)
	'''

if __name__ == '__main__':
	main()