import pandas as pd

top500search = pd.read_csv('_select_string1_count_from_picturethis_events_where_day_2022_07__202208291533.csv')
top500rank=pd.read_excel('toprank500.xlsx')
pruning_species = pd.read_excel('xiujian.xlsx')
dict_pruning = dict(zip(pruning_species['uid'].tolist(),pruning_species['groupid'].tolist()))
water_species = pd.read_excel('water.xlsx')
dict_water = dict(zip(water_species['uid'].tolist(),water_species['groupid'].tolist()))


# print(dict_pruning.get('bbl5prjz'))
#
# res=[]
# for  i in range(top500rank.shape[0]):
#     item = top500rank.iloc[i,:]
#     uid = item[0]
#     count = item[1]
#     pruning_groupid = dict_pruning.get(uid)
#     # water_groupid = dict_water.get(uid,default='None')
#     water_groupid = None
#
#     res.extend([{'uid':uid,'count':count,'pruning_groupid':pruning_groupid,'water_groupid':water_groupid}])


def foo(basic_species,file_name):
    res=[]
    for  i in range(basic_species.shape[0]):
        item = basic_species.iloc[i,:]
        uid = item[0]
        count = item[1]
        pruning_groupid = dict_pruning.get(uid)
        water_groupid = dict_water.get(uid)
        res.extend([{'uid':uid,'count':count,'pruning_groupid':pruning_groupid,'water_groupid':water_groupid}])

    df = pd.DataFrame(res)
    df.to_excel(file_name)
    print(df.head())

foo(top500search,'top500search_with_groupid.xlsx')
foo(top500rank,'top500rank_with_groupid.xlsx')
print('over')
print('git hub，and you')
