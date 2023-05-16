# SI-LIN308
Examining Simultaneous Interpretation

## CITATION

Kosuke Doi, Katsuhito Sudoh, Satoshi Nakamura.
Large-Scale English-Japanese Simultaneous Interpretation Corpus: Construction and Analyses with Sentence-Aligned Data
Proceedings of the 18th International Conference on Spoken Language Translation, pp. 226--235, 2021
https://aclanthology.org/2021.iwslt-1.27/

NAIST Simultaneous Interpretation Corpus (SIC) 2022
https://dsc-nlp.naist.jp/data/NAIST-SIC/2022/

## Simultaneous Interpretation Data

EJ: English-to-Japanese interpretation data (TED)

There are 14 directories, one for each talk.
The talks are the ones included in the training portion of MuST-C (https://ict.fbk.eu/must-c/).

A talk directory includes:
- talkurl: URL for viewing the video on the TED website
- en.json: English subtitle in JSON format, obtained from the TED website
- ja.json: Japanese subtitle in JSON format, obtained from the TED website (if any)
- SI.rank_S.tsv: Simultaneous interpretation transcripts in Japanese (by an S-rank interpreter; if any)
- SI.rank_A.tsv: Simultaneous interpretation transcripts in Japanese (by an A-rank interpreter; if any)
- SI.rank_B.tsv: Simultaneous interpretation transcripts in Japanese (by an B-rank interpreter; if any)

A JSON subtile can be converted into a tab-separated text by a tiny Python script TED_json2txt.py.
$ python3 TED_json2txt.py JSON > TSV

The transcripts are given by a tab-separated text file in UTF-8 encoding (w/o BOM).
Each column includes:
- Utterance ID in four digits
- Timestamp (beginning, in milliseconds)
- Timestamp (end, in milliseconds)
- Simultaneous interpretation transcript in Japanese
  -- (NOISE): Noise in recordings
  -- (F ...): Filler
  -- {A|B|C}: Speech error (A: the correct form, B: the reading of the correct form, C: the actual utterance)
  -- <H>: Stretched out utterance
* Please note that the timestamps may need some offsets due to the change in the eyecatch clips in the beginning of the talk videos.

