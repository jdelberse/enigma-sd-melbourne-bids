# Christchurch Dataset (`melbourne-bids`)

## Overview

*NB*: This dataset was shared and maintained under the name `melbourne-bids`. The name could not be changed, so the dataset is otherwise referred to as the Christchurch sample.

This dataset contains MRI data from a sleep manipulation study conducted at the New Zealand Brain Research Institute. It is part of the ENIGMA-Sleep Working Group collection used to study the effects of sleep loss on glymphatic MRI indices. The data are organized according to the Brain Imaging Data Structure (BIDS) and managed with DataLad (git-annex).

## Sample

| Item | Value |
|---|---|
| Site | Christchurch |
| Affiliation | New Zealand Brain Research Institute |
| Country | New Zealand |
| Participants (N) | 16 |
| Age, mean (SD), years | 24.8 (5.1) |
| Male (%) | 50.0 |

## Sleep protocol

- **SR**: sleep restriction, 3 h time in bed (TIB)

Participants were scanned under baseline and sleep manipulation conditions.

## Imaging data

### T1-weighted (`anat/`)

| Parameter | Value |
|---|---|
| Scanner | GE Signa HDx |
| Sequence | BRAVO |
| TR (ms) | 6.5 |
| TE (ms) | 2.80 |
| TI (ms) | 400 |
| Flip angle (°) | not reported |

## Data organization

- `sub-<ID>/ses-<label>/`: raw BIDS data (`anat/`)
- `participants.tsv`: participant-level information
- `sub-<ID>/sub-<ID>_sessions.tsv`: session-level information (condition, visit, date, time)
- `derivatives/`: processed outputs, if present

File contents are tracked with git-annex. After cloning, retrieve data with `datalad get <path>`.

## Original publication

Poudel, G. R., Innes, C. R. H., & Jones, R. D. (2018). Temporal evolution of neural activity and connectivity during microsleeps when rested and following sleep restriction. *NeuroImage*, 174, 263–273. [https://doi.org/10.1016/j.neuroimage.2018.03.031](https://doi.org/10.1016/j.neuroimage.2018.03.031)

## Contact

- Jorik D. Elberse: [j.elberse@fz-juelich.de](mailto:j.elberse@fz-juelich.de)
- Masoud Tahmasian: [m.tahmasian@fz-juelich.de](mailto:m.tahmasian@fz-juelich.de)

