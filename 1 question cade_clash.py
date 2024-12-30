# The Innovative Synergy Organization (ISO) focuses on efficiently organizing team schedules to enhance collaboration and reduce downtime between employees from different teams. The organization consists of n teams, each with 2 members. Members of the same team, identified as (i, 1) and (i, 2) for team i, work seamlessly regardless of whether they meet in the office. However, collaboration between members of different teams requires in-person meetings.
def sm(n, w):
    if w < n - 1:
        print("infinity")
        return

    schedule = []
    for i in range(w):
        week = []
        for j in range(n):
            week.append('1' if (i + j) % 2 == 0 else '2')
        schedule.append("".join(week))

    isolation = (w - 1) // (n - 1)

    print(isolation)
    for week in schedule:
        print(week)

n, w = map(int, input().split())
sm(n, w)
