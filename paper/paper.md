---
title: "Records, Not Collapse: Irreversible Recording as the Physical Locus of Proto-Experience"
author: "Viacheslav Zhygulin (<s.zhygulin@gmail.com>)"
date: "Draft of November 2026. Speculative position paper, not peer-reviewed."
abstract: |
  Panpsychist and Russellian-monist views place experience, or proto-experience, in the basic physical world, but have no agreed answer to *where* in physics it sits. Classic panpsychism puts it in particles, orchestrated objective reduction (Orch-OR) in gravitational wavefunction collapse, and integrated information theory (IIT) in integrated cause–effect structure. This paper argues, conditionally, that if any such view is true, the natural physical bearer of graded proto-experience is the *irreversible recording event*: the formation of a persistent, decohered record, which produces entropy. On this view a system's degree of experience tracks the entropy it spends, per gram, on forming persistent records that are integrated into its model of itself. The paper first surveys work in quantum gravity, quantum foundations, the thermodynamics of information, theories of consciousness and nonequilibrium neuroscience, and finds the thesis partially anticipated but not stated as a whole. It then separates clock-observers, which recent quantum-gravity work needs, from recorder-observers, which facts need, and names the missing theorem that would join them. On the way to the measure, weighting information by dissipation per gram, as a check on information-only measures, removes IIT's verdict that an inactive grid of logic gates is highly conscious, but favours computers over brains. Contrast cases follow: hot molecules, logic-gate grids, sleep, seizures and language models. A language model at inference forms no lasting internal records and scores near zero, whatever its hardware. The paper answers seven objections and ends with a pre-registrable test: does the time-irreversibility of brain dynamics still track consciousness once metabolism and signal power are controlled for?
bibliography: references.bib
link-citations: true
---

# Summary of claims

The paper's claims, numbered so that critics can target them separately. Each is marked as an established result **[E]**, a contested result **[C]**, or this paper's own proposal **[P]**.

1. **[E]** Recent algebraic work on de Sitter space and closed universes introduces an observer modelled as a clock: a degree of freedom whose energy is bounded below. Some models add decoherence, but none gives the observer memory, records or a thermodynamic arrow (§2.5).
2. **[E]** A long line of work in quantum foundations and thermodynamics ties facts to irreversible records, and records to entropy production (§2.6–2.7).
3. **[P]** No known result shows that quantum gravity *requires* a recording observer with a thermodynamic arrow. That missing theorem is the bridge any physics-based account of experience would need (§3.1).
4. **[P]** Observerhood is graded: clock, irreversible record, record used for self-maintenance, record integrated into a self-model (§3.2).
5. **[P]** *Conditional on* panpsychism or Russellian monism, the irreversible recording event is a better bearer of graded proto-experience than the particle, the collapse event or integrated information as such (§3.3).
6. **[P]** The degree of proto-experience tracks the entropy a system spends, per gram, on forming persistent records that are integrated into its model of itself, schematically $R = \frac{1}{M}\sum_r \Delta S_r\, p_r\, u_r$. Dissipation without such records, as in a star or a jet engine, does not count, and nor does integrated structure that forms none, as in a grid of logic gates. Weighting information by dissipation per gram, $E\,I/M$, removes the verdict of information-only measures that an inactive grid is highly conscious, but it still ranks processors above brains (§4).
7. **[C]** In brains, the time-irreversibility of large-scale dynamics falls in sleep, anaesthesia and disorders of consciousness (§2.8). Whether this survives controls for metabolism and signal power is open, and local seizure data point the other way (§5.3).
8. **[P]** The thesis makes comparative predictions inside brains that can be tested on open data, and it states what would refute it (§8–9).
9. **[P]** Per gram, a GPU die dissipates about $4\times10^4$ times as much as a brain, so measures built on dissipation, $E\,I/M$ included, favour chips. On the record measure, a language model at inference scores near zero whatever its hardware: it forms no internal records that outlast a request, and it integrates nothing it records into a self-model. In training a model forms lasting records, at a cost per retained bit not clearly below a brain's, so there the verdict rests on the integration term $u_r$, the measure's least formalised part (§5.6).

# 1. Introduction

Panpsychism and its relatives have returned to serious philosophy of mind. The motivation is familiar. Physics describes the structure and dynamics of matter, not its intrinsic nature. Experience is the one intrinsic nature we know directly. So perhaps experience, or some proto-phenomenal precursor of it, *is* that intrinsic nature [@russell1927; @strawson2006; @goff2017; @alter2015]. Whatever one makes of the argument, it leaves a question that its defenders have mostly left open: **which physical events or structures carry the proto-experience?** The answer matters. It fixes which systems have more experience and which have less. It shapes the combination problem. And it decides whether the view makes any contact with evidence.

Three answers dominate. The oldest says proto-experience belongs to the fundamental particles or fields themselves. Orch-OR says it belongs to moments of objective reduction, a gravitationally induced collapse of the wavefunction [@penrose1996; @hameroff2014]. IIT says it belongs to integrated cause–effect structure, measured by $\Phi$ [@tononi2004; @tononi2016; @albantakis2023]. IIT is not a panpsychism in the strict sense, but it shares the feature that matters here: it locates experience in a physical property that many non-living systems have.

This paper defends a fourth answer, *conditionally*. It does not argue that panpsychism is true. It argues that **if** one wants a physically grounded, graded proto-experience, then the best physical bearer is the *irreversible recording event*. Such an event leaves a trace that persists, cannot in practice be undone, and costs entropy to make. The degree of experience then tracks **the entropy a system spends, per gram, on forming persistent records that it integrates into a model of itself**. Recording events are the bearers; the measure grades how much recording a system does for itself.

The thesis draws on three bodies of work that rarely meet.

- **Quantum gravity.** Recent work introduces "observers" to define algebras of observables and finite entropies. These observers are clocks, not recorders [@chandrasekaran2023; @witten2024algebras; @harlow2026].
- **Quantum foundations and the thermodynamics of information.** Here facts are tied to records, and records to dissipation [@zurek2018; @rovelli2022; @landauer1961; @still2012; @kolchinsky2018].
- **Neuroscience.** Here the time-irreversibility of large-scale brain dynamics falls when consciousness is lost [@sanzperl2021; @gilson2023; @berjagabuisan2026].

The paper's contribution is to join these into one conditional argument, to make the joint explicit, and to say what would break it. For a survey of scientific theories of consciousness against which this one should be read, see @sethbayne2022.

Because the thesis lives or dies by its relation to prior work, the paper begins with a long literature overview (§2). It ends with a verdict on novelty. The argument follows in §3, a sketch of a measure in §4, contrast cases in §5, cosmological context in §6, objections in §7, a proposed empirical test in §8, and the author's credences in §9. Tangents such as thermal time and opposite arrows of time are confined to one paragraph (§6.2).

# 2. Literature overview

This section surveys nine literatures. For each it separates what is established from what is contested, and it notes what each contributes to, or takes from, the thesis. A summary table and a novelty verdict close the section (§2.10). The method and the full list of sources checked, with the verification status of each, are in the repository's `notes/literature-review.md`.

## 2.1 Panpsychism, Russellian monism and the location problem

Russellian monism starts from the observation that physics gives the relational or dispositional profile of matter and is silent on what has that profile. The silence leaves room for an intrinsic nature that also accounts for consciousness [@russell1927; @alter2015]. Strawson argued that a physicalist who takes experience seriously must accept panpsychism. Experience cannot emerge intelligibly from wholly non-experiential matter, in the way that liquidity emerges from molecules that are not liquid [@strawson2006]. Goff developed a Russellian panpsychism and later a cosmopsychist variant [@goff2017; @goff2019]. More recently he defended a teleological reading on which the universe is directed toward goals [@goff2023].

The central difficulty is the **combination problem**. William James stated it early. However many feelings are put together, "still each remains the same feeling it always was, shut in its own skin, windowless", and no further feeling of the whole arises without something more [@james1890, p. 160]. Chalmers surveys the problem in its contemporary forms [@chalmers2016], and Coleman locates the "real" combination problem in the relation between micro-subjects and emergence [@coleman2014]. **Cosmopsychism** reverses the direction of explanation: the cosmos is the basic subject and individual minds are derived from it [@shani2015; @nagasawa2016; @kastrup2018]. Miller showed that this only relocates the difficulty. Cosmopsychism faces a "de-combination problem" of explaining how subjects can be proper parts of a subject [@miller2018].

For present purposes the important point is negative. Neither the panpsychist nor the cosmopsychist literature has converged on a *physical* criterion for where proto-experience is concentrated. Particles are the default because they are fundamental, not because anything about their dynamics marks them out. Rovelli has suggested that the pervasive relationalism of modern physics partly supports the panpsychist idea of a monist continuity between mind and matter, while undermining its stronger forms [@rovelli2021panpsychism]. That suggestion concerns relations in general, not irreversible ones. The present thesis is an answer to the location problem that panpsychists inherit.

## 2.2 Process philosophy and the memory tradition

Two older traditions come closer to the thesis than contemporary panpsychism does.

The first is **Whitehead's process philosophy**. For Whitehead the basic units are "actual occasions", momentary processes of experience. Each takes up, or "prehends", the data of its past and integrates them [@whitehead1929]. Once complete, an occasion perishes as a subject but persists as a datum for later occasions: "actual entities 'perpetually perish' subjectively, but are immortal objectively. Actuality in perishing acquires objectivity, while it loses subjective immediacy" [@whitehead1929]. Whitehead called this the "objective immortality" of actual entities. Structurally, that is a theory in which every completed event leaves an indelible record that later events must take account of. Griffin developed it into a "panexperientialist" physicalism [@griffin1998]. Others have connected it to quantum theory: Epperson through an analysis of quantum mechanics alongside Whitehead's cosmology [@epperson2004], Stapp through a consciousness-based account of collapse [@stapp2007].

As far as this review could find, none of this work identifies the Whiteheadian occasion with *thermodynamically irreversible record formation*, or grades experience by the entropy spent on persistent records integrated into a self-model. The searches for such a link, which combined Whitehead's terms with decoherence, irreversibility and entropy, returned nothing relevant (see `notes/literature-review.md`).

