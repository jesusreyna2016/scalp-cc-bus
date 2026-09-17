# Scalp CC · report 2026-09-17T01:14Z
- signals=10714 outcomes=10179 pares_resueltos=10684 pendientes=30 huerfanos=26

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: by_kindside_aligned/RETEST/LONG|aligned=0 bajo de n=10 a n=9 desde la corrida previa (agregado, no archivo crudo -- revisar deduplicacion/re-pareo).
- MUESTRA: semana ya cerrada 2026-W36 bajo de n=3183 a n=3135 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W37 bajo de n=5389 a n=5338 desde la corrida previa -- vigilar, puede ser deduplicacion.
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.199 vs 0.055, delta 0.144 CI90 [0.094, 0.191], n 6518). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.214 vs 0.078, delta 0.136 CI90 [0.037, 0.24], n 1957). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.158 CI90 [0.073, 0.242], n 533). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.109 CI90 [0.069, 0.15], n 2204). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.053, "ci90": [0.034, 0.074], "p_mean_le_0": 0.0, "n": 10153}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 110 | 45.5 | 0.107 | 1.23 | 46 | 13.0 | 10.75 | 21.7 |
| 1m/INV/SHORT | 84 | 50.0 | 0.096 | 1.22 | 36 | 21.0 | 11.0 | 19.4 |
| 1m/RETEST/LONG | 3750 | 44.6 | 0.032 | 1.07 | 1780 | 13.0 | 9.0 | 29.1 |
| 1m/RETEST/SHORT | 2722 | 44.5 | 0.059 | 1.12 | 1233 | 18.0 | 12.0 | 32.6 |
| 2m/INV/LONG | 33 | 48.5 | -0.111 | 0.76 | 14 | 10.0 | 8.25 | 28.6 |
| 2m/INV/SHORT | 39 | 35.9 | 0.017 | 1.03 | 21 | 21.0 | 15.75 | 38.1 |
| 2m/RETEST/LONG | 1730 | 46.5 | 0.01 | 1.02 | 805 | 16.0 | 13.0 | 36.6 |
| 2m/RETEST/SHORT | 1171 | 48.6 | 0.094 | 1.2 | 511 | 22.0 | 13.0 | 41.5 |
| 5m/INV/LONG | 14 | 71.4 | 0.639 | 8.67 | 1 | 30.0 | 31.25 | 0.0 |
| 5m/INV/SHORT | 8 | 75.0 | 0.615 | 3.46 | 2 | 58.0 | 68.75 | 100.0 |
| 5m/RETEST/LONG | 622 | 51.0 | 0.153 | 1.35 | 257 | 25.0 | 19.0 | 49.0 |
| 5m/RETEST/SHORT | 401 | 48.4 | 0.096 | 1.21 | 162 | 31.0 | 23.0 | 38.3 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 745 | 25.8 | 0.123 | 1.19 | 447 | 28.5 | 15.0 | 19.9 |
| B | 4483 | 46.9 | 0.064 | 1.14 | 2010 | 17.0 | 12.0 | 33.7 |
| C | 5456 | 47.9 | 0.035 | 1.08 | 2411 | 16.0 | 12.0 | 36.5 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 4109 | 49.5 | 0.073 | 1.16 | 1835 | 13.0 | 9.0 | 39.2 |
| London | 1695 | 46.1 | -0.007 | 0.99 | 834 | 18.0 | 12.0 | 34.2 |
| NY | 1822 | 44.5 | 0.178 | 1.39 | 747 | 25.0 | 16.0 | 38.3 |
| Sin KZ | 3058 | 41.8 | -0.009 | 0.98 | 1452 | 18.0 | 13.0 | 24.5 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 2627 | 45.3 | 0.058 | 1.12 | 1187 | 21.0 | 14.0 | 32.9 |
| edge=0 | 4733 | 47.8 | 0.04 | 1.08 | 2123 | 14.0 | 10.0 | 38.2 |
| edge=1 | 3324 | 43.7 | 0.069 | 1.14 | 1558 | 17.0 | 14.0 | 28.5 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 10675 | 45.9 | 0.053 | 1.11 | 4867 | 17.0 | 12.0 | 33.8 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 68 | 54.4 | 0.154 | 1.39 | 24 | 10.5 | 10.0 | 29.2 |
| INV/LONG|edge=1 | 85 | 43.5 | 0.047 | 1.1 | 35 | 20.0 | 17.0 | 17.1 |
| INV/SHORT|edge=-1 | 76 | 40.8 | 0.099 | 1.2 | 37 | 22.0 | 12.0 | 27.0 |
| INV/SHORT|edge=0 | 47 | 53.2 | -0.028 | 0.94 | 20 | 13.0 | 17.0 | 35.0 |
| INV/SHORT|edge=1 | 8 | 75.0 | 0.901 | 4.6 | 2 | 32.5 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 266 | 54.1 | 0.18 | 1.44 | 105 | 12.0 | 7.25 | 49.5 |
| RETEST/LONG|edge=0 | 2737 | 47.9 | -0.009 | 0.98 | 1271 | 13.0 | 10.0 | 37.8 |
| RETEST/LONG|edge=1 | 3099 | 43.2 | 0.068 | 1.14 | 1466 | 17.0 | 13.0 | 27.8 |
| RETEST/SHORT|edge=-1 | 2281 | 44.4 | 0.041 | 1.08 | 1043 | 22.0 | 15.0 | 31.4 |
| RETEST/SHORT|edge=0 | 1881 | 47.3 | 0.11 | 1.24 | 808 | 17.0 | 10.0 | 39.4 |
| RETEST/SHORT|edge=1 | 132 | 54.5 | 0.065 | 1.15 | 55 | 14.0 | 10.0 | 56.4 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 39 | 38.5 | -0.051 | 0.9 | 19 | 14.0 | 15.5 | 15.8 |
| INV/LONG|tier=C | 118 | 51.7 | 0.158 | 1.4 | 42 | 14.0 | 12.0 | 26.2 |
| INV/SHORT|tier=B | 39 | 46.2 | 0.096 | 1.2 | 19 | 19.0 | 8.75 | 10.5 |
| INV/SHORT|tier=C | 92 | 47.8 | 0.108 | 1.24 | 40 | 25.0 | 28.0 | 37.5 |
| RETEST/LONG|tier=A+ | 453 | 25.4 | 0.114 | 1.18 | 275 | 23.0 | 13.5 | 18.5 |
| RETEST/LONG|tier=B | 2554 | 46.5 | 0.08 | 1.17 | 1155 | 15.0 | 11.0 | 32.6 |
| RETEST/LONG|tier=C | 3095 | 48.2 | -0.007 | 0.99 | 1412 | 14.0 | 11.0 | 36.2 |
| RETEST/SHORT|tier=A+ | 292 | 26.4 | 0.138 | 1.21 | 172 | 37.0 | 17.0 | 22.1 |
| RETEST/SHORT|tier=B | 1851 | 47.6 | 0.045 | 1.09 | 817 | 19.0 | 14.0 | 36.2 |
| RETEST/SHORT|tier=C | 2151 | 47.2 | 0.087 | 1.19 | 917 | 19.0 | 12.0 | 37.3 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 157 | 48.4 | 0.104 | 1.24 | 61 | 14.0 | 13.25 | 23.0 |
| INV/SHORT|aligned=1 | 131 | 47.3 | 0.104 | 1.23 | 59 | 21.5 | 16.25 | 28.8 |
| RETEST/LONG|aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 6093 | 45.8 | 0.038 | 1.08 | 2841 | 15.0 | 11.0 | 33.1 |
| RETEST/SHORT|aligned=1 | 4294 | 46.0 | 0.072 | 1.15 | 1906 | 20.0 | 13.0 | 35.5 |

