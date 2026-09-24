# Scalp CC · report 2026-09-24T01:14Z
- signals=16081 outcomes=15332 pares_resueltos=15938 pendientes=143 huerfanos=36

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: by_kindside_aligned/RETEST/LONG|aligned=0 bajo de n=10 a n=8 desde la corrida previa (agregado, no archivo crudo -- revisar deduplicacion/re-pareo).
- MUESTRA: semana ya cerrada 2026-W36 bajo de n=3183 a n=2965 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W37 bajo de n=5389 a n=5153 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W38 bajo de n=4911 a n=4769 desde la corrida previa -- vigilar, puede ser deduplicacion.
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.246 vs 0.083, delta 0.163 CI90 [0.123, 0.202], n 10125). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.204 vs 0.063, delta 0.141 CI90 [0.068, 0.221], n 2913). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.202 CI90 [0.127, 0.282], n 758). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.068 CI90 [0.035, 0.102], n 3698). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.075, "ci90": [0.058, 0.092], "p_mean_le_0": 0.0, "n": 15296}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 153 | 43.1 | 0.141 | 1.31 | 65 | 13.0 | 11.75 | 18.5 |
| 1m/INV/SHORT | 110 | 48.2 | 0.025 | 1.05 | 49 | 18.0 | 11.0 | 16.3 |
| 1m/RETEST/LONG | 6003 | 46.1 | 0.071 | 1.15 | 2814 | 15.0 | 10.0 | 29.1 |
| 1m/RETEST/SHORT | 3813 | 44.9 | 0.052 | 1.11 | 1750 | 17.0 | 11.0 | 31.1 |
| 2m/INV/LONG | 59 | 52.5 | 0.051 | 1.13 | 21 | 13.0 | 9.5 | 19.0 |
| 2m/INV/SHORT | 45 | 37.8 | -0.029 | 0.95 | 24 | 16.0 | 15.0 | 37.5 |
| 2m/RETEST/LONG | 2621 | 48.0 | 0.072 | 1.15 | 1197 | 17.0 | 13.0 | 37.1 |
| 2m/RETEST/SHORT | 1610 | 48.8 | 0.074 | 1.16 | 719 | 21.0 | 12.0 | 39.2 |
| 5m/INV/LONG | 18 | 66.7 | 0.396 | 3.11 | 3 | 30.0 | 29.75 | 66.7 |
| 5m/INV/SHORT | 11 | 63.6 | 0.413 | 2.38 | 3 | 35.5 | 63.5 | 66.7 |
| 5m/RETEST/LONG | 913 | 52.5 | 0.179 | 1.42 | 371 | 30.0 | 19.0 | 51.2 |
| 5m/RETEST/SHORT | 582 | 47.8 | 0.102 | 1.22 | 249 | 34.0 | 21.0 | 35.7 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 1133 | 25.9 | 0.129 | 1.2 | 701 | 27.0 | 14.0 | 21.4 |
| B | 6630 | 47.5 | 0.079 | 1.17 | 2984 | 17.0 | 12.0 | 33.0 |
| C | 8175 | 49.2 | 0.064 | 1.14 | 3580 | 16.0 | 12.0 | 35.5 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 5850 | 49.0 | 0.1 | 1.22 | 2601 | 13.0 | 9.0 | 37.1 |
| London | 2470 | 46.3 | 0.035 | 1.07 | 1219 | 17.0 | 12.0 | 33.2 |
| NY | 2753 | 46.1 | 0.113 | 1.24 | 1211 | 25.0 | 15.0 | 37.2 |
| Sin KZ | 4865 | 44.9 | 0.043 | 1.09 | 2234 | 19.0 | 13.0 | 26.2 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 3622 | 45.2 | 0.058 | 1.12 | 1667 | 21.0 | 13.0 | 31.6 |
| edge=0 | 7105 | 49.2 | 0.064 | 1.14 | 3165 | 15.0 | 11.0 | 37.3 |
| edge=1 | 5211 | 44.7 | 0.1 | 1.21 | 2433 | 18.0 | 13.0 | 28.8 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 8 | 50.0 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| aligned=1 | 15930 | 46.8 | 0.075 | 1.16 | 7264 | 17.0 | 12.0 | 33.1 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 92 | 53.3 | 0.155 | 1.39 | 33 | 12.0 | 11.0 | 27.3 |
| INV/LONG|edge=1 | 134 | 43.3 | 0.115 | 1.26 | 54 | 16.5 | 14.75 | 14.8 |
| INV/SHORT|edge=-1 | 95 | 40.0 | 0.024 | 1.05 | 48 | 21.0 | 12.0 | 25.0 |
| INV/SHORT|edge=0 | 62 | 53.2 | -0.049 | 0.89 | 25 | 11.0 | 14.0 | 28.0 |
| INV/SHORT|edge=1 | 9 | 66.7 | 0.69 | 3.07 | 3 | 28.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 343 | 53.6 | 0.169 | 1.41 | 137 | 13.0 | 9.0 | 47.4 |
| RETEST/LONG|edge=0 | 4278 | 49.9 | 0.053 | 1.11 | 1932 | 15.0 | 11.0 | 37.8 |
| RETEST/LONG|edge=1 | 4916 | 44.4 | 0.1 | 1.2 | 2313 | 18.0 | 13.0 | 28.4 |
| RETEST/SHORT|edge=-1 | 3180 | 44.5 | 0.046 | 1.09 | 1480 | 21.0 | 14.0 | 30.3 |
| RETEST/SHORT|edge=0 | 2673 | 47.8 | 0.082 | 1.18 | 1175 | 17.0 | 10.0 | 36.9 |
| RETEST/SHORT|edge=1 | 152 | 55.3 | 0.058 | 1.14 | 63 | 14.0 | 9.0 | 55.6 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 73 | 43.8 | 0.164 | 1.35 | 32 | 15.5 | 14.0 | 9.4 |
| INV/LONG|tier=C | 157 | 49.0 | 0.124 | 1.31 | 57 | 13.0 | 13.0 | 26.3 |
| INV/SHORT|tier=B | 46 | 39.1 | -0.037 | 0.93 | 26 | 18.5 | 10.75 | 7.7 |
| INV/SHORT|tier=C | 120 | 49.2 | 0.062 | 1.14 | 50 | 16.0 | 18.5 | 34.0 |
| RETEST/LONG|tier=A+ | 733 | 25.4 | 0.109 | 1.17 | 465 | 23.0 | 13.0 | 19.6 |
| RETEST/LONG|tier=B | 3982 | 47.6 | 0.111 | 1.24 | 1785 | 16.0 | 11.0 | 32.8 |
| RETEST/LONG|tier=C | 4822 | 50.2 | 0.053 | 1.12 | 2132 | 15.0 | 12.0 | 36.4 |
| RETEST/SHORT|tier=A+ | 400 | 27.0 | 0.167 | 1.26 | 236 | 34.5 | 15.0 | 25.0 |
| RETEST/SHORT|tier=B | 2529 | 47.6 | 0.026 | 1.05 | 1141 | 18.0 | 13.0 | 34.6 |
| RETEST/SHORT|tier=C | 3076 | 47.6 | 0.08 | 1.17 | 1341 | 19.0 | 12.0 | 34.5 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 230 | 47.4 | 0.137 | 1.33 | 89 | 14.0 | 14.0 | 20.2 |
| INV/SHORT|aligned=1 | 166 | 46.4 | 0.034 | 1.07 | 76 | 18.0 | 14.0 | 25.0 |
| RETEST/LONG|aligned=0 | 8 | 50.0 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| RETEST/LONG|aligned=1 | 9529 | 47.2 | 0.081 | 1.17 | 4381 | 16.0 | 12.0 | 33.2 |
| RETEST/SHORT|aligned=1 | 6005 | 46.2 | 0.063 | 1.13 | 2718 | 19.0 | 12.0 | 33.7 |

## Autopsia de SL
n_losses=7265  causas: RR-bajo×2719, contra-estructura×2478, stop-en-el-minimo×2407, killzone-Asia-largo×1624, sin-nivel-detras×1452, estirado×1232, chop×1073, SL-muy-pegado×902, sin-causa-clara×752, contra-sesgo×1
- INV/LONG (n=89): RR-bajo×38, killzone-Asia-largo×38, contra-estructura×24, estirado×21, stop-en-el-minimo×18, sin-nivel-detras×13, chop×11, SL-muy-pegado×7, sin-causa-clara×5
- INV/SHORT (n=76): RR-bajo×37, contra-estructura×22, stop-en-el-minimo×19, estirado×17, sin-causa-clara×13, SL-muy-pegado×9, chop×8, sin-nivel-detras×5
- RETEST/LONG (n=4382): RR-bajo×1645, killzone-Asia-largo×1586, contra-estructura×1560, stop-en-el-minimo×1454, sin-nivel-detras×913, estirado×718, chop×700, SL-muy-pegado×525, sin-causa-clara×358, contra-sesgo×1
- RETEST/SHORT (n=2718): RR-bajo×999, stop-en-el-minimo×916, contra-estructura×872, sin-nivel-detras×521, estirado×476, sin-causa-clara×376, SL-muy-pegado×361, chop×354

