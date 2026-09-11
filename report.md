# Scalp CC · report 2026-09-11T01:26Z
- signals=7077 outcomes=6927 pares_resueltos=7039 pendientes=38 huerfanos=25

## ⚠ ALERTAS (llevar al frente del resumen)
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.167 vs 0.014, delta 0.153 CI90 [0.094, 0.214], n 4504). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.084 CI90 [0.031, 0.137], n 1415). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.015, "ci90": [-0.009, 0.041], "p_mean_le_0": 0.152, "n": 6902}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 64 | 43.8 | 0.097 | 1.2 | 29 | 12.0 | 7.5 | 17.2 |
| 1m/INV/SHORT | 62 | 50.0 | 0.111 | 1.25 | 27 | 14.5 | 10.5 | 18.5 |
| 1m/RETEST/LONG | 2551 | 44.4 | 0.005 | 1.01 | 1269 | 13.0 | 9.0 | 28.5 |
| 1m/RETEST/SHORT | 1684 | 43.4 | 0.017 | 1.03 | 840 | 14.0 | 9.0 | 29.4 |
| 2m/INV/LONG | 26 | 42.3 | -0.247 | 0.56 | 14 | 8.0 | 12.5 | 28.6 |
| 2m/INV/SHORT | 27 | 33.3 | 0.019 | 1.04 | 14 | 10.0 | 5.0 | 42.9 |
| 2m/RETEST/LONG | 1198 | 46.7 | -0.032 | 0.94 | 595 | 15.0 | 12.0 | 37.5 |
| 2m/RETEST/SHORT | 789 | 48.2 | 0.074 | 1.15 | 377 | 19.0 | 10.0 | 39.5 |
| 5m/INV/LONG | 10 | 90.0 | 0.849 | 99.0 | 0 | 30.0 | 32.0 | None |
| 5m/INV/SHORT | 5 | 60.0 | -0.186 | 0.54 | 2 | 34.0 | 88.5 | 100.0 |
| 5m/RETEST/LONG | 379 | 53.6 | 0.09 | 1.2 | 164 | 21.0 | 19.0 | 50.6 |
| 5m/RETEST/SHORT | 244 | 47.5 | -0.005 | 0.99 | 117 | 28.0 | 19.25 | 38.5 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 473 | 25.2 | 0.041 | 1.06 | 306 | 25.5 | 15.5 | 19.3 |
| B | 2966 | 46.0 | 0.024 | 1.05 | 1448 | 15.0 | 10.0 | 30.9 |
| C | 3600 | 48.1 | 0.004 | 1.01 | 1694 | 14.0 | 11.0 | 36.9 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 2843 | 48.6 | 0.055 | 1.12 | 1305 | 11.0 | 8.0 | 37.9 |
| London | 1155 | 45.3 | -0.067 | 0.87 | 610 | 16.0 | 11.0 | 32.3 |
| NY | 1164 | 44.9 | 0.084 | 1.17 | 571 | 23.0 | 17.0 | 36.4 |
| Sin KZ | 1877 | 41.8 | -0.037 | 0.93 | 962 | 17.0 | 12.0 | 24.0 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 1762 | 43.8 | -0.01 | 0.98 | 887 | 16.5 | 11.0 | 29.8 |
| edge=0 | 3105 | 48.2 | 0.015 | 1.03 | 1481 | 13.0 | 10.0 | 39.1 |
| edge=1 | 2172 | 43.4 | 0.036 | 1.07 | 1080 | 17.0 | 13.0 | 26.7 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 7029 | 45.6 | 0.015 | 1.03 | 3447 | 15.0 | 11.0 | 32.8 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 41 | 48.8 | 0.005 | 1.01 | 19 | 9.0 | 8.25 | 26.3 |
| INV/LONG|edge=1 | 55 | 47.3 | 0.114 | 1.27 | 22 | 22.0 | 18.5 | 13.6 |
| INV/SHORT|edge=-1 | 57 | 40.4 | 0.08 | 1.16 | 28 | 20.0 | 10.5 | 25.0 |
| INV/SHORT|edge=0 | 35 | 54.3 | 0.068 | 1.16 | 14 | 11.0 | 11.0 | 42.9 |
| INV/SHORT|edge=1 | 2 | 50.0 | -0.29 | 0.42 | 1 | 7.0 | 5.0 | 0.0 |
| RETEST/LONG|edge=-1 | 212 | 47.6 | 0.043 | 1.09 | 97 | 11.0 | 7.0 | 49.5 |
| RETEST/LONG|edge=0 | 1886 | 49.0 | -0.038 | 0.92 | 910 | 12.0 | 10.0 | 39.2 |
| RETEST/LONG|edge=1 | 2030 | 42.8 | 0.034 | 1.07 | 1021 | 17.0 | 13.0 | 25.8 |
| RETEST/SHORT|edge=-1 | 1489 | 43.3 | -0.023 | 0.96 | 760 | 17.0 | 12.0 | 27.4 |
| RETEST/SHORT|edge=0 | 1143 | 46.8 | 0.103 | 1.21 | 538 | 15.0 | 9.0 | 39.2 |
| RETEST/SHORT|edge=1 | 85 | 55.3 | 0.028 | 1.07 | 36 | 13.0 | 6.5 | 61.1 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 30 | 46.7 | 0.14 | 1.34 | 11 | 19.5 | 14.5 | 9.1 |
| INV/LONG|tier=C | 70 | 48.6 | 0.059 | 1.13 | 32 | 12.0 | 13.5 | 25.0 |
| INV/SHORT|tier=B | 30 | 50.0 | 0.163 | 1.38 | 13 | 15.5 | 4.5 | 7.7 |
| INV/SHORT|tier=C | 64 | 43.8 | 0.021 | 1.04 | 30 | 13.0 | 14.0 | 40.0 |
| RETEST/LONG|tier=A+ | 301 | 23.9 | 0.002 | 1.0 | 195 | 21.0 | 18.25 | 16.9 |
| RETEST/LONG|tier=B | 1693 | 46.1 | 0.058 | 1.12 | 820 | 15.0 | 10.0 | 31.2 |
| RETEST/LONG|tier=C | 2134 | 48.8 | -0.043 | 0.91 | 1013 | 14.0 | 11.0 | 37.4 |
| RETEST/SHORT|tier=A+ | 172 | 27.3 | 0.107 | 1.16 | 111 | 31.0 | 10.5 | 23.4 |
| RETEST/SHORT|tier=B | 1213 | 45.6 | -0.031 | 0.94 | 604 | 15.0 | 10.0 | 31.3 |
| RETEST/SHORT|tier=C | 1332 | 47.1 | 0.079 | 1.16 | 619 | 16.0 | 11.0 | 36.5 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 100 | 48.0 | 0.082 | 1.18 | 43 | 13.0 | 14.25 | 20.9 |
| INV/SHORT|aligned=1 | 94 | 45.7 | 0.068 | 1.14 | 43 | 14.5 | 11.0 | 30.2 |
| RETEST/LONG|aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 4118 | 45.9 | 0.001 | 1.0 | 2027 | 14.0 | 11.0 | 33.0 |
| RETEST/SHORT|aligned=1 | 2717 | 45.2 | 0.031 | 1.06 | 1334 | 16.0 | 10.0 | 33.1 |

