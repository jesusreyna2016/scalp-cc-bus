# Scalp CC · report 2026-09-03T01:19Z
- signals=1035 outcomes=958 pares_resueltos=943 pendientes=92 huerfanos=22

## ⚠ ALERTAS (llevar al frente del resumen)
- ORFANOS: subieron a 22 (+5 vs los 17 de la corrida anterior committeada). Revisar pipeline Pine/ingest si sigue subiendo sin recompilar.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.239 vs 0.008, delta 0.231 CI90 [0.021, 0.499], n 517). Candidato para experiments.json + revision semanal. Matiz: el n=517 agregado mezcla 1m/2m/5m (el Pine aun no emite `retestBar2` para 1m SHORT); el efecto real y significativo esta en SHORT (1m n=138 delta +0.328 CI90[0.009,0.722]; 5m n=42 delta +1.701 CI90[0.076,4.452]) — en LONG el signo es plano/contrario y no significativo, no generalizar a LONG.

- E[R] global: {"expR": 0.032, "ci90": [-0.029, 0.097], "p_mean_le_0": 0.181, "n": 936}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 2 | 50.0 | -0.21 | 0.58 | 1 | 16.0 | 2.0 | 100.0 |
| 1m/INV/SHORT | 17 | 70.6 | 0.222 | 1.75 | 5 | 11.0 | 31.75 | 40.0 |
| 1m/RETEST/LONG | 217 | 47.5 | 0.034 | 1.07 | 106 | 14.0 | 9.5 | 32.1 |
| 1m/RETEST/SHORT | 356 | 47.8 | 0.026 | 1.05 | 171 | 13.5 | 8.0 | 39.8 |
| 2m/INV/LONG | 1 | 100.0 | 0.74 | 99.0 | 0 | 58.0 | 17.0 | None |
| 2m/INV/SHORT | 6 | 50.0 | -0.267 | 0.47 | 3 | 8.5 | 14.0 | 33.3 |
| 2m/RETEST/LONG | 78 | 52.6 | 0.098 | 1.21 | 36 | 17.0 | 17.0 | 36.1 |
| 2m/RETEST/SHORT | 165 | 43.6 | -0.087 | 0.84 | 85 | 15.5 | 13.25 | 45.9 |
| 5m/INV/SHORT | 3 | 66.7 | -0.04 | 0.88 | 1 | 79.0 | 95.75 | 100.0 |
| 5m/RETEST/LONG | 30 | 66.7 | 0.401 | 2.2 | 10 | 34.5 | 28.5 | 50.0 |
| 5m/RETEST/SHORT | 68 | 55.9 | 0.088 | 1.2 | 30 | 29.0 | 33.5 | 36.7 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 67 | 22.4 | -0.104 | 0.85 | 47 | 16.0 | 8.5 | 17.0 |
| B | 403 | 52.9 | 0.102 | 1.22 | 184 | 19.0 | 15.0 | 39.7 |
| C | 473 | 49.7 | -0.008 | 0.98 | 217 | 13.0 | 14.0 | 43.3 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 388 | 49.5 | 0.004 | 1.01 | 181 | 11.0 | 9.0 | 52.5 |
| London | 123 | 51.2 | -0.001 | 1.0 | 60 | 16.0 | 20.5 | 41.7 |
| NY | 108 | 48.1 | 0.113 | 1.22 | 55 | 38.5 | 31.25 | 23.6 |
| Sin KZ | 324 | 48.1 | 0.052 | 1.11 | 152 | 20.0 | 13.25 | 27.6 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 326 | 47.9 | -0.022 | 0.96 | 156 | 18.0 | 17.25 | 35.3 |
| edge=0 | 399 | 48.9 | 0.01 | 1.02 | 190 | 12.0 | 11.0 | 45.8 |
| edge=1 | 218 | 51.4 | 0.153 | 1.32 | 102 | 20.0 | 16.0 | 32.4 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| aligned=1 | 932 | 49.0 | 0.029 | 1.06 | 447 | 15.0 | 14.0 | 39.1 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=0 | 1 | 0.0 | -1.0 | 0.0 | 1 | 10.0 | None | 100.0 |
| INV/LONG|edge=1 | 2 | 100.0 | 0.66 | 99.0 | 0 | 40.0 | 13.25 | None |
| INV/SHORT|edge=-1 | 10 | 70.0 | 0.197 | 1.66 | 3 | 16.5 | 42.5 | 0.0 |
| INV/SHORT|edge=0 | 14 | 64.3 | 0.047 | 1.13 | 5 | 12.0 | 74.0 | 80.0 |
| INV/SHORT|edge=1 | 2 | 50.0 | -0.29 | 0.42 | 1 | 7.0 | 5.0 | 0.0 |
| RETEST/LONG|edge=-1 | 49 | 55.1 | 0.016 | 1.04 | 18 | 13.0 | 15.5 | 72.2 |
| RETEST/LONG|edge=0 | 124 | 51.6 | 0.004 | 1.01 | 58 | 10.5 | 9.0 | 32.8 |
| RETEST/LONG|edge=1 | 152 | 48.0 | 0.169 | 1.33 | 76 | 30.0 | 18.0 | 26.3 |
| RETEST/SHORT|edge=-1 | 267 | 45.7 | -0.036 | 0.93 | 135 | 21.0 | 16.75 | 31.1 |
| RETEST/SHORT|edge=0 | 260 | 46.9 | 0.015 | 1.03 | 126 | 13.0 | 10.0 | 50.0 |
| RETEST/SHORT|edge=1 | 62 | 58.1 | 0.11 | 1.27 | 25 | 13.0 | 9.0 | 52.0 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 1 | 100.0 | 0.58 | 99.0 | 0 | 22.0 | 2.0 | None |
| INV/LONG|tier=C | 2 | 50.0 | -0.13 | 0.74 | 1 | 34.0 | 17.0 | 100.0 |
| INV/SHORT|tier=B | 7 | 71.4 | 0.201 | 1.71 | 2 | 9.0 | 12.0 | 0.0 |
| INV/SHORT|tier=C | 19 | 63.2 | 0.034 | 1.09 | 7 | 13.0 | 74.25 | 57.1 |
| RETEST/LONG|tier=A+ | 13 | 7.7 | -0.705 | 0.24 | 12 | 5.0 | 9.0 | 0.0 |
| RETEST/LONG|tier=B | 153 | 51.6 | 0.225 | 1.47 | 73 | 27.0 | 16.5 | 41.1 |
| RETEST/LONG|tier=C | 159 | 52.8 | 0.011 | 1.02 | 67 | 14.0 | 14.0 | 32.8 |
| RETEST/SHORT|tier=A+ | 54 | 25.9 | 0.04 | 1.06 | 35 | 28.5 | 8.0 | 22.9 |
| RETEST/SHORT|tier=B | 242 | 52.9 | 0.019 | 1.04 | 109 | 17.0 | 13.25 | 39.4 |
| RETEST/SHORT|tier=C | 293 | 47.1 | -0.02 | 0.96 | 142 | 13.0 | 11.75 | 47.2 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 3 | 66.7 | 0.107 | 1.32 | 1 | 22.0 | 13.25 | 100.0 |
| INV/SHORT|aligned=1 | 26 | 65.4 | 0.079 | 1.23 | 9 | 12.0 | 64.0 | 44.4 |
| RETEST/LONG|aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| RETEST/LONG|aligned=1 | 314 | 50.3 | 0.076 | 1.16 | 151 | 15.0 | 14.0 | 34.4 |
| RETEST/SHORT|aligned=1 | 589 | 47.5 | 0.002 | 1.0 | 286 | 15.0 | 13.0 | 41.3 |

