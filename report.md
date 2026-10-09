# Scalp CC · report 2026-10-09T01:15Z
- signals=26273 outcomes=25141 pares_resueltos=26205 pendientes=68 huerfanos=40

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: semana ya cerrada 2026-W36 bajo de n=3183 a n=2683 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W37 bajo de n=5389 a n=4846 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W38 bajo de n=4911 a n=4370 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W39 bajo de n=5355 a n=4945 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W40 bajo de n=5356 a n=5286 desde la corrida previa -- vigilar, puede ser deduplicacion.
- SIGID: 2000 sigId de senales y 1855 de outcomes colisionan (mismo sigId, receivedAt distinto); 1074 tienen result DISTINTO entre ocurrencias -> no es reenvio, son pares reales distintos fusionados en un sigId (ver nota en sigid_collision_report). 'last wins' descarta una ocurrencia y desplaza la otra a una semana posterior: probable causa de las alertas MUESTRA. Arreglar la generacion de sigId en el Pine (deltas en dias casi siempre multiplo de 7, sugiere bar_index que se reinicia semanalmente).
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.184 vs 0.049, delta 0.135 CI90 [0.103, 0.166], n 16516). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.162 vs 0.042, delta 0.12 CI90 [0.069, 0.174], n 5269). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.094 CI90 [0.046, 0.145], n 1642). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.052 CI90 [0.03, 0.075], n 8242). Consistente con la hipotesis original de agent-instructions.md.
- METODO: tus predicciones de direccion aciertan 33.3% (peor que un volado, n=6, MAE=0.268). Se mas conservador con 'cambio del mes' y marcar experimental mas tiempo antes de subir confianza.

