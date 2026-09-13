# Scalp CC · report 2026-09-13T01:28Z
- signals=8471 outcomes=8344 pares_resueltos=8471 pendientes=0 huerfanos=25

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: by_tf_kind_side/2m/INV/LONG bajo de n=26 a n=25 desde la corrida previa (agregado, no archivo crudo -- revisar deduplicacion/re-pareo).
- MUESTRA: semana ya cerrada 2026-W36 bajo de n=3183 a n=3140 desde la corrida previa -- vigilar, puede ser deduplicacion.
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.187 vs 0.043, delta 0.144 CI90 [0.091, 0.202], n 5371). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.199 vs 0.065, delta 0.134 CI90 [0.022, 0.254], n 1542). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.081 CI90 [0.029, 0.133], n 1492). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.04, "ci90": [0.017, 0.062], "p_mean_le_0": 0.003, "n": 8319}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 73 | 42.5 | 0.123 | 1.25 | 33 | 13.5 | 8.5 | 21.2 |
| 1m/INV/SHORT | 73 | 46.6 | 0.077 | 1.16 | 34 | 18.0 | 11.0 | 17.6 |
| 1m/RETEST/LONG | 2970 | 44.0 | 0.017 | 1.03 | 1474 | 14.0 | 10.0 | 29.1 |
| 1m/RETEST/SHORT | 2146 | 44.7 | 0.038 | 1.07 | 1048 | 16.0 | 10.0 | 30.8 |
| 2m/INV/LONG | 25 | 44.0 | -0.217 | 0.6 | 13 | 9.0 | 12.5 | 30.8 |
| 2m/INV/SHORT | 35 | 37.1 | 0.044 | 1.08 | 18 | 18.0 | 12.0 | 33.3 |
| 2m/RETEST/LONG | 1377 | 46.8 | -0.012 | 0.98 | 679 | 16.0 | 12.25 | 35.6 |
| 2m/RETEST/SHORT | 961 | 49.3 | 0.106 | 1.23 | 441 | 20.0 | 11.0 | 40.6 |
| 5m/INV/LONG | 10 | 90.0 | 0.849 | 99.0 | 0 | 30.0 | 32.0 | None |
| 5m/INV/SHORT | 5 | 60.0 | -0.186 | 0.54 | 2 | 34.0 | 88.5 | 100.0 |
| 5m/RETEST/LONG | 484 | 52.9 | 0.154 | 1.35 | 210 | 25.0 | 18.25 | 49.0 |
| 5m/RETEST/SHORT | 312 | 51.0 | 0.086 | 1.19 | 138 | 30.0 | 21.0 | 39.1 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 572 | 25.7 | 0.064 | 1.1 | 368 | 28.0 | 15.0 | 20.4 |
| B | 3535 | 46.2 | 0.05 | 1.1 | 1703 | 16.0 | 11.0 | 32.3 |
| C | 4364 | 48.6 | 0.028 | 1.06 | 2019 | 15.0 | 11.0 | 36.2 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 3131 | 48.8 | 0.059 | 1.13 | 1432 | 11.0 | 8.0 | 38.1 |
| London | 1283 | 44.6 | -0.056 | 0.89 | 675 | 17.0 | 11.25 | 31.3 |
| NY | 1408 | 46.3 | 0.168 | 1.35 | 669 | 26.0 | 17.0 | 38.3 |
| Sin KZ | 2649 | 43.3 | -0.005 | 0.99 | 1314 | 18.0 | 13.0 | 26.0 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 2078 | 44.8 | 0.027 | 1.05 | 1029 | 18.0 | 13.0 | 30.9 |
| edge=0 | 3780 | 48.8 | 0.036 | 1.08 | 1770 | 14.0 | 10.0 | 38.2 |
| edge=1 | 2613 | 43.1 | 0.055 | 1.11 | 1291 | 18.0 | 13.0 | 27.9 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 8461 | 46.0 | 0.039 | 1.08 | 4089 | 16.0 | 11.0 | 33.1 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 46 | 47.8 | 0.04 | 1.08 | 22 | 10.0 | 8.75 | 31.8 |
| INV/LONG|edge=1 | 58 | 46.6 | 0.143 | 1.35 | 22 | 22.0 | 18.0 | 13.6 |
| INV/SHORT|edge=-1 | 67 | 40.3 | 0.146 | 1.3 | 33 | 22.0 | 11.5 | 21.2 |
| INV/SHORT|edge=0 | 43 | 51.2 | -0.051 | 0.89 | 19 | 11.0 | 21.5 | 36.8 |
| INV/SHORT|edge=1 | 3 | 33.3 | -0.527 | 0.21 | 2 | 8.0 | 5.0 | 0.0 |
| RETEST/LONG|edge=-1 | 217 | 48.8 | 0.058 | 1.13 | 97 | 11.0 | 8.0 | 49.5 |
| RETEST/LONG|edge=0 | 2184 | 48.9 | -0.018 | 0.96 | 1053 | 13.0 | 11.0 | 37.9 |
| RETEST/LONG|edge=1 | 2430 | 42.5 | 0.056 | 1.11 | 1213 | 18.0 | 13.0 | 27.0 |
| RETEST/SHORT|edge=-1 | 1790 | 44.4 | 0.018 | 1.03 | 897 | 20.0 | 14.0 | 29.2 |
| RETEST/SHORT|edge=0 | 1507 | 48.6 | 0.118 | 1.25 | 676 | 16.0 | 10.0 | 39.1 |
| RETEST/SHORT|edge=1 | 122 | 53.3 | 0.008 | 1.02 | 54 | 14.0 | 9.0 | 55.6 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 28 | 42.9 | 0.132 | 1.3 | 11 | 21.0 | 18.0 | 9.1 |
| INV/LONG|tier=C | 80 | 48.8 | 0.104 | 1.23 | 35 | 13.0 | 11.5 | 28.6 |
| INV/SHORT|tier=B | 38 | 47.4 | 0.192 | 1.41 | 18 | 18.5 | 8.75 | 5.6 |
| INV/SHORT|tier=C | 75 | 42.7 | -0.017 | 0.97 | 36 | 16.0 | 24.25 | 36.1 |
| RETEST/LONG|tier=A+ | 348 | 25.0 | 0.07 | 1.11 | 219 | 23.0 | 17.0 | 17.4 |
| RETEST/LONG|tier=B | 1997 | 45.4 | 0.064 | 1.13 | 967 | 15.0 | 11.0 | 32.4 |
| RETEST/LONG|tier=C | 2486 | 48.8 | -0.017 | 0.96 | 1177 | 14.0 | 12.0 | 35.9 |
| RETEST/SHORT|tier=A+ | 224 | 26.8 | 0.055 | 1.08 | 149 | 37.0 | 12.25 | 24.8 |
| RETEST/SHORT|tier=B | 1472 | 47.4 | 0.027 | 1.05 | 707 | 17.0 | 12.0 | 33.2 |
| RETEST/SHORT|tier=C | 1723 | 48.5 | 0.092 | 1.2 | 771 | 17.0 | 11.0 | 36.8 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 108 | 47.2 | 0.111 | 1.25 | 46 | 15.0 | 13.0 | 23.9 |
| INV/SHORT|aligned=1 | 113 | 44.2 | 0.055 | 1.11 | 54 | 18.0 | 12.0 | 25.9 |
| RETEST/LONG|aligned=0 | 10 | 50.0 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 4821 | 45.7 | 0.022 | 1.04 | 2362 | 15.0 | 11.0 | 32.8 |
| RETEST/SHORT|aligned=1 | 3419 | 46.6 | 0.061 | 1.13 | 1627 | 18.0 | 11.0 | 34.2 |

