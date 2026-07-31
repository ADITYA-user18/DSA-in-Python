height = [1,8,6,2,5,4,8,3,7]


left = 0
right = len(height)-1
maxi = 0
while left<right:
    width = right-left
    h = min(height[left],height[right])

    area = h*width

    maxi = max(area,maxi)

    if height[left]<height[right]:
        left+=1

    else:
        right-=1


print(maxi)








