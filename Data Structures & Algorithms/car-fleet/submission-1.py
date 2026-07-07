class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - position[x])/speed[x] for x in range(len(position))]
        indicies = sorted(range(len(time)), key=lambda x:position[x])
        time = [time[x] for x in indicies]
        print(time)
        cur_min = 0
        total_fleets = 0
        for i in range(len(time)-1,-1,-1):
            if time[i] > cur_min:
                total_fleets += 1
                cur_min = time[i]
        return total_fleets