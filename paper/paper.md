---
title: "Records, Not Collapse: Irreversible Recording as the Physical Locus of Proto-Experience"
author: "Viacheslav Zhygulin (<s.zhygulin@gmail.com>)"
date: "Draft of November 2026. Speculative position paper, not peer-reviewed."
abstract: |
  Panpsychist and Russellian-monist views hold that experience, or proto-experience, belongs to the basic physical world, but they have no agreed answer to *where* in physics it sits. Classic panpsychism puts it in particles. Orchestrated objective reduction (Orch-OR) puts it in gravitational wavefunction collapse. Integrated information theory (IIT) puts it in integrated cause–effect structure. This paper argues, conditionally, that if any such view is true, the natural physical bearer of graded proto-experience is the *irreversible recording event*: the formation of a persistent, decohered record whose formation produces entropy. On this view a system's degree of experience tracks its entropy production per unit mass, multiplied by the information in the persistent records, left by past recording events, that its own dynamics draw on. The paper first surveys the relevant work in quantum gravity, quantum foundations, the thermodynamics of information, theories of consciousness and nonequilibrium neuroscience. It finds the thesis partially anticipated but not stated as a whole. It then separates clock-observers, which recent quantum-gravity work needs, from recorder-observers, which facts need, and names the missing theorem that would join them. It proposes that measure and applies it to stars, processors, storage devices, logic-gate grids, hot molecules, sleep, seizures and language models. Counted as storage capacity, order-of-magnitude numbers put a human brain and a GPU-based language model within a factor of about 300 of each other; counted as functional knowledge, the model leads. It then answers seven objections. It ends with a test that can be pre-registered: does the time-irreversibility of brain dynamics still track consciousness once metabolism and signal power are controlled for?
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
6. **[P]** The degree of proto-experience tracks $R = \dot\Sigma\, I / M$: a system's entropy production rate, times the information in the persistent records its own dynamics draw on, per unit of its mass. Dissipation without such records, as in a star or a jet engine, scores zero. So do records that nothing runs on, as in a storage device (§4).
7. **[C]** In brains, the time-irreversibility of large-scale dynamics falls in sleep, anaesthesia and disorders of consciousness (§2.8). Whether this survives controls for metabolism and signal power is open, and local seizure data point the other way (§5.3).
8. **[P]** The thesis makes comparative predictions inside brains that can be tested on open data, and it states what would refute it (§8–9).
9. **[P]** Order-of-magnitude estimates put a human brain and a GPU system running a large language model within a factor of about 300 of each other on $R$, when bits are counted as storage capacity. Which one leads turns on the mass of the GPU packages that hold the model's weights, which no source consulted gives. Counted as functional knowledge, the model leads. For a model of a given size, inference and training score alike. The measure therefore does not rank brains robustly above such models (§5.6).

# 1. Introduction

Panpsychism and its relatives have returned to serious philosophy of mind. The motivation is familiar. Physics describes the structure and dynamics of matter, not its intrinsic nature. Experience is the one intrinsic nature we know directly. So perhaps experience, or some proto-phenomenal precursor of it, *is* that intrinsic nature [@russell1927; @strawson2006; @goff2017; @alter2015]. Whatever one makes of the argument, it leaves a question that its defenders have mostly left open: **which physical events or structures carry the proto-experience?** The answer matters. It fixes which systems have more experience and which have less. It shapes the combination problem. And it decides whether the view makes any contact with evidence.

Three answers dominate. The oldest says proto-experience belongs to the fundamental particles or fields themselves. Orch-OR says it belongs to moments of objective reduction, a gravitationally induced collapse of the wavefunction [@penrose1996; @hameroff2014]. IIT says it belongs to integrated cause–effect structure, measured by $\Phi$ [@tononi2004; @tononi2016; @albantakis2023]. IIT is not a panpsychism in the strict sense, but it shares the feature that matters here: it locates experience in a physical property that many non-living systems have.

This paper defends a fourth answer, *conditionally*. It does not argue that panpsychism is true. It argues that **if** one wants a physically grounded, graded proto-experience, then the best physical bearer is the *irreversible recording event*. Such an event leaves a trace that persists, cannot in practice be undone, and costs entropy to make. The degree of experience then tracks **a system's entropy production per unit mass, multiplied by the information in the persistent records that its own dynamics draw on**. Recording events make the records; how much experience a system has depends on how hard it runs on them.

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

As far as this review could find, none of this work identifies the Whiteheadian occasion with *thermodynamically irreversible record formation*, or grades experience by entropy production weighted by the information in records a system runs on. The searches for such a link, which combined Whitehead's terms with decoherence, irreversibility and entropy, returned nothing relevant (see `notes/literature-review.md`).

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

  This is the nearest mainstream neighbour. It differs from the present thesis in three ways. Its scale-free hypothesis is stated for *living* systems. Its stated aim is a framework that "makes no assumptions beyond those of quantum information theory", not a metaphysics of experience. And it does not grade experience by dissipation multiplied by the information in records the system's dynamics draw on.
- Kolchinsky and Wolpert supply the interventional template for "operative" records and the stricter, semantic variant of the measure (§4), but make no claim about experience [@kolchinsky2018].
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
| **Irreversible records that the system's dynamics run on** | **This paper** | **No** | **Yes** | **Near zero** | **Proposal** |

: **Table 1.** Candidate loci of (proto-)experience.

**Verdict: partially anticipated.** Each component of the thesis has precedents.

- *Records, irreversibility or memory as the bearer.* Anticipated in form by Whitehead and the memory tradition. Physically, it is anticipated by Rovelli's account of traces and by Fields, Glazebrook and Levin, and as a claim about experience by Peyru's recent preprint.
- *A graded measure tied to entropy production.* Anticipated empirically by the nonequilibrium-brain literature, and formally in part by Ito, Oizumi and Amari. Its normalisation by mass is Chaisson's.
- *Use of records by the system's own dynamics.* Anticipated formally by Kolchinsky and Wolpert's semantic information and by the free-energy principle.

No source found states the conjunction: a *conditional* argument that, among the candidate loci, the irreversible recording event is the best bearer of graded proto-experience. Nor does any source pair that argument with a measure on which neither dissipation nor stored records score alone, or with an empirical test designed against the metabolic confound. The paper's claim to novelty rests on that conjunction and on the explicit link to the clock-observers of quantum gravity. It does not rest on any single component.

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

