import numpy as np
import pandas as pd 
from mlxtend.frequent_patterns import apriori,association_rules
from sklearn.naive_bayes import MultinomialNB
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np
from sklearn import metrics
import xlsxwriter

warnings.filterwarnings("ignore")

def convert_to_excel(df,y_pred_class,skill_set):
    writer = pd.ExcelWriter('output.xlsx')
    sheet='Test'
    df.to_excel(writer, sheet,index=False)
    row=df.shape[0]+5
    wb = writer.book
    ws = writer.sheets[sheet]
    ws.write(row, 0, "Suitable job role-----")
    ws.write(row, 1, y_pred_class[0])
    ws.write(row+1, 0, "Skills you need to learn-----")
    ws.merge_range(row+2, 0, row+2, 15, ",".join(skill_set))
    writer.save()
    wb.close()


def multinomiannb(df,skills):
    X=df['Skills_required'].apply(lambda x: ','.join(map(str, x))).str.get_dummies(",")
    y=df['jobrole']
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    nb = MultinomialNB()
    nb.fit(X_train, y_train)
    aa=[1 if X.columns[i] in skills else 0 for i in range(X.shape[1])]
    y_pred_class = nb.predict([aa])
    rslt_df = df[df['jobrole'] == y_pred_class[0]] 
    skill_set=list(set(sum(rslt_df['Skills_required'].tolist(),[])))
    return(y_pred_class,skill_set)
    
def to_1D(series):
 return pd.Series([x for _list in series for x in _list])

def boolean_df(item_lists, unique_items):
    bool_dict = {}
    for i, item in enumerate(unique_items):
        bool_dict[item] = item_lists.apply(lambda x: item in x)
    return pd.DataFrame(bool_dict)


def skill_vs_no_of_jobs_graph(D,ax):
    # ploting
    # n=int(input("Enter no of entries in skill vs no of jobs graph="))
    n=11
    ax[1]=sns.barplot(y = list(D.values())[1:n], x = list(D.keys())[1:n],color = 'b',ax=ax[1])
    ax[1].set_ylabel("skill", fontsize = 15)
    ax[1].set_xlabel("No of jobs", fontsize = 15)
    ax[1].set_title("skill vs no of jobs", fontsize = 20)
    plt.show()
    

def skills_heatmap(dfs,D,ax):
    # n=int(input("Enter no of skills for heatmap="))
    n=11
    skills_bool=boolean_df(dfs,list(D.keys())[1:n])
    corr = skills_bool.corr(method = "pearson")
    skills_freq_mat = np.dot(corr.T, corr)
    skills_freq = pd.DataFrame(skills_freq_mat, columns = list(D.keys())[1:n], index = list(D.keys())[1:n])
    ax[0]=sns.heatmap(skills_freq, cmap = "Blues",ax=ax[0])
    ax[0].set_title("heatmap of skill set", fontsize = 20)
    plt.xticks(rotation=-60)
    plt.show()

def graphs(df,D):
    fig, ax = plt.subplots(2,1)
    fig.suptitle('Internship data analysis')
    skills_heatmap(df['Skills_required'],D,ax)
    skill_vs_no_of_jobs_graph(D,ax)

def freaquent_patterns(skl_set,skills):
    # min_support=float(input("Enter minimum support="))
    # min_threshold=int(input("Enter minimum threshold="))
    # min_lift=float(input("Enter minimum lift="))
    # min_confidence=float(input("Enter minimum confidence="))
    min_support=0.05
    min_threshold=2
    min_lift=6
    min_confidence=0.9
    frequent_itemsets=apriori(skl_set,min_support=min_support)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold)
    ss=rules[ (rules['lift'] >= min_lift) & (rules['confidence'] >= min_confidence) ]
    fp=[]
    for i in range(ss.shape[0]):
        fp.append([skills[i] for i in ss.iat[i,0]])
    
    return fp
    
        
def skills_checking(dfs,options):
    # options=["digital marketing","search engine optimization (seo)","english proficiency (spoken)"]
    # options=input("Enter skills=")
    if len(options)==0:
        return dfs
    sel=[]
    for i in dfs['Skills_required']:
        temp=[]
        for j in i:
            if j in options:
                temp.append(j in options)
            else:
                temp.append(j in options)
        sel.append(any(temp))
    ndf=dfs.loc[sel]
    return ndf

def filter_stipend(df,stipend):
    # appl=int(input("Enter min stipend="))
    # stipend=2000
    if stipend==0:
        return df
    rslt_df = df[df['stipend'] >= stipend] 
    return rslt_df

def filter_no_of_applications(df,appl):
    # appl=int(input("Enter min stipend="))
    # appl=20
    if appl==0:
        return df
    rslt_df = df[df['no_of_applications'] >= appl] 
    return rslt_df

def filter_duration(df,duration):
    # duration=int(input("Enter min stipend="))
    # duration=3
    if duration==0:
        return df
    rslt_df = df[[int(j.split(" ")[0]) <= duration for j in df['duration']]] 
    return rslt_df

def filter_no_of_openings(df,openings):
    # openings=int(input("Enter min stipend="))
    # openings=2
    if openings==0:
        return df
    rslt_df = df[df['Number_of_openings'] >= openings] 
    return rslt_df

def filter_candidates_hired(df,candidates_hired):
    # candidates_hired=int(input("Enter min stipend="))
    # candidates_hired=20
    if candidates_hired==0:
        return df
    rslt_df = df[df['candidates_hired'] >= candidates_hired] 
    return rslt_df

def filter_location(dfs,options):
    # location=["mumbai","work from home"]
    # location=input("Enter your locations=")
    if len(options)==0:
        return dfs
    sel=[]
    for i in dfs['location']:
        temp=[]
        for j in i:
            if j in options:
                temp.append(j in options)
            else:
                temp.append(j in options)
        sel.append(any(temp))
    ndf=dfs.loc[sel]
    return ndf

def filtering(ndf,fil):
    ndf=skills_checking(ndf,fil[0])
    ndf=filter_stipend(ndf,fil[1])
    ndf=filter_no_of_applications(ndf,fil[2])
    ndf=filter_location(ndf,fil[6])
    ndf=filter_duration(ndf,fil[3])
    ndf=filter_no_of_openings(ndf,fil[4])
    ndf=filter_candidates_hired(ndf,fil[5])
    return ndf


