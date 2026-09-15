# Scalp CC · report 2026-09-15T01:26Z
- signals=9458 outcomes=9179 pares_resueltos=9303 pendientes=155 huerfanos=26

## ⚠ ALERTAS (llevar al frente del resumen)
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.192 vs 0.046, delta 0.146 CI90 [0.096, 0.202], n 5794). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.193 vs 0.075, delta 0.118 CI90 [0.017, 0.225], n 1827). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.079 CI90 [0.03, 0.127], n 1557). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.045, "ci90": [0.024, 0.067], "p_mean_le_0": 0.0, "n": 9153}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 84 | 45.2 | 0.133 | 1.28 | 37 | 16.0 | 10.75 | 21.6 |
| 1m/INV/SHORT | 81 | 49.4 | 0.116 | 1.26 | 36 | 21.0 | 11.25 | 19.4 |
| 1m/RETEST/LONG | 3172 | 44.6 | 0.024 | 1.05 | 1563 | 14.0 | 10.0 | 28.5 |
| 1m/RETEST/SHORT | 2460 | 46.3 | 0.055 | 1.11 | 1171 | 17.0 | 12.0 | 32.7 |
| 2m/INV/LONG | 29 | 48.3 | -0.159 | 0.68 | 14 | 9.0 | 8.0 | 28.6 |
| 2m/INV/SHORT | 39 | 35.9 | 0.017 | 1.03 | 21 | 21.0 | 15.75 | 38.1 |
| 2m/RETEST/LONG | 1468 | 46.5 | -0.017 | 0.97 | 732 | 17.0 | 13.0 | 35.8 |
| 2m/RETEST/SHORT | 1078 | 49.9 | 0.089 | 1.19 | 493 | 21.0 | 12.75 | 41.0 |
| 5m/INV/LONG | 10 | 90.0 | 0.849 | 99.0 | 0 | 30.0 | 32.0 | None |
| 5m/INV/SHORT | 8 | 75.0 | 0.615 | 3.46 | 2 | 58.0 | 68.75 | 100.0 |
| 5m/RETEST/LONG | 523 | 53.2 | 0.155 | 1.35 | 227 | 25.0 | 18.75 | 48.0 |
| 5m/RETEST/SHORT | 351 | 51.6 | 0.077 | 1.17 | 155 | 30.5 | 21.0 | 39.4 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 638 | 27.3 | 0.098 | 1.15 | 404 | 28.0 | 15.0 | 19.3 |
| B | 3905 | 47.4 | 0.054 | 1.11 | 1853 | 17.0 | 12.0 | 33.3 |
| C | 4760 | 48.9 | 0.031 | 1.07 | 2194 | 16.0 | 12.0 | 36.3 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 3544 | 49.6 | 0.071 | 1.15 | 1605 | 12.0 | 9.0 | 39.0 |
| London | 1435 | 45.2 | -0.047 | 0.91 | 747 | 18.0 | 12.0 | 31.5 |
| NY | 1530 | 47.5 | 0.159 | 1.33 | 717 | 25.0 | 17.0 | 38.9 |
| Sin KZ | 2794 | 43.8 | -0.002 | 1.0 | 1382 | 18.0 | 13.0 | 25.4 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 2407 | 47.1 | 0.055 | 1.11 | 1146 | 21.0 | 14.0 | 32.5 |
| edge=0 | 4100 | 48.8 | 0.035 | 1.07 | 1923 | 14.0 | 10.0 | 38.2 |
| edge=1 | 2796 | 43.6 | 0.052 | 1.1 | 1382 | 18.0 | 13.0 | 27.9 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 9293 | 46.8 | 0.045 | 1.09 | 4450 | 17.0 | 12.0 | 33.5 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 54 | 51.9 | 0.068 | 1.15 | 24 | 10.0 | 9.25 | 29.2 |
| INV/LONG|edge=1 | 65 | 47.7 | 0.146 | 1.36 | 25 | 23.0 | 17.0 | 16.0 |
| INV/SHORT|edge=-1 | 75 | 41.3 | 0.133 | 1.27 | 37 | 24.0 | 12.0 | 27.0 |
| INV/SHORT|edge=0 | 45 | 51.1 | -0.056 | 0.88 | 20 | 11.0 | 20.0 | 35.0 |
| INV/SHORT|edge=1 | 8 | 75.0 | 0.901 | 4.6 | 2 | 32.5 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 240 | 52.1 | 0.123 | 1.29 | 101 | 13.0 | 8.0 | 48.5 |
| RETEST/LONG|edge=0 | 2326 | 48.9 | -0.011 | 0.98 | 1121 | 14.0 | 11.0 | 37.2 |
| RETEST/LONG|edge=1 | 2597 | 42.9 | 0.049 | 1.1 | 1300 | 18.0 | 13.0 | 26.9 |
| RETEST/SHORT|edge=-1 | 2088 | 46.7 | 0.043 | 1.09 | 1006 | 22.0 | 15.0 | 31.0 |
| RETEST/SHORT|edge=0 | 1675 | 48.6 | 0.101 | 1.22 | 758 | 17.0 | 10.0 | 40.0 |
| RETEST/SHORT|edge=1 | 126 | 53.2 | 0.005 | 1.01 | 55 | 14.0 | 9.0 | 56.4 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 31 | 41.9 | 0.106 | 1.23 | 13 | 22.0 | 17.0 | 15.4 |
| INV/LONG|tier=C | 92 | 52.2 | 0.127 | 1.3 | 38 | 15.0 | 12.0 | 26.3 |
| INV/SHORT|tier=B | 39 | 46.2 | 0.162 | 1.33 | 19 | 19.0 | 8.75 | 10.5 |
| INV/SHORT|tier=C | 89 | 47.2 | 0.097 | 1.21 | 40 | 25.0 | 28.0 | 37.5 |
| RETEST/LONG|tier=A+ | 383 | 26.1 | 0.076 | 1.12 | 241 | 22.5 | 15.0 | 17.0 |
| RETEST/LONG|tier=B | 2124 | 45.8 | 0.059 | 1.12 | 1028 | 15.0 | 11.0 | 32.2 |
| RETEST/LONG|tier=C | 2656 | 49.1 | -0.008 | 0.98 | 1253 | 15.0 | 12.0 | 35.4 |
| RETEST/SHORT|tier=A+ | 255 | 29.0 | 0.13 | 1.2 | 163 | 39.5 | 17.25 | 22.7 |
| RETEST/SHORT|tier=B | 1711 | 49.4 | 0.045 | 1.09 | 793 | 18.0 | 13.0 | 35.6 |
| RETEST/SHORT|tier=C | 1923 | 48.7 | 0.078 | 1.17 | 863 | 18.0 | 12.0 | 37.9 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 123 | 49.6 | 0.122 | 1.28 | 51 | 17.5 | 14.0 | 23.5 |
| INV/SHORT|aligned=1 | 128 | 46.9 | 0.117 | 1.25 | 59 | 22.0 | 17.75 | 28.8 |
| RETEST/LONG|aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 5153 | 46.0 | 0.025 | 1.05 | 2521 | 15.0 | 11.0 | 32.4 |
| RETEST/SHORT|aligned=1 | 3889 | 47.8 | 0.067 | 1.14 | 1819 | 19.0 | 13.0 | 35.5 |

