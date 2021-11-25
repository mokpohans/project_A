import pandas as pd
#github에 저장되어있는 csv파일을 불러오는 코드
Testdata = pd.read_csv('https://media.githubusercontent.com/media/mokpohans/project_A/master/CSV/%ED%95%9C%EA%B5%AD%EC%A7%80%EC%97%AD%EB%82%9C%EB%B0%A9%EA%B3%B5%EC%82%AC_%EC%9D%B8%EB%B2%84%ED%84%B0%EB%B3%84%20%EB%B6%84%EB%8B%A8%EC%9C%84%20%ED%83%9C%EC%96%91%EA%B4%91%EB%B0%9C%EC%A0%84%20%EC%A0%95%EB%B3%B4_20210831.csv', encoding='CP949')

#CSV파일에서 장소 열에서 발전소 위치를 중복없이 리스트로 만드는 코드
place = Testdata.장소
place_list = ['정선한교']
count_list=0
for i in place:
    if place_list[count_list] == i:
        pass
    else:
        print(i)
        count_list= count_list + 1
        place_list.insert(count_list,i)

print(place_list)

