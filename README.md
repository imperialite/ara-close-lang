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

### Implementation

Currently this before ACL 2023.
