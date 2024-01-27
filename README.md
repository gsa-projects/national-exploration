# national-exploration

자연 탐사 활동 중 주제로 정한 `오리 두 마리의 행동으로 난수 생성 알고리즘 만들기` - @rhseung, @selmango

오리의 행동을 영상으로 찍고 편집 프로그램을 통해 트래킹하기 편하도록 마커를 붙인 뒤, cv2로 트래킹하여 위치(좌표) 데이터를 긁었다.

```py
def duckduckgo(t1: float, t2: float, *, factor: int = 11) -> float:
    """
    duck and other duck goes.

    :return: random float in [0, 1)
    """

    y_weight = 3

    r1 = df[df['t'] == t1]
    r2 = df[df['t'] == t2]

    duck1 = np.array([(r1['x1'].item(), r1['y1'].item() * y_weight), (r2['x1'].item(), r2['y1'].item() * y_weight)])
    duck2 = np.array([(r1['x2'].item(), r1['y2'].item() * y_weight), (r2['x2'].item(), r2['y2'].item() * y_weight)])

    delta_duck1 = duck1[1] - duck1[0]
    delta_duck2 = duck2[1] - duck2[0]

    a1, a2 = atan2(delta_duck1[1], delta_duck1[0]), atan2(delta_duck2[1], delta_duck2[0])

    angle = a2 - a1     # -2pi < angle < 2pi

    return ((angle + 2*np.pi) * factor % (2*np.pi)) / (2*np.pi)
```

난수로 사용하기에 출력이 고르지 않아 힘들지만 `factor` 값을 크게 입력하면 쓸만해진다는 결과가 나옴.
