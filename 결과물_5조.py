import time
print("----상명 시네마에 오신것을 환영합니다.----")
time.sleep(0.7)
print()
print("n월 n일자 영화 예매를 하시겠습니까?")
print("Yes / No")
sel1 = input()

if 'Yes' in sel1 or 'yes' in sel1 :
   print("관람을 희망하는 영화를 선택하여 입력해주세요.")
   time.sleep(0.3)
   print()
   print("==듄==")
   print("==베놈2==")
   print("==이터널스==")
   print()
   time.sleep(0.3)
   movie=input("영화 이름 입력: ")

   if '듄' in movie :
      print()
      print("===================================")
      time.sleep(0.3)
      print()
      print("19:10")
      print("20:10")
      print("21:10")
      print()
      time.sleep(0.3)
      while True:
         시간대 = input("원하시는 시간대를 선택하여 입력해주세요:")
         if '19:10' in 시간대 or '20:10' in 시간대 or '21:10' in 시간대 :
            print()
            print(시간대, "시간을 선택하셨습니다.")
            time.sleep(0.3)
            print()
            print("===================================")
            print()
            print("인원 수를 입력해주세요 ")
            adult=int(input("성인 인원수 : "))
            youth=int(input("청소년 인원수 : "))
            kid=int(input("어린이 인원수 : "))
            total=adult+youth+kid

            print()
            time.sleep(0.3)
            print("===================================")
            print()
            print("A1 A2 A3 A4 A5 A6 A7 A8 A9 A10")
            print("B1 B2 B3 B4 B5 B6 B7 B8 B9 B10")
            print("C1 C2 C3 C4 C5 C6 C7 C8 C9 C10")
            print("D1 D2 D3 D4 D5 D6 D7 D8 D9 D10")
            print()
            time.sleep(0.3)
            seat=input("원하시는 좌석을 선택하여 주세요: ")
            seat1=0

            while seat1 < total-1:
               if "A" or "B" or "C" or "D" in seat:
                   seat1+=1
               seat=input("원하시는 좌석을 선택하여 주세요: ")
            print()
            time.sleep(0.3)
            print("좌석 선택이 완료되었습니다.")
            print()
            time.sleep(0.3)

            sum=0
            if adult > 0 :
               sum=adult * 12000
               print("성인", adult,"명", end=" ")

            if youth > 0 :
               sum=sum+(youth * 10000)
               print("청소년", youth,"명", end=" ")

            if kid > 0 :
               sum=sum+(kid * 5000)
               print("어린이", kid,"명", end=" ")

            print ("요금의 합계는", sum,"원입니다.")
            print()
            time.sleep(0.3)
            print("듄", 시간대, "예매가 완료되었습니다.")
            break

         else:
            print()
            time.sleep(0.3)
            print("-시간대를 정확히 입력해주세요.-")
            print()
            time.sleep(0.3)
            continue

   if '베놈2' in movie or '베놈' in movie :
      print()
      print("===================================")
      time.sleep(0.3)
      print()
      print("17:10")
      print("18:10")
      print("19:10")
      print("20:10")
      print()
      time.sleep(0.3)
      while True:
         시간대 = input("원하시는 시간대를 선택하여 입력해주세요:")
         if '17:10' in 시간대 or '18:10' in 시간대 or '19:10' in 시간대 or '20:10' in 시간대 :
            print()
            print(시간대, "시간을 선택하셨습니다.")
            time.sleep(0.3)
            print()
            print("===================================")
            print()
            print("인원 수를 입력해주세요 ")
            adult=int(input("성인 인원수 : "))
            youth=int(input("청소년 인원수 : "))
            kid=int(input("어린이 인원수 : "))
            total=adult+youth+kid

            print()
            time.sleep(0.3)
            print("===================================")
            print()
            print("A1 A2 A3 A4 A5 A6 A7 A8 A9 A10")
            print("B1 B2 B3 B4 B5 B6 B7 B8 B9 B10")
            print("C1 C2 C3 C4 C5 C6 C7 C8 C9 C10")
            print("D1 D2 D3 D4 D5 D6 D7 D8 D9 D10")
            print()
            time.sleep(0.3)
            seat=input("원하시는 좌석을 선택하여 주세요: ")
            seat1=0

            while seat1 < total-1:
                if "A" or "B" or "C" or "D" in seat:
                    seat1+=1
                seat=input("원하시는 좌석을 선택하여 주세요: ")
            print()
            time.sleep(0.3)
            print("좌석 선택이 완료되었습니다.")
            print()
            time.sleep(0.3)

            sum=0
            if adult > 0 :
               sum=adult * 12000
               print("성인", adult,"명", end=" ")

            if youth > 0 :
               sum=sum+(youth * 10000)
               print("청소년", youth,"명", end=" ")

            if kid > 0 :
               sum=sum+(kid * 5000)
               print("어린이", kid,"명", end=" ")

            print ("요금의 합계는", sum,"원입니다.")
            print()
            time.sleep(0.3)
            print("베놈2", 시간대, "예매가 완료되었습니다.")
            break

         else:
            print()
            time.sleep(0.3)
            print("-시간대를 정확히 입력해주세요.-")
            print()
            time.sleep(0.3)
            continue

   if '이터널스' in movie :
      print()
      print("===================================")
      time.sleep(0.3)
      print()
      print("12:10")
      print("17:10")
      print("18:10")
      print("19:10")
      print()
      time.sleep(0.3)
      while True:
         시간대 = input("원하시는 시간대를 선택하여 입력해주세요:")
         if '12:10' in 시간대 or '17:10' in 시간대 or '18:10' in 시간대 or '19:10' in 시간대 :
            print()
            print(시간대, "시간을 선택하셨습니다.")
            time.sleep(0.3)
            print()
            print("===================================")
            print()
            print("인원 수를 입력해주세요 ")
            adult=int(input("성인 인원수 : "))
            youth=int(input("청소년 인원수 : "))
            kid=int(input("어린이 인원수 : "))
            total=adult+youth+kid

            print()
            time.sleep(0.3)
            print("===================================")
            print()
            print("A1 A2 A3 A4 A5 A6 A7 A8 A9 A10")
            print("B1 B2 B3 B4 B5 B6 B7 B8 B9 B10")
            print("C1 C2 C3 C4 C5 C6 C7 C8 C9 C10")
            print("D1 D2 D3 D4 D5 D6 D7 D8 D9 D10")
            print()
            time.sleep(0.3)
            seat=input("원하시는 좌석을 선택하여 주세요: ")
            seat1=0

            while seat1 < total-1:
                if "A" or "B" or "C" or "D" in seat:
                    seat1+=1
                seat=input("원하시는 좌석을 선택하여 주세요: ")
            print()
            time.sleep(0.3)
            print("좌석 선택이 완료되었습니다.")
            print()
            time.sleep(0.3)

            sum=0
            if adult > 0 :
               sum=adult * 12000
               print("성인", adult,"명", end=" ")

            if youth > 0 :
               sum=sum+(youth * 10000)
               print("청소년", youth,"명", end=" ")

            if kid > 0 :
               sum=sum+(kid * 5000)
               print("어린이", kid,"명", end=" ")

            print ("요금의 합계는", sum,"원입니다.")
            print()
            time.sleep(0.3)
            print("이터널스", 시간대, "예매가 완료되었습니다.")
            break

         else:
            print()
            time.sleep(0.3)
            print("-시간대를 정확히 입력해주세요.-")
            print()
            time.sleep(0.3)
            continue
            
elif 'No' in sel1 or 'no' in sel1 :
   print("프로그램을 종료합니다.")
