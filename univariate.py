class Uni_analysis():
    def qualquan(dataset):
        Qual=[]
        Quan=[]
        for columnname in dataset.columns:
        #     print(columnname)
            if (dataset[columnname].dtypes == 'O'):
        #         print("Quan")
                Qual.append(columnname)
            else:
        #         print("Qual")
                Quan.append(columnname)
        return Qual,Quan
    
    def univariate_desc(dataset,Quan):
        descriptive = pd.DataFrame(index= ["Mean","Median","Mode",'Q1:25%','Q2:50%','Q3:75%','99%','Q4:100%','IQR','1.5 rule','Lesser Outlier','Greater Outlier','Min','Max'],columns=Quan)
        for columnname in Quan: # qual store in colname
            descriptive[columnname]['Mean'] = dataset[columnname].mean()
            descriptive[columnname]['Median'] = dataset[columnname].median()
            descriptive[columnname]['Mode'] = dataset[columnname].mode()[0]
            descriptive[columnname]['Q1:25%'] = dataset.describe()[columnname]["25%"]
            descriptive[columnname]['Q2:50%'] = dataset.describe()[columnname]["50%"]
            descriptive[columnname]['Q3:75%'] = dataset.describe()[columnname]["75%"]
            descriptive[columnname]['99%'] = np.percentile(dataset[columnname],99)
            descriptive[columnname]['Q4:100%'] = dataset.describe()[columnname]["max"]
            #IQR = q3-q1
            descriptive[columnname]['IQR'] = descriptive[columnname]["Q3:75%"]-descriptive[columnname]["Q1:25%"]
            #1.5*iqr
            descriptive[columnname]['1.5 rule'] = 1.5*descriptive[columnname]["IQR"]
            #LessOutlier = q1-1.5*iqr
            descriptive[columnname]['Lesser Outlier'] = descriptive[columnname]['Q1:25%']-descriptive[columnname]['1.5 rule']
            #greaterOutlier = q3+1.5*iqr
            descriptive[columnname]['Greater Outlier'] = descriptive[columnname]['Q3:75%']+descriptive[columnname]['1.5 rule']
            descriptive[columnname]['Min'] = dataset[columnname].min()
            descriptive[columnname]['Max'] = dataset[columnname].max()
        return descriptive
    
    def to_check_outliers(Quan):
        lesser=[]
        greater=[]
        for columnname in Quan:
          # Lesser outlier --> Min value should not be less than lesser
            if (descriptive[columnname]["Min"]<descriptive[columnname]["Lesser Outlier"]):
                lesser.append(columnname)

          # Greater outlier --> Max value should not be greater than greater.   
            if (descriptive[columnname]["Max"]>descriptive[columnname]["Greater Outlier"]):
                greater.append(columnname)
        return lesser,greater

    def to_replace_outlier(dataset,descriptive):
        for columnname in lesser:
            dataset[columnname][dataset[columnname]<descriptive[columnname]["Lesser Outlier"]]=descriptive[columnname]["Lesser Outlier"]
        for columnname in greater:
            dataset[columnname][dataset[columnname]>descriptive[columnname]["Greater Outlier"]]=descriptive[columnname]["Greater Outlier"]
        return
    
    def freqtable(columnname,dataset):
        freqtable = pd.DataFrame(columns =["Unique_values","Frequancy","Relative_Freq","CumulativeFreq"])
        freqtable["Unique_values"]=dataset[columnname].value_counts().index
        freqtable["Frequancy"]=dataset[columnname].value_counts().values
        n=len(freqtable)
        freqtable["Relative_Freq"]=dataset[columnname].value_counts().values/n
        freqtable["CumulativeFreq"]=freqtable["Relative_Freq"].cumsum() #inbuild func to find cummulative freq
        return freqtable
    
    