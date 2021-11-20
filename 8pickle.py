import pickle
#파일에 정보를 기록, b는 바이너리
# profile_file = open("profile.pickle","wb")
# profile = {"이름": "박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# #profile에 있는 정보를 파일에 저장
# pickle.dump(profile, profile_file)
# profile_file.close()

#파일에 있는 정보를 읽기
profile_file = open("profile.pickle","rb")
 #file에 있는 정보를 profile로 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close
