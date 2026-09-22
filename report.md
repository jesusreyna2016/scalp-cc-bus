# Scalp CC · report 2026-09-22T01:13Z
- signals=14193 outcomes=13584 pares_resueltos=14160 pendientes=33 huerfanos=34

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: semana ya cerrada 2026-W36 bajo de n=3183 a n=2991 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W37 bajo de n=5389 a n=5243 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W38 bajo de n=4911 a n=4894 desde la corrida previa -- vigilar, puede ser deduplicacion.
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.257 vs 0.09, delta 0.167 CI90 [0.124, 0.209], n 9039). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.207 vs 0.071, delta 0.137 CI90 [0.054, 0.224], n 2486). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.199 CI90 [0.123, 0.28], n 738). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.079 CI90 [0.044, 0.115], n 3060). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.081, "ci90": [0.063, 0.099], "p_mean_le_0": 0.0, "n": 13550}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 141 | 44.0 | 0.121 | 1.26 | 61 | 13.0 | 12.0 | 18.0 |
| 1m/INV/SHORT | 101 | 49.5 | 0.077 | 1.17 | 44 | 20.0 | 11.0 | 18.2 |
| 1m/RETEST/LONG | 5334 | 46.2 | 0.088 | 1.18 | 2473 | 15.0 | 10.0 | 29.2 |
| 1m/RETEST/SHORT | 3333 | 44.4 | 0.055 | 1.11 | 1534 | 17.0 | 11.0 | 31.6 |
| 2m/INV/LONG | 50 | 52.0 | 0.02 | 1.05 | 19 | 12.5 | 9.75 | 21.1 |
| 2m/INV/SHORT | 42 | 33.3 | -0.056 | 0.9 | 24 | 19.0 | 15.75 | 37.5 |
| 2m/RETEST/LONG | 2388 | 47.9 | 0.072 | 1.15 | 1087 | 18.0 | 13.0 | 37.6 |
| 2m/RETEST/SHORT | 1408 | 47.7 | 0.062 | 1.13 | 640 | 21.0 | 12.25 | 39.7 |
| 5m/INV/LONG | 17 | 64.7 | 0.407 | 3.03 | 3 | 31.0 | 30.5 | 66.7 |
| 5m/INV/SHORT | 9 | 66.7 | 0.436 | 2.31 | 3 | 37.0 | 68.75 | 66.7 |
| 5m/RETEST/LONG | 833 | 52.2 | 0.181 | 1.42 | 335 | 30.0 | 19.0 | 49.6 |
| 5m/RETEST/SHORT | 504 | 47.8 | 0.091 | 1.2 | 215 | 33.0 | 23.0 | 37.2 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 1003 | 27.0 | 0.179 | 1.28 | 605 | 29.0 | 14.5 | 21.0 |
| B | 5972 | 46.9 | 0.077 | 1.16 | 2706 | 17.0 | 12.0 | 32.8 |
| C | 7185 | 49.2 | 0.07 | 1.15 | 3127 | 17.0 | 12.0 | 36.4 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 5126 | 50.1 | 0.12 | 1.27 | 2229 | 13.0 | 10.0 | 38.8 |
| London | 2172 | 45.7 | 0.039 | 1.08 | 1077 | 18.0 | 12.0 | 33.4 |
| NY | 2496 | 45.3 | 0.122 | 1.26 | 1096 | 24.0 | 15.75 | 37.2 |
| Sin KZ | 4366 | 43.8 | 0.032 | 1.06 | 2036 | 19.0 | 13.0 | 25.5 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 3120 | 44.4 | 0.054 | 1.11 | 1454 | 20.0 | 14.0 | 31.4 |
| edge=0 | 6239 | 49.2 | 0.073 | 1.16 | 2752 | 16.0 | 11.0 | 38.3 |
| edge=1 | 4801 | 44.7 | 0.108 | 1.22 | 2232 | 18.0 | 13.0 | 28.8 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 14151 | 46.6 | 0.081 | 1.17 | 6437 | 18.0 | 12.0 | 33.4 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 83 | 53.0 | 0.118 | 1.29 | 30 | 11.5 | 11.25 | 26.7 |
| INV/LONG|edge=1 | 121 | 43.8 | 0.107 | 1.24 | 51 | 17.0 | 17.0 | 15.7 |
| INV/SHORT|edge=-1 | 89 | 39.3 | 0.035 | 1.07 | 46 | 22.0 | 12.0 | 26.1 |
| INV/SHORT|edge=0 | 54 | 53.7 | -0.006 | 0.99 | 22 | 13.0 | 14.0 | 31.8 |
| INV/SHORT|edge=1 | 9 | 66.7 | 0.69 | 3.07 | 3 | 28.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 285 | 54.0 | 0.197 | 1.48 | 112 | 12.0 | 7.0 | 51.8 |
| RETEST/LONG|edge=0 | 3751 | 50.3 | 0.064 | 1.14 | 1668 | 15.0 | 11.0 | 38.4 |
| RETEST/LONG|edge=1 | 4519 | 44.3 | 0.109 | 1.22 | 2115 | 18.0 | 13.0 | 28.4 |
| RETEST/SHORT|edge=-1 | 2742 | 43.6 | 0.039 | 1.08 | 1294 | 22.0 | 15.0 | 29.8 |
| RETEST/SHORT|edge=0 | 2351 | 47.3 | 0.086 | 1.18 | 1032 | 17.0 | 11.0 | 38.6 |
| RETEST/SHORT|edge=1 | 152 | 55.3 | 0.056 | 1.13 | 63 | 14.0 | 9.25 | 55.6 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 64 | 40.6 | 0.158 | 1.32 | 30 | 14.5 | 16.25 | 10.0 |
| INV/LONG|tier=C | 144 | 50.7 | 0.1 | 1.25 | 53 | 13.0 | 13.0 | 26.4 |
| INV/SHORT|tier=B | 46 | 41.3 | -0.007 | 0.99 | 25 | 18.5 | 9.5 | 8.0 |
| INV/SHORT|tier=C | 106 | 48.1 | 0.092 | 1.2 | 46 | 20.5 | 25.5 | 37.0 |
| RETEST/LONG|tier=A+ | 662 | 26.4 | 0.163 | 1.25 | 407 | 26.0 | 14.0 | 19.7 |
| RETEST/LONG|tier=B | 3658 | 47.4 | 0.114 | 1.24 | 1638 | 16.0 | 11.0 | 32.8 |
| RETEST/LONG|tier=C | 4235 | 50.4 | 0.063 | 1.14 | 1850 | 16.0 | 12.0 | 36.8 |
| RETEST/SHORT|tier=A+ | 341 | 28.2 | 0.21 | 1.33 | 198 | 36.0 | 15.0 | 23.7 |
| RETEST/SHORT|tier=B | 2204 | 46.4 | 0.014 | 1.03 | 1013 | 18.0 | 13.0 | 34.1 |
| RETEST/SHORT|tier=C | 2700 | 47.2 | 0.08 | 1.17 | 1178 | 19.0 | 12.0 | 36.2 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 208 | 47.6 | 0.118 | 1.27 | 83 | 14.0 | 14.0 | 20.5 |
| INV/SHORT|aligned=1 | 152 | 46.1 | 0.061 | 1.13 | 71 | 20.0 | 14.0 | 26.8 |
| RETEST/LONG|aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 8546 | 47.3 | 0.092 | 1.19 | 3894 | 17.0 | 12.0 | 33.3 |
| RETEST/SHORT|aligned=1 | 5245 | 45.6 | 0.061 | 1.12 | 2389 | 19.0 | 13.0 | 34.2 |

## Autopsia de SL
n_losses=6438  causas: RR-bajo×2429, contra-estructura×2209, stop-en-el-minimo×2152, killzone-Asia-largo×1365, sin-nivel-detras×1293, estirado×1099, chop×940, SL-muy-pegado×777, sin-causa-clara×677, contra-sesgo×1
- INV/LONG (n=83): RR-bajo×37, killzone-Asia-largo×34, contra-estructura×23, estirado×19, stop-en-el-minimo×17, chop×10, sin-nivel-detras×10, SL-muy-pegado×7, sin-causa-clara×4
- INV/SHORT (n=71): RR-bajo×35, contra-estructura×20, stop-en-el-minimo×19, estirado×15, sin-causa-clara×13, SL-muy-pegado×9, chop×8, sin-nivel-detras×5
- RETEST/LONG (n=3895): RR-bajo×1464, contra-estructura×1416, killzone-Asia-largo×1331, stop-en-el-minimo×1298, sin-nivel-detras×799, estirado×639, chop×611, SL-muy-pegado×457, sin-causa-clara×328, contra-sesgo×1
- RETEST/SHORT (n=2389): RR-bajo×893, stop-en-el-minimo×818, contra-estructura×750, sin-nivel-detras×479, estirado×426, sin-causa-clara×332, chop×311, SL-muy-pegado×304

