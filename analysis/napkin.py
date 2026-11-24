#!/usr/bin/env python3
"""Back-of-envelope numbers for paper section 5.6: a human brain and a language model.

Every input below carries the citation key of its source in paper/references.bib;
analysis/sources.md gives the locator, URL and verification level of each.
Inputs marked ASSUMED have no source. Run: python3 analysis/napkin.py
Prints the tables used in the paper, as Pandoc Markdown. Standard library only.
"""
from math import log, log2

KB = 1.380649e-23          # Boltzmann constant, J/K (exact, SI definition)
LN2 = log(2)
YEAR = 365.25 * 86400      # s
T_BRAIN = 310.0            # K, ASSUMED: body temperature, 37 C
T_DC = 300.0               # K, ASSUMED: data-centre heat rejected near room temperature

# ---- Human brain -------------------------------------------------------------
P_BRAIN = 20.0             # W, balasubramanian2021 ("~20 W"; 17-20 W from glucose uptake)
M_BRAIN = 1500.0           # g, herculanohouzel2012 ("about 1.5 kg")
N_SYN = 1.64e14            # neocortical synapses, tang2001 (stereology, 5 brains)
RATE = (0.16, 0.94)        # mean cortical spikes/s/neuron, lennie2003 (best estimate; generous case)
BITS_PER_SYN = 4.7         # bits/synapse, bartol2015 (rat CA1)
LTM_RATE = (1.2, 2.3)      # bits/s into long-term memory, landauer1986 (reading; pictures)
LTM_TOTAL = 1e9            # bits retained by a mature person, landauer1986
LTM_LOSS = 1e-9            # bits lost per bit per second, landauer1986 Table 1 central values
LIFE = 70 * YEAR           # s, the 70-year span landauer1986 uses
SPINE_LIFE = (1 * 7 * 86400, 2 * 7 * 86400)  # s, attardo2015 (mouse CA1 mean spine lifetime)
TAU_NEURON = (12.4e-3, 20.9e-3)  # s, stuart1998 (membrane time constant, rat L5)
PLAST_OF_FAST = (0.040, 0.112)   # plasticity / fast excitatory transmission energy, karbowski2019
FAST_OF_SIGNAL = 0.50      # postsynaptic glutamate receptors' share of signalling energy, howarth2012
SIGNAL_OF_TOTAL = 0.55     # signalling share of total brain energy ("at least"), engl2015
FLY_J_PER_BIT = 10e-3      # J/bit for long-term memory in Drosophila, girard2023 (preprint)

# ---- NVIDIA H100 SXM and language models ------------------------------------------
P_GPU = 700.0              # W, max TDP, nvidiah100
FLOPS = 1979e12 / 2        # dense BF16 FLOP/s: page figure is with sparsity, nvidiah100; andersch2022
MFU = (0.38, 0.43)         # BF16 model-FLOPs utilisation in Llama 3 training, grattafiori2024
DIE_CM2 = 8.14             # cm^2 (814 mm^2), andersch2022
RHO_SI = 2.329             # g/cm^3, henins1964
WAFER_CM = 0.0775          # cm (775 um, 300 mm wafer), svmisv029; die is no thicker than its wafer
# Llama 3 70B (grattafiori2024 Table 3)
LAYERS, DMODEL, HEADS, KV_HEADS, VOCAB = 80, 8192, 64, 8, 128_000
KV_BITS_PER_VALUE = 16     # ASSUMED: BF16 cache; FP8 would halve it
# MLPerf Inference v4.1, Llama 2 70B on 8x H100, Server scenario, mlcommons2024
TOK_S_8GPU = 21605.79      # completed tokens/s
TPOT = 0.155               # s per output token per stream (logged mean)
TOK_PER_REQ = 290          # output tokens per request (tokens/s divided by samples/s)
J_TOK_SAMSI = (3.0, 4.0)   # J per output token, LLaMA 65B on V100s, samsi2023
WH_PROMPT_GOOGLE = 0.24    # Wh per median Gemini Apps text prompt, elsworth2025
# Training
GPU_H_405B = 30.84e6       # GPU hours, Llama 3.1 405B, meta2024 (700 W each)
N_GPU_405B = 16384         # GPUs, grattafiori2024 ("up to 16K")
PARAMS_405B = 405e9
BITS_PER_PARAM = 2.0       # extractable knowledge capacity, allenzhu2024
E_GPT3 = 1287e6 * 3600     # J (1,287 MWh), patterson2021
PARAMS_GPT3 = 175e9


