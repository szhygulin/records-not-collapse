# Empirical plan: does brain irreversibility track consciousness beyond metabolism and activity?

This plan expands §8 of the paper. It describes a study; it does not report one. Dataset details were confirmed at their landing pages on 24 November 2026. Re-check licences and versions before use.

## 1. Question

Does the entropy production, or time-irreversibility, of large-scale brain dynamics track the level of consciousness **after** controlling for signal power, signal variance, and metabolic or activity proxies?

The paper's thesis predicts **yes**. On its measure, metabolism is one factor; a **no** would mean that within brains the measure reduces to energy rate density (paper §5.3). The main rival explanation, that irreversibility just indexes how busy the brain is, predicts **no** (paper §7, objection 2).

## 2. Why this has not been settled

Three findings leave the question open:

- **Same-direction confounds.** Irreversibility falls in sleep, anaesthesia and disorders of consciousness (Sanz Perl et al. 2021; Gilson et al. 2023; Berjaga-Buisan et al. 2026). Cerebral metabolism falls in the same states: about 45% under anaesthesia (Shulman et al. 2009), and cortical metabolism by 58% under propofol (Alkire et al. 1995). Awareness has a threshold near 42% of normal cortical metabolism (Stender et al. 2016).
- **Effort raises irreversibility.** In healthy subjects, irreversibility rises with physical and cognitive effort (Lynn et al. 2021).
- **Seizures point the other way.** Consciousness is often lost in seizures, yet local intracranial irreversibility is maximal during them (Blumenfeld 2012; Schindler et al. 2016).

**Existing confound work.** No study was found that regresses large-scale irreversibility on metabolism or signal power within subjects across states of consciousness. The nearest are:

- Gilson et al. (2023) report that entropy production correlates with the variance of the model's inputs, but do not regress it out.
- Yao (2024) tracks an amplitude-related nuisance quantity in sleep EEG.
- Dmochowski & Wolpert (2026, preprint) adjust irreversibility for response amplitude, in mouse photometry rather than consciousness.

**Action before pre-registration.** Re-run this search, especially for 2025–26 work from the Deco, Kringelbach, Sanz Perl and Tagliazucchi groups, who are publishing quickly in this area.

## 3. Data

| Dataset | Modality | N | Conditions | Licence | Where |
|---|---|---|---|---|---|
| OpenNeuro **ds006623**, Michigan Human Anesthesia fMRI Dataset-1 | fMRI (task + rest), T1w | 26 | Graded propofol sedation, including behavioural unresponsiveness | CC0 | <https://openneuro.org/datasets/ds006623> |
| OpenNeuro **ds003171** (Kandeepan et al.) | fMRI (3T, TR 2 s) | 17 | Awake / light / deep sedation / recovery; rest and auditory clip | CC0 | <https://openneuro.org/datasets/ds003171> |
| OpenNeuro **ds003768** (Gu et al.) | Simultaneous 32-ch EEG + fMRI | 33 | Rest and sleep, staged per 30-s epoch | CC0 | <https://openneuro.org/datasets/ds003768> |
| PhysioNet **Sleep-EDF Expanded** | 2-ch EEG (100 Hz), EOG, EMG | 197 recordings | Whole-night sleep with hypnograms; temazepam/placebo subset | ODC-By 1.0 | <https://physionet.org/content/sleep-edfx/1.0.0/> |
| University of Cambridge repository, propofol EEG (Chennu et al. 2016) | High-density EEG | See paper | Propofol sedation with behavioural responsiveness | See repository | <https://www.repository.cam.ac.uk/handle/1810/252736> |
| PhysioNet **CHB-MIT** Scalp EEG | Scalp EEG (256 Hz, ~23 ch) | 22 paediatric patients; 198 seizures | Seizure and interictal | ODC-By 1.0 | <https://physionet.org/content/chbmit/1.0.0/> |

Notes on these datasets:

- ds003171's README, as read, does not name the sedative. Confirm it with the cited papers.
- CHB-MIT carries **no annotation of consciousness** during seizures, so seizure type must be inferred from clinical records where available. Treat it as exploratory only.

**Not openly available, or licensing unclear.**