The second tradition treats **memory as the mark of the mental**. In an 1870 lecture to the Vienna Academy, the physiologist Ewald Hering described memory, or the "power of reproduction", as a basic faculty (*Grundvermögen*) of organised matter [@hering1870]. Samuel Butler's English rendering made it "one and the same primary force of organised matter — namely, its memory or power of reproduction" [@butler1880, p. 105]. Semon's theory of the "mneme" extended the idea [@semon1904]. Bergson made the contrast between matter and mind a contrast of memory. Pure perception is "mind without memory" and is part of matter, while spirit is marked by memory: "If matter does not remember the past, it is because it repeats the past unceasingly" [@bergson1911, pp. 295–297]. Peirce's objective idealism held that "matter is effete mind, inveterate habits becoming physical laws" [@peirce1891].

These authors anticipate the *form* of the present thesis. What separates mind from mere matter, on their views, is the retention of the past. What they lack is any physical account of what retention costs or why it is irreversible. That is the part the thermodynamics of information later supplied (§2.7).

## 2.3 Collapse-based accounts: Orch-OR

Penrose proposed that superpositions of sufficiently different mass distributions undergo an objective, gravitationally induced reduction [@penrose1996]. A closely related proposal had come from Diósi [@diosi1989]. Hameroff and Penrose combined this with a hypothesis about microtubules in neurons. On their Orch-OR theory, orchestrated reduction events in the brain give rise to moments of conscious awareness or choice [@hameroff2014]. Hameroff and Powell set out a panprotopsychist extension, linking the brain to what they called "pan-experiential quantum geometry" [@hameroff2008].

Two empirical results bear on this. Tegmark estimated decoherence times for neural degrees of freedom of roughly $10^{-13}$ to $10^{-20}$ s, against neural dynamical timescales of $10^{-3}$ to $10^{-1}$ s. He concluded that the cognitively relevant brain degrees of freedom are effectively classical [@tegmark2000]. More recently, an underground experiment at the Gran Sasso laboratory searched for the spontaneous radiation that the Diósi–Penrose model predicts. Its result "rules out the natural parameter-free version of the Diósi–Penrose model" [@donadi2021]. Versions with free parameters survive.

A neighbouring proposal reverses the order of explanation. Chalmers and McQueen combine IIT with continuous spontaneous localisation, so that consciousness triggers collapse. They find that simple versions are falsified by the quantum Zeno effect and that more complex ones might be tested with quantum computers [@chalmers2021].

For the thesis, the lesson is this. Collapse-based loci require new physics that is under increasing experimental pressure. A record-based locus needs only decoherence and thermodynamics, which are not in question.

## 2.4 Integrated information theory and its critics

IIT holds that consciousness is identical to a maximally irreducible cause–effect structure, quantified by integrated information $\Phi$ [@tononi2004; @tononi2016]. Its latest version states that "the postulates can be applied to any system of units in a state to determine whether it is conscious" [@albantakis2023]. That makes IIT the most explicit *physical-locus* theory on the market, which is why it is the main rival here.

Three lines of criticism matter.

**Counterexamples.** Aaronson exhibited simple linear-algebraic systems with very large $\Phi$ that do nothing intelligent. His original construction used a Vandermonde matrix over a finite field, with expander-graph or LDPC-code networks of logic gates as sparse physical realisations [@aaronson2014expander]. In the exchange that followed, Tononi accepted the consequence. Aaronson reports him as holding that, by IIT's lights, "even a network of XOR gates arranged in a 2D square grid is conscious", and that "the causal relationships that make up 2D space obtain whether the elements are on or off" [@aaronson2014phinal]. The 2D XOR grid thus comes from Tononi's reply, not from Aaronson's first post.

**Scientific status.** In 2023 a group signing as "IIT-Concerned" circulated an open letter calling IIT pseudoscience [@iitconcerned2023]. A version of the argument later appeared in *Nature Neuroscience* [@iitconcerned2025].

**Adversarial testing.** The Cogitate Consortium preregistered a test of IIT against the global neuronal workspace theory (GNWT), using fMRI, MEG and intracranial EEG in 256 participants. The results matched some predictions of each theory and substantially challenged key tenets of both. For IIT they found "a lack of sustained synchronization within the posterior cortex". For GNWT they found "the general lack of ignition at stimulus offset" [@cogitate2025].

One formal result points in the direction of the present thesis. Ito, Oizumi and Amari unified the entropy production of stochastic thermodynamics with "stochastic interaction", an integration measure from the IIT literature. They describe their framework as "a thermodynamic foundation of the integrated information theory" [@ito2020]. Integration and dissipation are therefore not foreign to each other.

## 2.5 Observers in physics I: the observer as a clock

A strand of recent quantum-gravity research reintroduces the observer, in a deflationary role.

**De Sitter space.** Chandrasekaran, Longo, Penington and Witten showed that the algebra of observables in a de Sitter static patch is a von Neumann algebra of Type II$_1$, rather than Type III, "provided an observer is included" [@chandrasekaran2023]. With this algebra, entropy becomes well defined. It is renormalised, so it is fixed only up to an additive constant. The maximum-entropy state is empty de Sitter space, paired with a thermal distribution for the observer's energy.

The observer is minimal. The authors adopt "a minimal model in which the observer consists only of a clock". The clock's Hamiltonian $q$ is non-negative, and they call the model "unrealistically simple". Witten's follow-up papers keep the same idealisation. The observer is a timelike worldline carrying a clock whose Hamiltonian is bounded below, and the model "is meant to be an idealization of our own situation in the universe" [@witten2024background; @witten2024algebras]. Witten states the gap himself: "A realistic observer would presumably also carry measuring equipment, and a recording device." The recording device is then left out [@witten2024algebras]. Maldacena likewise models an observer "simply ... as a particle with a clock" [@maldacena2026]. De Vuyst, Eccles, Hoehn and Kirklin show that these observers are quantum reference frames, and that the resulting gravitational entropy depends on which observer is chosen [@devuyst2025].

**Closed universes.** Gravitational path-integral arguments suggest that the Hilbert space of a closed universe is one-dimensional. The idea has antecedents in work on baby universes [@mcnamara2020; @marolf2020]. Harlow, Usatyuk and Zhao argue that the evidence for one-dimensionality is "fairly compelling". They then show that an observer recovers an approximate quantum-mechanical description of dimension about $e^{S_\text{Ob}}$, with errors exponentially small in the observer's entropy [@harlow2026]. Abdalla, Antonini, Iliesiu and Levine reach a related conclusion by a different rule: "the Hilbert space is not one-dimensional, as calculations in the absence of the observer suggest" [@abdalla2025]. Akers and collaborators show that the two rules differ and give different dimensions [@akers2025].

This result is **contested**:

- Liu argues that closed universes should have a semiclassical description rather than a one-dimensional Hilbert space, "with no need to introduce observers" [@liu2025].
- Antonini, Rath, Sasieta, Swingle and Vilar López argue that the one-dimensionality reflects the limited access of the external holographic description, not a breakdown of semiclassical physics [@antonini2025].
- Nomura and Ugajin accept one-dimensionality but derive predictions from partial observability, without external observers [@nomura2025].

**The observer in these models.** In the de Sitter papers the observer is a pure clock. Harlow, Usatyuk and Zhao go further. Their observer has finite entropy. It is classical in that "it has a basis of pointer states which are stable under interaction with its environment". And it is entangled with its environment [@harlow2026]. That is decoherence, so partway to a recorder. Even so, it has no memory register and no thermodynamic arrow, and the authors "prefer to avoid any detailed discussion of what constitutes an observer". The same minimalism appears in a recent general framework for observers, whose minimal observer "avoids complexity like memory, learning, or self-awareness" [@elshatlawy2025].[^elshatlawy]

[^elshatlawy]: The quoted sentence is from an earlier arXiv version of that paper; the current version (v3) could not be checked.

The upshot, which corrects a simpler version of this paper's starting point, is that quantum gravity has moved from clocks toward decohered observers. It has not moved to observers that keep records and have an arrow of time.

## 2.6 Observers in physics II: the observer as a recorder

A different tradition makes the observer a keeper of records.

**Early formulations.** In his long thesis, Everett described observers as "automatically functioning machines (servomechanisms) possessing recording devices (memory)". The phrase is quoted in @sep-everett; the published short version is @everett1957. Gell-Mann and Hartle defined an observer, or "information gathering and utilizing system" (IGUS), as a complex adaptive system that exploits the predictability of a quasiclassical domain [@gellmann2018]. Hartle's simple model of an IGUS is a robot whose memory registers "constitute the robot's memory of the past" [@hartle2005].

**Decoherence.** In the decoherent-histories framework, Halliwell tied decoherence to the existence of records stored somewhere in the universe, and noted that such "records may still exist but are necessarily imperfect" [@halliwell1999]. Zurek's programme of einselection and quantum Darwinism explains classicality through stable pointer states and their redundant imprinting on the environment [@zurek2003; @zurek2009].

**Records and reversibility.** Zurek made the link between records and irreversibility explicit. In quantum dynamics, "reversing quantum evolution that led to a measurement becomes in principle impossible for an observer who keeps the record". A friend who never learned the outcome could still undo it, so reversibility is *relative* to who holds the record [@zurek2018].

**Relational views.** Relational quantum mechanics denies any special observer: "there is no observer-observed distinction" [@rovelli1996]. Its later development distinguishes relative facts from "stable facts", the ones whose relativity decoherence lets us ignore [@dibiagio2021].

**No-go theorems.** Results on Wigner's friend show what is at stake in calling something an observer. Brukner derived a no-go theorem for observer-independent facts [@brukner2018]. Bong and colleagues proved a stronger version and tested it in an experiment in which "a photon's path is deemed an observer" [@bong2020]. Wiseman, Cavalcanti and Rieffel proposed that "a system's having *thoughts* is a sufficient condition for it to be an observer", which shifts the burden to a future human-level AI running on a quantum computer [@wiseman2023]. The physics literature has no agreed answer to which systems count.

