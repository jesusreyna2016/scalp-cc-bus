# Scalp CC · report 2026-09-05T01:30Z
- signals=3162 outcomes=3063 pares_resueltos=3140 pendientes=22 huerfanos=22

## ⚠ ALERTAS (llevar al frente del resumen)
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.135 vs -0.036, delta 0.171 CI90 [0.083, 0.26], n 2200). Candidato para experiments.json + revision semanal.

- E[R] global: {"expR": -0.023, "ci90": [-0.058, 0.013], "p_mean_le_0": 0.853, "n": 3041}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 40 | 47.5 | 0.307 | 1.72 | 16 | 10.0 | 5.0 | 18.8 |
| 1m/INV/SHORT | 19 | 68.4 | 0.264 | 1.95 | 5 | 13.0 | 21.0 | 40.0 |
| 1m/RETEST/LONG | 1355 | 43.0 | -0.025 | 0.95 | 695 | 11.0 | 9.0 | 27.8 |
| 1m/RETEST/SHORT | 465 | 43.7 | -0.004 | 0.99 | 219 | 15.0 | 10.0 | 37.4 |
| 2m/INV/LONG | 18 | 38.9 | -0.271 | 0.56 | 11 | 5.5 | 7.5 | 27.3 |
| 2m/INV/SHORT | 6 | 50.0 | -0.267 | 0.47 | 3 | 8.5 | 14.0 | 33.3 |
| 2m/RETEST/LONG | 687 | 45.4 | -0.073 | 0.86 | 354 | 14.0 | 12.0 | 36.7 |
| 2m/RETEST/SHORT | 214 | 41.6 | -0.106 | 0.8 | 108 | 17.0 | 16.0 | 42.6 |
| 5m/INV/LONG | 5 | 100.0 | 0.674 | 99.0 | 0 | 28.0 | 32.0 | None |
| 5m/INV/SHORT | 4 | 75.0 | 0.018 | 1.07 | 1 | 56.5 | 88.5 | 100.0 |
| 5m/RETEST/LONG | 234 | 53.0 | 0.098 | 1.22 | 99 | 20.5 | 18.25 | 53.5 |
| 5m/RETEST/SHORT | 93 | 49.5 | -0.007 | 0.99 | 41 | 32.0 | 23.0 | 36.6 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 215 | 20.9 | -0.075 | 0.89 | 139 | 16.0 | 16.0 | 13.7 |
| B | 1207 | 44.5 | -0.009 | 0.98 | 606 | 17.0 | 12.0 | 30.4 |
| C | 1718 | 48.0 | -0.027 | 0.94 | 807 | 12.0 | 11.0 | 40.4 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 1285 | 46.9 | -0.026 | 0.95 | 604 | 10.0 | 8.0 | 42.9 |
| London | 488 | 44.3 | -0.104 | 0.81 | 268 | 16.0 | 12.0 | 36.6 |
| NY | 468 | 44.0 | 0.198 | 1.4 | 224 | 33.5 | 21.0 | 30.4 |
| Sin KZ | 899 | 42.5 | -0.088 | 0.84 | 456 | 14.0 | 11.75 | 22.8 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 526 | 44.1 | -0.047 | 0.91 | 254 | 17.0 | 19.0 | 35.8 |
| edge=0 | 1485 | 47.9 | -0.02 | 0.96 | 711 | 10.0 | 9.0 | 41.9 |
| edge=1 | 1129 | 41.1 | -0.015 | 0.97 | 587 | 19.0 | 14.0 | 23.9 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| aligned=1 | 3129 | 44.8 | -0.024 | 0.95 | 1551 | 13.0 | 11.0 | 34.1 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 1 | 100.0 | 2.59 | 99.0 | 0 | 47.0 | 4.0 | None |
| INV/LONG|edge=0 | 30 | 50.0 | 0.082 | 1.17 | 14 | 6.5 | 4.5 | 28.6 |
| INV/LONG|edge=1 | 32 | 46.9 | 0.175 | 1.4 | 13 | 14.0 | 13.5 | 15.4 |
| INV/SHORT|edge=-1 | 12 | 75.0 | 0.262 | 2.05 | 3 | 23.0 | 50.0 | 0.0 |
| INV/SHORT|edge=0 | 15 | 60.0 | 0.047 | 1.13 | 5 | 12.0 | 74.0 | 80.0 |
| INV/SHORT|edge=1 | 2 | 50.0 | -0.29 | 0.42 | 1 | 7.0 | 5.0 | 0.0 |
| RETEST/LONG|edge=-1 | 133 | 45.9 | -0.004 | 0.99 | 59 | 9.0 | 7.0 | 47.5 |
| RETEST/LONG|edge=0 | 1113 | 49.1 | -0.028 | 0.94 | 541 | 10.0 | 8.0 | 41.2 |
| RETEST/LONG|edge=1 | 1030 | 40.0 | -0.028 | 0.95 | 548 | 19.0 | 14.0 | 22.8 |
| RETEST/SHORT|edge=-1 | 380 | 42.4 | -0.08 | 0.85 | 192 | 23.0 | 21.0 | 32.8 |
| RETEST/SHORT|edge=0 | 327 | 43.1 | -0.005 | 0.99 | 151 | 13.0 | 11.0 | 44.4 |
| RETEST/SHORT|edge=1 | 65 | 55.4 | 0.11 | 1.27 | 25 | 13.0 | 9.0 | 52.0 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 18 | 50.0 | 0.352 | 1.91 | 6 | 11.0 | 7.0 | 0.0 |
| INV/LONG|tier=C | 45 | 48.9 | 0.1 | 1.21 | 21 | 9.0 | 7.75 | 28.6 |
| INV/SHORT|tier=B | 7 | 71.4 | 0.201 | 1.71 | 2 | 9.0 | 12.0 | 0.0 |
| INV/SHORT|tier=C | 22 | 63.6 | 0.086 | 1.26 | 7 | 26.0 | 71.5 | 57.1 |
| RETEST/LONG|tier=A+ | 158 | 19.6 | -0.104 | 0.85 | 102 | 13.0 | 17.5 | 10.8 |
| RETEST/LONG|tier=B | 844 | 43.0 | -0.009 | 0.98 | 443 | 16.0 | 11.0 | 28.0 |
| RETEST/LONG|tier=C | 1274 | 49.1 | -0.03 | 0.94 | 603 | 11.0 | 10.0 | 40.0 |
| RETEST/SHORT|tier=A+ | 57 | 24.6 | 0.003 | 1.0 | 37 | 28.5 | 8.0 | 21.6 |
| RETEST/SHORT|tier=B | 338 | 47.3 | -0.032 | 0.93 | 155 | 18.0 | 19.0 | 38.7 |
| RETEST/SHORT|tier=C | 377 | 43.5 | -0.038 | 0.92 | 176 | 14.0 | 13.25 | 42.6 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 63 | 49.2 | 0.169 | 1.38 | 27 | 9.0 | 7.0 | 22.2 |
| INV/SHORT|aligned=1 | 29 | 65.5 | 0.115 | 1.36 | 9 | 14.0 | 57.0 | 44.4 |
| RETEST/LONG|aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| RETEST/LONG|aligned=1 | 2265 | 44.7 | -0.029 | 0.95 | 1147 | 12.0 | 10.0 | 32.8 |
| RETEST/SHORT|aligned=1 | 772 | 43.8 | -0.033 | 0.94 | 368 | 17.0 | 16.0 | 38.9 |