## Autopsia de SL
n_losses=448  causas: contra-estructura×188, RR-bajo×185, stop-en-el-minimo×175, sin-nivel-detras×82, estirado×79, chop×68, sin-causa-clara×61, SL-muy-pegado×47, killzone-Asia-largo×29, contra-sesgo×1
- INV/LONG (n=1): chop×1, RR-bajo×1, stop-en-el-minimo×1
- INV/SHORT (n=9): contra-estructura×6, RR-bajo×6, stop-en-el-minimo×4, chop×1, sin-causa-clara×1, SL-muy-pegado×1
- RETEST/LONG (n=152): RR-bajo×71, contra-estructura×56, stop-en-el-minimo×52, killzone-Asia-largo×29, chop×28, sin-nivel-detras×27, estirado×19, sin-causa-clara×19, SL-muy-pegado×9, contra-sesgo×1
- RETEST/SHORT (n=286): contra-estructura×126, stop-en-el-minimo×118, RR-bajo×107, estirado×60, sin-nivel-detras×55, sin-causa-clara×41, chop×38, SL-muy-pegado×37

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
    "n": 921,
    "naive_expR": 0.031,
    "managed_expR": 0.126,
    "delta": 0.095,
    "avgEntryBetterTk_p50": 3.3,
    "fill_t3plus_pct": 50.7,
    "fill_full_pct": 35.1,
    "m1_rate": 36.3,
    "m2_rate": 22.8,
    "m3_rate": 12.6,
    "beAfterM1_rate": 17.6
  },
  "by_tf_kind_side": {
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
      "n": 210,
      "naive_expR": 0.029,
      "managed_expR": 0.037,
      "delta": 0.008,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 53.3,
      "fill_full_pct": 41.4,
      "m1_rate": 31.9,
      "m2_rate": 19.0,
      "m3_rate": 11.4,
      "beAfterM1_rate": 16.2
    },
    "1m/RETEST/SHORT": {
      "n": 349,
      "naive_expR": 0.031,
      "managed_expR": 0.191,
      "delta": 0.16,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 47.3,
      "fill_full_pct": 26.4,
      "m1_rate": 41.0,
      "m2_rate": 26.4,
      "m3_rate": 13.8,
      "beAfterM1_rate": 19.8
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
      "n": 74,
      "naive_expR": 0.077,
      "managed_expR": 0.038,
      "delta": -0.039,
      "avgEntryBetterTk_p50": 4.2,
      "fill_t3plus_pct": 60.8,
      "fill_full_pct": 45.9,
      "m1_rate": 39.2,
      "m2_rate": 21.6,
      "m3_rate": 13.5,
      "beAfterM1_rate": 17.6
    },
    "2m/RETEST/SHORT": {
      "n": 162,
      "naive_expR": -0.087,
      "managed_expR": 0.024,
      "delta": 0.111,
      "avgEntryBetterTk_p50": 3.05,
      "fill_t3plus_pct": 48.8,
      "fill_full_pct": 39.5,
      "m1_rate": 30.9,
      "m2_rate": 19.8,
      "m3_rate": 13.0,
      "beAfterM1_rate": 16.7
    },
    "5m/INV/SHORT": {
      "n": 3,
      "naive_expR": -0.04,
      "managed_expR": 0.511,
      "delta": 0.551,
      "avgEntryBetterTk_p50": 35.1,
      "fill_t3plus_pct": 100.0,
      "fill_full_pct": 33.3,
      "m1_rate": 0.0,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 30,
      "naive_expR": 0.401,
      "managed_expR": 0.291,
      "delta": -0.11,
      "avgEntryBetterTk_p50": 7.3,
      "fill_t3plus_pct": 56.7,
      "fill_full_pct": 46.7,
      "m1_rate": 33.3,
      "m2_rate": 30.0,
      "m3_rate": 16.7,
      "beAfterM1_rate": 13.3
    },
    "5m/RETEST/SHORT": {
      "n": 67,
      "naive_expR": 0.081,
      "managed_expR": 0.23,
      "delta": 0.148,
      "avgEntryBetterTk_p50": 4.9,
      "fill_t3plus_pct": 52.2,
      "fill_full_pct": 31.3,
      "m1_rate": 41.8,
      "m2_rate": 25.4,
      "m3_rate": 10.4,
      "beAfterM1_rate": 17.9
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 534,
    "layer_expR": 0.01,
    "orig_expR": 0.233,
    "delta_orig_minus_layer": 0.223,
    "delta_ci90": [
      0.018,
      0.466
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 47.6,
    "orig_wrTP1": 31.8,
    "slTk_p50": 21.0,
    "slOrigTk_p50": 10.0,
    "orig_wider_pct": 3.2,
    "orig_saved_from_SL": 2,
    "orig_caused_SL": 86
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 17,
      "layer_expR": 0.053,
      "orig_expR": 0.044,
      "delta_orig_minus_layer": -0.009,
      "delta_ci90": [
        -0.708,
        0.908
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 64.7,
      "orig_wrTP1": 29.4,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 6
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
      "n": 517,
      "layer_expR": 0.008,
      "orig_expR": 0.239,
      "delta_orig_minus_layer": 0.231,
      "delta_ci90": [
        0.021,
        0.499
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.0,
      "orig_wrTP1": 31.9,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.3,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 80
    }
  },
  "by_tf_kind_side": {
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
      "n": 171,
      "layer_expR": 0.075,
      "orig_expR": -0.052,
      "delta_orig_minus_layer": -0.128,
      "delta_ci90": [
        -0.344,
        0.092
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.0,
      "orig_wrTP1": 28.7,
      "slTk_p50": 17.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 1.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 33
    },
    "1m/RETEST/SHORT": {
      "n": 138,
      "layer_expR": -0.054,
      "orig_expR": 0.274,
      "delta_orig_minus_layer": 0.328,
      "delta_ci90": [
        0.009,
        0.722
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.2,
      "orig_wrTP1": 31.2,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 0.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 18
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
      "n": 53,
      "layer_expR": 0.23,
      "orig_expR": 0.401,
      "delta_orig_minus_layer": 0.171,
      "delta_ci90": [
        -0.359,
        0.714
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 56.6,
      "orig_wrTP1": 32.1,
      "slTk_p50": 26.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 1.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 13
    },
    "2m/RETEST/SHORT": {
      "n": 83,
      "layer_expR": -0.22,
      "orig_expR": 0.069,
      "delta_orig_minus_layer": 0.289,
      "delta_ci90": [
        -0.021,
        0.632
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 39.8,
      "orig_wrTP1": 30.1,
      "slTk_p50": 27.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 8
    },
    "5m/RETEST/LONG": {
      "n": 30,
      "layer_expR": 0.401,
      "orig_expR": 0.118,
      "delta_orig_minus_layer": -0.283,
      "delta_ci90": [
        -0.634,
        0.027
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 66.7,
      "orig_wrTP1": 46.7,
      "slTk_p50": 29.5,
      "slOrigTk_p50": 23.0,
      "orig_wider_pct": 13.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 6
    },
    "5m/RETEST/SHORT": {
      "n": 42,
      "layer_expR": -0.167,
      "orig_expR": 1.534,
      "delta_orig_minus_layer": 1.701,
      "delta_ci90": [
        0.076,
        4.452
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 40.5,
      "orig_wrTP1": 40.5,
      "slTk_p50": 27.5,
      "slOrigTk_p50": 22.0,
      "orig_wider_pct": 19.0,
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
    "n": 943,
    "wrTP1": 49.1,
    "expR": 0.032
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 911,
  "brier": 0.223,
  "bias": 0.005,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -0.748
    },
    {
      "feature": "stretchAtr",
      "weight": -0.224
    },
    {
      "feature": "hourNY",
      "weight": 0.213
    },
    {
      "feature": "rvol",
      "weight": 0.169
    },
    {
      "feature": "atrPctUsed",
      "weight": 0.13
    },
    {
      "feature": "aligned",
      "weight": -0.109
    },
    {
      "feature": "biasScore",
      "weight": -0.103
    },
    {
      "feature": "chopIdx",
      "weight": -0.099
    },
    {
      "feature": "emaStack",
      "weight": -0.083
    },
    {
      "feature": "nearEdge",
      "weight": 0.073
    },
    {
      "feature": "structDir",
      "weight": -0.015
    },
    {
      "feature": "entryZoneTk",
      "weight": 0.012
    },
    {
      "feature": "nearTk",
      "weight": -0.0
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.18,
      "actual": 0.22,
      "n": 91
    },
    {
      "bin": 1,
      "pred": 0.346,
      "actual": 0.275,
      "n": 91
    },
    {
      "bin": 2,
      "pred": 0.424,
      "actual": 0.407,
      "n": 91
    },
    {
      "bin": 3,
      "pred": 0.475,
      "actual": 0.396,
      "n": 91
    },
    {
      "bin": 4,
      "pred": 0.515,
      "actual": 0.505,
      "n": 91
    },
    {
      "bin": 5,
      "pred": 0.545,
      "actual": 0.582,
      "n": 91
    },
    {
      "bin": 6,
      "pred": 0.583,
      "actual": 0.626,
      "n": 91
    },
    {
      "bin": 7,
      "pred": 0.617,
      "actual": 0.681,
      "n": 91
    },
    {
      "bin": 8,
      "pred": 0.66,
      "actual": 0.703,
      "n": 91
    },
    {
      "bin": 9,
      "pred": 0.736,
      "actual": 0.685,
      "n": 92
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
    "expR": 0.034,
    "ci90": [
      -0.106,
      0.183
    ],
    "p_mean_le_0": 0.359,
    "n": 214,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.026,
    "ci90": [
      -0.074,
      0.127
    ],
    "p_mean_le_0": 0.36,
    "n": 356,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.098,
    "ci90": [
      -0.128,
      0.352
    ],
    "p_mean_le_0": 0.251,
    "n": 77,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": -0.087,
    "ci90": [
      -0.225,
      0.052
    ],
    "p_mean_le_0": 0.856,
    "n": 162,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.401,
    "ci90": [
      0.025,
      0.784
    ],
    "p_mean_le_0": 0.04,
    "n": 30,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": 0.088,
    "ci90": [
      -0.139,
      0.332
    ],
    "p_mean_le_0": 0.261,
    "n": 68,
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
      "n": 249,
      "wrTP1": 52.2,
      "expR": 0.171,
      "pf": 1.37,
      "defining_features": {
        "biasScore": 1.31,
        "atrPctUsed": 1.26,
        "emaStack": 1.01,
        "nearEdge": 0.71
      }
    },
    {
      "id": 1,
      "n": 265,
      "wrTP1": 47.2,
      "expR": 0.052,
      "pf": 1.11,
      "defining_features": {
        "nearEdge": -0.96,
        "nearTk": 0.83,
        "biasScore": -0.78,
        "emaStack": -0.73
      }
    },
    {
      "id": 0,
      "n": 293,
      "wrTP1": 52.2,
      "expR": 0.032,
      "pf": 1.07,
      "defining_features": {
        "atrPctUsed": -0.78,
        "hourNY": 0.72,
        "nearTk": -0.46,
        "stretchAtr": -0.41
      }
    },
    {
      "id": 3,
      "n": 136,
      "wrTP1": 40.4,
      "expR": -0.26,
      "pf": 0.56,
      "defining_features": {
        "stretchAtr": 1.58,
        "rvol": 1.25,
        "chopIdx": -1.14,
        "structDir": 0.53
      }
    }
  ]
}
```

## Consistencia entre instrumentos
```json
{
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 12,
        "wrTP1": 66.7,
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
        "n": 35,
        "wrTP1": 45.7,
        "expR": 0.188
      },
      "NQ": {
        "n": 20,
        "wrTP1": 55.0,
        "expR": -0.067
      },
      "ES": {
        "n": 41,
        "wrTP1": 41.5,
        "expR": -0.086
      },
      "CL": {
        "n": 88,
        "wrTP1": 46.6,
        "expR": -0.172
      },
      "YM": {
        "n": 33,
        "wrTP1": 54.5,
        "expR": 0.622
      }
    },
    "expR_spread": 0.794,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 78,
        "wrTP1": 50.0,
        "expR": 0.175
      },
      "GC": {
        "n": 77,
        "wrTP1": 37.7,
        "expR": -0.16
      },
      "YM": {
        "n": 102,
        "wrTP1": 52.0,
        "expR": 0.064
      },
      "ES": {
        "n": 99,
        "wrTP1": 49.5,
        "expR": 0.013
      }
    },
    "expR_spread": 0.335,
    "verdict": "universal"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 12,
        "wrTP1": 58.3,
        "expR": -0.008
      },
      "GC": {
        "n": 11,
        "wrTP1": 63.6,
        "expR": 0.344
      },
      "CL": {
        "n": 29,
        "wrTP1": 37.9,
        "expR": -0.323
      },
      "ES": {
        "n": 16,
        "wrTP1": 50.0,
        "expR": 0.201
      },
      "YM": {
        "n": 10,
        "wrTP1": 80.0,
        "expR": 1.037
      }
    },
    "expR_spread": 1.36,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 40,
        "wrTP1": 40.0,
        "expR": -0.18
      },
      "YM": {
        "n": 52,
        "wrTP1": 44.2,
        "expR": -0.133
      },
      "GC": {
        "n": 31,
        "wrTP1": 41.9,
        "expR": -0.021
      },
      "NQ": {
        "n": 42,
        "wrTP1": 47.6,
        "expR": 0.014
      }
    },
    "expR_spread": 0.194,
    "verdict": "universal"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 5,
        "wrTP1": 80.0,
        "expR": 0.55
      },
      "ES": {
        "n": 9,
        "wrTP1": 55.6,
        "expR": 0.621
      },
      "YM": {
        "n": 8,
        "wrTP1": 50.0,
        "expR": 0.254
      },
      "CL": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.325
      },
      "NQ": {
        "n": 4,
        "wrTP1": 75.0,
        "expR": 0.093
      }
    },
    "expR_spread": 0.528,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 25,
        "wrTP1": 68.0,
        "expR": 0.354
      },
      "ES": {
        "n": 20,
        "wrTP1": 60.0,
        "expR": 0.175
      },
      "GC": {
        "n": 11,
        "wrTP1": 27.3,
        "expR": -0.489
      },
      "YM": {
        "n": 12,
        "wrTP1": 50.0,
        "expR": -0.08
      }
    },
    "expR_spread": 0.843,
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
    "n": 165,
    "wrTP1": 51.5,
    "nSL": 75,
    "nTO": 5,
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
    "n": 778,
    "wrTP1": 48.6,
    "nSL": 373,
    "nTO": 27,
    "expR": -0.002,
    "pf": 1.0,
    "mfe_p25": 8.0,
    "mfe_p50": 16.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 14.0,
    "winnerMAE_p90": 29.0,
    "loserMFEbeforeSL_p50": 3.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -12.0,
    "revAfterSL_rate": 40.2
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
  }
]
```

## Session Analyst
```json
{
  "available": true,
  "latest_plan": {
    "date": "2026-09-03",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-09-02T16:25:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "YM",
    "focus": {
      "sym": "YM",
      "verdict": "WAIT",
      "window": "20:00-23:00 CT",
      "setup": {
        "es": "pullback a VAH/EMA20/50 53112-53202 para comprar de nuevo",
        "en": "pullback into VAH/EMA20/50 53112-53202 to buy again"
      },
      "trigger": {
        "es": "cierre 5m dentro de 53112-53202 con mecha inferior o reclaim confirmado",
        "en": "5m close inside 53112-53202 with a lower wick or a confirmed reclaim"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 53044 mata el largo de la sesion",
        "en": "5m close sustained below 53044 kills the session's long"
      },
      "note": {
        "es": "YM lleva 2 de 2 liderando el alza del complejo -- compra el pullback, no el toque; no lo persigas estirado",
        "en": "YM is 2 for 2 leading the complex higher -- buy the pullback, not the touch; don't chase it stretched"
      }
    },
    "summary": {
      "es": [
        "Dia completo mixto: GC rompio 3 dias de tesis bajista con un dia fuerte al alza (+1.3%), YM confirmo su 2a sesion liderando el alza, NQ y CL cerraron practicamente PLANOS pese a rangos violentos, ES cerro alcista neto contra su propio sesgo corto.",
        "NQ: patron de 'giro de 1 dia' (2 seguidos) se rompio hoy -- balance/chop pegado a resistencia POC/VAH, sin resolver.",
        "ES: peor dia de precision del complejo, marco crudo se desalineo otra vez del sesgo fusionado.",
        "GC: 4o test del cluster 4383-4424 perdio memoria tras 3 rechazos seguidos -- tesis bajista ROTA, nueva tesis alcista desde cero.",
        "YM: 2/2 sesiones liderando la divergencia alcista frente a NQ/ES -- primer patron propio medible.",
        "CL: el inventario EIA si movio el precio (nuevo maximo semanal) pero no pudo sostenerse, cerro plano.",
        "Aun no reabre Globex (17:00 CT) al momento de esta corrida -- niveles de gap/DO/TDO/ONH/ONL de la nueva sesion se confirman con el reopen; se usa el cierre de hoy como referencia.",
        "Semana de NFP (viernes 4-sep) -- Asia de hoy sin eventos de alto impacto, pero NY de manana trae Claims/ISM Services/reporte de gas natural (medios), manos fuera moderadas.",
        "Sizing: limite $1,000 por cuenta (K=3 stops) -- casi todas las zonas de hoy piden micros, no full, para no quemar el limite en 1-2 stops.",
        "Limpio: YM."
      ],
      "en": [
        "Mixed full day: GC broke a 3-day bearish thesis with a strong up day (+1.3%), YM confirmed its 2nd session leading the rally, NQ and CL closed nearly FLAT despite violent ranges, ES closed net bullish against its own short bias.",
        "NQ: the '1-day reversal' pattern (2 in a row) broke today -- balance/chop stuck against POC/VAH resistance, unresolved.",
        "ES: the complex's worst accuracy day, 
```
