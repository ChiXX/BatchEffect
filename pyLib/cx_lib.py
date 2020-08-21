#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 23:52
# @Author  : Xu Chi
# @Email   : thisischixu@gmail.com
# @File    : cx_lib.py
# @Software: PyCharm
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np



def PCA_plot(dataFP, designFP, sample, groupBy):
    # dataFp: data file path
    # designFp: design file path
    # sample: sample name
    # groupBy: batch index

    data = pd.read_csv(dataFP, sep='\t')
    #     data['Peptide.Sequence'] = data.apply(lambda x: re.findall('[A-Z]*', x['Peptide.Sequence'])[0], axis=1)
    #     data = data.set_index('Peptide.Sequence', drop=True).dropna()

    design = pd.read_csv(designFP, sep='\t')[[sample, groupBy]]

    data = data[design[sample]].dropna()

    pca = PCA(n_components=4)
    data_pca = pca.fit_transform(data[design[sample]].T)
    data_pca = pd.DataFrame(data_pca, columns=[f"PC{i + 1}" for i in range(data_pca.shape[1])], index=design[sample])

    # calculate the contribution of eatch peptides to PC
    components = pca.components_.T * np.sqrt(pca.explained_variance_)
    components = pd.DataFrame(components, columns=data_pca.columns, index=data.index)

    # plot
    fig = plt.figure(dpi=128, figsize=(9, 4))
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)
    for i in design[groupBy].unique():
        ax1.scatter(data_pca.T[design[design[groupBy] == i][sample]].loc['PC1', :],
                    data_pca.T[design[design[groupBy] == i][sample]].loc['PC2', :])
        ax2.scatter(data_pca.T[design[design[groupBy] == i][sample]].loc['PC3', :],
                    data_pca.T[design[design[groupBy] == i][sample]].loc['PC4', :])
    ax1.set_xlabel("PC1: %0.3f" % pca.explained_variance_ratio_[0])
    ax1.set_ylabel("PC2: %0.3f" % pca.explained_variance_ratio_[1])
    ax2.set_xlabel("PC3: %0.3f" % pca.explained_variance_ratio_[2])
    ax2.set_ylabel("PC4: %0.3f" % pca.explained_variance_ratio_[3])

    fig.suptitle(dataFP.split('/')[-1].split('.')[0])
    plt.legend([f"Batch {i}" for i in design[groupBy].unique()], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    plt.show()

    return components, pca.explained_variance_ratio_


def feature_comparison(data, features, fig_size_x, fig_size_y):
    stable = data[data['Label'] == 0]
    unstable = data[data['Label'] == 1]
    plt.figure(dpi=300, figsize=(10, 10))
    num = 1
    for feature in features:
        plt.subplot(fig_size_x, fig_size_y, num)
        plt.hist([stable[feature], unstable[feature]], bins=25)
        plt.title(feature)
        num += 1
    plt.legend(['stable', 'unstable'], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    plt.subplots_adjust(wspace=0.8, hspace=0.8)