## Autopsia de SL
n_losses=4090  causas: RR-bajo×1555, contra-estructura×1433, stop-en-el-minimo×1355, killzone-Asia-largo×841, sin-nivel-detras×805, estirado×694, chop×591, SL-muy-pegado×512, sin-causa-clara×402, contra-sesgo×1
- INV/LONG (n=46): killzone-Asia-largo×22, RR-bajo×21, contra-estructura×14, stop-en-el-minimo×11, estirado×10, sin-nivel-detras×7, chop×4, SL-muy-pegado×4, sin-causa-clara×1
- INV/SHORT (n=54): RR-bajo×26, contra-estructura×18, stop-en-el-minimo×14, sin-causa-clara×11, estirado×9, SL-muy-pegado×7, chop×4, sin-nivel-detras×4
- RETEST/LONG (n=2363): RR-bajo×905, contra-estructura×875, killzone-Asia-largo×819, stop-en-el-minimo×774, sin-nivel-detras×481, estirado×382, chop×373, SL-muy-pegado×286, sin-causa-clara×180, contra-sesgo×1
- RETEST/SHORT (n=1627): RR-bajo×603, stop-en-el-minimo×556, contra-estructura×526, sin-nivel-detras×313, estirado×293, SL-muy-pegado×215, chop×210, sin-causa-clara×210

