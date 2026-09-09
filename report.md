# Scalp CC · report 2026-09-09T01:13Z
- signals=4780 outcomes=4298 pares_resueltos=4455 pendientes=325 huerfanos=22

## ⚠ ALERTAS (llevar al frente del resumen)
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.152 vs -0.017, delta 0.169 CI90 [0.097, 0.241], n 2941). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.372 vs -0.078, delta 0.45 CI90 [0.182, 0.764], n 376). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=AVOID rinden MEJOR de forma no-random (E[R] 0.175 CI90 [0.085, 0.267], n 452). Contrario a la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden PEOR de forma no-random (E[R] -0.196 CI90 [-0.301, -0.08], n 219). Contrario a la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": -0.02, "ci90": [-0.049, 0.009], "p_mean_le_0": 0.871, "n": 4276}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 52 | 44.2 | 0.212 | 1.48 | 21 | 10.0 | 5.0 | 23.8 |
| 1m/INV/SHORT | 37 | 51.4 | -0.054 | 0.88 | 16 | 11.0 | 11.5 | 25.0 |
| 1m/RETEST/LONG | 1776 | 43.9 | -0.005 | 0.99 | 873 | 12.0 | 9.0 | 28.8 |
| 1m/RETEST/SHORT | 847 | 41.0 | -0.048 | 0.91 | 422 | 13.0 | 8.0 | 30.6 |
| 2m/INV/LONG | 20 | 35.0 | -0.344 | 0.47 | 13 | 6.5 | 7.5 | 23.1 |
| 2m/INV/SHORT | 16 | 31.2 | -0.189 | 0.66 | 9 | 12.5 | 5.0 | 44.4 |
| 2m/RETEST/LONG | 872 | 45.8 | -0.04 | 0.92 | 433 | 14.0 | 13.0 | 38.1 |
| 2m/RETEST/SHORT | 385 | 42.6 | -0.068 | 0.87 | 192 | 17.0 | 12.0 | 40.1 |
| 5m/INV/LONG | 7 | 100.0 | 0.646 | 99.0 | 0 | 28.0 | 24.5 | None |
| 5m/INV/SHORT | 5 | 60.0 | -0.186 | 0.54 | 2 | 34.0 | 88.5 | 100.0 |
| 5m/RETEST/LONG | 302 | 52.0 | 0.081 | 1.18 | 127 | 20.0 | 18.0 | 51.2 |
| 5m/RETEST/SHORT | 136 | 47.8 | -0.027 | 0.94 | 59 | 29.0 | 21.0 | 37.3 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 315 | 22.2 | 0.014 | 1.02 | 198 | 19.0 | 14.0 | 15.2 |
| B | 1917 | 44.2 | -0.006 | 0.99 | 938 | 15.0 | 9.25 | 31.4 |
| C | 2223 | 47.6 | -0.036 | 0.93 | 1031 | 13.0 | 11.0 | 39.0 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 1863 | 47.0 | 0.008 | 1.02 | 830 | 11.0 | 8.0 | 41.8 |
| London | 702 | 43.2 | -0.126 | 0.77 | 387 | 15.0 | 12.0 | 33.3 |
| NY | 746 | 45.2 | 0.156 | 1.32 | 350 | 25.0 | 17.0 | 33.1 |
| Sin KZ | 1144 | 40.2 | -0.114 | 0.79 | 600 | 13.0 | 10.0 | 22.5 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 1087 | 42.4 | -0.037 | 0.93 | 535 | 15.0 | 9.0 | 32.5 |
| edge=0 | 1878 | 47.6 | -0.029 | 0.94 | 890 | 11.0 | 9.0 | 41.0 |
| edge=1 | 1490 | 41.7 | 0.005 | 1.01 | 742 | 18.0 | 13.0 | 25.3 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| aligned=1 | 4444 | 44.3 | -0.021 | 0.96 | 2166 | 14.0 | 10.0 | 33.6 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 35 | 48.6 | 0.028 | 1.06 | 17 | 7.0 | 6.0 | 23.5 |
| INV/LONG|edge=1 | 40 | 45.0 | 0.141 | 1.34 | 15 | 19.0 | 16.25 | 20.0 |
| INV/SHORT|edge=-1 | 36 | 36.1 | -0.284 | 0.5 | 20 | 15.0 | 21.0 | 30.0 |
| INV/SHORT|edge=0 | 20 | 65.0 | 0.245 | 1.77 | 6 | 11.0 | 23.0 | 66.7 |
| INV/SHORT|edge=1 | 2 | 50.0 | -0.29 | 0.42 | 1 | 7.0 | 5.0 | 0.0 |
| RETEST/LONG|edge=-1 | 176 | 45.5 | 0.044 | 1.09 | 82 | 11.0 | 8.0 | 46.3 |
| RETEST/LONG|edge=0 | 1391 | 49.5 | -0.017 | 0.96 | 650 | 10.0 | 9.0 | 41.7 |
| RETEST/LONG|edge=1 | 1383 | 41.0 | -0.003 | 0.99 | 701 | 18.0 | 13.0 | 24.5 |
| RETEST/SHORT|edge=-1 | 871 | 42.0 | -0.046 | 0.91 | 431 | 16.0 | 9.0 | 29.9 |
| RETEST/SHORT|edge=0 | 432 | 40.3 | -0.087 | 0.84 | 217 | 15.0 | 11.75 | 39.6 |
| RETEST/SHORT|edge=1 | 65 | 55.4 | 0.11 | 1.27 | 25 | 13.0 | 9.0 | 52.0 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 22 | 40.9 | 0.268 | 1.67 | 7 | 14.0 | 7.0 | 14.3 |
| INV/LONG|tier=C | 57 | 49.1 | 0.051 | 1.11 | 27 | 10.0 | 9.25 | 25.9 |
| INV/SHORT|tier=B | 17 | 47.1 | -0.058 | 0.87 | 7 | 11.5 | 6.75 | 0.0 |
| INV/SHORT|tier=C | 41 | 46.3 | -0.123 | 0.75 | 20 | 13.0 | 57.0 | 50.0 |
| RETEST/LONG|tier=A+ | 223 | 22.9 | 0.02 | 1.03 | 137 | 16.0 | 17.5 | 14.6 |
| RETEST/LONG|tier=B | 1140 | 43.9 | 0.011 | 1.02 | 569 | 15.0 | 10.0 | 30.1 |
| RETEST/LONG|tier=C | 1587 | 49.4 | -0.023 | 0.95 | 727 | 12.0 | 10.0 | 39.9 |
| RETEST/SHORT|tier=A+ | 92 | 20.7 | -0.001 | 1.0 | 61 | 29.0 | 7.5 | 16.4 |
| RETEST/SHORT|tier=B | 738 | 44.7 | -0.039 | 0.92 | 355 | 14.0 | 8.0 | 34.6 |
| RETEST/SHORT|tier=C | 538 | 42.2 | -0.077 | 0.85 | 257 | 16.0 | 14.0 | 37.0 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 79 | 46.8 | 0.106 | 1.23 | 34 | 10.5 | 8.0 | 23.5 |
| INV/SHORT|aligned=1 | 58 | 46.6 | -0.105 | 0.78 | 27 | 13.0 | 22.0 | 37.0 |
| RETEST/LONG|aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| RETEST/LONG|aligned=1 | 2939 | 45.3 | -0.008 | 0.98 | 1432 | 13.0 | 10.0 | 33.6 |
| RETEST/SHORT|aligned=1 | 1368 | 42.1 | -0.051 | 0.9 | 673 | 15.0 | 10.0 | 33.9 |

