piimport matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25, 36]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# names and fonsize
ax.set_title("Square numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square value", fontsize=14)

# labels fontsize
ax.tick_params(axis='both', labelsize=14)

plt.show()
