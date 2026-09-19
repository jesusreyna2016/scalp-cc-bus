# Scalp CC · report 2026-09-19T01:22Z
- signals=13132 outcomes=12548 pares_resueltos=13095 pendientes=37 huerfanos=32

## ⚠ ALERTAS (llevar al frente del resumen)
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.239 vs 0.061, delta 0.178 CI90 [0.136, 0.223], n 8313). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.212 vs 0.064, delta 0.148 CI90 [0.059, 0.24], n 2307). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.103 CI90 [0.028, 0.181], n 639). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.078 CI90 [0.043, 0.113], n 3064). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.055, "ci90": [0.037, 0.073], "p_mean_le_0": 0.0, "n": 12516}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 130 | 42.3 | 0.011 | 1.02 | 59 | 13.0 | 11.5 | 18.6 |
| 1m/INV/SHORT | 96 | 47.9 | 0.064 | 1.14 | 43 | 20.0 | 11.0 | 18.6 |
| 1m/RETEST/LONG | 4849 | 45.7 | 0.053 | 1.11 | 2286 | 15.0 | 11.0 | 28.6 |
| 1m/RETEST/SHORT | 3123 | 44.0 | 0.051 | 1.1 | 1444 | 17.0 | 11.0 | 31.2 |
| 2m/INV/LONG | 40 | 52.5 | -0.099 | 0.77 | 16 | 12.0 | 10.0 | 25.0 |
| 2m/INV/SHORT | 41 | 34.1 | -0.033 | 0.94 | 23 | 20.0 | 15.75 | 34.8 |
| 2m/RETEST/LONG | 2186 | 47.2 | 0.018 | 1.04 | 1020 | 18.0 | 13.0 | 36.3 |
| 2m/RETEST/SHORT | 1328 | 47.7 | 0.074 | 1.16 | 599 | 21.0 | 13.0 | 39.6 |
| 5m/INV/LONG | 16 | 62.5 | 0.405 | 2.89 | 3 | 37.0 | 31.25 | 66.7 |
| 5m/INV/SHORT | 9 | 66.7 | 0.436 | 2.31 | 3 | 37.0 | 68.75 | 66.7 |
| 5m/RETEST/LONG | 791 | 52.2 | 0.154 | 1.36 | 322 | 30.0 | 20.0 | 49.7 |
| 5m/RETEST/SHORT | 486 | 47.3 | 0.081 | 1.17 | 209 | 32.0 | 22.5 | 36.8 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 928 | 25.6 | 0.102 | 1.16 | 572 | 29.0 | 15.0 | 19.6 |
| B | 5454 | 46.8 | 0.053 | 1.11 | 2495 | 17.0 | 13.0 | 32.9 |
| C | 6713 | 48.6 | 0.051 | 1.11 | 2960 | 17.0 | 13.0 | 35.5 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 4725 | 49.7 | 0.089 | 1.19 | 2100 | 13.0 | 10.0 | 38.3 |
| London | 2022 | 46.0 | 0.004 | 1.01 | 1002 | 18.0 | 12.0 | 32.6 |
| NY | 2321 | 44.3 | 0.119 | 1.25 | 1024 | 25.0 | 16.0 | 36.8 |
| Sin KZ | 4027 | 43.3 | 0.006 | 1.01 | 1901 | 19.0 | 14.0 | 25.0 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 2971 | 44.3 | 0.05 | 1.1 | 1388 | 21.0 | 14.0 | 31.9 |
| edge=0 | 5817 | 48.6 | 0.053 | 1.11 | 2600 | 16.0 | 11.0 | 37.3 |
| edge=1 | 4307 | 44.3 | 0.062 | 1.13 | 2039 | 18.0 | 14.0 | 28.0 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 13086 | 46.2 | 0.055 | 1.11 | 6026 | 18.0 | 13.0 | 32.9 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 78 | 51.3 | 0.091 | 1.22 | 29 | 12.0 | 10.25 | 27.6 |
| INV/LONG|edge=1 | 104 | 42.3 | -0.052 | 0.89 | 47 | 19.5 | 17.5 | 17.0 |
| INV/SHORT|edge=-1 | 87 | 39.1 | 0.043 | 1.08 | 45 | 22.0 | 12.0 | 26.7 |
| INV/SHORT|edge=0 | 50 | 52.0 | -0.03 | 0.93 | 21 | 16.0 | 15.5 | 28.6 |
| INV/SHORT|edge=1 | 9 | 66.7 | 0.69 | 3.07 | 3 | 28.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 278 | 53.6 | 0.18 | 1.44 | 110 | 13.0 | 8.0 | 52.7 |
| RETEST/LONG|edge=0 | 3503 | 49.5 | 0.03 | 1.06 | 1591 | 15.0 | 11.0 | 37.5 |
| RETEST/LONG|edge=1 | 4045 | 43.9 | 0.064 | 1.13 | 1927 | 19.0 | 14.0 | 27.5 |
| RETEST/SHORT|edge=-1 | 2602 | 43.5 | 0.035 | 1.07 | 1231 | 22.0 | 15.0 | 30.2 |
| RETEST/SHORT|edge=0 | 2186 | 46.8 | 0.09 | 1.19 | 959 | 17.0 | 11.0 | 37.4 |
| RETEST/SHORT|edge=1 | 149 | 55.0 | 0.057 | 1.13 | 62 | 14.0 | 9.75 | 54.8 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 51 | 37.3 | -0.164 | 0.71 | 27 | 15.0 | 19.0 | 11.1 |
| INV/LONG|tier=C | 135 | 49.6 | 0.091 | 1.22 | 51 | 13.0 | 12.5 | 27.5 |
| INV/SHORT|tier=B | 45 | 42.2 | 0.015 | 1.03 | 24 | 18.0 | 9.5 | 8.3 |
| INV/SHORT|tier=C | 101 | 46.5 | 0.08 | 1.17 | 45 | 22.0 | 28.0 | 35.6 |
| RETEST/LONG|tier=A+ | 596 | 24.8 | 0.075 | 1.11 | 377 | 26.5 | 15.0 | 17.5 |
| RETEST/LONG|tier=B | 3274 | 47.2 | 0.079 | 1.17 | 1485 | 17.0 | 12.0 | 32.5 |
| RETEST/LONG|tier=C | 3956 | 49.7 | 0.028 | 1.06 | 1766 | 16.0 | 12.0 | 36.0 |
| RETEST/SHORT|tier=A+ | 332 | 27.1 | 0.152 | 1.24 | 195 | 33.5 | 15.0 | 23.6 |
| RETEST/SHORT|tier=B | 2084 | 46.5 | 0.018 | 1.04 | 959 | 18.0 | 13.0 | 34.8 |
| RETEST/SHORT|tier=C | 2521 | 46.8 | 0.084 | 1.18 | 1098 | 19.0 | 12.5 | 35.1 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 186 | 46.2 | 0.018 | 1.04 | 78 | 14.0 | 14.0 | 21.8 |
| INV/SHORT|aligned=1 | 146 | 45.2 | 0.06 | 1.12 | 69 | 20.5 | 16.25 | 26.1 |
| RETEST/LONG|aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 7817 | 46.8 | 0.053 | 1.11 | 3627 | 17.0 | 12.0 | 32.6 |
| RETEST/SHORT|aligned=1 | 4937 | 45.3 | 0.06 | 1.12 | 2252 | 19.0 | 13.0 | 34.0 |

## Autopsia de SL
n_losses=6027  causas: RR-bajo×2285, contra-estructura×2074, stop-en-el-minimo×1984, killzone-Asia-largo×1261, sin-nivel-detras×1221, estirado×1054, chop×869, SL-muy-pegado×741, sin-causa-clara×620, contra-sesgo×1
- INV/LONG (n=78): RR-bajo×36, killzone-Asia-largo×32, contra-estructura×22, stop-en-el-minimo×17, estirado×17, chop×10, sin-nivel-detras×9, SL-muy-pegado×7, sin-causa-clara×2
- INV/SHORT (n=69): RR-bajo×34, contra-estructura×19, stop-en-el-minimo×18, estirado×15, sin-causa-clara×12, SL-muy-pegado×9, chop×8, sin-nivel-detras×5
- RETEST/LONG (n=3628): RR-bajo×1377, contra-estructura×1330, killzone-Asia-largo×1229, stop-en-el-minimo×1184, sin-nivel-detras×760, estirado×612, chop×559, SL-muy-pegado×429, sin-causa-clara×299, contra-sesgo×1
- RETEST/SHORT (n=2252): RR-bajo×838, stop-en-el-minimo×765, contra-estructura×703, sin-nivel-detras×447, estirado×410, sin-causa-clara×307, SL-muy-pegado×296, chop×292