- Lucid-dreaming EEG (Konkoly et al. 2021): available on request under a data-use agreement.
- University of Bath EEG from patients with disorders of consciousness and locked-in syndrome (doi:10.15125/bath-01632): the licence on the supporting files reads "All rights reserved", and the data are task-based.
- An OpenNeuro psilocybin dataset (ds006072): exists, but its N and modality were not confirmed.

A decisive seizure test needs data that distinguish seizures with impaired awareness from seizures with preserved awareness. That probably means a clinical collaboration.

## 4. Estimators

1. **Entropy production and probability-flux curl**, following Sanz Perl et al. (2021).
2. **Multivariate Ornstein–Uhlenbeck entropy production**, following Gilson, Tagliazucchi & Cofré (2023).
3. **Model-free trajectory irreversibility.** These estimators measure how distinguishable the process is from its time reverse (Roldán & Parrondo 2010; Kawai, Parrondo & Van den Broeck 2007). Use them on symbolised or coarse-grained signals, and on EEG via permutation patterns (cf. Yao 2024).
4. Optionally, **fluctuation–dissipation-theorem violations** from fitted whole-brain models (Deco et al. 2023; Berjaga-Buisan et al. 2026). These are reported separately because they are model-dependent.

## 5. Covariates (the confounds)

For each subject, state and parcel or channel, compute:

- **Power and variance.** Signal variance; band-limited power (EEG: delta, theta, alpha, beta, gamma); amplitude of low-frequency fluctuations (fMRI).
- **Global activity.** Global-signal amplitude; mean absolute derivative.
- **Physiology.** Heart rate and respiration, where recorded. These are nuisance physiology, not metabolic measures.
- **Metabolism.** None of the open datasets above includes PET. Treat metabolism as unmeasured in this phase, state that plainly, and plan a second phase with FDG-PET data (Alkire et al. 1995 and Stender et al. 2016 show this is feasible clinically).

## 6. Analysis

1. Preprocess with the datasets' own derivatives where they exist, for example fMRIPrep / XCP-D for ds006623, to limit analytic freedom.
2. Compute each estimator per subject × state.
3. **Surrogates.** For each signal, generate surrogates that preserve the power spectrum and the amplitude distribution but are time-symmetric in distribution. Report each estimator relative to its surrogate distribution.
4. Fit **mixed-effects models**: irreversibility ~ state (or consciousness level) + covariates + (1 | subject). Report the state effect with and without covariates.
5. **Sensitivity checks.** Vary the parcellation, the time-series length (irreversibility estimators are biased by finite samples), the coarse-graining, and the motion-scrubbing thresholds.
6. **Discriminating contrasts.**
   - Propofol unresponsiveness versus deep sedation with preserved responsiveness, where available.
   - Sleep stages at matched spectral power.
   - (Exploratory) seizure versus interictal at matched broadband power.

## 7. Predictions and decision rule (to pre-register)

- **Supports the record view.** The partial effect of consciousness level on irreversibility survives the covariates and the surrogate normalisation, with the same sign as the uncontrolled effect, across at least two independent datasets.
- **Refutes the empirical claim.** With adequate power, the partial effect is null once power, variance and activity are controlled.
- **Refutes in seizures.** Once data with awareness labels exist, if whole-brain irreversibility, net of covariates, is *higher* during seizures with impaired awareness than during conscious baseline, then the claim that irreversibility marks consciousness fails. The paper's rescue, that in seizures the brain's dynamics carry little information about its stored records, then requires an independent measure of that information. Without one, the rescue is not accepted.

**Power.** Not computed here. Base it on the effect sizes reported in Gilson et al. (2023) and Sanz Perl et al. (2021), discounted for the expected shrinkage under covariate control.

## 8. Extensions (lower priority)

- Relate irreversibility during encoding to later memory, as a crude behavioural proxy for "persistent, used records".
- Test whether irreversibility predicts consciousness better than the perturbational complexity index (Casali et al. 2013) when the two are measured together.
- Apply the same pipeline to datasets with dissociated states, such as ketamine and disorders of consciousness, if access is granted.

## 9. Risks

- Irreversibility estimators are sensitive to sampling rate, filtering and finite length. Treat these as nuisance parameters fixed in advance.
- fMRI's haemodynamic smoothing may induce or mask asymmetries.
- Without metabolic data, phase 1 can rule out only a *power or activity* explanation, not a *metabolic* one.
