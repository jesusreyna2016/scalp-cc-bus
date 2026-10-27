# Scalp CC · report 2026-10-27T01:14Z
- signals=39987 outcomes=38491 pares_resueltos=39950 pendientes=37 huerfanos=46

## ⚠ ALERTAS (llevar al frente del resumen)
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.188 vs 0.042, delta 0.146 CI90 [0.122, 0.17], n 25736). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.128 vs 0.028, delta 0.1 CI90 [0.059, 0.142], n 7791). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.036 CI90 [0.019, 0.054], n 13916). Consistente con la hipotesis original de agent-instructions.md.
- METODO: tus predicciones de direccion aciertan 33.3% (peor que un volado, n=6, MAE=0.26). Se mas conservador con 'cambio del mes' y marcar experimental mas tiempo antes de subir confianza.
- MODO SOMBRA: 3 semanas CERRADAS seguidas sin batir al indicador crudo (2026-W41, 2026-W42, 2026-W43) -- espejo inverso del gate de promocion del peldano 0->1. No implica bajar de peldano (ya promovido), pero revisar shadow_rules en la revision semanal.

- E[R] global: {"expR": 0.043, "ci90": [0.032, 0.053], "p_mean_le_0": 0.0, "n": 38445}
- gate ejecucion: {"readyForLive": false, "segment": null, "weeklyStable3": null, "weeklyDetail": [], "slCauseMitigated": false, "fullyReady": false, "note": "readyForLive: n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side (solo agregado historico). fullyReady exige ademas weeklyStable3 (3 semanas CERRADAS seguidas con WR>=50 & PF>=1.3 en ese mismo segmento) y slCauseMitigated (experimento con verdict=confirmed dirigido a ese segmento). Solo fullyReady=true es luz verde real para subir de peldano; readyForLive=true con fullyReady=false es un near-miss a vigilar."}

## Integridad de sigId (colisiones, posible causa de alertas MUESTRA)
```json
{
  "signals": {
    "total_sigIds": 36468,
    "collided_sigIds": 3284,
    "collided_pct": 9.01,
    "delta_days_histogram": {
      "14": 873,
      "7": 828,
      "21": 458,
      "28": 324,
      "35": 216,
      "42": 172,
      "49": 63,
      "6": 54,
      "20": 50,
      "13": 44
    },
    "conflicting_result_n": 0,
    "conflicting_result_examples": []
  },
  "outcomes": {
    "total_sigIds": 35195,
    "collided_sigIds": 3076,
    "collided_pct": 8.74,
    "delta_days_histogram": {
      "14": 828,
      "7": 770,
      "21": 422,
      "28": 313,
      "35": 209,
      "42": 161,
      "49": 58,
      "6": 52,
      "20": 41,
      "13": 33
    },
    "conflicting_result_n": 1778,
    "conflicting_result_examples": [
      "NQ-2-22070-L",
      "NQ-2-22078-L",
      "GC-1-23456-S",
      "GC-1-23459-S",
      "YM-1-22698-S",
      "YM-1-22701-S",
      "GC-1-23515-S",
      "GC-1-23511-S"
    ]
  },
  "note": "colision = mismo sigId en >1 archivo diario con receivedAt distinto. 'last wins' en build_pairs() descarta una ocurrencia; si conflicting_result_n>0 confirma que son pares reales distintos, no un reenvio del mismo evento."
}
```

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 15m/RETEST/SHORT | 6 | 100.0 | 1.377 | 99.0 | 0 | 9132.0 | 3668.0 | None |
| 1m/INV/LONG | 403 | 46.4 | 0.132 | 1.3 | 170 | 14.0 | 10.5 | 18.2 |
| 1m/INV/SHORT | 281 | 47.0 | 0.078 | 1.18 | 111 | 21.0 | 14.0 | 15.3 |
| 1m/RETEST/LONG | 14924 | 44.8 | 0.03 | 1.06 | 7173 | 14.0 | 10.0 | 28.2 |
| 1m/RETEST/SHORT | 9429 | 44.6 | 0.031 | 1.06 | 4392 | 19.0 | 12.0 | 28.6 |
| 2m/INV/LONG | 146 | 50.7 | 0.026 | 1.06 | 60 | 16.0 | 15.25 | 16.7 |
| 2m/INV/SHORT | 104 | 46.2 | 0.118 | 1.27 | 43 | 28.0 | 13.25 | 34.9 |
| 2m/RETEST/LONG | 6553 | 47.4 | 0.044 | 1.09 | 3073 | 19.0 | 12.0 | 37.4 |
| 2m/RETEST/SHORT | 4105 | 47.6 | 0.054 | 1.11 | 1893 | 25.0 | 14.0 | 38.1 |
| 5m/INV/LONG | 39 | 69.2 | 0.239 | 2.07 | 8 | 28.5 | 25.0 | 75.0 |
| 5m/INV/SHORT | 23 | 56.5 | 0.11 | 1.29 | 8 | 21.0 | 50.0 | 37.5 |
| 5m/RETEST/LONG | 2370 | 51.2 | 0.104 | 1.23 | 1016 | 29.0 | 20.0 | 48.1 |
| 5m/RETEST/SHORT | 1567 | 47.7 | 0.069 | 1.15 | 686 | 35.0 | 22.5 | 39.4 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 2973 | 22.2 | 0.006 | 1.01 | 1940 | 27.0 | 12.0 | 17.2 |
| B | 17595 | 46.8 | 0.037 | 1.08 | 8132 | 18.0 | 12.0 | 33.5 |
| C | 19382 | 49.0 | 0.053 | 1.12 | 8561 | 18.0 | 13.0 | 34.3 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 14555 | 47.8 | 0.066 | 1.14 | 6647 | 13.0 | 9.0 | 33.9 |
| London | 5919 | 46.1 | 0.023 | 1.05 | 2933 | 18.0 | 12.0 | 34.5 |
| NY | 7112 | 44.4 | 0.032 | 1.06 | 3398 | 27.0 | 17.0 | 34.6 |
| Sin KZ | 12364 | 44.8 | 0.031 | 1.06 | 5655 | 20.0 | 13.0 | 27.3 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 9775 | 44.0 | 0.026 | 1.05 | 4628 | 22.0 | 14.75 | 29.6 |
| edge=0 | 16553 | 48.9 | 0.057 | 1.12 | 7451 | 17.0 | 11.0 | 36.3 |
| edge=1 | 13622 | 44.0 | 0.038 | 1.08 | 6554 | 18.0 | 12.0 | 29.2 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 28 | 67.9 | 0.576 | 4.31 | 4 | 303.0 | 1453.5 | 75.0 |
| aligned=1 | 39922 | 46.0 | 0.042 | 1.09 | 18629 | 18.0 | 12.0 | 32.1 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 13 | 38.5 | -0.152 | 0.75 | 8 | 9.0 | 7.0 | 25.0 |
| INV/LONG|edge=0 | 212 | 57.1 | 0.187 | 1.51 | 74 | 14.0 | 11.0 | 27.0 |
| INV/LONG|edge=1 | 363 | 44.6 | 0.079 | 1.17 | 156 | 16.0 | 13.0 | 16.0 |
| INV/SHORT|edge=-1 | 249 | 43.8 | 0.025 | 1.05 | 109 | 25.0 | 13.0 | 17.4 |
| INV/SHORT|edge=0 | 149 | 52.3 | 0.175 | 1.47 | 49 | 20.0 | 17.0 | 32.7 |
| INV/SHORT|edge=1 | 10 | 60.0 | 0.521 | 2.3 | 4 | 21.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 959 | 49.7 | 0.089 | 1.19 | 432 | 15.0 | 11.0 | 39.8 |
| RETEST/LONG|edge=0 | 10082 | 48.9 | 0.046 | 1.1 | 4620 | 15.0 | 10.0 | 36.0 |
| RETEST/LONG|edge=1 | 12806 | 43.7 | 0.034 | 1.07 | 6210 | 18.0 | 12.0 | 29.4 |
| RETEST/SHORT|edge=-1 | 8554 | 43.3 | 0.02 | 1.04 | 4079 | 23.0 | 15.0 | 28.8 |
| RETEST/SHORT|edge=0 | 6110 | 48.6 | 0.067 | 1.14 | 2708 | 20.0 | 12.0 | 37.1 |
| RETEST/SHORT|edge=1 | 443 | 53.0 | 0.105 | 1.24 | 184 | 20.5 | 16.5 | 36.4 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 224 | 41.5 | 0.072 | 1.15 | 103 | 15.0 | 13.0 | 12.6 |
| INV/LONG|tier=C | 364 | 53.6 | 0.138 | 1.35 | 135 | 15.0 | 12.0 | 25.2 |
| INV/SHORT|tier=B | 142 | 47.9 | 0.058 | 1.13 | 61 | 25.5 | 12.0 | 9.8 |
| INV/SHORT|tier=C | 266 | 47.0 | 0.108 | 1.26 | 101 | 22.0 | 20.0 | 28.7 |
| RETEST/LONG|tier=A+ | 1898 | 21.8 | 0.004 | 1.01 | 1263 | 23.0 | 10.0 | 15.4 |
| RETEST/LONG|tier=B | 10373 | 47.0 | 0.046 | 1.09 | 4813 | 16.0 | 11.0 | 35.0 |
| RETEST/LONG|tier=C | 11576 | 49.3 | 0.043 | 1.09 | 5186 | 16.0 | 12.0 | 34.3 |
| RETEST/SHORT|tier=A+ | 1075 | 22.9 | 0.008 | 1.01 | 677 | 36.0 | 15.0 | 20.5 |
| RETEST/SHORT|tier=B | 6856 | 46.5 | 0.024 | 1.05 | 3155 | 20.0 | 13.0 | 32.3 |
| RETEST/SHORT|tier=C | 7176 | 48.4 | 0.063 | 1.14 | 3139 | 22.0 | 14.0 | 34.8 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 588 | 49.0 | 0.113 | 1.26 | 238 | 15.0 | 12.0 | 19.7 |
| INV/SHORT|aligned=1 | 408 | 47.3 | 0.09 | 1.21 | 162 | 23.0 | 14.0 | 21.6 |
| RETEST/LONG|aligned=0 | 15 | 53.3 | 0.31 | 2.55 | 2 | 70.0 | 94.25 | 50.0 |
| RETEST/LONG|aligned=1 | 23832 | 46.1 | 0.041 | 1.08 | 11260 | 17.0 | 11.0 | 32.5 |
| RETEST/SHORT|aligned=0 | 13 | 84.6 | 0.78 | 6.07 | 2 | 7146.0 | 3524.0 | 100.0 |
| RETEST/SHORT|aligned=1 | 15094 | 45.7 | 0.041 | 1.08 | 6969 | 22.0 | 14.0 | 32.2 |

## Autopsia de SL
n_losses=18633  causas: RR-bajo×6847, contra-estructura×6260, stop-en-el-minimo×5990, killzone-Asia-largo×4296, sin-nivel-detras×3366, estirado×3125, chop×2807, SL-muy-pegado×2392, sin-causa-clara×2053, contra-sesgo×4
- INV/LONG (n=238): killzone-Asia-largo×115, RR-bajo×88, contra-estructura×74, estirado×51, stop-en-el-minimo×47, sin-nivel-detras×31, chop×27, SL-muy-pegado×24, sin-causa-clara×14
- INV/SHORT (n=162): RR-bajo×68, contra-estructura×50, estirado×37, stop-en-el-minimo×35, SL-muy-pegado×30, sin-causa-clara×23, chop×22, sin-nivel-detras×10
- RETEST/LONG (n=11262): RR-bajo×4187, killzone-Asia-largo×4181, contra-estructura×3939, stop-en-el-minimo×3659, sin-nivel-detras×2099, estirado×1898, chop×1712, SL-muy-pegado×1376, sin-causa-clara×976, contra-sesgo×2
- RETEST/SHORT (n=6971): RR-bajo×2504, stop-en-el-minimo×2249, contra-estructura×2197, sin-nivel-detras×1226, estirado×1139, chop×1046, sin-causa-clara×1040, SL-muy-pegado×962, contra-sesgo×2

