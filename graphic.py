import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import FuncFormatter
from pywaffle import Waffle


def create_bars_for_depression_groups(
        depression_groups,
        colors=("#318a8e", "#21721e", "#b2b217", "#6e1c77", "#8c0b3c")
):
    colors_bar = list(colors)

    fig, (ax_1, ax_2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7.5))
    ax_1.bar(
        x="Do not have Major Depression",
        height=depression_groups.values[0],
        color=colors_bar[0]
    )
    ax_1.bar(
        x="Do not have Major Depression",
        height=depression_groups.values[1],
        color=colors_bar[1],
        bottom=depression_groups.values[0]
    )

    for i, x_label in enumerate(depression_groups.index[2:], start=2):
        bottom = 0 if i <= 2 else sum(depression_groups.values[2:i])
        ax_1.bar(
            x="Have Major Depression",
            height=depression_groups.values[i],
            color=colors_bar[i],
            bottom=bottom
        )

    rect_not_depressed = ax_1.patches[:2]
    rect_depressed = ax_1.patches[2:]
    height_depr = sum([x.get_height() for x in rect_depressed])
    width_depr = rect_depressed[0].get_width()
    height_not_depr = sum([x.get_height() for x in rect_not_depressed])
    width_not_depr = rect_not_depressed[0].get_width()
    x_depr = rect_depressed[0].get_x()
    x_not_depr = rect_not_depressed[0].get_x()
    percentage_depr = np.round(height_depr / (height_depr + height_not_depr) * 100, 2)
    percentage_not_depr = np.round(height_not_depr / (height_depr + height_not_depr) * 100, 2)

    ax_1.text(
        x_not_depr + (width_not_depr / 2),
        height_not_depr - 100,
        f"{percentage_not_depr}%",
        ha='center',
        va='top',
        c="black",
        fontsize=24
    )
    ax_1.text(
        x_depr + (width_depr / 2),
        height_depr - 250,
        f"{percentage_depr}%",
        ha="center",
        va="bottom",
        c="black",
        fontsize=24
    )

    ax_1.set_xlabel("Depression", fontsize=14)
    ax_1.set_ylabel("Number of Surveyed", fontsize=14)
    ax_1.set_title("Number of Surveyed suffering from major depression", fontsize=16)
    ax_1.legend(depression_groups.index, loc="best", title="Depression level\n")

    for i, x_label in enumerate(depression_groups.index[1:], start=1):
        ax_2.bar(x="\n".join(x_label.split(" ")), height=depression_groups.values[i],
                 color=colors_bar[i])

    ax_2.set_xlabel("Depression Level", fontsize=14)
    ax_2.set_ylabel("Number of Surveyed", fontsize=14)
    ax_2.set_title("People with different depression level", fontsize=16)

    rects = ax_2.patches

    for rect, label in zip(rects, map(lambda x: int(x), depression_groups.values[1:])):
        height = rect.get_height()
        ax_2.text(
            rect.get_x() + rect.get_width() / 2,
            height - 0.5, label,
            ha='center',
            va='bottom',
            c="white"
        )


GROUP_BAR_COEFF = {0: -1, 1: 0, 2: 1, 3: -2, 4: 2, 5: 3, 6: -3}


def create_grouped_bars(
        *args, bar_width, xlabel, ylabel,
        colors=("#998c8c", "#a03b60", "#307899"),
        labels=("Total", "Female", "Male"),
        figsize=(8, 5)
):
    index = np.arange(len(args[0].values))
    # plt.figure(figsize=figsize)

    fig, ax = plt.subplots(1, 1, figsize=figsize)

    for i, depr_df in enumerate(args):
        plt.bar(
            index + bar_width * GROUP_BAR_COEFF[i],
            depr_df[True].values,
            width=bar_width,
            label=labels[i],
            color=colors[i]
        )

    rects = ax.patches
    values = []

    for values_array in args:
        for value in values_array[True].values:
            values.append(value)

    height_diff = 0.07 * max(values)

    for rect, label in zip(rects, map(lambda x: np.round(x, 1), values)):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            height - height_diff,
            label,
            ha='center',
            va='bottom',
            c="white"
        )

    plt.xticks(index, list(args[0][True].index), fontsize=12)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.tight_layout()
    plt.legend()