## Autopsia de SL · semana 2026-W38 (para revision semanal)
n_losses=2029  causas: RR-bajo×758, contra-estructura×671, stop-en-el-minimo×654, killzone-Asia-largo×460, sin-nivel-detras×427, estirado×363, chop×297, SL-muy-pegado×242, sin-causa-clara×231
ejemplos por causa: {"RR-bajo": ["CL-1-23392-L", "YM-1-23338-S", "YM-1-23940-L", "ES-1-24959-L", "ES-1-25022-L"], "contra-estructura": ["NQ-2-22865-L", "NQ-1-25031-L", "NQ-2-22875-L", "ES-2-22980-L", "GC-2-22998-L"], "stop-en-el-minimo": ["YM-1-23338-S", "ES-2-22832-L", "ES-2-22835-L", "CL-1-24795-L", "YM-2-22886-L"]}

## Contrafactual de gestion
```json
{
  "n": 9,
  "baseline_nextLevel_expR": 0.276,
  "fixed_1R": [
    0.258,
    8
  ],
  "fixed_1_5R": [
    0.276,
    8
  ],
  "fixed_2R": [
    0.276,
    8
  ],
  "fixed_3R": [
    0.276,
    8
  ],
  "altSL_0_5x_struct": [
    0.281,
    9
  ],
  "altSL_1_5x_struct": [
    0.26,
    9
  ],
  "note": "fixed_XR: R esperado si el objetivo fuera XR fijo con SL=struct. altSL: SL a mult del SL struct."
}
```

