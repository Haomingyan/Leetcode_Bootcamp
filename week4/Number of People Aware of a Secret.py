class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7

        people = [0] * (n + 1)
        people[1] = 1

        share_count = 0
        total_count = 0

        for day in range(2, n + 1):
            if day - delay >= 1:
                share_count = (share_count + people[day - delay]) % MOD
            if day - forget >= 1:
                share_count = (share_count - people[day - forget] + MOD) % MOD

            people[day] = share_count

        for day in range(n - forget + 1, n + 1):
            total_count = (total_count + people[day]) % MOD

        return total_count