## Autopsia de SL
n_losses=4868  causas: RR-bajo×1863, contra-estructura×1707, stop-en-el-minimo×1646, killzone-Asia-largo×1099, sin-nivel-detras×965, estirado×846, chop×695, SL-muy-pegado×600, sin-causa-clara×462, contra-sesgo×1
- INV/LONG (n=61): killzone-Asia-largo×32, RR-bajo×25, contra-estructura×19, estirado×15, stop-en-el-minimo×14, SL-muy-pegado×7, sin-nivel-detras×7, chop×5, sin-causa-clara×1
- INV/SHORT (n=59): RR-bajo×30, contra-estructura×18, stop-en-el-minimo×17, estirado×12, sin-causa-clara×11, SL-muy-pegado×8, chop×5, sin-nivel-detras×4
- RETEST/LONG (n=2842): RR-bajo×1083, killzone-Asia-largo×1067, contra-estructura×1060, stop-en-el-minimo×939, sin-nivel-detras×602, estirado×478, chop×438, SL-muy-pegado×344, sin-causa-clara×207, contra-sesgo×1
- RETEST/SHORT (n=1906): RR-bajo×725, stop-en-el-minimo×676, contra-estructura×610, sin-nivel-detras×352, estirado×341, chop×247, sin-causa-clara×243, SL-muy-pegado×241

