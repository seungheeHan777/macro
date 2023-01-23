import pyautogui

# 마우스 현재 위치 좌표를 알아내는 명령어
pyautogui.position()

# 마우스를 지정한 죄표로 이동하게 한다. (x,y,time) 
# time은 몇 초간 이동해서 그 좌표에 도달하게 하는 명령어

pyautogui.moveTo(487,359,2)

# moveRel은 현재 마우스 좌표 위치에서 변수값만큼 이동하는 것이다.
pyautogui.moveRel(487,0,2)

# 마우스 클릭

pyautogui.click()

# 마우스 더블 클릭

pyautogui.click(clicks=2)
pyautogui.doubleClick()
pyautogui.click(clicks=2,interval=2)    # 클릭을 하는 간격을 n초간 둔다

# 키보드 타이핑 입력

pyautogui.typewrite('Hi HAHAHHAHAAHAHAHA')

# 키보드 키 입력
# typewrite 사이에 []를 넣어서 키보드 키를 적으면 키보드 키가 자동 입력됨
pyautogui.typewrite(['enter'])
pyautogui.typewrite(['a','b','enter'])  # 이러면 a b 엔터가 입력
pyautogui.typewrite(['ab','enter'])     # 이러면 엔터만 입력됨, ab란 키는 키보드에 없으니까
