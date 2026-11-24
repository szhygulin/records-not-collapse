# Future work: do the metrics track how conscious people judge past AI models to be?

This plan describes a study; it does not report one. It was proposed by the author on 24 November 2026. Sources were checked on that date; re-check them before use.

## 1. Question

Across a series of past AI models, which candidate metric best tracks how conscious people judge each model to be, rated on a graded scale rather than yes or no?

The candidates are the paper's own:

- the record measure $R$, the least entropy a system must spend, per gram, on forming persistent records integrated into a self-model (paper §4);
- the check of §4 step 4: information weighted by entropy production per gram ($E\,I/M$);
- energy rate density (§4 step 3);
- an information-only stand-in. No tractable $\Phi$ exists for models of this size, so parameter count and training compute are used instead, and labelled as stand-ins.

People's ratings are not ground truth about consciousness. The study asks which metric matches folk attribution, and where the record view departs from it.

## 2. Why it is feasible

- **Model data are public.** Epoch AI's dataset "Data on AI models" covers over 3,700 models, with a "Notable AI models" subset, under CC BY 4.0 ([epoch.ai/data/ai-models](https://epoch.ai/data/ai-models)). It records parameters, training compute, publication date, training hardware and its quantity, hardware utilisation, training time, and an estimated training power draw. It has no energy field, so energy must be derived. Nor does it give hardware mass. Model cards and papers add architecture, context length and memory features.
- **Graded attribution can be measured.** Colombatto and Fleming asked 300 US residents to "rate the extent to which ChatGPT is capable of having conscious experience on a scale from 1 to 100". Two thirds (67%) gave it some possibility, that is, a rating above 1, and ratings rose with how often people used it ([doi:10.1093/nc/niae013](https://doi.org/10.1093/nc/niae013)).

## 3. Design

1. **Model panel.** About 15–30 models from several generations that can still be run, so that every model answers the same prompts.
2. **Metrics per model,** at napkin precision.
   - Energy rate density and $E\,I/M$ use Epoch's training power draw over the die-mass bound of paper §5.6 (vendor die area × wafer thickness × silicon density) times hardware quantity. Neither choice changes $R$. $I$ is counted as retained bits, at most 2 bits per parameter as in paper §5.6; training compute, in FLOP, is reported separately as an information-only stand-in.
   - $R$ needs each model's memory features to be coded: none; memory within a session; persistent memory across sessions; continual learning or test-time training. A frozen model integrates none of its records into a self-model, so its $R$ is near zero. These memory features raise only its record-forming part; $R$ stays near zero unless the records are integrated into a self-model the system uses to keep itself in existence (paper §5.4).
3. **Ratings.** Participants rate each model on the same 1–100 scale, after reading transcripts on matched prompts.
   - In one condition the model's name is hidden, so that ratings track behaviour rather than brand. In the other it is shown.
   - The study also records how often each participant uses AI systems, which Colombatto and Fleming found to matter.
   - Memory is invisible in a single-prompt transcript. Each model with memory is therefore also shown in a multi-session transcript in which it recalls an earlier session, paired with the same model with memory switched off; in the name-hidden condition this pair is the memory contrast.
4. **Analysis.**
   - Rank correlations between each metric and the mean rating across models.
   - Mixed-effects models with participants and prompts as random effects.
   - Covariates for capability and fluency, such as benchmark scores and first-person or emotional language. Colombatto and Fleming found that ratings tracked attributions of experience, such as feelings, and not of intelligence, so emotional and first-person language may matter more than capability.
5. **Pre-registration and ethics.** Pre-register the panel, prompts, metrics and decision rule. Obtain ethics approval and informed consent for the survey.

## 4. Predictions

- **Ratings follow cues of experience.** Folk ratings will most likely track fluency and first-person and emotional language, and perhaps capability. Metrics that scale with compute, including $E\,I/M$ and the information-only stand-ins, will correlate with them only in so far as those cues grow with model scale.
- **The record view expects a divergence.** It gives every frozen model an $R$ near zero, so it predicts that $R$ will not track the ratings across frozen models. That divergence bears on how people attribute consciousness, not on whether the record view is right.
- **The informative case is memory.** Persistent memory or continual learning is the one feature without which $R$ cannot rise, though on the paper's account it is not enough (paper §5.4). Do ratings rise for models with such memory, beyond what capability and fluency predict? A rise would show that folk attribution responds to a precondition the record view grades; no rise, that it ignores it. Neither result bears on whether the record view is right.
