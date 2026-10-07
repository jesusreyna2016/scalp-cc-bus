# Scalp CC · report 2026-10-07T01:15Z
- signals=24013 outcomes=23027 pares_resueltos=24004 pendientes=9 huerfanos=40

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: semana ya cerrada 2026-W37 bajo de n=5389 a n=4891 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W39 bajo de n=5355 a n=5038 desde la corrida previa -- vigilar, puede ser deduplicacion.
- SIGID: 1725 sigId de senales y 1617 de outcomes colisionan (mismo sigId, receivedAt distinto); 939 tienen result DISTINTO entre ocurrencias -> no es reenvio, son pares reales distintos fusionados en un sigId (ver nota en sigid_collision_report). 'last wins' descarta una ocurrencia y desplaza la otra a una semana posterior: probable causa de las alertas MUESTRA. Arreglar la generacion de sigId en el Pine (deltas en dias casi siempre multiplo de 7, sugiere bar_index que se reinicia semanalmente).
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.18 vs 0.049, delta 0.131 CI90 [0.1, 0.163], n 15074). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.149 vs 0.043, delta 0.106 CI90 [0.053, 0.16], n 4850). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.138 CI90 [0.08, 0.196], n 1149). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.05 CI90 [0.026, 0.073], n 7385). Consistente con la hipotesis original de agent-instructions.md.
- EXPERIMENTO: el efecto de sl_basis_retest se encoge desde que se aplico (2026-09-26): de 6 segmentos con n>=100 post-cambio, solo 1 sigue confirmando (CI90 no cruza cero) y 0 se invierten -- ver since_change vs by_basis (historico completo). No revertir sin mas evidencia, pero no tratar como confirmado fuera del/los segmento(s) que si certifican.
- METODO: tus predicciones de direccion aciertan 33.3% (peor que un volado, n=6, MAE=0.283). Se mas conservador con 'cambio del mes' y marcar experimental mas tiempo antes de subir confianza.

