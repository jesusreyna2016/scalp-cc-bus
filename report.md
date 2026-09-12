# Scalp CC · report 2026-09-12T01:13Z
- signals=7752 outcomes=7633 pares_resueltos=7752 pendientes=0 huerfanos=25

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: semana ya cerrada 2026-W36 bajo de n=3183 a n=3179 desde la corrida previa -- vigilar, puede ser deduplicacion.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.189 vs 0.047, delta 0.143 CI90 [0.087, 0.201], n 4834). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.211 vs 0.081, delta 0.13 CI90 [0.012, 0.256], n 1432). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.081 CI90 [0.029, 0.133], n 1490). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.043, "ci90": [0.019, 0.068], "p_mean_le_0": 0.001, "n": 7608}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 66 | 43.9 | 0.129 | 1.27 | 30 | 12.0 | 8.0 | 20.0 |
| 1m/INV/SHORT | 71 | 47.9 | 0.109 | 1.23 | 32 | 18.0 | 11.0 | 18.8 |
| 1m/RETEST/LONG | 2658 | 44.5 | 0.026 | 1.05 | 1312 | 13.0 | 9.0 | 29.3 |
| 1m/RETEST/SHORT | 2021 | 44.7 | 0.046 | 1.09 | 982 | 16.0 | 10.0 | 29.6 |
| 2m/INV/LONG | 26 | 42.3 | -0.247 | 0.56 | 14 | 8.0 | 12.5 | 28.6 |
| 2m/INV/SHORT | 33 | 33.3 | -0.04 | 0.93 | 18 | 16.0 | 6.5 | 33.3 |
| 2m/RETEST/LONG | 1254 | 47.0 | -0.008 | 0.98 | 618 | 16.0 | 12.0 | 37.5 |
| 2m/RETEST/SHORT | 908 | 49.1 | 0.11 | 1.23 | 417 | 20.0 | 11.0 | 41.2 |
| 5m/INV/LONG | 10 | 90.0 | 0.849 | 99.0 | 0 | 30.0 | 32.0 | None |
| 5m/INV/SHORT | 5 | 60.0 | -0.186 | 0.54 | 2 | 34.0 | 88.5 | 100.0 |
| 5m/RETEST/LONG | 402 | 53.5 | 0.104 | 1.23 | 175 | 22.0 | 19.0 | 48.0 |
| 5m/RETEST/SHORT | 298 | 51.0 | 0.084 | 1.19 | 131 | 29.0 | 20.25 | 38.9 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 536 | 27.2 | 0.117 | 1.18 | 338 | 28.0 | 15.0 | 19.8 |
| B | 3248 | 46.6 | 0.05 | 1.1 | 1562 | 16.0 | 10.0 | 31.9 |
| C | 3968 | 48.6 | 0.028 | 1.06 | 1831 | 15.0 | 11.0 | 36.8 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 2919 | 48.8 | 0.055 | 1.12 | 1334 | 11.0 | 8.0 | 37.9 |
| London | 1214 | 45.0 | -0.053 | 0.9 | 640 | 16.0 | 12.0 | 31.7 |
| NY | 1307 | 46.6 | 0.165 | 1.34 | 617 | 25.0 | 17.0 | 37.3 |
| Sin KZ | 2312 | 43.6 | 0.011 | 1.02 | 1140 | 19.0 | 13.0 | 26.3 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 1993 | 45.1 | 0.034 | 1.07 | 977 | 18.0 | 12.5 | 30.6 |
| edge=0 | 3433 | 48.7 | 0.039 | 1.08 | 1604 | 14.0 | 10.0 | 39.0 |
| edge=1 | 2326 | 43.6 | 0.057 | 1.11 | 1150 | 17.0 | 12.5 | 27.4 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 7742 | 46.3 | 0.043 | 1.09 | 3730 | 16.0 | 11.0 | 33.2 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 43 | 48.8 | 0.057 | 1.12 | 20 | 9.0 | 8.0 | 30.0 |
| INV/LONG|edge=1 | 55 | 47.3 | 0.114 | 1.27 | 22 | 22.0 | 18.5 | 13.6 |
| INV/SHORT|edge=-1 | 65 | 40.0 | 0.125 | 1.25 | 32 | 22.0 | 10.75 | 21.9 |
| INV/SHORT|edge=0 | 41 | 51.2 | -0.033 | 0.93 | 18 | 11.0 | 17.0 | 38.9 |
| INV/SHORT|edge=1 | 3 | 33.3 | -0.527 | 0.21 | 2 | 8.0 | 5.0 | 0.0 |
| RETEST/LONG|edge=-1 | 212 | 47.6 | 0.043 | 1.09 | 97 | 11.0 | 7.0 | 49.5 |
| RETEST/LONG|edge=0 | 1953 | 49.4 | -0.016 | 0.97 | 933 | 13.0 | 10.0 | 39.5 |
| RETEST/LONG|edge=1 | 2149 | 43.0 | 0.058 | 1.11 | 1075 | 18.0 | 13.0 | 26.4 |
| RETEST/SHORT|edge=-1 | 1712 | 45.0 | 0.028 | 1.06 | 846 | 19.0 | 13.0 | 28.7 |
| RETEST/SHORT|edge=0 | 1396 | 47.7 | 0.119 | 1.25 | 633 | 16.0 | 10.0 | 38.4 |
| RETEST/SHORT|edge=1 | 119 | 54.6 | 0.034 | 1.08 | 51 | 13.5 | 9.0 | 54.9 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 30 | 46.7 | 0.14 | 1.34 | 11 | 19.5 | 14.5 | 9.1 |
| INV/LONG|tier=C | 72 | 48.6 | 0.089 | 1.19 | 33 | 12.0 | 13.0 | 27.3 |
| INV/SHORT|tier=B | 36 | 47.2 | 0.157 | 1.33 | 17 | 18.0 | 5.0 | 5.9 |
| INV/SHORT|tier=C | 73 | 42.5 | -0.006 | 0.99 | 35 | 16.0 | 20.0 | 37.1 |
| RETEST/LONG|tier=A+ | 330 | 26.7 | 0.132 | 1.2 | 204 | 26.0 | 16.5 | 18.1 |
| RETEST/LONG|tier=B | 1766 | 45.8 | 0.061 | 1.12 | 859 | 15.0 | 10.0 | 31.8 |
| RETEST/LONG|tier=C | 2218 | 49.2 | -0.022 | 0.95 | 1042 | 14.0 | 11.0 | 37.5 |
| RETEST/SHORT|tier=A+ | 206 | 28.2 | 0.094 | 1.14 | 134 | 34.0 | 11.75 | 22.4 |
| RETEST/SHORT|tier=B | 1416 | 47.6 | 0.032 | 1.07 | 675 | 16.0 | 11.0 | 33.0 |
| RETEST/SHORT|tier=C | 1605 | 47.9 | 0.096 | 1.21 | 721 | 18.0 | 11.0 | 36.2 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 102 | 48.0 | 0.103 | 1.23 | 44 | 13.0 | 14.0 | 22.7 |
| INV/SHORT|aligned=1 | 109 | 44.0 | 0.049 | 1.1 | 52 | 18.0 | 11.25 | 26.9 |
| RETEST/LONG|aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 4304 | 46.1 | 0.023 | 1.05 | 2104 | 14.0 | 11.0 | 33.3 |
| RETEST/SHORT|aligned=1 | 3227 | 46.5 | 0.068 | 1.14 | 1530 | 18.0 | 11.0 | 33.6 |

