import pandas as pd

def shortestDist(points):
        sh = float("inf")
        for i in range(1, len(points)):
                d = dist(points[i-1], points[i])
                if d < sh:
                        sh = d
        return sh