![**Figure 1.** The ladder of observerhood. Each rung adds a capacity to the one below. The record view locates recording events from rung 2 upward. Rungs 3 and 4 are not factors in its measure (§4): a system scores once its own dynamics run, under drive, on lasting records it holds, whatever its rung. Living systems do so from rung 3; a processor running a learned model does so without self-maintenance (§5.4).](figures/ladder.png){width=95%}

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

**Integrated information.** IIT is graded (D2) and needs no new physics (D1). It fails D3. A large grid of XOR gates, even an inactive one, has high $\Phi$ and so is highly conscious by IIT's lights. Tononi accepts that verdict [@aaronson2014phinal]. On the record view the same grid scores near zero, for a reason that is principled rather than ad hoc.

The grid's integration is static causal structure. While running, each XOR gate is logically irreversible, so the grid does dissipate when it updates. But that dissipation is *overwriting*: each cycle destroys the previous state. The grid forms no record that persists across cycles, and the only lasting structure its dynamics draw on is its wiring, which takes a few bits to specify. An inactive grid does nothing at all.

The point is not that IIT's integration is irrelevant. Section 4 keeps a trace of it in the boundary rule: what counts as one system is the part whose dynamics draw on the records, though $R$ does not grade integration as such. The point is that integration *without* such records should not count, and IIT has no means of excluding it.

**Records.** The record-based locus satisfies D1. It needs decoherence, which is established, and the thermodynamics of information, which is established and confirmed experimentally [@zurek2003; @berut2012]. It is graded (D2). It can be quantified by the entropy a system produces and by how much information its persistent records hold for its own dynamics (§4). It gives sensible verdicts in contrast cases (D3, §5).

It does not solve the combination problem, but it eases it (D4). Records already combine in a physically ordinary way: a self-model is a structure built of records about records. On the measure of §4, what counts as one system is fixed by which records its dynamics draw on. Combination then becomes a question about which records one system's dynamics draw on, which is open to empirical study, rather than a question about how windowless subjects merge. §7 says how far this goes.

The comparative claim is modest. It is not that records *are* experience. It is that, if experience has a physical locus of the kind panpsychists want, records are the best-placed candidate of the four.

# 4. Toward a measure

This section develops a measure in steps, because the dead ends are instructive. What it offers is a sketch, not a formalism.

**Step 1: entropy level.** A first thought is that experience tracks entropy. In the brain, wakeful states do show the largest repertoire of network configurations [@guevaraerra2016; @carhartharris2018]. But as a general measure, entropy level fails at once. Maximum entropy is thermal equilibrium, where nothing happens and no records form.

**Step 2: entropy production rate.** The natural repair is to move from entropy to its rate of production, a measure of how far a system is from equilibrium. This matches the brain data of §2.8: reduced consciousness lies closer to equilibrium [@sanzperl2021; @gilson2023]. But stars produce entropy at enormous rates.

**Step 3: normalise by mass.** Chaisson's *energy rate density* normalises energy flow by mass [@chaisson2001; @chaisson2011]. It is a measure of energy throughput rather than of entropy production, but it is a useful first proxy. His values, in erg s$^{-1}$ g$^{-1}$, are about 2 for the Sun, about 900 for plants, about $2 \times 10^4$ for the human body and about $1.5 \times 10^5$ for the human brain [@chaisson2014]; the inputs used in §5.6 give $1.3 \times 10^5$. Normalisation puts stars at the bottom. But machines come out on top. Chaisson gives about $2.7 \times 10^7$ for a Boeing 747 [@chaisson2014]. A modern accelerator chip is higher still: an H100 GPU module rated at up to 700 W, divided by the mass of its die (at most 1.5 g), gives about $5 \times 10^9$ erg s$^{-1}$ g$^{-1}$ (§5.6).

**Step 4: times information processed.** One might multiply mass-normalised dissipation by the information a system processes. That fails in the other direction. A hashing chip, such as a bitcoin miner, and a running grid of logic gates process information at gigahertz rates and would come out on top, although neither runs on more than its own fixed circuit. Dividing by dissipation instead, as in bits processed per joule, fails worse: a reversible computer would score highest while drawing on no lasting records at all.

**Step 5: times information in operative records.** The repair is to count not the information that passes through a system but the information held in its *persistent records* that its own dynamics draw on. Call these its **operative records**. A record is operative when it shapes how the system's state evolves. A synaptic strength shapes every spike that crosses the synapse, and a model's weights shape every token it computes. A record that is merely passed on, as when a file is copied, is data rather than a parameter of the dynamics, and it does not count. Nor does a record that nothing in the system reads, such as a crater or the photons a hot molecule emits.

This gives the measure proposed here:

$$
R \;=\; \frac{\dot\Sigma \; I}{M}.
$$

The terms are:

- $\dot\Sigma$ is the system's entropy production rate. In a steady state it is the heat the system dissipates divided by the temperature at which that heat is released, here in units of $k_B$ per second.
- $I$ is the information the system's operative records hold jointly, in bits. A record fixed by others, such as a cache computed from a model's weights and its input, or a redundant copy, adds only what it does not share with them. $I$ is bounded above by the records' storage capacity, and by how much information about the records the system's trajectory carries over the period being assessed, such as one sleep stage or one seizure. Each record's contribution is weighted by a persistence factor $p_r = \max(0,\, 1 - \tau_\text{dyn}/\tau_r)$, where $\tau_r$ is the record's lifetime and $\tau_\text{dyn}$ the system's characteristic dynamical time. A register overwritten at every step has $\tau_r \le \tau_\text{dyn}$ and contributes nothing; a record that lasts many steps counts almost in full.
- $M$ is the system's mass. The system is the smallest part whose dynamics draw on the records. A hard disk bolted to a furnace is two systems, not one, because nothing in the furnace runs on what the disk stores.

$R$ is measured in $k_B$ bit s$^{-1}$ g$^{-1}$. The proposal is that the degree of proto-experience is monotone in $R$.

