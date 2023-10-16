import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

files = ["bac_GC.tsv", "phages_GC.tsv"]

for file in files:
    file_name = file
    base_name = file_name.split(".")[0]  #para el titulo
    output_name = f"scatter_{base_name}"
    df = pd.read_csv(file_name, sep="\t")

    plt.title(f"scatter {base_name}")
    ax = sns.scatterplot(data=df,
                         x="Length",
                         y="GC",
                         alpha=1,  # transparencia
                         hue="Length",
                         edgecolor="black",
                         palette="cubehelix_r")

    #### Cuantiles

    q1_x = df["Length"].quantile(0.25)
    q3_x = df["Length"].quantile(0.75)
    iqr_x = q3_x - q1_x
    limite_inferior_x = q1_x - 1.5 * iqr_x
    limite_superior_x = q3_x + 1.5 * iqr_x

    q1_y = df["GC"].quantile(0.25)
    q3_y = df["GC"].quantile(0.75)
    iqr_y = q3_y - q1_y
    limite_inferior_y = q1_y - 1.5 * iqr_y
    limite_superior_y = q3_y + 1.5 * iqr_y

    outliers_x = (df["Length"] < limite_inferior_x) | (df["Length"] > limite_superior_x)
    outliers_y = (df["GC"] < limite_inferior_y) | (df["GC"] > limite_superior_y)

    ax.axvline(x=limite_inferior_x,
               color="green",
               linestyle='--',
               linewidth=3,
               label='Límite Inferior (Outlier en X)'
               )

    ax.axvline(x=limite_superior_x,
               color='green',
               linestyle='--',
               linewidth=3,
               label='Límite Superior (Outlier en X)'
               )

    ax.axhline(y=limite_inferior_y,
               color='green',
               linestyle='--',
               linewidth=3,
               label='Límite Inferior (Outlier en Y)'
               )

    ax.axhline(y=limite_superior_y,
               color='green',
               linestyle='--',
               linewidth=3,
               label='Límite Superior (Outlier en Y)'
               )

    plt.savefig(f"{output_name}.jpg", dpi=300, bbox_inches='tight')
    plt.show()

###Histogramas

    sns.histplot(data=df,
                 kde=True,
                 x="GC",
                 binwidth=1,
                 element="step",
                 alpha=0.3,
                 color="maroon",
                 )

    sns.despine()
    plt.title(f"histograma {base_name}")  # sin el guion bajo
    plt.axvline(df["GC"].mean(),
                color="tomato",
                linestyle="--")

    plt.text(x=30, y=300, s=f'mean GC: {df["GC"].mean()}')
    plt.savefig(f"{output_name}.jpg", dpi=600)
    plt.show()

