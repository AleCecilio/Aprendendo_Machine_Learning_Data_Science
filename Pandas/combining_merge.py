import numpy as np
import pandas as pd


registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})

print(registrations,'\n')
print(logins,'\n')

print(pd.merge(registrations,logins,how='inner',on='name'),'\n')

print(pd.merge(left=registrations,right=logins,how='right',on='name'),'\n')

print(pd.merge(left=registrations,right=logins,how='left',on='name'),'\n')

print(pd.merge(registrations,logins,how='outer',on='name'),'\n')

registrations = registrations.set_index('name')
print(registrations,'\n')
print(pd.merge(registrations,logins,how='inner',left_index=True,right_on='name'),'\n')

registrations = registrations.reset_index()
registrations.columns = ['reg_name','reg_id']
resultado = pd.merge(registrations,logins,how='inner',left_on='reg_name',right_on='name')
print(resultado.drop('reg_name', axis=1),'\n')

registrations.columns = ['name','id']
logins.columns = ['name','id']
print(pd.merge(registrations,logins,on='name',suffixes=('_reg','_log')),'\n')