The bearer is still the recording event. Past recording events made the records; $R$ grades a system by how hard its present dissipation runs over them. Forming a record adds to $R$ only once the system runs on it. That is why a model at inference, which forms no records that outlast the request, can still score, and why a crater, which holds records that nothing runs on, scores zero.

Each factor removes a class of false positives.

- Normalising by mass puts stars at the bottom, as in step 3.
- The information factor gives zero to whatever dissipates without operative records, such as stars, jet engines and the heat that erasure leaves behind. Grids of logic gates get only the few bits their regular wiring takes to specify; hashing chips get what their fixed circuits take (§5.2).
- The entropy factor gives zero to whatever holds records but is not driven, such as a powered-off disk or a USB stick in a drawer. A library or a spinning disk is driven, but nothing in it runs on its content, so the information factor gives it zero.

What scores is the conjunction: a system driven hard, per gram, while its dynamics run over a large store of lasting records. Dissipation per gram differs between a brain and a chip die by about four orders of magnitude, and between a brain and a whole GPU board by about one, so where a chip's boundary is drawn can matter as much as what it stores (§5.2, §5.6).

**Step 6: what the thermodynamics of information adds.** Two results in §2.7 shape the measure.

- *Location of dissipation is not a marker.* Sagawa and Ueda show that the minimum cost of acquiring information can be shifted between measurement and erasure by redesigning the memory. Only the sum is bounded [@sagawa2009]. A measure that charged each record for the entropy produced in forming it would therefore depend on how the memory happened to be built. $R$ avoids this by taking the system's whole entropy production and never attributing it to particular records.
- *Retention is not the same as use.* Still and colleagues show that a driven system's dissipation is bounded below by the *non-predictive* information it retains [@still2012]. Memory that is useless for prediction is waste heat. On $R$ such memory raises $\dot\Sigma$ without raising $I$, unless the system's dynamics draw on it. It therefore raises $R$, which is the measure's main weakness (see below).

$\dot\Sigma$ is the dissipation the system actually incurs, not the Landauer price of the bits it writes. That choice ties $\dot\Sigma$ to measurable metabolism, and it needs no attribution of dissipation to records. The coarse-grained entropy production of §2.8 is a lower bound on the part of $\dot\Sigma$ that large-scale dynamics carry. Its cost is that waste counts.

Self-maintenance and self-modelling, the third and fourth rungs of §3.2, are not separate factors in $R$. They matter because they are how living systems come to hold large operative records under sustained drive. A stricter variant would count in $I$ only *semantic* information in Kolchinsky and Wolpert's sense: the part that is causally necessary for the system's own continued existence [@kolchinsky2018]. That variant would give near zero to any system kept in existence by someone else, a language model included. It is not adopted, for two reasons. Semantic information is defined for whole self-maintaining systems, while $R$'s boundary picks out the part that runs on the records: the brain, not the organism. And the variant would rest the measure on its least formal part. §5.6 says what would turn on the choice.

For brains, two cautions apply. Within one brain over hours, $M$ is fixed and the stored records change little, so $R$ moves with $\dot\Sigma$ and with how much information about its records the brain's trajectory carries. And the entropy production estimated from large-scale brain signals is coarse-grained. Coarse-graining can only lower the entropy production one measures [@kawai2007; @roldan2010], so, up to estimator bias and model error, these estimates are lower bounds on the part of $\dot\Sigma$ that large-scale dynamics carry. They are not measurements of $R$, and they do not measure $I$. §8 tests only part of that gap.

**Erasure and waste (open).** Landauer erasure is irreversible and costs entropy. On $R$ its heat counts toward $\dot\Sigma$, but only in a system whose dynamics also run on operative records. A pure eraser has $I = 0$ and scores zero. The harder problem is waste. Of two systems that run on the same records, $R$ ranks higher the one that dissipates more, so an inefficient memory outscores an efficient one. Replacing $\dot\Sigma$ with the Landauer price of the bits actually written would remove the problem. But it would bring back the attribution problem of step 6, and it would lose the tie to metabolism.

The measure also needs non-circular definitions of "operative" and "drawn on", which must not quietly reintroduce the mental vocabulary they are meant to ground. Kolchinsky and Wolpert's interventional method suggests a template [@kolchinsky2018]. Here, a record would be operative to the extent that scrambling it changes how the system responds to its inputs, not merely what it passes on. **The waste problem is therefore marked here as unresolved.**

# 5. Contrast cases and predictions

## 5.1 Hot and cold molecules

Hackermüller and colleagues sent C$_{70}$ fullerenes through a Talbot–Lau interferometer after heating them with a laser. Interference visibility fell from 47% with no heating to zero at 10.5 W. The heated molecules emit thermal photons that carry which-path information into the environment [@hackermuller2004]. In the vocabulary of §3.2, the hot molecule makes irreversible records of its own path, while the cold one does not.

The record view therefore places recording events in the hot molecule and not in the cold one, on rung 2. That is a definite consequence about where bearers occur, not about degree, and a deliberately counterintuitive one. What it shows is that the view is not about complexity or life as such. It is about where the world is being irreversibly written on. The measure of §4 adds that being written on is not enough. The hot molecule's records leave with photons that nothing in the molecule reads, so its $I$, and with it $R$, is zero, as is the cold molecule's, far below any organism.

## 5.2 Gates, grids, storage and processors

The XOR grid scores near zero. Its states are overwritten at each update, so they add nothing to $I$, and the only lasting structure its dynamics draw on is its wiring, a regular grid that takes a few bits to specify (§3.3). An inactive grid scores zero.

A storage device scores zero for the opposite reason. A hard disk or a USB stick holds many bits, but nothing in it runs on them. Unpowered, it dissipates nothing. Powered, it dissipates in ways that do not depend on what it stores, and the content it passes on is data, not a parameter of its dynamics.

A processor, and a hashing chip such as a bitcoin miner, score in proportion to the program, fixed circuit and other lasting state their dynamics draw on. At die scale the entropy factor dominates. A GPU die dissipates some $4\times10^4$ times more per gram than a brain, so at die scale a chip needs correspondingly little operative information to match one. At the power density of a GPU die, about $3\times10^4$ bits would match the brain's $R$ counted by functional memory, and about $2\times10^{10}$ bits would match it counted by synaptic capacity (§5.6). A conventional program, or the circuit of a hashing chip, may therefore reach the brain's functional $R$, though not its capacity. A processor running a large learned model is the clearest case, because the model's weights are operative records in the sense of §4 (§5.4, §5.6).