**What records cost.** Two results put the clock–recorder contrast in thermodynamic terms.

- *Real clocks cost entropy.* A clock that actually ticks and registers its ticks is an open, irreversible system. In an autonomous quantum clock, dissipated heat trades off against accuracy and resolution [@erker2017]. A nanomechanical clock experiment found that "the maximum possible accuracy for this classical clock is proportional to the entropy created per tick" [@pearson2021]. Milburn's review concludes that "good clocks require large energy dissipation" [@milburn2020].
- *Ideal records cannot be made.* "It is impossible to perform ideal projective measurements on quantum systems using finite resources" [@guryanova2020].

The idealised clock-observer of de Sitter algebras is thus a limiting case. Its conserved Hamiltonian sits outside these thermodynamic bounds. Any clock that is physically realised and that registers time lies on the far side of the line between clocks and recorders.

## 2.7 Thermodynamics of records, memory, prediction and agency

**Landauer's principle.** Landauer argued that logically irreversible operations, erasure above all, must dissipate heat [@landauer1961]. Bennett developed the theory of reversible computation and its relation to Maxwell's demon [@bennett1982; @bennett2003]. Bérut and colleagues confirmed experimentally that "the mean dissipated heat saturates at the Landauer bound in the limit of long erasure cycles" [@berut2012].

**Measurement versus erasure.** Sagawa and Ueda showed that only the *sum* of the work costs of measurement and erasure is bounded below. That sum is at least $kT$ times the mutual information acquired. How the cost divides between the two steps depends on how the memory is built [@sagawa2009]. Parrondo, Horowitz and Sagawa review the field [@parrondo2015], and Wolpert extends it to general computation [@wolpert2019]. Sagawa and Ueda's result matters for §4. It means that the *location* of dissipation cannot by itself tell us whether a record was formed.

**Prediction.** Still, Sivak, Bell and Crooks showed that a system driven by a changing signal dissipates in proportion to the information it retains about the signal that is *not* predictive of the signal's future. At each step, $\beta\langle W_\text{diss}\rangle = I_\text{mem} - I_\text{pred}$. Over a whole protocol, "the total nonpredictive information provides a lower bound on the total dissipation" [@still2012]. Memory that is useless for prediction is thermodynamically expensive.

**Self-maintenance.** Kolchinsky and Wolpert defined *semantic information* as the correlational information a system has about its environment that is "causally necessary for the system to maintain its own existence". Causal necessity is assessed by interventions that scramble system–environment correlations [@kolchinsky2018].

Taken together, these two results provide most of what the third and fourth rungs of the ladder in §3.2 need, in formal terms.

**Memory and the arrow of time.** Mlodinow and Brun argued that a memory's psychological arrow should align with the thermodynamic arrow wherever the latter is well defined [@mlodinow2014]. Wolpert and Kipper distinguished three types of memory system. Only one type exploits the second law, so that it informs only about the past, and human memory is of that type [@wolpert2024]. Gołosz has recently argued, against reductive readings, that the temporal asymmetry of traces and the thermodynamic arrow are "only arrows in time" that themselves need a deeper explanation [@golosz2025].

**Rovelli's account.** Rovelli gave the most direct statement of the idea this paper builds on. "A trace is an irreversible phenomenon." The formation of traces "is a mechanism that transforms initial low entropy (free energy) into available information". The information a trace can store is bounded by the entropy produced in making it [@rovelli2022]. In a companion paper he argued that "memory and agency can thus be viewed as mechanisms that convert free energy into information" [@rovelli2020agency].

**Fields.** Fields argued that factorising the world into an observed system and the rest is itself a limited, costly resource, with "each bit of uncertainty reduction" about the provenance of a recorded outcome costing "on the order of kT" [@fields2014].

**Life.** Living systems pay for their records too. Sensory adaptation in *E. coli* chemotaxis is "necessarily dissipative" [@lan2012]. Learning an external concentration requires breaking detailed balance and consuming energy [@mehta2012]. England derived a lower bound on the heat produced by self-replication [@england2013]. He later proposed "a general thermodynamic mechanism for self-organization via dissipation of absorbed work", which he called "dissipative adaptation" [@england2015; see also @perunov2016]. Related approaches include constructor theory [@marletto2015], the autopoietic theory of the living [@maturana1980], and the free-energy principle [@friston2010; @friston2013; @friston2019]. Stochastic thermodynamics supplies the formal tools common to all of them [@seifert2012].

## 2.8 The nonequilibrium brain

The empirical anchor for the thesis is a fast-growing literature on the *time-irreversibility*, or broken detailed balance, of large-scale brain dynamics. Nartallo-Kaluarachchi and colleagues review it [@nartallo2026].

**Main findings [established within this literature].**

- Sanz Perl and colleagues estimated entropy production and probability-flux curl from monkey electrocorticography (ECoG), recorded in sleep and under propofol, ketamine, and ketamine with medetomidine. They also used human fMRI in deep sleep and under propofol. They found that "all states of reduced consciousness unfolded at higher proximity to equilibrium" [@sanzperl2021].
- The INSIDEOUT framework found "significantly lower levels of reversibility ... in deep sleep and anaesthesia compared to wakefulness" [@deco2022insideout].
- Deep networks trained to tell forward from time-reversed monkey ECoG performed worse in deep sleep and under ketamine [@delafuente2023].
- Gilson, Tagliazucchi and Cofré fitted multivariate Ornstein–Uhlenbeck models to simultaneous EEG–fMRI in 15 participants. Mean entropy production fell from wakefulness through sleep stages N1, N2 and N3 (1.99, 1.65, 1.54, 1.49 in their units), with the largest drop at sleep onset [@gilson2023].
- A first fMRI study of patients with disorders of consciousness reported "the tendency of a decrease in the asymmetry of the brain signal" [@gguzman2023].
- Whole-brain models fitted to sleep and to disorders of consciousness show lower simulated irreversibility and lower simulated perturbational complexity [@stikvoort2025].
- Deviations from the fluctuation–dissipation theorem, another nonequilibrium index, fall stepwise with the level of consciousness in patients [@martinezmarin2025]. They also "decrease in unresponsive DoC and anesthesia compared with conscious conditions" across humans and rodents, mirroring the perturbational complexity index [@berjagabuisan2026; @deco2023fdt; @casali2013].
- Permutation-based time irreversibility of sleep EEG declines with sleep stage [@yao2024].

**Related entropy-based markers.** These measure entropy *levels*, not entropy *production*. Guevara Erra and colleagues reported that wakeful states show "the greatest number of possible configurations of interactions between brain networks, representing highest entropy values" [@guevaraerra2016]. The "entropic brain" hypothesis holds that "the entropy of spontaneous brain activity indexes the informational richness of conscious states" [@carhartharris2014; @carhartharris2018].

**Confounds [contested or open].** Three bodies of evidence complicate the picture.

- *Activity and effort.* In healthy subjects, violations of detailed balance "increase with physical and cognitive exertion" [@lynn2021]. Task state modulates irreversibility across about a thousand participants [@deco2023arrow]. Irreversibility therefore tracks activity as well as consciousness.
- *Metabolism.* Propofol unconsciousness depressed cortical glucose metabolism by 58% and subcortical metabolism by 48% [@alkire1995]. Anaesthesia-induced unconsciousness comes with "approximately 45% reduction in cerebral energy consumption" [@shulman2009]. In 131 patients, about 42% of normal cortical metabolism marked the threshold for sustained awareness [@stender2016]. Metabolism falls in the same states in which irreversibility falls, so the two are plausibly collinear.
- *Seizures.* Consciousness is often lost in seizures [@blumenfeld2012]. Yet in intracranial EEG "the maximally time-irreversible signals always occurred during seizures" [@schindler2016].

On the confounds, two further points. This review found no study that regresses large-scale irreversibility on metabolism or signal power within the same subjects. Gilson and colleagues report that entropy production correlates with the variance of the model's inputs [@gilson2023]. One recent preprint, on mouse photometry rather than consciousness, shows that irreversibility can be separated from response amplitude [@dmochowski2026]. §5.3 and §8 return to these confounds.

## 2.9 Thermodynamic and record-based proposals about consciousness

The novelty search (method in `notes/literature-review.md`) looked for prior work that makes irreversibility, records or dissipation the bearer or measure of experience. The closest works fall into four groups.

**Physical and biological frameworks.** These have the ingredients but stop short of the claim about experience.

- Fields, Glazebrook and Levin's "minimal physicalism" models every bipartite interaction as mutual observation. It invokes "Landauer's principle of the finite per-bit cost of irreversibly acquiring an observational outcome", and it hypothesises that "consciousness and cognition are scale-free phenomena that characterize all living systems" [@fields2021; see also @fields2022; @levin2019].

  This is the nearest mainstream neighbour. It differs from the present thesis in three ways. Its scale-free hypothesis is stated for *living* systems. Its stated aim is a framework that "makes no assumptions beyond those of quantum information theory", not a metaphysics of experience. And it does not grade experience by the entropy spent on persistent records integrated into a self-model.
- Kolchinsky and Wolpert supply the interventional template for the integration factor $u_r$ of the measure (§4), but make no claim about experience [@kolchinsky2018].
- Ito, Oizumi and Amari supply the formal bridge between entropy production and integration, also without such a claim [@ito2020].

**Thermodynamic theories of consciousness.** Ganesh proposes two conditions from nonequilibrium fluctuation theorems as *necessary* for any conscious system [@ganesh2020]. These are threshold conditions, not a graded proto-experience, and they do not involve records. Solms and Friston ground consciousness in the free-energy principle and in affect [@solms2018].

**Recent preprints and one chapter.** Only their abstracts were read, and the preprints are unreviewed.

