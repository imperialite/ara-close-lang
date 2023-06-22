# Automatic Readability Assessment for Closely Related Languages

This repository hosts the code and data used for the ACL2023 Long Findings paper *"Automatic Readability Assessment for Closely Related Languages"* by Joseph Imperial and Ekaterina Kochmar for [here](https://arxiv.org/abs/2305.13478).

### Dependencies
1. WEKA 3.7.
2. Rank-Biased Overlap (https://github.com/changyaochen/rbo).
3. Numpy and Pandas for data processing.

### Data
The dataset contribution of this study is a compilation of short fictional stories written in Bikol which was combined with other collected Philippine language corpora for readability assessment such as Tagalog and Cebuano. The data from these languages are all distributed across the Philippine elementary system's first three grade levels (L1, L2, L3). We sourced this dataset from [Let's Read Asia (LRA)](https://www.letsreadasia.org/), [Bloom Library](https://bloomlibrary.org/), [Department of Education](https://lrmds.deped.gov.ph/), and [Adarna House](https://adarna.com.ph/) with explicit permission obtained to share and conduct research with the corpus. We thank these organizations and institutions for their kindness in allowing us to use their data for research.

| Language        | Levels  | Doc Count | Sent Count | Vocab |
|-----------------|---------|:---------:|:----------:|:-----:|
|   Tagalog (265) | Level 1 |     72    |    2774    |  4027 |
|                 | Level 2 |     96    |    4520    |  7285 |
|                 | Level 3 |     97    |    10957   | 12130 |
|   Bikol (150)   | Level 1 |     68    |    1578    |  2674 |
|                 | Level 2 |     27    |    1144    |  2009 |
|                 | Level 3 |     55    |    3347    |  5509 |
|   Cebuano (349) | Level 1 |    167    |    1173    |  2184 |
|                 | Level 2 |    100    |    2803    |  4003 |
|                 | Level 3 |     82    |    3794    |  6115 |

### Code
#### Mutual Intelligibility via N-Gram Overlap and Genetic Distance


#### Linguistic Feature Extraction


#### Model Training with WEKA


### References
If you use any of the materials in this repository, including the dataset or the code, please add the following citations to your paper:
```
Imperial, J. M., Roxas, R. E., Campos, E. M., Oandasan, J., Caraballo, R., Sabdani, F. W., & Almaroi, A. R. (2019). Developing a machine learning-based grade level classifier for Filipino children’s literature. In 2019 International Conference on Asian Language Processing (IALP) (pp. 413-418). IEEE.

Imperial, J. M., & Ong, E. (2020). Exploring hybrid linguistic feature sets to measure filipino text readability. In 2020 International Conference on Asian Language Processing (IALP) (pp. 175-180). IEEE.

Imperial, J. M., Reyes, L. L. A., Ibanez, M. A., Sapinit, R., & Hussien, M. (2022). A Baseline Readability Model for Cebuano. In Proceedings of the 17th Workshop on Innovative Use of NLP for Building Educational Applications (BEA 2022) (pp. 27-32).

Imperial, J. M., & Kochmar, E. (2023). Automatic Readability Assessment for Closely Related Languages. arXiv preprint arXiv:2305.13478.
```


Currently this before ACL 2023.
