while True:
	try:
		a = int(input('請輸入第一位數字：'))
		b = int(input('請輸入第二位數字：'))
		c = int(input('請選擇何種運算符號？\n1.加, 2.減, 3.乘, 4.除'))
		if c == 1:
			print('{} 和 {} 相加後的答案為：{}'.format(a, b, a+b))
			d = input('要繼續嗎？按Q離開')
			if d == 'q' or d == 'Q':
				break
		elif c == 2:
			print('{} 和 {} 相減後的答案為：{}'.format(a, b, a-b))
			d = input('要繼續嗎？按Q離開')
			if d == 'q' or d == 'Q':
				break
		elif c == 3:
			print('{} 和 {} 相乘後的答案為：{}'.format(a, b, a*b))
			d = input('要繼續嗎？按Q離開')
			if d == 'q' or d == 'Q':
				break
		elif c == 4:
			print('{} 和 {} 相除後的答案為：{}'.format(a, b, a/b))
			d = input('要繼續嗎？按Q離開')
			if d == 'q' or d == 'Q':
				break
		else:
			print('輸入錯誤')
	except ValueError:
		print("輸入格式有誤")
	except:
		print("程式出現其它異常")