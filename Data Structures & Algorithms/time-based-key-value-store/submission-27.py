class TimeMap:

    def __init__(self):
        self.dict_ = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict_:
            self.dict_[key] = []  
        self.dict_[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dict_:
            pairs = self.dict_[key]
            result = ""

            left = 0 
            mid = 0 
            right = len(pairs) -1

            while left <= right:
                mid = (left+right) // 2
                # print(f"Dhukse key={key} time={timestamp} left={left}; right={right}")
                if pairs[mid][0] <= timestamp:
                    result = pairs[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result

        return ''