## Modelo GESTIONADO (escalera + parciales) vs INGENUO
```json
{
  "overall": {
    "n": 12502,
    "naive_expR": 0.055,
    "managed_expR": 0.129,
    "delta": 0.074,
    "avgEntryBetterTk_p50": 2.5,
    "fill_t3plus_pct": 46.0,
    "fill_full_pct": 32.7,
    "m1_rate": 37.1,
    "m2_rate": 23.1,
    "m3_rate": 12.4,
    "beAfterM1_rate": 17.9
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 121,
      "naive_expR": 0.011,
      "managed_expR": 0.222,
      "delta": 0.211,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 50.4,
      "fill_full_pct": 37.2,
      "m1_rate": 40.5,
      "m2_rate": 26.4,
      "m3_rate": 13.2,
      "beAfterM1_rate": 20.7
    },
    "1m/INV/SHORT": {
      "n": 92,
      "naive_expR": 0.064,
      "managed_expR": 0.271,
      "delta": 0.207,
      "avgEntryBetterTk_p50": 3.1500000000000004,
      "fill_t3plus_pct": 51.1,
      "fill_full_pct": 41.3,
      "m1_rate": 38.0,
      "m2_rate": 23.9,
      "m3_rate": 15.2,
      "beAfterM1_rate": 18.5
    },
    "1m/RETEST/LONG": {
      "n": 4695,
      "naive_expR": 0.052,
      "managed_expR": 0.135,
      "delta": 0.083,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.9,
      "fill_full_pct": 34.7,
      "m1_rate": 36.9,
      "m2_rate": 23.0,
      "m3_rate": 12.0,
      "beAfterM1_rate": 16.9
    },
    "1m/RETEST/SHORT": {
      "n": 2934,
      "naive_expR": 0.052,
      "managed_expR": 0.159,
      "delta": 0.107,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.1,
      "fill_full_pct": 33.5,
      "m1_rate": 39.8,
      "m2_rate": 24.8,
      "m3_rate": 14.0,
      "beAfterM1_rate": 18.9
    },
    "2m/INV/LONG": {
      "n": 38,
      "naive_expR": -0.099,
      "managed_expR": -0.059,
      "delta": 0.04,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 34.2,
      "m1_rate": 18.4,
      "m2_rate": 15.8,
      "m3_rate": 0.0,
      "beAfterM1_rate": 2.6
    },
    "2m/INV/SHORT": {
      "n": 41,
      "naive_expR": -0.033,
      "managed_expR": -0.09,
      "delta": -0.058,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 48.8,
      "fill_full_pct": 41.5,
      "m1_rate": 24.4,
      "m2_rate": 22.0,
      "m3_rate": 12.2,
      "beAfterM1_rate": 4.9
    },
    "2m/RETEST/LONG": {
      "n": 2097,
      "naive_expR": 0.017,
      "managed_expR": 0.071,
      "delta": 0.054,
      "avgEntryBetterTk_p50": 2.4,
      "fill_t3plus_pct": 43.3,
      "fill_full_pct": 29.9,
      "m1_rate": 34.9,
      "m2_rate": 20.5,
      "m3_rate": 10.8,
      "beAfterM1_rate": 17.9
    },
    "2m/RETEST/SHORT": {
      "n": 1271,
      "naive_expR": 0.074,
      "managed_expR": 0.143,
      "delta": 0.069,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 46.6,
      "fill_full_pct": 33.7,
      "m1_rate": 36.8,
      "m2_rate": 23.7,
      "m3_rate": 12.7,
      "beAfterM1_rate": 18.4
    },
    "5m/INV/LONG": {
      "n": 14,
      "naive_expR": 0.405,
      "managed_expR": 0.237,
      "delta": -0.168,
      "avgEntryBetterTk_p50": 2.65,
      "fill_t3plus_pct": 35.7,
      "fill_full_pct": 21.4,
      "m1_rate": 28.6,
      "m2_rate": 21.4,
      "m3_rate": 7.1,
      "beAfterM1_rate": 14.3
    },
    "5m/INV/SHORT": {
      "n": 9,
      "naive_expR": 0.436,
      "managed_expR": 0.473,
      "delta": 0.037,
      "avgEntryBetterTk_p50": 8.4,
      "fill_t3plus_pct": 66.7,
      "fill_full_pct": 44.4,
      "m1_rate": 33.3,
      "m2_rate": 22.2,
      "m3_rate": 22.2,
      "beAfterM1_rate": 11.1
    },
    "5m/RETEST/LONG": {
      "n": 745,
      "naive_expR": 0.154,
      "managed_expR": 0.104,
      "delta": -0.05,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 32.9,
      "fill_full_pct": 24.3,
      "m1_rate": 35.0,
      "m2_rate": 23.0,
      "m3_rate": 12.8,
      "beAfterM1_rate": 19.1
    },
    "5m/RETEST/SHORT": {
      "n": 445,
      "naive_expR": 0.08,
      "managed_expR": 0.126,
      "delta": 0.046,
      "avgEntryBetterTk_p50": 4.5,
      "fill_t3plus_pct": 42.5,
      "fill_full_pct": 26.7,
      "m1_rate": 37.1,
      "m2_rate": 22.5,
      "m3_rate": 12.6,
      "beAfterM1_rate": 18.9
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 10923,
    "layer_expR": 0.061,
    "orig_expR": 0.226,
    "delta_orig_minus_layer": 0.166,
    "delta_ci90": [
      0.129,
      0.203
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.2,
    "orig_wrTP1": 33.6,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 9.0,
    "orig_wider_pct": 4.0,
    "orig_saved_from_SL": 20,
    "orig_caused_SL": 1616
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 303,
      "layer_expR": 0.034,
      "orig_expR": -0.017,
      "delta_orig_minus_layer": -0.051,
      "delta_ci90": [
        -0.245,
        0.156
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.5,
      "orig_wrTP1": 26.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 6.9,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 65
    },
    "legacy": {
      "n": 7,
      "layer_expR": 0.339,
      "orig_expR": 1.227,
      "delta_orig_minus_layer": 0.889,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 85.7,
      "orig_wrTP1": 85.7,
      "slTk_p50": 6.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 42.9,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 1
    },
    "retestBar": {
      "n": 8313,
      "layer_expR": 0.061,
      "orig_expR": 0.239,
      "delta_orig_minus_layer": 0.178,
      "delta_ci90": [
        0.136,
        0.223
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.7,
      "orig_wrTP1": 34.2,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 4.2,
      "orig_saved_from_SL": 18,
      "orig_caused_SL": 1222
    },
    "retestBar2": {
      "n": 2307,
      "layer_expR": 0.064,
      "orig_expR": 0.212,
      "delta_orig_minus_layer": 0.148,
      "delta_ci90": [
        0.059,
        0.24
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.4,
      "orig_wrTP1": 32.2,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 329
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 121,
      "layer_expR": 0.011,
      "orig_expR": -0.172,
      "delta_orig_minus_layer": -0.183,
      "delta_ci90": [
        -0.462,
        0.1
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 45.5,
      "orig_wrTP1": 20.7,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 5.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 30
    },
    "1m/INV/SHORT": {
      "n": 82,
      "layer_expR": 0.065,
      "orig_expR": -0.089,
      "delta_orig_minus_layer": -0.154,
      "delta_ci90": [
        -0.498,
        0.201
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.8,
      "orig_wrTP1": 25.6,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.5,
      "orig_wider_pct": 3.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 19
    },
    "1m/RETEST/LONG": {
      "n": 4078,
      "layer_expR": 0.057,
      "orig_expR": 0.209,
      "delta_orig_minus_layer": 0.152,
      "delta_ci90": [
        0.09,
        0.213
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.6,
      "orig_wrTP1": 30.0,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 1.1,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 680
    },
    "1m/RETEST/SHORT": {
      "n": 2432,
      "layer_expR": 0.057,
      "orig_expR": 0.209,
      "delta_orig_minus_layer": 0.153,
      "delta_ci90": [
        0.063,
        0.244
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.2,
      "orig_wrTP1": 31.9,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 347
    },
    "2m/INV/LONG": {
      "n": 38,
      "layer_expR": -0.099,
      "orig_expR": 0.5,
      "delta_orig_minus_layer": 0.599,
      "delta_ci90": [
        -0.157,
        1.493
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 55.3,
      "orig_wrTP1": 34.2,
      "slTk_p50": 24.5,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 10.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 8
    },
    "2m/INV/SHORT": {
      "n": 40,
      "layer_expR": -0.044,
      "orig_expR": 0.346,
      "delta_orig_minus_layer": 0.39,
      "delta_ci90": [
        -0.055,
        0.993
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 32.5,
      "orig_wrTP1": 30.0,
      "slTk_p50": 23.5,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 5.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 2
    },
    "2m/RETEST/LONG": {
      "n": 1897,
      "layer_expR": 0.031,
      "orig_expR": 0.184,
      "delta_orig_minus_layer": 0.153,
      "delta_ci90": [
        0.079,
        0.228
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.8,
      "orig_wrTP1": 36.2,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 260
    },
    "2m/RETEST/SHORT": {
      "n": 1092,
      "layer_expR": 0.087,
      "orig_expR": 0.222,
      "delta_orig_minus_layer": 0.134,
      "delta_ci90": [
        0.039,
        0.234
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.3,
      "orig_wrTP1": 36.7,
      "slTk_p50": 22.5,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.9,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 150
    },
    "5m/INV/LONG": {
      "n": 14,
      "layer_expR": 0.405,
      "orig_expR": -0.54,
      "delta_orig_minus_layer": -0.945,
      "delta_ci90": [
        -1.456,
        -0.508
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 71.4,
      "orig_wrTP1": 35.7,
      "slTk_p50": 52.5,
      "slOrigTk_p50": 10.5,
      "orig_wider_pct": 21.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 5
    },
    "5m/INV/SHORT": {
      "n": 8,
      "layer_expR": 0.425,
      "orig_expR": -0.294,
      "delta_orig_minus_layer": -0.719,
      "delta_ci90": [
        -1.204,
        -0.241
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 62.5,
      "orig_wrTP1": 50.0,
      "slTk_p50": 39.0,
      "slOrigTk_p50": 73.0,
      "orig_wider_pct": 37.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 1
    },
    "5m/RETEST/LONG": {
      "n": 713,
      "layer_expR": 0.145,
      "orig_expR": 0.42,
      "delta_orig_minus_layer": 0.276,
      "delta_ci90": [
        0.111,
        0.466
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 55.4,
      "orig_wrTP1": 45.4,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 17.0,
      "orig_wider_pct": 16.1,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 77
    },
    "5m/RETEST/SHORT": {
      "n": 408,
      "layer_expR": 0.064,
      "orig_expR": 0.554,
      "delta_orig_minus_layer": 0.49,
      "delta_ci90": [
        0.142,
        0.909
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.5,
      "orig_wrTP1": 43.1,
      "slTk_p50": 31.0,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 21.1,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 37
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 2994,
    "wrTP1": 44.6,
    "expR": -0.021
  },
  "2026-W37": {
    "n": 5279,
    "wrTP1": 46.8,
    "expR": 0.071
  },
  "2026-W38": {
    "n": 4822,
    "wrTP1": 46.5,
    "expR": 0.087
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 36,
      "wrTP1": 44.4,
      "expR": 0.208,
      "pf": 1.44
    },
    "1m/INV/SHORT": {
      "n": 19,
      "wrTP1": 68.4,
      "expR": 0.264,
      "pf": 1.95
    },
    "1m/RETEST/LONG": {
      "n": 1279,
      "wrTP1": 42.5,
      "expR": -0.02,
      "pf": 0.96
    },
    "1m/RETEST/SHORT": {
      "n": 442,
      "wrTP1": 43.4,
      "expR": -0.012,
      "pf": 0.98
    },
    "2m/INV/LONG": {
      "n": 17,
      "wrTP1": 41.2,
      "expR": -0.228,
      "pf": 0.61
    },
    "2m/INV/SHORT": {
      "n": 6,
      "wrTP1": 50.0,
      "expR": -0.267,
      "pf": 0.47
    },
    "2m/RETEST/LONG": {
      "n": 641,
      "wrTP1": 46.2,
      "expR": -0.054,
      "pf": 0.89
    },
    "2m/RETEST/SHORT": {
      "n": 210,
      "wrTP1": 40.5,
      "expR": -0.114,
      "pf": 0.79
    },
    "5m/INV/LONG": {
      "n": 6,
      "wrTP1": 100.0,
      "expR": 0.712,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 0.018,
      "pf": 1.07
    },
    "5m/RETEST/LONG": {
      "n": 242,
      "wrTP1": 52.5,
      "expR": 0.082,
      "pf": 1.18
    },
    "5m/RETEST/SHORT": {
      "n": 92,
      "wrTP1": 46.7,
      "expR": -0.031,
      "pf": 0.94
    }
  },
  "2026-W37": {
    "1m/INV/LONG": {
      "n": 36,
      "wrTP1": 41.7,
      "expR": -0.046,
      "pf": 0.9
    },
    "1m/INV/SHORT": {
      "n": 55,
      "wrTP1": 41.8,
      "expR": 0.057,
      "pf": 1.11
    },
    "1m/RETEST/LONG": {
      "n": 1576,
      "wrTP1": 45.2,
      "expR": 0.049,
      "pf": 1.1
    },
    "1m/RETEST/SHORT": {
      "n": 1707,
      "wrTP1": 44.9,
      "expR": 0.043,
      "pf": 1.08
    },
    "2m/INV/LONG": {
      "n": 9,
      "wrTP1": 55.6,
      "expR": -0.009,
      "pf": 0.98
    },
    "2m/INV/SHORT": {
      "n": 31,
      "wrTP1": 35.5,
      "expR": 0.137,
      "pf": 1.27
    },
    "2m/RETEST/LONG": {
      "n": 663,
      "wrTP1": 47.8,
      "expR": 0.039,
      "pf": 1.08
    },
    "2m/RETEST/SHORT": {
      "n": 745,
      "wrTP1": 51.4,
      "expR": 0.148,
      "pf": 1.33
    },
    "5m/INV/LONG": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 1.055,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 1.212,
      "pf": 5.85
    },
    "5m/RETEST/LONG": {
      "n": 232,
      "wrTP1": 52.2,
      "expR": 0.203,
      "pf": 1.45
    },
    "5m/RETEST/SHORT": {
      "n": 217,
      "wrTP1": 51.6,
      "expR": 0.111,
      "pf": 1.24
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 58,
      "wrTP1": 41.4,
      "expR": -0.085,
      "pf": 0.84
    },
    "1m/INV/SHORT": {
      "n": 22,
      "wrTP1": 45.5,
      "expR": -0.098,
      "pf": 0.8
    },
    "1m/RETEST/LONG": {
      "n": 1994,
      "wrTP1": 48.1,
      "expR": 0.103,
      "pf": 1.22
    },
    "1m/RETEST/SHORT": {
      "n": 974,
      "wrTP1": 42.7,
      "expR": 0.099,
      "pf": 1.21
    },
    "2m/INV/LONG": {
      "n": 14,
      "wrTP1": 64.3,
      "expR": 0.018,
      "pf": 1.07
    },
    "2m/INV/SHORT": {
      "n": 4,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 882,
      "wrTP1": 47.4,
      "expR": 0.056,
      "pf": 1.12
    },
    "2m/RETEST/SHORT": {
      "n": 373,
      "wrTP1": 44.5,
      "expR": 0.022,
      "pf": 1.05
    },
    "5m/INV/LONG": {
      "n": 6,
      "wrTP1": 16.7,
      "expR": -0.705,
      "pf": 0.06
    },
    "5m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 317,
      "wrTP1": 52.1,
      "expR": 0.174,
      "pf": 1.43
    },
    "5m/RETEST/SHORT": {
      "n": 177,
      "wrTP1": 42.4,
      "expR": 0.102,
      "pf": 1.21
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 12077,
  "brier": 0.2222,
  "bias": -0.085,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.185
    },
    {
      "feature": "stretchAtr",
      "weight": -0.082
    },
    {
      "feature": "nearTk",
      "weight": -0.071
    },
    {
      "feature": "rvol",
      "weight": 0.044
    },
    {
      "feature": "biasScore",
      "weight": -0.043
    },
    {
      "feature": "emaStack",
      "weight": 0.037
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.03
    },
    {
      "feature": "structDir",
      "weight": 0.028
    },
    {
      "feature": "aligned",
      "weight": -0.026
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.022
    },
    {
      "feature": "nearEdge",
      "weight": 0.016
    },
    {
      "feature": "hourNY",
      "weight": 0.006
    },
    {
      "feature": "chopIdx",
      "weight": -0.005
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.16,
      "actual": 0.176,
      "n": 1207
    },
    {
      "bin": 1,
      "pred": 0.357,
      "actual": 0.315,
      "n": 1208
    },
    {
      "bin": 2,
      "pred": 0.442,
      "actual": 0.358,
      "n": 1208
    },
    {
      "bin": 3,
      "pred": 0.49,
      "actual": 0.393,
      "n": 1207
    },
    {
      "bin": 4,
      "pred": 0.53,
      "actual": 0.531,
      "n": 1208
    },
    {
      "bin": 5,
      "pred": 0.561,
      "actual": 0.543,
      "n": 1208
    },
    {
      "bin": 6,
      "pred": 0.586,
      "actual": 0.602,
      "n": 1207
    },
    {
      "bin": 7,
      "pred": 0.608,
      "actual": 0.669,
      "n": 1208
    },
    {
      "bin": 8,
      "pred": 0.629,
      "actual": 0.692,
      "n": 1208
    },
    {
      "bin": 9,
      "pred": 0.66,
      "actual": 0.73,
      "n": 1208
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": false,
  "reason": "pocas semanas",
  "weeks": 3
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.011,
    "ci90": [
      -0.168,
      0.19
    ],
    "p_mean_le_0": 0.469,
    "n": 121,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.064,
    "ci90": [
      -0.135,
      0.27
    ],
    "p_mean_le_0": 0.29,
    "n": 92,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.053,
    "ci90": [
      0.023,
      0.082
    ],
    "p_mean_le_0": 0.003,
    "n": 4699,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.051,
    "ci90": [
      0.012,
      0.09
    ],
    "p_mean_le_0": 0.012,
    "n": 2941,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": -0.099,
    "ci90": [
      -0.315,
      0.136
    ],
    "p_mean_le_0": 0.746,
    "n": 38,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": -0.033,
    "ci90": [
      -0.365,
      0.361
    ],
    "p_mean_le_0": 0.574,
    "n": 41,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.018,
    "ci90": [
      -0.024,
      0.06
    ],
    "p_mean_le_0": 0.249,
    "n": 2099,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.074,
    "ci90": [
      0.018,
      0.132
    ],
    "p_mean_le_0": 0.015,
    "n": 1271,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.405,
    "ci90": [
      -0.011,
      0.813
    ],
    "p_mean_le_0": 0.056,
    "n": 14,
    "survives_fdr10": false
  },
  "5m/INV/SHORT": {
    "expR": 0.436,
    "ci90": [
      -0.218,
      1.126
    ],
    "p_mean_le_0": 0.138,
    "n": 9,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.154,
    "ci90": [
      0.082,
      0.232
    ],
    "p_mean_le_0": 0.001,
    "n": 745,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.081,
    "ci90": [
      -0.015,
      0.185
    ],
    "p_mean_le_0": 0.084,
    "n": 446,
    "survives_fdr10": false
  }
}
```

