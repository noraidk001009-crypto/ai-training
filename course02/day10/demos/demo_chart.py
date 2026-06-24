import matplotlib.pyplot as plt

labels = ["fight", "defend", "poison"]
values = [8, 3, 2]
plt.bar(labels, values, color=["#2E86AB", "#28A745", "#6F42C1"])
plt.ylabel("Times used")
plt.title("Commands in sample fights")
plt.tight_layout()
plt.savefig("win_chart.png")
print("Saved win_chart.png")