def sci(x):
    """2 significant figures as Pandoc math."""
    if x == 0:
        return "0"
    m, e = f"{x:.1e}".split("e")
    e = int(e)
    if -2 <= e <= 3:
        return f"{x:.2g}" if abs(x) < 100 else f"{x:,.0f}"
    return f"${m}\\times10^{{{e}}}$"


def rng(a, b):
    return sci(a) if sci(a) == sci(b) else f"{sci(a)}–{sci(b)}"


def landauer(T):
    return KB * T * LN2


def main():
    lb, lg = landauer(T_BRAIN), landauer(T_DC)
    # Dissipation
    sig_b, sig_g = P_BRAIN / T_BRAIN / KB, P_GPU / T_DC / KB        # k_B per second
    die_g = DIE_CM2 * WAFER_CM * RHO_SI
    erd_b, erd_g = P_BRAIN * 1e7 / M_BRAIN, P_GPU * 1e7 / die_g      # erg/s/g
    ev = [N_SYN * r for r in RATE]                                  # synaptic events/s
    e_ev = [P_BRAIN / x for x in ev]                                # J/event, whole budget charged
    e_flop = [P_GPU / FLOPS, P_GPU / (FLOPS * MFU[0])]
    print("Table A. Dissipation\n")
    print("| Quantity | Human brain | One H100 GPU |\n|---|---|---|")
    print(f"| Power (W) | {sci(P_BRAIN)} | {sci(P_GPU)} |")
    print(f"| Mass (g) | {sci(M_BRAIN)} | ≤ {die_g:.1f} (die) |")
    print(f"| Energy rate density (erg s$^{{-1}}$ g$^{{-1}}$) | {sci(erd_b)} | ≥ {sci(erd_g)} |")
    print(f"| Entropy production ($k_B$ s$^{{-1}}$) | {sci(sig_b)} | {sci(sig_g)} |")
    print(f"| Landauer ceiling (bit erasures s$^{{-1}}$) | {sci(P_BRAIN / lb)} | {sci(P_GPU / lg)} |")
    print(f"| Elementary events s$^{{-1}}$ | {rng(*sorted(ev))} synaptic | {sci(FLOPS)} FLOP (peak) |")
    print(f"| Energy per event (J) | {rng(*sorted(e_ev))} | {rng(*e_flop)} |")
    print(f"| … in units of $kT\\ln 2$ | {rng(*sorted(x / lb for x in e_ev))} | {rng(*(x / lg for x in e_flop))} |")
    print(f"\nGPU/brain entropy production: {sig_g / sig_b:.0f}x; per gram: {sci((sig_g / die_g) / (sig_b / M_BRAIN))}x\n")

    # Records
    cap = N_SYN * BITS_PER_SYN
    rewrite = [cap / t for t in SPINE_LIFE[::-1]]
    kv_bits = 2 * LAYERS * KV_HEADS * (DMODEL // HEADS) * KV_BITS_PER_VALUE
    tok_gpu = TOK_S_8GPU / 8
    info_tok = log2(VOCAB)
    tau_req = TOK_PER_REQ * TPOT
    secs_405 = GPU_H_405B * 3600
    e_405 = secs_405 * P_GPU
    wall_405 = secs_405 / N_GPU_405B
    k405 = PARAMS_405B * BITS_PER_PARAM
    kgpt3 = PARAMS_GPT3 * BITS_PER_PARAM
    plast_share = [p * FAST_OF_SIGNAL * SIGNAL_OF_TOTAL for p in PLAST_OF_FAST]
    plast_w = [s * P_BRAIN for s in plast_share]

    def p(tr, td):
        return tr / (tr + td)

    print("Table B. Records\n")
    print("| Record | Information | Formation rate (bit s$^{-1}$) | Lifetime $\\tau_r$ | $1-p_r$ |\n|---|---|---|---|---|")
    print(f"| Brain: long-term memory (behavioural) | {sci(LTM_TOTAL)} bit (lifetime) | {rng(*LTM_RATE)} | ~{1 / LTM_LOSS / YEAR:.0f} years | {sci(TAU_NEURON[1] * LTM_LOSS)} |")
    print(f"| Brain: synaptic weights (capacity) | {sci(cap)} bit | ≤ {rng(*rewrite)} | 1–2 weeks (spines) | {sci(1 - p(SPINE_LIFE[0], TAU_NEURON[1]))} |")
    print(f"| LLM inference: KV cache, per GPU | ≤ {info_tok:.0f} bit/token ({sci(kv_bits)} physical) | ≤ {sci(tok_gpu * info_tok)} ({sci(tok_gpu * kv_bits)} physical) | ~{tau_req:.0f} s (one request) | {sci(1 - p(tau_req, TPOT))} |")
    print(f"| LLM inference: weights | — | 0 (frozen) | — | — |")
    print(f"| LLM training (405B): weights | ≤ {sci(k405)} bit knowledge ({sci(PARAMS_405B * 16)} raw) | {sci(k405 / wall_405)} cluster; {sci(k405 / secs_405)} per GPU | months or more | ≈ 0 |")
    print(f"\nKV: {kv_bits} bits/token; {tok_gpu:.0f} tok/s/GPU; {P_GPU / tok_gpu:.2f} J/token (TDP); "
          f"Samsi {J_TOK_SAMSI} J/token; Google {WH_PROMPT_GOOGLE * 3600:.0f} J/prompt; 405B wall ~{wall_405 / 86400:.0f} d\n")

    print("Table C. Cost of retained information\n")
    print("| System | Retained information (bit) | Energy (J) | J per bit | × $kT\\ln 2$ |\n|---|---|---|---|---|")
    e_life = P_BRAIN * LIFE
    rows = [
        ("Human, whole brain budget over 70 years", LTM_TOTAL, e_life, lb),
        ("Human, plasticity share only", LTM_TOTAL, (plast_w[0] * LIFE, plast_w[1] * LIFE), lb),
        ("Fruit fly, marginal cost of memory", None, None, lb),
        ("Llama 3.1 405B training", k405, e_405, lg),
        ("GPT-3 training", kgpt3, E_GPT3, lg),
    ]
    for name, bits, e, kt in rows:
        if bits is None:
            print(f"| {name} | — | — | {sci(FLY_J_PER_BIT)} | {sci(FLY_J_PER_BIT / kt)} |")
        elif isinstance(e, tuple):
            print(f"| {name} | {sci(bits)} | {rng(*e)} | {rng(e[0] / bits, e[1] / bits)} | {rng(e[0] / bits / kt, e[1] / bits / kt)} |")
        else:
            print(f"| {name} | {sci(bits)} | {sci(e)} | {sci(e / bits)} | {sci(e / bits / kt)} |")
    print(f"\nPlasticity share of brain energy: {rng(*plast_share)} = {rng(*plast_w)} W\n")

    print("Table D. The measure before $u_r$: entropy spent on records that outlast the dynamics ($k_B$ s$^{-1}$)\n")
    print("| Attribution of $\\Delta S_r$ | Human brain | H100, inference | H100, training |\n|---|---|---|---|")
    print(f"| Landauer floor, $k\\ln 2$ per retained bit | {rng(*(r * LN2 for r in LTM_RATE))} (behavioural); ≤ {rng(*(r * LN2 for r in rewrite))} (synaptic) "
          f"| 0 lasting; ≤ {sci(tok_gpu * info_tok * LN2)} within a request | {sci(k405 / secs_405 * LN2)} |")
    print(f"| Direct cost of writing | {rng(*(w / T_BRAIN / KB for w in plast_w))} (plasticity) | 0 lasting | not estimated |")
    print(f"| Whole budget of the system while it records | {sci(sig_b)} | 0 lasting | {sci(sig_g)} |")


if __name__ == "__main__":
    main()
