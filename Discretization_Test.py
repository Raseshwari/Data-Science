import pandas as pf
import numpy as np
np.set_printoptions(threshold=np.inf)

def discretize_data():
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



    #traverse the dataframe row wise and for every column label in the row check the value against 'mean' value and bin it in either 0 (value > mean) or 1 (value < mean).
    for index, item in data.iterrows():
        if item['loc'] >= loc_mean:
             loc.append(1)
        else:
            loc.append(0)

        if item['lOCode'] >= IOCode_mean:
             lOCode.append(1)
        else:
            lOCode.append(0)

        if item['lOComment'] >= lOComment_mean:
            lOComment.append(1)
        else:
            lOComment.append(0)

        if item['lOBlank'] >= lOBlank_mean:
            lOBlank.append(1)
        else:
            lOBlank.append(0)

        if item['locCodeAndComment'] >= locCodeAndComment_mean:
            locCodeAndComment.append(1)
        else:
            locCodeAndComment.append(0)

        if item['uniq_Op'] >= uniq_Op_mean:
            uniq_Op.append(1)
        else:
            uniq_Op.append(0)

        if item['total_Op'] >= total_Op_mean:
            total_Op.append(1)
        else:
            total_Op.append(0)

        if item['branchCount'] >= branchCount_mean:
            branchCount.append(1)
        else:
            branchCount.append(0)

        if item['ev(g)'] >= ev_mean:
            ev.append(1)
        else:
            ev.append(0)

        if item['iv(g)'] >= iv_mean:
            iv.append(1)
        else:
            iv.append(0)

        if item['n'] >= n_mean:
            n.append(1)
        else:
            n.append(0)

        if item['v'] >= v_mean:
            v.append(1)
        else:
            v.append(0)

        if item['l'] >= l_mean:
            l.append(1)
        else:
            l.append(0)

        if item['d'] >= d_mean:
            d.append(1)
        else:
            d.append(0)

        if item['i'] >= i_mean:
             i.append(1)
        else:
            i.append(0)

        if item['e'] >= e_mean:
            e.append(1)
        else:
            e.append(0)

        if item['b'] >= b_mean:
            b.append(1)
        else:
            b.append(0)

        if item['t'] >= t_mean:
            t.append(1)
        else:
            t.append(0)

        if item['v(g)'] >= vg_mean:
            vg.append(1)
        else:
            vg.append(0)

        if item['uniq_Opnd'] >= uniq_Opnd_mean:
            uniq_Opnd.append(1)
        else:
            uniq_Opnd.append(0)

        if item['total_Opnd'] >= total_Opnd_mean:
            total_Opnd.append(1)
        else:
            total_Opnd.append(0)


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
    training_set = test_df.values
    defects = data["defects"]
    return training_set, defects

#dividing data in folds
def create_data_folds(training_set, defects):
    training_fold = [training_set[i::10] for i in range(10)]
    target_fold = [defects[i::10] for i in range(10)]
    return np.asarray(training_fold), target_fold

def outcome_prob(defects):
    no_of_defects = len(defects)
    counter0, counter1 = 0, 0
    for values in defects:
        if values == 0:
            counter0 += 1
        if values == 1:
            counter1 += 1
    probability_of_zero = counter0/no_of_defects
    probability_of_one = counter1/no_of_defects

    prob = ((0, probability_of_zero), (1, probability_of_one))
    prob_dict = dict(prob)
    return prob_dict

# def calculate_class_prob(class_prob_dict):


if __name__ == "__main__":

    training_set, defects = discretize_data()
    train_fold, target_fold = create_data_folds(training_set, defects)
    # print(train_fold.shape)

    for i in range(10):
        validation_train_data = train_fold[i]
        training_data = [item for s in train_fold if s is not validation_train_data for item in s]
        training_data = np.asarray(training_data)
        # print(validation_data.shape, training_data.shape)

        validation_target_data = target_fold[i]
        training_target_data = [item for s in target_fold if s is not validation_target_data for item in s]
        training_target_data = np.asarray(training_target_data)
        # print(validation_target_data.shape, training_target_data.shape)

        prob_outcome = {}
        classes = np.unique(training_target_data)
        rows, columns = np.shape(training_data)
        for cls in classes:
            prob_outcome[cls] = {}

        class_prob_dict = outcome_prob(training_target_data)

        for cls in classes:
            row_indexes = np.where(training_target_data == cls)[0]
            subset = training_data[row_indexes, :]
            rw, cl = np.shape(subset)
            for j in range(0, cl):
                prob_outcome[cls][j] = outcome_prob(list(subset[:, j]))
                # print(prob_outcome)

        for j in validation_train_data:
            results = {}
            for cls in classes:
                class_probability = class_prob_dict[cls]
                for i in range(0, len(j)):
                    relative_values = prob_outcome[cls][i]
                    if j[i] in relative_values.keys():
                        class_probability *= relative_values[j[i]]
                    else:
                        class_probability *= 0
                    results[cls] = class_probability
            print(results)
        #
        # results = {}
        # for cls in classes:
        #     class_probability = class_prob_dict[cls]
        #
        #     row, col = validation_train_data.shape
        #     for rw in range(row):
        #         for cl in range(col):
        #             #print(validation_train_data[rw][cl])
        # #     for i in range(0, len(validation_train_data)):
        #             relative_values = prob_outcome[cls][cl]
        #             if validation_train_data[rw][cl] in relative_values.keys():
        #                 class_probability *= relative_values[validation_train_data[rw][cl]]
        #             else:
        #                 class_probability *= 0
        #             results[cls] = class_probability
        #             print(results)

        # results = {}
        # for cls in classes:
        #     class_probability = class_prob_dict[cls]
        #     ab = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        #     for i in range(0, len(ab)):
        #         relative_values = prob_outcome[cls][i]
        #         if ab[i] in relative_values.keys():
        #             class_probability *= relative_values[ab[i]]
        #         else:
        #             class_probability *= 0
        #         results[cls] = class_probability
        # print(results)