## Autopsia de SL
n_losses=2167  causas: RR-bajo×839, contra-estructura×797, stop-en-el-minimo×727, killzone-Asia-largo×555, sin-nivel-detras×414, estirado×377, chop×290, SL-muy-pegado×259, sin-causa-clara×223, contra-sesgo×1
- INV/LONG (n=34): RR-bajo×19, killzone-Asia-largo×18, contra-estructura×12, stop-en-el-minimo×8, estirado×6, SL-muy-pegado×3, sin-nivel-detras×3, chop×1, sin-causa-clara×1
- INV/SHORT (n=27): RR-bajo×16, stop-en-el-minimo×10, contra-estructura×10, sin-causa-clara×4, estirado×4, SL-muy-pegado×2, chop×1
- RETEST/LONG (n=1433): RR-bajo×569, contra-estructura×549, killzone-Asia-largo×537, stop-en-el-minimo×481, sin-nivel-detras×301, estirado×229, chop×205, SL-muy-pegado×158, sin-causa-clara×109, contra-sesgo×1
- RETEST/SHORT (n=673): RR-bajo×235, stop-en-el-minimo×228, contra-estructura×226, estirado×138, sin-nivel-detras×110, sin-causa-clara×109, SL-muy-pegado×96, chop×83

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
    "n": 4261,
    "naive_expR": -0.02,
    "managed_expR": 0.071,
    "delta": 0.092,
    "avgEntryBetterTk_p50": 2.4,
    "fill_t3plus_pct": 47.7,
    "fill_full_pct": 33.7,
    "m1_rate": 35.1,
    "m2_rate": 21.0,
    "m3_rate": 11.5,
    "beAfterM1_rate": 17.3
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 49,
      "naive_expR": 0.212,
      "managed_expR": 0.35,
      "delta": 0.139,
      "avgEntryBetterTk_p50": 1.0,
      "fill_t3plus_pct": 40.8,
      "fill_full_pct": 34.7,
      "m1_rate": 44.9,
      "m2_rate": 30.6,
      "m3_rate": 18.4,
      "beAfterM1_rate": 20.4
    },
    "1m/INV/SHORT": {
      "n": 35,
      "naive_expR": -0.054,
      "managed_expR": 0.224,
      "delta": 0.278,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 45.7,
      "fill_full_pct": 40.0,
      "m1_rate": 31.4,
      "m2_rate": 20.0,
      "m3_rate": 8.6,
      "beAfterM1_rate": 14.3
    },
    "1m/RETEST/LONG": {
      "n": 1716,
      "naive_expR": -0.006,
      "managed_expR": 0.064,
      "delta": 0.07,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 48.4,
      "fill_full_pct": 35.4,
      "m1_rate": 33.7,
      "m2_rate": 19.8,
      "m3_rate": 11.0,
      "beAfterM1_rate": 16.3
    },
    "1m/RETEST/SHORT": {
      "n": 796,
      "naive_expR": -0.046,
      "managed_expR": 0.126,
      "delta": 0.172,
      "avgEntryBetterTk_p50": 2.5,
      "fill_t3plus_pct": 47.5,
      "fill_full_pct": 29.9,
      "m1_rate": 41.3,
      "m2_rate": 24.4,
      "m3_rate": 13.6,
      "beAfterM1_rate": 20.4
    },
    "2m/INV/LONG": {
      "n": 20,
      "naive_expR": -0.344,
      "managed_expR": -0.317,
      "delta": 0.027,
      "avgEntryBetterTk_p50": 2.1500000000000004,
      "fill_t3plus_pct": 55.0,
      "fill_full_pct": 40.0,
      "m1_rate": 15.0,
      "m2_rate": 15.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 5.0
    },
    "2m/INV/SHORT": {
      "n": 16,
      "naive_expR": -0.189,
      "managed_expR": -0.171,
      "delta": 0.018,
      "avgEntryBetterTk_p50": 3.65,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 43.8,
      "m1_rate": 18.8,
      "m2_rate": 12.5,
      "m3_rate": 6.2,
      "beAfterM1_rate": 12.5
    },
    "2m/RETEST/LONG": {
      "n": 843,
      "naive_expR": -0.042,
      "managed_expR": 0.028,
      "delta": 0.071,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.5,
      "fill_full_pct": 33.2,
      "m1_rate": 32.9,
      "m2_rate": 19.8,
      "m3_rate": 10.8,
      "beAfterM1_rate": 16.8
    },
    "2m/RETEST/SHORT": {
      "n": 366,
      "naive_expR": -0.068,
      "managed_expR": 0.069,
      "delta": 0.137,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 49.7,
      "fill_full_pct": 38.8,
      "m1_rate": 35.8,
      "m2_rate": 22.7,
      "m3_rate": 13.9,
      "beAfterM1_rate": 17.2
    },
    "5m/INV/LONG": {
      "n": 7,
      "naive_expR": 0.646,
      "managed_expR": 0.787,
      "delta": 0.141,
      "avgEntryBetterTk_p50": 4.4,
      "fill_t3plus_pct": 42.9,
      "fill_full_pct": 28.6,
      "m1_rate": 42.9,
      "m2_rate": 28.6,
      "m3_rate": 0.0,
      "beAfterM1_rate": 14.3
    },
    "5m/INV/SHORT": {
      "n": 5,
      "naive_expR": -0.186,
      "managed_expR": 0.184,
      "delta": 0.37,
      "avgEntryBetterTk_p50": 11.5,
      "fill_t3plus_pct": 100.0,
      "fill_full_pct": 60.0,
      "m1_rate": 0.0,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 285,
      "naive_expR": 0.081,
      "managed_expR": 0.013,
      "delta": -0.068,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 37.2,
      "fill_full_pct": 26.7,
      "m1_rate": 31.2,
      "m2_rate": 18.6,
      "m3_rate": 9.5,
      "beAfterM1_rate": 17.5
    },
    "5m/RETEST/SHORT": {
      "n": 123,
      "naive_expR": -0.032,
      "managed_expR": 0.149,
      "delta": 0.181,
      "avgEntryBetterTk_p50": 4.9,
      "fill_t3plus_pct": 52.0,
      "fill_full_pct": 34.1,
      "m1_rate": 38.2,
      "m2_rate": 23.6,
      "m3_rate": 10.6,
      "beAfterM1_rate": 17.9
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 3437,
    "layer_expR": -0.023,
    "orig_expR": 0.18,
    "delta_orig_minus_layer": 0.203,
    "delta_ci90": [
      0.134,
      0.278
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 45.8,
    "orig_wrTP1": 32.8,
    "slTk_p50": 18.0,
    "slOrigTk_p50": 7.0,
    "orig_wider_pct": 4.2,
    "orig_saved_from_SL": 8,
    "orig_caused_SL": 455
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 120,
      "layer_expR": 0.006,
      "orig_expR": 0.27,
      "delta_orig_minus_layer": 0.265,
      "delta_ci90": [
        -0.068,
        0.643
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 46.7,
      "orig_wrTP1": 28.3,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 4.2,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 22
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
      "n": 2941,
      "layer_expR": -0.017,
      "orig_expR": 0.152,
      "delta_orig_minus_layer": 0.169,
      "delta_ci90": [
        0.097,
        0.241
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.4,
      "orig_wrTP1": 33.3,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.3,
      "orig_saved_from_SL": 8,
      "orig_caused_SL": 396
    },
    "retestBar2": {
      "n": 376,
      "layer_expR": -0.078,
      "orig_expR": 0.372,
      "delta_orig_minus_layer": 0.45,
      "delta_ci90": [
        0.182,
        0.764
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 40.2,
      "orig_wrTP1": 30.3,
      "slTk_p50": 13.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 3.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 37
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 49,
      "layer_expR": 0.212,
      "orig_expR": 0.402,
      "delta_orig_minus_layer": 0.19,
      "delta_ci90": [
        -0.38,
        0.816
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 46.9,
      "orig_wrTP1": 28.6,
      "slTk_p50": 12.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 4.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 9
    },
    "1m/INV/SHORT": {
      "n": 25,
      "layer_expR": -0.097,
      "orig_expR": -0.116,
      "delta_orig_minus_layer": -0.018,
      "delta_ci90": [
        -0.385,
        0.358
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 52.0,
      "orig_wrTP1": 32.0,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 5
    },
    "1m/RETEST/LONG": {
      "n": 1432,
      "layer_expR": -0.004,
      "orig_expR": 0.177,
      "delta_orig_minus_layer": 0.18,
      "delta_ci90": [
        0.074,
        0.296
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.8,
      "orig_wrTP1": 30.5,
      "slTk_p50": 17.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 206
    },
    "1m/RETEST/SHORT": {
      "n": 514,
      "layer_expR": -0.071,
      "orig_expR": 0.346,
      "delta_orig_minus_layer": 0.417,
      "delta_ci90": [
        0.2,
        0.644
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 41.2,
      "orig_wrTP1": 30.5,
      "slTk_p50": 15.5,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 2.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 55
    },
    "2m/INV/LONG": {
      "n": 20,
      "layer_expR": -0.344,
      "orig_expR": 1.194,
      "delta_orig_minus_layer": 1.538,
      "delta_ci90": [
        0.243,
        3.13
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 35.0,
      "orig_wrTP1": 25.0,
      "slTk_p50": 10.5,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 5.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 2
    },
    "2m/INV/SHORT": {
      "n": 15,
      "layer_expR": -0.23,
      "orig_expR": -0.081,
      "delta_orig_minus_layer": 0.149,
      "delta_ci90": [
        -0.179,
        0.452
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 26.7,
      "orig_wrTP1": 26.7,
      "slTk_p50": 17.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 0
    },
    "2m/RETEST/LONG": {
      "n": 742,
      "layer_expR": -0.022,
      "orig_expR": -0.012,
      "delta_orig_minus_layer": 0.01,
      "delta_ci90": [
        -0.079,
        0.1
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.6,
      "orig_wrTP1": 33.4,
      "slTk_p50": 18.5,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 105
    },
    "2m/RETEST/SHORT": {
      "n": 260,
      "layer_expR": -0.1,
      "orig_expR": 0.145,
      "delta_orig_minus_layer": 0.245,
      "delta_ci90": [
        0.035,
        0.466
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.6,
      "orig_wrTP1": 31.5,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 35
    },
    "5m/INV/LONG": {
      "n": 7,
      "layer_expR": 0.646,
      "orig_expR": -0.609,
      "delta_orig_minus_layer": -1.254,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 100.0,
      "orig_wrTP1": 28.6,
      "slTk_p50": 49.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 14.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 5
    },
    "5m/RETEST/LONG": {
      "n": 274,
      "layer_expR": 0.064,
      "orig_expR": 0.242,
      "delta_orig_minus_layer": 0.178,
      "delta_ci90": [
        0.005,
        0.38
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.7,
      "orig_wrTP1": 46.0,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 13.0,
      "orig_wider_pct": 16.4,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 27
    },
    "5m/RETEST/SHORT": {
      "n": 95,
      "layer_expR": -0.141,
      "orig_expR": 0.643,
      "delta_orig_minus_layer": 0.784,
      "delta_ci90": [
        0.064,
        1.975
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.3,
      "orig_wrTP1": 44.2,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 25.3,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 5
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 3231,
    "wrTP1": 44.6,
    "expR": -0.021
  },
  "2026-W37": {
    "n": 1224,
    "wrTP1": 43.7,
    "expR": -0.016
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 4143,
  "brier": 0.2198,
  "bias": -0.18,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -0.995
    },
    {
      "feature": "stretchAtr",
      "weight": -0.142
    },
    {
      "feature": "rvol",
      "weight": 0.117
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.081
    },
    {
      "feature": "hourNY",
      "weight": 0.078
    },
    {
      "feature": "chopIdx",
      "weight": -0.071
    },
    {
      "feature": "aligned",
      "weight": -0.06
    },
    {
      "feature": "entryZoneTk",
      "weight": 0.039
    },
    {
      "feature": "structDir",
      "weight": 0.027
    },
    {
      "feature": "emaStack",
      "weight": -0.008
    },
    {
      "feature": "nearEdge",
      "weight": 0.004
    },
    {
      "feature": "nearTk",
      "weight": 0.002
    },
    {
      "feature": "biasScore",
      "weight": -0.001
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.123,
      "actual": 0.167,
      "n": 414
    },
    {
      "bin": 1,
      "pred": 0.309,
      "actual": 0.287,
      "n": 414
    },
    {
      "bin": 2,
      "pred": 0.395,
      "actual": 0.3,
      "n": 414
    },
    {
      "bin": 3,
      "pred": 0.452,
      "actual": 0.373,
      "n": 415
    },
    {
      "bin": 4,
      "pred": 0.498,
      "actual": 0.449,
      "n": 414
    },
    {
      "bin": 5,
      "pred": 0.534,
      "actual": 0.546,
      "n": 414
    },
    {
      "bin": 6,
      "pred": 0.566,
      "actual": 0.588,
      "n": 415
    },
    {
      "bin": 7,
      "pred": 0.594,
      "actual": 0.667,
      "n": 414
    },
    {
      "bin": 8,
      "pred": 0.623,
      "actual": 0.679,
      "n": 414
    },
    {
      "bin": 9,
      "pred": 0.682,
      "actual": 0.713,
      "n": 415
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
  "weeks": 2
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.212,
    "ci90": [
      -0.103,
      0.534
    ],
    "p_mean_le_0": 0.162,
    "n": 49,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": -0.054,
    "ci90": [
      -0.315,
      0.209
    ],
    "p_mean_le_0": 0.635,
    "n": 35,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": -0.005,
    "ci90": [
      -0.055,
      0.045
    ],
    "p_mean_le_0": 0.577,
    "n": 1720,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": -0.048,
    "ci90": [
      -0.116,
      0.018
    ],
    "p_mean_le_0": 0.887,
    "n": 803,
    "survives_fdr10": false
  },
  "2m/INV/LONG": {
    "expR": -0.344,
    "ci90": [
      -0.675,
      0.027
    ],
    "p_mean_le_0": 0.942,
    "n": 20,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": -0.189,
    "ci90": [
      -0.599,
      0.244
    ],
    "p_mean_le_0": 0.781,
    "n": 16,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.04,
    "ci90": [
      -0.102,
      0.023
    ],
    "p_mean_le_0": 0.843,
    "n": 846,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": -0.068,
    "ci90": [
      -0.157,
      0.029
    ],
    "p_mean_le_0": 0.874,
    "n": 366,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.081,
    "ci90": [
      -0.03,
      0.194
    ],
    "p_mean_le_0": 0.114,
    "n": 285,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": -0.027,
    "ci90": [
      -0.187,
      0.145
    ],
    "p_mean_le_0": 0.605,
    "n": 124,
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
      "id": 1,
      "n": 1926,
      "wrTP1": 48.0,
      "expR": 0.049,
      "pf": 1.1,
      "defining_features": {
        "biasScore": 0.63,
        "emaStack": 0.62,
        "atrPctUsed": -0.46,
        "nearEdge": 0.46
      }
    },
    {
      "id": 2,
      "n": 1255,
      "wrTP1": 41.9,
      "expR": -0.056,
      "pf": 0.89,
      "defining_features": {
        "biasScore": -1.32,
        "emaStack": -1.1,
        "nearEdge": -0.99,
        "structDir": -0.49
      }
    },
    {
      "id": 0,
      "n": 713,
      "wrTP1": 40.7,
      "expR": -0.068,
      "pf": 0.88,
      "defining_features": {
        "atrPctUsed": 1.86,
        "biasScore": 0.63,
        "nearEdge": 0.41,
        "emaStack": 0.36
      }
    },
    {
      "id": 3,
      "n": 561,
      "wrTP1": 41.9,
      "expR": -0.118,
      "pf": 0.77,
      "defining_features": {
        "stretchAtr": 1.66,
        "rvol": 1.37,
        "chopIdx": -1.31,
        "hourNY": -0.26
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
        "n": 14,
        "wrTP1": 50.0,
        "expR": 0.428
      },
      "YM": {
        "n": 18,
        "wrTP1": 50.0,
        "expR": 0.501
      },
      "ES": {
        "n": 7,
        "wrTP1": 42.9,
        "expR": -0.434
      },
      "NQ": {
        "n": 6,
        "wrTP1": 33.3,
        "expR": 0.257
      },
      "GC": {
        "n": 7,
        "wrTP1": 28.6,
        "expR": -0.367
      }
    },
    "expR_spread": 0.935,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 27,
        "wrTP1": 44.4,
        "expR": -0.205
      },
      "NQ": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.795
      },
      "GC": {
        "n": 4,
        "wrTP1": 75.0,
        "expR": 0.512
      }
    },
    "expR_spread": 1.0,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 262,
        "wrTP1": 40.1,
        "expR": 0.096
      },
      "NQ": {
        "n": 391,
        "wrTP1": 46.5,
        "expR": 0.015
      },
      "ES": {
        "n": 373,
        "wrTP1": 41.6,
        "expR": -0.068
      },
      "CL": {
        "n": 459,
        "wrTP1": 45.8,
        "expR": -0.051
      },
      "YM": {
        "n": 291,
        "wrTP1": 44.0,
        "expR": 0.032
      }
    },
    "expR_spread": 0.164,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 116,
        "wrTP1": 44.8,
        "expR": 0.104
      },
      "GC": {
        "n": 192,
        "wrTP1": 38.0,
        "expR": -0.156
      },
      "YM": {
        "n": 288,
        "wrTP1": 41.3,
        "expR": 0.011
      },
      "ES": {
        "n": 216,
        "wrTP1": 43.1,
        "expR": -0.02
      },
      "CL": {
        "n": 35,
        "wrTP1": 28.6,
        "expR": -0.528
      }
    },
    "expR_spread": 0.632,
    "verdict": "instrument-specific"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": -0.213
      },
      "CL": {
        "n": 3,
        "wrTP1": 33.3,
        "expR": -0.527
      },
      "YM": {
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.673
      },
      "ES": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": 0.188
      },
      "NQ": {
        "n": 3,
        "wrTP1": 33.3,
        "expR": -0.387
      }
    },
    "expR_spread": 0.861,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 8,
        "wrTP1": 37.5,
        "expR": -0.004
      },
      "ES": {
        "n": 3,
        "wrTP1": 33.3,
        "expR": -0.44
      },
      "GC": {
        "n": 3,
        "wrTP1": 0.0,
        "expR": -0.327
      }
    },
    "expR_spread": 0.436,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 181,
        "wrTP1": 50.3,
        "expR": 0.086
      },
      "GC": {
        "n": 125,
        "wrTP1": 42.4,
        "expR": -0.039
      },
      "CL": {
        "n": 232,
        "wrTP1": 47.8,
        "expR": -0.005
      },
      "ES": {
        "n": 180,
        "wrTP1": 46.1,
        "expR": -0.07
      },
      "YM": {
        "n": 154,
        "wrTP1": 39.6,
        "expR": -0.206
      }
    },
    "expR_spread": 0.292,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 65,
        "wrTP1": 40.0,
        "expR": -0.117
      },
      "YM": {
        "n": 156,
        "wrTP1": 45.5,
        "expR": -0.012
      },
      "GC": {
        "n": 85,
        "wrTP1": 38.8,
        "expR": -0.112
      },
      "NQ": {
        "n": 62,
        "wrTP1": 45.2,
        "expR": 0.005
      },
      "CL": {
        "n": 17,
        "wrTP1": 35.3,
        "expR": -0.412
      }
    },
    "expR_spread": 0.417,
    "verdict": "instrument-specific"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 3,
        "wrTP1": 100.0,
        "expR": 0.443
      },
      "YM": {
        "n": 3,
        "wrTP1": 100.0,
        "expR": 0.763
      }
    },
    "expR_spread": 0.32,
    "verdict": "universal"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 11,
        "wrTP1": 63.6,
        "expR": 0.235
      },
      "ES": {
        "n": 62,
        "wrTP1": 54.8,
        "expR": 0.291
      },
      "YM": {
        "n": 58,
        "wrTP1": 48.3,
        "expR": 0.001
      },
      "CL": {
        "n": 82,
        "wrTP1": 56.1,
        "expR": 0.129
      },
      "NQ": {
        "n": 89,
        "wrTP1": 47.2,
        "expR": -0.078
      }
    },
    "expR_spread": 0.369,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 35,
        "wrTP1": 60.0,
        "expR": 0.181
      },
      "ES": {
        "n": 29,
        "wrTP1": 51.7,
        "expR": -0.015
      },
      "GC": {
        "n": 27,
        "wrTP1": 29.6,
        "expR": -0.369
      },
      "YM": {
        "n": 38,
        "wrTP1": 44.7,
        "expR": 0.049
      },
      "CL": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": -0.13
      }
    },
    "expR_spread": 0.55,
    "verdict": "instrument-specific"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 10,
  "near_news_30m": {
    "n": 0
  },
  "away_from_news": {
    "n": 4455,
    "wrTP1": 44.4,
    "nSL": 2167,
    "nTO": 312,
    "expR": -0.02,
    "pf": 0.96,
    "mfe_p25": 6.0,
    "mfe_p50": 14.0,
    "mfe_p75": 34.0,
    "winnerMAE_p75": 10.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 3.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -11.0,
    "revAfterSL_rate": 33.5
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
      "asOf": "2026-09-08 (martes -- primer dia habil COMPLETO post-feriado, salto grande de dato genuinamente nuevo, sin repeticion del bug de heal por segundo dia consecutivo)",
      "retest_1m_long": {
        "n": 1432,
        "deltaER_orig_minus_layer": 0.18,
        "ci90": [
          0.074,
          0.296
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 1135 a 1432 con el salto grande de dato de hoy, delta estable (0.183->0.18) -- segunda confirmacion independiente real."
      },
      "retest_1m_short": {
        "n": 514,
        "deltaER_orig_minus_layer": 0.417,
        "ci90": [
          0.2,
          0.644
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 229 a 514, el delta se hizo MAS fuerte (0.283->0.417) -- la lectura mas solida hasta ahora en este experimento."
      },
      "retest_2m_long": {
        "n": 742,
        "deltaER_orig_minus_layer": 0.01,
        "ci90": [
          -0.079,
          0.1
        ],
        "ci90_no_cruza_cero": false,
        "nota": "delta bajo a casi cero (0.028->0.01) con el salto de muestra -- sigue sin certificar, cada vez mas claro que 2m LONG no es candidato."
      },
      "retest_2m_short": {
        "n": 260,
        "deltaER_orig_minus_layer": 0.245,
        "ci90": [
          0.035,
          0.466
        ],
        "ci90_no_cruza_cero": true,
        "nota": "CERTIFICA POR PRIMERA VEZ hoy (ayer CI90=[-0.044,0.487] cruzaba cero, n=129->260) -- ya las tres TF de SHORT (1m/2m/5m) certifican."
      },
      "retest_5m_long": {
        "n": 274,
        "deltaER_orig_minus_layer": 0.178,
        "ci90": [
          0.005,
          0.38
        ],
        "ci90_no_cruza_cero": true,
        "nota": "CERTIFICA POR PRIMERA VEZ hoy pero al filo (limite inferior 0.005, casi cero; ayer CI90=[-0.086,0.36] cruzaba cero) -- tratar como debil hasta que se sostenga 1-2 corridas mas."
      },
      "retest_5m_short": {
        "n": 95,
        "deltaER_orig_minus_layer": 0.784,
        "ci90": [
          0.064,
          1.975
        ],
        "ci90_no_cruza_cero": true,
        "nota": "sigue siendo el efecto mas grande del dataset, CI se redujo bastante (era [0.012,3.025]) con mas muestra (n=62->95)."
      },
      "overall_by_basis_retestBar": {
        "n": 2941,
        "deltaER": 0.169,
        "ci90": [
          0.097,
          0.241
        ],
        "nota": "n subio de 2284 a 2941 con el salto de dato de hoy, delta estable -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba"
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
      "Vigilar: retestBar2 (1m SHORT = mecha vela retest + vela previa) sigue siendo una fraccion chica de la muestra 1m short -- puede mover el numero cuando crezca."
    ],
    "beforeN": 4318,
    "afterN": 0,
    "before": {
      "n": 4318,
      "wrTP1": 44.3,
      "nSL": 2106,
      "nTO": 300,
      "expR": -0.021,
      "pf": 0.96,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
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
    "date": "2026-09-08",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-08T19:12:39-05:00",
    "schema": "sa-plan-2",
    "cleanest": "CL",
    "focus": {
      "sym": "CL",
      "verdict": "WAIT",
      "window": "17:00-21:00 CT",
      "setup": {
        "es": "A+ pullback al cluster POC/VWAP/zona dorada 92.36-92.94 (confluencia 9), a favor de la tendencia alcista mas limpia del complejo, con las 5 lecturas de tendencia alineadas",
        "en": "A+ pullback into the POC/VWAP/golden-zone cluster 92.36-92.94 (confluence 9), with the complex's cleanest uptrend and all 5 trend reads aligned"
      },
      "trigger": {
        "es": "rechazo confirmado (mecha + cierre 5m de vuelta sobre 92.94) dentro de 92.36-92.94; o FVG 1h 92.45-93.17 reclamado tras el toque",
        "en": "confirmed rejection (wick + 5m close back above 92.94) inside 92.36-92.94; or the 1h FVG 92.45-93.17 reclaimed after the tag"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 92.12 (low overnight de ayer)",
        "en": "5m close sustained below 92.12 (yesterday's overnight low)"
      },
      "note": {
        "es": "ya marco un nuevo maximo de sesion (94.78) sin dar el retroceso -- sigue sin perseguir, el cluster 92.36-92.94 sigue siendo la unica entrada limpia",
        "en": "it already made a fresh session high (94.78) without giving the pullback -- still don't chase, the 92.36-92.94 cluster remains the only clean entry"
      }
    },
    "alarm": {
      "es": "Dos tesis de fondo se rompieron hoy: ES cerro a 5.75pts de su invalidacion (7672.25 vs 7666.25) y GC a 11.3pts de la suya (4381.0 vs 4369.70), ambas con cierre debil y todas las lecturas frescas ya en corto. Ademas la precision de escenario A sigue bajo 30% en ES (21%) y GC (18%) en la ventana de 20 dias -- ningun GO en ninguno de los dos hasta ver una reaccion real en zona.",
      "en": "Two underlying theses broke today: ES closed 5.75pts from its invalidation (7672.25 vs 7666.25) and GC 11.3pts from its own (4381.0 vs 4369.70), both closing weak with every fresh read now short. On top of that, scenario-A accuracy stays under 30% in ES (21%) and GC (18%) over the 20-day window -- no GO in either until a real reaction shows up at a level."
    },
    "summary": {
      "es": [
        "!! Dos tesis de fondo se rompieron hoy: ES cerro a 5.75pts de su invalidacion (7672.25 vs 7666.25) y GC a 11.3pts de la suya (4381.0 vs 4369.70), ambas con cierre debil y todas las lecturas frescas ya en corto. Ademas la precision de escenario A sigue bajo 30% en ES (21%) y GC (18%) en la ventana de 20 dias -- ningun GO en ninguno de los dos hasta ver una reaccion real en zona.",
        "NQ: reapertura tranquila, subio a 29545 sin tocar el cluster 29575-29605; sigue en zona de no-trade, nada disparo aun.",
        "ES: ya toco el borde bajo del cluster 7680-7688 (dayHi 7682.75) pero sin cierre ni rechazo confirmado; sigue en WAIT.",

```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 1551,
  "by_verdict": {
    "AVOID": {
      "n": 457,
      "wrTP1": 53.8,
      "nSL": 191,
      "nTO": 20,
      "expR": 0.175,
      "pf": 1.41,
      "mfe_p25": 5.0,
      "mfe_p50": 10.0,
      "mfe_p75": 19.25,
      "winnerMAE_p75": 6.0,
      "winnerMAE_p90": 10.5,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -8.0,
      "revAfterSL_rate": 34.0
    },
    "GO": {
      "n": 220,
      "wrTP1": 41.8,
      "nSL": 122,
      "nTO": 6,
      "expR": -0.196,
      "pf": 0.65,
      "mfe_p25": 4.0,
      "mfe_p50": 9.0,
      "mfe_p75": 19.0,
      "winnerMAE_p75": 4.25,
      "winnerMAE_p90": 11.0,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -8.0,
      "revAfterSL_rate": 32.8
    },
    "WAIT": {
      "n": 874,
      "wrTP1": 47.5,
      "nSL": 416,
      "nTO": 43,
      "expR": 0.008,
      "pf": 1.02,
      "mfe_p25": 11.0,
      "mfe_p50": 32.0,
      "mfe_p75": 63.0,
      "winnerMAE_p75": 20.5,
      "winnerMAE_p90": 44.60000000000002,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -22.0,
      "revAfterSL_rate": 41.6
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.175,
      "ci90": [
        0.085,
        0.267
      ],
      "p_mean_le_0": 0.001,
      "n": 452
    },
    "GO": {
      "expR": -0.196,
      "ci90": [
        -0.301,
        -0.08
      ],
      "p_mean_le_0": 0.998,
      "n": 219
    },
    "WAIT": {
      "expR": 0.008,
      "ci90": [
        -0.057,
        0.072
      ],
      "p_mean_le_0": 0.443,
      "n": 848
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 457,
      "wrTP1": 53.8,
      "nSL": 191,
      "nTO": 20,
      "expR": 0.175,
      "pf": 1.41,
      "mfe_p25": 5.0,
      "mfe_p50": 10.0,
      "mfe_p75": 19.25,
      "winnerMAE_p75": 6.0,
      "winnerMAE_p90": 10.5,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -8.0,
      "revAfterSL_rate": 34.0
    },
    "GO_or_WAIT": {
      "n": 1094,
      "wrTP1": 46.3,
      "nSL": 538,
      "nTO": 49,
      "expR": -0.034,
      "pf": 0.93,
      "mfe_p25": 8.0,
      "mfe_p50": 25.0,
      "mfe_p75": 57.0,
      "winnerMAE_p75": 18.0,
      "winnerMAE_p90": 42.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 39.6
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.175,
      "ci90": [
        0.085,
        0.267
      ],
      "p_mean_le_0": 0.001,
      "n": 452
    },
    "GO_or_WAIT": {
      "expR": -0.034,
      "ci90": [
        -0.09,
        0.022
      ],
      "p_mean_le_0": 0.848,
      "n": 1067
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "GO": {
        "n": 5,
        "wrTP1": 40.0,
        "nSL": 3,
        "nTO": 0,
        "expR": -0.212,
        "pf": 0.65,
        "mfe_p25": 2.0,
        "mfe_p50": 4.0,
        "mfe_p75": 24.0,
        "winnerMAE_p75": 5.25,
        "winnerMAE_p90": 6.3,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -8.0,
        "revAfterSL_rate": 33.3
      },
      "WAIT": {
        "n": 8,
        "wrTP1": 62.5,
        "nSL": 2,
        "nTO": 1,
        "expR": 0.396,
        "pf": 2.58,
        "mfe_p25": 47.75,
        "mfe_p50": 71.5,
        "mfe_p75": 113.25,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 99.80000000000001,
        "loserMFEbeforeSL_p50": 1.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 4.5,
        "entryZoneTk_p50": -22.0,
        "revAfterSL_rate": 50.0
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 8,
        "wrTP1": 50.0,
        "nSL": 4,
        "nTO": 0,
        "expR": -0.036,
        "pf": 0.93,
        "mfe_p25": 2.0,
        "mfe_p50": 7.5,
        "mfe_p75": 12.25,
        "winnerMAE_p75": 0.25,
        "winnerMAE_p90": 0.7000000000000002,
        "loserMFEbeforeSL_p50": 1.5,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -7.5,
        "revAfterSL_rate": 25.0
      },
      "WAIT": {
        "n": 13,
        "wrTP1": 69.2,
        "nSL": 4,
        "nTO": 0,
        "expR": 0.158,
        "pf": 1.52,
        "mfe_p25": 9.0,
        "mfe_p50": 28.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 64.0,
        "winnerMAE_p90": 77.6,
        "loserMFEbeforeSL_p50": 9.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 10.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 25.0
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 245,
        "wrTP1": 56.3,
        "nSL": 94,
        "nTO": 13,
        "expR": 0.211,
        "pf": 1.54,
        "mfe_p25": 5.0,
        "mfe_p50": 10.0,
        "mfe_p75": 18.0,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 12.0,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -7.0,
        "revAfterSL_rate": 45.7
      },
      "GO": {
        "n": 173,
        "wrTP1": 44.5,
        "nSL": 95,
        "nTO": 1,
        "expR": -0.18,
        "pf": 0.67,
        "mfe_p25": 4.0,
        "mfe_p50": 10.5,
        "mfe_p75": 24.25,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 14.400000000000006,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 34.7
      },
      "WAIT": {
        "n": 346,
        "wrTP1": 49.4,
        "nSL": 168,
        "nTO": 7,
        "expR": 0.073,
        "pf": 1.15,
        "mfe_p25": 19.0,
        "mfe_p50": 43.5,
        "mfe_p75": 81.75,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 42.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 42.9
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 204,
        "wrTP1": 51.0,
        "nSL": 93,
        "nTO": 7,
        "expR": 0.139,
        "pf": 1.3,
        "mfe_p25": 6.0,
        "mfe_p50": 12.0,
        "mfe_p75": 23.0,
        "winnerMAE_p75": 5.0,
        "winnerMAE_p90": 8.0,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -8.0,
        "revAfterSL_rate": 22.6
      },
      "GO": {
        "n": 40,
        "wrTP1": 32.5,
        "nSL": 22,
        "nTO": 5,
        "expR": -0.221,
        "pf": 0.61,
        "mfe_p25": 4.0,
        "mfe_p50": 6.5,
        "mfe_p75": 13.25,
        "winnerMAE_p75": 1.0,
        "winnerMAE_p90": 3.8000000000000007,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -6.0,
        "revAfterSL_rate": 22.7
      },
      "WAIT": {
        "n": 507,
        "wrTP1": 45.4,
        "nSL": 242,
        "nTO": 35,
        "expR": -0.049,
        "pf": 0.9,
        "mfe_p25": 8.0,
        "mfe_p50": 22.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 44.099999999999994,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 40.9
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```