## Autopsia de SL
n_losses=1552  causas: RR-bajo×624, contra-estructura×594, stop-en-el-minimo×529, killzone-Asia-largo×442, sin-nivel-detras×313, estirado×258, chop×218, SL-muy-pegado×178, sin-causa-clara×139, contra-sesgo×1
- INV/LONG (n=27): killzone-Asia-largo×15, RR-bajo×14, contra-estructura×11, stop-en-el-minimo×6, estirado×5, SL-muy-pegado×3, sin-nivel-detras×3, chop×1
- INV/SHORT (n=9): contra-estructura×6, RR-bajo×6, stop-en-el-minimo×4, chop×1, sin-causa-clara×1, SL-muy-pegado×1
- RETEST/LONG (n=1148): RR-bajo×467, contra-estructura×434, killzone-Asia-largo×427, stop-en-el-minimo×376, sin-nivel-detras×242, estirado×180, chop×164, SL-muy-pegado×126, sin-causa-clara×87, contra-sesgo×1
- RETEST/SHORT (n=368): contra-estructura×143, stop-en-el-minimo×143, RR-bajo×137, estirado×73, sin-nivel-detras×68, chop×52, sin-causa-clara×51, SL-muy-pegado×48

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
    "n": 3026,
    "naive_expR": -0.024,
    "managed_expR": 0.056,
    "delta": 0.079,
    "avgEntryBetterTk_p50": 2.5,
    "fill_t3plus_pct": 48.2,
    "fill_full_pct": 33.8,
    "m1_rate": 34.2,
    "m2_rate": 20.5,
    "m3_rate": 10.8,
    "beAfterM1_rate": 17.0
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 39,
      "naive_expR": 0.307,
      "managed_expR": 0.426,
      "delta": 0.119,
      "avgEntryBetterTk_p50": 1.0,
      "fill_t3plus_pct": 33.3,
      "fill_full_pct": 28.2,
      "m1_rate": 46.2,
      "m2_rate": 33.3,
      "m3_rate": 17.9,
      "beAfterM1_rate": 20.5
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
      "n": 1321,
      "naive_expR": -0.026,
      "managed_expR": 0.042,
      "delta": 0.068,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 49.7,
      "fill_full_pct": 36.4,
      "m1_rate": 33.4,
      "m2_rate": 19.8,
      "m3_rate": 10.9,
      "beAfterM1_rate": 15.8
    },
    "1m/RETEST/SHORT": {
      "n": 433,
      "naive_expR": 0.0,
      "managed_expR": 0.142,
      "delta": 0.142,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 50.8,
      "fill_full_pct": 30.7,
      "m1_rate": 40.0,
      "m2_rate": 24.9,
      "m3_rate": 13.4,
      "beAfterM1_rate": 19.4
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
      "n": 669,
      "naive_expR": -0.076,
      "managed_expR": 0.007,
      "delta": 0.083,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 47.4,
      "fill_full_pct": 32.0,
      "m1_rate": 32.9,
      "m2_rate": 19.6,
      "m3_rate": 9.9,
      "beAfterM1_rate": 16.9
    },
    "2m/RETEST/SHORT": {
      "n": 203,
      "naive_expR": -0.106,
      "managed_expR": 0.015,
      "delta": 0.121,
      "avgEntryBetterTk_p50": 3.2,
      "fill_t3plus_pct": 48.3,
      "fill_full_pct": 39.4,
      "m1_rate": 32.0,
      "m2_rate": 19.7,
      "m3_rate": 11.8,
      "beAfterM1_rate": 17.7
    },
    "5m/INV/LONG": {
      "n": 5,
      "naive_expR": 0.674,
      "managed_expR": 0.817,
      "delta": 0.143,
      "avgEntryBetterTk_p50": 4.4,
      "fill_t3plus_pct": 40.0,
      "fill_full_pct": 20.0,
      "m1_rate": 40.0,
      "m2_rate": 20.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 20.0
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
      "n": 224,
      "naive_expR": 0.098,
      "managed_expR": -0.02,
      "delta": -0.118,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 37.5,
      "fill_full_pct": 26.3,
      "m1_rate": 30.4,
      "m2_rate": 16.1,
      "m3_rate": 7.6,
      "beAfterM1_rate": 19.2
    },
    "5m/RETEST/SHORT": {
      "n": 86,
      "naive_expR": -0.013,
      "managed_expR": 0.227,
      "delta": 0.24,
      "avgEntryBetterTk_p50": 4.8,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 31.4,
      "m1_rate": 41.9,
      "m2_rate": 25.6,
      "m3_rate": 11.6,
      "beAfterM1_rate": 19.8
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 2359,
    "layer_expR": -0.033,
    "orig_expR": 0.148,
    "delta_orig_minus_layer": 0.181,
    "delta_ci90": [
      0.1,
      0.275
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 45.5,
    "orig_wrTP1": 32.0,
    "slTk_p50": 19.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.8,
    "orig_saved_from_SL": 7,
    "orig_caused_SL": 325
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 78,
      "layer_expR": 0.157,
      "orig_expR": 0.564,
      "delta_orig_minus_layer": 0.407,
      "delta_ci90": [
        -0.102,
        0.983
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 53.8,
      "orig_wrTP1": 29.5,
      "slTk_p50": 13.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 2.6,
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
      "n": 2200,
      "layer_expR": -0.036,
      "orig_expR": 0.135,
      "delta_orig_minus_layer": 0.171,
      "delta_ci90": [
        0.083,
        0.26
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.4,
      "orig_wrTP1": 32.3,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.8,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 296
    },
    "retestBar2": {
      "n": 81,
      "layer_expR": -0.121,
      "orig_expR": 0.121,
      "delta_orig_minus_layer": 0.242,
      "delta_ci90": [
        -0.25,
        0.95
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 39.5,
      "orig_wrTP1": 27.2,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 4.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 10
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 39,
      "layer_expR": 0.307,
      "orig_expR": 0.565,
      "delta_orig_minus_layer": 0.257,
      "delta_ci90": [
        -0.43,
        1.011
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.7,
      "orig_wrTP1": 28.2,
      "slTk_p50": 10.0,
      "slOrigTk_p50": 2.0,
      "orig_wider_pct": 2.6,
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
      "n": 1087,
      "layer_expR": -0.017,
      "orig_expR": 0.163,
      "delta_orig_minus_layer": 0.181,
      "delta_ci90": [
        0.061,
        0.314
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 43.7,
      "orig_wrTP1": 29.3,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.7,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 157
    },
    "1m/RETEST/SHORT": {
      "n": 219,
      "layer_expR": -0.079,
      "orig_expR": 0.217,
      "delta_orig_minus_layer": 0.296,
      "delta_ci90": [
        0.013,
        0.633
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 42.5,
      "orig_wrTP1": 29.7,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 2.3,
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
      "n": 577,
      "layer_expR": -0.057,
      "orig_expR": -0.039,
      "delta_orig_minus_layer": 0.018,
      "delta_ci90": [
        -0.078,
        0.124
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 46.8,
      "orig_wrTP1": 33.3,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 2.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 78
    },
    "2m/RETEST/SHORT": {
      "n": 123,
      "layer_expR": -0.201,
      "orig_expR": 0.025,
      "delta_orig_minus_layer": 0.226,
      "delta_ci90": [
        -0.046,
        0.505
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 40.7,
      "orig_wrTP1": 30.1,
      "slTk_p50": 30.0,
      "slOrigTk_p50": 14.0,
      "orig_wider_pct": 1.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 14
    },
    "5m/INV/LONG": {
      "n": 5,
      "layer_expR": 0.674,
      "orig_expR": -0.714,
      "delta_orig_minus_layer": -1.388,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 100.0,
      "orig_wrTP1": 20.0,
      "slTk_p50": 49.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 4
    },
    "5m/RETEST/LONG": {
      "n": 214,
      "layer_expR": 0.08,
      "orig_expR": 0.204,
      "delta_orig_minus_layer": 0.124,
      "delta_ci90": [
        -0.093,
        0.37
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 55.1,
      "orig_wrTP1": 44.4,
      "slTk_p50": 22.5,
      "slOrigTk_p50": 13.0,
      "orig_wider_pct": 15.4,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 25
    },
    "5m/RETEST/SHORT": {
      "n": 61,
      "layer_expR": -0.223,
      "orig_expR": 0.922,
      "delta_orig_minus_layer": 1.145,
      "delta_ci90": [
        0.013,
        3.032
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 41.0,
      "orig_wrTP1": 39.3,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 26.0,
      "orig_wider_pct": 19.7,
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
    "n": 3140,
    "wrTP1": 44.8,
    "expR": -0.023
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 2959,
  "brier": 0.2203,
  "bias": -0.178,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -0.928
    },
    {
      "feature": "stretchAtr",
      "weight": -0.183
    },
    {
      "feature": "chopIdx",
      "weight": -0.127
    },
    {
      "feature": "rvol",
      "weight": 0.108
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.078
    },
    {
      "feature": "aligned",
      "weight": -0.066
    },
    {
      "feature": "hourNY",
      "weight": 0.061
    },
    {
      "feature": "emaStack",
      "weight": -0.05
    },
    {
      "feature": "entryZoneTk",
      "weight": 0.042
    },
    {
      "feature": "biasScore",
      "weight": -0.041
    },
    {
      "feature": "structDir",
      "weight": -0.028
    },
    {
      "feature": "nearTk",
      "weight": -0.004
    },
    {
      "feature": "nearEdge",
      "weight": -0.001
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.128,
      "actual": 0.176,
      "n": 295
    },
    {
      "bin": 1,
      "pred": 0.31,
      "actual": 0.253,
      "n": 296
    },
    {
      "bin": 2,
      "pred": 0.391,
      "actual": 0.341,
      "n": 296
    },
    {
      "bin": 3,
      "pred": 0.446,
      "actual": 0.361,
      "n": 296
    },
    {
      "bin": 4,
      "pred": 0.492,
      "actual": 0.449,
      "n": 296
    },
    {
      "bin": 5,
      "pred": 0.531,
      "actual": 0.537,
      "n": 296
    },
    {
      "bin": 6,
      "pred": 0.56,
      "actual": 0.595,
      "n": 296
    },
    {
      "bin": 7,
      "pred": 0.589,
      "actual": 0.652,
      "n": 296
    },
    {
      "bin": 8,
      "pred": 0.624,
      "actual": 0.679,
      "n": 296
    },
    {
      "bin": 9,
      "pred": 0.689,
      "actual": 0.709,
      "n": 296
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
    "expR": 0.307,
    "ci90": [
      -0.088,
      0.695
    ],
    "p_mean_le_0": 0.101,
    "n": 39,
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
    "expR": -0.025,
    "ci90": [
      -0.082,
      0.034
    ],
    "p_mean_le_0": 0.773,
    "n": 1325,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": -0.004,
    "ci90": [
      -0.097,
      0.08
    ],
    "p_mean_le_0": 0.542,
    "n": 440,
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
    "expR": -0.073,
    "ci90": [
      -0.142,
      0.0
    ],
    "p_mean_le_0": 0.95,
    "n": 672,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": -0.106,
    "ci90": [
      -0.226,
      0.019
    ],
    "p_mean_le_0": 0.922,
    "n": 203,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.098,
    "ci90": [
      -0.029,
      0.237
    ],
    "p_mean_le_0": 0.102,
    "n": 224,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": -0.007,
    "ci90": [
      -0.191,
      0.21
    ],
    "p_mean_le_0": 0.53,
    "n": 87,
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
      "n": 1258,
      "wrTP1": 43.2,
      "expR": 0.005,
      "pf": 1.01,
      "defining_features": {
        "structDir": 0.89,
        "emaStack": 0.61,
        "biasScore": 0.57,
        "nearEdge": 0.33
      }
    },
    {
      "id": 1,
      "n": 696,
      "wrTP1": 44.3,
      "expR": -0.011,
      "pf": 0.98,
      "defining_features": {
        "biasScore": -1.61,
        "emaStack": -1.25,
        "nearEdge": -1.05,
        "structDir": -0.45
      }
    },
    {
      "id": 3,
      "n": 779,
      "wrTP1": 48.4,
      "expR": -0.043,
      "pf": 0.92,
      "defining_features": {
        "structDir": -1.12,
        "biasScore": 0.44,
        "stretchAtr": -0.26,
        "nearEdge": 0.25
      }
    },
    {
      "id": 2,
      "n": 407,
      "wrTP1": 43.7,
      "expR": -0.091,
      "pf": 0.82,
      "defining_features": {
        "stretchAtr": 1.62,
        "rvol": 1.32,
        "chopIdx": -1.31,
        "hourNY": -0.34
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
        "n": 12,
        "wrTP1": 50.0,
        "expR": 0.437
      },
      "YM": {
        "n": 18,
        "wrTP1": 50.0,
        "expR": 0.501
      },
      "ES": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": -0.375
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
        "n": 228,
        "wrTP1": 47.8,
        "expR": 0.024
      },
      "ES": {
        "n": 321,
        "wrTP1": 42.4,
        "expR": -0.031
      },
      "CL": {
        "n": 292,
        "wrTP1": 42.5,
        "expR": -0.201
      },
      "YM": {
        "n": 289,
        "wrTP1": 43.9,
        "expR": 0.034
      }
    },
    "expR_spread": 0.29,
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
        "n": 92,
        "wrTP1": 34.8,
        "expR": -0.152
      },
      "YM": {
        "n": 124,
        "wrTP1": 48.4,
        "expR": 0.087
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
        "n": 122,
        "wrTP1": 50.0,
        "expR": -0.021
      },
      "GC": {
        "n": 106,
        "wrTP1": 42.5,
        "expR": -0.012
      },
      "CL": {
        "n": 152,
        "wrTP1": 47.4,
        "expR": -0.075
      },
      "ES": {
        "n": 153,
        "wrTP1": 47.7,
        "expR": -0.021
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
        "n": 61,
        "wrTP1": 42.6,
        "expR": -0.121
      },
      "GC": {
        "n": 36,
        "wrTP1": 36.1,
        "expR": -0.09
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
        "n": 42,
        "wrTP1": 59.5,
        "expR": 0.159
      },
      "NQ": {
        "n": 68,
        "wrTP1": 48.5,
        "expR": -0.095
      }
    },
    "expR_spread": 0.451,
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
        "n": 13,
        "wrTP1": 23.1,
        "expR": -0.532
      },
      "YM": {
        "n": 15,
        "wrTP1": 40.0,
        "expR": -0.08
      },
      "CL": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.015
      }
    },
    "expR_spread": 0.713,
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
    "n": 268,
    "wrTP1": 47.4,
    "nSL": 127,
    "nTO": 14,
    "expR": 0.091,
    "pf": 1.19,
    "mfe_p25": 6.0,
    "mfe_p50": 14.0,
    "mfe_p75": 36.0,
    "winnerMAE_p75": 11.0,
    "winnerMAE_p90": 28.80000000000001,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -10.5,
    "revAfterSL_rate": 36.2
  },
  "away_from_news": {
    "n": 2872,
    "wrTP1": 44.6,
    "nSL": 1425,
    "nTO": 167,
    "expR": -0.034,
    "pf": 0.93,
    "mfe_p25": 6.0,
    "mfe_p50": 13.0,
    "mfe_p75": 35.0,
    "winnerMAE_p75": 11.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 3.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -11.0,
    "revAfterSL_rate": 33.9
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
    "hypothesis": "En RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. HASTA 2026-09-04 esto solo certificaba en SHORT (\"no aplica a largos\"); con la muestra de hoy (ver nota 2026-09-05) TAMBIEN certifica en 1m LONG, asi que se retira la exclusion dura de BUY RETEST y se deja como 'certifica por tf/side, no generalizar sin mirar la tabla' -- ver next_steps, se pide un dia mas para confirmar que el giro no es artefacto de la recuperacion de datos de hoy.",
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
      "asOf": "2026-09-05",
      "retest_1m_long": {
        "n": 1087,
        "deltaER_orig_minus_layer": 0.181,
        "ci90": [
          0.061,
          0.314
        ],
        "ci90_no_cruza_cero": true,
        "nota": "CAMBIO DE SIGNO vs 2026-09-04 (entonces plano/opuesto): certifica ahora, mismo orden de magnitud que SHORT. Pendiente de confirmar 2026-09-06 que no sea artefacto de la restauracion de datos de hoy (ver nota general de la corrida)."
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
      "2026-09-05: se recupero signals/2026-09-03.jsonl (ver nota de la corrida en state.json/narrative y en el historico de los playbooks) -- estaba truncado de 1280 a 24 lineas por un commit 'heal' que en realidad BORRO datos en vez de repararlos. Todas las cifras de esta entrada ya usan el dato restaurado. Confirmar el 2026-09-06 que retest_1m_long se mantiene positivo con datos nuevos genuinos (no solo re-anadidos) antes de tratarlo como hallazgo estable.",
      "Revision semanal del domingo: confirmar sobre walk-forward + segment_significance (FDR 10%), no solo in-sample (walk_forward todavia no esta listo, solo 1 semana de datos).",
      "Anadir linea a predictions.jsonl con predictedDeltaER antes de aplicar.",
      "Si pasa 2+ dias mas: cambio en Pine = para RETEST (long y short, no solo short) usar lg_slOrig (mecha de la vela del retest) como SL de trabajo en 1m; en 5m solo SHORT; en 2m no aplicar todavia (ningun lado certifica). Poner changeDate el dia que se aplique en los 12 graficos.",
      "Vigilar: retestBar2 (1m SHORT = mecha vela retest + vela previa) sigue siendo una fraccion chica de la muestra 1m short (n=81 de by_basis) -- puede mover el numero cuando crezca."
    ],
    "beforeN": 3048,
    "afterN": 0,
    "before": {
      "n": 3048,
      "wrTP1": 44.5,
      "nSL": 1516,
      "nTO": 175,
      "expR": -0.028,
      "pf": 0.94,
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
    "session": "ny",
    "runType": "pre-ny",
    "generatedAt": "2026-09-04T08:28:20-05:00",
    "schema": "sa-plan-2",
    "cleanest": "NQ",
    "focus": {
      "sym": "NQ",
      "verdict": "GO",
      "window": "08:15-10:30 CT",
      "setup": {
        "es": "reclamo confirmado del cluster VAL/apertura/low overnight, ahora pegado al PDH 29584.25 (2 ticks) con el motor de sesgo en BUSCANDO LARGO",
        "en": "confirmed reclaim of the VAL/day-open/overnight-low cluster, now pinned to PDH 29584.25 (2 ticks away) with the bias engine LOOKING FOR LONGS"
      },
      "trigger": {
        "es": "cierre 5m ya confirmado sobre 29530 con estiramiento en 0.17 ATR -- gatillo activo, busca reclamo/ruptura de PDH 29584.25 hacia VAH 29657.75",
        "en": "5m close already confirmed above 29530 with stretch at 0.17 ATR -- trigger is live, watch for a PDH 29584.25 reclaim/break toward VAH 29657.75"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 29482 (low overnight) mata la entrada de esta sesion",
        "en": "5m close sustained below 29482 (overnight low) kills this session's entry"
      },
      "note": {
        "es": "la confirmacion ya llego -- entra con el reclamo/ruptura de PDH, no compres a mercado sin que rompa; sigue siendo el unico GO del complejo, los otros 4 continuan estirados sin permiso",
        "en": "confirmation already landed -- enter on the PDH reclaim/break, don't buy at market without the break; it's still the complex's only GO, the other 4 remain stretched with no permission"
      }
    },
    "summary": {
      "es": [
        "!! NFP salio 07:30 CT y desato venta violenta en el complejo -- NQ ya confirmo reclamo y paso a GO, ES/GC/YM/CL siguen estirados 1.6-3 ATR sin permiso",
        "NQ: confirmo reclamo sobre 29530, estiramiento cayo a 0.17 ATR, pegado a PDH 29584.25 -- GO, objetivo VAH 29657-29700",
        "ES: barrio su low overnight 7731.25 en cluster VAL/FVG1h A+, sin permiso de sesion -- AVOID",
        "GC: paso de largo por la zona de descuento sin rechazo, dia ya al 116% del ATR (agotado) -- AVOID",
        "YM: retest de Londres cumplio hasta el dayHi pero el NFP lo devolvio todo -- AVOID",
        "CL: en tierra de nadie a menos de 1pt de su invalidacion semanal (89.04), sin sesgo -- AVOID",
        "mas limpio: NQ (unico GO del complejo, reclamo confirmado sobre PDH, el resto sigue estirado)",
        "limite diario $1000/3 stops: NQ y ES dan maxContracts=0 en full con estos stops, GC ni con micros compensa (stop ~$3500), solo YM cabria 1 full ($225 de stop) si llega a confirmar",
        "datos OK (5-10 min), noticias ALTA (post-NFP), calendario semana-NFP"
      ],
      "en": [
        "!! NFP printed at 07:30 CT and triggered a violent selloff across the complex -- NQ already confirmed the reclaim and flipped to GO, ES/GC/YM/CL remain stretched 1.6-3 ATR with no permission",
        "NQ: confirmed the reclaim ab
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
