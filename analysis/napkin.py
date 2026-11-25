#!/usr/bin/env python3
"""Back-of-envelope numbers for paper section 5.6: a human brain and a language model.

A napkin check, not a computation of the paper's measure R (section 4): Table 2
compares dissipation, the inference lines give the key-value cache facts, and
Table 3 compares information retained per joule.

Every input below carries the citation key of its source in paper/references.bib;
analysis/sources.md gives the locator, URL and verification level of each.
Inputs marked ASSUMED have no source. Run: python3 analysis/napkin.py
Prints the tables used in the paper, as Pandoc Markdown. Standard library only.
"""
from math import floor, log, log10, log2

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
LTM_TOTAL = 1e9            # bits retained by a mature person, landauer1986
LIFE = 70 * YEAR           # s, the 70-year span landauer1986 uses
PLAST_OF_FAST = (0.040, 0.112)   # plasticity / fast excitatory transmission energy, karbowski2019
FAST_OF_SIGNAL = 0.50      # postsynaptic glutamate receptors' share of signalling energy, howarth2012
SIGNAL_OF_TOTAL = 0.55     # signalling share of total brain energy ("at least"), engl2015
FLY_J_PER_BIT = 10e-3      # J/bit for long-term memory in Drosophila, girard2023 (preprint)
T_FLY = 300.0              # K, ASSUMED: a fly is near ambient temperature

# ---- NVIDIA H100 SXM and language models ------------------------------------------
P_GPU = 700.0              # W, max TDP, nvidiah100
FLOPS = 1979e12 / 2        # dense BF16 FLOP/s: page figure is with sparsity, nvidiah100; andersch2022
MFU_LOW = 0.38             # lowest BF16 model-FLOPs utilisation in Llama 3 training, grattafiori2024
DIE_CM2 = 8.14             # cm^2 (814 mm^2), andersch2022
RHO_SI = 2.329             # g/cm^3, henins1964
WAFER_CM = 0.0775          # cm (775 um, 300 mm wafer), svmisv029; die is no thicker than its wafer
VOCAB = 128_000            # Llama 3 vocabulary, grattafiori2024 (Table 3)
# MLPerf Inference v4.1, Llama 2 70B on 8x H100, Server scenario, mlcommons2024
TOK_S_8GPU = 21605.79      # completed tokens/s
TPOT = 0.155               # s per output token per stream (logged mean)
TOK_PER_REQ = 290          # output tokens per request (tokens/s divided by samples/s)
# Training
GPU_H_405B = 30.84e6       # GPU hours, Llama 3.1 405B, meta2024 (700 W each)
PARAMS_405B = 405e9        # meta2024 (model card)
BITS_PER_PARAM = 2.0       # extractable knowledge capacity, allenzhu2024
E_GPT3 = 1287e6 * 3600     # J (1,287 MWh), patterson2021
PARAMS_GPT3 = 175e9        # patterson2021 (Table 4)


def sci(x):
    """2 significant figures; Pandoc math for exponents outside -2..3."""
    if x == 0:
        return "0"
    r = float(f"{x:.2g}")
    e = floor(log10(abs(r)))
    if -2 <= e <= 3:
        return f"{r:,.{max(0, 1 - e)}f}"
    return f"${r / 10 ** e:.1f}\\times10^{{{e}}}$"


def rng(a, b):
    return sci(a) if sci(a) == sci(b) else f"{sci(a)}–{sci(b)}"


def landauer(T):
    return KB * T * LN2


def sigma(watts, kelvin):
    """Entropy production rate of a steady state, in k_B per second."""
    return watts / kelvin / KB


