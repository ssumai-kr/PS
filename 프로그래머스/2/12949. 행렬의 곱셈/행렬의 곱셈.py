def solution(arr1, arr2):
    n, m, p = len(arr1), len(arr2), len(arr2[0])
    answer = [[0] * p for _ in range(n)]       # 결과: n행 p열
    for i in range(n):                          # arr1의 i번째 행
        for j in range(p):                      # arr2의 j번째 열
            for k in range(m):                  # 같은 위치끼리 곱해서 더하기
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer