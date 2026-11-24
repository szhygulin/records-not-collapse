# Literature and novelty review

Review conducted 24 November 2026 for the paper "Records, Not Collapse". The paper's §2 is the reader-facing version of this review. This file records how the review was done, the novelty verdict and its grounds, what was searched and found nothing, and the verification status of every reference.

## 1. Verdict

**Partially anticipated.** No peer-reviewed source was found that states the paper's thesis as a whole. The thesis is the conjunction of four claims:

1. If panpsychism or Russellian monism is true, then the irreversible recording event is the best physical bearer of graded proto-experience, ahead of particles, collapse events and integrated information as such.
2. Its degree tracks entropy production spent on forming persistent records that are integrated into, and used by, a self-maintaining model.
3. This is to be distinguished from erasure and from raw dissipation.
4. It is to be tested against the metabolic confound in brain data.

Each *component* has precedents.

| Component | Closest prior work | What it lacks relative to the thesis |
|---|---|---|
| (i) records, irreversibility or memory as the bearer of the mental | Whitehead's "objective immortality" of perished occasions; Hering, Butler, Semon, Bergson and Peirce on memory and habit as the mark of mind; Rovelli (2022) on the physics of traces; Fields, Glazebrook & Levin (2021); Peyru (2026, preprint) | Whitehead and the memory tradition have no thermodynamics of records. Rovelli makes no claim about experience. Fields et al. restrict their scale-free hypothesis to living systems and make no metaphysical claim. Peyru (abstract only) has no gradation by entropy spent on records and no self-model. |
| (ii) a graded measure tied to entropy production | Nonequilibrium-brain literature (Sanz Perl et al. 2021; Gilson et al. 2023; Berjaga-Buisan et al. 2026); Ito, Oizumi & Amari (2020); Ganesh (2020); Noirmont (2026, preprint) | The empirical work is about markers in brains only. Ito et al. give a formal bridge with no claim about experience. Ganesh gives necessary conditions, not gradation. Noirmont proposes an emergentist threshold. |
| (iii) self-maintenance and self-modelling as amplifiers | Kolchinsky & Wolpert (2018) on semantic information; the free-energy principle (Friston 2010, 2013); Solms & Friston (2018); Levin (2019) | No link to records as bearers of experience, and no comparative argument against other loci. |

**Grounds for the novelty claim.** The paper claims novelty only for three things:

- the conditional, comparative argument across the four candidate loci;
- the explicit contrast between the clock-observers of quantum gravity and recorder-observers, with the missing "bridge theorem" named;
- the measure sketch that uses Still et al. (2012) and Sagawa & Ueda (2009) to separate integrated recording from erasure and from non-predictive dissipation, together with an empirical test designed against the metabolic confound.

**Effect on the paper's framing.** No change to the thesis was needed. The paper cites the partial anticipations in §2 and states what it adds (§2.10). Two framings *were* narrowed by the review, and the details are in `corrections.md`:

- Quantum-gravity observers are not all pure clocks. Harlow, Usatyuk and Zhao's observer is decohered.
- The brain evidence is confounded by metabolism, and local seizure data point the other way.

**Caveat.** Most of the closest hits on component (i) are unreviewed 2025–26 preprints whose full texts were not read. A specialist in process philosophy or in panpsychism might know older work that the searches missed. Searches of PhilPapers could not be run (HTTP 403 from the fetch tools). That gap matters most for the Whitehead literature.

## 2. Method

Network access from the authoring machine was limited, so the scholarly APIs were reached through fetch tools. The searches were split into six clusters, run in parallel, plus two follow-up passes to close gaps.

| Cluster | Scope |
|---|---|
| A | Observers in quantum gravity and quantum foundations |
| B | Thermodynamics of records, memory, agency and life |
| C1 | Panpsychism, process philosophy, the memory tradition, illusionism, unity of the self, AI consciousness |
| C2 | Orch-OR and collapse, IIT and its critics, the free-energy principle |
| D | Nonequilibrium brain dynamics, the metabolic confound, seizures, estimators, open datasets |
| E | Novelty search |
| F | Numbers for §5.6: brain energetics and memory; GPU hardware, language-model architecture, inference and training energy. Each value was found in one pass and re-checked against the source by a second, independent pass. Details are in `analysis/sources.md`. |

**Sources queried.**

- arXiv API, Crossref API, OpenAlex, Semantic Scholar (often rate-limited), Europe PMC and PubMed
- OpenLibrary and archive.org, for books and historical texts
- The Stanford Encyclopedia of Philosophy and the Internet Encyclopedia of Philosophy, for secondary characterisations
- Publisher pages, where reachable
- OpenNeuro (via its GitHub mirrors), PhysioNet and DataCite, for datasets
- A general web search, used to cross-check the novelty results and to confirm the metadata of *Journal of Consciousness Studies* papers

### 2.1 Novelty searches run

The searches were run on OpenAlex, Semantic Scholar and arXiv, with variants:

- irreversible record consciousness; irreversibility panpsychism; thermodynamic panpsychism
- entropy production consciousness theory; dissipation consciousness
- "proto-experience" thermodynamics; "entropy" "proto-consciousness"
- Landauer consciousness; Landauer integrated information; dissipation integrated information theory
- memory panpsychism physics; "trace" "experience" irreversibility physics
- arrow of time consciousness; consciousness and the second law; "thermodynamic theory of consciousness"; "free energy" "irreversibility" consciousness
- "quantum Darwinism" consciousness; decoherence panpsychism "actual occasions"; Whitehead decoherence irreversibility
- "records" observer consciousness physics; "information gathering and utilizing system" consciousness; "semantic information" consciousness
- "temporal asymmetry" consciousness panpsychism

A general web search was also run for: panpsychism + irreversible + records + memory + proto-experience + entropy production; and consciousness + arrow of time + panpsychism + Whitehead + decoherence.

### 2.2 Searches that returned nothing relevant

- arXiv: irreversible + panpsychism; records + consciousness + irreversib\*; panpsychism + thermodynamic/entropy/dissipative; "quantum darwinist" + consciousness.
- OpenAlex: Whitehead + irreversibility + decoherence; Whitehead + entropy + "actual occasion" + thermodynamic; "temporal asymmetry" + consciousness + panpsychism; "time irreversibility" + "integrated information"; "degrees of consciousness" + "entropy production"; consciousness + "second law" + memory traces.
- Web search: no source linking Whitehead's actual occasions to decoherence, irreversibility or entropy production.
- Quantum gravity: no gravitational-algebra or closed-universe paper was found that gives the observer memory, records or dissipation. No dedicated memory-keyword sweep of hep-th was run, so this negative is not exhaustive.

### 2.3 Other near hits not used in the paper

- arXiv:2204.07164, "A Higher Dimension of Consciousness: Constructing an empirically falsifiable panpsychist model of consciousness". A web-search summary says it links memory formation to awareness and discusses entropy generation. The arXiv record could not be retrieved (HTTP 429), so it is **[UNVERIFIED]**.
- "Panexperiential materialism: A physical exploration of qualitativeness in the brain", *Advances in Quantum Chemistry* (2020), pp. 301–367, doi:10.1016/bs.aiq.2020.08.004. No author or abstract was available in the Crossref record, so it is **[UNVERIFIED content]**.
- Further 2025–26 preprints found by the novelty search and judged less close: Nagae (2026, Landauer-type discard and the present moment); Yun (2026, time as the irreversible accumulation of distinctions); Yashchenko (2026, "information monism"); Fagan (2025, arXiv:2601.00021); Waterman (2025, 2026); Lugten (2024); Hamza (2026); Priiz (2026); van Santen (undated); Lahtee (2026); Awata (2026, *AIP Advances*); Helo Juan-Oliver (2025); Manco (2023). These were read at abstract level only and are not cited.

## 3. Unverified or dropped items

The paper does not use these.

| Item | Why it was dropped |
|---|---|
| Penrose's "1 in 10^(10^123)" estimate (*The Emperor's New Mind*, 1989) | No readable text; every archive.org scan is restricted |
| Wheeler, "Law without law" (1983), and the phrase "irreversible act of amplification" | The text could not be read, and the 1983 chapter metadata was not confirmed |
| Hameroff & Penrose (2014) on ubiquitous, non-orchestrated OR events as proto-conscious moments | Full text blocked (403); only the abstract was read |
| A passage in Strawson (2006) on vitalism or the emergence of life | No readable full text; SEP's account mentions only the liquidity analogy |
| Number of signatories of the 2023 IIT letter | The PDF timed out |
| Seager (1995), JCS 2(3):272–288 | Metadata from secondary citations only; not needed |
| Chalmers (2013), "Panpsychism and panprotopsychism" | Metadata secondary only; not needed |
| Deacon (2011), *Incomplete Nature* | Catalogue records disagree on the year (2011 or 2012); not needed |
| Reichenbach (1956); Thompson (2007); Dennett (1991) | Metadata confirmed but not needed |
| Shimony (1965); Kastner, Kauffman & Epperson (2018) | Not fetched (rate limits) |
| van der Heyden et al. (1996) on EEG time-reversibility | Not located |
| Yao et al. (2020) on permutation irreversibility in epileptic EEG | Metadata only; the direction of the effect is unknown |
| Lan et al. (2013), "A clock directly linking time to a particle's mass" | Metadata confirmed. Neither the content nor the published critiques could be checked, so the de Broglie–Compton clock point is made from physics without this citation |
| Lucid-dreaming EEG data of Konkoly et al. (2021) | Available only on request, so not an open dataset |
| Open ketamine fMRI dataset | None found |