## Clusters de regimen
```json
{
  "ready": true,
  "k": 4,
  "clusters": [
    {
      "id": 0,
      "n": 3727,
      "wrTP1": 44.0,
      "expR": 0.076,
      "pf": 1.15,
      "defining_features": {
        "structDir": 0.97,
        "biasScore": 0.77,
        "emaStack": 0.73,
        "nearEdge": 0.7
      }
    },
    {
      "id": 2,
      "n": 4620,
      "wrTP1": 44.8,
      "expR": 0.064,
      "pf": 1.13,
      "defining_features": {
        "biasScore": -1.2,
        "emaStack": -1.0,
        "nearEdge": -0.92,
        "structDir": -0.43
      }
    },
    {
      "id": 1,
      "n": 2317,
      "wrTP1": 50.4,
      "expR": 0.044,
      "pf": 1.1,
      "defining_features": {
        "hourNY": 1.39,
        "atrPctUsed": -0.86,
        "emaStack": 0.54,
        "biasScore": 0.51
      }
    },
    {
      "id": 3,
      "n": 2431,
      "wrTP1": 48.2,
      "expR": 0.018,
      "pf": 1.04,
      "defining_features": {
        "structDir": -1.03,
        "biasScore": 0.61,
        "nearEdge": 0.49,
        "hourNY": -0.48
      }
    }
  ]
}
```

## Consistencia entre instrumentos
```json
{
  "1m/INV/LONG": {
    "symbols": {
      "CL": {
        "n": 29,
        "wrTP1": 58.6,
        "expR": 0.464
      },
      "YM": {
        "n": 49,
        "wrTP1": 34.7,
        "expR": 0.016
      },
      "ES": {
        "n": 19,
        "wrTP1": 52.6,
        "expR": -0.112
      },
      "GC": {
        "n": 21,
        "wrTP1": 23.8,
        "expR": -0.556
      },
      "NQ": {
        "n": 12,
        "wrTP1": 50.0,
        "expR": 0.099
      }
    },
    "expR_spread": 1.02,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 55,
        "wrTP1": 45.5,
        "expR": 0.044
      },
      "NQ": {
        "n": 10,
        "wrTP1": 50.0,
        "expR": 0.071
      },
      "ES": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.57
      },
      "GC": {
        "n": 19,
        "wrTP1": 57.9,
        "expR": 0.122
      },
      "CL": {
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.556
      }
    },
    "expR_spread": 1.126,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 890,
        "wrTP1": 43.4,
        "expR": 0.034
      },
      "NQ": {
        "n": 1042,
        "wrTP1": 48.3,
        "expR": 0.078
      },
      "ES": {
        "n": 1029,
        "wrTP1": 48.5,
        "expR": 0.092
      },
      "CL": {
        "n": 1217,
        "wrTP1": 45.0,
        "expR": 0.029
      },
      "YM": {
        "n": 671,
        "wrTP1": 41.7,
        "expR": 0.018
      }
    },
    "expR_spread": 0.074,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 415,
        "wrTP1": 41.7,
        "expR": 0.088
      },
      "GC": {
        "n": 769,
        "wrTP1": 45.3,
        "expR": 0.062
      },
      "YM": {
        "n": 991,
        "wrTP1": 45.2,
        "expR": 0.105
      },
      "ES": {
        "n": 677,
        "wrTP1": 44.5,
        "expR": 0.008
      },
      "CL": {
        "n": 271,
        "wrTP1": 38.4,
        "expR": -0.122
      }
    },
    "expR_spread": 0.227,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.272
      },
      "CL": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.137
      },
      "YM": {
        "n": 10,
        "wrTP1": 40.0,
        "expR": -0.314
      },
      "ES": {
        "n": 8,
        "wrTP1": 75.0,
        "expR": 0.297
      },
      "NQ": {
        "n": 10,
        "wrTP1": 50.0,
        "expR": -0.094
      }
    },
    "expR_spread": 0.611,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 21,
        "wrTP1": 33.3,
        "expR": 0.072
      },
      "NQ": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": 0.324
      },
      "ES": {
        "n": 5,
        "wrTP1": 40.0,
        "expR": -0.072
      },
      "GC": {
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.46
      }
    },
    "expR_spread": 0.784,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 497,
        "wrTP1": 50.1,
        "expR": 0.069
      },
      "GC": {
        "n": 343,
        "wrTP1": 46.4,
        "expR": 0.016
      },
      "CL": {
        "n": 562,
        "wrTP1": 47.9,
        "expR": 0.035
      },
      "ES": {
        "n": 463,
        "wrTP1": 49.7,
        "expR": 0.014
      },
      "YM": {
        "n": 321,
        "wrTP1": 38.6,
        "expR": -0.088
      }
    },
    "expR_spread": 0.157,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 275,
        "wrTP1": 49.8,
        "expR": 0.05
      },
      "YM": {
        "n": 467,
        "wrTP1": 50.3,
        "expR": 0.132
      },
      "GC": {
        "n": 291,
        "wrTP1": 46.7,
        "expR": 0.085
      },
      "NQ": {
        "n": 201,
        "wrTP1": 42.3,
        "expR": 0.075
      },
      "CL": {
        "n": 94,
        "wrTP1": 43.6,
        "expR": -0.168
      }
    },
    "expR_spread": 0.3,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": -0.058
      },
      "YM": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.617
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 1.517
      }
    },
    "expR_spread": 1.575,
    "verdict": "instrument-specific"
  },
  "5m/INV/SHORT": {
    "symbols": {
      "NQ": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.85
      },
      "YM": {
        "n": 3,
        "wrTP1": 0.0,
        "expR": -1.0
      }
    },
    "expR_spread": 1.85,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 75,
        "wrTP1": 57.3,
        "expR": 0.224
      },
      "ES": {
        "n": 169,
        "wrTP1": 55.6,
        "expR": 0.292
      },
      "YM": {
        "n": 117,
        "wrTP1": 49.6,
        "expR": 0.179
      },
      "CL": {
        "n": 173,
        "wrTP1": 57.2,
        "expR": 0.263
      },
      "NQ": {
        "n": 257,
        "wrTP1": 46.3,
        "expR": -0.042
      }
    },
    "expR_spread": 0.334,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 81,
        "wrTP1": 48.1,
        "expR": -0.017
      },
      "ES": {
        "n": 99,
        "wrTP1": 55.6,
        "expR": 0.118
      },
      "GC": {
        "n": 102,
        "wrTP1": 36.3,
        "expR": 0.018
      },
      "YM": {
        "n": 161,
        "wrTP1": 49.7,
        "expR": 0.172
      },
      "CL": {
        "n": 43,
        "wrTP1": 44.2,
        "expR": -0.0
      }
    },
    "expR_spread": 0.189,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 16,
  "near_news_30m": {
    "n": 494,
    "wrTP1": 52.8,
    "nSL": 178,
    "nTO": 55,
    "expR": 0.318,
    "pf": 1.8,
    "mfe_p25": 12.0,
    "mfe_p50": 27.0,
    "mfe_p75": 64.0,
    "winnerMAE_p75": 16.0,
    "winnerMAE_p90": 35.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -18.0,
    "revAfterSL_rate": 43.3
  },
  "away_from_news": {
    "n": 12601,
    "wrTP1": 45.9,
    "nSL": 5849,
    "nTO": 963,
    "expR": 0.046,
    "pf": 1.09,
    "mfe_p25": 7.0,
    "mfe_p50": 17.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.6
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 4,
  "scored": 0,
  "mae_deltaER": null,
  "hit_direction_rate": null
}
```