def create_race_bars(races_age, races):
    index = np.arange(races_age.shape[1]) + 1
    index_l = np.arange(races_age.shape[1] + 1)
    bar_width = 0.16
    color_map = {
        "Mexican American": "#a56017", "Non-Hispanic Asian": "#b5ad5e",
        "Non-Hispanic Black": "#7f3805", "Non-Hispanic White": "#c9a199",
        "Other Hispanic": "#b57d4c", "Other Race - Including Multi-Racial": "#679376"
    }
    fig, ax = plt.subplots(1, 1, figsize=(14, 6))

    for i, value in enumerate(races[True]):
        race = races.index[i]
        plt.bar(
            x=bar_width * GROUP_BAR_COEFF[i],
            height=value,
            width=bar_width,
            color=color_map[race]
        )

    for i, race in enumerate(races_age.index):
        plt.bar(
            x=index + bar_width * GROUP_BAR_COEFF[i],
            height=races_age.loc[race, :],
            width=bar_width,
            color=color_map[race],
            label=race
        )

    rects = ax.patches
    races_values = []
    for i in [races_age.loc[index, :].values for index in races_age.index]:
        for j in i:
            races_values.append(j)

    values = [*races[True], *races_values]
    for rect, label in zip(rects, map(lambda x: np.round(x, 1), values)):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            height - 1.,
            label,
            ha='center',
            va='bottom',
            c="white"
        )

    plt.xticks(index_l, ["Total", *list(races_age.columns)], fontsize=14)
    plt.xlabel("Age group", fontsize=16)
    plt.ylabel("Percentage of depressed people", fontsize=16)
    plt.title("People with Major Depression over different races")
    plt.legend()


def create_income_bars(income_race, income_total):
    index = np.arange(income_race.shape[1]) + 1
    index_l = np.arange(income_race.shape[1] + 1)
    bar_width = 0.2
    color_map = {
        "$1649 and less": "#318a8e",
        "\\$1650-\\$4599": "#21721e",
        "$4600 and above": "#6b3414",
    }
    fig, ax = plt.subplots(1, 1, figsize=(14, 6))

    for i, value in enumerate(income_total[True]):
        race = income_total.index[i]
        ax.bar(
            x=bar_width * GROUP_BAR_COEFF[i],
            height=value,
            width=bar_width,
            color=color_map[race]
        )

    for i, race in enumerate(income_race.index):
        ax.bar(
            x=index + bar_width * GROUP_BAR_COEFF[i],
            height=income_race.loc[race, :],
            width=bar_width,
            color=color_map[race],
            label=race
        )

    rects = ax.patches
    income_race_values = []

    for i in [income_race.loc[index, :].values for index in income_race.index]:
        for j in i:
            income_race_values.append(j)

    values = [*income_total[True], *income_race_values]
    for rect, label in zip(rects, map(lambda x: np.round(x, 1), values)):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            height - 1.5,
            label,
            ha='center',
            va='bottom',
            c="white"
        )

    plt.xticks(index_l, ["Total", *list(income_race.columns)], fontsize=10)
    plt.xlabel("Race", fontsize=16)
    plt.ylabel("Percentage of depressed people", fontsize=16)
    plt.title(
        "Percentage of depressed people over different races and family incom groups",
        fontsize=18
    )
    plt.legend(title="Income group\n")


COLORS_LEVEL_MAP = {"Do not have Major Depression": "#73c66b", "Have Major Depression": "#e24480"}
COLORS_LEVEL_MAP_2 = {"Not depressed": "#73c66b", "Mild": "#83cfd1", "Moderate": "#886fe2",
                      "Moderately Severe": "#d469e0", "Severe": "#e24480"}


def create_subbar(axi, title, x_labels, height):
    axi.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x)}%"))
    axi.set_title(title)
    axi.yaxis.grid(True, linestyle="--", color="0.3")

    for i, x_label in enumerate(x_labels):
        axi.bar(x=x_label, height=height[i], color=COLORS_LEVEL_MAP[x_label])