## Autopsia de SL · semana 2026-W44 (para revision semanal)
n_losses=305  causas: RR-bajo×134, contra-estructura×128, stop-en-el-minimo×92, estirado×47, sin-nivel-detras×46, SL-muy-pegado×43, killzone-Asia-largo×40, chop×37, sin-causa-clara×28, contra-sesgo×3
ejemplos por causa: {"RR-bajo": ["GC-1-27823-S", "ES-1-21057-S", "NQ-1-21584-L", "ES-1-21331-S", "ES-2-21101-S"], "contra-estructura": ["ES-1-21057-S", "NQ-1-21584-L", "ES-1-21331-S", "NQ-1-21587-L", "YM-2-20996-L"], "stop-en-el-minimo": ["ES-1-21057-S", "NQ-1-21584-L", "ES-5-20698-S", "YM-5-20763-L", "NQ-1-21587-L"]}

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
    "n": 38432,
    "naive_expR": 0.043,
    "managed_expR": 0.128,
    "delta": 0.085,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 46.1,
    "fill_full_pct": 32.7,
    "m1_rate": 37.4,
    "m2_rate": 22.9,
    "m3_rate": 11.9,
    "beAfterM1_rate": 18.2
  },
  "by_tf_kind_side": {
    "15m/RETEST/SHORT": {
      "n": 6,
      "naive_expR": 1.377,
      "managed_expR": 0.525,
      "delta": -0.852,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 16.7,
      "fill_full_pct": 16.7,
      "m1_rate": 50.0,
      "m2_rate": 33.3,
      "m3_rate": 16.7,
      "beAfterM1_rate": 16.7
    },
    "1m/INV/LONG": {
      "n": 389,
      "naive_expR": 0.132,
      "managed_expR": 0.262,
      "delta": 0.129,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 49.4,
      "fill_full_pct": 36.0,
      "m1_rate": 40.9,
      "m2_rate": 24.9,
      "m3_rate": 12.6,
      "beAfterM1_rate": 19.5
    },
    "1m/INV/SHORT": {
      "n": 264,
      "naive_expR": 0.078,
      "managed_expR": 0.276,
      "delta": 0.198,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 48.9,
      "fill_full_pct": 36.4,
      "m1_rate": 39.0,
      "m2_rate": 25.4,
      "m3_rate": 12.9,
      "beAfterM1_rate": 15.5
    },
    "1m/RETEST/LONG": {
      "n": 14502,
      "naive_expR": 0.03,
      "managed_expR": 0.123,
      "delta": 0.093,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.2,
      "fill_full_pct": 33.7,
      "m1_rate": 37.1,
      "m2_rate": 22.6,
      "m3_rate": 11.8,
      "beAfterM1_rate": 17.5
    },
    "1m/RETEST/SHORT": {
      "n": 8961,
      "naive_expR": 0.031,
      "managed_expR": 0.158,
      "delta": 0.127,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 48.6,
      "fill_full_pct": 34.2,
      "m1_rate": 38.9,
      "m2_rate": 24.2,
      "m3_rate": 12.5,
      "beAfterM1_rate": 18.2
    },
    "2m/INV/LONG": {
      "n": 141,
      "naive_expR": 0.026,
      "managed_expR": 0.132,
      "delta": 0.106,
      "avgEntryBetterTk_p50": 4.2,
      "fill_t3plus_pct": 56.0,
      "fill_full_pct": 41.8,
      "m1_rate": 29.1,
      "m2_rate": 19.9,
      "m3_rate": 8.5,
      "beAfterM1_rate": 11.3
    },
    "2m/INV/SHORT": {
      "n": 100,
      "naive_expR": 0.118,
      "managed_expR": 0.284,
      "delta": 0.166,
      "avgEntryBetterTk_p50": 3.3,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 37.0,
      "m1_rate": 38.0,
      "m2_rate": 27.0,
      "m3_rate": 16.0,
      "beAfterM1_rate": 13.0
    },
    "2m/RETEST/LONG": {
      "n": 6347,
      "naive_expR": 0.043,
      "managed_expR": 0.097,
      "delta": 0.054,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 44.8,
      "fill_full_pct": 31.8,
      "m1_rate": 36.2,
      "m2_rate": 21.9,
      "m3_rate": 11.6,
      "beAfterM1_rate": 18.4
    },
    "2m/RETEST/SHORT": {
      "n": 3947,
      "naive_expR": 0.054,
      "managed_expR": 0.135,
      "delta": 0.081,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 45.5,
      "fill_full_pct": 32.2,
      "m1_rate": 37.9,
      "m2_rate": 23.2,
      "m3_rate": 12.0,
      "beAfterM1_rate": 19.7
    },
    "5m/INV/LONG": {
      "n": 36,
      "naive_expR": 0.239,
      "managed_expR": 0.266,
      "delta": 0.027,
      "avgEntryBetterTk_p50": 1.9,
      "fill_t3plus_pct": 38.9,
      "fill_full_pct": 27.8,
      "m1_rate": 19.4,
      "m2_rate": 8.3,
      "m3_rate": 2.8,
      "beAfterM1_rate": 13.9
    },
    "5m/INV/SHORT": {
      "n": 21,
      "naive_expR": 0.11,
      "managed_expR": 0.203,
      "delta": 0.093,
      "avgEntryBetterTk_p50": 7.0,
      "fill_t3plus_pct": 61.9,
      "fill_full_pct": 38.1,
      "m1_rate": 23.8,
      "m2_rate": 14.3,
      "m3_rate": 14.3,
      "beAfterM1_rate": 9.5
    },
    "5m/RETEST/LONG": {
      "n": 2260,
      "naive_expR": 0.104,
      "managed_expR": 0.089,
      "delta": -0.015,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 36.5,
      "fill_full_pct": 25.4,
      "m1_rate": 36.5,
      "m2_rate": 22.0,
      "m3_rate": 11.2,
      "beAfterM1_rate": 19.8
    },
    "5m/RETEST/SHORT": {
      "n": 1458,
      "naive_expR": 0.068,
      "managed_expR": 0.092,
      "delta": 0.023,
      "avgEntryBetterTk_p50": 4.8,
      "fill_t3plus_pct": 40.5,
      "fill_full_pct": 26.9,
      "m1_rate": 35.7,
      "m2_rate": 22.2,
      "m3_rate": 11.7,
      "beAfterM1_rate": 18.8
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 34466,
    "layer_expR": 0.041,
    "orig_expR": 0.174,
    "delta_orig_minus_layer": 0.133,
    "delta_ci90": [
      0.112,
      0.155
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 47.7,
    "orig_wrTP1": 33.0,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 9.0,
    "orig_wider_pct": 3.6,
    "orig_saved_from_SL": 45,
    "orig_caused_SL": 5098
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 939,
      "layer_expR": 0.103,
      "orig_expR": 0.173,
      "delta_orig_minus_layer": 0.069,
      "delta_ci90": [
        -0.078,
        0.23
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.4,
      "orig_wrTP1": 26.6,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.9,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 224
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
      "n": 25736,
      "layer_expR": 0.042,
      "orig_expR": 0.188,
      "delta_orig_minus_layer": 0.146,
      "delta_ci90": [
        0.122,
        0.17
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.0,
      "orig_wrTP1": 33.5,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 42,
      "orig_caused_SL": 3760
    },
    "retestBar2": {
      "n": 7791,
      "layer_expR": 0.028,
      "orig_expR": 0.128,
      "delta_orig_minus_layer": 0.1,
      "delta_ci90": [
        0.059,
        0.142
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.5,
      "orig_wrTP1": 32.3,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 2.3,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 1114
    }
  },
  "by_tf_kind_side": {
    "15m/RETEST/SHORT": {
      "n": 6,
      "layer_expR": 1.377,
      "orig_expR": 0.968,
      "delta_orig_minus_layer": -0.408,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 100.0,
      "orig_wrTP1": 66.7,
      "slTk_p50": 7935.5,
      "slOrigTk_p50": 4006.0,
      "orig_wider_pct": 16.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 2
    },
    "1m/INV/LONG": {
      "n": 389,
      "layer_expR": 0.132,
      "orig_expR": 0.217,
      "delta_orig_minus_layer": 0.085,
      "delta_ci90": [
        -0.113,
        0.275
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.1,
      "orig_wrTP1": 25.2,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 2.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 89
    },
    "1m/INV/SHORT": {
      "n": 254,
      "layer_expR": 0.079,
      "orig_expR": 0.069,
      "delta_orig_minus_layer": -0.01,
      "delta_ci90": [
        -0.283,
        0.295
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.6,
      "orig_wrTP1": 24.4,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 1.2,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 64
    },
    "1m/RETEST/LONG": {
      "n": 12584,
      "layer_expR": 0.026,
      "orig_expR": 0.152,
      "delta_orig_minus_layer": 0.126,
      "delta_ci90": [
        0.09,
        0.162
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.6,
      "orig_wrTP1": 28.8,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.0,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 2113
    },
    "1m/RETEST/SHORT": {
      "n": 7929,
      "layer_expR": 0.027,
      "orig_expR": 0.13,
      "delta_orig_minus_layer": 0.104,
      "delta_ci90": [
        0.062,
        0.147
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.5,
      "orig_wrTP1": 32.2,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 2.3,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 1132
    },
    "2m/INV/LONG": {
      "n": 141,
      "layer_expR": 0.026,
      "orig_expR": 0.476,
      "delta_orig_minus_layer": 0.45,
      "delta_ci90": [
        -0.078,
        1.051
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 52.5,
      "orig_wrTP1": 28.4,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 3.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 34
    },
    "2m/INV/SHORT": {
      "n": 99,
      "layer_expR": 0.115,
      "orig_expR": 0.091,
      "delta_orig_minus_layer": -0.024,
      "delta_ci90": [
        -0.35,
        0.352
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.5,
      "orig_wrTP1": 30.3,
      "slTk_p50": 26.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 18
    },
    "2m/RETEST/LONG": {
      "n": 5835,
      "layer_expR": 0.044,
      "orig_expR": 0.18,
      "delta_orig_minus_layer": 0.136,
      "delta_ci90": [
        0.089,
        0.179
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.3,
      "orig_wrTP1": 35.5,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.5,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 808
    },
    "2m/RETEST/SHORT": {
      "n": 3594,
      "layer_expR": 0.057,
      "orig_expR": 0.183,
      "delta_orig_minus_layer": 0.127,
      "delta_ci90": [
        0.074,
        0.182
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.7,
      "orig_wrTP1": 35.9,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 5,
      "orig_caused_SL": 501
    },
    "5m/INV/LONG": {
      "n": 36,
      "layer_expR": 0.239,
      "orig_expR": -0.082,
      "delta_orig_minus_layer": -0.321,
      "delta_ci90": [
        -0.75,
        0.102
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 75.0,
      "orig_wrTP1": 41.7,
      "slTk_p50": 27.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 11.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 12
    },
    "5m/INV/SHORT": {
      "n": 20,
      "layer_expR": 0.09,
      "orig_expR": -0.634,
      "delta_orig_minus_layer": -0.724,
      "delta_ci90": [
        -1.033,
        -0.429
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 60.0,
      "orig_wrTP1": 25.0,
      "slTk_p50": 37.5,
      "slOrigTk_p50": 6.5,
      "orig_wider_pct": 15.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 7
    },
    "5m/RETEST/LONG": {
      "n": 2180,
      "layer_expR": 0.095,
      "orig_expR": 0.353,
      "delta_orig_minus_layer": 0.258,
      "delta_ci90": [
        0.162,
        0.364
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.7,
      "orig_wrTP1": 45.1,
      "slTk_p50": 28.0,
      "slOrigTk_p50": 18.0,
      "orig_wider_pct": 14.4,
      "orig_saved_from_SL": 17,
      "orig_caused_SL": 204
    },
    "5m/RETEST/SHORT": {
      "n": 1399,
      "layer_expR": 0.064,
      "orig_expR": 0.296,
      "delta_orig_minus_layer": 0.232,
      "delta_ci90": [
        0.114,
        0.372
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.9,
      "orig_wrTP1": 43.5,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 18.2,
      "orig_saved_from_SL": 11,
      "orig_caused_SL": 114
    }
  },
  "since_change": {
    "changeDate": "2026-09-26",
    "n": 18697,
    "by_tf_kind_side": {
      "15m/RETEST/SHORT": {
        "n": 6,
        "layer_expR": 1.377,
        "orig_expR": 0.968,
        "delta_orig_minus_layer": -0.408,
        "delta_ci90": [
          null,
          null
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 100.0,
        "orig_wrTP1": 66.7,
        "slTk_p50": 7935.5,
        "slOrigTk_p50": 4006.0,
        "orig_wider_pct": 16.7,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 2
      },
      "1m/INV/LONG": {
        "n": 223,
        "layer_expR": 0.089,
        "orig_expR": 0.44,
        "delta_orig_minus_layer": 0.351,
        "delta_ci90": [
          0.074,
          0.645
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 48.9,
        "orig_wrTP1": 27.8,
        "slTk_p50": 16.0,
        "slOrigTk_p50": 3.0,
        "orig_wider_pct": 0.9,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 47
      },
      "1m/INV/SHORT": {
        "n": 132,
        "layer_expR": 0.093,
        "orig_expR": -0.195,
        "delta_orig_minus_layer": -0.288,
        "delta_ci90": [
          -0.513,
          -0.065
        ],
        "delta_beats_zero": false,
        "delta_below_zero": true,
        "layer_wrTP1": 49.2,
        "orig_wrTP1": 22.7,
        "slTk_p50": 19.0,
        "slOrigTk_p50": 5.5,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 35
      },
      "1m/RETEST/LONG": {
        "n": 6688,
        "layer_expR": -0.001,
        "orig_expR": 0.109,
        "delta_orig_minus_layer": 0.11,
        "delta_ci90": [
          0.063,
          0.158
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 44.8,
        "orig_wrTP1": 28.1,
        "slTk_p50": 15.0,
        "slOrigTk_p50": 6.0,
        "orig_wider_pct": 1.1,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 1118
      },
      "1m/RETEST/SHORT": {
        "n": 4350,
        "layer_expR": 0.023,
        "orig_expR": 0.098,
        "delta_orig_minus_layer": 0.075,
        "delta_ci90": [
          0.024,
          0.125
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 46.6,
        "orig_wrTP1": 32.3,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 2.1,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 625
      },
      "2m/INV/LONG": {
        "n": 78,
        "layer_expR": 0.059,
        "orig_expR": 0.198,
        "delta_orig_minus_layer": 0.139,
        "delta_ci90": [
          -0.381,
          0.852
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 53.8,
        "orig_wrTP1": 28.2,
        "slTk_p50": 24.0,
        "slOrigTk_p50": 7.5,
        "orig_wider_pct": 1.3,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 20
      },
      "2m/INV/SHORT": {
        "n": 45,
        "layer_expR": 0.133,
        "orig_expR": -0.074,
        "delta_orig_minus_layer": -0.207,
        "delta_ci90": [
          -0.732,
          0.38
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 55.6,
        "orig_wrTP1": 28.9,
        "slTk_p50": 29.0,
        "slOrigTk_p50": 8.0,
        "orig_wider_pct": 2.2,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 12
      },
      "2m/RETEST/LONG": {
        "n": 3147,
        "layer_expR": 0.045,
        "orig_expR": 0.168,
        "delta_orig_minus_layer": 0.124,
        "delta_ci90": [
          0.066,
          0.182
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 49.4,
        "orig_wrTP1": 35.1,
        "slTk_p50": 19.0,
        "slOrigTk_p50": 9.0,
        "orig_wider_pct": 3.7,
        "orig_saved_from_SL": 3,
        "orig_caused_SL": 455
      },
      "2m/RETEST/SHORT": {
        "n": 1977,
        "layer_expR": 0.045,
        "orig_expR": 0.152,
        "delta_orig_minus_layer": 0.107,
        "delta_ci90": [
          0.035,
          0.176
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 48.9,
        "orig_wrTP1": 35.1,
        "slTk_p50": 25.0,
        "slOrigTk_p50": 12.0,
        "orig_wider_pct": 3.1,
        "orig_saved_from_SL": 3,
        "orig_caused_SL": 276
      },
      "5m/INV/LONG": {
        "n": 18,
        "layer_expR": 0.041,
        "orig_expR": 0.226,
        "delta_orig_minus_layer": 0.185,
        "delta_ci90": [
          -0.471,
          0.942
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 72.2,
        "orig_wrTP1": 44.4,
        "slTk_p50": 24.0,
        "slOrigTk_p50": 7.5,
        "orig_wider_pct": 5.6,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 5
      },
      "5m/INV/SHORT": {
        "n": 10,
        "layer_expR": -0.199,
        "orig_expR": -0.833,
        "delta_orig_minus_layer": -0.634,
        "delta_ci90": [
          -1.078,
          -0.18
        ],
        "delta_beats_zero": false,
        "delta_below_zero": true,
        "layer_wrTP1": 50.0,
        "orig_wrTP1": 10.0,
        "slTk_p50": 35.0,
        "slOrigTk_p50": 4.5,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 4
      },
      "5m/RETEST/LONG": {
        "n": 1219,
        "layer_expR": 0.069,
        "orig_expR": 0.318,
        "delta_orig_minus_layer": 0.248,
        "delta_ci90": [
          0.128,
          0.391
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 53.4,
        "orig_wrTP1": 45.4,
        "slTk_p50": 28.0,
        "slOrigTk_p50": 18.0,
        "orig_wider_pct": 13.0,
        "orig_saved_from_SL": 10,
        "orig_caused_SL": 107
      },
      "5m/RETEST/SHORT": {
        "n": 804,
        "layer_expR": 0.055,
        "orig_expR": 0.195,
        "delta_orig_minus_layer": 0.14,
        "delta_ci90": [
          0.043,
          0.251
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 50.9,
        "orig_wrTP1": 43.8,
        "slTk_p50": 34.0,
        "slOrigTk_p50": 23.0,
        "orig_wider_pct": 15.7,
        "orig_saved_from_SL": 4,
        "orig_caused_SL": 61
      }
    },
    "note": "emparejado (rOrig vs rMultiple) solo con recvDate >= changeDate; compara contra by_tf_kind_side (todo el historico) para ver si el efecto se mantiene, se encoge (optimismo in-sample esperable) o se invierte en la ventana nueva. NO confundir con prediction_scoreboard."
  }
}
```

## Contrafactual de entrada por RR minimo (candidato sc_min_rr, ataca causa RR-bajo)
```json
{
  "1/RETEST/LONG": {
    "baseline": {
      "n": 14415,
      "wrTP1": 46.3,
      "nSL": 6840,
      "nTO": 894,
      "expR": 0.026,
      "pf": 1.05,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 31.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 29.6,
      "ci90": {
        "expR": 0.026,
        "ci90": [
          0.009,
          0.042
        ],
        "p_mean_le_0": 0.004,
        "n": 14002
      }
    },
    "cuts": {
      "1.0": {
        "n": 7027,
        "wrTP1": 30.3,
        "nSL": 4239,
        "nTO": 659,
        "expR": 0.018,
        "pf": 1.03,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 20.6,
        "ci90": {
          "expR": 0.018,
          "ci90": [
            -0.01,
            0.046
          ],
          "p_mean_le_0": 0.161,
          "n": 6790
        }
      },
      "1.2": {
        "n": 5805,
        "wrTP1": 27.6,
        "nSL": 3599,
        "nTO": 602,
        "expR": 0.03,
        "pf": 1.05,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 42.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 18.3,
        "ci90": {
          "expR": 0.03,
          "ci90": [
            -0.004,
            0.064
          ],
          "p_mean_le_0": 0.075,
          "n": 5604
        }
      },
      "1.3": {
        "n": 5300,
        "wrTP1": 26.3,
        "nSL": 3332,
        "nTO": 576,
        "expR": 0.031,
        "pf": 1.05,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 42.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.0,
        "ci90": {
          "expR": 0.031,
          "ci90": [
            -0.005,
            0.068
          ],
          "p_mean_le_0": 0.073,
          "n": 5110
        }
      },
      "1.5": {
        "n": 4499,
        "wrTP1": 23.6,
        "nSL": 2908,
        "nTO": 528,
        "expR": 0.022,
        "pf": 1.03,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 5.5,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 15.0,
        "ci90": {
          "expR": 0.022,
          "ci90": [
            -0.017,
            0.063
          ],
          "p_mean_le_0": 0.169,
          "n": 4338
        }
      },
      "2.0": {
        "n": 2963,
        "wrTP1": 17.6,
        "nSL": 2008,
        "nTO": 433,
        "expR": 0.007,
        "pf": 1.01,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 44.0,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 11.1,
        "ci90": {
          "expR": 0.007,
          "ci90": [
            -0.046,
            0.06
          ],
          "p_mean_le_0": 0.436,
          "n": 2855
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 9021,
      "wrTP1": 46.6,
      "nSL": 4116,
      "nTO": 703,
      "expR": 0.035,
      "pf": 1.07,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 38.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 30.6,
      "ci90": {
        "expR": 0.035,
        "ci90": [
          0.016,
          0.057
        ],
        "p_mean_le_0": 0.001,
        "n": 8581
      }
    },
    "cuts": {
      "1.0": {
        "n": 4394,
        "wrTP1": 30.7,
        "nSL": 2541,
        "nTO": 504,
        "expR": 0.022,
        "pf": 1.04,
        "mfe_p25": 11.0,
        "mfe_p50": 26.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 21.7,
        "ci90": {
          "expR": 0.022,
          "ci90": [
            -0.014,
            0.056
          ],
          "p_mean_le_0": 0.161,
          "n": 4119
        }
      },
      "1.2": {
        "n": 3599,
        "wrTP1": 27.5,
        "nSL": 2152,
        "nTO": 456,
        "expR": 0.021,
        "pf": 1.03,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.4,
        "ci90": {
          "expR": 0.021,
          "ci90": [
            -0.019,
            0.063
          ],
          "p_mean_le_0": 0.207,
          "n": 3361
        }
      },
      "1.3": {
        "n": 3299,
        "wrTP1": 26.1,
        "nSL": 1998,
        "nTO": 441,
        "expR": 0.019,
        "pf": 1.03,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.5,
        "ci90": {
          "expR": 0.019,
          "ci90": [
            -0.029,
            0.066
          ],
          "p_mean_le_0": 0.258,
          "n": 3074
        }
      },
      "1.5": {
        "n": 2784,
        "wrTP1": 23.3,
        "nSL": 1734,
        "nTO": 401,
        "expR": 0.007,
        "pf": 1.01,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 16.6,
        "ci90": {
          "expR": 0.007,
          "ci90": [
            -0.043,
            0.057
          ],
          "p_mean_le_0": 0.417,
          "n": 2590
        }
      },
      "2.0": {
        "n": 1890,
        "wrTP1": 18.0,
        "nSL": 1238,
        "nTO": 312,
        "expR": -0.02,
        "pf": 0.97,
        "mfe_p25": 12.0,
        "mfe_p50": 29.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 12.0,
        "ci90": {
          "expR": -0.02,
          "ci90": [
            -0.083,
            0.047
          ],
          "p_mean_le_0": 0.702,
          "n": 1755
        }
      }
    }
  },
  "15/RETEST/SHORT": {
    "baseline": {
      "n": 6,
      "wrTP1": 100.0,
      "nSL": 0,
      "nTO": 0,
      "expR": 1.377,
      "pf": 99.0,
      "mfe_p25": 7180.5,
      "mfe_p50": 9132.0,
      "mfe_p75": 13995.75,
      "winnerMAE_p75": 3668.0,
      "winnerMAE_p90": 5906.0,
      "loserMFEbeforeSL_p50": null,
      "bars_win_p50": 1.0,
      "bars_loss_p50": null,
      "entryZoneTk_p50": -11840.0,
      "revAfterSL_rate": null,
      "ci90": null
    },
    "cuts": {}
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 6360,
      "wrTP1": 48.8,
      "nSL": 2944,
      "nTO": 313,
      "expR": 0.038,
      "pf": 1.08,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 39.0,
      "ci90": {
        "expR": 0.038,
        "ci90": [
          0.013,
          0.062
        ],
        "p_mean_le_0": 0.004,
        "n": 6164
      }
    },
    "cuts": {
      "1.0": {
        "n": 2939,
        "wrTP1": 31.9,
        "nSL": 1777,
        "nTO": 224,
        "expR": 0.028,
        "pf": 1.04,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 31.6,
        "ci90": {
          "expR": 0.028,
          "ci90": [
            -0.02,
            0.074
          ],
          "p_mean_le_0": 0.168,
          "n": 2821
        }
      },
      "1.2": {
        "n": 2418,
        "wrTP1": 28.7,
        "nSL": 1521,
        "nTO": 202,
        "expR": 0.022,
        "pf": 1.03,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.600000000000023,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 29.2,
        "ci90": {
          "expR": 0.022,
          "ci90": [
            -0.034,
            0.073
          ],
          "p_mean_le_0": 0.259,
          "n": 2317
        }
      },
      "1.3": {
        "n": 2183,
        "wrTP1": 27.4,
        "nSL": 1392,
        "nTO": 192,
        "expR": 0.027,
        "pf": 1.04,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.200000000000045,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 28.2,
        "ci90": {
          "expR": 0.027,
          "ci90": [
            -0.032,
            0.083
          ],
          "p_mean_le_0": 0.216,
          "n": 2089
        }
      },
      "1.5": {
        "n": 1805,
        "wrTP1": 24.0,
        "nSL": 1190,
        "nTO": 181,
        "expR": 0.011,
        "pf": 1.02,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 25.6,
        "ci90": {
          "expR": 0.011,
          "ci90": [
            -0.055,
            0.079
          ],
          "p_mean_le_0": 0.402,
          "n": 1719
        }
      },
      "2.0": {
        "n": 1156,
        "wrTP1": 18.6,
        "nSL": 800,
        "nTO": 141,
        "expR": 0.012,
        "pf": 1.02,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 61.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 21.0,
        "ci90": {
          "expR": 0.012,
          "ci90": [
            -0.078,
            0.104
          ],
          "p_mean_le_0": 0.411,
          "n": 1092
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 3905,
      "wrTP1": 50.0,
      "nSL": 1749,
      "nTO": 202,
      "expR": 0.071,
      "pf": 1.15,
      "mfe_p25": 11.0,
      "mfe_p50": 24.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 32.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 41.2,
      "ci90": {
        "expR": 0.071,
        "ci90": [
          0.04,
          0.103
        ],
        "p_mean_le_0": 0.0,
        "n": 3771
      }
    },
    "cuts": {
      "1.0": {
        "n": 1791,
        "wrTP1": 33.1,
        "nSL": 1065,
        "nTO": 134,
        "expR": 0.062,
        "pf": 1.1,
        "mfe_p25": 16.0,
        "mfe_p50": 33.0,
        "mfe_p75": 64.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 31.899999999999977,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 33.7,
        "ci90": {
          "expR": 0.062,
          "ci90": [
            0.0,
            0.121
          ],
          "p_mean_le_0": 0.049,
          "n": 1716
        }
      },
      "1.2": {
        "n": 1463,
        "wrTP1": 29.7,
        "nSL": 908,
        "nTO": 121,
        "expR": 0.057,
        "pf": 1.09,
        "mfe_p25": 17.0,
        "mfe_p50": 34.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 15.75,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 30.8,
        "ci90": {
          "expR": 0.057,
          "ci90": [
            -0.011,
            0.131
          ],
          "p_mean_le_0": 0.08,
          "n": 1399
        }
      },
      "1.3": {
        "n": 1325,
        "wrTP1": 28.2,
        "nSL": 839,
        "nTO": 113,
        "expR": 0.051,
        "pf": 1.08,
        "mfe_p25": 17.0,
        "mfe_p50": 35.0,
        "mfe_p75": 69.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 29.6,
        "ci90": {
          "expR": 0.051,
          "ci90": [
            -0.024,
            0.128
          ],
          "p_mean_le_0": 0.133,
          "n": 1267
        }
      },
      "1.5": {
        "n": 1097,
        "wrTP1": 25.3,
        "nSL": 720,
        "nTO": 99,
        "expR": 0.044,
        "pf": 1.06,
        "mfe_p25": 17.25,
        "mfe_p50": 36.0,
        "mfe_p75": 74.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 32.30000000000001,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 28.2,
        "ci90": {
          "expR": 0.044,
          "ci90": [
            -0.043,
            0.13
          ],
          "p_mean_le_0": 0.203,
          "n": 1050
        }
      },
      "2.0": {
        "n": 716,
        "wrTP1": 20.9,
        "nSL": 490,
        "nTO": 76,
        "expR": 0.064,
        "pf": 1.09,
        "mfe_p25": 18.0,
        "mfe_p50": 38.0,
        "mfe_p75": 78.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.099999999999994,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 24.1,
        "ci90": {
          "expR": 0.064,
          "ci90": [
            -0.05,
            0.183
          ],
          "p_mean_le_0": 0.188,
          "n": 684
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 2276,
      "wrTP1": 53.3,
      "nSL": 949,
      "nTO": 114,
      "expR": 0.114,
      "pf": 1.26,
      "mfe_p25": 13.0,
      "mfe_p50": 28.0,
      "mfe_p75": 60.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 42.0,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -31.0,
      "revAfterSL_rate": 51.5,
      "ci90": {
        "expR": 0.114,
        "ci90": [
          0.074,
          0.156
        ],
        "p_mean_le_0": 0.0,
        "n": 2173
      }
    },
    "cuts": {
      "1.0": {
        "n": 958,
        "wrTP1": 37.1,
        "nSL": 530,
        "nTO": 73,
        "expR": 0.172,
        "pf": 1.29,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 36.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 46.8,
        "ci90": {
          "expR": 0.172,
          "ci90": [
            0.09,
            0.255
          ],
          "p_mean_le_0": 0.001,
          "n": 896
        }
      },
      "1.2": {
        "n": 787,
        "wrTP1": 34.6,
        "nSL": 448,
        "nTO": 67,
        "expR": 0.189,
        "pf": 1.31,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 72.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 30.900000000000006,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 44.4,
        "ci90": {
          "expR": 0.189,
          "ci90": [
            0.092,
            0.29
          ],
          "p_mean_le_0": 0.001,
          "n": 731
        }
      },
      "1.3": {
        "n": 711,
        "wrTP1": 31.5,
        "nSL": 425,
        "nTO": 62,
        "expR": 0.148,
        "pf": 1.23,
        "mfe_p25": 18.0,
        "mfe_p50": 37.0,
        "mfe_p75": 72.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 28.700000000000017,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 43.1,
        "ci90": {
          "expR": 0.148,
          "ci90": [
            0.043,
            0.258
          ],
          "p_mean_le_0": 0.006,
          "n": 660
        }
      },
      "1.5": {
        "n": 593,
        "wrTP1": 29.8,
        "nSL": 367,
        "nTO": 49,
        "expR": 0.154,
        "pf": 1.23,
        "mfe_p25": 18.0,
        "mfe_p50": 36.0,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 41.4,
        "ci90": {
          "expR": 0.154,
          "ci90": [
            0.034,
            0.273
          ],
          "p_mean_le_0": 0.018,
          "n": 554
        }
      },
      "2.0": {
        "n": 386,
        "wrTP1": 23.8,
        "nSL": 259,
        "nTO": 35,
        "expR": 0.1,
        "pf": 1.14,
        "mfe_p25": 19.0,
        "mfe_p50": 41.0,
        "mfe_p75": 80.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 21.900000000000006,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 34.7,
        "ci90": {
          "expR": 0.1,
          "ci90": [
            -0.064,
            0.264
          ],
          "p_mean_le_0": 0.171,
          "n": 361
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 1467,
      "wrTP1": 50.9,
      "nSL": 618,
      "nTO": 102,
      "expR": 0.078,
      "pf": 1.17,
      "mfe_p25": 15.0,
      "mfe_p50": 34.0,
      "mfe_p75": 65.0,
      "winnerMAE_p75": 22.5,
      "winnerMAE_p90": 47.0,
      "loserMFEbeforeSL_p50": 4.5,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -32.0,
      "revAfterSL_rate": 43.7,
      "ci90": {
        "expR": 0.078,
        "ci90": [
          0.028,
          0.13
        ],
        "p_mean_le_0": 0.005,
        "n": 1376
      }
    },
    "cuts": {
      "1.0": {
        "n": 632,
        "wrTP1": 31.3,
        "nSL": 373,
        "nTO": 61,
        "expR": 0.036,
        "pf": 1.06,
        "mfe_p25": 21.0,
        "mfe_p50": 43.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 21.75,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 37.3,
        "ci90": {
          "expR": 0.036,
          "ci90": [
            -0.061,
            0.139
          ],
          "p_mean_le_0": 0.277,
          "n": 581
        }
      },
      "1.2": {
        "n": 514,
        "wrTP1": 28.0,
        "nSL": 318,
        "nTO": 52,
        "expR": 0.024,
        "pf": 1.04,
        "mfe_p25": 22.0,
        "mfe_p50": 44.0,
        "mfe_p75": 87.5,
        "winnerMAE_p75": 20.25,
        "winnerMAE_p90": 39.80000000000007,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 33.6,
        "ci90": {
          "expR": 0.024,
          "ci90": [
            -0.093,
            0.145
          ],
          "p_mean_le_0": 0.371,
          "n": 471
        }
      },
      "1.3": {
        "n": 474,
        "wrTP1": 27.0,
        "nSL": 298,
        "nTO": 48,
        "expR": 0.011,
        "pf": 1.02,
        "mfe_p25": 23.5,
        "mfe_p50": 45.0,
        "mfe_p75": 88.5,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 41.89999999999999,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 33.2,
        "ci90": {
          "expR": 0.011,
          "ci90": [
            -0.116,
            0.145
          ],
          "p_mean_le_0": 0.458,
          "n": 435
        }
      },
      "1.5": {
        "n": 391,
        "wrTP1": 25.6,
        "nSL": 246,
        "nTO": 45,
        "expR": 0.029,
        "pf": 1.04,
        "mfe_p25": 24.0,
        "mfe_p50": 49.0,
        "mfe_p75": 94.0,
        "winnerMAE_p75": 20.25,
        "winnerMAE_p90": 41.300000000000026,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 28.9,
        "ci90": {
          "expR": 0.029,
          "ci90": [
            -0.116,
            0.179
          ],
          "p_mean_le_0": 0.367,
          "n": 355
        }
      },
      "2.0": {
        "n": 260,
        "wrTP1": 19.6,
        "nSL": 179,
        "nTO": 30,
        "expR": -0.041,
        "pf": 0.95,
        "mfe_p25": 26.0,
        "mfe_p50": 53.0,
        "mfe_p75": 103.0,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 44.0,
        "loserMFEbeforeSL_p50": 13.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -31.5,
        "revAfterSL_rate": 25.7,
        "ci90": {
          "expR": -0.041,
          "ci90": [
            -0.226,
            0.148
          ],
          "p_mean_le_0": 0.639,
          "n": 238
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
    "2026-W43",
    "2026-W44"
  ],
  "1/RETEST/LONG": {
    "baseline": {
      "n": 1733,
      "wrTP1": 41.8,
      "nSL": 887,
      "nTO": 122,
      "expR": -0.02,
      "pf": 0.96,
      "mfe_p25": 6.0,
      "mfe_p50": 13.5,
      "mfe_p75": 29.0,
      "winnerMAE_p75": 8.0,
      "winnerMAE_p90": 15.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 5.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 26.4,
      "ci90": {
        "expR": -0.02,
        "ci90": [
          -0.066,
          0.029
        ],
        "p_mean_le_0": 0.745,
        "n": 1686
      }
    },
    "cuts": {
      "1.2": {
        "n": 766,
        "wrTP1": 26.6,
        "nSL": 476,
        "nTO": 86,
        "expR": 0.032,
        "pf": 1.05,
        "mfe_p25": 9.5,
        "mfe_p50": 21.0,
        "mfe_p75": 36.5,
        "winnerMAE_p75": 7.25,
        "winnerMAE_p90": 16.700000000000017,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 17.4,
        "ci90": {
          "expR": 0.032,
          "ci90": [
            -0.055,
            0.13
          ],
          "p_mean_le_0": 0.287,
          "n": 743
        }
      },
      "1.3": {
        "n": 715,
        "wrTP1": 25.7,
        "nSL": 450,
        "nTO": 81,
        "expR": 0.035,
        "pf": 1.05,
        "mfe_p25": 10.0,
        "mfe_p50": 21.0,
        "mfe_p75": 37.0,
        "winnerMAE_p75": 7.25,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 17.3,
        "ci90": {
          "expR": 0.035,
          "ci90": [
            -0.06,
            0.132
          ],
          "p_mean_le_0": 0.279,
          "n": 695
        }
      },
      "1.5": {
        "n": 618,
        "wrTP1": 23.3,
        "nSL": 398,
        "nTO": 76,
        "expR": 0.025,
        "pf": 1.04,
        "mfe_p25": 9.0,
        "mfe_p50": 21.0,
        "mfe_p75": 37.0,
        "winnerMAE_p75": 7.25,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 5.5,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 15.1,
        "ci90": {
          "expR": 0.025,
          "ci90": [
            -0.084,
            0.135
          ],
          "p_mean_le_0": 0.358,
          "n": 601
        }
      },
      "2.0": {
        "n": 438,
        "wrTP1": 18.3,
        "nSL": 295,
        "nTO": 63,
        "expR": 0.005,
        "pf": 1.01,
        "mfe_p25": 9.0,
        "mfe_p50": 21.0,
        "mfe_p75": 38.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 12.100000000000009,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 9.5,
        "ci90": {
          "expR": 0.005,
          "ci90": [
            -0.13,
            0.142
          ],
          "p_mean_le_0": 0.496,
          "n": 427
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 1350,
      "wrTP1": 46.4,
      "nSL": 648,
      "nTO": 76,
      "expR": 0.011,
      "pf": 1.02,
      "mfe_p25": 10.5,
      "mfe_p50": 24.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 31.0,
      "loserMFEbeforeSL_p50": 6.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 30.2,
      "ci90": {
        "expR": 0.011,
        "ci90": [
          -0.04,
          0.064
        ],
        "p_mean_le_0": 0.367,
        "n": 1315
      }
    },
    "cuts": {
      "1.2": {
        "n": 538,
        "wrTP1": 28.1,
        "nSL": 335,
        "nTO": 52,
        "expR": 0.006,
        "pf": 1.01,
        "mfe_p25": 17.0,
        "mfe_p50": 35.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 37.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 20.6,
        "ci90": {
          "expR": 0.006,
          "ci90": [
            -0.099,
            0.113
          ],
          "p_mean_le_0": 0.48,
          "n": 519
        }
      },
      "1.3": {
        "n": 494,
        "wrTP1": 27.1,
        "nSL": 309,
        "nTO": 51,
        "expR": 0.012,
        "pf": 1.02,
        "mfe_p25": 18.0,
        "mfe_p50": 35.5,
        "mfe_p75": 70.25,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 35.400000000000006,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 21.0,
        "ci90": {
          "expR": 0.012,
          "ci90": [
            -0.1,
            0.122
          ],
          "p_mean_le_0": 0.462,
          "n": 476
        }
      },
      "1.5": {
        "n": 408,
        "wrTP1": 24.3,
        "nSL": 260,
        "nTO": 49,
        "expR": 0.011,
        "pf": 1.02,
        "mfe_p25": 19.0,
        "mfe_p50": 37.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 14.5,
        "winnerMAE_p90": 25.400000000000006,
        "loserMFEbeforeSL_p50": 9.5,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 20.0,
        "ci90": {
          "expR": 0.011,
          "ci90": [
            -0.118,
            0.144
          ],
          "p_mean_le_0": 0.455,
          "n": 391
        }
      },
      "2.0": {
        "n": 270,
        "wrTP1": 18.1,
        "nSL": 182,
        "nTO": 39,
        "expR": -0.018,
        "pf": 0.97,
        "mfe_p25": 21.0,
        "mfe_p50": 38.5,
        "mfe_p75": 85.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 22.400000000000034,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 14.3,
        "ci90": {
          "expR": -0.018,
          "ci90": [
            -0.192,
            0.153
          ],
          "p_mean_le_0": 0.576,
          "n": 256
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 796,
      "wrTP1": 44.6,
      "nSL": 403,
      "nTO": 38,
      "expR": -0.003,
      "pf": 0.99,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 35.0,
      "winnerMAE_p75": 10.5,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 29.8,
      "ci90": {
        "expR": -0.003,
        "ci90": [
          -0.074,
          0.074
        ],
        "p_mean_le_0": 0.535,
        "n": 779
      }
    },
    "cuts": {
      "1.2": {
        "n": 358,
        "wrTP1": 27.4,
        "nSL": 236,
        "nTO": 24,
        "expR": -0.023,
        "pf": 0.97,
        "mfe_p25": 13.0,
        "mfe_p50": 28.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 17.299999999999997,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 25.0,
        "ci90": {
          "expR": -0.023,
          "ci90": [
            -0.157,
            0.117
          ],
          "p_mean_le_0": 0.623,
          "n": 350
        }
      },
      "1.3": {
        "n": 318,
        "wrTP1": 26.1,
        "nSL": 213,
        "nTO": 22,
        "expR": -0.014,
        "pf": 0.98,
        "mfe_p25": 14.0,
        "mfe_p50": 29.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 15.599999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 25.4,
        "ci90": {
          "expR": -0.014,
          "ci90": [
            -0.165,
            0.143
          ],
          "p_mean_le_0": 0.584,
          "n": 311
        }
      },
      "1.5": {
        "n": 267,
        "wrTP1": 22.8,
        "nSL": 187,
        "nTO": 19,
        "expR": -0.04,
        "pf": 0.94,
        "mfe_p25": 14.0,
        "mfe_p50": 29.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 16.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 23.0,
        "ci90": {
          "expR": -0.04,
          "ci90": [
            -0.205,
            0.129
          ],
          "p_mean_le_0": 0.646,
          "n": 261
        }
      },
      "2.0": {
        "n": 188,
        "wrTP1": 14.9,
        "nSL": 144,
        "nTO": 16,
        "expR": -0.135,
        "pf": 0.83,
        "mfe_p25": 14.0,
        "mfe_p50": 29.5,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 17.500000000000004,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 7.5,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 18.8,
        "ci90": {
          "expR": -0.135,
          "ci90": [
            -0.344,
            0.095
          ],
          "p_mean_le_0": 0.848,
          "n": 184
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 638,
      "wrTP1": 51.9,
      "nSL": 293,
      "nTO": 14,
      "expR": 0.064,
      "pf": 1.14,
      "mfe_p25": 15.0,
      "mfe_p50": 31.5,
      "mfe_p75": 66.0,
      "winnerMAE_p75": 19.0,
      "winnerMAE_p90": 42.0,
      "loserMFEbeforeSL_p50": 8.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -24.0,
      "revAfterSL_rate": 36.5,
      "ci90": {
        "expR": 0.064,
        "ci90": [
          -0.009,
          0.138
        ],
        "p_mean_le_0": 0.082,
        "n": 628
      }
    },
    "cuts": {
      "1.2": {
        "n": 229,
        "wrTP1": 31.4,
        "nSL": 149,
        "nTO": 8,
        "expR": 0.023,
        "pf": 1.03,
        "mfe_p25": 23.0,
        "mfe_p50": 44.5,
        "mfe_p75": 84.25,
        "winnerMAE_p75": 18.25,
        "winnerMAE_p90": 42.9,
        "loserMFEbeforeSL_p50": 18.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -24.0,
        "revAfterSL_rate": 30.2,
        "ci90": {
          "expR": 0.023,
          "ci90": [
            -0.14,
            0.188
          ],
          "p_mean_le_0": 0.416,
          "n": 224
        }
      },
      "1.3": {
        "n": 207,
        "wrTP1": 30.9,
        "nSL": 136,
        "nTO": 7,
        "expR": 0.035,
        "pf": 1.05,
        "mfe_p25": 24.25,
        "mfe_p50": 45.5,
        "mfe_p75": 85.0,
        "winnerMAE_p75": 17.25,
        "winnerMAE_p90": 41.500000000000014,
        "loserMFEbeforeSL_p50": 18.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -24.0,
        "revAfterSL_rate": 29.4,
        "ci90": {
          "expR": 0.035,
          "ci90": [
            -0.139,
            0.213
          ],
          "p_mean_le_0": 0.373,
          "n": 202
        }
      },
      "1.5": {
        "n": 163,
        "wrTP1": 28.8,
        "nSL": 110,
        "nTO": 6,
        "expR": 0.049,
        "pf": 1.07,
        "mfe_p25": 25.0,
        "mfe_p50": 46.0,
        "mfe_p75": 94.0,
        "winnerMAE_p75": 17.5,
        "winnerMAE_p90": 45.39999999999999,
        "loserMFEbeforeSL_p50": 19.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -24.0,
        "revAfterSL_rate": 27.3,
        "ci90": {
          "expR": 0.049,
          "ci90": [
            -0.161,
            0.269
          ],
          "p_mean_le_0": 0.361,
          "n": 158
        }
      },
      "2.0": {
        "n": 101,
        "wrTP1": 25.7,
        "nSL": 71,
        "nTO": 4,
        "expR": 0.102,
        "pf": 1.14,
        "mfe_p25": 25.25,
        "mfe_p50": 47.5,
        "mfe_p75": 124.5,
        "winnerMAE_p75": 13.5,
        "winnerMAE_p90": 40.5,
        "loserMFEbeforeSL_p50": 19.0,
        "bars_win_p50": 5.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -24.0,
        "revAfterSL_rate": 23.9,
        "ci90": {
          "expR": 0.102,
          "ci90": [
            -0.21,
            0.39
          ],
          "p_mean_le_0": 0.303,
          "n": 98
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 311,
      "wrTP1": 49.2,
      "nSL": 145,
      "nTO": 13,
      "expR": -0.045,
      "pf": 0.91,
      "mfe_p25": 14.5,
      "mfe_p50": 29.0,
      "mfe_p75": 53.5,
      "winnerMAE_p75": 23.0,
      "winnerMAE_p90": 88.60000000000002,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -39.0,
      "revAfterSL_rate": 37.9,
      "ci90": {
        "expR": -0.045,
        "ci90": [
          -0.142,
          0.054
        ],
        "p_mean_le_0": 0.775,
        "n": 299
      }
    },
    "cuts": {
      "1.2": {
        "n": 108,
        "wrTP1": 23.1,
        "nSL": 74,
        "nTO": 9,
        "expR": -0.325,
        "pf": 0.56,
        "mfe_p25": 17.75,
        "mfe_p50": 33.0,
        "mfe_p75": 53.25,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 29.000000000000014,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 31.1,
        "ci90": {
          "expR": -0.325,
          "ci90": [
            -0.522,
            -0.125
          ],
          "p_mean_le_0": 0.996,
          "n": 100
        }
      },
      "1.3": {
        "n": 96,
        "wrTP1": 16.7,
        "nSL": 71,
        "nTO": 9,
        "expR": -0.461,
        "pf": 0.43,
        "mfe_p25": 16.0,
        "mfe_p50": 34.0,
        "mfe_p75": 55.5,
        "winnerMAE_p75": 11.25,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 29.6,
        "ci90": {
          "expR": -0.461,
          "ci90": [
            -0.648,
            -0.255
          ],
          "p_mean_le_0": 1.0,
          "n": 88
        }
      },
      "1.5": {
        "n": 81,
        "wrTP1": 16.0,
        "nSL": 62,
        "nTO": 6,
        "expR": -0.468,
        "pf": 0.43,
        "mfe_p25": 15.75,
        "mfe_p50": 32.5,
        "mfe_p75": 54.25,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 30.60000000000001,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 24.2,
        "ci90": {
          "expR": -0.468,
          "ci90": [
            -0.685,
            -0.236
          ],
          "p_mean_le_0": 1.0,
          "n": 76
        }
      },
      "2.0": {
        "n": 50,
        "wrTP1": 6.0,
        "nSL": 45,
        "nTO": 2,
        "expR": -0.749,
        "pf": 0.18,
        "mfe_p25": 16.0,
        "mfe_p50": 35.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 27.000000000000004,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 20.0,
        "ci90": {
          "expR": -0.749,
          "ci90": [
            -0.938,
            -0.51
          ],
          "p_mean_le_0": 1.0,
          "n": 49
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 261,
      "wrTP1": 52.9,
      "nSL": 110,
      "nTO": 13,
      "expR": 0.059,
      "pf": 1.13,
      "mfe_p25": 20.75,
      "mfe_p50": 39.0,
      "mfe_p75": 92.25,
      "winnerMAE_p75": 28.75,
      "winnerMAE_p90": 57.0,
      "loserMFEbeforeSL_p50": 4.5,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -55.0,
      "revAfterSL_rate": 43.6,
      "ci90": {
        "expR": 0.059,
        "ci90": [
          -0.06,
          0.167
        ],
        "p_mean_le_0": 0.223,
        "n": 248
      }
    },
    "cuts": {
      "1.2": {
        "n": 96,
        "wrTP1": 22.9,
        "nSL": 67,
        "nTO": 7,
        "expR": -0.243,
        "pf": 0.68,
        "mfe_p25": 26.0,
        "mfe_p50": 58.0,
        "mfe_p75": 130.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 44.0,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -53.0,
        "revAfterSL_rate": 34.3,
        "ci90": {
          "expR": -0.243,
          "ci90": [
            -0.474,
            -0.004
          ],
          "p_mean_le_0": 0.953,
          "n": 89
        }
      },
      "1.3": {
        "n": 89,
        "wrTP1": 19.1,
        "nSL": 65,
        "nTO": 7,
        "expR": -0.331,
        "pf": 0.58,
        "mfe_p25": 25.0,
        "mfe_p50": 57.0,
        "mfe_p75": 126.75,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 46.0,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -53.0,
        "revAfterSL_rate": 33.8,
        "ci90": {
          "expR": -0.331,
          "ci90": [
            -0.56,
            -0.078
          ],
          "p_mean_le_0": 0.983,
          "n": 82
        }
      },
      "1.5": {
        "n": 77,
        "wrTP1": 18.2,
        "nSL": 57,
        "nTO": 6,
        "expR": -0.361,
        "pf": 0.55,
        "mfe_p25": 22.5,
        "mfe_p50": 56.0,
        "mfe_p75": 115.5,
        "winnerMAE_p75": 17.75,
        "winnerMAE_p90": 44.0,
        "loserMFEbeforeSL_p50": 12.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -53.0,
        "revAfterSL_rate": 29.8,
        "ci90": {
          "expR": -0.361,
          "ci90": [
            -0.611,
            -0.094
          ],
          "p_mean_le_0": 0.986,
          "n": 71
        }
      },
      "2.0": {
        "n": 55,
        "wrTP1": 14.5,
        "nSL": 43,
        "nTO": 4,
        "expR": -0.432,
        "pf": 0.49,
        "mfe_p25": 26.5,
        "mfe_p50": 61.0,
        "mfe_p75": 123.5,
        "winnerMAE_p75": 21.5,
        "winnerMAE_p90": 44.0,
        "loserMFEbeforeSL_p50": 20.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -55.0,
        "revAfterSL_rate": 25.6,
        "ci90": {
          "expR": -0.432,
          "ci90": [
            -0.721,
            -0.106
          ],
          "p_mean_le_0": 0.986,
          "n": 51
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
    "n": 3231,
    "wrTP1": 44.5,
    "expR": -0.022
  },
  "2026-W37": {
    "n": 5390,
    "wrTP1": 46.8,
    "expR": 0.072
  },
  "2026-W38": {
    "n": 4916,
    "wrTP1": 46.2,
    "expR": 0.086
  },
  "2026-W39": {
    "n": 5356,
    "wrTP1": 45.4,
    "expR": 0.058
  },
  "2026-W40": {
    "n": 5358,
    "wrTP1": 45.2,
    "expR": 0.018
  },
  "2026-W41": {
    "n": 5225,
    "wrTP1": 46.5,
    "expR": 0.056
  },
  "2026-W42": {
    "n": 5126,
    "wrTP1": 48.1,
    "expR": 0.049
  },
  "2026-W43": {
    "n": 4711,
    "wrTP1": 44.1,
    "expR": -0.0
  },
  "2026-W44": {
    "n": 637,
    "wrTP1": 50.7,
    "expR": 0.051
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 42,
      "wrTP1": 47.6,
      "expR": 0.276,
      "pf": 1.64
    },
    "1m/INV/SHORT": {
      "n": 19,
      "wrTP1": 68.4,
      "expR": 0.264,
      "pf": 1.95
    },
    "1m/RETEST/LONG": {
      "n": 1402,
      "wrTP1": 42.7,
      "expR": -0.017,
      "pf": 0.97
    },
    "1m/RETEST/SHORT": {
      "n": 471,
      "wrTP1": 43.1,
      "expR": -0.009,
      "pf": 0.98
    },
    "2m/INV/LONG": {
      "n": 18,
      "wrTP1": 38.9,
      "expR": -0.271,
      "pf": 0.56
    },
    "2m/INV/SHORT": {
      "n": 6,
      "wrTP1": 50.0,
      "expR": -0.267,
      "pf": 0.47
    },
    "2m/RETEST/LONG": {
      "n": 705,
      "wrTP1": 45.5,
      "expR": -0.071,
      "pf": 0.87
    },
    "2m/RETEST/SHORT": {
      "n": 217,
      "wrTP1": 41.0,
      "expR": -0.115,
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
      "n": 245,
      "wrTP1": 52.7,
      "expR": 0.083,
      "pf": 1.19
    },
    "5m/RETEST/SHORT": {
      "n": 96,
      "wrTP1": 47.9,
      "expR": -0.018,
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
      "wrTP1": 47.6,
      "expR": 0.037,
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
      "n": 221,
      "wrTP1": 51.6,
      "expR": 0.118,
      "pf": 1.26
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 59,
      "wrTP1": 40.7,
      "expR": -0.102,
      "pf": 0.81
    },
    "1m/INV/SHORT": {
      "n": 22,
      "wrTP1": 45.5,
      "expR": -0.098,
      "pf": 0.8
    },
    "1m/RETEST/LONG": {
      "n": 2038,
      "wrTP1": 48.2,
      "expR": 0.112,
      "pf": 1.25
    },
    "1m/RETEST/SHORT": {
      "n": 984,
      "wrTP1": 42.1,
      "expR": 0.094,
      "pf": 1.2
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
      "n": 907,
      "wrTP1": 46.9,
      "expR": 0.045,
      "pf": 1.1
    },
    "2m/RETEST/SHORT": {
      "n": 378,
      "wrTP1": 43.9,
      "expR": 0.007,
      "pf": 1.01
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
      "n": 323,
      "wrTP1": 50.8,
      "expR": 0.18,
      "pf": 1.45
    },
    "5m/RETEST/SHORT": {
      "n": 177,
      "wrTP1": 41.8,
      "expR": 0.093,
      "pf": 1.19
    }
  },
  "2026-W39": {
    "1m/INV/LONG": {
      "n": 37,
      "wrTP1": 48.6,
      "expR": 0.702,
      "pf": 3.36
    },
    "1m/INV/SHORT": {
      "n": 43,
      "wrTP1": 48.8,
      "expR": 0.047,
      "pf": 1.12
    },
    "1m/RETEST/LONG": {
      "n": 2035,
      "wrTP1": 44.5,
      "expR": 0.057,
      "pf": 1.12
    },
    "1m/RETEST/SHORT": {
      "n": 1361,
      "wrTP1": 44.5,
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
      "n": 17,
      "wrTP1": 52.9,
      "expR": 0.511,
      "pf": 3.38
    },
    "2m/RETEST/LONG": {
      "n": 783,
      "wrTP1": 45.7,
      "expR": 0.125,
      "pf": 1.26
    },
    "2m/RETEST/SHORT": {
      "n": 571,
      "wrTP1": 49.0,
      "expR": 0.036,
      "pf": 1.08
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
      "n": 271,
      "wrTP1": 45.0,
      "expR": 0.091,
      "pf": 1.19
    },
    "5m/RETEST/SHORT": {
      "n": 206,
      "wrTP1": 46.1,
      "expR": 0.069,
      "pf": 1.14
    }
  },
  "2026-W40": {
    "1m/INV/LONG": {
      "n": 45,
      "wrTP1": 53.3,
      "expR": 0.285,
      "pf": 1.74
    },
    "1m/INV/SHORT": {
      "n": 49,
      "wrTP1": 38.8,
      "expR": -0.08,
      "pf": 0.84
    },
    "1m/RETEST/LONG": {
      "n": 1811,
      "wrTP1": 42.6,
      "expR": -0.031,
      "pf": 0.94
    },
    "1m/RETEST/SHORT": {
      "n": 1399,
      "wrTP1": 45.9,
      "expR": 0.027,
      "pf": 1.06
    },
    "2m/INV/LONG": {
      "n": 13,
      "wrTP1": 69.2,
      "expR": 0.156,
      "pf": 1.51
    },
    "2m/INV/SHORT": {
      "n": 20,
      "wrTP1": 55.0,
      "expR": -0.07,
      "pf": 0.81
    },
    "2m/RETEST/LONG": {
      "n": 855,
      "wrTP1": 46.3,
      "expR": -0.001,
      "pf": 1.0
    },
    "2m/RETEST/SHORT": {
      "n": 631,
      "wrTP1": 45.6,
      "expR": 0.113,
      "pf": 1.23
    },
    "5m/INV/LONG": {
      "n": 5,
      "wrTP1": 100.0,
      "expR": 0.374,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 3,
      "wrTP1": 33.3,
      "expR": -0.36,
      "pf": 0.28
    },
    "5m/RETEST/LONG": {
      "n": 294,
      "wrTP1": 53.4,
      "expR": 0.1,
      "pf": 1.22
    },
    "5m/RETEST/SHORT": {
      "n": 233,
      "wrTP1": 43.3,
      "expR": 0.022,
      "pf": 1.04
    }
  },
  "2026-W41": {
    "1m/INV/LONG": {
      "n": 55,
      "wrTP1": 47.3,
      "expR": 0.035,
      "pf": 1.08
    },
    "1m/INV/SHORT": {
      "n": 39,
      "wrTP1": 41.0,
      "expR": 0.165,
      "pf": 1.39
    },
    "1m/RETEST/LONG": {
      "n": 2054,
      "wrTP1": 45.7,
      "expR": 0.02,
      "pf": 1.04
    },
    "1m/RETEST/SHORT": {
      "n": 1081,
      "wrTP1": 41.4,
      "expR": 0.047,
      "pf": 1.09
    },
    "2m/INV/LONG": {
      "n": 27,
      "wrTP1": 44.4,
      "expR": -0.181,
      "pf": 0.65
    },
    "2m/INV/SHORT": {
      "n": 9,
      "wrTP1": 33.3,
      "expR": 0.377,
      "pf": 1.68
    },
    "2m/RETEST/LONG": {
      "n": 944,
      "wrTP1": 52.2,
      "expR": 0.107,
      "pf": 1.25
    },
    "2m/RETEST/SHORT": {
      "n": 481,
      "wrTP1": 45.1,
      "expR": 0.06,
      "pf": 1.12
    },
    "5m/INV/LONG": {
      "n": 8,
      "wrTP1": 50.0,
      "expR": -0.167,
      "pf": 0.61
    },
    "5m/INV/SHORT": {
      "n": 3,
      "wrTP1": 33.3,
      "expR": -0.513,
      "pf": 0.23
    },
    "5m/RETEST/LONG": {
      "n": 352,
      "wrTP1": 53.4,
      "expR": 0.16,
      "pf": 1.37
    },
    "5m/RETEST/SHORT": {
      "n": 172,
      "wrTP1": 50.6,
      "expR": 0.075,
      "pf": 1.17
    }
  },
  "2026-W42": {
    "1m/INV/LONG": {
      "n": 76,
      "wrTP1": 34.2,
      "expR": -0.201,
      "pf": 0.64
    },
    "1m/INV/SHORT": {
      "n": 24,
      "wrTP1": 58.3,
      "expR": 0.133,
      "pf": 1.39
    },
    "1m/RETEST/LONG": {
      "n": 2224,
      "wrTP1": 46.5,
      "expR": 0.047,
      "pf": 1.1
    },
    "1m/RETEST/SHORT": {
      "n": 1009,
      "wrTP1": 48.8,
      "expR": 0.045,
      "pf": 1.1
    },
    "2m/INV/LONG": {
      "n": 23,
      "wrTP1": 52.2,
      "expR": 0.25,
      "pf": 1.64
    },
    "2m/INV/SHORT": {
      "n": 6,
      "wrTP1": 83.3,
      "expR": 0.845,
      "pf": 99.0
    },
    "2m/RETEST/LONG": {
      "n": 857,
      "wrTP1": 49.6,
      "expR": 0.084,
      "pf": 1.18
    },
    "2m/RETEST/SHORT": {
      "n": 401,
      "wrTP1": 47.9,
      "expR": -0.053,
      "pf": 0.89
    },
    "5m/INV/LONG": {
      "n": 3,
      "wrTP1": 66.7,
      "expR": 0.017,
      "pf": 1.05
    },
    "5m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 321,
      "wrTP1": 53.3,
      "expR": 0.086,
      "pf": 1.19
    },
    "5m/RETEST/SHORT": {
      "n": 181,
      "wrTP1": 50.8,
      "expR": 0.124,
      "pf": 1.27
    }
  },
  "2026-W43": {
    "1m/INV/LONG": {
      "n": 48,
      "wrTP1": 60.4,
      "expR": 0.321,
      "pf": 1.91
    },
    "1m/INV/SHORT": {
      "n": 25,
      "wrTP1": 56.0,
      "expR": 0.29,
      "pf": 1.9
    },
    "1m/RETEST/LONG": {
      "n": 1595,
      "wrTP1": 40.8,
      "expR": -0.029,
      "pf": 0.95
    },
    "1m/RETEST/SHORT": {
      "n": 1205,
      "wrTP1": 43.5,
      "expR": -0.001,
      "pf": 1.0
    },
    "2m/INV/LONG": {
      "n": 15,
      "wrTP1": 53.3,
      "expR": 0.035,
      "pf": 1.08
    },
    "2m/INV/SHORT": {
      "n": 8,
      "wrTP1": 50.0,
      "expR": -0.217,
      "pf": 0.56
    },
    "2m/RETEST/LONG": {
      "n": 741,
      "wrTP1": 43.7,
      "expR": 0.01,
      "pf": 1.02
    },
    "2m/RETEST/SHORT": {
      "n": 545,
      "wrTP1": 51.0,
      "expR": 0.07,
      "pf": 1.15
    },
    "5m/INV/LONG": {
      "n": 2,
      "wrTP1": 50.0,
      "expR": -0.395,
      "pf": 0.21
    },
    "5m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 0.318,
      "pf": 2.27
    },
    "5m/RETEST/LONG": {
      "n": 289,
      "wrTP1": 46.4,
      "expR": -0.075,
      "pf": 0.85
    },
    "5m/RETEST/SHORT": {
      "n": 234,
      "wrTP1": 45.7,
      "expR": -0.001,
      "pf": 1.0
    }
  },
  "2026-W44": {
    "15m/RETEST/SHORT": {
      "n": 6,
      "wrTP1": 100.0,
      "expR": 1.377,
      "pf": 99.0
    },
    "1m/INV/LONG": {
      "n": 4,
      "wrTP1": 100.0,
      "expR": 1.165,
      "pf": 99.0
    },
    "1m/INV/SHORT": {
      "n": 3,
      "wrTP1": 33.3,
      "expR": -0.383,
      "pf": 0.42
    },
    "1m/RETEST/LONG": {
      "n": 157,
      "wrTP1": 47.1,
      "expR": 0.131,
      "pf": 1.25
    },
    "1m/RETEST/SHORT": {
      "n": 201,
      "wrTP1": 50.7,
      "expR": 0.027,
      "pf": 1.06
    },
    "2m/INV/SHORT": {
      "n": 3,
      "wrTP1": 66.7,
      "expR": 0.197,
      "pf": 1.59
    },
    "2m/RETEST/LONG": {
      "n": 67,
      "wrTP1": 46.3,
      "expR": -0.112,
      "pf": 0.78
    },
    "2m/RETEST/SHORT": {
      "n": 119,
      "wrTP1": 44.5,
      "expR": -0.092,
      "pf": 0.83
    },
    "5m/RETEST/LONG": {
      "n": 30,
      "wrTP1": 63.3,
      "expR": 0.063,
      "pf": 1.17
    },
    "5m/RETEST/SHORT": {
      "n": 47,
      "wrTP1": 66.0,
      "expR": 0.227,
      "pf": 1.67
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 37020,
  "brier": 0.2203,
  "bias": -0.117,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.339
    },
    {
      "feature": "nearTk",
      "weight": -0.089
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.065
    },
    {
      "feature": "stretchAtr",
      "weight": -0.052
    },
    {
      "feature": "aligned",
      "weight": -0.032
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.027
    },
    {
      "feature": "biasScore",
      "weight": -0.027
    },
    {
      "feature": "rvol",
      "weight": 0.021
    },
    {
      "feature": "chopIdx",
      "weight": -0.02
    },
    {
      "feature": "hourNY",
      "weight": 0.018
    },
    {
      "feature": "emaStack",
      "weight": 0.01
    },
    {
      "feature": "structDir",
      "weight": -0.001
    },
    {
      "feature": "nearEdge",
      "weight": -0.001
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.165,
      "actual": 0.16,
      "n": 3702
    },
    {
      "bin": 1,
      "pred": 0.368,
      "actual": 0.299,
      "n": 3702
    },
    {
      "bin": 2,
      "pred": 0.446,
      "actual": 0.33,
      "n": 3702
    },
    {
      "bin": 3,
      "pred": 0.491,
      "actual": 0.4,
      "n": 3702
    },
    {
      "bin": 4,
      "pred": 0.528,
      "actual": 0.501,
      "n": 3702
    },
    {
      "bin": 5,
      "pred": 0.556,
      "actual": 0.568,
      "n": 3702
    },
    {
      "bin": 6,
      "pred": 0.578,
      "actual": 0.614,
      "n": 3702
    },
    {
      "bin": 7,
      "pred": 0.597,
      "actual": 0.652,
      "n": 3702
    },
    {
      "bin": 8,
      "pred": 0.615,
      "actual": 0.684,
      "n": 3702
    },
    {
      "bin": 9,
      "pred": 0.642,
      "actual": 0.761,
      "n": 3702
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 34602,
  "testN": 5348,
  "testWeeks": [
    "2026-W43",
    "2026-W44"
  ],
  "model_oos_brier": 0.2189,
  "model_oos_n": 5348,
  "best_scheme_in_sample": {
    "scheme": "fixed_2R",
    "trainExpR": 0.049
  },
  "best_scheme_oos_expR": 0.028
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.132,
    "ci90": [
      0.021,
      0.25
    ],
    "p_mean_le_0": 0.025,
    "n": 389,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": 0.078,
    "ci90": [
      -0.034,
      0.196
    ],
    "p_mean_le_0": 0.128,
    "n": 264,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.03,
    "ci90": [
      0.013,
      0.047
    ],
    "p_mean_le_0": 0.003,
    "n": 14505,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.031,
    "ci90": [
      0.01,
      0.051
    ],
    "p_mean_le_0": 0.007,
    "n": 8967,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.026,
    "ci90": [
      -0.126,
      0.183
    ],
    "p_mean_le_0": 0.39,
    "n": 141,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.118,
    "ci90": [
      -0.086,
      0.344
    ],
    "p_mean_le_0": 0.183,
    "n": 100,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.044,
    "ci90": [
      0.019,
      0.071
    ],
    "p_mean_le_0": 0.002,
    "n": 6350,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.054,
    "ci90": [
      0.022,
      0.087
    ],
    "p_mean_le_0": 0.004,
    "n": 3947,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.239,
    "ci90": [
      0.012,
      0.467
    ],
    "p_mean_le_0": 0.044,
    "n": 36,
    "survives_fdr10": true
  },
  "5m/INV/SHORT": {
    "expR": 0.11,
    "ci90": [
      -0.262,
      0.496
    ],
    "p_mean_le_0": 0.325,
    "n": 21,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.104,
    "ci90": [
      0.065,
      0.147
    ],
    "p_mean_le_0": 0.0,
    "n": 2260,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.069,
    "ci90": [
      0.013,
      0.125
    ],
    "p_mean_le_0": 0.021,
    "n": 1459,
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
      "n": 5113,
      "wrTP1": 45.2,
      "expR": 0.053,
      "pf": 1.11,
      "defining_features": {
        "stretchAtr": 1.7,
        "chopIdx": -1.33,
        "rvol": 1.32,
        "biasScore": 0.21
      }
    },
    {
      "id": 3,
      "n": 17187,
      "wrTP1": 46.4,
      "expR": 0.046,
      "pf": 1.09,
      "defining_features": {
        "biasScore": 0.76,
        "emaStack": 0.72,
        "nearEdge": 0.6,
        "structDir": 0.35
      }
    },
    {
      "id": 2,
      "n": 12450,
      "wrTP1": 45.8,
      "expR": 0.039,
      "pf": 1.08,
      "defining_features": {
        "biasScore": -1.16,
        "emaStack": -1.04,
        "nearEdge": -0.91,
        "structDir": -0.49
      }
    },
    {
      "id": 1,
      "n": 5200,
      "wrTP1": 46.1,
      "expR": 0.032,
      "pf": 1.07,
      "defining_features": {
        "atrPctUsed": 1.68,
        "nearTk": 0.58,
        "stretchAtr": -0.32,
        "chopIdx": 0.31
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
        "n": 78,
        "wrTP1": 52.6,
        "expR": 0.366
      },
      "YM": {
        "n": 172,
        "wrTP1": 44.8,
        "expR": 0.159
      },
      "ES": {
        "n": 55,
        "wrTP1": 40.0,
        "expR": -0.097
      },
      "GC": {
        "n": 61,
        "wrTP1": 41.0,
        "expR": -0.141
      },
      "NQ": {
        "n": 37,
        "wrTP1": 59.5,
        "expR": 0.286
      }
    },
    "expR_spread": 0.507,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "GC": {
        "n": 58,
        "wrTP1": 67.2,
        "expR": 0.303
      },
      "YM": {
        "n": 134,
        "wrTP1": 39.6,
        "expR": 0.036
      },
      "NQ": {
        "n": 32,
        "wrTP1": 56.2,
        "expR": 0.08
      },
      "ES": {
        "n": 20,
        "wrTP1": 50.0,
        "expR": 0.247
      },
      "CL": {
        "n": 37,
        "wrTP1": 32.4,
        "expR": -0.271
      }
    },
    "expR_spread": 0.574,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 2394,
        "wrTP1": 43.3,
        "expR": -0.008
      },
      "NQ": {
        "n": 2646,
        "wrTP1": 44.9,
        "expR": 0.015
      },
      "ES": {
        "n": 3414,
        "wrTP1": 44.8,
        "expR": 0.009
      },
      "CL": {
        "n": 3182,
        "wrTP1": 44.4,
        "expR": 0.028
      },
      "YM": {
        "n": 3288,
        "wrTP1": 46.0,
        "expR": 0.095
      }
    },
    "expR_spread": 0.103,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 1374,
        "wrTP1": 41.7,
        "expR": 0.045
      },
      "GC": {
        "n": 2773,
        "wrTP1": 46.1,
        "expR": 0.051
      },
      "YM": {
        "n": 2229,
        "wrTP1": 44.1,
        "expR": 0.031
      },
      "ES": {
        "n": 1709,
        "wrTP1": 46.7,
        "expR": 0.044
      },
      "CL": {
        "n": 1344,
        "wrTP1": 42.4,
        "expR": -0.045
      }
    },
    "expR_spread": 0.096,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 21,
        "wrTP1": 47.6,
        "expR": -0.243
      },
      "CL": {
        "n": 20,
        "wrTP1": 60.0,
        "expR": 0.046
      },
      "YM": {
        "n": 56,
        "wrTP1": 41.1,
        "expR": -0.033
      },
      "ES": {
        "n": 26,
        "wrTP1": 65.4,
        "expR": 0.005
      },
      "NQ": {
        "n": 23,
        "wrTP1": 52.2,
        "expR": 0.454
      }
    },
    "expR_spread": 0.697,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 46,
        "wrTP1": 52.2,
        "expR": 0.405
      },
      "NQ": {
        "n": 16,
        "wrTP1": 43.8,
        "expR": -0.006
      },
      "ES": {
        "n": 14,
        "wrTP1": 35.7,
        "expR": 0.051
      },
      "CL": {
        "n": 12,
        "wrTP1": 50.0,
        "expR": -0.148
      },
      "GC": {
        "n": 16,
        "wrTP1": 37.5,
        "expR": -0.311
      }
    },
    "expR_spread": 0.716,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 1257,
        "wrTP1": 46.7,
        "expR": 0.055
      },
      "GC": {
        "n": 1035,
        "wrTP1": 45.4,
        "expR": 0.005
      },
      "CL": {
        "n": 1420,
        "wrTP1": 48.0,
        "expR": 0.051
      },
      "ES": {
        "n": 1413,
        "wrTP1": 47.3,
        "expR": 0.008
      },
      "YM": {
        "n": 1428,
        "wrTP1": 48.7,
        "expR": 0.09
      }
    },
    "expR_spread": 0.085,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 754,
        "wrTP1": 48.0,
        "expR": 0.019
      },
      "YM": {
        "n": 969,
        "wrTP1": 48.9,
        "expR": 0.11
      },
      "GC": {
        "n": 1157,
        "wrTP1": 49.4,
        "expR": 0.098
      },
      "NQ": {
        "n": 679,
        "wrTP1": 43.9,
        "expR": 0.017
      },
      "CL": {
        "n": 546,
        "wrTP1": 45.4,
        "expR": -0.038
      }
    },
    "expR_spread": 0.148,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 10,
        "wrTP1": 50.0,
        "expR": -0.065
      },
      "YM": {
        "n": 12,
        "wrTP1": 83.3,
        "expR": 0.247
      },
      "ES": {
        "n": 8,
        "wrTP1": 75.0,
        "expR": 0.209
      },
      "CL": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.748
      },
      "GC": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.063
      }
    },
    "expR_spread": 0.813,
    "verdict": "instrument-specific"
  },
  "5m/INV/SHORT": {
    "symbols": {
      "NQ": {
        "n": 7,
        "wrTP1": 71.4,
        "expR": 0.346
      },
      "YM": {
        "n": 5,
        "wrTP1": 20.0,
        "expR": -0.708
      },
      "ES": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": 0.16
      },
      "GC": {
        "n": 4,
        "wrTP1": 75.0,
        "expR": 0.77
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.245
      }
    },
    "expR_spread": 1.478,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 334,
        "wrTP1": 51.5,
        "expR": 0.106
      },
      "ES": {
        "n": 487,
        "wrTP1": 50.7,
        "expR": 0.082
      },
      "YM": {
        "n": 501,
        "wrTP1": 49.9,
        "expR": 0.108
      },
      "CL": {
        "n": 489,
        "wrTP1": 54.0,
        "expR": 0.164
      },
      "NQ": {
        "n": 541,
        "wrTP1": 49.0,
        "expR": 0.056
      },
      "BTCUSDT": {
        "n": 12,
        "wrTP1": 75.0,
        "expR": 0.383
      },
      "ETHUSDT": {
        "n": 6,
        "wrTP1": 100.0,
        "expR": 0.377
      }
    },
    "expR_spread": 0.327,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 245,
        "wrTP1": 47.8,
        "expR": 0.069
      },
      "ES": {
        "n": 330,
        "wrTP1": 50.6,
        "expR": 0.137
      },
      "GC": {
        "n": 422,
        "wrTP1": 46.4,
        "expR": 0.005
      },
      "YM": {
        "n": 326,
        "wrTP1": 47.5,
        "expR": 0.121
      },
      "CL": {
        "n": 233,
        "wrTP1": 45.5,
        "expR": 0.024
      },
      "ETHUSDT": {
        "n": 6,
        "wrTP1": 83.3,
        "expR": 0.402
      },
      "BTCUSDT": {
        "n": 5,
        "wrTP1": 20.0,
        "expR": -0.676
      }
    },
    "expR_spread": 1.078,
    "verdict": "instrument-specific"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 25,
  "near_news_30m": {
    "n": 63,
    "wrTP1": 52.4,
    "nSL": 23,
    "nTO": 7,
    "expR": 0.358,
    "pf": 1.89,
    "mfe_p25": 16.25,
    "mfe_p50": 32.5,
    "mfe_p75": 119.25,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 55.000000000000014,
    "loserMFEbeforeSL_p50": 6.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -21.0,
    "revAfterSL_rate": 34.8
  },
  "away_from_news": {
    "n": 39887,
    "wrTP1": 46.0,
    "nSL": 18610,
    "nTO": 2923,
    "expR": 0.042,
    "pf": 1.09,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 32.1
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 6,
  "mae_deltaER": 0.26,
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
    "hypothesis": "En RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. HASTA 2026-09-04 esto solo certificaba en SHORT (\"no aplica a largos\"); con la muestra de 2026-09-05 TAMBIEN certifica en 1m LONG, asi que se retira la exclusion dura de BUY RETEST y se deja como 'certifica por tf/side, no generalizar sin mirar la tabla'. 2026-09-06: mismas cifras exactas que 2026-09-05 (n identico) porque no llego dato nuevo. 2026-09-07 (lunes, primer dia con trades GENUINAMENTE nuevos post-restauracion, sin repeticion del bug de heal): retest_1m_long paso de n=1087 a n=1135 (+48 pares nuevos, no restaurados) y el delta se mantiene practicamente igual (0.181->0.183) con el CI90 todavia sin cruzar cero -- esta es la primera confirmacion independiente real que pedia el next_steps anterior. retest_1m_short tambien crecio con dato nuevo (n=219->229) y sigue certificando. 2026-09-08 (martes, primer dia habil COMPLETO post-feriado, salto grande de muestra real): retest_1m_long n=1135->1432 (delta 0.183->0.18, estable, segunda confirmacion independiente); retest_1m_short n=229->514 (delta 0.283->0.417, se hizo MAS fuerte); retest_2m_short CERTIFICA POR PRIMERA VEZ (n=129->260, CI90 dejo de cruzar cero); retest_5m_long CERTIFICA POR PRIMERA VEZ pero al filo (n=224->274, CI90=[0.005,0.36], limite inferior casi cero, vigilar que no se revierta con mas muestra); retest_2m_long sigue sin certificar y el delta bajo a casi cero (0.028->0.01, n=596->742). 2026-10-20: hito nuevo -- `since_change` certifica limpio ahora en los 6 de 6 segmentos RETEST del bus (el que faltaba, 5m SHORT, cruzo hoy su CI90 a positivo: [-0.005,0.299] -> [0.004,0.286], n=541->586, limite inferior apenas sobre cero pero real). Documentado en detalle en playbook/buy-retest.md y playbook/sell-retest.md (seccion Gestion). El verdict agregado formal de este experimento sigue en 'flat' por la limitacion de metrica ya conocida (mide con rMultiple, no con rOrig) -- no es evidencia de que el cambio no funcione, es la evidencia real viviendo fuera de ese campo. A evaluar en la revision semanal del domingo (2026-week-43): si corresponde subir la confianza documentada de 'aplicado, parcial' a 'aplicado, 6/6 certifican' y si shadow_rules deberia empezar a razonar sobre rOrig en el segmento del gate (5m LONG). No se decide hoy.",
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
      "2026-09-30 (miercoles, cuarto dia real de trading bajo el SL nuevo): el verdict mecanico agregado SIGUE en 'confirmed' (dispara la alerta EXPERIMENTO CONFIRMADO en report.md de hoy otra vez) y SIGUE sin tomarse al pie de la letra -- el desglose por segmento de prediction_scoreboard, con n ya bastante mas grande en los 6 (1m LONG n=437, 1m SHORT n=800, 2m LONG n=194, 2m SHORT n=318, 5m LONG n=76, 5m SHORT n=114 -- los 6 superan ya el afterN>=40 de agent-instructions.md), mantiene EXACTAMENTE el mismo patron de direccion que ayer, ahora con mucha mas muestra detras: 1m SHORT realDeltaER=+0.142 (vs +0.143 predicho, acierta casi exacto) y 2m SHORT realDeltaER=+0.167 (vs +0.151 predicho, acierta) siguen siendo los UNICOS 2 segmentos que confirman; 1m LONG realDeltaER=-0.028, 2m LONG realDeltaER=-0.097, 5m LONG realDeltaER=-0.151 y 5m SHORT realDeltaER=-0.086 siguen en direccion CONTRARIA a lo predicho (hit_direction_rate=33.3%, mae_deltaER=0.251). Nota importante: la hipotesis de ayer ('SHORT ayuda, LONG perjudica') ya NO describe el patron con precision -- 5m SHORT tambien se dio vuelta a negativo hoy con n=114 (ya no es 'n todavia chico', son 4 dias seguidos de dato real). El patron mas preciso hoy es: SOLO 1m y 2m SHORT confirman; las 3 ramas LONG (1m/2m/5m) Y 5m SHORT no confirman. Es el CUARTO dia consecutivo (09-28, 09-29, 09-30, y contando) con la misma division 2-vs-4, cada vez con mas muestra, sin ninguna reversion hacia el lado predicho en los 4 segmentos que fallan. Todavia no se cumple el criterio propio del experimento de '2 semanas consecutivas en la misma direccion' antes de tratarlo como resultado real, pero con afterN ya por encima de 40 en los 6 segmentos y 3-4 dias seguidos sin cambio de signo, el balance de evidencia se esta inclinando hacia un revert parcial. RECOMENDACION EXPLICITA para la revision semanal del domingo 2026-10-04 (no antes, hace falta ver si el patron se mantiene el resto de la semana): si 1m LONG, 2m LONG, 5m LONG y 5m SHORT siguen en direccion negativa el domingo, proponer formalmente revertir sl_basis_retest a '3-capas' en esos 4 segmentos (mantener la mecha del retest solo en 1m y 2m SHORT, que son los que realmente mejoraron). Correlacion en paralelo (no causal, anotar solo): el mismo segmento 2m/RETEST/LONG perdio hoy su significancia en segment_significance (survives_fdr10 paso de true a false, CI90=[-0.008,0.069] cruza cero por primera vez en semanas, ver report.alerts de hoy) -- dos senales independientes (el experimento de SL y la significancia cruda del segmento) apuntando en la misma direccion de deterioro para 2m LONG en la misma corrida.",
      "2026-10-02 (viernes, sexto dia habil real bajo el SL nuevo desde el sabado 09-26): afterN agregado ya grande en los 6 segmentos (1m LONG=1310, 1m SHORT=1323, 2m LONG=581, 2m SHORT=593, 5m LONG=201, 5m SHORT=203). Los 3 segmentos LONG SIGUEN en direccion CONTRARIA a lo predicho y sin mejorar vs ayer: 1m realDeltaER=-0.091 (predicho +0.152), 2m realDeltaER=-0.092 (predicho +0.154), 5m realDeltaER=-0.072 (predicho +0.255). NOVEDAD: el lado SHORT, que venia confirmando con claridad, se debilita en los 3 TF -- 1m SHORT casi plano (realDeltaER=+0.003 vs +0.143 predicho, ayer era +0.081), 2m SHORT sigue positivo pero mas debil (+0.038 vs +0.151 predicho, ayer +0.061), 5m SHORT empeora (-0.139 vs +0.567 predicho, ayer -0.072). hit_direction_rate se mantiene en 33.3% (2/6) pero mae_deltaER sube a 0.296, la peor lectura del scoreboard hasta la fecha. decay_weekly_by_segment de W40 (casi cerrada) muestra ruido adicional en 5m: 5m LONG se da vuelta a POSITIVO esta semana (n=196 E[R]=+0.068, rompe 2 semanas negativas) mientras 5m SHORT se da vuelta a NEGATIVO (n=201 E[R]=-0.033, rompe su racha positiva) -- consistente con que 5m (menor n) es el TF mas ruidoso de los 6, no un cambio de regimen. 1m y 2m LONG, los de mayor muestra y mas consistentes dia a dia, siguen negativos sin ninguna reversion desde el cambio. DECISION: siguen siendo 6 dias habiles de calendario desde el cambio (09-28 a 10-02), todavia no las '2 semanas consecutivas' del propio criterio del experimento -- se mantiene NO revertir hoy. Para la revision semanal del domingo 2026-10-04: si 1m y 2m LONG siguen negativos (son los que importan, con mas muestra y sin ruido de 5m), proponer formalmente revertir sl_basis_retest a 3-capas en RETEST LONG (1m/2m al menos; 5m LONG revirtio hoy a positivo, tratar con mas cautela y mas muestra antes de meterlo en el mismo paquete). El lado SHORT ya no es un bloque limpio de 'mejora en los 3 TF' -- sostener 1m/2m SHORT con el SL nuevo pero vigilar 1m SHORT (casi plano) y 5m SHORT (ya negativo) de cerca, no asumir que todo SHORT se mantiene con la misma fuerza que hace una semana.",
      "2026-10-03 (sabado, septimo dia de calendario desde el cambio, pero el hallazgo de hoy es metodologico, no de muestra nueva): se revisa la cadena de razonamiento de los ultimos 6 dias (09-28 a 10-02) que usaba prediction_scoreboard/eval_experiments para decir 'LONG se esta revirtiendo, preparar revert parcial el domingo'. Esa lectura compara expR de rMultiple ANTES vs DESPUES de changeDate -- pero appliedNote ya decia que 'el feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig'. Si rMultiple se calcula IGUAL antes y despues del cambio (siempre 3 capas, sin importar que input este activo en el Pine), un before/after sobre rMultiple NO puede medir el efecto de mover el SL -- solo mide como vino el mercado en el periodo 'after' (28 sep - 2 oct, que coincide con la semana W40 de bajo E[R] global, ver decay_weekly W40=0.013, casi identico al 'after' agregado de este experimento =0.014). Es una confusion clasica de regimen de mercado disfrazada de efecto del experimento. SE AGREGO HOY a analyze.py un campo nuevo sl_origin_vs_layer.since_change: el mismo emparejado (rOrig vs rMultiple, simultaneos, sin mezclar con calendario) que ya certifica el experimento en agregado, pero restringido a recvDate>=2026-09-26 (n=4734 en total RETEST). Resultado con la metrica correcta: NINGUN segmento sale negativo (delta_below_zero=false en los 6). 1m LONG delta=+0.001 CI90=[-0.071,0.078] (plano, no niega el experimento); 1m SHORT delta=+0.055 CI90=[-0.025,0.137] (plano, no confirma todavia); 2m LONG delta=+0.193 CI90=[0.075,0.322] -- CONFIRMA POSITIVO incluso solo con dato post-cambio (n=780); 2m SHORT delta=+0.025 CI90 cruza cero (plano); 5m LONG delta=+0.063 CI90 cruza cero (plano, n=278); 5m SHORT delta=+0.075 CI90 cruza cero (plano, n=208). El patron real es: el efecto se ENCOGIO frente a la estimacion in-sample completa (esperable, optimismo de haber minado 6 segmentos durante semanas) pero NO SE INVIRTIO en ninguno. CORRECCION DE RUMBO: se retira la recomendacion de las corridas 09-29 a 10-02 de formalizar un revert parcial de sl_basis_retest a LONG en la revision semanal de manana domingo 2026-10-04. Recomendacion para manana: NO revertir nada; documentar en la revision semanal que prediction_scoreboard no es la metrica valida para ESTE experimento en particular (si lo es para experimentos que cambien directamente el input que alimenta rMultiple) y que sl_origin_vs_layer.since_change es la referencia a vigilar de aqui en adelante. Seguir mirando since_change semana a semana; si algun segmento desarrolla delta_below_zero=true con n>=40 ahi si habria caso real para revertir ese segmento especifico.",
      "2026-10-04 (domingo, REVISION SEMANAL, octavo dia de calendario desde el cambio, sin dato jsonl nuevo del cron pero con el cierre formal de la semana 2026-W40): since_change (n=4734 total RETEST) con el cierre de W40 confirma la correccion de ayer con un dia mas de perspectiva. De los 6 segmentos con n>=100 post-cambio, SOLO 2m/RETEST/LONG sigue confirmando limpio (n=780, delta=+0.193 CI90=[0.075,0.322], no cruza cero); los otros 5 (1m LONG n=1545, 1m SHORT n=1236, 2m SHORT n=559, 5m LONG n=278, 5m SHORT n=208) quedan planos -- CI90 cruza cero en los dos sentidos, NINGUNO con delta_below_zero=true. Nueva alerta permanente agregada a analyze.py hoy (material_alerts): compara automaticamente cuantos segmentos con n>=100 confirman en since_change vs el total, para no depender de que el agente lo note a mano cada vez. Lectura honesta para la revision semanal (ver reviews/2026-week-40.md): el 'cambio del mes' del 2026-09-26 se declaro con 6/6 segmentos certificando en agregado historico (mezcla pre+post cambio) y una racha de ~18 lecturas sin reversion -- pero la UNICA medicion que aisla el efecto real (pareada, solo post-cambio) hoy solo sostiene esa fuerza en 1 de 6 segmentos; el resto simplemente no tiene evidencia suficiente todavia para confirmar NI para revertir. prediction_scoreboard (hit_direction_rate=33.3%, peor que un volado) mide lo mismo que ya se identifico como confundido con el regimen de mercado (rMultiple no cambia con el input del Pine) -- no usar ese numero para juzgar este experimento especifico, pero SI como leccion de metodo: la proxima vez que 6/6 segmentos certifiquen en agregado historico sin haber visto una sola lectura post-cambio real, declarar el 'cambio del mes' con mas cautela (marcar explicitamente 'pendiente de since_change' en vez de 'evidencia madura'). DECISION: no revertir nada. Mantener aplicado en los 6 segmentos, seguir acumulando since_change semana a semana; solo revertir un segmento especifico si desarrolla delta_below_zero=true con n>=40.",
      "2026-10-06 (martes, incidente de repo del dia -- ver buy-retest.md -- sin perdida de dato): eval_experiments() en report.json pone por primera vez verdict=\"flat\" para este experimento en su evaluacion agregada formal antes/despues (beforeN=16583 expR=0.061 vs afterN=6438 expR=0.013) -- confirma con muestra ya grande lo que la alerta de ayer avisaba (\"el efecto se encoge\"). NO es \"rejected\" (expR post-cambio sigue positivo, no negativo), asi que sigue sin caso para revertir, pero ya no corresponde describirlo como \"cambio ganador\" en el agregado. since_change por segmento (n=5895 total RETEST, recvDate>=2026-09-26) con un dia mas de perspectiva: SOLO 2m/RETEST/LONG sigue confirmando limpio (n=954, delta=+0.145 CI90=[0.039,0.258]); los otros 5 (1m LONG n=1900 delta=-0.015, 1m SHORT n=1557 delta=+0.04, 2m SHORT n=713 delta=+0.028, 5m LONG n=342 delta=+0.04, 5m SHORT n=273 delta=+0.059) siguen planos, ninguno delta_below_zero=true. Dato adicional que contextualiza el verdict=\"flat\": en 1m/RETEST/LONG, TANTO layer_expR (-0.05) COMO orig_expR (-0.065) son negativos desde el cambio -- el deterioro de ese segmento (ver decay_weekly_by_segment, 3 semanas cayendo, W41 ya en -0.108) no depende de que SL se use, es de regimen/muestra, no del experimento en si. DECISION: sin cambio -- mantener aplicado en los 6 segmentos, no revertir nada; bajar la confianza declarada del \"cambio del mes\" de 2026-09-26 a \"neutro en agregado, con una excepcion que si gana (2m LONG)\". Vigilar si algun segmento desarrolla delta_below_zero=true con n>=40, que seria el primer caso real para revertir.",
      "2026-10-07 (miercoles): since_change (recvDate>=2026-09-26) sigue el mismo patron que ayer sin cambio de fondo -- de los 6 segmentos RETEST con n>=100, SOLO 2m/RETEST/LONG sigue confirmando limpio (delta_beats_zero=true). verdict agregado formal sigue en 'flat' (sin recalculo nuevo hoy en report.json mas alla del crecimiento de n). Sin reversion en ningun segmento (delta_below_zero=false en todos). DECISION sin cambio: mantener aplicado en los 6 segmentos, no revertir nada.",
      "2026-10-08 (jueves): since_change (recvDate>=2026-09-26, muestra mas grande hoy, n=7610 total RETEST+INV) AMPLIA la confirmacion limpia de 1 a 4 de los 6 segmentos RETEST: 2m/RETEST/LONG sigue confirmando (delta=+0.105 CI90=[0.025,0.198]); 5m/RETEST/LONG CERTIFICA POR PRIMERA VEZ (n=485, delta=+0.245 CI90=[0.022,0.523], antes plano con CI90=[-0.059,0.137]); 1m/RETEST/SHORT CERTIFICA POR PRIMERA VEZ (n=1904, delta=+0.084 CI90=[0.008,0.158], antes plano). 1m/RETEST/LONG sigue plano (n=2542, delta=+0.015 CI90=[-0.048,0.073]) y 2m/5m SHORT siguen planos sin cambio de fondo. Ningun segmento sale delta_below_zero=true. Sube la confianza del cambio aplicado el 09-26 aunque el verdict agregado formal (que mezcla los 6 segmentos y toda la ventana before/after sin distinguir) siga en 'flat' -- la lectura por segmento es mas informativa que el agregado aqui. Se corrio ademas sl_origin_vs_layer.since_change por primera vez con muestra real para kind=INV (fuera del alcance de este experimento, que es RETEST-only): mixto y negativo con significancia en 2 de 3 TF de INV/LONG y en 1m INV/SHORT -- confirma que la exclusion original de kind=INV en este experimento fue correcta, no evaluar extenderlo ahi (ver buy-ifvg.md/sell-ifvg.md). DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada, no extender a INV.",
      "2026-10-11 (domingo, REVISION SEMANAL): con el pareo de sigId corregido anoche (analyze.py commit 57c2aee, recupera pares que 'last-wins' descartaba) y afterN ya en 10296, la confirmacion por segmento RETIENE sólo 2 de 6 segmentos (antes 4 el 2026-10-08): 1m/RETEST/SHORT (n=2142, delta=+0.099 CI90=[0.032,0.169]) y 5m/RETEST/LONG (n=593, delta=+0.243 CI90=[0.052,0.472]). 1m/RETEST/LONG (n=3290, delta=+0.056 CI90=[-0.011,0.13]), 2m/RETEST/LONG (n=1608, delta=+0.07 CI90=[-0.006,0.149]), 2m/RETEST/SHORT (n=973, delta=+0.031 CI90=[-0.057,0.12]) y 5m/RETEST/SHORT (n=365, delta=+0.038 CI90=[-0.062,0.139]) vuelven a plano. Ningun segmento sale delta_below_zero=true. Verdict agregado formal (eval_experiments, mezcla los 6 segmentos): 'flat' (beforeN=18341 expR=0.052 -> afterN=10296 expR=0.037). No esta claro si el pareo corregido es la causa de que la confirmacion por segmento haya bajado de 4 a 2 (mas muestra real con el mismo pareo tambien podria explicarlo) -- vigilar la proxima corrida con dato nuevo real (esta semana fue fin de semana, sin sesion CME) para separar ambos efectos. DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada (ninguno negativo con significancia), no declarar 'confirmed' a nivel de gate (slCauseMitigated de 5m/RETEST/LONG sigue false pese a que ese segmento si certifica individualmente -- ver reviews/2026-week-41.md).",
      "2026-10-12 (lunes, feriado bancario EEUU/Columbus Day, sesion CME de bajo volumen, dia habil pero corto en dato real): since_change (recvDate>=2026-09-26, n=9349 total RETEST+INV, subio de 9237 el 10-11) mantiene la misma foto que el domingo -- SOLO 2 de 6 segmentos RETEST siguen confirmando limpio: 1m/RETEST/SHORT (n=2145, delta=+0.099 CI90=[0.029,0.175]) y 5m/RETEST/LONG (n=616, delta=+0.224 CI90=[0.035,0.443], el segmento del gate de ejecucion). 2m/RETEST/LONG sigue al filo sin certificar (n=1633, delta=+0.071 CI90=[-0.007,0.146], limite inferior casi en cero, igual que el domingo). 1m/RETEST/LONG (n=3349, delta=+0.057 CI90=[-0.007,0.126]), 2m/RETEST/SHORT (n=973, delta=+0.031 CI90=[-0.057,0.12]) y 5m/RETEST/SHORT (n=365, delta=+0.038 CI90=[-0.062,0.139]) siguen planos. Ningun segmento sale delta_below_zero=true. Verdict agregado formal (eval_experiments) sigue en \"flat\". Sin cambio de fondo desde la revision semanal del 10-11 (dato nuevo escaso por el feriado) -- DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada, seguir vigilando since_change semana a semana.",
      "2026-10-13 (martes, primer dia habil completo post-feriado): since_change (recvDate>=2026-09-26, n=10149, subio de 9349 ayer) mantiene la misma foto -- de los 7 segmentos con n>=100 post-cambio, SOLO 2 siguen confirmando limpio: 1m/RETEST/SHORT (n=2271, delta=+0.091 CI90=[0.024,0.16]) y 5m/RETEST/LONG (n=669, delta=+0.212 CI90=[0.043,0.415]). 2m/RETEST/LONG sigue al filo sin certificar (n=1775, delta=+0.064 CI90=[-0.007,0.139], practicamente identico a ayer). Ningun segmento sale delta_below_zero=true. Verdict agregado formal (eval_experiments) sigue en flat (beforeN=18341 expR=0.052 -> afterN=11291 expR=0.036). Nota en paralelo (no de este experimento, mismo mecanismo de SL): walk_forward.testWeeks avanzo a [W41,W42]; en esa ventana nueva, rr1_threshold_cut_oos (experimento sc-min-rr-cut, cerrado rejected_oos) muestra que el baseline SIN ningun corte se fortalece en 2m y 5m RETEST/LONG (2m ya certifica limpio OOS, antes al filo) mientras se debilita en los tres TF RETEST/SHORT (los tres pierden la significancia que tenian) -- posible rotacion de regimen LONG/SHORT entre ventanas, no tiene que ver con el SL de este experimento pero contextualiza por que 5m/RETEST/SHORT perdio su survives_fdr10 hoy por primera vez (ver sell-retest.md). DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada, seguir vigilando since_change semana a semana.",
      "2026-10-14 (miercoles, CPI 13:30 UTC): since_change (recvDate>=2026-09-26, n=10942, subio de 10149 ayer) da el salto mas grande hasta ahora en el lado LONG -- AHORA CONFIRMAN LOS TRES TF LONG (antes solo 5m): 1m/RETEST/LONG (n=4040, delta=+0.069 CI90=[0.012,0.134], confirma por primera vez), 2m/RETEST/LONG (n=1906, delta=+0.08 CI90=[0.01,0.154], sale del filo de ayer [-0.007,0.139] y confirma limpio), 5m/RETEST/LONG (n=730, delta=+0.184 CI90=[0.037,0.363], sigue confirmando). El lado SHORT no se mueve: 1m/RETEST/SHORT sigue confirmando (n=2421, delta=+0.09 CI90=[0.028,0.155]); 2m/RETEST/SHORT (n=1105, delta=+0.058 CI90=[-0.03,0.155]) y 5m/RETEST/SHORT (n=427, delta=+0.035 CI90=[-0.052,0.126]) siguen planos, sin cruzar. Con esto son 4 de 6 segmentos RETEST confirmando limpio post-cambio (antes 2 de 6/7) y ninguno sale delta_below_zero=true. Verdict agregado formal (eval_experiments, mezcla los 6 segmentos) sigue en \"flat\" -- la mejora de hoy es por segmento, no cambia el agregado todavia. DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada; vigilar 2-3 corridas mas antes de proponer declarar el efecto LONG como candidato a confirmed en la revision semanal del domingo 2026-10-18 (si se sostiene).",
      "2026-10-15 (jueves): since_change (recvDate>=2026-09-26, n=11969, subio de 10942 ayer) mantiene la misma foto de ayer -- siguen confirmando limpio los mismos 4 de 6 segmentos RETEST: 1m/RETEST/LONG (n=4348, delta=+0.08 CI90=[0.024,0.14]), 2m/RETEST/LONG (n=2067, delta=+0.076 CI90=[0.01,0.147]), 5m/RETEST/LONG (n=777, delta=+0.183 CI90=[0.039,0.373]), 1m/RETEST/SHORT (n=2738, delta=+0.084 CI90=[0.021,0.15]). 2m/RETEST/SHORT mejora un poco pero sigue al filo (n=1223, delta=+0.087 CI90=[-0.005,0.185], limite inferior casi en cero) y 5m/RETEST/SHORT baja a plano (n=472, delta=+0.013 CI90=[-0.073,0.103], ayer 0.035). Ningun segmento RETEST sale delta_below_zero=true. Verdict agregado formal (eval_experiments) sigue en flat (beforeN=18341 expR=0.052 -> afterN=13242 expR=0.042). Nota en paralelo (no de este experimento, mismo mecanismo de SL): el segmento objetivo del gate (5m/RETEST/LONG) tuvo su W42 parcial pasar de n=121 (WR51.2 PF1.39, cumplia el gate numerico) a n=172 (WR50.0 PF1.24, ya NO cumple PF>=1.3) al sumar mas muestra -- mismo patron de lecturas tempranas de semana sobrestimando el efecto que ya se documento varias veces en este experimento. Tambien el modo sombra perdio la recuperacion de W42 que parecia tener ayer (ver state.json/shadow_weekly): con casi el doble de muestra el E[R] quedo empatado shadow=raw=0.058 (shadow_beats_raw=false), van 2 semanas seguidas sin batir claramente al crudo. DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada, seguir vigilando since_change semana a semana.",
      "2026-10-16 (viernes): since_change (recvDate>=2026-09-26, n=12231, subio de 11969 ayer) mantiene la misma foto de los ultimos dias -- siguen confirmando limpio los mismos 4 de 6 segmentos RETEST: 1m/RETEST/LONG (n=4426, delta=+0.091 CI90=[0.031,0.149]), 2m/RETEST/LONG (n=2113, delta=+0.073 CI90=[0.013,0.136]), 5m/RETEST/LONG (n=786, delta=+0.188 CI90=[0.043,0.36]), 1m/RETEST/SHORT (n=2821, delta=+0.087 CI90=[0.031,0.15]). 2m/RETEST/SHORT sigue al filo sin certificar (n=1244, delta=+0.085 CI90=[-0.005,0.18], practicamente igual a ayer) y 5m/RETEST/SHORT mejora bastante aunque sigue sin cruzar cero (n=487, delta=+0.049 CI90=[-0.05,0.154], ayer 0.013). Ningun segmento RETEST sale delta_below_zero=true. Verdict agregado formal (eval_experiments) sigue en flat (beforeN=18341 expR=0.052 -> afterN=13538 expR=0.038) -- se aclaro en los playbooks que este verdict agregado mide con la metrica rMultiple vieja (el feed no recalcula tras el cambio real en TradingView, ver appliedNote), asi que la evidencia real de este experimento sigue viviendo en since_change/by_basis, no en ese verdict. Nota en paralelo: el segmento objetivo del gate (5m/RETEST/LONG) tuvo su W42 parcial pasar de n=172 (WR50.0 PF1.24) a n=181 (WR49.7 PF1.20) -- por primera vez el WR tambien cae bajo 50, tercera corrida seguida en que la lectura de la semana se modera a la baja con mas muestra. DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada, seguir vigilando since_change semana a semana.",
      "2026-10-17 (sabado): since_change (recvDate>=2026-09-26, n=13497, subio de 12231 ayer) ahora confirma limpio 5 de 6 segmentos RETEST -- se suma 2m/RETEST/SHORT (n=1326, delta=+0.098 CI90=[0.007,0.194], primera vez que cruza fuera de cero) a los 4 que ya confirmaban: 1m/RETEST/LONG (n=5034, delta=+0.104 CI90=[0.051,0.16]), 1m/RETEST/SHORT (n=2995, delta=+0.086 CI90=[0.028,0.144]), 2m/RETEST/LONG (n=2353, delta=+0.092 CI90=[0.03,0.156]), 5m/RETEST/LONG (n=885, delta=+0.213 CI90=[0.081,0.368]). Solo 5m/RETEST/SHORT sigue plano (n=517, delta=+0.07 CI90=[-0.028,0.177], limite inferior aun bajo cero). Ningun segmento sale delta_below_zero=true. Verdict agregado formal (eval_experiments, mide con la metrica rMultiple vieja, no refleja el cambio real) sigue en 'flat' -- la evidencia real sigue viviendo en since_change/by_basis. Nota en paralelo (mismo mecanismo de SL, otro indicador): el segmento objetivo del gate (5m/RETEST/LONG) cerro su semana W42 completa en n=286 WR53.1 PF1.23 -- sigue sin cumplir PF>=1.3 (W41 si cumplio, W39/W40/W42 no), asi que weeklyStable3 sigue false. Tambien el modo sombra (shadow_rules, mecanismo distinto, mismo gate de execution-ladder.md) va 2 semanas seguidas (W41, W42) sin batir claramente al indicador crudo tras 4 semanas seguidas batiendolo (W37-W40) -- vigilar en la revision semanal de manana si se convierte en una tercera semana, podria estar relacionado con la misma rotacion de regimen LONG/SHORT que ya se noto el 10-13. DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada, seguir vigilando since_change semana a semana.",
      "2026-10-21 (miercoles, tercer dia de dato real de la semana): since_change (recvDate>=2026-09-26, n=15081, sube de 13497 ayer) mantiene y profundiza el hito de ayer -- siguen confirmando limpio los 6 de 6 segmentos RETEST, segundo dia consecutivo: 1m/RETEST/LONG (n=5627, delta=+0.119 CI90=[0.07,0.174]), 1m/RETEST/SHORT (n=3323, delta=+0.079 CI90=[0.024,0.132]), 2m/RETEST/LONG (n=2629, delta=+0.105 CI90=[0.048,0.164]), 2m/RETEST/SHORT (n=1474, delta=+0.098 CI90=[0.015,0.189]), 5m/RETEST/LONG (n=995, delta=+0.201 CI90=[0.081,0.342]), 5m/RETEST/SHORT (n=602, delta=+0.136 CI90=[0.016,0.283], ya no roza cero como ayer). Ningun segmento sale delta_below_zero=true. Verdict agregado formal (eval_experiments, mide con la metrica rMultiple vieja) sigue en 'flat' (beforeN=18341 expR=0.052 -> afterN=16630 expR=0.029) -- sin cambio de fondo, la evidencia real sigue viviendo en since_change/by_basis. Nota en paralelo (mismo mecanismo de SL, no de este experimento): el agregado historico completo de RETEST/LONG tuvo una semana de mercado floja los ultimos 3 dias (W43 en curso, los tres TF LONG en rojo, ver buy-retest.md) sin que esto afecte la direccion de since_change en ningun segmento LONG -- confirma otra vez que este experimento mide algo distinto del nivel absoluto de E[R] del dia. DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada. Con 2 dias consecutivos de 6/6 confirmando limpio, se considera para la revision semanal del domingo 2026-10-25 subir la confianza documentada del experimento de 'aplicado, parcial' a 'aplicado, 6/6 certifican de forma sostenida' -- no se decide hoy.",
      "2026-10-22 (jueves, cuarto dia de dato real de la semana): since_change (recvDate>=2026-09-26, n=15908, sube de 15081 ayer) completa su TERCER dia consecutivo con los 6 de 6 segmentos RETEST confirmando limpio: 1m/RETEST/LONG (n=5814, delta=+0.117 CI90=[0.067,0.17]), 1m/RETEST/SHORT (n=3585, delta=+0.085 CI90=[0.032,0.144]), 2m/RETEST/LONG (n=2715, delta=+0.121 CI90=[0.06,0.182]), 2m/RETEST/SHORT (n=1623, delta=+0.1 CI90=[0.021,0.181]), 5m/RETEST/LONG (n=1052, delta=+0.218 CI90=[0.105,0.356]), 5m/RETEST/SHORT (n=667, delta=+0.153 CI90=[0.04,0.287]). Ningun segmento sale delta_below_zero=true. Verdict agregado formal (eval_experiments, metrica rMultiple vieja) sigue en 'flat'. Nota en paralelo (mismo mecanismo de SL, no de este experimento): el agregado historico completo de 5m/RETEST/SHORT volvio a rozar cero en segment_significance (CI90 [0.003,0.118]->[-0.001,0.117]) porque W43 profundiza su rojo en ese TF especifico (n=62->127, E[R]-0.184->-0.105) -- esto NO afecta a since_change de este experimento, que sigue limpio en los 6/6; es evidencia adicional de que el experimento mide algo distinto del nivel absoluto de E[R] semanal. Tambien en paralelo: walk_forward.OOS E[R] del bus bajo de 0.015 a 0.008 (sigue positivo, margen muy delgado) y el modo sombra (shadow_weekly) sigue perdiendo en W43 (shadow n=2015 E[R]=-0.112 vs raw n=2171 E[R]=-0.096) -- si cierra asi serian 3 semanas seguidas sin batir al indicador crudo. DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada. Con 3 dias consecutivos de 6/6 confirmando limpio, se mantiene para la revision semanal del domingo 2026-10-25 la propuesta de subir la confianza documentada de 'aplicado, parcial' a 'aplicado, 6/6 certifican de forma sostenida' -- no se decide hoy.",
      "2026-10-23 (viernes, quinto dia de dato real de la semana): since_change (recvDate>=2026-09-26, n=17191, sube de 15908 ayer) completa su CUARTO dia consecutivo con los 6 de 6 segmentos RETEST confirmando limpio: 1m/RETEST/LONG (n=6363, delta=+0.111 CI90=[0.064,0.16]), 1m/RETEST/SHORT (n=3806, delta=+0.092 CI90=[0.036,0.15]), 2m/RETEST/LONG (n=3000, delta=+0.118 CI90=[0.061,0.18]), 2m/RETEST/SHORT (n=1710, delta=+0.093 CI90=[0.02,0.171]), 5m/RETEST/LONG (n=1136, delta=+0.206 CI90=[0.097,0.335]), 5m/RETEST/SHORT (n=697, delta=+0.147 CI90=[0.035,0.272]). Ningun segmento sale delta_below_zero=true. Verdict agregado formal (eval_experiments, metrica rMultiple vieja) sigue en 'flat'. Nota en paralelo (mismo mecanismo de SL, no de este experimento): walk_forward OOS E[R] del bus sube de 0.008 a 0.015, primera mejora tras varios dias de caida; decay_weekly_by_segment de W43 revierte parte de su rojo en RETEST/LONG (2m cruza a positivo por primera vez esta semana, 1m mejora fuerte) mientras en RETEST/SHORT 1m cruza a negativo por primera vez (ver buy-retest.md/sell-retest.md). El modo sombra (shadow_weekly) sigue perdiendo en W43 pero la brecha shadow-raw se estrecha (shadow n=3403 E[R]=-0.046 vs raw n=3559 E[R]=-0.039, de -0.016 a -0.007) -- si cierra asi serian 3 semanas seguidas sin batir al indicador crudo. DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada. Con 4 dias consecutivos de 6/6 confirmando limpio, se mantiene para la revision semanal del domingo 2026-10-25 la propuesta de subir la confianza documentada de 'aplicado, parcial' a 'aplicado, 6/6 certifican de forma sostenida' -- no se decide hoy.",
      "2026-10-25 (domingo, REVISION SEMANAL 2026-week-43): since_change (recvDate>=2026-09-26, n=18022, sube de 17191 el viernes) completa su SEXTO dia consecutivo con los 6 de 6 segmentos RETEST confirmando limpio -- y por primera vez 5m SHORT deja de estar 'al filo': 1m/RETEST/LONG (n=6555, delta=+0.115 CI90=[0.066,0.162]), 1m/RETEST/SHORT (n=4122, delta=+0.084 CI90=[0.034,0.139]), 2m/RETEST/LONG (n=3080, delta=+0.124 CI90=[0.065,0.185]), 2m/RETEST/SHORT (n=1842, delta=+0.098 CI90=[0.029,0.172]), 5m/RETEST/LONG (n=1186, delta=+0.204 CI90=[0.099,0.319]), 5m/RETEST/SHORT (n=742, delta=+0.128 CI90=[0.022,0.249] -- ya no cruza cero, el ultimo de los 6 en despejarse). Ningun segmento sale delta_below_zero=true desde el cambio, casi un mes sin ninguna reversion. DECISION de esta revision semanal (ver reviews/2026-week-43.md): se sube la confianza documentada del experimento de 'aplicado, parcial/mayoria certifica' a 'aplicado, 6/6 certifican de forma sostenida (~1 mes sin reversion)'. En paralelo, se marca que el criterio de madurez que shadow_rules venia esperando para decidir si medir con rOrig en vez de rMultiple YA SE CUMPLE -- no se implementa el cambio de metrica en esta misma corrida (toca el calculo historico del gate sombra-vs-crudo, que ademas esta en su tercera semana cerrada consecutiva sin batir al indicador crudo, ver shadow_weekly y la alerta nueva anadida hoy a analyze.py; conviene revisar el resultado con calma antes de tocar dos cosas la misma corrida) -- queda marcado 'listo para implementar' en la proxima corrida, ya no 'pendiente de madurar'. Nota de pipeline, no de este experimento: no llego ningun dato nuevo desde el jueves 2026-10-22 (falta el viernes 2026-10-23 completo, ver reviews/2026-week-43.md hallazgo 1) -- el n de este experimento solo subio por el recuento, no por dato genuinamente nuevo hoy.",
      "2026-10-26 (lunes): since_change (recvDate>=2026-09-26, n=18175, sube de 18022 el domingo) cumple hoy ~1 MES desde el changeDate (2026-09-26->2026-10-26) con los 6 de 6 segmentos RETEST todavia confirmando limpio, sin una sola reversion en todo el mes: 1m/RETEST/LONG (n=6560, delta=+0.114 CI90=[0.066,0.163]), 1m/RETEST/SHORT (n=4193, delta=+0.079 CI90=[0.03,0.133]), 2m/RETEST/LONG (n=3085, delta=+0.124 CI90=[0.067,0.185]), 2m/RETEST/SHORT (n=1879, delta=+0.107 CI90=[0.034,0.18]), 5m/RETEST/LONG (n=1189, delta=+0.204 CI90=[0.099,0.324]), 5m/RETEST/SHORT (n=772, delta=+0.146 CI90=[0.039,0.266]). Hallazgo nuevo de hoy: se reviso por primera vez a este nivel de detalle el since_change del lado INV (fuera del scope del experimento, kind=RETEST unicamente) y el efecto NO generaliza -- signo CONTRARIO en SHORT (1m/INV/SHORT n=129 delta=-0.305 CI90=[-0.538,-0.08], estructuralmente peor) e inconcluyente en LONG (1m/INV/LONG n=219 delta=+0.349 CI90=[0.073,0.655], positivo pero n demasiado chico y fuera de scope para actuar). Esto refuerza que el segment de este experimento debe seguir siendo {'kind':'RETEST'} unicamente -- no extender a INV sin evidencia propia y mayor muestra (ver buy-ifvg.md / sell-ifvg.md). Modo sombra: la alerta permanente anadida ayer a analyze.py dispara hoy por primera vez (3 semanas CERRADAS seguidas sin batir al indicador crudo: W41/W42/W43) -- no afecta a este experimento directamente (es un gate distinto, peldano 0->1 de la escalera), pero queda anotado como contexto: el cambio de metrica de shadow_rules (rMultiple-> rOrig) sigue 'listo para implementar', pendiente de ejecutarse. No se decide nada nuevo hoy sobre el verdict agregado (sigue 'flat' por la limitacion de metrica ya conocida)."
    ],
    "appliedNote": "2026-09-26: aplicado en scalp_command.pine (input sc_sl_retest_basis, default 'Auto (como se midio)'): en RETEST el SL real pasa a la mecha de la vela del retest; 1m SHORT suma la vela previa (retestBar2), igual que la medicion paralela. Base: los 6 segmentos RETEST certifican con CI90 > 0 (n=11273, E[R] 0.238 vs 0.065). El tier se sigue calculando con el stop de 3 capas. El feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig, asi que sl_origin_vs_layer sigue siendo la vigilancia. Rige en cada grafico desde que Jesus re-pega scalp_cc_FULL_for_tradingview.pine. Revertir = poner la base en '3 capas'.",
    "beforeN": 18341,
    "afterN": 20613,
    "before": {
      "n": 18341,
      "wrTP1": 45.8,
      "nSL": 8436,
      "nTO": 1513,
      "expR": 0.052,
      "pf": 1.11,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 32.8
    },
    "after": {
      "n": 20613,
      "wrTP1": 46.2,
      "nSL": 9797,
      "nTO": 1302,
      "expR": 0.032,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 32.1
    },
    "verdict": "flat"
  },
  {
    "id": "sc-min-rr-cut-2026-09-20",
    "status": "rejected_oos",
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
      "2026-09-29 (martes): el walk-forward testWeeks avanzo de [W38,W39] a [W39,W40] (W39 ya cerro, W40 es la semana en curso) y con la ventana nueva el unico candidato que habia confirmado OOS limpio el 09-27 (5m/RETEST/LONG) PIERDE la certificacion: baseline test n=287 expR=0.084 CI90=[-0.046,0.215] (cruza cero, antes n=544 expR=0.148 CI90=[0.056,0.247] no cruzaba) y los cortes 1.2/1.3 salen con CI90 igual de anchos y cruzando cero (ej. 1.2: expR=0.161 CI90=[-0.175,0.527]) -- el patron todavia apunta en la misma direccion (subir el piso de rr1 sube el E[R] observado) pero ya no certifica fuera de muestra con esta ventana mas chica (W40 apenas tiene unos dias de dato). No es una reversion de signo, es perdida de potencia estadistica al cambiar de ventana de test -- vigilar si vuelve a certificar cuando W40 cierre con mas muestra. Sigue sin proponerse ningun valor concreto de sc_aplus_rr; la linea 7 de predictions.jsonl sigue sin appliedDate.",
      "2026-10-04 (domingo, REVISION SEMANAL): el walk-forward testWeeks avanzo otra vez, ahora de [W38,W39] a [W39,W40] (los dos ya cerrados, no una semana parcial como el 09-29). El candidato que SI habia confirmado limpio en la revision de 2026-week-39.md con la ventana [W38,W39] (5m/RETEST/LONG, rr1>=1.2, baseline n=544 expR=0.148 CI90=[0.056,0.247], corte expR=0.372 CI90=[0.149,0.605]) deja de confirmar con [W39,W40]: baseline n=515 expR=0.102 CI90=[0.013,0.192] (todavia positivo), corte 1.2 n=178 expR=0.178 pero CI90=[-0.045,0.409] cruza cero. A diferencia del 09-29 (donde la perdida de potencia era por W40 parcial con pocos dias), esta vez W40 esta completa -- es una perdida de confirmacion real con la ventana madura, no un artefacto de muestra chica. Se retira como candidato activo esta semana (ver reviews/2026-week-40.md); como nunca se aplico en TradingView (status sigue 'proposed', predictions.jsonl linea de 2026-W39 sigue con appliedDate=null), no hay nada que revertir. Ningun otro segmento de RETEST confirma el corte de rr1 con el split OOS actual. Leccion de metodo: un candidato que confirma con una ventana OOS de 2 semanas puede dejar de confirmar en la siguiente sin que el patron in-sample cambie -- tratar cualquier confirmacion OOS de una sola ventana como fragil hasta verla sostenerse en 2-3 rodadas de la ventana, no solo una.",
      "2026-10-07 (miercoles): walk_forward.testWeeks sigue en [W40,W41] (sin avanzar desde la lectura del 10-05/10-06), pero rr1_threshold_cut_oos no se habia narrado todavia contra esta ventana concreta -- se hace hoy. Resultado: de los 4 segmentos que alguna vez confirmaron en alguna ventana OOS pasada (1m SHORT, 2m SHORT, 5m LONG, y ahora se agrega 2m LONG que no se habia mirado antes), NINGUNO confirma positivo en [W40,W41] -- 1m/RETEST/SHORT baseline n=1765 expR=0.045 CI90=[-0.001,0.094] (al filo de cero) y cae a plano/negativo en todos los cortes (cut>=2.0 expR=-0.012); 2m/RETEST/SHORT baseline n=789 expR=0.082 CI90=[0.012,0.159] (unico baseline que certifica) pero el corte lo EMPEORA monotonicamente (1.2:+0.049 -> 1.5:-0.03 -> 2.0:-0.022, todos CI90 cruzando cero); 5m/RETEST/LONG baseline n=379 expR=0.093 CI90=[-0.008,0.198] y el corte sube con muestra chica pero CI90 nunca deja de cruzar cero (cut 1.2 n=133 expR=0.189 CI90=[-0.048,0.433]). NUEVO Y MAS FUERTE: 2m/RETEST/LONG, que nunca se habia reportado como candidato de este corte, sale CLARAMENTE NEGATIVO y con muestra grande -- baseline n=1071 expR=-0.024 CI90=[-0.076,0.032] (ya negativo) y cada escalon de corte lo empeora con CI90 que NO cruza cero: cut>=1.2 n=404 expR=-0.174 CI90=[-0.285,-0.056]; cut>=1.5 n=307 expR=-0.306 CI90=[-0.439,-0.172]; cut>=2.0 n=195 expR=-0.342 CI90=[-0.515,-0.148]. Es la primera vez que este corte sale negativo fuera de muestra con significancia real (delta_below_zero equivalente), no solo 'deja de confirmar'. LECTURA: la racha de confirmaciones in-sample de 1m/2m SHORT y 5m LONG que motivo esta propuesta en 09-20/09-22 lleva ya DOS ventanas OOS distintas ([W39,W40] y [W40,W41]) sin replicarse, y ahora hay evidencia nueva de que subir el piso de rr1 puede ser CONTRAPRODUCENTE en 2m LONG. DECISION: no se propone sc_min_rr/sc_aplus_rr en ninguna revision semanal mientras este patron se mantenga -- se baja la prioridad de este experimento de 'candidato pendiente de confirmar' a 'probablemente no generaliza, vigilar solo si vuelve a aparecer con 2+ ventanas OOS seguidas en la misma direccion'. No cambia status (sigue 'proposed', nunca se aplico en TradingView, nada que revertir).",
      "2026-10-08 (jueves): walk_forward.testWeeks sigue en [W40,W41]. Hallazgo mas fuerte que el 10-07: en esta ventana OOS el BASELINE sin ningun corte de rr1 ya es negativo con significancia en 1m/RETEST/LONG (n=2841, expR=-0.047, CI90=[-0.081,-0.009]) y cada escalon de corte lo empeora mas (hasta expR=-0.208 en cut>=2.0). 2m/RETEST/LONG baseline esta plano (n=1348, expR=-0.005, CI90=[-0.051,0.044]) pero cualquier corte lo vuelve negativo con significancia (cut>=1.2 expR=-0.137 CI90=[-0.237,-0.03]). Del lado SHORT, 2m/RETEST/SHORT sigue siendo el unico baseline OOS significativo y positivo (n=919, expR=0.101, CI90=[0.035,0.169]) pero los cortes no mejoran eso (CI90 vuelve a cruzar cero en todos). 1m SHORT sigue al filo (CI90=[-0.001,0.085)). 5m LONG baseline sigue positivo y significativo (n=483, expR=0.123, CI90=[0.031,0.215]) -- el unico TF RETEST que sostiene el edge OOS limpio hoy entre los 6. CONCLUSION: subir rr1 no soluciona nada donde el problema es que el baseline mismo ya es negativo (1m/2m LONG); seguir sin proponer sc_min_rr/sc_aplus_rr al alza en ningun segmento mientras esto se sostenga.",
      "2026-10-09 (viernes): walk_forward.testWeeks sigue en [W40,W41]. Con esta ventana ya se evaluaron los 6 segmentos RETEST (los 3 LONG desde el 10-07/10-08, ahora tambien los 3 SHORT) y en NINGUNO el corte de rr1 mejora el E[R] fuera de muestra -- incluidos 1m SHORT y 2m SHORT, los dos candidatos originales de este experimento (09-20/09-22) que nunca se habian evaluado formalmente contra el split OOS actual hasta hoy. 2m/RETEST/SHORT baseline sigue siendo el unico SHORT que certifica (n=1013, expR=0.087, CI90=[0.024,0.152]) pero los 4 cortes de rr1 lo vuelven no significativo (CI90 cruza cero en todos, ej. cut>=1.2 expR=0.069 CI90=[-0.066,0.207]). 1m/RETEST/SHORT baseline sigue al filo (n=2292, expR=0.041, CI90=[0.002,0.083]) y el corte 2.0 lo manda a negativo (expR=-0.041). En LONG, 2m/RETEST/LONG ahora tiene los 4 cortes negativos con significancia (antes solo se sabia de un corte el 10-07); 1m/RETEST/LONG baseline mejora un poco (-0.047 -> -0.033) pero sigue compatible con negativo (CI90=[-0.066,0.001]). Solo 5m/RETEST/LONG se mantiene positivo y significativo en baseline sin necesidad de ningun corte (n=535, expR=0.1, CI90=[0.015,0.185]). DECISION: con los 6 segmentos ya evaluados contra 2+ ventanas OOS sin que ningun corte de rr1 generalice, se cierra este experimento como 'rejected_oos' -- nunca se aplico en TradingView (status previo 'proposed'), asi que no hay nada que revertir. Si se quiere perseguir la idea de RR minimo en el futuro, deberia evaluarse de nuevo desde cero con una ventana OOS distinta y mayor muestra, no reabrir este mismo experimento."
    ]
  }
]
```

## Session Analyst
```json
{
  "available": true,
  "latest_plan": {
    "date": "2026-10-27",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-10-26T16:30:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "GC",
    "focus": {
      "sym": "GC",
      "verdict": "WAIT",
      "window": "19:00-01:00 CT",
      "setup": {
        "es": "fade de la resistencia rota VAH 4036.6-4047.8, confluencia 6 (perfil+PDH cercano+MTF+prior del día)",
        "en": "fade of the broken VAH resistance 4036.6-4047.8, confluence 6 (profile+nearby PDH+MTF+prior day)"
      },
      "trigger": {
        "es": "toque de 4036.6-4047.8 con rechazo y cierre 5m de vuelta bajo 4036.6; la señal de venta del motor (hace 5 velas) ya apunta a esto",
        "en": "a tag of 4036.6-4047.8 with rejection and a 5m close back below 4036.6; the engine's sell signal (5 bars ago) already points this way"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 4047.8 (la cuna, ya probada 16 veces)",
        "en": "sustained 5m close above 4047.8 (the wedge, already tested 16 times)"
      },
      "note": {
        "es": "conflicto de marcos abierto (fondo -3/-3 vs la sesión que ya giró a LARGO en el orb): espera el rechazo real, no lo anticipes. El estiramiento de 3.9 ATR que marca el motor fusionado choca con el 0.1 ATR de drbias -- es el glitch conocido del cierre de 16:00, ignóralo",
        "en": "open frame conflict (background -3/-3 vs the session that already flipped LONG in orb): wait for the real rejection, don't front-run it. The 3.9 ATR stretch the fused engine shows clashes with drbias's 0.1 ATR -- the known 16:00-close glitch, ignore it"
      }
    },
    "summary": {
      "es": [
        "!! Narrativa de NQ y ES se rompió hoy: el corto de 3 días terminó con ES y YM confirmando sus propios máximos y cierre sostenido; revisa dayThesis.",
        "NQ: ruptura alcista día 1, muy estirada (lectura de 5.3 ATR del motor es el glitch conocido del cierre; drbias marca solo 0.2 ATR), sin borde a tiro todavía (zona de pullback 29326-29383 a ~70pts, estirada).",
        "ES: ruptura alcista día 1 menos limpia, cerró pegado al PDH 7714.25 (IBH con 25 toques, nivel desgastado); zona de reclamo 7698.5-7714.25 a tiro pero sin gatillo confirmado aún.",
        "GC: 1ª fisura real tras 5 sesiones de corto limpio; la resistencia 4036.6-4047.8 (16 toques) sigue aguantando por el margen más estrecho medido; más limpio del día.",
        "YM: la lectura más mezclada -- motor fusionado en LARGO FUERTE contra el sesgo corto de fondo, sin que ninguno gane; sin zona limpia hoy, no fuerces.",
        "CL: pagó TP1/TP2 del reinicio alcista y luego dio el primer giveback violento sin catalizador, cerrando de vuelta sobre ambas invalidaciones; zona de reclamo 100.72-101.34 solo B (conf. 5).",
        "Límite diario $1000/cuenta ⇒ con estos stops (NQ $1015, ES $412, GC $610, CL $730 por contrato full) el máximo en full sale en 0 en los 4 -- considera micros (/10) si operas alguna.",
  
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 20371,
  "by_verdict": {
    "AVOID": {
      "n": 2502,
      "wrTP1": 44.4,
      "nSL": 1206,
      "nTO": 184,
      "expR": 0.016,
      "pf": 1.03,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.8
    },
    "GO": {
      "n": 3511,
      "wrTP1": 47.4,
      "nSL": 1630,
      "nTO": 218,
      "expR": 0.02,
      "pf": 1.04,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 37.7
    },
    "WAIT": {
      "n": 14358,
      "wrTP1": 46.0,
      "nSL": 6824,
      "nTO": 933,
      "expR": 0.036,
      "pf": 1.07,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 32.6
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.016,
      "ci90": [
        -0.025,
        0.058
      ],
      "p_mean_le_0": 0.258,
      "n": 2381
    },
    "GO": {
      "expR": 0.02,
      "ci90": [
        -0.012,
        0.052
      ],
      "p_mean_le_0": 0.163,
      "n": 3381
    },
    "WAIT": {
      "expR": 0.036,
      "ci90": [
        0.019,
        0.054
      ],
      "p_mean_le_0": 0.0,
      "n": 13916
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 2502,
      "wrTP1": 44.4,
      "nSL": 1206,
      "nTO": 184,
      "expR": 0.016,
      "pf": 1.03,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.8
    },
    "GO_or_WAIT": {
      "n": 17869,
      "wrTP1": 46.2,
      "nSL": 8454,
      "nTO": 1151,
      "expR": 0.033,
      "pf": 1.07,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.6
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.016,
      "ci90": [
        -0.025,
        0.058
      ],
      "p_mean_le_0": 0.258,
      "n": 2381
    },
    "GO_or_WAIT": {
      "expR": 0.033,
      "ci90": [
        0.018,
        0.048
      ],
      "p_mean_le_0": 0.001,
      "n": 17297
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 42,
        "wrTP1": 45.2,
        "nSL": 19,
        "nTO": 4,
        "expR": -0.102,
        "pf": 0.79,
        "mfe_p25": 6.0,
        "mfe_p50": 13.5,
        "mfe_p75": 30.25,
        "winnerMAE_p75": 13.5,
        "winnerMAE_p90": 17.4,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -10.5,
        "revAfterSL_rate": 21.1
      },
      "GO": {
        "n": 57,
        "wrTP1": 52.6,
        "nSL": 22,
        "nTO": 5,
        "expR": 0.071,
        "pf": 1.17,
        "mfe_p25": 5.0,
        "mfe_p50": 18.0,
        "mfe_p75": 30.5,
        "winnerMAE_p75": 11.5,
        "winnerMAE_p90": 38.1,
        "loserMFEbeforeSL_p50": 3.5,
        "bars_win_p50": 5.5,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -9.0,
        "revAfterSL_rate": 31.8
      },
      "WAIT": {
        "n": 231,
        "wrTP1": 43.3,
        "nSL": 110,
        "nTO": 21,
        "expR": -0.022,
        "pf": 0.96,
        "mfe_p25": 7.0,
        "mfe_p50": 15.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 22.200000000000017,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 16.4
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 32,
        "wrTP1": 34.4,
        "nSL": 16,
        "nTO": 5,
        "expR": -0.247,
        "pf": 0.56,
        "mfe_p25": 8.0,
        "mfe_p50": 16.0,
        "mfe_p75": 24.0,
        "winnerMAE_p75": 4.5,
        "winnerMAE_p90": 6.0,
        "loserMFEbeforeSL_p50": 13.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 7.5,
        "entryZoneTk_p50": -11.5,
        "revAfterSL_rate": 12.5
      },
      "GO": {
        "n": 23,
        "wrTP1": 65.2,
        "nSL": 7,
        "nTO": 1,
        "expR": 0.22,
        "pf": 1.71,
        "mfe_p25": 11.5,
        "mfe_p50": 27.0,
        "mfe_p75": 49.5,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 29.39999999999999,
        "loserMFEbeforeSL_p50": 15.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 14.3
      },
      "WAIT": {
        "n": 179,
        "wrTP1": 49.2,
        "nSL": 66,
        "nTO": 25,
        "expR": 0.112,
        "pf": 1.29,
        "mfe_p25": 7.0,
        "mfe_p50": 23.5,
        "mfe_p75": 52.25,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 25.299999999999997,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 22.7
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 1555,
        "wrTP1": 44.2,
        "nSL": 767,
        "nTO": 100,
        "expR": -0.004,
        "pf": 0.99,
        "mfe_p25": 8.0,
        "mfe_p50": 16.0,
        "mfe_p75": 33.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 33.4
      },
      "GO": {
        "n": 2295,
        "wrTP1": 46.8,
        "nSL": 1098,
        "nTO": 123,
        "expR": 0.009,
        "pf": 1.02,
        "mfe_p25": 6.0,
        "mfe_p50": 15.0,
        "mfe_p75": 34.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 36.6
      },
      "WAIT": {
        "n": 8296,
        "wrTP1": 46.2,
        "nSL": 3985,
        "nTO": 476,
        "expR": 0.034,
        "pf": 1.07,
        "mfe_p25": 6.0,
        "mfe_p50": 15.0,
        "mfe_p75": 35.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 32.6
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 873,
        "wrTP1": 45.1,
        "nSL": 404,
        "nTO": 75,
        "expR": 0.068,
        "pf": 1.14,
        "mfe_p25": 9.0,
        "mfe_p50": 21.0,
        "mfe_p75": 40.0,
        "winnerMAE_p75": 15.75,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 39.1
      },
      "GO": {
        "n": 1136,
        "wrTP1": 47.9,
        "nSL": 503,
        "nTO": 89,
        "expR": 0.035,
        "pf": 1.07,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 34.69999999999999,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 40.6
      },
      "WAIT": {
        "n": 5652,
        "wrTP1": 45.6,
        "nSL": 2663,
        "nTO": 411,
        "expR": 0.041,
        "pf": 1.08,
        "mfe_p25": 9.0,
        "mfe_p50": 22.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 30.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 33.5
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
    "n": 36520,
    "wrTP1": 46.1,
    "nSL": 17062,
    "nTO": 2640,
    "expR": 0.042,
    "pf": 1.09,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.2
  },
  "shadow_ci90": {
    "expR": 0.042,
    "ci90": [
      0.032,
      0.053
    ],
    "p_mean_le_0": 0.0,
    "n": 35176
  },
  "raw_indicator": {
    "n": 38954,
    "wrTP1": 46.0,
    "nSL": 18233,
    "nTO": 2815,
    "expR": 0.041,
    "pf": 1.08,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 32.4
  },
  "raw_indicator_ci90": {
    "expR": 0.041,
    "ci90": [
      0.031,
      0.051
    ],
    "p_mean_le_0": 0.0,
    "n": 37494
  },
  "tier_ap_b_only": {
    "n": 20202,
    "wrTP1": 43.2,
    "nSL": 9908,
    "nTO": 1565,
    "expR": 0.032,
    "pf": 1.06,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 5.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 30.7
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.032,
    "ci90": [
      0.017,
      0.048
    ],
    "p_mean_le_0": 0.0,
    "n": 19465
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```

## Modo sombra por semana (gate: shadow_beats_raw 3 semanas seguidas, n>=60)
```json
{
  "2026-W36": {
    "shadow_n": 3044,
    "shadow_expR": -0.034,
    "raw_n": 3136,
    "raw_expR": -0.027,
    "shadow_beats_raw": false
  },
  "2026-W37": {
    "shadow_n": 4456,
    "shadow_expR": 0.084,
    "raw_n": 5248,
    "raw_expR": 0.07,
    "shadow_beats_raw": true
  },
  "2026-W38": {
    "shadow_n": 4293,
    "shadow_expR": 0.103,
    "raw_n": 4807,
    "raw_expR": 0.091,
    "shadow_beats_raw": true
  },
  "2026-W39": {
    "shadow_n": 5151,
    "shadow_expR": 0.053,
    "raw_n": 5227,
    "raw_expR": 0.051,
    "shadow_beats_raw": true
  },
  "2026-W40": {
    "shadow_n": 4684,
    "shadow_expR": 0.018,
    "raw_n": 5223,
    "raw_expR": 0.016,
    "shadow_beats_raw": true
  },
  "2026-W41": {
    "shadow_n": 5032,
    "shadow_expR": 0.053,
    "raw_n": 5084,
    "raw_expR": 0.057,
    "shadow_beats_raw": false
  },
  "2026-W42": {
    "shadow_n": 4786,
    "shadow_expR": 0.05,
    "raw_n": 4993,
    "raw_expR": 0.05,
    "shadow_beats_raw": false
  },
  "2026-W43": {
    "shadow_n": 4453,
    "shadow_expR": -0.009,
    "raw_n": 4609,
    "raw_expR": -0.005,
    "shadow_beats_raw": false
  },
  "2026-W44": {
    "shadow_n": 621,
    "shadow_expR": 0.032,
    "raw_n": 627,
    "raw_expR": 0.045,
    "shadow_beats_raw": false
  }
}
```
