# Investigating the Raman Modes of One Dimensional Carbon Chains

* For an explanation of the project see [Raman Spectra of Carbon Chains](https://github.com/alejandrox1/chains_nwchem/blob/master/carbon-chains.pdf)

# Benchmarks
## [Comparing Basis Sets](https://github.com/alejandrox1/chains_nwchem/tree/master/bench_basis)

* [makedir.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_basis/makedir.sh)
 This script takes as input a list of basis sets and a desired exchange correlation functional. The goal is to obtain the best combinations (see [Raman Spectra of Carbon Chains](https://github.com/alejandrox1/chains_nwchem/blob/master/carbon-chains.pdf) ).
 * [basissets.txt](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_basis/basissets.txt)
   List of basis sets
 * [FUNCTIONALS.txt](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_basis/FUNCTIONALS.txt)
   List of functionals supported by `NWCHEM` at the time of this work.
  * [acetlyne.nw](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_basis/acetylene.nw)
    [NWCHEM](http://www.nwchem-sw.org/index.php/Main_Page) file.
  * [monomer.xyz](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_basis/monomer.xyz)
    Input structure for calculations.
 * [getraman_res.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_basis/getraman_res.sh)
   Obtain all LO modes for the all the calculations performed.

To run these alculations on [Stampede](https://portal.tacc.utexas.edu/user-guides/stampede) see [STAMPEDE](https://github.com/alejandrox1/chains_nwchem/tree/master/bench_basis/STAMPEDE)
* [README](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_basis/STAMPEDE/README)
 Gives you an example on how to run the jobs on `Stampede`.
* [run_testsets.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_basis/STAMPEDE/run_testsets.sh)
 * [calc.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_basis/STAMPEDE/calc.sh)

## [Comparing Results with Similar Molecules](https://github.com/alejandrox1/chains_nwchem/tree/master/bench_mols)
* [runall.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_mols/runall.sh)
  Excuse the bad naming and lack of comments but this is a straightforward setup.
  Basically following the directory structure:
  ```
  Exchange functional and Basis Set
  |
  -----Molcule
  ```


 * [calc.nw](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_mols/calc.nw)
   Performs calculation
 * Input Structures:
    * [1-hexene.xyz](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_mols/1-hexene.xyz)
    * [224-trimethylpentane.xyz](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_mols/224-trimethylpentane.xyz)
    * [3-hexyne.xyz](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_mols/3-hexyne.xyz)
    * [benzene.xyz](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_mols/benzene.xyz)
    * [n-heptnane.xyz](https://github.com/alejandrox1/chains_nwchem/blob/master/bench_mols/n-heptnane.xyz)  


# [Preprocessing](https://github.com/alejandrox1/chains_nwchem/tree/master/calculations)
The following set of scripts run the QM calculations and perform any set up necessary.
Like always, sublist denote dependencies.

## Acetylenic Chanins
* [run_blyp-pcs0.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/run_blyp-pcs0.sh)
 * [raman_run_blyp-pcs0.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/raman_run_blyp-pcs0.sh)
    * [blyp-pcs0_acetylene.nw](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/blyp-pcs0_acetylene.nw)

* [run_bp91-pcs0.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/run_bp91-pcs0.sh)
 * [raman_run_bp91-pcs0.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/raman_run_bp91-pcs0.sh)
    * [bp91-pcs0_acetylene.nw](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/bp91-pcs0_acetylene.nw)

## Strained Acetylenic Chains
* [p_strain.py](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/p_strain.py)
  This script takes a [relaxed chain](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/get_relaxed_structures.sh) and strains it by a given amount. 

* [run_strained_blyp-pcs0.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/run_strained_blyp-pcs0.sh)
 * [raman_run_strained_blyp-pcs0.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/raman_run_strained_blyp-pcs0.sh)
    * [strained_blyp-pcs0_acetylene.nw](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/strained_blyp-pcs0_acetylene.nw)

* [run_strained_bp91-pcs0.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/run_strained_bp91-pcs0.sh)
 * [raman_run_strained_bp91-pcs0.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/raman_run_strained_bp91-pcs0.sh)
    * [strained_bp91-pcs0_acetylene.nw](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/strained_bp91-pcs0_acetylene.nw)

## Cumulenic Chains
* [run_cumul_blyp-pcs0.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/run_cumul_blyp-pcs0.sh)
 * [raman_run_blyp-pcs0_cumulene.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/raman_run_blyp-pcs0_cumulene.sh)
    * [blyp-pcs0_cumulene.nw](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/blyp-pcs0_cumulene.nw)

## Restarting Calculations
* [restart_raman.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/restart_raman.sh)
 * [acetylene_restart.nw](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/acetylene_restart.nw)
* [get_relaxed_structures.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/get_relaxed_structures.sh)

## Transfering Results
* [results_raman.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/results_raman.sh)
* [get_analysis.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/calculations/get_analysis.sh)




# [Analysis and Visualization](https://github.com/alejandrox1/chains_nwchem/tree/master/analysis_viz)
Sample output are included for the following scripts.

## Basic visualization of spectra
These scripts can be used to visualize the results from the generated `.normal` files.
* [spec.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/ANALYSIS_SCRIPTS/spec.sh) 
  Displays all the Raman spectrum.
 * [rs](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/ANALYSIS_SCRIPTS/rs)
   Gunplot add on.
* [zoom.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/ANALYSIS_SCRIPTS/zoom.sh)
  Zooms into a part of the Raman spectrum.
 * [zoom](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/ANALYSIS_SCRIPTS/zoom)
   Gnuplot add on.

## General 
* [visualize_vecs.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/visualize_vecs.sh)
  Driver script to visualize Raman modes.
 * [displacement_vectors.py](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/displacement_vectors.py)

* [Frequency-length.gnuplot](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/Frequency-length.gnuplot)
  Normal Raman plot.

* [cumulenic_acetylenic.py](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/cumulenic_acetylenic.py)
  Comparison of LO mode for acetylinic and cumulenic chains.

* [lo-change.py](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/lo-change.py)
  Size dependence of the LO mode..

* [Nwchem_espresso.py](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/Nwchem_espresso.py)
  Comparison of resoults from `Quantum Espresso` and `Nwchem`.

* [Strain.py](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/Strain.py)
  Visualize changes in frequency under applied strain.

### [Examples](https://github.com/alejandrox1/chains_nwchem/tree/master/analysis_viz/NEWER_RAMAN_RES/spectra-full)
* [PLOT_spce.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/blyp_RAMAN_RESULTS/PLOT_spec.sh)
 * [spectrum.sh](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/blyp_RAMAN_RESULTS/spectrum.sh)
    * [spectra.gnuplot](https://github.com/alejandrox1/chains_nwchem/blob/master/analysis_viz/NEWER_RAMAN_RES/blyp_RAMAN_RESULTS/spectrum.sh)

# [Structures](https://github.com/alejandrox1/chains_nwchem/tree/master/carbyne)
