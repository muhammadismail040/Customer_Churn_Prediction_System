import matplotlib.pyplot as plt
import seaborn as sns


def plot_count(data, column):

    plt.figure(figsize=(8,5))

    sns.countplot(
        data=data,
        x=column
    )

    plt.title(column)

    plt.show()