def create_waffle(title, x_labels, x_values, size):
    data = dict(zip(x_labels, x_values))
    return plt.figure(
        FigureClass=Waffle,
        rows=5,
        values=data,
        colors=("#318a8e", "#21721e", "#b2b217", "#6e1c77", "#8c0b3c"),
        title={'label': title, 'loc': 'left'},
        labels=[f"{k} ({v}%)" for k, v in data.items()],
        legend={'loc': 'upper left', 'bbox_to_anchor': (1.1, 1)},
        figsize=size,
    )


def create_drugs_bars(rehab_2_perc, tried_drugs_2_perc):
    index = np.arange(2)
    fig = plt.figure(figsize=(8, 5))
    bar_1 = [rehab_2_perc[True].values[0], tried_drugs_2_perc[True].values[0]]
    bar_2 = [rehab_2_perc[True].values[1], tried_drugs_2_perc[True].values[1]]
    plt.bar(index, bar_1, width=0.2, color="#8c0b3c", label="Yes")
    plt.bar(index + 0.2, bar_2, width=0.2, color="#318a8e", label="No")
    plt.xticks(index + 0.1, ["Were on Rehabilitation", "Tried cocaine/heroin/methamphetamine"])
    plt.ylabel("Percentage of surveyed with major depression", fontsize=14)
    plt.title("Comparison of different drug usage features with \nMajor Depression", fontsize=16)
    plt.legend()
    plt.show()


def create_drugs_waffles(rehab, rehab_perc, tried_drugs_perc):
    x_labels_2 = rehab.columns.values
    title_rehab_2 = "Surveyed drug rehabed percentage grouped with level of depression"
    percentages_rehab_2 = np.round(rehab_perc[rehab_perc.index == 1].values[0] - .005, 2)

    title_tried_drugs_2 = "Surveyed who ever used cocaine/heroin/methamphetamine percentage grouped with depression level"
    percentages_tried_drugs_2 = np.round(
        tried_drugs_perc[tried_drugs_perc.index == 1].values[0], 2
    )

    create_waffle(
        title=title_rehab_2, x_labels=x_labels_2, x_values=percentages_rehab_2, size=(12, 5)
    )
    create_waffle(
        title=title_tried_drugs_2,
        x_labels=x_labels_2,
        x_values=percentages_tried_drugs_2,
        size=(12, 7)
    )


def create_edu_distplots(high_school_ed, college_ed, univers_ed):
    fig = plt.figure(figsize=(14, 10))
    plt.subplot(2, 2, 1)
    sns.distplot(high_school_ed, hist_kws={"linewidth": 3, "alpha": 0.5})
    ax = sns.distplot(college_ed, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "#8c0b3c"})
    ax.set(xlabel='Family Income')
    plt.legend(["High school graduate/GED or equivalent", "Some college or AA degree"])

    plt.subplot(2, 2, 2)
    sns.distplot(high_school_ed, hist_kws={"linewidth": 3, "alpha": 0.5})
    ax = sns.distplot(univers_ed, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "#21721e"})
    ax.set(xlabel='Family Income')
    plt.legend(["High school graduate/GED or equivalent", "College graduate or above"])

    plt.subplot(2, 2, 3)
    sns.distplot(college_ed, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "#8c0b3c"})
    ax = sns.distplot(univers_ed, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "#21721e"})
    ax.set(xlabel='Family Income')
    plt.legend(["Some college or AA degree", "College graduate or above"])

    plt.subplot(2, 2, 4)
    sns.distplot(high_school_ed, hist_kws={"linewidth": 3, "alpha": 0.5})
    sns.distplot(college_ed, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "#8c0b3c"})
    ax = sns.distplot(univers_ed, hist_kws={"linewidth": 3, "alpha": 0.5, "color": "#21721e"})
    ax.set(xlabel='Family Income')
    plt.legend([
        "High school graduate/GED or equivalent",
        "Some college or AA degree",
        "College graduate or above"
    ])

    fig.suptitle("Correlation between Education level and Family Income", fontsize=16)


def create_alco_bars(alco_depression_crosstable_perc):
    ticks = ["1-3 /year", "< 1 /mo", "1 /mo", "2-3 /mo", "1 /week", "2-3 /week", "3+ /week"]
    index = np.arange(7)
    plt.figure(figsize=(9, 6))
    plt.bar(index, alco_depression_crosstable_perc[True], color="#8c0b3c")
    plt.xticks(index, ticks, fontsize=11)
    plt.ylabel("Percentage of surveyed with Major Depression", fontsize=14, )
    plt.xlabel("Times per interval surveyed drink", fontsize=14)
    plt.title("Percentage of People with Major Depression over \ndifferent Alcohol Use groups",
              fontsize=16)
    plt.show()


