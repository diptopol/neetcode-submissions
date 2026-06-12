class Solution:

    def encode(self, strs: List[str]) -> str:
        if  len(strs) == 0:
            return "DIPTOPOLEMPTY"

        encoded: str = ""
        for idx, s in enumerate(strs):
            encoded += s

            if (idx < len(strs) - 1): 
                encoded += "DIPTOPOL"

        return encoded


    def decode(self, s: str) -> List[str]:
        if s == "DIPTOPOLEMPTY":
            return []
        else:
            return s.split("DIPTOPOL")

               
