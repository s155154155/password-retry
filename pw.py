#密碼重試程式

password = 'a123456'
cot = 3
while True:
	pw = input('請輸入正確密碼 最多可輸入3次')
	if pw == password:
		print('登入成功')
		break
	else:
		cot = cot - 1
		print('密碼錯誤還有', cot,'次機會')
		if cot == 0:
			break

