import pandas as pd
def obs1():
    label=data['industry_name_ANZSIC'].tolist()
    label=list(dict.fromkeys(label))
    label.remove("All Industries")
    totinc=[]
    for i in data.index:
        if (data['year'][i]==2011 and data['rme_size_grp'][i]=="i_Industry_Total" and data['variable'][i]=="Total income"):
            totinc.append(data['value'][i])
    z=len(label)
    max=0
    for k in range(z):
        if(int(totinc[k])>int(max)):
            max=totinc[k]
            temp=k
    for j in range(z):
        print(label[j]," had a total income of ",totinc[j]," million dollars.")
    print("In the year 2011, ",label[temp]," had the maximum income of ",totinc[temp]," million dollars.")
def obs2():
    label = data['year'].tolist()
    label = list(dict.fromkeys(label))
    totinc=[]
    for i in data.index:
        if (data['industry_code_ANZSIC'][i] == "all" and data['variable'][i] == "Total income"):
            totinc.append(data['value'][i])
    z = len(label)
    max = 0
    for k in range(z):
        if(int(totinc[k]) > int(max)):
            max = totinc[k]
            temp = k
    for j in range(z):
        print(label[j], " had a total income of ", totinc[j], " million dollars.")
    print("The year ",label[temp]," had the maximum income of ", totinc[temp]," for new Zealand,")
def obs3():
    label = data['industry_name_ANZSIC'].tolist()
    label = list(dict.fromkeys(label))
    label.remove("All Industries")
    for i in data.index:
        if (data['year'][i] == 2015 and data['industry_code_ANZSIC'][i] == "all" and data['variable'][i] == "Total income"):
            total=data['value'][i]
    z = len(label)
    mean=int(total)/z
    print("The mean of total incomes of all industries in year 2015 is ",mean," million dollars.")
def obs4():
    label = data['industry_name_ANZSIC'].tolist()
    label = list(dict.fromkeys(label))
    label.remove("All Industries")
    sal = []
    for i in data.index:
        if (data['year'][i] == 2013 and data['rme_size_grp'][i] == "i_Industry_Total" and data['variable'][i] == "Salaries and wages paid"):
            sal.append(data['value'][i])
    z = len(label)
    min = sal[0]
    for k in range(z):
        if (int(sal[k]) < int(min)):
            min = sal[k]
            temp = k
    for j in range(z):
        print(label[j]," has given salaries and wages worth ",sal[j]," million dollars.")
    print("In the year 2013, ",label[temp]," has given the minimum salary and wages worth ",sal[temp]," million dollars.")
def obs5():
    lis = []
    for i in data.index:
        if (data['industry_code_ANZSIC'][i] == 'J' and data['rme_size_grp'][i] == "i_Industry_Total" and data['variable'][i] == "Total income"):
            lis.append(data['value'][i])
    z=len(lis)
    sum=0
    for j in range(z):
        sum+=int(lis[j])
    mean=sum/z
    print("The mean of total income of Information media and telecommunications industry from the year 2011 to 2018 is ",mean," million dollars.")
def obs6():
    label = data['industry_name_ANZSIC'].tolist()
    label = list(dict.fromkeys(label))
    label.remove("All Industries")
    exp = []
    for i in data.index:
        if (data['year'][i] == 2016 and data['rme_size_grp'][i] == "i_Industry_Total" and data['variable'][i] == "Total expenditure"):
            exp.append(data['value'][i])
    z = len(label)
    min = exp[0]
    for k in range(z):
        if (int(exp[k]) < int(min)):
            min = exp[k]
            temp = k
    for j in range(z):
        print(label[j], " has had a total expenditure of ", exp[j], " million dollars.")
    print("In the year 2016, ", label[temp], " has had the minimum total expenditure of ", exp[temp], " million dollars.")
if __name__=="__main__":
    data = pd.read_csv("annual.csv")
    print("Observation 1: Which industry had the maximum income in year 2011? ")
    obs1()
    print("\n")
    print("Observation 2: According to New Zealand's annual enterprise survey,which year has been most productive with maximum total income? ")
    obs2()
    print("\n")
    print("Observation 3: What is the mean of the total incomes of all industries in year 2015? ")
    obs3()
    print("\n")
    print("Observation 4: Which industry paid the minimum salary and wages in the year 2013? ")
    obs4()
    print("\n")
    print("Observation 5: What is the mean of total income of Information media and telecommunications industry from the year 2011 to 2018? ")
    obs5()
    print("\n")
    print("Obseration 6: Which industry had the least total expenditure in the year 2016? ")
    obs6()
    print("\n")


