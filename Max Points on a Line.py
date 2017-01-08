# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        self.points = points
        ans = 0
        dict = {}
        for i in range(len(points)):
            horz = same = 0
            dict.clear()
            for j in range(len(points)):
                if  points[j].x == points[i].x and points[j].y == points[i].y :
                    same = same + 1
                elif points[j].x == points[i].x :
                    horz = horz + 1
                else:
                    dict[(points[j].y - points[i].y) / (points[j].x - points[i].x)] += 1

            
            
            if horz + same > ans:

                ans = horz + same 

            for x in dict.keys():

                if dict[x] + same > ans:
                    ans = dict[x] + same
                
        return ans
