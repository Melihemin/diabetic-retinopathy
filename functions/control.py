def control(cnt, df):
    cnt_ = int(cnt)
    print(f' Retinopati derecesi [{cnt_}] : ',df['diagnosis'][cnt_])
    print(f' Encoder Edilmis Retinopati derecesi [{cnt_}] : ',y_train[cnt_])