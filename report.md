# Scalp CC · report 2026-09-23T01:14Z
- signals=15192 outcomes=14573 pares_resueltos=15157 pendientes=35 huerfanos=34

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: semana ya cerrada 2026-W37 bajo de n=5389 a n=5199 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W38 bajo de n=4911 a n=4847 desde la corrida previa -- vigilar, puede ser deduplicacion.
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.245 vs 0.085, delta 0.16 CI90 [0.118, 0.201], n 9692). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.204 vs 0.057, delta 0.147 CI90 [0.065, 0.227], n 2689). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.192 CI90 [0.113, 0.268], n 764). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.063 CI90 [0.033, 0.096], n 3656). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.076, "ci90": [0.059, 0.093], "p_mean_le_0": 0.0, "n": 14539}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 149 | 44.3 | 0.159 | 1.35 | 62 | 13.0 | 11.75 | 17.7 |
| 1m/INV/SHORT | 107 | 46.7 | 0.018 | 1.04 | 48 | 18.0 | 11.0 | 16.7 |
| 1m/RETEST/LONG | 5747 | 46.1 | 0.075 | 1.15 | 2688 | 15.0 | 10.0 | 29.6 |
| 1m/RETEST/SHORT | 3561 | 44.3 | 0.046 | 1.09 | 1650 | 17.0 | 11.0 | 30.6 |
| 2m/INV/LONG | 54 | 51.9 | 0.012 | 1.03 | 21 | 12.5 | 9.25 | 19.0 |
| 2m/INV/SHORT | 44 | 36.4 | -0.04 | 0.93 | 24 | 17.0 | 15.5 | 37.5 |
| 2m/RETEST/LONG | 2534 | 48.3 | 0.077 | 1.16 | 1151 | 18.0 | 13.0 | 37.4 |
| 2m/RETEST/SHORT | 1501 | 48.2 | 0.066 | 1.14 | 678 | 21.0 | 12.5 | 39.2 |
| 5m/INV/LONG | 18 | 66.7 | 0.396 | 3.11 | 3 | 30.0 | 29.75 | 66.7 |
| 5m/INV/SHORT | 10 | 60.0 | 0.436 | 2.31 | 3 | 37.0 | 68.75 | 66.7 |
| 5m/RETEST/LONG | 885 | 52.5 | 0.189 | 1.44 | 357 | 31.0 | 19.0 | 51.0 |
| 5m/RETEST/SHORT | 547 | 47.9 | 0.103 | 1.22 | 232 | 34.0 | 23.0 | 36.2 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 1039 | 26.7 | 0.162 | 1.25 | 635 | 29.0 | 14.0 | 21.4 |
| B | 6299 | 46.8 | 0.071 | 1.15 | 2865 | 17.0 | 12.0 | 32.9 |
| C | 7819 | 49.3 | 0.068 | 1.15 | 3417 | 17.0 | 12.0 | 35.7 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 5550 | 49.5 | 0.105 | 1.23 | 2450 | 13.0 | 10.0 | 38.3 |
| London | 2294 | 46.1 | 0.038 | 1.07 | 1133 | 18.0 | 12.0 | 33.2 |
| NY | 2664 | 45.5 | 0.11 | 1.23 | 1184 | 24.0 | 15.5 | 36.2 |
| Sin KZ | 4649 | 44.4 | 0.04 | 1.08 | 2150 | 19.0 | 13.0 | 25.9 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 3329 | 44.5 | 0.048 | 1.1 | 1549 | 21.0 | 14.0 | 31.0 |
| edge=0 | 6789 | 49.3 | 0.068 | 1.15 | 3017 | 15.0 | 11.0 | 37.5 |
| edge=1 | 5039 | 44.7 | 0.104 | 1.21 | 2351 | 18.0 | 13.0 | 29.2 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 15148 | 46.7 | 0.076 | 1.16 | 6916 | 18.0 | 12.0 | 33.2 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 89 | 53.9 | 0.169 | 1.44 | 31 | 11.5 | 10.25 | 25.8 |
| INV/LONG|edge=1 | 128 | 43.8 | 0.111 | 1.25 | 53 | 16.5 | 15.5 | 15.1 |
| INV/SHORT|edge=-1 | 91 | 37.4 | -0.0 | 1.0 | 48 | 21.0 | 12.0 | 25.0 |
| INV/SHORT|edge=0 | 61 | 52.5 | -0.037 | 0.91 | 24 | 11.0 | 14.25 | 29.2 |
| INV/SHORT|edge=1 | 9 | 66.7 | 0.69 | 3.07 | 3 | 28.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 323 | 53.6 | 0.149 | 1.36 | 131 | 12.0 | 8.0 | 50.4 |
| RETEST/LONG|edge=0 | 4094 | 50.3 | 0.061 | 1.13 | 1833 | 15.0 | 11.0 | 38.1 |
| RETEST/LONG|edge=1 | 4749 | 44.4 | 0.104 | 1.21 | 2232 | 19.0 | 13.0 | 28.9 |
| RETEST/SHORT|edge=-1 | 2911 | 43.8 | 0.038 | 1.08 | 1368 | 22.0 | 15.0 | 29.3 |
| RETEST/SHORT|edge=0 | 2545 | 47.3 | 0.078 | 1.17 | 1129 | 17.0 | 11.0 | 37.1 |
| RETEST/SHORT|edge=1 | 153 | 55.6 | 0.06 | 1.14 | 63 | 14.0 | 9.0 | 55.6 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 69 | 43.5 | 0.173 | 1.37 | 31 | 16.0 | 14.0 | 9.7 |
| INV/LONG|tier=C | 152 | 50.0 | 0.125 | 1.32 | 55 | 13.0 | 12.25 | 25.5 |
| INV/SHORT|tier=B | 46 | 39.1 | -0.054 | 0.91 | 26 | 18.0 | 9.75 | 7.7 |
| INV/SHORT|tier=C | 115 | 47.0 | 0.059 | 1.13 | 49 | 18.5 | 22.25 | 34.7 |
| RETEST/LONG|tier=A+ | 693 | 25.5 | 0.129 | 1.2 | 436 | 26.0 | 14.0 | 20.0 |
| RETEST/LONG|tier=B | 3851 | 47.4 | 0.108 | 1.23 | 1735 | 17.0 | 12.0 | 33.4 |
| RETEST/LONG|tier=C | 4622 | 50.6 | 0.062 | 1.14 | 2025 | 16.0 | 12.0 | 36.6 |
| RETEST/SHORT|tier=A+ | 346 | 28.9 | 0.229 | 1.37 | 199 | 37.0 | 15.0 | 24.6 |
| RETEST/SHORT|tier=B | 2333 | 46.2 | 0.008 | 1.02 | 1073 | 18.0 | 13.0 | 33.5 |
| RETEST/SHORT|tier=C | 2930 | 47.3 | 0.076 | 1.16 | 1288 | 19.0 | 12.0 | 34.7 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 221 | 48.0 | 0.141 | 1.33 | 86 | 14.0 | 13.75 | 19.8 |
| INV/SHORT|aligned=1 | 161 | 44.7 | 0.026 | 1.05 | 75 | 18.0 | 14.25 | 25.3 |
| RETEST/LONG|aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 9157 | 47.3 | 0.086 | 1.18 | 4195 | 17.0 | 12.0 | 33.6 |
| RETEST/SHORT|aligned=1 | 5609 | 45.7 | 0.057 | 1.12 | 2560 | 19.0 | 13.0 | 33.4 |