def main():
    lb, lg, lf = landauer(T_BRAIN), landauer(T_DC), landauer(T_FLY)
    # ---- Dissipation
    sig_b, sig_g = sigma(P_BRAIN, T_BRAIN), sigma(P_GPU, T_DC)
    die_g = DIE_CM2 * WAFER_CM * RHO_SI
    erd_b, erd_g = P_BRAIN * 1e7 / M_BRAIN, P_GPU * 1e7 / die_g      # erg/s/g
    ev = [N_SYN * r for r in RATE]                                  # synaptic events/s
    e_ev = [P_BRAIN / x for x in ev]                                # J/event, whole budget charged
    e_flop = [P_GPU / FLOPS, P_GPU / (FLOPS * MFU_LOW)]
    print("Table 2. Dissipation\n")
    print("| Quantity | Human brain | One H100 GPU |\n|---|---|---|")
    print(f"| Power (W) | {sci(P_BRAIN)} | {sci(P_GPU)} |")
    print(f"| Mass (g) | {sci(M_BRAIN)} | ≤ {die_g:.1f} (die) |")
    print(f"| Energy rate density (erg s$^{{-1}}$ g$^{{-1}}$) | {sci(erd_b)} | ≥ {sci(erd_g)} (module power over die mass) |")
    print(f"| Entropy production ($k_B$ s$^{{-1}}$) | {sci(sig_b)} | {sci(sig_g)} |")
    print(f"| Landauer ceiling (bit erasures s$^{{-1}}$) | {sci(P_BRAIN / lb)} | {sci(P_GPU / lg)} |")
    print(f"| Elementary events s$^{{-1}}$ | {rng(*sorted(ev))} synaptic | {sci(FLOPS)} operations (peak) |")
    print(f"| Energy per event (J) | {rng(*sorted(e_ev))} | {rng(*e_flop)} |")
    print(f"| Energy per event in units of $kT\\ln 2$ | {rng(*sorted(x / lb for x in e_ev))} | {rng(*(x / lg for x in e_flop))} |")
    print(f"\nGPU/brain: entropy production {sig_g / sig_b:.0f}x; energy rate density {sci(erd_g / erd_b)}x\n")

    # ---- Inference: what the key-value cache holds and how long it lives
    tok_gpu = TOK_S_8GPU / 8
    info_tok = log2(VOCAB)
    tau_req = TOK_PER_REQ * TPOT
    print(f"Inference: {tok_gpu:.0f} tok/s/GPU; {P_GPU / tok_gpu:.2f} J/token (TDP); at most {info_tok:.0f} bit of "
          f"information per token; cache lives ~{tau_req:.0f} s for a {TOK_PER_REQ}-token reply\n")

    # ---- Cost of retained information, as bits per joule
    secs_405 = GPU_H_405B * 3600
    e_405 = secs_405 * P_GPU
    k405, kgpt3 = (n * BITS_PER_PARAM for n in (PARAMS_405B, PARAMS_GPT3))
    plast_share = [p * FAST_OF_SIGNAL * SIGNAL_OF_TOTAL for p in PLAST_OF_FAST]
    plast_w = [s * P_BRAIN for s in plast_share]
    e_life = P_BRAIN * LIFE
    print("Table 3. Retained information per joule\n")
    print("| System | Retained information (bit) | Energy (J) | Bits per J | Fraction of the Landauer limit |\n|---|---|---|---|---|")
    print(f"| Human: whole brain budget over 70 years | {sci(LTM_TOTAL)} | {sci(e_life)} | {sci(LTM_TOTAL / e_life)} | {sci(LTM_TOTAL / e_life * lb)} |")
    hi, lo = (LTM_TOTAL / (w * LIFE) for w in plast_w)
    print(f"| Human: plasticity share only | {sci(LTM_TOTAL)} | {rng(*(w * LIFE for w in plast_w))} | {rng(lo, hi)} | {rng(lo * lb, hi * lb)} |")
    print(f"| Fruit fly: marginal cost of long-term memory | — | — | {sci(1 / FLY_J_PER_BIT)} | {sci(lf / FLY_J_PER_BIT)} |")
    print(f"| Llama 3.1 405B training | ≤ {sci(k405)} | {sci(e_405)} | ≤ {sci(k405 / e_405)} | ≤ {sci(k405 / e_405 * lg)} |")
    print(f"| GPT-3 training | ≤ {sci(kgpt3)} | {sci(E_GPT3)} | ≤ {sci(kgpt3 / E_GPT3)} | ≤ {sci(kgpt3 / E_GPT3 * lg)} |")
    jb = {"brain": e_life / LTM_TOTAL, "plast": [w * LIFE / LTM_TOTAL for w in plast_w],
          "llama": e_405 / k405, "gpt3": E_GPT3 / kgpt3}
    lo_r = min(jb["gpt3"], jb["llama"]) / jb["brain"]
    hi_r = max(jb["gpt3"], jb["llama"]) / min(jb["plast"])
    print(f"\nPlasticity share of brain energy: {rng(*plast_share)} = {rng(*plast_w)} W. "
          f"Training cost per bit relative to the human brain: at least {lo_r:.2f}x to {hi_r:.0f}x\n")

if __name__ == "__main__":
    main()
