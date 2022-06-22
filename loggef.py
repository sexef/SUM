



from platform import machine as m

linux=m()
if 'aarch64' in linux:
	import loggef
elif 'arm' in linux:
	import loggef32
else:
	print("only linux is supported on this version")
	input()

