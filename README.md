# Records, Not Collapse: Irreversible Recording as the Physical Locus of Proto-Experience

**Viacheslav Zhygulin** (<s.zhygulin@gmail.com>). Draft of November 2026.

> **Status:** a speculative position paper in philosophy of mind and philosophy of physics. It has **not been peer-reviewed**. It argues for a conditional thesis and states the author's credences and what would falsify the thesis.

## Abstract

Panpsychist and Russellian-monist views hold that experience, or proto-experience, belongs to the basic physical world, but they have no agreed answer to *where* in physics it sits. The usual candidates are particles, wavefunction collapse (Orch-OR) and integrated information (IIT).

This paper argues, conditionally, that if any such view is true, the natural physical bearer of graded proto-experience is the *irreversible recording event*: the formation of a persistent, decohered record whose formation produces entropy. On this view the degree of experience tracks $R = \dot\Sigma\, I / M$: a system's entropy production rate, times the information in the persistent records that its own dynamics draw on, per unit of its mass. Recording events make the records; the measure grades how hard a system runs on them.

The paper:

- surveys the relevant work in quantum gravity, quantum foundations, the thermodynamics of information, theories of consciousness and nonequilibrium neuroscience, and finds the thesis partially anticipated but not stated as a whole;
- separates the clock-observers that recent quantum-gravity work needs from the recorder-observers that facts need, and names the missing theorem that would join them;
- applies that measure, on which neither dissipation nor storage scores alone, to stars, processors, storage devices, logic-gate grids, hot molecules, sleep, seizures and language models;
- puts order-of-magnitude numbers on a human brain and a GPU-based language model, finding them within a factor of about 300 of each other when bits are counted as storage capacity, with the lead set by the mass of the GPU packages, which no source gives, and the model ahead when bits are counted as functional knowledge;
- answers seven objections;
- ends with a test that can be pre-registered: does the time-irreversibility of brain dynamics still track consciousness once metabolism and signal power are controlled for?

## Contents

| Path | What it is |
|---|---|
| [`paper/paper.md`](paper/paper.md) | Main text (Pandoc Markdown, about 12,600 words) |
| [`paper/paper.pdf`](paper/paper.pdf) | Built PDF |
| [`paper/references.bib`](paper/references.bib) | Bibliography; every entry verified against a primary record |
| [`paper/figures/ladder.svg`](paper/figures/ladder.svg) | Figure 1, the ladder of observerhood (PNG alongside) |
| [`notes/literature-review.md`](notes/literature-review.md) | Novelty verdict, search method, null results, and the verification status of every reference |
| [`notes/corrections.md`](notes/corrections.md) | Every point where the original brief was corrected or dropped against the sources |
| [`future-work/empirical-plan.md`](future-work/empirical-plan.md) | Proposed confound-controlled test on named open datasets |
| [`analysis/napkin.py`](analysis/napkin.py) | The arithmetic behind §5.6, the brain-versus-language-model numbers (`python3 analysis/napkin.py`, standard library only) |
| [`analysis/sources.md`](analysis/sources.md) | Source, locator and verification level of every input to `napkin.py` |

## Building the PDF

```sh
./build.sh
```

The script needs [Pandoc](https://pandoc.org/) 3.x. It first tries Tectonic (LaTeX). If Tectonic cannot fetch its package bundle, the script falls back to Pandoc's HTML output, printed to PDF by headless Google Chrome. Set `CHROME` to the Chrome binary if it is not at the macOS default path. The committed PDF was built by the Chrome fallback.

## How to cite

See [`CITATION.cff`](CITATION.cff):

> Zhygulin, V. (2026). *Records, Not Collapse: Irreversible Recording as the Physical Locus of Proto-Experience.* Speculative position paper, not peer-reviewed. GitHub repository.

## AI assistance disclosure

The ideas in this paper were developed in dialogue with Claude (Anthropic), and the manuscript, literature review and bibliography were drafted with the assistance of Claude Code. Every reference was checked against a primary record. Where a source's full text could not be read, the paper relies only on what its abstract or a verified secondary source states, and `notes/literature-review.md` records the verification level of each entry. The author takes full responsibility for the content.

## License

The text and figure are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/); see [`LICENSE`](LICENSE). The scripts (`analysis/napkin.py`, `build.sh`) are licensed under the MIT License; see [`LICENSE-CODE`](LICENSE-CODE). Quotations from other works remain under their own terms.
