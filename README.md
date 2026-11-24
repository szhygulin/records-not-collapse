# Records, Not Collapse: Irreversible Recording as the Physical Locus of Proto-Experience

**Viacheslav Zhygulin** (<s.zhygulin@gmail.com>). Draft of November 2026.

> **Status:** a speculative position paper in philosophy of mind and philosophy of physics. It has **not been peer-reviewed**. It argues for a conditional thesis and states the author's credences and what would falsify the thesis.

## Abstract

Panpsychist and Russellian-monist views hold that experience, or proto-experience, belongs to the basic physical world, but they have no agreed answer to *where* in physics it sits. The usual candidates are particles, wavefunction collapse (Orch-OR) and integrated information (IIT).

This paper argues, conditionally, that if any such view is true, the natural physical bearer of graded proto-experience is the *irreversible recording event*: the formation of a persistent, decohered record, which produces entropy. On this view a system's degree of experience tracks the entropy it spends, per gram, on forming persistent records that are integrated into its model of itself.

The paper:

- surveys the relevant work in quantum gravity, quantum foundations, the thermodynamics of information, theories of consciousness and nonequilibrium neuroscience, and finds the thesis partially anticipated but not stated as a whole;
- separates the clock-observers that recent quantum-gravity work needs from the recorder-observers that facts need, and names the missing theorem that would join them;
- builds the measure in steps. Weighting information by dissipation per gram ($E\,I/M$, the author's suggestion) serves as a check on information-only measures: it removes IIT's verdict that an inactive grid of logic gates is highly conscious, but it favours computers over brains;
- applies the measure to hot molecules, logic-gate grids, storage devices, stars, sleep, seizures and language models. A language model at inference forms no lasting internal records and scores near zero, whatever its hardware;
- answers seven objections;
- ends with a test that can be pre-registered: does the time-irreversibility of brain dynamics still track consciousness once metabolism and signal power are controlled for?

## Contents

| Path | What it is |
|---|---|
| [`paper/paper.md`](paper/paper.md) | Main text (Pandoc Markdown, about 13,000 words) |
| [`paper/paper.pdf`](paper/paper.pdf) | Built PDF |
| [`paper/references.bib`](paper/references.bib) | Bibliography; every entry verified against a primary record |
| [`paper/figures/ladder.svg`](paper/figures/ladder.svg) | Figure 1, the ladder of observerhood (PNG alongside) |
| [`notes/literature-review.md`](notes/literature-review.md) | Novelty verdict, search method, null results, and the verification status of every reference |
| [`notes/corrections.md`](notes/corrections.md) | Every point where the original brief was corrected or dropped against the sources |
| [`future-work/empirical-plan.md`](future-work/empirical-plan.md) | Proposed confound-controlled test on named open datasets |
| [`future-work/model-attribution-study.md`](future-work/model-attribution-study.md) | Proposed study: do the paper's metrics track graded human judgements of how conscious past AI models are? |
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
