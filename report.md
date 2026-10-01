# Scalp CC · report 2026-10-01T01:19Z
- signals=20790 outcomes=19819 pares_resueltos=20751 pendientes=39 huerfanos=40

## ⚠ ALERTAS (llevar al frente del resumen)
- SIGID: 1308 sigId de senales y 1208 de outcomes colisionan (mismo sigId, receivedAt distinto); 690 tienen result DISTINTO entre ocurrencias -> no es reenvio, son pares reales distintos fusionados en un sigId (ver nota en sigid_collision_report). 'last wins' descarta una ocurrencia y desplaza la otra a una semana posterior: probable causa de las alertas MUESTRA. Arreglar la generacion de sigId en el Pine (deltas en dias casi siempre multiplo de 7, sugiere bar_index que se reinicia semanalmente).
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.217 vs 0.054, delta 0.163 CI90 [0.129, 0.198], n 12831). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.18 vs 0.052, delta 0.128 CI90 [0.065, 0.191], n 4232). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.154 CI90 [0.087, 0.226], n 903). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.063 CI90 [0.036, 0.088], n 5554). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.055, "ci90": [0.041, 0.07], "p_mean_le_0": 0.0, "n": 19779}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Integridad de sigId (colisiones, posible causa de alertas MUESTRA)
```json
{
  "signals": {
    "total_sigIds": 20790,
    "collided_sigIds": 1308,
    "collided_pct": 6.29,
    "delta_days_histogram": {
      "14": 501,
      "7": 471,
      "21": 244,
      "15": 32,
      "28": 28,
      "8": 12,
      "22": 11,
      "29": 3,
      "13": 3,
      "6": 2
    },
    "conflicting_result_n": 0,
    "conflicting_result_examples": []
  },
  "outcomes": {
    "total_sigIds": 19819,
    "collided_sigIds": 1208,
    "collided_pct": 6.1,
    "delta_days_histogram": {
      "14": 477,
      "7": 428,
      "21": 223,
      "28": 27,
      "15": 25,
      "8": 13,
      "22": 9,
      "20": 2,
      "6": 2,
      "29": 1
    },
    "conflicting_result_n": 690,
    "conflicting_result_examples": [
      "NQ-2-22070-L",
      "NQ-2-22078-L",
      "GC-1-23456-S",
      "GC-1-23459-S",
      "YM-1-22698-S",
      "YM-1-22701-S",
      "GC-1-23515-S",
      "GC-1-23566-S"
    ]
  },
  "note": "colision = mismo sigId en >1 archivo diario con receivedAt distinto. 'last wins' en build_pairs() descarta una ocurrencia; si conflicting_result_n>0 confirma que son pares reales distintos, no un reenvio del mismo evento."
}
```

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 183 | 45.9 | 0.185 | 1.43 | 73 | 15.0 | 12.0 | 19.2 |
| 1m/INV/SHORT | 171 | 44.4 | -0.013 | 0.97 | 74 | 20.0 | 15.0 | 17.6 |
| 1m/RETEST/LONG | 7371 | 45.1 | 0.051 | 1.1 | 3476 | 15.0 | 10.0 | 28.2 |
| 1m/RETEST/SHORT | 5372 | 44.9 | 0.048 | 1.1 | 2443 | 18.0 | 11.0 | 31.1 |
| 2m/INV/LONG | 72 | 52.8 | 0.087 | 1.22 | 26 | 15.0 | 14.75 | 19.2 |
| 2m/INV/SHORT | 68 | 41.2 | 0.064 | 1.14 | 30 | 21.0 | 12.5 | 30.0 |
| 2m/RETEST/LONG | 3236 | 46.1 | 0.026 | 1.05 | 1520 | 19.0 | 13.0 | 37.1 |
| 2m/RETEST/SHORT | 2277 | 47.7 | 0.074 | 1.16 | 1022 | 23.0 | 13.0 | 40.3 |
| 5m/INV/LONG | 20 | 70.0 | 0.421 | 3.52 | 3 | 28.5 | 29.0 | 66.7 |
| 5m/INV/SHORT | 14 | 64.3 | 0.383 | 2.53 | 3 | 25.0 | 53.0 | 66.7 |
| 5m/RETEST/LONG | 1158 | 49.4 | 0.108 | 1.24 | 491 | 30.0 | 20.0 | 48.3 |
| 5m/RETEST/SHORT | 809 | 47.5 | 0.092 | 1.2 | 341 | 31.5 | 20.25 | 35.5 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 1456 | 23.6 | 0.025 | 1.04 | 912 | 26.0 | 13.0 | 19.1 |
| B | 9093 | 46.5 | 0.06 | 1.13 | 4125 | 18.0 | 12.0 | 33.1 |
| C | 10202 | 48.5 | 0.054 | 1.12 | 4465 | 18.0 | 13.0 | 35.4 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 7437 | 49.3 | 0.098 | 1.21 | 3319 | 14.0 | 10.0 | 36.5 |
| London | 3091 | 46.1 | 0.038 | 1.08 | 1509 | 18.0 | 12.0 | 33.8 |
| NY | 3666 | 43.8 | 0.046 | 1.09 | 1678 | 26.0 | 16.0 | 36.2 |
| Sin KZ | 6557 | 43.1 | 0.016 | 1.03 | 2996 | 21.0 | 14.0 | 26.5 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 5433 | 44.5 | 0.056 | 1.12 | 2474 | 21.0 | 14.0 | 31.1 |
| edge=0 | 8756 | 48.7 | 0.058 | 1.12 | 3901 | 17.0 | 11.0 | 37.6 |
| edge=1 | 6562 | 43.2 | 0.049 | 1.1 | 3127 | 19.0 | 13.0 | 28.3 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 7 | 57.1 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| aligned=1 | 20744 | 45.9 | 0.055 | 1.11 | 9501 | 18.0 | 12.0 | 32.8 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 107 | 56.1 | 0.199 | 1.53 | 37 | 13.0 | 11.0 | 27.0 |
| INV/LONG|edge=1 | 164 | 45.1 | 0.154 | 1.37 | 63 | 17.0 | 15.0 | 15.9 |
| INV/SHORT|edge=-1 | 153 | 39.2 | -0.04 | 0.92 | 72 | 24.0 | 14.75 | 20.8 |
| INV/SHORT|edge=0 | 91 | 51.6 | 0.078 | 1.19 | 32 | 15.5 | 17.0 | 28.1 |
| INV/SHORT|edge=1 | 9 | 66.7 | 0.69 | 3.07 | 3 | 28.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 441 | 50.6 | 0.128 | 1.28 | 191 | 17.0 | 11.5 | 42.4 |
| RETEST/LONG|edge=0 | 5111 | 48.9 | 0.046 | 1.1 | 2315 | 16.0 | 11.0 | 37.3 |
| RETEST/LONG|edge=1 | 6213 | 42.9 | 0.047 | 1.09 | 2981 | 19.0 | 13.0 | 28.1 |
| RETEST/SHORT|edge=-1 | 4835 | 44.2 | 0.052 | 1.11 | 2209 | 21.0 | 14.0 | 30.5 |
| RETEST/SHORT|edge=0 | 3447 | 48.1 | 0.071 | 1.15 | 1517 | 18.0 | 11.0 | 38.4 |
| RETEST/SHORT|edge=1 | 176 | 51.7 | -0.006 | 0.99 | 80 | 15.0 | 10.5 | 47.5 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 87 | 44.8 | 0.231 | 1.53 | 36 | 16.5 | 14.5 | 8.3 |
| INV/LONG|tier=C | 188 | 51.6 | 0.149 | 1.39 | 66 | 16.0 | 12.0 | 27.3 |
| INV/SHORT|tier=B | 83 | 38.6 | -0.099 | 0.82 | 42 | 19.5 | 12.0 | 7.1 |
| INV/SHORT|tier=C | 170 | 47.6 | 0.092 | 1.22 | 65 | 21.0 | 23.0 | 32.3 |
| RETEST/LONG|tier=A+ | 876 | 22.6 | -0.01 | 0.98 | 572 | 23.0 | 13.0 | 18.4 |
| RETEST/LONG|tier=B | 5043 | 46.1 | 0.068 | 1.14 | 2319 | 17.0 | 12.0 | 32.6 |
| RETEST/LONG|tier=C | 5846 | 49.0 | 0.042 | 1.09 | 2596 | 17.0 | 12.0 | 35.4 |
| RETEST/SHORT|tier=A+ | 580 | 25.2 | 0.08 | 1.12 | 340 | 29.0 | 14.0 | 20.3 |
| RETEST/SHORT|tier=B | 3880 | 47.2 | 0.049 | 1.1 | 1728 | 19.0 | 13.0 | 35.0 |
| RETEST/SHORT|tier=C | 3998 | 47.6 | 0.066 | 1.14 | 1738 | 20.0 | 12.0 | 35.7 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 275 | 49.5 | 0.176 | 1.44 | 102 | 16.0 | 13.0 | 20.6 |
| INV/SHORT|aligned=1 | 253 | 44.7 | 0.028 | 1.06 | 107 | 20.5 | 17.0 | 22.4 |
| RETEST/LONG|aligned=0 | 7 | 57.1 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| RETEST/LONG|aligned=1 | 11758 | 45.8 | 0.049 | 1.1 | 5486 | 17.0 | 12.0 | 32.5 |
| RETEST/SHORT|aligned=1 | 8458 | 45.9 | 0.059 | 1.12 | 3806 | 20.0 | 13.0 | 34.0 |

## Autopsia de SL
n_losses=9502  causas: RR-bajo×3499, contra-estructura×3137, stop-en-el-minimo×3120, killzone-Asia-largo×1971, sin-nivel-detras×1707, estirado×1604, chop×1457, SL-muy-pegado×1201, sin-causa-clara×1087, contra-sesgo×1
- INV/LONG (n=102): killzone-Asia-largo×43, RR-bajo×41, contra-estructura×28, estirado×25, stop-en-el-minimo×21, chop×15, sin-nivel-detras×14, SL-muy-pegado×10, sin-causa-clara×5
- INV/SHORT (n=107): RR-bajo×48, contra-estructura×30, estirado×27, stop-en-el-minimo×24, sin-causa-clara×19, SL-muy-pegado×16, chop×10, sin-nivel-detras×7
- RETEST/LONG (n=5487): RR-bajo×2035, killzone-Asia-largo×1928, contra-estructura×1907, stop-en-el-minimo×1782, sin-nivel-detras×1042, estirado×914, chop×896, SL-muy-pegado×646, sin-causa-clara×504, contra-sesgo×1
- RETEST/SHORT (n=3806): RR-bajo×1375, stop-en-el-minimo×1293, contra-estructura×1172, sin-nivel-detras×644, estirado×638, sin-causa-clara×559, chop×536, SL-muy-pegado×529

## Autopsia de SL · semana 2026-W40 (para revision semanal)
n_losses=1501  causas: RR-bajo×537, stop-en-el-minimo×496, contra-estructura×406, killzone-Asia-largo×265, chop×259, estirado×243, sin-causa-clara×210, SL-muy-pegado×184, sin-nivel-detras×152
ejemplos por causa: {"RR-bajo": ["GC-2-22069-L", "ES-2-22294-S", "YM-1-23306-S", "ES-1-24318-L", "NQ-2-22579-L"], "stop-en-el-minimo": ["YM-2-22154-S", "ES-2-22316-S", "YM-1-23153-S", "YM-1-23306-S", "CL-1-23954-L"], "contra-estructura": ["ES-2-22316-S", "CL-1-23954-L", "NQ-2-22579-L", "NQ-2-22582-L", "NQ-1-24678-L"]}

## Contrafactual de gestion
```json
{
  "n": 7,
  "baseline_nextLevel_expR": 0.236,
  "fixed_1R": [
    0.214,
    7
  ],
  "fixed_1_5R": [
    0.236,
    7
  ],
  "fixed_2R": [
    0.236,
    7
  ],
  "fixed_3R": [
    0.236,
    7
  ],
  "altSL_0_5x_struct": [
    0.205,
    7
  ],
  "altSL_1_5x_struct": [
    0.283,
    7
  ],
  "note": "fixed_XR: R esperado si el objetivo fuera XR fijo con SL=struct. altSL: SL a mult del SL struct."
}
```

