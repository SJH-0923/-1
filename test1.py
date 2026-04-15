'''
str3 = input("3개의 숫자를 입력하세요.").split() #스페이스 바로 구분
istr3 = int(str3[0]) #int는 리스트 변환 못 시킴
#istr3 = list(map(int,str3))
print(istr3)
'''

a, b, c = map(int, input("세 개의 숫자를 입력하세요. :").split())
print(a, b, c)

#split은 문자열에 속한 함수
#"1,2,3".split() ---> 이것도 됨