## Autopsia de SL
n_losses=3448  causas: RR-bajo×1291, contra-estructura×1242, stop-en-el-minimo×1131, killzone-Asia-largo×817, sin-nivel-detras×677, estirado×623, chop×466, SL-muy-pegado×415, sin-causa-clara×341, contra-sesgo×1
- INV/LONG (n=43): killzone-Asia-largo×21, RR-bajo×20, contra-estructura×13, estirado×10, stop-en-el-minimo×9, sin-nivel-detras×5, SL-muy-pegado×4, chop×3, sin-causa-clara×1
- INV/SHORT (n=43): RR-bajo×22, contra-estructura×14, stop-en-el-minimo×13, sin-causa-clara×8, estirado×8, SL-muy-pegado×5, sin-nivel-detras×4, chop×3
- RETEST/LONG (n=2028): killzone-Asia-largo×796, RR-bajo×786, contra-estructura×756, stop-en-el-minimo×668, sin-nivel-detras×405, estirado×348, chop×291, SL-muy-pegado×229, sin-causa-clara×148, contra-sesgo×1
- RETEST/SHORT (n=1334): RR-bajo×463, contra-estructura×459, stop-en-el-minimo×441, sin-nivel-detras×263, estirado×257, sin-causa-clara×184, SL-muy-pegado×177, chop×169

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
    "n": 6888,
    "naive_expR": 0.015,
    "managed_expR": 0.1,
    "delta": 0.085,
    "avgEntryBetterTk_p50": 2.6,
    "fill_t3plus_pct": 48.4,
    "fill_full_pct": 34.1,
    "m1_rate": 35.6,
    "m2_rate": 22.4,
    "m3_rate": 12.2,
    "beAfterM1_rate": 16.8
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 62,
      "naive_expR": 0.097,
      "managed_expR": 0.27,
      "delta": 0.173,
      "avgEntryBetterTk_p50": 2.05,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 38.7,
      "m1_rate": 43.5,
      "m2_rate": 30.6,
      "m3_rate": 17.7,
      "beAfterM1_rate": 17.7
    },
    "1m/INV/SHORT": {
      "n": 60,
      "naive_expR": 0.111,
      "managed_expR": 0.39,
      "delta": 0.279,
      "avgEntryBetterTk_p50": 3.0,
      "fill_t3plus_pct": 53.3,
      "fill_full_pct": 43.3,
      "m1_rate": 40.0,
      "m2_rate": 28.3,
      "m3_rate": 16.7,
      "beAfterM1_rate": 15.0
    },
    "1m/RETEST/LONG": {
      "n": 2506,
      "naive_expR": 0.004,
      "managed_expR": 0.093,
      "delta": 0.088,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 49.2,
      "fill_full_pct": 35.4,
      "m1_rate": 34.5,
      "m2_rate": 21.4,
      "m3_rate": 11.3,
      "beAfterM1_rate": 15.8
    },
    "1m/RETEST/SHORT": {
      "n": 1632,
      "naive_expR": 0.018,
      "managed_expR": 0.137,
      "delta": 0.12,
      "avgEntryBetterTk_p50": 2.6500000000000004,
      "fill_t3plus_pct": 48.9,
      "fill_full_pct": 33.4,
      "m1_rate": 39.3,
      "m2_rate": 25.0,
      "m3_rate": 14.2,
      "beAfterM1_rate": 18.5
    },
    "2m/INV/LONG": {
      "n": 26,
      "naive_expR": -0.247,
      "managed_expR": -0.231,
      "delta": 0.017,
      "avgEntryBetterTk_p50": 2.4000000000000004,
      "fill_t3plus_pct": 57.7,
      "fill_full_pct": 38.5,
      "m1_rate": 15.4,
      "m2_rate": 15.4,
      "m3_rate": 0.0,
      "beAfterM1_rate": 3.8
    },
    "2m/INV/SHORT": {
      "n": 27,
      "naive_expR": 0.019,
      "managed_expR": -0.002,
      "delta": -0.021,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 48.1,
      "fill_full_pct": 37.0,
      "m1_rate": 25.9,
      "m2_rate": 22.2,
      "m3_rate": 14.8,
      "beAfterM1_rate": 7.4
    },
    "2m/RETEST/LONG": {
      "n": 1180,
      "naive_expR": -0.033,
      "managed_expR": 0.05,
      "delta": 0.083,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 47.6,
      "fill_full_pct": 32.0,
      "m1_rate": 33.4,
      "m2_rate": 19.9,
      "m3_rate": 10.8,
      "beAfterM1_rate": 17.1
    },
    "2m/RETEST/SHORT": {
      "n": 777,
      "naive_expR": 0.074,
      "managed_expR": 0.147,
      "delta": 0.074,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.4,
      "fill_full_pct": 36.6,
      "m1_rate": 38.1,
      "m2_rate": 25.0,
      "m3_rate": 14.0,
      "beAfterM1_rate": 17.8
    },
    "5m/INV/LONG": {
      "n": 10,
      "naive_expR": 0.849,
      "managed_expR": 0.732,
      "delta": -0.117,
      "avgEntryBetterTk_p50": 4.2,
      "fill_t3plus_pct": 40.0,
      "fill_full_pct": 30.0,
      "m1_rate": 40.0,
      "m2_rate": 30.0,
      "m3_rate": 10.0,
      "beAfterM1_rate": 20.0
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
      "n": 369,
      "naive_expR": 0.09,
      "managed_expR": 0.026,
      "delta": -0.064,
      "avgEntryBetterTk_p50": 2.4,
      "fill_t3plus_pct": 39.8,
      "fill_full_pct": 28.5,
      "m1_rate": 30.9,
      "m2_rate": 19.0,
      "m3_rate": 10.0,
      "beAfterM1_rate": 16.3
    },
    "5m/RETEST/SHORT": {
      "n": 234,
      "naive_expR": -0.007,
      "managed_expR": 0.032,
      "delta": 0.039,
      "avgEntryBetterTk_p50": 4.95,
      "fill_t3plus_pct": 49.1,
      "fill_full_pct": 30.8,
      "m1_rate": 31.6,
      "m2_rate": 21.4,
      "m3_rate": 10.7,
      "beAfterM1_rate": 14.5
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 5806,
    "layer_expR": 0.022,
    "orig_expR": 0.171,
    "delta_orig_minus_layer": 0.149,
    "delta_ci90": [
      0.092,
      0.209
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 46.3,
    "orig_wrTP1": 32.3,
    "slTk_p50": 18.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.8,
    "orig_saved_from_SL": 12,
    "orig_caused_SL": 826
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 178,
      "layer_expR": 0.072,
      "orig_expR": 0.307,
      "delta_orig_minus_layer": 0.235,
      "delta_ci90": [
        -0.136,
        0.71
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 46.6,
      "orig_wrTP1": 26.4,
      "slTk_p50": 17.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 3.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 36
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
      "n": 4504,
      "layer_expR": 0.014,
      "orig_expR": 0.167,
      "delta_orig_minus_layer": 0.153,
      "delta_ci90": [
        0.094,
        0.214
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.8,
      "orig_wrTP1": 33.3,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 12,
      "orig_caused_SL": 623
    },
    "retestBar2": {
      "n": 1124,
      "layer_expR": 0.047,
      "orig_expR": 0.168,
      "delta_orig_minus_layer": 0.121,
      "delta_ci90": [
        -0.019,
        0.267
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 44.2,
      "orig_wrTP1": 29.4,
      "slTk_p50": 15.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 3.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 167
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 62,
      "layer_expR": 0.097,
      "orig_expR": 0.125,
      "delta_orig_minus_layer": 0.028,
      "delta_ci90": [
        -0.435,
        0.499
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 45.2,
      "orig_wrTP1": 24.2,
      "slTk_p50": 15.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 4.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 13
    },
    "1m/INV/SHORT": {
      "n": 50,
      "layer_expR": 0.122,
      "orig_expR": 0.531,
      "delta_orig_minus_layer": 0.408,
      "delta_ci90": [
        -0.548,
        1.779
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.0,
      "orig_wrTP1": 26.0,
      "slTk_p50": 16.5,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 12
    },
    "1m/RETEST/LONG": {
      "n": 2135,
      "layer_expR": 0.005,
      "orig_expR": 0.169,
      "delta_orig_minus_layer": 0.163,
      "delta_ci90": [
        0.076,
        0.254
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.4,
      "orig_wrTP1": 29.8,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.3,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 315
    },
    "1m/RETEST/SHORT": {
      "n": 1252,
      "layer_expR": 0.034,
      "orig_expR": 0.168,
      "delta_orig_minus_layer": 0.133,
      "delta_ci90": [
        0.003,
        0.271
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.1,
      "orig_wrTP1": 29.3,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 3.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 185
    },
    "2m/INV/LONG": {
      "n": 26,
      "layer_expR": -0.247,
      "orig_expR": 0.819,
      "delta_orig_minus_layer": 1.066,
      "delta_ci90": [
        0.007,
        2.311
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 42.3,
      "orig_wrTP1": 26.9,
      "slTk_p50": 13.5,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 3.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 4
    },
    "2m/INV/SHORT": {
      "n": 26,
      "layer_expR": 0.003,
      "orig_expR": 0.248,
      "delta_orig_minus_layer": 0.245,
      "delta_ci90": [
        -0.031,
        0.516
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 30.8,
      "orig_wrTP1": 26.9,
      "slTk_p50": 16.5,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 1
    },
    "2m/RETEST/LONG": {
      "n": 1063,
      "layer_expR": -0.018,
      "orig_expR": 0.024,
      "delta_orig_minus_layer": 0.042,
      "delta_ci90": [
        -0.034,
        0.126
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.6,
      "orig_wrTP1": 34.1,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 144
    },
    "2m/RETEST/SHORT": {
      "n": 625,
      "layer_expR": 0.096,
      "orig_expR": 0.212,
      "delta_orig_minus_layer": 0.117,
      "delta_ci90": [
        -0.009,
        0.243
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.9,
      "orig_wrTP1": 34.7,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 96
    },
    "5m/INV/LONG": {
      "n": 10,
      "layer_expR": 0.849,
      "orig_expR": -0.458,
      "delta_orig_minus_layer": -1.307,
      "delta_ci90": [
        -1.91,
        -0.771
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 90.0,
      "orig_wrTP1": 40.0,
      "slTk_p50": 43.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 20.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 5
    },
    "5m/RETEST/LONG": {
      "n": 355,
      "layer_expR": 0.081,
      "orig_expR": 0.235,
      "delta_orig_minus_layer": 0.154,
      "delta_ci90": [
        0.007,
        0.314
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.9,
      "orig_wrTP1": 46.2,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 13.0,
      "orig_wider_pct": 14.9,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 34
    },
    "5m/RETEST/SHORT": {
      "n": 198,
      "layer_expR": -0.045,
      "orig_expR": 0.642,
      "delta_orig_minus_layer": 0.687,
      "delta_ci90": [
        0.13,
        1.418
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.0,
      "orig_wrTP1": 41.9,
      "slTk_p50": 27.0,
      "slOrigTk_p50": 21.5,
      "orig_wider_pct": 21.7,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 16
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 3183,
    "wrTP1": 44.7,
    "expR": -0.018
  },
  "2026-W37": {
    "n": 3856,
    "wrTP1": 46.4,
    "expR": 0.042
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 6660,
  "brier": 0.2221,
  "bias": -0.154,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.143
    },
    {
      "feature": "stretchAtr",
      "weight": -0.16
    },
    {
      "feature": "rvol",
      "weight": 0.076
    },
    {
      "feature": "chopIdx",
      "weight": -0.073
    },
    {
      "feature": "biasScore",
      "weight": -0.067
    },
    {
      "feature": "nearTk",
      "weight": -0.067
    },
    {
      "feature": "nearEdge",
      "weight": 0.052
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.042
    },
    {
      "feature": "aligned",
      "weight": -0.037
    },
    {
      "feature": "structDir",
      "weight": 0.026
    },
    {
      "feature": "hourNY",
      "weight": 0.015
    },
    {
      "feature": "emaStack",
      "weight": -0.006
    },
    {
      "feature": "entryZoneTk",
      "weight": 0.003
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.154,
      "actual": 0.191,
      "n": 666
    },
    {
      "bin": 1,
      "pred": 0.335,
      "actual": 0.276,
      "n": 666
    },
    {
      "bin": 2,
      "pred": 0.415,
      "actual": 0.315,
      "n": 666
    },
    {
      "bin": 3,
      "pred": 0.465,
      "actual": 0.384,
      "n": 666
    },
    {
      "bin": 4,
      "pred": 0.505,
      "actual": 0.458,
      "n": 666
    },
    {
      "bin": 5,
      "pred": 0.538,
      "actual": 0.548,
      "n": 666
    },
    {
      "bin": 6,
      "pred": 0.564,
      "actual": 0.584,
      "n": 666
    },
    {
      "bin": 7,
      "pred": 0.587,
      "actual": 0.656,
      "n": 666
    },
    {
      "bin": 8,
      "pred": 0.613,
      "actual": 0.688,
      "n": 666
    },
    {
      "bin": 9,
      "pred": 0.659,
      "actual": 0.722,
      "n": 666
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
    "expR": 0.097,
    "ci90": [
      -0.168,
      0.382
    ],
    "p_mean_le_0": 0.285,
    "n": 62,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.111,
    "ci90": [
      -0.151,
      0.382
    ],
    "p_mean_le_0": 0.255,
    "n": 60,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.005,
    "ci90": [
      -0.035,
      0.047
    ],
    "p_mean_le_0": 0.439,
    "n": 2510,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.017,
    "ci90": [
      -0.033,
      0.072
    ],
    "p_mean_le_0": 0.293,
    "n": 1639,
    "survives_fdr10": false
  },
  "2m/INV/LONG": {
    "expR": -0.247,
    "ci90": [
      -0.537,
      0.051
    ],
    "p_mean_le_0": 0.904,
    "n": 26,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.019,
    "ci90": [
      -0.408,
      0.503
    ],
    "p_mean_le_0": 0.496,
    "n": 27,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.032,
    "ci90": [
      -0.088,
      0.021
    ],
    "p_mean_le_0": 0.84,
    "n": 1182,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.074,
    "ci90": [
      -0.002,
      0.145
    ],
    "p_mean_le_0": 0.056,
    "n": 777,
    "survives_fdr10": false
  },
  "5m/INV/LONG": {
    "expR": 0.849,
    "ci90": [
      0.522,
      1.254
    ],
    "p_mean_le_0": 0.0,
    "n": 10,
    "survives_fdr10": true
  },
  "5m/RETEST/LONG": {
    "expR": 0.09,
    "ci90": [
      -0.007,
      0.191
    ],
    "p_mean_le_0": 0.068,
    "n": 369,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": -0.005,
    "ci90": [
      -0.133,
      0.14
    ],
    "p_mean_le_0": 0.521,
    "n": 235,
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
      "n": 2442,
      "wrTP1": 45.6,
      "expR": 0.044,
      "pf": 1.09,
      "defining_features": {
        "biasScore": -1.09,
        "emaStack": -0.94,
        "nearEdge": -0.82,
        "structDir": -0.43
      }
    },
    {
      "id": 1,
      "n": 3426,
      "wrTP1": 47.2,
      "expR": 0.032,
      "pf": 1.07,
      "defining_features": {
        "biasScore": 0.76,
        "emaStack": 0.67,
        "nearEdge": 0.55,
        "structDir": 0.29
      }
    },
    {
      "id": 0,
      "n": 936,
      "wrTP1": 42.3,
      "expR": -0.063,
      "pf": 0.88,
      "defining_features": {
        "stretchAtr": 1.63,
        "rvol": 1.33,
        "chopIdx": -1.29,
        "hourNY": -0.17
      }
    },
    {
      "id": 3,
      "n": 235,
      "wrTP1": 36.6,
      "expR": -0.221,
      "pf": 0.63,
      "defining_features": {
        "entryZoneTk": -3.18,
        "nearTk": 2.5,
        "nearEdge": 0.28,
        "stretchAtr": 0.27
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
        "n": 19,
        "wrTP1": 52.6,
        "expR": 0.32
      },
      "YM": {
        "n": 21,
        "wrTP1": 38.1,
        "expR": 0.194
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
        "n": 11,
        "wrTP1": 45.5,
        "expR": -0.193
      }
    },
    "expR_spread": 0.754,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 46,
        "wrTP1": 45.7,
        "expR": 0.042
      },
      "NQ": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.37
      },
      "ES": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": 0.285
      },
      "GC": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.235
      }
    },
    "expR_spread": 0.328,
    "verdict": "universal"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 478,
        "wrTP1": 45.8,
        "expR": 0.113
      },
      "NQ": {
        "n": 561,
        "wrTP1": 44.4,
        "expR": -0.054
      },
      "ES": {
        "n": 477,
        "wrTP1": 44.0,
        "expR": -0.01
      },
      "CL": {
        "n": 720,
        "wrTP1": 44.7,
        "expR": -0.052
      },
      "YM": {
        "n": 315,
        "wrTP1": 41.9,
        "expR": 0.101
      }
    },
    "expR_spread": 0.167,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 207,
        "wrTP1": 44.0,
        "expR": 0.032
      },
      "GC": {
        "n": 318,
        "wrTP1": 40.9,
        "expR": -0.002
      },
      "YM": {
        "n": 650,
        "wrTP1": 44.8,
        "expR": 0.09
      },
      "ES": {
        "n": 466,
        "wrTP1": 44.4,
        "expR": -0.025
      },
      "CL": {
        "n": 43,
        "wrTP1": 27.9,
        "expR": -0.547
      }
    },
    "expR_spread": 0.637,
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
        "n": 4,
        "wrTP1": 50.0,
        "expR": -0.323
      },
      "YM": {
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.673
      },
      "ES": {
        "n": 5,
        "wrTP1": 60.0,
        "expR": 0.192
      },
      "NQ": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.035
      }
    },
    "expR_spread": 0.865,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 18,
        "wrTP1": 38.9,
        "expR": 0.251
      },
      "ES": {
        "n": 3,
        "wrTP1": 33.3,
        "expR": -0.44
      },
      "GC": {
        "n": 4,
        "wrTP1": 0.0,
        "expR": -0.495
      }
    },
    "expR_spread": 0.746,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 286,
        "wrTP1": 47.9,
        "expR": -0.037
      },
      "GC": {
        "n": 170,
        "wrTP1": 46.5,
        "expR": 0.045
      },
      "CL": {
        "n": 346,
        "wrTP1": 49.4,
        "expR": -0.023
      },
      "ES": {
        "n": 233,
        "wrTP1": 46.8,
        "expR": -0.049
      },
      "YM": {
        "n": 163,
        "wrTP1": 38.7,
        "expR": -0.102
      }
    },
    "expR_spread": 0.147,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 190,
        "wrTP1": 51.6,
        "expR": 0.064
      },
      "YM": {
        "n": 337,
        "wrTP1": 49.9,
        "expR": 0.152
      },
      "GC": {
        "n": 137,
        "wrTP1": 41.6,
        "expR": -0.017
      },
      "NQ": {
        "n": 105,
        "wrTP1": 47.6,
        "expR": 0.05
      },
      "CL": {
        "n": 20,
        "wrTP1": 35.0,
        "expR": -0.422
      }
    },
    "expR_spread": 0.574,
    "verdict": "instrument-specific"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.412
      },
      "YM": {
        "n": 3,
        "wrTP1": 100.0,
        "expR": 0.763
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 1.517
      }
    },
    "expR_spread": 1.105,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 13,
        "wrTP1": 69.2,
        "expR": 0.278
      },
      "ES": {
        "n": 73,
        "wrTP1": 52.1,
        "expR": 0.163
      },
      "YM": {
        "n": 60,
        "wrTP1": 48.3,
        "expR": 0.035
      },
      "CL": {
        "n": 113,
        "wrTP1": 58.4,
        "expR": 0.198
      },
      "NQ": {
        "n": 120,
        "wrTP1": 50.8,
        "expR": -0.051
      }
    },
    "expR_spread": 0.329,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 47,
        "wrTP1": 53.2,
        "expR": -0.014
      },
      "ES": {
        "n": 56,
        "wrTP1": 55.4,
        "expR": 0.098
      },
      "GC": {
        "n": 44,
        "wrTP1": 29.5,
        "expR": -0.406
      },
      "YM": {
        "n": 89,
        "wrTP1": 48.3,
        "expR": 0.161
      },
      "CL": {
        "n": 8,
        "wrTP1": 50.0,
        "expR": -0.239
      }
    },
    "expR_spread": 0.567,
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
    "n": 7039,
    "wrTP1": 45.6,
    "nSL": 3448,
    "nTO": 379,
    "expR": 0.015,
    "pf": 1.03,
    "mfe_p25": 7.0,
    "mfe_p50": 15.0,
    "mfe_p75": 37.0,
    "winnerMAE_p75": 11.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.5,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -12.0,
    "revAfterSL_rate": 32.8
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
      "asOf": "2026-09-11 (viernes -- incidente de repo: origin/main fue reescrito rio arriba, historia sin ancestro comun con la local; verificado como superset sin perdida de datos y resuelto con git reset --hard origin/main. Dato nuevo genuino del bus post-reset.)",
      "retest_1m_long": {
        "n": 2135,
        "deltaER_orig_minus_layer": 0.163,
        "ci90": [
          0.076,
          0.254
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 1706 a 2135, delta bajo un poco (0.178->0.163) pero sigue firme -- cuarta confirmacion independiente, sigue siendo la lectura mas estable del experimento."
      },
      "retest_1m_short": {
        "n": 1252,
        "deltaER_orig_minus_layer": 0.133,
        "ci90": [
          0.003,
          0.271
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 898 a 1252, delta bajo de 0.181 a 0.133 y el limite inferior del CI90 cayo de 0.027 a 0.003 -- certifica, pero a un paso de dejar de hacerlo; vigilar de cerca la proxima corrida."
      },
      "retest_2m_long": {
        "n": 1063,
        "deltaER_orig_minus_layer": 0.042,
        "ci90": [
          -0.034,
          0.126
        ],
        "ci90_no_cruza_cero": false,
        "nota": "n subio de 866 a 1063, delta subio un poco (0.018->0.042) pero sigue sin certificar -- quinta lectura seguida confirmando que 2m LONG no es candidato."
      },
      "retest_2m_short": {
        "n": 625,
        "deltaER_orig_minus_layer": 0.096,
        "ci90": [
          -0.009,
          0.243
        ],
        "ci90_no_cruza_cero": false,
        "nota": "PIERDE LA CERTIFICACION 'al filo' de ayer: n subio de 462 a 625, el CI90 volvio a cruzar cero (era [0.001,0.313]). Se cumplio la advertencia de tratarlo como debil -- sacar 2m SHORT de la propuesta de la revision semanal junto con 2m LONG."
      },
      "retest_5m_long": {
        "n": 355,
        "deltaER_orig_minus_layer": 0.154,
        "ci90": [
          0.007,
          0.314
        ],
        "ci90_no_cruza_cero": true,
        "nota": "RECUPERA LA CERTIFICACION que habia perdido ayer: n subio de 316 a 355, el CI90 volvio a quedar del lado positivo ([-0.011,0.32] -> [0.007,0.314]). Tercer vaiven certifica/no-certifica de este segmento en 3 dias -- seguir tratandolo como inestable, no incluir en la propuesta de la revision semanal hasta que se sostenga 2 lecturas seguidas del mismo lado."
      },
      "retest_5m_short": {
        "n": 198,
        "deltaER_orig_minus_layer": 0.687,
        "ci90": [
          0.13,
          1.418
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 149 a 198, delta bajo un poco (0.734->0.687) pero el CI90 se estrecho (antes [0.034,1.63]) -- sigue siendo el efecto mas grande y ahora tambien la lectura mas solida del dataset."
      },
      "overall_by_basis_retestBar": {
        "n": 4504,
        "deltaER": 0.153,
        "ci90": [
          0.094,
          0.214
        ],
        "nota": "n subio de 3637 a 4504, delta bajo un poco (0.162->0.153) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba."
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
      "2026-09-11 (viernes): incidente de repo (origin/main reescrito rio arriba, sin ancestro comun con la rama local; verificado como superset sin perdida de datos, resuelto con git reset --hard origin/main -- ver playbooks para el detalle). Dato nuevo genuino post-reset. Vista actualizada de candidatos: 1m LONG sigue solido (cuarta confirmacion, delta 0.163); 1m SHORT certifica pero a un paso de perder la certificacion (limite inferior del CI90 bajo a 0.003, vigilar de cerca); 5m SHORT sigue siendo el efecto mas grande y ahora la lectura mas solida (CI90 se estrecho); 5m LONG RECUPERA la certificacion que habia perdido ayer (tercer vaiven en 3 dias, seguir tratando como inestable). 2m SHORT PIERDE la certificacion 'al filo' de ayer (CI90 volvio a cruzar cero) -- se une a 2m LONG como no-candidato. Vista para la revision semanal del domingo 2026-09-13: candidatos solidos = 1m LONG y 5m SHORT; candidato debil/al filo = 1m SHORT; inestable (no incluir todavia) = 5m LONG; fuera = 2m LONG y 2m SHORT."
    ],
    "beforeN": 6845,
    "afterN": 0,
    "before": {
      "n": 6845,
      "wrTP1": 45.6,
      "nSL": 3362,
      "nTO": 362,
      "expR": 0.013,
      "pf": 1.03,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 37.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 33.0
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
    "date": "2026-09-11",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-10T19:15:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "ES",
    "focus": {
      "sym": "ES",
      "verdict": "AVOID",
      "window": "20:00-23:00 CT",
      "setup": {
        "es": "A+ retest IBH/VAH 7615-7632 + FVG 1h 7609-7632, corto a favor -- en espera de que enfrie el estiramiento",
        "en": "A+ IBH/VAH retest 7615-7632 + 1h FVG 7609-7632, short with bias -- waiting for the stretch to cool"
      },
      "trigger": {
        "es": "primero que el estiramiento baje de 2A; luego mecha dentro de 7615-7632 con cierre 5m de vuelta bajo 7615, o barrida de 7632 y rechazo inmediato",
        "en": "first wait for the stretch to drop under 2A; then a wick into 7615-7632 with a 5m close back below 7615, or a 7632 sweep with an immediate rejection"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 7646 (techo del FVG 4h)",
        "en": "5m close sustained above 7646 (4h FVG top)"
      },
      "note": {
        "es": "estirado 2.43A tras la reapertura -- no persigas mas corto aqui; la tesis (3 sesiones limpias) sigue siendo la mejor del complejo pero toca esperar a que enfrie antes del rebote a la zona",
        "en": "stretched 2.43A after the reopen -- don't chase more short here; the thesis (3 clean sessions) is still the best in the complex but it needs to cool off before the bounce into the zone"
      }
    },
    "summary": {
      "es": [
        "!! precision de escenario A bajo 30% en NQ/ES/GC (20d) -- escepticismo extra con escenarios A hoy (la otra causa de la alarma del pre-asia, orb caido, ya se resolvio)",
        "reapertura sin resolucion en indices: NQ y ES profundizaron el corto sin testear sus zonas A+ -- ahora estirados 3.55A/2.43A, AVOID temporal a perseguir mas aqui, ambos pegados a su minimo overnight",
        "GC y CL: el estiramiento extremo citado en el pre-asia (13.35A/15.22A) se normalizo (1.15A/0.99A command) -- era discrepancia de fuentes, no un giro real; siguen sin zona A+ a tiro, quedan en WAIT",
        "YM sigue en conflicto de marcos y ahora ademas indeciso (command paso de SHORT a NEUTRAL/DEBIL en el chop) -- WAIT",
        "CL ya hizo maximo nuevo sin retroceso (104.46, rompio el IBH previo 104.04) -- confirma el escenario B previsto (prob 0.68); el retroceso a 99.73-100.64 sigue sin llegar",
        "mas limpio: ES (tesis mas solida, 3 sesiones de confirmacion limpia) pero ahora en AVOID por estiramiento -- vigila que enfrie antes del rebote a 7615-7632",
        "limite $1000 por cuenta -- ninguna zona de hoy da maxContracts>0 en full size, revisa micros antes de entrar"
      ],
      "en": [
        "!! scenario-A accuracy under 30% on NQ/ES/GC (20d) -- extra skepticism on scenario-A calls today (the pre-asia's other alarm cause, orb down, has resolved)",
        "unresolved index reopen: NQ and ES deepened the short without tes
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 2616,
  "by_verdict": {
    "AVOID": {
      "n": 909,
      "wrTP1": 45.1,
      "nSL": 467,
      "nTO": 32,
      "expR": 0.012,
      "pf": 1.02,
      "mfe_p25": 6.0,
      "mfe_p50": 13.0,
      "mfe_p75": 24.0,
      "winnerMAE_p75": 7.0,
      "winnerMAE_p90": 16.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -9.0,
      "revAfterSL_rate": 35.3
    },
    "GO": {
      "n": 265,
      "wrTP1": 49.1,
      "nSL": 130,
      "nTO": 5,
      "expR": 0.024,
      "pf": 1.05,
      "mfe_p25": 8.75,
      "mfe_p50": 19.0,
      "mfe_p75": 43.25,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 24.400000000000034,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 31.5
    },
    "WAIT": {
      "n": 1442,
      "wrTP1": 48.4,
      "nSL": 654,
      "nTO": 90,
      "expR": 0.084,
      "pf": 1.18,
      "mfe_p25": 8.0,
      "mfe_p50": 21.0,
      "mfe_p75": 51.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 32.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 37.2
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.012,
      "ci90": [
        -0.057,
        0.086
      ],
      "p_mean_le_0": 0.385,
      "n": 898
    },
    "GO": {
      "expR": 0.024,
      "ci90": [
        -0.096,
        0.141
      ],
      "p_mean_le_0": 0.365,
      "n": 264
    },
    "WAIT": {
      "expR": 0.084,
      "ci90": [
        0.031,
        0.137
      ],
      "p_mean_le_0": 0.004,
      "n": 1415
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 909,
      "wrTP1": 45.1,
      "nSL": 467,
      "nTO": 32,
      "expR": 0.012,
      "pf": 1.02,
      "mfe_p25": 6.0,
      "mfe_p50": 13.0,
      "mfe_p75": 24.0,
      "winnerMAE_p75": 7.0,
      "winnerMAE_p90": 16.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -9.0,
      "revAfterSL_rate": 35.3
    },
    "GO_or_WAIT": {
      "n": 1707,
      "wrTP1": 48.5,
      "nSL": 784,
      "nTO": 95,
      "expR": 0.074,
      "pf": 1.16,
      "mfe_p25": 8.0,
      "mfe_p50": 21.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 30.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 36.2
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.012,
      "ci90": [
        -0.057,
        0.086
      ],
      "p_mean_le_0": 0.385,
      "n": 898
    },
    "GO_or_WAIT": {
      "expR": 0.074,
      "ci90": [
        0.025,
        0.123
      ],
      "p_mean_le_0": 0.004,
      "n": 1679
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "WAIT": {
        "n": 19,
        "wrTP1": 57.9,
        "nSL": 7,
        "nTO": 1,
        "expR": 0.215,
        "pf": 1.58,
        "mfe_p25": 19.5,
        "mfe_p50": 43.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 8.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 28.6
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 23,
        "wrTP1": 39.1,
        "nSL": 12,
        "nTO": 2,
        "expR": -0.151,
        "pf": 0.72,
        "mfe_p25": 6.5,
        "mfe_p50": 13.5,
        "mfe_p75": 21.75,
        "winnerMAE_p75": 4.0,
        "winnerMAE_p90": 6.6000000000000005,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 8.3
      },
      "WAIT": {
        "n": 19,
        "wrTP1": 47.4,
        "nSL": 9,
        "nTO": 1,
        "expR": -0.222,
        "pf": 0.53,
        "mfe_p25": 7.0,
        "mfe_p50": 24.0,
        "mfe_p75": 40.0,
        "winnerMAE_p75": 64.0,
        "winnerMAE_p90": 77.6,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -22.0,
        "revAfterSL_rate": 44.4
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 429,
        "wrTP1": 50.6,
        "nSL": 203,
        "nTO": 9,
        "expR": 0.069,
        "pf": 1.15,
        "mfe_p25": 6.0,
        "mfe_p50": 11.0,
        "mfe_p75": 22.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -8.0,
        "revAfterSL_rate": 34.5
      },
      "GO": {
        "n": 184,
        "wrTP1": 47.8,
        "nSL": 95,
        "nTO": 1,
        "expR": -0.066,
        "pf": 0.87,
        "mfe_p25": 8.5,
        "mfe_p50": 20.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 30.599999999999994,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.5,
        "revAfterSL_rate": 36.8
      },
      "WAIT": {
        "n": 758,
        "wrTP1": 52.1,
        "nSL": 318,
        "nTO": 45,
        "expR": 0.202,
        "pf": 1.48,
        "mfe_p25": 9.0,
        "mfe_p50": 24.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 25.600000000000023,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 40.3
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 454,
        "wrTP1": 40.3,
        "nSL": 251,
        "nTO": 20,
        "expR": -0.034,
        "pf": 0.94,
        "mfe_p25": 6.0,
        "mfe_p50": 14.0,
        "mfe_p75": 26.0,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 11.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 37.5
      },
      "GO": {
        "n": 76,
        "wrTP1": 51.3,
        "nSL": 33,
        "nTO": 4,
        "expR": 0.193,
        "pf": 1.44,
        "mfe_p25": 8.75,
        "mfe_p50": 14.5,
        "mfe_p75": 37.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 8.200000000000003,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -8.0,
        "revAfterSL_rate": 15.2
      },
      "WAIT": {
        "n": 646,
        "wrTP1": 43.8,
        "nSL": 320,
        "nTO": 43,
        "expR": -0.055,
        "pf": 0.89,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 36.80000000000001,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 34.1
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```