## Modelo GESTIONADO (escalera + parciales) vs INGENUO
```json
{
  "overall": {
    "n": 19766,
    "naive_expR": 0.055,
    "managed_expR": 0.132,
    "delta": 0.077,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 46.1,
    "fill_full_pct": 32.7,
    "m1_rate": 37.5,
    "m2_rate": 23.0,
    "m3_rate": 12.0,
    "beAfterM1_rate": 18.3
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 173,
      "naive_expR": 0.185,
      "managed_expR": 0.294,
      "delta": 0.11,
      "avgEntryBetterTk_p50": 2.5,
      "fill_t3plus_pct": 48.0,
      "fill_full_pct": 37.0,
      "m1_rate": 43.4,
      "m2_rate": 26.6,
      "m3_rate": 13.3,
      "beAfterM1_rate": 23.1
    },
    "1m/INV/SHORT": {
      "n": 161,
      "naive_expR": -0.013,
      "managed_expR": 0.194,
      "delta": 0.207,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 53.4,
      "fill_full_pct": 40.4,
      "m1_rate": 36.6,
      "m2_rate": 22.4,
      "m3_rate": 12.4,
      "beAfterM1_rate": 16.8
    },
    "1m/RETEST/LONG": {
      "n": 7122,
      "naive_expR": 0.051,
      "managed_expR": 0.136,
      "delta": 0.085,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 47.9,
      "fill_full_pct": 34.3,
      "m1_rate": 37.9,
      "m2_rate": 23.0,
      "m3_rate": 11.7,
      "beAfterM1_rate": 17.6
    },
    "1m/RETEST/SHORT": {
      "n": 5058,
      "naive_expR": 0.048,
      "managed_expR": 0.175,
      "delta": 0.127,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 47.4,
      "fill_full_pct": 33.1,
      "m1_rate": 39.5,
      "m2_rate": 24.5,
      "m3_rate": 13.4,
      "beAfterM1_rate": 18.8
    },
    "2m/INV/LONG": {
      "n": 68,
      "naive_expR": 0.087,
      "managed_expR": 0.072,
      "delta": -0.016,
      "avgEntryBetterTk_p50": 2.75,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 35.3,
      "m1_rate": 26.5,
      "m2_rate": 17.6,
      "m3_rate": 5.9,
      "beAfterM1_rate": 10.3
    },
    "2m/INV/SHORT": {
      "n": 65,
      "naive_expR": 0.064,
      "managed_expR": 0.109,
      "delta": 0.045,
      "avgEntryBetterTk_p50": 2.4,
      "fill_t3plus_pct": 49.2,
      "fill_full_pct": 36.9,
      "m1_rate": 30.8,
      "m2_rate": 23.1,
      "m3_rate": 15.4,
      "beAfterM1_rate": 10.8
    },
    "2m/RETEST/LONG": {
      "n": 3096,
      "naive_expR": 0.026,
      "managed_expR": 0.06,
      "delta": 0.034,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 45.3,
      "fill_full_pct": 32.1,
      "m1_rate": 34.8,
      "m2_rate": 20.3,
      "m3_rate": 10.2,
      "beAfterM1_rate": 18.0
    },
    "2m/RETEST/SHORT": {
      "n": 2176,
      "naive_expR": 0.074,
      "managed_expR": 0.14,
      "delta": 0.066,
      "avgEntryBetterTk_p50": 2.95,
      "fill_t3plus_pct": 44.7,
      "fill_full_pct": 31.7,
      "m1_rate": 37.4,
      "m2_rate": 23.3,
      "m3_rate": 12.0,
      "beAfterM1_rate": 19.5
    },
    "5m/INV/LONG": {
      "n": 18,
      "naive_expR": 0.421,
      "managed_expR": 0.369,
      "delta": -0.052,
      "avgEntryBetterTk_p50": 0.65,
      "fill_t3plus_pct": 33.3,
      "fill_full_pct": 22.2,
      "m1_rate": 16.7,
      "m2_rate": 11.1,
      "m3_rate": 5.6,
      "beAfterM1_rate": 11.1
    },
    "5m/INV/SHORT": {
      "n": 12,
      "naive_expR": 0.383,
      "managed_expR": 0.459,
      "delta": 0.077,
      "avgEntryBetterTk_p50": 7.050000000000001,
      "fill_t3plus_pct": 58.3,
      "fill_full_pct": 41.7,
      "m1_rate": 25.0,
      "m2_rate": 16.7,
      "m3_rate": 16.7,
      "beAfterM1_rate": 8.3
    },
    "5m/RETEST/LONG": {
      "n": 1080,
      "naive_expR": 0.108,
      "managed_expR": 0.075,
      "delta": -0.033,
      "avgEntryBetterTk_p50": 1.4,
      "fill_t3plus_pct": 34.7,
      "fill_full_pct": 25.7,
      "m1_rate": 35.2,
      "m2_rate": 22.3,
      "m3_rate": 12.0,
      "beAfterM1_rate": 19.4
    },
    "5m/RETEST/SHORT": {
      "n": 737,
      "naive_expR": 0.091,
      "managed_expR": 0.111,
      "delta": 0.021,
      "avgEntryBetterTk_p50": 4.9,
      "fill_t3plus_pct": 41.2,
      "fill_full_pct": 28.0,
      "m1_rate": 36.9,
      "m2_rate": 23.1,
      "m3_rate": 11.3,
      "beAfterM1_rate": 18.2
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 17548,
    "layer_expR": 0.055,
    "orig_expR": 0.205,
    "delta_orig_minus_layer": 0.15,
    "delta_ci90": [
      0.122,
      0.18
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.0,
    "orig_wrTP1": 33.4,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 9.0,
    "orig_wider_pct": 3.9,
    "orig_saved_from_SL": 23,
    "orig_caused_SL": 2580
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 2,
  "invalid_by_seg": {
    "1m/RETEST/LONG": 2
  },
  "by_basis": {
    "candle1": {
      "n": 485,
      "layer_expR": 0.104,
      "orig_expR": 0.099,
      "delta_orig_minus_layer": -0.006,
      "delta_ci90": [
        -0.195,
        0.209
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.7,
      "orig_wrTP1": 26.0,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 4.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 116
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
      "n": 12831,
      "layer_expR": 0.054,
      "orig_expR": 0.217,
      "delta_orig_minus_layer": 0.163,
      "delta_ci90": [
        0.129,
        0.198
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.1,
      "orig_wrTP1": 33.8,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 4.3,
      "orig_saved_from_SL": 22,
      "orig_caused_SL": 1853
    },
    "retestBar2": {
      "n": 4232,
      "layer_expR": 0.052,
      "orig_expR": 0.18,
      "delta_orig_minus_layer": 0.128,
      "delta_ci90": [
        0.065,
        0.191
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.4,
      "orig_wrTP1": 33.0,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 611
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 173,
      "layer_expR": 0.185,
      "orig_expR": 0.019,
      "delta_orig_minus_layer": -0.165,
      "delta_ci90": [
        -0.437,
        0.123
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.6,
      "orig_wrTP1": 22.0,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 46
    },
    "1m/INV/SHORT": {
      "n": 151,
      "layer_expR": -0.017,
      "orig_expR": -0.045,
      "delta_orig_minus_layer": -0.027,
      "delta_ci90": [
        -0.321,
        0.282
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 46.4,
      "orig_wrTP1": 23.8,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 34
    },
    "1m/RETEST/LONG": {
      "n": 6198,
      "layer_expR": 0.048,
      "orig_expR": 0.188,
      "delta_orig_minus_layer": 0.14,
      "delta_ci90": [
        0.092,
        0.194
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.1,
      "orig_wrTP1": 29.6,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 1.1,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 1024
    },
    "1m/RETEST/SHORT": {
      "n": 4348,
      "layer_expR": 0.048,
      "orig_expR": 0.174,
      "delta_orig_minus_layer": 0.126,
      "delta_ci90": [
        0.069,
        0.185
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.3,
      "orig_wrTP1": 32.8,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 629
    },
    "2m/INV/LONG": {
      "n": 68,
      "layer_expR": 0.087,
      "orig_expR": 0.829,
      "delta_orig_minus_layer": 0.742,
      "delta_ci90": [
        -0.064,
        1.711
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 55.9,
      "orig_wrTP1": 30.9,
      "slTk_p50": 24.5,
      "slOrigTk_p50": 5.5,
      "orig_wider_pct": 5.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 17
    },
    "2m/INV/SHORT": {
      "n": 64,
      "layer_expR": 0.058,
      "orig_expR": 0.092,
      "delta_orig_minus_layer": 0.033,
      "delta_ci90": [
        -0.296,
        0.457
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 42.2,
      "orig_wrTP1": 29.7,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 7.5,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 9
    },
    "2m/RETEST/LONG": {
      "n": 2850,
      "layer_expR": 0.03,
      "orig_expR": 0.197,
      "delta_orig_minus_layer": 0.167,
      "delta_ci90": [
        0.106,
        0.228
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.7,
      "orig_wrTP1": 35.7,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.6,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 373
    },
    "2m/RETEST/SHORT": {
      "n": 1938,
      "layer_expR": 0.084,
      "orig_expR": 0.215,
      "delta_orig_minus_layer": 0.131,
      "delta_ci90": [
        0.055,
        0.214
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.3,
      "orig_wrTP1": 36.2,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.9,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 275
    },
    "5m/INV/LONG": {
      "n": 18,
      "layer_expR": 0.421,
      "orig_expR": -0.401,
      "delta_orig_minus_layer": -0.821,
      "delta_ci90": [
        -1.32,
        -0.376
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 77.8,
      "orig_wrTP1": 38.9,
      "slTk_p50": 34.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 16.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 7
    },
    "5m/INV/SHORT": {
      "n": 11,
      "layer_expR": 0.37,
      "orig_expR": -0.335,
      "delta_orig_minus_layer": -0.705,
      "delta_ci90": [
        -1.103,
        -0.326
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 72.7,
      "orig_wrTP1": 45.5,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 18.0,
      "orig_wider_pct": 27.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 3
    },
    "5m/RETEST/LONG": {
      "n": 1040,
      "layer_expR": 0.1,
      "orig_expR": 0.354,
      "delta_orig_minus_layer": 0.255,
      "delta_ci90": [
        0.125,
        0.398
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.0,
      "orig_wrTP1": 43.9,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 18.0,
      "orig_wider_pct": 15.8,
      "orig_saved_from_SL": 8,
      "orig_caused_SL": 102
    },
    "5m/RETEST/SHORT": {
      "n": 689,
      "layer_expR": 0.085,
      "orig_expR": 0.409,
      "delta_orig_minus_layer": 0.324,
      "delta_ci90": [
        0.105,
        0.572
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.7,
      "orig_wrTP1": 43.8,
      "slTk_p50": 30.0,
      "slOrigTk_p50": 23.0,
      "orig_wider_pct": 20.9,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 61
    }
  }
}
```

## Contrafactual de entrada por RR minimo (candidato sc_min_rr, ataca causa RR-bajo)
```json
{
  "1/RETEST/LONG": {
    "baseline": {
      "n": 7082,
      "wrTP1": 46.9,
      "nSL": 3290,
      "nTO": 469,
      "expR": 0.042,
      "pf": 1.09,
      "mfe_p25": 6.0,
      "mfe_p50": 15.0,
      "mfe_p75": 35.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 29.8,
      "ci90": {
        "expR": 0.042,
        "ci90": [
          0.019,
          0.066
        ],
        "p_mean_le_0": 0.0,
        "n": 6842
      }
    },
    "cuts": {
      "1.0": {
        "n": 3481,
        "wrTP1": 30.7,
        "nSL": 2063,
        "nTO": 350,
        "expR": 0.03,
        "pf": 1.05,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 21.5,
        "ci90": {
          "expR": 0.03,
          "ci90": [
            -0.009,
            0.071
          ],
          "p_mean_le_0": 0.108,
          "n": 3332
        }
      },
      "1.2": {
        "n": 2888,
        "wrTP1": 27.8,
        "nSL": 1765,
        "nTO": 321,
        "expR": 0.035,
        "pf": 1.05,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 10.75,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 19.0,
        "ci90": {
          "expR": 0.035,
          "ci90": [
            -0.014,
            0.084
          ],
          "p_mean_le_0": 0.114,
          "n": 2759
        }
      },
      "1.3": {
        "n": 2635,
        "wrTP1": 26.0,
        "nSL": 1638,
        "nTO": 312,
        "expR": 0.026,
        "pf": 1.04,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.6,
        "ci90": {
          "expR": 0.026,
          "ci90": [
            -0.024,
            0.077
          ],
          "p_mean_le_0": 0.197,
          "n": 2509
        }
      },
      "1.5": {
        "n": 2230,
        "wrTP1": 23.6,
        "nSL": 1422,
        "nTO": 282,
        "expR": 0.025,
        "pf": 1.04,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 15.0,
        "ci90": {
          "expR": 0.025,
          "ci90": [
            -0.032,
            0.084
          ],
          "p_mean_le_0": 0.248,
          "n": 2124
        }
      },
      "2.0": {
        "n": 1438,
        "wrTP1": 17.2,
        "nSL": 961,
        "nTO": 229,
        "expR": 0.009,
        "pf": 1.01,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 11.2,
        "ci90": {
          "expR": 0.009,
          "ci90": [
            -0.069,
            0.089
          ],
          "p_mean_le_0": 0.449,
          "n": 1369
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 5121,
      "wrTP1": 47.1,
      "nSL": 2271,
      "nTO": 436,
      "expR": 0.058,
      "pf": 1.12,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 22.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 33.5,
      "ci90": {
        "expR": 0.058,
        "ci90": [
          0.03,
          0.085
        ],
        "p_mean_le_0": 0.001,
        "n": 4834
      }
    },
    "cuts": {
      "1.0": {
        "n": 2472,
        "wrTP1": 31.1,
        "nSL": 1396,
        "nTO": 307,
        "expR": 0.057,
        "pf": 1.09,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 23.4,
        "ci90": {
          "expR": 0.057,
          "ci90": [
            0.006,
            0.108
          ],
          "p_mean_le_0": 0.033,
          "n": 2289
        }
      },
      "1.2": {
        "n": 2041,
        "wrTP1": 28.3,
        "nSL": 1182,
        "nTO": 281,
        "expR": 0.068,
        "pf": 1.11,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 51.25,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 20.8,
        "ci90": {
          "expR": 0.068,
          "ci90": [
            0.006,
            0.126
          ],
          "p_mean_le_0": 0.032,
          "n": 1880
        }
      },
      "1.3": {
        "n": 1872,
        "wrTP1": 26.8,
        "nSL": 1096,
        "nTO": 274,
        "expR": 0.068,
        "pf": 1.11,
        "mfe_p25": 12.0,
        "mfe_p50": 25.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.9,
        "ci90": {
          "expR": 0.068,
          "ci90": [
            0.007,
            0.133
          ],
          "p_mean_le_0": 0.033,
          "n": 1718
        }
      },
      "1.5": {
        "n": 1598,
        "wrTP1": 24.6,
        "nSL": 963,
        "nTO": 242,
        "expR": 0.064,
        "pf": 1.1,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 54.25,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 17.8,
        "ci90": {
          "expR": 0.064,
          "ci90": [
            -0.009,
            0.137
          ],
          "p_mean_le_0": 0.075,
          "n": 1468
        }
      },
      "2.0": {
        "n": 1072,
        "wrTP1": 19.6,
        "nSL": 676,
        "nTO": 186,
        "expR": 0.051,
        "pf": 1.07,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 59.75,
        "winnerMAE_p75": 13.75,
        "winnerMAE_p90": 24.099999999999994,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 12.6,
        "ci90": {
          "expR": 0.051,
          "ci90": [
            -0.045,
            0.144
          ],
          "p_mean_le_0": 0.189,
          "n": 982
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 3135,
      "wrTP1": 47.6,
      "nSL": 1460,
      "nTO": 182,
      "expR": 0.013,
      "pf": 1.03,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 38.6,
      "ci90": {
        "expR": 0.013,
        "ci90": [
          -0.022,
          0.049
        ],
        "p_mean_le_0": 0.271,
        "n": 3003
      }
    },
    "cuts": {
      "1.0": {
        "n": 1415,
        "wrTP1": 30.2,
        "nSL": 860,
        "nTO": 128,
        "expR": -0.007,
        "pf": 0.99,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 54.5,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 31.5,
        "ci90": {
          "expR": -0.007,
          "ci90": [
            -0.075,
            0.062
          ],
          "p_mean_le_0": 0.571,
          "n": 1331
        }
      },
      "1.2": {
        "n": 1155,
        "wrTP1": 26.8,
        "nSL": 735,
        "nTO": 111,
        "expR": -0.017,
        "pf": 0.98,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.19999999999999,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.4,
        "ci90": {
          "expR": -0.017,
          "ci90": [
            -0.094,
            0.06
          ],
          "p_mean_le_0": 0.637,
          "n": 1084
        }
      },
      "1.3": {
        "n": 1053,
        "wrTP1": 25.9,
        "nSL": 674,
        "nTO": 106,
        "expR": -0.003,
        "pf": 1.0,
        "mfe_p25": 11.0,
        "mfe_p50": 23.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.80000000000001,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 27.7,
        "ci90": {
          "expR": -0.003,
          "ci90": [
            -0.086,
            0.083
          ],
          "p_mean_le_0": 0.532,
          "n": 987
        }
      },
      "1.5": {
        "n": 860,
        "wrTP1": 22.6,
        "nSL": 564,
        "nTO": 102,
        "expR": -0.007,
        "pf": 0.99,
        "mfe_p25": 11.0,
        "mfe_p50": 23.0,
        "mfe_p75": 59.75,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 25.5,
        "ci90": {
          "expR": -0.007,
          "ci90": [
            -0.104,
            0.093
          ],
          "p_mean_le_0": 0.559,
          "n": 798
        }
      },
      "2.0": {
        "n": 538,
        "wrTP1": 18.8,
        "nSL": 361,
        "nTO": 76,
        "expR": 0.051,
        "pf": 1.07,
        "mfe_p25": 11.0,
        "mfe_p50": 26.0,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 21.6,
        "ci90": {
          "expR": 0.051,
          "ci90": [
            -0.092,
            0.19
          ],
          "p_mean_le_0": 0.281,
          "n": 493
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 2149,
      "wrTP1": 50.4,
      "nSL": 933,
      "nTO": 132,
      "expR": 0.086,
      "pf": 1.19,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 27.700000000000045,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 44.2,
      "ci90": {
        "expR": 0.086,
        "ci90": [
          0.046,
          0.128
        ],
        "p_mean_le_0": 0.001,
        "n": 2066
      }
    },
    "cuts": {
      "1.0": {
        "n": 989,
        "wrTP1": 34.3,
        "nSL": 563,
        "nTO": 87,
        "expR": 0.107,
        "pf": 1.18,
        "mfe_p25": 15.0,
        "mfe_p50": 31.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.19999999999999,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 36.1,
        "ci90": {
          "expR": 0.107,
          "ci90": [
            0.03,
            0.191
          ],
          "p_mean_le_0": 0.015,
          "n": 945
        }
      },
      "1.2": {
        "n": 810,
        "wrTP1": 30.5,
        "nSL": 483,
        "nTO": 80,
        "expR": 0.096,
        "pf": 1.15,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 32.9,
        "ci90": {
          "expR": 0.096,
          "ci90": [
            -0.001,
            0.188
          ],
          "p_mean_le_0": 0.051,
          "n": 771
        }
      },
      "1.3": {
        "n": 738,
        "wrTP1": 28.7,
        "nSL": 449,
        "nTO": 77,
        "expR": 0.084,
        "pf": 1.13,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 64.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 31.8,
        "ci90": {
          "expR": 0.084,
          "ci90": [
            -0.01,
            0.18
          ],
          "p_mean_le_0": 0.066,
          "n": 701
        }
      },
      "1.5": {
        "n": 617,
        "wrTP1": 25.8,
        "nSL": 388,
        "nTO": 70,
        "expR": 0.074,
        "pf": 1.11,
        "mfe_p25": 17.0,
        "mfe_p50": 33.0,
        "mfe_p75": 69.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 30.2,
        "ci90": {
          "expR": 0.074,
          "ci90": [
            -0.038,
            0.191
          ],
          "p_mean_le_0": 0.138,
          "n": 586
        }
      },
      "2.0": {
        "n": 407,
        "wrTP1": 21.9,
        "nSL": 262,
        "nTO": 56,
        "expR": 0.119,
        "pf": 1.18,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 25.6,
        "ci90": {
          "expR": 0.119,
          "ci90": [
            -0.029,
            0.278
          ],
          "p_mean_le_0": 0.093,
          "n": 385
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 1101,
      "wrTP1": 52.0,
      "nSL": 450,
      "nTO": 79,
      "expR": 0.129,
      "pf": 1.3,
      "mfe_p25": 12.0,
      "mfe_p50": 28.0,
      "mfe_p75": 65.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 40.89999999999998,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -34.0,
      "revAfterSL_rate": 52.7,
      "ci90": {
        "expR": 0.129,
        "ci90": [
          0.069,
          0.189
        ],
        "p_mean_le_0": 0.0,
        "n": 1030
      }
    },
    "cuts": {
      "1.0": {
        "n": 455,
        "wrTP1": 35.8,
        "nSL": 242,
        "nTO": 50,
        "expR": 0.229,
        "pf": 1.39,
        "mfe_p25": 17.0,
        "mfe_p50": 38.0,
        "mfe_p75": 79.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 35.60000000000002,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 49.2,
        "ci90": {
          "expR": 0.229,
          "ci90": [
            0.098,
            0.364
          ],
          "p_mean_le_0": 0.001,
          "n": 413
        }
      },
      "1.2": {
        "n": 379,
        "wrTP1": 34.8,
        "nSL": 201,
        "nTO": 46,
        "expR": 0.29,
        "pf": 1.49,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 79.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 29.900000000000006,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 46.3,
        "ci90": {
          "expR": 0.29,
          "ci90": [
            0.139,
            0.436
          ],
          "p_mean_le_0": 0.001,
          "n": 341
        }
      },
      "1.3": {
        "n": 343,
        "wrTP1": 32.1,
        "nSL": 192,
        "nTO": 41,
        "expR": 0.253,
        "pf": 1.41,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 76.75,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 22.400000000000034,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 45.3,
        "ci90": {
          "expR": 0.253,
          "ci90": [
            0.092,
            0.411
          ],
          "p_mean_le_0": 0.004,
          "n": 310
        }
      },
      "1.5": {
        "n": 288,
        "wrTP1": 30.9,
        "nSL": 162,
        "nTO": 37,
        "expR": 0.292,
        "pf": 1.47,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 76.5,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 23.000000000000014,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 43.2,
        "ci90": {
          "expR": 0.292,
          "ci90": [
            0.105,
            0.484
          ],
          "p_mean_le_0": 0.003,
          "n": 259
        }
      },
      "2.0": {
        "n": 190,
        "wrTP1": 25.3,
        "nSL": 114,
        "nTO": 28,
        "expR": 0.301,
        "pf": 1.45,
        "mfe_p25": 17.0,
        "mfe_p50": 39.0,
        "mfe_p75": 88.75,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 5.5,
        "bars_win_p50": 5.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.5,
        "revAfterSL_rate": 38.6,
        "ci90": {
          "expR": 0.301,
          "ci90": [
            0.055,
            0.55
          ],
          "p_mean_le_0": 0.022,
          "n": 170
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 760,
      "wrTP1": 50.5,
      "nSL": 309,
      "nTO": 67,
      "expR": 0.118,
      "pf": 1.27,
      "mfe_p25": 13.75,
      "mfe_p50": 31.0,
      "mfe_p75": 58.25,
      "winnerMAE_p75": 20.25,
      "winnerMAE_p90": 40.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -29.0,
      "revAfterSL_rate": 38.8,
      "ci90": {
        "expR": 0.118,
        "ci90": [
          0.043,
          0.192
        ],
        "p_mean_le_0": 0.006,
        "n": 700
      }
    },
    "cuts": {
      "1.0": {
        "n": 331,
        "wrTP1": 34.4,
        "nSL": 179,
        "nTO": 38,
        "expR": 0.171,
        "pf": 1.29,
        "mfe_p25": 19.0,
        "mfe_p50": 40.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 21.75,
        "winnerMAE_p90": 40.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 30.7,
        "ci90": {
          "expR": 0.171,
          "ci90": [
            0.023,
            0.328
          ],
          "p_mean_le_0": 0.028,
          "n": 299
        }
      },
      "1.2": {
        "n": 274,
        "wrTP1": 30.7,
        "nSL": 158,
        "nTO": 32,
        "expR": 0.154,
        "pf": 1.24,
        "mfe_p25": 19.0,
        "mfe_p50": 41.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 19.25,
        "winnerMAE_p90": 36.400000000000006,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 27.8,
        "ci90": {
          "expR": 0.154,
          "ci90": [
            -0.019,
            0.321
          ],
          "p_mean_le_0": 0.069,
          "n": 247
        }
      },
      "1.3": {
        "n": 254,
        "wrTP1": 31.1,
        "nSL": 147,
        "nTO": 28,
        "expR": 0.165,
        "pf": 1.26,
        "mfe_p25": 21.0,
        "mfe_p50": 42.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 19.5,
        "winnerMAE_p90": 37.80000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 27.2,
        "ci90": {
          "expR": 0.165,
          "ci90": [
            -0.015,
            0.345
          ],
          "p_mean_le_0": 0.069,
          "n": 231
        }
      },
      "1.5": {
        "n": 208,
        "wrTP1": 28.8,
        "nSL": 121,
        "nTO": 27,
        "expR": 0.176,
        "pf": 1.27,
        "mfe_p25": 22.5,
        "mfe_p50": 45.5,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 19.5,
        "winnerMAE_p90": 35.60000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 24.8,
        "ci90": {
          "expR": 0.176,
          "ci90": [
            -0.037,
            0.401
          ],
          "p_mean_le_0": 0.094,
          "n": 186
        }
      },
      "2.0": {
        "n": 135,
        "wrTP1": 21.5,
        "nSL": 90,
        "nTO": 16,
        "expR": 0.058,
        "pf": 1.08,
        "mfe_p25": 25.0,
        "mfe_p50": 48.0,
        "mfe_p75": 84.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 22.2,
        "ci90": {
          "expR": 0.058,
          "ci90": [
            -0.2,
            0.35
          ],
          "p_mean_le_0": 0.353,
          "n": 123
        }
      }
    }
  }
}
```

