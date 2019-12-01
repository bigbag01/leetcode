#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
# 两种思路，一种用正则，一种用栈

# @lc code=start
class Solution:
    # 栈的做法
    # Your runtime beats 24.8 % of python3 submissions
    # Your memory usage beats 5.29 % of python3 submissions (13.9 MB)
    # def simplifyPath(self, path: str) -> str:
    #     stack = []
    #     cur_dir = ''
    #     path += '/'
    #     for s in path.split('/'):
    #         if s not in ['','.','..']:
    #             stack.append(s)
    #         elif s == '..' and stack:
    #             stack.pop()
            
    #     simplified_path=''
    #     for directory in stack:
    #         simplified_path += '/'+directory
        
    #     return simplified_path or '/'

    # 正则的做法
    # Your runtime beats 58.74 % of python3 submissions
    # Your memory usage beats 5.29 % of python3 submissions (13.9 MB)
    def simplifyPath(self, path: str) -> str:
        import re
        # 去除所有单个的.出现
        path = re.sub('/','//',path)
        path = re.sub('/\.(/|$)','/',path)

        # 去除重复的/出现
        path = re.sub('[/]+','/',path)

        # 去除目录和..对出现
        l = len(path)
        while True:
            path = re.sub(r'/((?![.]{2})[^/]+)/\.{2}($|[^.])','/',path)
            if len(path)==l:break
            l=len(path)

        #print(path)
        path = re.sub(r'^(/\.{2})+($|/)',r'/',path)
        path = path.strip('/')
        path = '/'+path
        return path 

sol = Solution()
print(sol.simplifyPath("/."))
print(sol.simplifyPath("/home//foo/"))
print(sol.simplifyPath("/a/./b/../../c/"))
print(sol.simplifyPath("/a/../../b/../c//.//"))
print(sol.simplifyPath("/a//b////c/d//././/.."))
print(sol.simplifyPath("/abc/..."))
print(sol.simplifyPath("/../../../../"))
print(sol.simplifyPath("/..hidden"))
print(sol.simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/"))
print(sol.simplifyPath("/.."))
print(sol.simplifyPath("/..."))

# @lc code=end

