# Scalp CC · report 2026-09-04T01:14Z
- signals=2430 outcomes=2342 pares_resueltos=2400 pendientes=30 huerfanos=22

## ⚠ ALERTAS (llevar al frente del resumen)
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.142 vs -0.035, delta 0.177 CI90 [0.077, 0.292], n 1639). Candidato para experiments.json + revision semanal.

- E[R] global: {"expR": -0.014, "ci90": [-0.056, 0.03], "p_mean_le_0": 0.708, "n": 2320}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 30 | 50.0 | 0.428 | 2.02 | 12 | 11.0 | 6.5 | 16.7 |
| 1m/INV/SHORT | 18 | 66.7 | 0.222 | 1.75 | 5 | 11.0 | 31.75 | 40.0 |
| 1m/RETEST/LONG | 993 | 43.2 | -0.004 | 0.99 | 502 | 12.0 | 9.0 | 27.1 |
| 1m/RETEST/SHORT | 412 | 44.4 | 0.015 | 1.03 | 188 | 14.0 | 9.5 | 37.8 |
| 2m/INV/LONG | 12 | 41.7 | -0.233 | 0.6 | 7 | 6.5 | 7.0 | 28.6 |
| 2m/INV/SHORT | 6 | 50.0 | -0.267 | 0.47 | 3 | 8.5 | 14.0 | 33.3 |
| 2m/RETEST/LONG | 491 | 42.8 | -0.13 | 0.76 | 264 | 16.0 | 14.0 | 36.4 |
| 2m/RETEST/SHORT | 191 | 41.9 | -0.08 | 0.85 | 95 | 17.0 | 16.5 | 43.2 |
| 5m/INV/LONG | 2 | 100.0 | 0.5 | 99.0 | 0 | 105.5 | 120.5 | None |
| 5m/INV/SHORT | 4 | 75.0 | 0.018 | 1.07 | 1 | 56.5 | 88.5 | 100.0 |
| 5m/RETEST/LONG | 157 | 54.8 | 0.169 | 1.4 | 64 | 25.0 | 19.0 | 53.1 |
| 5m/RETEST/SHORT | 84 | 50.0 | 0.03 | 1.06 | 36 | 30.5 | 29.75 | 30.6 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 154 | 20.8 | -0.012 | 0.98 | 94 | 16.0 | 16.5 | 12.8 |
| B | 949 | 45.3 | 0.031 | 1.06 | 466 | 17.0 | 14.0 | 30.5 |
| C | 1297 | 46.9 | -0.048 | 0.9 | 617 | 13.0 | 11.25 | 39.4 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 1038 | 47.0 | -0.02 | 0.96 | 476 | 10.0 | 8.0 | 41.8 |
| London | 326 | 46.6 | -0.09 | 0.83 | 173 | 20.0 | 14.0 | 44.5 |
| NY | 348 | 46.8 | 0.298 | 1.63 | 162 | 39.0 | 21.0 | 27.8 |
| Sin KZ | 688 | 38.8 | -0.133 | 0.76 | 366 | 14.0 | 12.0 | 20.8 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 432 | 44.2 | -0.029 | 0.94 | 201 | 17.0 | 20.5 | 32.3 |
| edge=0 | 1118 | 46.4 | -0.045 | 0.91 | 544 | 11.0 | 9.0 | 41.2 |
| edge=1 | 850 | 42.4 | 0.032 | 1.06 | 432 | 19.0 | 14.0 | 25.0 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| aligned=1 | 2389 | 44.5 | -0.016 | 0.97 | 1176 | 14.0 | 13.0 | 33.8 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=0 | 20 | 50.0 | 0.137 | 1.27 | 10 | 7.5 | 5.0 | 30.0 |
| INV/LONG|edge=1 | 24 | 50.0 | 0.346 | 1.87 | 9 | 20.5 | 11.75 | 11.1 |
| INV/SHORT|edge=-1 | 11 | 72.7 | 0.196 | 1.72 | 3 | 18.0 | 53.5 | 0.0 |
| INV/SHORT|edge=0 | 15 | 60.0 | 0.047 | 1.13 | 5 | 12.0 | 74.0 | 80.0 |
| INV/SHORT|edge=1 | 2 | 50.0 | -0.29 | 0.42 | 1 | 7.0 | 5.0 | 0.0 |
| RETEST/LONG|edge=-1 | 97 | 45.4 | 0.007 | 1.01 | 40 | 9.0 | 7.25 | 50.0 |
| RETEST/LONG|edge=0 | 785 | 47.1 | -0.069 | 0.87 | 393 | 11.0 | 8.0 | 38.7 |
| RETEST/LONG|edge=1 | 759 | 41.0 | 0.016 | 1.03 | 397 | 21.0 | 14.5 | 23.7 |
| RETEST/SHORT|edge=-1 | 324 | 42.9 | -0.048 | 0.91 | 158 | 24.5 | 21.0 | 28.5 |
| RETEST/SHORT|edge=0 | 298 | 43.6 | 0.006 | 1.01 | 136 | 13.0 | 11.75 | 47.8 |
| RETEST/SHORT|edge=1 | 65 | 55.4 | 0.11 | 1.27 | 25 | 13.0 | 9.0 | 52.0 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 13 | 53.8 | 0.577 | 2.65 | 4 | 19.0 | 7.0 | 0.0 |
| INV/LONG|tier=C | 31 | 48.4 | 0.114 | 1.24 | 15 | 9.0 | 8.0 | 26.7 |
| INV/SHORT|tier=B | 7 | 71.4 | 0.201 | 1.71 | 2 | 9.0 | 12.0 | 0.0 |
| INV/SHORT|tier=C | 21 | 61.9 | 0.041 | 1.12 | 7 | 19.5 | 74.0 | 57.1 |
| RETEST/LONG|tier=A+ | 97 | 18.6 | -0.021 | 0.97 | 57 | 14.0 | 18.25 | 7.0 |
| RETEST/LONG|tier=B | 635 | 43.0 | 0.022 | 1.04 | 334 | 16.0 | 12.0 | 28.7 |
| RETEST/LONG|tier=C | 909 | 47.7 | -0.059 | 0.88 | 439 | 12.0 | 10.0 | 37.8 |
| RETEST/SHORT|tier=A+ | 57 | 24.6 | 0.003 | 1.0 | 37 | 28.5 | 8.0 | 21.6 |
| RETEST/SHORT|tier=B | 294 | 49.3 | 0.02 | 1.04 | 126 | 19.5 | 20.0 | 36.5 |
| RETEST/SHORT|tier=C | 336 | 43.5 | -0.038 | 0.92 | 156 | 14.0 | 12.75 | 44.2 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 44 | 50.0 | 0.251 | 1.56 | 19 | 10.0 | 7.0 | 21.1 |
| INV/SHORT|aligned=1 | 28 | 64.3 | 0.083 | 1.25 | 9 | 13.0 | 60.5 | 44.4 |
| RETEST/LONG|aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| RETEST/LONG|aligned=1 | 1630 | 44.1 | -0.027 | 0.95 | 829 | 14.0 | 11.5 | 32.1 |
| RETEST/SHORT|aligned=1 | 687 | 44.4 | -0.01 | 0.98 | 319 | 16.0 | 16.0 | 38.6 |

