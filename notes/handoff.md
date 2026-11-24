# Handoff: work paused on 24 November 2026

The draft is complete through §5.6, "Rough numbers: a human brain and a language model", which was added on 24 November. The repository is **private**. The author's go to publish was given for when the work is done ("okay, when done - push paper to github, along with calculation scripts, and sources of data, but don't push data"). The author then paused the work ("let pause the work, commit and push current handout to github, I'll resume later with fresh session").

## 1. Decision the author owes: how the measure should count

This decision blocks the edits in §4 (the definition of $R$, $p_r$ and $u_r$), in §5.4 (the sentence "rests on the use factor $u_r$ alone"), and in §5.6 (Table 5 and findings 1, 4 and 5). It also blocks summary claim 9 and the README bullet on the brain-versus-model numbers.

**Already agreed with the author:**

- $\Delta S_r$ should be the Landauer price, $k\ln 2$ per bit, and not the dissipation actually spent. Otherwise inefficiency raises $R$: a jet engine fitted with a data logger, or a wasteful memory, would score high.
- Table 4 should switch from J per bit to bits per J, which reads more naturally because higher is better.

**Open: what counts.**

1. *Formation only.* $R$ counts lasting, used bits at the Landauer price.
2. *Formation plus use* (recommended). $R$ also counts the bits of the system's own persistent records that its processing reads. Under this option a USB stick scores near 0, because it stores records but never processes them. A bitcoin miner or an XOR grid also scores near 0, because it processes but keeps no records. A language model scores well above both, and a brain scores highest only through forming new lasting records and through self-maintenance.
   - Rough figures, not yet checked against sources: a brain uses $1$–$7\times10^{14}$ record bits per second ($6\times10^{12}$–$4\times10^{13}$ per J). An H100 at inference uses about $8\times10^{15}$ per second (about $10^{13}$ per J), counting one 16-bit weight per multiply-add at peak.