## Autopsia de SL · semana 2026-W38 (para revision semanal)
n_losses=775  causas: RR-bajo×306, stop-en-el-minimo×286, contra-estructura×276, killzone-Asia-largo×262, sin-nivel-detras×157, estirado×140, chop×109, SL-muy-pegado×88, sin-causa-clara×62
ejemplos por causa: {"RR-bajo": ["CL-1-23392-L", "NQ-5-20749-L", "CL-5-20795-L", "YM-2-21454-S", "YM-5-20950-S"], "stop-en-el-minimo": ["NQ-5-20749-L", "NQ-1-23388-L", "NQ-1-23634-L", "NQ-5-21185-L", "NQ-5-21912-S"], "contra-estructura": ["NQ-1-21696-L", "CL-5-20795-L", "ES-5-20579-S", "GC-1-34473-S", "GC-2-27588-S"]}

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
    "n": 10139,
    "naive_expR": 0.053,
    "managed_expR": 0.132,
    "delta": 0.078,
    "avgEntryBetterTk_p50": 2.5,
    "fill_t3plus_pct": 46.3,
    "fill_full_pct": 32.6,
    "m1_rate": 36.9,
    "m2_rate": 23.0,
    "m3_rate": 12.4,
    "beAfterM1_rate": 17.7
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 102,
      "naive_expR": 0.107,
      "managed_expR": 0.295,
      "delta": 0.188,
      "avgEntryBetterTk_p50": 2.1500000000000004,
      "fill_t3plus_pct": 47.1,
      "fill_full_pct": 33.3,
      "m1_rate": 43.1,
      "m2_rate": 28.4,
      "m3_rate": 14.7,
      "beAfterM1_rate": 21.6
    },
    "1m/INV/SHORT": {
      "n": 81,
      "naive_expR": 0.096,
      "managed_expR": 0.296,
      "delta": 0.2,
      "avgEntryBetterTk_p50": 3.2,
      "fill_t3plus_pct": 51.9,
      "fill_full_pct": 39.5,
      "m1_rate": 38.3,
      "m2_rate": 23.5,
      "m3_rate": 13.6,
      "beAfterM1_rate": 18.5
    },
    "1m/RETEST/LONG": {
      "n": 3615,
      "naive_expR": 0.032,
      "managed_expR": 0.119,
      "delta": 0.086,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.8,
      "fill_full_pct": 34.4,
      "m1_rate": 35.9,
      "m2_rate": 22.4,
      "m3_rate": 11.5,
      "beAfterM1_rate": 16.6
    },
    "1m/RETEST/SHORT": {
      "n": 2546,
      "naive_expR": 0.06,
      "managed_expR": 0.171,
      "delta": 0.111,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.4,
      "fill_full_pct": 33.4,
      "m1_rate": 40.3,
      "m2_rate": 25.0,
      "m3_rate": 14.0,
      "beAfterM1_rate": 19.1
    },
    "2m/INV/LONG": {
      "n": 31,
      "naive_expR": -0.111,
      "managed_expR": -0.052,
      "delta": 0.059,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 51.6,
      "fill_full_pct": 35.5,
      "m1_rate": 19.4,
      "m2_rate": 19.4,
      "m3_rate": 0.0,
      "beAfterM1_rate": 3.2
    },
    "2m/INV/SHORT": {
      "n": 39,
      "naive_expR": 0.017,
      "managed_expR": -0.044,
      "delta": -0.061,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 46.2,
      "fill_full_pct": 38.5,
      "m1_rate": 25.6,
      "m2_rate": 23.1,
      "m3_rate": 12.8,
      "beAfterM1_rate": 5.1
    },
    "2m/RETEST/LONG": {
      "n": 1648,
      "naive_expR": 0.01,
      "managed_expR": 0.084,
      "delta": 0.074,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 43.5,
      "fill_full_pct": 29.6,
      "m1_rate": 35.1,
      "m2_rate": 20.7,
      "m3_rate": 11.3,
      "beAfterM1_rate": 18.0
    },
    "2m/RETEST/SHORT": {
      "n": 1114,
      "naive_expR": 0.094,
      "managed_expR": 0.152,
      "delta": 0.058,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 47.2,
      "fill_full_pct": 34.6,
      "m1_rate": 37.1,
      "m2_rate": 23.7,
      "m3_rate": 12.4,
      "beAfterM1_rate": 18.0
    },
    "5m/INV/LONG": {
      "n": 12,
      "naive_expR": 0.639,
      "managed_expR": 0.443,
      "delta": -0.196,
      "avgEntryBetterTk_p50": 2.65,
      "fill_t3plus_pct": 33.3,
      "fill_full_pct": 25.0,
      "m1_rate": 33.3,
      "m2_rate": 25.0,
      "m3_rate": 8.3,
      "beAfterM1_rate": 16.7
    },
    "5m/INV/SHORT": {
      "n": 8,
      "naive_expR": 0.615,
      "managed_expR": 0.657,
      "delta": 0.042,
      "avgEntryBetterTk_p50": 8.4,
      "fill_t3plus_pct": 62.5,
      "fill_full_pct": 37.5,
      "m1_rate": 37.5,
      "m2_rate": 25.0,
      "m3_rate": 25.0,
      "beAfterM1_rate": 12.5
    },
    "5m/RETEST/LONG": {
      "n": 582,
      "naive_expR": 0.153,
      "managed_expR": 0.087,
      "delta": -0.065,
      "avgEntryBetterTk_p50": 1.45,
      "fill_t3plus_pct": 33.3,
      "fill_full_pct": 24.1,
      "m1_rate": 34.2,
      "m2_rate": 22.3,
      "m3_rate": 13.2,
      "beAfterM1_rate": 19.2
    },
    "5m/RETEST/SHORT": {
      "n": 361,
      "naive_expR": 0.094,
      "managed_expR": 0.139,
      "delta": 0.045,
      "avgEntryBetterTk_p50": 5.0,
      "fill_t3plus_pct": 46.0,
      "fill_full_pct": 29.6,
      "m1_rate": 35.2,
      "m2_rate": 22.4,
      "m3_rate": 13.0,
      "beAfterM1_rate": 16.9
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 8736,
    "layer_expR": 0.061,
    "orig_expR": 0.198,
    "delta_orig_minus_layer": 0.137,
    "delta_ci90": [
      0.096,
      0.181
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.2,
    "orig_wrTP1": 33.5,
    "slTk_p50": 19.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.8,
    "orig_saved_from_SL": 15,
    "orig_caused_SL": 1299
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 1,
  "invalid_by_seg": {
    "2m/RETEST/LONG": 1
  },
  "by_basis": {
    "candle1": {
      "n": 261,
      "layer_expR": 0.103,
      "orig_expR": 0.063,
      "delta_orig_minus_layer": -0.04,
      "delta_ci90": [
        -0.255,
        0.201
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.8,
      "orig_wrTP1": 28.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 8.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 57
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
      "n": 6518,
      "layer_expR": 0.055,
      "orig_expR": 0.199,
      "delta_orig_minus_layer": 0.144,
      "delta_ci90": [
        0.094,
        0.191
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.4,
      "orig_wrTP1": 33.9,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 13,
      "orig_caused_SL": 956
    },
    "retestBar2": {
      "n": 1957,
      "layer_expR": 0.078,
      "orig_expR": 0.214,
      "delta_orig_minus_layer": 0.136,
      "delta_ci90": [
        0.037,
        0.24
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.2,
      "orig_wrTP1": 32.7,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 286
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 102,
      "layer_expR": 0.107,
      "orig_expR": -0.056,
      "delta_orig_minus_layer": -0.162,
      "delta_ci90": [
        -0.485,
        0.163
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.0,
      "orig_wrTP1": 23.5,
      "slTk_p50": 15.5,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 5.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 26
    },
    "1m/INV/SHORT": {
      "n": 71,
      "layer_expR": 0.102,
      "orig_expR": -0.091,
      "delta_orig_minus_layer": -0.193,
      "delta_ci90": [
        -0.551,
        0.194
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.7,
      "orig_wrTP1": 26.8,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 4.2,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 17
    },
    "1m/RETEST/LONG": {
      "n": 3095,
      "layer_expR": 0.038,
      "orig_expR": 0.18,
      "delta_orig_minus_layer": 0.142,
      "delta_ci90": [
        0.066,
        0.218
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.7,
      "orig_wrTP1": 29.4,
      "slTk_p50": 17.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.1,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 505
    },
    "1m/RETEST/SHORT": {
      "n": 2085,
      "layer_expR": 0.068,
      "orig_expR": 0.211,
      "delta_orig_minus_layer": 0.143,
      "delta_ci90": [
        0.046,
        0.247
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.0,
      "orig_wrTP1": 32.4,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 304
    },
    "2m/INV/LONG": {
      "n": 31,
      "layer_expR": -0.111,
      "orig_expR": 0.637,
      "delta_orig_minus_layer": 0.748,
      "delta_ci90": [
        -0.142,
        1.885
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 51.6,
      "orig_wrTP1": 32.3,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 12.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 6
    },
    "2m/INV/SHORT": {
      "n": 38,
      "layer_expR": 0.006,
      "orig_expR": 0.417,
      "delta_orig_minus_layer": 0.411,
      "delta_ci90": [
        -0.059,
        1.034
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 34.2,
      "orig_wrTP1": 31.6,
      "slTk_p50": 23.5,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 5.3,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 2
    },
    "2m/RETEST/LONG": {
      "n": 1477,
      "layer_expR": 0.027,
      "orig_expR": 0.077,
      "delta_orig_minus_layer": 0.05,
      "delta_ci90": [
        -0.018,
        0.12
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.4,
      "orig_wrTP1": 35.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.2,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 207
    },
    "2m/RETEST/SHORT": {
      "n": 939,
      "layer_expR": 0.11,
      "orig_expR": 0.223,
      "delta_orig_minus_layer": 0.113,
      "delta_ci90": [
        0.012,
        0.215
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.8,
      "orig_wrTP1": 37.0,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 2.7,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 140
    },
    "5m/INV/LONG": {
      "n": 12,
      "layer_expR": 0.639,
      "orig_expR": -0.463,
      "delta_orig_minus_layer": -1.103,
      "delta_ci90": [
        -1.662,
        -0.625
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 83.3,
      "orig_wrTP1": 41.7,
      "slTk_p50": 43.0,
      "slOrigTk_p50": 6.5,
      "orig_wider_pct": 25.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 5
    },
    "5m/INV/SHORT": {
      "n": 7,
      "layer_expR": 0.629,
      "orig_expR": -0.193,
      "delta_orig_minus_layer": -0.821,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 71.4,
      "orig_wrTP1": 57.1,
      "slTk_p50": 46.0,
      "slOrigTk_p50": 88.0,
      "orig_wider_pct": 42.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 1
    },
    "5m/RETEST/LONG": {
      "n": 555,
      "layer_expR": 0.143,
      "orig_expR": 0.362,
      "delta_orig_minus_layer": 0.218,
      "delta_ci90": [
        0.05,
        0.403
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.4,
      "orig_wrTP1": 45.2,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 14.0,
      "orig_wider_pct": 16.2,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 54
    },
    "5m/RETEST/SHORT": {
      "n": 324,
      "layer_expR": 0.075,
      "orig_expR": 0.59,
      "delta_orig_minus_layer": 0.514,
      "delta_ci90": [
        0.133,
        0.987
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 52.5,
      "orig_wrTP1": 44.4,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 18.8,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 32
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 3135,
    "wrTP1": 44.8,
    "expR": -0.017
  },
  "2026-W37": {
    "n": 5338,
    "wrTP1": 46.8,
    "expR": 0.07
  },
  "2026-W38": {
    "n": 2211,
    "wrTP1": 45.4,
    "expR": 0.123
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 38,
      "wrTP1": 44.7,
      "expR": 0.278,
      "pf": 1.59
    },
    "1m/INV/SHORT": {
      "n": 19,
      "wrTP1": 68.4,
      "expR": 0.264,
      "pf": 1.95
    },
    "1m/RETEST/LONG": {
      "n": 1367,
      "wrTP1": 42.9,
      "expR": -0.012,
      "pf": 0.98
    },
    "1m/RETEST/SHORT": {
      "n": 447,
      "wrTP1": 43.8,
      "expR": -0.006,
      "pf": 0.99
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
      "n": 684,
      "wrTP1": 46.1,
      "expR": -0.062,
      "pf": 0.88
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
      "n": 243,
      "wrTP1": 52.7,
      "expR": 0.083,
      "pf": 1.19
    },
    "5m/RETEST/SHORT": {
      "n": 94,
      "wrTP1": 47.9,
      "expR": -0.019,
      "pf": 0.96
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
      "n": 56,
      "wrTP1": 41.1,
      "expR": 0.038,
      "pf": 1.07
    },
    "1m/RETEST/LONG": {
      "n": 1599,
      "wrTP1": 45.2,
      "expR": 0.047,
      "pf": 1.09
    },
    "1m/RETEST/SHORT": {
      "n": 1710,
      "wrTP1": 45.0,
      "expR": 0.045,
      "pf": 1.09
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
      "n": 682,
      "wrTP1": 47.7,
      "expR": 0.041,
      "pf": 1.08
    },
    "2m/RETEST/SHORT": {
      "n": 754,
      "wrTP1": 51.3,
      "expR": 0.143,
      "pf": 1.32
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
      "n": 235,
      "wrTP1": 52.3,
      "expR": 0.203,
      "pf": 1.45
    },
    "5m/RETEST/SHORT": {
      "n": 218,
      "wrTP1": 51.4,
      "expR": 0.106,
      "pf": 1.23
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 36,
      "wrTP1": 50.0,
      "expR": 0.07,
      "pf": 1.17
    },
    "1m/INV/SHORT": {
      "n": 9,
      "wrTP1": 66.7,
      "expR": 0.115,
      "pf": 1.46
    },
    "1m/RETEST/LONG": {
      "n": 784,
      "wrTP1": 46.4,
      "expR": 0.086,
      "pf": 1.19
    },
    "1m/RETEST/SHORT": {
      "n": 565,
      "wrTP1": 43.5,
      "expR": 0.177,
      "pf": 1.44
    },
    "2m/INV/LONG": {
      "n": 7,
      "wrTP1": 57.1,
      "expR": 0.102,
      "pf": 1.51
    },
    "2m/INV/SHORT": {
      "n": 2,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 364,
      "wrTP1": 45.1,
      "expR": 0.103,
      "pf": 1.23
    },
    "2m/RETEST/SHORT": {
      "n": 207,
      "wrTP1": 46.9,
      "expR": 0.117,
      "pf": 1.3
    },
    "5m/INV/LONG": {
      "n": 4,
      "wrTP1": 25.0,
      "expR": -0.41,
      "pf": 0.18
    },
    "5m/RETEST/LONG": {
      "n": 144,
      "wrTP1": 45.8,
      "expR": 0.192,
      "pf": 1.46
    },
    "5m/RETEST/SHORT": {
      "n": 89,
      "wrTP1": 41.6,
      "expR": 0.225,
      "pf": 1.6
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 9774,
  "brier": 0.2217,
  "bias": -0.077,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.192
    },
    {
      "feature": "stretchAtr",
      "weight": -0.116
    },
    {
      "feature": "nearTk",
      "weight": -0.083
    },
    {
      "feature": "biasScore",
      "weight": -0.079
    },
    {
      "feature": "rvol",
      "weight": 0.065
    },
    {
      "feature": "structDir",
      "weight": 0.046
    },
    {
      "feature": "nearEdge",
      "weight": 0.028
    },
    {
      "feature": "aligned",
      "weight": -0.028
    },
    {
      "feature": "emaStack",
      "weight": 0.027
    },
    {
      "feature": "chopIdx",
      "weight": -0.02
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.013
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.011
    },
    {
      "feature": "hourNY",
      "weight": 0.007
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.161,
      "actual": 0.172,
      "n": 977
    },
    {
      "bin": 1,
      "pred": 0.355,
      "actual": 0.305,
      "n": 977
    },
    {
      "bin": 2,
      "pred": 0.439,
      "actual": 0.354,
      "n": 978
    },
    {
      "bin": 3,
      "pred": 0.49,
      "actual": 0.421,
      "n": 977
    },
    {
      "bin": 4,
      "pred": 0.53,
      "actual": 0.504,
      "n": 978
    },
    {
      "bin": 5,
      "pred": 0.562,
      "actual": 0.569,
      "n": 977
    },
    {
      "bin": 6,
      "pred": 0.586,
      "actual": 0.605,
      "n": 977
    },
    {
      "bin": 7,
      "pred": 0.609,
      "actual": 0.653,
      "n": 978
    },
    {
      "bin": 8,
      "pred": 0.631,
      "actual": 0.707,
      "n": 977
    },
    {
      "bin": 9,
      "pred": 0.667,
      "actual": 0.729,
      "n": 978
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
    "expR": 0.107,
    "ci90": [
      -0.096,
      0.318
    ],
    "p_mean_le_0": 0.201,
    "n": 102,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.096,
    "ci90": [
      -0.116,
      0.328
    ],
    "p_mean_le_0": 0.237,
    "n": 81,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.032,
    "ci90": [
      -0.002,
      0.068
    ],
    "p_mean_le_0": 0.062,
    "n": 3619,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.059,
    "ci90": [
      0.018,
      0.1
    ],
    "p_mean_le_0": 0.011,
    "n": 2553,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": -0.111,
    "ci90": [
      -0.38,
      0.169
    ],
    "p_mean_le_0": 0.74,
    "n": 31,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.017,
    "ci90": [
      -0.335,
      0.412
    ],
    "p_mean_le_0": 0.477,
    "n": 39,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.01,
    "ci90": [
      -0.037,
      0.056
    ],
    "p_mean_le_0": 0.352,
    "n": 1650,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.094,
    "ci90": [
      0.035,
      0.151
    ],
    "p_mean_le_0": 0.005,
    "n": 1114,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.639,
    "ci90": [
      0.257,
      1.035
    ],
    "p_mean_le_0": 0.002,
    "n": 12,
    "survives_fdr10": true
  },
  "5m/INV/SHORT": {
    "expR": 0.615,
    "ci90": [
      -0.057,
      1.309
    ],
    "p_mean_le_0": 0.072,
    "n": 8,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.153,
    "ci90": [
      0.07,
      0.237
    ],
    "p_mean_le_0": 0.003,
    "n": 582,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.096,
    "ci90": [
      -0.009,
      0.207
    ],
    "p_mean_le_0": 0.072,
    "n": 362,
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
      "id": 2,
      "n": 3776,
      "wrTP1": 45.6,
      "expR": 0.076,
      "pf": 1.16,
      "defining_features": {
        "biasScore": -1.1,
        "emaStack": -0.99,
        "nearEdge": -0.84,
        "structDir": -0.45
      }
    },
    {
      "id": 0,
      "n": 3927,
      "wrTP1": 45.5,
      "expR": 0.072,
      "pf": 1.15,
      "defining_features": {
        "biasScore": 0.78,
        "nearEdge": 0.68,
        "emaStack": 0.67,
        "hourNY": -0.54
      }
    },
    {
      "id": 1,
      "n": 1836,
      "wrTP1": 49.6,
      "expR": 0.017,
      "pf": 1.04,
      "defining_features": {
        "hourNY": 1.31,
        "atrPctUsed": -0.84,
        "emaStack": 0.61,
        "biasScore": 0.58
      }
    },
    {
      "id": 3,
      "n": 1145,
      "wrTP1": 42.9,
      "expR": -0.025,
      "pf": 0.95,
      "defining_features": {
        "stretchAtr": 1.76,
        "rvol": 1.62,
        "chopIdx": -1.41,
        "entryZoneTk": -0.17
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
        "n": 44,
        "wrTP1": 38.6,
        "expR": 0.124
      },
      "ES": {
        "n": 13,
        "wrTP1": 53.8,
        "expR": -0.187
      },
      "NQ": {
        "n": 8,
        "wrTP1": 50.0,
        "expR": 0.261
      },
      "GC": {
        "n": 16,
        "wrTP1": 31.2,
        "expR": -0.408
      }
    },
    "expR_spread": 0.872,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 51,
        "wrTP1": 43.1,
        "expR": -0.012
      },
      "NQ": {
        "n": 9,
        "wrTP1": 55.6,
        "expR": 0.19
      },
      "ES": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.57
      },
      "GC": {
        "n": 18,
        "wrTP1": 61.1,
        "expR": 0.188
      }
    },
    "expR_spread": 0.582,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 573,
        "wrTP1": 44.2,
        "expR": 0.059
      },
      "NQ": {
        "n": 720,
        "wrTP1": 43.8,
        "expR": -0.032
      },
      "ES": {
        "n": 708,
        "wrTP1": 46.9,
        "expR": 0.072
      },
      "CL": {
        "n": 1201,
        "wrTP1": 45.2,
        "expR": 0.034
      },
      "YM": {
        "n": 548,
        "wrTP1": 42.0,
        "expR": 0.036
      }
    },
    "expR_spread": 0.104,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 404,
        "wrTP1": 42.1,
        "expR": 0.104
      },
      "GC": {
        "n": 745,
        "wrTP1": 45.2,
        "expR": 0.072
      },
      "YM": {
        "n": 848,
        "wrTP1": 45.8,
        "expR": 0.107
      },
      "ES": {
        "n": 674,
        "wrTP1": 44.5,
        "expR": 0.002
      },
      "CL": {
        "n": 51,
        "wrTP1": 31.4,
        "expR": -0.463
      }
    },
    "expR_spread": 0.57,
    "verdict": "instrument-specific"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 5,
        "wrTP1": 40.0,
        "expR": -0.37
      },
      "CL": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.137
      },
      "YM": {
        "n": 8,
        "wrTP1": 25.0,
        "expR": -0.484
      },
      "ES": {
        "n": 6,
        "wrTP1": 83.3,
        "expR": 0.442
      },
      "NQ": {
        "n": 8,
        "wrTP1": 50.0,
        "expR": -0.006
      }
    },
    "expR_spread": 0.926,
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
        "n": 366,
        "wrTP1": 48.6,
        "expR": 0.052
      },
      "GC": {
        "n": 209,
        "wrTP1": 44.5,
        "expR": 0.0
      },
      "CL": {
        "n": 540,
        "wrTP1": 48.3,
        "expR": 0.049
      },
      "ES": {
        "n": 328,
        "wrTP1": 48.5,
        "expR": -0.014
      },
      "YM": {
        "n": 287,
        "wrTP1": 39.4,
        "expR": -0.081
      }
    },
    "expR_spread": 0.133,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 274,
        "wrTP1": 50.0,
        "expR": 0.052
      },
      "YM": {
        "n": 400,
        "wrTP1": 51.5,
        "expR": 0.13
      },
      "GC": {
        "n": 282,
        "wrTP1": 47.2,
        "expR": 0.104
      },
      "NQ": {
        "n": 195,
        "wrTP1": 44.1,
        "expR": 0.121
      },
      "CL": {
        "n": 20,
        "wrTP1": 35.0,
        "expR": -0.422
      }
    },
    "expR_spread": 0.552,
    "verdict": "instrument-specific"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.13
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
    "expR_spread": 1.387,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 23,
        "wrTP1": 65.2,
        "expR": 0.498
      },
      "ES": {
        "n": 140,
        "wrTP1": 52.9,
        "expR": 0.245
      },
      "YM": {
        "n": 113,
        "wrTP1": 49.6,
        "expR": 0.198
      },
      "CL": {
        "n": 162,
        "wrTP1": 58.6,
        "expR": 0.301
      },
      "NQ": {
        "n": 184,
        "wrTP1": 41.8,
        "expR": -0.128
      }
    },
    "expR_spread": 0.626,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 77,
        "wrTP1": 50.6,
        "expR": 0.035
      },
      "ES": {
        "n": 98,
        "wrTP1": 56.1,
        "expR": 0.131
      },
      "GC": {
        "n": 96,
        "wrTP1": 35.4,
        "expR": 0.019
      },
      "YM": {
        "n": 121,
        "wrTP1": 51.2,
        "expR": 0.201
      },
      "CL": {
        "n": 9,
        "wrTP1": 44.4,
        "expR": -0.323
      }
    },
    "expR_spread": 0.524,
    "verdict": "instrument-specific"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 16,
  "near_news_30m": {
    "n": 230,
    "wrTP1": 46.1,
    "nSL": 78,
    "nTO": 46,
    "expR": 0.21,
    "pf": 1.5,
    "mfe_p25": 10.75,
    "mfe_p50": 20.5,
    "mfe_p75": 38.25,
    "winnerMAE_p75": 11.0,
    "winnerMAE_p90": 20.0,
    "loserMFEbeforeSL_p50": 2.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -16.5,
    "revAfterSL_rate": 46.2
  },
  "away_from_news": {
    "n": 10454,
    "wrTP1": 45.9,
    "nSL": 4790,
    "nTO": 864,
    "expR": 0.051,
    "pf": 1.1,
    "mfe_p25": 7.0,
    "mfe_p50": 17.0,
    "mfe_p75": 38.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 33.6
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
      "asOf": "2026-09-16 (miercoles). Dato nuevo genuino, sin incidentes de repo salvo el 'forced update' habitual sobre origin/main (shallow clone, mismo tip, resuelto con checkout -B main origin/main). n de pares resueltos subio de 9303 a 9587.",
      "retest_1m_long": {
        "n": 2737,
        "deltaER_orig_minus_layer": 0.15,
        "ci90": [
          0.072,
          0.231
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 2676 a 2737, delta practicamente identico (0.141->0.15) -- novena confirmacion independiente, sigue siendo la lectura mas estable del experimento."
      },
      "retest_1m_short": {
        "n": 1971,
        "deltaER_orig_minus_layer": 0.127,
        "ci90": [
          0.036,
          0.226
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 1955 a 1971, delta se mantiene sin cruzar cero (0.126->0.127), limite inferior del CI90 estable en 0.036."
      },
      "retest_2m_long": {
        "n": 1327,
        "deltaER_orig_minus_layer": 0.035,
        "ci90": [
          -0.039,
          0.109
        ],
        "ci90_no_cruza_cero": false,
        "nota": "n subio de 1306 a 1327, delta subio un poco (0.032->0.035) pero el CI90 sigue cruzando cero -- decima lectura seguida sin certificar, se mantiene fuera de la propuesta."
      },
      "retest_2m_short": {
        "n": 895,
        "deltaER_orig_minus_layer": 0.117,
        "ci90": [
          0.011,
          0.221
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 890 a 895, delta identico (0.117), el limite inferior del CI90 se mantiene muy pegado a cero (0.014->0.011) -- sigue como candidato debil/al filo, no promoverlo a la lista solida todavia."
      },
      "retest_5m_long": {
        "n": 492,
        "deltaER_orig_minus_layer": 0.248,
        "ci90": [
          0.063,
          0.479
        ],
        "ci90_no_cruza_cero": true,
        "nota": "SEXTA LECTURA SEGUIDA CERTIFICANDO: n subio de 489 a 492, delta practicamente identico (0.246->0.248) -- sigue estable, sin retroceso, desde que se incluyo en la propuesta de la revision semanal."
      },
      "retest_5m_short": {
        "n": 309,
        "deltaER_orig_minus_layer": 0.554,
        "ci90": [
          0.148,
          1.067
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 305 a 309, delta practicamente sin cambio (0.561->0.554) -- sigue siendo la lectura mas solida del experimento."
      },
      "overall_by_basis_retestBar": {
        "n": 5888,
        "deltaER": 0.15,
        "ci90": [
          0.101,
          0.205
        ],
        "nota": "n subio de 5794 a 5888, delta estable (0.146->0.15) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba."
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
      "2026-09-16 (miercoles, dato nuevo genuino, +284 pares resueltos en todo el bus): los 4 segmentos propuestos el 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con `delta_beats_zero=true` y sin ningun retroceso -- 1m LONG suma su NOVENA confirmacion, 1m SHORT y 5m SHORT estables, **5m LONG suma su SEXTA lectura seguida certificando**. 2m SHORT se mantiene exactamente igual (delta 0.117, limite inferior del CI90 baja un poco de 0.014 a 0.011 -- sigue candidato debil/al filo, todavia sin una segunda lectura clara lejos de cero). 2m LONG sigue sin certificar, decima lectura seguida (delta 0.035, CI90 cruza cero). Sin cambios de estado: sigue `proposed`, `changeDate` null. La escalera de ejecucion sigue bloqueada en el peldano 0 (asesor) porque, aun con `gate.readyForLive=true` en 5m/RETEST/LONG (n>=100, E[R]>0, PF>=1.3, WR>=50), este mismo experimento -- la causa de SL dominante en RETEST -- sigue sin un `changeDate` ni muestra post-cambio; ese es exactamente el requisito que falta segun `execution-ladder.md` peldano 2. Nada accionable nuevo para Jesus hoy mas alla de: si va a aplicar el cambio de SL estructural en los 12 graficos, este es el dia con la evidencia mas solida acumulada hasta ahora (6 confirmaciones seguidas en el candidato mas fragil, 5m LONG)."
    ],
    "beforeN": 10396,
    "afterN": 0,
    "before": {
      "n": 10396,
      "wrTP1": 45.9,
      "nSL": 4748,
      "nTO": 880,
      "expR": 0.052,
      "pf": 1.11,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 38.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 34.0
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
    "date": "2026-09-17",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-16T19:11:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "ES",
    "focus": {
      "sym": "ES",
      "verdict": "WAIT",
      "window": "17:00-01:00 CT",
      "setup": {
        "es": "la A+ real (fade 1h 7633.75-7674) ya esta al precio (7657.25) tras la reapertura -- el retest de VAL 7620-7627 quedo abajo, fuera de alcance por ahora",
        "en": "the real A+ (1h fade 7633.75-7674) is now at price (7657.25) after the reopen -- the VAL 7620-7627 retest is now below, out of reach for now"
      },
      "trigger": {
        "es": "rechazo confirmado en el FVG 1h (cierre 5m de vuelta bajo 7633.75) ya con el precio dentro de la zona; sin ese cierre no hay entrada, no te adelantes al primer toque",
        "en": "a confirmed rejection at the 1h FVG (5m close back below 7633.75) with price already inside the zone; no entry without that close, don't front-run the first tag"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 7674 (borde alto del FVG 1h) con seguimiento real",
        "en": "5m close sustained above 7674 (1h FVG high edge) with real follow-through"
      },
      "note": {
        "es": "el precio ya esta dentro de la zona A+ real -- espera el rechazo confirmado, no el primer toque; el retest de VAL quedo descartado por ahora",
        "en": "price is already inside the real A+ zone -- wait for the confirmed rejection, not the first tag; the VAL retest is off the table for now"
      }
    },
    "summary": {
      "es": [
        "!! dia de la Fed con reversion violenta en el complejo: tesis rota en ES/GC/CL, YM confirma bajista con minimo nuevo de ciclo, NQ vuelve casi al mismo nivel de hace 2 dias tras tocar maximo Y minimo nuevos",
        "NQ: WAIT · el rally de la reapertura llevo el precio a 29450.5 (+184.5p desde el cierre), ya sobre la invalidacion 29439 del corto -- zona A+ 29289-29326 fuera de alcance por ahora · EM 148p (44% usado, 271p restantes)",
        "ES: WAIT · corto · la A+ real (fade 1h 7633.75-7674) ya esta al precio, esperando el rechazo confirmado · EM 68p (52% usado, 38p restantes)",
        "GC: WAIT · corto tentativo · sigue sentado en el rango del minimo del dia (4296.8-4315.0), sin estructura fresca · EM 263p (16% usado, 100p restantes)",
        "YM: WAIT · el rebote de la reapertura llevo el precio a 52136 (+233p), ya dentro de la zona de reclamo alcista 52061-52466 -- htfzones sigue caida (~35h), conviccion no pasa de baja · EM 137p (48% usado, 325p restantes)",
        "CL: WAIT · corto · precio siguio cayendo a 101.77 sin rebotar a la zona 102.22-102.47, ya cerca del objetivo 1 (101.28) · EM 131p (18% usado, 380p restantes)",
        "mas limpio: ES (unico con el conflicto de marco resuelto)",
        "limite $1000 por cuenta ⇒ en casi todas las zonas de hoy el stop estructural deja maxContracts en 0 en full -- usa micros o pasa la s
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 4087,
  "by_verdict": {
    "AVOID": {
      "n": 1150,
      "wrTP1": 44.3,
      "nSL": 574,
      "nTO": 66,
      "expR": -0.004,
      "pf": 0.99,
      "mfe_p25": 6.0,
      "mfe_p50": 13.0,
      "mfe_p75": 27.0,
      "winnerMAE_p75": 9.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.5,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 32.8
    },
    "GO": {
      "n": 573,
      "wrTP1": 52.0,
      "nSL": 222,
      "nTO": 53,
      "expR": 0.158,
      "pf": 1.38,
      "mfe_p25": 11.0,
      "mfe_p50": 25.0,
      "mfe_p75": 53.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 31.30000000000001,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 40.5
    },
    "WAIT": {
      "n": 2364,
      "wrTP1": 48.9,
      "nSL": 973,
      "nTO": 235,
      "expR": 0.109,
      "pf": 1.25,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 42.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 24.5,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 40.3
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": -0.004,
      "ci90": [
        -0.066,
        0.057
      ],
      "p_mean_le_0": 0.555,
      "n": 1110
    },
    "GO": {
      "expR": 0.158,
      "ci90": [
        0.073,
        0.242
      ],
      "p_mean_le_0": 0.001,
      "n": 533
    },
    "WAIT": {
      "expR": 0.109,
      "ci90": [
        0.069,
        0.15
      ],
      "p_mean_le_0": 0.0,
      "n": 2204
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1150,
      "wrTP1": 44.3,
      "nSL": 574,
      "nTO": 66,
      "expR": -0.004,
      "pf": 0.99,
      "mfe_p25": 6.0,
      "mfe_p50": 13.0,
      "mfe_p75": 27.0,
      "winnerMAE_p75": 9.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.5,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 32.8
    },
    "GO_or_WAIT": {
      "n": 2937,
      "wrTP1": 49.5,
      "nSL": 1195,
      "nTO": 288,
      "expR": 0.118,
      "pf": 1.27,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 25.700000000000045,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 40.3
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": -0.004,
      "ci90": [
        -0.066,
        0.057
      ],
      "p_mean_le_0": 0.555,
      "n": 1110
    },
    "GO_or_WAIT": {
      "expR": 0.118,
      "ci90": [
        0.083,
        0.154
      ],
      "p_mean_le_0": 0.0,
      "n": 2737
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 11,
        "wrTP1": 54.5,
        "nSL": 4,
        "nTO": 1,
        "expR": 0.013,
        "pf": 1.03,
        "mfe_p25": 5.0,
        "mfe_p50": 6.0,
        "mfe_p75": 29.0,
        "winnerMAE_p75": 0.0,
        "winnerMAE_p90": 2.0,
        "loserMFEbeforeSL_p50": 15.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 25.0
      },
      "GO": {
        "n": 9,
        "wrTP1": 55.6,
        "nSL": 3,
        "nTO": 1,
        "expR": -0.016,
        "pf": 0.96,
        "mfe_p25": 19.75,
        "mfe_p50": 26.0,
        "mfe_p75": 33.25,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 28.400000000000002,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -60.0,
        "revAfterSL_rate": 33.3
      },
      "WAIT": {
        "n": 35,
        "wrTP1": 45.7,
        "nSL": 16,
        "nTO": 3,
        "expR": -0.078,
        "pf": 0.84,
        "mfe_p25": 7.0,
        "mfe_p50": 20.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 19.5,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 2.5,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 4.5,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 25.0
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
        "n": 22,
        "wrTP1": 54.5,
        "nSL": 9,
        "nTO": 1,
        "expR": -0.12,
        "pf": 0.71,
        "mfe_p25": 8.25,
        "mfe_p50": 22.0,
        "mfe_p75": 38.75,
        "winnerMAE_p75": 33.25,
        "winnerMAE_p90": 73.9,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -20.5,
        "revAfterSL_rate": 44.4
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 583,
        "wrTP1": 46.1,
        "nSL": 292,
        "nTO": 22,
        "expR": -0.019,
        "pf": 0.96,
        "mfe_p25": 6.0,
        "mfe_p50": 11.0,
        "mfe_p75": 21.5,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 17.200000000000017,
        "loserMFEbeforeSL_p50": 2.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 28.1
      },
      "GO": {
        "n": 366,
        "wrTP1": 51.1,
        "nSL": 150,
        "nTO": 29,
        "expR": 0.12,
        "pf": 1.28,
        "mfe_p25": 9.0,
        "mfe_p50": 24.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.5,
        "revAfterSL_rate": 42.0
      },
      "WAIT": {
        "n": 1351,
        "wrTP1": 51.1,
        "nSL": 531,
        "nTO": 129,
        "expR": 0.166,
        "pf": 1.4,
        "mfe_p25": 7.0,
        "mfe_p50": 17.0,
        "mfe_p75": 39.5,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 43.7
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 533,
        "wrTP1": 42.6,
        "nSL": 265,
        "nTO": 41,
        "expR": 0.026,
        "pf": 1.05,
        "mfe_p25": 7.0,
        "mfe_p50": 15.5,
        "mfe_p75": 30.0,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 20.80000000000001,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 38.9
      },
      "GO": {
        "n": 196,
        "wrTP1": 53.6,
        "nSL": 68,
        "nTO": 23,
        "expR": 0.231,
        "pf": 1.6,
        "mfe_p25": 13.0,
        "mfe_p50": 27.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 30.800000000000026,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 38.2
      },
      "WAIT": {
        "n": 956,
        "wrTP1": 45.7,
        "nSL": 417,
        "nTO": 102,
        "expR": 0.038,
        "pf": 1.08,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 44.75,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 28.400000000000034,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 36.5
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```