- Peyru proposes that the nodes where possibility becomes actuality need not be brains. Any "irreversible record-generating subsystems" qualify, with gravitational structure formation as a proto-case. This is the closest statement of component (i) found [@peyru2026].
- Noirmont identifies consciousness with self-organising dissipative structures, uses quantum Darwinism for redundant records, and sets an entropy-production threshold for phenomenal unity. The account is emergentist, with a threshold, not graded [@noirmont2026].
- Yuan proposes a "dissipative panpsychist framework" in which the bearer is a repeatable adaptive response pattern, not a record [@yuan2026].
- Devine identifies record formation with a many-to-one selection that has a Landauer cost, and expressly disclaims consciousness [@devine2026].
- Schneider proposes a "quantum Darwinist theory of consciousness" for classifying AI hardware, in which consciousness requires integrated information stabilised over time and redundantly recorded [@schneider2026].

## 2.10 Summary and novelty verdict

| Locus of (proto-)experience | Representative sources | New physics? | Graded? | Treats the XOR grid as | Status |
|---|---|---|---|---|---|
| Particles or fields | Russell; Strawson; Goff | No | Unclear | Not addressed | Philosophical, contested |
| Objective reduction | Penrose; Hameroff & Penrose | Yes | Per event | Not addressed | Natural DP version excluded [@donadi2021] |
| Integrated information ($\Phi$) | Tononi; Albantakis et al. | No | Yes | Highly conscious | Contested [@cogitate2025; @iitconcerned2025] |
| Actual occasions | Whitehead; Griffin | No | Yes | Not addressed | Metaphysical |
| Retention of the past | Hering; Bergson; Peirce | No | Yes | Not addressed | Historical |
| Observation with Landauer cost | Fields, Glazebrook & Levin | No | Not by entropy | Not addressed | Living systems only |
| **Persistent records integrated into a self-model** | **This paper** | **No** | **Yes** | **Near zero** | **Proposal** |

: **Table 1.** Candidate loci of (proto-)experience.

**Verdict: partially anticipated.** Each component of the thesis has precedents.

- *Records, irreversibility or memory as the bearer.* Anticipated in form by Whitehead and the memory tradition. Physically, it is anticipated by Rovelli's account of traces and by Fields, Glazebrook and Levin, and as a claim about experience by Peyru's recent preprint.
- *A graded measure tied to entropy production.* Anticipated empirically by the nonequilibrium-brain literature, and formally in part by Ito, Oizumi and Amari. Its normalisation by mass is Chaisson's.
- *Use of records by the system's own dynamics.* Anticipated formally by Kolchinsky and Wolpert's semantic information and by the free-energy principle.

No source found states the conjunction: a *conditional* argument that, among the candidate loci, the irreversible recording event is the best bearer of graded proto-experience. Nor does any source pair that argument with a measure that counts only the entropy spent on persistent records a system integrates into a model of itself, or with an empirical test designed against the metabolic confound. The paper's claim to novelty rests on that conjunction and on the explicit link to the clock-observers of quantum gravity. It does not rest on any single component.

# 3. The argument

## 3.1 Two notions of observer, and the missing bridge

Physics uses "observer" in two senses that are easy to run together.

An **observer-as-clock** is a degree of freedom with a Hamiltonian bounded below. It is idealised as nearly classical, and it serves as a reference against which other quantities are defined. This is the observer of the de Sitter and closed-universe papers (§2.5). It does real work. With it, the static-patch algebra becomes Type II$_1$ and entropy becomes well defined up to a constant [@chandrasekaran2023]. In some proposals, a closed universe acquires an effective Hilbert space only relative to such an observer [@harlow2026; @abdalla2025]. Yet the clock keeps no records. Its Hamiltonian is conserved, it dissipates nothing, and it carries no arrow of time. Witten's remark that "a realistic observer would presumably also carry ... a recording device" marks exactly what the model leaves out [@witten2024algebras].

An **observer-as-recorder** is a system that forms persistent, decohered records of what it interacts with, and pays for them in entropy. This is the observer of Everett's servomechanisms, Hartle's IGUS and Zurek's relative reversibility (§2.6). It also matches the thermodynamics of memory (§2.7). It is also the observer that *facts* require, in the following sense. If an outcome can still be reversed by anyone who matters, then it is not yet a fact for them. Zurek's result makes reversibility relative to the record-holder [@zurek2018]. Di Biagio and Rovelli's "stable facts" are the ones that decoherence has made effectively irreversible [@dibiagio2021].

The two notions come apart. A perfect clock keeps no records. A crater keeps records but tells no time with any precision. And the physical literature has so far needed only the first. **No result known to this author shows that quantum gravity requires an observer of the second kind**, that is, an observer whose records, dissipation and arrow of time are essential to defining states or algebras.

The closest approaches are partial. The closed-universe observer of Harlow, Usatyuk and Zhao has pointer states and is entangled with its environment, so it is decohered [@harlow2026]. It still has no memory and no arrow. Some critics of that programme propose models in which an arrow of time emerges [@antonini2025]. But nothing there makes a recording observer *necessary*. Physically realised clocks are already recorders, because their ticks cost entropy [@erker2017; @pearson2021; @milburn2020]. That fact holds outside the idealisation; it is not a theorem about quantum gravity.

Call the missing result the **bridge theorem**. It would show that any observer able to give a gravitating universe a nontrivial, well-defined physics must keep irreversible records, and so must sit on a thermodynamic gradient. If true, such a theorem would tie the physics of observers to the physics of experience as this paper construes it. If false, the clock-observers of quantum gravity remain a separate notion, and the record view must stand on its own, as it is argued to do below. This paper flags the bridge theorem as an open problem. It does not claim to supply it.

## 3.2 The ladder of observerhood

Observerhood is better treated as graded than as binary. Four rungs can be distinguished (Figure 1).

![**Figure 1.** The ladder of observerhood. Each rung adds a capacity to the one below. Recording events, the bearers of proto-experience on the record view, occur from rung 2 upward. The measure of §4 grows with the entropy a system spends on records that persist and are integrated into a model of itself, so living systems score from rung 3, and most on rung 4. A processor running a frozen model forms no records that outlast a request and integrates none into a self-model, so it scores near zero (§5.4).](figures/ladder.png){width=95%}

1. **Clock.** Any system with energy bounded below can serve as a clock, so clocks are everywhere and cheap. Idealised clocks keep no records.
2. **Irreversible record.** A crater, a damage track in a mineral, or a hot molecule that emits thermal photons carrying which-path information [@hackermuller2004]. Each is a persistent, decohered trace whose formation produced entropy. No life is required. Rovelli's conditions for traces are enough: subsystems that are effectively separated, a temperature difference, and long thermalisation times [@rovelli2022].
3. **Record used for self-maintenance.** A cell that adapts to a chemical gradient keeps records of its environment that are causally necessary for its persistence. That is semantic information in Kolchinsky and Wolpert's sense [@kolchinsky2018]. Keeping them is necessarily dissipative [@lan2012; @mehta2012].
4. **Record integrated into a self-model.** A brain binds records into a model of itself in its world, and uses that model to predict and act.

Two points follow.

*Clock plus memory is not life.* Life adds self-maintenance, and usually replication; these are the third rung and its thermodynamic costs [@england2013; @kolchinsky2018]. The record view does not equate observing with living.

*There is no paradox about observers before life.* Rungs 1 and 2 were common long before biology. The early universe was full of clocks and, once structure formed, full of records. A view on which facts need recorders does not need *minds* in order to have facts, which removes one traditional motivation for consciousness-based interpretations of quantum mechanics.

## 3.3 Why records, and not particles, collapse or integrated information

The argument is comparative. Assume, for the sake of argument, some panpsychist or Russellian-monist view. Which candidate locus best meets four desiderata?

- **(D1)** It requires no physics beyond what is established.
- **(D2)** It is graded in a way that tracks physical differences.
- **(D3)** It gives sensible verdicts in contrast cases.
- **(D4)** It eases rather than sharpens the combination problem.

**Particles.** An electron is a superb clock: it has a Compton frequency. It keeps no records. Its interactions are individually reversible at the level of its own dynamics, and it is identical to every other electron. Putting proto-experience there satisfies D1 trivially but fails D2, since all electrons are the same. And it *sharpens* the combination problem (D4). The micro-subjects are as many as the particles, they are qualitatively identical, and nothing about their dynamics says how they could combine. James's "windowless" feelings are the right image [@james1890].

**Collapse.** Orch-OR gives each objective reduction a moment of experience, and so gives a graded, event-based locus [@hameroff2014; @hameroff2008]. It fails D1. It needs a new law of physics whose simplest version has been excluded experimentally [@donadi2021]. It is also doubtful that the relevant quantum coherence survives in warm neural tissue [@tegmark2000]. The record view keeps what is attractive in Orch-OR, an event-based and graded locus that is tied to the emergence of definite outcomes. It drops the new physics. Decoherence plus thermodynamics already yields definite, irreversible, costed records.

**Integrated information.** IIT is graded (D2) and needs no new physics (D1). It fails D3. A large grid of XOR gates, even an inactive one, has high $\Phi$ and so is highly conscious by IIT's lights. Tononi accepts that verdict [@aaronson2014phinal]. The verdict comes from measuring information alone, and the fourth step in developing the measure (§4) checks it against one that does not. Weighting information by dissipation per gram, as $E\,I/M$ does, gives an inactive grid zero, since it dissipates nothing. That check removes IIT's verdict, but it still ranks processors above brains. On the record view the grid scores near zero, for a reason that is principled rather than ad hoc, and the same reason keeps processors low.

The grid's integration is static causal structure. While running, each XOR gate is logically irreversible, so the grid does dissipate when it updates. But that dissipation is *overwriting*: each cycle destroys the previous state. The grid forms no record that persists across cycles, and it has no model of itself into which a record could be integrated. On the measure of §4 both its persistence factor $p_r$ and its integration factor $u_r$ vanish. An inactive grid does nothing at all.

The point is not that IIT's integration is irrelevant. Section 4 keeps integration, but as the integration of records into the system's model of itself, the factor $u_r$, not as static causal structure. The point is that integration *without* persistent records should not count, and IIT has no means of excluding it.