3. *Bits processed per joule* (the author's suggestion). This is advised against, for two reasons. A reversible computer would score infinitely high while forming no records, which inverts the thesis. And a bitcoin miner would outrank both brains and language models.

The author's stated intuition, 24 November 2026: an LLM is more conscious than a USB stick, so the measure should count bits processed, not bits stored.

**Open: what "lasting" means.** $p_r = \tau_r/(\tau_r+\tau_\text{dyn})$ compares a record's lifetime with one dynamical step. On that definition the key–value cache of a model at inference has $p_r \approx 0.993$–$0.997$. At the Landauer floor, model inference then scores about $3\times10^4$ $k_B$ s$^{-1}$ per GPU, against about 1–2 for human behavioural memory and at most 5 for a GPU in training. So the model at inference outranks the brain.

If $\tau_r$ is measured against the system's own lifetime or self-maintenance cycle instead, the cache barely counts. The draft currently notes this repair but does not adopt it.

## 2. Review findings on §5.6 still to fix

An independent review of the §5.6 change was made on 24 November. The arithmetic and the transcription are clean. Every finding below is open. Items marked *(decision)* wait on §1.

**HIGH**

- *(decision)* Table 5 and finding 1 score inference as "0 lasting". That test is not in §4's formula, which gives inference about $3.2\times10^4$ $k_B$ s$^{-1}$ (see §1 above). Finding 1 is therefore circular, and §5.4's "for training … $u_r$ alone" is wrong by implication.
- *(decision)* Finding 4's "at least as high as a brain" and "therefore neither $\Delta S_r$ nor $p_r$" go beyond the data.
  - The direct-cost attribution, which is the one closest to §4's $\Delta S_r$, is not estimated for the GPU.
  - Whole-budget attribution is the raw-dissipation count that §4 step 6 rejects.
  - Fix: write the training floor as "≤ 5.1", change the finding to "is not clearly below", and say the verdict rests on $u_r$ "unless the direct write cost separates them".
- §5.6 says Samsi et al.'s 3–4 J/token is a "whole-system measurement". It is GPU energy only, extrapolated from one node.
- Finding 3 says a training run pays "between about a third … and $10^4$ times" the brain's cost. The $10^4$ end compares Llama's 96 J with the fruit fly's 0.01 J. Against the human brain alone the range is about 0.3–200×.

**MEDIUM**

- The key–value cache formation rate counts output tokens only. Prefill also writes cache entries for prompt tokens, so the rate is not an upper bound. Drop the "≤".
- Table 5's Landauer row mixes capacity bits (brain synapses) with knowledge bits (GPU). Drop the synaptic entry, or add the GPU's raw weight bits rewritten per optimiser step.
- The synaptic rewrite rate, based on spine turnover, is not an upper bound, because LTP and LTD rewrite spines that persist. Call it a turnover-based estimate.
- The training J/bit figures are floors, because 2 bits per parameter is a saturation capacity. Write "≥ 96" and "≥ 13", and say "at least comparable".
- $u_r$ is defined two ways in §4: "semantic *or* predictive and enters the self-model" (Step 6, list of terms) against "predictive and semantic" (Step 6, first bullet). Finding 5 silently uses one reading. Align the two definitions *(decision)*.
- Finding 4 compares the systems per device per second, while §5.2 compares them per joule. Under the Landauer floor, per joule, the brain leads by 6–11×. State the normalisation used.
- §4 step 5 says a brain spends "a large share of its budget forming … traces", but §5.6 puts plasticity at 1–3% and protein synthesis at no more than 1.3%. Qualify step 5.

**LOW / NIT**

- The 1−$p_r$ value for the key–value cache should be given as about $3.4$–$6.8\times10^{-3}$, because entries live about half the request on average.
- "≥ $4.8\times10^9$" erg s$^{-1}$ g$^{-1}$ should read "≈ $5\times10^9$ (module power over die mass)".
- $\tau_\text{dyn}$ = 20.9 ms is the CsCl value, not the control value. Use 12.4 ms, or label the 20.9 ms value.
- The fly row should use 300 K, not 310 K.
- `sci()` in `napkin.py` misformats values in [99.5, 100) and from 100 to 9,999. No current input hits this.
- "Every input comes from a cited source" should name the assumed inputs. The Table 3 caption needs the FP8 caveat.
- Table 4 mixes energy boundaries. Say so in its caption.
- "Retains about 7 bits/s" should be "at most about 7". Compare it with the human lifetime average of about 0.45 bit/s, as well as with Landauer's rate while attending.
- Drop the sensory-versus-behaviour "similar gap" sentence in finding 2. It compares input with throughput, not the redundancy within one record.
- §5.4 says context is "discarded at the end of a session", while §5.6 uses one request as the lifetime. Pick one, and mention that the cache can be kept across the turns of a conversation.
- After the inserted sentence in §5.4, "That verdict" is ambiguous.
- `notes/corrections.md` row 36 should cite svmisv029 and say "GPU", not "CPUs".
- Tiers in `notes/literature-review.md`:
  - girard2023 is tier P, which says only the abstract was read, but its full text was read.
  - elsworth2025 is an unreviewed technical report but is tier A.
  - tang2001 and holtmaat2005 were checked against the abstract, which meets the definition of tier A.
- §4 step 3 quotes Chaisson's brain value, 1.5×10⁵, while §5.6 computes 1.3×10⁵. Note the difference.
- nvidiah100 and svmisv029 carry no publication date, so they render as "n.d.". This is correct, since neither source is dated.

## 3. Before making the repository public

- Run the publish-set audit: author PII (the author's name and email are intended), credentials, third-party content, and licensing.
- The README licenses "the text and figure" under CC BY 4.0. Decide whether `analysis/napkin.py` is covered too.
- Rebuild the PDF with `./build.sh` (the Chrome fallback) after the edits.
- The raw, verified source data behind `analysis/sources.md`, with quotes, was not pushed, as the author asked. It lived in the session scratchpad. `analysis/sources.md` holds what is needed to re-check every input.
