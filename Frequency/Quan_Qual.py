class quantiquali():
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