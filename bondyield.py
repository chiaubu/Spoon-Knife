Python 3.5.0a2 (v3.5.0a2:0337bd7ebcb6+, Mar  9 2015, 10:29:45) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	a = float(input("Enter annual interest: "))
	b = float(input("Enter times interest is paid per year: "))
	pIp = a / b
	c = float(input("Enter discount rate: "))
	rorpp = c / b
	d = float(input("Enter years till maturity: "))
	nopp = d*b
	pva = pIp(1-(1 + rorpp)**-nopp) / rorpp
	e = float(input("Enter face value of bond: "))
	pv = e / (1 + rorpp)**nopp
	sum = pva + pv
	bondYield = 'The present value of interest is {} and present value of principal is {}, present bond yield is {}.'.format(pva, pv, sum)
	print(bondYield)

	
>>> main()
Enter annual interest: 6
Enter times interest is paid per year: 2
Enter discount rate: 5
Enter years till maturity: 10
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "C:\Users\Chiau\AppData\Local\Programs\Python\Python35\lib\idlelib\run.py", line 353, in runcode
    exec(code, self.locals)
  File "<pyshell#3>", line 1, in <module>
  File "<pyshell#2>", line 9, in main
TypeError: 'float' object is not subscriptable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Chiau\AppData\Local\Programs\Python\Python35\lib\idlelib\run.py", line 126, in main
    ret = method(*args, **kwargs)
  File "C:\Users\Chiau\AppData\Local\Programs\Python\Python35\lib\idlelib\run.py", line 365, in runcode
    print_exception()
  File "C:\Users\Chiau\AppData\Local\Programs\Python\Python35\lib\idlelib\run.py", line 216, in print_exception
    print_exc(typ, val, tb)
  File "C:\Users\Chiau\AppData\Local\Programs\Python\Python35\lib\idlelib\run.py", line 211, in print_exc
    traceback.print_list(tbe, file=efile)
  File "C:\Users\Chiau\AppData\Local\Programs\Python\Python35\lib\traceback.py", line 22, in print_list
    for item in StackSummary.from_list(extracted_list).format():
  File "C:\Users\Chiau\AppData\Local\Programs\Python\Python35\lib\traceback.py", line 370, in format
    frame.filename, frame.lineno, frame.name))
AttributeError: 'tuple' object has no attribute 'filename'

>>> ================================ RESTART ================================
>>> 
