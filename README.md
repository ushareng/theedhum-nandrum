# theedhum-nandrum (தீதும் நன்றும்)
A sentiment classifier on mixed language (and mixed script) reviews in Tamil, Malayalam and English. You can read our paper describing the approach at https://arxiv.org/abs/2010.03189. Please cite our paper if you are using this.

@misc{lakshmanan2020theedhum,
      title={Theedhum Nandrum@Dravidian-CodeMix-FIRE2020: A Sentiment Polarity Classifier for YouTube Comments with Code-switching between Tamil, Malayalam and English}, 
      author={BalaSundaraRaman Lakshmanan and Sanjeeth Kumar Ravindranath},
      year={2020},
      eprint={2010.03189},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

![Image of TheedhumNandrum](https://raw.githubusercontent.com/oligoglot/theedhum-nandrum/3d3e3f2ad236b74e7917c956f819c7316f3bc690/t-n.png)

## Installation
## Pre-requisites
* Python 3.7 or above
## Getting the code
----------------
* `cd /path/to/parent/`
* `git clone https://github.com/oligoglot/theedhum-nandrum.git`
* `cd theedhum-nandrum`

## Setting up dev environment
----------------
* `virtualenv venv_tn`
* `source venv_tn/bin/activate`
* `pip install -r requirements.txt `

## Running the classification scripts
----------------
* You need to activate the virtualenv
    * `source venv_tn/bin/activate`
* `cd src/tn`
* Hyper Parameter Tuning for SGD Classifier
   * `python3 sentiment_classifier.py experiment ta ../../resources/data/tamil_train.tsv ../../resources/data/tamil_dev.tsv configs/tuning_experiments_1.json`
* Classification for Tamil Input Set
  * `python3 sentiment_classifier.py test ta ../../resources/data/tamil_train.tsv ../../resources/data/tamil_dev.tsv <output File>`
* Classification for Malayalam Input Set
  * `python3 sentiment_classifier.py test ml ../../resources/data/malayalam_train.tsv ../../resources/data/malayalam_dev.tsv <output File>`


# Steps
## Pre-processing
### Noise removal
1. Remove irrelevant parts of the data, like html tags

### Language identification
1. If the text is a different language, need to output "Not tamil"

# Attributions
1. Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html
    Copyright (c) 2007-2016 Peter Norvig
    MIT license: www.opensource.org/licenses/mit-license.php
2. Module to convert Unicode Emojis to corresponding Sentiment Rankings.
    Based on the research by Kralj Novak P, Smailović J, Sluban B, Mozetič I
    (2015) on Sentiment of Emojis.
    Journal Link:
    https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144296
    CSV Data acquired from CLARIN repository,
    Repository Link: http://hdl.handle.net/11356/1048