**Records.** The record-based locus satisfies D1. It needs decoherence, which is established, and the thermodynamics of information, which is established and confirmed experimentally [@zurek2003; @berut2012]. It is graded (D2). It can be quantified by the entropy a system spends on records that persist and are integrated into its model of itself (§4). It gives sensible verdicts in contrast cases (D3, §5).

It does not solve the combination problem, but it eases it (D4). Records already combine in a physically ordinary way: a self-model is a structure built of records about records. On the measure of §4, a record counts in proportion to its integration into that self-model, the factor $u_r$. Combination then becomes a question about how records are integrated into one self-model, which is open to empirical study, rather than a question about how windowless subjects merge. §7 says how far this goes.

The comparative claim is modest. It is not that records *are* experience. It is that, if experience has a physical locus of the kind panpsychists want, records are the best-placed candidate of the four.

# 4. Toward a measure

This section develops a measure in steps, because the dead ends are instructive. What it offers is a sketch, not a formalism.

**Step 1: entropy level.** A first thought is that experience tracks entropy. In the brain, wakeful states do show the largest repertoire of network configurations [@guevaraerra2016; @carhartharris2018]. But as a general measure, entropy level fails at once. Maximum entropy is thermal equilibrium, where nothing happens and no records form.

**Step 2: entropy production rate.** The natural repair is to move from entropy to its rate of production, a measure of how far a system is from equilibrium. This matches the brain data of §2.8: reduced consciousness lies closer to equilibrium [@sanzperl2021; @gilson2023]. But stars produce entropy at enormous rates.

**Step 3: normalise by mass.** Chaisson's *energy rate density* normalises energy flow by mass [@chaisson2001; @chaisson2011]. It is a measure of energy throughput rather than of entropy production, but it is a useful first proxy. His values, in erg s$^{-1}$ g$^{-1}$, are about 2 for the Sun, about 900 for plants, about $2 \times 10^4$ for the human body and about $1.5 \times 10^5$ for the human brain [@chaisson2014]; the inputs used in §5.6 give $1.3 \times 10^5$. Normalisation puts stars at the bottom. But machines come out on top. Chaisson gives about $2.7 \times 10^7$ for a Boeing 747 [@chaisson2014]. A modern accelerator chip is higher still: an H100 GPU module rated at up to 700 W, divided by the mass of its die (at most 1.5 g), gives about $5 \times 10^9$ erg s$^{-1}$ g$^{-1}$ (§5.6).

**Step 4: times information.** The author proposed multiplying mass-normalised dissipation by information: $E\,I/M$, where $E$ is the entropy production rate, $I$ the information the system creates and $M$ its mass. It serves as a check on measures built on information alone, which rate an inactive grid of XOR gates as highly conscious. IIT gives the grid high $\Phi$ whether its gates are on or off, and Tononi accepts the verdict [@aaronson2014phinal]. Weighting information by dissipation per gram removes that verdict. An inactive grid dissipates nothing, so on $E\,I/M$ it scores zero. A running grid scores only for its activity, as any circuit does. Its states last one update, and the integrated wiring that earns it a high $\Phi$ adds nothing.

But $E\,I/M$ does not ask whether what a system creates lasts, and there it fails in the other direction. A processor creates and destroys information at gigahertz rates while dissipating, per gram, some $4 \times 10^4$ times what a brain does (§5.6). On $E\,I/M$ it ranks far above a brain.

**Step 5: entropy spent on persistent, integrated records.** The diagnosis is that steps 2–4 count *all* dissipation, and step 4 counts all information, however briefly it lasts. On the record view, only the entropy spent forming records that **persist** and are **integrated into the system's model of itself** should count. A processor dissipates mostly by overwriting and erasing. Its registers are written and destroyed billions of times a second, and what does persist in it, such as a program or a model's weights, enters no model the processor has of itself. A star accumulates no records that it uses for anything. A brain spends part of its budget forming synaptic, molecular and network-level traces. These persist for seconds to decades, and they feed a model the organism uses to keep itself alive and to act.

A schematic form, offered only to fix ideas:

$$
R \;=\; \frac{1}{M}\sum_{r} \Delta S_r\; p_r\; u_r .
$$

The sum runs over the records $r$ a system forms per unit time, and $M$ is the mass of the system that integrates them. $R$ is measured in $k_B$ s$^{-1}$ g$^{-1}$. The terms are:

- $\Delta S_r$ is the record's thermodynamic price: the Landauer cost of the bits it holds, $k \ln 2$ per bit [@landauer1961]. The dissipation a real system spends on a record, counting its formation and its eventual erasure together, is at least this price and usually far more (§5.6). That dissipation is an upper bound on the price and an imperfect proxy for it. Using the price means that waste does not count, so a wasteful memory does not outscore an efficient one. It also means that dissipation need not be located. Sagawa and Ueda show that only the sum of the costs of measurement and erasure is bounded, and that the split between them depends on how the memory is built [@sagawa2009].
- $p_r = \max(0,\, 1 - \tau_\text{dyn}/\tau_r)$ is a persistence factor. Here $\tau_r$ is the record's lifetime and $\tau_\text{dyn}$ the system's characteristic dynamical time. A register overwritten at every step has $\tau_r \le \tau_\text{dyn}$ and contributes nothing; a record that lasts many steps counts almost in full.
- $u_r \in [0,1]$ is the fraction of the record's information that is integrated into the system's model of itself in its world and used by the system to keep itself in existence and to act. The information counted is semantic in Kolchinsky and Wolpert's sense: causally necessary for the system's continued existence [@kolchinsky2018]. The model can be minimal: a cell's record of a chemical gradient counts on rung 3 of the ladder of observerhood (§3.2), while a brain's self-model, on rung 4, integrates far more.

The proposal is that the degree of proto-experience is monotone in $R$.

Because $R$ is taken per unit time and per gram, and the sum over records and the mass both grow with a system's size, two copies of a system score as one.

The factors are not chosen case by case; each is read off the definition of the bearer. A record has a thermodynamic price, which is $\Delta S_r$. It persists, which is $p_r$. And it is integrated into the system's model of itself, which is $u_r$. Dividing by mass follows Chaisson, for the reason step 3 gives.

**Bearer and measure.** Every recording event, from rung 2 up, is a bearer of proto-experience on this view. $R$ grades how much recording a system does *for itself*. A hot molecule hosts recording events and a cold one does not, so the hot one ranks above the cold one on rung 2 (§5.1). Yet both have $R$ near zero, because nothing integrates the records the hot one makes.

The other contrast cases follow the same pattern. Stars and jet engines dissipate without forming records that anything integrates. A storage device holds records but integrates none. A grid of logic gates overwrites its states at every update. A language model at inference forms no records that outlast the request: its weights are frozen, and its key–value cache, at most 17 bits of information per token, is dropped when the request ends. None of these systems integrates what it records into a model it uses to keep itself in existence, so $u_r \approx 0$. A model at inference therefore scores near zero whatever its hardware, its boundary or its mass (§5.4, §5.6).

**Brains.** Measured large-scale entropy production is at best a proxy for $R$. It is contaminated by dissipation spent on activity that forms no lasting, integrated records. On rodent-based estimates chained in §5.6, plasticity takes only a few per cent of the brain's energy budget [@karbowski2019; @howarth2012; @engl2015], yet plasticity is where the brain's lasting records are made. Estimates from large-scale signals are also coarse-grained, and coarse-graining can only lower the entropy production one measures [@kawai2007; @roldan2010]. They are therefore neither an upper nor a lower bound on the brain's $R$. §8 is designed around that gap.

**The thermodynamics of prediction.** Still, Sivak, Bell and Crooks show that a driven system's dissipation is bounded below by the *non-predictive* information it retains [@still2012]. Memory that is useless for prediction is waste heat. On $R$ it has $u_r \approx 0$, since a record that tells the system nothing about what comes next does not serve a model it acts on.

**The erasure problem (open).** Landauer erasure is itself irreversible and costs entropy. Why, then, does erasure not count as recording? The answer proposed here is that $R$ counts records that *persist and are integrated*, not irreversibility as such. Erased information leaves the system as heat. That heat is in principle a record in the environment, but one that no system integrates, so it has $u_r \approx 0$. The same answer covers the waste heat of a star or a jet engine.

This answer depends on non-circular definitions of "record", "persistence" and "integration into a self-model". They must not quietly reintroduce the mental vocabulary they are meant to ground. Kolchinsky and Wolpert's interventional method is the template [@kolchinsky2018]. Applied here, a record would be integrated to the extent that scrambling it degrades the system's ability to keep itself in existence and to act. Still and colleagues' decomposition into predictive and non-predictive information is another route [@still2012]. Neither has been extended to self-models. **The erasure problem is therefore marked here as unresolved.**

# 5. Contrast cases and predictions

## 5.1 Hot and cold molecules

Hackermüller and colleagues sent C$_{70}$ fullerenes through a Talbot–Lau interferometer after heating them with a laser. Interference visibility fell from 47% with no heating to zero at 10.5 W. The heated molecules emit thermal photons that carry which-path information into the environment [@hackermuller2004]. In the vocabulary of the ladder of §3.2, the hot molecule makes irreversible records of its own path, while the cold one does not.

The record view therefore ranks the hot molecule *above* the cold one on rung 2, the rung of irreversible records. The difference is tiny, and it lies on the lowest rung at which the view assigns anything. Still, it is a definite consequence, and a deliberately counterintuitive one. It should be owned rather than explained away. What it shows is that the view is not about complexity or life as such. It is about whether the world is being irreversibly written on.

The measure of §4 adds that being written on is not enough. The hot molecule's records leave with its photons, and nothing integrates them into a self-model, so $u_r = 0$ for each of them. Its $R$ is therefore near zero, like the cold molecule's, and far below that of any organism. The hot molecule hosts recording events, but it does almost no recording *for itself*.

## 5.2 Gates, grids, storage and processors

