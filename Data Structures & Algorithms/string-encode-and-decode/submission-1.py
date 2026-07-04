class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = [len(x) for x in strs]
        final_str = ""
        count = 0
        
        for i in lengths:
            final_str += str(i) + ","
        final_str = final_str.removesuffix(",")
        final_str += ":"
        for i in strs:
            final_str += i
        return final_str
        
    def decode(self, s: str) -> List[str]:
        if s == ":":
            return []
        splitter = s.index(":")
        formatter = s[:splitter]

        s = s[splitter+1:]
        
        formatter = [int(x) for x in formatter.split(",")]

        results = []
        start_string = 0
        stop_string = 0
        
        for i in formatter:
            stop_string += i
            results.append(s[start_string:stop_string])
            start_string = stop_string
        

        return results