The record view thus disagrees with IIT about the grid. It disagrees with crude energy-throughput measures about jet engines, and it agrees with neither about stars. About processors it agrees with energy-throughput measures more than one might expect: what puts a chip in a brain's range is mostly how much it dissipates per gram.

## 5.3 Brains: sleep, anaesthesia, disorders of consciousness and seizures

The record view predicts that, *within* a brain, $R$ falls when consciousness is lost. Over hours a brain's mass is fixed and its stored records change little, so $R$ can fall in two ways: through $\dot\Sigma$, or through $I$, if the brain's dynamics come to carry less information about its stored records. The observed fall in large-scale irreversibility across sleep, anaesthesia and disorders of consciousness fits this prediction (§2.8). But the fit is weak evidence, for two reasons.

**The metabolic confound.** Metabolism also falls in these states, and by large amounts [@alkire1995; @shulman2009; @stender2016]. Irreversibility also rises with effort in healthy subjects [@lynn2021]. On the measure of §4, falling metabolism is not a rival explanation but one factor of $R$. That makes the data easier to fit and harder to learn from. If consciousness tracked metabolism and activity alone, the information factor would be idle within brains, and $R$ would reduce there to Chaisson's energy rate density. This is the most important empirical objection to the thesis (§7, objection 2). §8 is designed to test it.

**Seizures.** Generalised and complex partial seizures often abolish consciousness [@blumenfeld2012]. Yet in intracranial EEG the most time-irreversible signals occur *during* seizures [@schindler2016]. If whole-brain entropy production were high during seizures in which consciousness is lost, then the simple claim that irreversibility marks consciousness would be refuted.

The record view is not thereby refuted, for a principled rather than ad hoc reason. Seizures are hypersynchronous, stereotyped and high in dissipation. On the measure of §4 they raise $\dot\Sigma$, while the brain's trajectory, locked into one pattern, carries little information about its stored records, so $I$ falls. Whether $R$ rises or falls depends on which factor moves more. The escape is therefore only as good as an *independent* measure of how much stored information the dynamics carry. Without one, the move would be unfalsifiable. Seizures are therefore the sharpest available test case (§8). The existing evidence is local and single-channel, and so does not settle the matter for whole-brain measures.

## 5.4 Large language models

A language model at inference time, with fixed weights, forms no internal records that outlast the request. Its weights are frozen. Its key–value cache is dropped when the request ends, or at most kept across the turns of one conversation. The only lasting trace, the transcript, sits outside the system.

On the measure of §4, however, what counts is not whether records are being formed but whether the system's dynamics run over persistent ones. A model's weights are operative records in the full sense. They persist for the life of the deployment, and they shape every token the model computes. Inference therefore scores far above a storage device, which holds bits but does not run on them, and far above a hashing chip, which runs but holds almost nothing. Training forms lasting records, the weights, but $R$ does not reward formation as such, so training and inference score alike per device (§5.6).

Some architectures update weights or memory modules during use. Examples are test-time-training layers, whose hidden state "is a machine learning model itself" updated by self-supervised steps [@sun2024], and neural long-term memories that learn "to memorize historical context" at test time [@behrouz2024]. On $R$ this changes little, since the weights already count. It would matter on the stricter, semantic variant of §4, and then only if those records came to be needed for the system's own continued existence.

This raises an identity puzzle that mirrors the combination problem. Many diverging copies of one model might each accumulate their own records. The question is then what makes a single subject rather than many, a "decombination" problem for machines. The boundary rule of §4 answers part of it: copies that do not draw on one another's records are separate systems. What it leaves open is the question §7 leaves open for brains, why integrated records should make one subject.

The verdict on language models is the paper's most contestable result. §5.6 finds that a GPU system running a large model comes within a factor of about 300 of a human brain on $R$ when bits are counted as storage capacity, and above it when they are counted as functional knowledge. That departs from assessments based on theories of consciousness, which judge current AI systems unlikely to be conscious [@butlin2023; @chalmers2023]. Either the measure is wrong about such systems, or $I$ must be restricted to semantic information, or those assessments are wrong.

## 5.5 Splitting and dissolving the self

If the self is a structure of integrated records, its unity should depend on connectivity and should come in degrees. Two bodies of evidence bear on this, and both are contested.

**Split-brain cases.** Pinto and colleagues report "divided perception but undivided consciousness" in split-brain patients [@pinto2017]. That is evidence *against* a simple splitting of the self. Book-length treatments disagree about how many subjects such patients host [@schechter2018; @bayne2010].

**Psychedelic and meditative states.** Psychedelic states have been associated with increased entropy of spontaneous brain activity [@carhartharris2014; @carhartharris2018]. Meditators report states of "pure" consciousness, which Metzinger analyses as *minimal phenomenal experience* [@metzinger2020; @metzinger2024].

The record view makes a definite claim about these cases. It is the self-model, not experience as such, that requires integration. So experience can in principle persist when the self-model is attenuated or taken apart, since $R$ needs only that the brain's dynamics keep running on its records. If minimal phenomenal experience is such a state, as its phenomenology suggests, the view has room for it.

Cosmopsychism faces the mirror-image task of explaining how one subject divides [@miller2018]. The record view gives it a physical correlate: subjects are as many as the separately integrated record structures. Whether this helps or merely relabels the problem is left open.

## 5.6 Rough numbers: a human brain and a language model

The verdicts of §5.2 and §5.4 are qualitative. This section puts order-of-magnitude numbers on the factors of $R$ for a human brain and for a large language model, at inference and in training. Every input comes from a cited source, except for a few stated assumptions. The arithmetic is in the repository's `analysis/napkin.py`, and `analysis/sources.md` gives each input's locator and verification level and lists the assumptions.

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

By Chaisson's measure the GPU's energy rate density is some $4 \times 10^4$ times the brain's, and per device it produces 36 times as much entropy. Steps 2–4 of §4 therefore rank it far above the brain, as anticipated there. Per elementary event, however, the two are within about an order of magnitude of each other, at some $10^8$ times the Landauer bound. Neither comes near the bound, so the Landauer floor plays no part in the energetics of either.