## Autopsia de SL · semana 2026-W37 (para revision semanal)
n_losses=2547  causas: RR-bajo×932, contra-estructura×841, stop-en-el-minimo×824, sin-nivel-detras×483, estirado×437, killzone-Asia-largo×387, chop×371, SL-muy-pegado×335, sin-causa-clara×271
ejemplos por causa: {"RR-bajo": ["YM-1-22917-S", "ES-1-24101-S", "ES-1-24139-S", "ES-1-24180-S", "ES-5-21264-S"], "contra-estructura": ["ES-1-24101-S", "ES-1-24139-S", "YM-1-23418-S", "YM-1-23425-S", "ES-1-24758-L"], "stop-en-el-minimo": ["YM-1-22701-S", "YM-1-22704-S", "ES-1-23866-S", "ES-1-24139-S", "ES-1-24180-S"]}

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
    "n": 8305,
    "naive_expR": 0.04,
    "managed_expR": 0.126,
    "delta": 0.086,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 48.1,
    "fill_full_pct": 33.9,
    "m1_rate": 36.4,
    "m2_rate": 23.3,
    "m3_rate": 12.7,
    "beAfterM1_rate": 17.0
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 70,
      "naive_expR": 0.123,
      "managed_expR": 0.263,
      "delta": 0.141,
      "avgEntryBetterTk_p50": 2.1500000000000004,
      "fill_t3plus_pct": 48.6,
      "fill_full_pct": 37.1,
      "m1_rate": 45.7,
      "m2_rate": 30.0,
      "m3_rate": 17.1,
      "beAfterM1_rate": 21.4
    },
    "1m/INV/SHORT": {
      "n": 71,
      "naive_expR": 0.077,
      "managed_expR": 0.301,
      "delta": 0.224,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 56.3,
      "fill_full_pct": 43.7,
      "m1_rate": 36.6,
      "m2_rate": 26.8,
      "m3_rate": 16.9,
      "beAfterM1_rate": 12.7
    },
    "1m/RETEST/LONG": {
      "n": 2918,
      "naive_expR": 0.017,
      "managed_expR": 0.11,
      "delta": 0.093,
      "avgEntryBetterTk_p50": 2.4,
      "fill_t3plus_pct": 49.5,
      "fill_full_pct": 35.5,
      "m1_rate": 35.3,
      "m2_rate": 22.1,
      "m3_rate": 11.8,
      "beAfterM1_rate": 16.3
    },
    "1m/RETEST/SHORT": {
      "n": 2093,
      "naive_expR": 0.039,
      "managed_expR": 0.152,
      "delta": 0.113,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 49.0,
      "fill_full_pct": 33.9,
      "m1_rate": 39.4,
      "m2_rate": 24.8,
      "m3_rate": 13.9,
      "beAfterM1_rate": 18.4
    },
    "2m/INV/LONG": {
      "n": 25,
      "naive_expR": -0.217,
      "managed_expR": -0.2,
      "delta": 0.017,
      "avgEntryBetterTk_p50": 2.2,
      "fill_t3plus_pct": 56.0,
      "fill_full_pct": 36.0,
      "m1_rate": 16.0,
      "m2_rate": 16.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 4.0
    },
    "2m/INV/SHORT": {
      "n": 35,
      "naive_expR": 0.044,
      "managed_expR": 0.066,
      "delta": 0.022,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 48.6,
      "fill_full_pct": 40.0,
      "m1_rate": 28.6,
      "m2_rate": 25.7,
      "m3_rate": 14.3,
      "beAfterM1_rate": 5.7
    },
    "2m/RETEST/LONG": {
      "n": 1357,
      "naive_expR": -0.013,
      "managed_expR": 0.077,
      "delta": 0.09,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 46.4,
      "fill_full_pct": 31.2,
      "m1_rate": 34.0,
      "m2_rate": 21.1,
      "m3_rate": 11.9,
      "beAfterM1_rate": 16.7
    },
    "2m/RETEST/SHORT": {
      "n": 946,
      "naive_expR": 0.106,
      "managed_expR": 0.174,
      "delta": 0.068,
      "avgEntryBetterTk_p50": 2.8499999999999996,
      "fill_t3plus_pct": 48.3,
      "fill_full_pct": 36.0,
      "m1_rate": 37.8,
      "m2_rate": 25.4,
      "m3_rate": 13.7,
      "beAfterM1_rate": 17.0
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
      "n": 473,
      "naive_expR": 0.154,
      "managed_expR": 0.099,
      "delta": -0.055,
      "avgEntryBetterTk_p50": 2.7,
      "fill_t3plus_pct": 37.6,
      "fill_full_pct": 26.8,
      "m1_rate": 34.5,
      "m2_rate": 23.3,
      "m3_rate": 13.1,
      "beAfterM1_rate": 18.4
    },
    "5m/RETEST/SHORT": {
      "n": 302,
      "naive_expR": 0.085,
      "managed_expR": 0.148,
      "delta": 0.063,
      "avgEntryBetterTk_p50": 4.85,
      "fill_t3plus_pct": 47.4,
      "fill_full_pct": 31.5,
      "m1_rate": 36.4,
      "m2_rate": 23.8,
      "m3_rate": 13.6,
      "beAfterM1_rate": 16.9
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 7117,
    "layer_expR": 0.049,
    "orig_expR": 0.193,
    "delta_orig_minus_layer": 0.144,
    "delta_ci90": [
      0.097,
      0.194
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 46.6,
    "orig_wrTP1": 32.4,
    "slTk_p50": 19.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.8,
    "orig_saved_from_SL": 13,
    "orig_caused_SL": 1027
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 204,
      "layer_expR": 0.08,
      "orig_expR": 0.308,
      "delta_orig_minus_layer": 0.228,
      "delta_ci90": [
        -0.128,
        0.656
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 45.6,
      "orig_wrTP1": 25.0,
      "slTk_p50": 18.5,
      "slOrigTk_p50": 4.5,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 42
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
      "n": 5371,
      "layer_expR": 0.043,
      "orig_expR": 0.187,
      "delta_orig_minus_layer": 0.144,
      "delta_ci90": [
        0.091,
        0.202
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.0,
      "orig_wrTP1": 33.0,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.1,
      "orig_saved_from_SL": 13,
      "orig_caused_SL": 765
    },
    "retestBar2": {
      "n": 1542,
      "layer_expR": 0.065,
      "orig_expR": 0.199,
      "delta_orig_minus_layer": 0.134,
      "delta_ci90": [
        0.022,
        0.254
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.3,
      "orig_wrTP1": 31.1,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 2.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 220
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 70,
      "layer_expR": 0.123,
      "orig_expR": 0.076,
      "delta_orig_minus_layer": -0.047,
      "delta_ci90": [
        -0.466,
        0.386
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 44.3,
      "orig_wrTP1": 21.4,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 4.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 16
    },
    "1m/INV/SHORT": {
      "n": 61,
      "layer_expR": 0.081,
      "orig_expR": 0.419,
      "delta_orig_minus_layer": 0.337,
      "delta_ci90": [
        -0.514,
        1.429
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 45.9,
      "orig_wrTP1": 23.0,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 1.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 14
    },
    "1m/RETEST/LONG": {
      "n": 2513,
      "layer_expR": 0.019,
      "orig_expR": 0.171,
      "delta_orig_minus_layer": 0.152,
      "delta_ci90": [
        0.068,
        0.241
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.0,
      "orig_wrTP1": 28.7,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.2,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 387
    },
    "1m/RETEST/SHORT": {
      "n": 1670,
      "layer_expR": 0.054,
      "orig_expR": 0.196,
      "delta_orig_minus_layer": 0.143,
      "delta_ci90": [
        0.037,
        0.254
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.1,
      "orig_wrTP1": 30.9,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 2.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 238
    },
    "2m/INV/LONG": {
      "n": 25,
      "layer_expR": -0.217,
      "orig_expR": 0.892,
      "delta_orig_minus_layer": 1.109,
      "delta_ci90": [
        0.045,
        2.422
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 44.0,
      "orig_wrTP1": 28.0,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 4
    },
    "2m/INV/SHORT": {
      "n": 34,
      "layer_expR": 0.033,
      "orig_expR": 0.503,
      "delta_orig_minus_layer": 0.47,
      "delta_ci90": [
        -0.05,
        1.155
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 35.3,
      "orig_wrTP1": 29.4,
      "slTk_p50": 21.5,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 2
    },
    "2m/RETEST/LONG": {
      "n": 1231,
      "layer_expR": 0.008,
      "orig_expR": 0.025,
      "delta_orig_minus_layer": 0.017,
      "delta_ci90": [
        -0.058,
        0.094
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.8,
      "orig_wrTP1": 33.8,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.2,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 174
    },
    "2m/RETEST/SHORT": {
      "n": 777,
      "layer_expR": 0.128,
      "orig_expR": 0.223,
      "delta_orig_minus_layer": 0.095,
      "delta_ci90": [
        -0.009,
        0.207
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.8,
      "orig_wrTP1": 35.8,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 118
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
      "n": 456,
      "layer_expR": 0.145,
      "orig_expR": 0.4,
      "delta_orig_minus_layer": 0.255,
      "delta_ci90": [
        0.059,
        0.494
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.9,
      "orig_wrTP1": 45.0,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 14.0,
      "orig_wider_pct": 15.8,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 44
    },
    "5m/RETEST/SHORT": {
      "n": 266,
      "layer_expR": 0.069,
      "orig_expR": 0.636,
      "delta_orig_minus_layer": 0.567,
      "delta_ci90": [
        0.145,
        1.115
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.1,
      "orig_wrTP1": 44.4,
      "slTk_p50": 28.0,
      "slOrigTk_p50": 21.5,
      "orig_wider_pct": 19.2,
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
    "n": 5331,
    "wrTP1": 46.8,
    "expR": 0.072
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
      "n": 35,
      "wrTP1": 40.0,
      "expR": -0.052,
      "pf": 0.9
    },
    "1m/INV/SHORT": {
      "n": 54,
      "wrTP1": 38.9,
      "expR": 0.014,
      "pf": 1.03
    },
    "1m/RETEST/LONG": {
      "n": 1600,
      "wrTP1": 44.9,
      "expR": 0.042,
      "pf": 1.08
    },
    "1m/RETEST/SHORT": {
      "n": 1697,
      "wrTP1": 45.0,
      "expR": 0.048,
      "pf": 1.09
    },
    "2m/INV/LONG": {
      "n": 8,
      "wrTP1": 50.0,
      "expR": -0.194,
      "pf": 0.55
    },
    "2m/INV/SHORT": {
      "n": 29,
      "wrTP1": 34.5,
      "expR": 0.108,
      "pf": 1.21
    },
    "2m/RETEST/LONG": {
      "n": 693,
      "wrTP1": 47.5,
      "expR": 0.037,
      "pf": 1.08
    },
    "2m/RETEST/SHORT": {
      "n": 751,
      "wrTP1": 51.8,
      "expR": 0.164,
      "pf": 1.37
    },
    "5m/INV/LONG": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 1.055,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 241,
      "wrTP1": 53.1,
      "expR": 0.223,
      "pf": 1.5
    },
    "5m/RETEST/SHORT": {
      "n": 218,
      "wrTP1": 52.3,
      "expR": 0.128,
      "pf": 1.29
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 7989,
  "brier": 0.2234,
  "bias": -0.13,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.166
    },
    {
      "feature": "stretchAtr",
      "weight": -0.142
    },
    {
      "feature": "rvol",
      "weight": 0.082
    },
    {
      "feature": "biasScore",
      "weight": -0.077
    },
    {
      "feature": "nearTk",
      "weight": -0.07
    },
    {
      "feature": "chopIdx",
      "weight": -0.056
    },
    {
      "feature": "nearEdge",
      "weight": 0.05
    },
    {
      "feature": "structDir",
      "weight": 0.035
    },
    {
      "feature": "aligned",
      "weight": -0.033
    },
    {
      "feature": "hourNY",
      "weight": 0.023
    },
    {
      "feature": "entryZoneTk",
      "weight": 0.008
    },
    {
      "feature": "emaStack",
      "weight": -0.006
    },
    {
      "feature": "atrPctUsed",
      "weight": 0.0
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.169,
      "actual": 0.192,
      "n": 798
    },
    {
      "bin": 1,
      "pred": 0.349,
      "actual": 0.297,
      "n": 799
    },
    {
      "bin": 2,
      "pred": 0.426,
      "actual": 0.329,
      "n": 799
    },
    {
      "bin": 3,
      "pred": 0.474,
      "actual": 0.394,
      "n": 799
    },
    {
      "bin": 4,
      "pred": 0.512,
      "actual": 0.466,
      "n": 799
    },
    {
      "bin": 5,
      "pred": 0.542,
      "actual": 0.552,
      "n": 799
    },
    {
      "bin": 6,
      "pred": 0.566,
      "actual": 0.602,
      "n": 799
    },
    {
      "bin": 7,
      "pred": 0.588,
      "actual": 0.625,
      "n": 799
    },
    {
      "bin": 8,
      "pred": 0.612,
      "actual": 0.711,
      "n": 799
    },
    {
      "bin": 9,
      "pred": 0.656,
      "actual": 0.713,
      "n": 799
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
    "expR": 0.123,
    "ci90": [
      -0.132,
      0.396
    ],
    "p_mean_le_0": 0.228,
    "n": 70,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.077,
    "ci90": [
      -0.168,
      0.332
    ],
    "p_mean_le_0": 0.315,
    "n": 71,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.017,
    "ci90": [
      -0.022,
      0.056
    ],
    "p_mean_le_0": 0.222,
    "n": 2922,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.038,
    "ci90": [
      -0.008,
      0.087
    ],
    "p_mean_le_0": 0.092,
    "n": 2100,
    "survives_fdr10": false
  },
  "2m/INV/LONG": {
    "expR": -0.217,
    "ci90": [
      -0.521,
      0.102
    ],
    "p_mean_le_0": 0.873,
    "n": 25,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.044,
    "ci90": [
      -0.331,
      0.458
    ],
    "p_mean_le_0": 0.444,
    "n": 35,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.012,
    "ci90": [
      -0.064,
      0.042
    ],
    "p_mean_le_0": 0.646,
    "n": 1359,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.106,
    "ci90": [
      0.037,
      0.173
    ],
    "p_mean_le_0": 0.003,
    "n": 946,
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
    "expR": 0.154,
    "ci90": [
      0.061,
      0.248
    ],
    "p_mean_le_0": 0.003,
    "n": 473,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.086,
    "ci90": [
      -0.027,
      0.208
    ],
    "p_mean_le_0": 0.115,
    "n": 303,
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
      "n": 3120,
      "wrTP1": 45.3,
      "expR": 0.066,
      "pf": 1.13,
      "defining_features": {
        "biasScore": 0.77,
        "emaStack": 0.67,
        "nearEdge": 0.65,
        "hourNY": -0.52
      }
    },
    {
      "id": 2,
      "n": 3001,
      "wrTP1": 46.2,
      "expR": 0.065,
      "pf": 1.13,
      "defining_features": {
        "biasScore": -1.08,
        "emaStack": -0.97,
        "nearEdge": -0.82,
        "structDir": -0.47
      }
    },
    {
      "id": 1,
      "n": 1406,
      "wrTP1": 49.4,
      "expR": -0.017,
      "pf": 0.96,
      "defining_features": {
        "hourNY": 1.31,
        "atrPctUsed": -0.82,
        "emaStack": 0.63,
        "biasScore": 0.58
      }
    },
    {
      "id": 3,
      "n": 944,
      "wrTP1": 43.1,
      "expR": -0.042,
      "pf": 0.92,
      "defining_features": {
        "stretchAtr": 1.75,
        "rvol": 1.6,
        "chopIdx": -1.36,
        "hourNY": -0.28
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
    "expR_spread": 0.803,
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
        "n": 10,
        "wrTP1": 50.0,
        "expR": 0.051
      }
    },
    "expR_spread": 0.327,
    "verdict": "universal"
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
        "n": 879,
        "wrTP1": 44.7,
        "expR": 0.01
      },
      "YM": {
        "n": 385,
        "wrTP1": 42.3,
        "expR": 0.092
      }
    },
    "expR_spread": 0.138,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 297,
        "wrTP1": 41.4,
        "expR": 0.099
      },
      "GC": {
        "n": 451,
        "wrTP1": 45.5,
        "expR": 0.046
      },
      "YM": {
        "n": 765,
        "wrTP1": 46.4,
        "expR": 0.088
      },
      "ES": {
        "n": 585,
        "wrTP1": 44.4,
        "expR": -0.025
      },
      "CL": {
        "n": 48,
        "wrTP1": 33.3,
        "expR": -0.443
      }
    },
    "expR_spread": 0.542,
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
        "n": 5,
        "wrTP1": 60.0,
        "expR": 0.228
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
    "expR_spread": 0.58,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 316,
        "wrTP1": 48.4,
        "expR": 0.009
      },
      "GC": {
        "n": 182,
        "wrTP1": 44.5,
        "expR": -0.005
      },
      "CL": {
        "n": 426,
        "wrTP1": 50.2,
        "expR": 0.04
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
    "expR_spread": 0.149,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 232,
        "wrTP1": 52.6,
        "expR": 0.115
      },
      "YM": {
        "n": 377,
        "wrTP1": 50.7,
        "expR": 0.135
      },
      "GC": {
        "n": 175,
        "wrTP1": 48.6,
        "expR": 0.071
      },
      "NQ": {
        "n": 157,
        "wrTP1": 43.9,
        "expR": 0.129
      },
      "CL": {
        "n": 20,
        "wrTP1": 35.0,
        "expR": -0.422
      }
    },
    "expR_spread": 0.557,
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
        "n": 131,
        "wrTP1": 60.3,
        "expR": 0.278
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
        "n": 66,
        "wrTP1": 51.5,
        "expR": 0.051
      },
      "ES": {
        "n": 82,
        "wrTP1": 59.8,
        "expR": 0.18
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
  "n_events": 10,
  "near_news_30m": {
    "n": 116,
    "wrTP1": 45.7,
    "nSL": 44,
    "nTO": 19,
    "expR": 1.024,
    "pf": 3.7,
    "mfe_p25": 20.75,
    "mfe_p50": 63.0,
    "mfe_p75": 216.0,
    "winnerMAE_p75": 18.0,
    "winnerMAE_p90": 32.800000000000004,
    "loserMFEbeforeSL_p50": 12.5,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -35.0,
    "revAfterSL_rate": 43.2
  },
  "away_from_news": {
    "n": 8355,
    "wrTP1": 46.0,
    "nSL": 4046,
    "nTO": 463,
    "expR": 0.026,
    "pf": 1.05,
    "mfe_p25": 7.0,
    "mfe_p50": 16.0,
    "mfe_p75": 38.0,
    "winnerMAE_p75": 11.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -12.0,
    "revAfterSL_rate": 33.0
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
    "beforeN": 8250,
    "afterN": 0,
    "before": {
      "n": 8250,
      "wrTP1": 46.0,
      "nSL": 3990,
      "nTO": 462,
      "expR": 0.039,
      "pf": 1.08,
      "mfe_p25": 7.0,
      "mfe_p50": 16.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 33.3
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
  "n_matched": 2686,
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
      "n": 260,
      "wrTP1": 49.2,
      "nSL": 127,
      "nTO": 5,
      "expR": 0.028,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 40.5,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 32.3
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
      "expR": 0.028,
      "ci90": [
        -0.089,
        0.149
      ],
      "p_mean_le_0": 0.338,
      "n": 259
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
      "n": 1780,
      "wrTP1": 49.0,
      "nSL": 812,
      "nTO": 96,
      "expR": 0.073,
      "pf": 1.16,
      "mfe_p25": 8.0,
      "mfe_p50": 20.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 28.899999999999977,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.5,
      "revAfterSL_rate": 36.5
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
      "expR": 0.073,
      "ci90": [
        0.026,
        0.12
      ],
      "p_mean_le_0": 0.005,
      "n": 1751
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
