class Solution:

    def getSubstrLength(self, visited):
        length = 0
        for key in visited:
            if visited[key] != None:
                length += 1

        return length

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        visited = {}

        for i in range(len(s)):
            if s[i] not in visited \
            or visited[s[i]] == None:
                visited[s[i]] = i
            
            else:
                length = self.getSubstrLength(visited)

                if (length > max_length):
                    max_length = length 
                
                for key in visited:
                    if visited[key] != None \
                    and visited[key] < visited[s[i]]:
                        visited[key] = None

                visited[s[i]] = i  


        length = self.getSubstrLength(visited)
        
        if length > max_length:
            max_length = length


        return max_length