## Appendix A. Verification status of every reference in `paper/references.bib`

Tiers:

- **A**: metadata confirmed from a primary record, *and* the specific claim the paper makes was checked against the source's text or abstract.
- **B**: metadata confirmed from a primary record (Crossref, arXiv, publisher, Europe PMC, OpenLibrary or archive.org). The paper uses the work only for what its title, abstract or a verified secondary source (SEP, IEP, publisher blurb) states, or for its standard characterisation.
- **S**: metadata confirmed only through secondary citations, such as an author eprint, a PhilPapers or PhilArchive listing, or repository records. These are *Journal of Consciousness Studies* papers, which carry no DOIs.
- **P**: an unreviewed preprint. Only the abstract was read.
- **D**: a dataset, confirmed at its landing page or repository.

| Key | Tier | Note |
|---|---|---|
| chandrasekaran2023 | A | arXiv text: observer definition, Type II₁, entropy, maximum-entropy state |
| witten2024background | A | arXiv text: observer as worldline plus clock |
| witten2024algebras | A | arXiv text: "recording device" sentence |
| harlow2026 | A | arXiv text: observer assumptions (pointer states, entanglement) |
| abdalla2025 | A | Abstract |
| akers2025 | A | Abstract |
| liu2025 | A | Abstract |
| antonini2025 | A | Abstract |
| nomura2025 | A | Abstract |
| mcnamara2020 | A | Abstract |
| marolf2020 | A | Abstract |
| maldacena2026 | A | arXiv text, §§1–4.2 |
| devuyst2025 | A | Abstract |
| elshatlawy2025 | A | Text of an earlier version; v3 not checked |
| everett1957 | B | Metadata only; the "servomechanisms" quote is from the 1956 thesis via SEP |
| sep-everett | A | SEP entry read |
| hartle2005 | A | arXiv text (memory registers) |
| gellmann2018 | A | Abstract (IGUS definition) |
| halliwell1999 | A | Abstract |
| zurek2003 | A | Abstract |
| zurek2009 | B | Metadata only; standard characterisation of quantum Darwinism |
| zurek2018 | A | Abstract (record-holder sentence) |
| rovelli1996 | A | Abstract |
| dibiagio2021 | A | Abstract |
| brukner2018 | A | Abstract |
| bong2020 | A | Abstract |
| wiseman2023 | A | Abstract |
| erker2017 | A | Abstract |
| pearson2021 | A | Abstract |
| milburn2020 | A | Abstract |
| guryanova2020 | A | Abstract |
| landauer1961 | B | Metadata; content via Bérut et al. abstract |
| bennett1982 | B | Metadata only |
| bennett2003 | B | Metadata only (title-level use) |
| berut2012 | A | Abstract |
| sagawa2009 | A | ar5iv text (inequalities) |
| parrondo2015 | B | Metadata only (cited as a review) |
| still2012 | A | ar5iv text (per-step equality, total bound) |
| kolchinsky2018 | A | Abstract (definition of semantic information) |
| wolpert2019 | A | Crossref abstract |
| wolpert2024 | A | Crossref abstract |
| mlodinow2014 | A | Abstract |
| golosz2025 | A | Crossref abstract |
| rovelli2022 | A | arXiv v1 text |
| rovelli2020agency | A | ar5iv text |
| rovelli2021panpsychism | A | Abstract (via OpenAlex) |
| fields2014 | A | ar5iv text |
| seifert2012 | A | arXiv abstract |
| ito2020 | A | Abstract |
| lan2012 | A | Abstract |
| mehta2012 | A | Abstract |
| england2013 | A | Abstract |
| england2015 | A | Abstract; the term is in the title |
| perunov2016 | A | Abstract and arXiv text |
| marletto2015 | A | Abstract |
| schrodinger1944 | B | OpenLibrary; cited only as a pointer to the physics-of-life tradition |
| prigogine1978 | B | Europe PMC metadata; pointer only |
| maturana1980 | B | OpenLibrary; pointer only |
| levin2019 | B | Crossref metadata; pointer only |
| chaisson2001 | B | OpenLibrary; concept of energy rate density |
| chaisson2011 | B | Crossref metadata; text closed |
| chaisson2014 | A | PMC full text (the numbers quoted) |
| hackermuller2004 | A | ar5iv text (visibility figures) |
| albert2000 | B | OpenLibrary; standard reference for the Past Hypothesis |
| albrecht2004 | A | Abstract |
| dyson2002 | A | Abstract |
| carroll2017 | A | Abstract |
| connes1994 | A | Abstract |
| jacobson1995 | A | Abstract |
| page1983 | B | Metadata; mechanism described via Moreva et al. abstract |
| moreva2014 | A | Abstract |
| schulman1999 | B | Crossref metadata; title-level use |
| russell1927 | B | OpenLibrary and a Coleman (2014) reference list; content via SEP |
| alter2015 | B | OpenLibrary |
| strawson2006 | S | JCS 13(10–11):3–31 per PhilPapers listing and other secondary records; argument via SEP |
| goff2017 | B | Crossref; content via SEP |
| goff2019 | B | OpenLibrary and Wikipedia; content via SEP |
| goff2023 | A | Crossref chapter abstracts |
| chalmers2016 | B | Crossref; title-level use |
| nagasawa2016 | B | Crossref; content via SEP |
| coleman2014 | B | Crossref; title-level use |
| james1890 | A | Text at York "Classics in the History of Psychology", p. 160; archive.org scan |
| shani2015 | B | Crossref; content via SEP |
| kastrup2018 | S | JCS 25(5–6):125–155 per PhilArchive listing and Wikipedia citations; OpenAlex confirms volume |
| miller2018 | A | Crossref abstract |
| whitehead1929 | A | archive.org scan text (perishing / objective immortality passage) |
| griffin1998 | B | OpenLibrary description |
| epperson2004 | B | OpenLibrary blurb |
| stapp2007 | B | OpenLibrary; content via Wikipedia |
| hering1870 | A | archive.org scan (2nd ed., 1876) |
| butler1880 | A | archive.org scan, p. 105 |
| semon1904 | B | archive.org metadata |
| bergson1911 | A | archive.org text, pp. 295–297 |
| peirce1891 | A | Wikisource text; the page range is weakly sourced |
| frankish2016 | S | Pages per author eprint and secondary citations |
| dennett2016 | S | Pages per secondary citations |
| penrose1996 | B | Crossref |
| diosi1989 | B | Crossref |
| hameroff2014 | B | Crossref and Europe PMC; abstract-level claim only |
| hameroff2008 | B | Crossref; title-level use |
| donadi2021 | A | arXiv abstract |
| tegmark2000 | A | Abstract |
| chalmers2021 | A | Abstract |
| tononi2004 | B | Crossref |
| tononi2016 | B | Europe PMC |
| albantakis2023 | A | Abstract |
| aaronson2014expander | A | Blog post read |
| aaronson2014phinal | A | Blog post read (Tononi quotations) |
| iitconcerned2023 | A | OSF record; first sentence read |
| iitconcerned2025 | B | Europe PMC and OpenAlex metadata |
| cogitate2025 | A | PMC full text (abstract sentences quoted) |
| casali2013 | B | Europe PMC |
| friston2010 | B | Europe PMC |
| friston2013 | B | Europe PMC |
| friston2019 | B | arXiv |
| solms2018 | S | OpenAlex and UCL repository; issue number from a repository string |
| fields2021 | A | PMC full text, first ~40k characters (quotes) |
| fields2022 | B | Europe PMC |
| sethbayne2022 | B | Europe PMC |
| ganesh2020 | A | arXiv abstract |
| pinto2017 | B | Crossref; title-level use |
| bayne2010 | B | OpenLibrary |
| schechter2018 | B | OpenLibrary (title corrected from the brief) |
| carhartharris2014 | B | Europe PMC |
| carhartharris2018 | A | Abstract |
| metzinger2020 | B | Crossref |
| metzinger2024 | B | Crossref and OpenAlex (open-access status) |
| chalmers2023 | A | arXiv abstract |
| butlin2023 | A | arXiv abstract |
| behrouz2024 | A | arXiv abstract and submission date |
| sun2024 | A | arXiv abstract |
| sanzperl2021 | A | APS abstract |
| gilson2023 | A | arXiv HTML text (numbers) |
| gguzman2023 | A | Abstract |
| deco2022insideout | A | Abstract |
| deco2023arrow | A | Abstract (via OpenAlex) |
| deco2023fdt | B | Crossref metadata; title-level use |
| lynn2021 | A | Significance statement |
| delafuente2023 | A | Crossref abstract |
| nartallo2026 | B | Crossref metadata (cited as a review by title) |
| stikvoort2025 | A | Crossref abstract |
| martinezmarin2025 | P | bioRxiv abstract |
| berjagabuisan2026 | A | Europe PMC abstract |
| yao2024 | A | Europe PMC abstract |
| dmochowski2026 | P | bioRxiv abstract |
| guevaraerra2016 | A | Abstract |
| shulman2009 | A | Abstract |
| stender2016 | A | Abstract |
| alkire1995 | A | Abstract |
| blumenfeld2012 | A | Abstract |
| schindler2016 | A | Abstract |
| roldan2010 | B | Crossref; standard characterisation of the estimator |
| kawai2007 | B | Crossref; standard characterisation |
| chennu2016 | A | PLOS article page (data availability) |
| konkoly2021 | A | PMC author manuscript (data availability) |
| ds003171 | D | OpenNeuro dataset_description and participants files |
| ds006623 | D | OpenNeuro dataset_description |
| ds003768 | D | OpenNeuro dataset_description |
| sleepedfx | D | PhysioNet landing page |
| chbmit | D | PhysioNet landing page |
| peyru2026 | P | Abstract via OpenAlex |
| noirmont2026 | P | Abstract via OpenAlex |
| yuan2026 | P | Abstract via OpenAlex |
| devine2026 | P | Abstract via OpenAlex |
| schneider2026 | P | Book chapter; abstract via OpenAlex |
| balasubramanian2021 | A | PMC full text: ~20 W, 17–20 W from glucose uptake (§5.6) |
| herculanohouzel2012 | A | PMC full text: brain ~1.5 kg (§5.6) |
| tang2001 | B | Europe PMC abstract: $1.64\times10^{14}$ neocortical synapses |
| lennie2003 | A | Author PDF: 0.16 and 0.94 spikes/s/neuron sustainable |
| engl2015 | A | Europe PMC full text: signalling ≥ 55%; protein synthesis ≤ 1.3% |
| howarth2012 | A | PMC full text: postsynaptic glutamate receptors 50% of signalling |
| karbowski2019 | A | arXiv text of the published paper: plasticity 4.0–11.2% of fast transmission |
| girard2023 | P | arXiv full text read: ~10 mJ/bit for long-term memory in Drosophila |
| bartol2015 | A | Europe PMC full text: 26 strengths, 4.7 bits per synapse |
| landauer1986 | A | PDF text: ~$10^9$ bits; 1.2 and 2.3 bit/s; loss rate Table 1 |
| zheng2025 | A | arXiv v2 text and Europe PMC record: ~10 bit/s behaviour, ~$10^9$ bit/s sensory |
| attardo2015 | A | PMC full text: mean spine lifetime ~1–2 weeks (mouse CA1) |
| holtmaat2005 | B | Europe PMC abstract: most thick neocortical spines persist for months |
| stuart1998 | A | PMC full text: membrane time constant 12.4 and 20.9 ms |
| nvidiah100 | A | Vendor page: 700 W TDP; 1,979 TFLOPS BF16 with sparsity |
| andersch2022 | A | Vendor blog: 814 mm², 80 billion transistors, 1000 TFLOPS dense (preliminary) |
| grattafiori2024 | A | arXiv PDF: Table 3 architecture; Table 4 utilisation; 16K GPUs |
| henins1964 | A | PMC full text: silicon density 2.329 g/cm³ |
| svmisv029 | A | Vendor sheet: 300 mm wafer 775 ± 25 µm |
| samsi2023 | A | arXiv text: 3–4 J per output token, LLaMA 65B (estimate) |
| elsworth2025 | A | arXiv text: 0.24 Wh median Gemini Apps text prompt |
| meta2024 | A | GitHub model card: 30.84M H100 hours for 405B at 700 W |
| patterson2021 | A | arXiv text: GPT-3 1,287 MWh |
| allenzhu2024 | A | arXiv text: 2 bits of knowledge per parameter |
| mlcommons2024 | D | MLPerf v4.1 result log on GitHub: 21,605.79 tokens/s, Server scenario |