## Autopsia de SL · semana 2026-W39 (para revision semanal)
n_losses=420  causas: stop-en-el-minimo×170, RR-bajo×149, contra-estructura×138, killzone-Asia-largo×102, sin-nivel-detras×77, chop×67, sin-causa-clara×58, estirado×53, SL-muy-pegado×34
ejemplos por causa: {"stop-en-el-minimo": ["ES-1-20747-L", "NQ-2-20762-L", "GC-1-27888-S", "GC-1-28004-S", "NQ-1-21276-L"], "RR-bajo": ["NQ-1-21276-L", "ES-1-21309-L", "ES-1-21345-L", "NQ-1-21390-L", "NQ-2-21045-L"], "contra-estructura": ["NQ-2-20762-L", "GC-1-28004-S", "NQ-1-21276-L", "NQ-1-21630-L", "NQ-1-21631-L"]}

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
    "n": 13536,
    "naive_expR": 0.081,
    "managed_expR": 0.142,
    "delta": 0.062,
    "avgEntryBetterTk_p50": 2.4,
    "fill_t3plus_pct": 46.0,
    "fill_full_pct": 32.8,
    "m1_rate": 37.4,
    "m2_rate": 23.4,
    "m3_rate": 12.7,
    "beAfterM1_rate": 17.8
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 132,
      "naive_expR": 0.121,
      "managed_expR": 0.237,
      "delta": 0.116,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 51.5,
      "fill_full_pct": 38.6,
      "m1_rate": 40.2,
      "m2_rate": 25.8,
      "m3_rate": 13.6,
      "beAfterM1_rate": 21.2
    },
    "1m/INV/SHORT": {
      "n": 97,
      "naive_expR": 0.077,
      "managed_expR": 0.255,
      "delta": 0.179,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 50.5,
      "fill_full_pct": 41.2,
      "m1_rate": 37.1,
      "m2_rate": 22.7,
      "m3_rate": 14.4,
      "beAfterM1_rate": 18.6
    },
    "1m/RETEST/LONG": {
      "n": 5169,
      "naive_expR": 0.088,
      "managed_expR": 0.158,
      "delta": 0.071,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.6,
      "fill_full_pct": 34.4,
      "m1_rate": 37.9,
      "m2_rate": 23.8,
      "m3_rate": 12.6,
      "beAfterM1_rate": 17.1
    },
    "1m/RETEST/SHORT": {
      "n": 3134,
      "naive_expR": 0.056,
      "managed_expR": 0.158,
      "delta": 0.102,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 49.1,
      "fill_full_pct": 34.3,
      "m1_rate": 39.5,
      "m2_rate": 24.8,
      "m3_rate": 14.0,
      "beAfterM1_rate": 18.6
    },
    "2m/INV/LONG": {
      "n": 48,
      "naive_expR": 0.02,
      "managed_expR": -0.0,
      "delta": -0.02,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.9,
      "fill_full_pct": 35.4,
      "m1_rate": 22.9,
      "m2_rate": 16.7,
      "m3_rate": 4.2,
      "beAfterM1_rate": 6.2
    },
    "2m/INV/SHORT": {
      "n": 42,
      "naive_expR": -0.056,
      "managed_expR": -0.112,
      "delta": -0.056,
      "avgEntryBetterTk_p50": 3.65,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 42.9,
      "m1_rate": 23.8,
      "m2_rate": 21.4,
      "m3_rate": 11.9,
      "beAfterM1_rate": 4.8
    },
    "2m/RETEST/LONG": {
      "n": 2294,
      "naive_expR": 0.071,
      "managed_expR": 0.096,
      "delta": 0.025,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 42.4,
      "fill_full_pct": 29.5,
      "m1_rate": 35.4,
      "m2_rate": 21.1,
      "m3_rate": 11.3,
      "beAfterM1_rate": 18.1
    },
    "2m/RETEST/SHORT": {
      "n": 1351,
      "naive_expR": 0.062,
      "managed_expR": 0.133,
      "delta": 0.072,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 46.8,
      "fill_full_pct": 34.0,
      "m1_rate": 36.3,
      "m2_rate": 23.3,
      "m3_rate": 12.4,
      "beAfterM1_rate": 18.1
    },
    "5m/INV/LONG": {
      "n": 15,
      "naive_expR": 0.407,
      "managed_expR": 0.275,
      "delta": -0.132,
      "avgEntryBetterTk_p50": 1.3,
      "fill_t3plus_pct": 33.3,
      "fill_full_pct": 20.0,
      "m1_rate": 26.7,
      "m2_rate": 20.0,
      "m3_rate": 6.7,
      "beAfterM1_rate": 13.3
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
      "n": 782,
      "naive_expR": 0.181,
      "managed_expR": 0.118,
      "delta": -0.063,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 31.8,
      "fill_full_pct": 23.5,
      "m1_rate": 35.5,
      "m2_rate": 23.5,
      "m3_rate": 13.3,
      "beAfterM1_rate": 18.9
    },
    "5m/RETEST/SHORT": {
      "n": 463,
      "naive_expR": 0.09,
      "managed_expR": 0.131,
      "delta": 0.041,
      "avgEntryBetterTk_p50": 4.8,
      "fill_t3plus_pct": 43.2,
      "fill_full_pct": 27.9,
      "m1_rate": 36.9,
      "m2_rate": 22.5,
      "m3_rate": 12.7,
      "beAfterM1_rate": 18.8
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 11856,
    "layer_expR": 0.086,
    "orig_expR": 0.242,
    "delta_orig_minus_layer": 0.156,
    "delta_ci90": [
      0.117,
      0.195
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.6,
    "orig_wrTP1": 33.7,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.8,
    "orig_saved_from_SL": 20,
    "orig_caused_SL": 1782
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 331,
      "layer_expR": 0.093,
      "orig_expR": 0.104,
      "delta_orig_minus_layer": 0.011,
      "delta_ci90": [
        -0.222,
        0.282
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.6,
      "orig_wrTP1": 26.6,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 6.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 74
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
      "n": 9039,
      "layer_expR": 0.09,
      "orig_expR": 0.257,
      "delta_orig_minus_layer": 0.167,
      "delta_ci90": [
        0.124,
        0.209
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.1,
      "orig_wrTP1": 34.4,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.1,
      "orig_saved_from_SL": 18,
      "orig_caused_SL": 1347
    },
    "retestBar2": {
      "n": 2486,
      "layer_expR": 0.071,
      "orig_expR": 0.207,
      "delta_orig_minus_layer": 0.137,
      "delta_ci90": [
        0.054,
        0.224
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.9,
      "orig_wrTP1": 32.5,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 361
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 132,
      "layer_expR": 0.121,
      "orig_expR": -0.202,
      "delta_orig_minus_layer": -0.323,
      "delta_ci90": [
        -0.617,
        -0.025
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 47.0,
      "orig_wrTP1": 20.5,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 5.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 35
    },
    "1m/INV/SHORT": {
      "n": 87,
      "layer_expR": 0.079,
      "orig_expR": -0.006,
      "delta_orig_minus_layer": -0.085,
      "delta_ci90": [
        -0.42,
        0.291
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.6,
      "orig_wrTP1": 26.4,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 21
    },
    "1m/RETEST/LONG": {
      "n": 4493,
      "layer_expR": 0.091,
      "orig_expR": 0.223,
      "delta_orig_minus_layer": 0.132,
      "delta_ci90": [
        0.076,
        0.191
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.1,
      "orig_wrTP1": 30.0,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.0,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 770
    },
    "1m/RETEST/SHORT": {
      "n": 2611,
      "layer_expR": 0.063,
      "orig_expR": 0.205,
      "delta_orig_minus_layer": 0.142,
      "delta_ci90": [
        0.063,
        0.23
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.7,
      "orig_wrTP1": 32.2,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 379
    },
    "2m/INV/LONG": {
      "n": 48,
      "layer_expR": 0.02,
      "orig_expR": 1.189,
      "delta_orig_minus_layer": 1.169,
      "delta_ci90": [
        0.077,
        2.491
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.2,
      "orig_wrTP1": 33.3,
      "slTk_p50": 22.5,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 8.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 10
    },
    "2m/INV/SHORT": {
      "n": 41,
      "layer_expR": -0.067,
      "orig_expR": 0.313,
      "delta_orig_minus_layer": 0.381,
      "delta_ci90": [
        -0.058,
        0.957
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 31.7,
      "orig_wrTP1": 29.3,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 4.9,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 2
    },
    "2m/RETEST/LONG": {
      "n": 2081,
      "layer_expR": 0.083,
      "orig_expR": 0.223,
      "delta_orig_minus_layer": 0.14,
      "delta_ci90": [
        0.07,
        0.216
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.3,
      "orig_wrTP1": 36.7,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 285
    },
    "2m/RETEST/SHORT": {
      "n": 1167,
      "layer_expR": 0.074,
      "orig_expR": 0.224,
      "delta_orig_minus_layer": 0.15,
      "delta_ci90": [
        0.057,
        0.246
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.1,
      "orig_wrTP1": 36.9,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.8,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 156
    },
    "5m/INV/LONG": {
      "n": 15,
      "layer_expR": 0.407,
      "orig_expR": -0.402,
      "delta_orig_minus_layer": -0.809,
      "delta_ci90": [
        -1.327,
        -0.334
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 73.3,
      "orig_wrTP1": 40.0,
      "slTk_p50": 49.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 20.0,
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
      "n": 747,
      "layer_expR": 0.171,
      "orig_expR": 0.47,
      "delta_orig_minus_layer": 0.299,
      "delta_ci90": [
        0.127,
        0.484
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 55.6,
      "orig_wrTP1": 45.8,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 17.0,
      "orig_wider_pct": 15.8,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 79
    },
    "5m/RETEST/SHORT": {
      "n": 426,
      "layer_expR": 0.075,
      "orig_expR": 0.53,
      "delta_orig_minus_layer": 0.455,
      "delta_ci90": [
        0.119,
        0.842
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.9,
      "orig_wrTP1": 43.4,
      "slTk_p50": 31.5,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 21.8,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 39
    }
  }
}
```

## Contrafactual de entrada por RR minimo (candidato sc_min_rr, ataca causa RR-bajo)
```json
{
  "1/RETEST/LONG": {
    "baseline": {
      "n": 5116,
      "wrTP1": 48.2,
      "nSL": 2336,
      "nTO": 315,
      "expR": 0.075,
      "pf": 1.16,
      "mfe_p25": 6.0,
      "mfe_p50": 15.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 31.0,
      "ci90": {
        "expR": 0.075,
        "ci90": [
          0.045,
          0.103
        ],
        "p_mean_le_0": 0.001,
        "n": 4959
      }
    },
    "cuts": {
      "1.0": {
        "n": 2487,
        "wrTP1": 32.2,
        "nSL": 1445,
        "nTO": 240,
        "expR": 0.094,
        "pf": 1.16,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 46.5,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 22.5,
        "ci90": {
          "expR": 0.094,
          "ci90": [
            0.045,
            0.145
          ],
          "p_mean_le_0": 0.003,
          "n": 2387
        }
      },
      "1.2": {
        "n": 2055,
        "wrTP1": 29.4,
        "nSL": 1232,
        "nTO": 218,
        "expR": 0.108,
        "pf": 1.17,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 19.6,
        "ci90": {
          "expR": 0.108,
          "ci90": [
            0.051,
            0.167
          ],
          "p_mean_le_0": 0.002,
          "n": 1970
        }
      },
      "1.3": {
        "n": 1875,
        "wrTP1": 27.9,
        "nSL": 1139,
        "nTO": 212,
        "expR": 0.109,
        "pf": 1.17,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 18.5,
        "ci90": {
          "expR": 0.109,
          "ci90": [
            0.047,
            0.173
          ],
          "p_mean_le_0": 0.002,
          "n": 1792
        }
      },
      "1.5": {
        "n": 1580,
        "wrTP1": 25.7,
        "nSL": 980,
        "nTO": 194,
        "expR": 0.124,
        "pf": 1.19,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 16.5,
        "ci90": {
          "expR": 0.124,
          "ci90": [
            0.053,
            0.198
          ],
          "p_mean_le_0": 0.003,
          "n": 1508
        }
      },
      "2.0": {
        "n": 1025,
        "wrTP1": 19.2,
        "nSL": 670,
        "nTO": 158,
        "expR": 0.122,
        "pf": 1.18,
        "mfe_p25": 8.0,
        "mfe_p50": 21.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 18.400000000000006,
        "loserMFEbeforeSL_p50": 6.5,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 12.4,
        "ci90": {
          "expR": 0.122,
          "ci90": [
            0.027,
            0.218
          ],
          "p_mean_le_0": 0.017,
          "n": 980
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 3183,
      "wrTP1": 46.5,
      "nSL": 1430,
      "nTO": 274,
      "expR": 0.059,
      "pf": 1.12,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 22.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 33.8,
      "ci90": {
        "expR": 0.059,
        "ci90": [
          0.024,
          0.095
        ],
        "p_mean_le_0": 0.003,
        "n": 3005
      }
    },
    "cuts": {
      "1.0": {
        "n": 1557,
        "wrTP1": 31.7,
        "nSL": 865,
        "nTO": 198,
        "expR": 0.097,
        "pf": 1.16,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.69999999999999,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 23.7,
        "ci90": {
          "expR": 0.097,
          "ci90": [
            0.033,
            0.161
          ],
          "p_mean_le_0": 0.005,
          "n": 1441
        }
      },
      "1.2": {
        "n": 1273,
        "wrTP1": 29.2,
        "nSL": 721,
        "nTO": 180,
        "expR": 0.124,
        "pf": 1.2,
        "mfe_p25": 10.0,
        "mfe_p50": 25.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 20.7,
        "ci90": {
          "expR": 0.124,
          "ci90": [
            0.043,
            0.202
          ],
          "p_mean_le_0": 0.002,
          "n": 1172
        }
      },
      "1.3": {
        "n": 1165,
        "wrTP1": 27.4,
        "nSL": 672,
        "nTO": 174,
        "expR": 0.119,
        "pf": 1.19,
        "mfe_p25": 10.0,
        "mfe_p50": 25.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.19999999999999,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.5,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 19.9,
        "ci90": {
          "expR": 0.119,
          "ci90": [
            0.039,
            0.205
          ],
          "p_mean_le_0": 0.005,
          "n": 1069
        }
      },
      "1.5": {
        "n": 988,
        "wrTP1": 25.7,
        "nSL": 579,
        "nTO": 155,
        "expR": 0.139,
        "pf": 1.22,
        "mfe_p25": 11.0,
        "mfe_p50": 28.0,
        "mfe_p75": 57.75,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.0,
        "ci90": {
          "expR": 0.139,
          "ci90": [
            0.05,
            0.23
          ],
          "p_mean_le_0": 0.005,
          "n": 906
        }
      },
      "2.0": {
        "n": 677,
        "wrTP1": 21.3,
        "nSL": 410,
        "nTO": 123,
        "expR": 0.157,
        "pf": 1.23,
        "mfe_p25": 10.0,
        "mfe_p50": 29.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 21.700000000000017,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 13.2,
        "ci90": {
          "expR": 0.157,
          "ci90": [
            0.042,
            0.276
          ],
          "p_mean_le_0": 0.015,
          "n": 618
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 2309,
      "wrTP1": 49.5,
      "nSL": 1041,
      "nTO": 125,
      "expR": 0.056,
      "pf": 1.12,
      "mfe_p25": 7.75,
      "mfe_p50": 17.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 24.799999999999955,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 39.3,
      "ci90": {
        "expR": 0.056,
        "ci90": [
          0.015,
          0.098
        ],
        "p_mean_le_0": 0.007,
        "n": 2224
      }
    },
    "cuts": {
      "1.0": {
        "n": 1030,
        "wrTP1": 32.1,
        "nSL": 609,
        "nTO": 90,
        "expR": 0.07,
        "pf": 1.11,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.5,
        "revAfterSL_rate": 31.0,
        "ci90": {
          "expR": 0.07,
          "ci90": [
            -0.011,
            0.149
          ],
          "p_mean_le_0": 0.085,
          "n": 975
        }
      },
      "1.2": {
        "n": 850,
        "wrTP1": 28.9,
        "nSL": 527,
        "nTO": 77,
        "expR": 0.068,
        "pf": 1.1,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 12.75,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 28.5,
        "ci90": {
          "expR": 0.068,
          "ci90": [
            -0.027,
            0.163
          ],
          "p_mean_le_0": 0.116,
          "n": 806
        }
      },
      "1.3": {
        "n": 780,
        "wrTP1": 28.2,
        "nSL": 487,
        "nTO": 73,
        "expR": 0.083,
        "pf": 1.13,
        "mfe_p25": 10.0,
        "mfe_p50": 23.5,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.099999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 27.5,
        "ci90": {
          "expR": 0.083,
          "ci90": [
            -0.016,
            0.185
          ],
          "p_mean_le_0": 0.085,
          "n": 740
        }
      },
      "1.5": {
        "n": 628,
        "wrTP1": 25.6,
        "nSL": 397,
        "nTO": 70,
        "expR": 0.114,
        "pf": 1.17,
        "mfe_p25": 10.5,
        "mfe_p50": 24.0,
        "mfe_p75": 61.5,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 24.9,
        "ci90": {
          "expR": 0.114,
          "ci90": [
            -0.005,
            0.23
          ],
          "p_mean_le_0": 0.057,
          "n": 591
        }
      },
      "2.0": {
        "n": 390,
        "wrTP1": 20.5,
        "nSL": 261,
        "nTO": 49,
        "expR": 0.15,
        "pf": 1.21,
        "mfe_p25": 11.0,
        "mfe_p50": 28.0,
        "mfe_p75": 70.75,
        "winnerMAE_p75": 11.25,
        "winnerMAE_p90": 20.400000000000034,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.5,
        "revAfterSL_rate": 21.1,
        "ci90": {
          "expR": 0.15,
          "ci90": [
            -0.016,
            0.327
          ],
          "p_mean_le_0": 0.071,
          "n": 366
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 1337,
      "wrTP1": 50.3,
      "nSL": 585,
      "nTO": 80,
      "expR": 0.088,
      "pf": 1.19,
      "mfe_p25": 9.0,
      "mfe_p50": 21.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 12.25,
      "winnerMAE_p90": 28.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 43.4,
      "ci90": {
        "expR": 0.088,
        "ci90": [
          0.035,
          0.144
        ],
        "p_mean_le_0": 0.003,
        "n": 1287
      }
    },
    "cuts": {
      "1.0": {
        "n": 592,
        "wrTP1": 34.1,
        "nSL": 341,
        "nTO": 49,
        "expR": 0.133,
        "pf": 1.22,
        "mfe_p25": 14.0,
        "mfe_p50": 30.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 36.4,
        "ci90": {
          "expR": 0.133,
          "ci90": [
            0.03,
            0.245
          ],
          "p_mean_le_0": 0.011,
          "n": 569
        }
      },
      "1.2": {
        "n": 475,
        "wrTP1": 31.6,
        "nSL": 278,
        "nTO": 47,
        "expR": 0.176,
        "pf": 1.29,
        "mfe_p25": 15.0,
        "mfe_p50": 31.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 13.75,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 32.7,
        "ci90": {
          "expR": 0.176,
          "ci90": [
            0.051,
            0.297
          ],
          "p_mean_le_0": 0.009,
          "n": 452
        }
      },
      "1.3": {
        "n": 435,
        "wrTP1": 30.3,
        "nSL": 259,
        "nTO": 44,
        "expR": 0.175,
        "pf": 1.28,
        "mfe_p25": 15.25,
        "mfe_p50": 31.0,
        "mfe_p75": 72.75,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 31.7,
        "ci90": {
          "expR": 0.175,
          "ci90": [
            0.043,
            0.313
          ],
          "p_mean_le_0": 0.013,
          "n": 414
        }
      },
      "1.5": {
        "n": 366,
        "wrTP1": 28.1,
        "nSL": 221,
        "nTO": 42,
        "expR": 0.194,
        "pf": 1.3,
        "mfe_p25": 16.0,
        "mfe_p50": 32.5,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 27.799999999999997,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.9,
        "ci90": {
          "expR": 0.194,
          "ci90": [
            0.041,
            0.351
          ],
          "p_mean_le_0": 0.017,
          "n": 346
        }
      },
      "2.0": {
        "n": 243,
        "wrTP1": 26.7,
        "nSL": 145,
        "nTO": 33,
        "expR": 0.328,
        "pf": 1.52,
        "mfe_p25": 20.0,
        "mfe_p50": 36.5,
        "mfe_p75": 80.5,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 24.800000000000004,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 27.6,
        "ci90": {
          "expR": 0.328,
          "ci90": [
            0.127,
            0.528
          ],
          "p_mean_le_0": 0.002,
          "n": 230
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 797,
      "wrTP1": 54.6,
      "nSL": 308,
      "nTO": 54,
      "expR": 0.202,
      "pf": 1.49,
      "mfe_p25": 12.0,
      "mfe_p50": 28.0,
      "mfe_p75": 65.0,
      "winnerMAE_p75": 19.0,
      "winnerMAE_p90": 37.60000000000002,
      "loserMFEbeforeSL_p50": 1.5,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -36.0,
      "revAfterSL_rate": 53.9,
      "ci90": {
        "expR": 0.202,
        "ci90": [
          0.128,
          0.277
        ],
        "p_mean_le_0": 0.0,
        "n": 751
      }
    },
    "cuts": {
      "1.0": {
        "n": 337,
        "wrTP1": 38.9,
        "nSL": 167,
        "nTO": 39,
        "expR": 0.35,
        "pf": 1.64,
        "mfe_p25": 15.25,
        "mfe_p50": 37.0,
        "mfe_p75": 80.75,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -31.0,
        "revAfterSL_rate": 49.7,
        "ci90": {
          "expR": 0.35,
          "ci90": [
            0.192,
            0.508
          ],
          "p_mean_le_0": 0.0,
          "n": 306
        }
      },
      "1.2": {
        "n": 286,
        "wrTP1": 39.2,
        "nSL": 137,
        "nTO": 37,
        "expR": 0.45,
        "pf": 1.84,
        "mfe_p25": 15.0,
        "mfe_p50": 37.0,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 28.30000000000004,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.5,
        "revAfterSL_rate": 46.7,
        "ci90": {
          "expR": 0.45,
          "ci90": [
            0.282,
            0.626
          ],
          "p_mean_le_0": 0.0,
          "n": 257
        }
      },
      "1.3": {
        "n": 258,
        "wrTP1": 35.7,
        "nSL": 132,
        "nTO": 34,
        "expR": 0.408,
        "pf": 1.72,
        "mfe_p25": 15.0,
        "mfe_p50": 36.0,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 21.900000000000006,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.5,
        "revAfterSL_rate": 46.2,
        "ci90": {
          "expR": 0.408,
          "ci90": [
            0.222,
            0.596
          ],
          "p_mean_le_0": 0.0,
          "n": 232
        }
      },
      "1.5": {
        "n": 218,
        "wrTP1": 34.9,
        "nSL": 111,
        "nTO": 31,
        "expR": 0.467,
        "pf": 1.82,
        "mfe_p25": 15.0,
        "mfe_p50": 36.0,
        "mfe_p75": 83.5,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 21.5,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -31.5,
        "revAfterSL_rate": 42.3,
        "ci90": {
          "expR": 0.467,
          "ci90": [
            0.25,
            0.687
          ],
          "p_mean_le_0": 0.0,
          "n": 195
        }
      },
      "2.0": {
        "n": 138,
        "wrTP1": 31.2,
        "nSL": 73,
        "nTO": 22,
        "expR": 0.572,
        "pf": 1.97,
        "mfe_p25": 16.75,
        "mfe_p50": 43.0,
        "mfe_p75": 113.25,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 20.60000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -34.5,
        "revAfterSL_rate": 34.2,
        "ci90": {
          "expR": 0.572,
          "ci90": [
            0.275,
            0.872
          ],
          "p_mean_le_0": 0.002,
          "n": 124
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 475,
      "wrTP1": 50.7,
      "nSL": 193,
      "nTO": 41,
      "expR": 0.111,
      "pf": 1.25,
      "mfe_p25": 13.0,
      "mfe_p50": 31.0,
      "mfe_p75": 62.75,
      "winnerMAE_p75": 23.0,
      "winnerMAE_p90": 41.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -29.0,
      "revAfterSL_rate": 41.5,
      "ci90": {
        "expR": 0.111,
        "ci90": [
          0.019,
          0.21
        ],
        "p_mean_le_0": 0.022,
        "n": 438
      }
    },
    "cuts": {
      "1.0": {
        "n": 200,
        "wrTP1": 34.0,
        "nSL": 109,
        "nTO": 23,
        "expR": 0.147,
        "pf": 1.24,
        "mfe_p25": 21.5,
        "mfe_p50": 41.0,
        "mfe_p75": 73.5,
        "winnerMAE_p75": 24.25,
        "winnerMAE_p90": 40.300000000000004,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -26.5,
        "revAfterSL_rate": 33.0,
        "ci90": {
          "expR": 0.147,
          "ci90": [
            -0.04,
            0.339
          ],
          "p_mean_le_0": 0.102,
          "n": 180
        }
      },
      "1.2": {
        "n": 164,
        "wrTP1": 28.7,
        "nSL": 96,
        "nTO": 21,
        "expR": 0.106,
        "pf": 1.16,
        "mfe_p25": 22.0,
        "mfe_p50": 43.0,
        "mfe_p75": 72.0,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 38.599999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 30.2,
        "ci90": {
          "expR": 0.106,
          "ci90": [
            -0.114,
            0.343
          ],
          "p_mean_le_0": 0.229,
          "n": 145
        }
      },
      "1.3": {
        "n": 148,
        "wrTP1": 27.7,
        "nSL": 89,
        "nTO": 18,
        "expR": 0.078,
        "pf": 1.12,
        "mfe_p25": 22.0,
        "mfe_p50": 43.0,
        "mfe_p75": 72.25,
        "winnerMAE_p75": 23.0,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -26.5,
        "revAfterSL_rate": 28.1,
        "ci90": {
          "expR": 0.078,
          "ci90": [
            -0.164,
            0.331
          ],
          "p_mean_le_0": 0.29,
          "n": 132
        }
      },
      "1.5": {
        "n": 122,
        "wrTP1": 27.9,
        "nSL": 71,
        "nTO": 17,
        "expR": 0.159,
        "pf": 1.24,
        "mfe_p25": 26.0,
        "mfe_p50": 51.0,
        "mfe_p75": 76.0,
        "winnerMAE_p75": 24.0,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 28.2,
        "ci90": {
          "expR": 0.159,
          "ci90": [
            -0.121,
            0.458
          ],
          "p_mean_le_0": 0.178,
          "n": 107
        }
      },
      "2.0": {
        "n": 77,
        "wrTP1": 23.4,
        "nSL": 50,
        "nTO": 9,
        "expR": 0.105,
        "pf": 1.15,
        "mfe_p25": 28.0,
        "mfe_p50": 53.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 30.25,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 30.0,
        "ci90": {
          "expR": 0.105,
          "ci90": [
            -0.262,
            0.483
          ],
          "p_mean_le_0": 0.31,
          "n": 69
        }
      }
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 2991,
    "wrTP1": 44.6,
    "expR": -0.02
  },
  "2026-W37": {
    "n": 5243,
    "wrTP1": 46.8,
    "expR": 0.072
  },
  "2026-W38": {
    "n": 4894,
    "wrTP1": 46.3,
    "expR": 0.089
  },
  "2026-W39": {
    "n": 1032,
    "wrTP1": 53.2,
    "expR": 0.367
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 35,
      "wrTP1": 45.7,
      "expR": 0.243,
      "pf": 1.53
    },
    "1m/INV/SHORT": {
      "n": 19,
      "wrTP1": 68.4,
      "expR": 0.264,
      "pf": 1.95
    },
    "1m/RETEST/LONG": {
      "n": 1278,
      "wrTP1": 42.5,
      "expR": -0.019,
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
      "n": 640,
      "wrTP1": 46.2,
      "expR": -0.053,
      "pf": 0.9
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
      "n": 1554,
      "wrTP1": 45.3,
      "expR": 0.054,
      "pf": 1.11
    },
    "1m/RETEST/SHORT": {
      "n": 1700,
      "wrTP1": 44.8,
      "expR": 0.042,
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
      "n": 658,
      "wrTP1": 47.6,
      "expR": 0.035,
      "pf": 1.07
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
      "n": 215,
      "wrTP1": 52.1,
      "expR": 0.121,
      "pf": 1.27
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 59,
      "wrTP1": 40.7,
      "expR": -0.102,
      "pf": 0.81
    },
    "1m/INV/SHORT": {
      "n": 22,
      "wrTP1": 45.5,
      "expR": -0.098,
      "pf": 0.8
    },
    "1m/RETEST/LONG": {
      "n": 2030,
      "wrTP1": 48.3,
      "expR": 0.116,
      "pf": 1.25
    },
    "1m/RETEST/SHORT": {
      "n": 984,
      "wrTP1": 42.3,
      "expR": 0.099,
      "pf": 1.21
    },
    "2m/INV/LONG": {
      "n": 16,
      "wrTP1": 56.2,
      "expR": -0.059,
      "pf": 0.79
    },
    "2m/INV/SHORT": {
      "n": 4,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 898,
      "wrTP1": 47.0,
      "expR": 0.05,
      "pf": 1.1
    },
    "2m/RETEST/SHORT": {
      "n": 377,
      "wrTP1": 43.8,
      "expR": 0.005,
      "pf": 1.01
    },
    "5m/INV/LONG": {
      "n": 7,
      "wrTP1": 28.6,
      "expR": -0.478,
      "pf": 0.2
    },
    "5m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 321,
      "wrTP1": 50.8,
      "expR": 0.179,
      "pf": 1.44
    },
    "5m/RETEST/SHORT": {
      "n": 175,
      "wrTP1": 42.3,
      "expR": 0.105,
      "pf": 1.22
    }
  },
  "2026-W39": {
    "1m/INV/LONG": {
      "n": 11,
      "wrTP1": 63.6,
      "expR": 1.341,
      "pf": 8.38
    },
    "1m/INV/SHORT": {
      "n": 5,
      "wrTP1": 80.0,
      "expR": 0.31,
      "pf": 2.55
    },
    "1m/RETEST/LONG": {
      "n": 472,
      "wrTP1": 50.2,
      "expR": 0.37,
      "pf": 1.86
    },
    "1m/RETEST/SHORT": {
      "n": 207,
      "wrTP1": 52.7,
      "expR": 0.128,
      "pf": 1.28
    },
    "2m/INV/LONG": {
      "n": 8,
      "wrTP1": 62.5,
      "expR": 0.72,
      "pf": 3.88
    },
    "2m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 192,
      "wrTP1": 58.3,
      "expR": 0.694,
      "pf": 3.15
    },
    "2m/RETEST/SHORT": {
      "n": 76,
      "wrTP1": 51.3,
      "expR": -0.07,
      "pf": 0.85
    },
    "5m/RETEST/LONG": {
      "n": 38,
      "wrTP1": 63.2,
      "expR": 0.664,
      "pf": 2.94
    },
    "5m/RETEST/SHORT": {
      "n": 22,
      "wrTP1": 54.5,
      "expR": 0.169,
      "pf": 1.41
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 13042,
  "brier": 0.2235,
  "bias": -0.056,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.144
    },
    {
      "feature": "nearTk",
      "weight": -0.102
    },
    {
      "feature": "stretchAtr",
      "weight": -0.066
    },
    {
      "feature": "emaStack",
      "weight": 0.037
    },
    {
      "feature": "rvol",
      "weight": 0.034
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.031
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.026
    },
    {
      "feature": "aligned",
      "weight": -0.025
    },
    {
      "feature": "biasScore",
      "weight": -0.024
    },
    {
      "feature": "structDir",
      "weight": 0.023
    },
    {
      "feature": "nearEdge",
      "weight": 0.014
    },
    {
      "feature": "hourNY",
      "weight": 0.01
    },
    {
      "feature": "chopIdx",
      "weight": -0.006
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.171,
      "actual": 0.194,
      "n": 1304
    },
    {
      "bin": 1,
      "pred": 0.37,
      "actual": 0.318,
      "n": 1304
    },
    {
      "bin": 2,
      "pred": 0.452,
      "actual": 0.36,
      "n": 1304
    },
    {
      "bin": 3,
      "pred": 0.498,
      "actual": 0.393,
      "n": 1304
    },
    {
      "bin": 4,
      "pred": 0.535,
      "actual": 0.533,
      "n": 1305
    },
    {
      "bin": 5,
      "pred": 0.564,
      "actual": 0.546,
      "n": 1304
    },
    {
      "bin": 6,
      "pred": 0.589,
      "actual": 0.62,
      "n": 1304
    },
    {
      "bin": 7,
      "pred": 0.609,
      "actual": 0.668,
      "n": 1304
    },
    {
      "bin": 8,
      "pred": 0.63,
      "actual": 0.691,
      "n": 1304
    },
    {
      "bin": 9,
      "pred": 0.659,
      "actual": 0.739,
      "n": 1305
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 8234,
  "testN": 5926,
  "testWeeks": [
    "2026-W38",
    "2026-W39"
  ],
  "model_oos_brier": 0.2223,
  "model_oos_n": 5926,
  "best_scheme_in_sample": {
    "scheme": "fixed_2R",
    "trainExpR": 0.039
  },
  "best_scheme_oos_expR": 0.105
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.121,
    "ci90": [
      -0.093,
      0.36
    ],
    "p_mean_le_0": 0.192,
    "n": 132,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.077,
    "ci90": [
      -0.116,
      0.283
    ],
    "p_mean_le_0": 0.273,
    "n": 97,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.088,
    "ci90": [
      0.059,
      0.117
    ],
    "p_mean_le_0": 0.0,
    "n": 5173,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.055,
    "ci90": [
      0.017,
      0.093
    ],
    "p_mean_le_0": 0.006,
    "n": 3141,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.02,
    "ci90": [
      -0.221,
      0.276
    ],
    "p_mean_le_0": 0.444,
    "n": 48,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": -0.056,
    "ci90": [
      -0.39,
      0.323
    ],
    "p_mean_le_0": 0.613,
    "n": 42,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.072,
    "ci90": [
      0.027,
      0.114
    ],
    "p_mean_le_0": 0.004,
    "n": 2296,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.062,
    "ci90": [
      0.008,
      0.118
    ],
    "p_mean_le_0": 0.032,
    "n": 1351,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.407,
    "ci90": [
      0.031,
      0.819
    ],
    "p_mean_le_0": 0.04,
    "n": 15,
    "survives_fdr10": true
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
    "expR": 0.181,
    "ci90": [
      0.105,
      0.258
    ],
    "p_mean_le_0": 0.0,
    "n": 782,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.091,
    "ci90": [
      -0.001,
      0.19
    ],
    "p_mean_le_0": 0.053,
    "n": 464,
    "survives_fdr10": true
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
      "n": 4051,
      "wrTP1": 44.3,
      "expR": 0.112,
      "pf": 1.23,
      "defining_features": {
        "structDir": 0.96,
        "biasScore": 0.76,
        "emaStack": 0.73,
        "nearEdge": 0.7
      }
    },
    {
      "id": 1,
      "n": 2520,
      "wrTP1": 51.3,
      "expR": 0.109,
      "pf": 1.25,
      "defining_features": {
        "hourNY": 1.37,
        "atrPctUsed": -0.86,
        "emaStack": 0.56,
        "biasScore": 0.55
      }
    },
    {
      "id": 2,
      "n": 4984,
      "wrTP1": 45.1,
      "expR": 0.061,
      "pf": 1.13,
      "defining_features": {
        "biasScore": -1.22,
        "emaStack": -1.01,
        "nearEdge": -0.93,
        "structDir": -0.43
      }
    },
    {
      "id": 3,
      "n": 2605,
      "wrTP1": 48.7,
      "expR": 0.041,
      "pf": 1.09,
      "defining_features": {
        "structDir": -1.04,
        "biasScore": 0.61,
        "nearEdge": 0.49,
        "hourNY": -0.49
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
        "n": 30,
        "wrTP1": 56.7,
        "expR": 0.411
      },
      "YM": {
        "n": 57,
        "wrTP1": 36.8,
        "expR": 0.267
      },
      "ES": {
        "n": 19,
        "wrTP1": 57.9,
        "expR": -0.01
      },
      "GC": {
        "n": 22,
        "wrTP1": 27.3,
        "expR": -0.51
      },
      "NQ": {
        "n": 13,
        "wrTP1": 53.8,
        "expR": 0.116
      }
    },
    "expR_spread": 0.921,
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
        "n": 20,
        "wrTP1": 60.0,
        "expR": 0.139
      },
      "CL": {
        "n": 10,
        "wrTP1": 40.0,
        "expR": -0.186
      }
    },
    "expR_spread": 0.756,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 944,
        "wrTP1": 43.6,
        "expR": 0.071
      },
      "NQ": {
        "n": 1131,
        "wrTP1": 47.2,
        "expR": 0.092
      },
      "ES": {
        "n": 1195,
        "wrTP1": 49.7,
        "expR": 0.147
      },
      "CL": {
        "n": 1217,
        "wrTP1": 45.0,
        "expR": 0.029
      },
      "YM": {
        "n": 847,
        "wrTP1": 44.5,
        "expR": 0.103
      }
    },
    "expR_spread": 0.118,
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
        "n": 823,
        "wrTP1": 46.1,
        "expR": 0.065
      },
      "YM": {
        "n": 994,
        "wrTP1": 45.2,
        "expR": 0.105
      },
      "ES": {
        "n": 677,
        "wrTP1": 44.5,
        "expR": 0.008
      },
      "CL": {
        "n": 424,
        "wrTP1": 41.7,
        "expR": -0.034
      }
    },
    "expR_spread": 0.139,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 7,
        "wrTP1": 42.9,
        "expR": -0.376
      },
      "CL": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.137
      },
      "YM": {
        "n": 14,
        "wrTP1": 35.7,
        "expR": -0.36
      },
      "ES": {
        "n": 11,
        "wrTP1": 81.8,
        "expR": 0.375
      },
      "NQ": {
        "n": 12,
        "wrTP1": 50.0,
        "expR": 0.453
      }
    },
    "expR_spread": 0.829,
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
      },
      "CL": {
        "n": 3,
        "wrTP1": 0.0,
        "expR": -1.0
      }
    },
    "expR_spread": 1.324,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 521,
        "wrTP1": 49.1,
        "expR": 0.125
      },
      "GC": {
        "n": 378,
        "wrTP1": 47.1,
        "expR": 0.087
      },
      "CL": {
        "n": 562,
        "wrTP1": 47.9,
        "expR": 0.035
      },
      "ES": {
        "n": 525,
        "wrTP1": 51.2,
        "expR": 0.095
      },
      "YM": {
        "n": 402,
        "wrTP1": 42.5,
        "expR": 0.005
      }
    },
    "expR_spread": 0.12,
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
        "n": 307,
        "wrTP1": 47.2,
        "expR": 0.085
      },
      "NQ": {
        "n": 201,
        "wrTP1": 42.3,
        "expR": 0.075
      },
      "CL": {
        "n": 158,
        "wrTP1": 44.3,
        "expR": -0.178
      }
    },
    "expR_spread": 0.31,
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
        "n": 79,
        "wrTP1": 58.2,
        "expR": 0.336
      },
      "ES": {
        "n": 173,
        "wrTP1": 54.9,
        "expR": 0.287
      },
      "YM": {
        "n": 143,
        "wrTP1": 52.4,
        "expR": 0.213
      },
      "CL": {
        "n": 173,
        "wrTP1": 57.2,
        "expR": 0.263
      },
      "NQ": {
        "n": 265,
        "wrTP1": 45.3,
        "expR": -0.007
      }
    },
    "expR_spread": 0.343,
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
        "n": 108,
        "wrTP1": 39.8,
        "expR": 0.07
      },
      "YM": {
        "n": 162,
        "wrTP1": 49.4,
        "expR": 0.164
      },
      "CL": {
        "n": 54,
        "wrTP1": 44.4,
        "expR": 0.039
      }
    },
    "expR_spread": 0.181,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 7,
  "near_news_30m": {
    "n": 0
  },
  "away_from_news": {
    "n": 14160,
    "wrTP1": 46.6,
    "nSL": 6438,
    "nTO": 1118,
    "expR": 0.081,
    "pf": 1.17,
    "mfe_p25": 7.0,
    "mfe_p50": 18.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 33.4
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
      "asOf": "2026-09-21 (lunes). Primer dia habil con dato nuevo genuino tras el fin de semana (+72 pares en todo el bus). n de pares resueltos subio de 13132 a 13204.",
      "retest_1m_long": {
        "n": 4111,
        "deltaER_orig_minus_layer": 0.147,
        "ci90": [
          0.084,
          0.21
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 4078 a 4111, delta estable (0.152->0.147) -- decimotercera confirmacion."
      },
      "retest_1m_short": {
        "n": 2440,
        "deltaER_orig_minus_layer": 0.153,
        "ci90": [
          0.066,
          0.244
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 2432 a 2440, delta identico (0.153) -- decimotercera confirmacion."
      },
      "retest_2m_long": {
        "n": 1919,
        "deltaER_orig_minus_layer": 0.151,
        "ci90": [
          0.078,
          0.228
        ],
        "ci90_no_cruza_cero": true,
        "nota": "TERCERA lectura consecutiva con dato genuinamente nuevo (primera 09-18, segunda 09-19, el 09-20 fue fin de semana sin trade real y no conto): n subio de 1897 a 1919, delta estable (0.153->0.151), CI90 practicamente igual (limite inferior 0.079->0.078). Cumple el criterio de '2-3 lecturas seguidas' que el experimento se puso a si mismo -- SE PROMUEVE a candidato de la propuesta formal hoy, con la misma advertencia de historial volatil que se le puso a 5m LONG cuando se sumo."
      },
      "retest_2m_short": {
        "n": 1097,
        "deltaER_orig_minus_layer": 0.134,
        "ci90": [
          0.04,
          0.232
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 1092 a 1097, delta identico (0.134), limite inferior del CI90 practicamente igual (0.039->0.04) -- sigue candidato debil/al filo, no se promueve."
      },
      "retest_5m_long": {
        "n": 713,
        "deltaER_orig_minus_layer": 0.276,
        "ci90": [
          0.111,
          0.466
        ],
        "ci90_no_cruza_cero": true,
        "nota": "sin senales 5m LONG nuevas hoy (n identico a ayer, 713) -- no cuenta como lectura independiente nueva, se mantiene en su novena confirmacion."
      },
      "retest_5m_short": {
        "n": 409,
        "deltaER_orig_minus_layer": 0.489,
        "ci90": [
          0.138,
          0.896
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 408 a 409 (+1), delta practicamente identico (0.49->0.489) -- sigue siendo la lectura mas solida del experimento por margen."
      },
      "overall_by_basis_retestBar": {
        "n": 8374,
        "deltaER": 0.175,
        "ci90": [
          0.133,
          0.219
        ],
        "nota": "n subio de 8313 a 8374, delta estable (0.178->0.175) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba."
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
      "2026-09-19 (sabado): salto de dato grande, el mayor en varios dias (n 11452->13092, +1640; el bus asento de una vez los archivos de 2026-09-18, mismo 'forced update' inofensivo de origin/main de siempre). Los 4 segmentos ya propuestos el 09-13 (1m LONG/SHORT, 5m LONG/SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG y 1m SHORT suman su DUODECIMA confirmacion (ambos practicamente sin cambio de delta), 5m LONG su NOVENA lectura seguida (delta baja un poco, 0.312->0.276, sigue muy lejos de cero) y 5m SHORT sigue siendo el efecto mas grande. HALLAZGO DEL DIA: 2m LONG suma su SEGUNDA lectura seguida certificando y se fortalece mucho (delta 0.074->0.153, CI90 limite inferior 0.005->0.079) -- un paso mas cerca de cumplir el criterio de '2-3 lecturas' para sumarse a la propuesta formal (vigilar una tercera lectura). 2m SHORT tiene su mejor lectura hasta ahora (limite inferior del CI90 0.031->0.039) pero se mantiene un dia mas como candidato debil antes de promoverlo. Vista actualizada: candidatos solidos sin cambio = 1m LONG, 1m SHORT, 5m LONG, 5m SHORT (los 4 ya propuestos); candidato experimental en camino de promocion = 2m LONG (segunda lectura, falta una tercera); candidato debil/al filo = 2m SHORT. Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView -- con 4 segmentos solidos y un quinto candidato acercandose (2m LONG en su segunda confirmacion), esta sigue siendo la evidencia mas fuerte acumulada hasta ahora para aplicar el cambio.",
      "2026-09-20 (domingo, REVISION SEMANAL, cierre de 2026-W38): primer fin de semana sin ningun archivo signals/outcomes nuevo desde que arranco el bus -- los +37 pares resueltos de hoy en todo el bus son TIMEOUT forzado de senales pendientes desde el viernes, sin trade real nuevo. Por eso esta medicion (que solo usa pares con outcome real) da exactamente los mismos numeros que ayer en los 6 segmentos RETEST: 1m LONG n=4078 delta=0.152, 1m SHORT n=2432 delta=0.153, 2m LONG n=1897 delta=0.153, 2m SHORT n=1092 delta=0.134, 5m LONG n=713 delta=0.276, 5m SHORT n=408 delta=0.49 -- NO cuenta como una lectura independiente nueva para ningun candidato (2m LONG sigue en su segunda lectura, todavia sin la tercera que pedia el criterio de promocion). Revision semanal completa en reviews/2026-week-38.md: se mantiene la propuesta formal de 4 segmentos (1m LONG/SHORT, 5m LONG/SHORT) sin cambios; 2m LONG y 2m SHORT siguen fuera, mas cerca que nunca pero sin una tercera lectura genuina.",
      "2026-09-21 (lunes, primer dia habil con dato nuevo genuino tras el fin de semana, +72 pares en todo el bus): 1m LONG y 1m SHORT suman su DECIMOTERCERA confirmacion sin ningun retroceso (n=4111 y n=2440). 5m LONG y 5m SHORT no tuvieron senales 5m nuevas hoy (5m LONG n identico 713, 5m SHORT +1 a 409) -- se mantienen en su novena/decima lectura respectivamente, sin avance ni retroceso. HALLAZGO PRINCIPAL: 2m LONG cumple hoy su TERCERA lectura consecutiva con dato genuinamente nuevo sosteniendo la certificacion (delta 0.153->0.151, CI90 practicamente sin cambio) -- se GRADUA de 'candidato experimental, vigilar una tercera lectura' a candidato de la propuesta formal, con la misma advertencia de historial volatil que se le puso a 5m LONG cuando se sumo el 09-13. La propuesta pasa de 4 a 5 segmentos: 1m LONG, 1m SHORT, 2m LONG, 5m LONG, 5m SHORT. 2m SHORT sigue sin alcanzar el mismo umbral (delta identico a ayer, limite inferior del CI90 practicamente sin moverse, 0.039->0.04) -- sigue fuera de la propuesta. Sin cambios de estado: sigue 'proposed', changeDate null, esperando que Jesus aplique el cambio en TradingView -- con 5 segmentos ahora con evidencia solida/experimental, esta es la evidencia acumulada mas fuerte y mas amplia hasta ahora para aplicar el cambio."
    ],
    "beforeN": 13800,
    "afterN": 0,
    "before": {
      "n": 13800,
      "wrTP1": 46.6,
      "nSL": 6284,
      "nTO": 1081,
      "expR": 0.08,
      "pf": 1.17,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.7
    },
    "after": {
      "n": 0
    }
  },
  {
    "id": "sc-min-rr-cut-2026-09-20",
    "status": "proposed",
    "hypothesis": "Subir sc_min_rr (o sc_aplus_rr) para exigir mas RR desde el origen de la senal sube el E[R] en RETEST porque ataca directo la causa de SL dominante 'RR-bajo' (37-38% de las perdidas en RETEST toda la vida del bus). Contrapartida esperada: baja el win rate (menos senales pasan el filtro, y las que pasan tienen el TP mas lejos del SL) pero las que sobreviven pagan mas R, y el neto deberia mejorar -- misma logica que el experimento sl-retest-wick pero del lado de la ENTRADA (que senales se toman), no de la gestion (donde se pone el stop).",
    "param": "sc_min_rr / sc_aplus_rr",
    "from": "sin piso explicito medido hoy (rr1 crudo del indicador)",
    "to": "candidatos a evaluar: 1.2 / 1.3 / 1.5 / 2.0 (ver evidencia por segmento)",
    "changeDate": null,
    "segment": {
      "kind": "RETEST"
    },
    "targetMetric": "expR",
    "minAfterN": 40,
    "evidence": {
      "source": "nuevo corte permanente en analyze.py de hoy (rr1_threshold_cut): por cada segmento tf/kind/side de RETEST, compara el E[R]/WR/PF/CI90 del segmento completo contra el subconjunto que solo toma senales con rr1>=X (contrafactual de entrada, no cambia gestion ni SL). Llena el hueco que la revision de 2026-week-37 dejo pendiente ('no hay todavia un corte contrafactual de rr1>=X').",
      "asOf": "2026-09-20 (domingo), primera lectura, dato identico al de ayer (fin de semana sin trade nuevo, ver nota de sl-retest-wick arriba).",
      "1m_short": {
        "baseline_n": 2998,
        "baseline_expR": 0.051,
        "rr1_ge_1_2_n": 1219,
        "rr1_ge_1_2_expR": 0.101,
        "ci90": [
          0.026,
          0.181
        ],
        "wr_baseline": 45.8,
        "wr_cut": 28.4
      },
      "2m_short": {
        "baseline_n": 1267,
        "baseline_expR": 0.099,
        "rr1_ge_1_2_n": 457,
        "rr1_ge_1_2_expR": 0.2,
        "ci90": [
          0.068,
          0.328
        ],
        "wr_baseline": 50.0,
        "wr_cut": 31.9
      },
      "5m_long": {
        "baseline_n": 767,
        "baseline_expR": 0.183,
        "rr1_ge_1_2_n": 276,
        "rr1_ge_1_2_expR": 0.408,
        "ci90": [
          0.231,
          0.582
        ],
        "wr_baseline": 53.8,
        "wr_cut": 38.0
      },
      "1m_long": {
        "baseline_n": 4695,
        "baseline_expR": 0.039,
        "rr1_ge_1_2_n": 1886,
        "rr1_ge_1_2_expR": 0.041,
        "ci90": "practicamente sin cambio vs baseline, efecto plano/nulo en este segmento -- no generalizar del resto"
      },
      "nota": "1m SHORT, 2m SHORT y 5m LONG muestran una relacion consistente: subir el piso de rr1 sube E[R] y PF de forma monotona-ish con CI90 que no cruza cero en ningun escalon (aunque son subconjuntos anidados, no lecturas independientes -- no comparar los CI90 entre escalones como si fueran experimentos separados). 1m LONG y 2m LONG NO muestran el mismo efecto (practicamente plano). Esto es coherente con el coeficiente mas grande del modelo P(TP1) (rr1, peso -1.185): mas RR exigido = menos probabilidad de tocar TP1, pero el modelo no dice si el NETO en R mejora o empeora, que es justo lo que mide este corte."
    },
    "next_steps": [
      "2026-09-20: primera lectura, in-sample, un solo dia de dato (identico a ayer por el fin de semana). NO proponer un valor concreto de sc_min_rr todavia -- falta: (a) walk_forward.ready (solo 3 semanas de historial), (b) que el patron se sostenga con dato genuinamente nuevo en corridas futuras, (c) decidir el punto exacto del trade-off WR-vs-E[R] que Jesus esta dispuesto a aceptar (WR cae de ~46-54% a ~28-38% en los tres segmentos donde el efecto es real).",
      "Vigilar en corridas futuras: si 1m SHORT, 2m SHORT y 5m LONG siguen mostrando el mismo patron con muestra nueva, y si 1m LONG / 2m LONG se mantienen planos (en cuyo caso la regla seria 'sc_min_rr mas alto solo para esos 3 segmentos', no un cambio global).",
      "Cuando haya 2-3 lecturas independientes seguidas confirmando: sumar a la propuesta formal de la revision semanal con predictedDeltaER en predictions.jsonl, igual que se hizo con sl-retest-wick.",
      "2026-09-21 (lunes, segunda lectura, primera con dato genuinamente nuevo desde que se anadio el corte el 09-20): el patron se mantiene igual que el domingo -- 1m SHORT, 2m SHORT y 5m LONG siguen mostrando que subir el piso de rr1 sube E[R] y PF de forma consistente con CI90 que no cruza cero; 1m LONG y 2m LONG siguen practicamente planos. Todavia in-sample, todavia sin walk_forward.ready con suficientes semanas -- sigue sin proponerse un valor concreto de sc_min_rr. Vigilar 2-3 lecturas mas con dato nuevo antes de sumarlo a una propuesta formal."
    ],
    "beforeN": 13800,
    "afterN": 0,
    "before": {
      "n": 13800,
      "wrTP1": 46.6,
      "nSL": 6284,
      "nTO": 1081,
      "expR": 0.08,
      "pf": 1.17,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.7
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
    "date": "2026-09-22",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-21T19:04:36-05:00",
    "schema": "sa-plan-2",
    "cleanest": "NQ",
    "instruments": {
      "NQ": {
        "biasDay": "LONG",
        "biasSession": "LONG",
        "conviction": "media",
        "prevDay": {
          "type": {
            "es": "dia de tendencia alcista extrema cerrando en el tercio alto",
            "en": "an extreme uptrend day closing in the upper third"
          },
          "closedAt": {
            "es": "30768.25, a 94.5 pts del maximo del dia 30862.75 (86% del rango recorrido)",
            "en": "30768.25, 94.5 pts off the day's high of 30862.75 (86% of the range covered)"
          },
          "prior": {
            "es": "CONTINUACION largo",
            "en": "long CONTINUATION"
          },
          "note": {
            "es": "4a sesion de tendencia confirmada, 217% del ATR recorrido -- el dia mas caro del ciclo; salvo reversal confirmado en la apertura",
            "en": "4th confirmed trend session, 217% of ATR covered -- the most expensive day of the cycle; barring a confirmed reversal at the open"
          }
        },
        "gap": {
          "pts": 0.0,
          "ticks": 0,
          "filled": true,
          "size": {
            "es": "sin gap todavia",
            "en": "no gap yet"
          },
          "note": {
            "es": "el mercado reabre a las 17:00 CT; no hay gap real hasta entonces",
            "en": "the market reopens at 17:00 CT; there's no real gap until then"
          }
        },
        "weekendGap": null,
        "smt": {
          "state": "ninguna",
          "note": {
            "es": "NQ, ES e YM hicieron maximo de ciclo nuevo hoy, sin divergencia activa; YM cerro relativamente mas lejos de su propio maximo (21% del rango) que NQ/ES (10-14%), vigilar si eso se convierte en divergencia real manana",
            "en": "NQ, ES and YM all made a fresh cycle high today, no active divergence; YM closed relatively further from its own high (21% of the range) than NQ/ES (10-14%), watch if that turns into real divergence tomorrow"
          }
        },
        "frameConflict": {
          "on": false,
          "note": {
            "es": "diario y semanal +3/+3, estructura y sesion totalmente alineados alcistas; la divergencia SMT con YM que preocupaba se cerro",
            "en": "daily and weekly +3/+3, structure and session frame fully aligned bullish; the SMT divergence with YM that worried us has closed"
          }
        },
        "whipsawRisk": {
          "score": 0.35,
          "note": {
            "es": "tendencia limpia sin conflicto, pero tras el dia mas extremo medido (217% ATR, error de EM de 521 pts en NY) sube el riesgo de una pausa/digestion real en vez de continuacion directa",
            "en": "a clean trend with no conflict, but after the most extreme day measured (217% of ATR, a 521-pt NY EM miss) th
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 5418,
  "by_verdict": {
    "AVOID": {
      "n": 1414,
      "wrTP1": 45.3,
      "nSL": 701,
      "nTO": 73,
      "expR": 0.009,
      "pf": 1.02,
      "mfe_p25": 6.0,
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
      "n": 777,
      "wrTP1": 52.4,
      "nSL": 312,
      "nTO": 58,
      "expR": 0.199,
      "pf": 1.47,
      "mfe_p25": 11.0,
      "mfe_p50": 28.0,
      "mfe_p75": 55.0,
      "winnerMAE_p75": 17.5,
      "winnerMAE_p90": 31.400000000000034,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 38.8
    },
    "WAIT": {
      "n": 3227,
      "wrTP1": 48.0,
      "nSL": 1419,
      "nTO": 259,
      "expR": 0.079,
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
        -0.045,
        0.069
      ],
      "p_mean_le_0": 0.379,
      "n": 1368
    },
    "GO": {
      "expR": 0.199,
      "ci90": [
        0.123,
        0.28
      ],
      "p_mean_le_0": 0.0,
      "n": 738
    },
    "WAIT": {
      "expR": 0.079,
      "ci90": [
        0.044,
        0.115
      ],
      "p_mean_le_0": 0.0,
      "n": 3060
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1414,
      "wrTP1": 45.3,
      "nSL": 701,
      "nTO": 73,
      "expR": 0.009,
      "pf": 1.02,
      "mfe_p25": 6.0,
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
      "n": 4004,
      "wrTP1": 48.9,
      "nSL": 1731,
      "nTO": 317,
      "expR": 0.102,
      "pf": 1.22,
      "mfe_p25": 8.0,
      "mfe_p50": 20.0,
      "mfe_p75": 46.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 36.7
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.009,
      "ci90": [
        -0.045,
        0.069
      ],
      "p_mean_le_0": 0.379,
      "n": 1368
    },
    "GO_or_WAIT": {
      "expR": 0.102,
      "ci90": [
        0.07,
        0.135
      ],
      "p_mean_le_0": 0.0,
      "n": 3798
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
        "n": 11,
        "wrTP1": 54.5,
        "nSL": 4,
        "nTO": 1,
        "expR": -0.071,
        "pf": 0.82,
        "mfe_p25": 18.5,
        "mfe_p50": 26.0,
        "mfe_p75": 30.5,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 30.0,
        "loserMFEbeforeSL_p50": 9.5,
        "bars_win_p50": 6.5,
        "bars_loss_p50": 3.5,
        "entryZoneTk_p50": -48.0,
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
        "n": 816,
        "wrTP1": 46.6,
        "nSL": 407,
        "nTO": 29,
        "expR": -0.011,
        "pf": 0.98,
        "mfe_p25": 6.0,
        "mfe_p50": 13.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 30.7
      },
      "GO": {
        "n": 532,
        "wrTP1": 51.1,
        "nSL": 226,
        "nTO": 34,
        "expR": 0.187,
        "pf": 1.42,
        "mfe_p25": 10.0,
        "mfe_p50": 27.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 38.5
      },
      "WAIT": {
        "n": 1947,
        "wrTP1": 50.3,
        "nSL": 820,
        "nTO": 147,
        "expR": 0.143,
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
        "revAfterSL_rate": 37.7
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 562,
        "wrTP1": 43.6,
        "nSL": 276,
        "nTO": 41,
        "expR": 0.055,
        "pf": 1.11,
        "mfe_p25": 8.0,
        "mfe_p50": 16.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 39.5
      },
      "GO": {
        "n": 232,
        "wrTP1": 55.2,
        "nSL": 81,
        "nTO": 23,
        "expR": 0.234,
        "pf": 1.62,
        "mfe_p25": 13.0,
        "mfe_p50": 30.0,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 21.25,
        "winnerMAE_p90": 35.09999999999998,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 40.7
      },
      "WAIT": {
        "n": 1202,
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

## Modo sombra (peldano 0->1, gate en execution-ladder.md)
```json
{
  "rule": {
    "version": 1,
    "definedAt": "2026-09-20",
    "criteria": {
      "kind": [
        "RETEST"
      ],
      "tf_side": [
        "1/LONG",
        "1/SHORT",
        "2/SHORT",
        "5/LONG"
      ],
      "excludeSaVerdict": [
        "AVOID"
      ]
    },
    "rationale": "kind=RETEST (prioridad 1; INV no tiene ningun segmento con survives_fdr10=true todavia). tf/side limitado a los 4 segmentos que hoy sobreviven FDR10 en segment_significance (1m LONG, 1m SHORT, 2m SHORT, 5m LONG) -- 2m LONG y 5m SHORT quedan fuera porque su CI90 de E[R] cruza o roza cero. Se excluyen senales del dia/sesion en un instrumento con veredicto Session Analyst=AVOID: avoid_vs_rest_ci90.AVOID no es significativo (p_mean_le_0 alto) mientras GO y WAIT si lo son (session_analyst_cross). SL/objetivo = el mismo del indicador (3 capas); el SL estructural de experiments.json (sl-retest-wick) sigue 'proposed' sin changeDate, no se incorpora a la sombra hasta que tenga muestra post-cambio."
  },
  "shadow": {
    "n": 9823,
    "wrTP1": 46.4,
    "nSL": 4452,
    "nTO": 814,
    "expR": 0.087,
    "pf": 1.18,
    "mfe_p25": 7.0,
    "mfe_p50": 18.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 32.6
  },
  "shadow_ci90": {
    "expR": 0.087,
    "ci90": [
      0.065,
      0.107
    ],
    "p_mean_le_0": 0.0,
    "n": 9401
  },
  "raw_indicator": {
    "n": 13800,
    "wrTP1": 46.6,
    "nSL": 6284,
    "nTO": 1081,
    "expR": 0.08,
    "pf": 1.17,
    "mfe_p25": 7.0,
    "mfe_p50": 18.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 33.7
  },
  "raw_indicator_ci90": {
    "expR": 0.08,
    "ci90": [
      0.062,
      0.099
    ],
    "p_mean_le_0": 0.0,
    "n": 13207
  },
  "tier_ap_b_only": {
    "n": 6865,
    "wrTP1": 44.1,
    "nSL": 3256,
    "nTO": 583,
    "expR": 0.091,
    "pf": 1.18,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 31.0
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.091,
    "ci90": [
      0.064,
      0.117
    ],
    "p_mean_le_0": 0.0,
    "n": 6570
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```
