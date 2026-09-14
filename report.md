# Scalp CC · report 2026-09-14T01:14Z
- signals=8595 outcomes=8442 pares_resueltos=8567 pendientes=28 huerfanos=25

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: semana ya cerrada 2026-W36 bajo de n=3183 a n=3140 desde la corrida previa -- vigilar, puede ser deduplicacion.
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.184 vs 0.044, delta 0.14 CI90 [0.088, 0.198], n 5413). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.196 vs 0.066, delta 0.131 CI90 [0.019, 0.248], n 1580). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.081 CI90 [0.029, 0.133], n 1492). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.043, "ci90": [0.02, 0.065], "p_mean_le_0": 0.001, "n": 8417}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 75 | 44.0 | 0.139 | 1.29 | 33 | 15.0 | 10.0 | 21.2 |
| 1m/INV/SHORT | 76 | 48.7 | 0.133 | 1.29 | 34 | 20.0 | 11.0 | 17.6 |
| 1m/RETEST/LONG | 2983 | 44.2 | 0.02 | 1.04 | 1476 | 14.0 | 10.0 | 29.1 |
| 1m/RETEST/SHORT | 2187 | 45.0 | 0.04 | 1.08 | 1063 | 16.0 | 11.0 | 31.1 |
| 2m/INV/LONG | 26 | 46.2 | -0.152 | 0.71 | 13 | 10.0 | 10.25 | 30.8 |
| 2m/INV/SHORT | 37 | 37.8 | 0.072 | 1.14 | 19 | 20.0 | 15.75 | 36.8 |
| 2m/RETEST/LONG | 1380 | 47.0 | -0.01 | 0.98 | 679 | 16.0 | 12.25 | 35.6 |
| 2m/RETEST/SHORT | 981 | 49.4 | 0.104 | 1.22 | 450 | 21.0 | 11.0 | 40.9 |
| 5m/INV/LONG | 10 | 90.0 | 0.849 | 99.0 | 0 | 30.0 | 32.0 | None |
| 5m/INV/SHORT | 8 | 75.0 | 0.615 | 3.46 | 2 | 58.0 | 68.75 | 100.0 |
| 5m/RETEST/LONG | 488 | 52.7 | 0.148 | 1.33 | 213 | 25.0 | 18.0 | 48.8 |
| 5m/RETEST/SHORT | 316 | 50.6 | 0.076 | 1.17 | 141 | 30.0 | 21.0 | 39.0 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 580 | 25.9 | 0.063 | 1.09 | 373 | 29.0 | 15.75 | 20.1 |
| B | 3569 | 46.6 | 0.055 | 1.11 | 1709 | 16.5 | 11.0 | 32.5 |
| C | 4418 | 48.7 | 0.03 | 1.06 | 2041 | 15.0 | 12.0 | 36.4 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 3227 | 49.3 | 0.066 | 1.14 | 1464 | 11.0 | 9.0 | 38.4 |
| London | 1283 | 44.6 | -0.056 | 0.89 | 675 | 17.0 | 11.25 | 31.3 |
| NY | 1408 | 46.3 | 0.168 | 1.35 | 669 | 26.0 | 17.0 | 38.3 |
| Sin KZ | 2649 | 43.4 | -0.005 | 0.99 | 1315 | 18.0 | 13.0 | 26.1 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 2126 | 45.4 | 0.036 | 1.07 | 1042 | 19.0 | 13.0 | 31.1 |
| edge=0 | 3817 | 48.8 | 0.036 | 1.07 | 1787 | 14.0 | 10.0 | 38.4 |
| edge=1 | 2624 | 43.3 | 0.058 | 1.12 | 1294 | 18.0 | 13.0 | 28.0 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 8557 | 46.3 | 0.042 | 1.09 | 4122 | 16.0 | 12.0 | 33.3 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 47 | 48.9 | 0.059 | 1.12 | 22 | 10.0 | 9.5 | 31.8 |
| INV/LONG|edge=1 | 60 | 48.3 | 0.172 | 1.44 | 22 | 22.5 | 17.0 | 13.6 |
| INV/SHORT|edge=-1 | 70 | 41.4 | 0.176 | 1.36 | 34 | 22.0 | 12.0 | 23.5 |
| INV/SHORT|edge=0 | 43 | 51.2 | -0.051 | 0.89 | 19 | 11.0 | 21.5 | 36.8 |
| INV/SHORT|edge=1 | 8 | 75.0 | 0.901 | 4.6 | 2 | 32.5 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 228 | 50.9 | 0.1 | 1.23 | 98 | 12.0 | 8.0 | 50.0 |
| RETEST/LONG|edge=0 | 2191 | 49.0 | -0.018 | 0.96 | 1055 | 13.0 | 11.0 | 37.8 |
| RETEST/LONG|edge=1 | 2432 | 42.5 | 0.055 | 1.11 | 1215 | 18.0 | 13.0 | 27.0 |
| RETEST/SHORT|edge=-1 | 1824 | 44.8 | 0.021 | 1.04 | 908 | 20.0 | 15.0 | 29.3 |
| RETEST/SHORT|edge=0 | 1536 | 48.6 | 0.114 | 1.25 | 691 | 16.0 | 10.0 | 39.5 |
| RETEST/SHORT|edge=1 | 124 | 53.2 | 0.005 | 1.01 | 55 | 14.0 | 9.0 | 56.4 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 28 | 42.9 | 0.132 | 1.3 | 11 | 21.0 | 18.0 | 9.1 |
| INV/LONG|tier=C | 83 | 50.6 | 0.135 | 1.31 | 35 | 14.0 | 12.0 | 28.6 |
| INV/SHORT|tier=B | 38 | 47.4 | 0.192 | 1.41 | 18 | 18.5 | 8.75 | 5.6 |
| INV/SHORT|tier=C | 83 | 47.0 | 0.125 | 1.27 | 37 | 22.0 | 28.0 | 37.8 |
| RETEST/LONG|tier=A+ | 348 | 25.0 | 0.07 | 1.11 | 219 | 23.0 | 17.0 | 17.4 |
| RETEST/LONG|tier=B | 2008 | 45.6 | 0.068 | 1.14 | 969 | 15.0 | 10.0 | 32.5 |
| RETEST/LONG|tier=C | 2495 | 48.9 | -0.017 | 0.96 | 1180 | 14.0 | 12.0 | 35.8 |
| RETEST/SHORT|tier=A+ | 232 | 27.2 | 0.052 | 1.08 | 154 | 39.0 | 14.0 | 24.0 |
| RETEST/SHORT|tier=B | 1495 | 47.9 | 0.033 | 1.07 | 711 | 17.0 | 13.0 | 33.5 |
| RETEST/SHORT|tier=C | 1757 | 48.4 | 0.087 | 1.19 | 789 | 17.0 | 11.0 | 37.4 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 111 | 48.6 | 0.135 | 1.31 | 46 | 17.5 | 13.5 | 23.9 |
| INV/SHORT|aligned=1 | 121 | 47.1 | 0.146 | 1.32 | 55 | 21.0 | 17.0 | 27.3 |
| RETEST/LONG|aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 4841 | 45.8 | 0.024 | 1.05 | 2367 | 15.0 | 11.0 | 32.8 |
| RETEST/SHORT|aligned=1 | 3484 | 46.8 | 0.061 | 1.13 | 1654 | 18.0 | 12.0 | 34.5 |