## Autopsia de SL
n_losses=4451  causas: RR-bajo×1701, contra-estructura×1551, stop-en-el-minimo×1491, killzone-Asia-largo×901, sin-nivel-detras×872, estirado×769, chop×636, SL-muy-pegado×553, sin-causa-clara×434, contra-sesgo×1
- INV/LONG (n=51): killzone-Asia-largo×25, RR-bajo×22, contra-estructura×14, estirado×13, stop-en-el-minimo×12, SL-muy-pegado×7, sin-nivel-detras×7, chop×5, sin-causa-clara×1
- INV/SHORT (n=59): RR-bajo×30, contra-estructura×18, stop-en-el-minimo×17, estirado×12, sin-causa-clara×11, SL-muy-pegado×8, chop×5, sin-nivel-detras×4
- RETEST/LONG (n=2522): RR-bajo×961, contra-estructura×933, killzone-Asia-largo×876, stop-en-el-minimo×816, sin-nivel-detras×523, estirado×419, chop×385, SL-muy-pegado×306, sin-causa-clara×193, contra-sesgo×1
- RETEST/SHORT (n=1819): RR-bajo×688, stop-en-el-minimo×646, contra-estructura×586, sin-nivel-detras×338, estirado×325, chop×241, SL-muy-pegado×232, sin-causa-clara×229

