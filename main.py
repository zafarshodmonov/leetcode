from p310 import Solution


def main():
    solution = Solution()

    # Input
    n = 4 
    edges = [[1,0],[1,2],[1,3]]

    # Processing
    ans = solution.findMinHeightTrees(n, edges)

    # Output
    print(ans)

if __name__ == "__main__":
    main()
