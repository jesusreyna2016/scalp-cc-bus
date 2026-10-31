# Scalp CC · report 2026-10-31T01:14Z
- signals=49441 outcomes=47819 pares_resueltos=49394 pendientes=47 huerfanos=54

## ⚠ ALERTAS (llevar al frente del resumen)
- SL CAUSA: 'contra-sesgo' salta a 25.4% de las perdidas en 2026-W44 vs media 0.0% de las 3 semanas previas (2026-W41, 2026-W42, 2026-W43). Ver sl_post_mortem_weekly_trend -- puede ser una causa nueva dominante, o (si el segmento que la dispara en realidad rinde bien, ej. aligned=0 en by_aligned) una etiqueta que crece de muestra sin ser el problema real.
- GATE: 29m/RETEST/SHORT cumple el chequeo numerico agregado (n/PF/WR) pero NO el gate completo todavia -- weeklyStable3=False, slCauseMitigated=False. Es un near-miss a vigilar, no subir de peldano.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.131 vs 0.036, delta 0.095 CI90 [0.077, 0.114], n 29603). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.063 vs 0.022, delta 0.041 CI90 [0.012, 0.069], n 8744). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.043 CI90 [0.028, 0.059], n 16401). Consistente con la hipotesis original de agent-instructions.md.
- METODO: tus predicciones de direccion aciertan 16.7% (peor que un volado, n=6, MAE=0.267). Se mas conservador con 'cambio del mes' y marcar experimental mas tiempo antes de subir confianza.
- MODO SOMBRA: 3 semanas CERRADAS seguidas sin batir al indicador crudo (2026-W41, 2026-W42, 2026-W43) -- espejo inverso del gate de promocion del peldano 0->1. No implica bajar de peldano (ya promovido), pero revisar shadow_rules en la revision semanal.

- E[R] global: {"expR": 0.039, "ci90": [0.031, 0.049], "p_mean_le_0": 0.0, "n": 47765}
- gate ejecucion: {"readyForLive": true, "segment": "29m/RETEST/SHORT", "weeklyStable3": false, "weeklyDetail": [{"week": "2026-W41", "wrTP1": null, "pf": null, "ok": false}, {"week": "2026-W42", "wrTP1": null, "pf": null, "ok": false}, {"week": "2026-W43", "wrTP1": null, "pf": null, "ok": false}], "slCauseMitigated": false, "fullyReady": false, "note": "readyForLive: n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side (solo agregado historico). fullyReady exige ademas weeklyStable3 (3 semanas CERRADAS seguidas con WR>=50 & PF>=1.3 en ese mismo segmento) y slCauseMitigated (experimento con verdict=confirmed dirigido a ese segmento). Solo fullyReady=true es luz verde real para subir de peldano; readyForLive=true con fullyReady=false es un near-miss a vigilar."}

## Integridad de sigId (colisiones, posible causa de alertas MUESTRA)
```json
{
  "signals": {
    "total_sigIds": 44747,
    "collided_sigIds": 4350,
    "collided_pct": 9.72,
    "delta_days_histogram": {
      "14": 932,
      "7": 835,
      "21": 481,
      "28": 469,
      "35": 426,
      "42": 376,
      "49": 177,
      "56": 152,
      "34": 62,
      "48": 58
    },
    "conflicting_result_n": 0,
    "conflicting_result_examples": []
  },
  "outcomes": {
    "total_sigIds": 43434,
    "collided_sigIds": 4071,
    "collided_pct": 9.37,
    "delta_days_histogram": {
      "14": 890,
      "7": 779,
      "21": 445,
      "28": 434,
      "35": 400,
      "42": 334,
      "49": 171,
      "56": 142,
      "34": 62,
      "41": 56
    },
    "conflicting_result_n": 2354,
    "conflicting_result_examples": [
      "NQ-2-22054-L",
      "NQ-1-23427-L",
      "NQ-2-22070-L",
      "NQ-2-22078-L",
      "GC-1-23456-S",
      "GC-1-23459-S",
      "GC-1-23483-S",
      "YM-1-22698-S"
    ]
  },
  "note": "colision = mismo sigId en >1 archivo diario con receivedAt distinto. 'last wins' en build_pairs() descarta una ocurrencia; si conflicting_result_n>0 confirma que son pares reales distintos, no un reenvio del mismo evento."
}
```

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 15m/INV/LONG | 4 | 50.0 | -0.115 | 0.77 | 2 | 92.0 | 155.75 | 0.0 |
| 15m/INV/SHORT | 1 | 100.0 | 1.35 | 99.0 | 0 | 39.0 | 18.0 | None |
| 15m/RETEST/LONG | 253 | 48.6 | -0.026 | 0.95 | 129 | 76.0 | 74.5 | 55.0 |
| 15m/RETEST/SHORT | 263 | 53.2 | 0.073 | 1.16 | 123 | 117.0 | 384.0 | 66.7 |
| 1m/INV/LONG | 452 | 46.5 | 0.116 | 1.26 | 192 | 15.0 | 11.0 | 18.2 |
| 1m/INV/SHORT | 329 | 46.5 | 0.084 | 1.2 | 130 | 21.0 | 14.0 | 16.9 |
| 1m/RETEST/LONG | 17097 | 45.0 | 0.026 | 1.05 | 8210 | 14.0 | 10.0 | 28.7 |
| 1m/RETEST/SHORT | 11350 | 45.0 | 0.03 | 1.06 | 5311 | 19.0 | 12.0 | 29.1 |
| 29m/RETEST/LONG | 106 | 53.8 | 0.143 | 1.31 | 49 | 132.0 | 331.0 | 55.1 |
| 29m/RETEST/SHORT | 161 | 57.1 | 0.175 | 1.41 | 69 | 127.0 | 196.75 | 66.7 |
| 2m/INV/LONG | 162 | 53.1 | 0.043 | 1.11 | 64 | 17.0 | 15.5 | 15.6 |
| 2m/INV/SHORT | 120 | 49.2 | 0.124 | 1.3 | 47 | 28.0 | 13.5 | 31.9 |
| 2m/RETEST/LONG | 7476 | 47.4 | 0.03 | 1.06 | 3538 | 19.0 | 12.0 | 38.8 |
| 2m/RETEST/SHORT | 4931 | 47.4 | 0.043 | 1.09 | 2308 | 24.0 | 15.0 | 39.0 |
| 3m/INV/LONG | 8 | 62.5 | 0.02 | 1.05 | 3 | 22.0 | 6.0 | 33.3 |
| 3m/INV/SHORT | 5 | 100.0 | 0.48 | 99.0 | 0 | 38.0 | 7.0 | None |
| 3m/RETEST/LONG | 768 | 53.3 | 0.073 | 1.16 | 350 | 22.0 | 14.0 | 53.1 |
| 3m/RETEST/SHORT | 742 | 54.0 | 0.109 | 1.25 | 327 | 21.5 | 15.0 | 55.0 |
| 5m/INV/LONG | 51 | 66.7 | 0.132 | 1.49 | 13 | 28.5 | 29.0 | 53.8 |
| 5m/INV/SHORT | 32 | 46.9 | 0.201 | 1.46 | 13 | 56.5 | 43.0 | 30.8 |
| 5m/RETEST/LONG | 2977 | 51.1 | 0.09 | 1.2 | 1298 | 33.0 | 24.0 | 47.9 |
| 5m/RETEST/SHORT | 2106 | 49.0 | 0.074 | 1.16 | 930 | 38.0 | 29.0 | 44.2 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 3377 | 22.5 | 0.011 | 1.02 | 2215 | 27.0 | 12.0 | 17.6 |
| B | 21508 | 47.2 | 0.032 | 1.07 | 9974 | 18.0 | 12.0 | 35.2 |
| C | 24509 | 49.5 | 0.05 | 1.11 | 10917 | 19.0 | 14.0 | 36.6 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 17939 | 48.6 | 0.069 | 1.15 | 8137 | 14.0 | 10.0 | 35.3 |
| London | 7518 | 46.0 | 0.013 | 1.02 | 3742 | 19.0 | 13.0 | 37.2 |
| NY | 8772 | 44.8 | 0.019 | 1.04 | 4227 | 27.0 | 18.0 | 37.1 |
| Sin KZ | 15165 | 45.6 | 0.03 | 1.06 | 7000 | 21.0 | 14.0 | 29.4 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 12973 | 44.9 | 0.028 | 1.06 | 6160 | 23.0 | 15.0 | 32.5 |
| edge=0 | 19215 | 49.0 | 0.053 | 1.11 | 8698 | 17.0 | 12.0 | 37.2 |
| edge=1 | 17206 | 45.3 | 0.033 | 1.07 | 8248 | 19.0 | 13.0 | 32.1 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 2660 | 53.3 | 0.066 | 1.14 | 1214 | 22.0 | 21.0 | 57.6 |
| aligned=1 | 46734 | 46.3 | 0.038 | 1.08 | 21892 | 19.0 | 13.0 | 32.9 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 26 | 50.0 | -0.025 | 0.95 | 13 | 20.0 | 15.0 | 15.4 |
| INV/LONG|edge=0 | 251 | 59.0 | 0.197 | 1.56 | 84 | 16.0 | 11.0 | 29.8 |
| INV/LONG|edge=1 | 400 | 44.0 | 0.043 | 1.09 | 177 | 16.0 | 13.0 | 14.7 |
| INV/SHORT|edge=-1 | 291 | 44.0 | 0.073 | 1.16 | 123 | 26.0 | 13.0 | 17.9 |
| INV/SHORT|edge=0 | 177 | 52.5 | 0.149 | 1.39 | 60 | 19.5 | 17.0 | 30.0 |
| INV/SHORT|edge=1 | 19 | 63.2 | 0.295 | 1.8 | 7 | 28.0 | 33.0 | 14.3 |
| RETEST/LONG|edge=-1 | 2561 | 51.1 | 0.067 | 1.14 | 1188 | 19.0 | 15.0 | 48.7 |
| RETEST/LONG|edge=0 | 11570 | 48.9 | 0.042 | 1.09 | 5313 | 15.0 | 11.0 | 37.1 |
| RETEST/LONG|edge=1 | 14546 | 43.9 | 0.023 | 1.05 | 7073 | 18.0 | 13.0 | 29.5 |
| RETEST/SHORT|edge=-1 | 10095 | 43.4 | 0.016 | 1.03 | 4836 | 24.0 | 15.0 | 28.9 |
| RETEST/SHORT|edge=0 | 7217 | 48.7 | 0.064 | 1.14 | 3241 | 20.0 | 13.0 | 37.7 |
| RETEST/SHORT|edge=1 | 2241 | 54.1 | 0.094 | 1.21 | 991 | 20.0 | 19.0 | 54.5 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 249 | 41.4 | 0.031 | 1.06 | 117 | 16.0 | 13.0 | 11.1 |
| INV/LONG|tier=C | 428 | 54.7 | 0.136 | 1.35 | 157 | 16.0 | 12.0 | 25.5 |
| INV/SHORT|tier=B | 159 | 45.9 | 0.041 | 1.09 | 69 | 25.0 | 12.0 | 10.1 |
| INV/SHORT|tier=C | 328 | 48.8 | 0.142 | 1.36 | 121 | 23.0 | 20.0 | 28.1 |
| RETEST/LONG|tier=A+ | 2149 | 22.0 | 0.006 | 1.01 | 1432 | 23.0 | 11.0 | 15.6 |
| RETEST/LONG|tier=B | 12433 | 47.6 | 0.04 | 1.08 | 5781 | 17.0 | 11.0 | 36.7 |
| RETEST/LONG|tier=C | 14095 | 49.4 | 0.034 | 1.07 | 6361 | 17.0 | 13.0 | 36.0 |
| RETEST/SHORT|tier=A+ | 1228 | 23.3 | 0.018 | 1.03 | 783 | 37.0 | 15.0 | 21.2 |
| RETEST/SHORT|tier=B | 8667 | 46.8 | 0.022 | 1.05 | 4007 | 20.0 | 13.0 | 34.2 |
| RETEST/SHORT|tier=C | 9658 | 49.3 | 0.065 | 1.14 | 4278 | 23.0 | 16.0 | 38.0 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=0 | 10 | 60.0 | -0.045 | 0.89 | 4 | 23.5 | 29.5 | 0.0 |
| INV/LONG|aligned=1 | 667 | 49.6 | 0.099 | 1.23 | 270 | 16.0 | 12.0 | 19.6 |
| INV/SHORT|aligned=0 | 8 | 62.5 | -0.037 | 0.9 | 3 | 25.5 | 32.0 | 33.3 |
| INV/SHORT|aligned=1 | 479 | 47.6 | 0.111 | 1.27 | 187 | 24.0 | 14.0 | 21.4 |
| RETEST/LONG|aligned=0 | 1129 | 51.6 | 0.026 | 1.05 | 530 | 22.0 | 20.0 | 57.2 |
| RETEST/LONG|aligned=1 | 27548 | 46.4 | 0.035 | 1.07 | 13044 | 17.0 | 12.0 | 33.2 |
| RETEST/SHORT|aligned=0 | 1513 | 54.6 | 0.096 | 1.21 | 677 | 22.0 | 21.0 | 58.3 |
| RETEST/SHORT|aligned=1 | 18040 | 45.9 | 0.038 | 1.08 | 8391 | 22.0 | 14.0 | 33.0 |

## Autopsia de SL
n_losses=23106  causas: RR-bajo×8905, contra-estructura×8108, stop-en-el-minimo×7891, killzone-Asia-largo×5018, estirado×3945, sin-nivel-detras×3738, chop×3383, SL-muy-pegado×2883, sin-causa-clara×2419, contra-sesgo×1214
- INV/LONG (n=274): killzone-Asia-largo×127, RR-bajo×103, contra-estructura×86, estirado×56, stop-en-el-minimo×53, sin-nivel-detras×33, chop×32, SL-muy-pegado×30, sin-causa-clara×18, contra-sesgo×4
- INV/SHORT (n=190): RR-bajo×82, contra-estructura×57, stop-en-el-minimo×41, estirado×41, SL-muy-pegado×33, sin-causa-clara×28, chop×26, sin-nivel-detras×13, contra-sesgo×3
- RETEST/LONG (n=13574): RR-bajo×5260, contra-estructura×4892, killzone-Asia-largo×4891, stop-en-el-minimo×4635, estirado×2338, sin-nivel-detras×2311, chop×1989, SL-muy-pegado×1623, sin-causa-clara×1141, contra-sesgo×530
- RETEST/SHORT (n=9068): RR-bajo×3460, stop-en-el-minimo×3162, contra-estructura×3073, estirado×1510, sin-nivel-detras×1381, chop×1336, sin-causa-clara×1232, SL-muy-pegado×1197, contra-sesgo×677

## Autopsia de SL · semana 2026-W44 (para revision semanal)
n_losses=4778  causas: RR-bajo×2192, stop-en-el-minimo×1993, contra-estructura×1976, contra-sesgo×1213, estirado×867, killzone-Asia-largo×762, chop×613, SL-muy-pegado×534, sin-nivel-detras×418, sin-causa-clara×394
ejemplos por causa: {"RR-bajo": ["YM-2-22042-S", "CL-1-23380-L", "NQ-1-23615-S", "YM-2-22073-S", "NQ-2-22218-S"], "stop-en-el-minimo": ["YM-2-22042-S", "YM-2-22073-S", "NQ-1-23743-S", "NQ-2-22221-S", "GC-2-22230-S"], "contra-estructura": ["NQ-2-22054-L", "YM-2-22042-S", "NQ-1-23740-S", "NQ-1-23743-S", "ES-1-23741-S"]}