## Autopsia de SL · semana 2026-W38 (para revision semanal)
n_losses=341  causas: RR-bajo×140, stop-en-el-minimo×123, contra-estructura×117, sin-nivel-detras×63, estirado×62, killzone-Asia-largo×58, chop×46, SL-muy-pegado×39, sin-causa-clara×33
ejemplos por causa: {"RR-bajo": ["NQ-5-20749-L", "CL-5-20795-L", "NQ-5-21912-S", "GC-1-34473-S", "GC-2-27588-S"], "stop-en-el-minimo": ["NQ-5-20749-L", "NQ-5-21912-S", "GC-1-34473-S", "GC-2-27588-S", "GC-1-34476-S"], "contra-estructura": ["NQ-1-21696-L", "CL-5-20795-L", "ES-5-20579-S", "GC-1-34473-S", "GC-2-27588-S"]}

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
    "n": 9139,
    "naive_expR": 0.045,
    "managed_expR": 0.128,
    "delta": 0.083,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 47.8,
    "fill_full_pct": 33.7,
    "m1_rate": 36.8,
    "m2_rate": 23.2,
    "m3_rate": 12.5,
    "beAfterM1_rate": 17.5
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 81,
      "naive_expR": 0.133,
      "managed_expR": 0.313,
      "delta": 0.18,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 45.7,
      "fill_full_pct": 33.3,
      "m1_rate": 48.1,
      "m2_rate": 30.9,
      "m3_rate": 16.0,
      "beAfterM1_rate": 24.7
    },
    "1m/INV/SHORT": {
      "n": 79,
      "naive_expR": 0.116,
      "managed_expR": 0.311,
      "delta": 0.195,
      "avgEntryBetterTk_p50": 3.2,
      "fill_t3plus_pct": 53.2,
      "fill_full_pct": 40.5,
      "m1_rate": 39.2,
      "m2_rate": 25.3,
      "m3_rate": 15.2,
      "beAfterM1_rate": 17.7
    },
    "1m/RETEST/LONG": {
      "n": 3121,
      "naive_expR": 0.023,
      "managed_expR": 0.113,
      "delta": 0.09,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 49.2,
      "fill_full_pct": 35.4,
      "m1_rate": 35.8,
      "m2_rate": 22.4,
      "m3_rate": 11.6,
      "beAfterM1_rate": 16.6
    },
    "1m/RETEST/SHORT": {
      "n": 2407,
      "naive_expR": 0.056,
      "managed_expR": 0.169,
      "delta": 0.113,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 49.0,
      "fill_full_pct": 33.7,
      "m1_rate": 40.3,
      "m2_rate": 25.1,
      "m3_rate": 14.0,
      "beAfterM1_rate": 19.0
    },
    "2m/INV/LONG": {
      "n": 29,
      "naive_expR": -0.159,
      "managed_expR": -0.153,
      "delta": 0.006,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 51.7,
      "fill_full_pct": 34.5,
      "m1_rate": 17.2,
      "m2_rate": 17.2,
      "m3_rate": 0.0,
      "beAfterM1_rate": 3.4
    },
    "2m/INV/SHORT": {
      "n": 39,
      "naive_expR": 0.017,
      "managed_expR": -0.044,
      "delta": -0.061,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 46.2,
      "fill_full_pct": 38.5,
      "m1_rate": 25.6,
      "m2_rate": 23.1,
      "m3_rate": 12.8,
      "beAfterM1_rate": 5.1
    },
    "2m/RETEST/LONG": {
      "n": 1449,
      "naive_expR": -0.018,
      "managed_expR": 0.063,
      "delta": 0.08,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 46.1,
      "fill_full_pct": 31.2,
      "m1_rate": 34.0,
      "m2_rate": 20.6,
      "m3_rate": 11.4,
      "beAfterM1_rate": 17.0
    },
    "2m/RETEST/SHORT": {
      "n": 1063,
      "naive_expR": 0.089,
      "managed_expR": 0.155,
      "delta": 0.066,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 48.6,
      "fill_full_pct": 35.7,
      "m1_rate": 36.9,
      "m2_rate": 24.1,
      "m3_rate": 12.7,
      "beAfterM1_rate": 17.4
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
      "n": 8,
      "naive_expR": 0.615,
      "managed_expR": 0.657,
      "delta": 0.042,
      "avgEntryBetterTk_p50": 8.4,
      "fill_t3plus_pct": 62.5,
      "fill_full_pct": 37.5,
      "m1_rate": 37.5,
      "m2_rate": 25.0,
      "m3_rate": 25.0,
      "beAfterM1_rate": 12.5
    },
    "5m/RETEST/LONG": {
      "n": 512,
      "naive_expR": 0.155,
      "managed_expR": 0.102,
      "delta": -0.053,
      "avgEntryBetterTk_p50": 2.7,
      "fill_t3plus_pct": 36.9,
      "fill_full_pct": 26.6,
      "m1_rate": 34.6,
      "m2_rate": 23.4,
      "m3_rate": 13.5,
      "beAfterM1_rate": 18.4
    },
    "5m/RETEST/SHORT": {
      "n": 341,
      "naive_expR": 0.076,
      "managed_expR": 0.137,
      "delta": 0.061,
      "avgEntryBetterTk_p50": 5.0,
      "fill_t3plus_pct": 47.5,
      "fill_full_pct": 30.5,
      "m1_rate": 34.9,
      "m2_rate": 22.6,
      "m3_rate": 12.9,
      "beAfterM1_rate": 16.1
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 7855,
    "layer_expR": 0.055,
    "orig_expR": 0.193,
    "delta_orig_minus_layer": 0.138,
    "delta_ci90": [
      0.09,
      0.187
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 47.4,
    "orig_wrTP1": 32.9,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.9,
    "orig_saved_from_SL": 15,
    "orig_caused_SL": 1161
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 234,
      "layer_expR": 0.119,
      "orig_expR": 0.223,
      "delta_orig_minus_layer": 0.104,
      "delta_ci90": [
        -0.21,
        0.467
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.3,
      "orig_wrTP1": 27.8,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 8.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 49
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
      "n": 5794,
      "layer_expR": 0.046,
      "orig_expR": 0.192,
      "delta_orig_minus_layer": 0.146,
      "delta_ci90": [
        0.096,
        0.202
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.6,
      "orig_wrTP1": 33.3,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.2,
      "orig_saved_from_SL": 13,
      "orig_caused_SL": 840
    },
    "retestBar2": {
      "n": 1827,
      "layer_expR": 0.075,
      "orig_expR": 0.193,
      "delta_orig_minus_layer": 0.118,
      "delta_ci90": [
        0.017,
        0.225
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.9,
      "orig_wrTP1": 32.1,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 272
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 81,
      "layer_expR": 0.133,
      "orig_expR": -0.031,
      "delta_orig_minus_layer": -0.164,
      "delta_ci90": [
        -0.529,
        0.227
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 46.9,
      "orig_wrTP1": 22.2,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 7.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 20
    },
    "1m/INV/SHORT": {
      "n": 69,
      "layer_expR": 0.125,
      "orig_expR": 0.336,
      "delta_orig_minus_layer": 0.21,
      "delta_ci90": [
        -0.509,
        1.143
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.3,
      "orig_wrTP1": 24.6,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 4.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 17
    },
    "1m/RETEST/LONG": {
      "n": 2676,
      "layer_expR": 0.03,
      "orig_expR": 0.171,
      "delta_orig_minus_layer": 0.141,
      "delta_ci90": [
        0.063,
        0.224
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.7,
      "orig_wrTP1": 28.6,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.2,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 432
    },
    "1m/RETEST/SHORT": {
      "n": 1955,
      "layer_expR": 0.065,
      "orig_expR": 0.191,
      "delta_orig_minus_layer": 0.126,
      "delta_ci90": [
        0.034,
        0.226
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.6,
      "orig_wrTP1": 31.9,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 290
    },
    "2m/INV/LONG": {
      "n": 29,
      "layer_expR": -0.159,
      "orig_expR": 0.75,
      "delta_orig_minus_layer": 0.909,
      "delta_ci90": [
        -0.027,
        2.134
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.3,
      "orig_wrTP1": 34.5,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 13.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 4
    },
    "2m/INV/SHORT": {
      "n": 38,
      "layer_expR": 0.006,
      "orig_expR": 0.417,
      "delta_orig_minus_layer": 0.411,
      "delta_ci90": [
        -0.059,
        1.034
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 34.2,
      "orig_wrTP1": 31.6,
      "slTk_p50": 23.5,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 5.3,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 2
    },
    "2m/RETEST/LONG": {
      "n": 1306,
      "layer_expR": 0.007,
      "orig_expR": 0.039,
      "delta_orig_minus_layer": 0.032,
      "delta_ci90": [
        -0.043,
        0.106
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.9,
      "orig_wrTP1": 34.2,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.3,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 181
    },
    "2m/RETEST/SHORT": {
      "n": 890,
      "layer_expR": 0.106,
      "orig_expR": 0.222,
      "delta_orig_minus_layer": 0.117,
      "delta_ci90": [
        0.014,
        0.223
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.2,
      "orig_wrTP1": 36.4,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 2.8,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 133
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
    "5m/INV/SHORT": {
      "n": 7,
      "layer_expR": 0.629,
      "orig_expR": -0.193,
      "delta_orig_minus_layer": -0.821,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 71.4,
      "orig_wrTP1": 57.1,
      "slTk_p50": 46.0,
      "slOrigTk_p50": 88.0,
      "orig_wider_pct": 42.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 1
    },
    "5m/RETEST/LONG": {
      "n": 489,
      "layer_expR": 0.155,
      "orig_expR": 0.401,
      "delta_orig_minus_layer": 0.246,
      "delta_ci90": [
        0.055,
        0.471
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.4,
      "orig_wrTP1": 45.4,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 14.0,
      "orig_wider_pct": 17.0,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 47
    },
    "5m/RETEST/SHORT": {
      "n": 305,
      "layer_expR": 0.062,
      "orig_expR": 0.623,
      "delta_orig_minus_layer": 0.561,
      "delta_ci90": [
        0.163,
        1.074
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.8,
      "orig_wrTP1": 44.3,
      "slTk_p50": 30.0,
      "slOrigTk_p50": 23.0,
      "orig_wider_pct": 19.0,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 29
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
    "expR": -0.016
  },
  "2026-W37": {
    "n": 5376,
    "wrTP1": 46.9,
    "expR": 0.071
  },
  "2026-W38": {
    "n": 787,
    "wrTP1": 54.4,
    "expR": 0.104
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 38,
      "wrTP1": 44.7,
      "expR": 0.278,
      "pf": 1.59
    },
    "1m/INV/SHORT": {
      "n": 19,
      "wrTP1": 68.4,
      "expR": 0.264,
      "pf": 1.95
    },
    "1m/RETEST/LONG": {
      "n": 1370,
      "wrTP1": 42.9,
      "expR": -0.012,
      "pf": 0.98
    },
    "1m/RETEST/SHORT": {
      "n": 449,
      "wrTP1": 43.7,
      "expR": -0.002,
      "pf": 1.0
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
      "n": 684,
      "wrTP1": 46.1,
      "expR": -0.062,
      "pf": 0.88
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
      "n": 243,
      "wrTP1": 52.7,
      "expR": 0.083,
      "pf": 1.19
    },
    "5m/RETEST/SHORT": {
      "n": 94,
      "wrTP1": 47.9,
      "expR": -0.019,
      "pf": 0.96
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
      "n": 57,
      "wrTP1": 42.1,
      "expR": 0.091,
      "pf": 1.18
    },
    "1m/RETEST/LONG": {
      "n": 1606,
      "wrTP1": 45.1,
      "expR": 0.046,
      "pf": 1.09
    },
    "1m/RETEST/SHORT": {
      "n": 1715,
      "wrTP1": 45.0,
      "expR": 0.046,
      "pf": 1.09
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
      "n": 694,
      "wrTP1": 47.7,
      "expR": 0.038,
      "pf": 1.08
    },
    "2m/RETEST/SHORT": {
      "n": 757,
      "wrTP1": 51.5,
      "expR": 0.151,
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
      "n": 242,
      "wrTP1": 52.5,
      "expR": 0.205,
      "pf": 1.46
    },
    "5m/RETEST/SHORT": {
      "n": 221,
      "wrTP1": 51.6,
      "expR": 0.113,
      "pf": 1.25
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 10,
      "wrTP1": 60.0,
      "expR": 0.201,
      "pf": 1.5
    },
    "1m/INV/SHORT": {
      "n": 5,
      "wrTP1": 60.0,
      "expR": -0.13,
      "pf": 0.68
    },
    "1m/RETEST/LONG": {
      "n": 196,
      "wrTP1": 52.0,
      "expR": 0.09,
      "pf": 1.2
    },
    "1m/RETEST/SHORT": {
      "n": 296,
      "wrTP1": 57.4,
      "expR": 0.193,
      "pf": 1.5
    },
    "2m/INV/LONG": {
      "n": 3,
      "wrTP1": 66.7,
      "expR": -0.217,
      "pf": 0.35
    },
    "2m/INV/SHORT": {
      "n": 2,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 90,
      "wrTP1": 41.1,
      "expR": -0.099,
      "pf": 0.83
    },
    "2m/RETEST/SHORT": {
      "n": 111,
      "wrTP1": 56.8,
      "expR": 0.027,
      "pf": 1.06
    },
    "5m/RETEST/LONG": {
      "n": 38,
      "wrTP1": 60.5,
      "expR": 0.284,
      "pf": 1.72
    },
    "5m/RETEST/SHORT": {
      "n": 36,
      "wrTP1": 61.1,
      "expR": 0.091,
      "pf": 1.23
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 8805,
  "brier": 0.223,
  "bias": -0.104,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.158
    },
    {
      "feature": "stretchAtr",
      "weight": -0.121
    },
    {
      "feature": "rvol",
      "weight": 0.084
    },
    {
      "feature": "nearTk",
      "weight": -0.077
    },
    {
      "feature": "biasScore",
      "weight": -0.072
    },
    {
      "feature": "structDir",
      "weight": 0.039
    },
    {
      "feature": "hourNY",
      "weight": 0.039
    },
    {
      "feature": "chopIdx",
      "weight": -0.034
    },
    {
      "feature": "aligned",
      "weight": -0.03
    },
    {
      "feature": "nearEdge",
      "weight": 0.016
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.008
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.004
    },
    {
      "feature": "emaStack",
      "weight": 0.003
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.167,
      "actual": 0.184,
      "n": 880
    },
    {
      "bin": 1,
      "pred": 0.351,
      "actual": 0.3,
      "n": 881
    },
    {
      "bin": 2,
      "pred": 0.432,
      "actual": 0.34,
      "n": 880
    },
    {
      "bin": 3,
      "pred": 0.481,
      "actual": 0.418,
      "n": 881
    },
    {
      "bin": 4,
      "pred": 0.52,
      "actual": 0.476,
      "n": 880
    },
    {
      "bin": 5,
      "pred": 0.551,
      "actual": 0.554,
      "n": 881
    },
    {
      "bin": 6,
      "pred": 0.575,
      "actual": 0.609,
      "n": 880
    },
    {
      "bin": 7,
      "pred": 0.598,
      "actual": 0.633,
      "n": 881
    },
    {
      "bin": 8,
      "pred": 0.621,
      "actual": 0.706,
      "n": 880
    },
    {
      "bin": 9,
      "pred": 0.662,
      "actual": 0.725,
      "n": 881
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
  "weeks": 3
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.133,
    "ci90": [
      -0.096,
      0.376
    ],
    "p_mean_le_0": 0.177,
    "n": 81,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.116,
    "ci90": [
      -0.108,
      0.351
    ],
    "p_mean_le_0": 0.201,
    "n": 79,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.024,
    "ci90": [
      -0.013,
      0.062
    ],
    "p_mean_le_0": 0.146,
    "n": 3125,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.055,
    "ci90": [
      0.014,
      0.101
    ],
    "p_mean_le_0": 0.015,
    "n": 2414,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": -0.159,
    "ci90": [
      -0.447,
      0.129
    ],
    "p_mean_le_0": 0.818,
    "n": 29,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.017,
    "ci90": [
      -0.335,
      0.412
    ],
    "p_mean_le_0": 0.477,
    "n": 39,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.017,
    "ci90": [
      -0.068,
      0.036
    ],
    "p_mean_le_0": 0.706,
    "n": 1451,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.089,
    "ci90": [
      0.028,
      0.149
    ],
    "p_mean_le_0": 0.009,
    "n": 1063,
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
  "5m/INV/SHORT": {
    "expR": 0.615,
    "ci90": [
      -0.057,
      1.309
    ],
    "p_mean_le_0": 0.072,
    "n": 8,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.155,
    "ci90": [
      0.067,
      0.246
    ],
    "p_mean_le_0": 0.003,
    "n": 512,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.077,
    "ci90": [
      -0.028,
      0.198
    ],
    "p_mean_le_0": 0.125,
    "n": 342,
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
      "n": 3401,
      "wrTP1": 47.6,
      "expR": 0.074,
      "pf": 1.15,
      "defining_features": {
        "biasScore": -1.06,
        "emaStack": -0.96,
        "nearEdge": -0.81,
        "structDir": -0.44
      }
    },
    {
      "id": 0,
      "n": 3355,
      "wrTP1": 45.0,
      "expR": 0.05,
      "pf": 1.1,
      "defining_features": {
        "biasScore": 0.8,
        "emaStack": 0.68,
        "nearEdge": 0.68,
        "hourNY": -0.51
      }
    },
    {
      "id": 1,
      "n": 1569,
      "wrTP1": 50.2,
      "expR": 0.018,
      "pf": 1.04,
      "defining_features": {
        "hourNY": 1.3,
        "atrPctUsed": -0.81,
        "emaStack": 0.64,
        "biasScore": 0.57
      }
    },
    {
      "id": 3,
      "n": 978,
      "wrTP1": 44.8,
      "expR": -0.027,
      "pf": 0.95,
      "defining_features": {
        "stretchAtr": 1.78,
        "rvol": 1.66,
        "chopIdx": -1.43,
        "entryZoneTk": -0.29
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
        "n": 27,
        "wrTP1": 59.3,
        "expR": 0.473
      },
      "YM": {
        "n": 30,
        "wrTP1": 36.7,
        "expR": 0.101
      },
      "ES": {
        "n": 8,
        "wrTP1": 50.0,
        "expR": -0.33
      },
      "NQ": {
        "n": 6,
        "wrTP1": 33.3,
        "expR": 0.212
      },
      "GC": {
        "n": 13,
        "wrTP1": 38.5,
        "expR": -0.26
      }
    },
    "expR_spread": 0.803,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 52,
        "wrTP1": 44.2,
        "expR": 0.048
      },
      "NQ": {
        "n": 9,
        "wrTP1": 55.6,
        "expR": 0.19
      },
      "ES": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.57
      },
      "GC": {
        "n": 14,
        "wrTP1": 57.1,
        "expR": 0.116
      }
    },
    "expR_spread": 0.522,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 530,
        "wrTP1": 43.8,
        "expR": 0.059
      },
      "NQ": {
        "n": 640,
        "wrTP1": 44.2,
        "expR": -0.042
      },
      "ES": {
        "n": 552,
        "wrTP1": 44.6,
        "expR": 0.016
      },
      "CL": {
        "n": 1015,
        "wrTP1": 46.2,
        "expR": 0.037
      },
      "YM": {
        "n": 435,
        "wrTP1": 42.5,
        "expR": 0.057
      }
    },
    "expR_spread": 0.101,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 388,
        "wrTP1": 43.8,
        "expR": 0.104
      },
      "GC": {
        "n": 584,
        "wrTP1": 48.6,
        "expR": 0.082
      },
      "YM": {
        "n": 786,
        "wrTP1": 46.8,
        "expR": 0.088
      },
      "ES": {
        "n": 653,
        "wrTP1": 45.9,
        "expR": 0.002
      },
      "CL": {
        "n": 49,
        "wrTP1": 32.7,
        "expR": -0.441
      }
    },
    "expR_spread": 0.545,
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
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.137
      },
      "YM": {
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.673
      },
      "ES": {
        "n": 5,
        "wrTP1": 80.0,
        "expR": 0.428
      },
      "NQ": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": -0.006
      }
    },
    "expR_spread": 1.101,
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
      }
    },
    "expR_spread": 0.784,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 318,
        "wrTP1": 49.1,
        "expR": 0.014
      },
      "GC": {
        "n": 187,
        "wrTP1": 44.4,
        "expR": -0.003
      },
      "CL": {
        "n": 476,
        "wrTP1": 50.2,
        "expR": 0.055
      },
      "ES": {
        "n": 261,
        "wrTP1": 44.8,
        "expR": -0.109
      },
      "YM": {
        "n": 226,
        "wrTP1": 38.9,
        "expR": -0.119
      }
    },
    "expR_spread": 0.174,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 270,
        "wrTP1": 50.7,
        "expR": 0.052
      },
      "YM": {
        "n": 379,
        "wrTP1": 51.5,
        "expR": 0.134
      },
      "GC": {
        "n": 221,
        "wrTP1": 51.1,
        "expR": 0.076
      },
      "NQ": {
        "n": 188,
        "wrTP1": 45.7,
        "expR": 0.121
      },
      "CL": {
        "n": 20,
        "wrTP1": 35.0,
        "expR": -0.422
      }
    },
    "expR_spread": 0.556,
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
        "n": 20,
        "wrTP1": 65.0,
        "expR": 0.448
      },
      "ES": {
        "n": 112,
        "wrTP1": 50.9,
        "expR": 0.173
      },
      "YM": {
        "n": 106,
        "wrTP1": 52.8,
        "expR": 0.209
      },
      "CL": {
        "n": 144,
        "wrTP1": 60.4,
        "expR": 0.298
      },
      "NQ": {
        "n": 141,
        "wrTP1": 46.1,
        "expR": -0.089
      }
    },
    "expR_spread": 0.537,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 76,
        "wrTP1": 51.3,
        "expR": 0.035
      },
      "ES": {
        "n": 93,
        "wrTP1": 59.1,
        "expR": 0.131
      },
      "GC": {
        "n": 67,
        "wrTP1": 38.8,
        "expR": -0.057
      },
      "YM": {
        "n": 106,
        "wrTP1": 53.8,
        "expR": 0.184
      },
      "CL": {
        "n": 9,
        "wrTP1": 44.4,
        "expR": -0.323
      }
    },
    "expR_spread": 0.507,
    "verdict": "instrument-specific"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 16,
  "near_news_30m": {
    "n": 45,
    "wrTP1": 68.9,
    "nSL": 14,
    "nTO": 0,
    "expR": 0.226,
    "pf": 1.72,
    "mfe_p25": 13.0,
    "mfe_p50": 24.0,
    "mfe_p75": 34.0,
    "winnerMAE_p75": 16.5,
    "winnerMAE_p90": 22.0,
    "loserMFEbeforeSL_p50": 1.5,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 2.5,
    "entryZoneTk_p50": -26.0,
    "revAfterSL_rate": 64.3
  },
  "away_from_news": {
    "n": 9258,
    "wrTP1": 46.7,
    "nSL": 4437,
    "nTO": 498,
    "expR": 0.044,
    "pf": 1.09,
    "mfe_p25": 7.0,
    "mfe_p50": 17.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -13.0,
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
      "asOf": "2026-09-15 (martes). Dato nuevo genuino, sin incidentes de repo en el bus de datos (el `git pull` inicial trajo un historial de origin/main reescrito rio arriba -- ya investigado: mismo tip que la rama local, sin perdida de commits propios, resuelto haciendo checkout de main sobre origin/main). n de pares resueltos subio de 9052 a 9303.",
      "retest_1m_long": {
        "n": 2676,
        "deltaER_orig_minus_layer": 0.141,
        "ci90": [
          0.063,
          0.224
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 2525 a 2676, delta practicamente identico (0.146->0.141) -- octava confirmacion independiente, sigue siendo la lectura mas estable del experimento."
      },
      "retest_1m_short": {
        "n": 1955,
        "deltaER_orig_minus_layer": 0.126,
        "ci90": [
          0.034,
          0.226
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 1708 a 1955, delta se mantiene sin cruzar cero (0.139->0.126), limite inferior del CI90 estable en 0.034."
      },
      "retest_2m_long": {
        "n": 1306,
        "deltaER_orig_minus_layer": 0.032,
        "ci90": [
          -0.043,
          0.106
        ],
        "ci90_no_cruza_cero": false,
        "nota": "n subio de 1235 a 1306, delta subio un poco (0.015->0.032) pero el CI90 sigue cruzando cero -- novena lectura seguida sin certificar, se mantiene fuera de la propuesta."
      },
      "retest_2m_short": {
        "n": 890,
        "deltaER_orig_minus_layer": 0.117,
        "ci90": [
          0.014,
          0.223
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 796 a 890, delta se fortalecio (0.093->0.117) y el CI90 ya no cruza cero, pero el limite inferior (0.014) sigue muy pegado a cero -- tratar como candidato debil/al filo, no promoverlo a la lista solida todavia (necesita mas de una lectura seguida lejos de cero)."
      },
      "retest_5m_long": {
        "n": 489,
        "deltaER_orig_minus_layer": 0.246,
        "ci90": [
          0.055,
          0.471
        ],
        "ci90_no_cruza_cero": true,
        "nota": "QUINTA LECTURA SEGUIDA CERTIFICANDO: n subio de 459 a 489, delta practicamente identico (0.252->0.246) -- sigue estable, sin retroceso, desde que se incluyo en la propuesta de la revision semanal."
      },
      "retest_5m_short": {
        "n": 305,
        "deltaER_orig_minus_layer": 0.561,
        "ci90": [
          0.163,
          1.074
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 270 a 305, delta practicamente sin cambio (0.559->0.561) -- sigue siendo la lectura mas solida del experimento."
      },
      "overall_by_basis_retestBar": {
        "n": 5794,
        "deltaER": 0.146,
        "ci90": [
          0.096,
          0.202
        ],
        "nota": "n subio de 5413 a 5794, delta estable (0.14->0.146) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba."
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
      "2026-09-15 (martes, primer dia habil despues de la reapertura de Globex del domingo, dato genuino): los 4 segmentos propuestos en la revision semanal del 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG suma su octava confirmacion, 1m SHORT y 5m SHORT se mantienen estables, 5m LONG suma su QUINTA lectura seguida certificando (ya el doble del umbral de '2 lecturas seguidas' que se puso el propio experimento el 09-08). Movimiento notable: 2m SHORT se fortalecio (delta 0.093->0.117, CI90 ya no cruza cero) pero su limite inferior (0.014) sigue demasiado pegado a cero para promoverlo -- se mantiene como candidato debil/al filo, fuera de la propuesta hasta una segunda lectura consecutiva lejos de cero. 2m LONG sigue sin certificar (novena lectura). Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView. Nota de mantenimiento (no de dato): se corrigio hoy un bug de analyze.py que hacia que la alerta MUESTRA de 2026-W36/W37 (caida de n ya explicada por dedup, sin perdida de archivo real) se repitiera identica cada corrida para siempre en vez de solo mientras la cifra siguiera empeorando; el efecto se vera desde la proxima corrida."
    ],
    "beforeN": 9052,
    "afterN": 0,
    "before": {
      "n": 9052,
      "wrTP1": 46.8,
      "nSL": 4341,
      "nTO": 478,
      "expR": 0.043,
      "pf": 1.09,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
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
    "date": "2026-09-15",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-14T19:15:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "GC",
    "focus": {
      "sym": "GC",
      "verdict": "GO",
      "window": "17:00-01:00 CT",
      "setup": {
        "es": "A+ pullback PDL/EMA/VWAP/FVG 1h 4333-4341 -- el rechazo ya se confirmo",
        "en": "A+ PDL/EMA/VWAP/1h FVG pullback 4333-4341 -- the rejection already confirmed"
      },
      "trigger": {
        "es": "ya disparo: mecha a 4343.6 y cierre de vuelta bajo 4333, precio actual 4329.0 -- corto en marcha",
        "en": "already fired: wick to 4343.6 and a close back below 4333, current price 4329.0 -- short underway"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 4356 (VAH)",
        "en": "5m close sustained above 4356 (VAH)"
      },
      "note": {
        "es": "el unico instrumento sin conflicto de marco ya confirmo el rechazo esperado -- gestiona el riesgo (stop sobre 4351), no persigas si ya extendio mucho mas hacia 4307.9",
        "en": "the only instrument with no frame conflict already confirmed the expected rejection -- manage risk (stop above 4351), don't chase if it's already extended much further toward 4307.9"
      }
    },
    "alarm": {
      "es": "3a rotacion de tesis del ciclo en NQ/ES en 4 sesiones, y hit-rate de escenario A bajo el 30% en 20 dias para NQ (28%) y GC (25%) -- trata la 'A' de hoy como apuesta debil, no como default",
      "en": "3rd thesis rotation of the cycle in NQ/ES within 4 sessions, and scenario-A hit-rate under 30% over 20 days for NQ (28%) and GC (25%) -- treat today's 'A' as a weak bet, not the default"
    },
    "dataHealth": {
      "snapshot": "OK",
      "builtAtAgeMin": 15,
      "stale": [],
      "missing": [],
      "notes": {
        "es": "snapshot fresco (~15min tras la reapertura de Tokio), las 6 fuentes de los 5 instrumentos llegaron frescas (<10min de antiguedad cada una).",
        "en": "fresh snapshot (~15min after Tokyo's open), all 6 sources for the 5 instruments arrived fresh (<10min old each)."
      }
    },
    "calendarContext": {
      "tags": [
        "semana-FOMC"
      ],
      "note": {
        "es": "FOMC (Fed Funds Rate + proyecciones + comunicado + rueda de prensa) manana miercoles 2026-09-16 ~13:00-13:30 CT -- un dia mas de cautela extra antes del evento. La sesion de Asia de hoy no trae catalizador USD/oil de alto impacto (el Claimant Count britanico cae 01:00 CT, GBP, bajo impacto directo para el bus); el API Weekly de crudo cae manana 15:30 CT, ya en la sesion de NY, fuera de esta ventana.",
        "en": "FOMC (Fed Funds Rate + projections + statement + press conference) tomorrow Wednesday 2026-09-16 ~13:00-13:30 CT -- one more day of extra caution before the event. Tonight's Asia session carries no high-impact USD/oil catalyst (UK Claimant Count falls 01:00 CT, GBP, low direct impact for the bus); the weekly
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 3001,
  "by_verdict": {
    "AVOID": {
      "n": 1053,
      "wrTP1": 46.2,
      "nSL": 531,
      "nTO": 36,
      "expR": 0.015,
      "pf": 1.03,
      "mfe_p25": 7.0,
      "mfe_p50": 14.0,
      "mfe_p75": 27.75,
      "winnerMAE_p75": 9.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 34.5
    },
    "GO": {
      "n": 363,
      "wrTP1": 53.4,
      "nSL": 162,
      "nTO": 7,
      "expR": 0.09,
      "pf": 1.2,
      "mfe_p25": 11.0,
      "mfe_p50": 24.0,
      "mfe_p75": 51.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 29.700000000000017,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 38.3
    },
    "WAIT": {
      "n": 1585,
      "wrTP1": 49.0,
      "nSL": 717,
      "nTO": 91,
      "expR": 0.079,
      "pf": 1.17,
      "mfe_p25": 8.0,
      "mfe_p50": 20.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 29.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 37.8
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.015,
      "ci90": [
        -0.047,
        0.083
      ],
      "p_mean_le_0": 0.351,
      "n": 1042
    },
    "GO": {
      "expR": 0.09,
      "ci90": [
        -0.008,
        0.193
      ],
      "p_mean_le_0": 0.064,
      "n": 362
    },
    "WAIT": {
      "expR": 0.079,
      "ci90": [
        0.03,
        0.127
      ],
      "p_mean_le_0": 0.006,
      "n": 1557
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1053,
      "wrTP1": 46.2,
      "nSL": 531,
      "nTO": 36,
      "expR": 0.015,
      "pf": 1.03,
      "mfe_p25": 7.0,
      "mfe_p50": 14.0,
      "mfe_p75": 27.75,
      "winnerMAE_p75": 9.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 34.5
    },
    "GO_or_WAIT": {
      "n": 1948,
      "wrTP1": 49.8,
      "nSL": 879,
      "nTO": 98,
      "expR": 0.081,
      "pf": 1.18,
      "mfe_p25": 8.0,
      "mfe_p50": 21.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 29.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 37.9
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.015,
      "ci90": [
        -0.047,
        0.083
      ],
      "p_mean_le_0": 0.351,
      "n": 1042
    },
    "GO_or_WAIT": {
      "expR": 0.081,
      "ci90": [
        0.037,
        0.124
      ],
      "p_mean_le_0": 0.002,
      "n": 1919
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 5,
        "wrTP1": 20.0,
        "nSL": 3,
        "nTO": 1,
        "expR": -0.52,
        "pf": 0.13,
        "mfe_p25": 5.0,
        "mfe_p50": 29.0,
        "mfe_p75": 29.0,
        "winnerMAE_p75": 4.0,
        "winnerMAE_p90": 4.0,
        "loserMFEbeforeSL_p50": 29.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 8.0,
        "entryZoneTk_p50": -39.0,
        "revAfterSL_rate": 0.0
      },
      "GO": {
        "n": 5,
        "wrTP1": 60.0,
        "nSL": 2,
        "nTO": 0,
        "expR": -0.01,
        "pf": 0.97,
        "mfe_p25": 23.0,
        "mfe_p50": 24.0,
        "mfe_p75": 28.0,
        "winnerMAE_p75": 7.5,
        "winnerMAE_p90": 7.8,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -60.0,
        "revAfterSL_rate": 50.0
      },
      "WAIT": {
        "n": 21,
        "wrTP1": 57.1,
        "nSL": 8,
        "nTO": 1,
        "expR": 0.18,
        "pf": 1.47,
        "mfe_p25": 12.0,
        "mfe_p50": 34.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 19.5,
        "winnerMAE_p90": 24.6,
        "loserMFEbeforeSL_p50": 0.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 37.5
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 24,
        "wrTP1": 37.5,
        "nSL": 13,
        "nTO": 2,
        "expR": -0.188,
        "pf": 0.67,
        "mfe_p25": 7.0,
        "mfe_p50": 14.0,
        "mfe_p75": 23.0,
        "winnerMAE_p75": 4.0,
        "winnerMAE_p90": 6.6000000000000005,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -10.5,
        "revAfterSL_rate": 15.4
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
        "n": 508,
        "wrTP1": 49.0,
        "nSL": 250,
        "nTO": 9,
        "expR": 0.018,
        "pf": 1.04,
        "mfe_p25": 6.0,
        "mfe_p50": 12.0,
        "mfe_p75": 23.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 18.200000000000017,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -9.0,
        "revAfterSL_rate": 31.2
      },
      "GO": {
        "n": 177,
        "wrTP1": 48.0,
        "nSL": 91,
        "nTO": 1,
        "expR": -0.06,
        "pf": 0.88,
        "mfe_p25": 8.0,
        "mfe_p50": 19.5,
        "mfe_p75": 46.5,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 29.200000000000017,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 38.5
      },
      "WAIT": {
        "n": 824,
        "wrTP1": 51.6,
        "nSL": 353,
        "nTO": 46,
        "expR": 0.167,
        "pf": 1.39,
        "mfe_p25": 8.0,
        "mfe_p50": 23.0,
        "mfe_p75": 52.75,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.600000000000023,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 39.7
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 516,
        "wrTP1": 44.0,
        "nSL": 265,
        "nTO": 24,
        "expR": 0.026,
        "pf": 1.05,
        "mfe_p25": 7.0,
        "mfe_p50": 15.5,
        "mfe_p75": 30.0,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 20.80000000000001,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 38.9
      },
      "GO": {
        "n": 179,
        "wrTP1": 58.7,
        "nSL": 68,
        "nTO": 6,
        "expR": 0.231,
        "pf": 1.6,
        "mfe_p25": 13.0,
        "mfe_p50": 27.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 30.800000000000026,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 38.2
      },
      "WAIT": {
        "n": 721,
        "wrTP1": 45.9,
        "nSL": 347,
        "nTO": 43,
        "expR": -0.021,
        "pf": 0.96,
        "mfe_p25": 7.0,
        "mfe_p50": 17.0,
        "mfe_p75": 42.5,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 33.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 35.7
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```