The XOR grid scores near zero. While it runs, each cycle overwrites the state the last one wrote. No state outlasts the grid's own dynamical time, so every persistence factor $p_r$ is zero, and nothing in the grid integrates its states into a self-model. An inactive grid forms no records at all and scores zero. IIT's $\Phi$ rates the same grid, active or not, as highly conscious (§3.3).

A storage device scores zero for a different reason. A hard disk or a USB stick forms persistent records when it is written, and each costs at least its Landauer price. But nothing in the device integrates them. It holds what it is given and uses none of it to keep itself in existence or to act, so $u_r = 0$. Unpowered, it forms no records at all.

A processor, and a hashing chip such as a bitcoin miner, dissipate mostly by overwriting and erasing. Their registers are rewritten at gigahertz rates, and little of what they compute persists. A hashing chip evaluates one fixed function over and over and keeps almost none of the results. The small share of a processor's dissipation that writes persistent memory does form records in the sense of §4. But those records are integrated into no self-model that the processor uses to keep itself in existence.

Per gram, a chip dissipates far more than a brain: a GPU die some $4 \times 10^4$ times as much (§5.6). Measures built on dissipation therefore rank it above a brain. That includes Chaisson's energy rate density and the E·I/M check of §4, which multiplies dissipation per gram by information: a chip also handles more information per second than a brain does. The record measure does not rank it above a brain. It counts only the price of records that persist and are integrated, and a chip forms almost none.

The record view thus disagrees with IIT about the grid. It disagrees with crude energy-throughput measures about processors and jet engines. And it agrees with neither about stars.

## 5.3 Brains: sleep, anaesthesia, disorders of consciousness and seizures

The record view predicts that, *within* a brain, $R$ falls when consciousness is lost. Over hours a brain's mass is fixed, so $R$ falls when the brain forms fewer lasting records, or integrates fewer of those it forms into its self-model. The observed fall in large-scale irreversibility across sleep, anaesthesia and disorders of consciousness fits this prediction (§2.8). But measured irreversibility is at best a proxy for $R$. It is contaminated by dissipation spent on activity that forms no lasting, integrated records. The fit is therefore weak evidence, for two reasons.

**The metabolic confound.** Metabolism also falls in these states, and by large amounts [@alkire1995; @shulman2009; @stender2016]. Irreversibility also rises with effort in healthy subjects [@lynn2021]. A view on which irreversibility merely tracks activity or metabolism predicts the same data. On the measure of §4, metabolism is not itself a factor of $R$. Plasticity takes only a few per cent of the brain's energy budget, yet it is where the brain's lasting records are made (§5.6). A fall in metabolism bears on the record view only in so far as it is a fall in record formation. This is the most important empirical objection to the thesis (§7, objection 2). §8 is designed to test it.

**Seizures.** Generalised and complex partial seizures often abolish consciousness [@blumenfeld2012]. Yet in intracranial EEG the most time-irreversible signals occur *during* seizures [@schindler2016]. If whole-brain entropy production were high during seizures in which consciousness is lost, then the simple claim that irreversibility marks consciousness would be refuted.

The record view is not thereby refuted, for a principled rather than ad hoc reason. Seizures are hypersynchronous, stereotyped and high in dissipation. On the record view their dynamics, locked into one pattern, form little that is new and integrate little of what they form. They are just the kind of activity that spends entropy *without* forming lasting, integrated records, so on the measure of §4 dissipation can rise while $R$ falls. But the escape is only as good as an *independent* measure of record formation. Without one, the move would be unfalsifiable. Seizures are therefore the sharpest available test case (§8). The existing evidence is local and single-channel, and so does not settle the matter for whole-brain measures.

## 5.4 Large language models

A language model at inference time, with fixed weights, dissipates a great deal of energy and processes a great deal of information. Yet it forms no internal records that outlast the request. Its weights are frozen. Its key–value cache is dropped when the request ends, or at most kept across the turns of one conversation. The only lasting trace, the transcript, sits outside the system. On the measure of §4 such a model therefore scores near zero, whatever hardware it runs on and whatever that hardware weighs. No choice of boundary or mass changes this, because there are almost no lasting records to count.

Training is different. It forms lasting records, the weights, at a cost per retained bit not clearly below a brain's (§5.6). But nothing integrates them into a self-model that the system uses to keep itself in existence. The model is kept in existence by its operators, so in Kolchinsky and Wolpert's sense its weights carry little semantic information *for the model* [@kolchinsky2018]. Its $u_r$ is near zero, and so is its $R$.

Some architectures update weights or memory modules during use. Examples are test-time-training layers, whose hidden state "is a machine learning model itself" updated by self-supervised steps [@sun2024], and neural long-term memories that learn "to memorize historical context" at test time [@behrouz2024]. Such systems form persistent records in use, which raises the record-forming term. $R$ would rise only if those records were integrated into a self-model that the system used to keep itself in existence.

This raises an identity puzzle that mirrors the combination problem. Many diverging copies of one model might each accumulate their own records. The question is then what makes a single subject rather than many, a "decombination" problem for machines. The measure of §4 does not settle it. Taken per gram, $R$ gives two copies the same score as one, so it grades how much recording each does for itself, not how many subjects there are.

The verdict, that current language models score near zero, is in line with assessments based on theories of consciousness, which judge current AI systems unlikely to be conscious [@butlin2023; @chalmers2023]. It is reached here for a different reason: from which records a system forms and integrates, not from which computations it performs.

## 5.5 Splitting and dissolving the self

If the self is a structure of integrated records, its unity should depend on connectivity and should come in degrees. Two bodies of evidence bear on this, and both are contested.

**Split-brain cases.** Pinto and colleagues report "divided perception but undivided consciousness" in split-brain patients [@pinto2017]. That is evidence *against* a simple splitting of the self. Book-length treatments disagree about how many subjects such patients host [@schechter2018; @bayne2010].

**Psychedelic and meditative states.** Psychedelic states have been associated with increased entropy of spontaneous brain activity [@carhartharris2014; @carhartharris2018]. Meditators report states of "pure" consciousness, which Metzinger analyses as *minimal phenomenal experience* [@metzinger2020; @metzinger2024].

The record view makes a definite claim about these cases. It is the self-model, not experience as such, that requires integration. So experience can in principle persist, at reduced $u_r$, when the self-model is attenuated or taken apart, as long as the brain keeps forming lasting records. If minimal phenomenal experience is such a state, as its phenomenology suggests, the view has room for it.

Cosmopsychism faces the mirror-image task of explaining how one subject divides [@miller2018]. The record view gives it a physical correlate: subjects are as many as the separately integrated record structures. Whether this helps or merely relabels the problem is left open.

## 5.6 Rough numbers: a human brain and a language model

The verdicts of §5.2 and §5.4 are qualitative. This section is a napkin check on them for a human brain and a large language model, at inference and in training; it computes no values of $R$. Every input comes from a cited source, except for a few stated assumptions. The arithmetic is in the repository's `analysis/napkin.py`, and `analysis/sources.md` gives each input's locator and verification level and lists the assumptions.

Two caveats apply throughout. The comparisons are between unlike things: a synaptic event is not a floating-point operation. And several inputs are estimates made in rodents or flies, not measurements in humans. Temperatures of 310 K for the brain and 300 K for a fly and for a data centre's surroundings are assumed.

**Dissipation.** The brain runs on about 20 W [@balasubramanian2021] and weighs about 1.5 kg [@herculanohouzel2012]. An NVIDIA H100 GPU is rated at up to 700 W, with a peak dense throughput of about $10^{15}$ 16-bit operations per second [@nvidiah100; @andersch2022]. Its die is 814 mm$^2$ [@andersch2022]. If the die is no thicker than the 775 µm wafer it is cut from, it weighs at most 1.5 g [@henins1964; @svmisv029].

| Quantity | Human brain | One H100 GPU |
|---|---|---|
| Power (W) | 20 | 700 |
| Mass (g) | 1,500 | ≤ 1.5 (die) |
| Energy rate density (erg s$^{-1}$ g$^{-1}$) | $1.3\times10^{5}$ | ≈ $4.8\times10^{9}$ (module power over die mass) |
| Entropy production ($k_B$ s$^{-1}$) | $4.7\times10^{21}$ | $1.7\times10^{23}$ |
| Landauer ceiling (bit erasures s$^{-1}$) | $6.7\times10^{21}$ | $2.4\times10^{23}$ |
| Elementary events s$^{-1}$ | $2.6\times10^{13}$–$1.5\times10^{14}$ synaptic | $9.9\times10^{14}$ operations (peak) |
| Energy per event (J) | $1.3\times10^{-13}$–$7.6\times10^{-13}$ | $7.1\times10^{-13}$–$1.9\times10^{-12}$ |
| Energy per event in units of $kT\ln 2$ | $4.4\times10^{7}$–$2.6\times10^{8}$ | $2.5\times10^{8}$–$6.5\times10^{8}$ |

: **Table 2.** Dissipation. Synaptic events are neocortical synapses [@tang2001] times the mean firing rate the cortical energy budget allows, 0.16 to 0.94 spikes per second [@lennie2003], with the whole brain budget charged to them. The GPU range runs from peak throughput down to the 38% utilisation achieved in Llama 3 training [@grattafiori2024].

By Chaisson's measure the GPU's energy rate density is some $4 \times 10^4$ times the brain's, and per device it produces 36 times as much entropy. It also performs more elementary events per second. The steps of §4 that grade dissipation per gram, Chaisson's energy rate density and the E·I/M check, therefore rank the chip far above the brain. Per elementary event, however, the two are within about an order of magnitude of each other, at some $10^8$ times the Landauer bound.

**Inference.** A GPU serving a 70-billion-parameter model produces about 2,700 tokens per second [@mlcommons2024], or about 0.26 J per token at its rated power. Its weights are frozen. Each token writes an entry to the key–value cache, which holds at most 17 bits of information, the base-2 logarithm of the size of a Llama 3 model's vocabulary [@grattafiori2024]. The cache is dropped when the request ends, after about 45 s for a reply of about 290 tokens on the benchmark used [@mlcommons2024], and nothing integrates it into a self-model. At inference the model therefore scores near zero on $R$, whatever its hardware and whatever that hardware weighs. The chip's dissipation, which puts it on top in the dissipation-based steps of §4, does not enter $R$; only the price of records does.

