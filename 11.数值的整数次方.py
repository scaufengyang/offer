def Power(base,exponent):
	if exponent == 0:
		return 1
	if exponent == 1:
		return base
	if exponent == -1:
		return 1/base

	result = Power(base,exponent>>1)
	result *= result
	if(exponent & 0x1) == 1:
		result *= base
	return result