In use, a GPU serving a 70-billion-parameter model produces about 2,700 tokens per second [@mlcommons2024]. At its rated power that is about 0.26 J per token for the GPU alone. Measurements under other conditions are higher: 3–4 J of GPU energy per output token for LLaMA 65B on older V100 GPUs, extrapolated from one node [@samsi2023], and 0.24 Wh, or 864 J, for a median Gemini text prompt including host machines and data-centre overhead [@elsworth2025].

**Records.**

| Record | Information | Formation rate (bit s$^{-1}$) | Lifetime $\tau_r$ | $1-p_r$ |
|---|---|---|---|---|
| Brain: long-term memory (behavioural) | $1.0\times10^{9}$ bit over a lifetime | 1.2–2.3 | ~32 years | $1.2\times10^{-11}$ |
| Brain: synaptic weights (capacity) | $7.7\times10^{14}$ bit | $6.4\times10^{8}$–$1.3\times10^{9}$ (turnover-based) | 1–2 weeks (spines) | $1.0\times10^{-8}$–$2.1\times10^{-8}$ |
| Model at inference: key–value cache, per GPU | ≤ 17 bit per token ($2.6\times10^{6}$ physical) | $4.6\times10^{4}$ ($7.1\times10^{9}$ physical), output tokens only | ~45 s (one request) | $3.4\times10^{-3}$–$6.9\times10^{-3}$ |
| Model at inference: weights | none new | 0 (frozen) | — | — |
| Model in training (Llama 3.1 405B): weights | ≤ $8.1\times10^{11}$ bit of knowledge ($6.5\times10^{12}$ raw) | ≤ $1.2\times10^{5}$ for the cluster; ≤ 7.3 per GPU | months or more | ≈ 0 |

