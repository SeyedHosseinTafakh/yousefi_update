# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:11:06 2020

@author: Hossein
"""



from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in nums:
            new_list.append(i*2)
        new_list=new_list.sort()
        return new_list
    

productExceptSelf()

