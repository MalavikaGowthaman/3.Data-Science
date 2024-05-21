class quantiquali():
    def qualquan(dataset):
        Qual=[]
        Quan=[]
        for columnname in dataset.columns:
        #     print(columnname)
            if (dataset[columnname].dtypes == 'O'):
        #         print("Quan")
                Quan.append(columnname)
            else:
        #         print("Qual")
                Qual.append(columnname)
        return Qual,Quan