## Autopsia de SL
n_losses=4123  causas: RR-bajo×1567, contra-estructura×1438, stop-en-el-minimo×1372, killzone-Asia-largo×845, sin-nivel-detras×810, estirado×708, chop×592, SL-muy-pegado×514, sin-causa-clara×403, contra-sesgo×1
- INV/LONG (n=46): killzone-Asia-largo×22, RR-bajo×21, contra-estructura×14, stop-en-el-minimo×11, estirado×10, sin-nivel-detras×7, chop×4, SL-muy-pegado×4, sin-causa-clara×1
- INV/SHORT (n=55): RR-bajo×27, contra-estructura×18, stop-en-el-minimo×15, sin-causa-clara×11, estirado×10, SL-muy-pegado×7, chop×4, sin-nivel-detras×4
- RETEST/LONG (n=2368): RR-bajo×907, contra-estructura×876, killzone-Asia-largo×823, stop-en-el-minimo×776, sin-nivel-detras×482, estirado×386, chop×373, SL-muy-pegado×286, sin-causa-clara×180, contra-sesgo×1
- RETEST/SHORT (n=1654): RR-bajo×612, stop-en-el-minimo×570, contra-estructura×530, sin-nivel-detras×317, estirado×302, SL-muy-pegado×217, chop×211, sin-causa-clara×211