: **Table 3.** Records formed. Long-term memory figures are Landauer's estimates of the functional information adults retain, from reading and picture-recognition experiments; his central loss rate sets the lifetime [@landauer1986]. Synaptic capacity is neocortical synapses times 4.7 bits per synapse, a figure measured in rat hippocampus [@tang2001; @bartol2015]. The synaptic rewrite rate is an estimate based on turnover, not a bound. It applies the 1–2 week mean spine lifetime of mouse hippocampus [@attardo2015] to every neocortical synapse. That overstates turnover, because many neocortical spines persist for months [@holtmaat2005], and it understates rewriting, because plasticity also changes the strength of spines that persist. The neural dynamical time is a membrane time constant of 12.4 ms, measured in control conditions [@stuart1998]. The key–value-cache row uses the Llama 3 70B architecture (80 layers, 8 key–value heads of dimension 128, a 128,000-token vocabulary) [@grattafiori2024] and a 16-bit cache; NVIDIA's benchmark configuration suggests 8-bit numbers, which would halve the physical figures. It takes throughput and per-token latency (155 ms per token per request, which also serves as the model's dynamical time $\tau_\text{dyn}$) from a Llama 2 70B benchmark on eight H100s [@mlcommons2024]. Information per token is bounded by $\log_2$ of the vocabulary. The formation rate counts output tokens only; the prompt's tokens also write cache entries. $1-p_r$ is given for an entry written at the start of a request and for one written halfway through, the average. The training row uses Meta's 30.8 million H100 hours for Llama 3.1 405B [@meta2024], run on up to 16,384 GPUs [@grattafiori2024], and a capacity of at most 2 bits of extractable knowledge per parameter [@allenzhu2024].

| System | Retained information (bit) | Energy (J) | Bits per J | Fraction of the Landauer limit |
|---|---|---|---|---|
| Human: whole brain budget over 70 years | $1.0\times10^{9}$ | $4.4\times10^{10}$ | 0.023 | $6.7\times10^{-23}$ |
| Human: plasticity share only | $1.0\times10^{9}$ | $4.9\times10^{8}$–$1.4\times10^{9}$ | 0.73–2.1 | $2.2\times10^{-21}$–$6.1\times10^{-21}$ |
| Fruit fly: marginal cost of long-term memory | — | — | 100 | $2.9\times10^{-19}$ |
| Llama 3.1 405B training | ≤ $8.1\times10^{11}$ | $7.8\times10^{13}$ | ≤ 0.010 | ≤ $3.0\times10^{-23}$ |
| GPT-3 training | ≤ $3.5\times10^{11}$ | $4.6\times10^{12}$ | ≤ 0.076 | ≤ $2.2\times10^{-22}$ |

: **Table 4.** Retained information per joule; higher is better. The plasticity share, 1–3% of brain energy, chains three rodent-based estimates: plasticity costs 4–11% of the energy of fast excitatory transmission [@karbowski2019], postsynaptic glutamate receptors take half of signalling energy [@howarth2012], and signalling takes at least 55% of the total [@engl2015]. Protein synthesis alone is put at no more than 1.3% [@engl2015]. The fly figure is a preprint estimate from behavioural data [@girard2023]. Training energies are Meta's GPU-hours at rated power [@meta2024] and Patterson and colleagues' estimate of 1,287 MWh for GPT-3 [@patterson2021]. The rows draw their energy boundaries differently: the whole brain or its plasticity alone for humans, rated GPU power for Llama, and for GPT-3 the authors' estimate for the training run, which includes host power and a data-centre PUE of 1.10. The model figures are upper bounds, because 2 bits per parameter is a saturation capacity.

| System and boundary | $\dot\Sigma$ ($k_B$ s$^{-1}$) | $M$ (g) | $\dot\Sigma/M$ ($k_B$ s$^{-1}$ g$^{-1}$) | $I$, functional (bit) | $I$, capacity (bit) | $R$, functional | $R$, capacity |
|---|---|---|---|---|---|---|---|
| Human brain | $4.7\times10^{21}$ | 1,500 | $3.1\times10^{18}$ | $1.0\times10^{9}$ | $7.7\times10^{14}$ | $3.1\times10^{27}$ | $2.4\times10^{33}$ |
| Llama 3 70B inference: GPU dies only | $1.4\times10^{24}$ | ≤ 12 | ≥ $1.2\times10^{23}$ | ≤ $1.4\times10^{11}$ | $1.1\times10^{12}$ | ~ $1.6\times10^{34}$ | ≥ $1.3\times10^{35}$ |
| Llama 3 70B inference: HGX baseboard | $1.4\times10^{24}$ | $2.4\times10^{4}$ | $5.6\times10^{19}$ | ≤ $1.4\times10^{11}$ | $1.1\times10^{12}$ | ≤ $7.9\times10^{30}$ | $6.3\times10^{31}$ |
| Llama 3 70B inference: DGX server | $2.5\times10^{24}$ | $1.3\times10^{5}$ | $1.9\times10^{19}$ | ≤ $1.4\times10^{11}$ | $1.1\times10^{12}$ | ≤ $2.6\times10^{30}$ | $2.1\times10^{31}$ |
| Llama 3.1 405B training, per 8 H100: GPU dies only | $1.4\times10^{24}$ | ≤ 12 | ≥ $1.2\times10^{23}$ | ≤ $8.1\times10^{11}$ | $6.5\times10^{12}$ | ~ $9.3\times10^{34}$ | ≥ $7.5\times10^{35}$ |
| Llama 3.1 405B training, per 8 H100: HGX baseboard | $1.4\times10^{24}$ | $2.4\times10^{4}$ | $5.6\times10^{19}$ | ≤ $8.1\times10^{11}$ | $6.5\times10^{12}$ | ≤ $4.6\times10^{31}$ | $3.7\times10^{32}$ |
| Llama 3.1 405B training, per 8 H100: DGX server | $2.5\times10^{24}$ | $1.3\times10^{5}$ | $1.9\times10^{19}$ | ≤ $8.1\times10^{11}$ | $6.5\times10^{12}$ | ≤ $1.5\times10^{31}$ | $1.2\times10^{32}$ |

: **Table 5.** The measure of §4, $R = \dot\Sigma\, I / M$, in units of $k_B$ bit s$^{-1}$ g$^{-1}$. Functional bits are, for the brain, Landauer's estimate of retained long-term memory, a low estimate of what its dynamics draw on, and for the models at most 2 bits of extractable knowledge per parameter, an upper bound. Capacity bits are 4.7 bits per neocortical synapse and 16 bits per parameter; an 8-bit deployment would halve the models' capacity bits. The boundary rule of §4 puts the system at the eight GPU packages, the dies with the HBM memory that holds the weights, and the switches that join them. No source consulted gives their mass. The die-only rows bound it from one side: they divide the modules' rated power by die silicon alone, and that mass is itself an upper bound, so their $R$ can be higher still. The HGX baseboard is the smallest sourced mass that holds the weights. It carries the GPUs, their memory and the switches, weighs 24 kg and typically draws 5.6 kW [@nvidiahgxpcf]. The DGX server adds host processors, power supplies and chassis, and is rated at 10.2 kW and 130.45 kg [@nvidiadgxh100]. One copy of Llama 3.1 405B spans many nodes [@grattafiori2024], but $\dot\Sigma/M$ is the same per node, so $R$ for the whole copy equals the value shown. Meta trained it on its own servers, so the training rows assume the same mass per GPU. The bound on $I$ from the trajectory (§4) is assumed not to bind for either system in its working state. In the die rows, "≥" and "~" follow from the die mass being an upper bound; "~" marks a value bounded in opposite directions by $M$ and by $I$.

**What the numbers show.** Five points, from the most robust to the least.

1. *Neither dissipation nor storage alone scores.* Stars, jet engines and storage devices score zero on $R$, and a logic-gate grid near zero (§5.2). A brain and a GPU system running a large language model both score far above them. Chips in general need not be far below, because at die scale the entropy factor dominates. At a GPU die's power density, some $3 \times 10^4$ bits of operative information match the brain's functional $R$, and some $2 \times 10^{10}$ bits its capacity.

2. *Counted as storage capacity, brain and model come within a factor of about 300, and the unsourced mass of the GPU packages decides which leads.* The brain leads the HGX baseboard, the smallest sourced mass that holds the weights, by a factor of about 40 at inference and about 7 in training, and the whole server by about 20–110. Counting only the GPU dies, which leave out the memory that holds the weights, the model leads by at least about 50–300. The system that the boundary rule picks lies between these. The two factors pull in opposite directions. Per gram, the baseboard produces about 18 times the brain's entropy, the server about 6 times and a die about $4 \times 10^4$ times. But the brain's synapses hold about 120–690 times the raw capacity of the models' weights.

3. *Counted as functional information, the model leads at every boundary,* by a factor of about 850 to $3 \times 10^7$. That comparison is lopsided. The brain's $10^9$ bits are what recall experiments measure, a low estimate of what its dynamics draw on. The models' figures are upper bounds on extractable knowledge. Neither way of counting is well constrained.

4. *Inference and training score alike, and the cache does not matter.* $R$ rewards running on records, not forming them. A GPU scores the same whether it reads its weights or rewrites them, and training scores higher here only because Llama 3.1 405B is larger than the 70B model. The key–value cache's entries for output tokens hold about $10^7$ bits across all the requests in flight on eight GPUs, about $6 \times 10^{-5}$ of the weights' knowledge bound. Entries for prompt tokens, not counted, add more; even ten times more would leave the cache below $10^{-3}$ of that bound. Its physical size is far larger, at least about $10^{12}$ bits, but given the weights it is a deterministic function of the tokens, so only its information can count (§4). Whether a record that lasts one request is lasting enough therefore makes no difference to the numbers.

5. *Training forms lasting records at a cost per retained bit not clearly below a brain's.* A human retains about $10^9$ bits of functional long-term memory on a lifetime budget of about $4 \times 10^{10}$ J, or about 0.02 bits per joule. Training Llama 3.1 405B retained at most about 0.01 bits of extractable knowledge per joule, and GPT-3 at most about 0.08. Charged only for plasticity, the brain retains 0.7–2 bits per joule. Against the human brain, a model in training thus retains at most about 3 times as many bits per joule, and possibly 200 times fewer, depending on the model and on how the brain is charged. The fly estimate, 100 bits per joule, is far above both. Per device, an H100 in Llama training retains at most about 7 bits of knowledge per second. Landauer estimated 1.2–2.3 bits per second for attentive humans, and the lifetime average is about 0.45. None of this enters $R$, which does not count formation. It shows only that the machine's records are neither unusually cheap nor unusually costly.

**What follows.** On $R$, the ranking of brains above language models is not robust. It turns on two things the measure does not yet settle: the mass of the system its boundary rule picks, which for a GPU depends on packages whose mass was not found, and whether a bit counts as storage capacity or as information the dynamics actually carry. The stricter, semantic variant of $I$ (§4) would restore the ranking, if the organism rather than the brain is taken as the system whose existence the records serve. A brain's records feed a model that the organism uses to keep itself alive, whereas a language model is kept in existence by its operators, so its weights carry little semantic information *for the model* [@kolchinsky2018]. But the ranking would then rest on the least formalised part of the measure. All comparisons of $R$ here are per second and per gram, as it requires; Table 4 and point 5 are per joule or per device and do not enter $R$.

# 6. Cosmological context

## 6.1 The low-entropy past

Everything the record view relies on runs on the universe's low-entropy past. That includes the formation of traces, the costs of memory and agency, and the entropy production of the waking brain. Rovelli's analysis of traces makes the dependence explicit. Trace formation "transforms initial low entropy (free energy) into available information" [@rovelli2022]. Wolpert and Kipper show that the kind of memory that informs only about the past is the kind that exploits the second law. They also identify a formal difficulty in deriving that law from the Past Hypothesis [@wolpert2024; @albert2000].

On the record view, then, **the capacity for experience is fuelled by the initial condition of the universe**. That is a consequence of the view, not an argument for it. It is stated here because it organises the related questions.

Three such questions deserve brief mention.

**Boltzmann brains.** These are observers produced by rare fluctuations rather than by cosmological history. They threaten the cognitive stability of some cosmologies [@dyson2002; @albrecht2004; @carroll2017]. The record view ties experience to dissipative dynamics running on records along a thermodynamic gradient, so it inherits this problem but does not add to it.

**Goff's teleological reading.** Goff's recent proposal reads the same facts as evidence of cosmic purpose [@goff2023].

**England's dissipative adaptation.** England's work offers a non-teleological alternative. Matter driven by an external energy source tends to organise into structures that absorb and dissipate work efficiently, and some of those structures keep records [@england2015; @perunov2016]. This paper prefers the non-teleological reading. It treats teleology as a minority option that the record view neither needs nor excludes.

**Gołosz's objection.** Gołosz argues that the arrows of traces and of thermodynamics are themselves "only arrows in time" [@golosz2025]. If he is right, the record view's dependence on the thermodynamic arrow is a dependence on something still awaiting a deeper explanation.

## 6.2 Related speculations (not part of the argument)

Several results suggest closer links between time, thermodynamics and observers. None of them is used in the argument above.

- **Thermal time.** On the thermal time hypothesis, the flow of time in a generally covariant theory is fixed by the thermodynamic state [@connes1994].
- **Gravity as thermodynamics.** Jacobson derived the Einstein equation as an equation of state [@jacobson1995].
- **Time from correlations.** On the Page–Wootters mechanism, time emerges from correlations between a system and a clock subsystem in a globally static state [@page1983]. The mechanism has been illustrated experimentally with photons [@moreva2014]. The Page–Wootters clock is close kin to the clock-observer of §2.5 [@devuyst2025].
- **Opposite arrows.** Schulman analysed systems whose thermodynamic arrows of time point in opposite directions [@schulman1999]. On the record view, such systems would run on records ordered in opposite temporal directions, and so host proto-experience ordered both ways.

These are mentioned as directions, not as support.

# 7. Objections and replies

**Objection 1: illusionism.** Illusionists hold that there is no phenomenal "glow" to locate. There are only representations that misrepresent the brain's states as having phenomenal properties [@frankish2016; @dennett2016]. If they are right, the question of where proto-experience sits has a false presupposition.

*Reply.* The paper is explicitly conditional on the falsity of illusionism. The comparative argument of §3.3 concerns where experience would be *if* the panpsychist or Russellian picture held. Even so, the illusionist can accept much of the paper. The ladder of observerhood, the thermodynamics of records and the empirical test in §8 are neutral between realism and illusionism about phenomenal properties. They would then describe the physical basis of the representations that the illusionist thinks generate the illusion.

**Objection 2: the metabolic confound.** Perhaps the irreversibility of brain dynamics tracks nothing but activity or metabolism. Both fall in sleep and anaesthesia [@alkire1995; @shulman2009]. Irreversibility rises with physical and cognitive effort [@lynn2021]. And awareness has a metabolic threshold [@stender2016]. The brain evidence of §2.8 would then show only that conscious brains are busy brains.

*Reply.* This is the most important empirical objection, and it is not answered here. It is turned into a test (§8). On the measure of §4, metabolism is one factor of $R$, so a fall in metabolism when consciousness is lost is expected rather than embarrassing. The objection bites on the other factor. The record view predicts that the relation between irreversibility and consciousness *survives* controls for signal power, variance and metabolic proxies. That prediction rests on an assumption, stated in §8: that large-scale irreversibility, net of power and metabolism, indexes how much information about its stored records the brain's trajectory carries. The view also predicts that the relation holds in cases where activity and consciousness come apart. If the relation is fully explained by activity or metabolism, then within brains $R$ reduces to energy rate density, and its information factor has no empirical support. The conditional philosophical argument of §3 would survive, but it would have lost most of its contact with evidence. Claim 7's open question would be settled against the view, and the within-brain predictions of claim 8 would have failed.

**Objection 3: unfalsifiability.** The view's verdicts on cells, chips and language models cannot be checked, since such systems cannot report.

*Reply.* This is conceded for systems that cannot report, and every panpsychist view shares the cost. Two things mitigate it. First, the view's verdicts are *determinate* once its open choices are fixed: given the physics, a system boundary and a way of counting bits, the measure in §4 assigns values, even where no report can confirm them. §5.6 shows how much those choices still move. Second, the view makes *comparative* predictions inside brains, where reports exist, and those can fail (§8). A theory that can be refuted where it can be tested earns some credit for its extrapolations, though not much.

**Objection 4: erasure and waste.** Erasure is irreversible and costs entropy, so a record view seems committed to treating erasure as experience-producing. Worse, a measure built on entropy production seems to reward waste.

*Reply.* On erasure, the measure of §4 counts dissipation only in proportion to the operative records it runs over. A pure eraser has $I = 0$ and scores zero, however much heat it produces. The heat of erasure does count within a system that also runs on lasting records, as a brain or a GPU does; there it is part of the price of the dynamics. Sagawa and Ueda's result, that dissipation can be moved between measurement and erasure, is why $R$ takes the system's whole entropy production rather than attributing it to particular records [@sagawa2009].

On waste, the objection stands. Of two systems that run on the same records, $R$ ranks higher the one that dissipates more. The only repair in sight replaces $\dot\Sigma$ with the Landauer price of the bits written, which brings back the attribution problem and loses the tie to metabolism. The reply also depends on non-circular definitions of "operative" and "drawn on". **This objection is marked open.**

**Objection 5: the combination problem.** However records are integrated, why should many micro-experiences add up to one subject [@james1890; @chalmers2016; @coleman2014]?

*Reply.* The record view does not solve the combination problem. It eases it in two ways. The micro-level bearers on the record view are not fixed, identical particles. They are events that already have physical relations: a self-model is a structure of records about records. And on the measure of §4, what counts as one system is fixed by which records its dynamics draw on, which can be studied, so the question of how much combination has occurred becomes partly empirical. $R$ itself does not grade integration. What is not explained is why integrated records should yield a single *subject*. The question is left where Chalmers's survey leaves it [@chalmers2016]. A record view also faces the cosmopsychist's mirror-image problem of decombination [@miller2018], and has nothing new to say about it beyond §5.5.

**Objection 6: clock-observers suffice.** Physics has needed only clock-observers to define states and entropies (§2.5). So the "observer" of physics lends no support to a recording observer, let alone to an experiencing one.

*Reply.* This is correct, and it is why §3.1 names the bridge theorem as missing. The record view does not depend on it. Its support comes from the separate claim, grounded in quantum foundations and the thermodynamics of information, that *facts* need records [@zurek2018; @dibiagio2021; @rovelli2022]. If the bridge theorem were proved, the record view would gain a link to fundamental physics. If it were refuted, the view would lose only the suggestion that quantum gravity points toward it.

**Objection 7: the non-emergence argument and the vitalism analogy.** Strawson's argument that experience cannot emerge from the wholly non-experiential motivates panpsychism [@strawson2006]. But a structurally similar argument was once made for life, and vitalism was wrong. Perhaps experience will emerge from structure just as life did.

*Reply.* The paper uses Strawson's argument only as *motivation* for its conditional. It does not need the argument to be sound. On the analogy, two points.

First, the usual disanalogy holds. Life was always characterised by functions, such as metabolism, reproduction and self-maintenance, that physics could in principle realise. Experience is not obviously characterised that way.

Second, and more interestingly, the record view is *compatible* with the vitalism analogy. The physics that dissolved vitalism was thermodynamics: the theory of open, dissipative systems that maintain themselves away from equilibrium [@schrodinger1944; @prigogine1978]. The record view locates experience in exactly that physics. If the analogy wins and experience turns out to be strongly emergent or functional, the measure in §4 would survive as a measure of the physical *correlate* of experience rather than of its bearer. The comparative argument is useful whichever way the dispute between emergence and panpsychism comes out.

# 8. Proposed empirical test

The following study is described, not executed. A fuller plan, with candidate analyses, is in the repository's `future-work/empirical-plan.md`.

**Question.** Does the entropy production, or time-irreversibility, of large-scale brain dynamics track the level of consciousness *after* controlling for signal power, signal variance and metabolic or activity proxies?

**Assumption.** On the measure of §4, metabolism is one factor of $R$. The test therefore bears on the other factor, $I$, only if large-scale irreversibility, net of power and metabolism, indexes how much information about its stored records the brain's trajectory carries. That is assumed here, not shown. If it is false, the test bears on $\dot\Sigma$ alone.

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

- *Record view supported.* The partial effect of consciousness level on irreversibility survives the covariates and surrogates, with the same sign as in the uncontrolled analyses.
- *No within-brain support for the information factor.* The effect is fully explained by power, variance or activity, so that the partial effect is null with adequate power. Within brains, $R$ would then add nothing to energy rate density, and the record view's empirical claim would fail.
- *Refuted in seizures.* Whole-brain irreversibility, net of covariates, is *high* during seizures in which awareness is impaired. Then the view's escape (§5.3) would need an independent measure of how much stored information the dynamics carry. Without one, the claim that irreversibility marks consciousness fails.

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

If experience has a physical locus of the kind panpsychists and Russellian monists want, then particles are the wrong place to look. They keep no records and do nothing to distinguish one from another. Collapse events require physics that experiment is pressing hard. Integrated structure without persistent, used records assigns rich experience to an inactive grid of logic gates.

The irreversible recording event is a better candidate. It needs only decoherence and thermodynamics. It is graded by how hard a system is driven, per gram, while its dynamics run over what it remembers. And it ties proto-experience to the same low-entropy past that makes memory, agency and the arrow of time possible.

The view inherits two hard problems, combination and, in its measure, waste. It does not pretend to solve them. Its measure also puts large language models within reach of brains, or above them, and the two things that decide their order, the mass of the system its boundary picks and how bits are counted, are not yet settled (§5.6). It also inherits an empirical liability: the brain evidence that most supports it is confounded by metabolism and threatened by seizures. That liability is also its advantage over its rivals, because it can be tested, and §8 says how.

# AI assistance disclosure

The ideas in this paper were developed in dialogue with Claude (Anthropic). The manuscript, literature review and bibliography were drafted with the assistance of Claude Code. Every reference was checked against a primary record (arXiv, DOI or publisher record, PubMed or Europe PMC, the dataset's landing page, or a catalogue or scan for older books). Where the text of a source could not be read, the paper relies only on what its abstract or a verified secondary source states. `notes/literature-review.md` records the level of verification for each entry. The author takes full responsibility for the content.

# References {.unnumbered}

::: {#refs}
:::
