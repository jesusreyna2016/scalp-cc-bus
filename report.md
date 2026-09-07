# Scalp CC · report 2026-09-07T01:14Z
- signals=3269 outcomes=3169 pares_resueltos=3257 pendientes=12 huerfanos=22

## ⚠ ALERTAS (llevar al frente del resumen)
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.138 vs -0.035, delta 0.172 CI90 [0.084, 0.262], n 2284). Candidato para experiments.json + revision semanal.

- E[R] global: {"expR": -0.022, "ci90": [-0.058, 0.014], "p_mean_le_0": 0.848, "n": 3147}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 42 | 47.6 | 0.276 | 1.64 | 17 | 10.0 | 6.25 | 17.6 |
| 1m/INV/SHORT | 19 | 68.4 | 0.264 | 1.95 | 5 | 13.0 | 21.0 | 40.0 |
| 1m/RETEST/LONG | 1412 | 43.0 | -0.015 | 0.97 | 717 | 11.0 | 9.0 | 27.8 |
| 1m/RETEST/SHORT | 479 | 43.2 | -0.013 | 0.97 | 226 | 16.0 | 10.0 | 37.6 |
| 2m/INV/LONG | 18 | 38.9 | -0.271 | 0.56 | 11 | 5.5 | 7.5 | 27.3 |
| 2m/INV/SHORT | 6 | 50.0 | -0.267 | 0.47 | 3 | 8.5 | 14.0 | 33.3 |
| 2m/RETEST/LONG | 708 | 45.5 | -0.072 | 0.86 | 364 | 14.0 | 12.0 | 37.4 |
| 2m/RETEST/SHORT | 221 | 40.7 | -0.124 | 0.77 | 113 | 18.0 | 17.5 | 43.4 |
| 5m/INV/LONG | 6 | 100.0 | 0.712 | 99.0 | 0 | 28.5 | 28.25 | None |
| 5m/INV/SHORT | 4 | 75.0 | 0.018 | 1.07 | 1 | 56.5 | 88.5 | 100.0 |
| 5m/RETEST/LONG | 246 | 52.8 | 0.086 | 1.19 | 104 | 20.0 | 18.75 | 52.9 |
| 5m/RETEST/SHORT | 96 | 47.9 | -0.018 | 0.96 | 42 | 30.5 | 23.0 | 35.7 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 217 | 20.7 | -0.084 | 0.88 | 141 | 16.0 | 16.0 | 13.5 |
| B | 1243 | 44.5 | 0.003 | 1.01 | 618 | 17.0 | 12.0 | 30.9 |
| C | 1797 | 47.6 | -0.033 | 0.93 | 844 | 12.0 | 11.0 | 40.2 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 1380 | 46.6 | -0.04 | 0.92 | 651 | 10.0 | 8.0 | 42.2 |
| London | 492 | 43.9 | -0.104 | 0.81 | 268 | 16.0 | 12.0 | 36.6 |
| NY | 468 | 44.0 | 0.198 | 1.4 | 224 | 33.5 | 21.0 | 30.4 |
| Sin KZ | 917 | 42.4 | -0.063 | 0.88 | 460 | 14.0 | 11.0 | 23.5 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 552 | 43.8 | -0.02 | 0.96 | 264 | 18.0 | 19.0 | 37.1 |
| edge=0 | 1552 | 47.4 | -0.027 | 0.94 | 744 | 11.0 | 9.0 | 41.7 |
| edge=1 | 1153 | 41.3 | -0.017 | 0.97 | 595 | 18.0 | 14.0 | 23.7 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| aligned=1 | 3246 | 44.6 | -0.024 | 0.95 | 1602 | 13.0 | 11.0 | 34.3 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 1 | 100.0 | 2.59 | 99.0 | 0 | 47.0 | 4.0 | None |
| INV/LONG|edge=0 | 31 | 48.4 | 0.047 | 1.1 | 15 | 6.0 | 4.5 | 26.7 |
| INV/LONG|edge=1 | 34 | 50.0 | 0.201 | 1.49 | 13 | 19.0 | 17.0 | 15.4 |
| INV/SHORT|edge=-1 | 12 | 75.0 | 0.262 | 2.05 | 3 | 23.0 | 50.0 | 0.0 |
| INV/SHORT|edge=0 | 15 | 60.0 | 0.047 | 1.13 | 5 | 12.0 | 74.0 | 80.0 |
| INV/SHORT|edge=1 | 2 | 50.0 | -0.29 | 0.42 | 1 | 7.0 | 5.0 | 0.0 |
| RETEST/LONG|edge=-1 | 143 | 46.9 | 0.12 | 1.26 | 63 | 9.0 | 7.0 | 49.2 |
| RETEST/LONG|edge=0 | 1171 | 48.7 | -0.031 | 0.94 | 566 | 10.0 | 8.0 | 41.2 |
| RETEST/LONG|edge=1 | 1052 | 40.1 | -0.031 | 0.94 | 556 | 19.0 | 14.0 | 22.7 |
| RETEST/SHORT|edge=-1 | 396 | 41.7 | -0.088 | 0.84 | 198 | 23.0 | 21.0 | 33.8 |
| RETEST/SHORT|edge=0 | 335 | 42.4 | -0.025 | 0.95 | 158 | 14.0 | 11.0 | 43.7 |
| RETEST/SHORT|edge=1 | 65 | 55.4 | 0.11 | 1.27 | 25 | 13.0 | 9.0 | 52.0 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 18 | 50.0 | 0.352 | 1.91 | 6 | 11.0 | 7.0 | 0.0 |
| INV/LONG|tier=C | 48 | 50.0 | 0.098 | 1.21 | 22 | 9.0 | 9.25 | 27.3 |
| INV/SHORT|tier=B | 7 | 71.4 | 0.201 | 1.71 | 2 | 9.0 | 12.0 | 0.0 |
| INV/SHORT|tier=C | 22 | 63.6 | 0.086 | 1.26 | 7 | 26.0 | 71.5 | 57.1 |
| RETEST/LONG|tier=A+ | 159 | 19.5 | -0.11 | 0.84 | 103 | 13.0 | 17.5 | 10.7 |
| RETEST/LONG|tier=B | 872 | 43.3 | 0.011 | 1.02 | 452 | 15.0 | 10.0 | 28.3 |
| RETEST/LONG|tier=C | 1335 | 48.7 | -0.034 | 0.93 | 630 | 11.0 | 10.0 | 39.8 |
| RETEST/SHORT|tier=A+ | 58 | 24.1 | -0.015 | 0.98 | 38 | 29.0 | 8.0 | 21.1 |
| RETEST/SHORT|tier=B | 346 | 46.5 | -0.04 | 0.92 | 158 | 19.0 | 19.0 | 39.9 |
| RETEST/SHORT|tier=C | 392 | 42.9 | -0.054 | 0.89 | 185 | 15.0 | 14.0 | 42.2 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 66 | 50.0 | 0.165 | 1.37 | 28 | 9.0 | 8.0 | 21.4 |
| INV/SHORT|aligned=1 | 29 | 65.5 | 0.115 | 1.36 | 9 | 14.0 | 57.0 | 44.4 |
| RETEST/LONG|aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| RETEST/LONG|aligned=1 | 2355 | 44.7 | -0.024 | 0.95 | 1184 | 12.0 | 10.0 | 32.9 |
| RETEST/SHORT|aligned=1 | 796 | 43.1 | -0.045 | 0.91 | 381 | 18.0 | 16.0 | 39.1 |

