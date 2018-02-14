import pandas as pf

#read csv file into dataframe
data = pf.read_csv("C:\\Users\ROSS\Documents\Study\Data Science\software-defects-cm1.csv")

#calculated mean value of each column and stored it in a variable for further use.
loc_mean = data["loc"].mean()
IOCode_mean = data["lOCode"].mean()
ev_mean = data["ev(g)"].mean()
iv_mean = data["iv(g)"].mean()
vg_mean = data["v(g)"].mean()
n_mean = data["n"].mean()
v_mean = data["v"].mean()
l_mean = data["l"].mean()
d_mean = data["d"].mean()
i_mean = data["i"].mean()
e_mean = data["e"].mean()
b_mean = data["b"].mean()
t_mean = data["t"].mean()
lOCode_mean = data["lOCode"].mean()
lOComment_mean = data["lOComment"].mean()
lOBlank_mean = data["lOBlank"].mean()
locCodeAndComment_mean = data["locCodeAndComment"].mean()
uniq_Op_mean = data["uniq_Op"].mean()
uniq_Opnd_mean = data["uniq_Opnd"].mean()
total_Op_mean = data["total_Op"].mean()
total_Opnd_mean = data["total_Opnd"].mean()
branchCount_mean = data["branchCount"].mean()

#declared lists for each column to store the binned values of 0 & 1
loc = []
lOCode = []
lOComment =[]
lOBlank = []
locCodeAndComment = []
uniq_Op = []
total_Op = []
total_Opnd = []
branchCount = []
ev = []
iv = []
n = []
v = []
l = []
d = []
i = []
e = []
b = []
t = []
vg = []
uniq_Opnd = []

#test_loc=data["loc"]
#t_loc = []
#print(test_10Code)

# for test in test_loc:
#     if test > loc_mean:
#         #print(test, loc_mean)
#         t_loc.append(0)
# #print(len(t_loc))
#print(vg_mean)

#traverse the dataframe row wise and for every column label in the row check the value against 'mean' value and bin it in either 0 (value > mean) or 1 (value < mean).
for index, item in data.iterrows():
    if item['loc'] >= loc_mean:
         loc.append(0)
    else:
        loc.append(1)

    if item['lOCode'] >= IOCode_mean:
         lOCode.append(0)
    else:
        lOCode.append(1)

    if item['lOComment'] >= lOComment_mean:
        lOComment.append(0)
    else:
        lOComment.append(1)

    if item['lOBlank'] >= lOBlank_mean:
        lOBlank.append(0)
    else:
        lOBlank.append(1)

    if item['locCodeAndComment'] >= locCodeAndComment_mean:
        locCodeAndComment.append(0)
    else:
        locCodeAndComment.append(1)

    if item['uniq_Op'] >= uniq_Op_mean:
        uniq_Op.append(0)
    else:
        uniq_Op.append(1)

    if item['total_Op'] >= total_Op_mean:
        total_Op.append(0)
    else:
        total_Op.append(1)

    if item['branchCount'] >= branchCount_mean:
        branchCount.append(0)
    else:
        branchCount.append(1)

    if item['ev(g)'] >= ev_mean:
        ev.append(0)
    else:
        ev.append(1)

    if item['iv(g)'] >= iv_mean:
        iv.append(0)
    else:
        iv.append(1)

    if item['n'] >= n_mean:
        n.append(0)
    else:
        n.append(1)

    if item['v'] >= v_mean:
        v.append(0)
    else:
        v.append(1)

    if item['l'] >= l_mean:
        l.append(0)
    else:
        l.append(1)

    if item['d'] >= d_mean:
        d.append(0)
    else:
        d.append(1)

    if item['i'] >= i_mean:
        i.append(0)
    else:
        i.append(1)

    if item['e'] >= e_mean:
        e.append(0)
    else:
        e.append(1)

    if item['b'] >= b_mean:
        b.append(0)
    else:
        b.append(1)

    if item['t'] >= t_mean:
        t.append(0)
    else:
        t.append(1)

    if item['v(g)'] >= vg_mean:
        vg.append(0)
    else:
        vg.append(1)

    if item['uniq_Opnd'] >= uniq_Opnd_mean:
        uniq_Opnd.append(0)
    else:
        uniq_Opnd.append(1)

    if item['total_Opnd'] >= total_Opnd_mean:
        total_Opnd.append(0)
    else:
        total_Opnd.append(1)


#created dictionary of the dataset to be imported using dataframes.from_dict - but this imports data row wise.
# # dataset_dict = [
# #     {'loc': loc}, {'v(g)': vg},
# #     {'ev(g)': ev}, {'iv(g)': iv},
# #     {'n': n}, {'v': v},
# #     {'l': l}, {'d': d},
# #     {'i': i}, {'e': e},
# #     {'b': b}, {'t': t},
# #     {'lOCode': lOCode}, {'lOComment': lOComment},
# #     {'lOBlank': lOBlank}, {'locCodeAndComment': locCodeAndComment},
# #     {'uniq_Op': uniq_Op}, {'uniq_Opnd': uniq_Opnd},
# #     {'total_Op': total_Op}, {'total_Opnd': total_Opnd},
# #     {'branchCount': branchCount}
# # ]
# #
# # #print(len(branchCount), len(total_Opnd))
# #

#created list of lists so that data can be imported in dataframes lisr wise.
test = [('loc', loc), ('v(g)', vg),
         ('ev(g)', ev), ('iv(g)', iv),
         ('n', n), ('v', v),
         ('l', l), ('d', d),
         ('i', i), ('e', e),
         ('b', b), ('t', t),
         ('lOCode', lOCode), ('lOComment', lOComment),
         ('lOBlank', lOBlank), ('locCodeAndComment', locCodeAndComment),
         ('uniq_Op', uniq_Op), ('uniq_Opnd', uniq_Opnd),
         ('total_Op', total_Op), ('total_Opnd', total_Opnd),
         ('branchCount', branchCount)
]

#imported data into dataframe
test_df = pf.DataFrame.from_items(test)
print(test_df)

# dataset_df = pf.DataFrame.from_dict(dataset_dict)
# print(dataset_df)