## Contrafactual RR minimo · fuera de muestra (mismo split que walk_forward)
```json
{
  "testWeeks": [
    "2026-W39",
    "2026-W40"
  ],
  "1/RETEST/LONG": {
    "baseline": {
      "n": 2729,
      "wrTP1": 45.7,
      "nSL": 1294,
      "nTO": 189,
      "expR": 0.019,
      "pf": 1.04,
      "mfe_p25": 6.25,
      "mfe_p50": 15.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 22.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 29.8,
      "ci90": {
        "expR": 0.019,
        "ci90": [
          -0.018,
          0.057
        ],
        "p_mean_le_0": 0.204,
        "n": 2634
      }
    },
    "cuts": {
      "1.2": {
        "n": 1127,
        "wrTP1": 27.0,
        "nSL": 698,
        "nTO": 125,
        "expR": -0.009,
        "pf": 0.99,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 19.1,
        "ci90": {
          "expR": -0.009,
          "ci90": [
            -0.086,
            0.068
          ],
          "p_mean_le_0": 0.568,
          "n": 1077
        }
      },
      "1.3": {
        "n": 1021,
        "wrTP1": 25.1,
        "nSL": 644,
        "nTO": 121,
        "expR": -0.019,
        "pf": 0.97,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 44.25,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 17.5,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.5,
        "ci90": {
          "expR": -0.019,
          "ci90": [
            -0.101,
            0.067
          ],
          "p_mean_le_0": 0.655,
          "n": 972
        }
      },
      "1.5": {
        "n": 865,
        "wrTP1": 22.4,
        "nSL": 562,
        "nTO": 109,
        "expR": -0.033,
        "pf": 0.95,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 19.400000000000034,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 13.9,
        "ci90": {
          "expR": -0.033,
          "ci90": [
            -0.128,
            0.058
          ],
          "p_mean_le_0": 0.729,
          "n": 825
        }
      },
      "2.0": {
        "n": 553,
        "wrTP1": 16.3,
        "nSL": 374,
        "nTO": 89,
        "expR": -0.053,
        "pf": 0.93,
        "mfe_p25": 7.0,
        "mfe_p50": 19.0,
        "mfe_p75": 44.25,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 13.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 11.0,
        "ci90": {
          "expR": -0.053,
          "ci90": [
            -0.177,
            0.083
          ],
          "p_mean_le_0": 0.751,
          "n": 524
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 2272,
      "wrTP1": 48.5,
      "nSL": 996,
      "nTO": 173,
      "expR": 0.055,
      "pf": 1.12,
      "mfe_p25": 9.0,
      "mfe_p50": 18.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 33.3,
      "ci90": {
        "expR": 0.055,
        "ci90": [
          0.017,
          0.097
        ],
        "p_mean_le_0": 0.005,
        "n": 2162
      }
    },
    "cuts": {
      "1.2": {
        "n": 881,
        "wrTP1": 28.3,
        "nSL": 522,
        "nTO": 110,
        "expR": 0.017,
        "pf": 1.03,
        "mfe_p25": 13.0,
        "mfe_p50": 24.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 20.200000000000017,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 21.1,
        "ci90": {
          "expR": 0.017,
          "ci90": [
            -0.064,
            0.106
          ],
          "p_mean_le_0": 0.373,
          "n": 820
        }
      },
      "1.3": {
        "n": 804,
        "wrTP1": 27.2,
        "nSL": 477,
        "nTO": 108,
        "expR": 0.028,
        "pf": 1.04,
        "mfe_p25": 14.0,
        "mfe_p50": 25.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 13.5,
        "winnerMAE_p90": 20.200000000000017,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.9,
        "ci90": {
          "expR": 0.028,
          "ci90": [
            -0.063,
            0.123
          ],
          "p_mean_le_0": 0.312,
          "n": 745
        }
      },
      "1.5": {
        "n": 683,
        "wrTP1": 24.7,
        "nSL": 420,
        "nTO": 94,
        "expR": 0.009,
        "pf": 1.01,
        "mfe_p25": 14.0,
        "mfe_p50": 24.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 20.200000000000017,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 17.6,
        "ci90": {
          "expR": 0.009,
          "ci90": [
            -0.091,
            0.115
          ],
          "p_mean_le_0": 0.449,
          "n": 634
        }
      },
      "2.0": {
        "n": 439,
        "wrTP1": 17.8,
        "nSL": 291,
        "nTO": 70,
        "expR": -0.075,
        "pf": 0.9,
        "mfe_p25": 14.0,
        "mfe_p50": 24.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 26.299999999999997,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 12.0,
        "ci90": {
          "expR": -0.075,
          "ci90": [
            -0.211,
            0.058
          ],
          "p_mean_le_0": 0.818,
          "n": 407
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 1122,
      "wrTP1": 46.8,
      "nSL": 529,
      "nTO": 68,
      "expR": 0.002,
      "pf": 1.0,
      "mfe_p25": 9.0,
      "mfe_p50": 20.0,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 30.600000000000023,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 40.5,
      "ci90": {
        "expR": 0.002,
        "ci90": [
          -0.055,
          0.06
        ],
        "p_mean_le_0": 0.471,
        "n": 1071
      }
    },
    "cuts": {
      "1.2": {
        "n": 403,
        "wrTP1": 24.6,
        "nSL": 262,
        "nTO": 42,
        "expR": -0.057,
        "pf": 0.92,
        "mfe_p25": 12.0,
        "mfe_p50": 24.5,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 32.4,
        "ci90": {
          "expR": -0.057,
          "ci90": [
            -0.195,
            0.077
          ],
          "p_mean_le_0": 0.756,
          "n": 374
        }
      },
      "1.3": {
        "n": 367,
        "wrTP1": 24.0,
        "nSL": 238,
        "nTO": 41,
        "expR": -0.029,
        "pf": 0.96,
        "mfe_p25": 11.5,
        "mfe_p50": 24.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 29.4,
        "ci90": {
          "expR": -0.029,
          "ci90": [
            -0.17,
            0.122
          ],
          "p_mean_le_0": 0.625,
          "n": 339
        }
      },
      "1.5": {
        "n": 310,
        "wrTP1": 20.3,
        "nSL": 207,
        "nTO": 40,
        "expR": -0.053,
        "pf": 0.93,
        "mfe_p25": 12.0,
        "mfe_p50": 23.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 15.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 27.5,
        "ci90": {
          "expR": -0.053,
          "ci90": [
            -0.206,
            0.123
          ],
          "p_mean_le_0": 0.686,
          "n": 283
        }
      },
      "2.0": {
        "n": 201,
        "wrTP1": 19.4,
        "nSL": 128,
        "nTO": 34,
        "expR": 0.092,
        "pf": 1.13,
        "mfe_p25": 12.0,
        "mfe_p50": 25.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 15.400000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 25.0,
        "ci90": {
          "expR": 0.092,
          "ci90": [
            -0.133,
            0.325
          ],
          "p_mean_le_0": 0.254,
          "n": 178
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 977,
      "wrTP1": 50.8,
      "nSL": 422,
      "nTO": 59,
      "expR": 0.068,
      "pf": 1.15,
      "mfe_p25": 11.0,
      "mfe_p50": 22.5,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 43.8,
      "ci90": {
        "expR": 0.068,
        "ci90": [
          0.009,
          0.129
        ],
        "p_mean_le_0": 0.03,
        "n": 938
      }
    },
    "cuts": {
      "1.2": {
        "n": 382,
        "wrTP1": 29.1,
        "nSL": 236,
        "nTO": 35,
        "expR": -0.023,
        "pf": 0.96,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 7.5,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 31.8,
        "ci90": {
          "expR": -0.023,
          "ci90": [
            -0.146,
            0.101
          ],
          "p_mean_le_0": 0.609,
          "n": 364
        }
      },
      "1.3": {
        "n": 343,
        "wrTP1": 26.5,
        "nSL": 218,
        "nTO": 34,
        "expR": -0.053,
        "pf": 0.92,
        "mfe_p25": 15.0,
        "mfe_p50": 31.0,
        "mfe_p75": 54.75,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.8,
        "ci90": {
          "expR": -0.053,
          "ci90": [
            -0.182,
            0.079
          ],
          "p_mean_le_0": 0.746,
          "n": 326
        }
      },
      "1.5": {
        "n": 287,
        "wrTP1": 22.6,
        "nSL": 193,
        "nTO": 29,
        "expR": -0.103,
        "pf": 0.85,
        "mfe_p25": 16.0,
        "mfe_p50": 31.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 28.5,
        "ci90": {
          "expR": -0.103,
          "ci90": [
            -0.246,
            0.049
          ],
          "p_mean_le_0": 0.875,
          "n": 275
        }
      },
      "2.0": {
        "n": 188,
        "wrTP1": 16.0,
        "nSL": 135,
        "nTO": 23,
        "expR": -0.177,
        "pf": 0.77,
        "mfe_p25": 15.0,
        "mfe_p50": 33.0,
        "mfe_p75": 62.5,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 21.5,
        "ci90": {
          "expR": -0.177,
          "ci90": [
            -0.372,
            0.021
          ],
          "p_mean_le_0": 0.931,
          "n": 179
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 377,
      "wrTP1": 48.3,
      "nSL": 166,
      "nTO": 29,
      "expR": 0.032,
      "pf": 1.07,
      "mfe_p25": 14.0,
      "mfe_p50": 28.5,
      "mfe_p75": 62.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 40.80000000000001,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -32.0,
      "revAfterSL_rate": 50.6,
      "ci90": {
        "expR": 0.032,
        "ci90": [
          -0.075,
          0.138
        ],
        "p_mean_le_0": 0.313,
        "n": 348
      }
    },
    "cuts": {
      "1.2": {
        "n": 122,
        "wrTP1": 27.9,
        "nSL": 76,
        "nTO": 12,
        "expR": 0.032,
        "pf": 1.05,
        "mfe_p25": 19.25,
        "mfe_p50": 37.5,
        "mfe_p75": 71.75,
        "winnerMAE_p75": 20.75,
        "winnerMAE_p90": 26.7,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 43.4,
        "ci90": {
          "expR": 0.032,
          "ci90": [
            -0.233,
            0.306
          ],
          "p_mean_le_0": 0.439,
          "n": 110
        }
      },
      "1.3": {
        "n": 112,
        "wrTP1": 26.8,
        "nSL": 72,
        "nTO": 10,
        "expR": 0.019,
        "pf": 1.03,
        "mfe_p25": 19.25,
        "mfe_p50": 36.0,
        "mfe_p75": 64.75,
        "winnerMAE_p75": 14.75,
        "winnerMAE_p90": 21.500000000000007,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 41.7,
        "ci90": {
          "expR": 0.019,
          "ci90": [
            -0.244,
            0.312
          ],
          "p_mean_le_0": 0.459,
          "n": 102
        }
      },
      "1.5": {
        "n": 94,
        "wrTP1": 26.6,
        "nSL": 61,
        "nTO": 8,
        "expR": 0.054,
        "pf": 1.08,
        "mfe_p25": 22.0,
        "mfe_p50": 36.5,
        "mfe_p75": 64.75,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.5,
        "revAfterSL_rate": 42.6,
        "ci90": {
          "expR": 0.054,
          "ci90": [
            -0.247,
            0.398
          ],
          "p_mean_le_0": 0.403,
          "n": 86
        }
      },
      "2.0": {
        "n": 66,
        "wrTP1": 18.2,
        "nSL": 46,
        "nTO": 8,
        "expR": -0.067,
        "pf": 0.91,
        "mfe_p25": 18.25,
        "mfe_p50": 37.0,
        "mfe_p75": 67.25,
        "winnerMAE_p75": 9.25,
        "winnerMAE_p90": 19.900000000000002,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -21.5,
        "revAfterSL_rate": 41.3,
        "ci90": {
          "expR": -0.067,
          "ci90": [
            -0.481,
            0.348
          ],
          "p_mean_le_0": 0.637,
          "n": 58
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 335,
      "wrTP1": 51.0,
      "nSL": 137,
      "nTO": 27,
      "expR": 0.114,
      "pf": 1.26,
      "mfe_p25": 15.0,
      "mfe_p50": 31.0,
      "mfe_p75": 54.0,
      "winnerMAE_p75": 18.5,
      "winnerMAE_p90": 40.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -29.0,
      "revAfterSL_rate": 36.5,
      "ci90": {
        "expR": 0.114,
        "ci90": [
          -0.002,
          0.227
        ],
        "p_mean_le_0": 0.052,
        "n": 311
      }
    },
    "cuts": {
      "1.2": {
        "n": 123,
        "wrTP1": 31.7,
        "nSL": 72,
        "nTO": 12,
        "expR": 0.142,
        "pf": 1.22,
        "mfe_p25": 19.0,
        "mfe_p50": 40.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 30.200000000000017,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.5,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 25.0,
        "ci90": {
          "expR": 0.142,
          "ci90": [
            -0.101,
            0.411
          ],
          "p_mean_le_0": 0.171,
          "n": 114
        }
      },
      "1.3": {
        "n": 116,
        "wrTP1": 32.8,
        "nSL": 67,
        "nTO": 11,
        "expR": 0.174,
        "pf": 1.28,
        "mfe_p25": 19.75,
        "mfe_p50": 40.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 17.5,
        "winnerMAE_p90": 30.800000000000026,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 25.4,
        "ci90": {
          "expR": 0.174,
          "ci90": [
            -0.088,
            0.444
          ],
          "p_mean_le_0": 0.139,
          "n": 108
        }
      },
      "1.5": {
        "n": 93,
        "wrTP1": 28.0,
        "nSL": 56,
        "nTO": 11,
        "expR": 0.114,
        "pf": 1.17,
        "mfe_p25": 19.0,
        "mfe_p50": 40.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 21.4,
        "ci90": {
          "expR": 0.114,
          "ci90": [
            -0.183,
            0.418
          ],
          "p_mean_le_0": 0.269,
          "n": 85
        }
      },
      "2.0": {
        "n": 62,
        "wrTP1": 17.7,
        "nSL": 43,
        "nTO": 8,
        "expR": -0.054,
        "pf": 0.93,
        "mfe_p25": 25.0,
        "mfe_p50": 44.0,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 13.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 16.3,
        "ci90": {
          "expR": -0.054,
          "ci90": [
            -0.428,
            0.341
          ],
          "p_mean_le_0": 0.607,
          "n": 57
        }
      }
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 2839,
    "wrTP1": 44.9,
    "expR": -0.017
  },
  "2026-W37": {
    "n": 4967,
    "wrTP1": 46.8,
    "expR": 0.075
  },
  "2026-W38": {
    "n": 4511,
    "wrTP1": 46.4,
    "expR": 0.103
  },
  "2026-W39": {
    "n": 5200,
    "wrTP1": 45.7,
    "expR": 0.058
  },
  "2026-W40": {
    "n": 3234,
    "wrTP1": 45.0,
    "expR": 0.018
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 34,
      "wrTP1": 47.1,
      "expR": 0.281,
      "pf": 1.64
    },
    "1m/INV/SHORT": {
      "n": 17,
      "wrTP1": 70.6,
      "expR": 0.243,
      "pf": 1.83
    },
    "1m/RETEST/LONG": {
      "n": 1202,
      "wrTP1": 42.8,
      "expR": -0.016,
      "pf": 0.97
    },
    "1m/RETEST/SHORT": {
      "n": 425,
      "wrTP1": 43.3,
      "expR": -0.017,
      "pf": 0.97
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
      "n": 608,
      "wrTP1": 46.4,
      "expR": -0.053,
      "pf": 0.9
    },
    "2m/RETEST/SHORT": {
      "n": 194,
      "wrTP1": 41.2,
      "expR": -0.105,
      "pf": 0.8
    },
    "5m/INV/LONG": {
      "n": 5,
      "wrTP1": 100.0,
      "expR": 0.674,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 0.018,
      "pf": 1.07
    },
    "5m/RETEST/LONG": {
      "n": 239,
      "wrTP1": 52.3,
      "expR": 0.071,
      "pf": 1.16
    },
    "5m/RETEST/SHORT": {
      "n": 88,
      "wrTP1": 48.9,
      "expR": 0.018,
      "pf": 1.04
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
      "n": 54,
      "wrTP1": 40.7,
      "expR": 0.037,
      "pf": 1.07
    },
    "1m/RETEST/LONG": {
      "n": 1473,
      "wrTP1": 45.3,
      "expR": 0.064,
      "pf": 1.13
    },
    "1m/RETEST/SHORT": {
      "n": 1605,
      "wrTP1": 45.0,
      "expR": 0.042,
      "pf": 1.08
    },
    "2m/INV/LONG": {
      "n": 8,
      "wrTP1": 62.5,
      "expR": 0.115,
      "pf": 1.37
    },
    "2m/INV/SHORT": {
      "n": 31,
      "wrTP1": 35.5,
      "expR": 0.137,
      "pf": 1.27
    },
    "2m/RETEST/LONG": {
      "n": 634,
      "wrTP1": 47.2,
      "expR": 0.029,
      "pf": 1.06
    },
    "2m/RETEST/SHORT": {
      "n": 694,
      "wrTP1": 51.3,
      "expR": 0.148,
      "pf": 1.33
    },
    "5m/INV/LONG": {
      "n": 3,
      "wrTP1": 66.7,
      "expR": 1.3,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 1.212,
      "pf": 5.85
    },
    "5m/RETEST/LONG": {
      "n": 225,
      "wrTP1": 51.6,
      "expR": 0.191,
      "pf": 1.42
    },
    "5m/RETEST/SHORT": {
      "n": 200,
      "wrTP1": 53.0,
      "expR": 0.157,
      "pf": 1.36
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 55,
      "wrTP1": 40.0,
      "expR": -0.128,
      "pf": 0.76
    },
    "1m/INV/SHORT": {
      "n": 21,
      "wrTP1": 42.9,
      "expR": -0.148,
      "pf": 0.72
    },
    "1m/RETEST/LONG": {
      "n": 1837,
      "wrTP1": 48.7,
      "expR": 0.137,
      "pf": 1.31
    },
    "1m/RETEST/SHORT": {
      "n": 948,
      "wrTP1": 42.6,
      "expR": 0.117,
      "pf": 1.25
    },
    "2m/INV/LONG": {
      "n": 15,
      "wrTP1": 53.3,
      "expR": -0.12,
      "pf": 0.61
    },
    "2m/INV/SHORT": {
      "n": 4,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 826,
      "wrTP1": 46.9,
      "expR": 0.052,
      "pf": 1.11
    },
    "2m/RETEST/SHORT": {
      "n": 348,
      "wrTP1": 43.7,
      "expR": 0.014,
      "pf": 1.03
    },
    "5m/INV/LONG": {
      "n": 7,
      "wrTP1": 28.6,
      "expR": -0.478,
      "pf": 0.2
    },
    "5m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 290,
      "wrTP1": 51.4,
      "expR": 0.198,
      "pf": 1.5
    },
    "5m/RETEST/SHORT": {
      "n": 159,
      "wrTP1": 40.3,
      "expR": 0.092,
      "pf": 1.19
    }
  },
  "2026-W39": {
    "1m/INV/LONG": {
      "n": 36,
      "wrTP1": 50.0,
      "expR": 0.749,
      "pf": 3.7
    },
    "1m/INV/SHORT": {
      "n": 42,
      "wrTP1": 50.0,
      "expR": 0.057,
      "pf": 1.15
    },
    "1m/RETEST/LONG": {
      "n": 1962,
      "wrTP1": 44.5,
      "expR": 0.054,
      "pf": 1.11
    },
    "1m/RETEST/SHORT": {
      "n": 1330,
      "wrTP1": 44.7,
      "expR": -0.007,
      "pf": 0.99
    },
    "2m/INV/LONG": {
      "n": 25,
      "wrTP1": 48.0,
      "expR": 0.267,
      "pf": 1.68
    },
    "2m/INV/SHORT": {
      "n": 16,
      "wrTP1": 56.2,
      "expR": 0.511,
      "pf": 3.38
    },
    "2m/RETEST/LONG": {
      "n": 763,
      "wrTP1": 46.4,
      "expR": 0.132,
      "pf": 1.27
    },
    "2m/RETEST/SHORT": {
      "n": 557,
      "wrTP1": 49.2,
      "expR": 0.031,
      "pf": 1.07
    },
    "5m/INV/LONG": {
      "n": 4,
      "wrTP1": 100.0,
      "expR": 0.632,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 3,
      "wrTP1": 66.7,
      "expR": 0.195,
      "pf": 99.0
    },
    "5m/RETEST/LONG": {
      "n": 265,
      "wrTP1": 44.9,
      "expR": 0.071,
      "pf": 1.15
    },
    "5m/RETEST/SHORT": {
      "n": 197,
      "wrTP1": 48.2,
      "expR": 0.097,
      "pf": 1.21
    }
  },
  "2026-W40": {
    "1m/INV/LONG": {
      "n": 22,
      "wrTP1": 59.1,
      "expR": 0.17,
      "pf": 1.51
    },
    "1m/INV/SHORT": {
      "n": 37,
      "wrTP1": 32.4,
      "expR": -0.229,
      "pf": 0.58
    },
    "1m/RETEST/LONG": {
      "n": 897,
      "wrTP1": 41.7,
      "expR": -0.058,
      "pf": 0.89
    },
    "1m/RETEST/SHORT": {
      "n": 1064,
      "wrTP1": 47.7,
      "expR": 0.096,
      "pf": 1.21
    },
    "2m/INV/LONG": {
      "n": 7,
      "wrTP1": 85.7,
      "expR": 0.619,
      "pf": 5.33
    },
    "2m/INV/SHORT": {
      "n": 11,
      "wrTP1": 45.5,
      "expR": -0.165,
      "pf": 0.59
    },
    "2m/RETEST/LONG": {
      "n": 405,
      "wrTP1": 42.2,
      "expR": -0.109,
      "pf": 0.8
    },
    "2m/RETEST/SHORT": {
      "n": 484,
      "wrTP1": 46.3,
      "expR": 0.125,
      "pf": 1.26
    },
    "5m/INV/LONG": {
      "n": 1,
      "wrTP1": 100.0,
      "expR": 0.16,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 2,
      "wrTP1": 50.0,
      "expR": 0.28,
      "pf": 99.0
    },
    "5m/RETEST/LONG": {
      "n": 139,
      "wrTP1": 45.3,
      "expR": -0.075,
      "pf": 0.86
    },
    "5m/RETEST/SHORT": {
      "n": 165,
      "wrTP1": 46.1,
      "expR": 0.034,
      "pf": 1.07
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 19024,
  "brier": 0.2208,
  "bias": -0.096,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.236
    },
    {
      "feature": "nearTk",
      "weight": -0.056
    },
    {
      "feature": "stretchAtr",
      "weight": -0.054
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.039
    },
    {
      "feature": "biasScore",
      "weight": -0.031
    },
    {
      "feature": "rvol",
      "weight": 0.029
    },
    {
      "feature": "emaStack",
      "weight": 0.024
    },
    {
      "feature": "nearEdge",
      "weight": -0.018
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.016
    },
    {
      "feature": "aligned",
      "weight": -0.015
    },
    {
      "feature": "hourNY",
      "weight": -0.007
    },
    {
      "feature": "structDir",
      "weight": 0.003
    },
    {
      "feature": "chopIdx",
      "weight": 0.0
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.154,
      "actual": 0.179,
      "n": 1902
    },
    {
      "bin": 1,
      "pred": 0.357,
      "actual": 0.301,
      "n": 1902
    },
    {
      "bin": 2,
      "pred": 0.443,
      "actual": 0.338,
      "n": 1903
    },
    {
      "bin": 3,
      "pred": 0.491,
      "actual": 0.389,
      "n": 1902
    },
    {
      "bin": 4,
      "pred": 0.532,
      "actual": 0.521,
      "n": 1903
    },
    {
      "bin": 5,
      "pred": 0.563,
      "actual": 0.567,
      "n": 1902
    },
    {
      "bin": 6,
      "pred": 0.588,
      "actual": 0.614,
      "n": 1902
    },
    {
      "bin": 7,
      "pred": 0.609,
      "actual": 0.661,
      "n": 1903
    },
    {
      "bin": 8,
      "pred": 0.629,
      "actual": 0.688,
      "n": 1902
    },
    {
      "bin": 9,
      "pred": 0.656,
      "actual": 0.749,
      "n": 1903
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 12317,
  "testN": 8434,
  "testWeeks": [
    "2026-W39",
    "2026-W40"
  ],
  "model_oos_brier": 0.2208,
  "model_oos_n": 8434,
  "best_scheme_in_sample": {
    "scheme": "nextLevel",
    "trainExpR": 0.063
  },
  "best_scheme_oos_expR": 0.043
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.185,
    "ci90": [
      0.011,
      0.364
    ],
    "p_mean_le_0": 0.035,
    "n": 173,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": -0.013,
    "ci90": [
      -0.158,
      0.137
    ],
    "p_mean_le_0": 0.57,
    "n": 161,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.051,
    "ci90": [
      0.027,
      0.076
    ],
    "p_mean_le_0": 0.0,
    "n": 7126,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.048,
    "ci90": [
      0.02,
      0.076
    ],
    "p_mean_le_0": 0.004,
    "n": 5065,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.087,
    "ci90": [
      -0.121,
      0.292
    ],
    "p_mean_le_0": 0.241,
    "n": 68,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.064,
    "ci90": [
      -0.199,
      0.341
    ],
    "p_mean_le_0": 0.347,
    "n": 65,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.026,
    "ci90": [
      -0.009,
      0.062
    ],
    "p_mean_le_0": 0.117,
    "n": 3097,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.074,
    "ci90": [
      0.028,
      0.12
    ],
    "p_mean_le_0": 0.004,
    "n": 2176,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.421,
    "ci90": [
      0.091,
      0.759
    ],
    "p_mean_le_0": 0.018,
    "n": 18,
    "survives_fdr10": true
  },
  "5m/INV/SHORT": {
    "expR": 0.383,
    "ci90": [
      -0.095,
      0.911
    ],
    "p_mean_le_0": 0.098,
    "n": 12,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.108,
    "ci90": [
      0.045,
      0.171
    ],
    "p_mean_le_0": 0.002,
    "n": 1080,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.092,
    "ci90": [
      0.017,
      0.168
    ],
    "p_mean_le_0": 0.022,
    "n": 738,
    "survives_fdr10": true
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
      "n": 790,
      "wrTP1": 46.6,
      "expR": 0.075,
      "pf": 1.17,
      "defining_features": {
        "rvol": 3.68,
        "stretchAtr": 1.73,
        "chopIdx": -1.31,
        "biasScore": -0.25
      }
    },
    {
      "id": 1,
      "n": 7987,
      "wrTP1": 45.9,
      "expR": 0.056,
      "pf": 1.12,
      "defining_features": {
        "biasScore": -1.06,
        "emaStack": -0.95,
        "nearEdge": -0.84,
        "structDir": -0.42
      }
    },
    {
      "id": 0,
      "n": 8472,
      "wrTP1": 47.2,
      "expR": 0.055,
      "pf": 1.11,
      "defining_features": {
        "biasScore": 0.8,
        "emaStack": 0.73,
        "nearEdge": 0.59,
        "stretchAtr": -0.44
      }
    },
    {
      "id": 3,
      "n": 3502,
      "wrTP1": 42.6,
      "expR": 0.047,
      "pf": 1.09,
      "defining_features": {
        "stretchAtr": 1.1,
        "chopIdx": -1.05,
        "biasScore": 0.54,
        "nearEdge": 0.54
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
        "n": 38,
        "wrTP1": 55.3,
        "expR": 0.611
      },
      "YM": {
        "n": 69,
        "wrTP1": 37.7,
        "expR": 0.232
      },
      "ES": {
        "n": 26,
        "wrTP1": 61.5,
        "expR": 0.132
      },
      "GC": {
        "n": 30,
        "wrTP1": 36.7,
        "expR": -0.316
      },
      "NQ": {
        "n": 20,
        "wrTP1": 50.0,
        "expR": 0.033
      }
    },
    "expR_spread": 0.927,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 94,
        "wrTP1": 37.2,
        "expR": -0.105
      },
      "NQ": {
        "n": 16,
        "wrTP1": 56.2,
        "expR": 0.128
      },
      "ES": {
        "n": 9,
        "wrTP1": 55.6,
        "expR": 0.448
      },
      "GC": {
        "n": 33,
        "wrTP1": 63.6,
        "expR": 0.152
      },
      "CL": {
        "n": 19,
        "wrTP1": 31.6,
        "expR": -0.258
      }
    },
    "expR_spread": 0.706,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 1154,
        "wrTP1": 42.9,
        "expR": 0.021
      },
      "NQ": {
        "n": 1661,
        "wrTP1": 45.1,
        "expR": 0.034
      },
      "ES": {
        "n": 1776,
        "wrTP1": 46.1,
        "expR": 0.047
      },
      "CL": {
        "n": 1607,
        "wrTP1": 45.7,
        "expR": 0.07
      },
      "YM": {
        "n": 1173,
        "wrTP1": 44.9,
        "expR": 0.083
      }
    },
    "expR_spread": 0.062,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 568,
        "wrTP1": 44.5,
        "expR": 0.147
      },
      "GC": {
        "n": 1412,
        "wrTP1": 44.9,
        "expR": 0.057
      },
      "YM": {
        "n": 1613,
        "wrTP1": 45.1,
        "expR": 0.048
      },
      "ES": {
        "n": 1001,
        "wrTP1": 46.4,
        "expR": 0.037
      },
      "CL": {
        "n": 778,
        "wrTP1": 43.1,
        "expR": -0.029
      }
    },
    "expR_spread": 0.176,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 9,
        "wrTP1": 44.4,
        "expR": -0.189
      },
      "CL": {
        "n": 8,
        "wrTP1": 62.5,
        "expR": -0.016
      },
      "YM": {
        "n": 21,
        "wrTP1": 38.1,
        "expR": -0.139
      },
      "ES": {
        "n": 15,
        "wrTP1": 73.3,
        "expR": 0.203
      },
      "NQ": {
        "n": 19,
        "wrTP1": 52.6,
        "expR": 0.434
      }
    },
    "expR_spread": 0.623,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 39,
        "wrTP1": 51.3,
        "expR": 0.267
      },
      "NQ": {
        "n": 9,
        "wrTP1": 44.4,
        "expR": 0.184
      },
      "ES": {
        "n": 8,
        "wrTP1": 25.0,
        "expR": -0.176
      },
      "GC": {
        "n": 7,
        "wrTP1": 14.3,
        "expR": -0.537
      },
      "CL": {
        "n": 5,
        "wrTP1": 20.0,
        "expR": -0.665
      }
    },
    "expR_spread": 0.932,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 770,
        "wrTP1": 45.1,
        "expR": 0.013
      },
      "GC": {
        "n": 482,
        "wrTP1": 45.0,
        "expR": 0.005
      },
      "CL": {
        "n": 733,
        "wrTP1": 48.0,
        "expR": 0.061
      },
      "ES": {
        "n": 712,
        "wrTP1": 47.5,
        "expR": -0.007
      },
      "YM": {
        "n": 539,
        "wrTP1": 44.3,
        "expR": 0.061
      }
    },
    "expR_spread": 0.068,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 453,
        "wrTP1": 46.8,
        "expR": -0.017
      },
      "YM": {
        "n": 684,
        "wrTP1": 49.9,
        "expR": 0.097
      },
      "GC": {
        "n": 567,
        "wrTP1": 50.1,
        "expR": 0.207
      },
      "NQ": {
        "n": 259,
        "wrTP1": 42.5,
        "expR": 0.104
      },
      "CL": {
        "n": 314,
        "wrTP1": 44.3,
        "expR": -0.096
      }
    },
    "expR_spread": 0.303,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": 0.027
      },
      "YM": {
        "n": 5,
        "wrTP1": 100.0,
        "expR": 0.526
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 1.473
      },
      "ES": {
        "n": 4,
        "wrTP1": 75.0,
        "expR": 0.453
      }
    },
    "expR_spread": 1.446,
    "verdict": "instrument-specific"
  },
  "5m/INV/SHORT": {
    "symbols": {
      "NQ": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.85
      },
      "YM": {
        "n": 3,
        "wrTP1": 0.0,
        "expR": -1.0
      },
      "GC": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.755
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.245
      }
    },
    "expR_spread": 1.85,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 128,
        "wrTP1": 48.4,
        "expR": 0.108
      },
      "ES": {
        "n": 249,
        "wrTP1": 49.4,
        "expR": 0.135
      },
      "YM": {
        "n": 194,
        "wrTP1": 51.5,
        "expR": 0.21
      },
      "CL": {
        "n": 248,
        "wrTP1": 51.2,
        "expR": 0.095
      },
      "NQ": {
        "n": 339,
        "wrTP1": 47.2,
        "expR": 0.038
      }
    },
    "expR_spread": 0.172,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 98,
        "wrTP1": 49.0,
        "expR": 0.008
      },
      "ES": {
        "n": 163,
        "wrTP1": 51.5,
        "expR": 0.106
      },
      "GC": {
        "n": 188,
        "wrTP1": 42.0,
        "expR": 0.017
      },
      "YM": {
        "n": 235,
        "wrTP1": 48.9,
        "expR": 0.187
      },
      "CL": {
        "n": 125,
        "wrTP1": 46.4,
        "expR": 0.076
      }
    },
    "expR_spread": 0.179,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 10,
  "near_news_30m": {
    "n": 169,
    "wrTP1": 46.2,
    "nSL": 82,
    "nTO": 9,
    "expR": -0.025,
    "pf": 0.95,
    "mfe_p25": 9.0,
    "mfe_p50": 18.0,
    "mfe_p75": 43.0,
    "winnerMAE_p75": 10.0,
    "winnerMAE_p90": 18.299999999999997,
    "loserMFEbeforeSL_p50": 4.5,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -10.0,
    "revAfterSL_rate": 40.2
  },
  "away_from_news": {
    "n": 20582,
    "wrTP1": 45.9,
    "nSL": 9420,
    "nTO": 1718,
    "expR": 0.055,
    "pf": 1.11,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.8
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 6,
  "mae_deltaER": 0.307,
  "hit_direction_rate": 33.3
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
    "status": "applied",
    "hypothesis": "En RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. HASTA 2026-09-04 esto solo certificaba en SHORT (\"no aplica a largos\"); con la muestra de 2026-09-05 TAMBIEN certifica en 1m LONG, asi que se retira la exclusion dura de BUY RETEST y se deja como 'certifica por tf/side, no generalizar sin mirar la tabla'. 2026-09-06: mismas cifras exactas que 2026-09-05 (n identico) porque no llego dato nuevo. 2026-09-07 (lunes, primer dia con trades GENUINAMENTE nuevos post-restauracion, sin repeticion del bug de heal): retest_1m_long paso de n=1087 a n=1135 (+48 pares nuevos, no restaurados) y el delta se mantiene practicamente igual (0.181->0.183) con el CI90 todavia sin cruzar cero -- esta es la primera confirmacion independiente real que pedia el next_steps anterior. retest_1m_short tambien crecio con dato nuevo (n=219->229) y sigue certificando. 2026-09-08 (martes, primer dia habil COMPLETO post-feriado, salto grande de muestra real): retest_1m_long n=1135->1432 (delta 0.183->0.18, estable, segunda confirmacion independiente); retest_1m_short n=229->514 (delta 0.283->0.417, se hizo MAS fuerte); retest_2m_short CERTIFICA POR PRIMERA VEZ (n=129->260, CI90 dejo de cruzar cero); retest_5m_long CERTIFICA POR PRIMERA VEZ pero al filo (n=224->274, CI90=[0.005,0.36], limite inferior casi cero, vigilar que no se revierta con mas muestra); retest_2m_long sigue sin certificar y el delta bajo a casi cero (0.028->0.01, n=596->742).",
    "param": "sl_basis_retest",
    "from": "3-capas (sc_slbuf x ATR1m + piso sc_floor_atr5 + techo sc_cap_atr5 / sc_cap_adr)",
    "to": "mecha de la vela del retest (lg_slOrig con slBasis=retestBar / retestBar2, crudo)",
    "changeDate": "2026-09-26",
    "segment": {
      "kind": "RETEST"
    },
    "targetMetric": "expR",
    "minAfterN": 40,
    "evidence": {
      "source": "sl_origin_vs_layer.by_basis / by_tf_kind_side (medicion PARALELA: misma entrada y mismos TP, solo se mueve el stop; rMultiple = base 3-capas, rOrig = base mecha del retest). No requiere cambio en TradingView para medir.",
      "asOf": "2026-09-21 (lunes). Primer dia habil con dato nuevo genuino tras el fin de semana (+72 pares en todo el bus). n de pares resueltos subio de 13132 a 13204.",
      "retest_1m_long": {
        "n": 4111,
        "deltaER_orig_minus_layer": 0.147,
        "ci90": [
          0.084,
          0.21
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 4078 a 4111, delta estable (0.152->0.147) -- decimotercera confirmacion."
      },
      "retest_1m_short": {
        "n": 2440,
        "deltaER_orig_minus_layer": 0.153,
        "ci90": [
          0.066,
          0.244
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 2432 a 2440, delta identico (0.153) -- decimotercera confirmacion."
      },
      "retest_2m_long": {
        "n": 1919,
        "deltaER_orig_minus_layer": 0.151,
        "ci90": [
          0.078,
          0.228
        ],
        "ci90_no_cruza_cero": true,
        "nota": "TERCERA lectura consecutiva con dato genuinamente nuevo (primera 09-18, segunda 09-19, el 09-20 fue fin de semana sin trade real y no conto): n subio de 1897 a 1919, delta estable (0.153->0.151), CI90 practicamente igual (limite inferior 0.079->0.078). Cumple el criterio de '2-3 lecturas seguidas' que el experimento se puso a si mismo -- SE PROMUEVE a candidato de la propuesta formal hoy, con la misma advertencia de historial volatil que se le puso a 5m LONG cuando se sumo."
      },
      "retest_2m_short": {
        "n": 1097,
        "deltaER_orig_minus_layer": 0.134,
        "ci90": [
          0.04,
          0.232
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 1092 a 1097, delta identico (0.134), limite inferior del CI90 practicamente igual (0.039->0.04) -- sigue candidato debil/al filo, no se promueve."
      },
      "retest_5m_long": {
        "n": 713,
        "deltaER_orig_minus_layer": 0.276,
        "ci90": [
          0.111,
          0.466
        ],
        "ci90_no_cruza_cero": true,
        "nota": "sin senales 5m LONG nuevas hoy (n identico a ayer, 713) -- no cuenta como lectura independiente nueva, se mantiene en su novena confirmacion."
      },
      "retest_5m_short": {
        "n": 409,
        "deltaER_orig_minus_layer": 0.489,
        "ci90": [
          0.138,
          0.896
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 408 a 409 (+1), delta practicamente identico (0.49->0.489) -- sigue siendo la lectura mas solida del experimento por margen."
      },
      "overall_by_basis_retestBar": {
        "n": 8374,
        "deltaER": 0.175,
        "ci90": [
          0.133,
          0.219
        ],
        "nota": "n subio de 8313 a 8374, delta estable (0.178->0.175) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba."
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
      "2026-09-15 (martes, primer dia habil despues de la reapertura de Globex del domingo, dato genuino): los 4 segmentos propuestos en la revision semanal del 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG suma su octava confirmacion, 1m SHORT y 5m SHORT se mantienen estables, 5m LONG suma su QUINTA lectura seguida certificando (ya el doble del umbral de '2 lecturas seguidas' que se puso el propio experimento el 09-08). Movimiento notable: 2m SHORT se fortalecio (delta 0.093->0.117, CI90 ya no cruza cero) pero su limite inferior (0.014) sigue demasiado pegado a cero para promoverlo -- se mantiene como candidato debil/al filo, fuera de la propuesta hasta una segunda lectura consecutiva lejos de cero. 2m LONG sigue sin certificar (novena lectura). Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView. Nota de mantenimiento (no de dato): se corrigio hoy un bug de analyze.py que hacia que la alerta MUESTRA de 2026-W36/W37 (caida de n ya explicada por dedup, sin perdida de archivo real) se repitiera identica cada corrida para siempre en vez de solo mientras la cifra siguiera empeorando; el efecto se vera desde la proxima corrida.",
      "2026-09-16 (miercoles, dato nuevo genuino, +284 pares resueltos en todo el bus): los 4 segmentos propuestos el 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con `delta_beats_zero=true` y sin ningun retroceso -- 1m LONG suma su NOVENA confirmacion, 1m SHORT y 5m SHORT estables, **5m LONG suma su SEXTA lectura seguida certificando**. 2m SHORT se mantiene exactamente igual (delta 0.117, limite inferior del CI90 baja un poco de 0.014 a 0.011 -- sigue candidato debil/al filo, todavia sin una segunda lectura clara lejos de cero). 2m LONG sigue sin certificar, decima lectura seguida (delta 0.035, CI90 cruza cero). Sin cambios de estado: sigue `proposed`, `changeDate` null. La escalera de ejecucion sigue bloqueada en el peldano 0 (asesor) porque, aun con `gate.readyForLive=true` en 5m/RETEST/LONG (n>=100, E[R]>0, PF>=1.3, WR>=50), este mismo experimento -- la causa de SL dominante en RETEST -- sigue sin un `changeDate` ni muestra post-cambio; ese es exactamente el requisito que falta segun `execution-ladder.md` peldano 2. Nada accionable nuevo para Jesus hoy mas alla de: si va a aplicar el cambio de SL estructural en los 12 graficos, este es el dia con la evidencia mas solida acumulada hasta ahora (6 confirmaciones seguidas en el candidato mas fragil, 5m LONG).",
      "2026-09-17 (jueves, dato nuevo genuino, +1097 pares resueltos en todo el bus, el salto mas grande en varios dias): los 4 segmentos propuestos el 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con `delta_beats_zero=true` y sin ningun retroceso -- 1m LONG suma su DECIMA confirmacion (n=2737->3095, delta 0.15->0.142, CI90 [0.066,0.218]), 1m SHORT sube (n=1971->2085, delta 0.127->0.143, CI90 [0.046,0.247]), 5m LONG suma su SEPTIMA lectura seguida certificando (n=492->555, delta 0.248->0.218, CI90 [0.05,0.403]) y 5m SHORT sigue siendo el efecto mas grande, con margen (n=309->324, delta 0.554->0.514, CI90 [0.133,0.987]). 2m SHORT se mantiene candidato debil/al filo por otra corrida mas (n=895->939, delta 0.117->0.113, limite inferior del CI90 practicamente igual, 0.011 vs 0.012). 2m LONG sigue sin certificar, undecima lectura seguida (n=1327->1477, delta 0.035->0.05, CI90 [-0.018,0.12] -- el delta sube y el limite inferior se acerca a cero, vigilar si se acerca a certificar en las proximas corridas). Nota de gate: la semana ya cerrada 2026-W37 en el segmento 5m/RETEST/LONG (el segmento objetivo del gate de ejecucion) paso de PF=1.44 a PF=1.45 pero perdio 6 pares de muestra por el mismo mecanismo de dedup que ya afectaba los conteos agregados (n=241->235) -- primera vez que se ve este efecto a nivel de segmento individual, sin evidencia de perdida real de archivo (file_integrity_check limpio). Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView. Hallazgo nuevo en paralelo (no de este experimento): por primera vez el veredicto SA=GO certifica con significancia junto a SA=WAIT en el cruce agregado con Session Analyst (ver report.alerts); y en el desglose por kind/side, la rama AVOID de RETEST/LONG cruza a E[R] negativo por primera vez mientras la rama WAIT de RETEST/SHORT cruza a positivo -- ver playbooks para el detalle por lado.",
      "2026-09-18 (viernes): HEAD quedo detached tras el `git pull` porque `origin/main` fue reescrito rio arriba (historia sin ancestro comun con la rama local, primera vez que pasa desde 09-11) -- verificado que el commit remoto contenia todo el trabajo esperado (mismo tip de datos, ultimos 50 commits del bus) antes de resolver con `checkout -B main origin/main`, sin perdida. Dato nuevo genuino grande (+768 pares en todo el dataset). **HALLAZGO PRINCIPAL: retest_2m_long CERTIFICA POR PRIMERA VEZ** tras 11 lecturas seguidas sin lograrlo (delta 0.05->0.074, CI90 [-0.018,0.12]->[0.005,0.145], limite inferior cruza por encima de cero) -- se trata como candidato nuevo y fragil, no se suma todavia a la propuesta formal (mismo criterio de '2-3 lecturas seguidas' que se aplico a 5m LONG en la semana pasada). Los 4 segmentos ya propuestos (1m LONG/SHORT, 5m LONG/SHORT) se mantienen TODOS con `delta_beats_zero=true` y se fortalecen: 1m LONG suma su UNDECIMA confirmacion, 1m SHORT sube de delta 0.143 a 0.155, 5m LONG suma su OCTAVA lectura seguida con un salto notable (0.218->0.312), 5m SHORT estable como el efecto mas grande. 2m SHORT tiene su mejor lectura hasta ahora (limite inferior del CI90 0.011->0.031) pero se mantiene un dia mas como candidato debil antes de promoverlo. Nota de gate: en el segmento objetivo (5m/RETEST/LONG), la semana ya cerrada 2026-W36 volvio a perder 1 par por dedup (n=242, PF=1.18, sigue <1.3) y 2026-W37 tambien perdio 1 par (n=234, pero PF SUBIO a 1.47) -- el dedup a nivel de segmento sigue siendo benigno (sin evidencia de perdida real de archivo) pero ya van 3 corridas seguidas afectando este segmento especifico, vigilar que no erosione la serie. Sin cambios de estado en el experimento: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView -- con 4 segmentos solidos (2 de ellos en su octava/undecima confirmacion sin un solo retroceso desde el 09-13) mas un quinto candidato nuevo (2m LONG), esta es la evidencia acumulada mas fuerte hasta ahora para aplicar el cambio.",
      "2026-09-19 (sabado): salto de dato grande, el mayor en varios dias (n 11452->13092, +1640; el bus asento de una vez los archivos de 2026-09-18, mismo 'forced update' inofensivo de origin/main de siempre). Los 4 segmentos ya propuestos el 09-13 (1m LONG/SHORT, 5m LONG/SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG y 1m SHORT suman su DUODECIMA confirmacion (ambos practicamente sin cambio de delta), 5m LONG su NOVENA lectura seguida (delta baja un poco, 0.312->0.276, sigue muy lejos de cero) y 5m SHORT sigue siendo el efecto mas grande. HALLAZGO DEL DIA: 2m LONG suma su SEGUNDA lectura seguida certificando y se fortalece mucho (delta 0.074->0.153, CI90 limite inferior 0.005->0.079) -- un paso mas cerca de cumplir el criterio de '2-3 lecturas' para sumarse a la propuesta formal (vigilar una tercera lectura). 2m SHORT tiene su mejor lectura hasta ahora (limite inferior del CI90 0.031->0.039) pero se mantiene un dia mas como candidato debil antes de promoverlo. Vista actualizada: candidatos solidos sin cambio = 1m LONG, 1m SHORT, 5m LONG, 5m SHORT (los 4 ya propuestos); candidato experimental en camino de promocion = 2m LONG (segunda lectura, falta una tercera); candidato debil/al filo = 2m SHORT. Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView -- con 4 segmentos solidos y un quinto candidato acercandose (2m LONG en su segunda confirmacion), esta sigue siendo la evidencia mas fuerte acumulada hasta ahora para aplicar el cambio.",
      "2026-09-20 (domingo, REVISION SEMANAL, cierre de 2026-W38): primer fin de semana sin ningun archivo signals/outcomes nuevo desde que arranco el bus -- los +37 pares resueltos de hoy en todo el bus son TIMEOUT forzado de senales pendientes desde el viernes, sin trade real nuevo. Por eso esta medicion (que solo usa pares con outcome real) da exactamente los mismos numeros que ayer en los 6 segmentos RETEST: 1m LONG n=4078 delta=0.152, 1m SHORT n=2432 delta=0.153, 2m LONG n=1897 delta=0.153, 2m SHORT n=1092 delta=0.134, 5m LONG n=713 delta=0.276, 5m SHORT n=408 delta=0.49 -- NO cuenta como una lectura independiente nueva para ningun candidato (2m LONG sigue en su segunda lectura, todavia sin la tercera que pedia el criterio de promocion). Revision semanal completa en reviews/2026-week-38.md: se mantiene la propuesta formal de 4 segmentos (1m LONG/SHORT, 5m LONG/SHORT) sin cambios; 2m LONG y 2m SHORT siguen fuera, mas cerca que nunca pero sin una tercera lectura genuina.",
      "2026-09-21 (lunes, primer dia habil con dato nuevo genuino tras el fin de semana, +72 pares en todo el bus): 1m LONG y 1m SHORT suman su DECIMOTERCERA confirmacion sin ningun retroceso (n=4111 y n=2440). 5m LONG y 5m SHORT no tuvieron senales 5m nuevas hoy (5m LONG n identico 713, 5m SHORT +1 a 409) -- se mantienen en su novena/decima lectura respectivamente, sin avance ni retroceso. HALLAZGO PRINCIPAL: 2m LONG cumple hoy su TERCERA lectura consecutiva con dato genuinamente nuevo sosteniendo la certificacion (delta 0.153->0.151, CI90 practicamente sin cambio) -- se GRADUA de 'candidato experimental, vigilar una tercera lectura' a candidato de la propuesta formal, con la misma advertencia de historial volatil que se le puso a 5m LONG cuando se sumo el 09-13. La propuesta pasa de 4 a 5 segmentos: 1m LONG, 1m SHORT, 2m LONG, 5m LONG, 5m SHORT. 2m SHORT sigue sin alcanzar el mismo umbral (delta identico a ayer, limite inferior del CI90 practicamente sin moverse, 0.039->0.04) -- sigue fuera de la propuesta. Sin cambios de estado: sigue 'proposed', changeDate null, esperando que Jesus aplique el cambio en TradingView -- con 5 segmentos ahora con evidencia solida/experimental, esta es la evidencia acumulada mas fuerte y mas amplia hasta ahora para aplicar el cambio.",
      "2026-09-22 (martes, salto de dato grande y genuino: el bus asento de una vez el lote de +1027 outcomes de 2026-09-21, n total de pares resueltos 13204->14160): los 5 segmentos ya propuestos (1m LONG/SHORT, 2m LONG, 5m LONG/SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG y 1m SHORT suman su DECIMOCUARTA/DECIMOQUINTA confirmacion (n=4493 y n=2611, deltas estables 0.132 y 0.142), 2m LONG suma su CUARTA lectura seguida (n=2081, delta 0.14, practicamente identico a ayer) y 5m LONG/SHORT tienen su primera lectura con dato nuevo desde el 09-21 y ambos se fortalecen (5m LONG delta 0.276->0.299, 5m SHORT delta 0.489->0.455 -- este ultimo baja un poco pero sigue siendo el efecto mas grande). HALLAZGO DEL DIA: 2m SHORT tiene su MEJOR lectura hasta ahora -- el limite inferior del CI90 sube de 0.04 a 0.057 (+42%), la subida mas grande en varias corridas -- pero todavia queda por debajo del rango tipico de graduacion de los 5 segmentos ya promovidos (~0.07-0.08 de limite inferior); se mantiene un dia mas como candidato debil/al filo, mas cerca que nunca. Nota en paralelo (no de este experimento, mismo mecanismo de SL): en INV/LONG (buy-ifvg.md) 1m certifica por primera vez a favor del SL de 3 capas (delta -0.323, CI90 no cruza cero) y 2m certifica por primera vez a favor del SL de vela-1 (delta +1.169, CI90 muy ancho, n=48 todavia chico) -- direcciones opuestas entre si, ninguno accionable todavia, pero primera senal estadistica real de esta medicion fuera de RETEST. Sin cambios de estado en este experimento: sigue 'proposed', changeDate null.",
      "2026-09-24 (jueves, dato nuevo genuino y parejo en los 6 segmentos, +189/+218/+137/+105/+50/+34 en n de 1m LONG/1m SHORT/2m LONG/2m SHORT/5m LONG/5m SHORT respectivamente): los 6 segmentos RETEST se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG n=5025 delta=0.13 CI90=[0.076,0.188], 1m SHORT n=3032 delta=0.146 CI90=[0.071,0.226], 2m LONG n=2299 delta=0.153 CI90=[0.086,0.224], 2m SHORT n=1357 delta=0.138 CI90=[0.052,0.225] (segundo dia seguido sosteniendo la graduacion del 09-23, ya no es lectura de un solo dia), 5m LONG n=827 delta=0.297 CI90=[0.146,0.468], 5m SHORT n=498 delta=0.365 CI90=[0.091,0.706] (sigue siendo el efecto mas grande). Con las 6 ramas certificando de forma estable durante varias semanas seguidas y muestras que van de cientos a miles, este es el experimento mas maduro de todo el bus -- la evidencia acumulada ya no deja ningun segmento RETEST fuera de la propuesta. Sigue 'proposed', changeDate null, esperando que Jesus aplique el cambio de SL estructural (lg_slOrig, mecha del retest) en scalp_command.pine.",
      "2026-09-26 (sabado, dato de 2026-09-25 (viernes) llegando completo, +499/+436/+219/+214/+96/+77 en n de 1m LONG/1m SHORT/2m LONG/2m SHORT/5m LONG/5m SHORT respectivamente): los 6 segmentos RETEST se mantienen TODOS con delta_beats_zero=true y sin ninguna reversion -- 1m LONG n=5545 delta=0.148 CI90=[0.094,0.204] (se fortalece un poco de 0.13), 1m SHORT n=3468 delta=0.15 CI90=[0.083,0.222] (estable), 2m LONG n=2530 delta=0.154 CI90=[0.09,0.223] (estable), 2m SHORT n=1571 delta=0.151 CI90=[0.064,0.244] (se fortalece de 0.138), 5m LONG n=933 delta=0.273 CI90=[0.139,0.43] (baja un poco de 0.297, sigue muy lejos de cero), 5m SHORT n=575 delta=0.363 CI90=[0.097,0.653] (estable, sigue el efecto mas grande). Nota de metodo importante: el mismo dia, el E[R] crudo de SELL RETEST (1m/2m/5m SHORT) se debilito en las tres ramas en `by_tf_kind_side`/`segment_significance` (1m SHORT incluso perdio el CI90-fuera-de-cero por primera vez) -- pero el delta de ESTE experimento (SL estructural vs 3 capas) NO comparte esa debilidad, se mantiene igual o mejor en los tres TF SHORT. Confirma que este experimento mide algo distinto del nivel absoluto de E[R] (compara dos bases de SL con la misma entrada y mismo TP), y es una senal de robustez: la ventaja del SL estructural no depende de que el dia sea bueno o malo para SHORT. Incidente de repo distinto a los anteriores: el harness bloqueo `checkout -B`/`reset --hard` como destruccion local irreversible; resuelto sin perder nada con `git merge origin/main --allow-unrelated-histories -X theirs` (arbol final identico a origin/main). Mejora permanente a analyze.py: nueva funcion `shadow_weekly()` (desglosa el modo sombra por semana ISO) -- primer resultado, no de este experimento pero relacionado: el modo sombra actual (que todavia NO incorpora este SL estructural, sigue usando el stop de 3 capas del indicador) le gano al indicador crudo 3 semanas seguidas (W36-W38) pero perdio esta semana (W39 parcial) -- otro argumento a favor de aplicar el cambio de SL antes de subir de peldano. Sigue 'proposed', changeDate null.",
      "2026-09-27 (domingo, REVISION SEMANAL, cierre 2026-W39): primer dia sin trade nuevo desde el cambio (aplicado ayer sabado, fin de semana sin sesion CME) -- prediction_scoreboard confirma appliedDate=2026-09-26 en las 6 lineas de predictions.jsonl (4 de W37 + 2 nuevas de 2m LONG/SHORT anadidas hoy), todas en status 'accruing' con afterN=0, como se esperaba. Antes del cambio, los 6 segmentos RETEST cerraron su ultima lectura in-sample con delta_orig_minus_layer/CI90: 1m LONG 0.148 [0.094,0.204] n=5545, 1m SHORT 0.15 [0.083,0.222] n=3468, 2m LONG 0.154 [0.09,0.223] n=2530, 2m SHORT 0.151 [0.064,0.244] n=1571, 5m LONG 0.273 [0.139,0.43] n=933, 5m SHORT 0.363 [0.097,0.653] n=575 -- sin ninguna reversion en ninguno de los 6 en toda su historia de confirmaciones. sl_origin_vs_layer sigue corriendo la medicion paralela (rMultiple=3-capas, rOrig=mecha) independiente del cambio real en TradingView, asi que se puede seguir comparando ambos stops aunque el SL real ya cambio -- util para verificar que el efecto medido en produccion coincide con lo medido in-sample. Primer chequeo real: esperar hasta que haya trades del lunes 2026-09-28 en adelante (afterN>=20 minimo, 40 para no marcarlo 'experimental' segun agent-instructions.md) antes de poder comparar antes/despues real. Nada que decidir hoy sobre este experimento mas alla de seguir vigilando el scoreboard cada corrida.",
      "2026-09-28 (lunes, primer dia con trades reales bajo el SL nuevo -- el cambio se aplico el sabado 2026-09-26 y no hubo sesion CME el domingo): se encontro y arreglo un bug en analyze.py -- eval_experiments() solo calculaba beforeN/afterN/verdict para status 'running'/'proposed', nunca para 'applied'. Como este experimento paso a 'applied' el 09-26, se habria quedado sin medicion antes/despues PARA SIEMPRE (el verdict confirmed/rejected que este mismo archivo lleva semanas anticipando nunca se habria calculado). Se agrego 'applied' a la lista de estados elegibles (mejora permanente, commit de hoy). Con el fix, el agregado (segment={'kind':'RETEST'}, sin desglose tf/side) da beforeN=17449 afterN=89 expR 0.057->0.225, verdict mecanico 'confirmed' (delta=0.168>0.05, afterN=89>=40) y dispara la alerta EXPERIMENTO CONFIRMADO en report.md de hoy. NO SE TOMA ESE VERDICT AL PIE DE LA LETRA: el desglose real por segmento en prediction_scoreboard (las lineas de predictions.jsonl por tf/side) muestra un primer dia volatil y contradictorio -- 1m LONG (n=37, la rama con mas historia e in-sample mas estable de las seis) sale con realDeltaER=-0.055, DIRECCION CONTRARIA a lo predicho (+0.152); 1m SHORT (n=33) sale con realDeltaER=+0.567, mas de 4x lo predicho (+0.143); 2m LONG/SHORT y 5m LONG/SHORT todavia con afterN de un solo digito (1, 3, 6, 9), sin ninguna base para leer direccion. Esto es exactamente el patron que el propio historial in-sample de este experimento documento una y otra vez ('lecturas con n en los cientos bajos pueden sobrestimar el efecto') pero mas extremo (aqui n esta en las decenas, no en los cientos, y es UN SOLO DIA). DECISION: el status se mantiene en 'applied', NO se sube a 'confirmed' todavia pese al verdict mecanico de hoy -- se sigue vigilando dia a dia hasta que cada segmento (no el agregado) junte afterN>=40 y, per agent-instructions.md, se vea la misma direccion sostenida 2 semanas seguidas antes de tratarlo como resultado real. Revisar de nuevo mañana con el segundo dia de dato real.",
      "2026-09-29 (martes, tercer dia real de trading bajo el SL nuevo desde el sabado 09-26): salto grande de afterN agregado (89->999) al asentarse mas dato real. El verdict mecanico de eval_experiments() sigue en 'confirmed' a nivel agregado (beforeN=17367 afterN=999, expR 0.056->0.114) pero el desglose por segmento en prediction_scoreboard (predictions.jsonl) ya tiene muestra suficiente para desconfiar del agregado, NO para confirmarlo: de los 6 segmentos propuestos, SOLO 2 van en la direccion predicha -- 1m SHORT (n=454) realDeltaER=+0.16 vs +0.143 predicho (acierta) y 2m SHORT (n=164) realDeltaER=+0.354 vs +0.151 predicho (acierta, sobra) -- mientras que LOS OTROS 4 SALEN EN DIRECCION CONTRARIA: 1m LONG (n=199) realDeltaER=-0.174 vs +0.152 predicho, 2m LONG (n=83) realDeltaER=-0.097 vs +0.154 predicho, 5m LONG (n=44) realDeltaER=-0.228 vs +0.255 predicho, 5m SHORT (n=55) realDeltaER=-0.277 vs +0.567 predicho. hit_direction_rate del prediction_scoreboard cae a 33.3% (2/6) con mae_deltaER=0.354, la peor calificacion del scoreboard hasta la fecha. Es el patron opuesto al que domina el resto del bus (donde SHORT y LONG solian moverse parecido): aqui el SL nuevo parece estar ayudando en SHORT (1m y 2m, n ya no chico) y perjudicando en LONG (los 3 TF, incluido 1m LONG que era la rama con mas historia in-sample de las seis) mas 5m SHORT (n todavia chico, 55, tratar con cautela). DECISION: el estado se mantiene en 'applied', el verdict mecanico 'confirmed' del agregado NO se toma al pie de la letra y no se reporta a Jesus como exito -- se recomienda EXPLICITAMENTE seguir vigilando dia a dia sin tocar nada mas (ni revertir ni reforzar) hasta que: (a) cada segmento LONG junte afterN>=40 (1m y 2m ya lo cumplen hoy, 5m LONG con 44 esta al filo) y (b) se sostenga la misma direccion 2 semanas seguidas por segmento, per agent-instructions.md. Si el patron LONG-negativo se sostiene con mas muestra en las proximas corridas (en particular 1m LONG, que ya tiene n=199 y viene de ser el segmento mas maduro y estable de toda la evidencia in-sample), ese es el escenario que justificaria proponer revertir el SL a 3 capas SOLO en el lado LONG de RETEST en la revision semanal del domingo 2026-10-04, dejando SHORT con el SL nuevo. No se propone ese revert todavia porque 3 dias (con un fin de semana sin sesion CME de por medio) es muy poca muestra temporal para distinguir una reversion real de ruido post-cambio -- ver el propio historial de este experimento (in-sample) documentando varias veces que lecturas con n en las decenas/cientos bajos sobrestiman el efecto en cualquier direccion.",
      "2026-09-30 (miercoles, cuarto dia real de trading bajo el SL nuevo): el verdict mecanico agregado SIGUE en 'confirmed' (dispara la alerta EXPERIMENTO CONFIRMADO en report.md de hoy otra vez) y SIGUE sin tomarse al pie de la letra -- el desglose por segmento de prediction_scoreboard, con n ya bastante mas grande en los 6 (1m LONG n=437, 1m SHORT n=800, 2m LONG n=194, 2m SHORT n=318, 5m LONG n=76, 5m SHORT n=114 -- los 6 superan ya el afterN>=40 de agent-instructions.md), mantiene EXACTAMENTE el mismo patron de direccion que ayer, ahora con mucha mas muestra detras: 1m SHORT realDeltaER=+0.142 (vs +0.143 predicho, acierta casi exacto) y 2m SHORT realDeltaER=+0.167 (vs +0.151 predicho, acierta) siguen siendo los UNICOS 2 segmentos que confirman; 1m LONG realDeltaER=-0.028, 2m LONG realDeltaER=-0.097, 5m LONG realDeltaER=-0.151 y 5m SHORT realDeltaER=-0.086 siguen en direccion CONTRARIA a lo predicho (hit_direction_rate=33.3%, mae_deltaER=0.251). Nota importante: la hipotesis de ayer ('SHORT ayuda, LONG perjudica') ya NO describe el patron con precision -- 5m SHORT tambien se dio vuelta a negativo hoy con n=114 (ya no es 'n todavia chico', son 4 dias seguidos de dato real). El patron mas preciso hoy es: SOLO 1m y 2m SHORT confirman; las 3 ramas LONG (1m/2m/5m) Y 5m SHORT no confirman. Es el CUARTO dia consecutivo (09-28, 09-29, 09-30, y contando) con la misma division 2-vs-4, cada vez con mas muestra, sin ninguna reversion hacia el lado predicho en los 4 segmentos que fallan. Todavia no se cumple el criterio propio del experimento de '2 semanas consecutivas en la misma direccion' antes de tratarlo como resultado real, pero con afterN ya por encima de 40 en los 6 segmentos y 3-4 dias seguidos sin cambio de signo, el balance de evidencia se esta inclinando hacia un revert parcial. RECOMENDACION EXPLICITA para la revision semanal del domingo 2026-10-04 (no antes, hace falta ver si el patron se mantiene el resto de la semana): si 1m LONG, 2m LONG, 5m LONG y 5m SHORT siguen en direccion negativa el domingo, proponer formalmente revertir sl_basis_retest a '3-capas' en esos 4 segmentos (mantener la mecha del retest solo en 1m y 2m SHORT, que son los que realmente mejoraron). Correlacion en paralelo (no causal, anotar solo): el mismo segmento 2m/RETEST/LONG perdio hoy su significancia en segment_significance (survives_fdr10 paso de true a false, CI90=[-0.008,0.069] cruza cero por primera vez en semanas, ver report.alerts de hoy) -- dos senales independientes (el experimento de SL y la significancia cruda del segmento) apuntando en la misma direccion de deterioro para 2m LONG en la misma corrida."
    ],
    "appliedNote": "2026-09-26: aplicado en scalp_command.pine (input sc_sl_retest_basis, default 'Auto (como se midio)'): en RETEST el SL real pasa a la mecha de la vela del retest; 1m SHORT suma la vela previa (retestBar2), igual que la medicion paralela. Base: los 6 segmentos RETEST certifican con CI90 > 0 (n=11273, E[R] 0.238 vs 0.065). El tier se sigue calculando con el stop de 3 capas. El feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig, asi que sl_origin_vs_layer sigue siendo la vigilancia. Rige en cada grafico desde que Jesus re-pega scalp_cc_FULL_for_tradingview.pine. Revertir = poner la base en '3 capas'.",
    "beforeN": 16992,
    "afterN": 3231,
    "before": {
      "n": 16992,
      "wrTP1": 46.0,
      "nSL": 7795,
      "nTO": 1389,
      "expR": 0.059,
      "pf": 1.12,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.0
    },
    "after": {
      "n": 3231,
      "wrTP1": 45.3,
      "nSL": 1498,
      "nTO": 268,
      "expR": 0.024,
      "pf": 1.05,
      "mfe_p25": 9.0,
      "mfe_p50": 20.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 28.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 33.6
    },
    "verdict": "flat"
  },
  {
    "id": "sc-min-rr-cut-2026-09-20",
    "status": "proposed",
    "hypothesis": "Subir sc_min_rr (o sc_aplus_rr) para exigir mas RR desde el origen de la senal sube el E[R] en RETEST porque ataca directo la causa de SL dominante 'RR-bajo' (37-38% de las perdidas en RETEST toda la vida del bus). Contrapartida esperada: baja el win rate (menos senales pasan el filtro, y las que pasan tienen el TP mas lejos del SL) pero las que sobreviven pagan mas R, y el neto deberia mejorar -- misma logica que el experimento sl-retest-wick pero del lado de la ENTRADA (que senales se toman), no de la gestion (donde se pone el stop).",
    "param": "sc_min_rr / sc_aplus_rr",
    "from": "sin piso explicito medido hoy (rr1 crudo del indicador)",
    "to": "candidatos a evaluar: 1.2 / 1.3 / 1.5 / 2.0 (ver evidencia por segmento)",
    "changeDate": null,
    "segment": {
      "kind": "RETEST"
    },
    "targetMetric": "expR",
    "minAfterN": 40,
    "evidence": {
      "source": "nuevo corte permanente en analyze.py de hoy (rr1_threshold_cut): por cada segmento tf/kind/side de RETEST, compara el E[R]/WR/PF/CI90 del segmento completo contra el subconjunto que solo toma senales con rr1>=X (contrafactual de entrada, no cambia gestion ni SL). Llena el hueco que la revision de 2026-week-37 dejo pendiente ('no hay todavia un corte contrafactual de rr1>=X').",
      "asOf": "2026-09-20 (domingo), primera lectura, dato identico al de ayer (fin de semana sin trade nuevo, ver nota de sl-retest-wick arriba).",
      "1m_short": {
        "baseline_n": 2998,
        "baseline_expR": 0.051,
        "rr1_ge_1_2_n": 1219,
        "rr1_ge_1_2_expR": 0.101,
        "ci90": [
          0.026,
          0.181
        ],
        "wr_baseline": 45.8,
        "wr_cut": 28.4
      },
      "2m_short": {
        "baseline_n": 1267,
        "baseline_expR": 0.099,
        "rr1_ge_1_2_n": 457,
        "rr1_ge_1_2_expR": 0.2,
        "ci90": [
          0.068,
          0.328
        ],
        "wr_baseline": 50.0,
        "wr_cut": 31.9
      },
      "5m_long": {
        "baseline_n": 767,
        "baseline_expR": 0.183,
        "rr1_ge_1_2_n": 276,
        "rr1_ge_1_2_expR": 0.408,
        "ci90": [
          0.231,
          0.582
        ],
        "wr_baseline": 53.8,
        "wr_cut": 38.0
      },
      "1m_long": {
        "baseline_n": 4695,
        "baseline_expR": 0.039,
        "rr1_ge_1_2_n": 1886,
        "rr1_ge_1_2_expR": 0.041,
        "ci90": "practicamente sin cambio vs baseline, efecto plano/nulo en este segmento -- no generalizar del resto"
      },
      "nota": "1m SHORT, 2m SHORT y 5m LONG muestran una relacion consistente: subir el piso de rr1 sube E[R] y PF de forma monotona-ish con CI90 que no cruza cero en ningun escalon (aunque son subconjuntos anidados, no lecturas independientes -- no comparar los CI90 entre escalones como si fueran experimentos separados). 1m LONG y 2m LONG NO muestran el mismo efecto (practicamente plano). Esto es coherente con el coeficiente mas grande del modelo P(TP1) (rr1, peso -1.185): mas RR exigido = menos probabilidad de tocar TP1, pero el modelo no dice si el NETO en R mejora o empeora, que es justo lo que mide este corte."
    },
    "next_steps": [
      "2026-09-20: primera lectura, in-sample, un solo dia de dato (identico a ayer por el fin de semana). NO proponer un valor concreto de sc_min_rr todavia -- falta: (a) walk_forward.ready (solo 3 semanas de historial), (b) que el patron se sostenga con dato genuinamente nuevo en corridas futuras, (c) decidir el punto exacto del trade-off WR-vs-E[R] que Jesus esta dispuesto a aceptar (WR cae de ~46-54% a ~28-38% en los tres segmentos donde el efecto es real).",
      "Vigilar en corridas futuras: si 1m SHORT, 2m SHORT y 5m LONG siguen mostrando el mismo patron con muestra nueva, y si 1m LONG / 2m LONG se mantienen planos (en cuyo caso la regla seria 'sc_min_rr mas alto solo para esos 3 segmentos', no un cambio global).",
      "Cuando haya 2-3 lecturas independientes seguidas confirmando: sumar a la propuesta formal de la revision semanal con predictedDeltaER en predictions.jsonl, igual que se hizo con sl-retest-wick.",
      "2026-09-21 (lunes, segunda lectura, primera con dato genuinamente nuevo desde que se anadio el corte el 09-20): el patron se mantiene igual que el domingo -- 1m SHORT, 2m SHORT y 5m LONG siguen mostrando que subir el piso de rr1 sube E[R] y PF de forma consistente con CI90 que no cruza cero; 1m LONG y 2m LONG siguen practicamente planos. Todavia in-sample, todavia sin walk_forward.ready con suficientes semanas -- sigue sin proponerse un valor concreto de sc_min_rr. Vigilar 2-3 lecturas mas con dato nuevo antes de sumarlo a una propuesta formal.",
      "2026-09-22 (martes, tercera lectura, con el lote grande de dato nuevo genuino del dia -- +1027 outcomes en todo el bus): 1m SHORT (cut>=1.2 n=1273 expR=0.124 CI90=[0.043,0.202]), 2m SHORT (n=475 expR=0.176 CI90=[0.051,0.297]) y 5m LONG (n=286 expR=0.45 CI90=[0.282,0.626]) siguen mostrando el mismo patron monotono, sin reversion en la tercera lectura. CAMBIO A VIGILAR: 1m LONG, que llevaba dos lecturas practicamente plano, hoy muestra un CI90 que ya no cruza cero (n=2055 expR=0.108 CI90=[0.051,0.167] vs baseline expR=0.075) -- todavia mas debil que los otros tres segmentos, pero ya no es claramente 'sin efecto'; 2m LONG sigue el mas debil/plano (n=850 expR=0.068 CI90=[-0.027,0.163], cruza cero). walk_forward.ready=true desde hace unos dias pero este corte especifico (rr1_threshold_cut) sigue sin evaluarse contra el split OOS -- pendiente antes de proponer un valor concreto. Sigue sin proponerse sc_min_rr en la revision semanal (la ultima fue el 09-20); revisar el patron de 1m LONG una vez mas el domingo antes de decidir si se suma a la propuesta.",
      "2026-09-24 (jueves): sin corte nuevo calculado explicitamente hoy en esta nota (ver report.json.rr1_threshold_cut para las cifras crudas del dia), el patron narrado el 09-22 se mantiene sin reversion conocida: 1m SHORT, 2m SHORT y 5m LONG siguen siendo los tres segmentos donde subir el piso de rr1 sube E[R]/PF de forma monotona con CI90 que no cruza cero; 1m LONG sigue mostrando un efecto mas debil que los otros tres pero ya no claramente plano (ver lectura del 09-22, CI90 dejo de cruzar cero en el corte 1.2); 2m LONG sigue siendo el mas plano/cruza cero. Sigue pendiente evaluar este corte contra el split walk-forward OOS (walk_forward.ready=true desde hace dias, pero el corte especifico rr1_threshold_cut todavia no se compara contra W38-W39) antes de proponer un valor concreto de sc_min_rr en la revision semanal del domingo 2026-09-27.",
      "2026-09-26 (sabado, cuarta lectura con corte recalculado, dato de 2026-09-25 completo): el patron se debilita en el corte 1.2 en varios segmentos a la vez, coincidiendo con la debilidad general de E[R] crudo en SELL RETEST que se vio hoy en todo el bus (ver playbooks) -- 1m SHORT (n=1638 expR=0.073 CI90=[0.007,0.138] vs baseline 0.043) sigue sin cruzar cero pero mas cerca que el 09-22 (era 0.124); 2m SHORT (n=646 expR=0.131 CI90=[0.035,0.235] vs baseline 0.097) sigue sin cruzar cero pero tambien mas debil que el 09-22 (0.176); 5m LONG (n=343 expR=0.375 CI90=[0.217,0.538] vs baseline 0.163) SIGUE siendo el mas fuerte y estable de los tres, practicamente igual al 09-22 (0.45) -- el unico de los tres candidatos que no comparte la debilidad de hoy. 1m LONG vuelve a mostrar un CI90 que cruza cero (n=2568 expR=0.055 CI90=[0.003,0.107] vs baseline 0.056, practicamente identico -- efecto nulo, revierte la lectura mas fuerte del 09-22) y 2m LONG sigue el mas plano/cruza cero (n=1026 expR=0.024 CI90=[-0.062,0.106]). Primera lectura separada de 5m SHORT (antes no se reportaba en esta nota): n=233 expR=0.138 CI90=[-0.044,0.326] vs baseline 0.106 -- cruza cero, no se suma como cuarto candidato todavia. Con dos de los tres candidatos (1m SHORT, 2m SHORT) debilitandose el mismo dia que el E[R] crudo de SHORT en general, hay que esperar el dato del lunes antes de decidir si es ruido de un viernes flojo o un cambio real del patron -- no se suma ni se descarta ningun segmento hoy. Sigue sin proponerse un valor concreto de sc_min_rr; sigue pendiente evaluar contra el split walk-forward OOS.",
      "2026-09-27 (domingo, REVISION SEMANAL): se agrego hoy a analyze.py el corte pendiente contra el split walk-forward (rr1_threshold_cut_oos, nueva funcion permanente) que este experimento llevaba pidiendo desde el 2026-09-22 ('pendiente evaluar este corte contra el split walk-forward OOS'). Resultado con testWeeks W38-W39 (mismo split que walk_forward.testWeeks): SOLO 5m LONG confirma fuera de muestra de forma clara -- baseline test n=544 expR=0.148 CI90=[0.056,0.247]; cortes 1.2/1.3/1.5 SUBEN el E[R] a 0.35-0.37 con CI90 que NO cruza cero (n=141-182, PF hasta 1.66) -- el patron in-sample se replica limpio fuera de muestra. Los otros dos candidatos in-sample (1m SHORT, 2m SHORT) NO se confirman: 1m SHORT sube de expR=0.052 a 0.073-0.094 con los cortes pero el CI90 sigue cruzando cero en el test set aislado (n mas chico, 425-836, falta potencia, no se descarta, solo no certifica todavia); 2m SHORT de hecho SE REVIERTE en el test set -- baseline test expR=0.058 (ya al filo, CI90=[-0.001,0.118]) y los 4 cortes dan expR NEGATIVO (-0.02 a -0.162), el corte 2.0 con CI90=[-0.382,0.05] casi enteramente del lado negativo. 1m LONG (que nunca certifico in-sample con consistencia) tambien se revierte en el test set: baseline test ya positivo (0.091) y los 4 cortes BAJAN el E[R] de forma monotona hasta 0.036 -- confirma que subir el piso de rr1 en 1m LONG no ayuda, va en contra. DECISION: no se propone sc_min_rr global. Se propone en la revision semanal de hoy (reviews/2026-week-39.md) SOLO un cambio experimental y acotado a 5m/RETEST/LONG (candidato a sc_aplus_rr o un filtro nuevo especifico de ese segmento, ya que sc_min_rr es global a todos los tf/side y subirlo global arriesga empeorar 1m LONG y 2m SHORT segun este mismo corte). Marcar 2m SHORT como alerta de metodo: un patron en apariencia solido in-sample (3+ lecturas consistentes) no sobrevivio el primer chequeo OOS real -- tratarlo como caso de estudio de por que el walk-forward es el numero que cuenta, no el contrafactual in-sample.",
      "2026-09-29 (martes): el walk-forward testWeeks avanzo de [W38,W39] a [W39,W40] (W39 ya cerro, W40 es la semana en curso) y con la ventana nueva el unico candidato que habia confirmado OOS limpio el 09-27 (5m/RETEST/LONG) PIERDE la certificacion: baseline test n=287 expR=0.084 CI90=[-0.046,0.215] (cruza cero, antes n=544 expR=0.148 CI90=[0.056,0.247] no cruzaba) y los cortes 1.2/1.3 salen con CI90 igual de anchos y cruzando cero (ej. 1.2: expR=0.161 CI90=[-0.175,0.527]) -- el patron todavia apunta en la misma direccion (subir el piso de rr1 sube el E[R] observado) pero ya no certifica fuera de muestra con esta ventana mas chica (W40 apenas tiene unos dias de dato). No es una reversion de signo, es perdida de potencia estadistica al cambiar de ventana de test -- vigilar si vuelve a certificar cuando W40 cierre con mas muestra. Sigue sin proponerse ningun valor concreto de sc_aplus_rr; la linea 7 de predictions.jsonl sigue sin appliedDate."
    ],
    "beforeN": 20223,
    "afterN": 0,
    "before": {
      "n": 20223,
      "wrTP1": 45.9,
      "nSL": 9293,
      "nTO": 1657,
      "expR": 0.053,
      "pf": 1.11,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 33.1
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
    "date": "2026-10-01",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-30T19:08:41-05:00",
    "schema": "sa-plan-2",
    "cleanest": "YM",
    "instruments": {
      "NQ": {
        "biasDay": "LONG",
        "biasSession": "LONG",
        "conviction": "baja",
        "prevDay": {
          "type": {
            "es": "reversal desde el máximo del día, con la estructura de precio marcando BOS bajista pese a la mecha alcista",
            "en": "reversal from the day's high, with price structure still flagging a bearish BOS despite the bullish wick"
          },
          "closedAt": {
            "es": "30729.25, entre el mínimo 30512.25 y el máximo 30906.00 (55% del rango, tercio medio-alto)",
            "en": "30729.25, between the 30512.25 low and 30906.00 high (55% of the range, mid-upper third)"
          },
          "prior": {
            "es": "reversal desde el máximo -- 30906/30826.75 techo a respetar, pero la reacción fue moderada, no violenta",
            "en": "reversal from the high -- 30906/30826.75 is the ceiling to respect, but the reaction was moderate, not violent"
          },
          "note": {
            "es": "tercera prueba real de la invalidación bajista 30826.75, esta vez CON perforación de mecha (30906, +79pts sobre el nivel) pero sin cierre 5m sostenido -- la tesis bajista sobrevive por un margen cada vez más fino",
            "en": "third real test of the 30826.75 bearish invalidation, this time WITH a wick breach (30906, +79pts above the level) but no sustained 5m close -- the bearish thesis survives by an ever-thinner margin"
          }
        },
        "gap": {
          "pts": 0.0,
          "ticks": 0,
          "filled": true,
          "size": {
            "es": "sin gap todavía",
            "en": "no gap yet"
          },
          "note": {
            "es": "la reapertura de Globex es a las 17:00 CT; todavía no hay gap real que medir",
            "en": "Globex reopens at 17:00 CT; there's no real gap to measure yet"
          }
        },
        "weekendGap": null,
        "smt": {
          "state": "ninguna",
          "note": {
            "es": "NQ, ES e YM revirtieron juntos desde sus máximos hoy, pero YM rompió mucho más fuerte (perdió su propia invalidación) mientras NQ/ES solo devolvieron terreno sin invalidar -- vigilar si esa debilidad relativa de YM se repite en los nuevos swings de esta noche",
            "en": "NQ, ES and YM all reversed together off their highs today, but YM broke far harder (lost its own invalidation) while NQ/ES only gave back ground without invalidating -- watch whether YM's relative weakness repeats in tonight's fresh swings"
          }
        },
        "frameConflict": {
          "on": true,
          "note": {
            "es": "el eje de gráfico (biasChart -3) ya no acompaña al diario/semanal fusionado (+3/+3, aún aligned=0 formalmente); dentro de la sesión, 3reads lee LONG pero c
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 8670,
  "by_verdict": {
    "AVOID": {
      "n": 1948,
      "wrTP1": 43.8,
      "nSL": 955,
      "nTO": 140,
      "expR": -0.003,
      "pf": 0.99,
      "mfe_p25": 7.0,
      "mfe_p50": 16.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 33.7
    },
    "GO": {
      "n": 965,
      "wrTP1": 49.5,
      "nSL": 394,
      "nTO": 93,
      "expR": 0.154,
      "pf": 1.35,
      "mfe_p25": 12.0,
      "mfe_p50": 28.0,
      "mfe_p75": 52.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 29.30000000000001,
      "loserMFEbeforeSL_p50": 4.5,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.5,
      "revAfterSL_rate": 42.4
    },
    "WAIT": {
      "n": 5757,
      "wrTP1": 47.8,
      "nSL": 2611,
      "nTO": 395,
      "expR": 0.063,
      "pf": 1.13,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 34.6
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": -0.003,
      "ci90": [
        -0.047,
        0.044
      ],
      "p_mean_le_0": 0.556,
      "n": 1849
    },
    "GO": {
      "expR": 0.154,
      "ci90": [
        0.087,
        0.226
      ],
      "p_mean_le_0": 0.0,
      "n": 903
    },
    "WAIT": {
      "expR": 0.063,
      "ci90": [
        0.036,
        0.088
      ],
      "p_mean_le_0": 0.0,
      "n": 5554
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1948,
      "wrTP1": 43.8,
      "nSL": 955,
      "nTO": 140,
      "expR": -0.003,
      "pf": 0.99,
      "mfe_p25": 7.0,
      "mfe_p50": 16.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 33.7
    },
    "GO_or_WAIT": {
      "n": 6722,
      "wrTP1": 48.0,
      "nSL": 3005,
      "nTO": 488,
      "expR": 0.076,
      "pf": 1.16,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 42.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 35.6
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": -0.003,
      "ci90": [
        -0.047,
        0.044
      ],
      "p_mean_le_0": 0.556,
      "n": 1849
    },
    "GO_or_WAIT": {
      "expR": 0.076,
      "ci90": [
        0.05,
        0.1
      ],
      "p_mean_le_0": 0.0,
      "n": 6457
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 29,
        "wrTP1": 55.2,
        "nSL": 10,
        "nTO": 3,
        "expR": 0.115,
        "pf": 1.32,
        "mfe_p25": 6.0,
        "mfe_p50": 13.5,
        "mfe_p75": 30.0,
        "winnerMAE_p75": 12.75,
        "winnerMAE_p90": 16.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.5,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 30.0
      },
      "GO": {
        "n": 10,
        "wrTP1": 60.0,
        "nSL": 3,
        "nTO": 1,
        "expR": 0.032,
        "pf": 1.1,
        "mfe_p25": 23.0,
        "mfe_p50": 28.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 30.0,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 6.5,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -54.0,
        "revAfterSL_rate": 33.3
      },
      "WAIT": {
        "n": 73,
        "wrTP1": 43.8,
        "nSL": 32,
        "nTO": 9,
        "expR": -0.031,
        "pf": 0.93,
        "mfe_p25": 8.0,
        "mfe_p50": 17.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 23.700000000000006,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 15.6
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 28,
        "wrTP1": 28.6,
        "nSL": 16,
        "nTO": 4,
        "expR": -0.447,
        "pf": 0.3,
        "mfe_p25": 6.0,
        "mfe_p50": 14.0,
        "mfe_p75": 21.0,
        "winnerMAE_p75": 5.25,
        "winnerMAE_p90": 6.8999999999999995,
        "loserMFEbeforeSL_p50": 13.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 7.5,
        "entryZoneTk_p50": -11.5,
        "revAfterSL_rate": 12.5
      },
      "WAIT": {
        "n": 89,
        "wrTP1": 48.3,
        "nSL": 36,
        "nTO": 10,
        "expR": -0.028,
        "pf": 0.93,
        "mfe_p25": 7.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 17.5,
        "winnerMAE_p90": 29.200000000000017,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 6.5,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 25.0
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 1161,
        "wrTP1": 44.0,
        "nSL": 582,
        "nTO": 68,
        "expR": -0.037,
        "pf": 0.93,
        "mfe_p25": 7.0,
        "mfe_p50": 14.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 32.1
      },
      "GO": {
        "n": 564,
        "wrTP1": 49.5,
        "nSL": 250,
        "nTO": 35,
        "expR": 0.141,
        "pf": 1.31,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 26.200000000000017,
        "loserMFEbeforeSL_p50": 3.5,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 40.4
      },
      "WAIT": {
        "n": 2986,
        "wrTP1": 48.8,
        "nSL": 1327,
        "nTO": 203,
        "expR": 0.09,
        "pf": 1.2,
        "mfe_p25": 7.0,
        "mfe_p50": 18.0,
        "mfe_p75": 39.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 33.7
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 730,
        "wrTP1": 43.6,
        "nSL": 347,
        "nTO": 65,
        "expR": 0.064,
        "pf": 1.13,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 38.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 37.5
      },
      "GO": {
        "n": 387,
        "wrTP1": 49.1,
        "nSL": 140,
        "nTO": 57,
        "expR": 0.17,
        "pf": 1.41,
        "mfe_p25": 15.0,
        "mfe_p50": 33.0,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 30.19999999999999,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 46.4
      },
      "WAIT": {
        "n": 2609,
        "wrTP1": 46.8,
        "nSL": 1216,
        "nTO": 173,
        "expR": 0.037,
        "pf": 1.08,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 40.75,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 36.3
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```

