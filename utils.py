# 이미지 내의 문자 형태가 거의 동일하므로, 데이터를 조금만 수집해도 됨
# 가능한 12개의 문자 : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, -, x
# 색상 추출기를 활용하여, 각 문자의 색상이 어떻게 구성되어 있는지 확인
# 파란색 : RGB에서 B값이 항상 FF
# 초록색 : RGB에서 G값이 항상 FF
# 빨간색 : RGB에서 R값이 항상 FF
# 파란색 & 초록색 : RGB에서 R값이 항상 AA 이하
# 파란색 & 빨간색 : RGB에서 G값이 항상 AA 이하
# 초록색 & 빨간색 : RGB에서 B값이 항상 AA 이하