## Autopsia de SL
n_losses=6917  causas: RR-bajo×2603, contra-estructura×2368, stop-en-el-minimo×2299, killzone-Asia-largo×1537, sin-nivel-detras×1399, estirado×1178, chop×1009, SL-muy-pegado×853, sin-causa-clara×714, contra-sesgo×1
- INV/LONG (n=86): RR-bajo×38, killzone-Asia-largo×36, contra-estructura×24, estirado×19, stop-en-el-minimo×17, chop×11, sin-nivel-detras×11, SL-muy-pegado×7, sin-causa-clara×4
- INV/SHORT (n=75): RR-bajo×37, contra-estructura×22, stop-en-el-minimo×19, estirado×16, sin-causa-clara×13, SL-muy-pegado×9, chop×8, sin-nivel-detras×5
- RETEST/LONG (n=4196): RR-bajo×1569, killzone-Asia-largo×1501, contra-estructura×1495, stop-en-el-minimo×1408, sin-nivel-detras×869, estirado×690, chop×659, SL-muy-pegado×500, sin-causa-clara×348, contra-sesgo×1
- RETEST/SHORT (n=2560): RR-bajo×959, stop-en-el-minimo×855, contra-estructura×827, sin-nivel-detras×514, estirado×453, sin-causa-clara×349, SL-muy-pegado×337, chop×331

