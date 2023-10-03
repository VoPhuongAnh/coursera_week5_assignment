# start = 2 (không bắt buộc), stop = 10 (bắt buộc), step = 1 (không bắt buộc)
# for i in range(2,10,1):
#     print(i)

# gọi i là indẽ của từng indice trong chuỗi s. Cho i chạy từ đầu đến cuối chuỗi. Xác định stop bằng độ dài chuỗi.
s = 'welcome to the hell'
for i in range(0,len(s),1):
    print('index', i , '=', s[i])