def create_dist_health(health_dep):
    # Slicing the data set by depression bins for seperate graphs
    a1 = health_dep.iloc[np.where(health_dep['DPQGR'] == 'Not Depressed')]
    a2 = health_dep.iloc[np.where(health_dep['DPQGR'] == 'Mild')]
    a3 = health_dep.iloc[np.where(health_dep['DPQGR'] == 'Moderate')]
    a4 = health_dep.iloc[np.where(health_dep['DPQGR'] == 'Moderately Severe')]
    a5 = health_dep.iloc[np.where(health_dep['DPQGR'] == 'Severe')]

    # Define plot size as 1x5, with a figure size and forcing the graphs to share y axis for ez comparison
    fig, (a1g, a2g, a3g, a4g, a5g) = plt.subplots(1, 5, figsize=(20, 6), sharey='row')
    fig.suptitle("Distribution of people's health across depression groups", fontsize=20)

    a1g = sns.barplot(x=a1['health'], y=a1['Percentage'], data=a1, ax=a1g,
                      order=("Excellent", "Fair", "Very good", "Good", "Poor"))
    a1g.set_title('Not depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a1g.get_xticklabels():
        item.set_rotation(90)
    a1g.set_ylabel('Percentage')
    a1g.set_xlabel('Health')

    a2g = sns.barplot(x=a2['health'], y=a2['Percentage'], data=a2, ax=a2g,
                      order=("Excellent", "Fair", "Very good", "Good", "Poor"))
    a2g.set_title('Mildly depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a2g.get_xticklabels():
        item.set_rotation(90)
    a2g.set_ylabel('Percentage')
    a2g.set_xlabel('Health')

    a3g = sns.barplot(x=a3['health'], y=a3['Percentage'], data=a3, ax=a3g,
                      order=("Excellent", "Fair", "Very good", "Good", "Poor"))
    a3g.set_title('Moderately depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a3g.get_xticklabels():
        item.set_rotation(90)
    a3g.set_ylabel('Percentage')
    a3g.set_xlabel('Health')

    a4g = sns.barplot(x=a4['health'], y=a4['Percentage'], data=a4, ax=a4g,
                      order=("Excellent", "Fair", "Very good", "Good", "Poor"))
    a4g.set_title('Moderate severely depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a4g.get_xticklabels():
        item.set_rotation(90)
    a4g.set_ylabel('Percentage')
    a4g.set_xlabel('Health')

    a5g = sns.barplot(x=a5['health'], y=a5['Percentage'], data=a5, ax=a5g,
                      order=("Excellent", "Fair", "Very good", "Good", "Poor"))
    a5g.set_title('Severely depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a5g.get_xticklabels():
        item.set_rotation(90)
    a5g.set_ylabel('Percentage')
    a5g.set_xlabel('Health')


def create_dist_insurance(ins_dep):
    # Slicing the data set by depression bins for seperate graphs
    a1 = ins_dep.iloc[np.where(ins_dep['DPQGR'] == 'Not Depressed')]
    a2 = ins_dep.iloc[np.where(ins_dep['DPQGR'] == 'Mild')]
    a3 = ins_dep.iloc[np.where(ins_dep['DPQGR'] == 'Moderate')]
    a4 = ins_dep.iloc[np.where(ins_dep['DPQGR'] == 'Moderately Severe')]
    a5 = ins_dep.iloc[np.where(ins_dep['DPQGR'] == 'Severe')]

    # Define plot size as 1x5, with a figure size and forcing the graphs to share y axis for ez comparison
    fig, (a1g, a2g, a3g, a4g, a5g) = plt.subplots(1, 5, figsize=(20, 6), sharey='row')
    fig.suptitle("Distribution of people's Insurance Status across depression groups", fontsize=20)

    a1g = sns.barplot(x=a1['HIQ011_B'], y=a1['Percentage'], data=a1, ax=a1g, order=("Yes", "No"))
    a1g.set_title('Not depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a1g.get_xticklabels():
        item.set_rotation(90)
    a1g.set_ylabel('Percentage')
    a1g.set_xlabel('Insurance Status')

    a2g = sns.barplot(x=a2['HIQ011_B'], y=a2['Percentage'], data=a2, ax=a2g, order=("Yes", "No"))
    a2g.set_title('Mildly depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a2g.get_xticklabels():
        item.set_rotation(90)
    a2g.set_ylabel('Percentage')
    a2g.set_xlabel('Insurance Status')

    a3g = sns.barplot(x=a3['HIQ011_B'], y=a3['Percentage'], data=a3, ax=a3g, order=("Yes", "No"))
    a3g.set_title('Moderately depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a3g.get_xticklabels():
        item.set_rotation(90)
    a3g.set_ylabel('Percentage')
    a3g.set_xlabel('Insurance Status')

    a4g = sns.barplot(x=a4['HIQ011_B'], y=a4['Percentage'], data=a4, ax=a4g, order=("Yes", "No"))
    a4g.set_title('Moderate severely depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a4g.get_xticklabels():
        item.set_rotation(90)
    a4g.set_ylabel('Percentage')
    a4g.set_xlabel('Insurance Status')

    a5g = sns.barplot(x=a5['HIQ011_B'], y=a5['Percentage'], data=a5, ax=a5g, order=("Yes", "No"))
    a5g.set_title('Severely depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a5g.get_xticklabels():
        item.set_rotation(90)
    a5g.set_ylabel('Percentage')
    a5g.set_xlabel('Insurance Status')


def create_income_bars2(inc_dep1):
    # Slicing the data set by depression bins for seperate graphs
    a1 = inc_dep1.iloc[np.where(inc_dep1['DPQGR'] == 'Not Depressed')]
    a2 = inc_dep1.iloc[np.where(inc_dep1['DPQGR'] == 'Mild')]
    a3 = inc_dep1.iloc[np.where(inc_dep1['DPQGR'] == 'Moderate')]
    a4 = inc_dep1.iloc[np.where(inc_dep1['DPQGR'] == 'Moderately Severe')]
    a5 = inc_dep1.iloc[np.where(inc_dep1['DPQGR'] == 'Severe')]

    # Define plot size as 1x5, with a figure size and forcing the graphs to share y axis for ez comparison
    fig, (a1g, a2g, a3g, a4g, a5g) = plt.subplots(1, 5, figsize=(20, 6), sharey='row')
    fig.suptitle("Distribution of people's Income Group across depression groups", fontsize=20)

    a1g = sns.barplot(x=a1['IND235GR'], y=a1['Percentage'], data=a1, ax=a1g)
    a1g.set_title('Not depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a1g.get_xticklabels():
        item.set_rotation(90)
    a1g.set_ylabel('Percentage')
    a1g.set_xlabel('Income group')

    a2g = sns.barplot(x=a2['IND235GR'], y=a2['Percentage'], data=a2, ax=a2g)
    a2g.set_title('Mildly depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a2g.get_xticklabels():
        item.set_rotation(90)
    a2g.set_ylabel('Percentage')
    a2g.set_xlabel('Income group')

    a3g = sns.barplot(x=a3['IND235GR'], y=a3['Percentage'], data=a3, ax=a3g)
    a3g.set_title('Moderately depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a3g.get_xticklabels():
        item.set_rotation(90)
    a3g.set_ylabel('Percentage')
    a3g.set_xlabel('Income group')

    a4g = sns.barplot(x=a4['IND235GR'], y=a4['Percentage'], data=a4, ax=a4g)
    a4g.set_title('Moderate severely depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a4g.get_xticklabels():
        item.set_rotation(90)
    a4g.set_ylabel('Percentage')
    a4g.set_xlabel('Income group')

    a5g = sns.barplot(x=a5['IND235GR'], y=a5['Percentage'], data=a5, ax=a5g)
    a5g.set_title('Severely depressed')
    # Turing the x tick labels by 90 degrees to reduce clutter
    for item in a5g.get_xticklabels():
        item.set_rotation(90)

    a5g.set_ylabel('Percentage')
    a5g.set_xlabel('Income group')