## Autopsia de SL
n_losses=1603  causas: RR-bajo×646, contra-estructura×608, stop-en-el-minimo×549, killzone-Asia-largo×476, sin-nivel-detras×333, estirado×271, chop×226, SL-muy-pegado×179, sin-causa-clara×139, contra-sesgo×1
- INV/LONG (n=28): killzone-Asia-largo×16, RR-bajo×15, contra-estructura×11, stop-en-el-minimo×6, estirado×5, SL-muy-pegado×3, sin-nivel-detras×3, chop×1
- INV/SHORT (n=9): contra-estructura×6, RR-bajo×6, stop-en-el-minimo×4, chop×1, sin-causa-clara×1, SL-muy-pegado×1
- RETEST/LONG (n=1185): RR-bajo×481, killzone-Asia-largo×460, contra-estructura×447, stop-en-el-minimo×390, sin-nivel-detras×257, estirado×187, chop×171, SL-muy-pegado×127, sin-causa-clara×87, contra-sesgo×1
- RETEST/SHORT (n=381): stop-en-el-minimo×149, RR-bajo×144, contra-estructura×144, estirado×79, sin-nivel-detras×73, chop×53, sin-causa-clara×51, SL-muy-pegado×48

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
    "n": 3132,
    "naive_expR": -0.023,
    "managed_expR": 0.051,
    "delta": 0.074,
    "avgEntryBetterTk_p50": 2.5,
    "fill_t3plus_pct": 48.3,
    "fill_full_pct": 33.9,
    "m1_rate": 33.9,
    "m2_rate": 20.2,
    "m3_rate": 10.8,
    "beAfterM1_rate": 16.9
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 41,
      "naive_expR": 0.276,
      "managed_expR": 0.389,
      "delta": 0.113,
      "avgEntryBetterTk_p50": 1.0,
      "fill_t3plus_pct": 34.1,
      "fill_full_pct": 29.3,
      "m1_rate": 46.3,
      "m2_rate": 31.7,
      "m3_rate": 17.1,
      "beAfterM1_rate": 22.0
    },
    "1m/INV/SHORT": {
      "n": 18,
      "naive_expR": 0.264,
      "managed_expR": 0.653,
      "delta": 0.39,
      "avgEntryBetterTk_p50": 3.85,
      "fill_t3plus_pct": 38.9,
      "fill_full_pct": 33.3,
      "m1_rate": 44.4,
      "m2_rate": 27.8,
      "m3_rate": 11.1,
      "beAfterM1_rate": 16.7
    },
    "1m/RETEST/LONG": {
      "n": 1374,
      "naive_expR": -0.017,
      "managed_expR": 0.044,
      "delta": 0.061,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 49.6,
      "fill_full_pct": 36.2,
      "m1_rate": 33.1,
      "m2_rate": 19.6,
      "m3_rate": 11.0,
      "beAfterM1_rate": 15.6
    },
    "1m/RETEST/SHORT": {
      "n": 444,
      "naive_expR": -0.01,
      "managed_expR": 0.129,
      "delta": 0.139,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 51.1,
      "fill_full_pct": 31.1,
      "m1_rate": 39.4,
      "m2_rate": 24.5,
      "m3_rate": 13.1,
      "beAfterM1_rate": 19.1
    },
    "2m/INV/LONG": {
      "n": 18,
      "naive_expR": -0.271,
      "managed_expR": -0.241,
      "delta": 0.03,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 55.6,
      "fill_full_pct": 38.9,
      "m1_rate": 16.7,
      "m2_rate": 16.7,
      "m3_rate": 0.0,
      "beAfterM1_rate": 5.6
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
      "n": 690,
      "naive_expR": -0.075,
      "managed_expR": 0.008,
      "delta": 0.083,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 47.4,
      "fill_full_pct": 31.7,
      "m1_rate": 32.9,
      "m2_rate": 19.6,
      "m3_rate": 10.0,
      "beAfterM1_rate": 17.0
    },
    "2m/RETEST/SHORT": {
      "n": 209,
      "naive_expR": -0.124,
      "managed_expR": -0.008,
      "delta": 0.116,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 48.8,
      "fill_full_pct": 39.7,
      "m1_rate": 31.6,
      "m2_rate": 19.1,
      "m3_rate": 11.5,
      "beAfterM1_rate": 17.7
    },
    "5m/INV/LONG": {
      "n": 6,
      "naive_expR": 0.712,
      "managed_expR": 0.903,
      "delta": 0.191,
      "avgEntryBetterTk_p50": 4.85,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 33.3,
      "m1_rate": 50.0,
      "m2_rate": 33.3,
      "m3_rate": 0.0,
      "beAfterM1_rate": 16.7
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
      "n": 235,
      "naive_expR": 0.086,
      "managed_expR": -0.041,
      "delta": -0.127,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 37.9,
      "fill_full_pct": 27.2,
      "m1_rate": 29.4,
      "m2_rate": 15.3,
      "m3_rate": 7.2,
      "beAfterM1_rate": 18.7
    },
    "5m/RETEST/SHORT": {
      "n": 87,
      "naive_expR": -0.025,
      "managed_expR": 0.213,
      "delta": 0.237,
      "avgEntryBetterTk_p50": 4.8,
      "fill_t3plus_pct": 50.6,
      "fill_full_pct": 31.0,
      "m1_rate": 41.4,
      "m2_rate": 25.3,
      "m3_rate": 11.5,
      "beAfterM1_rate": 19.5
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 2456,
    "layer_expR": -0.033,
    "orig_expR": 0.148,
    "delta_orig_minus_layer": 0.181,
    "delta_ci90": [
      0.102,
      0.273
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 45.4,
    "orig_wrTP1": 32.0,
    "slTk_p50": 19.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 4.3,
    "orig_saved_from_SL": 7,
    "orig_caused_SL": 338
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 81,
      "layer_expR": 0.154,
      "orig_expR": 0.536,
      "delta_orig_minus_layer": 0.382,
      "delta_ci90": [
        -0.111,
        0.938
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 54.3,
      "orig_wrTP1": 30.9,
      "slTk_p50": 13.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 4.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 19
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
      "n": 2284,
      "layer_expR": -0.035,
      "orig_expR": 0.138,
      "delta_orig_minus_layer": 0.172,
      "delta_ci90": [
        0.084,
        0.262
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.4,
      "orig_wrTP1": 32.2,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.1,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 309
    },
    "retestBar2": {
      "n": 91,
      "layer_expR": -0.165,
      "orig_expR": 0.05,
      "delta_orig_minus_layer": 0.215,
      "delta_ci90": [
        -0.218,
        0.852
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 38.5,
      "orig_wrTP1": 27.5,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 15.0,
      "orig_wider_pct": 8.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 10
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 41,
      "layer_expR": 0.276,
      "orig_expR": 0.516,
      "delta_orig_minus_layer": 0.24,
      "delta_ci90": [
        -0.431,
        0.958
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.8,
      "orig_wrTP1": 29.3,
      "slTk_p50": 10.0,
      "slOrigTk_p50": 2.0,
      "orig_wider_pct": 4.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 8
    },
    "1m/INV/SHORT": {
      "n": 8,
      "layer_expR": 0.527,
      "orig_expR": 0.21,
      "delta_orig_minus_layer": -0.318,
      "delta_ci90": [
        -1.305,
        0.655
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 87.5,
      "orig_wrTP1": 37.5,
      "slTk_p50": 18.5,
      "slOrigTk_p50": 8.5,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 4
    },
    "1m/RETEST/LONG": {
      "n": 1135,
      "layer_expR": -0.01,
      "orig_expR": 0.174,
      "delta_orig_minus_layer": 0.183,
      "delta_ci90": [
        0.057,
        0.324
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 43.8,
      "orig_wrTP1": 29.3,
      "slTk_p50": 17.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.8,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 165
    },
    "1m/RETEST/SHORT": {
      "n": 229,
      "layer_expR": -0.098,
      "orig_expR": 0.185,
      "delta_orig_minus_layer": 0.283,
      "delta_ci90": [
        0.011,
        0.609
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 41.9,
      "orig_wrTP1": 29.7,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 28
    },
    "2m/INV/LONG": {
      "n": 18,
      "layer_expR": -0.271,
      "orig_expR": 1.437,
      "delta_orig_minus_layer": 1.708,
      "delta_ci90": [
        0.256,
        3.449
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 38.9,
      "orig_wrTP1": 27.8,
      "slTk_p50": 10.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 5.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 2
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
      "n": 596,
      "layer_expR": -0.053,
      "orig_expR": -0.025,
      "delta_orig_minus_layer": 0.028,
      "delta_ci90": [
        -0.069,
        0.136
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.0,
      "orig_wrTP1": 33.2,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 82
    },
    "2m/RETEST/SHORT": {
      "n": 129,
      "layer_expR": -0.226,
      "orig_expR": -0.011,
      "delta_orig_minus_layer": 0.215,
      "delta_ci90": [
        -0.044,
        0.487
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 39.5,
      "orig_wrTP1": 29.5,
      "slTk_p50": 31.0,
      "slOrigTk_p50": 14.0,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 14
    },
    "5m/INV/LONG": {
      "n": 6,
      "layer_expR": 0.712,
      "orig_expR": -0.543,
      "delta_orig_minus_layer": -1.255,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 100.0,
      "orig_wrTP1": 33.3,
      "slTk_p50": 34.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 16.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 4
    },
    "5m/RETEST/LONG": {
      "n": 224,
      "layer_expR": 0.066,
      "orig_expR": 0.183,
      "delta_orig_minus_layer": 0.117,
      "delta_ci90": [
        -0.086,
        0.36
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 54.9,
      "orig_wrTP1": 44.2,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 13.0,
      "orig_wider_pct": 15.6,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 26
    },
    "5m/RETEST/SHORT": {
      "n": 62,
      "layer_expR": -0.236,
      "orig_expR": 0.891,
      "delta_orig_minus_layer": 1.127,
      "delta_ci90": [
        0.012,
        3.025
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 40.3,
      "orig_wrTP1": 38.7,
      "slTk_p50": 33.0,
      "slOrigTk_p50": 26.0,
      "orig_wider_pct": 21.0,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 4
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
    "n": 26,
    "wrTP1": 50.0,
    "expR": -0.193
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 3057,
  "brier": 0.2199,
  "bias": -0.177,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -0.927
    },
    {
      "feature": "stretchAtr",
      "weight": -0.202
    },
    {
      "feature": "rvol",
      "weight": 0.132
    },
    {
      "feature": "chopIdx",
      "weight": -0.128
    },
    {
      "feature": "aligned",
      "weight": -0.064
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.064
    },
    {
      "feature": "hourNY",
      "weight": 0.054
    },
    {
      "feature": "entryZoneTk",
      "weight": 0.045
    },
    {
      "feature": "emaStack",
      "weight": -0.043
    },
    {
      "feature": "biasScore",
      "weight": -0.038
    },
    {
      "feature": "structDir",
      "weight": -0.028
    },
    {
      "feature": "nearTk",
      "weight": -0.006
    },
    {
      "feature": "nearEdge",
      "weight": -0.003
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.127,
      "actual": 0.174,
      "n": 305
    },
    {
      "bin": 1,
      "pred": 0.309,
      "actual": 0.265,
      "n": 306
    },
    {
      "bin": 2,
      "pred": 0.391,
      "actual": 0.317,
      "n": 306
    },
    {
      "bin": 3,
      "pred": 0.446,
      "actual": 0.397,
      "n": 305
    },
    {
      "bin": 4,
      "pred": 0.493,
      "actual": 0.428,
      "n": 306
    },
    {
      "bin": 5,
      "pred": 0.531,
      "actual": 0.536,
      "n": 306
    },
    {
      "bin": 6,
      "pred": 0.56,
      "actual": 0.597,
      "n": 305
    },
    {
      "bin": 7,
      "pred": 0.59,
      "actual": 0.637,
      "n": 306
    },
    {
      "bin": 8,
      "pred": 0.624,
      "actual": 0.686,
      "n": 306
    },
    {
      "bin": 9,
      "pred": 0.691,
      "actual": 0.719,
      "n": 306
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
    "expR": 0.276,
    "ci90": [
      -0.102,
      0.653
    ],
    "p_mean_le_0": 0.116,
    "n": 41,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.264,
    "ci90": [
      -0.06,
      0.61
    ],
    "p_mean_le_0": 0.093,
    "n": 18,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": -0.015,
    "ci90": [
      -0.073,
      0.044
    ],
    "p_mean_le_0": 0.672,
    "n": 1378,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": -0.013,
    "ci90": [
      -0.101,
      0.069
    ],
    "p_mean_le_0": 0.614,
    "n": 451,
    "survives_fdr10": false
  },
  "2m/INV/LONG": {
    "expR": -0.271,
    "ci90": [
      -0.638,
      0.119
    ],
    "p_mean_le_0": 0.879,
    "n": 18,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.072,
    "ci90": [
      -0.139,
      -0.002
    ],
    "p_mean_le_0": 0.956,
    "n": 693,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": -0.124,
    "ci90": [
      -0.246,
      -0.001
    ],
    "p_mean_le_0": 0.953,
    "n": 209,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.086,
    "ci90": [
      -0.034,
      0.218
    ],
    "p_mean_le_0": 0.128,
    "n": 235,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": -0.018,
    "ci90": [
      -0.209,
      0.194
    ],
    "p_mean_le_0": 0.561,
    "n": 88,
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
      "n": 1291,
      "wrTP1": 43.9,
      "expR": 0.011,
      "pf": 1.02,
      "defining_features": {
        "atrPctUsed": 0.67,
        "biasScore": 0.54,
        "hourNY": -0.46,
        "nearEdge": 0.45
      }
    },
    {
      "id": 1,
      "n": 728,
      "wrTP1": 44.1,
      "expR": -0.002,
      "pf": 1.0,
      "defining_features": {
        "biasScore": -1.5,
        "emaStack": -1.27,
        "nearEdge": -1.08,
        "structDir": -0.57
      }
    },
    {
      "id": 0,
      "n": 762,
      "wrTP1": 47.4,
      "expR": -0.06,
      "pf": 0.88,
      "defining_features": {
        "hourNY": 1.16,
        "atrPctUsed": -0.83,
        "emaStack": 0.49,
        "biasScore": 0.42
      }
    },
    {
      "id": 2,
      "n": 476,
      "wrTP1": 43.1,
      "expR": -0.084,
      "pf": 0.84,
      "defining_features": {
        "stretchAtr": 1.55,
        "chopIdx": -1.29,
        "rvol": 1.13,
        "hourNY": -0.44
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
        "n": 13,
        "wrTP1": 53.8,
        "expR": 0.428
      },
      "YM": {
        "n": 18,
        "wrTP1": 50.0,
        "expR": 0.501
      },
      "ES": {
        "n": 5,
        "wrTP1": 40.0,
        "expR": -0.5
      },
      "GC": {
        "n": 4,
        "wrTP1": 25.0,
        "expR": -0.608
      }
    },
    "expR_spread": 1.109,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 14,
        "wrTP1": 64.3,
        "expR": 0.198
      },
      "NQ": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.795
      }
    },
    "expR_spread": 0.597,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 225,
        "wrTP1": 38.7,
        "expR": 0.089
      },
      "NQ": {
        "n": 256,
        "wrTP1": 46.1,
        "expR": 0.005
      },
      "ES": {
        "n": 333,
        "wrTP1": 40.8,
        "expR": -0.058
      },
      "CL": {
        "n": 309,
        "wrTP1": 45.0,
        "expR": -0.108
      },
      "YM": {
        "n": 289,
        "wrTP1": 43.9,
        "expR": 0.034
      }
    },
    "expR_spread": 0.197,
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
        "n": 102,
        "wrTP1": 34.3,
        "expR": -0.189
      },
      "YM": {
        "n": 128,
        "wrTP1": 47.7,
        "expR": 0.093
      },
      "ES": {
        "n": 107,
        "wrTP1": 45.8,
        "expR": 0.003
      },
      "CL": {
        "n": 26,
        "wrTP1": 38.5,
        "expR": -0.365
      }
    },
    "expR_spread": 0.469,
    "verdict": "instrument-specific"
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
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.673
      },
      "ES": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": 0.188
      }
    },
    "expR_spread": 0.861,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 129,
        "wrTP1": 49.6,
        "expR": -0.028
      },
      "GC": {
        "n": 106,
        "wrTP1": 42.5,
        "expR": -0.012
      },
      "CL": {
        "n": 164,
        "wrTP1": 48.2,
        "expR": -0.061
      },
      "ES": {
        "n": 155,
        "wrTP1": 47.1,
        "expR": -0.03
      },
      "YM": {
        "n": 154,
        "wrTP1": 39.6,
        "expR": -0.206
      }
    },
    "expR_spread": 0.194,
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
        "n": 62,
        "wrTP1": 41.9,
        "expR": -0.121
      },
      "GC": {
        "n": 42,
        "wrTP1": 33.3,
        "expR": -0.192
      },
      "NQ": {
        "n": 62,
        "wrTP1": 45.2,
        "expR": 0.005
      },
      "CL": {
        "n": 15,
        "wrTP1": 40.0,
        "expR": -0.334
      }
    },
    "expR_spread": 0.339,
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
        "n": 56,
        "wrTP1": 55.4,
        "expR": 0.356
      },
      "YM": {
        "n": 57,
        "wrTP1": 49.1,
        "expR": 0.02
      },
      "CL": {
        "n": 50,
        "wrTP1": 58.0,
        "expR": 0.091
      },
      "NQ": {
        "n": 72,
        "wrTP1": 48.6,
        "expR": -0.088
      }
    },
    "expR_spread": 0.444,
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
        "n": 24,
        "wrTP1": 50.0,
        "expR": 0.022
      },
      "GC": {
        "n": 14,
        "wrTP1": 21.4,
        "expR": -0.568
      },
      "YM": {
        "n": 17,
        "wrTP1": 35.3,
        "expR": -0.08
      },
      "CL": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.015
      }
    },
    "expR_spread": 0.749,
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
    "n": 3257,
    "wrTP1": 44.6,
    "nSL": 1603,
    "nTO": 200,
    "expR": -0.022,
    "pf": 0.96,
    "mfe_p25": 6.0,
    "mfe_p50": 13.0,
    "mfe_p75": 35.0,
    "winnerMAE_p75": 11.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 3.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -11.0,
    "revAfterSL_rate": 34.2
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
    "hypothesis": "En RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. HASTA 2026-09-04 esto solo certificaba en SHORT (\"no aplica a largos\"); con la muestra de 2026-09-05 TAMBIEN certifica en 1m LONG, asi que se retira la exclusion dura de BUY RETEST y se deja como 'certifica por tf/side, no generalizar sin mirar la tabla'. 2026-09-06: mismas cifras exactas que 2026-09-05 (n identico) porque no llego dato nuevo -- mercado cerrado el fin de semana, no cuenta como dia adicional de confirmacion, ver next_steps.",
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
      "asOf": "2026-09-06 (cifras identicas a 2026-09-05, ver nota de dataset sin cambios)",
      "retest_1m_long": {
        "n": 1087,
        "deltaER_orig_minus_layer": 0.181,
        "ci90": [
          0.061,
          0.314
        ],
        "ci90_no_cruza_cero": true,
        "nota": "Se mantiene igual que 2026-09-05 (mismo n, no llego dato nuevo el fin de semana) -- confirmado que NO fue artefacto de la restauracion de datos (la restauracion de hoy reprodujo el mismo numero), pero todavia falta un dia con trades genuinamente nuevos para contar como confirmacion independiente."
      },
      "retest_1m_short": {
        "n": 219,
        "deltaER_orig_minus_layer": 0.296,
        "ci90": [
          0.013,
          0.633
        ],
        "ci90_no_cruza_cero": true,
        "nota": "sigue certificando, ya con muestra mas sana tras restaurar signals/2026-09-03.jsonl"
      },
      "retest_2m_long": {
        "n": 577,
        "deltaER_orig_minus_layer": 0.018,
        "ci90": [
          -0.078,
          0.124
        ],
        "ci90_no_cruza_cero": false
      },
      "retest_2m_short": {
        "n": 123,
        "deltaER_orig_minus_layer": 0.226,
        "ci90": [
          -0.046,
          0.505
        ],
        "ci90_no_cruza_cero": false,
        "nota": "no certifica pero el CI ya roza cero por poco"
      },
      "retest_5m_long": {
        "n": 214,
        "deltaER_orig_minus_layer": 0.124,
        "ci90": [
          -0.093,
          0.37
        ],
        "ci90_no_cruza_cero": false
      },
      "retest_5m_short": {
        "n": 61,
        "deltaER_orig_minus_layer": 1.145,
        "ci90": [
          0.013,
          3.032
        ],
        "ci90_no_cruza_cero": true,
        "nota": "sigue siendo el efecto mas grande del dataset, CI muy ancho por n chico"
      },
      "overall_by_basis_retestBar": {
        "n": 2200,
        "deltaER": 0.171,
        "ci90": [
          0.083,
          0.26
        ],
        "nota": "ya no mezcla una rama plana con una real (LONG y SHORT certifican ambos en 1m) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba"
      }
    },
    "next_steps": [
      "2026-09-05: se recupero signals/2026-09-03.jsonl (ver nota de la corrida en state.json/narrative y en el historico de los playbooks) -- estaba truncado de 1280 a 24 lineas por un commit 'heal' que en realidad BORRO datos en vez de repararlos.",
      "2026-09-06: EL MISMO BUG SE REPITIO -- un segundo commit 'heal 24 orphan signal(s) 2026-09-03' (0cf0a30, autor jesusreyna2016, ts commit 2026-09-04 20:31 -0500) volvio a truncar signals/2026-09-03.jsonl de 1280 a 24 lineas, DESPUES de que el agente ya lo habia arreglado el dia anterior (commit 945c337). Se restauro de nuevo desde 945c337. Se anadio una guarda permanente en analyze.py (file_integrity_check: compara lineas de cada signals/outcomes/*.jsonl contra el maximo visto en corridas previas via state.json.file_line_counts, y alerta si algun archivo ENCOGIO). Jesus debe revisar/desactivar el job externo de 'heal' de huerfanos -- esta confundiendo señales legitimas con duplicados y borrando datos reales dos veces en 3 dias.",
      "No llego dato de mercado nuevo el fin de semana del 2026-09-05/06 (CME cerrado) -- normal, no es un fallo de pipeline aparte del bug de 'heal' de arriba. La confirmacion de retest_1m_long queda pendiente de un dia habil con trades genuinamente nuevos (probablemente 2026-09-08, lunes).",
      "Revision semanal del domingo: confirmar sobre walk-forward + segment_significance (FDR 10%), no solo in-sample (walk_forward todavia no esta listo, solo 1 semana de datos).",
      "Anadir linea a predictions.jsonl con predictedDeltaER antes de aplicar.",
      "Cuando se confirme con datos nuevos genuinos (no solo restaurados): cambio en Pine = para RETEST (long y short, no solo short) usar lg_slOrig (mecha de la vela del retest) como SL de trabajo en 1m; en 5m solo SHORT; en 2m no aplicar todavia (ningun lado certifica). Poner changeDate el dia que se aplique en los 12 graficos.",
      "Vigilar: retestBar2 (1m SHORT = mecha vela retest + vela previa) sigue siendo una fraccion chica de la muestra 1m short (n=81 de by_basis) -- puede mover el numero cuando crezca."
    ],
    "beforeN": 3162,
    "afterN": 0,
    "before": {
      "n": 3162,
      "wrTP1": 44.3,
      "nSL": 1566,
      "nTO": 194,
      "expR": -0.028,
      "pf": 0.95,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 35.75,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 34.4
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
    "date": "2026-09-06",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-09-06T16:45:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "CL",
    "focus": {
      "sym": "CL",
      "verdict": "WAIT",
      "window": "20:00-23:00 CT",
      "setup": {
        "es": "A+ pullback a POC/VWAP 90.60-91.00, confluencia 6, a favor de la reactivacion semanal",
        "en": "A+ POC/VWAP pullback 90.60-91.00, confluence 6, with the weekly reactivation"
      },
      "trigger": {
        "es": "cierre 5m con mecha inferior en 90.60-91.00, o reclamo confirmado sobre VAH 91.67",
        "en": "5m close with a lower wick in 90.60-91.00, or a confirmed reclaim above VAH 91.67"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 89.04 (la propia invalidacion semanal, ya testeada ayer)",
        "en": "5m close sustained below 89.04 (the weekly invalidation itself, already tested yesterday)"
      },
      "note": {
        "es": "ayer toco la invalidacion exacta (88.72) y reclamo con fuerza -- el proceso mas limpio del complejo; espera el pullback real, no lo persigas",
        "en": "yesterday it tagged the exact invalidation (88.72) and reclaimed hard -- the complex's cleanest process; wait for the real pullback, don't chase it"
      }
    },
    "summary": {
      "es": [
        "NQ: cerro plano (+18pts) pero en el 23% inferior de un dia de whipsaw por NFP, dentro de zona de no-trade -- sesgo de dia LONG, sesion NEUTRAL, A+ en 29468-29505 si retrocede.",
        "ES: el cierre mas fragil del complejo, pegado al minimo del dia (7711.75) -- zona 7708-7723 con confluencia 8 pero con un FVG bajista bloqueando el 40% del camino al objetivo (OBJETIVO_BLOQUEADO).",
        "GC: el mas balanceado, cerrando a mitad de su rango -- solo zona B (confluencia 4) en 4441-4459, marco diario debilitado de +3 a +1.",
        "YM: primera fisura real del liderazgo de 4 sesiones, cierre en el 7% inferior del rango -- zona mas floja del complejo (confluencia 3) en 53235-53340.",
        "CL: el proceso mas limpio -- toco la invalidacion semanal exacta (88.72 vs 89.04) y reclamo con fuerza hasta cerca de VAH, cerrando en el 72% del rango.",
        "Sin noticias de alto impacto en la ventana de Asia esta noche (proximos eventos: miercoles-viernes de la semana que entra). Datos base = cierre del viernes 2026-09-04 congelado por el fin de semana (Globex reabre 17:00 CT hoy) -- no se marca 'datos rezagados', refleja el mercado cerrado, no un feed caido.",
        "Sizing: limite diario 1000 USD (extremo bajo, usar salvo indicacion contraria), 3 stops seguidos y se acaba el dia -- con los stops estructurales de esta noche (200-2500 USD/contrato full segun instrumento), varias zonas dan maxContracts 0-1 en full: usa micros donde el stop no quepa.",
        "Se calificio el dia de futuros 2026-09-04 (viernes, NFP) en esta corrida -- ver reviews/2026-09-04.md: 41% de aciertos en 66 predicciones e
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 885,
  "by_verdict": {
    "AVOID": {
      "n": 92,
      "wrTP1": 56.5,
      "nSL": 40,
      "nTO": 0,
      "expR": 0.204,
      "pf": 1.47,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 31.5,
      "winnerMAE_p75": 13.75,
      "winnerMAE_p90": 22.9,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 47.5
    },
    "GO": {
      "n": 122,
      "wrTP1": 37.7,
      "nSL": 75,
      "nTO": 1,
      "expR": -0.273,
      "pf": 0.56,
      "mfe_p25": 7.0,
      "mfe_p50": 16.0,
      "mfe_p75": 32.0,
      "winnerMAE_p75": 9.0,
      "winnerMAE_p90": 25.5,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 37.3
    },
    "WAIT": {
      "n": 671,
      "wrTP1": 46.5,
      "nSL": 321,
      "nTO": 38,
      "expR": -0.014,
      "pf": 0.97,
      "mfe_p25": 9.0,
      "mfe_p50": 28.0,
      "mfe_p75": 62.0,
      "winnerMAE_p75": 22.0,
      "winnerMAE_p90": 49.80000000000007,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -21.0,
      "revAfterSL_rate": 38.3
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 92,
      "wrTP1": 56.5,
      "nSL": 40,
      "nTO": 0,
      "expR": 0.204,
      "pf": 1.47,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 31.5,
      "winnerMAE_p75": 13.75,
      "winnerMAE_p90": 22.9,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 47.5
    },
    "GO_or_WAIT": {
      "n": 793,
      "wrTP1": 45.1,
      "nSL": 396,
      "nTO": 39,
      "expR": -0.055,
      "pf": 0.89,
      "mfe_p25": 8.0,
      "mfe_p50": 25.0,
      "mfe_p75": 59.0,
      "winnerMAE_p75": 21.0,
      "winnerMAE_p90": 48.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -20.0,
      "revAfterSL_rate": 38.1
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; sin prueba de significancia todavia (ver bootstrap_er_ci para eso mas adelante)."
}
```
