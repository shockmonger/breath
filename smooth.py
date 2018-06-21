import numpy

def smooth(x,window_len=11,window='hanning'):
	if x.ndim != 1:
		raise ValueError, 'only 1d smooth'

	if x.size < window_len:
		raise ValueError, 'input vec needs to be bigger than widow size'

	if window_len < 3:
		return x

	if not window in ['flat','hanning','hamming','bartlett','blackman']:
		raise ValueError, 'Windiw is not of recognizable type'

	s = numpy.r_[x[window_len-1:0:-1],x,x[-2:window_len-1:-1]]
	if window == 'flat':
		w = numpy.ones(window_len,'d')
	else:
		w=eval('numpy.'+window+'(window_len)')

	y = numpy.convolve(w/w.sum(),s,mode = 'valid')
	return y