- E[R] global: {"expR": 0.051, "ci90": [0.038, 0.064], "p_mean_le_0": 0.0, "n": 25101}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Integridad de sigId (colisiones, posible causa de alertas MUESTRA)
```json
{
  "signals": {
    "total_sigIds": 26273,
    "collided_sigIds": 2000,
    "collided_pct": 7.61,
    "delta_days_histogram": {
      "14": 645,
      "7": 626,
      "21": 334,
      "28": 199,
      "35": 44,
      "20": 32,
      "15": 30,
      "29": 24,
      "13": 22,
      "8": 12
    },
    "conflicting_result_n": 0,
    "conflicting_result_examples": []
  },
  "outcomes": {
    "total_sigIds": 25141,
    "collided_sigIds": 1855,
    "collided_pct": 7.38,
    "delta_days_histogram": {
      "14": 611,
      "7": 575,
      "21": 307,
      "28": 197,
      "35": 36,
      "20": 26,
      "15": 22,
      "29": 17,
      "13": 16,
      "8": 14
    },
    "conflicting_result_n": 1074,
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
| 1m/INV/LONG | 233 | 47.6 | 0.173 | 1.4 | 96 | 15.0 | 11.0 | 20.8 |
| 1m/INV/SHORT | 211 | 45.0 | 0.028 | 1.06 | 89 | 20.0 | 14.0 | 18.0 |
| 1m/RETEST/LONG | 9389 | 45.0 | 0.034 | 1.07 | 4474 | 15.0 | 10.0 | 27.8 |
| 1m/RETEST/SHORT | 6567 | 44.5 | 0.043 | 1.09 | 3030 | 18.0 | 11.0 | 29.0 |
| 2m/INV/LONG | 93 | 51.6 | 0.039 | 1.1 | 36 | 15.0 | 17.25 | 19.4 |
| 2m/INV/SHORT | 83 | 42.2 | 0.083 | 1.18 | 37 | 24.0 | 12.0 | 32.4 |
| 2m/RETEST/LONG | 4199 | 47.5 | 0.038 | 1.08 | 1947 | 19.0 | 14.0 | 38.6 |
| 2m/RETEST/SHORT | 2816 | 47.7 | 0.081 | 1.17 | 1277 | 23.0 | 13.0 | 39.3 |
| 5m/INV/LONG | 28 | 71.4 | 0.349 | 3.18 | 4 | 28.0 | 29.0 | 75.0 |
| 5m/INV/SHORT | 18 | 55.6 | 0.128 | 1.34 | 6 | 14.5 | 52.25 | 33.3 |
| 5m/RETEST/LONG | 1532 | 51.3 | 0.12 | 1.27 | 647 | 31.0 | 20.0 | 50.2 |
| 5m/RETEST/SHORT | 1036 | 47.6 | 0.088 | 1.19 | 444 | 31.0 | 19.0 | 36.5 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 1858 | 23.0 | -0.001 | 1.0 | 1185 | 26.0 | 13.0 | 18.6 |
| B | 11520 | 46.9 | 0.053 | 1.11 | 5237 | 18.0 | 12.0 | 33.7 |
| C | 12827 | 48.7 | 0.055 | 1.12 | 5665 | 18.0 | 12.0 | 34.2 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 9490 | 49.0 | 0.084 | 1.18 | 4284 | 13.0 | 9.0 | 35.6 |
| London | 3723 | 45.6 | 0.037 | 1.07 | 1843 | 19.0 | 12.0 | 33.6 |
| NY | 4652 | 44.4 | 0.044 | 1.09 | 2181 | 26.0 | 16.0 | 34.2 |
| Sin KZ | 8340 | 44.1 | 0.02 | 1.04 | 3779 | 21.0 | 14.0 | 27.4 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 6844 | 44.4 | 0.049 | 1.1 | 3162 | 21.0 | 14.0 | 29.8 |
| edge=0 | 10997 | 48.8 | 0.056 | 1.12 | 4949 | 16.0 | 11.0 | 36.3 |
| edge=1 | 8364 | 44.0 | 0.044 | 1.09 | 3976 | 19.0 | 14.0 | 29.9 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 7 | 57.1 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| aligned=1 | 26198 | 46.1 | 0.05 | 1.1 | 12086 | 18.0 | 12.0 | 32.5 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 9 | 44.4 | 0.042 | 1.08 | 5 | 21.0 | 9.0 | 20.0 |
| INV/LONG|edge=0 | 133 | 57.1 | 0.168 | 1.45 | 46 | 14.5 | 11.25 | 28.3 |
| INV/LONG|edge=1 | 212 | 46.7 | 0.145 | 1.34 | 85 | 16.0 | 15.5 | 18.8 |
| INV/SHORT|edge=-1 | 187 | 40.6 | -0.025 | 0.95 | 86 | 25.0 | 14.0 | 19.8 |
| INV/SHORT|edge=0 | 115 | 50.4 | 0.128 | 1.31 | 42 | 13.0 | 14.75 | 31.0 |
| INV/SHORT|edge=1 | 10 | 60.0 | 0.521 | 2.3 | 4 | 21.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 638 | 53.6 | 0.169 | 1.4 | 258 | 15.0 | 11.75 | 40.3 |
| RETEST/LONG|edge=0 | 6594 | 48.8 | 0.034 | 1.07 | 3027 | 16.0 | 11.0 | 35.9 |
| RETEST/LONG|edge=1 | 7888 | 43.7 | 0.041 | 1.08 | 3783 | 19.0 | 14.0 | 29.8 |
| RETEST/SHORT|edge=-1 | 6010 | 43.5 | 0.039 | 1.08 | 2813 | 22.0 | 14.0 | 29.1 |
| RETEST/SHORT|edge=0 | 4155 | 48.5 | 0.086 | 1.19 | 1834 | 18.0 | 11.0 | 37.1 |
| RETEST/SHORT|edge=1 | 254 | 51.2 | 0.032 | 1.07 | 104 | 12.0 | 7.75 | 41.3 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 114 | 46.5 | 0.204 | 1.46 | 48 | 15.0 | 15.0 | 12.5 |
| INV/LONG|tier=C | 240 | 52.5 | 0.125 | 1.32 | 88 | 16.0 | 12.0 | 27.3 |
| INV/SHORT|tier=B | 105 | 43.8 | -0.016 | 0.97 | 49 | 20.5 | 12.0 | 10.2 |
| INV/SHORT|tier=C | 207 | 45.4 | 0.083 | 1.19 | 83 | 21.0 | 20.0 | 30.1 |
| RETEST/LONG|tier=A+ | 1113 | 22.3 | -0.025 | 0.96 | 734 | 23.0 | 11.0 | 18.7 |
| RETEST/LONG|tier=B | 6485 | 47.2 | 0.066 | 1.14 | 2958 | 17.0 | 12.0 | 34.8 |
| RETEST/LONG|tier=C | 7522 | 49.1 | 0.034 | 1.07 | 3376 | 17.0 | 13.0 | 34.2 |
| RETEST/SHORT|tier=A+ | 745 | 24.0 | 0.036 | 1.05 | 451 | 29.0 | 14.0 | 18.6 |
| RETEST/SHORT|tier=B | 4816 | 46.6 | 0.034 | 1.07 | 2182 | 19.0 | 12.0 | 33.2 |
| RETEST/SHORT|tier=C | 4858 | 48.1 | 0.084 | 1.18 | 2118 | 19.0 | 12.0 | 34.7 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 354 | 50.6 | 0.151 | 1.37 | 136 | 15.0 | 13.5 | 22.1 |
| INV/SHORT|aligned=1 | 312 | 44.9 | 0.048 | 1.11 | 132 | 21.0 | 14.25 | 22.7 |
| RETEST/LONG|aligned=0 | 7 | 57.1 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| RETEST/LONG|aligned=1 | 15113 | 46.3 | 0.043 | 1.09 | 7067 | 17.0 | 12.0 | 32.8 |
| RETEST/SHORT|aligned=1 | 10419 | 45.7 | 0.058 | 1.12 | 4751 | 20.0 | 12.0 | 32.5 |

## Autopsia de SL
n_losses=12087  causas: RR-bajo×4472, contra-estructura×3990, stop-en-el-minimo×3924, killzone-Asia-largo×2637, sin-nivel-detras×2229, estirado×2016, chop×1821, SL-muy-pegado×1517, sin-causa-clara×1355, contra-sesgo×1
- INV/LONG (n=136): killzone-Asia-largo×61, RR-bajo×52, contra-estructura×44, stop-en-el-minimo×30, estirado×29, chop×19, sin-nivel-detras×18, SL-muy-pegado×12, sin-causa-clara×7
- INV/SHORT (n=132): RR-bajo×56, contra-estructura×39, estirado×31, stop-en-el-minimo×30, SL-muy-pegado×22, sin-causa-clara×21, chop×16, sin-nivel-detras×11
- RETEST/LONG (n=7068): RR-bajo×2642, killzone-Asia-largo×2576, contra-estructura×2405, stop-en-el-minimo×2321, sin-nivel-detras×1378, estirado×1182, chop×1128, SL-muy-pegado×843, sin-causa-clara×622, contra-sesgo×1
- RETEST/SHORT (n=4751): RR-bajo×1722, stop-en-el-minimo×1543, contra-estructura×1502, sin-nivel-detras×822, estirado×774, sin-causa-clara×705, chop×658, SL-muy-pegado×640

## Autopsia de SL · semana 2026-W41 (para revision semanal)
n_losses=1901  causas: RR-bajo×699, contra-estructura×618, stop-en-el-minimo×577, killzone-Asia-largo×506, sin-nivel-detras×432, estirado×297, chop×272, SL-muy-pegado×255, sin-causa-clara×200
ejemplos por causa: {"RR-bajo": ["NQ-2-22865-L", "GC-1-25190-L", "NQ-1-25261-L", "ES-5-20105-L", "ES-5-20108-L"], "contra-estructura": ["NQ-5-20112-L", "CL-5-20267-L", "GC-1-26356-L", "CL-1-28001-S", "GC-1-28794-S"], "stop-en-el-minimo": ["NQ-1-25261-L", "ES-5-20105-L", "ES-5-20108-L", "NQ-5-20112-L", "CL-2-23172-L"]}

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
    "n": 25088,
    "naive_expR": 0.051,
    "managed_expR": 0.13,
    "delta": 0.079,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 46.3,
    "fill_full_pct": 32.7,
    "m1_rate": 37.4,
    "m2_rate": 22.9,
    "m3_rate": 12.0,
    "beAfterM1_rate": 18.1
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 223,
      "naive_expR": 0.173,
      "managed_expR": 0.255,
      "delta": 0.082,
      "avgEntryBetterTk_p50": 2.2,
      "fill_t3plus_pct": 48.9,
      "fill_full_pct": 36.8,
      "m1_rate": 39.9,
      "m2_rate": 24.7,
      "m3_rate": 11.2,
      "beAfterM1_rate": 19.7
    },
    "1m/INV/SHORT": {
      "n": 199,
      "naive_expR": 0.028,
      "managed_expR": 0.241,
      "delta": 0.213,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 51.8,
      "fill_full_pct": 38.7,
      "m1_rate": 38.2,
      "m2_rate": 25.1,
      "m3_rate": 12.6,
      "beAfterM1_rate": 15.6
    },
    "1m/RETEST/LONG": {
      "n": 9098,
      "naive_expR": 0.034,
      "managed_expR": 0.126,
      "delta": 0.093,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 48.0,
      "fill_full_pct": 33.9,
      "m1_rate": 37.4,
      "m2_rate": 22.5,
      "m3_rate": 11.7,
      "beAfterM1_rate": 17.6
    },
    "1m/RETEST/SHORT": {
      "n": 6199,
      "naive_expR": 0.043,
      "managed_expR": 0.164,
      "delta": 0.121,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 48.2,
      "fill_full_pct": 33.7,
      "m1_rate": 38.9,
      "m2_rate": 24.6,
      "m3_rate": 13.2,
      "beAfterM1_rate": 18.0
    },
    "2m/INV/LONG": {
      "n": 89,
      "naive_expR": 0.039,
      "managed_expR": 0.091,
      "delta": 0.051,
      "avgEntryBetterTk_p50": 3.8,
      "fill_t3plus_pct": 57.3,
      "fill_full_pct": 43.8,
      "m1_rate": 27.0,
      "m2_rate": 19.1,
      "m3_rate": 5.6,
      "beAfterM1_rate": 10.1
    },
    "2m/INV/SHORT": {
      "n": 80,
      "naive_expR": 0.083,
      "managed_expR": 0.157,
      "delta": 0.074,
      "avgEntryBetterTk_p50": 3.3,
      "fill_t3plus_pct": 47.5,
      "fill_full_pct": 35.0,
      "m1_rate": 33.8,
      "m2_rate": 23.8,
      "m3_rate": 13.8,
      "beAfterM1_rate": 13.8
    },
    "2m/RETEST/LONG": {
      "n": 4049,
      "naive_expR": 0.038,
      "managed_expR": 0.079,
      "delta": 0.041,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 45.4,
      "fill_full_pct": 31.9,
      "m1_rate": 35.5,
      "m2_rate": 20.7,
      "m3_rate": 10.8,
      "beAfterM1_rate": 18.4
    },
    "2m/RETEST/SHORT": {
      "n": 2703,
      "naive_expR": 0.081,
      "managed_expR": 0.145,
      "delta": 0.064,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 44.4,
      "fill_full_pct": 31.7,
      "m1_rate": 38.0,
      "m2_rate": 23.5,
      "m3_rate": 12.5,
      "beAfterM1_rate": 19.8
    },
    "5m/INV/LONG": {
      "n": 25,
      "naive_expR": 0.349,
      "managed_expR": 0.404,
      "delta": 0.055,
      "avgEntryBetterTk_p50": 2.5,
      "fill_t3plus_pct": 36.0,
      "fill_full_pct": 24.0,
      "m1_rate": 16.0,
      "m2_rate": 8.0,
      "m3_rate": 4.0,
      "beAfterM1_rate": 12.0
    },
    "5m/INV/SHORT": {
      "n": 16,
      "naive_expR": 0.128,
      "managed_expR": 0.208,
      "delta": 0.08,
      "avgEntryBetterTk_p50": 7.7,
      "fill_t3plus_pct": 62.5,
      "fill_full_pct": 43.8,
      "m1_rate": 18.8,
      "m2_rate": 12.5,
      "m3_rate": 12.5,
      "beAfterM1_rate": 6.2
    },
    "5m/RETEST/LONG": {
      "n": 1452,
      "naive_expR": 0.12,
      "managed_expR": 0.095,
      "delta": -0.025,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 35.3,
      "fill_full_pct": 25.0,
      "m1_rate": 36.2,
      "m2_rate": 22.8,
      "m3_rate": 11.9,
      "beAfterM1_rate": 19.2
    },
    "5m/RETEST/SHORT": {
      "n": 955,
      "naive_expR": 0.087,
      "managed_expR": 0.105,
      "delta": 0.018,
      "avgEntryBetterTk_p50": 4.9,
      "fill_t3plus_pct": 40.7,
      "fill_full_pct": 28.5,
      "m1_rate": 36.8,
      "m2_rate": 22.5,
      "m3_rate": 12.0,
      "beAfterM1_rate": 19.0
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 22405,
    "layer_expR": 0.049,
    "orig_expR": 0.176,
    "delta_orig_minus_layer": 0.128,
    "delta_ci90": [
      0.103,
      0.154
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 47.9,
    "orig_wrTP1": 33.0,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 9.0,
    "orig_wider_pct": 3.7,
    "orig_saved_from_SL": 26,
    "orig_caused_SL": 3372
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 7,
  "invalid_by_seg": {
    "1m/RETEST/LONG": 4,
    "1m/RETEST/SHORT": 3
  },
  "by_basis": {
    "candle1": {
      "n": 620,
      "layer_expR": 0.103,
      "orig_expR": 0.099,
      "delta_orig_minus_layer": -0.004,
      "delta_ci90": [
        -0.167,
        0.171
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.2,
      "orig_wrTP1": 25.6,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 153
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
      "n": 16516,
      "layer_expR": 0.049,
      "orig_expR": 0.184,
      "delta_orig_minus_layer": 0.135,
      "delta_ci90": [
        0.103,
        0.166
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.2,
      "orig_wrTP1": 33.5,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 4.1,
      "orig_saved_from_SL": 25,
      "orig_caused_SL": 2460
    },
    "retestBar2": {
      "n": 5269,
      "layer_expR": 0.042,
      "orig_expR": 0.162,
      "delta_orig_minus_layer": 0.12,
      "delta_ci90": [
        0.069,
        0.174
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.7,
      "orig_wrTP1": 32.3,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 759
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 223,
      "layer_expR": 0.173,
      "orig_expR": 0.295,
      "delta_orig_minus_layer": 0.121,
      "delta_ci90": [
        -0.129,
        0.395
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.8,
      "orig_wrTP1": 25.6,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 54
    },
    "1m/INV/SHORT": {
      "n": 189,
      "layer_expR": 0.027,
      "orig_expR": -0.157,
      "delta_orig_minus_layer": -0.184,
      "delta_ci90": [
        -0.415,
        0.083
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.1,
      "orig_wrTP1": 21.7,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 1.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 48
    },
    "1m/RETEST/LONG": {
      "n": 7938,
      "layer_expR": 0.03,
      "orig_expR": 0.144,
      "delta_orig_minus_layer": 0.114,
      "delta_ci90": [
        0.069,
        0.16
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.9,
      "orig_wrTP1": 28.8,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 1.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 1355
    },
    "1m/RETEST/SHORT": {
      "n": 5385,
      "layer_expR": 0.039,
      "orig_expR": 0.158,
      "delta_orig_minus_layer": 0.119,
      "delta_ci90": [
        0.07,
        0.173
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.6,
      "orig_wrTP1": 32.2,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 777
    },
    "2m/INV/LONG": {
      "n": 89,
      "layer_expR": 0.039,
      "orig_expR": 0.376,
      "delta_orig_minus_layer": 0.337,
      "delta_ci90": [
        -0.29,
        1.126
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 53.9,
      "orig_wrTP1": 27.0,
      "slTk_p50": 27.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 5.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 24
    },
    "2m/INV/SHORT": {
      "n": 79,
      "layer_expR": 0.078,
      "orig_expR": 0.142,
      "delta_orig_minus_layer": 0.064,
      "delta_ci90": [
        -0.333,
        0.523
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 43.0,
      "orig_wrTP1": 29.1,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 12
    },
    "2m/RETEST/LONG": {
      "n": 3734,
      "layer_expR": 0.035,
      "orig_expR": 0.159,
      "delta_orig_minus_layer": 0.125,
      "delta_ci90": [
        0.071,
        0.179
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.3,
      "orig_wrTP1": 35.4,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 524
    },
    "2m/RETEST/SHORT": {
      "n": 2424,
      "layer_expR": 0.09,
      "orig_expR": 0.205,
      "delta_orig_minus_layer": 0.115,
      "delta_ci90": [
        0.048,
        0.184
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.9,
      "orig_wrTP1": 35.7,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.8,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 347
    },
    "5m/INV/LONG": {
      "n": 25,
      "layer_expR": 0.349,
      "orig_expR": -0.47,
      "delta_orig_minus_layer": -0.819,
      "delta_ci90": [
        -1.196,
        -0.48
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 80.0,
      "orig_wrTP1": 36.0,
      "slTk_p50": 31.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 12.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 11
    },
    "5m/INV/SHORT": {
      "n": 15,
      "layer_expR": 0.102,
      "orig_expR": -0.512,
      "delta_orig_minus_layer": -0.614,
      "delta_ci90": [
        -0.931,
        -0.301
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 60.0,
      "orig_wrTP1": 33.3,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 20.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 4
    },
    "5m/RETEST/LONG": {
      "n": 1402,
      "layer_expR": 0.114,
      "orig_expR": 0.36,
      "delta_orig_minus_layer": 0.247,
      "delta_ci90": [
        0.133,
        0.376
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.1,
      "orig_wrTP1": 45.0,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 19.0,
      "orig_wider_pct": 14.9,
      "orig_saved_from_SL": 10,
      "orig_caused_SL": 138
    },
    "5m/RETEST/SHORT": {
      "n": 902,
      "layer_expR": 0.083,
      "orig_expR": 0.332,
      "delta_orig_minus_layer": 0.249,
      "delta_ci90": [
        0.078,
        0.44
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.2,
      "orig_wrTP1": 43.5,
      "slTk_p50": 30.0,
      "slOrigTk_p50": 22.0,
      "orig_wider_pct": 19.3,
      "orig_saved_from_SL": 8,
      "orig_caused_SL": 78
    }
  },
  "since_change": {
    "changeDate": "2026-09-26",
    "n": 8338,
    "by_tf_kind_side": {
      "1m/INV/LONG": {
        "n": 83,
        "layer_expR": 0.206,
        "orig_expR": 0.753,
        "delta_orig_minus_layer": 0.547,
        "delta_ci90": [
          0.096,
          1.063
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 54.2,
        "orig_wrTP1": 30.1,
        "slTk_p50": 17.0,
        "slOrigTk_p50": 3.0,
        "orig_wider_pct": 2.4,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 20
      },
      "1m/INV/SHORT": {
        "n": 79,
        "layer_expR": 0.054,
        "orig_expR": -0.328,
        "delta_orig_minus_layer": -0.382,
        "delta_ci90": [
          -0.627,
          -0.126
        ],
        "delta_beats_zero": false,
        "delta_below_zero": true,
        "layer_wrTP1": 44.3,
        "orig_wrTP1": 19.0,
        "slTk_p50": 18.0,
        "slOrigTk_p50": 5.0,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 20
      },
      "1m/RETEST/LONG": {
        "n": 2801,
        "layer_expR": -0.035,
        "orig_expR": 0.028,
        "delta_orig_minus_layer": 0.063,
        "delta_ci90": [
          -0.009,
          0.143
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 44.6,
        "orig_wrTP1": 27.5,
        "slTk_p50": 17.0,
        "slOrigTk_p50": 7.0,
        "orig_wider_pct": 1.1,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 481
      },
      "1m/RETEST/SHORT": {
        "n": 2079,
        "layer_expR": 0.046,
        "orig_expR": 0.139,
        "delta_orig_minus_layer": 0.093,
        "delta_ci90": [
          0.022,
          0.166
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 46.7,
        "orig_wrTP1": 32.2,
        "slTk_p50": 19.0,
        "slOrigTk_p50": 9.0,
        "orig_wider_pct": 2.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 302
      },
      "2m/INV/LONG": {
        "n": 32,
        "layer_expR": 0.098,
        "orig_expR": -0.427,
        "delta_orig_minus_layer": -0.525,
        "delta_ci90": [
          -0.907,
          -0.134
        ],
        "delta_beats_zero": false,
        "delta_below_zero": true,
        "layer_wrTP1": 59.4,
        "orig_wrTP1": 25.0,
        "slTk_p50": 31.5,
        "slOrigTk_p50": 9.5,
        "orig_wider_pct": 3.1,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 11
      },
      "2m/INV/SHORT": {
        "n": 26,
        "layer_expR": 0.081,
        "orig_expR": 0.035,
        "delta_orig_minus_layer": -0.046,
        "delta_ci90": [
          -0.832,
          0.889
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 50.0,
        "orig_wrTP1": 26.9,
        "slTk_p50": 25.0,
        "slOrigTk_p50": 6.0,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 6
      },
      "2m/RETEST/LONG": {
        "n": 1377,
        "layer_expR": 0.01,
        "orig_expR": 0.088,
        "delta_orig_minus_layer": 0.078,
        "delta_ci90": [
          0.006,
          0.157
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 49.7,
        "orig_wrTP1": 34.1,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 10.0,
        "orig_wider_pct": 3.8,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 215
      },
      "2m/RETEST/SHORT": {
        "n": 952,
        "layer_expR": 0.102,
        "orig_expR": 0.138,
        "delta_orig_minus_layer": 0.037,
        "delta_ci90": [
          -0.05,
          0.123
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 48.5,
        "orig_wrTP1": 33.7,
        "slTk_p50": 22.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 3.5,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 142
      },
      "5m/INV/LONG": {
        "n": 10,
        "layer_expR": 0.109,
        "orig_expR": -0.498,
        "delta_orig_minus_layer": -0.607,
        "delta_ci90": [
          -1.008,
          -0.246
        ],
        "delta_beats_zero": false,
        "delta_below_zero": true,
        "layer_wrTP1": 80.0,
        "orig_wrTP1": 40.0,
        "slTk_p50": 26.5,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 10.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 4
      },
      "5m/INV/SHORT": {
        "n": 5,
        "layer_expR": -0.452,
        "orig_expR": -0.666,
        "delta_orig_minus_layer": -0.214,
        "delta_ci90": [
          null,
          null
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 40.0,
        "orig_wrTP1": 20.0,
        "slTk_p50": 22.0,
        "slOrigTk_p50": 3.0,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 1
      },
      "5m/RETEST/LONG": {
        "n": 533,
        "layer_expR": 0.084,
        "orig_expR": 0.315,
        "delta_orig_minus_layer": 0.231,
        "delta_ci90": [
          0.023,
          0.468
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 54.0,
        "orig_wrTP1": 45.2,
        "slTk_p50": 29.0,
        "slOrigTk_p50": 18.0,
        "orig_wider_pct": 12.9,
        "orig_saved_from_SL": 4,
        "orig_caused_SL": 51
      },
      "5m/RETEST/SHORT": {
        "n": 361,
        "layer_expR": 0.043,
        "orig_expR": 0.077,
        "delta_orig_minus_layer": 0.034,
        "delta_ci90": [
          -0.06,
          0.142
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 50.4,
        "orig_wrTP1": 42.9,
        "slTk_p50": 30.0,
        "slOrigTk_p50": 21.0,
        "orig_wider_pct": 16.1,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 29
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
      "n": 9060,
      "wrTP1": 46.6,
      "nSL": 4257,
      "nTO": 577,
      "expR": 0.026,
      "pf": 1.05,
      "mfe_p25": 6.0,
      "mfe_p50": 15.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 29.2,
      "ci90": {
        "expR": 0.026,
        "ci90": [
          0.005,
          0.048
        ],
        "p_mean_le_0": 0.021,
        "n": 8778
      }
    },
    "cuts": {
      "1.0": {
        "n": 4409,
        "wrTP1": 30.1,
        "nSL": 2656,
        "nTO": 425,
        "expR": 0.006,
        "pf": 1.01,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 44.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 20.6,
        "ci90": {
          "expR": 0.006,
          "ci90": [
            -0.032,
            0.043
          ],
          "p_mean_le_0": 0.413,
          "n": 4239
        }
      },
      "1.2": {
        "n": 3647,
        "wrTP1": 27.5,
        "nSL": 2259,
        "nTO": 385,
        "expR": 0.015,
        "pf": 1.02,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.9,
        "ci90": {
          "expR": 0.015,
          "ci90": [
            -0.028,
            0.058
          ],
          "p_mean_le_0": 0.301,
          "n": 3502
        }
      },
      "1.3": {
        "n": 3307,
        "wrTP1": 26.1,
        "nSL": 2077,
        "nTO": 368,
        "expR": 0.014,
        "pf": 1.02,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 16.3,
        "ci90": {
          "expR": 0.014,
          "ci90": [
            -0.031,
            0.058
          ],
          "p_mean_le_0": 0.304,
          "n": 3167
        }
      },
      "1.5": {
        "n": 2791,
        "wrTP1": 23.2,
        "nSL": 1811,
        "nTO": 333,
        "expR": -0.001,
        "pf": 1.0,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 14.0,
        "ci90": {
          "expR": -0.001,
          "ci90": [
            -0.05,
            0.053
          ],
          "p_mean_le_0": 0.506,
          "n": 2672
        }
      },
      "2.0": {
        "n": 1819,
        "wrTP1": 17.2,
        "nSL": 1238,
        "nTO": 269,
        "expR": -0.021,
        "pf": 0.97,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 9.25,
        "winnerMAE_p90": 18.900000000000034,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 10.6,
        "ci90": {
          "expR": -0.021,
          "ci90": [
            -0.088,
            0.046
          ],
          "p_mean_le_0": 0.7,
          "n": 1739
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 6283,
      "wrTP1": 46.5,
      "nSL": 2838,
      "nTO": 522,
      "expR": 0.05,
      "pf": 1.1,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 35.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 31.0,
      "ci90": {
        "expR": 0.05,
        "ci90": [
          0.025,
          0.074
        ],
        "p_mean_le_0": 0.001,
        "n": 5942
      }
    },
    "cuts": {
      "1.0": {
        "n": 3048,
        "wrTP1": 30.8,
        "nSL": 1741,
        "nTO": 368,
        "expR": 0.052,
        "pf": 1.08,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 21.7,
        "ci90": {
          "expR": 0.052,
          "ci90": [
            0.008,
            0.097
          ],
          "p_mean_le_0": 0.026,
          "n": 2835
        }
      },
      "1.2": {
        "n": 2514,
        "wrTP1": 28.1,
        "nSL": 1469,
        "nTO": 339,
        "expR": 0.067,
        "pf": 1.11,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 19.4,
        "ci90": {
          "expR": 0.067,
          "ci90": [
            0.014,
            0.121
          ],
          "p_mean_le_0": 0.021,
          "n": 2326
        }
      },
      "1.3": {
        "n": 2307,
        "wrTP1": 26.7,
        "nSL": 1364,
        "nTO": 328,
        "expR": 0.069,
        "pf": 1.11,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 18.3,
        "ci90": {
          "expR": 0.069,
          "ci90": [
            0.012,
            0.126
          ],
          "p_mean_le_0": 0.025,
          "n": 2130
        }
      },
      "1.5": {
        "n": 1966,
        "wrTP1": 24.6,
        "nSL": 1187,
        "nTO": 295,
        "expR": 0.075,
        "pf": 1.11,
        "mfe_p25": 11.0,
        "mfe_p50": 26.0,
        "mfe_p75": 52.75,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 16.1,
        "ci90": {
          "expR": 0.075,
          "ci90": [
            0.011,
            0.139
          ],
          "p_mean_le_0": 0.024,
          "n": 1814
        }
      },
      "2.0": {
        "n": 1336,
        "wrTP1": 19.5,
        "nSL": 845,
        "nTO": 230,
        "expR": 0.064,
        "pf": 1.09,
        "mfe_p25": 11.0,
        "mfe_p50": 27.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 11.7,
        "ci90": {
          "expR": 0.064,
          "ci90": [
            -0.021,
            0.145
          ],
          "p_mean_le_0": 0.114,
          "n": 1230
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 4081,
      "wrTP1": 48.8,
      "nSL": 1875,
      "nTO": 214,
      "expR": 0.027,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 42.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 27.90000000000009,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 40.1,
      "ci90": {
        "expR": 0.027,
        "ci90": [
          -0.003,
          0.056
        ],
        "p_mean_le_0": 0.071,
        "n": 3939
      }
    },
    "cuts": {
      "1.0": {
        "n": 1832,
        "wrTP1": 30.8,
        "nSL": 1111,
        "nTO": 157,
        "expR": -0.002,
        "pf": 1.0,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 32.5,
        "ci90": {
          "expR": -0.002,
          "ci90": [
            -0.059,
            0.057
          ],
          "p_mean_le_0": 0.522,
          "n": 1741
        }
      },
      "1.2": {
        "n": 1498,
        "wrTP1": 27.6,
        "nSL": 945,
        "nTO": 139,
        "expR": -0.007,
        "pf": 0.99,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.9,
        "ci90": {
          "expR": -0.007,
          "ci90": [
            -0.073,
            0.064
          ],
          "p_mean_le_0": 0.577,
          "n": 1420
        }
      },
      "1.3": {
        "n": 1363,
        "wrTP1": 26.5,
        "nSL": 868,
        "nTO": 134,
        "expR": 0.001,
        "pf": 1.0,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 28.9,
        "ci90": {
          "expR": 0.001,
          "ci90": [
            -0.074,
            0.076
          ],
          "p_mean_le_0": 0.5,
          "n": 1290
        }
      },
      "1.5": {
        "n": 1120,
        "wrTP1": 22.9,
        "nSL": 736,
        "nTO": 128,
        "expR": -0.018,
        "pf": 0.97,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 62.25,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.5,
        "revAfterSL_rate": 26.8,
        "ci90": {
          "expR": -0.018,
          "ci90": [
            -0.103,
            0.07
          ],
          "p_mean_le_0": 0.611,
          "n": 1052
        }
      },
      "2.0": {
        "n": 700,
        "wrTP1": 18.4,
        "nSL": 475,
        "nTO": 96,
        "expR": 0.02,
        "pf": 1.03,
        "mfe_p25": 11.0,
        "mfe_p50": 26.5,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.200000000000003,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 21.7,
        "ci90": {
          "expR": 0.02,
          "ci90": [
            -0.099,
            0.142
          ],
          "p_mean_le_0": 0.398,
          "n": 650
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 2663,
      "wrTP1": 50.4,
      "nSL": 1169,
      "nTO": 153,
      "expR": 0.096,
      "pf": 1.21,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 45.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 42.9,
      "ci90": {
        "expR": 0.096,
        "ci90": [
          0.057,
          0.135
        ],
        "p_mean_le_0": 0.0,
        "n": 2568
      }
    },
    "cuts": {
      "1.0": {
        "n": 1233,
        "wrTP1": 34.0,
        "nSL": 713,
        "nTO": 101,
        "expR": 0.118,
        "pf": 1.2,
        "mfe_p25": 16.0,
        "mfe_p50": 31.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 26.19999999999999,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 34.8,
        "ci90": {
          "expR": 0.118,
          "ci90": [
            0.043,
            0.194
          ],
          "p_mean_le_0": 0.005,
          "n": 1183
        }
      },
      "1.2": {
        "n": 1015,
        "wrTP1": 30.5,
        "nSL": 612,
        "nTO": 93,
        "expR": 0.117,
        "pf": 1.19,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 26.100000000000023,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 31.0,
        "ci90": {
          "expR": 0.117,
          "ci90": [
            0.035,
            0.202
          ],
          "p_mean_le_0": 0.009,
          "n": 971
        }
      },
      "1.3": {
        "n": 926,
        "wrTP1": 29.0,
        "nSL": 568,
        "nTO": 89,
        "expR": 0.114,
        "pf": 1.18,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.8,
        "ci90": {
          "expR": 0.114,
          "ci90": [
            0.023,
            0.206
          ],
          "p_mean_le_0": 0.021,
          "n": 885
        }
      },
      "1.5": {
        "n": 770,
        "wrTP1": 26.0,
        "nSL": 490,
        "nTO": 80,
        "expR": 0.108,
        "pf": 1.16,
        "mfe_p25": 17.0,
        "mfe_p50": 33.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 28.6,
        "ci90": {
          "expR": 0.108,
          "ci90": [
            0.002,
            0.208
          ],
          "p_mean_le_0": 0.047,
          "n": 737
        }
      },
      "2.0": {
        "n": 510,
        "wrTP1": 21.6,
        "nSL": 335,
        "nTO": 65,
        "expR": 0.15,
        "pf": 1.22,
        "mfe_p25": 17.0,
        "mfe_p50": 36.5,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 26.10000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 23.9,
        "ci90": {
          "expR": 0.15,
          "ci90": [
            0.014,
            0.29
          ],
          "p_mean_le_0": 0.037,
          "n": 486
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 1469,
      "wrTP1": 53.5,
      "nSL": 601,
      "nTO": 82,
      "expR": 0.136,
      "pf": 1.32,
      "mfe_p25": 12.0,
      "mfe_p50": 30.0,
      "mfe_p75": 66.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 42.0,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -34.0,
      "revAfterSL_rate": 54.1,
      "ci90": {
        "expR": 0.136,
        "ci90": [
          0.083,
          0.189
        ],
        "p_mean_le_0": 0.0,
        "n": 1396
      }
    },
    "cuts": {
      "1.0": {
        "n": 612,
        "wrTP1": 38.6,
        "nSL": 324,
        "nTO": 52,
        "expR": 0.249,
        "pf": 1.44,
        "mfe_p25": 17.0,
        "mfe_p50": 41.0,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 35.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.5,
        "revAfterSL_rate": 50.3,
        "ci90": {
          "expR": 0.249,
          "ci90": [
            0.143,
            0.356
          ],
          "p_mean_le_0": 0.0,
          "n": 569
        }
      },
      "1.2": {
        "n": 506,
        "wrTP1": 36.4,
        "nSL": 274,
        "nTO": 48,
        "expR": 0.278,
        "pf": 1.47,
        "mfe_p25": 18.0,
        "mfe_p50": 41.0,
        "mfe_p75": 82.5,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 31.400000000000034,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 48.2,
        "ci90": {
          "expR": 0.278,
          "ci90": [
            0.154,
            0.407
          ],
          "p_mean_le_0": 0.0,
          "n": 467
        }
      },
      "1.3": {
        "n": 456,
        "wrTP1": 33.8,
        "nSL": 259,
        "nTO": 43,
        "expR": 0.247,
        "pf": 1.4,
        "mfe_p25": 18.0,
        "mfe_p50": 40.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 17.75,
        "winnerMAE_p90": 28.400000000000034,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -31.0,
        "revAfterSL_rate": 46.7,
        "ci90": {
          "expR": 0.247,
          "ci90": [
            0.118,
            0.388
          ],
          "p_mean_le_0": 0.002,
          "n": 422
        }
      },
      "1.5": {
        "n": 377,
        "wrTP1": 31.0,
        "nSL": 223,
        "nTO": 37,
        "expR": 0.245,
        "pf": 1.38,
        "mfe_p25": 18.0,
        "mfe_p50": 38.5,
        "mfe_p75": 82.25,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 27.80000000000001,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 45.7,
        "ci90": {
          "expR": 0.245,
          "ci90": [
            0.103,
            0.401
          ],
          "p_mean_le_0": 0.004,
          "n": 348
        }
      },
      "2.0": {
        "n": 241,
        "wrTP1": 24.9,
        "nSL": 153,
        "nTO": 28,
        "expR": 0.223,
        "pf": 1.32,
        "mfe_p25": 18.0,
        "mfe_p50": 43.0,
        "mfe_p75": 93.0,
        "winnerMAE_p75": 12.5,
        "winnerMAE_p90": 19.200000000000003,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 39.2,
        "ci90": {
          "expR": 0.223,
          "ci90": [
            -0.008,
            0.447
          ],
          "p_mean_le_0": 0.054,
          "n": 221
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 976,
      "wrTP1": 50.5,
      "nSL": 405,
      "nTO": 78,
      "expR": 0.109,
      "pf": 1.24,
      "mfe_p25": 14.0,
      "mfe_p50": 30.0,
      "mfe_p75": 57.0,
      "winnerMAE_p75": 19.0,
      "winnerMAE_p90": 37.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -28.0,
      "revAfterSL_rate": 39.8,
      "ci90": {
        "expR": 0.109,
        "ci90": [
          0.043,
          0.173
        ],
        "p_mean_le_0": 0.005,
        "n": 908
      }
    },
    "cuts": {
      "1.0": {
        "n": 426,
        "wrTP1": 33.8,
        "nSL": 236,
        "nTO": 46,
        "expR": 0.151,
        "pf": 1.25,
        "mfe_p25": 19.0,
        "mfe_p50": 40.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 20.25,
        "winnerMAE_p90": 36.70000000000002,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 32.6,
        "ci90": {
          "expR": 0.151,
          "ci90": [
            0.027,
            0.283
          ],
          "p_mean_le_0": 0.02,
          "n": 389
        }
      },
      "1.2": {
        "n": 347,
        "wrTP1": 30.5,
        "nSL": 201,
        "nTO": 40,
        "expR": 0.159,
        "pf": 1.25,
        "mfe_p25": 19.0,
        "mfe_p50": 40.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 28.9,
        "ci90": {
          "expR": 0.159,
          "ci90": [
            0.009,
            0.316
          ],
          "p_mean_le_0": 0.043,
          "n": 315
        }
      },
      "1.3": {
        "n": 321,
        "wrTP1": 30.8,
        "nSL": 186,
        "nTO": 36,
        "expR": 0.176,
        "pf": 1.28,
        "mfe_p25": 21.0,
        "mfe_p50": 41.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 35.400000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 28.0,
        "ci90": {
          "expR": 0.176,
          "ci90": [
            0.018,
            0.339
          ],
          "p_mean_le_0": 0.029,
          "n": 293
        }
      },
      "1.5": {
        "n": 263,
        "wrTP1": 28.9,
        "nSL": 152,
        "nTO": 35,
        "expR": 0.206,
        "pf": 1.32,
        "mfe_p25": 22.0,
        "mfe_p50": 45.0,
        "mfe_p75": 82.25,
        "winnerMAE_p75": 20.25,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 24.3,
        "ci90": {
          "expR": 0.206,
          "ci90": [
            0.021,
            0.409
          ],
          "p_mean_le_0": 0.035,
          "n": 236
        }
      },
      "2.0": {
        "n": 172,
        "wrTP1": 22.1,
        "nSL": 112,
        "nTO": 22,
        "expR": 0.134,
        "pf": 1.19,
        "mfe_p25": 25.0,
        "mfe_p50": 48.0,
        "mfe_p75": 90.0,
        "winnerMAE_p75": 19.75,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 7.5,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 22.3,
        "ci90": {
          "expR": 0.134,
          "ci90": [
            -0.115,
            0.397
          ],
          "p_mean_le_0": 0.194,
          "n": 157
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
      "n": 3144,
      "wrTP1": 45.0,
      "nSL": 1545,
      "nTO": 183,
      "expR": -0.033,
      "pf": 0.93,
      "mfe_p25": 6.0,
      "mfe_p50": 15.0,
      "mfe_p75": 32.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 27.1,
      "ci90": {
        "expR": -0.033,
        "ci90": [
          -0.066,
          0.001
        ],
        "p_mean_le_0": 0.943,
        "n": 3069
      }
    },
    "cuts": {
      "1.2": {
        "n": 1239,
        "wrTP1": 25.7,
        "nSL": 805,
        "nTO": 115,
        "expR": -0.078,
        "pf": 0.88,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 16.0,
        "ci90": {
          "expR": -0.078,
          "ci90": [
            -0.145,
            -0.01
          ],
          "p_mean_le_0": 0.973,
          "n": 1207
        }
      },
      "1.3": {
        "n": 1105,
        "wrTP1": 25.2,
        "nSL": 720,
        "nTO": 106,
        "expR": -0.056,
        "pf": 0.92,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 43.5,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.200000000000017,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 13.5,
        "ci90": {
          "expR": -0.056,
          "ci90": [
            -0.132,
            0.022
          ],
          "p_mean_le_0": 0.894,
          "n": 1075
        }
      },
      "1.5": {
        "n": 929,
        "wrTP1": 21.0,
        "nSL": 638,
        "nTO": 96,
        "expR": -0.114,
        "pf": 0.84,
        "mfe_p25": 7.0,
        "mfe_p50": 18.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 21.599999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 11.9,
        "ci90": {
          "expR": -0.114,
          "ci90": [
            -0.196,
            -0.027
          ],
          "p_mean_le_0": 0.981,
          "n": 904
        }
      },
      "2.0": {
        "n": 622,
        "wrTP1": 15.1,
        "nSL": 450,
        "nTO": 78,
        "expR": -0.17,
        "pf": 0.77,
        "mfe_p25": 7.0,
        "mfe_p50": 18.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 19.400000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 8.9,
        "ci90": {
          "expR": -0.17,
          "ci90": [
            -0.285,
            -0.061
          ],
          "p_mean_le_0": 0.994,
          "n": 601
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 2292,
      "wrTP1": 46.5,
      "nSL": 1061,
      "nTO": 165,
      "expR": 0.041,
      "pf": 1.08,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 34.5,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 28.1,
      "ci90": {
        "expR": 0.041,
        "ci90": [
          0.002,
          0.083
        ],
        "p_mean_le_0": 0.043,
        "n": 2187
      }
    },
    "cuts": {
      "1.2": {
        "n": 940,
        "wrTP1": 27.4,
        "nSL": 569,
        "nTO": 113,
        "expR": 0.018,
        "pf": 1.03,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.5,
        "ci90": {
          "expR": 0.018,
          "ci90": [
            -0.067,
            0.104
          ],
          "p_mean_le_0": 0.381,
          "n": 884
        }
      },
      "1.3": {
        "n": 870,
        "wrTP1": 26.4,
        "nSL": 532,
        "nTO": 108,
        "expR": 0.02,
        "pf": 1.03,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 12.75,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 17.1,
        "ci90": {
          "expR": 0.02,
          "ci90": [
            -0.068,
            0.109
          ],
          "p_mean_le_0": 0.365,
          "n": 819
        }
      },
      "1.5": {
        "n": 739,
        "wrTP1": 24.4,
        "nSL": 458,
        "nTO": 101,
        "expR": 0.028,
        "pf": 1.04,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 19.19999999999999,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 14.4,
        "ci90": {
          "expR": 0.028,
          "ci90": [
            -0.065,
            0.135
          ],
          "p_mean_le_0": 0.311,
          "n": 694
        }
      },
      "2.0": {
        "n": 511,
        "wrTP1": 17.6,
        "nSL": 339,
        "nTO": 82,
        "expR": -0.041,
        "pf": 0.94,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 23.10000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 9.7,
        "ci90": {
          "expR": -0.041,
          "ci90": [
            -0.171,
            0.092
          ],
          "p_mean_le_0": 0.723,
          "n": 479
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 1467,
      "wrTP1": 49.8,
      "nSL": 678,
      "nTO": 58,
      "expR": 0.007,
      "pf": 1.01,
      "mfe_p25": 9.0,
      "mfe_p50": 21.0,
      "mfe_p75": 45.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 30.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 42.2,
      "ci90": {
        "expR": 0.007,
        "ci90": [
          -0.038,
          0.057
        ],
        "p_mean_le_0": 0.403,
        "n": 1437
      }
    },
    "cuts": {
      "1.2": {
        "n": 537,
        "wrTP1": 26.8,
        "nSL": 349,
        "nTO": 44,
        "expR": -0.105,
        "pf": 0.84,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 62.75,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.700000000000017,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 30.9,
        "ci90": {
          "expR": -0.105,
          "ci90": [
            -0.206,
            -0.006
          ],
          "p_mean_le_0": 0.957,
          "n": 518
        }
      },
      "1.3": {
        "n": 481,
        "wrTP1": 24.9,
        "nSL": 318,
        "nTO": 43,
        "expR": -0.115,
        "pf": 0.83,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 65.5,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.10000000000001,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 30.2,
        "ci90": {
          "expR": -0.115,
          "ci90": [
            -0.222,
            -0.011
          ],
          "p_mean_le_0": 0.965,
          "n": 463
        }
      },
      "1.5": {
        "n": 411,
        "wrTP1": 20.4,
        "nSL": 286,
        "nTO": 41,
        "expR": -0.189,
        "pf": 0.74,
        "mfe_p25": 12.0,
        "mfe_p50": 26.5,
        "mfe_p75": 67.75,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.700000000000003,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 28.0,
        "ci90": {
          "expR": -0.189,
          "ci90": [
            -0.303,
            -0.063
          ],
          "p_mean_le_0": 0.99,
          "n": 394
        }
      },
      "2.0": {
        "n": 264,
        "wrTP1": 15.2,
        "nSL": 189,
        "nTO": 35,
        "expR": -0.218,
        "pf": 0.72,
        "mfe_p25": 10.0,
        "mfe_p50": 26.0,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 8.5,
        "winnerMAE_p90": 18.1,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 20.6,
        "ci90": {
          "expR": -0.218,
          "ci90": [
            -0.375,
            -0.047
          ],
          "p_mean_le_0": 0.987,
          "n": 248
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 1013,
      "wrTP1": 49.3,
      "nSL": 464,
      "nTO": 50,
      "expR": 0.087,
      "pf": 1.18,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 46.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 41.2,
      "ci90": {
        "expR": 0.087,
        "ci90": [
          0.024,
          0.152
        ],
        "p_mean_le_0": 0.013,
        "n": 980
      }
    },
    "cuts": {
      "1.2": {
        "n": 406,
        "wrTP1": 29.1,
        "nSL": 257,
        "nTO": 31,
        "expR": 0.069,
        "pf": 1.1,
        "mfe_p25": 14.0,
        "mfe_p50": 32.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 28.4,
        "ci90": {
          "expR": 0.069,
          "ci90": [
            -0.066,
            0.207
          ],
          "p_mean_le_0": 0.217,
          "n": 391
        }
      },
      "1.3": {
        "n": 375,
        "wrTP1": 28.0,
        "nSL": 240,
        "nTO": 30,
        "expR": 0.074,
        "pf": 1.11,
        "mfe_p25": 13.0,
        "mfe_p50": 32.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 25.60000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 27.1,
        "ci90": {
          "expR": 0.074,
          "ci90": [
            -0.072,
            0.226
          ],
          "p_mean_le_0": 0.207,
          "n": 361
        }
      },
      "1.5": {
        "n": 313,
        "wrTP1": 23.3,
        "nSL": 213,
        "nTO": 27,
        "expR": 0.03,
        "pf": 1.04,
        "mfe_p25": 14.0,
        "mfe_p50": 33.5,
        "mfe_p75": 69.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 26.799999999999997,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 26.8,
        "ci90": {
          "expR": 0.03,
          "ci90": [
            -0.129,
            0.192
          ],
          "p_mean_le_0": 0.371,
          "n": 302
        }
      },
      "2.0": {
        "n": 213,
        "wrTP1": 17.4,
        "nSL": 153,
        "nTO": 23,
        "expR": 0.02,
        "pf": 1.03,
        "mfe_p25": 12.0,
        "mfe_p50": 40.0,
        "mfe_p75": 77.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 20.3,
        "ci90": {
          "expR": 0.02,
          "ci90": [
            -0.2,
            0.25
          ],
          "p_mean_le_0": 0.453,
          "n": 205
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 535,
      "wrTP1": 54.6,
      "nSL": 234,
      "nTO": 9,
      "expR": 0.1,
      "pf": 1.22,
      "mfe_p25": 13.0,
      "mfe_p50": 31.0,
      "mfe_p75": 65.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 43.900000000000034,
      "loserMFEbeforeSL_p50": 1.5,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -33.0,
      "revAfterSL_rate": 53.4,
      "ci90": {
        "expR": 0.1,
        "ci90": [
          0.015,
          0.185
        ],
        "p_mean_le_0": 0.029,
        "n": 527
      }
    },
    "cuts": {
      "1.2": {
        "n": 187,
        "wrTP1": 36.9,
        "nSL": 113,
        "nTO": 5,
        "expR": 0.174,
        "pf": 1.28,
        "mfe_p25": 20.5,
        "mfe_p50": 42.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 30.400000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 47.8,
        "ci90": {
          "expR": 0.174,
          "ci90": [
            -0.025,
            0.375
          ],
          "p_mean_le_0": 0.08,
          "n": 183
        }
      },
      "1.3": {
        "n": 171,
        "wrTP1": 35.1,
        "nSL": 106,
        "nTO": 5,
        "expR": 0.155,
        "pf": 1.24,
        "mfe_p25": 21.0,
        "mfe_p50": 42.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 17.25,
        "winnerMAE_p90": 30.200000000000003,
        "loserMFEbeforeSL_p50": 7.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.0,
        "revAfterSL_rate": 46.2,
        "ci90": {
          "expR": 0.155,
          "ci90": [
            -0.054,
            0.377
          ],
          "p_mean_le_0": 0.11,
          "n": 167
        }
      },
      "1.5": {
        "n": 139,
        "wrTP1": 29.5,
        "nSL": 96,
        "nTO": 2,
        "expR": 0.068,
        "pf": 1.1,
        "mfe_p25": 21.0,
        "mfe_p50": 41.0,
        "mfe_p75": 78.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 30.0,
        "loserMFEbeforeSL_p50": 5.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 47.9,
        "ci90": {
          "expR": 0.068,
          "ci90": [
            -0.174,
            0.326
          ],
          "p_mean_le_0": 0.321,
          "n": 137
        }
      },
      "2.0": {
        "n": 84,
        "wrTP1": 21.4,
        "nSL": 64,
        "nTO": 2,
        "expR": -0.069,
        "pf": 0.91,
        "mfe_p25": 18.25,
        "mfe_p50": 42.0,
        "mfe_p75": 83.75,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 11.400000000000006,
        "loserMFEbeforeSL_p50": 7.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -31.0,
        "revAfterSL_rate": 40.6,
        "ci90": {
          "expR": -0.069,
          "ci90": [
            -0.379,
            0.283
          ],
          "p_mean_le_0": 0.641,
          "n": 82
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 372,
      "wrTP1": 50.3,
      "nSL": 159,
      "nTO": 26,
      "expR": 0.077,
      "pf": 1.17,
      "mfe_p25": 13.0,
      "mfe_p50": 26.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 32.0,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -27.0,
      "revAfterSL_rate": 40.9,
      "ci90": {
        "expR": 0.077,
        "ci90": [
          -0.023,
          0.178
        ],
        "p_mean_le_0": 0.108,
        "n": 349
      }
    },
    "cuts": {
      "1.2": {
        "n": 125,
        "wrTP1": 29.6,
        "nSL": 73,
        "nTO": 15,
        "expR": 0.116,
        "pf": 1.18,
        "mfe_p25": 18.0,
        "mfe_p50": 33.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 28.4,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 30.1,
        "ci90": {
          "expR": 0.116,
          "ci90": [
            -0.134,
            0.366
          ],
          "p_mean_le_0": 0.237,
          "n": 113
        }
      },
      "1.3": {
        "n": 115,
        "wrTP1": 30.4,
        "nSL": 66,
        "nTO": 14,
        "expR": 0.169,
        "pf": 1.27,
        "mfe_p25": 18.0,
        "mfe_p50": 36.5,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 20.5,
        "winnerMAE_p90": 28.6,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 28.8,
        "ci90": {
          "expR": 0.169,
          "ci90": [
            -0.103,
            0.446
          ],
          "p_mean_le_0": 0.149,
          "n": 104
        }
      },
      "1.5": {
        "n": 93,
        "wrTP1": 28.0,
        "nSL": 53,
        "nTO": 14,
        "expR": 0.212,
        "pf": 1.33,
        "mfe_p25": 18.0,
        "mfe_p50": 35.0,
        "mfe_p75": 89.25,
        "winnerMAE_p75": 20.75,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 20.8,
        "ci90": {
          "expR": 0.212,
          "ci90": [
            -0.084,
            0.534
          ],
          "p_mean_le_0": 0.128,
          "n": 82
        }
      },
      "2.0": {
        "n": 60,
        "wrTP1": 21.7,
        "nSL": 38,
        "nTO": 9,
        "expR": 0.185,
        "pf": 1.26,
        "mfe_p25": 24.0,
        "mfe_p50": 39.0,
        "mfe_p75": 94.75,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 21.6,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 15.8,
        "ci90": {
          "expR": 0.185,
          "ci90": [
            -0.227,
            0.621
          ],
          "p_mean_le_0": 0.245,
          "n": 54
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
    "n": 2683,
    "wrTP1": 44.7,
    "expR": -0.02
  },
  "2026-W37": {
    "n": 4846,
    "wrTP1": 46.8,
    "expR": 0.072
  },
  "2026-W38": {
    "n": 4370,
    "wrTP1": 46.3,
    "expR": 0.101
  },
  "2026-W39": {
    "n": 4945,
    "wrTP1": 46.1,
    "expR": 0.07
  },
  "2026-W40": {
    "n": 5286,
    "wrTP1": 45.5,
    "expR": 0.018
  },
  "2026-W41": {
    "n": 4075,
    "wrTP1": 46.8,
    "expR": 0.04
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 31,
      "wrTP1": 45.2,
      "expR": 0.254,
      "pf": 1.56
    },
    "1m/INV/SHORT": {
      "n": 17,
      "wrTP1": 70.6,
      "expR": 0.243,
      "pf": 1.83
    },
    "1m/RETEST/LONG": {
      "n": 1102,
      "wrTP1": 42.7,
      "expR": -0.014,
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
      "n": 569,
      "wrTP1": 45.5,
      "expR": -0.074,
      "pf": 0.86
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
      "n": 233,
      "wrTP1": 52.4,
      "expR": 0.08,
      "pf": 1.18
    },
    "5m/RETEST/SHORT": {
      "n": 87,
      "wrTP1": 49.4,
      "expR": 0.031,
      "pf": 1.07
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
      "n": 1435,
      "wrTP1": 45.5,
      "expR": 0.063,
      "pf": 1.13
    },
    "1m/RETEST/SHORT": {
      "n": 1573,
      "wrTP1": 44.8,
      "expR": 0.034,
      "pf": 1.07
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
      "n": 611,
      "wrTP1": 46.6,
      "expR": 0.022,
      "pf": 1.05
    },
    "2m/RETEST/SHORT": {
      "n": 687,
      "wrTP1": 51.5,
      "expR": 0.153,
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
      "n": 53,
      "wrTP1": 41.5,
      "expR": -0.091,
      "pf": 0.82
    },
    "1m/INV/SHORT": {
      "n": 19,
      "wrTP1": 42.1,
      "expR": -0.179,
      "pf": 0.66
    },
    "1m/RETEST/LONG": {
      "n": 1753,
      "wrTP1": 48.3,
      "expR": 0.122,
      "pf": 1.27
    },
    "1m/RETEST/SHORT": {
      "n": 934,
      "wrTP1": 42.7,
      "expR": 0.128,
      "pf": 1.28
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
      "n": 799,
      "wrTP1": 47.3,
      "expR": 0.061,
      "pf": 1.13
    },
    "2m/RETEST/SHORT": {
      "n": 344,
      "wrTP1": 43.9,
      "expR": 0.018,
      "pf": 1.04
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
      "n": 31,
      "wrTP1": 51.6,
      "expR": 0.641,
      "pf": 2.99
    },
    "1m/INV/SHORT": {
      "n": 38,
      "wrTP1": 50.0,
      "expR": -0.008,
      "pf": 0.98
    },
    "1m/RETEST/LONG": {
      "n": 1876,
      "wrTP1": 44.8,
      "expR": 0.062,
      "pf": 1.13
    },
    "1m/RETEST/SHORT": {
      "n": 1259,
      "wrTP1": 45.4,
      "expR": 0.009,
      "pf": 1.02
    },
    "2m/INV/LONG": {
      "n": 25,
      "wrTP1": 48.0,
      "expR": 0.267,
      "pf": 1.68
    },
    "2m/INV/SHORT": {
      "n": 15,
      "wrTP1": 53.3,
      "expR": 0.449,
      "pf": 2.95
    },
    "2m/RETEST/LONG": {
      "n": 724,
      "wrTP1": 46.8,
      "expR": 0.154,
      "pf": 1.33
    },
    "2m/RETEST/SHORT": {
      "n": 521,
      "wrTP1": 49.3,
      "expR": 0.046,
      "pf": 1.1
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
      "n": 48,
      "wrTP1": 39.6,
      "expR": -0.059,
      "pf": 0.88
    },
    "1m/RETEST/LONG": {
      "n": 1786,
      "wrTP1": 42.7,
      "expR": -0.036,
      "pf": 0.93
    },
    "1m/RETEST/SHORT": {
      "n": 1373,
      "wrTP1": 45.9,
      "expR": 0.03,
      "pf": 1.06
    },
    "2m/INV/LONG": {
      "n": 13,
      "wrTP1": 69.2,
      "expR": 0.156,
      "pf": 1.51
    },
    "2m/INV/SHORT": {
      "n": 19,
      "wrTP1": 57.9,
      "expR": -0.018,
      "pf": 0.95
    },
    "2m/RETEST/LONG": {
      "n": 839,
      "wrTP1": 46.6,
      "expR": 0.002,
      "pf": 1.0
    },
    "2m/RETEST/SHORT": {
      "n": 628,
      "wrTP1": 46.5,
      "expR": 0.114,
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
      "n": 39,
      "wrTP1": 53.8,
      "expR": 0.116,
      "pf": 1.28
    },
    "1m/INV/SHORT": {
      "n": 35,
      "wrTP1": 42.9,
      "expR": 0.165,
      "pf": 1.39
    },
    "1m/RETEST/LONG": {
      "n": 1437,
      "wrTP1": 45.5,
      "expR": -0.013,
      "pf": 0.97
    },
    "1m/RETEST/SHORT": {
      "n": 1007,
      "wrTP1": 43.3,
      "expR": 0.073,
      "pf": 1.15
    },
    "2m/INV/LONG": {
      "n": 18,
      "wrTP1": 50.0,
      "expR": -0.006,
      "pf": 0.99
    },
    "2m/INV/SHORT": {
      "n": 8,
      "wrTP1": 25.0,
      "expR": 0.305,
      "pf": 1.49
    },
    "2m/RETEST/LONG": {
      "n": 657,
      "wrTP1": 51.9,
      "expR": 0.046,
      "pf": 1.1
    },
    "2m/RETEST/SHORT": {
      "n": 443,
      "wrTP1": 47.2,
      "expR": 0.084,
      "pf": 1.17
    },
    "5m/INV/LONG": {
      "n": 5,
      "wrTP1": 40.0,
      "expR": -0.388,
      "pf": 0.23
    },
    "5m/INV/SHORT": {
      "n": 3,
      "wrTP1": 33.3,
      "expR": -0.513,
      "pf": 0.23
    },
    "5m/RETEST/LONG": {
      "n": 257,
      "wrTP1": 52.1,
      "expR": 0.065,
      "pf": 1.14
    },
    "5m/RETEST/SHORT": {
      "n": 166,
      "wrTP1": 51.2,
      "expR": 0.083,
      "pf": 1.19
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 24171,
  "brier": 0.2206,
  "bias": -0.103,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.233
    },
    {
      "feature": "nearTk",
      "weight": -0.068
    },
    {
      "feature": "stretchAtr",
      "weight": -0.052
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.031
    },
    {
      "feature": "rvol",
      "weight": 0.024
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.019
    },
    {
      "feature": "biasScore",
      "weight": -0.016
    },
    {
      "feature": "structDir",
      "weight": -0.016
    },
    {
      "feature": "aligned",
      "weight": -0.013
    },
    {
      "feature": "emaStack",
      "weight": 0.012
    },
    {
      "feature": "hourNY",
      "weight": 0.006
    },
    {
      "feature": "nearEdge",
      "weight": -0.006
    },
    {
      "feature": "chopIdx",
      "weight": 0.003
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.152,
      "actual": 0.18,
      "n": 2417
    },
    {
      "bin": 1,
      "pred": 0.356,
      "actual": 0.295,
      "n": 2417
    },
    {
      "bin": 2,
      "pred": 0.443,
      "actual": 0.338,
      "n": 2417
    },
    {
      "bin": 3,
      "pred": 0.491,
      "actual": 0.389,
      "n": 2417
    },
    {
      "bin": 4,
      "pred": 0.532,
      "actual": 0.515,
      "n": 2417
    },
    {
      "bin": 5,
      "pred": 0.563,
      "actual": 0.568,
      "n": 2417
    },
    {
      "bin": 6,
      "pred": 0.588,
      "actual": 0.609,
      "n": 2417
    },
    {
      "bin": 7,
      "pred": 0.608,
      "actual": 0.659,
      "n": 2417
    },
    {
      "bin": 8,
      "pred": 0.628,
      "actual": 0.697,
      "n": 2417
    },
    {
      "bin": 9,
      "pred": 0.654,
      "actual": 0.751,
      "n": 2418
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 16844,
  "testN": 9361,
  "testWeeks": [
    "2026-W40",
    "2026-W41"
  ],
  "model_oos_brier": 0.2182,
  "model_oos_n": 9361,
  "best_scheme_in_sample": {
    "scheme": "nextLevel",
    "trainExpR": 0.064
  },
  "best_scheme_oos_expR": 0.028
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.173,
    "ci90": [
      0.019,
      0.335
    ],
    "p_mean_le_0": 0.029,
    "n": 223,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": 0.028,
    "ci90": [
      -0.105,
      0.155
    ],
    "p_mean_le_0": 0.373,
    "n": 199,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.034,
    "ci90": [
      0.013,
      0.055
    ],
    "p_mean_le_0": 0.004,
    "n": 9102,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.043,
    "ci90": [
      0.016,
      0.068
    ],
    "p_mean_le_0": 0.001,
    "n": 6206,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.039,
    "ci90": [
      -0.133,
      0.217
    ],
    "p_mean_le_0": 0.367,
    "n": 89,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.083,
    "ci90": [
      -0.156,
      0.347
    ],
    "p_mean_le_0": 0.29,
    "n": 80,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.038,
    "ci90": [
      0.006,
      0.07
    ],
    "p_mean_le_0": 0.025,
    "n": 4050,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.081,
    "ci90": [
      0.039,
      0.125
    ],
    "p_mean_le_0": 0.0,
    "n": 2703,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.349,
    "ci90": [
      0.099,
      0.615
    ],
    "p_mean_le_0": 0.01,
    "n": 25,
    "survives_fdr10": true
  },
  "5m/INV/SHORT": {
    "expR": 0.128,
    "ci90": [
      -0.304,
      0.572
    ],
    "p_mean_le_0": 0.333,
    "n": 16,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.12,
    "ci90": [
      0.065,
      0.172
    ],
    "p_mean_le_0": 0.0,
    "n": 1452,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.088,
    "ci90": [
      0.024,
      0.151
    ],
    "p_mean_le_0": 0.011,
    "n": 956,
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
      "n": 9261,
      "wrTP1": 45.6,
      "expR": 0.06,
      "pf": 1.12,
      "defining_features": {
        "biasScore": -1.11,
        "emaStack": -0.99,
        "nearEdge": -0.87,
        "structDir": -0.43
      }
    },
    {
      "id": 0,
      "n": 9783,
      "wrTP1": 45.8,
      "expR": 0.059,
      "pf": 1.12,
      "defining_features": {
        "biasScore": 0.79,
        "emaStack": 0.67,
        "nearEdge": 0.67,
        "hourNY": -0.49
      }
    },
    {
      "id": 2,
      "n": 2779,
      "wrTP1": 43.5,
      "expR": 0.029,
      "pf": 1.06,
      "defining_features": {
        "stretchAtr": 1.85,
        "rvol": 1.6,
        "chopIdx": -1.43,
        "hourNY": -0.16
      }
    },
    {
      "id": 3,
      "n": 4382,
      "wrTP1": 49.6,
      "expR": 0.027,
      "pf": 1.06,
      "defining_features": {
        "hourNY": 1.33,
        "atrPctUsed": -0.94,
        "emaStack": 0.61,
        "biasScore": 0.58
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
        "n": 49,
        "wrTP1": 53.1,
        "expR": 0.306
      },
      "YM": {
        "n": 88,
        "wrTP1": 43.2,
        "expR": 0.196
      },
      "ES": {
        "n": 33,
        "wrTP1": 48.5,
        "expR": 0.114
      },
      "NQ": {
        "n": 27,
        "wrTP1": 59.3,
        "expR": 0.404
      },
      "GC": {
        "n": 36,
        "wrTP1": 41.7,
        "expR": -0.192
      }
    },
    "expR_spread": 0.596,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 112,
        "wrTP1": 40.2,
        "expR": 0.018
      },
      "NQ": {
        "n": 20,
        "wrTP1": 55.0,
        "expR": 0.054
      },
      "ES": {
        "n": 10,
        "wrTP1": 50.0,
        "expR": 0.303
      },
      "GC": {
        "n": 41,
        "wrTP1": 63.4,
        "expR": 0.199
      },
      "CL": {
        "n": 28,
        "wrTP1": 28.6,
        "expR": -0.379
      }
    },
    "expR_spread": 0.682,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 1455,
        "wrTP1": 42.5,
        "expR": -0.007
      },
      "NQ": {
        "n": 2067,
        "wrTP1": 45.4,
        "expR": 0.025
      },
      "ES": {
        "n": 2296,
        "wrTP1": 45.1,
        "expR": 0.02
      },
      "CL": {
        "n": 1960,
        "wrTP1": 45.2,
        "expR": 0.049
      },
      "YM": {
        "n": 1611,
        "wrTP1": 46.5,
        "expR": 0.083
      }
    },
    "expR_spread": 0.09,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 640,
        "wrTP1": 41.7,
        "expR": 0.088
      },
      "GC": {
        "n": 1837,
        "wrTP1": 45.2,
        "expR": 0.066
      },
      "YM": {
        "n": 1868,
        "wrTP1": 45.1,
        "expR": 0.057
      },
      "ES": {
        "n": 1069,
        "wrTP1": 45.5,
        "expR": 0.009
      },
      "CL": {
        "n": 1153,
        "wrTP1": 43.1,
        "expR": -0.012
      }
    },
    "expR_spread": 0.1,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 15,
        "wrTP1": 40.0,
        "expR": -0.327
      },
      "CL": {
        "n": 15,
        "wrTP1": 60.0,
        "expR": -0.08
      },
      "YM": {
        "n": 26,
        "wrTP1": 38.5,
        "expR": -0.13
      },
      "ES": {
        "n": 17,
        "wrTP1": 76.5,
        "expR": 0.205
      },
      "NQ": {
        "n": 20,
        "wrTP1": 50.0,
        "expR": 0.513
      }
    },
    "expR_spread": 0.84,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 44,
        "wrTP1": 52.3,
        "expR": 0.384
      },
      "NQ": {
        "n": 10,
        "wrTP1": 40.0,
        "expR": 0.066
      },
      "ES": {
        "n": 9,
        "wrTP1": 22.2,
        "expR": -0.279
      },
      "CL": {
        "n": 11,
        "wrTP1": 45.5,
        "expR": -0.258
      },
      "GC": {
        "n": 9,
        "wrTP1": 11.1,
        "expR": -0.64
      }
    },
    "expR_spread": 1.024,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 967,
        "wrTP1": 46.6,
        "expR": 0.028
      },
      "GC": {
        "n": 675,
        "wrTP1": 46.4,
        "expR": 0.021
      },
      "CL": {
        "n": 904,
        "wrTP1": 47.9,
        "expR": 0.033
      },
      "ES": {
        "n": 935,
        "wrTP1": 47.6,
        "expR": -0.004
      },
      "YM": {
        "n": 718,
        "wrTP1": 48.9,
        "expR": 0.13
      }
    },
    "expR_spread": 0.134,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 479,
        "wrTP1": 46.1,
        "expR": -0.033
      },
      "YM": {
        "n": 812,
        "wrTP1": 50.4,
        "expR": 0.128
      },
      "GC": {
        "n": 777,
        "wrTP1": 49.7,
        "expR": 0.171
      },
      "NQ": {
        "n": 291,
        "wrTP1": 40.2,
        "expR": 0.051
      },
      "CL": {
        "n": 457,
        "wrTP1": 46.0,
        "expR": -0.009
      }
    },
    "expR_spread": 0.204,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": 0.232
      },
      "YM": {
        "n": 9,
        "wrTP1": 88.9,
        "expR": 0.32
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 1.473
      },
      "ES": {
        "n": 7,
        "wrTP1": 71.4,
        "expR": 0.19
      }
    },
    "expR_spread": 1.283,
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
        "n": 5,
        "wrTP1": 20.0,
        "expR": -0.708
      },
      "ES": {
        "n": 3,
        "wrTP1": 33.3,
        "expR": 0.063
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
    "expR_spread": 1.558,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 208,
        "wrTP1": 50.0,
        "expR": 0.106
      },
      "ES": {
        "n": 336,
        "wrTP1": 51.2,
        "expR": 0.106
      },
      "YM": {
        "n": 260,
        "wrTP1": 53.5,
        "expR": 0.241
      },
      "CL": {
        "n": 300,
        "wrTP1": 51.3,
        "expR": 0.088
      },
      "NQ": {
        "n": 428,
        "wrTP1": 50.7,
        "expR": 0.085
      }
    },
    "expR_spread": 0.156,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 104,
        "wrTP1": 48.1,
        "expR": 0.054
      },
      "ES": {
        "n": 177,
        "wrTP1": 51.4,
        "expR": 0.106
      },
      "GC": {
        "n": 282,
        "wrTP1": 44.7,
        "expR": 0.001
      },
      "YM": {
        "n": 273,
        "wrTP1": 48.0,
        "expR": 0.175
      },
      "CL": {
        "n": 200,
        "wrTP1": 47.5,
        "expR": 0.093
      }
    },
    "expR_spread": 0.174,
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
    "n": 135,
    "wrTP1": 37.0,
    "nSL": 66,
    "nTO": 19,
    "expR": -0.121,
    "pf": 0.78,
    "mfe_p25": 8.0,
    "mfe_p50": 14.0,
    "mfe_p75": 28.0,
    "winnerMAE_p75": 14.75,
    "winnerMAE_p90": 19.200000000000003,
    "loserMFEbeforeSL_p50": 5.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 25.8
  },
  "away_from_news": {
    "n": 26070,
    "wrTP1": 46.2,
    "nSL": 12021,
    "nTO": 2015,
    "expR": 0.051,
    "pf": 1.11,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 32.5
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 6,
  "mae_deltaER": 0.268,
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
      "2026-10-06 (martes, incidente de repo del dia -- ver buy-retest.md -- sin perdida de dato): eval_experiments() en report.json pone por primera vez verdict=\"flat\" para este experimento en su evaluacion agregada formal antes/despues (beforeN=16583 expR=0.061 vs afterN=6438 expR=0.013) -- confirma con muestra ya grande lo que la alerta de ayer avisaba (\"el efecto se encoge\"). NO es \"rejected\" (expR post-cambio sigue positivo, no negativo), asi que sigue sin caso para revertir, pero ya no corresponde describirlo como \"cambio ganador\" en el agregado. since_change por segmento (n=5895 total RETEST, recvDate>=2026-09-26) con un dia mas de perspectiva: SOLO 2m/RETEST/LONG sigue confirmando limpio (n=954, delta=+0.145 CI90=[0.039,0.258]); los otros 5 (1m LONG n=1900 delta=-0.015, 1m SHORT n=1557 delta=+0.04, 2m SHORT n=713 delta=+0.028, 5m LONG n=342 delta=+0.04, 5m SHORT n=273 delta=+0.059) siguen planos, ninguno delta_below_zero=true. Dato adicional que contextualiza el verdict=\"flat\": en 1m/RETEST/LONG, TANTO layer_expR (-0.05) COMO orig_expR (-0.065) son negativos desde el cambio -- el deterioro de ese segmento (ver decay_weekly_by_segment, 3 semanas cayendo, W41 ya en -0.108) no depende de que SL se use, es de regimen/muestra, no del experimento en si. DECISION: sin cambio -- mantener aplicado en los 6 segmentos, no revertir nada; bajar la confianza declarada del \"cambio del mes\" de 2026-09-26 a \"neutro en agregado, con una excepcion que si gana (2m LONG)\". Vigilar si algun segmento desarrolla delta_below_zero=true con n>=40, que seria el primer caso real para revertir.",
      "2026-10-07 (miercoles): since_change (recvDate>=2026-09-26) sigue el mismo patron que ayer sin cambio de fondo -- de los 6 segmentos RETEST con n>=100, SOLO 2m/RETEST/LONG sigue confirmando limpio (delta_beats_zero=true). verdict agregado formal sigue en 'flat' (sin recalculo nuevo hoy en report.json mas alla del crecimiento de n). Sin reversion en ningun segmento (delta_below_zero=false en todos). DECISION sin cambio: mantener aplicado en los 6 segmentos, no revertir nada.",
      "2026-10-08 (jueves): since_change (recvDate>=2026-09-26, muestra mas grande hoy, n=7610 total RETEST+INV) AMPLIA la confirmacion limpia de 1 a 4 de los 6 segmentos RETEST: 2m/RETEST/LONG sigue confirmando (delta=+0.105 CI90=[0.025,0.198]); 5m/RETEST/LONG CERTIFICA POR PRIMERA VEZ (n=485, delta=+0.245 CI90=[0.022,0.523], antes plano con CI90=[-0.059,0.137]); 1m/RETEST/SHORT CERTIFICA POR PRIMERA VEZ (n=1904, delta=+0.084 CI90=[0.008,0.158], antes plano). 1m/RETEST/LONG sigue plano (n=2542, delta=+0.015 CI90=[-0.048,0.073]) y 2m/5m SHORT siguen planos sin cambio de fondo. Ningun segmento sale delta_below_zero=true. Sube la confianza del cambio aplicado el 09-26 aunque el verdict agregado formal (que mezcla los 6 segmentos y toda la ventana before/after sin distinguir) siga en 'flat' -- la lectura por segmento es mas informativa que el agregado aqui. Se corrio ademas sl_origin_vs_layer.since_change por primera vez con muestra real para kind=INV (fuera del alcance de este experimento, que es RETEST-only): mixto y negativo con significancia en 2 de 3 TF de INV/LONG y en 1m INV/SHORT -- confirma que la exclusion original de kind=INV en este experimento fue correcta, no evaluar extenderlo ahi (ver buy-ifvg.md/sell-ifvg.md). DECISION sin cambio: mantener aplicado en los 6 segmentos RETEST, no revertir nada, no extender a INV."
    ],
    "appliedNote": "2026-09-26: aplicado en scalp_command.pine (input sc_sl_retest_basis, default 'Auto (como se midio)'): en RETEST el SL real pasa a la mecha de la vela del retest; 1m SHORT suma la vela previa (retestBar2), igual que la medicion paralela. Base: los 6 segmentos RETEST certifican con CI90 > 0 (n=11273, E[R] 0.238 vs 0.065). El tier se sigue calculando con el stop de 3 capas. El feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig, asi que sl_origin_vs_layer sigue siendo la vigilancia. Rige en cada grafico desde que Jesus re-pega scalp_cc_FULL_for_tradingview.pine. Revertir = poner la base en '3 capas'.",
    "beforeN": 16342,
    "afterN": 9197,
    "before": {
      "n": 16342,
      "wrTP1": 46.0,
      "nSL": 7465,
      "nTO": 1355,
      "expR": 0.062,
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
      "n": 9197,
      "wrTP1": 46.1,
      "nSL": 4354,
      "nTO": 600,
      "expR": 0.028,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 32.1
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
      "2026-10-04 (domingo, REVISION SEMANAL): el walk-forward testWeeks avanzo otra vez, ahora de [W38,W39] a [W39,W40] (los dos ya cerrados, no una semana parcial como el 09-29). El candidato que SI habia confirmado limpio en la revision de 2026-week-39.md con la ventana [W38,W39] (5m/RETEST/LONG, rr1>=1.2, baseline n=544 expR=0.148 CI90=[0.056,0.247], corte expR=0.372 CI90=[0.149,0.605]) deja de confirmar con [W39,W40]: baseline n=515 expR=0.102 CI90=[0.013,0.192] (todavia positivo), corte 1.2 n=178 expR=0.178 pero CI90=[-0.045,0.409] cruza cero. A diferencia del 09-29 (donde la perdida de potencia era por W40 parcial con pocos dias), esta vez W40 esta completa -- es una perdida de confirmacion real con la ventana madura, no un artefacto de muestra chica. Se retira como candidato activo esta semana (ver reviews/2026-week-40.md); como nunca se aplico en TradingView (status sigue 'proposed', predictions.jsonl linea de 2026-W39 sigue con appliedDate=null), no hay nada que revertir. Ningun otro segmento de RETEST confirma el corte de rr1 con el split OOS actual. Leccion de metodo: un candidato que confirma con una ventana OOS de 2 semanas puede dejar de confirmar en la siguiente sin que el patron in-sample cambie -- tratar cualquier confirmacion OOS de una sola ventana como fragil hasta verla sostenerse en 2-3 rodadas de la ventana, no solo una.",
      "2026-10-07 (miercoles): walk_forward.testWeeks sigue en [W40,W41] (sin avanzar desde la lectura del 10-05/10-06), pero rr1_threshold_cut_oos no se habia narrado todavia contra esta ventana concreta -- se hace hoy. Resultado: de los 4 segmentos que alguna vez confirmaron en alguna ventana OOS pasada (1m SHORT, 2m SHORT, 5m LONG, y ahora se agrega 2m LONG que no se habia mirado antes), NINGUNO confirma positivo en [W40,W41] -- 1m/RETEST/SHORT baseline n=1765 expR=0.045 CI90=[-0.001,0.094] (al filo de cero) y cae a plano/negativo en todos los cortes (cut>=2.0 expR=-0.012); 2m/RETEST/SHORT baseline n=789 expR=0.082 CI90=[0.012,0.159] (unico baseline que certifica) pero el corte lo EMPEORA monotonicamente (1.2:+0.049 -> 1.5:-0.03 -> 2.0:-0.022, todos CI90 cruzando cero); 5m/RETEST/LONG baseline n=379 expR=0.093 CI90=[-0.008,0.198] y el corte sube con muestra chica pero CI90 nunca deja de cruzar cero (cut 1.2 n=133 expR=0.189 CI90=[-0.048,0.433]). NUEVO Y MAS FUERTE: 2m/RETEST/LONG, que nunca se habia reportado como candidato de este corte, sale CLARAMENTE NEGATIVO y con muestra grande -- baseline n=1071 expR=-0.024 CI90=[-0.076,0.032] (ya negativo) y cada escalon de corte lo empeora con CI90 que NO cruza cero: cut>=1.2 n=404 expR=-0.174 CI90=[-0.285,-0.056]; cut>=1.5 n=307 expR=-0.306 CI90=[-0.439,-0.172]; cut>=2.0 n=195 expR=-0.342 CI90=[-0.515,-0.148]. Es la primera vez que este corte sale negativo fuera de muestra con significancia real (delta_below_zero equivalente), no solo 'deja de confirmar'. LECTURA: la racha de confirmaciones in-sample de 1m/2m SHORT y 5m LONG que motivo esta propuesta en 09-20/09-22 lleva ya DOS ventanas OOS distintas ([W39,W40] y [W40,W41]) sin replicarse, y ahora hay evidencia nueva de que subir el piso de rr1 puede ser CONTRAPRODUCENTE en 2m LONG. DECISION: no se propone sc_min_rr/sc_aplus_rr en ninguna revision semanal mientras este patron se mantenga -- se baja la prioridad de este experimento de 'candidato pendiente de confirmar' a 'probablemente no generaliza, vigilar solo si vuelve a aparecer con 2+ ventanas OOS seguidas en la misma direccion'. No cambia status (sigue 'proposed', nunca se aplico en TradingView, nada que revertir).",
      "2026-10-08 (jueves): walk_forward.testWeeks sigue en [W40,W41]. Hallazgo mas fuerte que el 10-07: en esta ventana OOS el BASELINE sin ningun corte de rr1 ya es negativo con significancia en 1m/RETEST/LONG (n=2841, expR=-0.047, CI90=[-0.081,-0.009]) y cada escalon de corte lo empeora mas (hasta expR=-0.208 en cut>=2.0). 2m/RETEST/LONG baseline esta plano (n=1348, expR=-0.005, CI90=[-0.051,0.044]) pero cualquier corte lo vuelve negativo con significancia (cut>=1.2 expR=-0.137 CI90=[-0.237,-0.03]). Del lado SHORT, 2m/RETEST/SHORT sigue siendo el unico baseline OOS significativo y positivo (n=919, expR=0.101, CI90=[0.035,0.169]) pero los cortes no mejoran eso (CI90 vuelve a cruzar cero en todos). 1m SHORT sigue al filo (CI90=[-0.001,0.085)). 5m LONG baseline sigue positivo y significativo (n=483, expR=0.123, CI90=[0.031,0.215]) -- el unico TF RETEST que sostiene el edge OOS limpio hoy entre los 6. CONCLUSION: subir rr1 no soluciona nada donde el problema es que el baseline mismo ya es negativo (1m/2m LONG); seguir sin proponer sc_min_rr/sc_aplus_rr al alza en ningun segmento mientras esto se sostenga."
    ],
    "beforeN": 25539,
    "afterN": 0,
    "before": {
      "n": 25539,
      "wrTP1": 46.1,
      "nSL": 11819,
      "nTO": 1955,
      "expR": 0.049,
      "pf": 1.1,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
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
    "date": "2026-10-09",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-10-08T21:12:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "CL",
    "focus": {
      "sym": "CL",
      "verdict": "GO",
      "window": "20:00-23:00 CT",
      "setup": {
        "es": "A+8 retest 90.78-91.32 (VAL/EMA50/PDH + FVG 4h) a favor del giro alcista confirmado",
        "en": "A+8 retest at 90.78-91.32 (VAL/EMA50/PDH + 4h FVG) with the confirmed bullish reversal"
      },
      "trigger": {
        "es": "rechazo con cierre 15m de vuelta sobre 91.00 tras tocar el cluster; o reclamo directo con cierre 15m sostenido sobre 91.32",
        "en": "a rejection with a 15m close back above 91.00 after tagging the cluster; or a direct reclaim with a 15m close sustained above 91.32"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 90.60 mata la entrada de esta noche (el giro de fondo solo muere bajo 87.96)",
        "en": "a 5m close sustained below 90.60 kills tonight's entry (the underlying reversal only dies below 87.96)"
      },
      "note": {
        "es": "usa tamaño reducido: el stop no cabe en el limite diario a full, opera en micros. Cobra el parcial en 91.73, no busques todo el runner.",
        "en": "use reduced size: the stop doesn't fit the daily limit at full size, trade micros. Bank the partial at 91.73, don't hunt the whole runner."
      }
    },
    "alarm": {
      "es": "NQ rompio su tendencia alcista de 5 dias: cierre 31007, bien debajo de la invalidacion 31143, nueva tesis bajista dia 1. GC sigue con escenario A debil (29% en 20d).",
      "en": "NQ broke its 5-day uptrend: close at 31007, well below the 31143 invalidation, new bearish thesis day 1. GC's scenario A still runs weak (29% over 20 days)."
    },
    "summary": {
      "es": [
        "!! NQ rompio su tendencia de 5 dias: cierre 31007, muy bajo 31143. Reinicio bajista dia 1.",
        "NQ: WAIT, borde SHORT 31120-31156 algo lejos (ESTIRADA), el marco diario/semanal aun lento en confirmar.",
        "ES: WAIT, A+9 en VAL/ONL 7802.75-7815.75 bloqueado por conflicto de marcos (dia vs sesion).",
        "GC: WAIT, 3a sesion sin romper 4128.1-4166.8, el sesgo del dia giro LONG pero el marco superior sigue -3/-1.",
        "YM: WAIT, el rebote mas violento medido (690pts) deja alarma viva en 51744, no persigas ningun lado.",
        "CL: GO, A+8 en 90.78-91.32 a favor del giro alcista confirmado -- lo mas limpio de la noche.",
        "mas limpio: CL",
        "Limite $1000/cuenta: casi ninguna zona de hoy cabe en full, opera micros en CL/GC si entras.",
        "Precision 20d: GC escenario A 29% sigue bajo el piso de 30%, trata sus A como candidatas debiles."
      ],
      "en": [
        "!! NQ broke its 5-day uptrend: close 31007, well below 31143. Bearish reset, day 1.",
        "NQ: WAIT, the 31120-31156 SHORT edge is a bit far (STRETCHED), the higher-timeframe daily/weekly frame still slow to
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 12189,
  "by_verdict": {
    "AVOID": {
      "n": 1979,
      "wrTP1": 43.8,
      "nSL": 966,
      "nTO": 147,
      "expR": 0.007,
      "pf": 1.01,
      "mfe_p25": 7.25,
      "mfe_p50": 16.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.1
    },
    "GO": {
      "n": 1715,
      "wrTP1": 50.0,
      "nSL": 739,
      "nTO": 119,
      "expR": 0.094,
      "pf": 1.21,
      "mfe_p25": 8.0,
      "mfe_p50": 21.0,
      "mfe_p75": 45.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 28.399999999999977,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 38.6
    },
    "WAIT": {
      "n": 8495,
      "wrTP1": 46.8,
      "nSL": 3985,
      "nTO": 531,
      "expR": 0.052,
      "pf": 1.11,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 38.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 32.7
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.007,
      "ci90": [
        -0.039,
        0.053
      ],
      "p_mean_le_0": 0.417,
      "n": 1878
    },
    "GO": {
      "expR": 0.094,
      "ci90": [
        0.046,
        0.145
      ],
      "p_mean_le_0": 0.0,
      "n": 1642
    },
    "WAIT": {
      "expR": 0.052,
      "ci90": [
        0.03,
        0.075
      ],
      "p_mean_le_0": 0.0,
      "n": 8242
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1979,
      "wrTP1": 43.8,
      "nSL": 966,
      "nTO": 147,
      "expR": 0.007,
      "pf": 1.01,
      "mfe_p25": 7.25,
      "mfe_p50": 16.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.1
    },
    "GO_or_WAIT": {
      "n": 10210,
      "wrTP1": 47.4,
      "nSL": 4724,
      "nTO": 650,
      "expR": 0.059,
      "pf": 1.12,
      "mfe_p25": 7.0,
      "mfe_p50": 18.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 33.7
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.007,
      "ci90": [
        -0.039,
        0.053
      ],
      "p_mean_le_0": 0.417,
      "n": 1878
    },
    "GO_or_WAIT": {
      "expR": 0.059,
      "ci90": [
        0.039,
        0.079
      ],
      "p_mean_le_0": 0.0,
      "n": 9884
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 33,
        "wrTP1": 48.5,
        "nSL": 14,
        "nTO": 3,
        "expR": -0.025,
        "pf": 0.94,
        "mfe_p25": 6.0,
        "mfe_p50": 14.0,
        "mfe_p75": 30.25,
        "winnerMAE_p75": 12.75,
        "winnerMAE_p90": 16.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.5,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 28.6
      },
      "GO": {
        "n": 24,
        "wrTP1": 58.3,
        "nSL": 7,
        "nTO": 3,
        "expR": 0.18,
        "pf": 1.56,
        "mfe_p25": 11.0,
        "mfe_p50": 29.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 33.0,
        "winnerMAE_p90": 41.1,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -21.5,
        "revAfterSL_rate": 28.6
      },
      "WAIT": {
        "n": 110,
        "wrTP1": 40.9,
        "nSL": 54,
        "nTO": 11,
        "expR": -0.025,
        "pf": 0.95,
        "mfe_p25": 6.0,
        "mfe_p50": 14.0,
        "mfe_p75": 25.75,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.200000000000003,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 18.5
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
      "GO": {
        "n": 7,
        "wrTP1": 71.4,
        "nSL": 2,
        "nTO": 0,
        "expR": 0.531,
        "pf": 2.86,
        "mfe_p25": 39.5,
        "mfe_p50": 59.0,
        "mfe_p75": 79.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 28.200000000000003,
        "loserMFEbeforeSL_p50": 26.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 7.5,
        "entryZoneTk_p50": -35.0,
        "revAfterSL_rate": 50.0
      },
      "WAIT": {
        "n": 135,
        "wrTP1": 47.4,
        "nSL": 54,
        "nTO": 17,
        "expR": 0.058,
        "pf": 1.14,
        "mfe_p25": 6.75,
        "mfe_p50": 19.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 24.400000000000006,
        "loserMFEbeforeSL_p50": 3.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.5,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 22.2
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 1190,
        "wrTP1": 44.4,
        "nSL": 588,
        "nTO": 74,
        "expR": -0.014,
        "pf": 0.97,
        "mfe_p25": 7.0,
        "mfe_p50": 15.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.30000000000001,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 33.2
      },
      "GO": {
        "n": 1174,
        "wrTP1": 49.2,
        "nSL": 537,
        "nTO": 59,
        "expR": 0.074,
        "pf": 1.16,
        "mfe_p25": 6.0,
        "mfe_p50": 18.0,
        "mfe_p75": 42.75,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 28.600000000000136,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 37.2
      },
      "WAIT": {
        "n": 4465,
        "wrTP1": 47.3,
        "nSL": 2103,
        "nTO": 251,
        "expR": 0.044,
        "pf": 1.09,
        "mfe_p25": 7.0,
        "mfe_p50": 16.0,
        "mfe_p75": 37.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 32.1
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 728,
        "wrTP1": 43.1,
        "nSL": 348,
        "nTO": 66,
        "expR": 0.06,
        "pf": 1.12,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 38.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 36.8
      },
      "GO": {
        "n": 510,
        "wrTP1": 51.0,
        "nSL": 193,
        "nTO": 57,
        "expR": 0.133,
        "pf": 1.32,
        "mfe_p25": 13.0,
        "mfe_p50": 27.5,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 42.5
      },
      "WAIT": {
        "n": 3785,
        "wrTP1": 46.5,
        "nSL": 1774,
        "nTO": 252,
        "expR": 0.065,
        "pf": 1.13,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 39.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 34.2
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
    "n": 23621,
    "wrTP1": 46.2,
    "nSL": 10883,
    "nTO": 1815,
    "expR": 0.052,
    "pf": 1.11,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.5
  },
  "shadow_ci90": {
    "expR": 0.052,
    "ci90": [
      0.039,
      0.066
    ],
    "p_mean_le_0": 0.0,
    "n": 22648
  },
  "raw_indicator": {
    "n": 25539,
    "wrTP1": 46.1,
    "nSL": 11819,
    "nTO": 1955,
    "expR": 0.049,
    "pf": 1.1,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 32.7
  },
  "raw_indicator_ci90": {
    "expR": 0.049,
    "ci90": [
      0.036,
      0.063
    ],
    "p_mean_le_0": 0.0,
    "n": 24469
  },
  "tier_ap_b_only": {
    "n": 13159,
    "wrTP1": 43.6,
    "nSL": 6325,
    "nTO": 1100,
    "expR": 0.045,
    "pf": 1.09,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 5.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 31.2
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.045,
    "ci90": [
      0.026,
      0.064
    ],
    "p_mean_le_0": 0.0,
    "n": 12582
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```

