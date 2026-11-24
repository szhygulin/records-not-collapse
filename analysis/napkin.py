#!/usr/bin/env python3
"""Back-of-envelope numbers for paper section 5.6: a human brain and a language model.

The measure of paper section 4 is R = Sigma_dot * I / M: entropy production rate
(k_B/s) times the information in the operative records the system's dynamics
draw on (bit), per gram of the system. Table 5 computes it.

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
BITS_PER_SYN = 4.7         # bits/synapse, bartol2015 (rat CA1)
LTM_RATE = (1.2, 2.3)      # bits/s into long-term memory, landauer1986 (reading; pictures)
LTM_TOTAL = 1e9            # bits retained by a mature person, landauer1986
LTM_LOSS = 1e-9            # bits lost per bit per second, landauer1986 Table 1 central values
LIFE = 70 * YEAR           # s, the 70-year span landauer1986 uses
SPINE_LIFE = (1 * 7 * 86400, 2 * 7 * 86400)  # s, attardo2015 (mouse CA1 mean spine lifetime)
TAU_NEURON = 12.4e-3       # s, stuart1998 (membrane time constant, rat L5, control; 20.9 ms with CsCl)
PLAST_OF_FAST = (0.040, 0.112)   # plasticity / fast excitatory transmission energy, karbowski2019
FAST_OF_SIGNAL = 0.50      # postsynaptic glutamate receptors' share of signalling energy, howarth2012
SIGNAL_OF_TOTAL = 0.55     # signalling share of total brain energy ("at least"), engl2015
FLY_J_PER_BIT = 10e-3      # J/bit for long-term memory in Drosophila, girard2023 (preprint)
T_FLY = 300.0              # K, ASSUMED: a fly is near ambient temperature

# ---- NVIDIA H100 SXM and language models ------------------------------------------
P_GPU = 700.0              # W, max TDP, nvidiah100
FLOPS = 1979e12 / 2        # dense BF16 FLOP/s: page figure is with sparsity, nvidiah100; andersch2022
MFU = (0.38, 0.43)         # BF16 model-FLOPs utilisation in Llama 3 training, grattafiori2024
DIE_CM2 = 8.14             # cm^2 (814 mm^2), andersch2022
RHO_SI = 2.329             # g/cm^3, henins1964
WAFER_CM = 0.0775          # cm (775 um, 300 mm wafer), svmisv029; die is no thicker than its wafer
# Larger boundaries around 8 H100 GPUs
HGX_KG = 24.0              # kg, HGX H100 8-GPU baseboard ("Product weight 24 kg"), nvidiahgxpcf
HGX_W = 5600.0             # W, same sheet, "Typical power consumption 5600 W"
DGX_KG = 130.45            # kg, DGX H100 system weight (287.6 lb), nvidiadgxh100
DGX_W = 10.2e3             # W, DGX H100 max system power, nvidiadgxh100
# Llama 3 70B (grattafiori2024 Table 3)
LAYERS, DMODEL, HEADS, KV_HEADS, VOCAB = 80, 8192, 64, 8, 128_000
PARAMS_70B = 70e9          # ASSUMED: nominal parameter count of the 70B models
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
PARAMS_405B = 405e9        # meta2024 (model card)
BITS_PER_PARAM = 2.0       # extractable knowledge capacity, allenzhu2024
WEIGHT_BITS = 16           # ASSUMED: BF16 weights (capacity count); FP8 would halve it
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
    e_flop = [P_GPU / FLOPS, P_GPU / (FLOPS * MFU[0])]
    print("Table 2. Dissipation\n")
    print("| Quantity | Human brain | One H100 GPU |\n|---|---|---|")
    print(f"| Power (W) | {sci(P_BRAIN)} | {sci(P_GPU)} |")
    print(f"| Mass (g) | {sci(M_BRAIN)} | ≤ {die_g:.1f} (die) |")
    print(f"| Energy rate density (erg s$^{{-1}}$ g$^{{-1}}$) | {sci(erd_b)} | ≈ {sci(erd_g)} (module power over die mass) |")
    print(f"| Entropy production ($k_B$ s$^{{-1}}$) | {sci(sig_b)} | {sci(sig_g)} |")
    print(f"| Landauer ceiling (bit erasures s$^{{-1}}$) | {sci(P_BRAIN / lb)} | {sci(P_GPU / lg)} |")
    print(f"| Elementary events s$^{{-1}}$ | {rng(*sorted(ev))} synaptic | {sci(FLOPS)} operations (peak) |")
    print(f"| Energy per event (J) | {rng(*sorted(e_ev))} | {rng(*e_flop)} |")
    print(f"| Energy per event in units of $kT\\ln 2$ | {rng(*sorted(x / lb for x in e_ev))} | {rng(*(x / lg for x in e_flop))} |")
    print(f"\nGPU/brain: entropy production {sig_g / sig_b:.0f}x; energy rate density {sci(erd_g / erd_b)}x\n")

    # ---- Records
    cap = N_SYN * BITS_PER_SYN
    rewrite = [cap / t for t in SPINE_LIFE[::-1]]
    kv_bits = 2 * LAYERS * KV_HEADS * (DMODEL // HEADS) * KV_BITS_PER_VALUE
    tok_gpu = TOK_S_8GPU / 8
    info_tok = log2(VOCAB)
    tau_req = TOK_PER_REQ * TPOT
    streams = TOK_S_8GPU * TPOT                     # concurrent requests on 8 GPUs (Little's law)
    kv_live_info = streams * TOK_PER_REQ / 2 * info_tok   # entries live half a request on average
    kv_live_phys = streams * TOK_PER_REQ / 2 * kv_bits
    secs_405 = GPU_H_405B * 3600
    e_405 = secs_405 * P_GPU
    wall_405 = secs_405 / N_GPU_405B
    k405, kgpt3, k70 = (n * BITS_PER_PARAM for n in (PARAMS_405B, PARAMS_GPT3, PARAMS_70B))

    def one_minus_p(tr, td):
        """1 - p_r for p_r = max(0, 1 - td/tr) (paper section 4)."""
        return min(1.0, td / tr)

    print("Table 3. Records\n")
    print("| Record | Information | Formation rate (bit s$^{-1}$) | Lifetime $\\tau_r$ | $1-p_r$ |\n|---|---|---|---|---|")
    print(f"| Brain: long-term memory (behavioural) | {sci(LTM_TOTAL)} bit over a lifetime | {rng(*LTM_RATE)} | ~{1 / LTM_LOSS / YEAR:.0f} years | {sci(one_minus_p(1 / LTM_LOSS, TAU_NEURON))} |")
    print(f"| Brain: synaptic weights (capacity) | {sci(cap)} bit | {rng(*rewrite)} (turnover-based) | 1–2 weeks (spines) | {rng(*(one_minus_p(t, TAU_NEURON) for t in SPINE_LIFE[::-1]))} |")
    print(f"| Model at inference: key–value cache, per GPU | ≤ {info_tok:.0f} bit per token ({sci(kv_bits)} physical) | {sci(tok_gpu * info_tok)} ({sci(tok_gpu * kv_bits)} physical), output tokens only | ~{tau_req:.0f} s (one request) | {rng(one_minus_p(tau_req, TPOT), one_minus_p(tau_req / 2, TPOT))} |")
    print(f"| Model at inference: weights | none new | 0 (frozen) | — | — |")
    print(f"| Model in training (Llama 3.1 405B): weights | ≤ {sci(k405)} bit of knowledge ({sci(PARAMS_405B * WEIGHT_BITS)} raw) | ≤ {sci(k405 / wall_405)} for the cluster; ≤ {sci(k405 / secs_405)} per GPU | months or more | ≈ 0 |")
    print(f"\nKV: {kv_bits} bits/token; {tok_gpu:.0f} tok/s/GPU; {P_GPU / tok_gpu:.2f} J/token (TDP); "
          f"{streams:.0f} concurrent requests on 8 GPUs; live cache {sci(kv_live_info)} bit informational, "
          f"{sci(kv_live_phys)} physical; Samsi {J_TOK_SAMSI} J/token; Google {WH_PROMPT_GOOGLE * 3600:.0f} J/prompt; "
          f"405B wall ~{wall_405 / 86400:.0f} d; lifetime-average human retention {sci(LTM_TOTAL / LIFE)} bit/s\n")

    # ---- Cost of retained information, as bits per joule
    plast_share = [p * FAST_OF_SIGNAL * SIGNAL_OF_TOTAL for p in PLAST_OF_FAST]
    plast_w = [s * P_BRAIN for s in plast_share]
    e_life = P_BRAIN * LIFE
    print("Table 4. Retained information per joule\n")
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

    # ---- The measure R = Sigma_dot * I / M
    # (name, Sigma_dot, M, I_functional, I_capacity, M qualifier, R-functional qualifier, R-capacity qualifier)
    rows = [("Human brain", sig_b, M_BRAIN, LTM_TOTAL, cap, "", "", "")]
    for label, params in (("Llama 3 70B inference", PARAMS_70B), ("Llama 3.1 405B training, per 8 H100", PARAMS_405B)):
        i_f, i_c = params * BITS_PER_PARAM, params * WEIGHT_BITS
        rows += [
            # die mass is an upper bound and leaves out the HBM that holds the weights
            (f"{label}: GPU dies only", 8 * sig_g, 8 * die_g, i_f, i_c, "≤ ", "~ ", "≥ "),
            (f"{label}: HGX baseboard", sigma(HGX_W, T_DC), HGX_KG * 1e3, i_f, i_c, "", "≤ ", ""),
            (f"{label}: DGX server", sigma(DGX_W, T_DC), DGX_KG * 1e3, i_f, i_c, "", "≤ ", ""),
        ]
    print("Table 5. The measure $R = \\dot\\Sigma\\, I / M$\n")
    print("| System and boundary | $\\dot\\Sigma$ ($k_B$ s$^{-1}$) | $M$ (g) | $\\dot\\Sigma/M$ ($k_B$ s$^{-1}$ g$^{-1}$) "
          "| $I$, functional (bit) | $I$, capacity (bit) | $R$, functional | $R$, capacity |\n|---|---|---|---|---|---|---|---|")
    res = {}
    for name, s_, m, i_f, i_c, qm, qf, qc in rows:
        qi = "" if name.startswith("Human") else "≤ "
        print(f"| {name} | {sci(s_)} | {qm}{sci(m)} | {qc}{sci(s_ / m)} | {qi}{sci(i_f)} | {sci(i_c)} | {qf}{sci(s_ * i_f / m)} | {qc}{sci(s_ * i_c / m)} |")
        res[name] = (s_ / m, s_ * i_f / m, s_ * i_c / m)
    b = res["Human brain"]
    print("\nRatios to the human brain (density; R functional; R capacity):")
    for name, v in res.items():
        if not name.startswith("Human"):
            print(f"  {name}: {sci(v[0] / b[0])}; {sci(v[1] / b[1])}; {sci(v[2] / b[2])}")
    print(f"  Brain capacity / 70B capacity: {sci(cap / (PARAMS_70B * WEIGHT_BITS))}; / 405B: {sci(cap / (PARAMS_405B * WEIGHT_BITS))}")
    print(f"  Live KV cache (output tokens) / 70B knowledge bound: {sci(kv_live_info / (PARAMS_70B * BITS_PER_PARAM))}")
    print("Operative information a chip needs to equal the brain's R (functional; capacity), by density:")
    for name in ("Llama 3 70B inference: GPU dies only", "Llama 3 70B inference: HGX baseboard", "Llama 3 70B inference: DGX server"):
        d = res[name][0]
        print(f"  {name.split(': ')[1]}: {sci(b[1] / d)} bit; {sci(b[2] / d)} bit")


if __name__ == "__main__":
    main()
