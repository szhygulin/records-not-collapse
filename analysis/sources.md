# Sources for `napkin.py`

Every input to `analysis/napkin.py`, which computes the numbers in paper §5.6, is listed below with where it comes from. Each value was read in the source on 24 November 2026 and checked a second time, by a separate pass that re-opened the source. Keys refer to `paper/references.bib`.

The **Read** column gives the verification level: *full text*, *abstract* or *vendor page*. Values the script marks `ASSUMED` have no source and are listed at the end.

## Human brain

| Script input | Value | Source | Where in the source | Read | Caveat |
|---|---|---|---|---|---|
| `P_BRAIN` | about 20 W (17–20 W from glucose uptake) | balasubramanian2021, [PMC8364152](https://pmc.ncbi.nlm.nih.gov/articles/PMC8364152/) | main text | full text | A commentary. The watt figure is cited from older handbooks. Herculano-Houzel (2012) gives 516 kcal/day, about 25 W. |
| `M_BRAIN` | about 1.5 kg | herculanohouzel2012, [PMC3386878](https://pmc.ncbi.nlm.nih.gov/articles/PMC3386878) | introduction | full text | A rounded background figure. |
| `N_SYN` | $1.64\times10^{14}$ neocortical synapses | tang2001, [doi:10.1002/syn.1083](https://doi.org/10.1002/syn.1083) | abstract | abstract | Stereology on five young male brains. Pakkenberg et al. (2003) give $1.5\times10^{14}$; it is the same group. |
| `RATE` | 0.16 spikes/s/neuron (best estimate); 0.94 (generous case) | lennie2003, [author PDF](https://www2.bcs.rochester.edu/sites/plennie/pdfs/Lennie03a.pdf) | "Sustainable Spike Rate" | full text | The rate the cortical energy budget can sustain, not a recorded rate. Scaled from rat. |
| `BITS_PER_SYN` | 4.7 bits per synapse (26 distinguishable strengths) | bartol2015, [doi:10.7554/eLife.10778](https://doi.org/10.7554/eLife.10778) | abstract; methods | full text | Rat hippocampus CA1. Spine volume is used as a proxy for synaptic strength. |
| `LTM_RATE` | 1.2 bit/s (reading); 2.3 bit/s (pictures) | landauer1986, [doi:10.1207/s15516709cog1004_4](https://doi.org/10.1207/s15516709cog1004_4) | pp. 480–484; Table 1 | full text | Functional information retained by attentive adults. The author puts it within a factor of five. |
| `LTM_TOTAL` | about $10^9$ bits for a mature person | landauer1986 | p. 491 | full text | An estimate from input and loss rates. |
| `LTM_LOSS` | $10^{-9}$ bit/bit/s | landauer1986 | Table 1, central values | full text | Sets the ~30-year lifetime in Table 3. |
| `SPINE_LIFE` | mean spine lifetime ~1–2 weeks | attardo2015, [PMC4648621](https://pmc.ncbi.nlm.nih.gov/articles/PMC4648621/) | abstract | full text | Mouse hippocampus CA1. Many neocortical spines persist for months (holtmaat2005, abstract), so the rewrite rate is a loose upper bound. |
| `TAU_NEURON` | 12.4 ms (control); 20.9 ms (with CsCl) | stuart1998, [PMC6793161](https://pmc.ncbi.nlm.nih.gov/articles/PMC6793161/) | Results, "Uniform models" | full text | Rat layer 5 pyramidal neurons, in vitro. |
| `PLAST_OF_FAST` | plasticity costs 4.0–11.2% of fast excitatory transmission energy | karbowski2019, [arXiv:1910.07414](https://arxiv.org/abs/1910.07414) | abstract; Table 2 | full text | A model estimate from rat data. The arXiv version is the published *J Neurophysiol* paper. |
| `FAST_OF_SIGNAL` | postsynaptic glutamate receptors take 50% of signalling energy | howarth2012, [PMC3390818](https://pmc.ncbi.nlm.nih.gov/articles/PMC3390818/) | abstract | full text | Rodent cortex model, assuming a 4 Hz firing rate. |
| `SIGNAL_OF_TOTAL` | signalling takes at least 55% of brain energy | engl2015, [PMC4560575](https://pmc.ncbi.nlm.nih.gov/articles/PMC4560575/) | Discussion | full text | Inferred from sodium-pump block experiments. |
| (text only) | protein synthesis takes no more than ~1.3% of brain ATP | engl2015 | "Proteins and phospholipids synthesis…" | full text | A theoretical estimate from rat protein turnover. |
| `FLY_J_PER_BIT` | about 10 mJ/bit for long-term memory | girard2023, [arXiv:2301.09565](https://arxiv.org/abs/2301.09565) | abstract; Discussion | full text | Unreviewed preprint. Drosophila, from other groups' behavioural data. |
| (text only) | behaviour ~10 bit/s; sensory input ~$10^9$ bit/s | zheng2025, [arXiv:2408.10234](https://arxiv.org/abs/2408.10234) | abstract; §2 | full text | Review-based estimates. |

## GPU and language models

| Script input | Value | Source | Where in the source | Read | Caveat |
|---|---|---|---|---|---|
| `P_GPU` | up to 700 W | nvidiah100, [nvidia.com](https://www.nvidia.com/en-us/data-center/h100/) | spec table, H100 SXM, "Max TDP" | vendor page | Rated power, not measured draw. |
| `FLOPS` | 1,979 TFLOPS BF16 with sparsity, so about 989 dense | nvidiah100; andersch2022, [NVIDIA blog](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/) | spec table; blog Table 1 (1000 dense, preliminary) | vendor page | Peak figures. |
| `MFU` | 38–43% BF16 model-FLOPs utilisation | grattafiori2024, [arXiv:2407.21783](https://arxiv.org/abs/2407.21783) | Table 4 | full text | Measured in Llama 3 pre-training. |
| `DIE_CM2` | 814 mm² | andersch2022 | GH100 paragraph; Table 3 | vendor page | |
| `RHO_SI` | 2.329 g/cm³ | henins1964, [PMC6628575](https://pmc.ncbi.nlm.nih.gov/articles/PMC6628575/) | abstract | full text | |
| `WAFER_CM` | 775 ± 25 µm for a 300 mm wafer | svmisv029, [SVMI SV029](https://svmi.com/wp-content/uploads/2021/01/SV029.pdf) | geometry table | vendor page | One vendor's sheet, not the SEMI standard. Used as an upper bound on die thickness. |
| `LAYERS` … `VOCAB` | Llama 3 70B: 80 layers, model dimension 8,192, 64 heads, 8 key–value heads, vocabulary 128,000 | grattafiori2024 | Table 3 | full text | |
| `TOK_S_8GPU`, `TPOT`, `TOK_PER_REQ` | 21,605.79 tokens/s on 8 GPUs; ~155 ms per output token; ~290 tokens per request | mlcommons2024, [MLPerf v4.1 log](https://raw.githubusercontent.com/mlcommons/inference_results_v4.1/main/closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx8_TRT/llama2-70b-99/Server/performance/run_1/mlperf_log_summary.txt) | results summary, Server scenario | full text | Llama 2 70B, not Llama 3. NVIDIA's config suggests FP8, so the 16-bit cache assumption may double the physical cache size. Tokens per request is tokens/s divided by samples/s. |
| `J_TOK_SAMSI` | about 3–4 J per output token | samsi2023, [arXiv:2310.03003](https://arxiv.org/abs/2310.03003) | §IV-C | full text | LLaMA 65B on V100 GPUs. GPU energy only, extrapolated from one node. |
| `WH_PROMPT_GOOGLE` | 0.24 Wh per median Gemini Apps text prompt | elsworth2025, [arXiv:2508.15734](https://arxiv.org/abs/2508.15734) | abstract; §4.1; Table 1 | full text | Includes host, idle machines and data-centre overhead. The "median" is a model-level statistic (§3.4). |
| `GPU_H_405B` | 30.84M H100 hours at 700 W | meta2024, [model card](https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/MODEL_CARD.md) | "Hardware and Software" table | full text | Meta's estimate. The GPU hours may include work beyond pre-training. |
| `N_GPU_405B` | up to 16K H100 GPUs | grattafiori2024 | §3.3.1 | full text | Used only to convert GPU hours to wall-clock time (~78 days). |
| `BITS_PER_PARAM` | 2 bits of knowledge per parameter | allenzhu2024, [arXiv:2404.05405](https://arxiv.org/abs/2404.05405) | abstract; §1 | full text | Synthetic biography data, with 1,000 exposures per fact. An upper bound on extractable knowledge, not total weight information. |
| `E_GPT3` | 1,287 MWh | patterson2021, [arXiv:2104.10350](https://arxiv.org/abs/2104.10350) | §3; Table 4 | full text | The authors' estimate from OpenAI-supplied inputs. Not metered. |

## Assumed, no source

- `T_BRAIN` = 310 K (body temperature) and `T_DC` = 300 K (heat rejected near room temperature).
- `KV_BITS_PER_VALUE` = 16 (a BF16 key–value cache).
- `LIFE` = 70 years, the span Landauer (1986) uses.
- `KB` is exact by the SI definition.
