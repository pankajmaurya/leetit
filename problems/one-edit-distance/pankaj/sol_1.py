class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def isSame(a, b):
            return a == b
        # len difference of 2 or more => edit distance is more than 1.
        if abs(len(s) - len(t)) > 1:
            return False
        
        # insert
        # delete
        # replace
        
        if s == "" and t == "":
            return False
        
        if s == "" and len(t) == 1 or t == "" and len(s) == 1:
            return True
        
        if s[0] == t[0]:
            return self.isOneEditDistance(s[1:], t[1:])
        else:
            # either do insert 
            insertCase = isSame(s, t[1:])
            deleteCase = isSame(s[1:], t)
            replaceCase = isSame(s[1:], t[1:])
            return insertCase or deleteCase or replaceCase