## Autopsia de SL
n_losses=1177  causas: RR-bajo×474, contra-estructura×456, stop-en-el-minimo×397, killzone-Asia-largo×314, sin-nivel-detras×248, estirado×194, chop×177, SL-muy-pegado×129, sin-causa-clara×111, contra-sesgo×1
- INV/LONG (n=19): killzone-Asia-largo×11, RR-bajo×9, contra-estructura×7, stop-en-el-minimo×4, estirado×4, sin-nivel-detras×3, SL-muy-pegado×2, chop×1
- INV/SHORT (n=9): contra-estructura×6, RR-bajo×6, stop-en-el-minimo×4, chop×1, sin-causa-clara×1, SL-muy-pegado×1
- RETEST/LONG (n=830): RR-bajo×338, contra-estructura×316, killzone-Asia-largo×303, stop-en-el-minimo×266, sin-nivel-detras×187, chop×132, estirado×122, SL-muy-pegado×86, sin-causa-clara×63, contra-sesgo×1
- RETEST/SHORT (n=319): contra-estructura×127, stop-en-el-minimo×123, RR-bajo×121, estirado×68, sin-nivel-detras×58, sin-causa-clara×47, chop×43, SL-muy-pegado×40

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
    "n": 2305,
    "naive_expR": -0.015,
    "managed_expR": 0.068,
    "delta": 0.083,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 48.8,
    "fill_full_pct": 33.7,
    "m1_rate": 34.1,
    "m2_rate": 20.7,
    "m3_rate": 11.2,
    "beAfterM1_rate": 16.6
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 30,
      "naive_expR": 0.428,
      "managed_expR": 0.535,
      "delta": 0.108,
      "avgEntryBetterTk_p50": 0.9,
      "fill_t3plus_pct": 30.0,
      "fill_full_pct": 26.7,
      "m1_rate": 50.0,
      "m2_rate": 40.0,
      "m3_rate": 20.0,
      "beAfterM1_rate": 20.0
    },
    "1m/INV/SHORT": {
      "n": 17,
      "naive_expR": 0.222,
      "managed_expR": 0.574,
      "delta": 0.352,
      "avgEntryBetterTk_p50": 4.2,
      "fill_t3plus_pct": 41.2,
      "fill_full_pct": 35.3,
      "m1_rate": 41.2,
      "m2_rate": 23.5,
      "m3_rate": 5.9,
      "beAfterM1_rate": 17.6
    },
    "1m/RETEST/LONG": {
      "n": 971,
      "naive_expR": -0.005,
      "managed_expR": 0.052,
      "delta": 0.057,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 50.4,
      "fill_full_pct": 36.8,
      "m1_rate": 32.6,
      "m2_rate": 19.3,
      "m3_rate": 11.1,
      "beAfterM1_rate": 15.0
    },
    "1m/RETEST/SHORT": {
      "n": 380,
      "naive_expR": 0.02,
      "managed_expR": 0.165,
      "delta": 0.146,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 49.2,
      "fill_full_pct": 29.2,
      "m1_rate": 40.8,
      "m2_rate": 25.5,
      "m3_rate": 13.2,
      "beAfterM1_rate": 20.0
    },
    "2m/INV/LONG": {
      "n": 12,
      "naive_expR": -0.233,
      "managed_expR": -0.219,
      "delta": 0.014,
      "avgEntryBetterTk_p50": 1.8,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 33.3,
      "m1_rate": 16.7,
      "m2_rate": 16.7,
      "m3_rate": 0.0,
      "beAfterM1_rate": 0.0
    },
    "2m/INV/SHORT": {
      "n": 6,
      "naive_expR": -0.267,
      "managed_expR": -0.203,
      "delta": 0.064,
      "avgEntryBetterTk_p50": 4.45,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 50.0,
      "m1_rate": 0.0,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 475,
      "naive_expR": -0.135,
      "managed_expR": -0.021,
      "delta": 0.113,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 49.1,
      "fill_full_pct": 31.8,
      "m1_rate": 31.8,
      "m2_rate": 19.4,
      "m3_rate": 9.9,
      "beAfterM1_rate": 16.6
    },
    "2m/RETEST/SHORT": {
      "n": 180,
      "naive_expR": -0.08,
      "managed_expR": 0.011,
      "delta": 0.091,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 48.9,
      "fill_full_pct": 39.4,
      "m1_rate": 31.1,
      "m2_rate": 19.4,
      "m3_rate": 12.2,
      "beAfterM1_rate": 17.2
    },
    "5m/INV/SHORT": {
      "n": 4,
      "naive_expR": 0.018,
      "managed_expR": 0.481,
      "delta": 0.463,
      "avgEntryBetterTk_p50": 23.3,
      "fill_t3plus_pct": 100.0,
      "fill_full_pct": 50.0,
      "m1_rate": 0.0,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 151,
      "naive_expR": 0.169,
      "managed_expR": 0.065,
      "delta": -0.103,
      "avgEntryBetterTk_p50": 2.7,
      "fill_t3plus_pct": 38.4,
      "fill_full_pct": 25.8,
      "m1_rate": 33.8,
      "m2_rate": 19.9,
      "m3_rate": 10.6,
      "beAfterM1_rate": 18.5
    },
    "5m/RETEST/SHORT": {
      "n": 77,
      "naive_expR": 0.023,
      "managed_expR": 0.197,
      "delta": 0.174,
      "avgEntryBetterTk_p50": 4.8,
      "fill_t3plus_pct": 50.6,
      "fill_full_pct": 31.2,
      "m1_rate": 40.3,
      "m2_rate": 23.4,
      "m3_rate": 10.4,
      "beAfterM1_rate": 18.2
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 1729,
    "layer_expR": -0.028,
    "orig_expR": 0.155,
    "delta_orig_minus_layer": 0.183,
    "delta_ci90": [
      0.084,
      0.29
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 44.7,
    "orig_wrTP1": 31.1,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.7,
    "orig_saved_from_SL": 4,
    "orig_caused_SL": 240
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 59,
      "layer_expR": 0.2,
      "orig_expR": 0.788,
      "delta_orig_minus_layer": 0.588,
      "delta_ci90": [
        -0.051,
        1.333
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 54.2,
      "orig_wrTP1": 28.8,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 15
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
      "n": 1639,
      "layer_expR": -0.035,
      "orig_expR": 0.142,
      "delta_orig_minus_layer": 0.177,
      "delta_ci90": [
        0.077,
        0.292
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.4,
      "orig_wrTP1": 31.3,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.8,
      "orig_saved_from_SL": 4,
      "orig_caused_SL": 219
    },
    "retestBar2": {
      "n": 31,
      "layer_expR": -0.11,
      "orig_expR": -0.371,
      "delta_orig_minus_layer": -0.261,
      "delta_ci90": [
        -0.583,
        0.062
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 41.9,
      "orig_wrTP1": 22.6,
      "slTk_p50": 45.0,
      "slOrigTk_p50": 25.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 6
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 30,
      "layer_expR": 0.428,
      "orig_expR": 0.871,
      "delta_orig_minus_layer": 0.443,
      "delta_ci90": [
        -0.362,
        1.327
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.0,
      "orig_wrTP1": 26.7,
      "slTk_p50": 10.0,
      "slOrigTk_p50": 2.0,
      "orig_wider_pct": 3.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 7
    },
    "1m/INV/SHORT": {
      "n": 7,
      "layer_expR": 0.463,
      "orig_expR": -0.35,
      "delta_orig_minus_layer": -0.813,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 85.7,
      "orig_wrTP1": 28.6,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 4
    },
    "1m/RETEST/LONG": {
      "n": 802,
      "layer_expR": 0.012,
      "orig_expR": 0.155,
      "delta_orig_minus_layer": 0.143,
      "delta_ci90": [
        -0.0,
        0.297
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 43.5,
      "orig_wrTP1": 28.7,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 2.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 120
    },
    "1m/RETEST/SHORT": {
      "n": 169,
      "layer_expR": -0.064,
      "orig_expR": 0.155,
      "delta_orig_minus_layer": 0.22,
      "delta_ci90": [
        -0.056,
        0.55
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 43.8,
      "orig_wrTP1": 29.6,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 0.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 24
    },
    "2m/INV/LONG": {
      "n": 12,
      "layer_expR": -0.233,
      "orig_expR": 2.239,
      "delta_orig_minus_layer": 2.472,
      "delta_ci90": [
        0.456,
        5.001
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 41.7,
      "orig_wrTP1": 33.3,
      "slTk_p50": 13.5,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 8.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 1
    },
    "2m/INV/SHORT": {
      "n": 5,
      "layer_expR": -0.404,
      "orig_expR": -0.06,
      "delta_orig_minus_layer": 0.344,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 40.0,
      "orig_wrTP1": 40.0,
      "slTk_p50": 17.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 0
    },
    "2m/RETEST/LONG": {
      "n": 403,
      "layer_expR": -0.121,
      "orig_expR": -0.052,
      "delta_orig_minus_layer": 0.069,
      "delta_ci90": [
        -0.053,
        0.19
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 43.7,
      "orig_wrTP1": 31.3,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 50
    },
    "2m/RETEST/SHORT": {
      "n": 101,
      "layer_expR": -0.184,
      "orig_expR": 0.116,
      "delta_orig_minus_layer": 0.3,
      "delta_ci90": [
        -0.024,
        0.651
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 40.6,
      "orig_wrTP1": 29.7,
      "slTk_p50": 37.0,
      "slOrigTk_p50": 14.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 11
    },
    "5m/RETEST/LONG": {
      "n": 143,
      "layer_expR": 0.13,
      "orig_expR": 0.132,
      "delta_orig_minus_layer": 0.003,
      "delta_ci90": [
        -0.216,
        0.25
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 55.9,
      "orig_wrTP1": 44.1,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 15.0,
      "orig_wider_pct": 15.4,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 18
    },
    "5m/RETEST/SHORT": {
      "n": 52,
      "layer_expR": -0.206,
      "orig_expR": 1.18,
      "delta_orig_minus_layer": 1.386,
      "delta_ci90": [
        0.061,
        3.601
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 40.4,
      "orig_wrTP1": 40.4,
      "slTk_p50": 36.5,
      "slOrigTk_p50": 25.5,
      "orig_wider_pct": 17.3,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 2
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 2400,
    "wrTP1": 44.6,
    "expR": -0.014
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 2247,
  "brier": 0.2183,
  "bias": -0.177,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -0.944
    },
    {
      "feature": "stretchAtr",
      "weight": -0.218
    },
    {
      "feature": "chopIdx",
      "weight": -0.155
    },
    {
      "feature": "hourNY",
      "weight": 0.142
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.102
    },
    {
      "feature": "aligned",
      "weight": -0.078
    },
    {
      "feature": "rvol",
      "weight": 0.071
    },
    {
      "feature": "emaStack",
      "weight": -0.059
    },
    {
      "feature": "biasScore",
      "weight": -0.039
    },
    {
      "feature": "nearEdge",
      "weight": 0.017
    },
    {
      "feature": "nearTk",
      "weight": 0.015
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.008
    },
    {
      "feature": "structDir",
      "weight": 0.005
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.121,
      "actual": 0.161,
      "n": 224
    },
    {
      "bin": 1,
      "pred": 0.303,
      "actual": 0.249,
      "n": 225
    },
    {
      "bin": 2,
      "pred": 0.389,
      "actual": 0.329,
      "n": 225
    },
    {
      "bin": 3,
      "pred": 0.445,
      "actual": 0.375,
      "n": 224
    },
    {
      "bin": 4,
      "pred": 0.489,
      "actual": 0.471,
      "n": 225
    },
    {
      "bin": 5,
      "pred": 0.528,
      "actual": 0.556,
      "n": 225
    },
    {
      "bin": 6,
      "pred": 0.559,
      "actual": 0.585,
      "n": 224
    },
    {
      "bin": 7,
      "pred": 0.593,
      "actual": 0.636,
      "n": 225
    },
    {
      "bin": 8,
      "pred": 0.634,
      "actual": 0.667,
      "n": 225
    },
    {
      "bin": 9,
      "pred": 0.707,
      "actual": 0.733,
      "n": 225
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
  "weeks": 1
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.428,
    "ci90": [
      -0.02,
      0.94
    ],
    "p_mean_le_0": 0.059,
    "n": 30,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.222,
    "ci90": [
      -0.126,
      0.587
    ],
    "p_mean_le_0": 0.155,
    "n": 17,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": -0.004,
    "ci90": [
      -0.075,
      0.071
    ],
    "p_mean_le_0": 0.531,
    "n": 975,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.015,
    "ci90": [
      -0.081,
      0.108
    ],
    "p_mean_le_0": 0.42,
    "n": 387,
    "survives_fdr10": false
  },
  "2m/INV/LONG": {
    "expR": -0.233,
    "ci90": [
      -0.649,
      0.22
    ],
    "p_mean_le_0": 0.8,
    "n": 12,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.13,
    "ci90": [
      -0.208,
      -0.049
    ],
    "p_mean_le_0": 0.998,
    "n": 478,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": -0.08,
    "ci90": [
      -0.208,
      0.056
    ],
    "p_mean_le_0": 0.837,
    "n": 180,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.169,
    "ci90": [
      0.007,
      0.348
    ],
    "p_mean_le_0": 0.042,
    "n": 151,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": 0.03,
    "ci90": [
      -0.17,
      0.254
    ],
    "p_mean_le_0": 0.405,
    "n": 78,
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
      "id": 3,
      "n": 307,
      "wrTP1": 49.8,
      "expR": 0.129,
      "pf": 1.3,
      "defining_features": {
        "biasScore": -1.3,
        "hourNY": 1.18,
        "emaStack": -1.12,
        "atrPctUsed": -0.76
      }
    },
    {
      "id": 0,
      "n": 518,
      "wrTP1": 49.4,
      "expR": -0.006,
      "pf": 0.99,
      "defining_features": {
        "hourNY": 1.11,
        "atrPctUsed": -0.91,
        "emaStack": 0.59,
        "biasScore": 0.57
      }
    },
    {
      "id": 2,
      "n": 1099,
      "wrTP1": 41.8,
      "expR": -0.014,
      "pf": 0.97,
      "defining_features": {
        "atrPctUsed": 0.76,
        "biasScore": 0.62,
        "nearEdge": 0.56,
        "emaStack": 0.45
      }
    },
    {
      "id": 1,
      "n": 476,
      "wrTP1": 42.4,
      "expR": -0.117,
      "pf": 0.78,
      "defining_features": {
        "biasScore": -1.22,
        "nearEdge": -1.08,
        "hourNY": -1.05,
        "emaStack": -0.95
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
        "n": 10,
        "wrTP1": 50.0,
        "expR": 0.365
      },
      "YM": {
        "n": 15,
        "wrTP1": 60.0,
        "expR": 0.643
      },
      "GC": {
        "n": 3,
        "wrTP1": 33.3,
        "expR": -0.477
      }
    },
    "expR_spread": 1.12,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 13,
        "wrTP1": 61.5,
        "expR": 0.133
      },
      "NQ": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.795
      }
    },
    "expR_spread": 0.662,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 181,
        "wrTP1": 40.9,
        "expR": 0.23
      },
      "NQ": {
        "n": 123,
        "wrTP1": 50.4,
        "expR": 0.054
      },
      "ES": {
        "n": 209,
        "wrTP1": 39.2,
        "expR": -0.039
      },
      "CL": {
        "n": 253,
        "wrTP1": 41.5,
        "expR": -0.232
      },
      "YM": {
        "n": 227,
        "wrTP1": 46.7,
        "expR": 0.067
      }
    },
    "expR_spread": 0.462,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 116,
        "wrTP1": 44.8,
        "expR": 0.104
      },
      "GC": {
        "n": 79,
        "wrTP1": 36.7,
        "expR": -0.16
      },
      "YM": {
        "n": 110,
        "wrTP1": 48.2,
        "expR": 0.064
      },
      "ES": {
        "n": 107,
        "wrTP1": 45.8,
        "expR": 0.003
      }
    },
    "expR_spread": 0.264,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.05
      },
      "CL": {
        "n": 3,
        "wrTP1": 33.3,
        "expR": -0.527
      },
      "YM": {
        "n": 4,
        "wrTP1": 0.0,
        "expR": -1.0
      }
    },
    "expR_spread": 1.05,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 73,
        "wrTP1": 45.2,
        "expR": -0.199
      },
      "GC": {
        "n": 90,
        "wrTP1": 43.3,
        "expR": 0.04
      },
      "CL": {
        "n": 109,
        "wrTP1": 39.4,
        "expR": -0.218
      },
      "ES": {
        "n": 98,
        "wrTP1": 45.9,
        "expR": -0.048
      },
      "YM": {
        "n": 121,
        "wrTP1": 41.3,
        "expR": -0.201
      }
    },
    "expR_spread": 0.258,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 40,
        "wrTP1": 40.0,
        "expR": -0.18
      },
      "YM": {
        "n": 56,
        "wrTP1": 41.1,
        "expR": -0.133
      },
      "GC": {
        "n": 33,
        "wrTP1": 39.4,
        "expR": -0.021
      },
      "NQ": {
        "n": 62,
        "wrTP1": 45.2,
        "expR": 0.005
      }
    },
    "expR_spread": 0.185,
    "verdict": "universal"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 9,
        "wrTP1": 66.7,
        "expR": 0.378
      },
      "ES": {
        "n": 35,
        "wrTP1": 51.4,
        "expR": 0.435
      },
      "YM": {
        "n": 41,
        "wrTP1": 58.5,
        "expR": 0.134
      },
      "CL": {
        "n": 28,
        "wrTP1": 57.1,
        "expR": 0.146
      },
      "NQ": {
        "n": 44,
        "wrTP1": 50.0,
        "expR": -0.02
      }
    },
    "expR_spread": 0.455,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 35,
        "wrTP1": 60.0,
        "expR": 0.181
      },
      "ES": {
        "n": 22,
        "wrTP1": 54.5,
        "expR": 0.12
      },
      "GC": {
        "n": 12,
        "wrTP1": 25.0,
        "expR": -0.489
      },
      "YM": {
        "n": 15,
        "wrTP1": 40.0,
        "expR": -0.08
      }
    },
    "expR_spread": 0.67,
    "verdict": "instrument-specific"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 15,
  "near_news_30m": {
    "n": 174,
    "wrTP1": 48.9,
    "nSL": 75,
    "nTO": 14,
    "expR": 0.195,
    "pf": 1.43,
    "mfe_p25": 6.0,
    "mfe_p50": 14.0,
    "mfe_p75": 37.0,
    "winnerMAE_p75": 11.0,
    "winnerMAE_p90": 31.200000000000017,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 4.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -9.0,
    "revAfterSL_rate": 33.3
  },
  "away_from_news": {
    "n": 2226,
    "wrTP1": 44.2,
    "nSL": 1102,
    "nTO": 139,
    "expR": -0.03,
    "pf": 0.94,
    "mfe_p25": 6.0,
    "mfe_p50": 14.0,
    "mfe_p75": 37.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 27.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -12.0,
    "revAfterSL_rate": 33.8
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 0,
  "note": "sin predictions.jsonl todavia"
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
    "hypothesis": "En SELL RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. NO aplica a BUY RETEST (plano u opuesto, sin significancia): no generalizar a largos.",
    "param": "sl_basis_retest_short",
    "from": "3-capas (sc_slbuf x ATR1m + piso sc_floor_atr5 + techo sc_cap_atr5 / sc_cap_adr)",
    "to": "mecha de la vela del retest (lg_slOrig con slBasis=retestBar / retestBar2, crudo)",
    "changeDate": null,
    "segment": {
      "kind": "RETEST",
      "side": "SHORT"
    },
    "targetMetric": "expR",
    "minAfterN": 40,
    "evidence": {
      "source": "sl_origin_vs_layer.by_basis (medicion PARALELA: misma entrada y mismos TP, solo se mueve el stop; rMultiple = base 3-capas, rOrig = base mecha del retest). No requiere cambio en TradingView para medir.",
      "asOf": "2026-09-03",
      "sell_retest_1m": {
        "n": 138,
        "deltaER_orig_minus_layer": 0.328,
        "ci90_no_cruza_cero": true
      },
      "sell_retest_5m": {
        "n": 42,
        "deltaER_orig_minus_layer": 1.7
      },
      "buy_retest": "no significativo / opuesto -> no aplicar a largos",
      "overall_by_basis_retestBar": {
        "n_aprox": 517,
        "deltaER_aprox": 0.231,
        "ci90": [
          0.021,
          0.499
        ]
      }
    },
    "next_steps": [
      "Revision semanal del domingo: confirmar sobre walk-forward + segment_significance (FDR 10%), no solo in-sample.",
      "Anadir linea a predictions.jsonl con predictedDeltaER antes de aplicar.",
      "Si pasa: cambio en Pine = para RETEST SHORT usar lg_slOrig (mecha de la vela del retest) como SL de trabajo, no solo como medicion paralela; mantener 3-capas para el resto. Poner changeDate el dia que se aplique en los 12 graficos.",
      "Vigilar: retestBar2 (1m SHORT = mecha vela retest + vela previa) aun no aparece en los datos; puede cambiar el numero de 1m cuando entre."
    ],
    "beforeN": 687,
    "afterN": 0,
    "before": {
      "n": 687,
      "wrTP1": 44.4,
      "nSL": 319,
      "nTO": 63,
      "expR": -0.01,
      "pf": 0.98,
      "mfe_p25": 7.0,
      "mfe_p50": 16.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 33.200000000000045,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 38.6
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
    "date": "2026-09-04",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-09-03T16:25:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "CL",
    "focus": {
      "sym": "CL",
      "verdict": "WAIT",
      "window": "17:00-01:00 CT",
      "setup": {
        "es": "retest de 91.75-92.29 (PDH roto de ayer, ahora soporte) con reclamo confirmado",
        "en": "retest of 91.75-92.29 (yesterday's broken PDH, now support) with a confirmed reclaim"
      },
      "trigger": {
        "es": "cierre 5m dentro de 91.75-92.29 con mecha inferior, o defensa de POC/VWAP 91.5-91.7 con reclamo sobre 91.75",
        "en": "5m close inside 91.75-92.29 with a lower wick, or POC/VWAP 91.5-91.7 defended with a reclaim above 91.75"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 90.97 devuelve el precio a rango dentro de 89.04-92.29",
        "en": "5m close sustained below 90.97 sends price back into the 89.04-92.29 range"
      },
      "note": {
        "es": "el unico instrumento sin estiramiento extremo esta noche -- los otros 4 estan 7-11 ATR estirados, no los persigas",
        "en": "the only instrument without an extreme stretch tonight -- the other 4 are 7-11 ATR stretched, don't chase them"
      }
    },
    "summary": {
      "es": [
        "dia historico de expansion: NQ/ES/YM/GC rompieron a nuevos maximos y cerraron cerca de ellos, GC+YM a un paso de sus maximos semanales",
        "NQ: la tesis bajista de 3 dias murio esta manana sobre 29317.75 -- tesis nueva alcista, pero cierra 10.9 ATR estirado, no persigas",
        "ES: el corto de 4 dias murio en el mismo nivel que su contra-caso llevaba semanas marcando (7691.25) -- tesis nueva alcista, 6.9 ATR estirado",
        "GC: 2a sesion de ruptura, primer pullback real tardio (4558.5 a 4520.30) pero sin llegar aun a la zona de descuento 4479-4497",
        "YM: 3a sesion seguida liderando el complejo al alza, a 35pts de su maximo semanal (53862) -- el mas limpio en tendencia, pero tambien el mas estirado (10.3 ATR)",
        "CL: unico instrumento sin estiramiento extremo, consolidando en POC/VWAP tras el round-trip de ayer -- el mas limpio para esta noche",
        "!! semana de NFP: dato de empleo manana viernes 07:30 CT, dentro de la sesion NY del dia que empieza esta noche -- trata el dia entero con mas cautela aunque Asia/Londres no traigan nada de impacto",
        "sizing: limite diario ~$1,000 por cuenta (el extremo bajo del rango) suele ser la cuenta entera -- multiplica por N si copytradeas N cuentas",
        "mas limpio: CL"
      ],
      "en": [
        "historic expansion day: NQ/ES/YM/GC broke to new highs and closed near them, GC+YM one step from their weekly highs",
        "NQ: the 3-day bearish thesis died this morning above 29317.75 -- new bullish thesis, but closes 10.9 ATR stretched, don't chase",
        "ES: the 4-day short died at the exact level its own counter-case had been flaggin
```
