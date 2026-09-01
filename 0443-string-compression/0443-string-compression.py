class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)

        while read < n:
            element = chars[read]
            count = 0

            while read < n and chars[read] == element:
                read += 1
                count += 1

            chars[write] = element
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write