# User function Template for python3

class Solution:
    def countSpecialNumbers(self, N, arr):

        # Code here

        m = max(arr)
        freq = [0 for _ in range(m + 1)]
        for i in arr:
            if freq[i] <= 1:
                for j in range(i, m + 1, i):
                    freq[j] += 1
        count = sum(1 for i in arr if freq[i] > 1)
        return count


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        N = int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))

        T -= 1
# } Driver Code Ends