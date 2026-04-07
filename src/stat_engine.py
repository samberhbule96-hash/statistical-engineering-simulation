import math
from typing import List, Union, Any, Dict

class StatEngine:
    def __init__(self, raw_data: List[Any]):
        """Clean data and handle mixed types/empty arrays (Slide 13/25)."""
        self.data = []
        for item in raw_data:
            try:
                if item is not None:
                    self.data.append(float(item))
            except (ValueError, TypeError):
                continue
        
        if not self.data:
            raise ValueError("StatEngine Error: No valid numeric data found.")

    def get_mean(self) -> float:
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        s = sorted(self.data)
        n = len(s)
        mid = n // 2
        return (s[mid-1] + s[mid]) / 2.0 if n % 2 == 0 else float(s[mid])

    def get_mode(self) -> Union[List[float], str]:
        counts = {}
        for x in self.data:
            counts[x] = counts.get(x, 0) + 1
        
        max_f = max(counts.values())
        if max_f == 1 and len(self.data) > 1:
            return "Specific Message: All values are unique; no mode exists."
        
        return sorted([k for k, v in counts.items() if v == max_f])

    def get_variance(self, is_sample: bool = True) -> float:
        n = len(self.data)
        if is_sample and n <= 1:
            raise ZeroDivisionError("Sample variance requires n > 1 (Bessel's Correction).")
        
        mu = self.get_mean()
        sq_diff = sum((x - mu)**2 for x in self.data)
        return sq_diff / (n - 1 if is_sample else n)

    def get_standard_deviation(self, is_sample: bool = True) -> float:
        return math.sqrt(self.get_variance(is_sample))

    def get_outliers(self, threshold: float = 2.0) -> List[float]:
        mu = self.get_mean()
        sigma = self.get_standard_deviation(is_sample=True)
        return [x for x in self.data if abs(x - mu) > (threshold * sigma)]