## Experimentos
```json
[
  {
    "id": "example-0000",
    "status": "template",
    "hypothesis": "Ejemplo. Subir sc_min_rr de 1.0 a 1.3 sube E[R] en 1m/RETEST porque elimina las señales con TP1 mas cerca que el SL.",
    "param": "sc_min_rr",
    "from": 1.0,
    "to": 1.3,
    "changeDate": null,
    "segment": {
      "tf": "1",
      "kind": "RETEST"
    },
    "targetMetric": "expR",
    "minAfterN": 40
  },
  {
    "id": "sl-retest-wick-2026-09-03",
    "status": "proposed",
    "hypothesis": "En RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. HASTA 2026-09-04 esto solo certificaba en SHORT (\"no aplica a largos\"); con la muestra de 2026-09-05 TAMBIEN certifica en 1m LONG, asi que se retira la exclusion dura de BUY RETEST y se deja como 'certifica por tf/side, no generalizar sin mirar la tabla'. 2026-09-06: mismas cifras exactas que 2026-09-05 (n identico) porque no llego dato nuevo. 2026-09-07 (lunes, primer dia con trades GENUINAMENTE nuevos post-restauracion, sin repeticion del bug de heal): retest_1m_long paso de n=1087 a n=1135 (+48 pares nuevos, no restaurados) y el delta se mantiene practicamente igual (0.181->0.183) con el CI90 todavia sin cruzar cero -- esta es la primera confirmacion independiente real que pedia el next_steps anterior. retest_1m_short tambien crecio con dato nuevo (n=219->229) y sigue certificando. 2026-09-08 (martes, primer dia habil COMPLETO post-feriado, salto grande de muestra real): retest_1m_long n=1135->1432 (delta 0.183->0.18, estable, segunda confirmacion independiente); retest_1m_short n=229->514 (delta 0.283->0.417, se hizo MAS fuerte); retest_2m_short CERTIFICA POR PRIMERA VEZ (n=129->260, CI90 dejo de cruzar cero); retest_5m_long CERTIFICA POR PRIMERA VEZ pero al filo (n=224->274, CI90=[0.005,0.36], limite inferior casi cero, vigilar que no se revierta con mas muestra); retest_2m_long sigue sin certificar y el delta bajo a casi cero (0.028->0.01, n=596->742).",
    "param": "sl_basis_retest",
    "from": "3-capas (sc_slbuf x ATR1m + piso sc_floor_atr5 + techo sc_cap_atr5 / sc_cap_adr)",
    "to": "mecha de la vela del retest (lg_slOrig con slBasis=retestBar / retestBar2, crudo)",
    "changeDate": null,
    "segment": {
      "kind": "RETEST"
    },
    "targetMetric": "expR",
    "minAfterN": 40,
    "evidence": {
      "source": "sl_origin_vs_layer.by_basis / by_tf_kind_side (medicion PARALELA: misma entrada y mismos TP, solo se mueve el stop; rMultiple = base 3-capas, rOrig = base mecha del retest). No requiere cambio en TradingView para medir.",
      "asOf": "2026-09-19 (sabado). Dato nuevo genuino, salto grande (el bus asento de una vez los outcomes/signals de 2026-09-18). Repo tuvo otra vez 'forced update' sobre origin/main (mismo patron de siempre, verificado como superset sin perdida). n de pares resueltos subio de 11452 a 13092.",
      "retest_1m_long": {
        "n": 4078,
        "deltaER_orig_minus_layer": 0.152,
        "ci90": [
          0.09,
          0.213
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 3410 a 4078, delta practicamente identico (0.145->0.152) -- duodecima confirmacion independiente, sigue siendo la lectura mas estable del experimento."
      },
      "retest_1m_short": {
        "n": 2432,
        "deltaER_orig_minus_layer": 0.153,
        "ci90": [
          0.063,
          0.244
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 2179 a 2432, delta practicamente identico (0.155->0.153) -- duodecima confirmacion, sigue estable."
      },
      "retest_2m_long": {
        "n": 1897,
        "deltaER_orig_minus_layer": 0.153,
        "ci90": [
          0.079,
          0.228
        ],
        "ci90_no_cruza_cero": true,
        "nota": "SEGUNDA lectura seguida certificando (se sumo ayer por primera vez tras 11 lecturas): n subio de 1599 a 1897, delta subio fuerte de 0.074 a 0.153 y el limite inferior del CI90 se aleja mucho mas de cero (0.005->0.079) -- se acerca a cumplir el criterio de '2-3 lecturas seguidas' para promoverlo a la propuesta formal; vigilar una tercera lectura antes de sumarlo."
      },
      "retest_2m_short": {
        "n": 1092,
        "deltaER_orig_minus_layer": 0.134,
        "ci90": [
          0.039,
          0.234
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 984 a 1092, delta sube (0.123->0.134) y el limite inferior del CI90 sigue alejandose de cero (0.031->0.039) -- mejor lectura hasta ahora de este candidato, se mantiene un dia mas antes de promoverlo."
      },
      "retest_5m_long": {
        "n": 713,
        "deltaER_orig_minus_layer": 0.276,
        "ci90": [
          0.111,
          0.466
        ],
        "ci90_no_cruza_cero": true,
        "nota": "NOVENA LECTURA SEGUIDA CERTIFICANDO: n subio de 622 a 713, delta baja de 0.312 a 0.276 pero sigue muy lejos de cero -- sigue sin retroceso desde que se incluyo en la propuesta de la revision semanal."
      },
      "retest_5m_short": {
        "n": 408,
        "deltaER_orig_minus_layer": 0.49,
        "ci90": [
          0.142,
          0.909
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 369 a 408, delta baja un poco (0.546->0.49) pero sigue siendo la lectura mas solida del experimento por margen."
      },
      "overall_by_basis_retestBar": {
        "n": 8313,
        "deltaER": 0.178,
        "ci90": [
          0.136,
          0.223
        ],
        "nota": "n subio de 7109 a 8313, delta sube (0.163->0.178) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba."
      }
    },
    "next_steps": [
      "2026-09-05: se recupero signals/2026-09-03.jsonl (ver nota de la corrida en state.json/narrative y en el historico de los playbooks) -- estaba truncado de 1280 a 24 lineas por un commit 'heal' que en realidad BORRO datos en vez de repararlos.",
      "2026-09-06: EL MISMO BUG SE REPITIO -- un segundo commit 'heal 24 orphan signal(s) 2026-09-03' (0cf0a30, autor jesusreyna2016, ts commit 2026-09-04 20:31 -0500) volvio a truncar signals/2026-09-03.jsonl de 1280 a 24 lineas, DESPUES de que el agente ya lo habia arreglado el dia anterior (commit 945c337). Se restauro de nuevo desde 945c337. Se anadio una guarda permanente en analyze.py (file_integrity_check: compara lineas de cada signals/outcomes/*.jsonl contra el maximo visto en corridas previas via state.json.file_line_counts, y alerta si algun archivo ENCOGIO). Jesus debe revisar/desactivar el job externo de 'heal' de huerfanos -- esta confundiendo señales legitimas con duplicados y borrando datos reales dos veces en 3 dias.",
      "2026-09-07 (lunes): PRIMER DIA SIN REPETICION DEL BUG -- file_line_counts confirma que ningun signals/outcomes/*.jsonl encogio; todos los archivos crecieron o se mantuvieron. La guarda de analyze.py sigue activa por si vuelve a pasar. Llego dato genuinamente nuevo (38 signals, 44 outcomes de 2026-09-07 + 69/62 de 2026-09-06 que no estaban contados en la corrida anterior) -- retest_1m_long y retest_1m_short subieron de n con delta estable, primera confirmacion independiente real (ver evidence arriba).",
      "2026-09-08 (martes): SEGUNDO DIA SIN REPETICION DEL BUG, salto grande de dato genuinamente nuevo (primer dia habil completo post-feriado). retest_1m_long/short mejoran o se mantienen (segunda confirmacion independiente); retest_2m_short y retest_5m_long CERTIFICAN POR PRIMERA VEZ (este ultimo al filo del cero, tratar como debil). Nota de metodo importante: en el mismo dia, segment_significance de 2m/RETEST (ambos lados) REVIRTIO su certificacion negativa de ayer al cruzar el CI90 de nuevo por cero con mas muestra -- prueba de que hay que seguir siendo conservador incluso con lecturas que 'parecian asentadas' con n mediano (cientos, no miles). Aplicar el mismo escepticismo a las certificaciones nuevas de hoy (2m short, 5m long) hasta que se sostengan 2-3 corridas mas.",
      "Revision semanal del domingo: confirmar sobre walk-forward + segment_significance (FDR 10%), no solo in-sample (walk_forward todavia no esta listo, solo 2 semanas de datos).",
      "Anadir linea a predictions.jsonl con predictedDeltaER antes de aplicar.",
      "Cuando se confirme con datos nuevos genuinos (no solo restaurados) durante varios dias mas y walk-forward este listo: cambio en Pine = para RETEST usar lg_slOrig (mecha de la vela del retest) como SL de trabajo en 1m (long y short) y 5m/2m SHORT; en 2m LONG y 5m LONG esperar mas confirmacion (5m LONG certifica pero al filo). Poner changeDate el dia que se aplique en los 12 graficos.",
      "Vigilar: retestBar2 (1m SHORT = mecha vela retest + vela previa) sigue siendo una fraccion chica de la muestra 1m short -- puede mover el numero cuando crezca.",
      "2026-09-10 (jueves): salto grande de dato nuevo (bus asento signals/outcomes/2026-09-08.jsonl completos, +1203 pares en todo el dataset). Patron de metodo importante que se repite: 1m SHORT paso de un delta que parecia muy fuerte (n=514, delta=0.417) a uno mas moderado pero todavia solido (n=898, delta=0.181) -- confirma otra vez que las lecturas con n en los cientos bajos pueden sobrestimar el efecto, tratar el numero mas reciente (mayor n) como el mas representativo, no promediar con lecturas viejas de n mas chico. 5m LONG PERDIO la certificacion 'al filo' de ayer (CI90 volvio a cruzar cero) -- se cumplio la advertencia de tratarlo como debil; sacarlo de cualquier propuesta hasta que vuelva a certificar sostenido. 2m SHORT tambien se debilito (certifica al filo, limite inferior del CI90 en 0.001). El unico segmento que se fortalecio con mas confianza fue 1m LONG (tercera confirmacion, delta estable) y 5m SHORT (sigue siendo el efecto mas grande, con margen). Vista global: SOLO 1m LONG, 1m SHORT y 5m SHORT siguen siendo candidatos solidos para la propuesta de la revision semanal del domingo 2026-09-13; 2m SHORT es candidato debil; 2m LONG y 5m LONG quedan fuera por ahora.",
      "2026-09-11 (viernes): incidente de repo (origin/main reescrito rio arriba, sin ancestro comun con la rama local; verificado como superset sin perdida de datos, resuelto con git reset --hard origin/main -- ver playbooks para el detalle). Dato nuevo genuino post-reset. Vista actualizada de candidatos: 1m LONG sigue solido (cuarta confirmacion, delta 0.163); 1m SHORT certifica pero a un paso de perder la certificacion (limite inferior del CI90 bajo a 0.003, vigilar de cerca); 5m SHORT sigue siendo el efecto mas grande y ahora la lectura mas solida (CI90 se estrecho); 5m LONG RECUPERA la certificacion que habia perdido ayer (tercer vaiven en 3 dias, seguir tratando como inestable). 2m SHORT PIERDE la certificacion 'al filo' de ayer (CI90 volvio a cruzar cero) -- se une a 2m LONG como no-candidato. Vista para la revision semanal del domingo 2026-09-13: candidatos solidos = 1m LONG y 5m SHORT; candidato debil/al filo = 1m SHORT; inestable (no incluir todavia) = 5m LONG; fuera = 2m LONG y 2m SHORT.",
      "2026-09-12 (sabado, ultima corrida antes de la revision semanal de manana domingo 2026-09-13): dato nuevo genuino sin incidentes de repo (+713 pares). Dos movimientos favorables: 1m SHORT deja de estar 'al filo' -- el limite inferior de su CI90 subio de 0.003 a 0.022, ya no es el candidato mas fragil de los tres solidos. Y sobre todo: **5m LONG certifica por SEGUNDA lectura seguida** (09-11 y hoy, delta 0.154->0.187, CI90 cada vez mas lejos de cero) -- es la primera vez que cumple la barra de '2 lecturas seguidas del mismo lado' que el propio experimento se puso el 09-08 tras tres vaivenes en 3 dias; pasa de 'inestable, no incluir' a candidato EXPERIMENTAL para la propuesta de manana, con la advertencia explicita de su historial volatil (no tratarlo al mismo nivel de confianza que 1m LONG/SHORT o 5m SHORT hasta una tercera lectura). 1m LONG (quinta confirmacion) y 5m SHORT (sigue siendo el efecto mas grande, CI90 mas angosto) se mantienen como los dos candidatos mas solidos sin cambios de fondo. 2m LONG (sexta lectura sin certificar) sigue fuera; 2m SHORT sigue sin certificar pero ahora es el no-candidato mas cerca de cero (limite inferior del CI90 = -0.001). PARA LA REVISION SEMANAL DE MANANA: candidatos solidos = 1m LONG, 1m SHORT (ya no al filo), 5m SHORT; candidato experimental (2 lecturas, vigilar una tercera) = 5m LONG; fuera = 2m LONG y 2m SHORT (este ultimo el mas cerca de flipear, seguir vigilando aunque no se proponga todavia).",
      "2026-09-13 (domingo, REVISION SEMANAL): dato nuevo genuino (+719 pares, sin incidentes de perdida real -- ver nota de proceso en `asOf`, hubo un `git pull` con 'forced update' al iniciar la corrida por una reescritura upstream de `origin/main`, verificada como superset y resuelta sin perder trabajo local). **5m LONG cumple hoy su TERCERA lectura seguida certificando** (delta 0.187->0.255, CI90 cada vez mas lejos de cero) -- se gradua de 'candidato experimental' a candidato SOLIDO, aunque se mantiene la nota de historial volatil (3 vaivenes entre 09-08 y 09-11) como diferencia frente a 1m LONG (sexta confirmacion sin un solo vaiven en su historia). DECISION DE LA REVISION SEMANAL: se propone formalmente a Jesus aplicar el cambio de SL en `scalp_command.pine` (usar `lg_slOrig`/mecha del retest en vez del stop de 3 capas) en los 4 segmentos que certifican de forma estable con n>=20 post-cambio exigido: **1m LONG, 1m SHORT, 5m LONG, 5m SHORT**. 2m LONG y 2m SHORT quedan explicitamente fuera de la propuesta (septima y octava lectura sin certificar de forma estable). Se anadieron 4 lineas a `predictions.jsonl` (una por segmento, `predictedDeltaER` = delta medido hoy) para poder puntuar el acierto una vez Jesus aplique el cambio y se junte muestra post-cambio (afterN>=40, marcar `experimental` hasta 40+ muestras y 2 semanas consecutivas en la misma direccion, per agent-instructions.md). Ver `reviews/2026-week-37.md` para el detalle completo de la revision. Status del experimento se mantiene en `proposed` (no aplicado todavia en TradingView, `changeDate` sigue null) -- pasara a medirse antes/despues (y potencialmente a `confirmed`) recien cuando Jesus ponga fecha de cambio en los graficos.",
      "2026-09-14 (lunes, primer dia habil tras la revision semanal): dato nuevo minimo (+96 pares en todo el dataset, reapertura de Globex del domingo). **Los 4 segmentos propuestos ayer (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen todos con `delta_beats_zero=true` sin ningun retroceso** -- primer dia de confirmacion post-propuesta, deltas practicamente identicos a ayer en los cuatro. 5m LONG suma su CUARTA lectura seguida certificando. 2m LONG y 2m SHORT siguen fuera (octava y novena lectura sin certificar). Sin cambios a la propuesta: sigue en estado `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView.",
      "2026-09-15 (martes, primer dia habil despues de la reapertura de Globex del domingo, dato genuino): los 4 segmentos propuestos en la revision semanal del 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG suma su octava confirmacion, 1m SHORT y 5m SHORT se mantienen estables, 5m LONG suma su QUINTA lectura seguida certificando (ya el doble del umbral de '2 lecturas seguidas' que se puso el propio experimento el 09-08). Movimiento notable: 2m SHORT se fortalecio (delta 0.093->0.117, CI90 ya no cruza cero) pero su limite inferior (0.014) sigue demasiado pegado a cero para promoverlo -- se mantiene como candidato debil/al filo, fuera de la propuesta hasta una segunda lectura consecutiva lejos de cero. 2m LONG sigue sin certificar (novena lectura). Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView. Nota de mantenimiento (no de dato): se corrigio hoy un bug de analyze.py que hacia que la alerta MUESTRA de 2026-W36/W37 (caida de n ya explicada por dedup, sin perdida de archivo real) se repitiera identica cada corrida para siempre en vez de solo mientras la cifra siguiera empeorando; el efecto se vera desde la proxima corrida.",
      "2026-09-16 (miercoles, dato nuevo genuino, +284 pares resueltos en todo el bus): los 4 segmentos propuestos el 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con `delta_beats_zero=true` y sin ningun retroceso -- 1m LONG suma su NOVENA confirmacion, 1m SHORT y 5m SHORT estables, **5m LONG suma su SEXTA lectura seguida certificando**. 2m SHORT se mantiene exactamente igual (delta 0.117, limite inferior del CI90 baja un poco de 0.014 a 0.011 -- sigue candidato debil/al filo, todavia sin una segunda lectura clara lejos de cero). 2m LONG sigue sin certificar, decima lectura seguida (delta 0.035, CI90 cruza cero). Sin cambios de estado: sigue `proposed`, `changeDate` null. La escalera de ejecucion sigue bloqueada en el peldano 0 (asesor) porque, aun con `gate.readyForLive=true` en 5m/RETEST/LONG (n>=100, E[R]>0, PF>=1.3, WR>=50), este mismo experimento -- la causa de SL dominante en RETEST -- sigue sin un `changeDate` ni muestra post-cambio; ese es exactamente el requisito que falta segun `execution-ladder.md` peldano 2. Nada accionable nuevo para Jesus hoy mas alla de: si va a aplicar el cambio de SL estructural en los 12 graficos, este es el dia con la evidencia mas solida acumulada hasta ahora (6 confirmaciones seguidas en el candidato mas fragil, 5m LONG).",
      "2026-09-17 (jueves, dato nuevo genuino, +1097 pares resueltos en todo el bus, el salto mas grande en varios dias): los 4 segmentos propuestos el 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con `delta_beats_zero=true` y sin ningun retroceso -- 1m LONG suma su DECIMA confirmacion (n=2737->3095, delta 0.15->0.142, CI90 [0.066,0.218]), 1m SHORT sube (n=1971->2085, delta 0.127->0.143, CI90 [0.046,0.247]), 5m LONG suma su SEPTIMA lectura seguida certificando (n=492->555, delta 0.248->0.218, CI90 [0.05,0.403]) y 5m SHORT sigue siendo el efecto mas grande, con margen (n=309->324, delta 0.554->0.514, CI90 [0.133,0.987]). 2m SHORT se mantiene candidato debil/al filo por otra corrida mas (n=895->939, delta 0.117->0.113, limite inferior del CI90 practicamente igual, 0.011 vs 0.012). 2m LONG sigue sin certificar, undecima lectura seguida (n=1327->1477, delta 0.035->0.05, CI90 [-0.018,0.12] -- el delta sube y el limite inferior se acerca a cero, vigilar si se acerca a certificar en las proximas corridas). Nota de gate: la semana ya cerrada 2026-W37 en el segmento 5m/RETEST/LONG (el segmento objetivo del gate de ejecucion) paso de PF=1.44 a PF=1.45 pero perdio 6 pares de muestra por el mismo mecanismo de dedup que ya afectaba los conteos agregados (n=241->235) -- primera vez que se ve este efecto a nivel de segmento individual, sin evidencia de perdida real de archivo (file_integrity_check limpio). Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView. Hallazgo nuevo en paralelo (no de este experimento): por primera vez el veredicto SA=GO certifica con significancia junto a SA=WAIT en el cruce agregado con Session Analyst (ver report.alerts); y en el desglose por kind/side, la rama AVOID de RETEST/LONG cruza a E[R] negativo por primera vez mientras la rama WAIT de RETEST/SHORT cruza a positivo -- ver playbooks para el detalle por lado.",
      "2026-09-18 (viernes): HEAD quedo detached tras el `git pull` porque `origin/main` fue reescrito rio arriba (historia sin ancestro comun con la rama local, primera vez que pasa desde 09-11) -- verificado que el commit remoto contenia todo el trabajo esperado (mismo tip de datos, ultimos 50 commits del bus) antes de resolver con `checkout -B main origin/main`, sin perdida. Dato nuevo genuino grande (+768 pares en todo el dataset). **HALLAZGO PRINCIPAL: retest_2m_long CERTIFICA POR PRIMERA VEZ** tras 11 lecturas seguidas sin lograrlo (delta 0.05->0.074, CI90 [-0.018,0.12]->[0.005,0.145], limite inferior cruza por encima de cero) -- se trata como candidato nuevo y fragil, no se suma todavia a la propuesta formal (mismo criterio de '2-3 lecturas seguidas' que se aplico a 5m LONG en la semana pasada). Los 4 segmentos ya propuestos (1m LONG/SHORT, 5m LONG/SHORT) se mantienen TODOS con `delta_beats_zero=true` y se fortalecen: 1m LONG suma su UNDECIMA confirmacion, 1m SHORT sube de delta 0.143 a 0.155, 5m LONG suma su OCTAVA lectura seguida con un salto notable (0.218->0.312), 5m SHORT estable como el efecto mas grande. 2m SHORT tiene su mejor lectura hasta ahora (limite inferior del CI90 0.011->0.031) pero se mantiene un dia mas como candidato debil antes de promoverlo. Nota de gate: en el segmento objetivo (5m/RETEST/LONG), la semana ya cerrada 2026-W36 volvio a perder 1 par por dedup (n=242, PF=1.18, sigue <1.3) y 2026-W37 tambien perdio 1 par (n=234, pero PF SUBIO a 1.47) -- el dedup a nivel de segmento sigue siendo benigno (sin evidencia de perdida real de archivo) pero ya van 3 corridas seguidas afectando este segmento especifico, vigilar que no erosione la serie. Sin cambios de estado en el experimento: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView -- con 4 segmentos solidos (2 de ellos en su octava/undecima confirmacion sin un solo retroceso desde el 09-13) mas un quinto candidato nuevo (2m LONG), esta es la evidencia acumulada mas fuerte hasta ahora para aplicar el cambio.",
      "2026-09-19 (sabado): salto de dato grande, el mayor en varios dias (n 11452->13092, +1640; el bus asento de una vez los archivos de 2026-09-18, mismo 'forced update' inofensivo de origin/main de siempre). Los 4 segmentos ya propuestos el 09-13 (1m LONG/SHORT, 5m LONG/SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG y 1m SHORT suman su DUODECIMA confirmacion (ambos practicamente sin cambio de delta), 5m LONG su NOVENA lectura seguida (delta baja un poco, 0.312->0.276, sigue muy lejos de cero) y 5m SHORT sigue siendo el efecto mas grande. HALLAZGO DEL DIA: 2m LONG suma su SEGUNDA lectura seguida certificando y se fortalece mucho (delta 0.074->0.153, CI90 limite inferior 0.005->0.079) -- un paso mas cerca de cumplir el criterio de '2-3 lecturas' para sumarse a la propuesta formal (vigilar una tercera lectura). 2m SHORT tiene su mejor lectura hasta ahora (limite inferior del CI90 0.031->0.039) pero se mantiene un dia mas como candidato debil antes de promoverlo. Vista actualizada: candidatos solidos sin cambio = 1m LONG, 1m SHORT, 5m LONG, 5m SHORT (los 4 ya propuestos); candidato experimental en camino de promocion = 2m LONG (segunda lectura, falta una tercera); candidato debil/al filo = 2m SHORT. Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView -- con 4 segmentos solidos y un quinto candidato acercandose (2m LONG en su segunda confirmacion), esta sigue siendo la evidencia mas fuerte acumulada hasta ahora para aplicar el cambio."
    ],
    "beforeN": 12763,
    "afterN": 0,
    "before": {
      "n": 12763,
      "wrTP1": 46.2,
      "nSL": 5880,
      "nTO": 985,
      "expR": 0.056,
      "pf": 1.12,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 33.1
    },
    "after": {
      "n": 0
    }
  }
]
```

## Session Analyst
```json
{
  "available": true,
  "latest_plan": {
    "date": "2026-09-18",
    "session": "ny",
    "runType": "pre-ny",
    "generatedAt": "2026-09-18T08:02:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "GC",
    "focus": {
      "sym": "GC",
      "verdict": "GO",
      "window": "08:30-11:00 CT",
      "setup": {
        "es": "A+ reclaim de VWAP/EMA20 con TDO ya defendido y reclamado 4397.6-4408.5, confluencia 8",
        "en": "A+ VWAP/EMA20 reclaim with TDO already defended and reclaimed 4397.6-4408.5, confluence 8"
      },
      "trigger": {
        "es": "cierre de 5m sobre 4408.5 tras defender el retroceso a TDO 4397.6 (ya reclamado según el registro de toques), con la síntesis dando permiso de largo",
        "en": "a 5m close above 4408.5 after defending the pullback to TDO 4397.6 (already reclaimed per the touch log), with the fused voice granting long permission"
      },
      "invalid": {
        "es": "cierre de 5m sostenido bajo 4393.5",
        "en": "a sustained 5m close below 4393.5"
      },
      "note": {
        "es": "la síntesis vuelve a marcar largo con permiso tras dos rebotes limpios en 24h; si ya perdiste el primer test, no promedies ni subas tamaño solo porque el nivel se ve bonito",
        "en": "the fused voice is back to marking a long with permission after two clean bounces in 24h; if you already missed the first test, don't average in or size up just because the level looks good"
      }
    },
    "alarm": {
      "es": "la precisión de 20 días sigue floja: acierto de sesgo de ES en 43% y hit-rate del escenario A por debajo de 30% en NQ, ES y GC — trata las llamadas de convicción de hoy con descuento",
      "en": "the 20-day precision is still weak: ES's bias hit rate sits at 43% and scenario-A hit rate is below 30% in NQ, ES and GC — discount today's high-conviction calls accordingly"
    },
    "dataHealth": {
      "snapshot": "OK",
      "builtAtAgeMin": 14,
      "stale": [],
      "missing": [],
      "notes": {
        "es": "el snapshot llegó a tiempo (14 min). Las 2 fuentes que llevaban muertas en la corrida anterior ya volvieron: la síntesis del sesgo de NQ (63h caída) y las lecturas de tendencia de ES (15h caída) están frescas otra vez. Las 6 fuentes de los 5 instrumentos están sanas.",
        "en": "the snapshot arrived on time (14 min). The 2 sources that were dead last run are back: NQ's fused bias voice (63h down) and ES's trend reads (15h down) are fresh again. All 6 sources across the 5 instruments are healthy."
      }
    },
    "calendarContext": {
      "tags": [
        "triple-witching",
        "opex"
      ],
      "note": {
        "es": "hoy es el tercer viernes de septiembre: triple vencimiento trimestral de opciones y futuros. Efecto aplicado: rango esperado ensanchado un 12% en los tres índices, más mechas y menos fiabilidad de la dirección intradía. No hay FOMC ni NFP hoy.",
        "en": "today is the third Friday of September: quarterly triple witching for options and futu
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 5328,
  "by_verdict": {
    "AVOID": {
      "n": 1419,
      "wrTP1": 45.3,
      "nSL": 703,
      "nTO": 73,
      "expR": 0.009,
      "pf": 1.02,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 31.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 34.0
    },
    "GO": {
      "n": 678,
      "wrTP1": 50.9,
      "nSL": 280,
      "nTO": 53,
      "expR": 0.103,
      "pf": 1.23,
      "mfe_p25": 10.0,
      "mfe_p50": 25.0,
      "mfe_p75": 52.0,
      "winnerMAE_p75": 18.0,
      "winnerMAE_p90": 32.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 37.1
    },
    "WAIT": {
      "n": 3231,
      "wrTP1": 47.9,
      "nSL": 1423,
      "nTO": 259,
      "expR": 0.078,
      "pf": 1.17,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 36.3
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.009,
      "ci90": [
        -0.048,
        0.065
      ],
      "p_mean_le_0": 0.396,
      "n": 1373
    },
    "GO": {
      "expR": 0.103,
      "ci90": [
        0.028,
        0.181
      ],
      "p_mean_le_0": 0.011,
      "n": 639
    },
    "WAIT": {
      "expR": 0.078,
      "ci90": [
        0.043,
        0.113
      ],
      "p_mean_le_0": 0.0,
      "n": 3064
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1419,
      "wrTP1": 45.3,
      "nSL": 703,
      "nTO": 73,
      "expR": 0.009,
      "pf": 1.02,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 31.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 34.0
    },
    "GO_or_WAIT": {
      "n": 3909,
      "wrTP1": 48.5,
      "nSL": 1703,
      "nTO": 312,
      "expR": 0.082,
      "pf": 1.18,
      "mfe_p25": 8.0,
      "mfe_p50": 20.0,
      "mfe_p75": 45.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 36.4
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.009,
      "ci90": [
        -0.048,
        0.065
      ],
      "p_mean_le_0": 0.396,
      "n": 1373
    },
    "GO_or_WAIT": {
      "expR": 0.082,
      "ci90": [
        0.05,
        0.114
      ],
      "p_mean_le_0": 0.0,
      "n": 3703
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 13,
        "wrTP1": 53.8,
        "nSL": 5,
        "nTO": 1,
        "expR": -0.028,
        "pf": 0.93,
        "mfe_p25": 5.0,
        "mfe_p50": 6.0,
        "mfe_p75": 29.0,
        "winnerMAE_p75": 0.0,
        "winnerMAE_p90": 1.6000000000000014,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 40.0
      },
      "GO": {
        "n": 10,
        "wrTP1": 50.0,
        "nSL": 4,
        "nTO": 1,
        "expR": -0.126,
        "pf": 0.72,
        "mfe_p25": 17.0,
        "mfe_p50": 24.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 28.400000000000002,
        "loserMFEbeforeSL_p50": 9.5,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.5,
        "entryZoneTk_p50": -54.0,
        "revAfterSL_rate": 25.0
      },
      "WAIT": {
        "n": 47,
        "wrTP1": 40.4,
        "nSL": 24,
        "nTO": 4,
        "expR": -0.216,
        "pf": 0.6,
        "mfe_p25": 7.75,
        "mfe_p50": 17.5,
        "mfe_p75": 36.25,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 26.599999999999994,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 20.8
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 23,
        "wrTP1": 34.8,
        "nSL": 13,
        "nTO": 2,
        "expR": -0.333,
        "pf": 0.44,
        "mfe_p25": 6.5,
        "mfe_p50": 13.5,
        "mfe_p75": 21.75,
        "winnerMAE_p75": 4.5,
        "winnerMAE_p90": 6.8999999999999995,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 15.4
      },
      "WAIT": {
        "n": 31,
        "wrTP1": 45.2,
        "nSL": 15,
        "nTO": 2,
        "expR": -0.183,
        "pf": 0.63,
        "mfe_p25": 10.0,
        "mfe_p50": 20.0,
        "mfe_p75": 38.75,
        "winnerMAE_p75": 19.75,
        "winnerMAE_p90": 71.70000000000002,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 8.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 40.0
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 820,
        "wrTP1": 46.7,
        "nSL": 408,
        "nTO": 29,
        "expR": -0.01,
        "pf": 0.98,
        "mfe_p25": 6.0,
        "mfe_p50": 14.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 30.9
      },
      "GO": {
        "n": 469,
        "wrTP1": 49.9,
        "nSL": 206,
        "nTO": 29,
        "expR": 0.055,
        "pf": 1.12,
        "mfe_p25": 9.0,
        "mfe_p50": 24.0,
        "mfe_p75": 50.25,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 31.700000000000017,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 37.4
      },
      "WAIT": {
        "n": 1950,
        "wrTP1": 50.2,
        "nSL": 824,
        "nTO": 147,
        "expR": 0.14,
        "pf": 1.32,
        "mfe_p25": 7.0,
        "mfe_p50": 19.0,
        "mfe_p75": 44.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 37.6
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 563,
        "wrTP1": 43.5,
        "nSL": 277,
        "nTO": 41,
        "expR": 0.053,
        "pf": 1.1,
        "mfe_p25": 8.0,
        "mfe_p50": 16.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 39.4
      },
      "GO": {
        "n": 197,
        "wrTP1": 53.3,
        "nSL": 69,
        "nTO": 23,
        "expR": 0.224,
        "pf": 1.58,
        "mfe_p25": 12.75,
        "mfe_p50": 26.5,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 30.800000000000026,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 37.7
      },
      "WAIT": {
        "n": 1203,
        "wrTP1": 44.6,
        "nSL": 560,
        "nTO": 106,
        "expR": -0.009,
        "pf": 0.98,
        "mfe_p25": 9.0,
        "mfe_p50": 19.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 34.8
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```