## Autopsia de SL · semana 2026-W39 (para revision semanal)
n_losses=1350  causas: RR-bajo×490, stop-en-el-minimo×462, contra-estructura×441, killzone-Asia-largo×379, sin-nivel-detras×258, chop×212, estirado×205, SL-muy-pegado×168, sin-causa-clara×150
ejemplos por causa: {"RR-bajo": ["NQ-2-22078-L", "YM-2-22234-S", "NQ-1-24664-L", "CL-1-24584-L", "NQ-1-21276-L"], "stop-en-el-minimo": ["YM-1-22993-S", "YM-2-22231-S", "YM-2-22234-S", "GC-1-24191-S", "ES-1-20747-L"], "contra-estructura": ["GC-1-24154-S", "GC-1-24191-S", "NQ-1-24655-L", "NQ-1-24664-L", "NQ-2-20762-L"]}

## Contrafactual de gestion
```json
{
  "n": 8,
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
    0.18,
    8
  ],
  "altSL_1_5x_struct": [
    0.247,
    8
  ],
  "note": "fixed_XR: R esperado si el objetivo fuera XR fijo con SL=struct. altSL: SL a mult del SL struct."
}
```

## Modelo GESTIONADO (escalera + parciales) vs INGENUO
```json
{
  "overall": {
    "n": 15283,
    "naive_expR": 0.075,
    "managed_expR": 0.141,
    "delta": 0.066,
    "avgEntryBetterTk_p50": 2.3,
    "fill_t3plus_pct": 45.7,
    "fill_full_pct": 32.4,
    "m1_rate": 37.6,
    "m2_rate": 23.2,
    "m3_rate": 12.5,
    "beAfterM1_rate": 18.2
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 144,
      "naive_expR": 0.141,
      "managed_expR": 0.245,
      "delta": 0.104,
      "avgEntryBetterTk_p50": 2.65,
      "fill_t3plus_pct": 49.3,
      "fill_full_pct": 36.8,
      "m1_rate": 41.7,
      "m2_rate": 25.7,
      "m3_rate": 13.2,
      "beAfterM1_rate": 22.2
    },
    "1m/INV/SHORT": {
      "n": 107,
      "naive_expR": 0.025,
      "managed_expR": 0.152,
      "delta": 0.126,
      "avgEntryBetterTk_p50": 3.0,
      "fill_t3plus_pct": 53.3,
      "fill_full_pct": 43.0,
      "m1_rate": 33.6,
      "m2_rate": 19.6,
      "m3_rate": 12.1,
      "beAfterM1_rate": 17.8
    },
    "1m/RETEST/LONG": {
      "n": 5825,
      "naive_expR": 0.071,
      "managed_expR": 0.147,
      "delta": 0.076,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.5,
      "fill_full_pct": 33.6,
      "m1_rate": 37.9,
      "m2_rate": 23.4,
      "m3_rate": 12.2,
      "beAfterM1_rate": 17.4
    },
    "1m/RETEST/SHORT": {
      "n": 3605,
      "naive_expR": 0.053,
      "managed_expR": 0.164,
      "delta": 0.112,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.8,
      "fill_full_pct": 33.9,
      "m1_rate": 39.2,
      "m2_rate": 24.4,
      "m3_rate": 13.7,
      "beAfterM1_rate": 18.4
    },
    "2m/INV/LONG": {
      "n": 55,
      "naive_expR": 0.051,
      "managed_expR": 0.037,
      "delta": -0.014,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.3,
      "fill_full_pct": 36.4,
      "m1_rate": 23.6,
      "m2_rate": 16.4,
      "m3_rate": 5.5,
      "beAfterM1_rate": 9.1
    },
    "2m/INV/SHORT": {
      "n": 45,
      "naive_expR": -0.029,
      "managed_expR": -0.068,
      "delta": -0.039,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 51.1,
      "fill_full_pct": 40.0,
      "m1_rate": 24.4,
      "m2_rate": 20.0,
      "m3_rate": 11.1,
      "beAfterM1_rate": 6.7
    },
    "2m/RETEST/LONG": {
      "n": 2522,
      "naive_expR": 0.072,
      "managed_expR": 0.093,
      "delta": 0.021,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 42.8,
      "fill_full_pct": 30.2,
      "m1_rate": 35.7,
      "m2_rate": 21.1,
      "m3_rate": 11.4,
      "beAfterM1_rate": 18.5
    },
    "2m/RETEST/SHORT": {
      "n": 1553,
      "naive_expR": 0.074,
      "managed_expR": 0.15,
      "delta": 0.076,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 44.6,
      "fill_full_pct": 32.3,
      "m1_rate": 36.9,
      "m2_rate": 23.3,
      "m3_rate": 12.6,
      "beAfterM1_rate": 19.1
    },
    "5m/INV/LONG": {
      "n": 16,
      "naive_expR": 0.396,
      "managed_expR": 0.265,
      "delta": -0.131,
      "avgEntryBetterTk_p50": 0.65,
      "fill_t3plus_pct": 31.2,
      "fill_full_pct": 18.8,
      "m1_rate": 25.0,
      "m2_rate": 18.8,
      "m3_rate": 6.2,
      "beAfterM1_rate": 12.5
    },
    "5m/INV/SHORT": {
      "n": 10,
      "naive_expR": 0.413,
      "managed_expR": 0.485,
      "delta": 0.072,
      "avgEntryBetterTk_p50": 8.4,
      "fill_t3plus_pct": 70.0,
      "fill_full_pct": 50.0,
      "m1_rate": 30.0,
      "m2_rate": 20.0,
      "m3_rate": 20.0,
      "beAfterM1_rate": 10.0
    },
    "5m/RETEST/LONG": {
      "n": 863,
      "naive_expR": 0.179,
      "managed_expR": 0.116,
      "delta": -0.062,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 31.1,
      "fill_full_pct": 23.5,
      "m1_rate": 35.9,
      "m2_rate": 23.6,
      "m3_rate": 13.2,
      "beAfterM1_rate": 19.2
    },
    "5m/RETEST/SHORT": {
      "n": 538,
      "naive_expR": 0.101,
      "managed_expR": 0.128,
      "delta": 0.028,
      "avgEntryBetterTk_p50": 4.8,
      "fill_t3plus_pct": 42.8,
      "fill_full_pct": 28.1,
      "m1_rate": 38.5,
      "m2_rate": 23.0,
      "m3_rate": 12.1,
      "beAfterM1_rate": 20.1
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 13403,
    "layer_expR": 0.079,
    "orig_expR": 0.236,
    "delta_orig_minus_layer": 0.157,
    "delta_ci90": [
      0.124,
      0.193
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.7,
    "orig_wrTP1": 33.7,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 8.0,
    "orig_wider_pct": 3.9,
    "orig_saved_from_SL": 20,
    "orig_caused_SL": 2021
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 2,
  "invalid_by_seg": {
    "1m/RETEST/LONG": 2
  },
  "by_basis": {
    "candle1": {
      "n": 365,
      "layer_expR": 0.092,
      "orig_expR": 0.201,
      "delta_orig_minus_layer": 0.109,
      "delta_ci90": [
        -0.122,
        0.368
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.8,
      "orig_wrTP1": 26.6,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 6.3,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 82
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
      "n": 10125,
      "layer_expR": 0.083,
      "orig_expR": 0.246,
      "delta_orig_minus_layer": 0.163,
      "delta_ci90": [
        0.123,
        0.202
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.1,
      "orig_wrTP1": 34.3,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.2,
      "orig_saved_from_SL": 18,
      "orig_caused_SL": 1514
    },
    "retestBar2": {
      "n": 2913,
      "layer_expR": 0.063,
      "orig_expR": 0.204,
      "delta_orig_minus_layer": 0.141,
      "delta_ci90": [
        0.068,
        0.221
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.2,
      "orig_wrTP1": 32.7,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 425
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 144,
      "layer_expR": 0.141,
      "orig_expR": -0.048,
      "delta_orig_minus_layer": -0.189,
      "delta_ci90": [
        -0.46,
        0.105
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 45.8,
      "orig_wrTP1": 20.8,
      "slTk_p50": 15.5,
      "slOrigTk_p50": 3.5,
      "orig_wider_pct": 4.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 36
    },
    "1m/INV/SHORT": {
      "n": 97,
      "layer_expR": 0.022,
      "orig_expR": 0.114,
      "delta_orig_minus_layer": 0.091,
      "delta_ci90": [
        -0.324,
        0.564
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.5,
      "orig_wrTP1": 25.8,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 22
    },
    "1m/RETEST/LONG": {
      "n": 5025,
      "layer_expR": 0.074,
      "orig_expR": 0.204,
      "delta_orig_minus_layer": 0.13,
      "delta_ci90": [
        0.076,
        0.188
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.9,
      "orig_wrTP1": 29.8,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.1,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 863
    },
    "1m/RETEST/SHORT": {
      "n": 3032,
      "layer_expR": 0.057,
      "orig_expR": 0.203,
      "delta_orig_minus_layer": 0.146,
      "delta_ci90": [
        0.071,
        0.226
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.1,
      "orig_wrTP1": 32.5,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 443
    },
    "2m/INV/LONG": {
      "n": 55,
      "layer_expR": 0.051,
      "orig_expR": 1.084,
      "delta_orig_minus_layer": 1.033,
      "delta_ci90": [
        0.042,
        2.263
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 56.4,
      "orig_wrTP1": 32.7,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 7.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 13
    },
    "2m/INV/SHORT": {
      "n": 44,
      "layer_expR": -0.039,
      "orig_expR": 0.406,
      "delta_orig_minus_layer": 0.445,
      "delta_ci90": [
        -0.028,
        1.049
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 36.4,
      "orig_wrTP1": 29.5,
      "slTk_p50": 22.5,
      "slOrigTk_p50": 6.5,
      "orig_wider_pct": 6.8,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 4
    },
    "2m/RETEST/LONG": {
      "n": 2299,
      "layer_expR": 0.079,
      "orig_expR": 0.232,
      "delta_orig_minus_layer": 0.153,
      "delta_ci90": [
        0.086,
        0.224
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.3,
      "orig_wrTP1": 36.8,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.2,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 312
    },
    "2m/RETEST/SHORT": {
      "n": 1357,
      "layer_expR": 0.086,
      "orig_expR": 0.224,
      "delta_orig_minus_layer": 0.138,
      "delta_ci90": [
        0.052,
        0.225
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.0,
      "orig_wrTP1": 37.4,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 187
    },
    "5m/INV/LONG": {
      "n": 16,
      "layer_expR": 0.396,
      "orig_expR": -0.314,
      "delta_orig_minus_layer": -0.711,
      "delta_ci90": [
        -1.239,
        -0.218
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 75.0,
      "orig_wrTP1": 43.8,
      "slTk_p50": 43.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 18.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 5
    },
    "5m/INV/SHORT": {
      "n": 9,
      "layer_expR": 0.401,
      "orig_expR": -0.372,
      "delta_orig_minus_layer": -0.773,
      "delta_ci90": [
        -1.203,
        -0.349
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 66.7,
      "orig_wrTP1": 44.4,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 58.0,
      "orig_wider_pct": 33.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 2
    },
    "5m/RETEST/LONG": {
      "n": 827,
      "layer_expR": 0.159,
      "orig_expR": 0.456,
      "delta_orig_minus_layer": 0.297,
      "delta_ci90": [
        0.146,
        0.468
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 55.4,
      "orig_wrTP1": 45.7,
      "slTk_p50": 28.0,
      "slOrigTk_p50": 17.0,
      "orig_wider_pct": 16.2,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 86
    },
    "5m/RETEST/SHORT": {
      "n": 498,
      "layer_expR": 0.091,
      "orig_expR": 0.455,
      "delta_orig_minus_layer": 0.365,
      "delta_ci90": [
        0.091,
        0.706
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.8,
      "orig_wrTP1": 42.6,
      "slTk_p50": 31.0,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 22.5,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 48
    }
  }
}
```

