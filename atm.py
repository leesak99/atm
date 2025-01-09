#출금 요청한 금액을 받는 변수 : withdraw_amount
#출금을 요청한 금액을 balance 변수에서 뺀 결과가 들어가도록 코드를 작성해주세요
#영수증에 다음 순서로 값이 들어가도록 코드를 만들어주세요 -> ()"출금", withdraw_amount, balance)) 순으로 데이터를 넣어주세요
#가지고 있는 금액보다 출금을 원하는 금액 클때 가지고 있는 금액만 출금되도록 코드를 작성해주세요
#단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될때마다 이력이 기록됩니다.
#영수증 변수는 : recipts
## 입력 검증 및 에러 처리추가
## 잘못된 입력 값 (숫자가 아닌값, 음수 값 등) 처리하도록 기능추가하기
## 유효하지 않은 메뉴선택 시 경고 메세지 또는 사용방법 재안내를 해주세요 (if문에 조건문달기)
receipts =[] # []대괄호 : list / {key:value}중괄호 : dick / () : tuple
balance = 3000  #현재 잔액을 보여주세요

while True:
    print()
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 4:종료)")
    if num == '4':
        break
    if num == "1":
        deposit_amount = int(input("입금할 금액을 입력해주세요 : ")) #input() 내장함수 / int() : 저수형을 데이터로 형변환해주는 내장함수()
        balance = balance + deposit_amount # balance += deposit_amount
        receipts.append(("입금", deposit_amount, balance))
        print(f"입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.")
    if num == "2" :
        withdraw_amount = int(input("출금할 금액을 입력해주세요 : ")) #2000
        withdraw_amount = min(balance, withdraw_amount) 
        balance -= withdraw_amount 
        receipts.append(("출금", withdraw_amount, balance))
        print(f"출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.")

print(f"서비스를 종료합니다.현재 잔액1은{balance}원입니다.")




    