## Modo sombra (peldano 0->1, gate en execution-ladder.md)
```json
{
  "rule": {
    "version": 2,
    "definedAt": "2026-09-27",
    "criteria": {
      "kind": [
        "RETEST"
      ],
      "tf_side": [
        "1/LONG",
        "1/SHORT",
        "2/LONG",
        "2/SHORT",
        "5/LONG",
        "5/SHORT"
      ],
      "excludeSaVerdict": [
        "AVOID"
      ]
    },
    "rationale": "kind=RETEST (prioridad 1; INV no tiene ningun segmento con survives_fdr10=true todavia). REVISION SEMANAL 2026-09-27 (v1->v2): v1 (2026-09-20) limitaba tf_side a 4 segmentos (1/LONG, 1/SHORT, 2/SHORT, 5/LONG) porque 2m LONG y 5m SHORT todavia cruzaban/rozaban cero en ese momento. Desde entonces segment_significance certifico ambos de forma sostenida durante varias corridas seguidas (2m LONG desde 2026-09-18, 5m SHORT desde antes) sin ninguna reversion, y hoy los 6 segmentos RETEST (1m/2m/5m x LONG/SHORT) tienen survives_fdr10=true con CI90 que no cruza cero -- ver segment_significance de hoy. Se amplia tf_side a los 6 segmentos certificados; la justificacion vieja de v1 (excluir 2m LONG/5m SHORT por CI90 rozando cero) ya no la sostiene el dato, quedaba pendiente de esta revision semanal desde 2026-09-24 (ver playbook buy-retest.md, historico). Se excluyen senales del dia/sesion en un instrumento con veredicto Session Analyst=AVOID: avoid_vs_rest_ci90.AVOID no es significativo (p_mean_le_0 alto) mientras GO y WAIT si lo son (session_analyst_cross). SL/objetivo = el mismo del indicador (3 capas); el SL estructural de experiments.json (sl-retest-wick) SE APLICO en TradingView el 2026-09-26 pero el feed sigue registrando el 3-capas como rMultiple (el SL real ya cambio, la medicion paralela sigue corriendo en sl_origin_vs_layer) -- no se incorpora a la sombra hasta que haya muestra post-cambio suficiente para decidir si usar rOrig en vez de rMultiple."
  },
  "shadow": {
    "n": 18332,
    "wrTP1": 46.1,
    "nSL": 8364,
    "nTO": 1524,
    "expR": 0.059,
    "pf": 1.12,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 42.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 33.0
  },
  "shadow_ci90": {
    "expR": 0.059,
    "ci90": [
      0.043,
      0.074
    ],
    "p_mean_le_0": 0.0,
    "n": 17486
  },
  "raw_indicator": {
    "n": 20223,
    "wrTP1": 45.9,
    "nSL": 9293,
    "nTO": 1657,
    "expR": 0.053,
    "pf": 1.11,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 33.1
  },
  "raw_indicator_ci90": {
    "expR": 0.053,
    "ci90": [
      0.039,
      0.07
    ],
    "p_mean_le_0": 0.0,
    "n": 19282
  },
  "tier_ap_b_only": {
    "n": 10379,
    "wrTP1": 43.4,
    "nSL": 4959,
    "nTO": 919,
    "expR": 0.055,
    "pf": 1.11,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 5.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 31.0
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.055,
    "ci90": [
      0.033,
      0.078
    ],
    "p_mean_le_0": 0.0,
    "n": 9883
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```

## Modo sombra por semana (gate: shadow_beats_raw 3 semanas seguidas, n>=60)
```json
{
  "2026-W36": {
    "shadow_n": 2676,
    "shadow_expR": -0.03,
    "raw_n": 2756,
    "raw_expR": -0.022,
    "shadow_beats_raw": false
  },
  "2026-W37": {
    "shadow_n": 4088,
    "shadow_expR": 0.09,
    "raw_n": 4831,
    "raw_expR": 0.074,
    "shadow_beats_raw": true
  },
  "2026-W38": {
    "shadow_n": 3934,
    "shadow_expR": 0.121,
    "raw_n": 4408,
    "raw_expR": 0.11,
    "shadow_beats_raw": true
  },
  "2026-W39": {
    "shadow_n": 4998,
    "shadow_expR": 0.053,
    "raw_n": 5074,
    "raw_expR": 0.05,
    "shadow_beats_raw": true
  },
  "2026-W40": {
    "shadow_n": 2636,
    "shadow_expR": 0.023,
    "raw_n": 3154,
    "raw_expR": 0.019,
    "shadow_beats_raw": true
  }
}
```