## Contrafactual de entrada por RR minimo (candidato sc_min_rr, ataca causa RR-bajo)
```json
{
  "1/RETEST/LONG": {
    "baseline": {
      "n": 5775,
      "wrTP1": 47.9,
      "nSL": 2669,
      "nTO": 341,
      "expR": 0.06,
      "pf": 1.13,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 33.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 30.7,
      "ci90": {
        "expR": 0.06,
        "ci90": [
          0.035,
          0.088
        ],
        "p_mean_le_0": 0.0,
        "n": 5605
      }
    },
    "cuts": {
      "1.0": {
        "n": 2812,
        "wrTP1": 31.9,
        "nSL": 1659,
        "nTO": 255,
        "expR": 0.065,
        "pf": 1.11,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 22.0,
        "ci90": {
          "expR": 0.065,
          "ci90": [
            0.016,
            0.109
          ],
          "p_mean_le_0": 0.013,
          "n": 2706
        }
      },
      "1.2": {
        "n": 2320,
        "wrTP1": 29.1,
        "nSL": 1413,
        "nTO": 231,
        "expR": 0.076,
        "pf": 1.12,
        "mfe_p25": 8.0,
        "mfe_p50": 17.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 10.25,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 19.4,
        "ci90": {
          "expR": 0.076,
          "ci90": [
            0.018,
            0.131
          ],
          "p_mean_le_0": 0.009,
          "n": 2229
        }
      },
      "1.3": {
        "n": 2118,
        "wrTP1": 27.5,
        "nSL": 1311,
        "nTO": 224,
        "expR": 0.072,
        "pf": 1.11,
        "mfe_p25": 8.0,
        "mfe_p50": 17.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 18.1,
        "ci90": {
          "expR": 0.072,
          "ci90": [
            0.014,
            0.131
          ],
          "p_mean_le_0": 0.021,
          "n": 2030
        }
      },
      "1.5": {
        "n": 1788,
        "wrTP1": 25.4,
        "nSL": 1131,
        "nTO": 203,
        "expR": 0.083,
        "pf": 1.12,
        "mfe_p25": 8.0,
        "mfe_p50": 17.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 16.0,
        "ci90": {
          "expR": 0.083,
          "ci90": [
            0.016,
            0.148
          ],
          "p_mean_le_0": 0.02,
          "n": 1713
        }
      },
      "2.0": {
        "n": 1143,
        "wrTP1": 18.9,
        "nSL": 764,
        "nTO": 163,
        "expR": 0.074,
        "pf": 1.11,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 8.25,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.5,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 12.0,
        "ci90": {
          "expR": 0.074,
          "ci90": [
            -0.015,
            0.165
          ],
          "p_mean_le_0": 0.088,
          "n": 1098
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 3650,
      "wrTP1": 46.9,
      "nSL": 1635,
      "nTO": 303,
      "expR": 0.058,
      "pf": 1.12,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 33.3,
      "ci90": {
        "expR": 0.058,
        "ci90": [
          0.025,
          0.092
        ],
        "p_mean_le_0": 0.003,
        "n": 3463
      }
    },
    "cuts": {
      "1.0": {
        "n": 1758,
        "wrTP1": 31.4,
        "nSL": 993,
        "nTO": 213,
        "expR": 0.078,
        "pf": 1.13,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.5,
        "revAfterSL_rate": 23.9,
        "ci90": {
          "expR": 0.078,
          "ci90": [
            0.02,
            0.138
          ],
          "p_mean_le_0": 0.017,
          "n": 1639
        }
      },
      "1.2": {
        "n": 1432,
        "wrTP1": 28.8,
        "nSL": 828,
        "nTO": 192,
        "expR": 0.101,
        "pf": 1.16,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 11.25,
        "winnerMAE_p90": 20.900000000000034,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 20.8,
        "ci90": {
          "expR": 0.101,
          "ci90": [
            0.024,
            0.17
          ],
          "p_mean_le_0": 0.013,
          "n": 1330
        }
      },
      "1.3": {
        "n": 1309,
        "wrTP1": 27.2,
        "nSL": 767,
        "nTO": 186,
        "expR": 0.104,
        "pf": 1.16,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 19.9,
        "ci90": {
          "expR": 0.104,
          "ci90": [
            0.027,
            0.181
          ],
          "p_mean_le_0": 0.013,
          "n": 1212
        }
      },
      "1.5": {
        "n": 1109,
        "wrTP1": 25.3,
        "nSL": 663,
        "nTO": 165,
        "expR": 0.118,
        "pf": 1.18,
        "mfe_p25": 11.0,
        "mfe_p50": 27.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 17.6,
        "ci90": {
          "expR": 0.118,
          "ci90": [
            0.026,
            0.207
          ],
          "p_mean_le_0": 0.017,
          "n": 1026
        }
      },
      "2.0": {
        "n": 752,
        "wrTP1": 20.7,
        "nSL": 467,
        "nTO": 129,
        "expR": 0.132,
        "pf": 1.19,
        "mfe_p25": 11.0,
        "mfe_p50": 28.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 12.4,
        "ci90": {
          "expR": 0.132,
          "ci90": [
            0.019,
            0.249
          ],
          "p_mean_le_0": 0.026,
          "n": 693
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 2540,
      "wrTP1": 49.5,
      "nSL": 1150,
      "nTO": 132,
      "expR": 0.058,
      "pf": 1.12,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 38.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 3.5,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 38.6,
      "ci90": {
        "expR": 0.058,
        "ci90": [
          0.017,
          0.098
        ],
        "p_mean_le_0": 0.009,
        "n": 2449
      }
    },
    "cuts": {
      "1.0": {
        "n": 1139,
        "wrTP1": 32.7,
        "nSL": 674,
        "nTO": 93,
        "expR": 0.078,
        "pf": 1.13,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 54.75,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 21.900000000000034,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 31.0,
        "ci90": {
          "expR": 0.078,
          "ci90": [
            -0.001,
            0.158
          ],
          "p_mean_le_0": 0.051,
          "n": 1082
        }
      },
      "1.2": {
        "n": 930,
        "wrTP1": 29.6,
        "nSL": 575,
        "nTO": 80,
        "expR": 0.085,
        "pf": 1.13,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 56.25,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.0,
        "ci90": {
          "expR": 0.085,
          "ci90": [
            -0.004,
            0.177
          ],
          "p_mean_le_0": 0.059,
          "n": 884
        }
      },
      "1.3": {
        "n": 851,
        "wrTP1": 29.0,
        "nSL": 528,
        "nTO": 76,
        "expR": 0.106,
        "pf": 1.16,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 27.8,
        "ci90": {
          "expR": 0.106,
          "ci90": [
            0.012,
            0.204
          ],
          "p_mean_le_0": 0.03,
          "n": 809
        }
      },
      "1.5": {
        "n": 685,
        "wrTP1": 26.6,
        "nSL": 430,
        "nTO": 73,
        "expR": 0.142,
        "pf": 1.21,
        "mfe_p25": 11.0,
        "mfe_p50": 23.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 25.8,
        "ci90": {
          "expR": 0.142,
          "ci90": [
            0.028,
            0.259
          ],
          "p_mean_le_0": 0.016,
          "n": 646
        }
      },
      "2.0": {
        "n": 424,
        "wrTP1": 21.5,
        "nSL": 282,
        "nTO": 51,
        "expR": 0.183,
        "pf": 1.26,
        "mfe_p25": 11.0,
        "mfe_p50": 27.0,
        "mfe_p75": 68.5,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 21.3,
        "ci90": {
          "expR": 0.183,
          "ci90": [
            0.026,
            0.351
          ],
          "p_mean_le_0": 0.024,
          "n": 399
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 1531,
      "wrTP1": 51.3,
      "nSL": 659,
      "nTO": 87,
      "expR": 0.102,
      "pf": 1.23,
      "mfe_p25": 9.0,
      "mfe_p50": 21.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 42.8,
      "ci90": {
        "expR": 0.102,
        "ci90": [
          0.049,
          0.148
        ],
        "p_mean_le_0": 0.0,
        "n": 1481
      }
    },
    "cuts": {
      "1.0": {
        "n": 682,
        "wrTP1": 34.3,
        "nSL": 391,
        "nTO": 57,
        "expR": 0.134,
        "pf": 1.22,
        "mfe_p25": 15.25,
        "mfe_p50": 30.5,
        "mfe_p75": 60.75,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 36.6,
        "ci90": {
          "expR": 0.134,
          "ci90": [
            0.033,
            0.23
          ],
          "p_mean_le_0": 0.01,
          "n": 658
        }
      },
      "1.2": {
        "n": 549,
        "wrTP1": 31.0,
        "nSL": 324,
        "nTO": 55,
        "expR": 0.155,
        "pf": 1.25,
        "mfe_p25": 16.0,
        "mfe_p50": 31.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.099999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 32.7,
        "ci90": {
          "expR": 0.155,
          "ci90": [
            0.039,
            0.269
          ],
          "p_mean_le_0": 0.017,
          "n": 525
        }
      },
      "1.3": {
        "n": 502,
        "wrTP1": 29.5,
        "nSL": 301,
        "nTO": 53,
        "expR": 0.153,
        "pf": 1.24,
        "mfe_p25": 17.0,
        "mfe_p50": 32.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 31.9,
        "ci90": {
          "expR": 0.153,
          "ci90": [
            0.029,
            0.276
          ],
          "p_mean_le_0": 0.019,
          "n": 479
        }
      },
      "1.5": {
        "n": 424,
        "wrTP1": 27.6,
        "nSL": 258,
        "nTO": 49,
        "expR": 0.174,
        "pf": 1.27,
        "mfe_p25": 17.0,
        "mfe_p50": 33.0,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.8,
        "ci90": {
          "expR": 0.174,
          "ci90": [
            0.041,
            0.314
          ],
          "p_mean_le_0": 0.018,
          "n": 404
        }
      },
      "2.0": {
        "n": 279,
        "wrTP1": 25.8,
        "nSL": 169,
        "nTO": 38,
        "expR": 0.293,
        "pf": 1.46,
        "mfe_p25": 20.0,
        "mfe_p50": 36.0,
        "mfe_p75": 75.75,
        "winnerMAE_p75": 11.5,
        "winnerMAE_p90": 25.699999999999996,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 26.6,
        "ci90": {
          "expR": 0.293,
          "ci90": [
            0.111,
            0.481
          ],
          "p_mean_le_0": 0.004,
          "n": 266
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 876,
      "wrTP1": 54.7,
      "nSL": 344,
      "nTO": 53,
      "expR": 0.197,
      "pf": 1.47,
      "mfe_p25": 12.0,
      "mfe_p50": 28.0,
      "mfe_p75": 64.0,
      "winnerMAE_p75": 19.0,
      "winnerMAE_p90": 37.19999999999999,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -36.0,
      "revAfterSL_rate": 55.2,
      "ci90": {
        "expR": 0.197,
        "ci90": [
          0.126,
          0.267
        ],
        "p_mean_le_0": 0.0,
        "n": 831
      }
    },
    "cuts": {
      "1.0": {
        "n": 363,
        "wrTP1": 38.6,
        "nSL": 185,
        "nTO": 38,
        "expR": 0.348,
        "pf": 1.63,
        "mfe_p25": 16.0,
        "mfe_p50": 37.0,
        "mfe_p75": 79.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -31.0,
        "revAfterSL_rate": 50.8,
        "ci90": {
          "expR": 0.348,
          "ci90": [
            0.2,
            0.495
          ],
          "p_mean_le_0": 0.0,
          "n": 333
        }
      },
      "1.2": {
        "n": 308,
        "wrTP1": 38.6,
        "nSL": 153,
        "nTO": 36,
        "expR": 0.441,
        "pf": 1.81,
        "mfe_p25": 16.75,
        "mfe_p50": 37.0,
        "mfe_p75": 79.25,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 23.40000000000002,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 47.7,
        "ci90": {
          "expR": 0.441,
          "ci90": [
            0.275,
            0.613
          ],
          "p_mean_le_0": 0.001,
          "n": 280
        }
      },
      "1.3": {
        "n": 279,
        "wrTP1": 35.8,
        "nSL": 146,
        "nTO": 33,
        "expR": 0.416,
        "pf": 1.72,
        "mfe_p25": 17.0,
        "mfe_p50": 36.5,
        "mfe_p75": 79.75,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 21.10000000000001,
        "loserMFEbeforeSL_p50": 3.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 47.3,
        "ci90": {
          "expR": 0.416,
          "ci90": [
            0.225,
            0.604
          ],
          "p_mean_le_0": 0.0,
          "n": 254
        }
      },
      "1.5": {
        "n": 238,
        "wrTP1": 35.3,
        "nSL": 123,
        "nTO": 31,
        "expR": 0.484,
        "pf": 1.85,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 81.0,
        "winnerMAE_p75": 14.25,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -31.5,
        "revAfterSL_rate": 43.1,
        "ci90": {
          "expR": 0.484,
          "ci90": [
            0.273,
            0.693
          ],
          "p_mean_le_0": 0.0,
          "n": 215
        }
      },
      "2.0": {
        "n": 154,
        "wrTP1": 31.8,
        "nSL": 83,
        "nTO": 22,
        "expR": 0.593,
        "pf": 2.0,
        "mfe_p25": 17.75,
        "mfe_p50": 41.5,
        "mfe_p75": 110.75,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -34.5,
        "revAfterSL_rate": 36.1,
        "ci90": {
          "expR": 0.593,
          "ci90": [
            0.309,
            0.89
          ],
          "p_mean_le_0": 0.0,
          "n": 140
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 549,
      "wrTP1": 50.6,
      "nSL": 224,
      "nTO": 47,
      "expR": 0.124,
      "pf": 1.28,
      "mfe_p25": 14.0,
      "mfe_p50": 32.0,
      "mfe_p75": 62.0,
      "winnerMAE_p75": 21.0,
      "winnerMAE_p90": 40.30000000000001,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -29.5,
      "revAfterSL_rate": 39.3,
      "ci90": {
        "expR": 0.124,
        "ci90": [
          0.041,
          0.212
        ],
        "p_mean_le_0": 0.01,
        "n": 509
      }
    },
    "cuts": {
      "1.0": {
        "n": 244,
        "wrTP1": 34.4,
        "nSL": 135,
        "nTO": 25,
        "expR": 0.145,
        "pf": 1.24,
        "mfe_p25": 22.0,
        "mfe_p50": 41.0,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 23.25,
        "winnerMAE_p90": 40.7,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 31.1,
        "ci90": {
          "expR": 0.145,
          "ci90": [
            -0.021,
            0.321
          ],
          "p_mean_le_0": 0.071,
          "n": 225
        }
      },
      "1.2": {
        "n": 202,
        "wrTP1": 29.7,
        "nSL": 119,
        "nTO": 23,
        "expR": 0.117,
        "pf": 1.18,
        "mfe_p25": 22.0,
        "mfe_p50": 43.0,
        "mfe_p75": 71.25,
        "winnerMAE_p75": 19.5,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.5,
        "revAfterSL_rate": 28.6,
        "ci90": {
          "expR": 0.117,
          "ci90": [
            -0.081,
            0.325
          ],
          "p_mean_le_0": 0.184,
          "n": 184
        }
      },
      "1.3": {
        "n": 184,
        "wrTP1": 29.3,
        "nSL": 110,
        "nTO": 20,
        "expR": 0.109,
        "pf": 1.17,
        "mfe_p25": 22.0,
        "mfe_p50": 43.0,
        "mfe_p75": 72.0,
        "winnerMAE_p75": 20.5,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 2.5,
        "entryZoneTk_p50": -26.5,
        "revAfterSL_rate": 27.3,
        "ci90": {
          "expR": 0.109,
          "ci90": [
            -0.106,
            0.322
          ],
          "p_mean_le_0": 0.183,
          "n": 169
        }
      },
      "1.5": {
        "n": 149,
        "wrTP1": 26.8,
        "nSL": 90,
        "nTO": 19,
        "expR": 0.107,
        "pf": 1.16,
        "mfe_p25": 25.0,
        "mfe_p50": 49.0,
        "mfe_p75": 76.0,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 41.70000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 25.6,
        "ci90": {
          "expR": 0.107,
          "ci90": [
            -0.126,
            0.348
          ],
          "p_mean_le_0": 0.229,
          "n": 135
        }
      },
      "2.0": {
        "n": 93,
        "wrTP1": 21.5,
        "nSL": 62,
        "nTO": 11,
        "expR": 0.063,
        "pf": 1.09,
        "mfe_p25": 25.75,
        "mfe_p50": 53.0,
        "mfe_p75": 84.5,
        "winnerMAE_p75": 32.25,
        "winnerMAE_p90": 42.50000000000002,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 25.8,
        "ci90": {
          "expR": 0.063,
          "ci90": [
            -0.25,
            0.383
          ],
          "p_mean_le_0": 0.371,
          "n": 86
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
    "n": 2965,
    "wrTP1": 44.6,
    "expR": -0.02
  },
  "2026-W37": {
    "n": 5153,
    "wrTP1": 46.8,
    "expR": 0.073
  },
  "2026-W38": {
    "n": 4769,
    "wrTP1": 46.2,
    "expR": 0.091
  },
  "2026-W39": {
    "n": 3051,
    "wrTP1": 50.1,
    "expR": 0.145
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 35,
      "wrTP1": 45.7,
      "expR": 0.243,
      "pf": 1.53
    },
    "1m/INV/SHORT": {
      "n": 17,
      "wrTP1": 70.6,
      "expR": 0.243,
      "pf": 1.83
    },
    "1m/RETEST/LONG": {
      "n": 1271,
      "wrTP1": 42.4,
      "expR": -0.02,
      "pf": 0.96
    },
    "1m/RETEST/SHORT": {
      "n": 435,
      "wrTP1": 43.4,
      "expR": -0.015,
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
      "n": 637,
      "wrTP1": 46.2,
      "expR": -0.053,
      "pf": 0.9
    },
    "2m/RETEST/SHORT": {
      "n": 203,
      "wrTP1": 40.9,
      "expR": -0.107,
      "pf": 0.8
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
      "n": 242,
      "wrTP1": 52.5,
      "expR": 0.082,
      "pf": 1.18
    },
    "5m/RETEST/SHORT": {
      "n": 92,
      "wrTP1": 46.7,
      "expR": -0.031,
      "pf": 0.94
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
      "n": 1517,
      "wrTP1": 45.2,
      "expR": 0.057,
      "pf": 1.12
    },
    "1m/RETEST/SHORT": {
      "n": 1668,
      "wrTP1": 44.6,
      "expR": 0.039,
      "pf": 1.08
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
      "n": 653,
      "wrTP1": 47.5,
      "expR": 0.035,
      "pf": 1.07
    },
    "2m/RETEST/SHORT": {
      "n": 734,
      "wrTP1": 51.6,
      "expR": 0.151,
      "pf": 1.34
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
      "n": 230,
      "wrTP1": 52.6,
      "expR": 0.213,
      "pf": 1.48
    },
    "5m/RETEST/SHORT": {
      "n": 213,
      "wrTP1": 52.1,
      "expR": 0.125,
      "pf": 1.28
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 58,
      "wrTP1": 39.7,
      "expR": -0.146,
      "pf": 0.73
    },
    "1m/INV/SHORT": {
      "n": 22,
      "wrTP1": 45.5,
      "expR": -0.098,
      "pf": 0.8
    },
    "1m/RETEST/LONG": {
      "n": 1964,
      "wrTP1": 48.2,
      "expR": 0.117,
      "pf": 1.26
    },
    "1m/RETEST/SHORT": {
      "n": 973,
      "wrTP1": 42.4,
      "expR": 0.107,
      "pf": 1.23
    },
    "2m/INV/LONG": {
      "n": 16,
      "wrTP1": 56.2,
      "expR": -0.059,
      "pf": 0.79
    },
    "2m/INV/SHORT": {
      "n": 4,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 871,
      "wrTP1": 46.7,
      "expR": 0.052,
      "pf": 1.11
    },
    "2m/RETEST/SHORT": {
      "n": 371,
      "wrTP1": 43.9,
      "expR": 0.008,
      "pf": 1.02
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
      "n": 311,
      "wrTP1": 50.5,
      "expR": 0.175,
      "pf": 1.43
    },
    "5m/RETEST/SHORT": {
      "n": 171,
      "wrTP1": 42.1,
      "expR": 0.104,
      "pf": 1.22
    }
  },
  "2026-W39": {
    "1m/INV/LONG": {
      "n": 24,
      "wrTP1": 50.0,
      "expR": 0.885,
      "pf": 4.54
    },
    "1m/INV/SHORT": {
      "n": 17,
      "wrTP1": 52.9,
      "expR": -0.084,
      "pf": 0.8
    },
    "1m/RETEST/LONG": {
      "n": 1251,
      "wrTP1": 47.5,
      "expR": 0.112,
      "pf": 1.23
    },
    "1m/RETEST/SHORT": {
      "n": 737,
      "wrTP1": 49.7,
      "expR": 0.056,
      "pf": 1.12
    },
    "2m/INV/LONG": {
      "n": 17,
      "wrTP1": 58.8,
      "expR": 0.506,
      "pf": 2.9
    },
    "2m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 0.01,
      "pf": 1.04
    },
    "2m/RETEST/LONG": {
      "n": 460,
      "wrTP1": 53.7,
      "expR": 0.333,
      "pf": 1.81
    },
    "2m/RETEST/SHORT": {
      "n": 302,
      "wrTP1": 53.0,
      "expR": 0.075,
      "pf": 1.18
    },
    "5m/INV/LONG": {
      "n": 1,
      "wrTP1": 100.0,
      "expR": 0.24,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 2,
      "wrTP1": 50.0,
      "expR": 0.21,
      "pf": 99.0
    },
    "5m/RETEST/LONG": {
      "n": 130,
      "wrTP1": 56.9,
      "expR": 0.297,
      "pf": 1.72
    },
    "5m/RETEST/SHORT": {
      "n": 106,
      "wrTP1": 49.1,
      "expR": 0.157,
      "pf": 1.36
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 14728,
  "brier": 0.2231,
  "bias": -0.057,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.17
    },
    {
      "feature": "nearTk",
      "weight": -0.102
    },
    {
      "feature": "stretchAtr",
      "weight": -0.05
    },
    {
      "feature": "rvol",
      "weight": 0.04
    },
    {
      "feature": "biasScore",
      "weight": -0.037
    },
    {
      "feature": "emaStack",
      "weight": 0.037
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.023
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.017
    },
    {
      "feature": "aligned",
      "weight": -0.017
    },
    {
      "feature": "nearEdge",
      "weight": 0.012
    },
    {
      "feature": "hourNY",
      "weight": -0.01
    },
    {
      "feature": "structDir",
      "weight": 0.01
    },
    {
      "feature": "chopIdx",
      "weight": -0.008
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.171,
      "actual": 0.191,
      "n": 1472
    },
    {
      "bin": 1,
      "pred": 0.373,
      "actual": 0.327,
      "n": 1473
    },
    {
      "bin": 2,
      "pred": 0.454,
      "actual": 0.359,
      "n": 1473
    },
    {
      "bin": 3,
      "pred": 0.499,
      "actual": 0.398,
      "n": 1473
    },
    {
      "bin": 4,
      "pred": 0.537,
      "actual": 0.508,
      "n": 1473
    },
    {
      "bin": 5,
      "pred": 0.566,
      "actual": 0.567,
      "n": 1472
    },
    {
      "bin": 6,
      "pred": 0.589,
      "actual": 0.614,
      "n": 1473
    },
    {
      "bin": 7,
      "pred": 0.609,
      "actual": 0.66,
      "n": 1473
    },
    {
      "bin": 8,
      "pred": 0.628,
      "actual": 0.697,
      "n": 1473
    },
    {
      "bin": 9,
      "pred": 0.656,
      "actual": 0.747,
      "n": 1473
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 8118,
  "testN": 7820,
  "testWeeks": [
    "2026-W38",
    "2026-W39"
  ],
  "model_oos_brier": 0.2227,
  "model_oos_n": 7820,
  "best_scheme_in_sample": {
    "scheme": "nextLevel",
    "trainExpR": 0.04
  },
  "best_scheme_oos_expR": 0.113
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.141,
    "ci90": [
      -0.048,
      0.357
    ],
    "p_mean_le_0": 0.114,
    "n": 144,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.025,
    "ci90": [
      -0.153,
      0.212
    ],
    "p_mean_le_0": 0.417,
    "n": 107,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.071,
    "ci90": [
      0.044,
      0.1
    ],
    "p_mean_le_0": 0.0,
    "n": 5829,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.052,
    "ci90": [
      0.019,
      0.087
    ],
    "p_mean_le_0": 0.005,
    "n": 3612,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.051,
    "ci90": [
      -0.165,
      0.292
    ],
    "p_mean_le_0": 0.36,
    "n": 55,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": -0.029,
    "ci90": [
      -0.337,
      0.332
    ],
    "p_mean_le_0": 0.568,
    "n": 45,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.072,
    "ci90": [
      0.031,
      0.115
    ],
    "p_mean_le_0": 0.003,
    "n": 2523,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.074,
    "ci90": [
      0.023,
      0.124
    ],
    "p_mean_le_0": 0.006,
    "n": 1553,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.396,
    "ci90": [
      0.023,
      0.769
    ],
    "p_mean_le_0": 0.039,
    "n": 16,
    "survives_fdr10": true
  },
  "5m/INV/SHORT": {
    "expR": 0.413,
    "ci90": [
      -0.198,
      1.048
    ],
    "p_mean_le_0": 0.127,
    "n": 10,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.179,
    "ci90": [
      0.109,
      0.25
    ],
    "p_mean_le_0": 0.0,
    "n": 863,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.102,
    "ci90": [
      0.015,
      0.189
    ],
    "p_mean_le_0": 0.028,
    "n": 539,
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
      "id": 0,
      "n": 6120,
      "wrTP1": 47.0,
      "expR": 0.098,
      "pf": 1.2,
      "defining_features": {
        "biasScore": 0.75,
        "nearEdge": 0.66,
        "emaStack": 0.64,
        "hourNY": -0.53
      }
    },
    {
      "id": 3,
      "n": 5467,
      "wrTP1": 46.2,
      "expR": 0.062,
      "pf": 1.13,
      "defining_features": {
        "biasScore": -1.15,
        "emaStack": -1.01,
        "nearEdge": -0.87,
        "structDir": -0.44
      }
    },
    {
      "id": 2,
      "n": 2654,
      "wrTP1": 49.9,
      "expR": 0.061,
      "pf": 1.13,
      "defining_features": {
        "hourNY": 1.33,
        "atrPctUsed": -0.85,
        "biasScore": 0.59,
        "emaStack": 0.59
      }
    },
    {
      "id": 1,
      "n": 1697,
      "wrTP1": 43.3,
      "expR": 0.053,
      "pf": 1.11,
      "defining_features": {
        "stretchAtr": 1.81,
        "rvol": 1.59,
        "chopIdx": -1.44,
        "hourNY": -0.18
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
        "n": 31,
        "wrTP1": 54.8,
        "expR": 0.434
      },
      "YM": {
        "n": 60,
        "wrTP1": 33.3,
        "expR": 0.274
      },
      "ES": {
        "n": 23,
        "wrTP1": 60.9,
        "expR": 0.138
      },
      "GC": {
        "n": 24,
        "wrTP1": 33.3,
        "expR": -0.428
      },
      "NQ": {
        "n": 15,
        "wrTP1": 46.7,
        "expR": -0.033
      }
    },
    "expR_spread": 0.862,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 59,
        "wrTP1": 40.7,
        "expR": -0.073
      },
      "NQ": {
        "n": 10,
        "wrTP1": 50.0,
        "expR": 0.071
      },
      "ES": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.57
      },
      "GC": {
        "n": 23,
        "wrTP1": 65.2,
        "expR": 0.216
      },
      "CL": {
        "n": 12,
        "wrTP1": 41.7,
        "expR": -0.178
      }
    },
    "expR_spread": 0.748,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 996,
        "wrTP1": 43.1,
        "expR": 0.048
      },
      "NQ": {
        "n": 1304,
        "wrTP1": 46.7,
        "expR": 0.061
      },
      "ES": {
        "n": 1468,
        "wrTP1": 47.9,
        "expR": 0.091
      },
      "CL": {
        "n": 1290,
        "wrTP1": 45.9,
        "expR": 0.048
      },
      "YM": {
        "n": 945,
        "wrTP1": 45.7,
        "expR": 0.111
      }
    },
    "expR_spread": 0.063,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 417,
        "wrTP1": 42.0,
        "expR": 0.1
      },
      "GC": {
        "n": 976,
        "wrTP1": 47.0,
        "expR": 0.063
      },
      "YM": {
        "n": 1132,
        "wrTP1": 44.1,
        "expR": 0.069
      },
      "ES": {
        "n": 692,
        "wrTP1": 45.4,
        "expR": 0.024
      },
      "CL": {
        "n": 596,
        "wrTP1": 44.5,
        "expR": 0.002
      }
    },
    "expR_spread": 0.098,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 7,
        "wrTP1": 42.9,
        "expR": -0.376
      },
      "CL": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": -0.063
      },
      "YM": {
        "n": 16,
        "wrTP1": 31.2,
        "expR": -0.406
      },
      "ES": {
        "n": 13,
        "wrTP1": 84.6,
        "expR": 0.416
      },
      "NQ": {
        "n": 16,
        "wrTP1": 50.0,
        "expR": 0.439
      }
    },
    "expR_spread": 0.845,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 23,
        "wrTP1": 39.1,
        "expR": 0.096
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
      },
      "CL": {
        "n": 4,
        "wrTP1": 25.0,
        "expR": -0.665
      }
    },
    "expR_spread": 0.989,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 586,
        "wrTP1": 47.3,
        "expR": 0.08
      },
      "GC": {
        "n": 403,
        "wrTP1": 47.4,
        "expR": 0.074
      },
      "CL": {
        "n": 587,
        "wrTP1": 48.9,
        "expR": 0.051
      },
      "ES": {
        "n": 589,
        "wrTP1": 50.8,
        "expR": 0.078
      },
      "YM": {
        "n": 456,
        "wrTP1": 44.7,
        "expR": 0.08
      }
    },
    "expR_spread": 0.029,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 286,
        "wrTP1": 50.0,
        "expR": 0.052
      },
      "YM": {
        "n": 498,
        "wrTP1": 51.4,
        "expR": 0.152
      },
      "GC": {
        "n": 393,
        "wrTP1": 48.9,
        "expR": 0.088
      },
      "NQ": {
        "n": 201,
        "wrTP1": 42.3,
        "expR": 0.075
      },
      "CL": {
        "n": 232,
        "wrTP1": 47.0,
        "expR": -0.085
      }
    },
    "expR_spread": 0.237,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": -0.058
      },
      "YM": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.617
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 1.517
      },
      "ES": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.335
      }
    },
    "expR_spread": 1.575,
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
      }
    },
    "expR_spread": 1.85,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 91,
        "wrTP1": 53.8,
        "expR": 0.23
      },
      "ES": {
        "n": 196,
        "wrTP1": 53.6,
        "expR": 0.235
      },
      "YM": {
        "n": 164,
        "wrTP1": 53.0,
        "expR": 0.224
      },
      "CL": {
        "n": 186,
        "wrTP1": 57.5,
        "expR": 0.282
      },
      "NQ": {
        "n": 276,
        "wrTP1": 47.5,
        "expR": 0.024
      }
    },
    "expR_spread": 0.258,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 81,
        "wrTP1": 48.1,
        "expR": -0.017
      },
      "ES": {
        "n": 103,
        "wrTP1": 53.4,
        "expR": 0.072
      },
      "GC": {
        "n": 133,
        "wrTP1": 40.6,
        "expR": 0.052
      },
      "YM": {
        "n": 177,
        "wrTP1": 48.0,
        "expR": 0.173
      },
      "CL": {
        "n": 88,
        "wrTP1": 51.1,
        "expR": 0.173
      }
    },
    "expR_spread": 0.19,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 7,
  "near_news_30m": {
    "n": 38,
    "wrTP1": 39.5,
    "nSL": 17,
    "nTO": 6,
    "expR": -0.129,
    "pf": 0.76,
    "mfe_p25": 2.0,
    "mfe_p50": 4.5,
    "mfe_p75": 15.25,
    "winnerMAE_p75": 3.5,
    "winnerMAE_p90": 21.199999999999992,
    "loserMFEbeforeSL_p50": 1.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 6.0,
    "entryZoneTk_p50": -5.0,
    "revAfterSL_rate": 29.4
  },
  "away_from_news": {
    "n": 15900,
    "wrTP1": 46.8,
    "nSL": 7248,
    "nTO": 1204,
    "expR": 0.075,
    "pf": 1.16,
    "mfe_p25": 7.0,
    "mfe_p50": 17.0,
    "mfe_p75": 39.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 33.1
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
      "2026-09-22 (martes, salto de dato grande y genuino: el bus asento de una vez el lote de +1027 outcomes de 2026-09-21, n total de pares resueltos 13204->14160): los 5 segmentos ya propuestos (1m LONG/SHORT, 2m LONG, 5m LONG/SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG y 1m SHORT suman su DECIMOCUARTA/DECIMOQUINTA confirmacion (n=4493 y n=2611, deltas estables 0.132 y 0.142), 2m LONG suma su CUARTA lectura seguida (n=2081, delta 0.14, practicamente identico a ayer) y 5m LONG/SHORT tienen su primera lectura con dato nuevo desde el 09-21 y ambos se fortalecen (5m LONG delta 0.276->0.299, 5m SHORT delta 0.489->0.455 -- este ultimo baja un poco pero sigue siendo el efecto mas grande). HALLAZGO DEL DIA: 2m SHORT tiene su MEJOR lectura hasta ahora -- el limite inferior del CI90 sube de 0.04 a 0.057 (+42%), la subida mas grande en varias corridas -- pero todavia queda por debajo del rango tipico de graduacion de los 5 segmentos ya promovidos (~0.07-0.08 de limite inferior); se mantiene un dia mas como candidato debil/al filo, mas cerca que nunca. Nota en paralelo (no de este experimento, mismo mecanismo de SL): en INV/LONG (buy-ifvg.md) 1m certifica por primera vez a favor del SL de 3 capas (delta -0.323, CI90 no cruza cero) y 2m certifica por primera vez a favor del SL de vela-1 (delta +1.169, CI90 muy ancho, n=48 todavia chico) -- direcciones opuestas entre si, ninguno accionable todavia, pero primera senal estadistica real de esta medicion fuera de RETEST. Sin cambios de estado en este experimento: sigue 'proposed', changeDate null."
    ],
    "beforeN": 15542,
    "afterN": 0,
    "before": {
      "n": 15542,
      "wrTP1": 46.8,
      "nSL": 7100,
      "nTO": 1165,
      "expR": 0.074,
      "pf": 1.16,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.4
    },
    "after": {
      "n": 0
    }
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
      "2026-09-22 (martes, tercera lectura, con el lote grande de dato nuevo genuino del dia -- +1027 outcomes en todo el bus): 1m SHORT (cut>=1.2 n=1273 expR=0.124 CI90=[0.043,0.202]), 2m SHORT (n=475 expR=0.176 CI90=[0.051,0.297]) y 5m LONG (n=286 expR=0.45 CI90=[0.282,0.626]) siguen mostrando el mismo patron monotono, sin reversion en la tercera lectura. CAMBIO A VIGILAR: 1m LONG, que llevaba dos lecturas practicamente plano, hoy muestra un CI90 que ya no cruza cero (n=2055 expR=0.108 CI90=[0.051,0.167] vs baseline expR=0.075) -- todavia mas debil que los otros tres segmentos, pero ya no es claramente 'sin efecto'; 2m LONG sigue el mas debil/plano (n=850 expR=0.068 CI90=[-0.027,0.163], cruza cero). walk_forward.ready=true desde hace unos dias pero este corte especifico (rr1_threshold_cut) sigue sin evaluarse contra el split OOS -- pendiente antes de proponer un valor concreto. Sigue sin proponerse sc_min_rr en la revision semanal (la ultima fue el 09-20); revisar el patron de 1m LONG una vez mas el domingo antes de decidir si se suma a la propuesta."
    ],
    "beforeN": 15542,
    "afterN": 0,
    "before": {
      "n": 15542,
      "wrTP1": 46.8,
      "nSL": 7100,
      "nTO": 1165,
      "expR": 0.074,
      "pf": 1.16,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
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
    "date": "2026-09-24",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-23T19:22:22-05:00",
    "schema": "sa-plan-2",
    "cleanest": "GC",
    "focus": {
      "sym": "GC",
      "verdict": "WAIT",
      "window": "20:00-23:00 CT",
      "setup": {
        "es": "cluster VWAP/disc25/IBH roto 4344.1-4356.0, confluencia 11 pero ahora a 19.9 pts (86% del presupuesto de Asia) -- STRETCHED, se mantuvo intacto en la reapertura pero aun no a tiro",
        "en": "the broken VWAP/disc25/IBH cluster 4344.1-4356.0, confluence 11 but now 19.9 pts away (86% of Asia's budget) -- STRETCHED, held intact through the reopen but still not in reach"
      },
      "trigger": {
        "es": "esperar a que el precio se acerque de verdad al cluster (reduce la distancia bajo el 55% del presupuesto) y ahi buscar el rechazo confirmado con cierre 5m de vuelta bajo 4344.10; el permiso corto fusionado ya esta activo",
        "en": "wait for price to actually approach the cluster (cuts the distance under 55% of the budget) and only then look for a confirmed rejection with a 5m close back below 4344.10; the fused short permission is already active"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 4362.30 mata el setup de esta ventana",
        "en": "a sustained 5m close above 4362.30 kills this window's setup"
      },
      "note": {
        "es": "el instrumento mas limpio del bus (4 dias confirmados, el unico GO de ayer pago >=3R); se mantuvo quieto en la reapertura sin acercarse al nivel -- no persigas, espera que venga a ti",
        "en": "the cleanest instrument in the bus (4 confirmed days, yesterday's only GO paid >=3R); it stayed quiet through the reopen without approaching the level -- don't chase it, let it come to you"
      }
    },
    "summary": {
      "es": [
        "NQ: primera correccion real ayer (flush a VAL y recuperacion); en la reapertura ya rompio su propio no-trade y el cluster POC/EMA (ONL tocado 5x sin reclamo), zona SHORT aun mas lejos -- WAIT.",
        "ES: tesis alcista de 5 dias rota ayer; en la reapertura perdio su no-trade camino al minimo de ayer, sin zona tactica a tiro -- WAIT.",
        "GC: el mas limpio del bus, 4 dias confirmados bajistas; se mantuvo quieto en la reapertura sin acercarse al cluster VWAP/IBH (86% del presupuesto) -- WAIT.",
        "YM: tesis bajista confirmada 2 dias; en la reapertura ya extendio bajo el minimo de ayer sin necesidad de la zona dorada, que quedo aun mas lejos -- WAIT pese al mapa bonito.",
        "CL: el rally del EIA perdio impulso en la reapertura, retrocedio al borde del no-trade (91.99) -- WAIT, sin conviccion en ningun lado.",
        "mas limpio: GC",
        "sin GO esta noche en ningun instrumento -- la reapertura confirmo mas chop/continuacion sin tocar ninguna zona A+ a tiro; deja que el precio venga a los niveles, no lo persigas.",
        "limite $1000 por cuenta (extremo bajo) y 3 stops segu
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 6071,
  "by_verdict": {
    "AVOID": {
      "n": 1393,
      "wrTP1": 45.1,
      "nSL": 692,
      "nTO": 73,
      "expR": 0.007,
      "pf": 1.01,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 31.5,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.300000000000068,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 34.2
    },
    "GO": {
      "n": 798,
      "wrTP1": 52.5,
      "nSL": 319,
      "nTO": 60,
      "expR": 0.202,
      "pf": 1.48,
      "mfe_p25": 12.0,
      "mfe_p50": 29.0,
      "mfe_p75": 56.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 31.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.5,
      "revAfterSL_rate": 39.5
    },
    "WAIT": {
      "n": 3880,
      "wrTP1": 47.8,
      "nSL": 1726,
      "nTO": 298,
      "expR": 0.068,
      "pf": 1.14,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 35.1
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.007,
      "ci90": [
        -0.048,
        0.064
      ],
      "p_mean_le_0": 0.427,
      "n": 1347
    },
    "GO": {
      "expR": 0.202,
      "ci90": [
        0.127,
        0.282
      ],
      "p_mean_le_0": 0.0,
      "n": 758
    },
    "WAIT": {
      "expR": 0.068,
      "ci90": [
        0.035,
        0.102
      ],
      "p_mean_le_0": 0.0,
      "n": 3698
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1393,
      "wrTP1": 45.1,
      "nSL": 692,
      "nTO": 73,
      "expR": 0.007,
      "pf": 1.01,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 31.5,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.300000000000068,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 34.2
    },
    "GO_or_WAIT": {
      "n": 4678,
      "wrTP1": 48.6,
      "nSL": 2045,
      "nTO": 358,
      "expR": 0.091,
      "pf": 1.2,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 35.7
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.007,
      "ci90": [
        -0.048,
        0.064
      ],
      "p_mean_le_0": 0.427,
      "n": 1347
    },
    "GO_or_WAIT": {
      "expR": 0.091,
      "ci90": [
        0.063,
        0.122
      ],
      "p_mean_le_0": 0.0,
      "n": 4456
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 13,
        "wrTP1": 53.8,
        "nSL": 5,
        "nTO": 1,
        "expR": -0.028,
        "pf": 0.93,
        "mfe_p25": 5.0,
        "mfe_p50": 6.0,
        "mfe_p75": 29.0,
        "winnerMAE_p75": 0.0,
        "winnerMAE_p90": 1.6000000000000014,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 40.0
      },
      "GO": {
        "n": 11,
        "wrTP1": 54.5,
        "nSL": 4,
        "nTO": 1,
        "expR": -0.071,
        "pf": 0.82,
        "mfe_p25": 18.5,
        "mfe_p50": 26.0,
        "mfe_p75": 30.5,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 30.0,
        "loserMFEbeforeSL_p50": 9.5,
        "bars_win_p50": 6.5,
        "bars_loss_p50": 3.5,
        "entryZoneTk_p50": -48.0,
        "revAfterSL_rate": 25.0
      },
      "WAIT": {
        "n": 58,
        "wrTP1": 39.7,
        "nSL": 27,
        "nTO": 8,
        "expR": -0.081,
        "pf": 0.84,
        "mfe_p25": 7.25,
        "mfe_p50": 17.0,
        "mfe_p75": 32.5,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 24.8,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 18.5
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 22,
        "wrTP1": 31.8,
        "nSL": 13,
        "nTO": 2,
        "expR": -0.403,
        "pf": 0.35,
        "mfe_p25": 6.0,
        "mfe_p50": 13.0,
        "mfe_p75": 21.0,
        "winnerMAE_p75": 5.0,
        "winnerMAE_p90": 7.200000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -10.5,
        "revAfterSL_rate": 15.4
      },
      "WAIT": {
        "n": 38,
        "wrTP1": 42.1,
        "nSL": 18,
        "nTO": 4,
        "expR": -0.232,
        "pf": 0.55,
        "mfe_p25": 6.0,
        "mfe_p50": 18.0,
        "mfe_p75": 35.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 69.5,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 8.0,
        "entryZoneTk_p50": -12.5,
        "revAfterSL_rate": 33.3
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 796,
        "wrTP1": 46.4,
        "nSL": 398,
        "nTO": 29,
        "expR": -0.015,
        "pf": 0.97,
        "mfe_p25": 6.0,
        "mfe_p50": 14.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 31.2
      },
      "GO": {
        "n": 519,
        "wrTP1": 50.7,
        "nSL": 222,
        "nTO": 34,
        "expR": 0.192,
        "pf": 1.43,
        "mfe_p25": 10.0,
        "mfe_p50": 27.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 30.80000000000001,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 37.4
      },
      "WAIT": {
        "n": 2330,
        "wrTP1": 49.7,
        "nSL": 1009,
        "nTO": 164,
        "expR": 0.119,
        "pf": 1.26,
        "mfe_p25": 7.0,
        "mfe_p50": 18.0,
        "mfe_p75": 40.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 36.8
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 562,
        "wrTP1": 43.6,
        "nSL": 276,
        "nTO": 41,
        "expR": 0.055,
        "pf": 1.11,
        "mfe_p25": 8.0,
        "mfe_p50": 16.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 39.5
      },
      "GO": {
        "n": 264,
        "wrTP1": 55.7,
        "nSL": 92,
        "nTO": 25,
        "expR": 0.222,
        "pf": 1.59,
        "mfe_p25": 14.0,
        "mfe_p50": 32.5,
        "mfe_p75": 56.75,
        "winnerMAE_p75": 20.5,
        "winnerMAE_p90": 30.80000000000001,
        "loserMFEbeforeSL_p50": 5.5,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 45.7
      },
      "WAIT": {
        "n": 1454,
        "wrTP1": 45.4,
        "nSL": 672,
        "nTO": 122,
        "expR": -0.003,
        "pf": 0.99,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 33.2
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
    "version": 1,
    "definedAt": "2026-09-20",
    "criteria": {
      "kind": [
        "RETEST"
      ],
      "tf_side": [
        "1/LONG",
        "1/SHORT",
        "2/SHORT",
        "5/LONG"
      ],
      "excludeSaVerdict": [
        "AVOID"
      ]
    },
    "rationale": "kind=RETEST (prioridad 1; INV no tiene ningun segmento con survives_fdr10=true todavia). tf/side limitado a los 4 segmentos que hoy sobreviven FDR10 en segment_significance (1m LONG, 1m SHORT, 2m SHORT, 5m LONG) -- 2m LONG y 5m SHORT quedan fuera porque su CI90 de E[R] cruza o roza cero. Se excluyen senales del dia/sesion en un instrumento con veredicto Session Analyst=AVOID: avoid_vs_rest_ci90.AVOID no es significativo (p_mean_le_0 alto) mientras GO y WAIT si lo son (session_analyst_cross). SL/objetivo = el mismo del indicador (3 capas); el SL estructural de experiments.json (sl-retest-wick) sigue 'proposed' sin changeDate, no se incorpora a la sombra hasta que tenga muestra post-cambio."
  },
  "shadow": {
    "n": 11273,
    "wrTP1": 46.6,
    "nSL": 5132,
    "nTO": 883,
    "expR": 0.077,
    "pf": 1.16,
    "mfe_p25": 7.0,
    "mfe_p50": 17.0,
    "mfe_p75": 39.0,
    "winnerMAE_p75": 11.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -13.0,
    "revAfterSL_rate": 32.4
  },
  "shadow_ci90": {
    "expR": 0.077,
    "ci90": [
      0.057,
      0.097
    ],
    "p_mean_le_0": 0.0,
    "n": 10830
  },
  "raw_indicator": {
    "n": 15542,
    "wrTP1": 46.8,
    "nSL": 7100,
    "nTO": 1165,
    "expR": 0.074,
    "pf": 1.16,
    "mfe_p25": 7.0,
    "mfe_p50": 17.0,
    "mfe_p75": 39.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 33.4
  },
  "raw_indicator_ci90": {
    "expR": 0.074,
    "ci90": [
      0.057,
      0.092
    ],
    "p_mean_le_0": 0.0,
    "n": 14919
  },
  "tier_ap_b_only": {
    "n": 7644,
    "wrTP1": 44.4,
    "nSL": 3627,
    "nTO": 625,
    "expR": 0.086,
    "pf": 1.17,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 31.2
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.086,
    "ci90": [
      0.06,
      0.112
    ],
    "p_mean_le_0": 0.0,
    "n": 7331
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```
