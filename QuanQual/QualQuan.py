class quantitative_qualitative():
    def quanqual (dataset):
        qual=[]
        quan=[]
        for columnname in dataset.columns:
    #         print(columnname)
            if (dataset[columnname].dtypes == 'O'):
    #             print("Qual")
                qual.append(columnname)

            else:
    #             print("Quan")
                quan.append(columnname)

        return quan,qual
