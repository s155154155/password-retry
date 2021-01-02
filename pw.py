#密碼的重試程式

password = 'a123456'
cot = 3
while cot > 0:
	cot = cot - 1
	pw = input('請輸入正確密碼 最多可輸入3次')
	if pw == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if cot > 0:
			print('還有', cot,'次機會')
		else:
			print('密碼已鎖住')
