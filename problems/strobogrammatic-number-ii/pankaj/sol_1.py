class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        d = {'1':'1', '8':'8', '6':'9', '9':'6', '0':'0'}
        dsame = ['0', '1', '8']
        
        allsofar = []
        def gen(cur, upto, sofar):
            # print('gen receieved params : ', cur, upto, sofar)
            if cur == upto:
                for v in sofar:
                    allsofar.append(v)
                return
            else:
                for k in d:
                    gen(cur+1, upto, [item + str(k) for item in sofar])
            
        
        if n == 0:
            return []
        elif n == 1:
            return map(str, dsame)
        else:
            upto = n / 2
            gen(1, upto, sofar = ["1", "8", "6", "9"])
            answerlist = allsofar
            # print('after gen: ', allsofar)
            if n % 2 == 1:
                # append dsame at n/2
                answerlist = [a + option for a in answerlist for option in dsame]
            # print(answerlist, upto)
            final = []
            for a in answerlist:
                # say a = "11"
                y = a
                for i in range(upto - 1, -1, -1):
                    y = y + d[a[i]]
                final.append(y)
            # complete the number via d
            return sorted(final)