## Autopsia de SL · semana 2026-W39 (para revision semanal)
n_losses=935  causas: RR-bajo×340, stop-en-el-minimo×327, contra-estructura×312, killzone-Asia-largo×286, sin-nivel-detras×189, estirado×138, chop×137, SL-muy-pegado×113, sin-causa-clara×100
ejemplos por causa: {"RR-bajo": ["NQ-1-21276-L", "ES-1-21309-L", "ES-1-21345-L", "NQ-1-21390-L", "NQ-2-21045-L"], "stop-en-el-minimo": ["ES-1-20747-L", "NQ-2-20762-L", "GC-1-27888-S", "GC-1-28004-S", "NQ-1-21276-L"], "contra-estructura": ["NQ-2-20762-L", "GC-1-28004-S", "NQ-1-21276-L", "NQ-1-21630-L", "NQ-1-21631-L"]}

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
    "n": 14525,
    "naive_expR": 0.076,
    "managed_expR": 0.139,
    "delta": 0.064,
    "avgEntryBetterTk_p50": 2.4,
    "fill_t3plus_pct": 46.0,
    "fill_full_pct": 32.7,
    "m1_rate": 37.5,
    "m2_rate": 23.3,
    "m3_rate": 12.6,
    "beAfterM1_rate": 18.0
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 140,
      "naive_expR": 0.159,
      "managed_expR": 0.25,
      "delta": 0.09,
      "avgEntryBetterTk_p50": 2.65,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 37.9,
      "m1_rate": 41.4,
      "m2_rate": 25.7,
      "m3_rate": 12.9,
      "beAfterM1_rate": 22.1
    },
    "1m/INV/SHORT": {
      "n": 103,
      "naive_expR": 0.018,
      "managed_expR": 0.163,
      "delta": 0.145,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 54.4,
      "fill_full_pct": 44.7,
      "m1_rate": 34.0,
      "m2_rate": 20.4,
      "m3_rate": 12.6,
      "beAfterM1_rate": 17.5
    },
    "1m/RETEST/LONG": {
      "n": 5580,
      "naive_expR": 0.075,
      "managed_expR": 0.151,
      "delta": 0.076,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 48.0,
      "fill_full_pct": 34.5,
      "m1_rate": 37.8,
      "m2_rate": 23.5,
      "m3_rate": 12.4,
      "beAfterM1_rate": 17.2
    },
    "1m/RETEST/SHORT": {
      "n": 3361,
      "naive_expR": 0.047,
      "managed_expR": 0.154,
      "delta": 0.108,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.8,
      "fill_full_pct": 33.9,
      "m1_rate": 39.2,
      "m2_rate": 24.4,
      "m3_rate": 13.5,
      "beAfterM1_rate": 18.5
    },
    "2m/INV/LONG": {
      "n": 52,
      "naive_expR": 0.012,
      "managed_expR": -0.015,
      "delta": -0.027,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 48.1,
      "fill_full_pct": 36.5,
      "m1_rate": 23.1,
      "m2_rate": 15.4,
      "m3_rate": 3.8,
      "beAfterM1_rate": 7.7
    },
    "2m/INV/SHORT": {
      "n": 44,
      "naive_expR": -0.04,
      "managed_expR": -0.079,
      "delta": -0.039,
      "avgEntryBetterTk_p50": 3.65,
      "fill_t3plus_pct": 52.3,
      "fill_full_pct": 40.9,
      "m1_rate": 25.0,
      "m2_rate": 20.5,
      "m3_rate": 11.4,
      "beAfterM1_rate": 6.8
    },
    "2m/RETEST/LONG": {
      "n": 2439,
      "naive_expR": 0.077,
      "managed_expR": 0.098,
      "delta": 0.022,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 42.4,
      "fill_full_pct": 29.8,
      "m1_rate": 35.7,
      "m2_rate": 21.2,
      "m3_rate": 11.4,
      "beAfterM1_rate": 18.4
    },
    "2m/RETEST/SHORT": {
      "n": 1443,
      "naive_expR": 0.066,
      "managed_expR": 0.135,
      "delta": 0.069,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 45.7,
      "fill_full_pct": 33.1,
      "m1_rate": 36.5,
      "m2_rate": 23.3,
      "m3_rate": 12.5,
      "beAfterM1_rate": 18.6
    },
    "5m/INV/LONG": {
      "n": 16,
      "naive_expR": 0.396,
      "managed_expR": 0.265,
      "delta": -0.131,
      "avgEntryBetterTk_p50": 0.65,
      "fill_t3plus_pct": 31.2,
      "fill_full_pct": 18.8,
      "m1_rate": 25.0,
      "m2_rate": 18.8,
      "m3_rate": 6.2,
      "beAfterM1_rate": 12.5
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
      "n": 835,
      "naive_expR": 0.189,
      "managed_expR": 0.128,
      "delta": -0.061,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 31.7,
      "fill_full_pct": 23.8,
      "m1_rate": 36.3,
      "m2_rate": 24.0,
      "m3_rate": 13.4,
      "beAfterM1_rate": 19.4
    },
    "5m/RETEST/SHORT": {
      "n": 503,
      "naive_expR": 0.102,
      "managed_expR": 0.137,
      "delta": 0.035,
      "avgEntryBetterTk_p50": 4.8,
      "fill_t3plus_pct": 42.9,
      "fill_full_pct": 28.2,
      "m1_rate": 38.4,
      "m2_rate": 23.3,
      "m3_rate": 12.5,
      "beAfterM1_rate": 20.1
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 12733,
    "layer_expR": 0.079,
    "orig_expR": 0.233,
    "delta_orig_minus_layer": 0.154,
    "delta_ci90": [
      0.118,
      0.19
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.6,
    "orig_wrTP1": 33.8,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 4.0,
    "orig_saved_from_SL": 20,
    "orig_caused_SL": 1895
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 2,
  "invalid_by_seg": {
    "1m/RETEST/LONG": 2
  },
  "by_basis": {
    "candle1": {
      "n": 352,
      "layer_expR": 0.09,
      "orig_expR": 0.14,
      "delta_orig_minus_layer": 0.049,
      "delta_ci90": [
        -0.177,
        0.305
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.3,
      "orig_wrTP1": 26.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 6.2,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 78
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
      "n": 9692,
      "layer_expR": 0.085,
      "orig_expR": 0.245,
      "delta_orig_minus_layer": 0.16,
      "delta_ci90": [
        0.118,
        0.201
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.1,
      "orig_wrTP1": 34.4,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 4.3,
      "orig_saved_from_SL": 18,
      "orig_caused_SL": 1439
    },
    "retestBar2": {
      "n": 2689,
      "layer_expR": 0.057,
      "orig_expR": 0.204,
      "delta_orig_minus_layer": 0.147,
      "delta_ci90": [
        0.065,
        0.227
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.7,
      "orig_wrTP1": 32.7,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.7,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 378
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 140,
      "layer_expR": 0.159,
      "orig_expR": -0.046,
      "delta_orig_minus_layer": -0.205,
      "delta_ci90": [
        -0.515,
        0.101
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.1,
      "orig_wrTP1": 21.4,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.5,
      "orig_wider_pct": 5.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 36
    },
    "1m/INV/SHORT": {
      "n": 93,
      "layer_expR": 0.014,
      "orig_expR": -0.07,
      "delta_orig_minus_layer": -0.084,
      "delta_ci90": [
        -0.412,
        0.262
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.3,
      "orig_wrTP1": 24.7,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 3.2,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 21
    },
    "1m/RETEST/LONG": {
      "n": 4836,
      "layer_expR": 0.078,
      "orig_expR": 0.205,
      "delta_orig_minus_layer": 0.126,
      "delta_ci90": [
        0.072,
        0.184
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.0,
      "orig_wrTP1": 30.0,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.1,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 826
    },
    "1m/RETEST/SHORT": {
      "n": 2814,
      "layer_expR": 0.051,
      "orig_expR": 0.202,
      "delta_orig_minus_layer": 0.151,
      "delta_ci90": [
        0.074,
        0.236
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.5,
      "orig_wrTP1": 32.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 396
    },
    "2m/INV/LONG": {
      "n": 52,
      "layer_expR": 0.012,
      "orig_expR": 1.128,
      "delta_orig_minus_layer": 1.115,
      "delta_ci90": [
        0.118,
        2.378
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.8,
      "orig_wrTP1": 32.7,
      "slTk_p50": 22.5,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 7.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 11
    },
    "2m/INV/SHORT": {
      "n": 43,
      "layer_expR": -0.051,
      "orig_expR": 0.252,
      "delta_orig_minus_layer": 0.303,
      "delta_ci90": [
        -0.12,
        0.851
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 34.9,
      "orig_wrTP1": 27.9,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 4.7,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 4
    },
    "2m/RETEST/LONG": {
      "n": 2218,
      "layer_expR": 0.082,
      "orig_expR": 0.233,
      "delta_orig_minus_layer": 0.151,
      "delta_ci90": [
        0.087,
        0.221
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.5,
      "orig_wrTP1": 37.0,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.3,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 300
    },
    "2m/RETEST/SHORT": {
      "n": 1252,
      "layer_expR": 0.078,
      "orig_expR": 0.218,
      "delta_orig_minus_layer": 0.139,
      "delta_ci90": [
        0.051,
        0.235
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.5,
      "orig_wrTP1": 37.1,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.8,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 169
    },
    "5m/INV/LONG": {
      "n": 16,
      "layer_expR": 0.396,
      "orig_expR": -0.314,
      "delta_orig_minus_layer": -0.711,
      "delta_ci90": [
        -1.239,
        -0.218
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 75.0,
      "orig_wrTP1": 43.8,
      "slTk_p50": 43.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 18.8,
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
      "n": 797,
      "layer_expR": 0.169,
      "orig_expR": 0.441,
      "delta_orig_minus_layer": 0.272,
      "delta_ci90": [
        0.117,
        0.439
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 55.6,
      "orig_wrTP1": 45.9,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 18.0,
      "orig_wider_pct": 16.3,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 83
    },
    "5m/RETEST/SHORT": {
      "n": 464,
      "layer_expR": 0.089,
      "orig_expR": 0.478,
      "delta_orig_minus_layer": 0.39,
      "delta_ci90": [
        0.094,
        0.756
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.1,
      "orig_wrTP1": 43.3,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 22.8,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 43
    }
  }
}
```

## Contrafactual de entrada por RR minimo (candidato sc_min_rr, ataca causa RR-bajo)
```json
{
  "1/RETEST/LONG": {
    "baseline": {
      "n": 5519,
      "wrTP1": 48.0,
      "nSL": 2543,
      "nTO": 325,
      "expR": 0.063,
      "pf": 1.13,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 31.3,
      "ci90": {
        "expR": 0.063,
        "ci90": [
          0.036,
          0.09
        ],
        "p_mean_le_0": 0.0,
        "n": 5360
      }
    },
    "cuts": {
      "1.0": {
        "n": 2684,
        "wrTP1": 31.9,
        "nSL": 1581,
        "nTO": 247,
        "expR": 0.069,
        "pf": 1.11,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 22.5,
        "ci90": {
          "expR": 0.069,
          "ci90": [
            0.021,
            0.117
          ],
          "p_mean_le_0": 0.009,
          "n": 2584
        }
      },
      "1.2": {
        "n": 2216,
        "wrTP1": 29.1,
        "nSL": 1348,
        "nTO": 223,
        "expR": 0.08,
        "pf": 1.13,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 19.9,
        "ci90": {
          "expR": 0.08,
          "ci90": [
            0.025,
            0.136
          ],
          "p_mean_le_0": 0.007,
          "n": 2131
        }
      },
      "1.3": {
        "n": 2019,
        "wrTP1": 27.5,
        "nSL": 1247,
        "nTO": 217,
        "expR": 0.078,
        "pf": 1.12,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 18.6,
        "ci90": {
          "expR": 0.078,
          "ci90": [
            0.017,
            0.141
          ],
          "p_mean_le_0": 0.019,
          "n": 1936
        }
      },
      "1.5": {
        "n": 1699,
        "wrTP1": 25.1,
        "nSL": 1074,
        "nTO": 198,
        "expR": 0.086,
        "pf": 1.13,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.400000000000034,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 16.5,
        "ci90": {
          "expR": 0.086,
          "ci90": [
            0.017,
            0.155
          ],
          "p_mean_le_0": 0.016,
          "n": 1627
        }
      },
      "2.0": {
        "n": 1091,
        "wrTP1": 18.8,
        "nSL": 725,
        "nTO": 161,
        "expR": 0.086,
        "pf": 1.12,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 12.1,
        "ci90": {
          "expR": 0.086,
          "ci90": [
            -0.008,
            0.178
          ],
          "p_mean_le_0": 0.065,
          "n": 1047
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 3399,
      "wrTP1": 46.5,
      "nSL": 1536,
      "nTO": 284,
      "expR": 0.052,
      "pf": 1.11,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 22.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 32.9,
      "ci90": {
        "expR": 0.052,
        "ci90": [
          0.017,
          0.087
        ],
        "p_mean_le_0": 0.004,
        "n": 3220
      }
    },
    "cuts": {
      "1.0": {
        "n": 1650,
        "wrTP1": 31.6,
        "nSL": 927,
        "nTO": 202,
        "expR": 0.084,
        "pf": 1.14,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 23.1,
        "ci90": {
          "expR": 0.084,
          "ci90": [
            0.018,
            0.147
          ],
          "p_mean_le_0": 0.018,
          "n": 1534
        }
      },
      "1.2": {
        "n": 1345,
        "wrTP1": 29.1,
        "nSL": 771,
        "nTO": 183,
        "expR": 0.111,
        "pf": 1.18,
        "mfe_p25": 10.0,
        "mfe_p50": 25.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 20.4,
        "ci90": {
          "expR": 0.111,
          "ci90": [
            0.034,
            0.184
          ],
          "p_mean_le_0": 0.004,
          "n": 1244
        }
      },
      "1.3": {
        "n": 1225,
        "wrTP1": 27.4,
        "nSL": 712,
        "nTO": 177,
        "expR": 0.113,
        "pf": 1.18,
        "mfe_p25": 11.0,
        "mfe_p50": 27.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 19.5,
        "ci90": {
          "expR": 0.113,
          "ci90": [
            0.036,
            0.195
          ],
          "p_mean_le_0": 0.007,
          "n": 1129
        }
      },
      "1.5": {
        "n": 1038,
        "wrTP1": 25.5,
        "nSL": 617,
        "nTO": 156,
        "expR": 0.125,
        "pf": 1.19,
        "mfe_p25": 11.0,
        "mfe_p50": 28.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 17.7,
        "ci90": {
          "expR": 0.125,
          "ci90": [
            0.039,
            0.219
          ],
          "p_mean_le_0": 0.011,
          "n": 956
        }
      },
      "2.0": {
        "n": 715,
        "wrTP1": 20.7,
        "nSL": 444,
        "nTO": 123,
        "expR": 0.124,
        "pf": 1.18,
        "mfe_p25": 10.0,
        "mfe_p50": 29.0,
        "mfe_p75": 61.25,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 12.6,
        "ci90": {
          "expR": 0.124,
          "ci90": [
            0.009,
            0.241
          ],
          "p_mean_le_0": 0.042,
          "n": 656
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 2453,
      "wrTP1": 49.9,
      "nSL": 1104,
      "nTO": 126,
      "expR": 0.063,
      "pf": 1.13,
      "mfe_p25": 7.5,
      "mfe_p50": 17.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 39.0,
      "ci90": {
        "expR": 0.063,
        "ci90": [
          0.022,
          0.105
        ],
        "p_mean_le_0": 0.006,
        "n": 2367
      }
    },
    "cuts": {
      "1.0": {
        "n": 1092,
        "wrTP1": 32.2,
        "nSL": 649,
        "nTO": 91,
        "expR": 0.074,
        "pf": 1.12,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 31.3,
        "ci90": {
          "expR": 0.074,
          "ci90": [
            -0.001,
            0.157
          ],
          "p_mean_le_0": 0.054,
          "n": 1036
        }
      },
      "1.2": {
        "n": 896,
        "wrTP1": 29.2,
        "nSL": 556,
        "nTO": 78,
        "expR": 0.08,
        "pf": 1.12,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 58.5,
        "winnerMAE_p75": 11.75,
        "winnerMAE_p90": 21.900000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.0,
        "ci90": {
          "expR": 0.08,
          "ci90": [
            -0.011,
            0.174
          ],
          "p_mean_le_0": 0.076,
          "n": 851
        }
      },
      "1.3": {
        "n": 819,
        "wrTP1": 28.7,
        "nSL": 510,
        "nTO": 74,
        "expR": 0.102,
        "pf": 1.16,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 11.5,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 27.6,
        "ci90": {
          "expR": 0.102,
          "ci90": [
            0.008,
            0.207
          ],
          "p_mean_le_0": 0.035,
          "n": 778
        }
      },
      "1.5": {
        "n": 660,
        "wrTP1": 26.1,
        "nSL": 417,
        "nTO": 71,
        "expR": 0.134,
        "pf": 1.2,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 61.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 22.900000000000006,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 25.4,
        "ci90": {
          "expR": 0.134,
          "ci90": [
            0.023,
            0.253
          ],
          "p_mean_le_0": 0.028,
          "n": 622
        }
      },
      "2.0": {
        "n": 414,
        "wrTP1": 21.3,
        "nSL": 276,
        "nTO": 50,
        "expR": 0.181,
        "pf": 1.25,
        "mfe_p25": 11.0,
        "mfe_p50": 28.0,
        "mfe_p75": 69.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.5,
        "bars_win_p50": 7.5,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 20.7,
        "ci90": {
          "expR": 0.181,
          "ci90": [
            0.017,
            0.358
          ],
          "p_mean_le_0": 0.036,
          "n": 389
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 1426,
      "wrTP1": 50.7,
      "nSL": 621,
      "nTO": 82,
      "expR": 0.093,
      "pf": 1.2,
      "mfe_p25": 9.0,
      "mfe_p50": 21.0,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 12.5,
      "winnerMAE_p90": 28.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 42.8,
      "ci90": {
        "expR": 0.093,
        "ci90": [
          0.041,
          0.143
        ],
        "p_mean_le_0": 0.002,
        "n": 1375
      }
    },
    "cuts": {
      "1.0": {
        "n": 626,
        "wrTP1": 34.5,
        "nSL": 359,
        "nTO": 51,
        "expR": 0.137,
        "pf": 1.23,
        "mfe_p25": 15.0,
        "mfe_p50": 30.5,
        "mfe_p75": 62.75,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 28.5,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 36.8,
        "ci90": {
          "expR": 0.137,
          "ci90": [
            0.036,
            0.234
          ],
          "p_mean_le_0": 0.013,
          "n": 602
        }
      },
      "1.2": {
        "n": 503,
        "wrTP1": 31.8,
        "nSL": 294,
        "nTO": 49,
        "expR": 0.173,
        "pf": 1.28,
        "mfe_p25": 16.0,
        "mfe_p50": 31.0,
        "mfe_p75": 70.5,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 33.3,
        "ci90": {
          "expR": 0.173,
          "ci90": [
            0.051,
            0.291
          ],
          "p_mean_le_0": 0.009,
          "n": 479
        }
      },
      "1.3": {
        "n": 459,
        "wrTP1": 30.3,
        "nSL": 273,
        "nTO": 47,
        "expR": 0.17,
        "pf": 1.27,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 72.25,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 28.200000000000003,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 32.2,
        "ci90": {
          "expR": 0.17,
          "ci90": [
            0.038,
            0.298
          ],
          "p_mean_le_0": 0.015,
          "n": 436
        }
      },
      "1.5": {
        "n": 385,
        "wrTP1": 28.3,
        "nSL": 233,
        "nTO": 43,
        "expR": 0.191,
        "pf": 1.3,
        "mfe_p25": 17.0,
        "mfe_p50": 33.0,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 30.0,
        "ci90": {
          "expR": 0.191,
          "ci90": [
            0.045,
            0.341
          ],
          "p_mean_le_0": 0.015,
          "n": 365
        }
      },
      "2.0": {
        "n": 253,
        "wrTP1": 26.5,
        "nSL": 152,
        "nTO": 34,
        "expR": 0.316,
        "pf": 1.5,
        "mfe_p25": 21.0,
        "mfe_p50": 36.0,
        "mfe_p75": 79.5,
        "winnerMAE_p75": 9.5,
        "winnerMAE_p90": 24.199999999999996,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 27.0,
        "ci90": {
          "expR": 0.316,
          "ci90": [
            0.122,
            0.517
          ],
          "p_mean_le_0": 0.005,
          "n": 240
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 848,
      "wrTP1": 54.8,
      "nSL": 330,
      "nTO": 53,
      "expR": 0.208,
      "pf": 1.51,
      "mfe_p25": 12.0,
      "mfe_p50": 29.0,
      "mfe_p75": 65.0,
      "winnerMAE_p75": 19.0,
      "winnerMAE_p90": 37.60000000000002,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -36.0,
      "revAfterSL_rate": 55.2,
      "ci90": {
        "expR": 0.208,
        "ci90": [
          0.138,
          0.282
        ],
        "p_mean_le_0": 0.0,
        "n": 803
      }
    },
    "cuts": {
      "1.0": {
        "n": 355,
        "wrTP1": 39.2,
        "nSL": 178,
        "nTO": 38,
        "expR": 0.369,
        "pf": 1.67,
        "mfe_p25": 16.0,
        "mfe_p50": 37.0,
        "mfe_p75": 80.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -31.0,
        "revAfterSL_rate": 51.1,
        "ci90": {
          "expR": 0.369,
          "ci90": [
            0.222,
            0.525
          ],
          "p_mean_le_0": 0.0,
          "n": 325
        }
      },
      "1.2": {
        "n": 303,
        "wrTP1": 39.3,
        "nSL": 148,
        "nTO": 36,
        "expR": 0.463,
        "pf": 1.86,
        "mfe_p25": 16.0,
        "mfe_p50": 37.0,
        "mfe_p75": 81.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 23.40000000000002,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 48.0,
        "ci90": {
          "expR": 0.463,
          "ci90": [
            0.289,
            0.634
          ],
          "p_mean_le_0": 0.0,
          "n": 275
        }
      },
      "1.3": {
        "n": 273,
        "wrTP1": 36.3,
        "nSL": 141,
        "nTO": 33,
        "expR": 0.436,
        "pf": 1.77,
        "mfe_p25": 16.0,
        "mfe_p50": 36.5,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 21.200000000000003,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 47.5,
        "ci90": {
          "expR": 0.436,
          "ci90": [
            0.243,
            0.634
          ],
          "p_mean_le_0": 0.0,
          "n": 248
        }
      },
      "1.5": {
        "n": 233,
        "wrTP1": 35.6,
        "nSL": 119,
        "nTO": 31,
        "expR": 0.503,
        "pf": 1.89,
        "mfe_p25": 16.25,
        "mfe_p50": 36.0,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 14.5,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.0,
        "revAfterSL_rate": 43.7,
        "ci90": {
          "expR": 0.503,
          "ci90": [
            0.29,
            0.726
          ],
          "p_mean_le_0": 0.0,
          "n": 210
        }
      },
      "2.0": {
        "n": 149,
        "wrTP1": 32.2,
        "nSL": 79,
        "nTO": 22,
        "expR": 0.625,
        "pf": 2.07,
        "mfe_p25": 20.5,
        "mfe_p50": 44.0,
        "mfe_p75": 113.5,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -35.0,
        "revAfterSL_rate": 36.7,
        "ci90": {
          "expR": 0.625,
          "ci90": [
            0.313,
            0.929
          ],
          "p_mean_le_0": 0.001,
          "n": 135
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 516,
      "wrTP1": 50.8,
      "nSL": 208,
      "nTO": 46,
      "expR": 0.126,
      "pf": 1.29,
      "mfe_p25": 13.0,
      "mfe_p50": 32.0,
      "mfe_p75": 63.0,
      "winnerMAE_p75": 23.0,
      "winnerMAE_p90": 41.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 1.5,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -30.0,
      "revAfterSL_rate": 40.4,
      "ci90": {
        "expR": 0.126,
        "ci90": [
          0.034,
          0.224
        ],
        "p_mean_le_0": 0.009,
        "n": 476
      }
    },
    "cuts": {
      "1.0": {
        "n": 224,
        "wrTP1": 35.7,
        "nSL": 120,
        "nTO": 24,
        "expR": 0.188,
        "pf": 1.32,
        "mfe_p25": 22.0,
        "mfe_p50": 41.0,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 24.0,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 32.5,
        "ci90": {
          "expR": 0.188,
          "ci90": [
            0.015,
            0.373
          ],
          "p_mean_le_0": 0.035,
          "n": 205
        }
      },
      "1.2": {
        "n": 185,
        "wrTP1": 30.8,
        "nSL": 106,
        "nTO": 22,
        "expR": 0.158,
        "pf": 1.25,
        "mfe_p25": 22.0,
        "mfe_p50": 43.0,
        "mfe_p75": 72.5,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 5.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 30.2,
        "ci90": {
          "expR": 0.158,
          "ci90": [
            -0.053,
            0.375
          ],
          "p_mean_le_0": 0.108,
          "n": 167
        }
      },
      "1.3": {
        "n": 168,
        "wrTP1": 30.4,
        "nSL": 98,
        "nTO": 19,
        "expR": 0.145,
        "pf": 1.23,
        "mfe_p25": 24.0,
        "mfe_p50": 43.0,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 28.6,
        "ci90": {
          "expR": 0.145,
          "ci90": [
            -0.076,
            0.374
          ],
          "p_mean_le_0": 0.141,
          "n": 153
        }
      },
      "1.5": {
        "n": 135,
        "wrTP1": 28.1,
        "nSL": 79,
        "nTO": 18,
        "expR": 0.174,
        "pf": 1.27,
        "mfe_p25": 27.0,
        "mfe_p50": 50.0,
        "mfe_p75": 77.0,
        "winnerMAE_p75": 24.0,
        "winnerMAE_p90": 43.10000000000003,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 27.8,
        "ci90": {
          "expR": 0.174,
          "ci90": [
            -0.087,
            0.443
          ],
          "p_mean_le_0": 0.131,
          "n": 121
        }
      },
      "2.0": {
        "n": 84,
        "wrTP1": 23.8,
        "nSL": 54,
        "nTO": 10,
        "expR": 0.159,
        "pf": 1.23,
        "mfe_p25": 30.0,
        "mfe_p50": 53.0,
        "mfe_p75": 85.0,
        "winnerMAE_p75": 32.25,
        "winnerMAE_p90": 42.50000000000002,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -31.5,
        "revAfterSL_rate": 29.6,
        "ci90": {
          "expR": 0.159,
          "ci90": [
            -0.18,
            0.527
          ],
          "p_mean_le_0": 0.22,
          "n": 77
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
    "n": 5199,
    "wrTP1": 46.8,
    "expR": 0.072
  },
  "2026-W38": {
    "n": 4847,
    "wrTP1": 46.3,
    "expR": 0.089
  },
  "2026-W39": {
    "n": 2120,
    "wrTP1": 50.5,
    "expR": 0.187
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
      "n": 54,
      "wrTP1": 40.7,
      "expR": 0.037,
      "pf": 1.07
    },
    "1m/RETEST/LONG": {
      "n": 1531,
      "wrTP1": 45.1,
      "expR": 0.054,
      "pf": 1.11
    },
    "1m/RETEST/SHORT": {
      "n": 1687,
      "wrTP1": 44.7,
      "expR": 0.038,
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
      "n": 656,
      "wrTP1": 47.6,
      "expR": 0.036,
      "pf": 1.07
    },
    "2m/RETEST/SHORT": {
      "n": 741,
      "wrTP1": 51.7,
      "expR": 0.153,
      "pf": 1.34
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
      "n": 231,
      "wrTP1": 52.4,
      "expR": 0.208,
      "pf": 1.46
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
      "n": 58,
      "wrTP1": 39.7,
      "expR": -0.146,
      "pf": 0.73
    },
    "1m/INV/SHORT": {
      "n": 22,
      "wrTP1": 45.5,
      "expR": -0.098,
      "pf": 0.8
    },
    "1m/RETEST/LONG": {
      "n": 2003,
      "wrTP1": 48.4,
      "expR": 0.117,
      "pf": 1.26
    },
    "1m/RETEST/SHORT": {
      "n": 976,
      "wrTP1": 42.4,
      "expR": 0.104,
      "pf": 1.22
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
      "n": 894,
      "wrTP1": 46.9,
      "expR": 0.047,
      "pf": 1.1
    },
    "2m/RETEST/SHORT": {
      "n": 375,
      "wrTP1": 44.0,
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
      "n": 319,
      "wrTP1": 50.8,
      "expR": 0.177,
      "pf": 1.44
    },
    "5m/RETEST/SHORT": {
      "n": 172,
      "wrTP1": 41.9,
      "expR": 0.096,
      "pf": 1.2
    }
  },
  "2026-W39": {
    "1m/INV/LONG": {
      "n": 20,
      "wrTP1": 60.0,
      "expR": 1.159,
      "pf": 8.73
    },
    "1m/INV/SHORT": {
      "n": 12,
      "wrTP1": 41.7,
      "expR": -0.24,
      "pf": 0.53
    },
    "1m/RETEST/LONG": {
      "n": 935,
      "wrTP1": 47.9,
      "expR": 0.151,
      "pf": 1.32
    },
    "1m/RETEST/SHORT": {
      "n": 456,
      "wrTP1": 48.0,
      "expR": 0.02,
      "pf": 1.04
    },
    "2m/INV/LONG": {
      "n": 12,
      "wrTP1": 58.3,
      "expR": 0.452,
      "pf": 2.36
    },
    "2m/INV/SHORT": {
      "n": 3,
      "wrTP1": 66.7,
      "expR": -0.143,
      "pf": 0.57
    },
    "2m/RETEST/LONG": {
      "n": 344,
      "wrTP1": 57.0,
      "expR": 0.465,
      "pf": 2.25
    },
    "2m/RETEST/SHORT": {
      "n": 175,
      "wrTP1": 51.4,
      "expR": 0.019,
      "pf": 1.04
    },
    "5m/INV/LONG": {
      "n": 1,
      "wrTP1": 100.0,
      "expR": 0.24,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": null,
      "pf": null
    },
    "5m/RETEST/LONG": {
      "n": 93,
      "wrTP1": 59.1,
      "expR": 0.449,
      "pf": 2.16
    },
    "5m/RETEST/SHORT": {
      "n": 68,
      "wrTP1": 51.5,
      "expR": 0.23,
      "pf": 1.57
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 13998,
  "brier": 0.2234,
  "bias": -0.059,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.139
    },
    {
      "feature": "nearTk",
      "weight": -0.1
    },
    {
      "feature": "stretchAtr",
      "weight": -0.052
    },
    {
      "feature": "emaStack",
      "weight": 0.049
    },
    {
      "feature": "rvol",
      "weight": 0.043
    },
    {
      "feature": "biasScore",
      "weight": -0.032
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.028
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.027
    },
    {
      "feature": "aligned",
      "weight": -0.024
    },
    {
      "feature": "nearEdge",
      "weight": 0.013
    },
    {
      "feature": "hourNY",
      "weight": -0.008
    },
    {
      "feature": "structDir",
      "weight": 0.007
    },
    {
      "feature": "chopIdx",
      "weight": -0.003
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.168,
      "actual": 0.194,
      "n": 1399
    },
    {
      "bin": 1,
      "pred": 0.37,
      "actual": 0.326,
      "n": 1400
    },
    {
      "bin": 2,
      "pred": 0.452,
      "actual": 0.357,
      "n": 1400
    },
    {
      "bin": 3,
      "pred": 0.498,
      "actual": 0.397,
      "n": 1400
    },
    {
      "bin": 4,
      "pred": 0.535,
      "actual": 0.511,
      "n": 1400
    },
    {
      "bin": 5,
      "pred": 0.565,
      "actual": 0.558,
      "n": 1399
    },
    {
      "bin": 6,
      "pred": 0.588,
      "actual": 0.609,
      "n": 1400
    },
    {
      "bin": 7,
      "pred": 0.608,
      "actual": 0.666,
      "n": 1400
    },
    {
      "bin": 8,
      "pred": 0.628,
      "actual": 0.7,
      "n": 1400
    },
    {
      "bin": 9,
      "pred": 0.659,
      "actual": 0.741,
      "n": 1400
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 8190,
  "testN": 6967,
  "testWeeks": [
    "2026-W38",
    "2026-W39"
  ],
  "model_oos_brier": 0.2231,
  "model_oos_n": 6967,
  "best_scheme_in_sample": {
    "scheme": "fixed_2R",
    "trainExpR": 0.039
  },
  "best_scheme_oos_expR": 0.091
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.159,
    "ci90": [
      -0.044,
      0.38
    ],
    "p_mean_le_0": 0.102,
    "n": 140,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.018,
    "ci90": [
      -0.171,
      0.211
    ],
    "p_mean_le_0": 0.418,
    "n": 103,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.075,
    "ci90": [
      0.046,
      0.104
    ],
    "p_mean_le_0": 0.0,
    "n": 5584,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.046,
    "ci90": [
      0.011,
      0.083
    ],
    "p_mean_le_0": 0.015,
    "n": 3368,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.012,
    "ci90": [
      -0.218,
      0.262
    ],
    "p_mean_le_0": 0.464,
    "n": 52,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": -0.04,
    "ci90": [
      -0.365,
      0.313
    ],
    "p_mean_le_0": 0.586,
    "n": 44,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.077,
    "ci90": [
      0.036,
      0.12
    ],
    "p_mean_le_0": 0.001,
    "n": 2441,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.066,
    "ci90": [
      0.014,
      0.116
    ],
    "p_mean_le_0": 0.019,
    "n": 1443,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.396,
    "ci90": [
      0.023,
      0.769
    ],
    "p_mean_le_0": 0.039,
    "n": 16,
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
    "expR": 0.189,
    "ci90": [
      0.117,
      0.264
    ],
    "p_mean_le_0": 0.0,
    "n": 835,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.103,
    "ci90": [
      0.012,
      0.197
    ],
    "p_mean_le_0": 0.029,
    "n": 504,
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
      "n": 4311,
      "wrTP1": 44.8,
      "expR": 0.118,
      "pf": 1.24,
      "defining_features": {
        "structDir": 0.95,
        "biasScore": 0.76,
        "emaStack": 0.74,
        "nearEdge": 0.69
      }
    },
    {
      "id": 1,
      "n": 2773,
      "wrTP1": 50.1,
      "expR": 0.073,
      "pf": 1.16,
      "defining_features": {
        "hourNY": 1.35,
        "atrPctUsed": -0.86,
        "biasScore": 0.57,
        "emaStack": 0.55
      }
    },
    {
      "id": 2,
      "n": 5362,
      "wrTP1": 45.2,
      "expR": 0.055,
      "pf": 1.11,
      "defining_features": {
        "biasScore": -1.21,
        "emaStack": -1.01,
        "nearEdge": -0.92,
        "structDir": -0.42
      }
    },
    {
      "id": 3,
      "n": 2711,
      "wrTP1": 49.2,
      "expR": 0.051,
      "pf": 1.11,
      "defining_features": {
        "structDir": -1.05,
        "biasScore": 0.61,
        "hourNY": -0.51,
        "nearEdge": 0.49
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
        "n": 31,
        "wrTP1": 54.8,
        "expR": 0.434
      },
      "YM": {
        "n": 58,
        "wrTP1": 34.5,
        "expR": 0.283
      },
      "ES": {
        "n": 22,
        "wrTP1": 63.6,
        "expR": 0.192
      },
      "GC": {
        "n": 24,
        "wrTP1": 33.3,
        "expR": -0.428
      },
      "NQ": {
        "n": 14,
        "wrTP1": 50.0,
        "expR": 0.036
      }
    },
    "expR_spread": 0.862,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 59,
        "wrTP1": 40.7,
        "expR": -0.052
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
        "n": 12,
        "wrTP1": 41.7,
        "expR": -0.178
      }
    },
    "expR_spread": 0.748,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 994,
        "wrTP1": 43.2,
        "expR": 0.048
      },
      "NQ": {
        "n": 1244,
        "wrTP1": 46.9,
        "expR": 0.073
      },
      "ES": {
        "n": 1353,
        "wrTP1": 48.6,
        "expR": 0.103
      },
      "CL": {
        "n": 1243,
        "wrTP1": 45.3,
        "expR": 0.034
      },
      "YM": {
        "n": 913,
        "wrTP1": 45.9,
        "expR": 0.12
      }
    },
    "expR_spread": 0.086,
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
        "n": 869,
        "wrTP1": 46.0,
        "expR": 0.054
      },
      "YM": {
        "n": 1051,
        "wrTP1": 43.8,
        "expR": 0.066
      },
      "ES": {
        "n": 677,
        "wrTP1": 44.5,
        "expR": 0.008
      },
      "CL": {
        "n": 549,
        "wrTP1": 44.6,
        "expR": 0.012
      }
    },
    "expR_spread": 0.08,
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
        "n": 15,
        "wrTP1": 33.3,
        "expR": -0.406
      },
      "ES": {
        "n": 12,
        "wrTP1": 83.3,
        "expR": 0.407
      },
      "NQ": {
        "n": 14,
        "wrTP1": 50.0,
        "expR": 0.375
      }
    },
    "expR_spread": 0.813,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 22,
        "wrTP1": 36.4,
        "expR": 0.079
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
        "n": 4,
        "wrTP1": 25.0,
        "expR": -0.665
      }
    },
    "expR_spread": 0.989,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 558,
        "wrTP1": 49.3,
        "expR": 0.117
      },
      "GC": {
        "n": 402,
        "wrTP1": 47.5,
        "expR": 0.077
      },
      "CL": {
        "n": 571,
        "wrTP1": 48.0,
        "expR": 0.039
      },
      "ES": {
        "n": 564,
        "wrTP1": 51.4,
        "expR": 0.089
      },
      "YM": {
        "n": 439,
        "wrTP1": 44.0,
        "expR": 0.061
      }
    },
    "expR_spread": 0.078,
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
        "n": 479,
        "wrTP1": 50.7,
        "expR": 0.139
      },
      "GC": {
        "n": 342,
        "wrTP1": 46.8,
        "expR": 0.053
      },
      "NQ": {
        "n": 201,
        "wrTP1": 42.3,
        "expR": 0.075
      },
      "CL": {
        "n": 204,
        "wrTP1": 48.0,
        "expR": -0.069
      }
    },
    "expR_spread": 0.208,
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
      },
      "ES": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.335
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
        "n": 90,
        "wrTP1": 54.4,
        "expR": 0.244
      },
      "ES": {
        "n": 185,
        "wrTP1": 54.1,
        "expR": 0.261
      },
      "YM": {
        "n": 158,
        "wrTP1": 53.8,
        "expR": 0.251
      },
      "CL": {
        "n": 178,
        "wrTP1": 57.3,
        "expR": 0.293
      },
      "NQ": {
        "n": 274,
        "wrTP1": 47.1,
        "expR": 0.02
      }
    },
    "expR_spread": 0.273,
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
        "n": 120,
        "wrTP1": 40.0,
        "expR": 0.076
      },
      "YM": {
        "n": 172,
        "wrTP1": 47.7,
        "expR": 0.148
      },
      "CL": {
        "n": 75,
        "wrTP1": 50.7,
        "expR": 0.152
      }
    },
    "expR_spread": 0.169,
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
    "n": 32,
    "wrTP1": 46.9,
    "nSL": 17,
    "nTO": 0,
    "expR": -0.129,
    "pf": 0.76,
    "mfe_p25": 2.0,
    "mfe_p50": 4.5,
    "mfe_p75": 15.25,
    "winnerMAE_p75": 3.5,
    "winnerMAE_p90": 21.199999999999992,
    "loserMFEbeforeSL_p50": 1.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 6.0,
    "entryZoneTk_p50": -5.0,
    "revAfterSL_rate": 29.4
  },
  "away_from_news": {
    "n": 15125,
    "wrTP1": 46.7,
    "nSL": 6900,
    "nTO": 1159,
    "expR": 0.076,
    "pf": 1.16,
    "mfe_p25": 7.0,
    "mfe_p50": 18.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 33.2
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
      "2026-09-21 (lunes, primer dia habil con dato nuevo genuino tras el fin de semana, +72 pares en todo el bus): 1m LONG y 1m SHORT suman su DECIMOTERCERA confirmacion sin ningun retroceso (n=4111 y n=2440). 5m LONG y 5m SHORT no tuvieron senales 5m nuevas hoy (5m LONG n identico 713, 5m SHORT +1 a 409) -- se mantienen en su novena/decima lectura respectivamente, sin avance ni retroceso. HALLAZGO PRINCIPAL: 2m LONG cumple hoy su TERCERA lectura consecutiva con dato genuinamente nuevo sosteniendo la certificacion (delta 0.153->0.151, CI90 practicamente sin cambio) -- se GRADUA de 'candidato experimental, vigilar una tercera lectura' a candidato de la propuesta formal, con la misma advertencia de historial volatil que se le puso a 5m LONG cuando se sumo el 09-13. La propuesta pasa de 4 a 5 segmentos: 1m LONG, 1m SHORT, 2m LONG, 5m LONG, 5m SHORT. 2m SHORT sigue sin alcanzar el mismo umbral (delta identico a ayer, limite inferior del CI90 practicamente sin moverse, 0.039->0.04) -- sigue fuera de la propuesta. Sin cambios de estado: sigue 'proposed', changeDate null, esperando que Jesus aplique el cambio en TradingView -- con 5 segmentos ahora con evidencia solida/experimental, esta es la evidencia acumulada mas fuerte y mas amplia hasta ahora para aplicar el cambio.",
      "2026-09-22 (martes, salto de dato grande y genuino: el bus asento de una vez el lote de +1027 outcomes de 2026-09-21, n total de pares resueltos 13204->14160): los 5 segmentos ya propuestos (1m LONG/SHORT, 2m LONG, 5m LONG/SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG y 1m SHORT suman su DECIMOCUARTA/DECIMOQUINTA confirmacion (n=4493 y n=2611, deltas estables 0.132 y 0.142), 2m LONG suma su CUARTA lectura seguida (n=2081, delta 0.14, practicamente identico a ayer) y 5m LONG/SHORT tienen su primera lectura con dato nuevo desde el 09-21 y ambos se fortalecen (5m LONG delta 0.276->0.299, 5m SHORT delta 0.489->0.455 -- este ultimo baja un poco pero sigue siendo el efecto mas grande). HALLAZGO DEL DIA: 2m SHORT tiene su MEJOR lectura hasta ahora -- el limite inferior del CI90 sube de 0.04 a 0.057 (+42%), la subida mas grande en varias corridas -- pero todavia queda por debajo del rango tipico de graduacion de los 5 segmentos ya promovidos (~0.07-0.08 de limite inferior); se mantiene un dia mas como candidato debil/al filo, mas cerca que nunca. Nota en paralelo (no de este experimento, mismo mecanismo de SL): en INV/LONG (buy-ifvg.md) 1m certifica por primera vez a favor del SL de 3 capas (delta -0.323, CI90 no cruza cero) y 2m certifica por primera vez a favor del SL de vela-1 (delta +1.169, CI90 muy ancho, n=48 todavia chico) -- direcciones opuestas entre si, ninguno accionable todavia, pero primera senal estadistica real de esta medicion fuera de RETEST. Sin cambios de estado en este experimento: sigue 'proposed', changeDate null."
    ],
    "beforeN": 14775,
    "afterN": 0,
    "before": {
      "n": 14775,
      "wrTP1": 46.7,
      "nSL": 6756,
      "nTO": 1116,
      "expR": 0.075,
      "pf": 1.16,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.5
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
      "2026-09-21 (lunes, segunda lectura, primera con dato genuinamente nuevo desde que se anadio el corte el 09-20): el patron se mantiene igual que el domingo -- 1m SHORT, 2m SHORT y 5m LONG siguen mostrando que subir el piso de rr1 sube E[R] y PF de forma consistente con CI90 que no cruza cero; 1m LONG y 2m LONG siguen practicamente planos. Todavia in-sample, todavia sin walk_forward.ready con suficientes semanas -- sigue sin proponerse un valor concreto de sc_min_rr. Vigilar 2-3 lecturas mas con dato nuevo antes de sumarlo a una propuesta formal.",
      "2026-09-22 (martes, tercera lectura, con el lote grande de dato nuevo genuino del dia -- +1027 outcomes en todo el bus): 1m SHORT (cut>=1.2 n=1273 expR=0.124 CI90=[0.043,0.202]), 2m SHORT (n=475 expR=0.176 CI90=[0.051,0.297]) y 5m LONG (n=286 expR=0.45 CI90=[0.282,0.626]) siguen mostrando el mismo patron monotono, sin reversion en la tercera lectura. CAMBIO A VIGILAR: 1m LONG, que llevaba dos lecturas practicamente plano, hoy muestra un CI90 que ya no cruza cero (n=2055 expR=0.108 CI90=[0.051,0.167] vs baseline expR=0.075) -- todavia mas debil que los otros tres segmentos, pero ya no es claramente 'sin efecto'; 2m LONG sigue el mas debil/plano (n=850 expR=0.068 CI90=[-0.027,0.163], cruza cero). walk_forward.ready=true desde hace unos dias pero este corte especifico (rr1_threshold_cut) sigue sin evaluarse contra el split OOS -- pendiente antes de proponer un valor concreto. Sigue sin proponerse sc_min_rr en la revision semanal (la ultima fue el 09-20); revisar el patron de 1m LONG una vez mas el domingo antes de decidir si se suma a la propuesta."
    ],
    "beforeN": 14775,
    "afterN": 0,
    "before": {
      "n": 14775,
      "wrTP1": 46.7,
      "nSL": 6756,
      "nTO": 1116,
      "expR": 0.075,
      "pf": 1.16,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.5
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
    "date": "2026-09-23",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-22T19:20:41-05:00",
    "schema": "sa-plan-2",
    "cleanest": "YM",
    "focus": {
      "sym": "YM",
      "verdict": "WAIT",
      "window": "20:00-23:00 CT",
      "setup": {
        "es": "corto en el rechazo del FVG de 1h 52263-52379 (cluster EMA20/EMA50/VWAP), a favor del reinicio bajista recien confirmado",
        "en": "short on rejection at the 1h FVG 52263-52379 (EMA20/EMA50/VWAP cluster), with the freshly-confirmed bearish restart"
      },
      "trigger": {
        "es": "cierre 5m de vuelta bajo 52283 tras un toque del FVG de 1h 52263-52379",
        "en": "a 5m close back below 52283 after a tag of the 1h FVG 52263-52379"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 52400 (techo del FVG 1h mas colchon)",
        "en": "a sustained 5m close above 52400 (the 1h FVG ceiling plus cushion)"
      },
      "note": {
        "es": "el precio sigue encerrado dentro del FVG sin dar el rechazo real -- no vendas el primer toque; y recuerda que YM ya rompio 4 tesis de 1 dia en 2 semanas, protege la ganancia si aparece rapido",
        "en": "price is still locked inside the FVG without giving the real rejection -- don't sell the first tag; and remember YM has already broken 4 one-day theses in 2 weeks, protect the gain if it shows up fast"
      }
    },
    "summary": {
      "es": [
        "!! la tesis alcista de YM se rompio: cerro 52263, bajo su invalidacion 52344, devolviendo 581 pts del reclamo",
        "NQ: 5a sesion de tendencia alcista, maximo de ciclo nuevo 31065.50, pero SMT bajista real (ES/YM no confirmaron) -- convicción media, mercado sin reabrir",
        "ES: primera grieta real tras 4 dias limpios -- toco el PDH por 5 ticks y revirtio a un cierre rojo; conflicto de marcos activo, conviccion baja",
        "GC: el dia mas violento medido -- nuevo minimo de ciclo y luego maximo a 9 pts de invalidar el corto; division real sesion-vs-fondo, sesgo NEUTRAL por honestidad",
        "YM: rompio su 4a tesis de 1 dia en 2 semanas, la mas violenta -- ahora es el instrumento mas limpio por alineamiento (4 marcos bajistas sin fisura)",
        "CL: reinicio bajista confirmado 3a sesion pese al round-trip mas extremo del bus -- hoy es gestion, el EIA de mañana 09:30 CT es el catalizador real",
        "mas limpio: YM",
        "limite $1000 por cuenta -> maxContracts sale 0-1 en las mejores zonas de hoy; en GC/ES/CL el stop no cabe en full, usa micros o pasala",
        "sin datos de ejecucion de ayer (live/journal.json sin actualizar desde 2026-09-21) -- no se pudo cruzar plan vs ejecucion real"
      ],
      "en": [
        "!! YM's bullish thesis broke: it closed at 52263, below its 52344 invalidation, giving back 581 pts of the reclaim",
        "NQ: 5th bullish trend session, fresh cycle high 31065.50, but real bearish SMT (ES/YM didn't confirm) -- medium convictio
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 6022,
  "by_verdict": {
    "AVOID": {
      "n": 1400,
      "wrTP1": 45.0,
      "nSL": 697,
      "nTO": 73,
      "expR": 0.005,
      "pf": 1.01,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 31.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.100000000000023,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 34.1
    },
    "GO": {
      "n": 803,
      "wrTP1": 52.2,
      "nSL": 326,
      "nTO": 58,
      "expR": 0.192,
      "pf": 1.45,
      "mfe_p25": 10.0,
      "mfe_p50": 26.5,
      "mfe_p75": 53.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 31.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 37.7
    },
    "WAIT": {
      "n": 3819,
      "wrTP1": 47.7,
      "nSL": 1718,
      "nTO": 279,
      "expR": 0.063,
      "pf": 1.13,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 34.6
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.005,
      "ci90": [
        -0.05,
        0.06
      ],
      "p_mean_le_0": 0.434,
      "n": 1354
    },
    "GO": {
      "expR": 0.192,
      "ci90": [
        0.113,
        0.268
      ],
      "p_mean_le_0": 0.0,
      "n": 764
    },
    "WAIT": {
      "expR": 0.063,
      "ci90": [
        0.033,
        0.096
      ],
      "p_mean_le_0": 0.001,
      "n": 3656
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1400,
      "wrTP1": 45.0,
      "nSL": 697,
      "nTO": 73,
      "expR": 0.005,
      "pf": 1.01,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 31.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.100000000000023,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 34.1
    },
    "GO_or_WAIT": {
      "n": 4622,
      "wrTP1": 48.5,
      "nSL": 2044,
      "nTO": 337,
      "expR": 0.085,
      "pf": 1.18,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 35.1
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.005,
      "ci90": [
        -0.05,
        0.06
      ],
      "p_mean_le_0": 0.434,
      "n": 1354
    },
    "GO_or_WAIT": {
      "expR": 0.085,
      "ci90": [
        0.056,
        0.115
      ],
      "p_mean_le_0": 0.0,
      "n": 4420
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
        "n": 56,
        "wrTP1": 39.3,
        "nSL": 27,
        "nTO": 7,
        "expR": -0.089,
        "pf": 0.82,
        "mfe_p25": 7.0,
        "mfe_p50": 17.0,
        "mfe_p75": 33.0,
        "winnerMAE_p75": 18.5,
        "winnerMAE_p90": 24.900000000000002,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.5,
        "revAfterSL_rate": 18.5
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 22,
        "wrTP1": 31.8,
        "nSL": 13,
        "nTO": 2,
        "expR": -0.403,
        "pf": 0.35,
        "mfe_p25": 6.0,
        "mfe_p50": 13.0,
        "mfe_p75": 21.0,
        "winnerMAE_p75": 5.0,
        "winnerMAE_p90": 7.200000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -10.5,
        "revAfterSL_rate": 15.4
      },
      "WAIT": {
        "n": 38,
        "wrTP1": 42.1,
        "nSL": 18,
        "nTO": 4,
        "expR": -0.232,
        "pf": 0.55,
        "mfe_p25": 6.0,
        "mfe_p50": 18.0,
        "mfe_p75": 35.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 69.5,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 8.0,
        "entryZoneTk_p50": -12.5,
        "revAfterSL_rate": 33.3
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 803,
        "wrTP1": 46.2,
        "nSL": 403,
        "nTO": 29,
        "expR": -0.018,
        "pf": 0.97,
        "mfe_p25": 6.0,
        "mfe_p50": 14.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 31.0
      },
      "GO": {
        "n": 557,
        "wrTP1": 51.0,
        "nSL": 240,
        "nTO": 33,
        "expR": 0.177,
        "pf": 1.4,
        "mfe_p25": 9.0,
        "mfe_p50": 25.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 30.700000000000017,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 37.1
      },
      "WAIT": {
        "n": 2316,
        "wrTP1": 49.6,
        "nSL": 1014,
        "nTO": 153,
        "expR": 0.115,
        "pf": 1.25,
        "mfe_p25": 7.0,
        "mfe_p50": 17.0,
        "mfe_p75": 40.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.200000000000045,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 36.7
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
        "n": 233,
        "wrTP1": 54.9,
        "nSL": 81,
        "nTO": 24,
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
        "n": 1409,
        "wrTP1": 45.1,
        "nSL": 659,
        "nTO": 115,
        "expR": -0.011,
        "pf": 0.98,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 26.600000000000023,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 32.2
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
    "n": 10622,
    "wrTP1": 46.4,
    "nSL": 4847,
    "nTO": 842,
    "expR": 0.078,
    "pf": 1.16,
    "mfe_p25": 7.0,
    "mfe_p50": 17.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 32.5
  },
  "shadow_ci90": {
    "expR": 0.078,
    "ci90": [
      0.055,
      0.097
    ],
    "p_mean_le_0": 0.0,
    "n": 10197
  },
  "raw_indicator": {
    "n": 14775,
    "wrTP1": 46.7,
    "nSL": 6756,
    "nTO": 1116,
    "expR": 0.075,
    "pf": 1.16,
    "mfe_p25": 7.0,
    "mfe_p50": 18.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 33.5
  },
  "raw_indicator_ci90": {
    "expR": 0.075,
    "ci90": [
      0.058,
      0.092
    ],
    "p_mean_le_0": 0.0,
    "n": 14175
  },
  "tier_ap_b_only": {
    "n": 7223,
    "wrTP1": 44.0,
    "nSL": 3443,
    "nTO": 600,
    "expR": 0.084,
    "pf": 1.17,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.25,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 31.2
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.084,
    "ci90": [
      0.055,
      0.111
    ],
    "p_mean_le_0": 0.0,
    "n": 6919
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```
