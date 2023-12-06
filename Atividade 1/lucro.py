def maximum_profit(days, cost_per_day, revenues):
    max_profit = 0
    for i in range(days):
        for j in range(i, days):
            total_revenue = sum(revenues[i:j+1])
            total_cost = cost_per_day * (j - i + 1)
            max_profit = max(max_profit, total_revenue - total_cost)
    return max_profit

def main():
    while True:
        try:
            days = int(input())
            if days == 0:
                break
            cost_per_day = int(input())
            revenues = [int(input()) for _ in range(days)]
            result = maximum_profit(days, cost_per_day, revenues)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()