**Training.** Training does form lasting records, the weights. Table 3 compares how much information a brain and a model in training retain per joule.

| System | Retained information (bit) | Energy (J) | Bits per J | Fraction of the Landauer limit |
|---|---|---|---|---|
| Human: whole brain budget over 70 years | $1.0\times10^{9}$ | $4.4\times10^{10}$ | 0.023 | $6.7\times10^{-23}$ |
| Human: plasticity share only | $1.0\times10^{9}$ | $4.9\times10^{8}$–$1.4\times10^{9}$ | 0.73–2.1 | $2.2\times10^{-21}$–$6.1\times10^{-21}$ |
| Fruit fly: marginal cost of long-term memory | — | — | 100 | $2.9\times10^{-19}$ |
| Llama 3.1 405B training | ≤ $8.1\times10^{11}$ | $7.8\times10^{13}$ | ≤ 0.010 | ≤ $3.0\times10^{-23}$ |
| GPT-3 training | ≤ $3.5\times10^{11}$ | $4.6\times10^{12}$ | ≤ 0.076 | ≤ $2.2\times10^{-22}$ |

: **Table 3.** Retained information per joule; higher is better. The human figure is Landauer's estimate of the functional information adults retain, from reading and picture-recognition experiments [@landauer1986]. The plasticity share, 1–3% of brain energy, chains three rodent-based estimates: plasticity costs 4–11% of the energy of fast excitatory transmission [@karbowski2019], postsynaptic glutamate receptors take half of signalling energy [@howarth2012], and signalling takes at least 55% of the total [@engl2015]. The fly figure is a preprint estimate from behavioural data [@girard2023]. The model figures assume at most 2 bits of extractable knowledge per parameter [@allenzhu2024], a saturation capacity, so they are upper bounds. Training energies are Meta's 30.8 million H100 hours at rated power [@meta2024] and Patterson and colleagues' estimate of 1,287 MWh for GPT-3, which includes host power and data-centre overhead [@patterson2021]. The rows draw their energy boundaries differently.

A human retains about $10^9$ bits of functional long-term memory on a lifetime budget of about $4 \times 10^{10}$ J, or about 0.02 bits per joule. Training Llama 3.1 405B retained at most about 0.01 bits of extractable knowledge per joule, and GPT-3 at most about 0.08. Charged only for plasticity, the brain retains 0.7–2 bits per joule. Against the human brain, a model in training thus retains at most about 3 times as many bits per joule, and possibly some 200 times fewer, depending on the model and on how the brain is charged.

Every row of Table 3 lies between about $3 \times 10^{-23}$ and $3 \times 10^{-19}$ of what the Landauer limit allows. Brain and model both pay far more than the Landauer price for each bit they keep, and neither pays clearly less than the other. So neither the price term of $R$ nor the actual cost separates them. What separates them is $u_r$: a brain's records feed a self-model that the organism uses to keep itself alive, and a model's weights feed none (§5.4).

**What follows.** Dissipation per gram favours the chip by four orders of magnitude, which is why the dissipation-based steps of §4 fail. At inference the record measure puts the model near zero, because it forms no records that outlast the request and integrates none into a self-model. In training the verdict rests on $u_r$, the least formalised factor of the measure. That is a weakness of the measure. It is also a prediction: a system whose persistent records were integrated into a self-model it needed for its own continued existence would score with brains, whatever it was made of.

# 6. Cosmological context

## 6.1 The low-entropy past

Everything the record view relies on runs on the universe's low-entropy past. That includes the formation of traces, the costs of memory and agency, and the entropy production of the waking brain. Rovelli's analysis of traces makes the dependence explicit. Trace formation "transforms initial low entropy (free energy) into available information" [@rovelli2022]. Wolpert and Kipper show that the kind of memory that informs only about the past is the kind that exploits the second law. They also identify a formal difficulty in deriving that law from the Past Hypothesis [@wolpert2024; @albert2000].

On the record view, then, **the capacity for experience is fuelled by the initial condition of the universe**. That is a consequence of the view, not an argument for it. It is stated here because it organises the related questions.

Four such questions deserve brief mention.

**Boltzmann brains.** These are observers produced by rare fluctuations rather than by cosmological history. They threaten the cognitive stability of some cosmologies [@dyson2002; @albrecht2004; @carroll2017]. The record view ties experience to the formation of records along a thermodynamic gradient, so it inherits this problem but does not add to it.

**Goff's teleological reading.** Goff's recent proposal reads the same facts as evidence of cosmic purpose [@goff2023].

**England's dissipative adaptation.** England's work offers a non-teleological alternative. Matter driven by an external energy source tends to organise into structures that absorb and dissipate work efficiently, and some of those structures keep records [@england2015; @perunov2016]. This paper prefers the non-teleological reading. It treats teleology as a minority option that the record view neither needs nor excludes.

**Gołosz's objection.** Gołosz argues that the arrows of traces and of thermodynamics are themselves "only arrows in time" [@golosz2025]. If he is right, the record view's dependence on the thermodynamic arrow is a dependence on something still awaiting a deeper explanation.

## 6.2 Related speculations (not part of the argument)

Several results suggest closer links between time, thermodynamics and observers. None of them is used in the argument above.

- **Thermal time.** On the thermal time hypothesis, the flow of time in a generally covariant theory is fixed by the thermodynamic state [@connes1994].
- **Gravity as thermodynamics.** Jacobson derived the Einstein equation as an equation of state [@jacobson1995].
- **Time from correlations.** On the Page–Wootters mechanism, time emerges from correlations between a system and a clock subsystem in a globally static state [@page1983]. The mechanism has been illustrated experimentally with photons [@moreva2014]. The Page–Wootters clock is close kin to the clock-observer of §2.5 [@devuyst2025].
- **Opposite arrows.** Schulman analysed systems whose thermodynamic arrows of time point in opposite directions [@schulman1999]. On the record view, such systems would host records, and so proto-experience, ordered in opposite temporal directions.

These are mentioned as directions, not as support.

# 7. Objections and replies

**Objection 1: illusionism.** Illusionists hold that there is no phenomenal "glow" to locate. There are only representations that misrepresent the brain's states as having phenomenal properties [@frankish2016; @dennett2016]. If they are right, the question of where proto-experience sits has a false presupposition.

*Reply.* The paper is explicitly conditional on the falsity of illusionism. The comparative argument of §3.3 concerns where experience would be *if* the panpsychist or Russellian picture held. Even so, the illusionist can accept much of the paper. The ladder of observerhood, the thermodynamics of records and the empirical test in §8 are neutral between realism and illusionism about phenomenal properties. They would then describe the physical basis of the representations that the illusionist thinks generate the illusion.

**Objection 2: the metabolic confound.** Perhaps the irreversibility of brain dynamics tracks nothing but activity or metabolism. Both fall in sleep and anaesthesia [@alkire1995; @shulman2009]. Irreversibility rises with physical and cognitive effort [@lynn2021]. And awareness has a metabolic threshold [@stender2016]. The brain evidence of §2.8 would then show only that conscious brains are busy brains.

*Reply.* This is the most important empirical objection, and it is not answered here. It is turned into a test (§8). Metabolism is not a factor of $R$. $R$ counts the price of persistent, integrated records, and dissipation spent on activity that forms no lasting, used records adds nothing to it. Measured irreversibility is therefore a proxy for $R$ that activity contaminates. That gap is exactly what §8 tests. The record view predicts that the relation between irreversibility and consciousness *survives* controls for signal power, variance and metabolic proxies, if the irreversibility that remains reflects the formation of records. The view also predicts that the relation holds in cases where activity and consciousness come apart. If irreversibility is fully explained by activity or metabolism, the within-brain support for the view fails. The conditional philosophical argument of §3 would survive, but it would have lost most of its contact with evidence. Claim 7's open question would be settled against the view, and the within-brain predictions of claim 8 would have failed.

**Objection 3: unfalsifiability.** The view's verdicts on cells, chips and language models cannot be checked, since such systems cannot report.

*Reply.* This is conceded for systems that cannot report, and every panpsychist view shares the cost. Two things mitigate it. First, the view's verdicts are *determinate* once records, persistence and integration are defined: given the physics, the measure in §4 assigns values, even where no report can confirm them. Second, the view makes *comparative* predictions inside brains, where reports exist, and those can fail (§8). A theory that can be refuted where it can be tested earns some credit for its extrapolations, though not much.

**Objection 4: erasure and waste.** Erasure is irreversible and costs entropy, so a record view seems committed to treating erasure as experience-producing. Worse, a measure built on entropy production seems to reward waste.

*Reply.* On erasure, the measure of §4 counts records that persist and are integrated into the system's self-model, not irreversibility as such. Erased information leaves as heat that nothing integrates, so its integration factor $u_r$ is near zero, however much heat the erasure produces. The same holds for the waste heat of a star or a jet engine.

On waste, $R$ charges each record its Landauer price, $k_B \ln 2$ per bit it holds, and not the dissipation actually spent in forming it. Waste therefore does not count: a wasteful memory does not outscore an efficient one that forms the same records. Charging the price also needs no attribution of dissipation to particular records. Sagawa and Ueda showed that only the sum of the costs of measurement and erasure is bounded, and that how it divides between the two depends on how the memory is built [@sagawa2009]. What stays open is the erasure problem itself. The reply depends on non-circular definitions of record, persistence and integration, which are not yet available and which must not quietly reintroduce the mental vocabulary they are meant to ground. **This objection is marked open.**

**Objection 5: the combination problem.** However records are integrated, why should many micro-experiences add up to one subject [@james1890; @chalmers2016; @coleman2014]?

