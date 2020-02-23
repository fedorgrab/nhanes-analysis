# NHANES data analysis: 
ALY6140 Homework

[**The National Health and Nutrition Examination Survey**](https://www.cdc.gov/nchs/nhanes/index.htm?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnchs%2Fnhanes.htm) is a survey research program performed by the National Center for Health Statistics
to determine the health status of citizens in the United States.
The survey consists of interviews, physical examinations and laboratory tests.

## Goals:
* Observe features correlating with depressive symptoms. 
* Analyse spread of Major Depression over different social groups and statuses in the US.
* Predict occurence of Major Depression.

 ## Definitions:
 
**Depression:** Measured by the NHANES using the Patient Health Questionnaire (PHQ–9), a screening instrument consisting of questions about the frequency of symptoms of depression over the past 2 weeks. Response categories are: "not at all", "several days", "more than half the days" and "nearly every day" represent a score of 0–3. A total score of 0–27 is then calculated.

**Major Depression:** Depression is a PHQ–9 score of 10 or higher, because surveyed with a score > or = 10 have a sensetivity of 88% and a specificity of 88% for major depression according to [validity of a brief depression severity measure](https://www.ncbi.nlm.nih.gov/pubmed/11556941)
 
All data observation steps are presented in [NHANES_analysis.ipynb](https://github.com/fedorgrab/nhanes-analysis/blob/master/NHANES_analysis.ipynb)

## Insights:

### During 2015–2016, ~8.55% of Americans aged 17 and over had depression (moderate or severe depressive symptoms in the past 2 weeks). 
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_overall.png?style=centerme)
___
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_gender_age.png)
* **Males have significantly lower rates than females overall and in every age group.**
* **The highest rate of depression, 14.6%, was found in women aged 30-42.**
* **Depression was more prevalent among females and persons aged 56-69.**
___
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_gender_marital.png)
* **Males have significantly lower rates than females overall and in every Marital status group.**
* **Significant difference occurred between females and males Living with partner.**
* **Major Depression was more prevalent among females and Separated persons.**
* **Major Depression was less prevailed among married people.**
* **The most prevalent group of depressed people, 22.9%, is separated females.**
---
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_gender_sexual_orientation.png)
* **Straight people have significantly lower rates than Bisexuals and gays among either males or females and overall.**
* **Significant difference occurred between females and males living with partner.**
* **Major Depression was more prevalent among Bisexual people.**
* **Major Depression was less prevalent among Straight people**
* **Major Depression was equally rated among bisexual females and males.**
---
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_race_age.png)
* **Non-Hispanic White and Other Hispanic groups have significantly greater rates than others.**
* **The lowest rates occurred over Non-Hispanic Asian race.**
* **Significant difference occurred over Non-Hispanic Black betwen 30-42 and 43-55.**
---
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_income_race.png)
* **Representatives with high level of Monthly income showed the lowest rates of Major Depression overall and among different races, as opposed to persons with low level of Monthly income.**
* **Significant difference occurred over different Income group in Non-Hispanic White race.**
---
#### During the analysis significant correlation occurred between Depression Score and level of Education. However including Education code as a feature in predictive model raised mean absolute error, thus correlation between Education level and Depression Score is accepted as consequence of impact of level of Family Income on Depression Score due to the fact that Education level affects monthly Family Income Index.
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_income_education.png)

* **Representatives with high level of Education showed the highest rates of Monthly Family Income as opposed to persons with low level of Education prevailing on rates of lowest Family Income.**
* **Representatives with high level of Education showed the highest rates of Monthly Family Income as opposed to persons with low level of Education prevailing on rates of lowest Family Income.**
---

![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_drug_use.png)
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_drug_use_2.png)
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_drug_use_3.png)

* **People who were on rehabilitation program and who tried cocaine/methamphetamine/heroin had significant higher rates of Major Depression.**
---
![](https://github.com/fedorgrab/nhanes-analysis/blob/master/charts/depression_alco_use.png)
* **Major depression rate remains stable over people who drink alcohol 1-3 times per month, 1 time per week and 2-3 times per week.**
* **Persons drinking 3 and more times per week occurred the most prevailed rate of depression among different alcohol consuming groups accounting for more than 12%.**
* **The second prevailed rate of depression occurred in groups consuming alcohol less than 1 time per month accounting for roughly 12%.** 
---

NOTES: Depression is defined as having moderate to severe depressive symptoms. \
SOURCE: CDC/NCHS, National Health and Nutrition Examination Survey.
