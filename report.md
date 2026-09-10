# Scalp CC · report 2026-09-10T01:14Z
- signals=5658 outcomes=5539 pares_resueltos=5658 pendientes=0 huerfanos=23

## ⚠ ALERTAS (llevar al frente del resumen)
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.168 vs 0.007, delta 0.162 CI90 [0.093, 0.227], n 3637). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=AVOID rinden MEJOR de forma no-random (E[R] 0.122 CI90 [0.045, 0.193], n 637). Contrario a la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden PEOR de forma no-random (E[R] -0.196 CI90 [-0.301, -0.08], n 219). Contrario a la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.018, "ci90": [-0.01, 0.045], "p_mean_le_0": 0.144, "n": 5516}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 53 | 47.2 | 0.225 | 1.53 | 21 | 11.0 | 6.0 | 23.8 |
| 1m/INV/SHORT | 54 | 53.7 | 0.138 | 1.34 | 21 | 14.0 | 10.0 | 19.0 |
| 1m/RETEST/LONG | 2065 | 45.1 | 0.003 | 1.01 | 1019 | 12.0 | 9.0 | 29.2 |
| 1m/RETEST/SHORT | 1295 | 42.8 | 0.051 | 1.1 | 631 | 16.0 | 9.0 | 27.4 |
| 2m/INV/LONG | 22 | 36.4 | -0.32 | 0.48 | 13 | 6.5 | 7.25 | 23.1 |
| 2m/INV/SHORT | 23 | 34.8 | -0.14 | 0.73 | 12 | 16.0 | 4.25 | 33.3 |
| 2m/RETEST/LONG | 988 | 46.3 | -0.052 | 0.9 | 498 | 14.0 | 12.0 | 38.0 |
| 2m/RETEST/SHORT | 612 | 45.6 | 0.057 | 1.11 | 301 | 22.0 | 9.5 | 36.2 |
| 5m/INV/LONG | 7 | 100.0 | 0.646 | 99.0 | 0 | 28.0 | 24.5 | None |
| 5m/INV/SHORT | 5 | 60.0 | -0.186 | 0.54 | 2 | 34.0 | 88.5 | 100.0 |
| 5m/RETEST/LONG | 341 | 53.7 | 0.093 | 1.21 | 146 | 20.0 | 18.5 | 52.1 |
| 5m/RETEST/SHORT | 193 | 46.1 | 0.02 | 1.04 | 94 | 35.0 | 21.0 | 37.2 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 403 | 26.1 | 0.104 | 1.16 | 247 | 26.0 | 13.0 | 21.1 |
| B | 2427 | 46.2 | 0.017 | 1.03 | 1181 | 15.0 | 9.0 | 30.6 |
| C | 2828 | 47.6 | 0.007 | 1.01 | 1330 | 14.0 | 11.0 | 36.5 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 2271 | 48.9 | 0.053 | 1.11 | 1029 | 11.0 | 7.0 | 39.8 |
| London | 853 | 45.0 | -0.053 | 0.9 | 452 | 17.0 | 12.0 | 31.9 |
| NY | 952 | 45.3 | 0.114 | 1.23 | 456 | 23.0 | 16.5 | 33.6 |
| Sin KZ | 1582 | 40.9 | -0.052 | 0.9 | 821 | 17.0 | 12.0 | 23.3 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 1485 | 44.0 | 0.018 | 1.04 | 729 | 16.0 | 10.0 | 29.6 |
| edge=0 | 2410 | 47.7 | 0.02 | 1.04 | 1150 | 13.0 | 10.0 | 38.6 |
| edge=1 | 1763 | 43.6 | 0.015 | 1.03 | 879 | 18.0 | 13.0 | 27.1 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| aligned=1 | 5647 | 45.5 | 0.017 | 1.03 | 2757 | 15.0 | 10.0 | 32.6 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 37 | 48.6 | 0.022 | 1.05 | 17 | 7.0 | 5.5 | 23.5 |
| INV/LONG|edge=1 | 41 | 48.8 | 0.161 | 1.4 | 15 | 22.0 | 17.0 | 20.0 |
| INV/SHORT|edge=-1 | 52 | 42.3 | -0.043 | 0.91 | 25 | 18.0 | 10.75 | 24.0 |
| INV/SHORT|edge=0 | 28 | 60.7 | 0.218 | 1.63 | 9 | 12.0 | 11.0 | 44.4 |
| INV/SHORT|edge=1 | 2 | 50.0 | -0.29 | 0.42 | 1 | 7.0 | 5.0 | 0.0 |
| RETEST/LONG|edge=-1 | 191 | 47.6 | 0.064 | 1.14 | 86 | 10.0 | 7.0 | 46.5 |
| RETEST/LONG|edge=0 | 1562 | 49.6 | -0.029 | 0.94 | 747 | 11.0 | 9.0 | 41.1 |
| RETEST/LONG|edge=1 | 1641 | 43.0 | 0.012 | 1.02 | 830 | 18.0 | 13.0 | 26.0 |
| RETEST/SHORT|edge=-1 | 1238 | 43.5 | 0.012 | 1.02 | 616 | 17.0 | 10.0 | 27.4 |
| RETEST/SHORT|edge=0 | 783 | 43.6 | 0.113 | 1.22 | 377 | 20.0 | 11.0 | 34.2 |
| RETEST/SHORT|edge=1 | 79 | 53.2 | 0.022 | 1.05 | 33 | 13.5 | 8.5 | 57.6 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 23 | 47.8 | 0.293 | 1.82 | 7 | 19.0 | 7.0 | 14.3 |
| INV/LONG|tier=C | 59 | 49.2 | 0.047 | 1.1 | 27 | 10.0 | 9.0 | 25.9 |
| INV/SHORT|tier=B | 28 | 53.6 | 0.104 | 1.25 | 11 | 14.0 | 4.5 | 0.0 |
| INV/SHORT|tier=C | 54 | 46.3 | 0.002 | 1.0 | 24 | 18.0 | 23.0 | 41.7 |
| RETEST/LONG|tier=A+ | 252 | 25.4 | 0.055 | 1.08 | 156 | 19.0 | 16.75 | 19.9 |
| RETEST/LONG|tier=B | 1361 | 45.9 | 0.025 | 1.05 | 672 | 15.0 | 10.0 | 30.7 |
| RETEST/LONG|tier=C | 1781 | 49.5 | -0.034 | 0.93 | 835 | 12.0 | 11.0 | 39.0 |
| RETEST/SHORT|tier=A+ | 151 | 27.2 | 0.185 | 1.29 | 91 | 37.0 | 9.0 | 23.1 |
| RETEST/SHORT|tier=B | 1015 | 46.4 | -0.001 | 1.0 | 491 | 15.0 | 9.0 | 31.4 |
| RETEST/SHORT|tier=C | 934 | 43.9 | 0.085 | 1.17 | 444 | 21.0 | 13.0 | 32.0 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 82 | 48.8 | 0.112 | 1.25 | 34 | 11.0 | 8.25 | 23.5 |
| INV/SHORT|aligned=1 | 82 | 48.8 | 0.037 | 1.08 | 35 | 15.0 | 11.0 | 28.6 |
| RETEST/LONG|aligned=0 | 11 | 54.5 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| RETEST/LONG|aligned=1 | 3383 | 46.3 | -0.005 | 0.99 | 1662 | 13.0 | 11.0 | 33.9 |
| RETEST/SHORT|aligned=1 | 2100 | 43.9 | 0.05 | 1.1 | 1026 | 18.0 | 10.0 | 30.9 |

