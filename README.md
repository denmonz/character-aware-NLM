# Character-Aware Neural Language Model
#### Seminar in Statistical Language Modeling (COMP_SCI 397)
#### Group 6: Zane Denmon, Nayan Mehta, KJ Schmidt, Neelanshi Varia

## Problem Statement:
We propose using a Character-level Convolutional Neural Network and it’s variants on large versus small datasets and comparing performance. Particularly, we would like to see how highway layers affect the model’s performance on large datasets. Yoon Kim et al.’s paper [Character-Aware Neural Language Models](https://arxiv.org/pdf/1508.06615.pdf) compares word-level CNNs to character-level CNNs using the Penn Treebank dataset. We would like to compare their char-CNN results on this dataset to our results of a char-CNN on a larger dataset. The paper also lightly investigates the use of highway layers. The paper found that having one to two highway layers was important, but more highway layers generally resulted in similar performance; and having more convolutional layers before max-pooling did not help. However, they note that this may depend on the size of the dataset. We will change the architecture of the model using various amounts and variants of highway layers, dropouts and CNNs. And observe how this affects the model’s performance on a larger dataset. 

## Creating Conda Environment
After cloning the repostiory, run the following commands to get your conda environment created:

`conda env create --file env-mac.yml`

and activated:

`conda activate character-aware-NLM`