## Modo sombra por semana (gate: shadow_beats_raw 3 semanas seguidas, n>=60)
```json
{
  "2026-W36": {
    "shadow_n": 2533,
    "shadow_expR": -0.031,
    "raw_n": 2605,
    "raw_expR": -0.025,
    "shadow_beats_raw": false
  },
  "2026-W37": {
    "shadow_n": 3974,
    "shadow_expR": 0.087,
    "raw_n": 4712,
    "raw_expR": 0.071,
    "shadow_beats_raw": true
  },
  "2026-W38": {
    "shadow_n": 3820,
    "shadow_expR": 0.119,
    "raw_n": 4273,
    "raw_expR": 0.107,
    "shadow_beats_raw": true
  },
  "2026-W39": {
    "shadow_n": 4765,
    "shadow_expR": 0.065,
    "raw_n": 4829,
    "raw_expR": 0.064,
    "shadow_beats_raw": true
  },
  "2026-W40": {
    "shadow_n": 4614,
    "shadow_expR": 0.019,
    "raw_n": 5153,
    "raw_expR": 0.016,
    "shadow_beats_raw": true
  },
  "2026-W41": {
    "shadow_n": 3915,
    "shadow_expR": 0.033,
    "raw_n": 3967,
    "raw_expR": 0.038,
    "shadow_beats_raw": false
  }
}
```