## Autopsia de SL
n_losses=2758  causas: RR-bajo×1026, contra-estructura×1025, stop-en-el-minimo×898, killzone-Asia-largo×670, sin-nivel-detras×543, estirado×503, chop×360, SL-muy-pegado×343, sin-causa-clara×271, contra-sesgo×1
- INV/LONG (n=34): RR-bajo×19, killzone-Asia-largo×18, contra-estructura×12, stop-en-el-minimo×8, estirado×6, SL-muy-pegado×3, sin-nivel-detras×3, chop×1, sin-causa-clara×1
- INV/SHORT (n=35): RR-bajo×18, contra-estructura×12, stop-en-el-minimo×10, sin-causa-clara×7, estirado×5, SL-muy-pegado×4, chop×2, sin-nivel-detras×1
- RETEST/LONG (n=1663): contra-estructura×662, killzone-Asia-largo×652, RR-bajo×651, stop-en-el-minimo×563, sin-nivel-detras×337, estirado×279, chop×236, SL-muy-pegado×187, sin-causa-clara×114, contra-sesgo×1
- RETEST/SHORT (n=1026): contra-estructura×339, RR-bajo×338, stop-en-el-minimo×317, estirado×213, sin-nivel-detras×202, sin-causa-clara×149, SL-muy-pegado×149, chop×121

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
    "n": 5501,
    "naive_expR": 0.018,
    "managed_expR": 0.109,
    "delta": 0.092,
    "avgEntryBetterTk_p50": 2.5,
    "fill_t3plus_pct": 48.3,
    "fill_full_pct": 34.0,
    "m1_rate": 36.3,
    "m2_rate": 22.7,
    "m3_rate": 12.5,
    "beAfterM1_rate": 17.5
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 51,
      "naive_expR": 0.225,
      "managed_expR": 0.367,
      "delta": 0.142,
      "avgEntryBetterTk_p50": 1.0,
      "fill_t3plus_pct": 41.2,
      "fill_full_pct": 35.3,
      "m1_rate": 45.1,
      "m2_rate": 31.4,
      "m3_rate": 17.6,
      "beAfterM1_rate": 19.6
    },
    "1m/INV/SHORT": {
      "n": 51,
      "naive_expR": 0.138,
      "managed_expR": 0.419,
      "delta": 0.281,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 45.1,
      "fill_full_pct": 39.2,
      "m1_rate": 39.2,
      "m2_rate": 27.5,
      "m3_rate": 15.7,
      "beAfterM1_rate": 15.7
    },
    "1m/RETEST/LONG": {
      "n": 2022,
      "naive_expR": 0.002,
      "managed_expR": 0.087,
      "delta": 0.085,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 48.9,
      "fill_full_pct": 35.3,
      "m1_rate": 34.2,
      "m2_rate": 20.7,
      "m3_rate": 11.0,
      "beAfterM1_rate": 16.2
    },
    "1m/RETEST/SHORT": {
      "n": 1238,
      "naive_expR": 0.053,
      "managed_expR": 0.175,
      "delta": 0.123,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.5,
      "fill_full_pct": 32.1,
      "m1_rate": 41.8,
      "m2_rate": 26.6,
      "m3_rate": 15.2,
      "beAfterM1_rate": 19.8
    },
    "2m/INV/LONG": {
      "n": 22,
      "naive_expR": -0.32,
      "managed_expR": -0.312,
      "delta": 0.008,
      "avgEntryBetterTk_p50": 2.1500000000000004,
      "fill_t3plus_pct": 59.1,
      "fill_full_pct": 36.4,
      "m1_rate": 13.6,
      "m2_rate": 13.6,
      "m3_rate": 0.0,
      "beAfterM1_rate": 4.5
    },
    "2m/INV/SHORT": {
      "n": 23,
      "naive_expR": -0.14,
      "managed_expR": -0.009,
      "delta": 0.131,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 47.8,
      "fill_full_pct": 43.5,
      "m1_rate": 26.1,
      "m2_rate": 21.7,
      "m3_rate": 13.0,
      "beAfterM1_rate": 8.7
    },
    "2m/RETEST/LONG": {
      "n": 970,
      "naive_expR": -0.054,
      "managed_expR": 0.039,
      "delta": 0.093,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.9,
      "fill_full_pct": 33.3,
      "m1_rate": 33.3,
      "m2_rate": 19.6,
      "m3_rate": 10.7,
      "beAfterM1_rate": 17.5
    },
    "2m/RETEST/SHORT": {
      "n": 599,
      "naive_expR": 0.057,
      "managed_expR": 0.173,
      "delta": 0.116,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.4,
      "fill_full_pct": 36.7,
      "m1_rate": 40.7,
      "m2_rate": 27.0,
      "m3_rate": 15.9,
      "beAfterM1_rate": 19.4
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
      "n": 330,
      "naive_expR": 0.093,
      "managed_expR": 0.025,
      "delta": -0.068,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 38.5,
      "fill_full_pct": 28.2,
      "m1_rate": 31.2,
      "m2_rate": 19.1,
      "m3_rate": 9.7,
      "beAfterM1_rate": 17.0
    },
    "5m/RETEST/SHORT": {
      "n": 183,
      "naive_expR": 0.017,
      "managed_expR": 0.102,
      "delta": 0.084,
      "avgEntryBetterTk_p50": 5.6,
      "fill_t3plus_pct": 54.1,
      "fill_full_pct": 34.4,
      "m1_rate": 36.1,
      "m2_rate": 25.1,
      "m3_rate": 12.6,
      "beAfterM1_rate": 15.8
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 4544,
    "layer_expR": 0.026,
    "orig_expR": 0.194,
    "delta_orig_minus_layer": 0.168,
    "delta_ci90": [
      0.107,
      0.236
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 46.5,
    "orig_wrTP1": 32.7,
    "slTk_p50": 19.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 4.1,
    "orig_saved_from_SL": 10,
    "orig_caused_SL": 635
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 147,
      "layer_expR": 0.07,
      "orig_expR": 0.474,
      "delta_orig_minus_layer": 0.404,
      "delta_ci90": [
        -0.031,
        0.983
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.0,
      "orig_wrTP1": 29.3,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 29
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
      "n": 3637,
      "layer_expR": 0.007,
      "orig_expR": 0.168,
      "delta_orig_minus_layer": 0.162,
      "delta_ci90": [
        0.093,
        0.227
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.9,
      "orig_wrTP1": 33.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.2,
      "orig_saved_from_SL": 10,
      "orig_caused_SL": 502
    },
    "retestBar2": {
      "n": 760,
      "layer_expR": 0.108,
      "orig_expR": 0.262,
      "delta_orig_minus_layer": 0.154,
      "delta_ci90": [
        -0.012,
        0.323
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 43.8,
      "orig_wrTP1": 30.1,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 104
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 51,
      "layer_expR": 0.225,
      "orig_expR": 0.392,
      "delta_orig_minus_layer": 0.168,
      "delta_ci90": [
        -0.366,
        0.785
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.0,
      "orig_wrTP1": 29.4,
      "slTk_p50": 12.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 3.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 10
    },
    "1m/INV/SHORT": {
      "n": 41,
      "layer_expR": 0.159,
      "orig_expR": 0.779,
      "delta_orig_minus_layer": 0.62,
      "delta_ci90": [
        -0.489,
        2.212
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 56.1,
      "orig_wrTP1": 29.3,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 11
    },
    "1m/RETEST/LONG": {
      "n": 1706,
      "layer_expR": 0.002,
      "orig_expR": 0.18,
      "delta_orig_minus_layer": 0.178,
      "delta_ci90": [
        0.079,
        0.284
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.4,
      "orig_wrTP1": 30.6,
      "slTk_p50": 17.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 253
    },
    "1m/RETEST/SHORT": {
      "n": 898,
      "layer_expR": 0.083,
      "orig_expR": 0.264,
      "delta_orig_minus_layer": 0.181,
      "delta_ci90": [
        0.027,
        0.33
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 43.9,
      "orig_wrTP1": 30.3,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 122
    },
    "2m/INV/LONG": {
      "n": 22,
      "layer_expR": -0.32,
      "orig_expR": 1.074,
      "delta_orig_minus_layer": 1.394,
      "delta_ci90": [
        0.185,
        2.804
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 36.4,
      "orig_wrTP1": 27.3,
      "slTk_p50": 10.5,
      "slOrigTk_p50": 3.5,
      "orig_wider_pct": 4.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 2
    },
    "2m/INV/SHORT": {
      "n": 22,
      "layer_expR": -0.165,
      "orig_expR": 0.054,
      "delta_orig_minus_layer": 0.219,
      "delta_ci90": [
        -0.04,
        0.439
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 31.8,
      "orig_wrTP1": 31.8,
      "slTk_p50": 19.5,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 0
    },
    "2m/RETEST/LONG": {
      "n": 866,
      "layer_expR": -0.039,
      "orig_expR": -0.021,
      "delta_orig_minus_layer": 0.018,
      "delta_ci90": [
        -0.062,
        0.099
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.2,
      "orig_wrTP1": 33.3,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 121
    },
    "2m/RETEST/SHORT": {
      "n": 462,
      "layer_expR": 0.084,
      "orig_expR": 0.233,
      "delta_orig_minus_layer": 0.149,
      "delta_ci90": [
        0.001,
        0.313
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.6,
      "orig_wrTP1": 33.3,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 2.8,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 67
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
      "n": 316,
      "layer_expR": 0.083,
      "orig_expR": 0.225,
      "delta_orig_minus_layer": 0.142,
      "delta_ci90": [
        -0.011,
        0.32
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 55.4,
      "orig_wrTP1": 46.2,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 13.0,
      "orig_wider_pct": 15.5,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 32
    },
    "5m/RETEST/SHORT": {
      "n": 149,
      "layer_expR": -0.013,
      "orig_expR": 0.721,
      "delta_orig_minus_layer": 0.734,
      "delta_ci90": [
        0.034,
        1.63
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.0,
      "orig_wrTP1": 40.9,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 26.2,
      "orig_saved_from_SL": 5,
      "orig_caused_SL": 11
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
    "n": 2427,
    "wrTP1": 46.6,
    "expR": 0.069
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 5331,
  "brier": 0.2226,
  "bias": -0.139,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -0.894
    },
    {
      "feature": "stretchAtr",
      "weight": -0.177
    },
    {
      "feature": "rvol",
      "weight": 0.089
    },
    {
      "feature": "biasScore",
      "weight": -0.082
    },
    {
      "feature": "chopIdx",
      "weight": -0.077
    },
    {
      "feature": "hourNY",
      "weight": 0.076
    },
    {
      "feature": "aligned",
      "weight": -0.048
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.047
    },
    {
      "feature": "structDir",
      "weight": 0.037
    },
    {
      "feature": "nearTk",
      "weight": -0.028
    },
    {
      "feature": "nearEdge",
      "weight": 0.025
    },
    {
      "feature": "emaStack",
      "weight": 0.021
    },
    {
      "feature": "entryZoneTk",
      "weight": 0.019
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.143,
      "actual": 0.197,
      "n": 533
    },
    {
      "bin": 1,
      "pred": 0.324,
      "actual": 0.283,
      "n": 533
    },
    {
      "bin": 2,
      "pred": 0.405,
      "actual": 0.308,
      "n": 533
    },
    {
      "bin": 3,
      "pred": 0.46,
      "actual": 0.398,
      "n": 533
    },
    {
      "bin": 4,
      "pred": 0.503,
      "actual": 0.452,
      "n": 533
    },
    {
      "bin": 5,
      "pred": 0.538,
      "actual": 0.516,
      "n": 533
    },
    {
      "bin": 6,
      "pred": 0.567,
      "actual": 0.63,
      "n": 533
    },
    {
      "bin": 7,
      "pred": 0.593,
      "actual": 0.645,
      "n": 533
    },
    {
      "bin": 8,
      "pred": 0.622,
      "actual": 0.675,
      "n": 533
    },
    {
      "bin": 9,
      "pred": 0.676,
      "actual": 0.721,
      "n": 534
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
    "expR": 0.225,
    "ci90": [
      -0.084,
      0.531
    ],
    "p_mean_le_0": 0.127,
    "n": 51,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.138,
    "ci90": [
      -0.112,
      0.4
    ],
    "p_mean_le_0": 0.198,
    "n": 51,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.003,
    "ci90": [
      -0.041,
      0.05
    ],
    "p_mean_le_0": 0.474,
    "n": 2026,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.051,
    "ci90": [
      -0.008,
      0.111
    ],
    "p_mean_le_0": 0.083,
    "n": 1245,
    "survives_fdr10": false
  },
  "2m/INV/LONG": {
    "expR": -0.32,
    "ci90": [
      -0.625,
      0.02
    ],
    "p_mean_le_0": 0.944,
    "n": 22,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": -0.14,
    "ci90": [
      -0.475,
      0.18
    ],
    "p_mean_le_0": 0.776,
    "n": 23,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.052,
    "ci90": [
      -0.11,
      0.007
    ],
    "p_mean_le_0": 0.926,
    "n": 973,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.057,
    "ci90": [
      -0.026,
      0.142
    ],
    "p_mean_le_0": 0.138,
    "n": 599,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.093,
    "ci90": [
      -0.009,
      0.203
    ],
    "p_mean_le_0": 0.064,
    "n": 330,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": 0.02,
    "ci90": [
      -0.139,
      0.188
    ],
    "p_mean_le_0": 0.408,
    "n": 184,
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
      "n": 1852,
      "wrTP1": 43.8,
      "expR": 0.055,
      "pf": 1.11,
      "defining_features": {
        "biasScore": -1.13,
        "emaStack": -0.98,
        "nearEdge": -0.88,
        "structDir": -0.47
      }
    },
    {
      "id": 1,
      "n": 2856,
      "wrTP1": 48.1,
      "expR": 0.04,
      "pf": 1.08,
      "defining_features": {
        "biasScore": 0.72,
        "emaStack": 0.64,
        "nearEdge": 0.52,
        "stretchAtr": -0.29
      }
    },
    {
      "id": 0,
      "n": 755,
      "wrTP1": 41.7,
      "expR": -0.1,
      "pf": 0.81,
      "defining_features": {
        "stretchAtr": 1.61,
        "rvol": 1.32,
        "chopIdx": -1.29,
        "hourNY": -0.16
      }
    },
    {
      "id": 3,
      "n": 195,
      "wrTP1": 37.4,
      "expR": -0.19,
      "pf": 0.67,
      "defining_features": {
        "entryZoneTk": -3.25,
        "nearTk": 2.26,
        "nearEdge": 0.53,
        "biasScore": 0.39
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
        "n": 8,
        "wrTP1": 50.0,
        "expR": -0.141
      }
    },
    "expR_spread": 0.935,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 40,
        "wrTP1": 50.0,
        "expR": 0.041
      },
      "NQ": {
        "n": 5,
        "wrTP1": 80.0,
        "expR": 0.644
      },
      "ES": {
        "n": 3,
        "wrTP1": 33.3,
        "expR": 0.307
      },
      "GC": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.235
      }
    },
    "expR_spread": 0.603,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 315,
        "wrTP1": 44.8,
        "expR": 0.118
      },
      "NQ": {
        "n": 471,
        "wrTP1": 45.9,
        "expR": -0.016
      },
      "ES": {
        "n": 428,
        "wrTP1": 43.9,
        "expR": -0.035
      },
      "CL": {
        "n": 560,
        "wrTP1": 46.1,
        "expR": -0.031
      },
      "YM": {
        "n": 291,
        "wrTP1": 44.0,
        "expR": 0.032
      }
    },
    "expR_spread": 0.153,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 147,
        "wrTP1": 45.6,
        "expR": 0.116
      },
      "GC": {
        "n": 305,
        "wrTP1": 40.3,
        "expR": -0.001
      },
      "YM": {
        "n": 488,
        "wrTP1": 44.1,
        "expR": 0.13
      },
      "ES": {
        "n": 312,
        "wrTP1": 43.9,
        "expR": 0.037
      },
      "CL": {
        "n": 43,
        "wrTP1": 27.9,
        "expR": -0.547
      }
    },
    "expR_spread": 0.677,
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
        "n": 4,
        "wrTP1": 50.0,
        "expR": 0.188
      },
      "NQ": {
        "n": 4,
        "wrTP1": 25.0,
        "expR": -0.405
      }
    },
    "expR_spread": 0.861,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 14,
        "wrTP1": 42.9,
        "expR": 0.056
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
    "expR_spread": 0.551,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 215,
        "wrTP1": 48.4,
        "expR": -0.005
      },
      "GC": {
        "n": 125,
        "wrTP1": 42.4,
        "expR": -0.039
      },
      "CL": {
        "n": 288,
        "wrTP1": 48.6,
        "expR": -0.027
      },
      "ES": {
        "n": 206,
        "wrTP1": 48.1,
        "expR": -0.032
      },
      "YM": {
        "n": 154,
        "wrTP1": 39.6,
        "expR": -0.206
      }
    },
    "expR_spread": 0.201,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 116,
        "wrTP1": 46.6,
        "expR": 0.062
      },
      "YM": {
        "n": 270,
        "wrTP1": 47.4,
        "expR": 0.13
      },
      "GC": {
        "n": 133,
        "wrTP1": 42.1,
        "expR": -0.001
      },
      "NQ": {
        "n": 73,
        "wrTP1": 46.6,
        "expR": 0.021
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
        "n": 68,
        "wrTP1": 54.4,
        "expR": 0.244
      },
      "YM": {
        "n": 58,
        "wrTP1": 48.3,
        "expR": 0.001
      },
      "CL": {
        "n": 103,
        "wrTP1": 58.3,
        "expR": 0.172
      },
      "NQ": {
        "n": 101,
        "wrTP1": 50.5,
        "expR": -0.05
      }
    },
    "expR_spread": 0.294,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 39,
        "wrTP1": 56.4,
        "expR": 0.094
      },
      "ES": {
        "n": 38,
        "wrTP1": 52.6,
        "expR": 0.144
      },
      "GC": {
        "n": 42,
        "wrTP1": 31.0,
        "expR": -0.377
      },
      "YM": {
        "n": 66,
        "wrTP1": 45.5,
        "expR": 0.203
      },
      "CL": {
        "n": 8,
        "wrTP1": 50.0,
        "expR": -0.239
      }
    },
    "expR_spread": 0.58,
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
    "n": 5658,
    "wrTP1": 45.5,
    "nSL": 2758,
    "nTO": 327,
    "expR": 0.018,
    "pf": 1.04,
    "mfe_p25": 7.0,
    "mfe_p50": 15.0,
    "mfe_p75": 37.0,
    "winnerMAE_p75": 10.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 3.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -12.0,
    "revAfterSL_rate": 32.6
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
    "beforeN": 5494,
    "afterN": 0,
    "before": {
      "n": 5494,
      "wrTP1": 45.4,
      "nSL": 2689,
      "nTO": 312,
      "expR": 0.016,
      "pf": 1.03,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 37.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 32.7
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
    "date": "2026-09-09",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-09T19:14:21-05:00",
    "schema": "sa-plan-2",
    "cleanest": "YM",
    "focus": {
      "sym": "YM",
      "verdict": "WAIT",
      "window": "20:00-23:00 CT",
      "setup": {
        "es": "A+ fade de la zona de liquidez 52557-52581 (confluencia 6, FVG 15m + S/D HTF + sesgo fusionado FUERTE)",
        "en": "A+ fade of the 52557-52581 liquidity zone (confluence 6, 15m FVG + HTF S/D + fused bias FUERTE)"
      },
      "trigger": {
        "es": "mecha dentro de 52557-52581 con cierre 5m de vuelta bajo 52557; o reclamo con fuerza real y cierre 5m sostenido sobre 52581 invalida el corto",
        "en": "a wick inside 52557-52581 with a 5m close back below 52557; or a strong reclaim with a 5m close sustained above 52581 kills the short"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 52595 (IBH de hoy)",
        "en": "5m close sustained above 52595 (today's IBH)"
      },
      "note": {
        "es": "a favor del corto mejor alineado del complejo esta noche (4 fuentes + el sesgo fusionado FUERTE); espera el rebote hasta la zona y el rechazo, no lo persigas en el precio actual",
        "en": "with tonight's best-aligned short in the complex (4 sources + the fused bias FUERTE); wait for the bounce into the zone and the rejection, don't chase it at the current price"
      }
    },
    "summary": {
      "es": [
        "!! el acierto de escenario A sigue bajo 30% en NQ/ES/GC (20d) -- ver alarma.",
        "orb volvio tras 3 corridas caido (los 5 instrumentos) -- confirma de cerca las zonas de no-trade ya usadas de sustituto, sin cambiar ninguna lectura.",
        "NQ: sigue en el mismo cluster tecnico sin resolucion; el sesgo fusionado paso de NEUTRAL/DEBIL a BUSCANDO LONG (MODERADO) tras la reapertura pero sin tocar ninguna zona, WAIT.",
        "ES: pegado al cluster POC/VWAP (7648-7650) desde el cierre, sin subir a probar el cluster 7663-7680 ni romper el low 7628.75, WAIT.",
        "GC: el conflicto se enfrio -- el sesgo fusionado paso de BUSCANDO LONG a ESPERAR/NEUTRAL -- pero el precio cayo a 4437.50, alejandose del cluster golden 4448-4453, WAIT.",
        "YM: sigue el mas limpio y alineado, subio ligero a 52503 pero aun a 54-78pts de la zona de liquidez 52557-52581, WAIT.",
        "CL: hizo nuevo maximo de la noche (97.79, escenario B en marcha) y volvio a 97.02, sigue sin dar el retroceso al cluster 95.55-96.43, WAIT.",
        "Sizing: limite $1000 por cuenta (K=3) sin cambios -- la mayoria de zonas piden micros o 0-1 contrato full.",
        "Ayer se calificaron las 75 predicciones y el cierre completo del 2026-09-08 (ver reviews/2026-09-08.md): 41/75 (55%)."
      ],
      "en": [
        "!! scenario-A accuracy is still below 30% in NQ/ES/GC (20d) -- see alarm.",
        "orb came back after 3 runs down (all 5 instruments) -- it closely confirms the no-trade zones al
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 1845,
  "by_verdict": {
    "AVOID": {
      "n": 641,
      "wrTP1": 51.3,
      "nSL": 286,
      "nTO": 26,
      "expR": 0.122,
      "pf": 1.27,
      "mfe_p25": 6.0,
      "mfe_p50": 13.0,
      "mfe_p75": 28.0,
      "winnerMAE_p75": 7.0,
      "winnerMAE_p90": 13.199999999999989,
      "loserMFEbeforeSL_p50": 2.5,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -9.0,
      "revAfterSL_rate": 32.2
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
      "n": 984,
      "wrTP1": 47.5,
      "nSL": 472,
      "nTO": 45,
      "expR": 0.011,
      "pf": 1.02,
      "mfe_p25": 11.0,
      "mfe_p50": 29.0,
      "mfe_p75": 61.0,
      "winnerMAE_p75": 19.0,
      "winnerMAE_p90": 42.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -19.0,
      "revAfterSL_rate": 41.3
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.122,
      "ci90": [
        0.045,
        0.193
      ],
      "p_mean_le_0": 0.005,
      "n": 637
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
      "expR": 0.011,
      "ci90": [
        -0.051,
        0.075
      ],
      "p_mean_le_0": 0.392,
      "n": 958
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 641,
      "wrTP1": 51.3,
      "nSL": 286,
      "nTO": 26,
      "expR": 0.122,
      "pf": 1.27,
      "mfe_p25": 6.0,
      "mfe_p50": 13.0,
      "mfe_p75": 28.0,
      "winnerMAE_p75": 7.0,
      "winnerMAE_p90": 13.199999999999989,
      "loserMFEbeforeSL_p50": 2.5,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -9.0,
      "revAfterSL_rate": 32.2
    },
    "GO_or_WAIT": {
      "n": 1204,
      "wrTP1": 46.4,
      "nSL": 594,
      "nTO": 51,
      "expR": -0.027,
      "pf": 0.95,
      "mfe_p25": 8.0,
      "mfe_p50": 22.0,
      "mfe_p75": 55.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 37.39999999999998,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 39.6
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.122,
      "ci90": [
        0.045,
        0.193
      ],
      "p_mean_le_0": 0.005,
      "n": 637
    },
    "GO_or_WAIT": {
      "expR": -0.027,
      "ci90": [
        -0.08,
        0.025
      ],
      "p_mean_le_0": 0.81,
      "n": 1177
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
        "n": 11,
        "wrTP1": 45.5,
        "nSL": 6,
        "nTO": 0,
        "expR": 0.057,
        "pf": 1.1,
        "mfe_p25": 4.5,
        "mfe_p50": 11.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 1.0,
        "winnerMAE_p90": 7.000000000000002,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 9.5,
        "entryZoneTk_p50": -8.0,
        "revAfterSL_rate": 16.7
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
        "n": 276,
        "wrTP1": 56.5,
        "nSL": 107,
        "nTO": 13,
        "expR": 0.193,
        "pf": 1.49,
        "mfe_p25": 6.0,
        "mfe_p50": 10.0,
        "mfe_p75": 20.0,
        "winnerMAE_p75": 7.25,
        "winnerMAE_p90": 13.5,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -8.0,
        "revAfterSL_rate": 50.5
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
        "n": 414,
        "wrTP1": 48.6,
        "nSL": 204,
        "nTO": 9,
        "expR": 0.045,
        "pf": 1.09,
        "mfe_p25": 15.0,
        "mfe_p50": 36.0,
        "mfe_p75": 66.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 39.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -21.5,
        "revAfterSL_rate": 42.2
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 354,
        "wrTP1": 47.5,
        "nSL": 173,
        "nTO": 13,
        "expR": 0.067,
        "pf": 1.14,
        "mfe_p25": 7.0,
        "mfe_p50": 16.0,
        "mfe_p75": 35.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 12.600000000000023,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 21.4
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
        "n": 549,
        "wrTP1": 45.9,
        "nSL": 262,
        "nTO": 35,
        "expR": -0.025,
        "pf": 0.95,
        "mfe_p25": 8.0,
        "mfe_p50": 22.0,
        "mfe_p75": 54.5,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 41.900000000000006,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 40.8
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```