## Autopsia de SL
n_losses=3731  causas: RR-bajo×1413, contra-estructura×1313, stop-en-el-minimo×1239, killzone-Asia-largo×827, sin-nivel-detras×728, estirado×659, chop×519, SL-muy-pegado×449, sin-causa-clara×368, contra-sesgo×1
- INV/LONG (n=44): killzone-Asia-largo×22, RR-bajo×21, contra-estructura×13, stop-en-el-minimo×10, estirado×10, sin-nivel-detras×5, SL-muy-pegado×4, chop×3, sin-causa-clara×1
- INV/SHORT (n=52): RR-bajo×26, contra-estructura×17, stop-en-el-minimo×14, sin-causa-clara×10, estirado×9, SL-muy-pegado×7, chop×4, sin-nivel-detras×4
- RETEST/LONG (n=2105): RR-bajo×816, killzone-Asia-largo×805, contra-estructura×786, stop-en-el-minimo×701, sin-nivel-detras×414, estirado×361, chop×311, SL-muy-pegado×234, sin-causa-clara×155, contra-sesgo×1
- RETEST/SHORT (n=1530): RR-bajo×550, stop-en-el-minimo×514, contra-estructura×497, sin-nivel-detras×305, estirado×279, SL-muy-pegado×204, sin-causa-clara×202, chop×201

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
    "n": 7594,
    "naive_expR": 0.043,
    "managed_expR": 0.123,
    "delta": 0.08,
    "avgEntryBetterTk_p50": 2.7,
    "fill_t3plus_pct": 48.2,
    "fill_full_pct": 33.9,
    "m1_rate": 36.2,
    "m2_rate": 23.1,
    "m3_rate": 12.8,
    "beAfterM1_rate": 16.7
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 64,
      "naive_expR": 0.129,
      "managed_expR": 0.278,
      "delta": 0.149,
      "avgEntryBetterTk_p50": 2.0,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 39.1,
      "m1_rate": 43.8,
      "m2_rate": 31.2,
      "m3_rate": 18.8,
      "beAfterM1_rate": 17.2
    },
    "1m/INV/SHORT": {
      "n": 69,
      "naive_expR": 0.109,
      "managed_expR": 0.339,
      "delta": 0.23,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 55.1,
      "fill_full_pct": 42.0,
      "m1_rate": 37.7,
      "m2_rate": 27.5,
      "m3_rate": 17.4,
      "beAfterM1_rate": 13.0
    },
    "1m/RETEST/LONG": {
      "n": 2611,
      "naive_expR": 0.026,
      "managed_expR": 0.104,
      "delta": 0.078,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 49.3,
      "fill_full_pct": 35.0,
      "m1_rate": 34.8,
      "m2_rate": 22.0,
      "m3_rate": 11.7,
      "beAfterM1_rate": 15.7
    },
    "1m/RETEST/SHORT": {
      "n": 1968,
      "naive_expR": 0.047,
      "managed_expR": 0.159,
      "delta": 0.112,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.9,
      "fill_full_pct": 33.4,
      "m1_rate": 39.6,
      "m2_rate": 25.2,
      "m3_rate": 14.1,
      "beAfterM1_rate": 18.3
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
      "n": 33,
      "naive_expR": -0.04,
      "managed_expR": 0.023,
      "delta": 0.063,
      "avgEntryBetterTk_p50": 3.8,
      "fill_t3plus_pct": 51.5,
      "fill_full_pct": 42.4,
      "m1_rate": 27.3,
      "m2_rate": 24.2,
      "m3_rate": 15.2,
      "beAfterM1_rate": 6.1
    },
    "2m/RETEST/LONG": {
      "n": 1235,
      "naive_expR": -0.009,
      "managed_expR": 0.069,
      "delta": 0.078,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 47.3,
      "fill_full_pct": 32.1,
      "m1_rate": 33.8,
      "m2_rate": 20.7,
      "m3_rate": 11.7,
      "beAfterM1_rate": 16.9
    },
    "2m/RETEST/SHORT": {
      "n": 893,
      "naive_expR": 0.11,
      "managed_expR": 0.178,
      "delta": 0.068,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.2,
      "fill_full_pct": 36.6,
      "m1_rate": 38.1,
      "m2_rate": 25.5,
      "m3_rate": 14.2,
      "beAfterM1_rate": 17.1
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
      "n": 392,
      "naive_expR": 0.104,
      "managed_expR": 0.057,
      "delta": -0.047,
      "avgEntryBetterTk_p50": 2.7,
      "fill_t3plus_pct": 38.3,
      "fill_full_pct": 27.6,
      "m1_rate": 32.1,
      "m2_rate": 20.7,
      "m3_rate": 11.5,
      "beAfterM1_rate": 16.3
    },
    "5m/RETEST/SHORT": {
      "n": 288,
      "naive_expR": 0.083,
      "managed_expR": 0.146,
      "delta": 0.064,
      "avgEntryBetterTk_p50": 4.8,
      "fill_t3plus_pct": 46.5,
      "fill_full_pct": 30.2,
      "m1_rate": 36.8,
      "m2_rate": 23.6,
      "m3_rate": 13.5,
      "beAfterM1_rate": 17.0
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 6461,
    "layer_expR": 0.055,
    "orig_expR": 0.196,
    "delta_orig_minus_layer": 0.141,
    "delta_ci90": [
      0.089,
      0.196
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 47.0,
    "orig_wrTP1": 32.9,
    "slTk_p50": 19.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.8,
    "orig_saved_from_SL": 12,
    "orig_caused_SL": 924
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 195,
      "layer_expR": 0.072,
      "orig_expR": 0.253,
      "delta_orig_minus_layer": 0.181,
      "delta_ci90": [
        -0.175,
        0.638
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 45.6,
      "orig_wrTP1": 25.1,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 3.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 40
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
      "n": 4834,
      "layer_expR": 0.047,
      "orig_expR": 0.189,
      "delta_orig_minus_layer": 0.143,
      "delta_ci90": [
        0.087,
        0.201
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.5,
      "orig_wrTP1": 33.8,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 12,
      "orig_caused_SL": 675
    },
    "retestBar2": {
      "n": 1432,
      "layer_expR": 0.081,
      "orig_expR": 0.211,
      "delta_orig_minus_layer": 0.13,
      "delta_ci90": [
        0.012,
        0.256
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.7,
      "orig_wrTP1": 31.1,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 2.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 209
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 64,
      "layer_expR": 0.129,
      "orig_expR": 0.09,
      "delta_orig_minus_layer": -0.039,
      "delta_ci90": [
        -0.482,
        0.455
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 45.3,
      "orig_wrTP1": 23.4,
      "slTk_p50": 15.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 4.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 14
    },
    "1m/INV/SHORT": {
      "n": 59,
      "layer_expR": 0.118,
      "orig_expR": 0.467,
      "delta_orig_minus_layer": 0.349,
      "delta_ci90": [
        -0.547,
        1.441
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.5,
      "orig_wrTP1": 23.7,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 1.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 14
    },
    "1m/RETEST/LONG": {
      "n": 2231,
      "layer_expR": 0.032,
      "orig_expR": 0.183,
      "delta_orig_minus_layer": 0.152,
      "delta_ci90": [
        0.069,
        0.238
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.7,
      "orig_wrTP1": 29.8,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.3,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 334
    },
    "1m/RETEST/SHORT": {
      "n": 1560,
      "layer_expR": 0.068,
      "orig_expR": 0.207,
      "delta_orig_minus_layer": 0.139,
      "delta_ci90": [
        0.022,
        0.256
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.4,
      "orig_wrTP1": 30.9,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 2.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 227
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
      "n": 32,
      "layer_expR": -0.054,
      "orig_expR": 0.067,
      "delta_orig_minus_layer": 0.121,
      "delta_ci90": [
        -0.142,
        0.372
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 31.2,
      "orig_wrTP1": 25.0,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 4.5,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 2
    },
    "2m/RETEST/LONG": {
      "n": 1116,
      "layer_expR": 0.009,
      "orig_expR": 0.027,
      "delta_orig_minus_layer": 0.019,
      "delta_ci90": [
        -0.057,
        0.104
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.0,
      "orig_wrTP1": 34.1,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 155
    },
    "2m/RETEST/SHORT": {
      "n": 729,
      "layer_expR": 0.142,
      "orig_expR": 0.252,
      "delta_orig_minus_layer": 0.11,
      "delta_ci90": [
        -0.001,
        0.224
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 51.0,
      "orig_wrTP1": 35.9,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.2,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 111
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
      "n": 378,
      "layer_expR": 0.096,
      "orig_expR": 0.284,
      "delta_orig_minus_layer": 0.187,
      "delta_ci90": [
        0.028,
        0.363
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.8,
      "orig_wrTP1": 46.3,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 14.0,
      "orig_wider_pct": 15.3,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 35
    },
    "5m/RETEST/SHORT": {
      "n": 252,
      "layer_expR": 0.066,
      "orig_expR": 0.654,
      "delta_orig_minus_layer": 0.588,
      "delta_ci90": [
        0.146,
        1.133
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.2,
      "orig_wrTP1": 44.8,
      "slTk_p50": 27.0,
      "slOrigTk_p50": 21.0,
      "orig_wider_pct": 19.4,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 22
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 3179,
    "wrTP1": 44.7,
    "expR": -0.018
  },
  "2026-W37": {
    "n": 4573,
    "wrTP1": 47.4,
    "expR": 0.084
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 7318,
  "brier": 0.2237,
  "bias": -0.116,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.099
    },
    {
      "feature": "stretchAtr",
      "weight": -0.147
    },
    {
      "feature": "rvol",
      "weight": 0.079
    },
    {
      "feature": "biasScore",
      "weight": -0.072
    },
    {
      "feature": "nearTk",
      "weight": -0.066
    },
    {
      "feature": "chopIdx",
      "weight": -0.059
    },
    {
      "feature": "nearEdge",
      "weight": 0.041
    },
    {
      "feature": "structDir",
      "weight": 0.039
    },
    {
      "feature": "aligned",
      "weight": -0.034
    },
    {
      "feature": "hourNY",
      "weight": 0.016
    },
    {
      "feature": "emaStack",
      "weight": -0.013
    },
    {
      "feature": "atrPctUsed",
      "weight": 0.008
    },
    {
      "feature": "entryZoneTk",
      "weight": 0.002
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.162,
      "actual": 0.207,
      "n": 731
    },
    {
      "bin": 1,
      "pred": 0.346,
      "actual": 0.301,
      "n": 732
    },
    {
      "bin": 2,
      "pred": 0.425,
      "actual": 0.331,
      "n": 732
    },
    {
      "bin": 3,
      "pred": 0.475,
      "actual": 0.388,
      "n": 732
    },
    {
      "bin": 4,
      "pred": 0.514,
      "actual": 0.462,
      "n": 732
    },
    {
      "bin": 5,
      "pred": 0.546,
      "actual": 0.547,
      "n": 731
    },
    {
      "bin": 6,
      "pred": 0.571,
      "actual": 0.604,
      "n": 732
    },
    {
      "bin": 7,
      "pred": 0.594,
      "actual": 0.626,
      "n": 732
    },
    {
      "bin": 8,
      "pred": 0.617,
      "actual": 0.71,
      "n": 732
    },
    {
      "bin": 9,
      "pred": 0.66,
      "actual": 0.727,
      "n": 732
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
    "expR": 0.129,
    "ci90": [
      -0.138,
      0.414
    ],
    "p_mean_le_0": 0.231,
    "n": 64,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.109,
    "ci90": [
      -0.141,
      0.377
    ],
    "p_mean_le_0": 0.244,
    "n": 69,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.026,
    "ci90": [
      -0.015,
      0.068
    ],
    "p_mean_le_0": 0.155,
    "n": 2615,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.046,
    "ci90": [
      0.001,
      0.095
    ],
    "p_mean_le_0": 0.044,
    "n": 1975,
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
    "expR": -0.04,
    "ci90": [
      -0.391,
      0.395
    ],
    "p_mean_le_0": 0.589,
    "n": 33,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.008,
    "ci90": [
      -0.064,
      0.046
    ],
    "p_mean_le_0": 0.598,
    "n": 1237,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.11,
    "ci90": [
      0.04,
      0.18
    ],
    "p_mean_le_0": 0.004,
    "n": 893,
    "survives_fdr10": true
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
    "expR": 0.104,
    "ci90": [
      0.006,
      0.202
    ],
    "p_mean_le_0": 0.038,
    "n": 392,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": 0.084,
    "ci90": [
      -0.031,
      0.211
    ],
    "p_mean_le_0": 0.128,
    "n": 289,
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
      "n": 2277,
      "wrTP1": 45.8,
      "expR": 0.083,
      "pf": 1.17,
      "defining_features": {
        "biasScore": -1.03,
        "emaStack": -0.89,
        "nearEdge": -0.79,
        "structDir": -0.43
      }
    },
    {
      "id": 1,
      "n": 3336,
      "wrTP1": 45.9,
      "expR": 0.047,
      "pf": 1.09,
      "defining_features": {
        "biasScore": 0.85,
        "emaStack": 0.78,
        "nearEdge": 0.66,
        "structDir": 0.4
      }
    },
    {
      "id": 2,
      "n": 1227,
      "wrTP1": 51.0,
      "expR": 0.039,
      "pf": 1.09,
      "defining_features": {
        "hourNY": 1.27,
        "atrPctUsed": -0.78,
        "emaStack": -0.5,
        "biasScore": -0.49
      }
    },
    {
      "id": 0,
      "n": 912,
      "wrTP1": 42.5,
      "expR": -0.064,
      "pf": 0.88,
      "defining_features": {
        "stretchAtr": 1.72,
        "rvol": 1.52,
        "chopIdx": -1.34,
        "hourNY": -0.25
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
        "n": 21,
        "wrTP1": 52.4,
        "expR": 0.4
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
    "expR_spread": 0.834,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 49,
        "wrTP1": 44.9,
        "expR": 0.085
      },
      "NQ": {
        "n": 8,
        "wrTP1": 50.0,
        "expR": 0.027
      },
      "ES": {
        "n": 5,
        "wrTP1": 60.0,
        "expR": 0.354
      },
      "GC": {
        "n": 9,
        "wrTP1": 55.6,
        "expR": 0.168
      }
    },
    "expR_spread": 0.327,
    "verdict": "universal"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 481,
        "wrTP1": 45.5,
        "expR": 0.108
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
        "n": 824,
        "wrTP1": 45.4,
        "expR": 0.027
      },
      "YM": {
        "n": 315,
        "wrTP1": 41.9,
        "expR": 0.101
      }
    },
    "expR_spread": 0.162,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 268,
        "wrTP1": 42.2,
        "expR": 0.129
      },
      "GC": {
        "n": 412,
        "wrTP1": 47.3,
        "expR": 0.091
      },
      "YM": {
        "n": 744,
        "wrTP1": 45.7,
        "expR": 0.083
      },
      "ES": {
        "n": 554,
        "wrTP1": 43.9,
        "expR": -0.03
      },
      "CL": {
        "n": 43,
        "wrTP1": 27.9,
        "expR": -0.547
      }
    },
    "expR_spread": 0.676,
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
        "n": 20,
        "wrTP1": 35.0,
        "expR": 0.126
      },
      "NQ": {
        "n": 3,
        "wrTP1": 33.3,
        "expR": -0.567
      },
      "ES": {
        "n": 5,
        "wrTP1": 40.0,
        "expR": -0.072
      },
      "GC": {
        "n": 5,
        "wrTP1": 20.0,
        "expR": -0.352
      }
    },
    "expR_spread": 0.693,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 288,
        "wrTP1": 47.6,
        "expR": -0.044
      },
      "GC": {
        "n": 173,
        "wrTP1": 45.7,
        "expR": 0.027
      },
      "CL": {
        "n": 394,
        "wrTP1": 51.3,
        "expR": 0.071
      },
      "ES": {
        "n": 236,
        "wrTP1": 46.2,
        "expR": -0.057
      },
      "YM": {
        "n": 163,
        "wrTP1": 38.7,
        "expR": -0.102
      }
    },
    "expR_spread": 0.173,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 220,
        "wrTP1": 50.9,
        "expR": 0.087
      },
      "YM": {
        "n": 365,
        "wrTP1": 50.7,
        "expR": 0.143
      },
      "GC": {
        "n": 166,
        "wrTP1": 48.8,
        "expR": 0.088
      },
      "NQ": {
        "n": 137,
        "wrTP1": 44.5,
        "expR": 0.165
      },
      "CL": {
        "n": 20,
        "wrTP1": 35.0,
        "expR": -0.422
      }
    },
    "expR_spread": 0.587,
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
        "n": 63,
        "wrTP1": 46.0,
        "expR": -0.016
      },
      "CL": {
        "n": 127,
        "wrTP1": 61.4,
        "expR": 0.309
      },
      "NQ": {
        "n": 126,
        "wrTP1": 48.4,
        "expR": -0.097
      }
    },
    "expR_spread": 0.406,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 57,
        "wrTP1": 50.9,
        "expR": -0.011
      },
      "ES": {
        "n": 79,
        "wrTP1": 59.5,
        "expR": 0.188
      },
      "GC": {
        "n": 54,
        "wrTP1": 37.0,
        "expR": -0.107
      },
      "YM": {
        "n": 100,
        "wrTP1": 52.0,
        "expR": 0.19
      },
      "CL": {
        "n": 8,
        "wrTP1": 50.0,
        "expR": -0.239
      }
    },
    "expR_spread": 0.429,
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
    "n": 40,
    "wrTP1": 60.0,
    "nSL": 8,
    "nTO": 8,
    "expR": 1.954,
    "pf": 10.77,
    "mfe_p25": 32.25,
    "mfe_p50": 88.0,
    "mfe_p75": 174.0,
    "winnerMAE_p75": 15.0,
    "winnerMAE_p90": 30.799999999999997,
    "loserMFEbeforeSL_p50": 14.0,
    "bars_win_p50": 4.0,
    "bars_loss_p50": 9.5,
    "entryZoneTk_p50": -27.0,
    "revAfterSL_rate": 25.0
  },
  "away_from_news": {
    "n": 7712,
    "wrTP1": 46.2,
    "nSL": 3723,
    "nTO": 426,
    "expR": 0.033,
    "pf": 1.07,
    "mfe_p25": 7.0,
    "mfe_p50": 16.0,
    "mfe_p75": 38.0,
    "winnerMAE_p75": 11.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -12.0,
    "revAfterSL_rate": 33.2
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
    "beforeN": 7541,
    "afterN": 0,
    "before": {
      "n": 7541,
      "wrTP1": 46.3,
      "nSL": 3635,
      "nTO": 416,
      "expR": 0.042,
      "pf": 1.09,
      "mfe_p25": 7.0,
      "mfe_p50": 16.0,
      "mfe_p75": 38.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 33.4
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
    "session": "ny",
    "runType": "pre-ny",
    "generatedAt": "2026-09-11T07:55:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "NQ",
    "focus": {
      "sym": "NQ",
      "verdict": "WAIT",
      "window": "08:30-11:00 CT",
      "setup": {
        "es": "probando el techo del cluster VAH/FVG 29359-29363 tras romper el IB al alza -- si confirma, la entrada real es el retroceso a 29309-29333 (EMA20/EMA50/VAH)",
        "en": "testing the top of the VAH/FVG 29359-29363 cluster after breaking the IB up -- if it confirms, the real entry is the pullback to 29309-29333 (EMA20/EMA50/VAH)"
      },
      "trigger": {
        "es": "cierre 5m sostenido sobre 29363 con seguimiento primero; luego, en el retroceso, cierre 5m de vuelta sobre 29309",
        "en": "a sustained 5m close above 29363 with follow-through first; then, on the pullback, a 5m close back above 29309"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 29278 devuelve todo el cluster y reabre el corto hacia el PDL 29043.25",
        "en": "a sustained 5m close below 29278 gives back the whole cluster and reopens the short toward the PDL 29043.25"
      },
      "note": {
        "es": "todo el complejo (NQ/ES/YM) esta probando el mismo tipo de techo a la vez tras el CPI de las 07:30 CT -- no persigas el toque, el dia ya gasto 82-95% de su presupuesto de rango; espera el retroceso",
        "en": "the whole complex (NQ/ES/YM) is testing the same kind of ceiling at once after the 07:30 CT CPI -- don't chase the touch, the day has already burned 82-95% of its range budget; wait for the pullback"
      }
    },
    "summary": {
      "es": [
        "El CPI de EEUU (07:30 CT, 25 min antes de esta corrida) desato una ruptura de todo el complejo de indices: NQ, ES e YM rompieron su Initial Balance al alza y prueban el techo de sus respectivos clusters de decision a la vez -- pero los 3 ya gastaron 81-95% de su presupuesto de rango, sin margen para perseguir.",
        "NQ WAIT: GIRA el sesgo a LARGO (marco diario volteo a +1, alineado con el semanal), probando el techo 29359-29363 sin cierre confirmado -- espera el retroceso a 29309-29333.",
        "ES WAIT: tambien GIRA a LARGO, pero literalmente a 1.5pts de romper su propia tesis bajista de 3 dias (7648) con solo 7.25pts de ATR restante -- sin margen para forzar nada.",
        "GC WAIT: el mas mixto del complejo, 1h/4h confirman alcista pero command fusiona NEUTRAL/DEBIL sin permiso de entrada; su zona de venta 4432-4453 queda fuera de alcance esta sesion.",
        "YM WAIT: unico indice que NO volteo su marco diario -- roza el maximo overnight 52500 tras 14 toques sin un solo reclamo, mantiene el corto de fondo degradado en vez de girar como NQ/ES.",
        "CL WAIT: confirmo la ruptura de su propia tesis larga (perdio 100.04) tras el giro violento de Londres -- dia ya al 145% de su ATR normal, reinicio bajista candidato, sin presupuesto para
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 2694,
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
      "n": 1520,
      "wrTP1": 48.9,
      "nSL": 684,
      "nTO": 93,
      "expR": 0.081,
      "pf": 1.18,
      "mfe_p25": 8.0,
      "mfe_p50": 20.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 30.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 37.1
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
      "expR": 0.081,
      "ci90": [
        0.029,
        0.133
      ],
      "p_mean_le_0": 0.004,
      "n": 1490
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
      "n": 1785,
      "wrTP1": 48.9,
      "nSL": 814,
      "nTO": 98,
      "expR": 0.072,
      "pf": 1.16,
      "mfe_p25": 8.0,
      "mfe_p50": 20.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 29.0,
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
      "expR": 0.072,
      "ci90": [
        0.026,
        0.122
      ],
      "p_mean_le_0": 0.003,
      "n": 1754
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "WAIT": {
        "n": 20,
        "wrTP1": 55.0,
        "nSL": 8,
        "nTO": 1,
        "expR": 0.154,
        "pf": 1.39,
        "mfe_p25": 15.25,
        "mfe_p50": 38.5,
        "mfe_p75": 53.5,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 0.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -16.5,
        "revAfterSL_rate": 37.5
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
        "n": 780,
        "wrTP1": 52.1,
        "nSL": 327,
        "nTO": 47,
        "expR": 0.191,
        "pf": 1.45,
        "mfe_p25": 8.0,
        "mfe_p50": 23.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 39.4
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
        "n": 701,
        "wrTP1": 45.2,
        "nSL": 340,
        "nTO": 44,
        "expR": -0.04,
        "pf": 0.92,
        "mfe_p25": 7.0,
        "mfe_p50": 17.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 34.7
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```