*Reply.* The record view does not solve the combination problem. It eases it in two ways. The micro-level bearers on the record view are not fixed, identical particles. They are events that already have physical relations of integration: a self-model is a structure of records about records. And integration comes in degrees. The factor $u_r$ of §4 is the fraction of a record's information that the system integrates into its self-model, and Kolchinsky and Wolpert's interventional method suggests how to measure it [@kolchinsky2018]. So the question of how much combination has occurred becomes partly empirical. What is not explained is why integrated records should yield a single *subject*. The question is left where Chalmers's survey leaves it [@chalmers2016]. A record view also faces the cosmopsychist's mirror-image problem of decombination [@miller2018], and has nothing new to say about it beyond §5.5.

**Objection 6: clock-observers suffice.** Physics has needed only clock-observers to define states and entropies (§2.5). So the "observer" of physics lends no support to a recording observer, let alone to an experiencing one.

*Reply.* This is correct, and it is why §3.1 names the bridge theorem as missing. The record view does not depend on it. Its support comes from the separate claim, grounded in quantum foundations and the thermodynamics of information, that *facts* need records [@zurek2018; @dibiagio2021; @rovelli2022]. If the bridge theorem were proved, the record view would gain a link to fundamental physics. If it were refuted, the view would lose only the suggestion that quantum gravity points toward it.

**Objection 7: the non-emergence argument and the vitalism analogy.** Strawson's argument that experience cannot emerge from the wholly non-experiential motivates panpsychism [@strawson2006]. But a structurally similar argument was once made for life, and vitalism was wrong. Perhaps experience will emerge from structure just as life did.

*Reply.* The paper uses Strawson's argument only as *motivation* for its conditional. It does not need the argument to be sound. On the analogy, two points.

First, the usual disanalogy holds. Life was always characterised by functions, such as metabolism, reproduction and self-maintenance, that physics could in principle realise. Experience is not obviously characterised that way.

Second, and more interestingly, the record view is *compatible* with the vitalism analogy. The physics that dissolved vitalism was thermodynamics: the theory of open, dissipative systems that maintain themselves away from equilibrium [@schrodinger1944; @prigogine1978]. The record view locates experience in exactly that physics. If the analogy wins and experience turns out to be strongly emergent or functional, the measure in §4 would survive as a measure of the physical *correlate* of experience rather than of its bearer. The comparative argument is useful whichever way the dispute between emergence and panpsychism comes out.

# 8. Proposed empirical test

The following study is described, not executed. A fuller plan, with candidate analyses, is in the repository's `future-work/empirical-plan.md`.

**Question.** Does the entropy production, or time-irreversibility, of large-scale brain dynamics track the level of consciousness *after* controlling for signal power, signal variance and metabolic or activity proxies?

**Assumption.** Measured large-scale irreversibility is at best a proxy for $R$. It includes dissipation spent on activity that forms no lasting, used records. The test asks whether irreversibility tracks consciousness beyond activity and metabolism. The record view predicts that it does, if the irreversibility that remains reflects the formation of records. That is assumed here, not shown. If it is false, a surviving effect shows only that irreversibility tracks consciousness, not that records matter.

**What already exists.** The review found no study that regresses large-scale irreversibility on metabolism or signal power within subjects across states of consciousness. Two results come close. Gilson and colleagues report that model-based entropy production correlates with the variance of the model's inputs [@gilson2023]. Yao's sleep-EEG study tracks an amplitude-related nuisance variable [@yao2024]. One preprint shows, in mice and outside the study of consciousness, that changes in irreversibility can be separated from response amplitude [@dmochowski2026]. The confound analysis therefore appears to be new. A focused search before pre-registration should confirm this.

**Data.** All of the following were confirmed to exist at their landing pages; details are in the plan.

- *Graded propofol sedation, fMRI.* Two datasets: 26 healthy volunteers, including behavioural unresponsiveness [@ds006623]; and 17 healthy volunteers sedated at awake, light, deep and recovery levels, at rest and during an auditory task [@ds003171].
- *Propofol sedation, EEG.* A dataset deposited by Chennu and colleagues in the University of Cambridge repository [@chennu2016].
- *Sleep.* Simultaneous EEG–fMRI in 33 sleeping participants, with sleep stages scored [@ds003768]. Also 197 whole-night polysomnographic recordings with hypnograms [@sleepedfx].
- *Seizures.* Scalp EEG of 198 annotated seizures in 22 paediatric patients [@chbmit]. This dataset has no annotation of consciousness during seizures, a limitation discussed below.

**Method.**

1. Reproduce the published estimators: entropy production and probability-flux curl [@sanzperl2021], and multivariate Ornstein–Uhlenbeck entropy production [@gilson2023]. Add trajectory-based irreversibility estimators that measure how distinguishable a process is from its time reverse [@roldan2010; @kawai2007].
2. For each subject, state and parcel, compute the nuisance covariates: signal variance, band-limited power, amplitude of low-frequency fluctuations, global signal amplitude, and, where available, physiological proxies.
3. Fit mixed-effects models of irreversibility on state, with subjects as random effects, with and without the covariates.
4. Add surrogate controls that preserve each signal's power spectrum and amplitude distribution but destroy time asymmetry. Report the effect of state as a partial effect, net of covariates and surrogates.
5. Pre-register the estimator, parcellation, covariates, inclusion criteria and the decision rule below.

**Discriminating cases.**

- *Seizures* are the key falsification case. Consciousness is often lost while activity and metabolism are high [@blumenfeld2012], and local irreversibility peaks [@schindler2016]. Open scalp EEG lacks consciousness labels, so a decisive test needs data that separate seizures with impaired awareness from seizures with preserved awareness. Such data may require collaboration.
- *Disorders of consciousness and locked-in syndrome* separate consciousness from responsiveness. Open data are scarce, and the one candidate dataset found has unclear licensing.
- *Lucid dreaming* separates consciousness from external responsiveness in the other direction. Existing data from two-way communication with dreamers are available only on request [@konkoly2021].

**Predictions and decision rule.**

- *Record view supported.* The partial effect of consciousness level on irreversibility survives the covariates and surrogates, with the same sign as in the uncontrolled analyses. That is what the record view predicts if the irreversibility that remains reflects record formation.
- *No within-brain support for the record view.* The effect is fully explained by power, variance, activity or metabolic proxies, so that the partial effect is null with adequate power. Irreversibility would then track activity and nothing more, and the record view's empirical claim would fail.
- *Refuted in seizures.* Whole-brain irreversibility, net of covariates, is *high* during seizures in which awareness is impaired. Then the view's escape (§5.3) would need an independent measure of record formation. Without one, the claim that irreversibility marks consciousness fails.

**A second study (future work).** The metrics of §4 can also be set against how people judge AI systems. Public data on past AI models give their parameters, training compute, hardware and release dates [@epochai2026]. For a panel of such models one can compute energy rate density, the $E\,I/M$ check, information-only stand-ins and $R$. Each can then be compared with graded ratings of how conscious people judge each model to be. Colombatto and Fleming used such a scale, from 1 to 100, and most of their participants attributed some possibility of phenomenal consciousness to ChatGPT [@colombatto2024]. Folk ratings are not ground truth. The record view expects them to diverge from $R$, which is near zero for every frozen model. The informative case is whether ratings rise for models with persistent memory beyond what their capability predicts. The plan is in the repository's `future-work/model-attribution-study.md`.

# 9. Author's credences

The following are subjective credences, stated so that readers can calibrate. They are not results.

- That the time-irreversibility of large-scale brain dynamics is a reliable marker of consciousness *in brains*: **about 60%**. The seizure and metabolism evidence reviewed in §2.8 is the main reason it is not higher.
- That the record-based measure is the right *kind* of measure for systems in general: **about 15%**.
- That an explicit formal statement of "proto-experience is carried by irreversible recording events" is not already in the literature: **about 60% before the review**. The review found partial anticipations but no full statement in peer-reviewed work (§2.10). The author has not revised this figure.
- That any panpsychism-family view is true: **undecided**. For the record, the AI system with which these ideas were developed offered a rough split during the conversation. It put about 20% on fundamental (proto-)experience, 30% on strong emergence, 25% on illusionism and 25% on the question being ill-posed. That split is reported as a record of the dialogue, not as evidence.

**What would most change these numbers.**

- The test in §8 coming out against the record view would move the first credence down sharply and the second down moderately.
- A proof of the bridge theorem in §3.1 would move the second credence up.
- Discovery of an earlier full statement of the thesis would move the third credence to near zero. The rest of the paper would stand as a defence of that earlier statement.

# 10. Conclusion

If experience has a physical locus of the kind panpsychists and Russellian monists want, then particles are the wrong place to look. They keep no records and do nothing to distinguish one from another. Collapse events require physics that experiment is pressing hard. Integrated structure without persistent records assigns rich experience to an inactive grid of logic gates.

The irreversible recording event is a better candidate. It needs only decoherence and thermodynamics. It is graded by the entropy a system spends, per gram, on persistent records that it integrates into a model of itself. Measures built on information alone call the grid highly conscious. Weighting information by dissipation per gram, as $E\,I/M$ does, removes that verdict but ranks processors above brains. Counting only records that persist and are integrated removes both errors. A language model at inference forms no records that outlast a request and integrates none into a self-model, so it scores near zero, whatever its hardware. In training, the verdict rests on the integration term alone. And the view ties proto-experience to the same low-entropy past that makes memory, agency and the arrow of time possible.

The view inherits two hard problems, combination and erasure, and does not pretend to solve them. It also inherits an empirical liability: the brain evidence that most supports it is confounded by metabolism and threatened by seizures. That liability is also its advantage over its rivals, because it can be tested, and §8 says how.

# AI assistance disclosure

The ideas in this paper were developed in dialogue with Claude (Anthropic). The manuscript, literature review and bibliography were drafted with the assistance of Claude Code. Every reference was checked against a primary record (arXiv, DOI or publisher record, PubMed or Europe PMC, the dataset's landing page, or a catalogue or scan for older books). Where the text of a source could not be read, the paper relies only on what its abstract or a verified secondary source states. `notes/literature-review.md` records the level of verification for each entry. The author takes full responsibility for the content.

# References {.unnumbered}

::: {#refs}
:::
