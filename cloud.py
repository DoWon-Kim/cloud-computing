import boto3
import sys
import pprint

def menu():             #amazon ec2 관리 메뉴 함수
    while True:
        print("-------------------------------------------------")
        print("1. list instance           2. available zone")
        print("3. start instance          4. available regions")
        print("5. stop instance           6. create instance")
        print("7. reboot instance         8. list images")
        print("9.                         99. quit")
        print("-------------------------------------------------")
        number = input("번호를 입력하세요:")
        if number == "1":       #1.인스터스 목록
            print("list instance..")
            list_instance()
        elif number == "2":     #2.이용가능한 존 목록
            print("available zone..")
            available_zones()
        elif number == "3":     #3.인스턴스 실행
            print("start instance..")
            start_instance()
        elif number == "4":     #4.이용가능한 지역 목록
            print("available regions..")
            available_regions()
        elif number == "5":     #5.인스턴스 중지
            print("stop instance..")
            stop_instance()
        elif number == "6":     #6.인스턴스 생성
            print("create instance..")
            creat_instance()
        elif number == "7":     #7.인스턴스 재실행
            print("reboot instnace..")
            reboot_instance()
        elif number == "8":     #9.이미지 목록
            print("list images..")
            list_images()
        elif number == "9":
            print("준비중입니다.")
        elif number == "99":    #99.종료
            print("종료합니다.")
            sys.exit()
        else:
            print("다시 입력하세요.")

def list_instance():
    print("준비중입니다.")
def available_zones():
    print("준비중입니다.")
def start_instance():
    print("준비중입니다.")
def available_regions():
    print("준비중입니다.")
def stop_instance():
    print("준비중입니다.")
def creat_instance():
    print("준비중입니다.")
def reboot_instance():
    print("준비중입니다.")
def list_images():
    print("준비중입니다.")

if __name__=='__main__':
    menu()