- E[R] global: {"expR": 0.049, "ci90": [0.036, 0.063], "p_mean_le_0": 0.0, "n": 22987}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Integridad de sigId (colisiones, posible causa de alertas MUESTRA)
```json
{
  "signals": {
    "total_sigIds": 24013,
    "collided_sigIds": 1725,
    "collided_pct": 7.18,
    "delta_days_histogram": {
      "7": 593,
      "14": 585,
      "21": 299,
      "28": 161,
      "15": 31,
      "29": 22,
      "8": 12,
      "13": 9,
      "22": 7,
      "31": 2
    },
    "conflicting_result_n": 0,
    "conflicting_result_examples": []
  },
  "outcomes": {
    "total_sigIds": 23027,
    "collided_sigIds": 1617,
    "collided_pct": 7.02,
    "delta_days_histogram": {
      "14": 559,
      "7": 548,
      "21": 275,
      "28": 161,
      "15": 23,
      "29": 17,
      "8": 13,
      "22": 6,
      "13": 6,
      "20": 3
    },
    "conflicting_result_n": 939,
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
| 1m/INV/LONG | 210 | 46.7 | 0.162 | 1.37 | 87 | 15.0 | 11.75 | 21.8 |
| 1m/INV/SHORT | 192 | 44.8 | 0.004 | 1.01 | 82 | 19.0 | 14.0 | 17.1 |
| 1m/RETEST/LONG | 8579 | 44.9 | 0.038 | 1.08 | 4078 | 15.0 | 11.0 | 27.8 |
| 1m/RETEST/SHORT | 6075 | 44.7 | 0.04 | 1.08 | 2808 | 18.0 | 11.0 | 29.8 |
| 2m/INV/LONG | 77 | 51.9 | 0.049 | 1.12 | 29 | 15.0 | 17.0 | 17.2 |
| 2m/INV/SHORT | 80 | 43.8 | 0.129 | 1.29 | 34 | 22.0 | 12.0 | 32.4 |
| 2m/RETEST/LONG | 3823 | 46.8 | 0.031 | 1.06 | 1796 | 20.0 | 14.0 | 38.3 |
| 2m/RETEST/SHORT | 2602 | 47.8 | 0.078 | 1.17 | 1183 | 23.0 | 13.0 | 40.2 |
| 5m/INV/LONG | 25 | 76.0 | 0.408 | 4.13 | 3 | 28.0 | 29.0 | 66.7 |
| 5m/INV/SHORT | 16 | 56.2 | 0.185 | 1.52 | 5 | 14.5 | 53.0 | 40.0 |
| 5m/RETEST/LONG | 1376 | 51.1 | 0.119 | 1.27 | 578 | 31.0 | 20.0 | 50.7 |
| 5m/RETEST/SHORT | 949 | 47.4 | 0.074 | 1.16 | 411 | 31.0 | 20.0 | 37.0 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 1720 | 23.1 | 0.006 | 1.01 | 1099 | 26.0 | 14.0 | 19.1 |
| B | 10551 | 47.0 | 0.057 | 1.12 | 4793 | 18.0 | 12.0 | 33.7 |
| C | 11733 | 48.5 | 0.048 | 1.1 | 5202 | 18.0 | 13.0 | 34.6 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 8843 | 48.9 | 0.09 | 1.19 | 3997 | 13.0 | 10.0 | 35.8 |
| London | 3483 | 45.8 | 0.034 | 1.07 | 1723 | 19.0 | 12.0 | 34.1 |
| NY | 4197 | 44.2 | 0.041 | 1.08 | 1954 | 26.0 | 17.0 | 34.7 |
| Sin KZ | 7481 | 43.6 | 0.01 | 1.02 | 3420 | 21.0 | 14.0 | 27.3 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 6278 | 45.1 | 0.059 | 1.12 | 2867 | 21.0 | 14.0 | 30.7 |
| edge=0 | 10059 | 48.5 | 0.05 | 1.11 | 4548 | 17.0 | 11.0 | 36.7 |
| edge=1 | 7667 | 43.4 | 0.04 | 1.08 | 3679 | 19.0 | 14.0 | 29.4 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 7 | 57.1 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| aligned=1 | 23997 | 46.0 | 0.049 | 1.1 | 11093 | 19.0 | 13.0 | 32.7 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 5 | 60.0 | 0.602 | 2.5 | 2 | 42.0 | 9.5 | 50.0 |
| INV/LONG|edge=0 | 122 | 56.6 | 0.156 | 1.42 | 42 | 14.0 | 11.0 | 26.2 |
| INV/LONG|edge=1 | 185 | 45.9 | 0.138 | 1.32 | 75 | 16.0 | 15.0 | 18.7 |
| INV/SHORT|edge=-1 | 172 | 40.7 | -0.017 | 0.97 | 78 | 22.0 | 14.0 | 19.2 |
| INV/SHORT|edge=0 | 107 | 50.5 | 0.101 | 1.24 | 40 | 13.0 | 14.75 | 30.0 |
| INV/SHORT|edge=1 | 9 | 66.7 | 0.69 | 3.07 | 3 | 28.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 579 | 54.1 | 0.196 | 1.48 | 228 | 15.0 | 11.0 | 42.1 |
| RETEST/LONG|edge=0 | 5955 | 48.8 | 0.035 | 1.07 | 2724 | 16.0 | 11.0 | 36.5 |
| RETEST/LONG|edge=1 | 7244 | 43.2 | 0.039 | 1.08 | 3500 | 19.0 | 14.0 | 29.2 |
| RETEST/SHORT|edge=-1 | 5522 | 44.3 | 0.046 | 1.09 | 2559 | 21.0 | 14.0 | 30.1 |
| RETEST/SHORT|edge=0 | 3875 | 47.7 | 0.069 | 1.15 | 1742 | 18.0 | 11.0 | 37.3 |
| RETEST/SHORT|edge=1 | 229 | 49.8 | -0.023 | 0.95 | 101 | 12.0 | 9.0 | 43.6 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 95 | 45.3 | 0.219 | 1.49 | 41 | 15.0 | 15.0 | 12.2 |
| INV/LONG|tier=C | 217 | 52.5 | 0.123 | 1.32 | 78 | 16.0 | 12.75 | 26.9 |
| INV/SHORT|tier=B | 97 | 42.3 | -0.042 | 0.92 | 46 | 18.0 | 12.0 | 6.5 |
| INV/SHORT|tier=C | 191 | 46.6 | 0.097 | 1.23 | 75 | 20.0 | 20.0 | 32.0 |
| RETEST/LONG|tier=A+ | 1029 | 22.1 | -0.028 | 0.96 | 683 | 24.0 | 12.0 | 18.9 |
| RETEST/LONG|tier=B | 5951 | 46.7 | 0.067 | 1.14 | 2728 | 17.0 | 12.0 | 33.9 |
| RETEST/LONG|tier=C | 6798 | 49.1 | 0.034 | 1.07 | 3041 | 17.0 | 13.0 | 34.8 |
| RETEST/SHORT|tier=A+ | 691 | 24.7 | 0.06 | 1.09 | 416 | 28.0 | 15.0 | 19.5 |
| RETEST/SHORT|tier=B | 4408 | 47.5 | 0.043 | 1.09 | 1978 | 19.0 | 13.0 | 34.5 |
| RETEST/SHORT|tier=C | 4527 | 47.4 | 0.064 | 1.14 | 2008 | 19.0 | 12.0 | 34.9 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 312 | 50.3 | 0.153 | 1.38 | 119 | 16.0 | 14.0 | 21.8 |
| INV/SHORT|aligned=1 | 288 | 45.1 | 0.049 | 1.11 | 121 | 20.0 | 14.0 | 22.3 |
| RETEST/LONG|aligned=0 | 7 | 57.1 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| RETEST/LONG|aligned=1 | 13771 | 46.1 | 0.044 | 1.09 | 6451 | 18.0 | 12.0 | 32.7 |
| RETEST/SHORT|aligned=1 | 9626 | 45.8 | 0.054 | 1.11 | 4402 | 20.0 | 13.0 | 33.2 |

## Autopsia de SL
n_losses=11094  causas: RR-bajo×4113, contra-estructura×3659, stop-en-el-minimo×3628, killzone-Asia-largo×2406, sin-nivel-detras×2007, estirado×1869, chop×1655, SL-muy-pegado×1391, sin-causa-clara×1236, contra-sesgo×1
- INV/LONG (n=119): killzone-Asia-largo×54, RR-bajo×49, contra-estructura×37, stop-en-el-minimo×26, estirado×26, chop×18, sin-nivel-detras×16, SL-muy-pegado×11, sin-causa-clara×5
- INV/SHORT (n=121): RR-bajo×58, contra-estructura×36, estirado×28, stop-en-el-minimo×27, sin-causa-clara×20, SL-muy-pegado×16, chop×11, sin-nivel-detras×10
- RETEST/LONG (n=6452): RR-bajo×2396, killzone-Asia-largo×2352, contra-estructura×2206, stop-en-el-minimo×2112, sin-nivel-detras×1205, estirado×1073, chop×1024, SL-muy-pegado×770, sin-causa-clara×574, contra-sesgo×1
- RETEST/SHORT (n=4402): RR-bajo×1610, stop-en-el-minimo×1463, contra-estructura×1380, sin-nivel-detras×776, estirado×742, sin-causa-clara×637, chop×602, SL-muy-pegado×594

## Autopsia de SL · semana 2026-W41 (para revision semanal)
n_losses=759  causas: RR-bajo×275, contra-estructura×238, killzone-Asia-largo×235, stop-en-el-minimo×229, sin-nivel-detras×187, estirado×115, SL-muy-pegado×101, chop×96, sin-causa-clara×71
ejemplos por causa: {"RR-bajo": ["CL-2-24585-L", "GC-1-28794-S", "GC-2-25017-S", "YM-1-26811-L", "YM-1-27118-L"], "contra-estructura": ["CL-1-28001-S", "GC-1-28794-S", "CL-2-24913-L", "GC-2-25014-S", "GC-2-25017-S"], "killzone-Asia-largo": ["NQ-1-27553-L", "CL-2-24895-L", "CL-2-24913-L", "YM-1-26788-L", "YM-1-26794-L"]}

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
    "n": 22974,
    "naive_expR": 0.049,
    "managed_expR": 0.127,
    "delta": 0.078,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 46.2,
    "fill_full_pct": 32.5,
    "m1_rate": 37.4,
    "m2_rate": 22.8,
    "m3_rate": 12.0,
    "beAfterM1_rate": 18.2
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 200,
      "naive_expR": 0.162,
      "managed_expR": 0.251,
      "delta": 0.089,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 49.5,
      "fill_full_pct": 37.0,
      "m1_rate": 41.0,
      "m2_rate": 24.5,
      "m3_rate": 12.5,
      "beAfterM1_rate": 21.0
    },
    "1m/INV/SHORT": {
      "n": 181,
      "naive_expR": 0.004,
      "managed_expR": 0.181,
      "delta": 0.176,
      "avgEntryBetterTk_p50": 3.3,
      "fill_t3plus_pct": 50.8,
      "fill_full_pct": 38.7,
      "m1_rate": 35.9,
      "m2_rate": 22.1,
      "m3_rate": 12.2,
      "beAfterM1_rate": 16.0
    },
    "1m/RETEST/LONG": {
      "n": 8304,
      "naive_expR": 0.038,
      "managed_expR": 0.129,
      "delta": 0.091,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 48.2,
      "fill_full_pct": 34.0,
      "m1_rate": 37.7,
      "m2_rate": 22.6,
      "m3_rate": 11.7,
      "beAfterM1_rate": 17.7
    },
    "1m/RETEST/SHORT": {
      "n": 5745,
      "naive_expR": 0.04,
      "managed_expR": 0.162,
      "delta": 0.121,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 47.9,
      "fill_full_pct": 33.2,
      "m1_rate": 38.8,
      "m2_rate": 24.3,
      "m3_rate": 13.2,
      "beAfterM1_rate": 18.1
    },
    "2m/INV/LONG": {
      "n": 73,
      "naive_expR": 0.049,
      "managed_expR": 0.046,
      "delta": -0.003,
      "avgEntryBetterTk_p50": 3.8,
      "fill_t3plus_pct": 54.8,
      "fill_full_pct": 39.7,
      "m1_rate": 24.7,
      "m2_rate": 16.4,
      "m3_rate": 5.5,
      "beAfterM1_rate": 11.0
    },
    "2m/INV/SHORT": {
      "n": 77,
      "naive_expR": 0.129,
      "managed_expR": 0.141,
      "delta": 0.012,
      "avgEntryBetterTk_p50": 2.4,
      "fill_t3plus_pct": 48.1,
      "fill_full_pct": 36.4,
      "m1_rate": 32.5,
      "m2_rate": 22.1,
      "m3_rate": 14.3,
      "beAfterM1_rate": 14.3
    },
    "2m/RETEST/LONG": {
      "n": 3680,
      "naive_expR": 0.031,
      "managed_expR": 0.071,
      "delta": 0.04,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 45.2,
      "fill_full_pct": 31.7,
      "m1_rate": 35.5,
      "m2_rate": 20.9,
      "m3_rate": 10.8,
      "beAfterM1_rate": 18.2
    },
    "2m/RETEST/SHORT": {
      "n": 2501,
      "naive_expR": 0.078,
      "managed_expR": 0.139,
      "delta": 0.061,
      "avgEntryBetterTk_p50": 3.0,
      "fill_t3plus_pct": 44.2,
      "fill_full_pct": 31.2,
      "m1_rate": 37.6,
      "m2_rate": 23.3,
      "m3_rate": 12.4,
      "beAfterM1_rate": 19.6
    },
    "5m/INV/LONG": {
      "n": 23,
      "naive_expR": 0.408,
      "managed_expR": 0.469,
      "delta": 0.06,
      "avgEntryBetterTk_p50": 1.3,
      "fill_t3plus_pct": 34.8,
      "fill_full_pct": 21.7,
      "m1_rate": 13.0,
      "m2_rate": 8.7,
      "m3_rate": 4.3,
      "beAfterM1_rate": 8.7
    },
    "5m/INV/SHORT": {
      "n": 14,
      "naive_expR": 0.185,
      "managed_expR": 0.251,
      "delta": 0.066,
      "avgEntryBetterTk_p50": 8.4,
      "fill_t3plus_pct": 64.3,
      "fill_full_pct": 42.9,
      "m1_rate": 21.4,
      "m2_rate": 14.3,
      "m3_rate": 14.3,
      "beAfterM1_rate": 7.1
    },
    "5m/RETEST/LONG": {
      "n": 1299,
      "naive_expR": 0.119,
      "managed_expR": 0.093,
      "delta": -0.026,
      "avgEntryBetterTk_p50": 1.9,
      "fill_t3plus_pct": 34.2,
      "fill_full_pct": 24.6,
      "m1_rate": 36.1,
      "m2_rate": 22.6,
      "m3_rate": 11.8,
      "beAfterM1_rate": 19.6
    },
    "5m/RETEST/SHORT": {
      "n": 877,
      "naive_expR": 0.073,
      "managed_expR": 0.084,
      "delta": 0.011,
      "avgEntryBetterTk_p50": 4.9,
      "fill_t3plus_pct": 41.3,
      "fill_full_pct": 29.0,
      "m1_rate": 36.1,
      "m2_rate": 21.8,
      "m3_rate": 11.2,
      "beAfterM1_rate": 18.9
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 20480,
    "layer_expR": 0.049,
    "orig_expR": 0.17,
    "delta_orig_minus_layer": 0.122,
    "delta_ci90": [
      0.095,
      0.149
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 47.9,
    "orig_wrTP1": 33.0,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 9.0,
    "orig_wider_pct": 3.8,
    "orig_saved_from_SL": 27,
    "orig_caused_SL": 3076
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 3,
  "invalid_by_seg": {
    "1m/RETEST/LONG": 3
  },
  "by_basis": {
    "candle1": {
      "n": 556,
      "layer_expR": 0.103,
      "orig_expR": 0.106,
      "delta_orig_minus_layer": 0.004,
      "delta_ci90": [
        -0.171,
        0.198
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.2,
      "orig_wrTP1": 26.3,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 4.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 134
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
      "n": 15074,
      "layer_expR": 0.049,
      "orig_expR": 0.18,
      "delta_orig_minus_layer": 0.131,
      "delta_ci90": [
        0.1,
        0.163
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.1,
      "orig_wrTP1": 33.4,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 4.3,
      "orig_saved_from_SL": 26,
      "orig_caused_SL": 2239
    },
    "retestBar2": {
      "n": 4850,
      "layer_expR": 0.043,
      "orig_expR": 0.149,
      "delta_orig_minus_layer": 0.106,
      "delta_ci90": [
        0.053,
        0.16
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.9,
      "orig_wrTP1": 32.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 703
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 200,
      "layer_expR": 0.162,
      "orig_expR": 0.156,
      "delta_orig_minus_layer": -0.005,
      "delta_ci90": [
        -0.273,
        0.288
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.0,
      "orig_wrTP1": 23.5,
      "slTk_p50": 16.5,
      "slOrigTk_p50": 3.5,
      "orig_wider_pct": 4.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 51
    },
    "1m/INV/SHORT": {
      "n": 171,
      "layer_expR": 0.002,
      "orig_expR": -0.102,
      "delta_orig_minus_layer": -0.103,
      "delta_ci90": [
        -0.357,
        0.161
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 46.8,
      "orig_wrTP1": 23.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 1.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 40
    },
    "1m/RETEST/LONG": {
      "n": 7248,
      "layer_expR": 0.035,
      "orig_expR": 0.137,
      "delta_orig_minus_layer": 0.101,
      "delta_ci90": [
        0.058,
        0.148
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.9,
      "orig_wrTP1": 28.8,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 1.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 1235
    },
    "1m/RETEST/SHORT": {
      "n": 4966,
      "layer_expR": 0.04,
      "orig_expR": 0.145,
      "delta_orig_minus_layer": 0.105,
      "delta_ci90": [
        0.051,
        0.158
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.8,
      "orig_wrTP1": 32.3,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 721
    },
    "2m/INV/LONG": {
      "n": 73,
      "layer_expR": 0.049,
      "orig_expR": 0.596,
      "delta_orig_minus_layer": 0.547,
      "delta_ci90": [
        -0.212,
        1.456
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 54.8,
      "orig_wrTP1": 28.8,
      "slTk_p50": 26.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 6.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 19
    },
    "2m/INV/SHORT": {
      "n": 76,
      "layer_expR": 0.126,
      "orig_expR": 0.227,
      "delta_orig_minus_layer": 0.101,
      "delta_ci90": [
        -0.314,
        0.559
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 44.7,
      "orig_wrTP1": 31.6,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 6.5,
      "orig_wider_pct": 2.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 11
    },
    "2m/RETEST/LONG": {
      "n": 3395,
      "layer_expR": 0.029,
      "orig_expR": 0.178,
      "delta_orig_minus_layer": 0.149,
      "delta_ci90": [
        0.093,
        0.206
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.8,
      "orig_wrTP1": 35.0,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.6,
      "orig_saved_from_SL": 4,
      "orig_caused_SL": 472
    },
    "2m/RETEST/SHORT": {
      "n": 2237,
      "layer_expR": 0.087,
      "orig_expR": 0.199,
      "delta_orig_minus_layer": 0.112,
      "delta_ci90": [
        0.046,
        0.183
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.0,
      "orig_wrTP1": 35.7,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.9,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 323
    },
    "5m/INV/LONG": {
      "n": 23,
      "layer_expR": 0.408,
      "orig_expR": -0.423,
      "delta_orig_minus_layer": -0.832,
      "delta_ci90": [
        -1.216,
        -0.476
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 82.6,
      "orig_wrTP1": 39.1,
      "slTk_p50": 31.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 13.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 10
    },
    "5m/INV/SHORT": {
      "n": 13,
      "layer_expR": 0.159,
      "orig_expR": -0.437,
      "delta_orig_minus_layer": -0.596,
      "delta_ci90": [
        -0.944,
        -0.253
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 61.5,
      "orig_wrTP1": 38.5,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 23.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 3
    },
    "5m/RETEST/LONG": {
      "n": 1253,
      "layer_expR": 0.111,
      "orig_expR": 0.302,
      "delta_orig_minus_layer": 0.192,
      "delta_ci90": [
        0.095,
        0.29
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.1,
      "orig_wrTP1": 45.1,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 19.0,
      "orig_wider_pct": 15.5,
      "orig_saved_from_SL": 10,
      "orig_caused_SL": 123
    },
    "5m/RETEST/SHORT": {
      "n": 825,
      "layer_expR": 0.069,
      "orig_expR": 0.352,
      "delta_orig_minus_layer": 0.283,
      "delta_ci90": [
        0.098,
        0.493
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.9,
      "orig_wrTP1": 43.6,
      "slTk_p50": 30.0,
      "slOrigTk_p50": 22.0,
      "orig_wider_pct": 19.8,
      "orig_saved_from_SL": 8,
      "orig_caused_SL": 68
    }
  },
  "since_change": {
    "changeDate": "2026-09-26",
    "n": 6204,
    "by_tf_kind_side": {
      "1m/INV/LONG": {
        "n": 57,
        "layer_expR": 0.178,
        "orig_expR": 0.545,
        "delta_orig_minus_layer": 0.367,
        "delta_ci90": [
          -0.209,
          1.025
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 52.6,
        "orig_wrTP1": 26.3,
        "slTk_p50": 18.0,
        "slOrigTk_p50": 3.0,
        "orig_wider_pct": 3.5,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 15
      },
      "1m/INV/SHORT": {
        "n": 59,
        "layer_expR": -0.047,
        "orig_expR": -0.307,
        "delta_orig_minus_layer": -0.261,
        "delta_ci90": [
          -0.559,
          0.039
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 40.7,
        "orig_wrTP1": 20.3,
        "slTk_p50": 17.0,
        "slOrigTk_p50": 4.0,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 12
      },
      "1m/RETEST/LONG": {
        "n": 2028,
        "layer_expR": -0.047,
        "orig_expR": -0.05,
        "delta_orig_minus_layer": -0.003,
        "delta_ci90": [
          -0.071,
          0.065
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 44.1,
        "orig_wrTP1": 26.8,
        "slTk_p50": 18.0,
        "slOrigTk_p50": 7.0,
        "orig_wider_pct": 1.2,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 351
      },
      "1m/RETEST/SHORT": {
        "n": 1602,
        "layer_expR": 0.052,
        "orig_expR": 0.101,
        "delta_orig_minus_layer": 0.049,
        "delta_ci90": [
          -0.023,
          0.122
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 47.6,
        "orig_wrTP1": 32.5,
        "slTk_p50": 19.0,
        "slOrigTk_p50": 9.0,
        "orig_wider_pct": 2.1,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 241
      },
      "2m/INV/LONG": {
        "n": 16,
        "layer_expR": 0.199,
        "orig_expR": -0.227,
        "delta_orig_minus_layer": -0.426,
        "delta_ci90": [
          -1.003,
          0.193
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 68.8,
        "orig_wrTP1": 31.2,
        "slTk_p50": 31.5,
        "slOrigTk_p50": 10.0,
        "orig_wider_pct": 6.2,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 6
      },
      "2m/INV/SHORT": {
        "n": 22,
        "layer_expR": 0.189,
        "orig_expR": 0.224,
        "delta_orig_minus_layer": 0.035,
        "delta_ci90": [
          -0.954,
          1.108
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 54.5,
        "orig_wrTP1": 31.8,
        "slTk_p50": 23.0,
        "slOrigTk_p50": 6.0,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 5
      },
      "2m/RETEST/LONG": {
        "n": 1007,
        "layer_expR": -0.019,
        "orig_expR": 0.118,
        "delta_orig_minus_layer": 0.138,
        "delta_ci90": [
          0.039,
          0.241
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 48.1,
        "orig_wrTP1": 32.3,
        "slTk_p50": 22.0,
        "slOrigTk_p50": 10.0,
        "orig_wider_pct": 4.5,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 160
      },
      "2m/RETEST/SHORT": {
        "n": 741,
        "layer_expR": 0.112,
        "orig_expR": 0.128,
        "delta_orig_minus_layer": 0.017,
        "delta_ci90": [
          -0.082,
          0.121
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 48.9,
        "orig_wrTP1": 33.6,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 3.6,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 114
      },
      "5m/INV/LONG": {
        "n": 8,
        "layer_expR": 0.219,
        "orig_expR": -0.372,
        "delta_orig_minus_layer": -0.591,
        "delta_ci90": [
          -1.057,
          -0.166
        ],
        "delta_beats_zero": false,
        "delta_below_zero": true,
        "layer_wrTP1": 87.5,
        "orig_wrTP1": 50.0,
        "slTk_p50": 26.5,
        "slOrigTk_p50": 13.5,
        "orig_wider_pct": 12.5,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 3
      },
      "5m/RETEST/LONG": {
        "n": 378,
        "layer_expR": 0.069,
        "orig_expR": 0.119,
        "delta_orig_minus_layer": 0.05,
        "delta_ci90": [
          -0.044,
          0.145
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 54.0,
        "orig_wrTP1": 45.8,
        "slTk_p50": 30.0,
        "slOrigTk_p50": 19.0,
        "orig_wider_pct": 14.0,
        "orig_saved_from_SL": 4,
        "orig_caused_SL": 35
      },
      "5m/RETEST/SHORT": {
        "n": 283,
        "layer_expR": -0.005,
        "orig_expR": 0.071,
        "delta_orig_minus_layer": 0.075,
        "delta_ci90": [
          -0.025,
          0.177
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 49.5,
        "orig_wrTP1": 43.5,
        "slTk_p50": 30.0,
        "slOrigTk_p50": 20.0,
        "orig_wider_pct": 16.6,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 19
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
      "n": 8279,
      "wrTP1": 46.5,
      "nSL": 3884,
      "nTO": 542,
      "expR": 0.029,
      "pf": 1.06,
      "mfe_p25": 6.0,
      "mfe_p50": 15.0,
      "mfe_p75": 35.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 29.1,
      "ci90": {
        "expR": 0.029,
        "ci90": [
          0.008,
          0.051
        ],
        "p_mean_le_0": 0.015,
        "n": 8013
      }
    },
    "cuts": {
      "1.0": {
        "n": 4063,
        "wrTP1": 30.1,
        "nSL": 2443,
        "nTO": 397,
        "expR": 0.007,
        "pf": 1.01,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 20.9,
        "ci90": {
          "expR": 0.007,
          "ci90": [
            -0.031,
            0.043
          ],
          "p_mean_le_0": 0.391,
          "n": 3905
        }
      },
      "1.2": {
        "n": 3352,
        "wrTP1": 27.5,
        "nSL": 2071,
        "nTO": 360,
        "expR": 0.017,
        "pf": 1.03,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 18.3,
        "ci90": {
          "expR": 0.017,
          "ci90": [
            -0.026,
            0.062
          ],
          "p_mean_le_0": 0.251,
          "n": 3218
        }
      },
      "1.3": {
        "n": 3038,
        "wrTP1": 25.9,
        "nSL": 1906,
        "nTO": 344,
        "expR": 0.015,
        "pf": 1.02,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.300000000000068,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 16.8,
        "ci90": {
          "expR": 0.015,
          "ci90": [
            -0.033,
            0.062
          ],
          "p_mean_le_0": 0.3,
          "n": 2908
        }
      },
      "1.5": {
        "n": 2558,
        "wrTP1": 23.2,
        "nSL": 1655,
        "nTO": 310,
        "expR": 0.004,
        "pf": 1.01,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 14.4,
        "ci90": {
          "expR": 0.004,
          "ci90": [
            -0.049,
            0.058
          ],
          "p_mean_le_0": 0.438,
          "n": 2449
        }
      },
      "2.0": {
        "n": 1658,
        "wrTP1": 17.4,
        "nSL": 1121,
        "nTO": 249,
        "expR": -0.006,
        "pf": 0.99,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 19.30000000000001,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 10.9,
        "ci90": {
          "expR": -0.006,
          "ci90": [
            -0.075,
            0.069
          ],
          "p_mean_le_0": 0.552,
          "n": 1587
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 5817,
      "wrTP1": 46.7,
      "nSL": 2628,
      "nTO": 473,
      "expR": 0.05,
      "pf": 1.1,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 31.8,
      "ci90": {
        "expR": 0.05,
        "ci90": [
          0.025,
          0.076
        ],
        "p_mean_le_0": 0.001,
        "n": 5514
      }
    },
    "cuts": {
      "1.0": {
        "n": 2798,
        "wrTP1": 31.0,
        "nSL": 1599,
        "nTO": 331,
        "expR": 0.058,
        "pf": 1.09,
        "mfe_p25": 11.0,
        "mfe_p50": 23.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 22.6,
        "ci90": {
          "expR": 0.058,
          "ci90": [
            0.012,
            0.106
          ],
          "p_mean_le_0": 0.021,
          "n": 2610
        }
      },
      "1.2": {
        "n": 2302,
        "wrTP1": 28.3,
        "nSL": 1345,
        "nTO": 305,
        "expR": 0.075,
        "pf": 1.12,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 20.3,
        "ci90": {
          "expR": 0.075,
          "ci90": [
            0.021,
            0.129
          ],
          "p_mean_le_0": 0.013,
          "n": 2136
        }
      },
      "1.3": {
        "n": 2110,
        "wrTP1": 26.9,
        "nSL": 1246,
        "nTO": 297,
        "expR": 0.077,
        "pf": 1.12,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 20.400000000000034,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 19.2,
        "ci90": {
          "expR": 0.077,
          "ci90": [
            0.022,
            0.138
          ],
          "p_mean_le_0": 0.013,
          "n": 1952
        }
      },
      "1.5": {
        "n": 1802,
        "wrTP1": 24.8,
        "nSL": 1092,
        "nTO": 264,
        "expR": 0.078,
        "pf": 1.12,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 17.0,
        "ci90": {
          "expR": 0.078,
          "ci90": [
            0.009,
            0.144
          ],
          "p_mean_le_0": 0.029,
          "n": 1669
        }
      },
      "2.0": {
        "n": 1214,
        "wrTP1": 20.0,
        "nSL": 768,
        "nTO": 203,
        "expR": 0.078,
        "pf": 1.11,
        "mfe_p25": 11.0,
        "mfe_p50": 26.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 23.600000000000023,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 12.6,
        "ci90": {
          "expR": 0.078,
          "ci90": [
            -0.009,
            0.165
          ],
          "p_mean_le_0": 0.071,
          "n": 1123
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 3716,
      "wrTP1": 48.1,
      "nSL": 1732,
      "nTO": 195,
      "expR": 0.019,
      "pf": 1.04,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 28.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 39.7,
      "ci90": {
        "expR": 0.019,
        "ci90": [
          -0.012,
          0.05
        ],
        "p_mean_le_0": 0.167,
        "n": 3581
      }
    },
    "cuts": {
      "1.0": {
        "n": 1681,
        "wrTP1": 30.8,
        "nSL": 1024,
        "nTO": 139,
        "expR": -0.004,
        "pf": 0.99,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 32.0,
        "ci90": {
          "expR": -0.004,
          "ci90": [
            -0.063,
            0.059
          ],
          "p_mean_le_0": 0.549,
          "n": 1596
        }
      },
      "1.2": {
        "n": 1378,
        "wrTP1": 27.4,
        "nSL": 879,
        "nTO": 121,
        "expR": -0.019,
        "pf": 0.97,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 21.30000000000001,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 30.0,
        "ci90": {
          "expR": -0.019,
          "ci90": [
            -0.087,
            0.05
          ],
          "p_mean_le_0": 0.651,
          "n": 1306
        }
      },
      "1.3": {
        "n": 1254,
        "wrTP1": 26.5,
        "nSL": 806,
        "nTO": 116,
        "expR": -0.008,
        "pf": 0.99,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.5,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.0,
        "ci90": {
          "expR": -0.008,
          "ci90": [
            -0.086,
            0.065
          ],
          "p_mean_le_0": 0.592,
          "n": 1187
        }
      },
      "1.5": {
        "n": 1026,
        "wrTP1": 22.6,
        "nSL": 684,
        "nTO": 110,
        "expR": -0.035,
        "pf": 0.95,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 26.8,
        "ci90": {
          "expR": -0.035,
          "ci90": [
            -0.126,
            0.055
          ],
          "p_mean_le_0": 0.742,
          "n": 964
        }
      },
      "2.0": {
        "n": 639,
        "wrTP1": 18.3,
        "nSL": 439,
        "nTO": 83,
        "expR": 0.005,
        "pf": 1.01,
        "mfe_p25": 11.25,
        "mfe_p50": 26.0,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 21.4,
        "ci90": {
          "expR": 0.005,
          "ci90": [
            -0.118,
            0.128
          ],
          "p_mean_le_0": 0.484,
          "n": 594
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 2466,
      "wrTP1": 50.4,
      "nSL": 1087,
      "nTO": 137,
      "expR": 0.092,
      "pf": 1.2,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 45.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 43.7,
      "ci90": {
        "expR": 0.092,
        "ci90": [
          0.054,
          0.133
        ],
        "p_mean_le_0": 0.0,
        "n": 2383
      }
    },
    "cuts": {
      "1.0": {
        "n": 1144,
        "wrTP1": 34.2,
        "nSL": 662,
        "nTO": 91,
        "expR": 0.114,
        "pf": 1.19,
        "mfe_p25": 16.0,
        "mfe_p50": 31.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 35.5,
        "ci90": {
          "expR": 0.114,
          "ci90": [
            0.042,
            0.19
          ],
          "p_mean_le_0": 0.004,
          "n": 1100
        }
      },
      "1.2": {
        "n": 941,
        "wrTP1": 30.7,
        "nSL": 568,
        "nTO": 84,
        "expR": 0.111,
        "pf": 1.18,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 32.0,
        "ci90": {
          "expR": 0.111,
          "ci90": [
            0.023,
            0.199
          ],
          "p_mean_le_0": 0.021,
          "n": 902
        }
      },
      "1.3": {
        "n": 858,
        "wrTP1": 29.0,
        "nSL": 528,
        "nTO": 81,
        "expR": 0.103,
        "pf": 1.16,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 31.1,
        "ci90": {
          "expR": 0.103,
          "ci90": [
            0.009,
            0.199
          ],
          "p_mean_le_0": 0.036,
          "n": 821
        }
      },
      "1.5": {
        "n": 717,
        "wrTP1": 25.7,
        "nSL": 459,
        "nTO": 74,
        "expR": 0.087,
        "pf": 1.13,
        "mfe_p25": 17.0,
        "mfe_p50": 33.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 29.8,
        "ci90": {
          "expR": 0.087,
          "ci90": [
            -0.023,
            0.189
          ],
          "p_mean_le_0": 0.089,
          "n": 686
        }
      },
      "2.0": {
        "n": 475,
        "wrTP1": 21.7,
        "nSL": 312,
        "nTO": 60,
        "expR": 0.137,
        "pf": 1.2,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 74.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 25.6,
        "ci90": {
          "expR": 0.137,
          "ci90": [
            -0.006,
            0.279
          ],
          "p_mean_le_0": 0.058,
          "n": 453
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 1318,
      "wrTP1": 53.3,
      "nSL": 536,
      "nTO": 79,
      "expR": 0.138,
      "pf": 1.32,
      "mfe_p25": 12.0,
      "mfe_p50": 30.0,
      "mfe_p75": 66.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 42.0,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -36.0,
      "revAfterSL_rate": 54.7,
      "ci90": {
        "expR": 0.138,
        "ci90": [
          0.081,
          0.193
        ],
        "p_mean_le_0": 0.0,
        "n": 1248
      }
    },
    "cuts": {
      "1.0": {
        "n": 543,
        "wrTP1": 37.6,
        "nSL": 289,
        "nTO": 50,
        "expR": 0.244,
        "pf": 1.42,
        "mfe_p25": 17.0,
        "mfe_p50": 40.0,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 50.5,
        "ci90": {
          "expR": 0.244,
          "ci90": [
            0.128,
            0.358
          ],
          "p_mean_le_0": 0.0,
          "n": 502
        }
      },
      "1.2": {
        "n": 453,
        "wrTP1": 36.2,
        "nSL": 243,
        "nTO": 46,
        "expR": 0.293,
        "pf": 1.5,
        "mfe_p25": 17.0,
        "mfe_p50": 40.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 29.700000000000017,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 48.1,
        "ci90": {
          "expR": 0.293,
          "ci90": [
            0.158,
            0.426
          ],
          "p_mean_le_0": 0.0,
          "n": 416
        }
      },
      "1.3": {
        "n": 409,
        "wrTP1": 33.3,
        "nSL": 232,
        "nTO": 41,
        "expR": 0.251,
        "pf": 1.41,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.0,
        "revAfterSL_rate": 47.0,
        "ci90": {
          "expR": 0.251,
          "ci90": [
            0.106,
            0.392
          ],
          "p_mean_le_0": 0.002,
          "n": 377
        }
      },
      "1.5": {
        "n": 342,
        "wrTP1": 31.0,
        "nSL": 199,
        "nTO": 37,
        "expR": 0.262,
        "pf": 1.41,
        "mfe_p25": 18.0,
        "mfe_p50": 37.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 24.5,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.0,
        "revAfterSL_rate": 45.7,
        "ci90": {
          "expR": 0.262,
          "ci90": [
            0.097,
            0.428
          ],
          "p_mean_le_0": 0.002,
          "n": 313
        }
      },
      "2.0": {
        "n": 217,
        "wrTP1": 24.9,
        "nSL": 135,
        "nTO": 28,
        "expR": 0.255,
        "pf": 1.37,
        "mfe_p25": 17.0,
        "mfe_p50": 41.0,
        "mfe_p75": 99.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 20.400000000000006,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -34.0,
        "revAfterSL_rate": 37.8,
        "ci90": {
          "expR": 0.255,
          "ci90": [
            0.027,
            0.488
          ],
          "p_mean_le_0": 0.032,
          "n": 197
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 894,
      "wrTP1": 50.3,
      "nSL": 374,
      "nTO": 70,
      "expR": 0.101,
      "pf": 1.22,
      "mfe_p25": 14.0,
      "mfe_p50": 30.0,
      "mfe_p75": 57.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 38.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -28.0,
      "revAfterSL_rate": 40.4,
      "ci90": {
        "expR": 0.101,
        "ci90": [
          0.033,
          0.17
        ],
        "p_mean_le_0": 0.01,
        "n": 834
      }
    },
    "cuts": {
      "1.0": {
        "n": 390,
        "wrTP1": 33.6,
        "nSL": 218,
        "nTO": 41,
        "expR": 0.143,
        "pf": 1.23,
        "mfe_p25": 18.25,
        "mfe_p50": 40.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 37.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 33.0,
        "ci90": {
          "expR": 0.143,
          "ci90": [
            0.003,
            0.279
          ],
          "p_mean_le_0": 0.048,
          "n": 358
        }
      },
      "1.2": {
        "n": 316,
        "wrTP1": 31.0,
        "nSL": 183,
        "nTO": 35,
        "expR": 0.168,
        "pf": 1.26,
        "mfe_p25": 19.0,
        "mfe_p50": 41.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 33.599999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.5,
        "revAfterSL_rate": 29.0,
        "ci90": {
          "expR": 0.168,
          "ci90": [
            0.007,
            0.329
          ],
          "p_mean_le_0": 0.043,
          "n": 289
        }
      },
      "1.3": {
        "n": 292,
        "wrTP1": 31.2,
        "nSL": 170,
        "nTO": 31,
        "expR": 0.179,
        "pf": 1.28,
        "mfe_p25": 21.0,
        "mfe_p50": 42.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 35.0,
        "loserMFEbeforeSL_p50": 6.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.5,
        "revAfterSL_rate": 28.2,
        "ci90": {
          "expR": 0.179,
          "ci90": [
            0.015,
            0.356
          ],
          "p_mean_le_0": 0.037,
          "n": 269
        }
      },
      "1.5": {
        "n": 239,
        "wrTP1": 29.3,
        "nSL": 139,
        "nTO": 30,
        "expR": 0.207,
        "pf": 1.32,
        "mfe_p25": 22.0,
        "mfe_p50": 45.0,
        "mfe_p75": 76.0,
        "winnerMAE_p75": 20.75,
        "winnerMAE_p90": 33.2,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 25.2,
        "ci90": {
          "expR": 0.207,
          "ci90": [
            0.008,
            0.405
          ],
          "p_mean_le_0": 0.042,
          "n": 217
        }
      },
      "2.0": {
        "n": 151,
        "wrTP1": 21.9,
        "nSL": 99,
        "nTO": 19,
        "expR": 0.135,
        "pf": 1.19,
        "mfe_p25": 25.5,
        "mfe_p50": 49.0,
        "mfe_p75": 89.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 39.400000000000006,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 23.2,
        "ci90": {
          "expR": 0.135,
          "ci90": [
            -0.131,
            0.408
          ],
          "p_mean_le_0": 0.216,
          "n": 139
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
    "2026-W40",
    "2026-W41"
  ],
  "1/RETEST/LONG": {
    "baseline": {
      "n": 2270,
      "wrTP1": 44.0,
      "nSL": 1131,
      "nTO": 141,
      "expR": -0.051,
      "pf": 0.9,
      "mfe_p25": 6.0,
      "mfe_p50": 15.0,
      "mfe_p75": 35.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.300000000000068,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 26.1,
      "ci90": {
        "expR": -0.051,
        "ci90": [
          -0.089,
          -0.013
        ],
        "p_mean_le_0": 0.985,
        "n": 2212
      }
    },
    "cuts": {
      "1.2": {
        "n": 906,
        "wrTP1": 25.1,
        "nSL": 596,
        "nTO": 83,
        "expR": -0.111,
        "pf": 0.84,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 11.5,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 16.6,
        "ci90": {
          "expR": -0.111,
          "ci90": [
            -0.193,
            -0.028
          ],
          "p_mean_le_0": 0.988,
          "n": 886
        }
      },
      "1.3": {
        "n": 801,
        "wrTP1": 24.5,
        "nSL": 530,
        "nTO": 75,
        "expR": -0.093,
        "pf": 0.87,
        "mfe_p25": 8.0,
        "mfe_p50": 19.5,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 24.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 14.3,
        "ci90": {
          "expR": -0.093,
          "ci90": [
            -0.174,
            -0.003
          ],
          "p_mean_le_0": 0.957,
          "n": 782
        }
      },
      "1.5": {
        "n": 668,
        "wrTP1": 20.1,
        "nSL": 467,
        "nTO": 67,
        "expR": -0.156,
        "pf": 0.78,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 24.700000000000003,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 12.4,
        "ci90": {
          "expR": -0.156,
          "ci90": [
            -0.253,
            -0.055
          ],
          "p_mean_le_0": 0.996,
          "n": 653
        }
      },
      "2.0": {
        "n": 443,
        "wrTP1": 14.9,
        "nSL": 325,
        "nTO": 52,
        "expR": -0.2,
        "pf": 0.74,
        "mfe_p25": 7.0,
        "mfe_p50": 19.0,
        "mfe_p75": 44.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 9.2,
        "ci90": {
          "expR": -0.2,
          "ci90": [
            -0.327,
            -0.069
          ],
          "p_mean_le_0": 0.994,
          "n": 431
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 1765,
      "wrTP1": 47.1,
      "nSL": 820,
      "nTO": 114,
      "expR": 0.045,
      "pf": 1.09,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 34.5,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 29.5,
      "ci90": {
        "expR": 0.045,
        "ci90": [
          -0.001,
          0.094
        ],
        "p_mean_le_0": 0.057,
        "n": 1699
      }
    },
    "cuts": {
      "1.2": {
        "n": 712,
        "wrTP1": 27.8,
        "nSL": 435,
        "nTO": 79,
        "expR": 0.024,
        "pf": 1.04,
        "mfe_p25": 10.0,
        "mfe_p50": 22.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 21.600000000000023,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 20.7,
        "ci90": {
          "expR": 0.024,
          "ci90": [
            -0.073,
            0.121
          ],
          "p_mean_le_0": 0.354,
          "n": 678
        }
      },
      "1.3": {
        "n": 657,
        "wrTP1": 26.8,
        "nSL": 404,
        "nTO": 77,
        "expR": 0.03,
        "pf": 1.05,
        "mfe_p25": 10.0,
        "mfe_p50": 22.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 19.1,
        "ci90": {
          "expR": 0.03,
          "ci90": [
            -0.074,
            0.128
          ],
          "p_mean_le_0": 0.319,
          "n": 625
        }
      },
      "1.5": {
        "n": 563,
        "wrTP1": 24.7,
        "nSL": 354,
        "nTO": 70,
        "expR": 0.028,
        "pf": 1.04,
        "mfe_p25": 10.0,
        "mfe_p50": 22.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 21.60000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 16.7,
        "ci90": {
          "expR": 0.028,
          "ci90": [
            -0.085,
            0.144
          ],
          "p_mean_le_0": 0.331,
          "n": 537
        }
      },
      "2.0": {
        "n": 379,
        "wrTP1": 18.7,
        "nSL": 253,
        "nTO": 55,
        "expR": -0.012,
        "pf": 0.98,
        "mfe_p25": 10.0,
        "mfe_p50": 21.5,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 14.5,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 11.5,
        "ci90": {
          "expR": -0.012,
          "ci90": [
            -0.157,
            0.132
          ],
          "p_mean_le_0": 0.578,
          "n": 362
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 1071,
      "wrTP1": 47.9,
      "nSL": 519,
      "nTO": 39,
      "expR": -0.024,
      "pf": 0.95,
      "mfe_p25": 10.0,
      "mfe_p50": 23.0,
      "mfe_p75": 50.25,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 31.80000000000001,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 42.2,
      "ci90": {
        "expR": -0.024,
        "ci90": [
          -0.076,
          0.032
        ],
        "p_mean_le_0": 0.752,
        "n": 1048
      }
    },
    "cuts": {
      "1.2": {
        "n": 404,
        "wrTP1": 25.7,
        "nSL": 274,
        "nTO": 26,
        "expR": -0.174,
        "pf": 0.75,
        "mfe_p25": 13.0,
        "mfe_p50": 27.0,
        "mfe_p75": 69.0,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 32.5,
        "ci90": {
          "expR": -0.174,
          "ci90": [
            -0.285,
            -0.056
          ],
          "p_mean_le_0": 0.991,
          "n": 391
        }
      },
      "1.3": {
        "n": 362,
        "wrTP1": 24.0,
        "nSL": 250,
        "nTO": 25,
        "expR": -0.186,
        "pf": 0.74,
        "mfe_p25": 13.0,
        "mfe_p50": 26.5,
        "mfe_p75": 69.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.400000000000006,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 31.6,
        "ci90": {
          "expR": -0.186,
          "ci90": [
            -0.304,
            -0.059
          ],
          "p_mean_le_0": 0.996,
          "n": 350
        }
      },
      "1.5": {
        "n": 307,
        "wrTP1": 18.2,
        "nSL": 228,
        "nTO": 23,
        "expR": -0.306,
        "pf": 0.6,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 28.9,
        "ci90": {
          "expR": -0.306,
          "ci90": [
            -0.439,
            -0.172
          ],
          "p_mean_le_0": 1.0,
          "n": 296
        }
      },
      "2.0": {
        "n": 195,
        "wrTP1": 13.3,
        "nSL": 147,
        "nTO": 22,
        "expR": -0.342,
        "pf": 0.57,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 67.25,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 19.5,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 20.4,
        "ci90": {
          "expR": -0.342,
          "ci90": [
            -0.515,
            -0.148
          ],
          "p_mean_le_0": 0.999,
          "n": 184
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 789,
      "wrTP1": 49.2,
      "nSL": 367,
      "nTO": 34,
      "expR": 0.082,
      "pf": 1.17,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -19.0,
      "revAfterSL_rate": 42.8,
      "ci90": {
        "expR": 0.082,
        "ci90": [
          0.012,
          0.159
        ],
        "p_mean_le_0": 0.028,
        "n": 768
      }
    },
    "cuts": {
      "1.2": {
        "n": 322,
        "wrTP1": 29.2,
        "nSL": 206,
        "nTO": 22,
        "expR": 0.049,
        "pf": 1.07,
        "mfe_p25": 14.0,
        "mfe_p50": 31.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 17.75,
        "winnerMAE_p90": 26.700000000000003,
        "loserMFEbeforeSL_p50": 7.5,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 30.1,
        "ci90": {
          "expR": 0.049,
          "ci90": [
            -0.1,
            0.2
          ],
          "p_mean_le_0": 0.312,
          "n": 312
        }
      },
      "1.3": {
        "n": 298,
        "wrTP1": 27.9,
        "nSL": 193,
        "nTO": 22,
        "expR": 0.048,
        "pf": 1.07,
        "mfe_p25": 13.0,
        "mfe_p50": 31.0,
        "mfe_p75": 62.25,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.5,
        "revAfterSL_rate": 29.5,
        "ci90": {
          "expR": 0.048,
          "ci90": [
            -0.116,
            0.225
          ],
          "p_mean_le_0": 0.322,
          "n": 288
        }
      },
      "1.5": {
        "n": 251,
        "wrTP1": 21.9,
        "nSL": 175,
        "nTO": 21,
        "expR": -0.03,
        "pf": 0.96,
        "mfe_p25": 13.25,
        "mfe_p50": 31.0,
        "mfe_p75": 67.25,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 29.1,
        "ci90": {
          "expR": -0.03,
          "ci90": [
            -0.206,
            0.158
          ],
          "p_mean_le_0": 0.616,
          "n": 242
        }
      },
      "2.0": {
        "n": 172,
        "wrTP1": 16.9,
        "nSL": 125,
        "nTO": 18,
        "expR": -0.022,
        "pf": 0.97,
        "mfe_p25": 12.25,
        "mfe_p50": 34.5,
        "mfe_p75": 74.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -18.5,
        "revAfterSL_rate": 23.2,
        "ci90": {
          "expR": -0.022,
          "ci90": [
            -0.265,
            0.242
          ],
          "p_mean_le_0": 0.57,
          "n": 166
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 379,
      "wrTP1": 54.4,
      "nSL": 167,
      "nTO": 6,
      "expR": 0.093,
      "pf": 1.21,
      "mfe_p25": 13.0,
      "mfe_p50": 32.5,
      "mfe_p75": 65.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 44.0,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -38.0,
      "revAfterSL_rate": 54.5,
      "ci90": {
        "expR": 0.093,
        "ci90": [
          -0.008,
          0.198
        ],
        "p_mean_le_0": 0.066,
        "n": 374
      }
    },
    "cuts": {
      "1.2": {
        "n": 133,
        "wrTP1": 36.8,
        "nSL": 81,
        "nTO": 3,
        "expR": 0.189,
        "pf": 1.3,
        "mfe_p25": 21.0,
        "mfe_p50": 41.0,
        "mfe_p75": 87.5,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 27.60000000000001,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -38.0,
        "revAfterSL_rate": 46.9,
        "ci90": {
          "expR": 0.189,
          "ci90": [
            -0.048,
            0.433
          ],
          "p_mean_le_0": 0.099,
          "n": 131
        }
      },
      "1.3": {
        "n": 123,
        "wrTP1": 34.1,
        "nSL": 78,
        "nTO": 3,
        "expR": 0.143,
        "pf": 1.22,
        "mfe_p25": 21.0,
        "mfe_p50": 40.0,
        "mfe_p75": 84.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 26.499999999999993,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -38.0,
        "revAfterSL_rate": 46.2,
        "ci90": {
          "expR": 0.143,
          "ci90": [
            -0.109,
            0.412
          ],
          "p_mean_le_0": 0.182,
          "n": 121
        }
      },
      "1.5": {
        "n": 103,
        "wrTP1": 29.1,
        "nSL": 71,
        "nTO": 2,
        "expR": 0.069,
        "pf": 1.1,
        "mfe_p25": 21.0,
        "mfe_p50": 39.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 27.300000000000004,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -37.0,
        "revAfterSL_rate": 47.9,
        "ci90": {
          "expR": 0.069,
          "ci90": [
            -0.211,
            0.351
          ],
          "p_mean_le_0": 0.375,
          "n": 101
        }
      },
      "2.0": {
        "n": 60,
        "wrTP1": 20.0,
        "nSL": 46,
        "nTO": 2,
        "expR": -0.079,
        "pf": 0.9,
        "mfe_p25": 18.5,
        "mfe_p50": 37.0,
        "mfe_p75": 91.5,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 16.200000000000003,
        "loserMFEbeforeSL_p50": 7.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -37.0,
        "revAfterSL_rate": 37.0,
        "ci90": {
          "expR": -0.079,
          "ci90": [
            -0.452,
            0.336
          ],
          "p_mean_le_0": 0.646,
          "n": 58
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 289,
      "wrTP1": 49.8,
      "nSL": 127,
      "nTO": 18,
      "expR": 0.048,
      "pf": 1.1,
      "mfe_p25": 13.25,
      "mfe_p50": 25.0,
      "mfe_p75": 48.75,
      "winnerMAE_p75": 19.25,
      "winnerMAE_p90": 32.70000000000002,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -26.0,
      "revAfterSL_rate": 43.3,
      "ci90": {
        "expR": 0.048,
        "ci90": [
          -0.061,
          0.16
        ],
        "p_mean_le_0": 0.233,
        "n": 274
      }
    },
    "cuts": {
      "1.2": {
        "n": 93,
        "wrTP1": 31.2,
        "nSL": 54,
        "nTO": 10,
        "expR": 0.145,
        "pf": 1.23,
        "mfe_p25": 15.0,
        "mfe_p50": 33.0,
        "mfe_p75": 61.75,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 27.4,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 31.5,
        "ci90": {
          "expR": 0.145,
          "ci90": [
            -0.136,
            0.437
          ],
          "p_mean_le_0": 0.208,
          "n": 86
        }
      },
      "1.3": {
        "n": 85,
        "wrTP1": 31.8,
        "nSL": 49,
        "nTO": 9,
        "expR": 0.189,
        "pf": 1.3,
        "mfe_p25": 18.0,
        "mfe_p50": 33.0,
        "mfe_p75": 61.5,
        "winnerMAE_p75": 20.5,
        "winnerMAE_p90": 27.800000000000004,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 30.6,
        "ci90": {
          "expR": 0.189,
          "ci90": [
            -0.111,
            0.513
          ],
          "p_mean_le_0": 0.152,
          "n": 79
        }
      },
      "1.5": {
        "n": 68,
        "wrTP1": 29.4,
        "nSL": 39,
        "nTO": 9,
        "expR": 0.235,
        "pf": 1.37,
        "mfe_p25": 18.0,
        "mfe_p50": 33.0,
        "mfe_p75": 68.75,
        "winnerMAE_p75": 21.25,
        "winnerMAE_p90": 27.200000000000003,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 23.1,
        "ci90": {
          "expR": 0.235,
          "ci90": [
            -0.122,
            0.607
          ],
          "p_mean_le_0": 0.144,
          "n": 62
        }
      },
      "2.0": {
        "n": 38,
        "wrTP1": 21.1,
        "nSL": 24,
        "nTO": 6,
        "expR": 0.252,
        "pf": 1.37,
        "mfe_p25": 24.0,
        "mfe_p50": 42.0,
        "mfe_p75": 92.5,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 20.6,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 16.7,
        "ci90": {
          "expR": 0.252,
          "ci90": [
            -0.299,
            0.766
          ],
          "p_mean_le_0": 0.23,
          "n": 35
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
    "n": 2724,
    "wrTP1": 44.6,
    "expR": -0.019
  },
  "2026-W37": {
    "n": 4891,
    "wrTP1": 47.0,
    "expR": 0.077
  },
  "2026-W38": {
    "n": 4433,
    "wrTP1": 46.3,
    "expR": 0.099
  },
  "2026-W39": {
    "n": 5038,
    "wrTP1": 45.9,
    "expR": 0.064
  },
  "2026-W40": {
    "n": 5339,
    "wrTP1": 45.4,
    "expR": 0.017
  },
  "2026-W41": {
    "n": 1579,
    "wrTP1": 46.9,
    "expR": 0.011
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 32,
      "wrTP1": 46.9,
      "expR": 0.264,
      "pf": 1.6
    },
    "1m/INV/SHORT": {
      "n": 17,
      "wrTP1": 70.6,
      "expR": 0.243,
      "pf": 1.83
    },
    "1m/RETEST/LONG": {
      "n": 1130,
      "wrTP1": 42.7,
      "expR": -0.013,
      "pf": 0.97
    },
    "1m/RETEST/SHORT": {
      "n": 421,
      "wrTP1": 43.0,
      "expR": -0.022,
      "pf": 0.96
    },
    "2m/INV/LONG": {
      "n": 15,
      "wrTP1": 40.0,
      "expR": -0.248,
      "pf": 0.59
    },
    "2m/INV/SHORT": {
      "n": 6,
      "wrTP1": 50.0,
      "expR": -0.267,
      "pf": 0.47
    },
    "2m/RETEST/LONG": {
      "n": 574,
      "wrTP1": 45.5,
      "expR": -0.065,
      "pf": 0.88
    },
    "2m/RETEST/SHORT": {
      "n": 193,
      "wrTP1": 41.5,
      "expR": -0.1,
      "pf": 0.81
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
      "n": 34,
      "wrTP1": 41.2,
      "expR": -0.052,
      "pf": 0.9
    },
    "1m/INV/SHORT": {
      "n": 54,
      "wrTP1": 40.7,
      "expR": 0.037,
      "pf": 1.07
    },
    "1m/RETEST/LONG": {
      "n": 1450,
      "wrTP1": 45.6,
      "expR": 0.067,
      "pf": 1.14
    },
    "1m/RETEST/SHORT": {
      "n": 1591,
      "wrTP1": 45.1,
      "expR": 0.043,
      "pf": 1.09
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
      "n": 618,
      "wrTP1": 47.1,
      "expR": 0.027,
      "pf": 1.06
    },
    "2m/RETEST/SHORT": {
      "n": 692,
      "wrTP1": 51.4,
      "expR": 0.152,
      "pf": 1.34
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
      "n": 209,
      "wrTP1": 52.6,
      "expR": 0.195,
      "pf": 1.44
    },
    "5m/RETEST/SHORT": {
      "n": 197,
      "wrTP1": 53.3,
      "expR": 0.162,
      "pf": 1.37
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 54,
      "wrTP1": 40.7,
      "expR": -0.11,
      "pf": 0.79
    },
    "1m/INV/SHORT": {
      "n": 20,
      "wrTP1": 45.0,
      "expR": -0.101,
      "pf": 0.8
    },
    "1m/RETEST/LONG": {
      "n": 1791,
      "wrTP1": 48.4,
      "expR": 0.124,
      "pf": 1.27
    },
    "1m/RETEST/SHORT": {
      "n": 941,
      "wrTP1": 42.7,
      "expR": 0.123,
      "pf": 1.27
    },
    "2m/INV/LONG": {
      "n": 14,
      "wrTP1": 50.0,
      "expR": -0.147,
      "pf": 0.56
    },
    "2m/INV/SHORT": {
      "n": 4,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 812,
      "wrTP1": 47.0,
      "expR": 0.054,
      "pf": 1.11
    },
    "2m/RETEST/SHORT": {
      "n": 347,
      "wrTP1": 43.5,
      "expR": 0.008,
      "pf": 1.02
    },
    "5m/INV/LONG": {
      "n": 6,
      "wrTP1": 33.3,
      "expR": -0.348,
      "pf": 0.3
    },
    "5m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 286,
      "wrTP1": 51.4,
      "expR": 0.195,
      "pf": 1.49
    },
    "5m/RETEST/SHORT": {
      "n": 157,
      "wrTP1": 40.1,
      "expR": 0.098,
      "pf": 1.2
    }
  },
  "2026-W39": {
    "1m/INV/LONG": {
      "n": 32,
      "wrTP1": 53.1,
      "expR": 0.655,
      "pf": 3.1
    },
    "1m/INV/SHORT": {
      "n": 39,
      "wrTP1": 51.3,
      "expR": 0.02,
      "pf": 1.05
    },
    "1m/RETEST/LONG": {
      "n": 1892,
      "wrTP1": 44.7,
      "expR": 0.062,
      "pf": 1.13
    },
    "1m/RETEST/SHORT": {
      "n": 1303,
      "wrTP1": 44.9,
      "expR": -0.003,
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
      "n": 732,
      "wrTP1": 46.7,
      "expR": 0.148,
      "pf": 1.31
    },
    "2m/RETEST/SHORT": {
      "n": 543,
      "wrTP1": 49.2,
      "expR": 0.035,
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
      "n": 253,
      "wrTP1": 45.5,
      "expR": 0.093,
      "pf": 1.2
    },
    "5m/RETEST/SHORT": {
      "n": 196,
      "wrTP1": 48.5,
      "expR": 0.103,
      "pf": 1.22
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
      "expR": -0.033,
      "pf": 0.94
    },
    "1m/RETEST/SHORT": {
      "n": 1380,
      "wrTP1": 45.9,
      "expR": 0.028,
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
      "wrTP1": 46.4,
      "expR": -0.002,
      "pf": 1.0
    },
    "2m/RETEST/SHORT": {
      "n": 631,
      "wrTP1": 46.4,
      "expR": 0.111,
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
      "wrTP1": 53.7,
      "expR": 0.101,
      "pf": 1.23
    },
    "5m/RETEST/SHORT": {
      "n": 233,
      "wrTP1": 43.8,
      "expR": 0.024,
      "pf": 1.05
    }
  },
  "2026-W41": {
    "1m/INV/LONG": {
      "n": 13,
      "wrTP1": 46.2,
      "expR": -0.186,
      "pf": 0.62
    },
    "1m/INV/SHORT": {
      "n": 13,
      "wrTP1": 30.8,
      "expR": -0.047,
      "pf": 0.91
    },
    "1m/RETEST/LONG": {
      "n": 505,
      "wrTP1": 44.8,
      "expR": -0.063,
      "pf": 0.87
    },
    "1m/RETEST/SHORT": {
      "n": 439,
      "wrTP1": 45.1,
      "expR": 0.096,
      "pf": 1.19
    },
    "2m/INV/LONG": {
      "n": 2,
      "wrTP1": 50.0,
      "expR": -0.025,
      "pf": 0.95
    },
    "2m/INV/SHORT": {
      "n": 3,
      "wrTP1": 33.3,
      "expR": 1.827,
      "pf": 6.48
    },
    "2m/RETEST/LONG": {
      "n": 232,
      "wrTP1": 50.0,
      "expR": -0.036,
      "pf": 0.93
    },
    "2m/RETEST/SHORT": {
      "n": 196,
      "wrTP1": 49.5,
      "expR": 0.113,
      "pf": 1.23
    },
    "5m/INV/LONG": {
      "n": 2,
      "wrTP1": 50.0,
      "expR": -0.445,
      "pf": 0.11
    },
    "5m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 95,
      "wrTP1": 50.5,
      "expR": -0.019,
      "pf": 0.96
    },
    "5m/RETEST/SHORT": {
      "n": 78,
      "wrTP1": 53.8,
      "expR": -0.062,
      "pf": 0.87
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 22137,
  "brier": 0.2211,
  "bias": -0.105,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.225
    },
    {
      "feature": "nearTk",
      "weight": -0.053
    },
    {
      "feature": "stretchAtr",
      "weight": -0.049
    },
    {
      "feature": "rvol",
      "weight": 0.034
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.034
    },
    {
      "feature": "nearEdge",
      "weight": -0.034
    },
    {
      "feature": "emaStack",
      "weight": 0.021
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.019
    },
    {
      "feature": "aligned",
      "weight": -0.014
    },
    {
      "feature": "chopIdx",
      "weight": 0.009
    },
    {
      "feature": "structDir",
      "weight": -0.008
    },
    {
      "feature": "biasScore",
      "weight": -0.005
    },
    {
      "feature": "hourNY",
      "weight": 0.002
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.154,
      "actual": 0.179,
      "n": 2213
    },
    {
      "bin": 1,
      "pred": 0.357,
      "actual": 0.302,
      "n": 2214
    },
    {
      "bin": 2,
      "pred": 0.442,
      "actual": 0.331,
      "n": 2214
    },
    {
      "bin": 3,
      "pred": 0.49,
      "actual": 0.396,
      "n": 2213
    },
    {
      "bin": 4,
      "pred": 0.53,
      "actual": 0.514,
      "n": 2214
    },
    {
      "bin": 5,
      "pred": 0.561,
      "actual": 0.568,
      "n": 2214
    },
    {
      "bin": 6,
      "pred": 0.585,
      "actual": 0.599,
      "n": 2213
    },
    {
      "bin": 7,
      "pred": 0.606,
      "actual": 0.66,
      "n": 2214
    },
    {
      "bin": 8,
      "pred": 0.626,
      "actual": 0.695,
      "n": 2214
    },
    {
      "bin": 9,
      "pred": 0.653,
      "actual": 0.745,
      "n": 2214
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 17086,
  "testN": 6918,
  "testWeeks": [
    "2026-W40",
    "2026-W41"
  ],
  "model_oos_brier": 0.2197,
  "model_oos_n": 6918,
  "best_scheme_in_sample": {
    "scheme": "nextLevel",
    "trainExpR": 0.063
  },
  "best_scheme_oos_expR": 0.016
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.162,
    "ci90": [
      0.002,
      0.342
    ],
    "p_mean_le_0": 0.048,
    "n": 200,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": 0.004,
    "ci90": [
      -0.125,
      0.139
    ],
    "p_mean_le_0": 0.5,
    "n": 181,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.038,
    "ci90": [
      0.015,
      0.061
    ],
    "p_mean_le_0": 0.004,
    "n": 8308,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.04,
    "ci90": [
      0.014,
      0.067
    ],
    "p_mean_le_0": 0.007,
    "n": 5752,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.049,
    "ci90": [
      -0.141,
      0.25
    ],
    "p_mean_le_0": 0.35,
    "n": 73,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.129,
    "ci90": [
      -0.119,
      0.405
    ],
    "p_mean_le_0": 0.224,
    "n": 77,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.031,
    "ci90": [
      -0.004,
      0.063
    ],
    "p_mean_le_0": 0.066,
    "n": 3681,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.078,
    "ci90": [
      0.036,
      0.125
    ],
    "p_mean_le_0": 0.0,
    "n": 2501,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.408,
    "ci90": [
      0.14,
      0.678
    ],
    "p_mean_le_0": 0.004,
    "n": 23,
    "survives_fdr10": true
  },
  "5m/INV/SHORT": {
    "expR": 0.185,
    "ci90": [
      -0.278,
      0.695
    ],
    "p_mean_le_0": 0.259,
    "n": 14,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.119,
    "ci90": [
      0.062,
      0.173
    ],
    "p_mean_le_0": 0.001,
    "n": 1299,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.074,
    "ci90": [
      0.006,
      0.143
    ],
    "p_mean_le_0": 0.039,
    "n": 878,
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
      "id": 1,
      "n": 8566,
      "wrTP1": 45.7,
      "expR": 0.056,
      "pf": 1.12,
      "defining_features": {
        "biasScore": -1.1,
        "emaStack": -0.98,
        "nearEdge": -0.86,
        "structDir": -0.42
      }
    },
    {
      "id": 0,
      "n": 8915,
      "wrTP1": 45.4,
      "expR": 0.053,
      "pf": 1.11,
      "defining_features": {
        "biasScore": 0.79,
        "emaStack": 0.67,
        "nearEdge": 0.67,
        "hourNY": -0.51
      }
    },
    {
      "id": 3,
      "n": 3996,
      "wrTP1": 49.6,
      "expR": 0.04,
      "pf": 1.09,
      "defining_features": {
        "hourNY": 1.33,
        "atrPctUsed": -0.92,
        "emaStack": 0.63,
        "biasScore": 0.6
      }
    },
    {
      "id": 2,
      "n": 2527,
      "wrTP1": 43.8,
      "expR": 0.028,
      "pf": 1.06,
      "defining_features": {
        "stretchAtr": 1.86,
        "rvol": 1.63,
        "chopIdx": -1.45,
        "hourNY": -0.16
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
        "n": 42,
        "wrTP1": 52.4,
        "expR": 0.356
      },
      "YM": {
        "n": 80,
        "wrTP1": 42.5,
        "expR": 0.209
      },
      "ES": {
        "n": 31,
        "wrTP1": 54.8,
        "expR": 0.155
      },
      "GC": {
        "n": 32,
        "wrTP1": 34.4,
        "expR": -0.362
      },
      "NQ": {
        "n": 25,
        "wrTP1": 56.0,
        "expR": 0.344
      }
    },
    "expR_spread": 0.718,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 104,
        "wrTP1": 39.4,
        "expR": -0.044
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
        "n": 37,
        "wrTP1": 64.9,
        "expR": 0.192
      },
      "CL": {
        "n": 26,
        "wrTP1": 26.9,
        "expR": -0.372
      }
    },
    "expR_spread": 0.82,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 1326,
        "wrTP1": 41.8,
        "expR": -0.024
      },
      "NQ": {
        "n": 1934,
        "wrTP1": 45.3,
        "expR": 0.039
      },
      "ES": {
        "n": 2120,
        "wrTP1": 45.8,
        "expR": 0.043
      },
      "CL": {
        "n": 1766,
        "wrTP1": 45.2,
        "expR": 0.052
      },
      "YM": {
        "n": 1433,
        "wrTP1": 45.5,
        "expR": 0.067
      }
    },
    "expR_spread": 0.091,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 576,
        "wrTP1": 43.9,
        "expR": 0.129
      },
      "GC": {
        "n": 1685,
        "wrTP1": 45.7,
        "expR": 0.067
      },
      "YM": {
        "n": 1752,
        "wrTP1": 44.2,
        "expR": 0.038
      },
      "ES": {
        "n": 1036,
        "wrTP1": 45.9,
        "expR": 0.019
      },
      "CL": {
        "n": 1026,
        "wrTP1": 43.1,
        "expR": -0.03
      }
    },
    "expR_spread": 0.159,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 11,
        "wrTP1": 36.4,
        "expR": -0.336
      },
      "CL": {
        "n": 11,
        "wrTP1": 63.6,
        "expR": -0.057
      },
      "YM": {
        "n": 22,
        "wrTP1": 36.4,
        "expR": -0.145
      },
      "ES": {
        "n": 15,
        "wrTP1": 80.0,
        "expR": 0.283
      },
      "NQ": {
        "n": 18,
        "wrTP1": 50.0,
        "expR": 0.409
      }
    },
    "expR_spread": 0.745,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 44,
        "wrTP1": 52.3,
        "expR": 0.392
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
      "CL": {
        "n": 11,
        "wrTP1": 45.5,
        "expR": -0.258
      },
      "GC": {
        "n": 8,
        "wrTP1": 12.5,
        "expR": -0.595
      }
    },
    "expR_spread": 0.987,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 923,
        "wrTP1": 45.7,
        "expR": 0.017
      },
      "GC": {
        "n": 590,
        "wrTP1": 46.1,
        "expR": 0.026
      },
      "CL": {
        "n": 814,
        "wrTP1": 47.4,
        "expR": 0.043
      },
      "ES": {
        "n": 862,
        "wrTP1": 47.2,
        "expR": -0.02
      },
      "YM": {
        "n": 634,
        "wrTP1": 47.6,
        "expR": 0.111
      }
    },
    "expR_spread": 0.131,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 462,
        "wrTP1": 46.8,
        "expR": -0.022
      },
      "YM": {
        "n": 756,
        "wrTP1": 49.3,
        "expR": 0.108
      },
      "GC": {
        "n": 700,
        "wrTP1": 50.4,
        "expR": 0.173
      },
      "NQ": {
        "n": 267,
        "wrTP1": 41.9,
        "expR": 0.082
      },
      "CL": {
        "n": 417,
        "wrTP1": 45.6,
        "expR": -0.018
      }
    },
    "expR_spread": 0.195,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.232
      },
      "YM": {
        "n": 8,
        "wrTP1": 87.5,
        "expR": 0.318
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 1.473
      },
      "ES": {
        "n": 6,
        "wrTP1": 83.3,
        "expR": 0.428
      }
    },
    "expR_spread": 1.241,
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
        "n": 4,
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
        "n": 172,
        "wrTP1": 51.2,
        "expR": 0.13
      },
      "ES": {
        "n": 310,
        "wrTP1": 51.0,
        "expR": 0.113
      },
      "YM": {
        "n": 230,
        "wrTP1": 52.2,
        "expR": 0.223
      },
      "CL": {
        "n": 268,
        "wrTP1": 51.5,
        "expR": 0.103
      },
      "NQ": {
        "n": 396,
        "wrTP1": 50.3,
        "expR": 0.068
      }
    },
    "expR_spread": 0.155,
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
        "n": 169,
        "wrTP1": 50.3,
        "expR": 0.075
      },
      "GC": {
        "n": 240,
        "wrTP1": 43.3,
        "expR": -0.017
      },
      "YM": {
        "n": 255,
        "wrTP1": 48.2,
        "expR": 0.178
      },
      "CL": {
        "n": 187,
        "wrTP1": 48.1,
        "expR": 0.084
      }
    },
    "expR_spread": 0.195,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 5,
  "near_news_30m": {
    "n": 20,
    "wrTP1": 70.0,
    "nSL": 6,
    "nTO": 0,
    "expR": 0.451,
    "pf": 2.5,
    "mfe_p25": 7.75,
    "mfe_p50": 15.0,
    "mfe_p75": 36.0,
    "winnerMAE_p75": 7.25,
    "winnerMAE_p90": 16.00000000000001,
    "loserMFEbeforeSL_p50": 0.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 1.5,
    "entryZoneTk_p50": -13.5,
    "revAfterSL_rate": 50.0
  },
  "away_from_news": {
    "n": 23984,
    "wrTP1": 46.0,
    "nSL": 11088,
    "nTO": 1867,
    "expR": 0.049,
    "pf": 1.1,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.7
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 6,
  "mae_deltaER": 0.283,
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
      "2026-09-30 (miercoles, cuarto dia real de trading bajo el SL nuevo): el verdict mecanico agregado SIGUE en 'confirmed' (dispara la alerta EXPERIMENTO CONFIRMADO en report.md de hoy otra vez) y SIGUE sin tomarse al pie de la letra -- el desglose por segmento de prediction_scoreboard, con n ya bastante mas grande en los 6 (1m LONG n=437, 1m SHORT n=800, 2m LONG n=194, 2m SHORT n=318, 5m LONG n=76, 5m SHORT n=114 -- los 6 superan ya el afterN>=40 de agent-instructions.md), mantiene EXACTAMENTE el mismo patron de direccion que ayer, ahora con mucha mas muestra detras: 1m SHORT realDeltaER=+0.142 (vs +0.143 predicho, acierta casi exacto) y 2m SHORT realDeltaER=+0.167 (vs +0.151 predicho, acierta) siguen siendo los UNICOS 2 segmentos que confirman; 1m LONG realDeltaER=-0.028, 2m LONG realDeltaER=-0.097, 5m LONG realDeltaER=-0.151 y 5m SHORT realDeltaER=-0.086 siguen en direccion CONTRARIA a lo predicho (hit_direction_rate=33.3%, mae_deltaER=0.251). Nota importante: la hipotesis de ayer ('SHORT ayuda, LONG perjudica') ya NO describe el patron con precision -- 5m SHORT tambien se dio vuelta a negativo hoy con n=114 (ya no es 'n todavia chico', son 4 dias seguidos de dato real). El patron mas preciso hoy es: SOLO 1m y 2m SHORT confirman; las 3 ramas LONG (1m/2m/5m) Y 5m SHORT no confirman. Es el CUARTO dia consecutivo (09-28, 09-29, 09-30, y contando) con la misma division 2-vs-4, cada vez con mas muestra, sin ninguna reversion hacia el lado predicho en los 4 segmentos que fallan. Todavia no se cumple el criterio propio del experimento de '2 semanas consecutivas en la misma direccion' antes de tratarlo como resultado real, pero con afterN ya por encima de 40 en los 6 segmentos y 3-4 dias seguidos sin cambio de signo, el balance de evidencia se esta inclinando hacia un revert parcial. RECOMENDACION EXPLICITA para la revision semanal del domingo 2026-10-04 (no antes, hace falta ver si el patron se mantiene el resto de la semana): si 1m LONG, 2m LONG, 5m LONG y 5m SHORT siguen en direccion negativa el domingo, proponer formalmente revertir sl_basis_retest a '3-capas' en esos 4 segmentos (mantener la mecha del retest solo en 1m y 2m SHORT, que son los que realmente mejoraron). Correlacion en paralelo (no causal, anotar solo): el mismo segmento 2m/RETEST/LONG perdio hoy su significancia en segment_significance (survives_fdr10 paso de true a false, CI90=[-0.008,0.069] cruza cero por primera vez en semanas, ver report.alerts de hoy) -- dos senales independientes (el experimento de SL y la significancia cruda del segmento) apuntando en la misma direccion de deterioro para 2m LONG en la misma corrida.",
      "2026-10-02 (viernes, sexto dia habil real bajo el SL nuevo desde el sabado 09-26): afterN agregado ya grande en los 6 segmentos (1m LONG=1310, 1m SHORT=1323, 2m LONG=581, 2m SHORT=593, 5m LONG=201, 5m SHORT=203). Los 3 segmentos LONG SIGUEN en direccion CONTRARIA a lo predicho y sin mejorar vs ayer: 1m realDeltaER=-0.091 (predicho +0.152), 2m realDeltaER=-0.092 (predicho +0.154), 5m realDeltaER=-0.072 (predicho +0.255). NOVEDAD: el lado SHORT, que venia confirmando con claridad, se debilita en los 3 TF -- 1m SHORT casi plano (realDeltaER=+0.003 vs +0.143 predicho, ayer era +0.081), 2m SHORT sigue positivo pero mas debil (+0.038 vs +0.151 predicho, ayer +0.061), 5m SHORT empeora (-0.139 vs +0.567 predicho, ayer -0.072). hit_direction_rate se mantiene en 33.3% (2/6) pero mae_deltaER sube a 0.296, la peor lectura del scoreboard hasta la fecha. decay_weekly_by_segment de W40 (casi cerrada) muestra ruido adicional en 5m: 5m LONG se da vuelta a POSITIVO esta semana (n=196 E[R]=+0.068, rompe 2 semanas negativas) mientras 5m SHORT se da vuelta a NEGATIVO (n=201 E[R]=-0.033, rompe su racha positiva) -- consistente con que 5m (menor n) es el TF mas ruidoso de los 6, no un cambio de regimen. 1m y 2m LONG, los de mayor muestra y mas consistentes dia a dia, siguen negativos sin ninguna reversion desde el cambio. DECISION: siguen siendo 6 dias habiles de calendario desde el cambio (09-28 a 10-02), todavia no las '2 semanas consecutivas' del propio criterio del experimento -- se mantiene NO revertir hoy. Para la revision semanal del domingo 2026-10-04: si 1m y 2m LONG siguen negativos (son los que importan, con mas muestra y sin ruido de 5m), proponer formalmente revertir sl_basis_retest a 3-capas en RETEST LONG (1m/2m al menos; 5m LONG revirtio hoy a positivo, tratar con mas cautela y mas muestra antes de meterlo en el mismo paquete). El lado SHORT ya no es un bloque limpio de 'mejora en los 3 TF' -- sostener 1m/2m SHORT con el SL nuevo pero vigilar 1m SHORT (casi plano) y 5m SHORT (ya negativo) de cerca, no asumir que todo SHORT se mantiene con la misma fuerza que hace una semana.",
      "2026-10-03 (sabado, septimo dia de calendario desde el cambio, pero el hallazgo de hoy es metodologico, no de muestra nueva): se revisa la cadena de razonamiento de los ultimos 6 dias (09-28 a 10-02) que usaba prediction_scoreboard/eval_experiments para decir 'LONG se esta revirtiendo, preparar revert parcial el domingo'. Esa lectura compara expR de rMultiple ANTES vs DESPUES de changeDate -- pero appliedNote ya decia que 'el feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig'. Si rMultiple se calcula IGUAL antes y despues del cambio (siempre 3 capas, sin importar que input este activo en el Pine), un before/after sobre rMultiple NO puede medir el efecto de mover el SL -- solo mide como vino el mercado en el periodo 'after' (28 sep - 2 oct, que coincide con la semana W40 de bajo E[R] global, ver decay_weekly W40=0.013, casi identico al 'after' agregado de este experimento =0.014). Es una confusion clasica de regimen de mercado disfrazada de efecto del experimento. SE AGREGO HOY a analyze.py un campo nuevo sl_origin_vs_layer.since_change: el mismo emparejado (rOrig vs rMultiple, simultaneos, sin mezclar con calendario) que ya certifica el experimento en agregado, pero restringido a recvDate>=2026-09-26 (n=4734 en total RETEST). Resultado con la metrica correcta: NINGUN segmento sale negativo (delta_below_zero=false en los 6). 1m LONG delta=+0.001 CI90=[-0.071,0.078] (plano, no niega el experimento); 1m SHORT delta=+0.055 CI90=[-0.025,0.137] (plano, no confirma todavia); 2m LONG delta=+0.193 CI90=[0.075,0.322] -- CONFIRMA POSITIVO incluso solo con dato post-cambio (n=780); 2m SHORT delta=+0.025 CI90 cruza cero (plano); 5m LONG delta=+0.063 CI90 cruza cero (plano, n=278); 5m SHORT delta=+0.075 CI90 cruza cero (plano, n=208). El patron real es: el efecto se ENCOGIO frente a la estimacion in-sample completa (esperable, optimismo de haber minado 6 segmentos durante semanas) pero NO SE INVIRTIO en ninguno. CORRECCION DE RUMBO: se retira la recomendacion de las corridas 09-29 a 10-02 de formalizar un revert parcial de sl_basis_retest a LONG en la revision semanal de manana domingo 2026-10-04. Recomendacion para manana: NO revertir nada; documentar en la revision semanal que prediction_scoreboard no es la metrica valida para ESTE experimento en particular (si lo es para experimentos que cambien directamente el input que alimenta rMultiple) y que sl_origin_vs_layer.since_change es la referencia a vigilar de aqui en adelante. Seguir mirando since_change semana a semana; si algun segmento desarrolla delta_below_zero=true con n>=40 ahi si habria caso real para revertir ese segmento especifico.",
      "2026-10-04 (domingo, REVISION SEMANAL, octavo dia de calendario desde el cambio, sin dato jsonl nuevo del cron pero con el cierre formal de la semana 2026-W40): since_change (n=4734 total RETEST) con el cierre de W40 confirma la correccion de ayer con un dia mas de perspectiva. De los 6 segmentos con n>=100 post-cambio, SOLO 2m/RETEST/LONG sigue confirmando limpio (n=780, delta=+0.193 CI90=[0.075,0.322], no cruza cero); los otros 5 (1m LONG n=1545, 1m SHORT n=1236, 2m SHORT n=559, 5m LONG n=278, 5m SHORT n=208) quedan planos -- CI90 cruza cero en los dos sentidos, NINGUNO con delta_below_zero=true. Nueva alerta permanente agregada a analyze.py hoy (material_alerts): compara automaticamente cuantos segmentos con n>=100 confirman en since_change vs el total, para no depender de que el agente lo note a mano cada vez. Lectura honesta para la revision semanal (ver reviews/2026-week-40.md): el 'cambio del mes' del 2026-09-26 se declaro con 6/6 segmentos certificando en agregado historico (mezcla pre+post cambio) y una racha de ~18 lecturas sin reversion -- pero la UNICA medicion que aisla el efecto real (pareada, solo post-cambio) hoy solo sostiene esa fuerza en 1 de 6 segmentos; el resto simplemente no tiene evidencia suficiente todavia para confirmar NI para revertir. prediction_scoreboard (hit_direction_rate=33.3%, peor que un volado) mide lo mismo que ya se identifico como confundido con el regimen de mercado (rMultiple no cambia con el input del Pine) -- no usar ese numero para juzgar este experimento especifico, pero SI como leccion de metodo: la proxima vez que 6/6 segmentos certifiquen en agregado historico sin haber visto una sola lectura post-cambio real, declarar el 'cambio del mes' con mas cautela (marcar explicitamente 'pendiente de since_change' en vez de 'evidencia madura'). DECISION: no revertir nada. Mantener aplicado en los 6 segmentos, seguir acumulando since_change semana a semana; solo revertir un segmento especifico si desarrolla delta_below_zero=true con n>=40.",
      "2026-10-06 (martes, incidente de repo del dia -- ver buy-retest.md -- sin perdida de dato): eval_experiments() en report.json pone por primera vez verdict=\"flat\" para este experimento en su evaluacion agregada formal antes/despues (beforeN=16583 expR=0.061 vs afterN=6438 expR=0.013) -- confirma con muestra ya grande lo que la alerta de ayer avisaba (\"el efecto se encoge\"). NO es \"rejected\" (expR post-cambio sigue positivo, no negativo), asi que sigue sin caso para revertir, pero ya no corresponde describirlo como \"cambio ganador\" en el agregado. since_change por segmento (n=5895 total RETEST, recvDate>=2026-09-26) con un dia mas de perspectiva: SOLO 2m/RETEST/LONG sigue confirmando limpio (n=954, delta=+0.145 CI90=[0.039,0.258]); los otros 5 (1m LONG n=1900 delta=-0.015, 1m SHORT n=1557 delta=+0.04, 2m SHORT n=713 delta=+0.028, 5m LONG n=342 delta=+0.04, 5m SHORT n=273 delta=+0.059) siguen planos, ninguno delta_below_zero=true. Dato adicional que contextualiza el verdict=\"flat\": en 1m/RETEST/LONG, TANTO layer_expR (-0.05) COMO orig_expR (-0.065) son negativos desde el cambio -- el deterioro de ese segmento (ver decay_weekly_by_segment, 3 semanas cayendo, W41 ya en -0.108) no depende de que SL se use, es de regimen/muestra, no del experimento en si. DECISION: sin cambio -- mantener aplicado en los 6 segmentos, no revertir nada; bajar la confianza declarada del \"cambio del mes\" de 2026-09-26 a \"neutro en agregado, con una excepcion que si gana (2m LONG)\". Vigilar si algun segmento desarrolla delta_below_zero=true con n>=40, que seria el primer caso real para revertir."
    ],
    "appliedNote": "2026-09-26: aplicado en scalp_command.pine (input sc_sl_retest_basis, default 'Auto (como se midio)'): en RETEST el SL real pasa a la mecha de la vela del retest; 1m SHORT suma la vela previa (retestBar2), igual que la medicion paralela. Base: los 6 segmentos RETEST certifican con CI90 > 0 (n=11273, E[R] 0.238 vs 0.065). El tier se sigue calculando con el stop de 3 capas. El feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig, asi que sl_origin_vs_layer sigue siendo la vigilancia. Rige en cada grafico desde que Jesus re-pega scalp_cc_FULL_for_tradingview.pine. Revertir = poner la base en '3 capas'.",
    "beforeN": 16578,
    "afterN": 6826,
    "before": {
      "n": 16578,
      "wrTP1": 46.0,
      "nSL": 7584,
      "nTO": 1369,
      "expR": 0.061,
      "pf": 1.13,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.0
    },
    "after": {
      "n": 6826,
      "wrTP1": 45.9,
      "nSL": 3270,
      "nTO": 425,
      "expR": 0.017,
      "pf": 1.03,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 32.8
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
      "2026-09-29 (martes): el walk-forward testWeeks avanzo de [W38,W39] a [W39,W40] (W39 ya cerro, W40 es la semana en curso) y con la ventana nueva el unico candidato que habia confirmado OOS limpio el 09-27 (5m/RETEST/LONG) PIERDE la certificacion: baseline test n=287 expR=0.084 CI90=[-0.046,0.215] (cruza cero, antes n=544 expR=0.148 CI90=[0.056,0.247] no cruzaba) y los cortes 1.2/1.3 salen con CI90 igual de anchos y cruzando cero (ej. 1.2: expR=0.161 CI90=[-0.175,0.527]) -- el patron todavia apunta en la misma direccion (subir el piso de rr1 sube el E[R] observado) pero ya no certifica fuera de muestra con esta ventana mas chica (W40 apenas tiene unos dias de dato). No es una reversion de signo, es perdida de potencia estadistica al cambiar de ventana de test -- vigilar si vuelve a certificar cuando W40 cierre con mas muestra. Sigue sin proponerse ningun valor concreto de sc_aplus_rr; la linea 7 de predictions.jsonl sigue sin appliedDate.",
      "2026-10-04 (domingo, REVISION SEMANAL): el walk-forward testWeeks avanzo otra vez, ahora de [W38,W39] a [W39,W40] (los dos ya cerrados, no una semana parcial como el 09-29). El candidato que SI habia confirmado limpio en la revision de 2026-week-39.md con la ventana [W38,W39] (5m/RETEST/LONG, rr1>=1.2, baseline n=544 expR=0.148 CI90=[0.056,0.247], corte expR=0.372 CI90=[0.149,0.605]) deja de confirmar con [W39,W40]: baseline n=515 expR=0.102 CI90=[0.013,0.192] (todavia positivo), corte 1.2 n=178 expR=0.178 pero CI90=[-0.045,0.409] cruza cero. A diferencia del 09-29 (donde la perdida de potencia era por W40 parcial con pocos dias), esta vez W40 esta completa -- es una perdida de confirmacion real con la ventana madura, no un artefacto de muestra chica. Se retira como candidato activo esta semana (ver reviews/2026-week-40.md); como nunca se aplico en TradingView (status sigue 'proposed', predictions.jsonl linea de 2026-W39 sigue con appliedDate=null), no hay nada que revertir. Ningun otro segmento de RETEST confirma el corte de rr1 con el split OOS actual. Leccion de metodo: un candidato que confirma con una ventana OOS de 2 semanas puede dejar de confirmar en la siguiente sin que el patron in-sample cambie -- tratar cualquier confirmacion OOS de una sola ventana como fragil hasta verla sostenerse en 2-3 rodadas de la ventana, no solo una."
    ],
    "beforeN": 23404,
    "afterN": 0,
    "before": {
      "n": 23404,
      "wrTP1": 46.0,
      "nSL": 10854,
      "nTO": 1794,
      "expR": 0.048,
      "pf": 1.1,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 32.9
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
    "date": "2026-10-07",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-10-06T16:45:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "NQ",
    "focus": {
      "sym": "NQ",
      "verdict": "GO",
      "window": "17:00-22:00 CT",
      "setup": {
        "es": "A+ pullback FVG 1h/4h 31427.75-31440.25, confluencia 6",
        "en": "A+ 1h/4h FVG pullback 31427.75-31440.25, confluence 6"
      },
      "trigger": {
        "es": "reclamo del FVG con cierre 15m de vuelta sobre 31433; o barrida de 31420 y reclaim rapido",
        "en": "FVG reclaim with a 15m close back above 31433; or a 31420 sweep with a fast reclaim"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 31420 (debajo del FVG)",
        "en": "5m close sustained below 31420 (below the FVG)"
      },
      "note": {
        "es": "3 sesiones seguidas sin dar este pullback; si llega, no lo persigas, espera el reclamo real",
        "en": "3 sessions in a row without this pullback; if it comes, don't chase it, wait for the real reclaim"
      }
    },
    "summary": {
      "es": [
        "!! GC: hit-rate de escenario A en 27% (n52) + FOMC Minutes manana 13:00 CT -> EM del dia +20%",
        "NQ: tendencia alcista dia 4, primera reversion de cierre real (-116pts desde el maximo); GO en el pullback 31427-440, aun sin tocar en 3 sesiones",
        "ES: unico indice que SI dio sus retests hoy; GO en VAL/IBL 7858-860",
        "GC: giro fallido (blow-off 6.8 ATR que no sostuvo); WAIT, conflicto de marcos reafirmado",
        "YM: giro SI sostenido; WAIT por el diario crudo (-3) sin confirmar, vigilar 2a sesion",
        "CL: giro completo sin catalizador, la 7a bisagra del mismo nivel; WAIT, conviccion baja hasta la 2a sesion",
        "mas limpio: NQ",
        "limite diario $1000 (3 stops) -> NQ y YM caben en full con la mejor A+; ES/GC/CL piden micros con ese stop"
      ],
      "en": [
        "!! GC: scenario-A hit rate at 27% (n52) + FOMC Minutes tomorrow 13:00 CT -> day's EM +20%",
        "NQ: uptrend day 4, first real closing reversal (-116pts off the high); GO on the 31427-440 pullback, still untouched after 3 sessions",
        "ES: the only index that gave its retests today; GO on VAL/IBL 7858-860",
        "GC: failed reversal (6.8 ATR blow-off that didn't hold); WAIT, frame conflict reasserted",
        "YM: reversal DID hold; WAIT because the raw daily indicator (-3) hasn't confirmed, watch for a 2nd session",
        "CL: complete reversal with no catalyst, the 7th hinge at the same level; WAIT, low conviction until a 2nd session",
        "cleanest: NQ",
        "daily limit $1000 (3 stops) -> NQ and YM fit full-size on their best A+; ES/GC/CL need micros with that stop"
      ]
    },
    "alarm": {
      "es": "GC: hit-rate de escenario A 27% (n52, bajo el umbral de 30%) + FOMC Minutes manana 13:00 CT -> EM del dia ajustado +20%",
      "en": "GC: scenario-A hit rate 27% (n52, be
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 10765,
  "by_verdict": {
    "AVOID": {
      "n": 1942,
      "wrTP1": 43.5,
      "nSL": 954,
      "nTO": 143,
      "expR": -0.004,
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
      "revAfterSL_rate": 33.5
    },
    "GO": {
      "n": 1214,
      "wrTP1": 51.5,
      "nSL": 494,
      "nTO": 95,
      "expR": 0.138,
      "pf": 1.32,
      "mfe_p25": 9.0,
      "mfe_p50": 23.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 42.7
    },
    "WAIT": {
      "n": 7609,
      "wrTP1": 46.8,
      "nSL": 3573,
      "nTO": 472,
      "expR": 0.05,
      "pf": 1.1,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 33.1
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": -0.004,
      "ci90": [
        -0.051,
        0.044
      ],
      "p_mean_le_0": 0.556,
      "n": 1841
    },
    "GO": {
      "expR": 0.138,
      "ci90": [
        0.08,
        0.196
      ],
      "p_mean_le_0": 0.0,
      "n": 1149
    },
    "WAIT": {
      "expR": 0.05,
      "ci90": [
        0.026,
        0.073
      ],
      "p_mean_le_0": 0.0,
      "n": 7385
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1942,
      "wrTP1": 43.5,
      "nSL": 954,
      "nTO": 143,
      "expR": -0.004,
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
      "revAfterSL_rate": 33.5
    },
    "GO_or_WAIT": {
      "n": 8823,
      "wrTP1": 47.5,
      "nSL": 4067,
      "nTO": 567,
      "expR": 0.062,
      "pf": 1.13,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 34.2
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": -0.004,
      "ci90": [
        -0.051,
        0.044
      ],
      "p_mean_le_0": 0.556,
      "n": 1841
    },
    "GO_or_WAIT": {
      "expR": 0.062,
      "ci90": [
        0.039,
        0.083
      ],
      "p_mean_le_0": 0.0,
      "n": 8534
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 30,
        "wrTP1": 53.3,
        "nSL": 11,
        "nTO": 3,
        "expR": 0.076,
        "pf": 1.2,
        "mfe_p25": 6.0,
        "mfe_p50": 14.0,
        "mfe_p75": 30.0,
        "winnerMAE_p75": 12.75,
        "winnerMAE_p90": 16.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 36.4
      },
      "GO": {
        "n": 13,
        "wrTP1": 53.8,
        "nSL": 4,
        "nTO": 2,
        "expR": -0.048,
        "pf": 0.87,
        "mfe_p25": 19.75,
        "mfe_p50": 28.5,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 28.0,
        "winnerMAE_p90": 39.6,
        "loserMFEbeforeSL_p50": 42.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 8.5,
        "entryZoneTk_p50": -48.0,
        "revAfterSL_rate": 25.0
      },
      "WAIT": {
        "n": 96,
        "wrTP1": 40.6,
        "nSL": 46,
        "nTO": 11,
        "expR": 0.009,
        "pf": 1.02,
        "mfe_p25": 5.75,
        "mfe_p50": 14.5,
        "mfe_p75": 25.25,
        "winnerMAE_p75": 11.5,
        "winnerMAE_p90": 21.60000000000001,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 15.2
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
        "n": 117,
        "wrTP1": 47.9,
        "nSL": 47,
        "nTO": 14,
        "expR": 0.032,
        "pf": 1.08,
        "mfe_p25": 6.0,
        "mfe_p50": 16.0,
        "mfe_p75": 39.5,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 25.5,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 21.3
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 1152,
        "wrTP1": 43.8,
        "nSL": 577,
        "nTO": 70,
        "expR": -0.034,
        "pf": 0.94,
        "mfe_p25": 7.0,
        "mfe_p50": 14.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.600000000000023,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 32.1
      },
      "GO": {
        "n": 768,
        "wrTP1": 51.6,
        "nSL": 337,
        "nTO": 35,
        "expR": 0.116,
        "pf": 1.26,
        "mfe_p25": 7.0,
        "mfe_p50": 20.0,
        "mfe_p75": 44.25,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 41.8
      },
      "WAIT": {
        "n": 4045,
        "wrTP1": 47.3,
        "nSL": 1885,
        "nTO": 245,
        "expR": 0.056,
        "pf": 1.12,
        "mfe_p25": 7.0,
        "mfe_p50": 17.0,
        "mfe_p75": 40.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 32.1
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 732,
        "wrTP1": 43.2,
        "nSL": 350,
        "nTO": 66,
        "expR": 0.057,
        "pf": 1.11,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 38.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 36.9
      },
      "GO": {
        "n": 429,
        "wrTP1": 51.0,
        "nSL": 152,
        "nTO": 58,
        "expR": 0.176,
        "pf": 1.44,
        "mfe_p25": 13.0,
        "mfe_p50": 31.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 18.5,
        "winnerMAE_p90": 28.200000000000017,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.5,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 45.4
      },
      "WAIT": {
        "n": 3351,
        "wrTP1": 46.4,
        "nSL": 1595,
        "nTO": 202,
        "expR": 0.045,
        "pf": 1.09,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 40.0,
        "winnerMAE_p75": 12.75,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 35.0
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
    "n": 21520,
    "wrTP1": 46.2,
    "nSL": 9927,
    "nTO": 1658,
    "expR": 0.052,
    "pf": 1.11,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 42.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.8
  },
  "shadow_ci90": {
    "expR": 0.052,
    "ci90": [
      0.038,
      0.066
    ],
    "p_mean_le_0": 0.0,
    "n": 20632
  },
  "raw_indicator": {
    "n": 23404,
    "wrTP1": 46.0,
    "nSL": 10854,
    "nTO": 1794,
    "expR": 0.048,
    "pf": 1.1,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.9
  },
  "raw_indicator_ci90": {
    "expR": 0.048,
    "ci90": [
      0.034,
      0.062
    ],
    "p_mean_le_0": 0.0,
    "n": 22419
  },
  "tier_ap_b_only": {
    "n": 12079,
    "wrTP1": 43.6,
    "nSL": 5805,
    "nTO": 1005,
    "expR": 0.05,
    "pf": 1.1,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 5.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 31.3
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.05,
    "ci90": [
      0.03,
      0.068
    ],
    "p_mean_le_0": 0.0,
    "n": 11556
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```