## Autopsia de SL · semana 2026-W38 (para revision semanal)
n_losses=6  causas: RR-bajo×3, stop-en-el-minimo×3, contra-estructura×2, estirado×1, killzone-Asia-largo×1, chop×1, sin-causa-clara×1
ejemplos por causa: {"RR-bajo": ["NQ-5-21912-S", "GC-1-34476-S", "NQ-1-27530-S"], "stop-en-el-minimo": ["NQ-5-21912-S", "GC-1-34476-S", "NQ-1-27530-S"], "contra-estructura": ["GC-1-34476-S", "NQ-1-27530-S"]}

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
    "n": 8403,
    "naive_expR": 0.042,
    "managed_expR": 0.127,
    "delta": 0.084,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 48.1,
    "fill_full_pct": 33.9,
    "m1_rate": 36.6,
    "m2_rate": 23.3,
    "m3_rate": 12.7,
    "beAfterM1_rate": 17.2
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 72,
      "naive_expR": 0.139,
      "managed_expR": 0.279,
      "delta": 0.14,
      "avgEntryBetterTk_p50": 2.1500000000000004,
      "fill_t3plus_pct": 48.6,
      "fill_full_pct": 36.1,
      "m1_rate": 47.2,
      "m2_rate": 30.6,
      "m3_rate": 16.7,
      "beAfterM1_rate": 22.2
    },
    "1m/INV/SHORT": {
      "n": 74,
      "naive_expR": 0.133,
      "managed_expR": 0.316,
      "delta": 0.183,
      "avgEntryBetterTk_p50": 3.3,
      "fill_t3plus_pct": 55.4,
      "fill_full_pct": 43.2,
      "m1_rate": 39.2,
      "m2_rate": 27.0,
      "m3_rate": 16.2,
      "beAfterM1_rate": 16.2
    },
    "1m/RETEST/LONG": {
      "n": 2932,
      "naive_expR": 0.02,
      "managed_expR": 0.113,
      "delta": 0.094,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 49.5,
      "fill_full_pct": 35.5,
      "m1_rate": 35.5,
      "m2_rate": 22.3,
      "m3_rate": 11.7,
      "beAfterM1_rate": 16.2
    },
    "1m/RETEST/SHORT": {
      "n": 2134,
      "naive_expR": 0.041,
      "managed_expR": 0.152,
      "delta": 0.111,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 49.1,
      "fill_full_pct": 33.8,
      "m1_rate": 39.6,
      "m2_rate": 24.7,
      "m3_rate": 13.7,
      "beAfterM1_rate": 18.7
    },
    "2m/INV/LONG": {
      "n": 26,
      "naive_expR": -0.152,
      "managed_expR": -0.141,
      "delta": 0.011,
      "avgEntryBetterTk_p50": 2.1500000000000004,
      "fill_t3plus_pct": 53.8,
      "fill_full_pct": 34.6,
      "m1_rate": 19.2,
      "m2_rate": 19.2,
      "m3_rate": 0.0,
      "beAfterM1_rate": 3.8
    },
    "2m/INV/SHORT": {
      "n": 37,
      "naive_expR": 0.072,
      "managed_expR": 0.008,
      "delta": -0.064,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 45.9,
      "fill_full_pct": 37.8,
      "m1_rate": 27.0,
      "m2_rate": 24.3,
      "m3_rate": 13.5,
      "beAfterM1_rate": 5.4
    },
    "2m/RETEST/LONG": {
      "n": 1361,
      "naive_expR": -0.011,
      "managed_expR": 0.08,
      "delta": 0.09,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 46.4,
      "fill_full_pct": 31.2,
      "m1_rate": 34.2,
      "m2_rate": 21.2,
      "m3_rate": 11.8,
      "beAfterM1_rate": 16.8
    },
    "2m/RETEST/SHORT": {
      "n": 966,
      "naive_expR": 0.104,
      "managed_expR": 0.168,
      "delta": 0.064,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.0,
      "fill_full_pct": 35.8,
      "m1_rate": 37.8,
      "m2_rate": 25.2,
      "m3_rate": 13.5,
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
      "n": 477,
      "naive_expR": 0.148,
      "managed_expR": 0.092,
      "delta": -0.055,
      "avgEntryBetterTk_p50": 2.7,
      "fill_t3plus_pct": 37.9,
      "fill_full_pct": 27.3,
      "m1_rate": 34.4,
      "m2_rate": 23.1,
      "m3_rate": 13.0,
      "beAfterM1_rate": 18.4
    },
    "5m/RETEST/SHORT": {
      "n": 306,
      "naive_expR": 0.075,
      "managed_expR": 0.137,
      "delta": 0.063,
      "avgEntryBetterTk_p50": 4.9,
      "fill_t3plus_pct": 47.7,
      "fill_full_pct": 31.4,
      "m1_rate": 35.9,
      "m2_rate": 23.5,
      "m3_rate": 13.4,
      "beAfterM1_rate": 16.7
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 7208,
    "layer_expR": 0.051,
    "orig_expR": 0.19,
    "delta_orig_minus_layer": 0.139,
    "delta_ci90": [
      0.092,
      0.188
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 46.9,
    "orig_wrTP1": 32.5,
    "slTk_p50": 19.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.9,
    "orig_saved_from_SL": 15,
    "orig_caused_SL": 1047
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 215,
      "layer_expR": 0.142,
      "orig_expR": 0.3,
      "delta_orig_minus_layer": 0.158,
      "delta_ci90": [
        -0.187,
        0.56
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.9,
      "orig_wrTP1": 27.9,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 7.4,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 44
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
      "n": 5413,
      "layer_expR": 0.044,
      "orig_expR": 0.184,
      "delta_orig_minus_layer": 0.14,
      "delta_ci90": [
        0.088,
        0.198
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.1,
      "orig_wrTP1": 33.0,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.1,
      "orig_saved_from_SL": 13,
      "orig_caused_SL": 777
    },
    "retestBar2": {
      "n": 1580,
      "layer_expR": 0.066,
      "orig_expR": 0.196,
      "delta_orig_minus_layer": 0.131,
      "delta_ci90": [
        0.019,
        0.248
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.7,
      "orig_wrTP1": 31.5,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 2.9,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 226
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 72,
      "layer_expR": 0.139,
      "orig_expR": 0.061,
      "delta_orig_minus_layer": -0.078,
      "delta_ci90": [
        -0.471,
        0.334
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 45.8,
      "orig_wrTP1": 22.2,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 5.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 17
    },
    "1m/INV/SHORT": {
      "n": 64,
      "layer_expR": 0.145,
      "orig_expR": 0.397,
      "delta_orig_minus_layer": 0.252,
      "delta_ci90": [
        -0.505,
        1.245
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.4,
      "orig_wrTP1": 25.0,
      "slTk_p50": 18.5,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 4.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 15
    },
    "1m/RETEST/LONG": {
      "n": 2525,
      "layer_expR": 0.022,
      "orig_expR": 0.168,
      "delta_orig_minus_layer": 0.146,
      "delta_ci90": [
        0.065,
        0.234
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.2,
      "orig_wrTP1": 28.6,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.2,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 394
    },
    "1m/RETEST/SHORT": {
      "n": 1708,
      "layer_expR": 0.055,
      "orig_expR": 0.194,
      "delta_orig_minus_layer": 0.139,
      "delta_ci90": [
        0.032,
        0.25
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.5,
      "orig_wrTP1": 31.3,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 8.5,
      "orig_wider_pct": 2.8,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 244
    },
    "2m/INV/LONG": {
      "n": 26,
      "layer_expR": -0.152,
      "orig_expR": 0.873,
      "delta_orig_minus_layer": 1.025,
      "delta_ci90": [
        -0.018,
        2.287
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 46.2,
      "orig_wrTP1": 30.8,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 7.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 4
    },
    "2m/INV/SHORT": {
      "n": 36,
      "layer_expR": 0.062,
      "orig_expR": 0.496,
      "delta_orig_minus_layer": 0.434,
      "delta_ci90": [
        -0.071,
        1.114
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 36.1,
      "orig_wrTP1": 33.3,
      "slTk_p50": 22.5,
      "slOrigTk_p50": 5.5,
      "orig_wider_pct": 5.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 2
    },
    "2m/RETEST/LONG": {
      "n": 1235,
      "layer_expR": 0.01,
      "orig_expR": 0.025,
      "delta_orig_minus_layer": 0.015,
      "delta_ci90": [
        -0.062,
        0.091
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.0,
      "orig_wrTP1": 33.8,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.2,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 176
    },
    "2m/RETEST/SHORT": {
      "n": 796,
      "layer_expR": 0.123,
      "orig_expR": 0.216,
      "delta_orig_minus_layer": 0.093,
      "delta_ci90": [
        -0.011,
        0.204
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.9,
      "orig_wrTP1": 35.8,
      "slTk_p50": 20.5,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 121
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
      "n": 459,
      "layer_expR": 0.141,
      "orig_expR": 0.393,
      "delta_orig_minus_layer": 0.252,
      "delta_ci90": [
        0.054,
        0.49
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.8,
      "orig_wrTP1": 44.9,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 14.0,
      "orig_wider_pct": 16.1,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 44
    },
    "5m/RETEST/SHORT": {
      "n": 270,
      "layer_expR": 0.058,
      "orig_expR": 0.617,
      "delta_orig_minus_layer": 0.559,
      "delta_ci90": [
        0.152,
        1.105
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.7,
      "orig_wrTP1": 44.1,
      "slTk_p50": 28.5,
      "slOrigTk_p50": 22.5,
      "orig_wider_pct": 19.3,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 24
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
    "n": 5389,
    "wrTP1": 46.9,
    "expR": 0.072
  },
  "2026-W38": {
    "n": 38,
    "wrTP1": 84.2,
    "expR": 0.591
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
      "n": 37,
      "wrTP1": 43.2,
      "expR": -0.008,
      "pf": 0.98
    },
    "1m/INV/SHORT": {
      "n": 57,
      "wrTP1": 42.1,
      "expR": 0.091,
      "pf": 1.18
    },
    "1m/RETEST/LONG": {
      "n": 1608,
      "wrTP1": 45.1,
      "expR": 0.045,
      "pf": 1.09
    },
    "1m/RETEST/SHORT": {
      "n": 1718,
      "wrTP1": 45.0,
      "expR": 0.045,
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
      "n": 762,
      "wrTP1": 51.3,
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
      "n": 245,
      "wrTP1": 52.7,
      "expR": 0.209,
      "pf": 1.47
    },
    "5m/RETEST/SHORT": {
      "n": 220,
      "wrTP1": 51.8,
      "expR": 0.118,
      "pf": 1.26
    }
  },
  "2026-W38": {
    "1m/RETEST/LONG": {
      "n": 5,
      "wrTP1": 80.0,
      "expR": 0.58,
      "pf": 3.9
    },
    "1m/RETEST/SHORT": {
      "n": 20,
      "wrTP1": 80.0,
      "expR": 0.52,
      "pf": 3.6
    },
    "2m/RETEST/LONG": {
      "n": 2,
      "wrTP1": 100.0,
      "expR": 0.91,
      "pf": 99.0
    },
    "2m/RETEST/SHORT": {
      "n": 9,
      "wrTP1": 100.0,
      "expR": 0.901,
      "pf": 99.0
    },
    "5m/RETEST/SHORT": {
      "n": 2,
      "wrTP1": 50.0,
      "expR": -0.385,
      "pf": 0.23
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 8087,
  "brier": 0.2234,
  "bias": -0.121,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.165
    },
    {
      "feature": "stretchAtr",
      "weight": -0.137
    },
    {
      "feature": "rvol",
      "weight": 0.084
    },
    {
      "feature": "biasScore",
      "weight": -0.076
    },
    {
      "feature": "nearTk",
      "weight": -0.072
    },
    {
      "feature": "chopIdx",
      "weight": -0.053
    },
    {
      "feature": "nearEdge",
      "weight": 0.042
    },
    {
      "feature": "structDir",
      "weight": 0.038
    },
    {
      "feature": "hourNY",
      "weight": 0.033
    },
    {
      "feature": "aligned",
      "weight": -0.033
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.008
    },
    {
      "feature": "emaStack",
      "weight": -0.004
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.003
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.17,
      "actual": 0.193,
      "n": 808
    },
    {
      "bin": 1,
      "pred": 0.351,
      "actual": 0.295,
      "n": 809
    },
    {
      "bin": 2,
      "pred": 0.428,
      "actual": 0.335,
      "n": 809
    },
    {
      "bin": 3,
      "pred": 0.476,
      "actual": 0.402,
      "n": 808
    },
    {
      "bin": 4,
      "pred": 0.514,
      "actual": 0.455,
      "n": 809
    },
    {
      "bin": 5,
      "pred": 0.544,
      "actual": 0.549,
      "n": 809
    },
    {
      "bin": 6,
      "pred": 0.569,
      "actual": 0.611,
      "n": 808
    },
    {
      "bin": 7,
      "pred": 0.591,
      "actual": 0.624,
      "n": 809
    },
    {
      "bin": 8,
      "pred": 0.614,
      "actual": 0.727,
      "n": 809
    },
    {
      "bin": 9,
      "pred": 0.657,
      "actual": 0.71,
      "n": 809
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
    "expR": 0.139,
    "ci90": [
      -0.103,
      0.402
    ],
    "p_mean_le_0": 0.181,
    "n": 72,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.133,
    "ci90": [
      -0.104,
      0.38
    ],
    "p_mean_le_0": 0.181,
    "n": 74,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.02,
    "ci90": [
      -0.019,
      0.06
    ],
    "p_mean_le_0": 0.195,
    "n": 2936,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.04,
    "ci90": [
      -0.005,
      0.089
    ],
    "p_mean_le_0": 0.074,
    "n": 2141,
    "survives_fdr10": false
  },
  "2m/INV/LONG": {
    "expR": -0.152,
    "ci90": [
      -0.467,
      0.17
    ],
    "p_mean_le_0": 0.79,
    "n": 26,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.072,
    "ci90": [
      -0.301,
      0.467
    ],
    "p_mean_le_0": 0.382,
    "n": 37,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.01,
    "ci90": [
      -0.062,
      0.043
    ],
    "p_mean_le_0": 0.625,
    "n": 1363,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.104,
    "ci90": [
      0.036,
      0.171
    ],
    "p_mean_le_0": 0.004,
    "n": 966,
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
    "expR": 0.148,
    "ci90": [
      0.058,
      0.242
    ],
    "p_mean_le_0": 0.003,
    "n": 477,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.076,
    "ci90": [
      -0.039,
      0.198
    ],
    "p_mean_le_0": 0.134,
    "n": 307,
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
      "n": 3156,
      "wrTP1": 45.2,
      "expR": 0.067,
      "pf": 1.13,
      "defining_features": {
        "biasScore": 0.78,
        "emaStack": 0.67,
        "nearEdge": 0.66,
        "hourNY": -0.53
      }
    },
    {
      "id": 2,
      "n": 3076,
      "wrTP1": 46.5,
      "expR": 0.067,
      "pf": 1.14,
      "defining_features": {
        "biasScore": -1.07,
        "emaStack": -0.97,
        "nearEdge": -0.81,
        "structDir": -0.47
      }
    },
    {
      "id": 1,
      "n": 1432,
      "wrTP1": 49.9,
      "expR": -0.009,
      "pf": 0.98,
      "defining_features": {
        "hourNY": 1.29,
        "atrPctUsed": -0.81,
        "emaStack": 0.64,
        "biasScore": 0.58
      }
    },
    {
      "id": 3,
      "n": 903,
      "wrTP1": 43.4,
      "expR": -0.043,
      "pf": 0.91,
      "defining_features": {
        "stretchAtr": 1.8,
        "rvol": 1.68,
        "chopIdx": -1.42,
        "entryZoneTk": -0.24
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
        "n": 23,
        "wrTP1": 56.5,
        "expR": 0.428
      },
      "YM": {
        "n": 26,
        "wrTP1": 38.5,
        "expR": 0.172
      },
      "ES": {
        "n": 7,
        "wrTP1": 42.9,
        "expR": -0.403
      },
      "NQ": {
        "n": 6,
        "wrTP1": 33.3,
        "expR": 0.373
      },
      "GC": {
        "n": 13,
        "wrTP1": 38.5,
        "expR": -0.26
      }
    },
    "expR_spread": 0.831,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 50,
        "wrTP1": 44.0,
        "expR": 0.062
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
        "n": 11,
        "wrTP1": 54.5,
        "expR": 0.155
      }
    },
    "expR_spread": 0.508,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 526,
        "wrTP1": 43.3,
        "expR": 0.051
      },
      "NQ": {
        "n": 632,
        "wrTP1": 44.0,
        "expR": -0.046
      },
      "ES": {
        "n": 548,
        "wrTP1": 44.5,
        "expR": 0.019
      },
      "CL": {
        "n": 891,
        "wrTP1": 45.3,
        "expR": 0.018
      },
      "YM": {
        "n": 386,
        "wrTP1": 42.5,
        "expR": 0.095
      }
    },
    "expR_spread": 0.141,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 319,
        "wrTP1": 43.9,
        "expR": 0.121
      },
      "GC": {
        "n": 466,
        "wrTP1": 45.7,
        "expR": 0.044
      },
      "YM": {
        "n": 766,
        "wrTP1": 46.3,
        "expR": 0.087
      },
      "ES": {
        "n": 588,
        "wrTP1": 44.4,
        "expR": -0.026
      },
      "CL": {
        "n": 48,
        "wrTP1": 33.3,
        "expR": -0.443
      }
    },
    "expR_spread": 0.564,
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
        "n": 5,
        "wrTP1": 60.0,
        "expR": 0.036
      },
      "YM": {
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.673
      },
      "ES": {
        "n": 4,
        "wrTP1": 75.0,
        "expR": 0.49
      },
      "NQ": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.035
      }
    },
    "expR_spread": 1.163,
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
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.545
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
    "expR_spread": 1.005,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 316,
        "wrTP1": 48.7,
        "expR": 0.009
      },
      "GC": {
        "n": 182,
        "wrTP1": 44.5,
        "expR": -0.005
      },
      "CL": {
        "n": 429,
        "wrTP1": 50.6,
        "expR": 0.045
      },
      "ES": {
        "n": 261,
        "wrTP1": 44.8,
        "expR": -0.109
      },
      "YM": {
        "n": 192,
        "wrTP1": 41.1,
        "expR": -0.037
      }
    },
    "expR_spread": 0.154,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 237,
        "wrTP1": 51.9,
        "expR": 0.1
      },
      "YM": {
        "n": 377,
        "wrTP1": 50.7,
        "expR": 0.135
      },
      "GC": {
        "n": 178,
        "wrTP1": 48.3,
        "expR": 0.065
      },
      "NQ": {
        "n": 169,
        "wrTP1": 46.2,
        "expR": 0.144
      },
      "CL": {
        "n": 20,
        "wrTP1": 35.0,
        "expR": -0.422
      }
    },
    "expR_spread": 0.566,
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
        "n": 18,
        "wrTP1": 66.7,
        "expR": 0.46
      },
      "ES": {
        "n": 111,
        "wrTP1": 50.5,
        "expR": 0.171
      },
      "YM": {
        "n": 83,
        "wrTP1": 53.0,
        "expR": 0.282
      },
      "CL": {
        "n": 135,
        "wrTP1": 59.3,
        "expR": 0.252
      },
      "NQ": {
        "n": 141,
        "wrTP1": 46.1,
        "expR": -0.089
      }
    },
    "expR_spread": 0.549,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 68,
        "wrTP1": 51.5,
        "expR": 0.038
      },
      "ES": {
        "n": 84,
        "wrTP1": 58.3,
        "expR": 0.152
      },
      "GC": {
        "n": 55,
        "wrTP1": 36.4,
        "expR": -0.124
      },
      "YM": {
        "n": 100,
        "wrTP1": 52.0,
        "expR": 0.19
      },
      "CL": {
        "n": 9,
        "wrTP1": 44.4,
        "expR": -0.323
      }
    },
    "expR_spread": 0.513,
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
    "n": 0
  },
  "away_from_news": {
    "n": 8567,
    "wrTP1": 46.3,
    "nSL": 4123,
    "nTO": 480,
    "expR": 0.043,
    "pf": 1.09,
    "mfe_p25": 7.0,
    "mfe_p50": 16.0,
    "mfe_p75": 39.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.700000000000273,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -12.0,
    "revAfterSL_rate": 33.3
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
      "asOf": "2026-09-13 (domingo, revision semanal). Dato nuevo genuino (+719 pares resueltos en todo el dataset desde ayer, n paso de 7752 a 8471). Sin incidentes de repo hoy (ver nota de proceso en playbooks: hubo un `git pull` con \"forced update\" al iniciar la corrida -- verificado como reescritura upstream de origin/main sin ancestro comun con el commit local; se confirmo con `git log main..origin/main` que la rama remota SUMA commits de 2026-09-10/11/12 que no estaban en el checkout local, y con `git log origin/main..main` que lo que se pierde localmente es una racha de commits duplicados/spam del 2026-09-07 -- superset sin perdida de datos, resuelto con `git checkout -B main origin/main`).",
      "retest_1m_long": {
        "n": 2513,
        "deltaER_orig_minus_layer": 0.152,
        "ci90": [
          0.068,
          0.241
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 2231 a 2513, delta identico a ayer (0.152) -- sexta confirmacion independiente, sigue siendo la lectura mas estable del experimento."
      },
      "retest_1m_short": {
        "n": 1670,
        "deltaER_orig_minus_layer": 0.143,
        "ci90": [
          0.037,
          0.254
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 1560 a 1670, delta subio un poco (0.139->0.143) y el limite inferior del CI90 sigue firme en 0.037 (subio de 0.022) -- segundo dia seguido alejandose de 'al filo'."
      },
      "retest_2m_long": {
        "n": 1231,
        "deltaER_orig_minus_layer": 0.017,
        "ci90": [
          -0.058,
          0.094
        ],
        "ci90_no_cruza_cero": false,
        "nota": "n subio de 1116 a 1231, delta bajo de 0.019 a 0.017 -- septima lectura seguida confirmando que 2m LONG no es candidato."
      },
      "retest_2m_short": {
        "n": 777,
        "deltaER_orig_minus_layer": 0.095,
        "ci90": [
          -0.009,
          0.207
        ],
        "ci90_no_cruza_cero": false,
        "nota": "n subio de 729 a 777, delta bajo un poco (0.11->0.095) y el limite inferior del CI90 volvio a alejarse de cero hacia el lado negativo (-0.001->-0.009) -- sigue siendo el no-candidato mas cerca de flipear, pero hoy se aleja en vez de acercarse."
      },
      "retest_5m_long": {
        "n": 456,
        "deltaER_orig_minus_layer": 0.255,
        "ci90": [
          0.059,
          0.494
        ],
        "ci90_no_cruza_cero": true,
        "nota": "TERCERA LECTURA SEGUIDA CERTIFICANDO (09-11, 09-12 y hoy): n subio de 378 a 456, delta MEJORO de nuevo (0.187->0.255), CI90 [0.028,0.363] -> [0.059,0.494] (mas lejos de cero todavia). Cumple hoy la barra mas exigente que el propio next_steps establecio ('una tercera lectura antes de tratarlo al nivel de 1m LONG/SHORT o 5m SHORT') -- se GRADUA de 'candidato experimental' a candidato solido en esta revision semanal, aunque se mantiene la nota de que tuvo 3 vaivenes certifica/no-certifica en su historia (09-08 a 09-11), asi que se marca como 'solido pero con historial volatil' en vez de al mismo nivel que 1m LONG (sexta confirmacion sin un solo vaiven)."
      },
      "retest_5m_short": {
        "n": 266,
        "deltaER_orig_minus_layer": 0.567,
        "ci90": [
          0.145,
          1.115
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 252 a 266, delta practicamente sin cambio (0.588->0.567) y el CI90 se mantiene casi identico ([0.146,1.133]->[0.145,1.115]) -- sigue siendo la lectura mas solida del experimento, ahora con una corrida mas de estabilidad."
      },
      "overall_by_basis_retestBar": {
        "n": 5371,
        "deltaER": 0.144,
        "ci90": [
          0.091,
          0.202
        ],
        "nota": "n subio de 4834 a 5371, delta estable (0.143->0.144) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba."
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
      "2026-09-13 (domingo, REVISION SEMANAL): dato nuevo genuino (+719 pares, sin incidentes de perdida real -- ver nota de proceso en `asOf`, hubo un `git pull` con 'forced update' al iniciar la corrida por una reescritura upstream de `origin/main`, verificada como superset y resuelta sin perder trabajo local). **5m LONG cumple hoy su TERCERA lectura seguida certificando** (delta 0.187->0.255, CI90 cada vez mas lejos de cero) -- se gradua de 'candidato experimental' a candidato SOLIDO, aunque se mantiene la nota de historial volatil (3 vaivenes entre 09-08 y 09-11) como diferencia frente a 1m LONG (sexta confirmacion sin un solo vaiven en su historia). DECISION DE LA REVISION SEMANAL: se propone formalmente a Jesus aplicar el cambio de SL en `scalp_command.pine` (usar `lg_slOrig`/mecha del retest en vez del stop de 3 capas) en los 4 segmentos que certifican de forma estable con n>=20 post-cambio exigido: **1m LONG, 1m SHORT, 5m LONG, 5m SHORT**. 2m LONG y 2m SHORT quedan explicitamente fuera de la propuesta (septima y octava lectura sin certificar de forma estable). Se anadieron 4 lineas a `predictions.jsonl` (una por segmento, `predictedDeltaER` = delta medido hoy) para poder puntuar el acierto una vez Jesus aplique el cambio y se junte muestra post-cambio (afterN>=40, marcar `experimental` hasta 40+ muestras y 2 semanas consecutivas en la misma direccion, per agent-instructions.md). Ver `reviews/2026-week-37.md` para el detalle completo de la revision. Status del experimento se mantiene en `proposed` (no aplicado todavia en TradingView, `changeDate` sigue null) -- pasara a medirse antes/despues (y potencialmente a `confirmed`) recien cuando Jesus ponga fecha de cambio en los graficos."
    ],
    "beforeN": 8335,
    "afterN": 0,
    "before": {
      "n": 8335,
      "wrTP1": 46.2,
      "nSL": 4022,
      "nTO": 460,
      "expR": 0.04,
      "pf": 1.08,
      "mfe_p25": 7.0,
      "mfe_p50": 16.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
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
    "date": "2026-09-14",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-13T19:12:17-05:00",
    "schema": "sa-plan-2",
    "cleanest": "GC",
    "focus": {
      "sym": "GC",
      "verdict": "WAIT",
      "window": "hasta Londres (~01:25 CT)",
      "setup": {
        "es": "sin zona tactica anotada cerca del precio -- GC rompio su unico soporte (POC/VWAP 4386-4396) y el sesgo fusionado paso a FUERTE bajista (el mas claro del bus); vigila una reaccion en VAL 4371.9, a solo 1.4pts",
        "en": "no tactical zone scored near price -- GC broke its only support (POC/VWAP 4386-4396) and the fused bias flipped to FUERTE bearish (the clearest read on the bus); watch for a reaction at VAL 4371.9, just 1.4pts away"
      },
      "trigger": {
        "es": "reaccion real en VAL 4371.9: mecha con cierre 5m de vuelta sobre 4372, o ruptura limpia con seguimiento hacia PDL 4354.7",
        "en": "a real reaction at VAL 4371.9: a wick with a 5m close back above 4372, or a clean break with follow-through toward PDL 4354.7"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 4396 (POC/VWAP) revalida el intento largo que se acaba de romper",
        "en": "a 5m close sustained above 4396 (POC/VWAP) revalidates the long attempt that just broke"
      },
      "note": {
        "es": "ninguna zona A+/B del plan del pre-asia sigue viva a este precio en ningun instrumento del bus -- el gap de reapertura borro el mapa completo; sin GO hasta que Londres traiga una zona fresca (corrida pre-london 01:25 CT)",
        "en": "no A+/B zone from the pre-asia plan is still alive at this price on any bus instrument -- the reopen gap erased the whole map; no GO until London brings a fresh zone (pre-london run at 01:25 CT)"
      }
    },
    "summary": {
      "es": [
        "NQ: gap bajista de 394pts (grande) en la reapertura, atraveso 29278 y su zona de retest sin sostener, cae a 29017.50 bajo el minimo del viernes; corto de fondo reabierto, sin zona tactica cerca.",
        "ES: mismo guion, gap de 51.5pts, perdio 7626 (su invalidacion) y el retest 7642-7660, cotiza en 7615.50; corto de 3 dias reabierto.",
        "GC: gap bajista de 15pts, rompio tambien su unica zona tactica (POC/VWAP 4386-4396) y cae a 4373.30, a 1.4pts de VAL; sesgo fusionado ahora FUERTE a la baja, el mas claro del bus.",
        "YM: gap bajista de 200pts, perdio el golden/VAL y su invalidacion (52469), cae a 52440 -- fue el primero en romper, tal como anticipaba el counterCase (su marco diario propio nunca confirmo el alza).",
        "CL: guion opuesto, gap alcista de 2.26pts, reclamo 100.04 y rompio con fuerza 100.64, extendiendose a 102.56; la bisagra se resolvio a favor del largo de fondo.",
        "Todo el mapa de zonas del pre-asia (NQ, ES, YM, GC) quedo invalidado o fuera de alcance en la propia reapertura de las 17:00 CT; ninguna zona A+/B sigue viva a este precio -- toca esperar a Londres (01:25 CT) 
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 2711,
  "by_verdict": {
    "AVOID": {
      "n": 906,
      "wrTP1": 45.0,
      "nSL": 466,
      "nTO": 32,
      "expR": 0.011,
      "pf": 1.02,
      "mfe_p25": 6.0,
      "mfe_p50": 13.0,
      "mfe_p75": 24.0,
      "winnerMAE_p75": 7.25,
      "winnerMAE_p90": 16.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -9.0,
      "revAfterSL_rate": 35.2
    },
    "GO": {
      "n": 285,
      "wrTP1": 52.6,
      "nSL": 130,
      "nTO": 5,
      "expR": 0.082,
      "pf": 1.18,
      "mfe_p25": 9.0,
      "mfe_p50": 20.5,
      "mfe_p75": 50.25,
      "winnerMAE_p75": 13.75,
      "winnerMAE_p90": 29.099999999999994,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 33.1
    },
    "WAIT": {
      "n": 1520,
      "wrTP1": 48.9,
      "nSL": 685,
      "nTO": 91,
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
      "revAfterSL_rate": 37.2
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.011,
      "ci90": [
        -0.06,
        0.083
      ],
      "p_mean_le_0": 0.408,
      "n": 895
    },
    "GO": {
      "expR": 0.082,
      "ci90": [
        -0.032,
        0.208
      ],
      "p_mean_le_0": 0.117,
      "n": 284
    },
    "WAIT": {
      "expR": 0.081,
      "ci90": [
        0.029,
        0.133
      ],
      "p_mean_le_0": 0.004,
      "n": 1492
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 906,
      "wrTP1": 45.0,
      "nSL": 466,
      "nTO": 32,
      "expR": 0.011,
      "pf": 1.02,
      "mfe_p25": 6.0,
      "mfe_p50": 13.0,
      "mfe_p75": 24.0,
      "winnerMAE_p75": 7.25,
      "winnerMAE_p90": 16.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -9.0,
      "revAfterSL_rate": 35.2
    },
    "GO_or_WAIT": {
      "n": 1805,
      "wrTP1": 49.5,
      "nSL": 815,
      "nTO": 96,
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
      "revAfterSL_rate": 36.6
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.011,
      "ci90": [
        -0.06,
        0.083
      ],
      "p_mean_le_0": 0.408,
      "n": 895
    },
    "GO_or_WAIT": {
      "expR": 0.081,
      "ci90": [
        0.035,
        0.127
      ],
      "p_mean_le_0": 0.002,
      "n": 1776
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
        "n": 426,
        "wrTP1": 50.5,
        "nSL": 202,
        "nTO": 9,
        "expR": 0.067,
        "pf": 1.14,
        "mfe_p25": 6.0,
        "mfe_p50": 11.0,
        "mfe_p75": 22.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -8.0,
        "revAfterSL_rate": 34.2
      },
      "GO": {
        "n": 179,
        "wrTP1": 48.0,
        "nSL": 92,
        "nTO": 1,
        "expR": -0.062,
        "pf": 0.88,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 15.75,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.5,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 38.0
      },
      "WAIT": {
        "n": 780,
        "wrTP1": 52.2,
        "nSL": 327,
        "nTO": 46,
        "expR": 0.192,
        "pf": 1.46,
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
        "n": 101,
        "wrTP1": 60.4,
        "nSL": 36,
        "nTO": 4,
        "expR": 0.304,
        "pf": 1.84,
        "mfe_p25": 9.0,
        "mfe_p50": 26.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -9.0,
        "revAfterSL_rate": 19.4
      },
      "WAIT": {
        "n": 701,
        "wrTP1": 45.2,
        "nSL": 341,
        "nTO": 43,
        "expR": -0.041,
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
        "revAfterSL_rate": 34.9
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```
