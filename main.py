"""#Data visualization using panda, matplotlib, seaborn 
import pandas as pd
#process of todayproject
#1. Load data using pandas
#2. Clean the data
#3. Analysis the data
#4. Graph -> Visualization  
#5. Report generate using fpdfz

import matplotlib.pyplot as plt
import seaborn as sns
#pip install fpdf2
import fpdf

#Data load and Clean
#try and catch
print("1.----------------cleaning the data---------------")
try:
    df = pd.read_csv("titanic.csv")#df -> data
    print("Data loaded successfully!")
    print(df.columns)
except FileNotFoundError:
    print("File not found")
    exit()

#data cleaning
if "Age" in df.columns:
    #medium of the age
    df['Age'] = df['Age'].fillna(df['Age'].median())

print("Data cleaned successfully")
print(df['Age'])
#perform statistical analysis
print('Perform Statistical Analysis')
#gender, overall survival rate, -> percentage, class -> using mean
overall_survival_rate = df['Survived'].mean() * 100
survive_by_gender = df.groupby('Sex')['Survived'].mean()*100 #male, #female -> percentage
survival_by_class = df.groupby('Pclass')['Survived'].mean()*100 #1-.percentage . 3 -> percentage

#print
print(f'overall survived rate \n {overall_survival_rate: 2f}')#2f le decimal pachadi ko 2 ota value matra dinxa
print(f"\nSurvival rate by gender \n {survive_by_gender}")
print(f"\nSurvival rate by class\n {survival_by_class}")

#plotting in 
print("3. Plotting the graph using metaplot and seaborn")

#sns
sns.set_theme(style="whitegrid")#bar chat
plt.figure(figsize=(8,6))
sns.barplot(x=survival_by_class.index, y=survival_by_class.values, palette="coolwarm")
plt.title("graph1 : Survival rate by gender")
plt.ylabel("Survive by %")
plt.ylim(0,100)
plt.savefig("graph1.png")
plt.close()

#show the age survival rate using histogram
plt.figure(figsize=(8,6))
sns.histplot(data=df, x="Age",hue="Survived",kde=True,palette="Set2",multiple="stack",bins=30)
plt.title("graph2 : Age survival rate ")
plt.xlabel("Age")
plt.legend(title="Survived", labels=["Yes","No"])
plt.savefig("graph2.png")
plt.close()

#show the age survival rate using histogram
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="Age", y= "Fare", hue="Survived")
plt.title("graph3 : Age survival rate ")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.ylim(0,300)
plt.legend(title="Survived", labels=["Yes","No"])
plt.savefig("graph3.png")
plt.close()
"""

# Data visualization using panda, matplotlib, seaborn
import pandas as pd
# Process of today project
# 1. Load Data using pandas
# 2. Clean the data 
# 3. Analyisis the data 
# 4. Graph -> Visualization
# 5. Report generate using fpdf2 
import matplotlib.pyplot as plt
import seaborn as sns
#  pip install fpdf2
from fpdf import FPDF

# Data load and Clean
# try and catch
print("1.-----------------cleaning the data ---------------")
try:
    df = pd.read_csv("titanic.csv") # df -> data 
    print("Data loaded successfully") #
    print(df.columns)
except FileNotFoundError:
    print("File not found")
    exit()

# data cleaning
if "Age" in df.columns:
    # medium of the age mainly used for 
    df['Age'] = df['Age'].fillna(df['Age'].median())
    print(df['Age'])
print("data cleaned successfully")

# perform Statistical Analyiss
print('Perfom Statistiacl Analyisi')
# gender, overall_survival_rate -> percentage, class_ # mean
oveall_surviavl_rate = df['Survived'].mean() *100
survive_by_gender = df.groupby('Sex')['Survived'].mean() * 100 # male, # femal -> percentage
# clss -> 
survival_by_class  = df.groupby('Pclass')['Survived'].mean() * 100 # 1 -. percentage , 3 -> percentage

# print
print(f'\noverall survial rate \n {oveall_surviavl_rate:.2f}')
print(f"\nsurvival rate by gender\n {survive_by_gender}")
print(f"\nsurvival rate by class\n{survival_by_class}")

# plotting in 
print("3. Plotting the graph using matplotlib and seaborn")
# sns
sns.set_theme(style="whitegrid")
#bar chat 
plt.figure(figsize=(8,6))
sns.barplot(x=survival_by_class.index, y=survival_by_class.values, palette="coolwarm")
plt.title("graph1 :  Survival rate by passasnger class")
plt.ylabel("Survive by %")
plt.ylim(0,100)
plt.savefig("graph1.png")
plt.close()
#show the survive rate by gender
plt.figure(figsize=(8,6))
sns.barplot(x=survive_by_gender.index, y=survive_by_gender.values, palette="coolwarm")
plt.title("graph1 :  Survival rate by passasnger class")
plt.ylabel("Survive rate by %")
plt.ylim(0,100)
plt.savefig("graph2.png")
plt.close()
# show the age survival rate using historam 0 to 1
plt.figure(figsize=(8,6))
sns.histplot(data = df, x = "Age", hue="Survived", kde=True, palette="Set2", multiple="stack", bins=30)
plt.title("graph3 :Age survival rate  ")
plt.xlabel("Age")
plt.legend(title="Survived", labels=["Yes", "No"])
plt.savefig("graph3.png")
plt.close()
# show the a scatterplot
plt.figure(figsize=(8,6))
sns.scatterplot(data = df, x = "Age", y = "Fare", hue = "Survived", palette="Set2", alpha=0.7)
plt.title("graph4 :Age survival rate  ")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.ylim(0,300)
plt.legend(title="Survived", labels=["Dies", "Survived"])
plt.savefig("graph4.png")
plt.close()

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, 'Titanic Survival Analysis Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF('P', 'mm', 'A4')
pdf.add_page() 

# --- Add Title ---
pdf.set_font("Arial", 'B', 18) 
pdf.cell(0, 15, "Titanic Survival Analysis Report", ln=True, align="C")
pdf.ln(5)  

pdf.set_font("Arial", '', 11) 
pdf.multi_cell(0, 7,
f"""This report provides a detailed analysis of the factors affecting passenger survival on the Titanic. The dataset contains information on {len(df)} passengers.

**Key Statistical Findings:**
- **Overall Survival Rate:** {oveall_surviavl_rate:.2f}% of passengers survived.
- **Gender Impact:** Females had a significantly higher survival rate ({survive_by_gender['female']:.2f}%) compared to males ({survive_by_gender['male']:.2f}%).
- **Class Impact:** 1st class passengers had the highest chance of survival ({survival_by_class[1]:.2f}%), while 3rd class had the lowest ({survival_by_class[3]:.2f}%).
""")
pdf.ln(10)

pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Visual Analysis", ln=True, align="L")

image_width = 90
pdf.image("graph1.png", x=15, w=image_width)
pdf.image("graph2.png", x=105, w=image_width)
pdf.ln(image_width + 5)  

pdf.image("graph3.png", x=15, w=image_width)
pdf.image("graph4.png", x=105, w=image_width)
pdf.ln(image_width + 5)

pdf.output("titanic_analysis_report.pdf")

print("\nPDF report 'titanic_analysis_report.pdf' generated successfully!")
print("\n--- Project Complete ---")