## Modo sombra por semana (gate: shadow_beats_raw 3 semanas seguidas, n>=60)
```json
{
  "2026-W36": {
    "shadow_n": 2572,
    "shadow_expR": -0.03,
    "raw_n": 2645,
    "raw_expR": -0.024,
    "shadow_beats_raw": false
  },
  "2026-W37": {
    "shadow_n": 4017,
    "shadow_expR": 0.092,
    "raw_n": 4757,
    "raw_expR": 0.076,
    "shadow_beats_raw": true
  },
  "2026-W38": {
    "shadow_n": 3875,
    "shadow_expR": 0.117,
    "raw_n": 4334,
    "raw_expR": 0.105,
    "shadow_beats_raw": true
  },
  "2026-W39": {
    "shadow_n": 4851,
    "shadow_expR": 0.06,
    "raw_n": 4919,
    "raw_expR": 0.058,
    "shadow_beats_raw": true
  },
  "2026-W40": {
    "shadow_n": 4665,
    "shadow_expR": 0.018,
    "raw_n": 5204,
    "raw_expR": 0.016,
    "shadow_beats_raw": true
  },
  "2026-W41": {
    "shadow_n": 1540,
    "shadow_expR": 0.009,
    "raw_n": 1545,
    "raw_expR": 0.011,
    "shadow_beats_raw": false
  }
}
```
