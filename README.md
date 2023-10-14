# Automatic Readability Assessment for Closely Related Languages

This repository hosts the code and data used for the ACL2023 Long Findings paper *"Automatic Readability Assessment for Closely Related Languages"* by Joseph Imperial and Ekaterina Kochmar for [here](https://aclanthology.org/2023.findings-acl.331/).

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

All used datasets are inside the `data` folder categorized by language. The formatted .txt and .csv files as the extracted features from the code are included in each language except in Tagalog, where the raw Adarna House data is not added due to copyright permissions. The results can still be reproduced using the extracted feature file.

### Code
#### Mutual Intelligibility via N-Gram Overlap and Genetic Distance
The code for calculating the two measures of mutual intelligibility, `n-gram overlap` and `genetic distance` are inside the data/mutual_intelligibility/ngrams/`ngram_overlap.ipynb` and data/mutual_intelligibility/genetic_distance/`exact_consonant_match.py` respectively. For `n-gram overlap` you would need two big comparable corpora for Language A and Language B to compare their top overlapping bigrams and trigrams. In the study, we simply used the aggregated collected storybooks per language. For `genetic distance`, you would need two lists of the top common words used for each language. These can easily be extracted in vocabulary websites or derived from large corpora as well.

#### Linguistic Feature Extraction
Inside the `code` folder there are three parser files (`syll_parse.py`, `trad_parser.py`, `CLGSNGO_parser.py`), three function files (`SYLL.py`, `TRAD.py`, `CLGSNGO.py`), and one for extracting the embeddings from a multilingual BERT model (`extract_embeddings.py`). The function files contain the functions for extracting the linguistic features, and these are called in the parser files where you input your .csv files to iterate row-by-row. Each parser file will output a .csv file containing the extracted features, which you can combine or concatenate together for experimentation (see examples such as `tag_features.csv` in the data/tagalog/ folder).

#### Model Training with WEKA
All model training is done with WEKA 3.7 using the default settings for Random Forest. You can double-check your hyperparameter values with ours, as shown in the Appendix of the paper. If you are new to WEKA, there are good video tutorials online, such as from [DataMining Tutorials](https://www.youtube.com/watch?v=_LbnNTz4-mI) and [Rushdi Shams](https://www.youtube.com/watch?v=uiDFa7iY9yo) on Youtube.

### References
If you use any of the materials in this repository, including the dataset or the code, please add the following citations to your paper:
```
Imperial, J. M., Roxas, R. E., Campos, E. M., Oandasan, J., Caraballo, R., Sabdani, F. W., & Almaroi, A. R. (2019). Developing a machine learning-based grade level classifier for Filipino children’s literature. In 2019 International Conference on Asian Language Processing (IALP) (pp. 413-418). IEEE.

Imperial, J. M., & Ong, E. (2020). Exploring hybrid linguistic feature sets to measure filipino text readability. In 2020 International Conference on Asian Language Processing (IALP) (pp. 175-180). IEEE.

Imperial, J. M., Reyes, L. L. A., Ibanez, M. A., Sapinit, R., & Hussien, M. (2022). A Baseline Readability Model for Cebuano. In Proceedings of the 17th Workshop on Innovative Use of NLP for Building Educational Applications (BEA 2022) (pp. 27-32).

Imperial, J. M., & Kochmar, E. (2023). Automatic Readability Assessment for Closely Related Languages. arXiv preprint arXiv:2305.13478.
```

### Contact
If you need any help reproducing the results, please don't hesitate to contact me below:

**Joseph Marvin Imperial** <br/>
jmri20@bath.ac.uk <br/>
www.josephimperial.com 