## Autopsia de SL · tendencia semanal de causas (% de las perdidas de esa semana)
```json
{
  "2026-W37": {
    "n_losses": 2574,
    "causes_pct": {
      "RR-bajo": 36.5,
      "contra-estructura": 32.8,
      "stop-en-el-minimo": 32.6,
      "sin-nivel-detras": 19.0,
      "estirado": 17.5,
      "killzone-Asia-largo": 15.2,
      "chop": 14.4,
      "SL-muy-pegado": 13.1,
      "sin-causa-clara": 10.5
    }
  },
  "2026-W38": {
    "n_losses": 2051,
    "causes_pct": {
      "RR-bajo": 37.5,
      "contra-estructura": 33.3,
      "stop-en-el-minimo": 32.1,
      "killzone-Asia-largo": 23.1,
      "sin-nivel-detras": 20.8,
      "estirado": 17.8,
      "chop": 14.7,
      "SL-muy-pegado": 11.8,
      "sin-causa-clara": 11.4
    }
  },
  "2026-W39": {
    "n_losses": 2436,
    "causes_pct": {
      "RR-bajo": 35.6,
      "contra-estructura": 33.5,
      "stop-en-el-minimo": 32.1,
      "killzone-Asia-largo": 20.9,
      "sin-nivel-detras": 18.3,
      "chop": 16.1,
      "estirado": 16.0,
      "SL-muy-pegado": 13.5,
      "sin-causa-clara": 13.0
    }
  },
  "2026-W40": {
    "n_losses": 2546,
    "causes_pct": {
      "RR-bajo": 37.1,
      "stop-en-el-minimo": 33.2,
      "contra-estructura": 29.5,
      "killzone-Asia-largo": 20.3,
      "estirado": 16.7,
      "chop": 15.6,
      "sin-causa-clara": 12.4,
      "SL-muy-pegado": 12.2,
      "sin-nivel-detras": 11.9
    }
  },
  "2026-W41": {
    "n_losses": 2378,
    "causes_pct": {
      "RR-bajo": 36.0,
      "contra-estructura": 34.3,
      "stop-en-el-minimo": 31.4,
      "killzone-Asia-largo": 27.5,
      "sin-nivel-detras": 21.7,
      "estirado": 15.4,
      "chop": 14.3,
      "SL-muy-pegado": 13.0,
      "sin-causa-clara": 10.1
    }
  },
  "2026-W42": {
    "n_losses": 2434,
    "causes_pct": {
      "RR-bajo": 36.6,
      "contra-estructura": 34.5,
      "stop-en-el-minimo": 33.4,
      "killzone-Asia-largo": 27.8,
      "estirado": 17.3,
      "chop": 15.7,
      "sin-nivel-detras": 15.4,
      "SL-muy-pegado": 13.6,
      "sin-causa-clara": 9.9
    }
  },
  "2026-W43": {
    "n_losses": 2319,
    "causes_pct": {
      "RR-bajo": 34.8,
      "contra-estructura": 33.4,
      "stop-en-el-minimo": 29.1,
      "killzone-Asia-largo": 24.4,
      "sin-nivel-detras": 18.9,
      "estirado": 16.9,
      "chop": 15.6,
      "SL-muy-pegado": 13.4,
      "sin-causa-clara": 11.6
    }
  },
  "2026-W44": {
    "n_losses": 4778,
    "causes_pct": {
      "RR-bajo": 45.9,
      "stop-en-el-minimo": 41.7,
      "contra-estructura": 41.4,
      "contra-sesgo": 25.4,
      "estirado": 18.1,
      "killzone-Asia-largo": 15.9,
      "chop": 12.8,
      "SL-muy-pegado": 11.2,
      "sin-nivel-detras": 8.7,
      "sin-causa-clara": 8.2
    }
  }
}
```

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
    "n": 47752,
    "naive_expR": 0.039,
    "managed_expR": 0.116,
    "delta": 0.077,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 45.7,
    "fill_full_pct": 32.3,
    "m1_rate": 37.0,
    "m2_rate": 22.5,
    "m3_rate": 11.6,
    "beAfterM1_rate": 18.2
  },
  "by_tf_kind_side": {
    "15m/INV/LONG": {
      "n": 4,
      "naive_expR": -0.115,
      "managed_expR": 0.166,
      "delta": 0.281,
      "avgEntryBetterTk_p50": 15.1,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 25.0,
      "m1_rate": 50.0,
      "m2_rate": 50.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 0.0
    },
    "15m/RETEST/LONG": {
      "n": 253,
      "naive_expR": -0.026,
      "managed_expR": -0.161,
      "delta": -0.134,
      "avgEntryBetterTk_p50": 9.8,
      "fill_t3plus_pct": 38.3,
      "fill_full_pct": 25.3,
      "m1_rate": 32.0,
      "m2_rate": 19.4,
      "m3_rate": 8.7,
      "beAfterM1_rate": 16.2
    },
    "15m/RETEST/SHORT": {
      "n": 263,
      "naive_expR": 0.073,
      "managed_expR": 0.014,
      "delta": -0.059,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 27.4,
      "fill_full_pct": 15.2,
      "m1_rate": 34.2,
      "m2_rate": 20.5,
      "m3_rate": 12.9,
      "beAfterM1_rate": 17.9
    },
    "1m/INV/LONG": {
      "n": 437,
      "naive_expR": 0.116,
      "managed_expR": 0.258,
      "delta": 0.142,
      "avgEntryBetterTk_p50": 2.5,
      "fill_t3plus_pct": 50.6,
      "fill_full_pct": 37.1,
      "m1_rate": 41.2,
      "m2_rate": 24.7,
      "m3_rate": 11.9,
      "beAfterM1_rate": 19.5
    },
    "1m/INV/SHORT": {
      "n": 310,
      "naive_expR": 0.084,
      "managed_expR": 0.272,
      "delta": 0.189,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 48.4,
      "fill_full_pct": 36.5,
      "m1_rate": 40.6,
      "m2_rate": 24.5,
      "m3_rate": 11.9,
      "beAfterM1_rate": 18.1
    },
    "1m/RETEST/LONG": {
      "n": 16624,
      "naive_expR": 0.026,
      "managed_expR": 0.12,
      "delta": 0.094,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.5,
      "fill_full_pct": 33.8,
      "m1_rate": 36.8,
      "m2_rate": 22.3,
      "m3_rate": 11.8,
      "beAfterM1_rate": 17.6
    },
    "1m/RETEST/SHORT": {
      "n": 10849,
      "naive_expR": 0.03,
      "managed_expR": 0.153,
      "delta": 0.123,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 48.5,
      "fill_full_pct": 34.2,
      "m1_rate": 38.5,
      "m2_rate": 23.9,
      "m3_rate": 12.2,
      "beAfterM1_rate": 18.1
    },
    "29m/RETEST/LONG": {
      "n": 106,
      "naive_expR": 0.143,
      "managed_expR": -0.151,
      "delta": -0.295,
      "avgEntryBetterTk_p50": 14.45,
      "fill_t3plus_pct": 45.3,
      "fill_full_pct": 34.0,
      "m1_rate": 31.1,
      "m2_rate": 20.8,
      "m3_rate": 8.5,
      "beAfterM1_rate": 10.4
    },
    "29m/RETEST/SHORT": {
      "n": 161,
      "naive_expR": 0.175,
      "managed_expR": -0.128,
      "delta": -0.303,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 23.6,
      "fill_full_pct": 11.8,
      "m1_rate": 37.3,
      "m2_rate": 16.8,
      "m3_rate": 10.6,
      "beAfterM1_rate": 22.4
    },
    "2m/INV/LONG": {
      "n": 157,
      "naive_expR": 0.043,
      "managed_expR": 0.152,
      "delta": 0.109,
      "avgEntryBetterTk_p50": 4.2,
      "fill_t3plus_pct": 54.1,
      "fill_full_pct": 39.5,
      "m1_rate": 27.4,
      "m2_rate": 19.1,
      "m3_rate": 7.6,
      "beAfterM1_rate": 10.2
    },
    "2m/INV/SHORT": {
      "n": 116,
      "naive_expR": 0.124,
      "managed_expR": 0.277,
      "delta": 0.153,
      "avgEntryBetterTk_p50": 3.3499999999999996,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 37.9,
      "m1_rate": 35.3,
      "m2_rate": 25.0,
      "m3_rate": 14.7,
      "beAfterM1_rate": 12.1
    },
    "2m/RETEST/LONG": {
      "n": 7265,
      "naive_expR": 0.029,
      "managed_expR": 0.086,
      "delta": 0.057,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 44.5,
      "fill_full_pct": 31.6,
      "m1_rate": 35.7,
      "m2_rate": 21.6,
      "m3_rate": 11.2,
      "beAfterM1_rate": 18.3
    },
    "2m/RETEST/SHORT": {
      "n": 4763,
      "naive_expR": 0.043,
      "managed_expR": 0.127,
      "delta": 0.084,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 45.6,
      "fill_full_pct": 31.9,
      "m1_rate": 37.7,
      "m2_rate": 22.8,
      "m3_rate": 11.9,
      "beAfterM1_rate": 19.6
    },
    "3m/INV/LONG": {
      "n": 8,
      "naive_expR": 0.02,
      "managed_expR": -0.006,
      "delta": -0.026,
      "avgEntryBetterTk_p50": 4.2,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 25.0,
      "m1_rate": 12.5,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 12.5
    },
    "3m/INV/SHORT": {
      "n": 5,
      "naive_expR": 0.48,
      "managed_expR": 0.295,
      "delta": -0.185,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 20.0,
      "fill_full_pct": 20.0,
      "m1_rate": 40.0,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 40.0
    },
    "3m/RETEST/LONG": {
      "n": 764,
      "naive_expR": 0.073,
      "managed_expR": 0.009,
      "delta": -0.064,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 45.2,
      "fill_full_pct": 30.9,
      "m1_rate": 32.9,
      "m2_rate": 17.9,
      "m3_rate": 8.8,
      "beAfterM1_rate": 18.7
    },
    "3m/RETEST/SHORT": {
      "n": 738,
      "naive_expR": 0.109,
      "managed_expR": 0.081,
      "delta": -0.028,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 38.9,
      "fill_full_pct": 28.3,
      "m1_rate": 36.4,
      "m2_rate": 20.9,
      "m3_rate": 9.3,
      "beAfterM1_rate": 19.2
    },
    "5m/INV/LONG": {
      "n": 48,
      "naive_expR": 0.132,
      "managed_expR": 0.114,
      "delta": -0.018,
      "avgEntryBetterTk_p50": 3.65,
      "fill_t3plus_pct": 39.6,
      "fill_full_pct": 31.2,
      "m1_rate": 18.8,
      "m2_rate": 6.2,
      "m3_rate": 2.1,
      "beAfterM1_rate": 14.6
    },
    "5m/INV/SHORT": {
      "n": 30,
      "naive_expR": 0.201,
      "managed_expR": 0.294,
      "delta": 0.093,
      "avgEntryBetterTk_p50": 6.35,
      "fill_t3plus_pct": 56.7,
      "fill_full_pct": 40.0,
      "m1_rate": 30.0,
      "m2_rate": 23.3,
      "m3_rate": 20.0,
      "beAfterM1_rate": 13.3
    },
    "5m/RETEST/LONG": {
      "n": 2858,
      "naive_expR": 0.09,
      "managed_expR": 0.082,
      "delta": -0.009,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 37.2,
      "fill_full_pct": 26.0,
      "m1_rate": 36.5,
      "m2_rate": 22.1,
      "m3_rate": 11.0,
      "beAfterM1_rate": 19.7
    },
    "5m/RETEST/SHORT": {
      "n": 1992,
      "naive_expR": 0.073,
      "managed_expR": 0.085,
      "delta": 0.012,
      "avgEntryBetterTk_p50": 3.6,
      "fill_t3plus_pct": 37.5,
      "fill_full_pct": 24.8,
      "m1_rate": 36.0,
      "m2_rate": 21.8,
      "m3_rate": 11.3,
      "beAfterM1_rate": 19.2
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 39283,
    "layer_expR": 0.035,
    "orig_expR": 0.166,
    "delta_orig_minus_layer": 0.131,
    "delta_ci90": [
      0.07,
      0.231
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.0,
    "orig_wrTP1": 34.9,
    "slTk_p50": 22.0,
    "slOrigTk_p50": 10.0,
    "orig_wider_pct": 4.6,
    "orig_saved_from_SL": 86,
    "orig_caused_SL": 5221
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 3751,
  "invalid_by_seg": {
    "2m/RETEST/LONG": 509,
    "1m/RETEST/SHORT": 764,
    "2m/RETEST/SHORT": 249,
    "1m/RETEST/LONG": 1774,
    "1m/INV/SHORT": 48,
    "5m/RETEST/LONG": 103,
    "1m/INV/LONG": 83,
    "2m/INV/LONG": 23,
    "5m/INV/LONG": 4,
    "2m/INV/SHORT": 8,
    "5m/RETEST/SHORT": 69,
    "5m/INV/SHORT": 2,
    "3m/RETEST/LONG": 55,
    "3m/RETEST/SHORT": 42,
    "15m/RETEST/LONG": 5,
    "29m/RETEST/SHORT": 4,
    "15m/RETEST/SHORT": 8,
    "29m/RETEST/LONG": 1
  },
  "by_basis": {
    "candle1": {
      "n": 936,
      "layer_expR": 0.104,
      "orig_expR": 2.232,
      "delta_orig_minus_layer": 2.129,
      "delta_ci90": [
        -0.094,
        6.416
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 51.9,
      "orig_wrTP1": 28.8,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 3.7,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 218
    },
    "legacy": {
      "n": 6,
      "layer_expR": 0.227,
      "orig_expR": 1.598,
      "delta_orig_minus_layer": 1.372,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 83.3,
      "orig_wrTP1": 100.0,
      "slTk_p50": 7.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 50.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 0
    },
    "retestBar": {
      "n": 29603,
      "layer_expR": 0.036,
      "orig_expR": 0.131,
      "delta_orig_minus_layer": 0.095,
      "delta_ci90": [
        0.077,
        0.114
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.4,
      "orig_wrTP1": 35.6,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 5.3,
      "orig_saved_from_SL": 81,
      "orig_caused_SL": 3863
    },
    "retestBar2": {
      "n": 8744,
      "layer_expR": 0.022,
      "orig_expR": 0.063,
      "delta_orig_minus_layer": 0.041,
      "delta_ci90": [
        0.012,
        0.069
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.3,
      "orig_wrTP1": 33.3,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 1140
    }
  },
  "by_tf_kind_side": {
    "15m/RETEST/LONG": {
      "n": 247,
      "layer_expR": -0.01,
      "orig_expR": 0.527,
      "delta_orig_minus_layer": 0.537,
      "delta_ci90": [
        0.209,
        0.939
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.4,
      "orig_wrTP1": 47.8,
      "slTk_p50": 54.0,
      "slOrigTk_p50": 55.0,
      "orig_wider_pct": 30.4,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 10
    },
    "15m/RETEST/SHORT": {
      "n": 248,
      "layer_expR": 0.068,
      "orig_expR": 0.24,
      "delta_orig_minus_layer": 0.172,
      "delta_ci90": [
        -0.01,
        0.36
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 53.6,
      "orig_wrTP1": 47.2,
      "slTk_p50": 70.0,
      "slOrigTk_p50": 68.0,
      "orig_wider_pct": 26.2,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 22
    },
    "1m/INV/LONG": {
      "n": 354,
      "layer_expR": 0.109,
      "orig_expR": 0.118,
      "delta_orig_minus_layer": 0.009,
      "delta_ci90": [
        -0.174,
        0.189
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.6,
      "orig_wrTP1": 26.3,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 79
    },
    "1m/INV/SHORT": {
      "n": 252,
      "layer_expR": 0.08,
      "orig_expR": -0.044,
      "delta_orig_minus_layer": -0.123,
      "delta_ci90": [
        -0.326,
        0.086
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.2,
      "orig_wrTP1": 26.2,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 2.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 59
    },
    "1m/RETEST/LONG": {
      "n": 12656,
      "layer_expR": 0.021,
      "orig_expR": 0.079,
      "delta_orig_minus_layer": 0.058,
      "delta_ci90": [
        0.033,
        0.084
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.4,
      "orig_wrTP1": 30.4,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 1.2,
      "orig_saved_from_SL": 4,
      "orig_caused_SL": 1909
    },
    "1m/RETEST/SHORT": {
      "n": 8867,
      "layer_expR": 0.022,
      "orig_expR": 0.064,
      "delta_orig_minus_layer": 0.042,
      "delta_ci90": [
        0.015,
        0.071
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.3,
      "orig_wrTP1": 33.3,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 1156
    },
    "29m/RETEST/LONG": {
      "n": 105,
      "layer_expR": 0.154,
      "orig_expR": 1.092,
      "delta_orig_minus_layer": 0.937,
      "delta_ci90": [
        0.076,
        2.144
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.3,
      "orig_wrTP1": 60.0,
      "slTk_p50": 51.0,
      "slOrigTk_p50": 91.0,
      "orig_wider_pct": 52.4,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 0
    },
    "29m/RETEST/SHORT": {
      "n": 156,
      "layer_expR": 0.213,
      "orig_expR": 0.416,
      "delta_orig_minus_layer": 0.203,
      "delta_ci90": [
        0.014,
        0.46
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 59.0,
      "orig_wrTP1": 59.6,
      "slTk_p50": 73.5,
      "slOrigTk_p50": 92.5,
      "orig_wider_pct": 41.7,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 6
    },
    "2m/INV/LONG": {
      "n": 134,
      "layer_expR": 0.072,
      "orig_expR": 0.398,
      "delta_orig_minus_layer": 0.326,
      "delta_ci90": [
        -0.183,
        0.946
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 56.7,
      "orig_wrTP1": 29.9,
      "slTk_p50": 27.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 36
    },
    "2m/INV/SHORT": {
      "n": 107,
      "layer_expR": 0.098,
      "orig_expR": 0.036,
      "delta_orig_minus_layer": -0.062,
      "delta_ci90": [
        -0.312,
        0.221
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 51.4,
      "orig_wrTP1": 32.7,
      "slTk_p50": 30.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.7,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 21
    },
    "2m/RETEST/LONG": {
      "n": 6175,
      "layer_expR": 0.027,
      "orig_expR": 0.107,
      "delta_orig_minus_layer": 0.08,
      "delta_ci90": [
        0.046,
        0.114
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.1,
      "orig_wrTP1": 36.6,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.9,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 779
    },
    "2m/RETEST/SHORT": {
      "n": 4105,
      "layer_expR": 0.044,
      "orig_expR": 0.119,
      "delta_orig_minus_layer": 0.076,
      "delta_ci90": [
        0.034,
        0.115
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.2,
      "orig_wrTP1": 36.1,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 546
    },
    "3m/INV/LONG": {
      "n": 8,
      "layer_expR": 0.02,
      "orig_expR": 0.708,
      "delta_orig_minus_layer": 0.688,
      "delta_ci90": [
        -0.085,
        1.396
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 62.5,
      "orig_wrTP1": 50.0,
      "slTk_p50": 31.0,
      "slOrigTk_p50": 8.5,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 1
    },
    "3m/INV/SHORT": {
      "n": 5,
      "layer_expR": 0.48,
      "orig_expR": 1.078,
      "delta_orig_minus_layer": 0.598,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 100.0,
      "orig_wrTP1": 60.0,
      "slTk_p50": 55.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 2
    },
    "3m/RETEST/LONG": {
      "n": 657,
      "layer_expR": 0.077,
      "orig_expR": 0.408,
      "delta_orig_minus_layer": 0.331,
      "delta_ci90": [
        0.205,
        0.465
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.9,
      "orig_wrTP1": 41.1,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 5.5,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 86
    },
    "3m/RETEST/SHORT": {
      "n": 653,
      "layer_expR": 0.094,
      "orig_expR": 0.196,
      "delta_orig_minus_layer": 0.102,
      "delta_ci90": [
        -0.002,
        0.213
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 54.2,
      "orig_wrTP1": 39.2,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 98
    },
    "5m/INV/LONG": {
      "n": 44,
      "layer_expR": 0.162,
      "orig_expR": 0.112,
      "delta_orig_minus_layer": -0.05,
      "delta_ci90": [
        -0.426,
        0.351
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 72.7,
      "orig_wrTP1": 47.7,
      "slTk_p50": 36.0,
      "slOrigTk_p50": 11.5,
      "orig_wider_pct": 9.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 11
    },
    "5m/INV/SHORT": {
      "n": 27,
      "layer_expR": 0.279,
      "orig_expR": 73.524,
      "delta_orig_minus_layer": 73.246,
      "delta_ci90": [
        -1.025,
        221.403
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 51.9,
      "orig_wrTP1": 22.2,
      "slTk_p50": 52.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 18.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 8
    },
    "5m/RETEST/LONG": {
      "n": 2640,
      "layer_expR": 0.075,
      "orig_expR": 0.243,
      "delta_orig_minus_layer": 0.168,
      "delta_ci90": [
        0.106,
        0.233
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.3,
      "orig_wrTP1": 45.5,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 22.0,
      "orig_wider_pct": 14.8,
      "orig_saved_from_SL": 23,
      "orig_caused_SL": 229
    },
    "5m/RETEST/SHORT": {
      "n": 1838,
      "layer_expR": 0.049,
      "orig_expR": 0.166,
      "delta_orig_minus_layer": 0.116,
      "delta_ci90": [
        0.036,
        0.205
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.1,
      "orig_wrTP1": 43.1,
      "slTk_p50": 36.0,
      "slOrigTk_p50": 26.0,
      "orig_wider_pct": 17.0,
      "orig_saved_from_SL": 15,
      "orig_caused_SL": 162
    }
  },
  "since_change": {
    "changeDate": "2026-09-26",
    "n": 24964,
    "by_tf_kind_side": {
      "15m/RETEST/LONG": {
        "n": 247,
        "layer_expR": -0.01,
        "orig_expR": 0.527,
        "delta_orig_minus_layer": 0.537,
        "delta_ci90": [
          0.209,
          0.939
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 49.4,
        "orig_wrTP1": 47.8,
        "slTk_p50": 54.0,
        "slOrigTk_p50": 55.0,
        "orig_wider_pct": 30.4,
        "orig_saved_from_SL": 6,
        "orig_caused_SL": 10
      },
      "15m/RETEST/SHORT": {
        "n": 248,
        "layer_expR": 0.068,
        "orig_expR": 0.24,
        "delta_orig_minus_layer": 0.172,
        "delta_ci90": [
          -0.01,
          0.36
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 53.6,
        "orig_wrTP1": 47.2,
        "slTk_p50": 70.0,
        "slOrigTk_p50": 68.0,
        "orig_wider_pct": 26.2,
        "orig_saved_from_SL": 6,
        "orig_caused_SL": 22
      },
      "1m/INV/LONG": {
        "n": 222,
        "layer_expR": 0.083,
        "orig_expR": 0.207,
        "delta_orig_minus_layer": 0.124,
        "delta_ci90": [
          -0.08,
          0.345
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 50.0,
        "orig_wrTP1": 28.4,
        "slTk_p50": 17.0,
        "slOrigTk_p50": 5.0,
        "orig_wider_pct": 0.9,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 48
      },
      "1m/INV/SHORT": {
        "n": 148,
        "layer_expR": 0.113,
        "orig_expR": -0.051,
        "delta_orig_minus_layer": -0.164,
        "delta_ci90": [
          -0.396,
          0.066
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 48.6,
        "orig_wrTP1": 26.4,
        "slTk_p50": 25.5,
        "slOrigTk_p50": 6.0,
        "orig_wider_pct": 1.4,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 34
      },
      "1m/RETEST/LONG": {
        "n": 7475,
        "layer_expR": -0.004,
        "orig_expR": 0.029,
        "delta_orig_minus_layer": 0.033,
        "delta_ci90": [
          0.001,
          0.066
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 44.9,
        "orig_wrTP1": 29.8,
        "slTk_p50": 17.0,
        "slOrigTk_p50": 7.0,
        "orig_wider_pct": 1.3,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 1132
      },
      "1m/RETEST/SHORT": {
        "n": 5607,
        "layer_expR": 0.018,
        "orig_expR": 0.061,
        "delta_orig_minus_layer": 0.043,
        "delta_ci90": [
          0.008,
          0.077
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 46.4,
        "orig_wrTP1": 33.1,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 2.1,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 749
      },
      "29m/RETEST/LONG": {
        "n": 105,
        "layer_expR": 0.154,
        "orig_expR": 1.092,
        "delta_orig_minus_layer": 0.937,
        "delta_ci90": [
          0.076,
          2.144
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 54.3,
        "orig_wrTP1": 60.0,
        "slTk_p50": 51.0,
        "slOrigTk_p50": 91.0,
        "orig_wider_pct": 52.4,
        "orig_saved_from_SL": 6,
        "orig_caused_SL": 0
      },
      "29m/RETEST/SHORT": {
        "n": 156,
        "layer_expR": 0.213,
        "orig_expR": 0.416,
        "delta_orig_minus_layer": 0.203,
        "delta_ci90": [
          0.014,
          0.46
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 59.0,
        "orig_wrTP1": 59.6,
        "slTk_p50": 73.5,
        "slOrigTk_p50": 92.5,
        "orig_wider_pct": 41.7,
        "orig_saved_from_SL": 7,
        "orig_caused_SL": 6
      },
      "2m/INV/LONG": {
        "n": 83,
        "layer_expR": 0.134,
        "orig_expR": 0.274,
        "delta_orig_minus_layer": 0.14,
        "delta_ci90": [
          -0.386,
          0.826
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 60.2,
        "orig_wrTP1": 31.3,
        "slTk_p50": 28.0,
        "slOrigTk_p50": 9.0,
        "orig_wider_pct": 1.2,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 24
      },
      "2m/INV/SHORT": {
        "n": 57,
        "layer_expR": 0.019,
        "orig_expR": -0.218,
        "delta_orig_minus_layer": -0.237,
        "delta_ci90": [
          -0.517,
          0.042
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 57.9,
        "orig_wrTP1": 31.6,
        "slTk_p50": 36.0,
        "slOrigTk_p50": 8.0,
        "orig_wider_pct": 5.3,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 15
      },
      "2m/RETEST/LONG": {
        "n": 3684,
        "layer_expR": 0.015,
        "orig_expR": 0.075,
        "delta_orig_minus_layer": 0.06,
        "delta_ci90": [
          0.019,
          0.102
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 49.0,
        "orig_wrTP1": 36.2,
        "slTk_p50": 20.0,
        "slOrigTk_p50": 10.0,
        "orig_wider_pct": 4.2,
        "orig_saved_from_SL": 3,
        "orig_caused_SL": 475
      },
      "2m/RETEST/SHORT": {
        "n": 2582,
        "layer_expR": 0.027,
        "orig_expR": 0.079,
        "delta_orig_minus_layer": 0.052,
        "delta_ci90": [
          0.005,
          0.1
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 48.3,
        "orig_wrTP1": 34.8,
        "slTk_p50": 26.0,
        "slOrigTk_p50": 13.0,
        "orig_wider_pct": 3.1,
        "orig_saved_from_SL": 4,
        "orig_caused_SL": 352
      },
      "3m/INV/LONG": {
        "n": 8,
        "layer_expR": 0.02,
        "orig_expR": 0.708,
        "delta_orig_minus_layer": 0.688,
        "delta_ci90": [
          -0.085,
          1.396
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 62.5,
        "orig_wrTP1": 50.0,
        "slTk_p50": 31.0,
        "slOrigTk_p50": 8.5,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 1
      },
      "3m/INV/SHORT": {
        "n": 5,
        "layer_expR": 0.48,
        "orig_expR": 1.078,
        "delta_orig_minus_layer": 0.598,
        "delta_ci90": [
          null,
          null
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 100.0,
        "orig_wrTP1": 60.0,
        "slTk_p50": 55.0,
        "slOrigTk_p50": 9.0,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 2
      },
      "3m/RETEST/LONG": {
        "n": 657,
        "layer_expR": 0.077,
        "orig_expR": 0.408,
        "delta_orig_minus_layer": 0.331,
        "delta_ci90": [
          0.205,
          0.465
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 53.9,
        "orig_wrTP1": 41.1,
        "slTk_p50": 23.0,
        "slOrigTk_p50": 12.0,
        "orig_wider_pct": 5.5,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 86
      },
      "3m/RETEST/SHORT": {
        "n": 653,
        "layer_expR": 0.094,
        "orig_expR": 0.196,
        "delta_orig_minus_layer": 0.102,
        "delta_ci90": [
          -0.002,
          0.213
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 54.2,
        "orig_wrTP1": 39.2,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 3.1,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 98
      },
      "5m/INV/LONG": {
        "n": 26,
        "layer_expR": -0.028,
        "orig_expR": 0.46,
        "delta_orig_minus_layer": 0.488,
        "delta_ci90": [
          0.005,
          1.039
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 69.2,
        "orig_wrTP1": 53.8,
        "slTk_p50": 35.5,
        "slOrigTk_p50": 13.0,
        "orig_wider_pct": 3.8,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 4
      },
      "5m/INV/SHORT": {
        "n": 17,
        "layer_expR": 0.219,
        "orig_expR": 117.03,
        "delta_orig_minus_layer": 116.811,
        "delta_ci90": [
          -1.121,
          352.177
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 41.2,
        "orig_wrTP1": 11.8,
        "slTk_p50": 68.0,
        "slOrigTk_p50": 9.0,
        "orig_wider_pct": 11.8,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 5
      },
      "5m/RETEST/LONG": {
        "n": 1717,
        "layer_expR": 0.05,
        "orig_expR": 0.225,
        "delta_orig_minus_layer": 0.175,
        "delta_ci90": [
          0.098,
          0.269
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 52.7,
        "orig_wrTP1": 45.5,
        "slTk_p50": 33.0,
        "slOrigTk_p50": 23.0,
        "orig_wider_pct": 13.7,
        "orig_saved_from_SL": 16,
        "orig_caused_SL": 140
      },
      "5m/RETEST/SHORT": {
        "n": 1262,
        "layer_expR": 0.05,
        "orig_expR": 0.157,
        "delta_orig_minus_layer": 0.107,
        "delta_ci90": [
          0.023,
          0.202
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 51.5,
        "orig_wrTP1": 43.0,
        "slTk_p50": 39.0,
        "slOrigTk_p50": 28.0,
        "orig_wider_pct": 14.6,
        "orig_saved_from_SL": 8,
        "orig_caused_SL": 115
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
      "n": 16539,
      "wrTP1": 46.6,
      "nSL": 7836,
      "nTO": 1003,
      "expR": 0.023,
      "pf": 1.05,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 32.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 30.1,
      "ci90": {
        "expR": 0.023,
        "ci90": [
          0.008,
          0.038
        ],
        "p_mean_le_0": 0.007,
        "n": 16075
      }
    },
    "cuts": {
      "1.0": {
        "n": 7903,
        "wrTP1": 30.5,
        "nSL": 4767,
        "nTO": 729,
        "expR": 0.015,
        "pf": 1.02,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 21.1,
        "ci90": {
          "expR": 0.015,
          "ci90": [
            -0.011,
            0.043
          ],
          "p_mean_le_0": 0.181,
          "n": 7645
        }
      },
      "1.2": {
        "n": 6492,
        "wrTP1": 27.6,
        "nSL": 4034,
        "nTO": 668,
        "expR": 0.024,
        "pf": 1.04,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 42.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 18.8,
        "ci90": {
          "expR": 0.024,
          "ci90": [
            -0.009,
            0.055
          ],
          "p_mean_le_0": 0.119,
          "n": 6273
        }
      },
      "1.3": {
        "n": 5916,
        "wrTP1": 26.1,
        "nSL": 3729,
        "nTO": 642,
        "expR": 0.023,
        "pf": 1.04,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 42.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.5,
        "ci90": {
          "expR": 0.023,
          "ci90": [
            -0.011,
            0.057
          ],
          "p_mean_le_0": 0.138,
          "n": 5708
        }
      },
      "1.5": {
        "n": 5013,
        "wrTP1": 23.4,
        "nSL": 3252,
        "nTO": 590,
        "expR": 0.012,
        "pf": 1.02,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 15.6,
        "ci90": {
          "expR": 0.012,
          "ci90": [
            -0.026,
            0.051
          ],
          "p_mean_le_0": 0.319,
          "n": 4838
        }
      },
      "2.0": {
        "n": 3284,
        "wrTP1": 17.4,
        "nSL": 2235,
        "nTO": 479,
        "expR": -0.006,
        "pf": 0.99,
        "mfe_p25": 8.0,
        "mfe_p50": 20.5,
        "mfe_p75": 44.0,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 11.5,
        "ci90": {
          "expR": -0.006,
          "ci90": [
            -0.057,
            0.044
          ],
          "p_mean_le_0": 0.581,
          "n": 3164
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 10867,
      "wrTP1": 47.0,
      "nSL": 4990,
      "nTO": 770,
      "expR": 0.032,
      "pf": 1.07,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 38.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 30.9,
      "ci90": {
        "expR": 0.032,
        "ci90": [
          0.014,
          0.051
        ],
        "p_mean_le_0": 0.003,
        "n": 10394
      }
    },
    "cuts": {
      "1.0": {
        "n": 5182,
        "wrTP1": 31.2,
        "nSL": 3014,
        "nTO": 550,
        "expR": 0.022,
        "pf": 1.04,
        "mfe_p25": 11.0,
        "mfe_p50": 26.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 22.0,
        "ci90": {
          "expR": 0.022,
          "ci90": [
            -0.011,
            0.055
          ],
          "p_mean_le_0": 0.135,
          "n": 4893
        }
      },
      "1.2": {
        "n": 4211,
        "wrTP1": 27.6,
        "nSL": 2548,
        "nTO": 501,
        "expR": 0.014,
        "pf": 1.02,
        "mfe_p25": 11.0,
        "mfe_p50": 26.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.5,
        "ci90": {
          "expR": 0.014,
          "ci90": [
            -0.025,
            0.055
          ],
          "p_mean_le_0": 0.295,
          "n": 3960
        }
      },
      "1.3": {
        "n": 3851,
        "wrTP1": 26.0,
        "nSL": 2365,
        "nTO": 484,
        "expR": 0.009,
        "pf": 1.01,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.4,
        "ci90": {
          "expR": 0.009,
          "ci90": [
            -0.033,
            0.052
          ],
          "p_mean_le_0": 0.365,
          "n": 3614
        }
      },
      "1.5": {
        "n": 3232,
        "wrTP1": 23.2,
        "nSL": 2038,
        "nTO": 444,
        "expR": -0.001,
        "pf": 1.0,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 23.100000000000023,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 16.0,
        "ci90": {
          "expR": -0.001,
          "ci90": [
            -0.049,
            0.046
          ],
          "p_mean_le_0": 0.494,
          "n": 3026
        }
      },
      "2.0": {
        "n": 2183,
        "wrTP1": 17.8,
        "nSL": 1444,
        "nTO": 350,
        "expR": -0.023,
        "pf": 0.97,
        "mfe_p25": 12.0,
        "mfe_p50": 29.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 8.5,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 11.5,
        "ci90": {
          "expR": -0.023,
          "ci90": [
            -0.085,
            0.039
          ],
          "p_mean_le_0": 0.724,
          "n": 2037
        }
      }
    }
  },
  "15/RETEST/LONG": {
    "baseline": {
      "n": 241,
      "wrTP1": 51.0,
      "nSL": 118,
      "nTO": 0,
      "expR": 0.015,
      "pf": 1.03,
      "mfe_p25": 29.0,
      "mfe_p50": 71.0,
      "mfe_p75": 291.0,
      "winnerMAE_p75": 74.5,
      "winnerMAE_p90": 396.99999999999994,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -77.0,
      "revAfterSL_rate": 60.2,
      "ci90": {
        "expR": 0.015,
        "ci90": [
          -0.109,
          0.133
        ],
        "p_mean_le_0": 0.411,
        "n": 241
      }
    },
    "cuts": {
      "1.0": {
        "n": 81,
        "wrTP1": 32.1,
        "nSL": 55,
        "nTO": 0,
        "expR": -0.091,
        "pf": 0.87,
        "mfe_p25": 37.0,
        "mfe_p50": 75.0,
        "mfe_p75": 291.0,
        "winnerMAE_p75": 58.25,
        "winnerMAE_p90": 453.5,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -57.0,
        "revAfterSL_rate": 72.7,
        "ci90": {
          "expR": -0.091,
          "ci90": [
            -0.333,
            0.17
          ],
          "p_mean_le_0": 0.741,
          "n": 81
        }
      },
      "1.2": {
        "n": 62,
        "wrTP1": 27.4,
        "nSL": 45,
        "nTO": 0,
        "expR": -0.137,
        "pf": 0.81,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 242.5,
        "winnerMAE_p75": 59.0,
        "winnerMAE_p90": 4705.800000000004,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -60.0,
        "revAfterSL_rate": 75.6,
        "ci90": {
          "expR": -0.137,
          "ci90": [
            -0.422,
            0.164
          ],
          "p_mean_le_0": 0.775,
          "n": 62
        }
      },
      "1.3": {
        "n": 57,
        "wrTP1": 26.3,
        "nSL": 42,
        "nTO": 0,
        "expR": -0.17,
        "pf": 0.77,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 257.0,
        "winnerMAE_p75": 85.0,
        "winnerMAE_p90": 6694.199999999996,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -69.0,
        "revAfterSL_rate": 76.2,
        "ci90": {
          "expR": -0.17,
          "ci90": [
            -0.46,
            0.144
          ],
          "p_mean_le_0": 0.822,
          "n": 57
        }
      },
      "1.5": {
        "n": 40,
        "wrTP1": 30.0,
        "nSL": 28,
        "nTO": 0,
        "expR": -0.022,
        "pf": 0.97,
        "mfe_p25": 41.0,
        "mfe_p50": 81.0,
        "mfe_p75": 317.0,
        "winnerMAE_p75": 267.75,
        "winnerMAE_p90": 9676.800000000003,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.5,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -53.5,
        "revAfterSL_rate": 71.4,
        "ci90": {
          "expR": -0.022,
          "ci90": [
            -0.408,
            0.365
          ],
          "p_mean_le_0": 0.546,
          "n": 40
        }
      },
      "2.0": {
        "n": 22,
        "wrTP1": 22.7,
        "nSL": 17,
        "nTO": 0,
        "expR": -0.191,
        "pf": 0.75,
        "mfe_p25": 44.75,
        "mfe_p50": 190.5,
        "mfe_p75": 20063.5,
        "winnerMAE_p75": 10671.0,
        "winnerMAE_p90": 16837.8,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -57.0,
        "revAfterSL_rate": 64.7,
        "ci90": {
          "expR": -0.191,
          "ci90": [
            -0.684,
            0.416
          ],
          "p_mean_le_0": 0.749,
          "n": 22
        }
      }
    }
  },
  "15/RETEST/SHORT": {
    "baseline": {
      "n": 257,
      "wrTP1": 54.5,
      "nSL": 117,
      "nTO": 0,
      "expR": 0.098,
      "pf": 1.22,
      "mfe_p25": 32.0,
      "mfe_p50": 117.0,
      "mfe_p75": 1269.0,
      "winnerMAE_p75": 384.0,
      "winnerMAE_p90": 4113.200000000003,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -216.0,
      "revAfterSL_rate": 70.1,
      "ci90": {
        "expR": 0.098,
        "ci90": [
          -0.025,
          0.218
        ],
        "p_mean_le_0": 0.095,
        "n": 257
      }
    },
    "cuts": {
      "1.0": {
        "n": 89,
        "wrTP1": 38.2,
        "nSL": 55,
        "nTO": 0,
        "expR": 0.169,
        "pf": 1.27,
        "mfe_p25": 61.0,
        "mfe_p50": 180.0,
        "mfe_p75": 5828.0,
        "winnerMAE_p75": 2502.0,
        "winnerMAE_p90": 3795.5,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -230.0,
        "revAfterSL_rate": 61.8,
        "ci90": {
          "expR": 0.169,
          "ci90": [
            -0.103,
            0.43
          ],
          "p_mean_le_0": 0.17,
          "n": 89
        }
      },
      "1.2": {
        "n": 71,
        "wrTP1": 39.4,
        "nSL": 43,
        "nTO": 0,
        "expR": 0.256,
        "pf": 1.42,
        "mfe_p25": 61.0,
        "mfe_p50": 145.0,
        "mfe_p75": 6692.5,
        "winnerMAE_p75": 2418.0,
        "winnerMAE_p90": 3647.8,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -230.0,
        "revAfterSL_rate": 58.1,
        "ci90": {
          "expR": 0.256,
          "ci90": [
            -0.07,
            0.591
          ],
          "p_mean_le_0": 0.102,
          "n": 71
        }
      },
      "1.3": {
        "n": 67,
        "wrTP1": 38.8,
        "nSL": 41,
        "nTO": 0,
        "expR": 0.234,
        "pf": 1.38,
        "mfe_p25": 61.0,
        "mfe_p50": 134.0,
        "mfe_p75": 6692.5,
        "winnerMAE_p75": 2115.25,
        "winnerMAE_p90": 3200.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -230.0,
        "revAfterSL_rate": 58.5,
        "ci90": {
          "expR": 0.234,
          "ci90": [
            -0.109,
            0.595
          ],
          "p_mean_le_0": 0.131,
          "n": 67
        }
      },
      "1.5": {
        "n": 53,
        "wrTP1": 32.1,
        "nSL": 36,
        "nTO": 0,
        "expR": 0.12,
        "pf": 1.18,
        "mfe_p25": 66.0,
        "mfe_p50": 145.0,
        "mfe_p75": 7557.0,
        "winnerMAE_p75": 2376.0,
        "winnerMAE_p90": 2711.4,
        "loserMFEbeforeSL_p50": 0.5,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.5,
        "entryZoneTk_p50": -230.0,
        "revAfterSL_rate": 55.6,
        "ci90": {
          "expR": 0.12,
          "ci90": [
            -0.244,
            0.542
          ],
          "p_mean_le_0": 0.319,
          "n": 53
        }
      },
      "2.0": {
        "n": 33,
        "wrTP1": 24.2,
        "nSL": 25,
        "nTO": 0,
        "expR": -0.027,
        "pf": 0.96,
        "mfe_p25": 74.0,
        "mfe_p50": 272.0,
        "mfe_p75": 9996.0,
        "winnerMAE_p75": 2445.25,
        "winnerMAE_p90": 3000.7,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 1.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -465.0,
        "revAfterSL_rate": 48.0,
        "ci90": {
          "expR": -0.027,
          "ci90": [
            -0.505,
            0.49
          ],
          "p_mean_le_0": 0.557,
          "n": 33
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 7256,
      "wrTP1": 48.9,
      "nSL": 3384,
      "nTO": 325,
      "expR": 0.027,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 40.5,
      "ci90": {
        "expR": 0.027,
        "ci90": [
          0.004,
          0.051
        ],
        "p_mean_le_0": 0.022,
        "n": 7055
      }
    },
    "cuts": {
      "1.0": {
        "n": 3287,
        "wrTP1": 31.9,
        "nSL": 2006,
        "nTO": 233,
        "expR": 0.014,
        "pf": 1.02,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 33.4,
        "ci90": {
          "expR": 0.014,
          "ci90": [
            -0.028,
            0.058
          ],
          "p_mean_le_0": 0.286,
          "n": 3166
        }
      },
      "1.2": {
        "n": 2683,
        "wrTP1": 28.6,
        "nSL": 1706,
        "nTO": 210,
        "expR": 0.005,
        "pf": 1.01,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 31.2,
        "ci90": {
          "expR": 0.005,
          "ci90": [
            -0.043,
            0.054
          ],
          "p_mean_le_0": 0.425,
          "n": 2579
        }
      },
      "1.3": {
        "n": 2416,
        "wrTP1": 27.3,
        "nSL": 1557,
        "nTO": 200,
        "expR": 0.01,
        "pf": 1.02,
        "mfe_p25": 12.0,
        "mfe_p50": 25.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 30.1,
        "ci90": {
          "expR": 0.01,
          "ci90": [
            -0.042,
            0.063
          ],
          "p_mean_le_0": 0.379,
          "n": 2319
        }
      },
      "1.5": {
        "n": 1996,
        "wrTP1": 24.1,
        "nSL": 1325,
        "nTO": 189,
        "expR": -0.001,
        "pf": 1.0,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.900000000000034,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 27.4,
        "ci90": {
          "expR": -0.001,
          "ci90": [
            -0.065,
            0.063
          ],
          "p_mean_le_0": 0.493,
          "n": 1907
        }
      },
      "2.0": {
        "n": 1257,
        "wrTP1": 18.7,
        "nSL": 873,
        "nTO": 149,
        "expR": 0.001,
        "pf": 1.0,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 61.75,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 21.4,
        "ci90": {
          "expR": 0.001,
          "ci90": [
            -0.084,
            0.087
          ],
          "p_mean_le_0": 0.479,
          "n": 1190
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 4707,
      "wrTP1": 49.6,
      "nSL": 2149,
      "nTO": 222,
      "expR": 0.055,
      "pf": 1.12,
      "mfe_p25": 11.0,
      "mfe_p50": 24.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 33.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 41.8,
      "ci90": {
        "expR": 0.055,
        "ci90": [
          0.027,
          0.083
        ],
        "p_mean_le_0": 0.001,
        "n": 4563
      }
    },
    "cuts": {
      "1.0": {
        "n": 2152,
        "wrTP1": 33.0,
        "nSL": 1291,
        "nTO": 150,
        "expR": 0.045,
        "pf": 1.07,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 65.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 33.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 33.8,
        "ci90": {
          "expR": 0.045,
          "ci90": [
            -0.008,
            0.1
          ],
          "p_mean_le_0": 0.079,
          "n": 2071
        }
      },
      "1.2": {
        "n": 1730,
        "wrTP1": 29.6,
        "nSL": 1082,
        "nTO": 136,
        "expR": 0.04,
        "pf": 1.06,
        "mfe_p25": 17.0,
        "mfe_p50": 34.0,
        "mfe_p75": 70.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 30.9,
        "ci90": {
          "expR": 0.04,
          "ci90": [
            -0.021,
            0.102
          ],
          "p_mean_le_0": 0.141,
          "n": 1661
        }
      },
      "1.3": {
        "n": 1556,
        "wrTP1": 27.8,
        "nSL": 996,
        "nTO": 128,
        "expR": 0.028,
        "pf": 1.04,
        "mfe_p25": 17.0,
        "mfe_p50": 35.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 33.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 29.4,
        "ci90": {
          "expR": 0.028,
          "ci90": [
            -0.037,
            0.097
          ],
          "p_mean_le_0": 0.241,
          "n": 1493
        }
      },
      "1.5": {
        "n": 1284,
        "wrTP1": 24.9,
        "nSL": 853,
        "nTO": 111,
        "expR": 0.018,
        "pf": 1.03,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 33.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 27.5,
        "ci90": {
          "expR": 0.018,
          "ci90": [
            -0.061,
            0.098
          ],
          "p_mean_le_0": 0.345,
          "n": 1235
        }
      },
      "2.0": {
        "n": 835,
        "wrTP1": 20.2,
        "nSL": 579,
        "nTO": 87,
        "expR": 0.029,
        "pf": 1.04,
        "mfe_p25": 18.0,
        "mfe_p50": 38.5,
        "mfe_p75": 81.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.200000000000017,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 22.6,
        "ci90": {
          "expR": 0.029,
          "ci90": [
            -0.074,
            0.133
          ],
          "p_mean_le_0": 0.34,
          "n": 802
        }
      }
    }
  },
  "29/RETEST/LONG": {
    "baseline": {
      "n": 100,
      "wrTP1": 57.0,
      "nSL": 43,
      "nTO": 0,
      "expR": 0.212,
      "pf": 1.49,
      "mfe_p25": 42.0,
      "mfe_p50": 118.5,
      "mfe_p75": 1455.5,
      "winnerMAE_p75": 331.0,
      "winnerMAE_p90": 8496.399999999994,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -71.0,
      "revAfterSL_rate": 62.8,
      "ci90": {
        "expR": 0.212,
        "ci90": [
          0.003,
          0.437
        ],
        "p_mean_le_0": 0.05,
        "n": 100
      }
    },
    "cuts": {
      "1.0": {
        "n": 40,
        "wrTP1": 42.5,
        "nSL": 23,
        "nTO": 0,
        "expR": 0.338,
        "pf": 1.59,
        "mfe_p25": 43.5,
        "mfe_p50": 97.5,
        "mfe_p75": 465.5,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 1451.2000000000012,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -39.5,
        "revAfterSL_rate": 73.9,
        "ci90": {
          "expR": 0.338,
          "ci90": [
            -0.103,
            0.81
          ],
          "p_mean_le_0": 0.106,
          "n": 40
        }
      },
      "1.2": {
        "n": 30,
        "wrTP1": 33.3,
        "nSL": 20,
        "nTO": 0,
        "expR": 0.195,
        "pf": 1.29,
        "mfe_p25": 55.0,
        "mfe_p50": 97.5,
        "mfe_p75": 582.5,
        "winnerMAE_p75": 79.0,
        "winnerMAE_p90": 431.7999999999988,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -38.0,
        "revAfterSL_rate": 70.0,
        "ci90": {
          "expR": 0.195,
          "ci90": [
            -0.344,
            0.809
          ],
          "p_mean_le_0": 0.293,
          "n": 30
        }
      },
      "1.3": {
        "n": 27,
        "wrTP1": 33.3,
        "nSL": 18,
        "nTO": 0,
        "expR": 0.245,
        "pf": 1.37,
        "mfe_p25": 55.0,
        "mfe_p50": 91.0,
        "mfe_p75": 524.0,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 767.6000000000006,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -41.0,
        "revAfterSL_rate": 66.7,
        "ci90": {
          "expR": 0.245,
          "ci90": [
            -0.34,
            0.864
          ],
          "p_mean_le_0": 0.273,
          "n": 27
        }
      },
      "1.5": {
        "n": 23,
        "wrTP1": 30.4,
        "nSL": 16,
        "nTO": 0,
        "expR": 0.255,
        "pf": 1.37,
        "mfe_p25": 55.5,
        "mfe_p50": 142.0,
        "mfe_p75": 1142.5,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 1439.2000000000012,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -42.0,
        "revAfterSL_rate": 62.5,
        "ci90": {
          "expR": 0.255,
          "ci90": [
            -0.403,
            0.964
          ],
          "p_mean_le_0": 0.282,
          "n": 23
        }
      }
    }
  },
  "29/RETEST/SHORT": {
    "baseline": {
      "n": 157,
      "wrTP1": 58.6,
      "nSL": 65,
      "nTO": 0,
      "expR": 0.205,
      "pf": 1.5,
      "mfe_p25": 30.0,
      "mfe_p50": 102.0,
      "mfe_p75": 727.0,
      "winnerMAE_p75": 196.75,
      "winnerMAE_p90": 2354.400000000008,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -198.0,
      "revAfterSL_rate": 70.8,
      "ci90": {
        "expR": 0.205,
        "ci90": [
          0.055,
          0.351
        ],
        "p_mean_le_0": 0.011,
        "n": 157
      }
    },
    "cuts": {
      "1.0": {
        "n": 48,
        "wrTP1": 43.8,
        "nSL": 27,
        "nTO": 0,
        "expR": 0.306,
        "pf": 1.54,
        "mfe_p25": 47.0,
        "mfe_p50": 107.5,
        "mfe_p75": 824.75,
        "winnerMAE_p75": 292.0,
        "winnerMAE_p90": 1161.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -218.0,
        "revAfterSL_rate": 51.9,
        "ci90": {
          "expR": 0.306,
          "ci90": [
            -0.063,
            0.676
          ],
          "p_mean_le_0": 0.087,
          "n": 48
        }
      },
      "1.2": {
        "n": 38,
        "wrTP1": 36.8,
        "nSL": 24,
        "nTO": 0,
        "expR": 0.236,
        "pf": 1.37,
        "mfe_p25": 48.5,
        "mfe_p50": 130.5,
        "mfe_p75": 1148.75,
        "winnerMAE_p75": 375.25,
        "winnerMAE_p90": 2089.200000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -259.5,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.236,
          "ci90": [
            -0.195,
            0.714
          ],
          "p_mean_le_0": 0.191,
          "n": 38
        }
      },
      "1.3": {
        "n": 35,
        "wrTP1": 34.3,
        "nSL": 23,
        "nTO": 0,
        "expR": 0.215,
        "pf": 1.33,
        "mfe_p25": 84.0,
        "mfe_p50": 177.0,
        "mfe_p75": 1223.5,
        "winnerMAE_p75": 592.5,
        "winnerMAE_p90": 2354.4000000000005,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -281.0,
        "revAfterSL_rate": 52.2,
        "ci90": {
          "expR": 0.215,
          "ci90": [
            -0.255,
            0.677
          ],
          "p_mean_le_0": 0.24,
          "n": 35
        }
      },
      "1.5": {
        "n": 27,
        "wrTP1": 37.0,
        "nSL": 17,
        "nTO": 0,
        "expR": 0.354,
        "pf": 1.56,
        "mfe_p25": 84.0,
        "mfe_p50": 113.0,
        "mfe_p75": 672.0,
        "winnerMAE_p75": 267.75,
        "winnerMAE_p90": 478.7999999999997,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -198.0,
        "revAfterSL_rate": 41.2,
        "ci90": {
          "expR": 0.354,
          "ci90": [
            -0.224,
            0.899
          ],
          "p_mean_le_0": 0.164,
          "n": 27
        }
      }
    }
  },
  "3/RETEST/LONG": {
    "baseline": {
      "n": 757,
      "wrTP1": 54.0,
      "nSL": 342,
      "nTO": 6,
      "expR": 0.08,
      "pf": 1.18,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 31.0,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 54.4,
      "ci90": {
        "expR": 0.08,
        "ci90": [
          0.014,
          0.145
        ],
        "p_mean_le_0": 0.018,
        "n": 753
      }
    },
    "cuts": {
      "1.0": {
        "n": 264,
        "wrTP1": 39.4,
        "nSL": 158,
        "nTO": 2,
        "expR": 0.107,
        "pf": 1.18,
        "mfe_p25": 14.0,
        "mfe_p50": 32.0,
        "mfe_p75": 68.25,
        "winnerMAE_p75": 13.25,
        "winnerMAE_p90": 38.80000000000001,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -16.5,
        "revAfterSL_rate": 48.7,
        "ci90": {
          "expR": 0.107,
          "ci90": [
            -0.031,
            0.26
          ],
          "p_mean_le_0": 0.106,
          "n": 264
        }
      },
      "1.2": {
        "n": 198,
        "wrTP1": 36.4,
        "nSL": 124,
        "nTO": 2,
        "expR": 0.112,
        "pf": 1.18,
        "mfe_p25": 16.25,
        "mfe_p50": 36.0,
        "mfe_p75": 76.0,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 35.09999999999999,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -16.5,
        "revAfterSL_rate": 47.6,
        "ci90": {
          "expR": 0.112,
          "ci90": [
            -0.066,
            0.296
          ],
          "p_mean_le_0": 0.144,
          "n": 198
        }
      },
      "1.3": {
        "n": 171,
        "wrTP1": 36.3,
        "nSL": 107,
        "nTO": 2,
        "expR": 0.141,
        "pf": 1.23,
        "mfe_p25": 21.0,
        "mfe_p50": 37.0,
        "mfe_p75": 76.0,
        "winnerMAE_p75": 13.75,
        "winnerMAE_p90": 39.599999999999994,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 46.7,
        "ci90": {
          "expR": 0.141,
          "ci90": [
            -0.052,
            0.34
          ],
          "p_mean_le_0": 0.116,
          "n": 171
        }
      },
      "1.5": {
        "n": 127,
        "wrTP1": 37.0,
        "nSL": 78,
        "nTO": 2,
        "expR": 0.242,
        "pf": 1.39,
        "mfe_p25": 22.5,
        "mfe_p50": 41.0,
        "mfe_p75": 80.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 43.999999999999986,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 41.0,
        "ci90": {
          "expR": 0.242,
          "ci90": [
            0.008,
            0.477
          ],
          "p_mean_le_0": 0.045,
          "n": 127
        }
      },
      "2.0": {
        "n": 70,
        "wrTP1": 32.9,
        "nSL": 45,
        "nTO": 2,
        "expR": 0.295,
        "pf": 1.46,
        "mfe_p25": 31.0,
        "mfe_p50": 50.0,
        "mfe_p75": 87.25,
        "winnerMAE_p75": 12.5,
        "winnerMAE_p90": 26.400000000000002,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 40.0,
        "ci90": {
          "expR": 0.295,
          "ci90": [
            -0.051,
            0.655
          ],
          "p_mean_le_0": 0.084,
          "n": 70
        }
      }
    }
  },
  "3/RETEST/SHORT": {
    "baseline": {
      "n": 725,
      "wrTP1": 55.3,
      "nSL": 314,
      "nTO": 10,
      "expR": 0.12,
      "pf": 1.27,
      "mfe_p25": 11.0,
      "mfe_p50": 21.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 34.0,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -22.0,
      "revAfterSL_rate": 57.3,
      "ci90": {
        "expR": 0.12,
        "ci90": [
          0.05,
          0.184
        ],
        "p_mean_le_0": 0.002,
        "n": 721
      }
    },
    "cuts": {
      "1.0": {
        "n": 250,
        "wrTP1": 40.4,
        "nSL": 140,
        "nTO": 9,
        "expR": 0.195,
        "pf": 1.34,
        "mfe_p25": 15.0,
        "mfe_p50": 27.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 30.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 52.9,
        "ci90": {
          "expR": 0.195,
          "ci90": [
            0.047,
            0.354
          ],
          "p_mean_le_0": 0.013,
          "n": 247
        }
      },
      "1.2": {
        "n": 184,
        "wrTP1": 36.4,
        "nSL": 108,
        "nTO": 9,
        "expR": 0.201,
        "pf": 1.33,
        "mfe_p25": 16.0,
        "mfe_p50": 29.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 30.799999999999997,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.201,
          "ci90": [
            0.005,
            0.389
          ],
          "p_mean_le_0": 0.044,
          "n": 181
        }
      },
      "1.3": {
        "n": 159,
        "wrTP1": 35.8,
        "nSL": 93,
        "nTO": 9,
        "expR": 0.238,
        "pf": 1.4,
        "mfe_p25": 16.0,
        "mfe_p50": 29.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 30.199999999999996,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 46.2,
        "ci90": {
          "expR": 0.238,
          "ci90": [
            0.031,
            0.449
          ],
          "p_mean_le_0": 0.027,
          "n": 156
        }
      },
      "1.5": {
        "n": 132,
        "wrTP1": 31.1,
        "nSL": 83,
        "nTO": 8,
        "expR": 0.171,
        "pf": 1.27,
        "mfe_p25": 16.25,
        "mfe_p50": 29.5,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 41.0,
        "ci90": {
          "expR": 0.171,
          "ci90": [
            -0.071,
            0.412
          ],
          "p_mean_le_0": 0.122,
          "n": 130
        }
      },
      "2.0": {
        "n": 67,
        "wrTP1": 31.3,
        "nSL": 41,
        "nTO": 5,
        "expR": 0.382,
        "pf": 1.61,
        "mfe_p25": 19.25,
        "mfe_p50": 33.0,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 22.0,
        "ci90": {
          "expR": 0.382,
          "ci90": [
            0.022,
            0.772
          ],
          "p_mean_le_0": 0.042,
          "n": 66
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 2863,
      "wrTP1": 53.1,
      "nSL": 1216,
      "nTO": 126,
      "expR": 0.103,
      "pf": 1.23,
      "mfe_p25": 14.0,
      "mfe_p50": 32.0,
      "mfe_p75": 76.0,
      "winnerMAE_p75": 24.0,
      "winnerMAE_p90": 72.0,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -35.0,
      "revAfterSL_rate": 51.2,
      "ci90": {
        "expR": 0.103,
        "ci90": [
          0.066,
          0.139
        ],
        "p_mean_le_0": 0.0,
        "n": 2753
      }
    },
    "cuts": {
      "1.0": {
        "n": 1183,
        "wrTP1": 36.5,
        "nSL": 670,
        "nTO": 81,
        "expR": 0.142,
        "pf": 1.24,
        "mfe_p25": 19.0,
        "mfe_p50": 41.0,
        "mfe_p75": 95.0,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 60.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 46.0,
        "ci90": {
          "expR": 0.142,
          "ci90": [
            0.068,
            0.219
          ],
          "p_mean_le_0": 0.001,
          "n": 1117
        }
      },
      "1.2": {
        "n": 965,
        "wrTP1": 34.2,
        "nSL": 561,
        "nTO": 74,
        "expR": 0.161,
        "pf": 1.26,
        "mfe_p25": 19.0,
        "mfe_p50": 41.5,
        "mfe_p75": 95.0,
        "winnerMAE_p75": 19.75,
        "winnerMAE_p90": 43.200000000000045,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 43.5,
        "ci90": {
          "expR": 0.161,
          "ci90": [
            0.074,
            0.249
          ],
          "p_mean_le_0": 0.0,
          "n": 906
        }
      },
      "1.3": {
        "n": 871,
        "wrTP1": 31.3,
        "nSL": 529,
        "nTO": 69,
        "expR": 0.125,
        "pf": 1.19,
        "mfe_p25": 19.0,
        "mfe_p50": 41.0,
        "mfe_p75": 96.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 38.80000000000001,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 42.5,
        "ci90": {
          "expR": 0.125,
          "ci90": [
            0.03,
            0.222
          ],
          "p_mean_le_0": 0.016,
          "n": 817
        }
      },
      "1.5": {
        "n": 712,
        "wrTP1": 29.9,
        "nSL": 444,
        "nTO": 55,
        "expR": 0.145,
        "pf": 1.22,
        "mfe_p25": 20.0,
        "mfe_p50": 41.0,
        "mfe_p75": 98.5,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 37.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 41.7,
        "ci90": {
          "expR": 0.145,
          "ci90": [
            0.038,
            0.255
          ],
          "p_mean_le_0": 0.013,
          "n": 671
        }
      },
      "2.0": {
        "n": 451,
        "wrTP1": 24.2,
        "nSL": 302,
        "nTO": 40,
        "expR": 0.106,
        "pf": 1.15,
        "mfe_p25": 21.0,
        "mfe_p50": 46.5,
        "mfe_p75": 109.25,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 34.400000000000006,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 33.4,
        "ci90": {
          "expR": 0.106,
          "ci90": [
            -0.035,
            0.253
          ],
          "p_mean_le_0": 0.114,
          "n": 424
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 1985,
      "wrTP1": 52.0,
      "nSL": 845,
      "nTO": 108,
      "expR": 0.085,
      "pf": 1.19,
      "mfe_p25": 16.0,
      "mfe_p50": 37.0,
      "mfe_p75": 85.0,
      "winnerMAE_p75": 29.0,
      "winnerMAE_p90": 78.89999999999998,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -38.0,
      "revAfterSL_rate": 48.6,
      "ci90": {
        "expR": 0.085,
        "ci90": [
          0.041,
          0.13
        ],
        "p_mean_le_0": 0.001,
        "n": 1889
      }
    },
    "cuts": {
      "1.0": {
        "n": 837,
        "wrTP1": 33.2,
        "nSL": 493,
        "nTO": 66,
        "expR": 0.062,
        "pf": 1.1,
        "mfe_p25": 22.0,
        "mfe_p50": 47.5,
        "mfe_p75": 105.0,
        "winnerMAE_p75": 25.0,
        "winnerMAE_p90": 58.80000000000007,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -34.0,
        "revAfterSL_rate": 42.2,
        "ci90": {
          "expR": 0.062,
          "ci90": [
            -0.026,
            0.148
          ],
          "p_mean_le_0": 0.134,
          "n": 782
        }
      },
      "1.2": {
        "n": 670,
        "wrTP1": 29.0,
        "nSL": 419,
        "nTO": 57,
        "expR": 0.035,
        "pf": 1.05,
        "mfe_p25": 24.0,
        "mfe_p50": 49.0,
        "mfe_p75": 108.5,
        "winnerMAE_p75": 23.0,
        "winnerMAE_p90": 63.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -35.5,
        "revAfterSL_rate": 38.7,
        "ci90": {
          "expR": 0.035,
          "ci90": [
            -0.074,
            0.144
          ],
          "p_mean_le_0": 0.299,
          "n": 623
        }
      },
      "1.3": {
        "n": 613,
        "wrTP1": 27.7,
        "nSL": 391,
        "nTO": 52,
        "expR": 0.015,
        "pf": 1.02,
        "mfe_p25": 24.0,
        "mfe_p50": 50.0,
        "mfe_p75": 114.0,
        "winnerMAE_p75": 23.0,
        "winnerMAE_p90": 63.99999999999994,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -36.0,
        "revAfterSL_rate": 38.4,
        "ci90": {
          "expR": 0.015,
          "ci90": [
            -0.095,
            0.131
          ],
          "p_mean_le_0": 0.414,
          "n": 571
        }
      },
      "1.5": {
        "n": 504,
        "wrTP1": 26.8,
        "nSL": 321,
        "nTO": 48,
        "expR": 0.048,
        "pf": 1.07,
        "mfe_p25": 24.25,
        "mfe_p50": 52.0,
        "mfe_p75": 114.0,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 69.00000000000009,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -34.5,
        "revAfterSL_rate": 34.0,
        "ci90": {
          "expR": 0.048,
          "ci90": [
            -0.074,
            0.178
          ],
          "p_mean_le_0": 0.268,
          "n": 466
        }
      },
      "2.0": {
        "n": 332,
        "wrTP1": 20.5,
        "nSL": 231,
        "nTO": 33,
        "expR": -0.031,
        "pf": 0.96,
        "mfe_p25": 27.75,
        "mfe_p50": 55.5,
        "mfe_p75": 115.25,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 46.10000000000003,
        "loserMFEbeforeSL_p50": 14.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -35.0,
        "revAfterSL_rate": 29.0,
        "ci90": {
          "expR": -0.031,
          "ci90": [
            -0.194,
            0.14
          ],
          "p_mean_le_0": 0.628,
          "n": 308
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
      "n": 3857,
      "wrTP1": 45.2,
      "nSL": 1883,
      "nTO": 231,
      "expR": -0.006,
      "pf": 0.99,
      "mfe_p25": 7.0,
      "mfe_p50": 14.0,
      "mfe_p75": 31.0,
      "winnerMAE_p75": 9.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 30.3,
      "ci90": {
        "expR": -0.006,
        "ci90": [
          -0.037,
          0.025
        ],
        "p_mean_le_0": 0.646,
        "n": 3759
      }
    },
    "cuts": {
      "1.2": {
        "n": 1453,
        "wrTP1": 26.8,
        "nSL": 911,
        "nTO": 152,
        "expR": 0.004,
        "pf": 1.01,
        "mfe_p25": 10.0,
        "mfe_p50": 22.0,
        "mfe_p75": 39.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 20.1,
        "ci90": {
          "expR": 0.004,
          "ci90": [
            -0.062,
            0.069
          ],
          "p_mean_le_0": 0.449,
          "n": 1412
        }
      },
      "1.3": {
        "n": 1331,
        "wrTP1": 25.3,
        "nSL": 847,
        "nTO": 147,
        "expR": -0.001,
        "pf": 1.0,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 39.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 19.2,
        "ci90": {
          "expR": -0.001,
          "ci90": [
            -0.069,
            0.068
          ],
          "p_mean_le_0": 0.532,
          "n": 1293
        }
      },
      "1.5": {
        "n": 1132,
        "wrTP1": 22.3,
        "nSL": 742,
        "nTO": 138,
        "expR": -0.024,
        "pf": 0.97,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 39.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 18.900000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.5,
        "ci90": {
          "expR": -0.024,
          "ci90": [
            -0.1,
            0.054
          ],
          "p_mean_le_0": 0.691,
          "n": 1101
        }
      },
      "2.0": {
        "n": 759,
        "wrTP1": 16.9,
        "nSL": 522,
        "nTO": 109,
        "expR": -0.049,
        "pf": 0.93,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 12.299999999999997,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 11.7,
        "ci90": {
          "expR": -0.049,
          "ci90": [
            -0.149,
            0.054
          ],
          "p_mean_le_0": 0.789,
          "n": 736
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 3196,
      "wrTP1": 47.9,
      "nSL": 1522,
      "nTO": 143,
      "expR": 0.014,
      "pf": 1.03,
      "mfe_p25": 9.0,
      "mfe_p50": 19.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 31.7,
      "ci90": {
        "expR": 0.014,
        "ci90": [
          -0.017,
          0.048
        ],
        "p_mean_le_0": 0.228,
        "n": 3128
      }
    },
    "cuts": {
      "1.2": {
        "n": 1150,
        "wrTP1": 28.0,
        "nSL": 731,
        "nTO": 97,
        "expR": -0.01,
        "pf": 0.98,
        "mfe_p25": 13.0,
        "mfe_p50": 29.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 30.800000000000068,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 7.5,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 20.2,
        "ci90": {
          "expR": -0.01,
          "ci90": [
            -0.081,
            0.064
          ],
          "p_mean_le_0": 0.594,
          "n": 1118
        }
      },
      "1.3": {
        "n": 1046,
        "wrTP1": 26.4,
        "nSL": 676,
        "nTO": 94,
        "expR": -0.017,
        "pf": 0.97,
        "mfe_p25": 13.0,
        "mfe_p50": 29.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.1,
        "ci90": {
          "expR": -0.017,
          "ci90": [
            -0.095,
            0.063
          ],
          "p_mean_le_0": 0.666,
          "n": 1016
        }
      },
      "1.5": {
        "n": 856,
        "wrTP1": 23.4,
        "nSL": 564,
        "nTO": 92,
        "expR": -0.018,
        "pf": 0.97,
        "mfe_p25": 15.0,
        "mfe_p50": 31.0,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 26.099999999999994,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 16.3,
        "ci90": {
          "expR": -0.018,
          "ci90": [
            -0.103,
            0.074
          ],
          "p_mean_le_0": 0.633,
          "n": 827
        }
      },
      "2.0": {
        "n": 563,
        "wrTP1": 17.4,
        "nSL": 388,
        "nTO": 77,
        "expR": -0.031,
        "pf": 0.96,
        "mfe_p25": 16.0,
        "mfe_p50": 34.5,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 10.75,
        "winnerMAE_p90": 23.299999999999997,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 11.1,
        "ci90": {
          "expR": -0.031,
          "ci90": [
            -0.144,
            0.092
          ],
          "p_mean_le_0": 0.668,
          "n": 538
        }
      }
    }
  },
  "15/RETEST/LONG": {
    "baseline": {
      "n": 241,
      "wrTP1": 51.0,
      "nSL": 118,
      "nTO": 0,
      "expR": 0.015,
      "pf": 1.03,
      "mfe_p25": 29.0,
      "mfe_p50": 71.0,
      "mfe_p75": 291.0,
      "winnerMAE_p75": 74.5,
      "winnerMAE_p90": 396.99999999999994,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -77.0,
      "revAfterSL_rate": 60.2,
      "ci90": {
        "expR": 0.015,
        "ci90": [
          -0.109,
          0.133
        ],
        "p_mean_le_0": 0.411,
        "n": 241
      }
    },
    "cuts": {
      "1.2": {
        "n": 62,
        "wrTP1": 27.4,
        "nSL": 45,
        "nTO": 0,
        "expR": -0.137,
        "pf": 0.81,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 242.5,
        "winnerMAE_p75": 59.0,
        "winnerMAE_p90": 4705.800000000004,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -60.0,
        "revAfterSL_rate": 75.6,
        "ci90": {
          "expR": -0.137,
          "ci90": [
            -0.422,
            0.164
          ],
          "p_mean_le_0": 0.775,
          "n": 62
        }
      },
      "1.3": {
        "n": 57,
        "wrTP1": 26.3,
        "nSL": 42,
        "nTO": 0,
        "expR": -0.17,
        "pf": 0.77,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 257.0,
        "winnerMAE_p75": 85.0,
        "winnerMAE_p90": 6694.199999999996,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -69.0,
        "revAfterSL_rate": 76.2,
        "ci90": {
          "expR": -0.17,
          "ci90": [
            -0.46,
            0.144
          ],
          "p_mean_le_0": 0.822,
          "n": 57
        }
      },
      "1.5": {
        "n": 40,
        "wrTP1": 30.0,
        "nSL": 28,
        "nTO": 0,
        "expR": -0.022,
        "pf": 0.97,
        "mfe_p25": 41.0,
        "mfe_p50": 81.0,
        "mfe_p75": 317.0,
        "winnerMAE_p75": 267.75,
        "winnerMAE_p90": 9676.800000000003,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.5,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -53.5,
        "revAfterSL_rate": 71.4,
        "ci90": {
          "expR": -0.022,
          "ci90": [
            -0.408,
            0.365
          ],
          "p_mean_le_0": 0.546,
          "n": 40
        }
      },
      "2.0": {
        "n": 22,
        "wrTP1": 22.7,
        "nSL": 17,
        "nTO": 0,
        "expR": -0.191,
        "pf": 0.75,
        "mfe_p25": 44.75,
        "mfe_p50": 190.5,
        "mfe_p75": 20063.5,
        "winnerMAE_p75": 10671.0,
        "winnerMAE_p90": 16837.8,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -57.0,
        "revAfterSL_rate": 64.7,
        "ci90": {
          "expR": -0.191,
          "ci90": [
            -0.684,
            0.416
          ],
          "p_mean_le_0": 0.749,
          "n": 22
        }
      }
    }
  },
  "15/RETEST/SHORT": {
    "baseline": {
      "n": 257,
      "wrTP1": 54.5,
      "nSL": 117,
      "nTO": 0,
      "expR": 0.098,
      "pf": 1.22,
      "mfe_p25": 32.0,
      "mfe_p50": 117.0,
      "mfe_p75": 1269.0,
      "winnerMAE_p75": 384.0,
      "winnerMAE_p90": 4113.200000000003,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -216.0,
      "revAfterSL_rate": 70.1,
      "ci90": {
        "expR": 0.098,
        "ci90": [
          -0.025,
          0.218
        ],
        "p_mean_le_0": 0.095,
        "n": 257
      }
    },
    "cuts": {
      "1.2": {
        "n": 71,
        "wrTP1": 39.4,
        "nSL": 43,
        "nTO": 0,
        "expR": 0.256,
        "pf": 1.42,
        "mfe_p25": 61.0,
        "mfe_p50": 145.0,
        "mfe_p75": 6692.5,
        "winnerMAE_p75": 2418.0,
        "winnerMAE_p90": 3647.8,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -230.0,
        "revAfterSL_rate": 58.1,
        "ci90": {
          "expR": 0.256,
          "ci90": [
            -0.07,
            0.591
          ],
          "p_mean_le_0": 0.102,
          "n": 71
        }
      },
      "1.3": {
        "n": 67,
        "wrTP1": 38.8,
        "nSL": 41,
        "nTO": 0,
        "expR": 0.234,
        "pf": 1.38,
        "mfe_p25": 61.0,
        "mfe_p50": 134.0,
        "mfe_p75": 6692.5,
        "winnerMAE_p75": 2115.25,
        "winnerMAE_p90": 3200.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -230.0,
        "revAfterSL_rate": 58.5,
        "ci90": {
          "expR": 0.234,
          "ci90": [
            -0.109,
            0.595
          ],
          "p_mean_le_0": 0.131,
          "n": 67
        }
      },
      "1.5": {
        "n": 53,
        "wrTP1": 32.1,
        "nSL": 36,
        "nTO": 0,
        "expR": 0.12,
        "pf": 1.18,
        "mfe_p25": 66.0,
        "mfe_p50": 145.0,
        "mfe_p75": 7557.0,
        "winnerMAE_p75": 2376.0,
        "winnerMAE_p90": 2711.4,
        "loserMFEbeforeSL_p50": 0.5,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.5,
        "entryZoneTk_p50": -230.0,
        "revAfterSL_rate": 55.6,
        "ci90": {
          "expR": 0.12,
          "ci90": [
            -0.244,
            0.542
          ],
          "p_mean_le_0": 0.319,
          "n": 53
        }
      },
      "2.0": {
        "n": 33,
        "wrTP1": 24.2,
        "nSL": 25,
        "nTO": 0,
        "expR": -0.027,
        "pf": 0.96,
        "mfe_p25": 74.0,
        "mfe_p50": 272.0,
        "mfe_p75": 9996.0,
        "winnerMAE_p75": 2445.25,
        "winnerMAE_p90": 3000.7,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 1.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -465.0,
        "revAfterSL_rate": 48.0,
        "ci90": {
          "expR": -0.027,
          "ci90": [
            -0.505,
            0.49
          ],
          "p_mean_le_0": 0.557,
          "n": 33
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 1692,
      "wrTP1": 47.2,
      "nSL": 843,
      "nTO": 50,
      "expR": -0.025,
      "pf": 0.95,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 27.200000000000045,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 40.7,
      "ci90": {
        "expR": -0.025,
        "ci90": [
          -0.071,
          0.02
        ],
        "p_mean_le_0": 0.818,
        "n": 1670
      }
    },
    "cuts": {
      "1.2": {
        "n": 623,
        "wrTP1": 27.3,
        "nSL": 421,
        "nTO": 32,
        "expR": -0.072,
        "pf": 0.9,
        "mfe_p25": 12.0,
        "mfe_p50": 27.5,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.099999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 34.9,
        "ci90": {
          "expR": -0.072,
          "ci90": [
            -0.173,
            0.03
          ],
          "p_mean_le_0": 0.875,
          "n": 612
        }
      },
      "1.3": {
        "n": 551,
        "wrTP1": 26.0,
        "nSL": 378,
        "nTO": 30,
        "expR": -0.067,
        "pf": 0.9,
        "mfe_p25": 13.0,
        "mfe_p50": 28.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.799999999999997,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 34.4,
        "ci90": {
          "expR": -0.067,
          "ci90": [
            -0.174,
            0.045
          ],
          "p_mean_le_0": 0.849,
          "n": 541
        }
      },
      "1.5": {
        "n": 458,
        "wrTP1": 23.8,
        "nSL": 322,
        "nTO": 27,
        "expR": -0.07,
        "pf": 0.9,
        "mfe_p25": 13.0,
        "mfe_p50": 28.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 21.200000000000003,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 31.4,
        "ci90": {
          "expR": -0.07,
          "ci90": [
            -0.19,
            0.054
          ],
          "p_mean_le_0": 0.822,
          "n": 449
        }
      },
      "2.0": {
        "n": 289,
        "wrTP1": 16.6,
        "nSL": 217,
        "nTO": 24,
        "expR": -0.131,
        "pf": 0.83,
        "mfe_p25": 14.0,
        "mfe_p50": 30.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 24.60000000000005,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 21.2,
        "ci90": {
          "expR": -0.131,
          "ci90": [
            -0.295,
            0.048
          ],
          "p_mean_le_0": 0.882,
          "n": 282
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 1440,
      "wrTP1": 49.5,
      "nSL": 693,
      "nTO": 34,
      "expR": 0.019,
      "pf": 1.04,
      "mfe_p25": 11.0,
      "mfe_p50": 25.0,
      "mfe_p75": 58.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 42.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -20.0,
      "revAfterSL_rate": 41.1,
      "ci90": {
        "expR": 0.019,
        "ci90": [
          -0.031,
          0.069
        ],
        "p_mean_le_0": 0.271,
        "n": 1420
      }
    },
    "cuts": {
      "1.2": {
        "n": 496,
        "wrTP1": 30.2,
        "nSL": 323,
        "nTO": 23,
        "expR": -0.018,
        "pf": 0.97,
        "mfe_p25": 19.0,
        "mfe_p50": 41.0,
        "mfe_p75": 83.75,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 42.099999999999994,
        "loserMFEbeforeSL_p50": 11.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.5,
        "revAfterSL_rate": 30.7,
        "ci90": {
          "expR": -0.018,
          "ci90": [
            -0.135,
            0.093
          ],
          "p_mean_le_0": 0.62,
          "n": 486
        }
      },
      "1.3": {
        "n": 438,
        "wrTP1": 28.1,
        "nSL": 293,
        "nTO": 22,
        "expR": -0.036,
        "pf": 0.95,
        "mfe_p25": 19.0,
        "mfe_p50": 42.0,
        "mfe_p75": 85.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 41.999999999999986,
        "loserMFEbeforeSL_p50": 12.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -20.0,
        "revAfterSL_rate": 29.0,
        "ci90": {
          "expR": -0.036,
          "ci90": [
            -0.155,
            0.089
          ],
          "p_mean_le_0": 0.676,
          "n": 428
        }
      },
      "1.5": {
        "n": 350,
        "wrTP1": 25.4,
        "nSL": 243,
        "nTO": 18,
        "expR": -0.045,
        "pf": 0.94,
        "mfe_p25": 19.0,
        "mfe_p50": 42.0,
        "mfe_p75": 87.5,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 43.0,
        "loserMFEbeforeSL_p50": 12.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -20.0,
        "revAfterSL_rate": 25.5,
        "ci90": {
          "expR": -0.045,
          "ci90": [
            -0.194,
            0.106
          ],
          "p_mean_le_0": 0.697,
          "n": 343
        }
      },
      "2.0": {
        "n": 220,
        "wrTP1": 20.5,
        "nSL": 160,
        "nTO": 15,
        "expR": -0.049,
        "pf": 0.93,
        "mfe_p25": 20.75,
        "mfe_p50": 44.0,
        "mfe_p75": 100.25,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 41.00000000000001,
        "loserMFEbeforeSL_p50": 15.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -20.5,
        "revAfterSL_rate": 18.8,
        "ci90": {
          "expR": -0.049,
          "ci90": [
            -0.239,
            0.173
          ],
          "p_mean_le_0": 0.665,
          "n": 216
        }
      }
    }
  },
  "29/RETEST/LONG": {
    "baseline": {
      "n": 100,
      "wrTP1": 57.0,
      "nSL": 43,
      "nTO": 0,
      "expR": 0.212,
      "pf": 1.49,
      "mfe_p25": 42.0,
      "mfe_p50": 118.5,
      "mfe_p75": 1455.5,
      "winnerMAE_p75": 331.0,
      "winnerMAE_p90": 8496.399999999994,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -71.0,
      "revAfterSL_rate": 62.8,
      "ci90": {
        "expR": 0.212,
        "ci90": [
          0.003,
          0.437
        ],
        "p_mean_le_0": 0.05,
        "n": 100
      }
    },
    "cuts": {
      "1.2": {
        "n": 30,
        "wrTP1": 33.3,
        "nSL": 20,
        "nTO": 0,
        "expR": 0.195,
        "pf": 1.29,
        "mfe_p25": 55.0,
        "mfe_p50": 97.5,
        "mfe_p75": 582.5,
        "winnerMAE_p75": 79.0,
        "winnerMAE_p90": 431.7999999999988,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -38.0,
        "revAfterSL_rate": 70.0,
        "ci90": {
          "expR": 0.195,
          "ci90": [
            -0.344,
            0.809
          ],
          "p_mean_le_0": 0.293,
          "n": 30
        }
      },
      "1.3": {
        "n": 27,
        "wrTP1": 33.3,
        "nSL": 18,
        "nTO": 0,
        "expR": 0.245,
        "pf": 1.37,
        "mfe_p25": 55.0,
        "mfe_p50": 91.0,
        "mfe_p75": 524.0,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 767.6000000000006,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -41.0,
        "revAfterSL_rate": 66.7,
        "ci90": {
          "expR": 0.245,
          "ci90": [
            -0.34,
            0.864
          ],
          "p_mean_le_0": 0.273,
          "n": 27
        }
      },
      "1.5": {
        "n": 23,
        "wrTP1": 30.4,
        "nSL": 16,
        "nTO": 0,
        "expR": 0.255,
        "pf": 1.37,
        "mfe_p25": 55.5,
        "mfe_p50": 142.0,
        "mfe_p75": 1142.5,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 1439.2000000000012,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -42.0,
        "revAfterSL_rate": 62.5,
        "ci90": {
          "expR": 0.255,
          "ci90": [
            -0.403,
            0.964
          ],
          "p_mean_le_0": 0.282,
          "n": 23
        }
      }
    }
  },
  "29/RETEST/SHORT": {
    "baseline": {
      "n": 157,
      "wrTP1": 58.6,
      "nSL": 65,
      "nTO": 0,
      "expR": 0.205,
      "pf": 1.5,
      "mfe_p25": 30.0,
      "mfe_p50": 102.0,
      "mfe_p75": 727.0,
      "winnerMAE_p75": 196.75,
      "winnerMAE_p90": 2354.400000000008,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -198.0,
      "revAfterSL_rate": 70.8,
      "ci90": {
        "expR": 0.205,
        "ci90": [
          0.055,
          0.351
        ],
        "p_mean_le_0": 0.011,
        "n": 157
      }
    },
    "cuts": {
      "1.2": {
        "n": 38,
        "wrTP1": 36.8,
        "nSL": 24,
        "nTO": 0,
        "expR": 0.236,
        "pf": 1.37,
        "mfe_p25": 48.5,
        "mfe_p50": 130.5,
        "mfe_p75": 1148.75,
        "winnerMAE_p75": 375.25,
        "winnerMAE_p90": 2089.200000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -259.5,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.236,
          "ci90": [
            -0.195,
            0.714
          ],
          "p_mean_le_0": 0.191,
          "n": 38
        }
      },
      "1.3": {
        "n": 35,
        "wrTP1": 34.3,
        "nSL": 23,
        "nTO": 0,
        "expR": 0.215,
        "pf": 1.33,
        "mfe_p25": 84.0,
        "mfe_p50": 177.0,
        "mfe_p75": 1223.5,
        "winnerMAE_p75": 592.5,
        "winnerMAE_p90": 2354.4000000000005,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -281.0,
        "revAfterSL_rate": 52.2,
        "ci90": {
          "expR": 0.215,
          "ci90": [
            -0.255,
            0.677
          ],
          "p_mean_le_0": 0.24,
          "n": 35
        }
      },
      "1.5": {
        "n": 27,
        "wrTP1": 37.0,
        "nSL": 17,
        "nTO": 0,
        "expR": 0.354,
        "pf": 1.56,
        "mfe_p25": 84.0,
        "mfe_p50": 113.0,
        "mfe_p75": 672.0,
        "winnerMAE_p75": 267.75,
        "winnerMAE_p90": 478.7999999999997,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -198.0,
        "revAfterSL_rate": 41.2,
        "ci90": {
          "expR": 0.354,
          "ci90": [
            -0.224,
            0.899
          ],
          "p_mean_le_0": 0.164,
          "n": 27
        }
      }
    }
  },
  "3/RETEST/LONG": {
    "baseline": {
      "n": 757,
      "wrTP1": 54.0,
      "nSL": 342,
      "nTO": 6,
      "expR": 0.08,
      "pf": 1.18,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 31.0,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 54.4,
      "ci90": {
        "expR": 0.08,
        "ci90": [
          0.014,
          0.145
        ],
        "p_mean_le_0": 0.018,
        "n": 753
      }
    },
    "cuts": {
      "1.2": {
        "n": 198,
        "wrTP1": 36.4,
        "nSL": 124,
        "nTO": 2,
        "expR": 0.112,
        "pf": 1.18,
        "mfe_p25": 16.25,
        "mfe_p50": 36.0,
        "mfe_p75": 76.0,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 35.09999999999999,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -16.5,
        "revAfterSL_rate": 47.6,
        "ci90": {
          "expR": 0.112,
          "ci90": [
            -0.066,
            0.296
          ],
          "p_mean_le_0": 0.144,
          "n": 198
        }
      },
      "1.3": {
        "n": 171,
        "wrTP1": 36.3,
        "nSL": 107,
        "nTO": 2,
        "expR": 0.141,
        "pf": 1.23,
        "mfe_p25": 21.0,
        "mfe_p50": 37.0,
        "mfe_p75": 76.0,
        "winnerMAE_p75": 13.75,
        "winnerMAE_p90": 39.599999999999994,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 46.7,
        "ci90": {
          "expR": 0.141,
          "ci90": [
            -0.052,
            0.34
          ],
          "p_mean_le_0": 0.116,
          "n": 171
        }
      },
      "1.5": {
        "n": 127,
        "wrTP1": 37.0,
        "nSL": 78,
        "nTO": 2,
        "expR": 0.242,
        "pf": 1.39,
        "mfe_p25": 22.5,
        "mfe_p50": 41.0,
        "mfe_p75": 80.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 43.999999999999986,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 41.0,
        "ci90": {
          "expR": 0.242,
          "ci90": [
            0.008,
            0.477
          ],
          "p_mean_le_0": 0.045,
          "n": 127
        }
      },
      "2.0": {
        "n": 70,
        "wrTP1": 32.9,
        "nSL": 45,
        "nTO": 2,
        "expR": 0.295,
        "pf": 1.46,
        "mfe_p25": 31.0,
        "mfe_p50": 50.0,
        "mfe_p75": 87.25,
        "winnerMAE_p75": 12.5,
        "winnerMAE_p90": 26.400000000000002,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 40.0,
        "ci90": {
          "expR": 0.295,
          "ci90": [
            -0.051,
            0.655
          ],
          "p_mean_le_0": 0.084,
          "n": 70
        }
      }
    }
  },
  "3/RETEST/SHORT": {
    "baseline": {
      "n": 725,
      "wrTP1": 55.3,
      "nSL": 314,
      "nTO": 10,
      "expR": 0.12,
      "pf": 1.27,
      "mfe_p25": 11.0,
      "mfe_p50": 21.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 34.0,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -22.0,
      "revAfterSL_rate": 57.3,
      "ci90": {
        "expR": 0.12,
        "ci90": [
          0.05,
          0.184
        ],
        "p_mean_le_0": 0.002,
        "n": 721
      }
    },
    "cuts": {
      "1.2": {
        "n": 184,
        "wrTP1": 36.4,
        "nSL": 108,
        "nTO": 9,
        "expR": 0.201,
        "pf": 1.33,
        "mfe_p25": 16.0,
        "mfe_p50": 29.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 30.799999999999997,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.201,
          "ci90": [
            0.005,
            0.389
          ],
          "p_mean_le_0": 0.044,
          "n": 181
        }
      },
      "1.3": {
        "n": 159,
        "wrTP1": 35.8,
        "nSL": 93,
        "nTO": 9,
        "expR": 0.238,
        "pf": 1.4,
        "mfe_p25": 16.0,
        "mfe_p50": 29.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 30.199999999999996,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 46.2,
        "ci90": {
          "expR": 0.238,
          "ci90": [
            0.031,
            0.449
          ],
          "p_mean_le_0": 0.027,
          "n": 156
        }
      },
      "1.5": {
        "n": 132,
        "wrTP1": 31.1,
        "nSL": 83,
        "nTO": 8,
        "expR": 0.171,
        "pf": 1.27,
        "mfe_p25": 16.25,
        "mfe_p50": 29.5,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 41.0,
        "ci90": {
          "expR": 0.171,
          "ci90": [
            -0.071,
            0.412
          ],
          "p_mean_le_0": 0.122,
          "n": 130
        }
      },
      "2.0": {
        "n": 67,
        "wrTP1": 31.3,
        "nSL": 41,
        "nTO": 5,
        "expR": 0.382,
        "pf": 1.61,
        "mfe_p25": 19.25,
        "mfe_p50": 33.0,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 22.0,
        "ci90": {
          "expR": 0.382,
          "ci90": [
            0.022,
            0.772
          ],
          "p_mean_le_0": 0.042,
          "n": 66
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 898,
      "wrTP1": 51.3,
      "nSL": 412,
      "nTO": 25,
      "expR": 0.024,
      "pf": 1.05,
      "mfe_p25": 18.0,
      "mfe_p50": 44.0,
      "mfe_p75": 381.5,
      "winnerMAE_p75": 80.0,
      "winnerMAE_p90": 1601.0,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -53.0,
      "revAfterSL_rate": 45.6,
      "ci90": {
        "expR": 0.024,
        "ci90": [
          -0.036,
          0.086
        ],
        "p_mean_le_0": 0.245,
        "n": 879
      }
    },
    "cuts": {
      "1.2": {
        "n": 286,
        "wrTP1": 29.0,
        "nSL": 187,
        "nTO": 16,
        "expR": -0.09,
        "pf": 0.87,
        "mfe_p25": 23.0,
        "mfe_p50": 53.0,
        "mfe_p75": 483.0,
        "winnerMAE_p75": 57.5,
        "winnerMAE_p90": 691.1999999999998,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -37.0,
        "revAfterSL_rate": 36.4,
        "ci90": {
          "expR": -0.09,
          "ci90": [
            -0.235,
            0.059
          ],
          "p_mean_le_0": 0.849,
          "n": 275
        }
      },
      "1.3": {
        "n": 256,
        "wrTP1": 25.4,
        "nSL": 175,
        "nTO": 16,
        "expR": -0.146,
        "pf": 0.8,
        "mfe_p25": 24.0,
        "mfe_p50": 54.0,
        "mfe_p75": 413.0,
        "winnerMAE_p75": 46.0,
        "winnerMAE_p90": 351.40000000000015,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -37.0,
        "revAfterSL_rate": 36.0,
        "ci90": {
          "expR": -0.146,
          "ci90": [
            -0.295,
            0.008
          ],
          "p_mean_le_0": 0.942,
          "n": 245
        }
      },
      "1.5": {
        "n": 200,
        "wrTP1": 24.5,
        "nSL": 139,
        "nTO": 12,
        "expR": -0.124,
        "pf": 0.83,
        "mfe_p25": 23.0,
        "mfe_p50": 57.0,
        "mfe_p75": 460.0,
        "winnerMAE_p75": 39.0,
        "winnerMAE_p90": 474.00000000000125,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -36.0,
        "revAfterSL_rate": 34.5,
        "ci90": {
          "expR": -0.124,
          "ci90": [
            -0.305,
            0.056
          ],
          "p_mean_le_0": 0.877,
          "n": 193
        }
      },
      "2.0": {
        "n": 115,
        "wrTP1": 17.4,
        "nSL": 88,
        "nTO": 7,
        "expR": -0.251,
        "pf": 0.68,
        "mfe_p25": 29.75,
        "mfe_p50": 59.0,
        "mfe_p75": 1102.25,
        "winnerMAE_p75": 139.75,
        "winnerMAE_p90": 1595.6000000000006,
        "loserMFEbeforeSL_p50": 14.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.5,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 22.7,
        "ci90": {
          "expR": -0.251,
          "ci90": [
            -0.48,
            -0.021
          ],
          "p_mean_le_0": 0.96,
          "n": 112
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 779,
      "wrTP1": 54.3,
      "nSL": 337,
      "nTO": 19,
      "expR": 0.089,
      "pf": 1.2,
      "mfe_p25": 19.0,
      "mfe_p50": 51.0,
      "mfe_p75": 300.0,
      "winnerMAE_p75": 51.0,
      "winnerMAE_p90": 542.0,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -68.0,
      "revAfterSL_rate": 56.1,
      "ci90": {
        "expR": 0.089,
        "ci90": [
          0.023,
          0.158
        ],
        "p_mean_le_0": 0.015,
        "n": 761
      }
    },
    "cuts": {
      "1.2": {
        "n": 252,
        "wrTP1": 28.6,
        "nSL": 168,
        "nTO": 12,
        "expR": -0.047,
        "pf": 0.93,
        "mfe_p25": 27.0,
        "mfe_p50": 63.0,
        "mfe_p75": 319.0,
        "winnerMAE_p75": 45.25,
        "winnerMAE_p90": 1501.2999999999995,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -57.0,
        "revAfterSL_rate": 46.4,
        "ci90": {
          "expR": -0.047,
          "ci90": [
            -0.202,
            0.116
          ],
          "p_mean_le_0": 0.677,
          "n": 241
        }
      },
      "1.3": {
        "n": 228,
        "wrTP1": 25.9,
        "nSL": 158,
        "nTO": 11,
        "expR": -0.107,
        "pf": 0.85,
        "mfe_p25": 26.25,
        "mfe_p50": 63.0,
        "mfe_p75": 371.0,
        "winnerMAE_p75": 53.0,
        "winnerMAE_p90": 1635.2000000000016,
        "loserMFEbeforeSL_p50": 8.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -57.0,
        "revAfterSL_rate": 46.2,
        "ci90": {
          "expR": -0.107,
          "ci90": [
            -0.272,
            0.067
          ],
          "p_mean_le_0": 0.851,
          "n": 218
        }
      },
      "1.5": {
        "n": 190,
        "wrTP1": 25.8,
        "nSL": 132,
        "nTO": 9,
        "expR": -0.076,
        "pf": 0.89,
        "mfe_p25": 26.0,
        "mfe_p50": 62.5,
        "mfe_p75": 285.5,
        "winnerMAE_p75": 44.0,
        "winnerMAE_p90": 2152.2000000000016,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -54.0,
        "revAfterSL_rate": 41.7,
        "ci90": {
          "expR": -0.076,
          "ci90": [
            -0.248,
            0.119
          ],
          "p_mean_le_0": 0.741,
          "n": 182
        }
      },
      "2.0": {
        "n": 127,
        "wrTP1": 19.7,
        "nSL": 95,
        "nTO": 7,
        "expR": -0.18,
        "pf": 0.77,
        "mfe_p25": 29.0,
        "mfe_p50": 62.0,
        "mfe_p75": 215.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 741.8000000000017,
        "loserMFEbeforeSL_p50": 18.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -53.0,
        "revAfterSL_rate": 33.7,
        "ci90": {
          "expR": -0.18,
          "ci90": [
            -0.419,
            0.059
          ],
          "p_mean_le_0": 0.895,
          "n": 121
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
    "n": 10081,
    "wrTP1": 49.3,
    "expR": 0.027
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
    "15m/INV/LONG": {
      "n": 4,
      "wrTP1": 50.0,
      "expR": -0.115,
      "pf": 0.77
    },
    "15m/INV/SHORT": {
      "n": 1,
      "wrTP1": 100.0,
      "expR": 1.35,
      "pf": 99.0
    },
    "15m/RETEST/LONG": {
      "n": 253,
      "wrTP1": 48.6,
      "expR": -0.026,
      "pf": 0.95
    },
    "15m/RETEST/SHORT": {
      "n": 263,
      "wrTP1": 53.2,
      "expR": 0.073,
      "pf": 1.16
    },
    "1m/INV/LONG": {
      "n": 53,
      "wrTP1": 50.9,
      "expR": 0.073,
      "pf": 1.17
    },
    "1m/INV/SHORT": {
      "n": 51,
      "wrTP1": 43.1,
      "expR": 0.084,
      "pf": 1.2
    },
    "1m/RETEST/LONG": {
      "n": 2330,
      "wrTP1": 46.9,
      "expR": 0.003,
      "pf": 1.01
    },
    "1m/RETEST/SHORT": {
      "n": 2122,
      "wrTP1": 47.5,
      "expR": 0.027,
      "pf": 1.06
    },
    "29m/RETEST/LONG": {
      "n": 106,
      "wrTP1": 53.8,
      "expR": 0.143,
      "pf": 1.31
    },
    "29m/RETEST/SHORT": {
      "n": 161,
      "wrTP1": 57.1,
      "expR": 0.175,
      "pf": 1.41
    },
    "2m/INV/LONG": {
      "n": 16,
      "wrTP1": 75.0,
      "expR": 0.192,
      "pf": 1.77
    },
    "2m/INV/SHORT": {
      "n": 19,
      "wrTP1": 68.4,
      "expR": 0.169,
      "pf": 1.6
    },
    "2m/RETEST/LONG": {
      "n": 990,
      "wrTP1": 48.0,
      "expR": -0.071,
      "pf": 0.86
    },
    "2m/RETEST/SHORT": {
      "n": 945,
      "wrTP1": 46.0,
      "expR": -0.018,
      "pf": 0.96
    },
    "3m/INV/LONG": {
      "n": 8,
      "wrTP1": 62.5,
      "expR": 0.02,
      "pf": 1.05
    },
    "3m/INV/SHORT": {
      "n": 5,
      "wrTP1": 100.0,
      "expR": 0.48,
      "pf": 99.0
    },
    "3m/RETEST/LONG": {
      "n": 768,
      "wrTP1": 53.3,
      "expR": 0.073,
      "pf": 1.16
    },
    "3m/RETEST/SHORT": {
      "n": 742,
      "wrTP1": 54.0,
      "expR": 0.109,
      "pf": 1.25
    },
    "5m/INV/LONG": {
      "n": 12,
      "wrTP1": 58.3,
      "expR": -0.188,
      "pf": 0.55
    },
    "5m/INV/SHORT": {
      "n": 9,
      "wrTP1": 22.2,
      "expR": 0.413,
      "pf": 1.74
    },
    "5m/RETEST/LONG": {
      "n": 637,
      "wrTP1": 51.3,
      "expR": 0.038,
      "pf": 1.08
    },
    "5m/RETEST/SHORT": {
      "n": 586,
      "wrTP1": 53.9,
      "expR": 0.099,
      "pf": 1.22
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 46141,
  "brier": 0.2214,
  "bias": -0.101,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.299
    },
    {
      "feature": "stretchAtr",
      "weight": -0.055
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.045
    },
    {
      "feature": "nearTk",
      "weight": -0.043
    },
    {
      "feature": "hourNY",
      "weight": 0.031
    },
    {
      "feature": "biasScore",
      "weight": -0.029
    },
    {
      "feature": "emaStack",
      "weight": 0.019
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.019
    },
    {
      "feature": "rvol",
      "weight": 0.017
    },
    {
      "feature": "chopIdx",
      "weight": -0.015
    },
    {
      "feature": "aligned",
      "weight": -0.007
    },
    {
      "feature": "structDir",
      "weight": -0.005
    },
    {
      "feature": "nearEdge",
      "weight": 0.003
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.168,
      "actual": 0.167,
      "n": 4614
    },
    {
      "bin": 1,
      "pred": 0.372,
      "actual": 0.309,
      "n": 4614
    },
    {
      "bin": 2,
      "pred": 0.449,
      "actual": 0.318,
      "n": 4614
    },
    {
      "bin": 3,
      "pred": 0.494,
      "actual": 0.426,
      "n": 4614
    },
    {
      "bin": 4,
      "pred": 0.53,
      "actual": 0.507,
      "n": 4614
    },
    {
      "bin": 5,
      "pred": 0.558,
      "actual": 0.563,
      "n": 4614
    },
    {
      "bin": 6,
      "pred": 0.58,
      "actual": 0.619,
      "n": 4614
    },
    {
      "bin": 7,
      "pred": 0.599,
      "actual": 0.644,
      "n": 4614
    },
    {
      "bin": 8,
      "pred": 0.617,
      "actual": 0.691,
      "n": 4614
    },
    {
      "bin": 9,
      "pred": 0.644,
      "actual": 0.748,
      "n": 4615
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
  "testN": 14792,
  "testWeeks": [
    "2026-W43",
    "2026-W44"
  ],
  "model_oos_brier": 0.2371,
  "model_oos_n": 14792,
  "best_scheme_in_sample": {
    "scheme": "fixed_2R",
    "trainExpR": 0.049
  },
  "best_scheme_oos_expR": 0.039
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "15m/RETEST/LONG": {
    "expR": -0.026,
    "ci90": [
      -0.138,
      0.094
    ],
    "p_mean_le_0": 0.653,
    "n": 253,
    "survives_fdr10": false
  },
  "15m/RETEST/SHORT": {
    "expR": 0.073,
    "ci90": [
      -0.044,
      0.196
    ],
    "p_mean_le_0": 0.16,
    "n": 263,
    "survives_fdr10": false
  },
  "1m/INV/LONG": {
    "expR": 0.116,
    "ci90": [
      0.02,
      0.221
    ],
    "p_mean_le_0": 0.024,
    "n": 437,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": 0.084,
    "ci90": [
      -0.024,
      0.185
    ],
    "p_mean_le_0": 0.098,
    "n": 310,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.026,
    "ci90": [
      0.01,
      0.041
    ],
    "p_mean_le_0": 0.004,
    "n": 16627,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.03,
    "ci90": [
      0.011,
      0.048
    ],
    "p_mean_le_0": 0.006,
    "n": 10855,
    "survives_fdr10": true
  },
  "29m/RETEST/LONG": {
    "expR": 0.143,
    "ci90": [
      -0.051,
      0.354
    ],
    "p_mean_le_0": 0.107,
    "n": 106,
    "survives_fdr10": false
  },
  "29m/RETEST/SHORT": {
    "expR": 0.175,
    "ci90": [
      0.03,
      0.316
    ],
    "p_mean_le_0": 0.024,
    "n": 161,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.043,
    "ci90": [
      -0.1,
      0.194
    ],
    "p_mean_le_0": 0.335,
    "n": 157,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.124,
    "ci90": [
      -0.065,
      0.329
    ],
    "p_mean_le_0": 0.143,
    "n": 116,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.03,
    "ci90": [
      0.006,
      0.053
    ],
    "p_mean_le_0": 0.017,
    "n": 7268,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.043,
    "ci90": [
      0.015,
      0.075
    ],
    "p_mean_le_0": 0.006,
    "n": 4763,
    "survives_fdr10": true
  },
  "3m/INV/LONG": {
    "expR": 0.02,
    "ci90": [
      -0.444,
      0.46
    ],
    "p_mean_le_0": 0.462,
    "n": 8,
    "survives_fdr10": false
  },
  "3m/RETEST/LONG": {
    "expR": 0.073,
    "ci90": [
      0.008,
      0.141
    ],
    "p_mean_le_0": 0.034,
    "n": 764,
    "survives_fdr10": true
  },
  "3m/RETEST/SHORT": {
    "expR": 0.109,
    "ci90": [
      0.04,
      0.177
    ],
    "p_mean_le_0": 0.004,
    "n": 738,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.132,
    "ci90": [
      -0.064,
      0.323
    ],
    "p_mean_le_0": 0.136,
    "n": 48,
    "survives_fdr10": false
  },
  "5m/INV/SHORT": {
    "expR": 0.201,
    "ci90": [
      -0.204,
      0.59
    ],
    "p_mean_le_0": 0.205,
    "n": 30,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.09,
    "ci90": [
      0.056,
      0.128
    ],
    "p_mean_le_0": 0.0,
    "n": 2858,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.074,
    "ci90": [
      0.028,
      0.121
    ],
    "p_mean_le_0": 0.005,
    "n": 1993,
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
      "id": 3,
      "n": 2735,
      "wrTP1": 52.8,
      "expR": 0.057,
      "pf": 1.12,
      "defining_features": {
        "aligned": -4.06,
        "entryZoneTk": -0.76,
        "nearTk": 0.66,
        "rr1": -0.19
      }
    },
    {
      "id": 2,
      "n": 23000,
      "wrTP1": 46.9,
      "expR": 0.04,
      "pf": 1.08,
      "defining_features": {
        "biasScore": 0.76,
        "emaStack": 0.69,
        "nearEdge": 0.54,
        "stretchAtr": -0.33
      }
    },
    {
      "id": 0,
      "n": 6654,
      "wrTP1": 45.0,
      "expR": 0.039,
      "pf": 1.08,
      "defining_features": {
        "stretchAtr": 1.64,
        "chopIdx": -1.28,
        "rvol": 1.26,
        "aligned": 0.24
      }
    },
    {
      "id": 1,
      "n": 17005,
      "wrTP1": 46.0,
      "expR": 0.036,
      "pf": 1.07,
      "defining_features": {
        "biasScore": -1.11,
        "emaStack": -0.97,
        "nearEdge": -0.81,
        "structDir": -0.42
      }
    }
  ]
}
```

## Consistencia entre instrumentos
```json
{
  "15m/RETEST/LONG": {
    "symbols": {
      "ES": {
        "n": 39,
        "wrTP1": 51.3,
        "expR": 0.066
      },
      "NQ": {
        "n": 28,
        "wrTP1": 53.6,
        "expR": 0.077
      },
      "GC": {
        "n": 24,
        "wrTP1": 58.3,
        "expR": 0.292
      },
      "CL": {
        "n": 37,
        "wrTP1": 51.4,
        "expR": 0.002
      },
      "YM": {
        "n": 45,
        "wrTP1": 57.8,
        "expR": 0.185
      },
      "ETHUSDT": {
        "n": 40,
        "wrTP1": 52.5,
        "expR": -0.147
      },
      "BTCUSDT": {
        "n": 40,
        "wrTP1": 20.0,
        "expR": -0.523
      }
    },
    "expR_spread": 0.815,
    "verdict": "instrument-specific"
  },
  "15m/RETEST/SHORT": {
    "symbols": {
      "BTCUSDT": {
        "n": 58,
        "wrTP1": 62.1,
        "expR": 0.296
      },
      "ETHUSDT": {
        "n": 47,
        "wrTP1": 44.7,
        "expR": -0.211
      },
      "YM": {
        "n": 22,
        "wrTP1": 63.6,
        "expR": 0.29
      },
      "ES": {
        "n": 28,
        "wrTP1": 50.0,
        "expR": -0.072
      },
      "GC": {
        "n": 28,
        "wrTP1": 60.7,
        "expR": 0.212
      },
      "NQ": {
        "n": 35,
        "wrTP1": 48.6,
        "expR": 0.059
      },
      "CL": {
        "n": 45,
        "wrTP1": 46.7,
        "expR": -0.008
      }
    },
    "expR_spread": 0.507,
    "verdict": "instrument-specific"
  },
  "1m/INV/LONG": {
    "symbols": {
      "CL": {
        "n": 90,
        "wrTP1": 46.7,
        "expR": 0.228
      },
      "GC": {
        "n": 67,
        "wrTP1": 46.3,
        "expR": -0.031
      },
      "YM": {
        "n": 195,
        "wrTP1": 45.6,
        "expR": 0.152
      },
      "ES": {
        "n": 59,
        "wrTP1": 39.0,
        "expR": -0.132
      },
      "NQ": {
        "n": 41,
        "wrTP1": 61.0,
        "expR": 0.285
      }
    },
    "expR_spread": 0.417,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "GC": {
        "n": 74,
        "wrTP1": 56.8,
        "expR": 0.17
      },
      "YM": {
        "n": 159,
        "wrTP1": 41.5,
        "expR": 0.08
      },
      "NQ": {
        "n": 38,
        "wrTP1": 60.5,
        "expR": 0.125
      },
      "ES": {
        "n": 21,
        "wrTP1": 47.6,
        "expR": 0.269
      },
      "CL": {
        "n": 37,
        "wrTP1": 32.4,
        "expR": -0.271
      }
    },
    "expR_spread": 0.54,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 2677,
        "wrTP1": 44.3,
        "expR": 0.007
      },
      "NQ": {
        "n": 3016,
        "wrTP1": 45.0,
        "expR": 0.005
      },
      "ES": {
        "n": 3842,
        "wrTP1": 45.0,
        "expR": 0.001
      },
      "CL": {
        "n": 3647,
        "wrTP1": 45.0,
        "expR": 0.031
      },
      "YM": {
        "n": 3915,
        "wrTP1": 45.7,
        "expR": 0.074
      }
    },
    "expR_spread": 0.073,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 1715,
        "wrTP1": 41.9,
        "expR": 0.041
      },
      "GC": {
        "n": 3323,
        "wrTP1": 46.6,
        "expR": 0.052
      },
      "YM": {
        "n": 2644,
        "wrTP1": 45.0,
        "expR": 0.039
      },
      "ES": {
        "n": 2067,
        "wrTP1": 45.9,
        "expR": 0.024
      },
      "CL": {
        "n": 1601,
        "wrTP1": 44.0,
        "expR": -0.035
      }
    },
    "expR_spread": 0.087,
    "verdict": "universal"
  },
  "29m/RETEST/LONG": {
    "symbols": {
      "YM": {
        "n": 18,
        "wrTP1": 55.6,
        "expR": 0.406
      },
      "NQ": {
        "n": 9,
        "wrTP1": 55.6,
        "expR": 0.316
      },
      "ES": {
        "n": 7,
        "wrTP1": 28.6,
        "expR": -0.616
      },
      "CL": {
        "n": 27,
        "wrTP1": 55.6,
        "expR": 0.268
      },
      "BTCUSDT": {
        "n": 26,
        "wrTP1": 42.3,
        "expR": -0.243
      },
      "GC": {
        "n": 6,
        "wrTP1": 100.0,
        "expR": 0.997
      },
      "ETHUSDT": {
        "n": 13,
        "wrTP1": 61.5,
        "expR": 0.191
      }
    },
    "expR_spread": 1.613,
    "verdict": "instrument-specific"
  },
  "29m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 28,
        "wrTP1": 50.0,
        "expR": 0.079
      },
      "CL": {
        "n": 25,
        "wrTP1": 52.0,
        "expR": 0.02
      },
      "YM": {
        "n": 18,
        "wrTP1": 66.7,
        "expR": 0.346
      },
      "NQ": {
        "n": 26,
        "wrTP1": 69.2,
        "expR": 0.525
      },
      "ETHUSDT": {
        "n": 32,
        "wrTP1": 56.2,
        "expR": 0.099
      },
      "GC": {
        "n": 8,
        "wrTP1": 37.5,
        "expR": -0.391
      },
      "BTCUSDT": {
        "n": 24,
        "wrTP1": 58.3,
        "expR": 0.235
      }
    },
    "expR_spread": 0.916,
    "verdict": "instrument-specific"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 22,
        "wrTP1": 45.5,
        "expR": -0.278
      },
      "CL": {
        "n": 21,
        "wrTP1": 61.9,
        "expR": 0.118
      },
      "YM": {
        "n": 60,
        "wrTP1": 40.0,
        "expR": -0.073
      },
      "ES": {
        "n": 28,
        "wrTP1": 67.9,
        "expR": 0.019
      },
      "NQ": {
        "n": 31,
        "wrTP1": 64.5,
        "expR": 0.486
      }
    },
    "expR_spread": 0.764,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 54,
        "wrTP1": 55.6,
        "expR": 0.386
      },
      "NQ": {
        "n": 19,
        "wrTP1": 47.4,
        "expR": 0.019
      },
      "ES": {
        "n": 14,
        "wrTP1": 35.7,
        "expR": 0.051
      },
      "CL": {
        "n": 14,
        "wrTP1": 50.0,
        "expR": -0.132
      },
      "GC": {
        "n": 19,
        "wrTP1": 42.1,
        "expR": -0.261
      }
    },
    "expR_spread": 0.647,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 1467,
        "wrTP1": 46.6,
        "expR": 0.036
      },
      "GC": {
        "n": 1132,
        "wrTP1": 46.0,
        "expR": 0.009
      },
      "CL": {
        "n": 1606,
        "wrTP1": 48.7,
        "expR": 0.044
      },
      "ES": {
        "n": 1651,
        "wrTP1": 46.9,
        "expR": -0.017
      },
      "YM": {
        "n": 1620,
        "wrTP1": 48.5,
        "expR": 0.072
      }
    },
    "expR_spread": 0.089,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 917,
        "wrTP1": 47.5,
        "expR": 0.005
      },
      "YM": {
        "n": 1097,
        "wrTP1": 48.1,
        "expR": 0.081
      },
      "GC": {
        "n": 1369,
        "wrTP1": 49.1,
        "expR": 0.092
      },
      "NQ": {
        "n": 862,
        "wrTP1": 44.0,
        "expR": 0.017
      },
      "CL": {
        "n": 686,
        "wrTP1": 46.8,
        "expR": -0.025
      }
    },
    "expR_spread": 0.117,
    "verdict": "universal"
  },
  "3m/RETEST/LONG": {
    "symbols": {
      "YM": {
        "n": 192,
        "wrTP1": 54.7,
        "expR": 0.038
      },
      "ES": {
        "n": 180,
        "wrTP1": 51.1,
        "expR": -0.025
      },
      "NQ": {
        "n": 142,
        "wrTP1": 48.6,
        "expR": -0.029
      },
      "CL": {
        "n": 146,
        "wrTP1": 60.3,
        "expR": 0.294
      },
      "GC": {
        "n": 108,
        "wrTP1": 50.9,
        "expR": 0.133
      }
    },
    "expR_spread": 0.323,
    "verdict": "universal"
  },
  "3m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 146,
        "wrTP1": 53.4,
        "expR": 0.057
      },
      "ES": {
        "n": 127,
        "wrTP1": 48.0,
        "expR": -0.09
      },
      "GC": {
        "n": 142,
        "wrTP1": 56.3,
        "expR": 0.237
      },
      "CL": {
        "n": 180,
        "wrTP1": 56.1,
        "expR": 0.123
      },
      "YM": {
        "n": 147,
        "wrTP1": 55.1,
        "expR": 0.193
      }
    },
    "expR_spread": 0.327,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 12,
        "wrTP1": 58.3,
        "expR": 0.034
      },
      "YM": {
        "n": 13,
        "wrTP1": 76.9,
        "expR": 0.152
      },
      "ES": {
        "n": 12,
        "wrTP1": 66.7,
        "expR": 0.008
      },
      "CL": {
        "n": 8,
        "wrTP1": 62.5,
        "expR": 0.492
      },
      "GC": {
        "n": 4,
        "wrTP1": 75.0,
        "expR": 0.188
      }
    },
    "expR_spread": 0.484,
    "verdict": "instrument-specific"
  },
  "5m/INV/SHORT": {
    "symbols": {
      "NQ": {
        "n": 9,
        "wrTP1": 55.6,
        "expR": 0.56
      },
      "YM": {
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.757
      },
      "ES": {
        "n": 5,
        "wrTP1": 40.0,
        "expR": 0.744
      },
      "GC": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": 0.318
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.245
      }
    },
    "expR_spread": 1.501,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 375,
        "wrTP1": 52.0,
        "expR": 0.124
      },
      "ES": {
        "n": 551,
        "wrTP1": 50.1,
        "expR": 0.059
      },
      "YM": {
        "n": 584,
        "wrTP1": 51.0,
        "expR": 0.115
      },
      "CL": {
        "n": 574,
        "wrTP1": 54.9,
        "expR": 0.172
      },
      "NQ": {
        "n": 591,
        "wrTP1": 48.1,
        "expR": 0.03
      },
      "BTCUSDT": {
        "n": 165,
        "wrTP1": 47.3,
        "expR": -0.035
      },
      "ETHUSDT": {
        "n": 137,
        "wrTP1": 54.7,
        "expR": 0.089
      }
    },
    "expR_spread": 0.207,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 297,
        "wrTP1": 47.5,
        "expR": 0.047
      },
      "ES": {
        "n": 381,
        "wrTP1": 49.9,
        "expR": 0.156
      },
      "GC": {
        "n": 510,
        "wrTP1": 48.2,
        "expR": 0.032
      },
      "YM": {
        "n": 409,
        "wrTP1": 49.1,
        "expR": 0.119
      },
      "CL": {
        "n": 301,
        "wrTP1": 46.5,
        "expR": 0.028
      },
      "ETHUSDT": {
        "n": 92,
        "wrTP1": 62.0,
        "expR": 0.158
      },
      "BTCUSDT": {
        "n": 116,
        "wrTP1": 49.1,
        "expR": -0.042
      }
    },
    "expR_spread": 0.2,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 25,
  "near_news_30m": {
    "n": 1149,
    "wrTP1": 49.3,
    "nSL": 556,
    "nTO": 26,
    "expR": 0.04,
    "pf": 1.08,
    "mfe_p25": 12.0,
    "mfe_p50": 30.0,
    "mfe_p75": 69.0,
    "winnerMAE_p75": 24.0,
    "winnerMAE_p90": 86.0,
    "loserMFEbeforeSL_p50": 3.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 2.0,
    "entryZoneTk_p50": -19.0,
    "revAfterSL_rate": 45.7
  },
  "away_from_news": {
    "n": 48245,
    "wrTP1": 46.6,
    "nSL": 22550,
    "nTO": 3227,
    "expR": 0.039,
    "pf": 1.08,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 43.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 28.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 33.9
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 6,
  "mae_deltaER": 0.267,
  "hit_direction_rate": 16.7
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
      "2026-10-26 (lunes): since_change (recvDate>=2026-09-26, n=18175, sube de 18022 el domingo) cumple hoy ~1 MES desde el changeDate (2026-09-26->2026-10-26) con los 6 de 6 segmentos RETEST todavia confirmando limpio, sin una sola reversion en todo el mes: 1m/RETEST/LONG (n=6560, delta=+0.114 CI90=[0.066,0.163]), 1m/RETEST/SHORT (n=4193, delta=+0.079 CI90=[0.03,0.133]), 2m/RETEST/LONG (n=3085, delta=+0.124 CI90=[0.067,0.185]), 2m/RETEST/SHORT (n=1879, delta=+0.107 CI90=[0.034,0.18]), 5m/RETEST/LONG (n=1189, delta=+0.204 CI90=[0.099,0.324]), 5m/RETEST/SHORT (n=772, delta=+0.146 CI90=[0.039,0.266]). Hallazgo nuevo de hoy: se reviso por primera vez a este nivel de detalle el since_change del lado INV (fuera del scope del experimento, kind=RETEST unicamente) y el efecto NO generaliza -- signo CONTRARIO en SHORT (1m/INV/SHORT n=129 delta=-0.305 CI90=[-0.538,-0.08], estructuralmente peor) e inconcluyente en LONG (1m/INV/LONG n=219 delta=+0.349 CI90=[0.073,0.655], positivo pero n demasiado chico y fuera de scope para actuar). Esto refuerza que el segment de este experimento debe seguir siendo {'kind':'RETEST'} unicamente -- no extender a INV sin evidencia propia y mayor muestra (ver buy-ifvg.md / sell-ifvg.md). Modo sombra: la alerta permanente anadida ayer a analyze.py dispara hoy por primera vez (3 semanas CERRADAS seguidas sin batir al indicador crudo: W41/W42/W43) -- no afecta a este experimento directamente (es un gate distinto, peldano 0->1 de la escalera), pero queda anotado como contexto: el cambio de metrica de shadow_rules (rMultiple-> rOrig) sigue 'listo para implementar', pendiente de ejecutarse. No se decide nada nuevo hoy sobre el verdict agregado (sigue 'flat' por la limitacion de metrica ya conocida).",
      "2026-10-27 (martes): since_change (recvDate>=2026-09-26, n=18697, sube de 18175 ayer) pasa su PRIMER MES COMPLETO desde el changeDate (2026-09-26->2026-10-27) con los 6 de 6 segmentos RETEST todavia confirmando limpio, sin una sola reversion en 31 dias: 1m/RETEST/LONG (n=6688, delta=+0.11 CI90=[0.063,0.158]); 2m/RETEST/LONG (n=3147, delta=+0.124 CI90=[0.066,0.182]); 5m/RETEST/LONG (n=1219, delta=+0.248 CI90=[0.128,0.391], el mas fuerte, sube de 0.204 ayer); 1m/RETEST/SHORT (n=4350, delta=+0.075 CI90=[0.024,0.125]); 2m/RETEST/SHORT (n=1977, delta=+0.107 CI90=[0.035,0.176]); 5m/RETEST/SHORT (n=804, delta=+0.14 CI90=[0.043,0.251]). Sin cambio de confianza documentada (sigue en \"aplicado, 6/6 certifican de forma sostenida\").",
      "2026-10-29 (jueves): CORRECCION DE METODO, no reversion de senal. analyze.py tenia un piso demasiado bajo en invalid_geometry (excluia solo slOrigTk<=0); con slOrigTk=1 (SL estructural a 1 tick de la entrada, denominador casi cero) rOrig explotaba a valores absurdos (hasta 3403R en BTCUSDT, tambien visto en NQ/GC/YM, no es exclusivo de un simbolo). Eso inflaba by_basis y since_change: antes de hoy by_basis.retestBar reportaba delta=0.397 (n=30186) y since_change decia 6/6 segmentos RETEST certificando limpio un mes completo sin reversion. Se subio el piso a slOrigTk<=1 (excluye ~2723 filas degeneradas de retestBar y ~716 de retestBar2) y se recalculo: by_basis.retestBar delta bajo a 0.087 CI90=[0.068,0.105] (n=27463, sigue sin cruzar cero, la direccion del edge es real, la magnitud previa era ficticia) y retestBar2 a delta=0.033 CI90=[0.004,0.061] (n=8046, al filo). since_change con el piso corregido: de los 6 segmentos RETEST, SOLO 3 certifican limpio hoy (2m/RETEST/LONG delta=0.061 CI90=[0.018,0.103] n=3515; 5m/RETEST/LONG delta=0.138 CI90=[0.065,0.233] n=1547; 5m/RETEST/SHORT delta=0.077 CI90=[0.002,0.168] n=1070); 1m/RETEST/LONG (delta=0.032 CI90=[0.0,0.065] n=7130), 1m/RETEST/SHORT (delta=0.031 CI90=[-0.005,0.065] n=4909) y 2m/RETEST/SHORT (delta=0.054 CI90=[0.0,0.111] n=2266) ya NO certifican (CI90 toca o cruza cero). La narrativa previa de \"6/6 certifican, un mes sin reversion\" era optimismo inflado por la geometria degenerada, no evidencia real de ese alcance. No se revierte el cambio aplicado en TradingView (la direccion sigue siendo real donde certifica, y no hay evidencia de que haga dano en 1m/2m SHORT, solo que no esta confirmado ahi). Se baja la confianza documentada de \"aplicado, 6/6 certifican de forma sostenida\" a \"aplicado, 3/6 certifican tras corregir geometria degenerada (2m LONG, 5m LONG, 5m SHORT); 1m LONG, 1m SHORT y 2m SHORT sin confirmar, vigilar si recuperan CI90>0 con mas muestra o si se mantienen al filo\". Vigilar en corridas futuras si 1m/2m SHORT recuperan certificacion con mas dato limpio."
    ],
    "appliedNote": "2026-09-26: aplicado en scalp_command.pine (input sc_sl_retest_basis, default 'Auto (como se midio)'): en RETEST el SL real pasa a la mecha de la vela del retest; 1m SHORT suma la vela previa (retestBar2), igual que la medicion paralela. Base: los 6 segmentos RETEST certifican con CI90 > 0 (n=11273, E[R] 0.238 vs 0.065). El tier se sigue calculando con el stop de 3 capas. El feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig, asi que sl_origin_vs_layer sigue siendo la vigilancia. Rige en cada grafico desde que Jesus re-pega scalp_cc_FULL_for_tradingview.pine. Revertir = poner la base en '3 capas'.",
    "beforeN": 18341,
    "afterN": 29889,
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
      "n": 29889,
      "wrTP1": 47.1,
      "nSL": 14206,
      "nTO": 1610,
      "expR": 0.029,
      "pf": 1.06,
      "mfe_p25": 9.0,
      "mfe_p50": 20.0,
      "mfe_p75": 45.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 33.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 35.4
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
  },
  {
    "id": "aligned-shift-detected-2026-10-26",
    "status": "detected_unconfirmed",
    "hypothesis": "No es un experimento propuesto por el agente, es un cambio detectado en el DATO que agent-instructions.md pide registrar como posible cambio de input de Jesus: el campo aligned (que define la causa de SL contra-sesgo) paso de ser casi siempre 1 (aligned=0 en ~0.0-0.1% de las perdidas, W36-W43) a aligned=0 en 20-46% de las senales desde 2026-10-26, visible en TODOS los simbolos (YM 20.9%, GC 23.5%, NQ 29.4%, ES 30.3%, CL 32.1% desde esa fecha), no solo en los simbolos nuevos BTCUSDT/ETHUSDT (42-46%, mas alto pero no categoricamente distinto). El campo ver se mantiene en v4 todo el tiempo, por lo que si hubo un cambio de input no quedo registrado ahi. Contraintuitivo: aligned=0 NO rinde peor -- by_aligned de hoy da aligned=0 E[R]=0.084 PF=1.19 WR=54.3% (n=2471) vs aligned=1 E[R]=0.039 PF=1.08 WR=46.2% (n=45549), es decir el grupo contra-sesgo rinde MEJOR. El salto de causas_pct contra-sesgo a 27% en sl_post_mortem_weekly_trend (W44) es un efecto de que crecio mucho de muestra, no evidencia de que el bias filter se haya roto o deba endurecerse.",
    "param": "desconocido -- posible cambio en el calculo de biasScore/aligned del Pine, o en el input que fija el umbral de alineacion con el sesgo de TF superior; no identificable solo con el feed de datos",
    "from": "aligned=0 en ~0% de las senales (historico W36-W43)",
    "to": "aligned=0 en 20-46% de las senales por simbolo desde 2026-10-26",
    "changeDate": "2026-10-26",
    "segment": {},
    "targetMetric": "by_aligned.expR / sl_post_mortem causa contra-sesgo (share)",
    "minAfterN": 40,
    "note": "PENDIENTE DE CONFIRMAR CON JESUS: preguntar si cambio algun input de sesgo/alineacion (o el indicador en si) alrededor del 2026-10-26, coincide con la aparicion de BTCUSDT/ETHUSDT y del tf=29m nuevo en el bus. Mientras no se confirme, NO se trata como experimento con before/after formal (no hay un input concreto que medir antes/despues), solo se vigila que by_aligned siga sano."
  }
]
```

## Session Analyst
```json
{
  "available": true,
  "latest_plan": {
    "date": "2026-10-31",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-10-30T16:09:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "CL",
    "focus": {
      "sym": "CL",
      "verdict": "WAIT",
      "window": "reapertura domingo 17:00 CT",
      "setup": {
        "es": "sin setup operable: mercado cerrado todo el fin de semana",
        "en": "no tradable setup: the market is closed the whole weekend"
      },
      "trigger": {
        "es": "ninguno hasta que reabra Globex el domingo 17:00 CT",
        "en": "none until Globex reopens Sunday 17:00 CT"
      },
      "invalid": {
        "es": "no aplica mientras el mercado este cerrado",
        "en": "not applicable while the market is closed"
      },
      "note": {
        "es": "hoy no hay nada, no fuerces; el plan real de la reapertura lo da la pre-asia del domingo",
        "en": "nothing today, don't force it; the real reopen plan comes from Sunday's own pre-asia"
      }
    },
    "summary": {
      "es": [
        "Mercado de futuros cerrado hasta la reapertura de Globex el domingo 17:00 CT: no hay sesion de Asia que operar este sabado.",
        "NQ: corto confirmado dia 2, cerro 28527.25 muy estirado (3.2 ATR) tras un dia de tendencia extrema (-652.75pts).",
        "ES: corto confirmado, cerro 7613.00 (-96.25pts) tras romper la invalidacion de 3 dias esta misma madrugada.",
        "GC: corto confirmado dia 2, cerro 3886.3 (-147.3pts) con el mayor estiramiento de los 5 (15.5 ATR).",
        "YM: corto confirmado dia 2, cerro 51922 (-577pts) muy estirado (6.3 ATR).",
        "CL: largo confirmado dia 4, cerro 102.88 casi plano pese a un rango amplio (hod 104.99/lod 102.43): reversion intradia a vigilar.",
        "mas limpio: CL (4 marcos alineados desde hace dias, aunque hoy con reversion intradia marcada)",
        "Este plan es un puente de fin de semana: lo reemplaza por completo la pre-asia del domingo antes de la reapertura real."
      ],
      "en": [
        "Futures market closed until the Sunday 17:00 CT Globex reopen: there is no Asia session to trade this Saturday.",
        "NQ: short confirmed, day 2, closed 28527.25 very stretched (3.2 ATR) after an extreme trend day (-652.75pts).",
        "ES: short confirmed, closed 7613.00 (-96.25pts) after breaking the 3-day invalidation earlier this morning.",
        "GC: short confirmed, day 2, closed 3886.3 (-147.3pts) with the biggest stretch of the five (15.5 ATR).",
        "YM: short confirmed, day 2, closed 51922 (-577pts), very stretched (6.3 ATR).",
        "CL: long confirmed, day 4, closed 102.88 nearly flat despite a wide range (hod 104.99/lod 102.43): an intraday reversal worth watching.",
        "cleanest: CL (4 frames aligned for days, though today with a marked intraday reversal)",
        "This plan is a weekend bridge: Sunday's own pre-asia fully replaces it before the real reopen."
      ]
    },
    "alarm": null,
    "dataH
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 24749,
  "by_verdict": {
    "AVOID": {
      "n": 2997,
      "wrTP1": 44.9,
      "nSL": 1450,
      "nTO": 202,
      "expR": 0.022,
      "pf": 1.04,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 33.9
    },
    "GO": {
      "n": 4874,
      "wrTP1": 47.7,
      "nSL": 2298,
      "nTO": 253,
      "expR": 0.005,
      "pf": 1.01,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 29.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 40.6
    },
    "WAIT": {
      "n": 16878,
      "wrTP1": 46.8,
      "nSL": 7955,
      "nTO": 1020,
      "expR": 0.043,
      "pf": 1.09,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 34.5
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.022,
      "ci90": [
        -0.016,
        0.061
      ],
      "p_mean_le_0": 0.187,
      "n": 2876
    },
    "GO": {
      "expR": 0.005,
      "ci90": [
        -0.023,
        0.031
      ],
      "p_mean_le_0": 0.411,
      "n": 4723
    },
    "WAIT": {
      "expR": 0.043,
      "ci90": [
        0.028,
        0.059
      ],
      "p_mean_le_0": 0.0,
      "n": 16401
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 2997,
      "wrTP1": 44.9,
      "nSL": 1450,
      "nTO": 202,
      "expR": 0.022,
      "pf": 1.04,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 33.9
    },
    "GO_or_WAIT": {
      "n": 21752,
      "wrTP1": 47.0,
      "nSL": 10253,
      "nTO": 1273,
      "expR": 0.035,
      "pf": 1.07,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 35.9
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.022,
      "ci90": [
        -0.016,
        0.061
      ],
      "p_mean_le_0": 0.187,
      "n": 2876
    },
    "GO_or_WAIT": {
      "expR": 0.035,
      "ci90": [
        0.022,
        0.049
      ],
      "p_mean_le_0": 0.0,
      "n": 21124
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 43,
        "wrTP1": 44.2,
        "nSL": 20,
        "nTO": 4,
        "expR": -0.124,
        "pf": 0.75,
        "mfe_p25": 6.0,
        "mfe_p50": 13.0,
        "mfe_p75": 30.0,
        "winnerMAE_p75": 13.5,
        "winnerMAE_p90": 17.4,
        "loserMFEbeforeSL_p50": 5.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 20.0
      },
      "GO": {
        "n": 70,
        "wrTP1": 55.7,
        "nSL": 26,
        "nTO": 5,
        "expR": 0.092,
        "pf": 1.24,
        "mfe_p25": 6.0,
        "mfe_p50": 19.5,
        "mfe_p75": 32.5,
        "winnerMAE_p75": 14.5,
        "winnerMAE_p90": 42.0,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 30.8
      },
      "WAIT": {
        "n": 250,
        "wrTP1": 44.8,
        "nSL": 117,
        "nTO": 21,
        "expR": -0.018,
        "pf": 0.96,
        "mfe_p25": 7.0,
        "mfe_p50": 15.0,
        "mfe_p75": 33.25,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 24.900000000000006,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 16.2
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 37,
        "wrTP1": 35.1,
        "nSL": 19,
        "nTO": 5,
        "expR": -0.271,
        "pf": 0.52,
        "mfe_p25": 8.25,
        "mfe_p50": 16.5,
        "mfe_p75": 27.0,
        "winnerMAE_p75": 4.0,
        "winnerMAE_p90": 5.800000000000001,
        "loserMFEbeforeSL_p50": 13.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 8.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 10.5
      },
      "GO": {
        "n": 30,
        "wrTP1": 60.0,
        "nSL": 9,
        "nTO": 3,
        "expR": 0.208,
        "pf": 1.68,
        "mfe_p25": 12.75,
        "mfe_p50": 26.0,
        "mfe_p75": 59.75,
        "winnerMAE_p75": 20.25,
        "winnerMAE_p90": 60.50000000000006,
        "loserMFEbeforeSL_p50": 25.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 9.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 11.1
      },
      "WAIT": {
        "n": 213,
        "wrTP1": 49.8,
        "nSL": 78,
        "nTO": 29,
        "expR": 0.127,
        "pf": 1.33,
        "mfe_p25": 8.0,
        "mfe_p50": 23.5,
        "mfe_p75": 52.25,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 30.5,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 23.1
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 1664,
        "wrTP1": 44.2,
        "nSL": 829,
        "nTO": 100,
        "expR": -0.015,
        "pf": 0.97,
        "mfe_p25": 8.0,
        "mfe_p50": 15.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 33.4
      },
      "GO": {
        "n": 3110,
        "wrTP1": 47.0,
        "nSL": 1510,
        "nTO": 138,
        "expR": -0.008,
        "pf": 0.98,
        "mfe_p25": 6.0,
        "mfe_p50": 16.0,
        "mfe_p75": 35.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 39.5
      },
      "WAIT": {
        "n": 9434,
        "wrTP1": 47.1,
        "nSL": 4492,
        "nTO": 501,
        "expR": 0.04,
        "pf": 1.08,
        "mfe_p25": 7.0,
        "mfe_p50": 16.0,
        "mfe_p75": 37.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 34.7
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 1253,
        "wrTP1": 46.1,
        "nSL": 582,
        "nTO": 93,
        "expR": 0.085,
        "pf": 1.17,
        "mfe_p25": 9.0,
        "mfe_p50": 20.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 35.7
      },
      "GO": {
        "n": 1664,
        "wrTP1": 48.3,
        "nSL": 753,
        "nTO": 107,
        "expR": 0.022,
        "pf": 1.05,
        "mfe_p25": 10.0,
        "mfe_p50": 22.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 35.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 43.4
      },
      "WAIT": {
        "n": 6981,
        "wrTP1": 46.5,
        "nSL": 3268,
        "nTO": 469,
        "expR": 0.047,
        "pf": 1.1,
        "mfe_p25": 10.0,
        "mfe_p50": 21.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 30.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 35.2
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
    "n": 43126,
    "wrTP1": 46.3,
    "nSL": 20234,
    "nTO": 2908,
    "expR": 0.036,
    "pf": 1.07,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 42.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 28.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 33.3
  },
  "shadow_ci90": {
    "expR": 0.036,
    "ci90": [
      0.026,
      0.046
    ],
    "p_mean_le_0": 0.0,
    "n": 41669
  },
  "raw_indicator": {
    "n": 48230,
    "wrTP1": 46.6,
    "nSL": 22642,
    "nTO": 3123,
    "expR": 0.038,
    "pf": 1.08,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 43.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 29.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 34.4
  },
  "raw_indicator_ci90": {
    "expR": 0.038,
    "ci90": [
      0.029,
      0.047
    ],
    "p_mean_le_0": 0.0,
    "n": 46649
  },
  "tier_ap_b_only": {
    "n": 24477,
    "wrTP1": 43.9,
    "nSL": 12003,
    "nTO": 1738,
    "expR": 0.029,
    "pf": 1.06,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.3
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.029,
    "ci90": [
      0.015,
      0.042
    ],
    "p_mean_le_0": 0.001,
    "n": 23683
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
    "shadow_n": 7227,
    "shadow_expR": 0.006,
    "raw_n": 9903,
    "raw_expR": 0.026,
    "shadow_beats_raw": false
  }
}
```
