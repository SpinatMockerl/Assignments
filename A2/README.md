# Medizinische Genomanalysen 2019 - Assignment 2

## News
* Deadline: 20.05.2019
* Use the chr21_**new**.vcf and chr22_**new**.vcf files
* Use this information to get the variant callers
```callsetnames=,HiSeqPE300xfreebayes```
* Use this information to get the reference version
```difficultregion=AllRepeats_lt51bp_gt95identity_merged,hg38_self_chain_withalts_gt10k```

## Overview
* Fork and clone the repository
* Complete the python program, based on the template, to calculate various properties
* Complete all TODOs
* **Hint**: Call the individual methods from *print_summary*
* Commit (often)
* Push to **your** repository

## Data
* VCF chr21: [http://hmd.ait.ac.at/medgen2019/chr21.vcf](http://hmd.ait.ac.at/medgen2019/chr21.vcf)
* VCF chr22: [http://hmd.ait.ac.at/medgen2019/chr22.vcf](http://hmd.ait.ac.at/medgen2019/chr22.vcf)
* All datasets [http://hmd.ait.ac.at/medgen2019/](http://hmd.ait.ac.at/medgen2019/)

## Data backup
* VCF chr21: [http://hmd.ait.ac.at/medgen2019/chr21_new.vcf](http://hmd.ait.ac.at/medgen2019/chr21_new.vcf)
* VCF chr22: [http://hmd.ait.ac.at/medgen2019/chr22_new.vcf](http://hmd.ait.ac.at/medgen2019/chr22_new.vcf)

## Tools
* pyvcf (http://pyvcf.readthedocs.io/en/latest/)

## Work
* Perform the calculation using chr22
* **Only** when implementing the method *merge_chrs_into_one_vcf* use **both** chromosomes (chr21 and chr22) 




