## QCCalculator
![Python package](https://github.com/bigbio/qccalculator/workflows/Python%20package/badge.svg)

Development for python driven QC calculation (QCCalculator). The tool support different file formats and compute a set of metrics. The supported file formats are:

- mzML  (mass spectrometry data including spectra and chromatogram)
- idXML (peptide and protein identification information)

Metrics are grouped into different categories:

### Basic QC metrics

- Spectrum acquisition metric values - MS1: RT, SN, peakcount, int
- Spectrum acquisition metric values - MS2: -""-
- Spectra topn ranks: RT, rank
- Tandem spectrum metric values - MS2: RT, precursor_int, surveyscan_int, precursor_err, precursor_mz, precursor_c, surveyscan_max
- Trap metric values - MS1: RT, iontraptime
- Trap metric values - MS2: RT, iontraptime
- Total ion current chromatogram: RT, int

### Identification QC metrics

- Identifications accuracy metric values: RT, MZ, delta_ppm, abs_err
- Identification scoring metric values: RT, c, score
- Identifications sequence metric values: RT, peptide, target
- Hydrophobicity metric values: RT, gravy

### Install

pip install -U git+https://github.com/bigbio/qccalculator.git#egg=QCCalculator

## Dependencies
    - biopython
    - click
    - mzqc-pylib
    - pandas
    - plotly-express
    - pronto
    - pyopenms
    - requests
    - toposort

See setup.py for most recent listing.

## Development
Structure:

QCCalculator is structured as a click applications project.
The `cli.py` module contains the application code calling the metric calculation (from the other modules), data input (from pyopenms and pandas), and mzQC assembly (from mzqc-pylib).
The other modules contain metric calculation code for metric calculation and value collection split per topic of metrics.


### Contribution
For example, to add a new input from mzTab, you need a new module `mztab.py` to read the identification data. You also need to extend the command function for full QC in `cli.py`. The code should accept the results of `mztab.py`, optimally directly using the umbrella function `getIDQuality`. If that is not possible, you'd need to add a `idqcmztab.py` module to reuse the metric calculations with more direct input of values.
