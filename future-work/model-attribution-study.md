# Future work: do the metrics track how conscious people judge past AI models to be?

This plan describes a study; it does not report one. It was proposed by the author on 24 November 2026. Sources were checked on that date; re-check them before use.

## 1. Question

Across a series of past AI models, which candidate metric best tracks how conscious people judge each model to be, rated on a graded scale rather than yes or no?

The candidates are the paper's own:

- the record measure $R$, entropy spent per gram on persistent records integrated into a self-model (paper §4);
- the check of §4 step 4: information weighted by entropy production per gram ($E \cdot I / M$);
- energy rate density (§4 step 3);
- an information-only stand-in. No tractable $\Phi$ exists for models of this size, so parameter count and training compute are used instead, and labelled as stand-ins.

People's ratings are not ground truth about consciousness. The study asks which metric matches folk attribution, and where the record view departs from it.

## 2. Why it is feasible

- **Model data are public.** Epoch AI's dataset "Data on AI models" covers over 3,700 models, with a "Notable AI models" subset, under CC BY 4.0 ([epoch.ai/data/ai-models](https://epoch.ai/data/ai-models)). It records parameters, training compute, publication date, training hardware and its quantity, hardware utilisation, training time, and an estimated training power draw. It has no energy field, so energy must be derived. Model cards and papers add architecture, context length and memory features.
- **Graded attribution can be measured.** Colombatto and Fleming asked 300 US residents to "rate the extent to which ChatGPT is capable of having conscious experience on a scale from 1 to 100". Two thirds (67%) gave it some possibility, that is, a rating above 1, and ratings rose with how often people used it ([doi:10.1093/nc/niae013](https://doi.org/10.1093/nc/niae013)).

## 3. Design

1. **Model panel.** About 15–30 models from several generations that can still be run, or that have public transcripts, so that every model answers the same prompts.
2. **Metrics per model,** at napkin precision, with the system boundary stated for each.
   - Energy rate density and $E \cdot I / M$ come from power draw and hardware mass. $I$ is counted both as parameters and as training compute.
   - $R$ needs each model's memory features to be coded: none; memory within a session; persistent memory across sessions; continual learning or test-time training. A frozen model forms no lasting records at inference, so its $R$ is near zero. Only these memory features can lift it.
3. **Ratings.** Participants rate each model on the same 1–100 scale, after reading transcripts on matched prompts.
   - In one condition the model's name is hidden, so that ratings track behaviour rather than brand. In the other it is shown.
   - The study also records how often each participant uses AI systems, which Colombatto and Fleming found to matter.
4. **Analysis.**
   - Rank correlations between each metric and the mean rating across models.
   - Mixed-effects models with participants and prompts as random effects.
   - Covariates for capability and fluency, such as benchmark scores and first-person or emotional language. These are the cues that most likely drive attribution.
5. **Pre-registration and ethics.** Pre-register the panel, prompts, metrics and decision rule. Obtain ethics approval and informed consent for the survey.

## 4. Predictions

- **Ratings follow capability.** Folk ratings will most likely track capability and fluency. Metrics that scale with compute, including $E \cdot I / M$ and the information-only stand-ins, should therefore correlate with them.
- **The record view expects a divergence.** It gives every frozen model an $R$ near zero, so it predicts that $R$ will not track the ratings across frozen models. That divergence bears on how people attribute consciousness, not on whether the record view is right.
- **The informative case is memory.** The record view gains or loses something only here: do ratings rise for models with persistent memory or continual learning, beyond what capability and fluency predict? A rise would show that people are sensitive to the same feature the record view grades. No rise would show that folk attribution ignores it.
