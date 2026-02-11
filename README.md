[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18604834.svg)](https://doi.org/10.5281/zenodo.18604834)

Title: Collatz-12 Python Implementation
Author: Hiroshi Harada
Year: 2026
License: CC BY 4.0

Description
This archive provides a minimal and clean Python implementation of the Collatz‑12 (Duodecadia) dynamical system.
The Collatz‑12 map is defined by twelve modular rules based on n mod 12, combining:
- division operations (÷12, ÷6, ÷4, ÷3, ÷2)
- acceleration operations of the form 13n ± c
These rules generate a rich 12‑adic structure with alternating contraction and explosive growth.
A distinctive feature of the system is the Outer Rim, consisting of the residue classes
{1, 5, 7, 11} mod 12, where all ×13 accelerations occur.
Among them, Class 7 acts as the strongest accelerator, known as the Sanctuary.
Although all orbits eventually converge to 1, many numbers exhibit long, glider‑like behavior, repeatedly returning to the Rim and producing large peaks before collapsing.
This code supports numerical exploration of such Sanctuary‑driven dynamics.

Included Functions
- step12(n)
One iteration of the 12‑branch Duodecadia map.
- analyze_duodecadia(n)
Computes steps, peak value, and Rim‑hit statistics (including Sanctuary hits).
- main()
Interactive mode: enter a number and obtain its full analysis.
- hunt_sanctuary(start, end) (optional)
Scans a range of integers to search for “Sanctuary Children” — numbers that hit Class 7 unusually often.

Files in this archive
- collatz12.py — main implementation
- README.md — documentation (this file)
- LICENSE — CC BY 4.0

Purpose
This archive is intended for:
- reproducible research
- numerical experiments
- exploration of Rim dynamics and Sanctuary‑driven growth
- identification of long‑orbit “Sanctuary Children”
- investigation of near‑escape behavior in the Collatz‑12 system
The implementation is deliberately minimal to encourage modification and experimentation.

Citation
If you use this code, please cite the Zenodo DOI associated with this archive.

Contact
Hiroshi Harada
