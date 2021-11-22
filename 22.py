def upper(nums,target):# 上确界 找到第一个接近target并且大于=target的值.
    l=0
    r=len(nums)
    mid=0
    while (l<r):
        mid=l+(r-l)//2

        if nums[mid]>=target:
            r=mid
        else:

            l=mid+1


    return l
print(upper([1,4,5,7],3))
print(upper([3,3,3,3],3))
def lower(nums,target):# 下确界=====找到第一个最接近target并且小于等于target的值.
    l=0
    r=len(nums)
    mid=0
    while (l<r):
        mid=l+(r-l)//2
        if nums[mid] == target:  # 如果中间等于target那么我们答案一定在左边.所以r=mid.这里面区间我们用的是左闭右闭
            r=mid
        if l==mid:#防止死循环
            return l
        if nums[mid]<target:  # 如果中间小于target那么答案在mid到r里面.
            l=mid
        else:

            r=mid-1 # mid大于target.那么答案在left到mid-1


    return l
print(lower([3,3,3,3],3))