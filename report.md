# Scalp CC · report 2026-10-30T01:44Z
- signals=48109 outcomes=46479 pares_resueltos=48049 pendientes=60 huerfanos=54

## ⚠ ALERTAS (llevar al frente del resumen)
- SL CAUSA: 'contra-sesgo' salta a 26.9% de las perdidas en 2026-W44 vs media 0.0% de las 3 semanas previas (2026-W41, 2026-W42, 2026-W43). Ver sl_post_mortem_weekly_trend -- puede ser una causa nueva dominante, o (si el segmento que la dispara en realidad rinde bien, ej. aligned=0 en by_aligned) una etiqueta que crece de muestra sin ser el problema real.
- GATE: 29m/RETEST/SHORT cumple el chequeo numerico agregado (n/PF/WR) pero NO el gate completo todavia -- weeklyStable3=False, slCauseMitigated=False. Es un near-miss a vigilar, no subir de peldano.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.13 vs 0.04, delta 0.091 CI90 [0.074, 0.11], n 28809). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.057 vs 0.017, delta 0.041 CI90 [0.01, 0.071], n 8367). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.043 CI90 [0.028, 0.059], n 16400). Consistente con la hipotesis original de agent-instructions.md.
- METODO: tus predicciones de direccion aciertan 0.0% (peor que un volado, n=6, MAE=0.267). Se mas conservador con 'cambio del mes' y marcar experimental mas tiempo antes de subir confianza.
- MODO SOMBRA: 3 semanas CERRADAS seguidas sin batir al indicador crudo (2026-W41, 2026-W42, 2026-W43) -- espejo inverso del gate de promocion del peldano 0->1. No implica bajar de peldano (ya promovido), pero revisar shadow_rules en la revision semanal.

- E[R] global: {"expR": 0.041, "ci90": [0.032, 0.051], "p_mean_le_0": 0.0, "n": 46425}
- gate ejecucion: {"readyForLive": true, "segment": "29m/RETEST/SHORT", "weeklyStable3": false, "weeklyDetail": [{"week": "2026-W41", "wrTP1": null, "pf": null, "ok": false}, {"week": "2026-W42", "wrTP1": null, "pf": null, "ok": false}, {"week": "2026-W43", "wrTP1": null, "pf": null, "ok": false}], "slCauseMitigated": false, "fullyReady": false, "note": "readyForLive: n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side (solo agregado historico). fullyReady exige ademas weeklyStable3 (3 semanas CERRADAS seguidas con WR>=50 & PF>=1.3 en ese mismo segmento) y slCauseMitigated (experimento con verdict=confirmed dirigido a ese segmento). Solo fullyReady=true es luz verde real para subir de peldano; readyForLive=true con fullyReady=false es un near-miss a vigilar."}

## Integridad de sigId (colisiones, posible causa de alertas MUESTRA)
```json
{
  "signals": {
    "total_sigIds": 43463,
    "collided_sigIds": 4302,
    "collided_pct": 9.9,
    "delta_days_histogram": {
      "14": 913,
      "7": 835,
      "21": 479,
      "28": 464,
      "35": 417,
      "42": 373,
      "49": 175,
      "56": 147,
      "34": 62,
      "48": 58
    },
    "conflicting_result_n": 0,
    "conflicting_result_examples": []
  },
  "outcomes": {
    "total_sigIds": 42145,
    "collided_sigIds": 4020,
    "collided_pct": 9.54,
    "delta_days_histogram": {
      "14": 871,
      "7": 779,
      "21": 443,
      "28": 429,
      "35": 391,
      "42": 331,
      "49": 167,
      "56": 135,
      "34": 62,
      "41": 56
    },
    "conflicting_result_n": 2331,
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
| 15m/INV/LONG | 3 | 66.7 | 0.18 | 1.54 | 1 | 101.0 | 155.75 | 0.0 |
| 15m/RETEST/LONG | 204 | 50.5 | 0.031 | 1.06 | 100 | 73.0 | 57.5 | 54.0 |
| 15m/RETEST/SHORT | 234 | 52.1 | 0.064 | 1.13 | 112 | 128.0 | 451.5 | 67.0 |
| 1m/INV/LONG | 441 | 47.2 | 0.138 | 1.32 | 183 | 15.0 | 11.0 | 18.0 |
| 1m/INV/SHORT | 319 | 46.4 | 0.08 | 1.19 | 126 | 20.5 | 14.0 | 16.7 |
| 1m/RETEST/LONG | 16954 | 45.0 | 0.027 | 1.06 | 8131 | 14.0 | 10.0 | 28.6 |
| 1m/RETEST/SHORT | 10919 | 44.9 | 0.026 | 1.05 | 5115 | 18.0 | 12.0 | 29.0 |
| 29m/RETEST/LONG | 82 | 57.3 | 0.151 | 1.35 | 35 | 132.0 | 399.0 | 54.3 |
| 29m/RETEST/SHORT | 149 | 58.4 | 0.182 | 1.44 | 62 | 127.0 | 195.5 | 69.4 |
| 2m/INV/LONG | 162 | 53.1 | 0.043 | 1.11 | 64 | 17.0 | 15.5 | 15.6 |
| 2m/INV/SHORT | 119 | 48.7 | 0.121 | 1.29 | 47 | 28.0 | 13.75 | 31.9 |
| 2m/RETEST/LONG | 7431 | 47.5 | 0.032 | 1.06 | 3510 | 19.0 | 12.0 | 38.9 |
| 2m/RETEST/SHORT | 4761 | 47.5 | 0.045 | 1.09 | 2219 | 24.0 | 14.0 | 39.0 |
| 3m/INV/LONG | 8 | 62.5 | 0.02 | 1.05 | 3 | 22.0 | 6.0 | 33.3 |
| 3m/INV/SHORT | 4 | 100.0 | 0.425 | 99.0 | 0 | 30.5 | 13.0 | None |
| 3m/RETEST/LONG | 642 | 55.3 | 0.13 | 1.3 | 278 | 22.0 | 14.0 | 55.4 |
| 3m/RETEST/SHORT | 629 | 54.2 | 0.119 | 1.27 | 276 | 22.0 | 14.0 | 55.1 |
| 5m/INV/LONG | 49 | 67.3 | 0.154 | 1.59 | 12 | 28.5 | 29.0 | 58.3 |
| 5m/INV/SHORT | 30 | 50.0 | 0.287 | 1.73 | 11 | 41.0 | 43.0 | 36.4 |
| 5m/RETEST/LONG | 2902 | 51.5 | 0.1 | 1.22 | 1252 | 33.0 | 23.0 | 48.2 |
| 5m/RETEST/SHORT | 2007 | 48.7 | 0.067 | 1.14 | 886 | 37.0 | 26.75 | 43.6 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 3302 | 22.4 | 0.01 | 1.01 | 2164 | 27.0 | 12.0 | 17.5 |
| B | 21035 | 47.2 | 0.031 | 1.06 | 9765 | 18.0 | 12.0 | 35.0 |
| C | 23712 | 49.6 | 0.054 | 1.12 | 10494 | 19.0 | 14.0 | 36.4 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 17559 | 48.8 | 0.073 | 1.16 | 7927 | 14.0 | 10.0 | 35.6 |
| London | 7266 | 46.3 | 0.021 | 1.04 | 3593 | 19.0 | 13.0 | 37.2 |
| NY | 8500 | 44.8 | 0.015 | 1.03 | 4090 | 27.0 | 18.0 | 36.3 |
| Sin KZ | 14724 | 45.4 | 0.027 | 1.06 | 6813 | 21.0 | 14.0 | 28.9 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 12449 | 44.9 | 0.025 | 1.05 | 5911 | 22.0 | 15.0 | 32.2 |
| edge=0 | 18666 | 49.1 | 0.057 | 1.12 | 8414 | 17.0 | 11.0 | 37.1 |
| edge=1 | 16934 | 45.3 | 0.035 | 1.07 | 8098 | 19.0 | 13.0 | 32.0 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 2475 | 54.3 | 0.085 | 1.19 | 1104 | 21.0 | 21.0 | 58.1 |
| aligned=1 | 45574 | 46.2 | 0.038 | 1.08 | 21319 | 19.0 | 13.0 | 32.7 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 25 | 52.0 | 0.014 | 1.03 | 12 | 21.0 | 15.0 | 16.7 |
| INV/LONG|edge=0 | 246 | 58.9 | 0.206 | 1.58 | 82 | 16.0 | 11.0 | 28.0 |
| INV/LONG|edge=1 | 392 | 44.9 | 0.065 | 1.14 | 169 | 16.0 | 13.0 | 15.4 |
| INV/SHORT|edge=-1 | 284 | 43.7 | 0.061 | 1.14 | 121 | 25.0 | 13.0 | 17.4 |
| INV/SHORT|edge=0 | 170 | 52.9 | 0.167 | 1.45 | 56 | 19.0 | 16.5 | 32.1 |
| INV/SHORT|edge=1 | 18 | 61.1 | 0.273 | 1.7 | 7 | 23.5 | 34.0 | 14.3 |
| RETEST/LONG|edge=-1 | 2415 | 52.0 | 0.089 | 1.19 | 1095 | 18.0 | 14.0 | 49.0 |
| RETEST/LONG|edge=0 | 11416 | 48.9 | 0.045 | 1.09 | 5233 | 15.0 | 11.0 | 36.7 |
| RETEST/LONG|edge=1 | 14384 | 44.0 | 0.025 | 1.05 | 6978 | 18.0 | 13.0 | 29.5 |
| RETEST/SHORT|edge=-1 | 9725 | 43.2 | 0.008 | 1.02 | 4683 | 23.0 | 15.0 | 28.7 |
| RETEST/SHORT|edge=0 | 6834 | 48.8 | 0.069 | 1.15 | 3043 | 20.0 | 13.0 | 38.1 |
| RETEST/SHORT|edge=1 | 2140 | 54.2 | 0.091 | 1.2 | 944 | 20.0 | 18.0 | 53.2 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 245 | 42.0 | 0.048 | 1.1 | 113 | 16.0 | 13.0 | 11.5 |
| INV/LONG|tier=C | 418 | 55.3 | 0.154 | 1.41 | 150 | 16.0 | 12.0 | 25.3 |
| INV/SHORT|tier=B | 154 | 44.8 | 0.031 | 1.07 | 68 | 25.0 | 12.0 | 8.8 |
| INV/SHORT|tier=C | 318 | 49.1 | 0.145 | 1.36 | 116 | 23.0 | 20.25 | 29.3 |
| RETEST/LONG|tier=A+ | 2125 | 22.0 | 0.009 | 1.01 | 1414 | 23.0 | 11.0 | 15.8 |
| RETEST/LONG|tier=B | 12293 | 47.7 | 0.043 | 1.09 | 5700 | 17.0 | 11.0 | 36.6 |
| RETEST/LONG|tier=C | 13797 | 49.6 | 0.04 | 1.09 | 6192 | 17.0 | 13.0 | 35.6 |
| RETEST/SHORT|tier=A+ | 1177 | 23.0 | 0.011 | 1.02 | 750 | 37.0 | 14.0 | 20.5 |
| RETEST/SHORT|tier=B | 8343 | 46.6 | 0.013 | 1.03 | 3884 | 20.0 | 13.0 | 33.7 |
| RETEST/SHORT|tier=C | 9179 | 49.4 | 0.069 | 1.15 | 4036 | 22.0 | 15.0 | 38.3 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=0 | 9 | 66.7 | 0.061 | 1.18 | 3 | 25.0 | 29.5 | 0.0 |
| INV/LONG|aligned=1 | 654 | 50.2 | 0.115 | 1.28 | 260 | 16.0 | 12.0 | 19.6 |
| INV/SHORT|aligned=0 | 8 | 62.5 | -0.037 | 0.9 | 3 | 25.5 | 32.0 | 33.3 |
| INV/SHORT|aligned=1 | 464 | 47.4 | 0.109 | 1.26 | 181 | 24.0 | 14.0 | 21.5 |
| RETEST/LONG|aligned=0 | 1005 | 53.3 | 0.066 | 1.15 | 452 | 20.0 | 19.0 | 59.7 |
| RETEST/LONG|aligned=1 | 27210 | 46.4 | 0.038 | 1.08 | 12854 | 17.0 | 12.0 | 33.1 |
| RETEST/SHORT|aligned=0 | 1453 | 54.9 | 0.098 | 1.22 | 646 | 22.0 | 23.0 | 57.3 |
| RETEST/SHORT|aligned=1 | 17246 | 45.8 | 0.035 | 1.07 | 8024 | 22.0 | 14.0 | 32.9 |

## Autopsia de SL
n_losses=22423  causas: RR-bajo×8647, contra-estructura×7865, stop-en-el-minimo×7616, killzone-Asia-largo×4974, estirado×3817, sin-nivel-detras×3592, chop×3287, SL-muy-pegado×2788, sin-causa-clara×2352, contra-sesgo×1104
- INV/LONG (n=263): killzone-Asia-largo×126, RR-bajo×100, contra-estructura×83, estirado×53, stop-en-el-minimo×51, sin-nivel-detras×33, chop×29, SL-muy-pegado×27, sin-causa-clara×16, contra-sesgo×3
- INV/SHORT (n=184): RR-bajo×79, contra-estructura×55, estirado×41, stop-en-el-minimo×40, SL-muy-pegado×31, sin-causa-clara×27, chop×26, sin-nivel-detras×11, contra-sesgo×3
- RETEST/LONG (n=13306): RR-bajo×5155, killzone-Asia-largo×4848, contra-estructura×4783, stop-en-el-minimo×4519, sin-nivel-detras×2289, estirado×2282, chop×1957, SL-muy-pegado×1590, sin-causa-clara×1116, contra-sesgo×452
- RETEST/SHORT (n=8670): RR-bajo×3313, stop-en-el-minimo×3006, contra-estructura×2944, estirado×1441, chop×1275, sin-nivel-detras×1259, sin-causa-clara×1193, SL-muy-pegado×1140, contra-sesgo×646

## Autopsia de SL · semana 2026-W44 (para revision semanal)
n_losses=4095  causas: RR-bajo×1934, contra-estructura×1733, stop-en-el-minimo×1718, contra-sesgo×1103, estirado×739, killzone-Asia-largo×718, chop×517, SL-muy-pegado×439, sin-causa-clara×327, sin-nivel-detras×272
ejemplos por causa: {"RR-bajo": ["YM-2-22042-S", "CL-1-23380-L", "NQ-1-23615-S", "YM-2-22073-S", "NQ-2-22218-S"], "contra-estructura": ["NQ-2-22054-L", "YM-2-22042-S", "NQ-1-23740-S", "NQ-1-23743-S", "ES-1-23741-S"], "stop-en-el-minimo": ["YM-2-22042-S", "YM-2-22073-S", "NQ-1-23743-S", "NQ-2-22221-S", "GC-2-22230-S"]}

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
    "n_losses": 4095,
    "causes_pct": {
      "RR-bajo": 47.2,
      "contra-estructura": 42.3,
      "stop-en-el-minimo": 42.0,
      "contra-sesgo": 26.9,
      "estirado": 18.0,
      "killzone-Asia-largo": 17.5,
      "chop": 12.6,
      "SL-muy-pegado": 10.7,
      "sin-causa-clara": 8.0,
      "sin-nivel-detras": 6.6
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
    "n": 46412,
    "naive_expR": 0.041,
    "managed_expR": 0.117,
    "delta": 0.076,
    "avgEntryBetterTk_p50": 2.7,
    "fill_t3plus_pct": 45.7,
    "fill_full_pct": 32.3,
    "m1_rate": 37.0,
    "m2_rate": 22.5,
    "m3_rate": 11.7,
    "beAfterM1_rate": 18.2
  },
  "by_tf_kind_side": {
    "15m/INV/LONG": {
      "n": 3,
      "naive_expR": 0.18,
      "managed_expR": 0.555,
      "delta": 0.375,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 33.3,
      "fill_full_pct": 0.0,
      "m1_rate": 66.7,
      "m2_rate": 66.7,
      "m3_rate": 0.0,
      "beAfterM1_rate": 0.0
    },
    "15m/RETEST/LONG": {
      "n": 204,
      "naive_expR": 0.031,
      "managed_expR": -0.15,
      "delta": -0.181,
      "avgEntryBetterTk_p50": 9.45,
      "fill_t3plus_pct": 37.7,
      "fill_full_pct": 24.0,
      "m1_rate": 31.9,
      "m2_rate": 19.1,
      "m3_rate": 9.3,
      "beAfterM1_rate": 14.7
    },
    "15m/RETEST/SHORT": {
      "n": 234,
      "naive_expR": 0.064,
      "managed_expR": -0.031,
      "delta": -0.096,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 27.8,
      "fill_full_pct": 15.8,
      "m1_rate": 32.1,
      "m2_rate": 19.7,
      "m3_rate": 12.0,
      "beAfterM1_rate": 15.8
    },
    "1m/INV/LONG": {
      "n": 426,
      "naive_expR": 0.138,
      "managed_expR": 0.269,
      "delta": 0.131,
      "avgEntryBetterTk_p50": 2.4,
      "fill_t3plus_pct": 50.2,
      "fill_full_pct": 36.6,
      "m1_rate": 41.5,
      "m2_rate": 24.9,
      "m3_rate": 12.2,
      "beAfterM1_rate": 19.2
    },
    "1m/INV/SHORT": {
      "n": 300,
      "naive_expR": 0.08,
      "managed_expR": 0.273,
      "delta": 0.193,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 49.0,
      "fill_full_pct": 36.7,
      "m1_rate": 41.0,
      "m2_rate": 25.0,
      "m3_rate": 12.0,
      "beAfterM1_rate": 18.0
    },
    "1m/RETEST/LONG": {
      "n": 16481,
      "naive_expR": 0.027,
      "managed_expR": 0.121,
      "delta": 0.094,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.5,
      "fill_full_pct": 33.8,
      "m1_rate": 36.8,
      "m2_rate": 22.4,
      "m3_rate": 11.9,
      "beAfterM1_rate": 17.5
    },
    "1m/RETEST/SHORT": {
      "n": 10422,
      "naive_expR": 0.026,
      "managed_expR": 0.148,
      "delta": 0.122,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 48.4,
      "fill_full_pct": 34.3,
      "m1_rate": 38.4,
      "m2_rate": 23.8,
      "m3_rate": 12.2,
      "beAfterM1_rate": 18.0
    },
    "29m/RETEST/LONG": {
      "n": 82,
      "naive_expR": 0.151,
      "managed_expR": -0.11,
      "delta": -0.261,
      "avgEntryBetterTk_p50": 16.950000000000003,
      "fill_t3plus_pct": 41.5,
      "fill_full_pct": 29.3,
      "m1_rate": 31.7,
      "m2_rate": 22.0,
      "m3_rate": 7.3,
      "beAfterM1_rate": 9.8
    },
    "29m/RETEST/SHORT": {
      "n": 149,
      "naive_expR": 0.182,
      "managed_expR": -0.131,
      "delta": -0.313,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 22.1,
      "fill_full_pct": 10.7,
      "m1_rate": 36.9,
      "m2_rate": 16.1,
      "m3_rate": 10.1,
      "beAfterM1_rate": 22.8
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
      "n": 115,
      "naive_expR": 0.121,
      "managed_expR": 0.272,
      "delta": 0.151,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 50.4,
      "fill_full_pct": 38.3,
      "m1_rate": 35.7,
      "m2_rate": 25.2,
      "m3_rate": 14.8,
      "beAfterM1_rate": 12.2
    },
    "2m/RETEST/LONG": {
      "n": 7220,
      "naive_expR": 0.031,
      "managed_expR": 0.088,
      "delta": 0.057,
      "avgEntryBetterTk_p50": 2.7,
      "fill_t3plus_pct": 44.5,
      "fill_full_pct": 31.6,
      "m1_rate": 35.8,
      "m2_rate": 21.7,
      "m3_rate": 11.3,
      "beAfterM1_rate": 18.3
    },
    "2m/RETEST/SHORT": {
      "n": 4593,
      "naive_expR": 0.045,
      "managed_expR": 0.125,
      "delta": 0.08,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 45.3,
      "fill_full_pct": 31.8,
      "m1_rate": 37.6,
      "m2_rate": 22.7,
      "m3_rate": 11.8,
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
      "n": 4,
      "naive_expR": 0.425,
      "managed_expR": 0.286,
      "delta": -0.139,
      "avgEntryBetterTk_p50": 1.35,
      "fill_t3plus_pct": 25.0,
      "fill_full_pct": 25.0,
      "m1_rate": 25.0,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 25.0
    },
    "3m/RETEST/LONG": {
      "n": 638,
      "naive_expR": 0.13,
      "managed_expR": 0.056,
      "delta": -0.074,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 46.1,
      "fill_full_pct": 32.1,
      "m1_rate": 34.2,
      "m2_rate": 19.0,
      "m3_rate": 9.6,
      "beAfterM1_rate": 19.0
    },
    "3m/RETEST/SHORT": {
      "n": 625,
      "naive_expR": 0.119,
      "managed_expR": 0.092,
      "delta": -0.027,
      "avgEntryBetterTk_p50": 2.6,
      "fill_t3plus_pct": 38.4,
      "fill_full_pct": 27.8,
      "m1_rate": 37.1,
      "m2_rate": 21.3,
      "m3_rate": 9.4,
      "beAfterM1_rate": 19.7
    },
    "5m/INV/LONG": {
      "n": 46,
      "naive_expR": 0.154,
      "managed_expR": 0.129,
      "delta": -0.025,
      "avgEntryBetterTk_p50": 3.0,
      "fill_t3plus_pct": 39.1,
      "fill_full_pct": 30.4,
      "m1_rate": 19.6,
      "m2_rate": 6.5,
      "m3_rate": 2.2,
      "beAfterM1_rate": 15.2
    },
    "5m/INV/SHORT": {
      "n": 28,
      "naive_expR": 0.287,
      "managed_expR": 0.291,
      "delta": 0.004,
      "avgEntryBetterTk_p50": 6.35,
      "fill_t3plus_pct": 57.1,
      "fill_full_pct": 39.3,
      "m1_rate": 28.6,
      "m2_rate": 21.4,
      "m3_rate": 21.4,
      "beAfterM1_rate": 10.7
    },
    "5m/RETEST/LONG": {
      "n": 2783,
      "naive_expR": 0.1,
      "managed_expR": 0.085,
      "delta": -0.015,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 37.1,
      "fill_full_pct": 26.0,
      "m1_rate": 36.4,
      "m2_rate": 22.2,
      "m3_rate": 11.1,
      "beAfterM1_rate": 19.5
    },
    "5m/RETEST/SHORT": {
      "n": 1894,
      "naive_expR": 0.067,
      "managed_expR": 0.082,
      "delta": 0.015,
      "avgEntryBetterTk_p50": 3.6,
      "fill_t3plus_pct": 37.5,
      "fill_full_pct": 25.1,
      "m1_rate": 35.7,
      "m2_rate": 21.6,
      "m3_rate": 11.1,
      "beAfterM1_rate": 18.8
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 38088,
    "layer_expR": 0.036,
    "orig_expR": 0.166,
    "delta_orig_minus_layer": 0.13,
    "delta_ci90": [
      0.066,
      0.233
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.1,
    "orig_wrTP1": 34.9,
    "slTk_p50": 22.0,
    "slOrigTk_p50": 10.0,
    "orig_wider_pct": 4.5,
    "orig_saved_from_SL": 82,
    "orig_caused_SL": 5095
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 3681,
  "invalid_by_seg": {
    "2m/RETEST/LONG": 508,
    "1m/RETEST/SHORT": 742,
    "2m/RETEST/SHORT": 243,
    "1m/RETEST/LONG": 1759,
    "1m/INV/SHORT": 45,
    "5m/RETEST/LONG": 102,
    "1m/INV/LONG": 81,
    "2m/INV/LONG": 23,
    "5m/INV/LONG": 4,
    "2m/INV/SHORT": 8,
    "5m/RETEST/SHORT": 67,
    "5m/INV/SHORT": 2,
    "3m/RETEST/LONG": 44,
    "3m/RETEST/SHORT": 36,
    "15m/RETEST/LONG": 4,
    "29m/RETEST/SHORT": 4,
    "15m/RETEST/SHORT": 8,
    "29m/RETEST/LONG": 1
  },
  "by_basis": {
    "candle1": {
      "n": 912,
      "layer_expR": 0.112,
      "orig_expR": 2.283,
      "delta_orig_minus_layer": 2.17,
      "delta_ci90": [
        -0.106,
        6.571
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 52.3,
      "orig_wrTP1": 28.7,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 3.8,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 217
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
      "n": 28809,
      "layer_expR": 0.04,
      "orig_expR": 0.13,
      "delta_orig_minus_layer": 0.091,
      "delta_ci90": [
        0.074,
        0.11
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.5,
      "orig_wrTP1": 35.6,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 5.2,
      "orig_saved_from_SL": 77,
      "orig_caused_SL": 3789
    },
    "retestBar2": {
      "n": 8367,
      "layer_expR": 0.017,
      "orig_expR": 0.057,
      "delta_orig_minus_layer": 0.041,
      "delta_ci90": [
        0.01,
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
      "orig_caused_SL": 1089
    }
  },
  "by_tf_kind_side": {
    "15m/RETEST/LONG": {
      "n": 199,
      "layer_expR": 0.049,
      "orig_expR": 0.399,
      "delta_orig_minus_layer": 0.35,
      "delta_ci90": [
        0.143,
        0.611
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.3,
      "orig_wrTP1": 49.7,
      "slTk_p50": 53.0,
      "slOrigTk_p50": 55.0,
      "orig_wider_pct": 30.2,
      "orig_saved_from_SL": 5,
      "orig_caused_SL": 8
    },
    "15m/RETEST/SHORT": {
      "n": 220,
      "layer_expR": 0.065,
      "orig_expR": 0.241,
      "delta_orig_minus_layer": 0.176,
      "delta_ci90": [
        -0.029,
        0.388
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 52.7,
      "orig_wrTP1": 46.4,
      "slTk_p50": 73.5,
      "slOrigTk_p50": 78.5,
      "orig_wider_pct": 27.3,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 20
    },
    "1m/INV/LONG": {
      "n": 345,
      "layer_expR": 0.13,
      "orig_expR": 0.136,
      "delta_orig_minus_layer": 0.006,
      "delta_ci90": [
        -0.182,
        0.195
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.3,
      "orig_wrTP1": 26.4,
      "slTk_p50": 17.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 79
    },
    "1m/INV/SHORT": {
      "n": 245,
      "layer_expR": 0.074,
      "orig_expR": -0.095,
      "delta_orig_minus_layer": -0.169,
      "delta_ci90": [
        -0.365,
        0.026
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.4,
      "orig_wrTP1": 25.7,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 2.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 59
    },
    "1m/RETEST/LONG": {
      "n": 12544,
      "layer_expR": 0.023,
      "orig_expR": 0.081,
      "delta_orig_minus_layer": 0.058,
      "delta_ci90": [
        0.033,
        0.085
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.5,
      "orig_wrTP1": 30.4,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 1.3,
      "orig_saved_from_SL": 4,
      "orig_caused_SL": 1895
    },
    "1m/RETEST/SHORT": {
      "n": 8490,
      "layer_expR": 0.017,
      "orig_expR": 0.059,
      "delta_orig_minus_layer": 0.042,
      "delta_ci90": [
        0.015,
        0.072
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.3,
      "orig_wrTP1": 33.3,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 1105
    },
    "29m/RETEST/LONG": {
      "n": 81,
      "layer_expR": 0.165,
      "orig_expR": 1.359,
      "delta_orig_minus_layer": 1.194,
      "delta_ci90": [
        0.084,
        2.743
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 58.0,
      "orig_wrTP1": 64.2,
      "slTk_p50": 72.0,
      "slOrigTk_p50": 103.0,
      "orig_wider_pct": 56.8,
      "orig_saved_from_SL": 5,
      "orig_caused_SL": 0
    },
    "29m/RETEST/SHORT": {
      "n": 144,
      "layer_expR": 0.223,
      "orig_expR": 0.452,
      "delta_orig_minus_layer": 0.229,
      "delta_ci90": [
        0.024,
        0.501
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 60.4,
      "orig_wrTP1": 61.1,
      "slTk_p50": 73.0,
      "slOrigTk_p50": 82.5,
      "orig_wider_pct": 41.0,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 5
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
      "n": 106,
      "layer_expR": 0.094,
      "orig_expR": 0.014,
      "delta_orig_minus_layer": -0.08,
      "delta_ci90": [
        -0.332,
        0.209
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.9,
      "orig_wrTP1": 32.1,
      "slTk_p50": 29.5,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.7,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 21
    },
    "2m/RETEST/LONG": {
      "n": 6134,
      "layer_expR": 0.03,
      "orig_expR": 0.111,
      "delta_orig_minus_layer": 0.081,
      "delta_ci90": [
        0.047,
        0.117
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.2,
      "orig_wrTP1": 36.7,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.9,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 774
    },
    "2m/RETEST/SHORT": {
      "n": 3946,
      "layer_expR": 0.045,
      "orig_expR": 0.121,
      "delta_orig_minus_layer": 0.076,
      "delta_ci90": [
        0.036,
        0.118
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.4,
      "orig_wrTP1": 36.3,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 3.5,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 525
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
    "3m/RETEST/LONG": {
      "n": 551,
      "layer_expR": 0.128,
      "orig_expR": 0.491,
      "delta_orig_minus_layer": 0.363,
      "delta_ci90": [
        0.212,
        0.523
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 55.7,
      "orig_wrTP1": 42.1,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 5.6,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 77
    },
    "3m/RETEST/SHORT": {
      "n": 553,
      "layer_expR": 0.105,
      "orig_expR": 0.179,
      "delta_orig_minus_layer": 0.074,
      "delta_ci90": [
        -0.04,
        0.199
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 54.4,
      "orig_wrTP1": 38.2,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 90
    },
    "5m/INV/LONG": {
      "n": 42,
      "layer_expR": 0.188,
      "orig_expR": 0.126,
      "delta_orig_minus_layer": -0.062,
      "delta_ci90": [
        -0.439,
        0.367
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 73.8,
      "orig_wrTP1": 47.6,
      "slTk_p50": 35.5,
      "slOrigTk_p50": 11.5,
      "orig_wider_pct": 9.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 11
    },
    "5m/INV/SHORT": {
      "n": 25,
      "layer_expR": 0.381,
      "orig_expR": 79.486,
      "delta_orig_minus_layer": 79.106,
      "delta_ci90": [
        -1.114,
        239.084
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 56.0,
      "orig_wrTP1": 24.0,
      "slTk_p50": 49.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 20.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 8
    },
    "5m/RETEST/LONG": {
      "n": 2567,
      "layer_expR": 0.084,
      "orig_expR": 0.234,
      "delta_orig_minus_layer": 0.15,
      "delta_ci90": [
        0.09,
        0.213
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.7,
      "orig_wrTP1": 45.8,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 21.0,
      "orig_wider_pct": 14.9,
      "orig_saved_from_SL": 23,
      "orig_caused_SL": 227
    },
    "5m/RETEST/SHORT": {
      "n": 1747,
      "layer_expR": 0.046,
      "orig_expR": 0.162,
      "delta_orig_minus_layer": 0.117,
      "delta_ci90": [
        0.034,
        0.216
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.1,
      "orig_wrTP1": 43.2,
      "slTk_p50": 35.0,
      "slOrigTk_p50": 25.0,
      "orig_wider_pct": 17.6,
      "orig_saved_from_SL": 14,
      "orig_caused_SL": 152
    }
  },
  "since_change": {
    "changeDate": "2026-09-26",
    "n": 23769,
    "by_tf_kind_side": {
      "15m/RETEST/LONG": {
        "n": 199,
        "layer_expR": 0.049,
        "orig_expR": 0.399,
        "delta_orig_minus_layer": 0.35,
        "delta_ci90": [
          0.143,
          0.611
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 51.3,
        "orig_wrTP1": 49.7,
        "slTk_p50": 53.0,
        "slOrigTk_p50": 55.0,
        "orig_wider_pct": 30.2,
        "orig_saved_from_SL": 5,
        "orig_caused_SL": 8
      },
      "15m/RETEST/SHORT": {
        "n": 220,
        "layer_expR": 0.065,
        "orig_expR": 0.241,
        "delta_orig_minus_layer": 0.176,
        "delta_ci90": [
          -0.029,
          0.388
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 52.7,
        "orig_wrTP1": 46.4,
        "slTk_p50": 73.5,
        "slOrigTk_p50": 78.5,
        "orig_wider_pct": 27.3,
        "orig_saved_from_SL": 6,
        "orig_caused_SL": 20
      },
      "1m/INV/LONG": {
        "n": 213,
        "layer_expR": 0.116,
        "orig_expR": 0.24,
        "delta_orig_minus_layer": 0.125,
        "delta_ci90": [
          -0.093,
          0.361
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 51.2,
        "orig_wrTP1": 28.6,
        "slTk_p50": 17.0,
        "slOrigTk_p50": 5.0,
        "orig_wider_pct": 0.9,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 48
      },
      "1m/INV/SHORT": {
        "n": 141,
        "layer_expR": 0.105,
        "orig_expR": -0.141,
        "delta_orig_minus_layer": -0.246,
        "delta_ci90": [
          -0.449,
          -0.034
        ],
        "delta_beats_zero": false,
        "delta_below_zero": true,
        "layer_wrTP1": 48.9,
        "orig_wrTP1": 25.5,
        "slTk_p50": 25.0,
        "slOrigTk_p50": 6.0,
        "orig_wider_pct": 1.4,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 34
      },
      "1m/RETEST/LONG": {
        "n": 7363,
        "layer_expR": -0.001,
        "orig_expR": 0.032,
        "delta_orig_minus_layer": 0.033,
        "delta_ci90": [
          0.001,
          0.063
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 44.9,
        "orig_wrTP1": 29.8,
        "slTk_p50": 17.0,
        "slOrigTk_p50": 7.0,
        "orig_wider_pct": 1.3,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 1118
      },
      "1m/RETEST/SHORT": {
        "n": 5230,
        "layer_expR": 0.009,
        "orig_expR": 0.052,
        "delta_orig_minus_layer": 0.043,
        "delta_ci90": [
          0.009,
          0.078
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 46.4,
        "orig_wrTP1": 33.1,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 2.1,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 698
      },
      "29m/RETEST/LONG": {
        "n": 81,
        "layer_expR": 0.165,
        "orig_expR": 1.359,
        "delta_orig_minus_layer": 1.194,
        "delta_ci90": [
          0.084,
          2.743
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 58.0,
        "orig_wrTP1": 64.2,
        "slTk_p50": 72.0,
        "slOrigTk_p50": 103.0,
        "orig_wider_pct": 56.8,
        "orig_saved_from_SL": 5,
        "orig_caused_SL": 0
      },
      "29m/RETEST/SHORT": {
        "n": 144,
        "layer_expR": 0.223,
        "orig_expR": 0.452,
        "delta_orig_minus_layer": 0.229,
        "delta_ci90": [
          0.024,
          0.501
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 60.4,
        "orig_wrTP1": 61.1,
        "slTk_p50": 73.0,
        "slOrigTk_p50": 82.5,
        "orig_wider_pct": 41.0,
        "orig_saved_from_SL": 6,
        "orig_caused_SL": 5
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
        "n": 56,
        "layer_expR": 0.011,
        "orig_expR": -0.265,
        "delta_orig_minus_layer": -0.276,
        "delta_ci90": [
          -0.551,
          0.0
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 57.1,
        "orig_wrTP1": 30.4,
        "slTk_p50": 34.5,
        "slOrigTk_p50": 8.0,
        "orig_wider_pct": 5.4,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 15
      },
      "2m/RETEST/LONG": {
        "n": 3643,
        "layer_expR": 0.019,
        "orig_expR": 0.081,
        "delta_orig_minus_layer": 0.061,
        "delta_ci90": [
          0.022,
          0.104
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 49.1,
        "orig_wrTP1": 36.3,
        "slTk_p50": 20.0,
        "slOrigTk_p50": 10.0,
        "orig_wider_pct": 4.2,
        "orig_saved_from_SL": 3,
        "orig_caused_SL": 470
      },
      "2m/RETEST/SHORT": {
        "n": 2423,
        "layer_expR": 0.028,
        "orig_expR": 0.079,
        "delta_orig_minus_layer": 0.051,
        "delta_ci90": [
          0.002,
          0.104
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 48.5,
        "orig_wrTP1": 35.0,
        "slTk_p50": 26.0,
        "slOrigTk_p50": 13.0,
        "orig_wider_pct": 3.1,
        "orig_saved_from_SL": 4,
        "orig_caused_SL": 331
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
      "3m/RETEST/LONG": {
        "n": 551,
        "layer_expR": 0.128,
        "orig_expR": 0.491,
        "delta_orig_minus_layer": 0.363,
        "delta_ci90": [
          0.212,
          0.523
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 55.7,
        "orig_wrTP1": 42.1,
        "slTk_p50": 23.0,
        "slOrigTk_p50": 12.0,
        "orig_wider_pct": 5.6,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 77
      },
      "3m/RETEST/SHORT": {
        "n": 553,
        "layer_expR": 0.105,
        "orig_expR": 0.179,
        "delta_orig_minus_layer": 0.074,
        "delta_ci90": [
          -0.04,
          0.199
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 54.4,
        "orig_wrTP1": 38.2,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 3.1,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 90
      },
      "5m/INV/LONG": {
        "n": 24,
        "layer_expR": 0.001,
        "orig_expR": 0.514,
        "delta_orig_minus_layer": 0.513,
        "delta_ci90": [
          -0.01,
          1.118
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 70.8,
        "orig_wrTP1": 54.2,
        "slTk_p50": 34.0,
        "slOrigTk_p50": 13.0,
        "orig_wider_pct": 4.2,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 4
      },
      "5m/INV/SHORT": {
        "n": 15,
        "layer_expR": 0.382,
        "orig_expR": 132.767,
        "delta_orig_minus_layer": 132.385,
        "delta_ci90": [
          -1.263,
          399.068
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 46.7,
        "orig_wrTP1": 13.3,
        "slTk_p50": 63.0,
        "slOrigTk_p50": 9.0,
        "orig_wider_pct": 13.3,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 5
      },
      "5m/RETEST/LONG": {
        "n": 1644,
        "layer_expR": 0.063,
        "orig_expR": 0.21,
        "delta_orig_minus_layer": 0.147,
        "delta_ci90": [
          0.07,
          0.239
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 53.4,
        "orig_wrTP1": 46.0,
        "slTk_p50": 33.0,
        "slOrigTk_p50": 22.0,
        "orig_wider_pct": 13.7,
        "orig_saved_from_SL": 16,
        "orig_caused_SL": 138
      },
      "5m/RETEST/SHORT": {
        "n": 1171,
        "layer_expR": 0.045,
        "orig_expR": 0.152,
        "delta_orig_minus_layer": 0.107,
        "delta_ci90": [
          0.017,
          0.208
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 51.4,
        "orig_wrTP1": 43.0,
        "slTk_p50": 38.0,
        "slOrigTk_p50": 26.0,
        "orig_wider_pct": 15.2,
        "orig_saved_from_SL": 7,
        "orig_caused_SL": 105
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
      "n": 16403,
      "wrTP1": 46.6,
      "nSL": 7763,
      "nTO": 1003,
      "expR": 0.024,
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
      "revAfterSL_rate": 29.9,
      "ci90": {
        "expR": 0.024,
        "ci90": [
          0.009,
          0.04
        ],
        "p_mean_le_0": 0.004,
        "n": 15939
      }
    },
    "cuts": {
      "1.0": {
        "n": 7841,
        "wrTP1": 30.5,
        "nSL": 4724,
        "nTO": 729,
        "expR": 0.018,
        "pf": 1.03,
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
          "expR": 0.018,
          "ci90": [
            -0.009,
            0.045
          ],
          "p_mean_le_0": 0.143,
          "n": 7583
        }
      },
      "1.2": {
        "n": 6442,
        "wrTP1": 27.6,
        "nSL": 3994,
        "nTO": 668,
        "expR": 0.028,
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
          "expR": 0.028,
          "ci90": [
            -0.003,
            0.06
          ],
          "p_mean_le_0": 0.073,
          "n": 6223
        }
      },
      "1.3": {
        "n": 5869,
        "wrTP1": 26.2,
        "nSL": 3691,
        "nTO": 642,
        "expR": 0.027,
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
        "revAfterSL_rate": 17.4,
        "ci90": {
          "expR": 0.027,
          "ci90": [
            -0.005,
            0.062
          ],
          "p_mean_le_0": 0.08,
          "n": 5661
        }
      },
      "1.5": {
        "n": 4974,
        "wrTP1": 23.4,
        "nSL": 3218,
        "nTO": 590,
        "expR": 0.017,
        "pf": 1.03,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 15.5,
        "ci90": {
          "expR": 0.017,
          "ci90": [
            -0.019,
            0.055
          ],
          "p_mean_le_0": 0.219,
          "n": 4799
        }
      },
      "2.0": {
        "n": 3261,
        "wrTP1": 17.5,
        "nSL": 2212,
        "nTO": 479,
        "expR": 0.001,
        "pf": 1.0,
        "mfe_p25": 8.0,
        "mfe_p50": 21.0,
        "mfe_p75": 44.0,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 11.3,
        "ci90": {
          "expR": 0.001,
          "ci90": [
            -0.049,
            0.052
          ],
          "p_mean_le_0": 0.496,
          "n": 3141
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 10478,
      "wrTP1": 46.8,
      "nSL": 4816,
      "nTO": 757,
      "expR": 0.03,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 38.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 30.8,
      "ci90": {
        "expR": 0.03,
        "ci90": [
          0.012,
          0.048
        ],
        "p_mean_le_0": 0.007,
        "n": 10009
      }
    },
    "cuts": {
      "1.0": {
        "n": 5012,
        "wrTP1": 31.1,
        "nSL": 2912,
        "nTO": 541,
        "expR": 0.021,
        "pf": 1.03,
        "mfe_p25": 11.0,
        "mfe_p50": 26.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 22.0,
        "ci90": {
          "expR": 0.021,
          "ci90": [
            -0.014,
            0.056
          ],
          "p_mean_le_0": 0.162,
          "n": 4723
        }
      },
      "1.2": {
        "n": 4072,
        "wrTP1": 27.6,
        "nSL": 2456,
        "nTO": 492,
        "expR": 0.016,
        "pf": 1.03,
        "mfe_p25": 11.0,
        "mfe_p50": 26.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.4,
        "ci90": {
          "expR": 0.016,
          "ci90": [
            -0.024,
            0.055
          ],
          "p_mean_le_0": 0.263,
          "n": 3821
        }
      },
      "1.3": {
        "n": 3726,
        "wrTP1": 26.1,
        "nSL": 2280,
        "nTO": 475,
        "expR": 0.012,
        "pf": 1.02,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.3,
        "ci90": {
          "expR": 0.012,
          "ci90": [
            -0.031,
            0.054
          ],
          "p_mean_le_0": 0.32,
          "n": 3489
        }
      },
      "1.5": {
        "n": 3130,
        "wrTP1": 23.2,
        "nSL": 1968,
        "nTO": 435,
        "expR": 0.001,
        "pf": 1.0,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 16.2,
        "ci90": {
          "expR": 0.001,
          "ci90": [
            -0.047,
            0.048
          ],
          "p_mean_le_0": 0.478,
          "n": 2924
        }
      },
      "2.0": {
        "n": 2109,
        "wrTP1": 17.9,
        "nSL": 1389,
        "nTO": 342,
        "expR": -0.019,
        "pf": 0.97,
        "mfe_p25": 12.0,
        "mfe_p50": 29.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 11.75,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 11.5,
        "ci90": {
          "expR": -0.019,
          "ci90": [
            -0.08,
            0.044
          ],
          "p_mean_le_0": 0.7,
          "n": 1963
        }
      }
    }
  },
  "15/RETEST/LONG": {
    "baseline": {
      "n": 193,
      "wrTP1": 53.4,
      "nSL": 90,
      "nTO": 0,
      "expR": 0.082,
      "pf": 1.18,
      "mfe_p25": 29.0,
      "mfe_p50": 68.0,
      "mfe_p75": 237.0,
      "winnerMAE_p75": 57.5,
      "winnerMAE_p90": 377.3999999999999,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -72.0,
      "revAfterSL_rate": 60.0,
      "ci90": {
        "expR": 0.082,
        "ci90": [
          -0.055,
          0.218
        ],
        "p_mean_le_0": 0.172,
        "n": 193
      }
    },
    "cuts": {
      "1.0": {
        "n": 60,
        "wrTP1": 35.0,
        "nSL": 39,
        "nTO": 0,
        "expR": 0.01,
        "pf": 1.02,
        "mfe_p25": 37.75,
        "mfe_p50": 69.5,
        "mfe_p75": 150.5,
        "winnerMAE_p75": 36.0,
        "winnerMAE_p90": 114.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -54.0,
        "revAfterSL_rate": 79.5,
        "ci90": {
          "expR": 0.01,
          "ci90": [
            -0.277,
            0.315
          ],
          "p_mean_le_0": 0.48,
          "n": 60
        }
      },
      "1.2": {
        "n": 47,
        "wrTP1": 31.9,
        "nSL": 32,
        "nTO": 0,
        "expR": -0.002,
        "pf": 1.0,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 161.0,
        "winnerMAE_p75": 57.5,
        "winnerMAE_p90": 482.9999999999998,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -53.0,
        "revAfterSL_rate": 81.2,
        "ci90": {
          "expR": -0.002,
          "ci90": [
            -0.355,
            0.36
          ],
          "p_mean_le_0": 0.515,
          "n": 47
        }
      },
      "1.3": {
        "n": 42,
        "wrTP1": 31.0,
        "nSL": 29,
        "nTO": 0,
        "expR": -0.03,
        "pf": 0.96,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 171.5,
        "winnerMAE_p75": 56.0,
        "winnerMAE_p90": 606.0000000000005,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -56.5,
        "revAfterSL_rate": 82.8,
        "ci90": {
          "expR": -0.03,
          "ci90": [
            -0.403,
            0.35
          ],
          "p_mean_le_0": 0.577,
          "n": 42
        }
      },
      "1.5": {
        "n": 29,
        "wrTP1": 34.5,
        "nSL": 19,
        "nTO": 0,
        "expR": 0.122,
        "pf": 1.19,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 257.0,
        "winnerMAE_p75": 99.5,
        "winnerMAE_p90": 1723.1999999999966,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -52.0,
        "revAfterSL_rate": 84.2,
        "ci90": {
          "expR": 0.122,
          "ci90": [
            -0.343,
            0.632
          ],
          "p_mean_le_0": 0.358,
          "n": 29
        }
      }
    }
  },
  "15/RETEST/SHORT": {
    "baseline": {
      "n": 231,
      "wrTP1": 52.8,
      "nSL": 109,
      "nTO": 0,
      "expR": 0.078,
      "pf": 1.17,
      "mfe_p25": 33.5,
      "mfe_p50": 128.0,
      "mfe_p75": 1697.0,
      "winnerMAE_p75": 451.5,
      "winnerMAE_p90": 4058.5000000000014,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -247.0,
      "revAfterSL_rate": 68.8,
      "ci90": {
        "expR": 0.078,
        "ci90": [
          -0.05,
          0.209
        ],
        "p_mean_le_0": 0.172,
        "n": 231
      }
    },
    "cuts": {
      "1.0": {
        "n": 79,
        "wrTP1": 39.2,
        "nSL": 48,
        "nTO": 0,
        "expR": 0.223,
        "pf": 1.37,
        "mfe_p25": 66.0,
        "mfe_p50": 202.0,
        "mfe_p75": 6895.5,
        "winnerMAE_p75": 2598.5,
        "winnerMAE_p90": 3812.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -326.0,
        "revAfterSL_rate": 58.3,
        "ci90": {
          "expR": 0.223,
          "ci90": [
            -0.082,
            0.531
          ],
          "p_mean_le_0": 0.115,
          "n": 79
        }
      },
      "1.2": {
        "n": 62,
        "wrTP1": 40.3,
        "nSL": 37,
        "nTO": 0,
        "expR": 0.319,
        "pf": 1.53,
        "mfe_p25": 66.0,
        "mfe_p50": 182.5,
        "mfe_p75": 7566.0,
        "winnerMAE_p75": 2544.0,
        "winnerMAE_p90": 3694.6000000000004,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -326.0,
        "revAfterSL_rate": 54.1,
        "ci90": {
          "expR": 0.319,
          "ci90": [
            -0.045,
            0.667
          ],
          "p_mean_le_0": 0.07,
          "n": 62
        }
      },
      "1.3": {
        "n": 58,
        "wrTP1": 39.7,
        "nSL": 35,
        "nTO": 0,
        "expR": 0.297,
        "pf": 1.49,
        "mfe_p25": 66.0,
        "mfe_p50": 162.5,
        "mfe_p75": 7566.0,
        "winnerMAE_p75": 2460.0,
        "winnerMAE_p90": 3440.6000000000004,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -362.0,
        "revAfterSL_rate": 54.3,
        "ci90": {
          "expR": 0.297,
          "ci90": [
            -0.052,
            0.674
          ],
          "p_mean_le_0": 0.084,
          "n": 58
        }
      },
      "1.5": {
        "n": 45,
        "wrTP1": 33.3,
        "nSL": 30,
        "nTO": 0,
        "expR": 0.205,
        "pf": 1.31,
        "mfe_p25": 75.0,
        "mfe_p50": 228.0,
        "mfe_p75": 8134.0,
        "winnerMAE_p75": 2460.0,
        "winnerMAE_p90": 2740.6,
        "loserMFEbeforeSL_p50": 3.5,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -465.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.205,
          "ci90": [
            -0.212,
            0.666
          ],
          "p_mean_le_0": 0.234,
          "n": 45
        }
      },
      "2.0": {
        "n": 29,
        "wrTP1": 27.6,
        "nSL": 21,
        "nTO": 0,
        "expR": 0.107,
        "pf": 1.15,
        "mfe_p25": 74.0,
        "mfe_p50": 272.0,
        "mfe_p75": 16232.0,
        "winnerMAE_p75": 2445.25,
        "winnerMAE_p90": 3000.7,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 1.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -516.0,
        "revAfterSL_rate": 42.9,
        "ci90": {
          "expR": 0.107,
          "ci90": [
            -0.443,
            0.776
          ],
          "p_mean_le_0": 0.374,
          "n": 29
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 7214,
      "wrTP1": 48.9,
      "nSL": 3359,
      "nTO": 325,
      "expR": 0.029,
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
      "revAfterSL_rate": 40.6,
      "ci90": {
        "expR": 0.029,
        "ci90": [
          0.005,
          0.051
        ],
        "p_mean_le_0": 0.021,
        "n": 7013
      }
    },
    "cuts": {
      "1.0": {
        "n": 3269,
        "wrTP1": 31.9,
        "nSL": 1992,
        "nTO": 233,
        "expR": 0.016,
        "pf": 1.03,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 33.6,
        "ci90": {
          "expR": 0.016,
          "ci90": [
            -0.026,
            0.058
          ],
          "p_mean_le_0": 0.276,
          "n": 3148
        }
      },
      "1.2": {
        "n": 2668,
        "wrTP1": 28.6,
        "nSL": 1694,
        "nTO": 210,
        "expR": 0.008,
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
        "revAfterSL_rate": 31.3,
        "ci90": {
          "expR": 0.008,
          "ci90": [
            -0.04,
            0.06
          ],
          "p_mean_le_0": 0.383,
          "n": 2564
        }
      },
      "1.3": {
        "n": 2401,
        "wrTP1": 27.3,
        "nSL": 1545,
        "nTO": 200,
        "expR": 0.013,
        "pf": 1.02,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 30.2,
        "ci90": {
          "expR": 0.013,
          "ci90": [
            -0.043,
            0.068
          ],
          "p_mean_le_0": 0.353,
          "n": 2304
        }
      },
      "1.5": {
        "n": 1982,
        "wrTP1": 24.2,
        "nSL": 1313,
        "nTO": 189,
        "expR": 0.003,
        "pf": 1.0,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 27.5,
        "ci90": {
          "expR": 0.003,
          "ci90": [
            -0.058,
            0.065
          ],
          "p_mean_le_0": 0.492,
          "n": 1893
        }
      },
      "2.0": {
        "n": 1250,
        "wrTP1": 18.8,
        "nSL": 866,
        "nTO": 149,
        "expR": 0.007,
        "pf": 1.01,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 62.5,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 21.6,
        "ci90": {
          "expR": 0.007,
          "ci90": [
            -0.081,
            0.097
          ],
          "p_mean_le_0": 0.43,
          "n": 1183
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 4545,
      "wrTP1": 49.8,
      "nSL": 2065,
      "nTO": 218,
      "expR": 0.058,
      "pf": 1.12,
      "mfe_p25": 11.0,
      "mfe_p50": 24.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 32.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 41.9,
      "ci90": {
        "expR": 0.058,
        "ci90": [
          0.029,
          0.088
        ],
        "p_mean_le_0": 0.001,
        "n": 4401
      }
    },
    "cuts": {
      "1.0": {
        "n": 2064,
        "wrTP1": 33.1,
        "nSL": 1234,
        "nTO": 146,
        "expR": 0.049,
        "pf": 1.08,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 65.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 31.700000000000045,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 33.7,
        "ci90": {
          "expR": 0.049,
          "ci90": [
            -0.001,
            0.104
          ],
          "p_mean_le_0": 0.057,
          "n": 1983
        }
      },
      "1.2": {
        "n": 1662,
        "wrTP1": 29.5,
        "nSL": 1039,
        "nTO": 132,
        "expR": 0.04,
        "pf": 1.06,
        "mfe_p25": 17.0,
        "mfe_p50": 34.0,
        "mfe_p75": 70.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 30.6,
        "ci90": {
          "expR": 0.04,
          "ci90": [
            -0.023,
            0.106
          ],
          "p_mean_le_0": 0.134,
          "n": 1593
        }
      },
      "1.3": {
        "n": 1494,
        "wrTP1": 27.8,
        "nSL": 954,
        "nTO": 124,
        "expR": 0.031,
        "pf": 1.05,
        "mfe_p25": 17.0,
        "mfe_p50": 35.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 31.5,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 29.1,
        "ci90": {
          "expR": 0.031,
          "ci90": [
            -0.038,
            0.103
          ],
          "p_mean_le_0": 0.237,
          "n": 1431
        }
      },
      "1.5": {
        "n": 1236,
        "wrTP1": 25.0,
        "nSL": 820,
        "nTO": 107,
        "expR": 0.021,
        "pf": 1.03,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 74.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 27.6,
        "ci90": {
          "expR": 0.021,
          "ci90": [
            -0.061,
            0.1
          ],
          "p_mean_le_0": 0.359,
          "n": 1187
        }
      },
      "2.0": {
        "n": 802,
        "wrTP1": 20.3,
        "nSL": 556,
        "nTO": 83,
        "expR": 0.031,
        "pf": 1.04,
        "mfe_p25": 18.0,
        "mfe_p50": 38.0,
        "mfe_p75": 79.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 22.8,
        "ci90": {
          "expR": 0.031,
          "ci90": [
            -0.08,
            0.141
          ],
          "p_mean_le_0": 0.337,
          "n": 769
        }
      }
    }
  },
  "29/RETEST/LONG": {
    "baseline": {
      "n": 76,
      "wrTP1": 61.8,
      "nSL": 29,
      "nTO": 0,
      "expR": 0.242,
      "pf": 1.63,
      "mfe_p25": 45.5,
      "mfe_p50": 113.5,
      "mfe_p75": 1455.5,
      "winnerMAE_p75": 399.0,
      "winnerMAE_p90": 8496.399999999994,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -74.0,
      "revAfterSL_rate": 65.5,
      "ci90": {
        "expR": 0.242,
        "ci90": [
          0.033,
          0.462
        ],
        "p_mean_le_0": 0.03,
        "n": 76
      }
    },
    "cuts": {
      "1.0": {
        "n": 26,
        "wrTP1": 46.2,
        "nSL": 14,
        "nTO": 0,
        "expR": 0.334,
        "pf": 1.62,
        "mfe_p25": 42.5,
        "mfe_p50": 73.0,
        "mfe_p75": 143.5,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 114.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -39.5,
        "revAfterSL_rate": 78.6,
        "ci90": {
          "expR": 0.334,
          "ci90": [
            -0.154,
            0.857
          ],
          "p_mean_le_0": 0.12,
          "n": 26
        }
      },
      "1.2": {
        "n": 20,
        "wrTP1": 40.0,
        "nSL": 12,
        "nTO": 0,
        "expR": 0.202,
        "pf": 1.34,
        "mfe_p25": 44.5,
        "mfe_p50": 73.0,
        "mfe_p75": 142.5,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 1103.3999999999994,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 75.0,
        "ci90": {
          "expR": 0.202,
          "ci90": [
            -0.37,
            0.768
          ],
          "p_mean_le_0": 0.284,
          "n": 20
        }
      }
    }
  },
  "29/RETEST/SHORT": {
    "baseline": {
      "n": 148,
      "wrTP1": 58.8,
      "nSL": 61,
      "nTO": 0,
      "expR": 0.19,
      "pf": 1.46,
      "mfe_p25": 30.0,
      "mfe_p50": 120.0,
      "mfe_p75": 652.75,
      "winnerMAE_p75": 195.5,
      "winnerMAE_p90": 1691.4000000000076,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -202.0,
      "revAfterSL_rate": 70.5,
      "ci90": {
        "expR": 0.19,
        "ci90": [
          0.037,
          0.34
        ],
        "p_mean_le_0": 0.019,
        "n": 148
      }
    },
    "cuts": {
      "1.0": {
        "n": 46,
        "wrTP1": 43.5,
        "nSL": 26,
        "nTO": 0,
        "expR": 0.27,
        "pf": 1.48,
        "mfe_p25": 47.5,
        "mfe_p50": 130.5,
        "mfe_p75": 916.25,
        "winnerMAE_p75": 319.75,
        "winnerMAE_p90": 1293.6000000000017,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -259.5,
        "revAfterSL_rate": 53.8,
        "ci90": {
          "expR": 0.27,
          "ci90": [
            -0.107,
            0.633
          ],
          "p_mean_le_0": 0.117,
          "n": 46
        }
      },
      "1.2": {
        "n": 37,
        "wrTP1": 35.1,
        "nSL": 24,
        "nTO": 0,
        "expR": 0.154,
        "pf": 1.24,
        "mfe_p25": 47.0,
        "mfe_p50": 148.0,
        "mfe_p75": 1211.0,
        "winnerMAE_p75": 403.0,
        "winnerMAE_p90": 2221.800000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -281.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.154,
          "ci90": [
            -0.281,
            0.615
          ],
          "p_mean_le_0": 0.284,
          "n": 37
        }
      },
      "1.3": {
        "n": 34,
        "wrTP1": 32.4,
        "nSL": 23,
        "nTO": 0,
        "expR": 0.125,
        "pf": 1.19,
        "mfe_p25": 92.0,
        "mfe_p50": 178.0,
        "mfe_p75": 1229.75,
        "winnerMAE_p75": 782.0,
        "winnerMAE_p90": 2487.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -281.0,
        "revAfterSL_rate": 52.2,
        "ci90": {
          "expR": 0.125,
          "ci90": [
            -0.31,
            0.597
          ],
          "p_mean_le_0": 0.366,
          "n": 34
        }
      },
      "1.5": {
        "n": 26,
        "wrTP1": 34.6,
        "nSL": 17,
        "nTO": 0,
        "expR": 0.243,
        "pf": 1.37,
        "mfe_p25": 92.0,
        "mfe_p50": 130.5,
        "mfe_p75": 817.0,
        "winnerMAE_p75": 292.0,
        "winnerMAE_p90": 554.6000000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -218.0,
        "revAfterSL_rate": 41.2,
        "ci90": {
          "expR": 0.243,
          "ci90": [
            -0.313,
            0.788
          ],
          "p_mean_le_0": 0.271,
          "n": 26
        }
      }
    }
  },
  "3/RETEST/LONG": {
    "baseline": {
      "n": 633,
      "wrTP1": 56.1,
      "nSL": 272,
      "nTO": 6,
      "expR": 0.135,
      "pf": 1.31,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 50.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 32.60000000000002,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 56.6,
      "ci90": {
        "expR": 0.135,
        "ci90": [
          0.061,
          0.212
        ],
        "p_mean_le_0": 0.001,
        "n": 629
      }
    },
    "cuts": {
      "1.0": {
        "n": 217,
        "wrTP1": 42.4,
        "nSL": 123,
        "nTO": 2,
        "expR": 0.204,
        "pf": 1.36,
        "mfe_p25": 15.0,
        "mfe_p50": 35.0,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 14.25,
        "winnerMAE_p90": 41.80000000000001,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 52.8,
        "ci90": {
          "expR": 0.204,
          "ci90": [
            0.033,
            0.365
          ],
          "p_mean_le_0": 0.021,
          "n": 217
        }
      },
      "1.2": {
        "n": 165,
        "wrTP1": 39.4,
        "nSL": 98,
        "nTO": 2,
        "expR": 0.209,
        "pf": 1.35,
        "mfe_p25": 20.0,
        "mfe_p50": 38.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 38.400000000000006,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 52.0,
        "ci90": {
          "expR": 0.209,
          "ci90": [
            0.012,
            0.408
          ],
          "p_mean_le_0": 0.042,
          "n": 165
        }
      },
      "1.3": {
        "n": 142,
        "wrTP1": 39.4,
        "nSL": 84,
        "nTO": 2,
        "expR": 0.245,
        "pf": 1.41,
        "mfe_p25": 24.25,
        "mfe_p50": 40.0,
        "mfe_p75": 84.5,
        "winnerMAE_p75": 14.25,
        "winnerMAE_p90": 42.5,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.245,
          "ci90": [
            0.027,
            0.462
          ],
          "p_mean_le_0": 0.029,
          "n": 142
        }
      },
      "1.5": {
        "n": 106,
        "wrTP1": 39.6,
        "nSL": 62,
        "nTO": 2,
        "expR": 0.337,
        "pf": 1.58,
        "mfe_p25": 25.25,
        "mfe_p50": 43.5,
        "mfe_p75": 85.0,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 48.999999999999986,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -15.5,
        "revAfterSL_rate": 41.9,
        "ci90": {
          "expR": 0.337,
          "ci90": [
            0.07,
            0.614
          ],
          "p_mean_le_0": 0.02,
          "n": 106
        }
      },
      "2.0": {
        "n": 60,
        "wrTP1": 33.3,
        "nSL": 38,
        "nTO": 2,
        "expR": 0.339,
        "pf": 1.54,
        "mfe_p25": 31.0,
        "mfe_p50": 48.0,
        "mfe_p75": 88.25,
        "winnerMAE_p75": 11.25,
        "winnerMAE_p90": 29.300000000000033,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 39.5,
        "ci90": {
          "expR": 0.339,
          "ci90": [
            -0.036,
            0.728
          ],
          "p_mean_le_0": 0.07,
          "n": 60
        }
      }
    }
  },
  "3/RETEST/SHORT": {
    "baseline": {
      "n": 616,
      "wrTP1": 55.4,
      "nSL": 266,
      "nTO": 9,
      "expR": 0.135,
      "pf": 1.31,
      "mfe_p25": 11.75,
      "mfe_p50": 22.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 35.0,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -22.0,
      "revAfterSL_rate": 57.1,
      "ci90": {
        "expR": 0.135,
        "ci90": [
          0.061,
          0.208
        ],
        "p_mean_le_0": 0.001,
        "n": 612
      }
    },
    "cuts": {
      "1.0": {
        "n": 220,
        "wrTP1": 40.9,
        "nSL": 122,
        "nTO": 8,
        "expR": 0.223,
        "pf": 1.4,
        "mfe_p25": 15.0,
        "mfe_p50": 26.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 12.75,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 1.5,
        "bars_win_p50": 2.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 53.3,
        "ci90": {
          "expR": 0.223,
          "ci90": [
            0.071,
            0.391
          ],
          "p_mean_le_0": 0.008,
          "n": 217
        }
      },
      "1.2": {
        "n": 163,
        "wrTP1": 36.2,
        "nSL": 96,
        "nTO": 8,
        "expR": 0.212,
        "pf": 1.35,
        "mfe_p25": 16.75,
        "mfe_p50": 29.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 51.0,
        "ci90": {
          "expR": 0.212,
          "ci90": [
            0.005,
            0.414
          ],
          "p_mean_le_0": 0.045,
          "n": 160
        }
      },
      "1.3": {
        "n": 141,
        "wrTP1": 36.2,
        "nSL": 82,
        "nTO": 8,
        "expR": 0.262,
        "pf": 1.44,
        "mfe_p25": 17.25,
        "mfe_p50": 29.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 13.5,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 1.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -22.0,
        "revAfterSL_rate": 46.3,
        "ci90": {
          "expR": 0.262,
          "ci90": [
            0.037,
            0.495
          ],
          "p_mean_le_0": 0.025,
          "n": 138
        }
      },
      "1.5": {
        "n": 117,
        "wrTP1": 31.6,
        "nSL": 73,
        "nTO": 7,
        "expR": 0.2,
        "pf": 1.31,
        "mfe_p25": 17.5,
        "mfe_p50": 30.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 41.1,
        "ci90": {
          "expR": 0.2,
          "ci90": [
            -0.066,
            0.464
          ],
          "p_mean_le_0": 0.103,
          "n": 115
        }
      },
      "2.0": {
        "n": 62,
        "wrTP1": 32.3,
        "nSL": 37,
        "nTO": 5,
        "expR": 0.421,
        "pf": 1.69,
        "mfe_p25": 19.0,
        "mfe_p50": 33.0,
        "mfe_p75": 69.0,
        "winnerMAE_p75": 13.25,
        "winnerMAE_p90": 22.70000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.5,
        "revAfterSL_rate": 21.6,
        "ci90": {
          "expR": 0.421,
          "ci90": [
            0.025,
            0.844
          ],
          "p_mean_le_0": 0.042,
          "n": 61
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 2790,
      "wrTP1": 53.5,
      "nSL": 1172,
      "nTO": 124,
      "expR": 0.112,
      "pf": 1.26,
      "mfe_p25": 14.0,
      "mfe_p50": 32.0,
      "mfe_p75": 73.0,
      "winnerMAE_p75": 23.0,
      "winnerMAE_p90": 66.70000000000005,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -35.0,
      "revAfterSL_rate": 51.5,
      "ci90": {
        "expR": 0.112,
        "ci90": [
          0.076,
          0.149
        ],
        "p_mean_le_0": 0.0,
        "n": 2680
      }
    },
    "cuts": {
      "1.0": {
        "n": 1144,
        "wrTP1": 37.3,
        "nSL": 638,
        "nTO": 79,
        "expR": 0.168,
        "pf": 1.28,
        "mfe_p25": 19.0,
        "mfe_p50": 40.5,
        "mfe_p75": 90.0,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 58.2000000000001,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 46.6,
        "ci90": {
          "expR": 0.168,
          "ci90": [
            0.09,
            0.245
          ],
          "p_mean_le_0": 0.0,
          "n": 1078
        }
      },
      "1.2": {
        "n": 930,
        "wrTP1": 35.1,
        "nSL": 532,
        "nTO": 72,
        "expR": 0.191,
        "pf": 1.31,
        "mfe_p25": 18.0,
        "mfe_p50": 41.0,
        "mfe_p75": 90.0,
        "winnerMAE_p75": 19.75,
        "winnerMAE_p90": 42.5,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 44.0,
        "ci90": {
          "expR": 0.191,
          "ci90": [
            0.105,
            0.284
          ],
          "p_mean_le_0": 0.0,
          "n": 871
        }
      },
      "1.3": {
        "n": 839,
        "wrTP1": 32.2,
        "nSL": 502,
        "nTO": 67,
        "expR": 0.155,
        "pf": 1.24,
        "mfe_p25": 19.0,
        "mfe_p50": 41.0,
        "mfe_p75": 91.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 39.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 43.2,
        "ci90": {
          "expR": 0.155,
          "ci90": [
            0.062,
            0.252
          ],
          "p_mean_le_0": 0.006,
          "n": 785
        }
      },
      "1.5": {
        "n": 688,
        "wrTP1": 30.8,
        "nSL": 423,
        "nTO": 53,
        "expR": 0.176,
        "pf": 1.27,
        "mfe_p25": 20.0,
        "mfe_p50": 41.0,
        "mfe_p75": 92.0,
        "winnerMAE_p75": 18.25,
        "winnerMAE_p90": 37.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 42.1,
        "ci90": {
          "expR": 0.176,
          "ci90": [
            0.06,
            0.296
          ],
          "p_mean_le_0": 0.003,
          "n": 647
        }
      },
      "2.0": {
        "n": 437,
        "wrTP1": 24.9,
        "nSL": 290,
        "nTO": 38,
        "expR": 0.131,
        "pf": 1.19,
        "mfe_p25": 20.0,
        "mfe_p50": 44.0,
        "mfe_p75": 99.75,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 34.400000000000006,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 34.1,
        "ci90": {
          "expR": 0.131,
          "ci90": [
            -0.018,
            0.286
          ],
          "p_mean_le_0": 0.077,
          "n": 410
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 1892,
      "wrTP1": 51.7,
      "nSL": 807,
      "nTO": 107,
      "expR": 0.075,
      "pf": 1.17,
      "mfe_p25": 16.0,
      "mfe_p50": 36.0,
      "mfe_p75": 78.0,
      "winnerMAE_p75": 26.75,
      "winnerMAE_p90": 66.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -37.0,
      "revAfterSL_rate": 47.8,
      "ci90": {
        "expR": 0.075,
        "ci90": [
          0.032,
          0.12
        ],
        "p_mean_le_0": 0.001,
        "n": 1797
      }
    },
    "cuts": {
      "1.0": {
        "n": 790,
        "wrTP1": 32.4,
        "nSL": 469,
        "nTO": 65,
        "expR": 0.041,
        "pf": 1.07,
        "mfe_p25": 21.0,
        "mfe_p50": 45.0,
        "mfe_p75": 95.25,
        "winnerMAE_p75": 23.25,
        "winnerMAE_p90": 51.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.0,
        "revAfterSL_rate": 40.9,
        "ci90": {
          "expR": 0.041,
          "ci90": [
            -0.044,
            0.132
          ],
          "p_mean_le_0": 0.224,
          "n": 736
        }
      },
      "1.2": {
        "n": 631,
        "wrTP1": 28.1,
        "nSL": 398,
        "nTO": 56,
        "expR": 0.01,
        "pf": 1.02,
        "mfe_p25": 22.0,
        "mfe_p50": 46.0,
        "mfe_p75": 101.0,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 49.80000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -34.0,
        "revAfterSL_rate": 37.2,
        "ci90": {
          "expR": 0.01,
          "ci90": [
            -0.099,
            0.127
          ],
          "p_mean_le_0": 0.444,
          "n": 585
        }
      },
      "1.3": {
        "n": 580,
        "wrTP1": 26.9,
        "nSL": 372,
        "nTO": 52,
        "expR": -0.004,
        "pf": 0.99,
        "mfe_p25": 23.25,
        "mfe_p50": 48.0,
        "mfe_p75": 104.5,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 53.5,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -34.0,
        "revAfterSL_rate": 36.8,
        "ci90": {
          "expR": -0.004,
          "ci90": [
            -0.114,
            0.113
          ],
          "p_mean_le_0": 0.529,
          "n": 538
        }
      },
      "1.5": {
        "n": 479,
        "wrTP1": 25.9,
        "nSL": 307,
        "nTO": 48,
        "expR": 0.026,
        "pf": 1.04,
        "mfe_p25": 24.0,
        "mfe_p50": 51.0,
        "mfe_p75": 109.0,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 48.7,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.0,
        "revAfterSL_rate": 32.6,
        "ci90": {
          "expR": 0.026,
          "ci90": [
            -0.099,
            0.16
          ],
          "p_mean_le_0": 0.372,
          "n": 441
        }
      },
      "2.0": {
        "n": 317,
        "wrTP1": 19.9,
        "nSL": 221,
        "nTO": 33,
        "expR": -0.046,
        "pf": 0.94,
        "mfe_p25": 26.0,
        "mfe_p50": 53.0,
        "mfe_p75": 110.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 44.0,
        "loserMFEbeforeSL_p50": 14.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -34.0,
        "revAfterSL_rate": 27.6,
        "ci90": {
          "expR": -0.046,
          "ci90": [
            -0.215,
            0.123
          ],
          "p_mean_le_0": 0.675,
          "n": 293
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
      "n": 3721,
      "wrTP1": 45.1,
      "nSL": 1810,
      "nTO": 231,
      "expR": -0.001,
      "pf": 1.0,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 31.0,
      "winnerMAE_p75": 9.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 29.6,
      "ci90": {
        "expR": -0.001,
        "ci90": [
          -0.032,
          0.032
        ],
        "p_mean_le_0": 0.534,
        "n": 3623
      }
    },
    "cuts": {
      "1.2": {
        "n": 1403,
        "wrTP1": 27.1,
        "nSL": 871,
        "nTO": 152,
        "expR": 0.022,
        "pf": 1.03,
        "mfe_p25": 10.0,
        "mfe_p50": 22.5,
        "mfe_p75": 39.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 19.7,
        "ci90": {
          "expR": 0.022,
          "ci90": [
            -0.045,
            0.09
          ],
          "p_mean_le_0": 0.302,
          "n": 1362
        }
      },
      "1.3": {
        "n": 1284,
        "wrTP1": 25.5,
        "nSL": 809,
        "nTO": 147,
        "expR": 0.018,
        "pf": 1.03,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 39.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.30000000000001,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 18.9,
        "ci90": {
          "expR": 0.018,
          "ci90": [
            -0.054,
            0.088
          ],
          "p_mean_le_0": 0.353,
          "n": 1246
        }
      },
      "1.5": {
        "n": 1093,
        "wrTP1": 22.6,
        "nSL": 708,
        "nTO": 138,
        "expR": -0.001,
        "pf": 1.0,
        "mfe_p25": 10.0,
        "mfe_p50": 23.0,
        "mfe_p75": 39.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.2,
        "ci90": {
          "expR": -0.001,
          "ci90": [
            -0.081,
            0.082
          ],
          "p_mean_le_0": 0.52,
          "n": 1062
        }
      },
      "2.0": {
        "n": 736,
        "wrTP1": 17.4,
        "nSL": 499,
        "nTO": 109,
        "expR": -0.018,
        "pf": 0.97,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 12.299999999999997,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 11.0,
        "ci90": {
          "expR": -0.018,
          "ci90": [
            -0.12,
            0.087
          ],
          "p_mean_le_0": 0.624,
          "n": 713
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 2807,
      "wrTP1": 47.3,
      "nSL": 1348,
      "nTO": 130,
      "expR": 0.007,
      "pf": 1.01,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 31.4,
      "ci90": {
        "expR": 0.007,
        "ci90": [
          -0.027,
          0.042
        ],
        "p_mean_le_0": 0.368,
        "n": 2743
      }
    },
    "cuts": {
      "1.2": {
        "n": 1011,
        "wrTP1": 28.1,
        "nSL": 639,
        "nTO": 88,
        "expR": -0.006,
        "pf": 0.99,
        "mfe_p25": 13.0,
        "mfe_p50": 29.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 26.700000000000017,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 20.0,
        "ci90": {
          "expR": -0.006,
          "ci90": [
            -0.081,
            0.072
          ],
          "p_mean_le_0": 0.563,
          "n": 979
        }
      },
      "1.3": {
        "n": 921,
        "wrTP1": 26.6,
        "nSL": 591,
        "nTO": 85,
        "expR": -0.011,
        "pf": 0.98,
        "mfe_p25": 13.0,
        "mfe_p50": 29.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 25.599999999999994,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.1,
        "ci90": {
          "expR": -0.011,
          "ci90": [
            -0.094,
            0.071
          ],
          "p_mean_le_0": 0.599,
          "n": 891
        }
      },
      "1.5": {
        "n": 754,
        "wrTP1": 23.5,
        "nSL": 494,
        "nTO": 83,
        "expR": -0.015,
        "pf": 0.98,
        "mfe_p25": 15.0,
        "mfe_p50": 31.0,
        "mfe_p75": 66.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.400000000000006,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.5,
        "revAfterSL_rate": 16.8,
        "ci90": {
          "expR": -0.015,
          "ci90": [
            -0.106,
            0.082
          ],
          "p_mean_le_0": 0.602,
          "n": 725
        }
      },
      "2.0": {
        "n": 489,
        "wrTP1": 17.8,
        "nSL": 333,
        "nTO": 69,
        "expR": -0.015,
        "pf": 0.98,
        "mfe_p25": 17.0,
        "mfe_p50": 35.0,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 11.1,
        "ci90": {
          "expR": -0.015,
          "ci90": [
            -0.148,
            0.118
          ],
          "p_mean_le_0": 0.58,
          "n": 464
        }
      }
    }
  },
  "15/RETEST/LONG": {
    "baseline": {
      "n": 193,
      "wrTP1": 53.4,
      "nSL": 90,
      "nTO": 0,
      "expR": 0.082,
      "pf": 1.18,
      "mfe_p25": 29.0,
      "mfe_p50": 68.0,
      "mfe_p75": 237.0,
      "winnerMAE_p75": 57.5,
      "winnerMAE_p90": 377.3999999999999,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -72.0,
      "revAfterSL_rate": 60.0,
      "ci90": {
        "expR": 0.082,
        "ci90": [
          -0.055,
          0.218
        ],
        "p_mean_le_0": 0.172,
        "n": 193
      }
    },
    "cuts": {
      "1.2": {
        "n": 47,
        "wrTP1": 31.9,
        "nSL": 32,
        "nTO": 0,
        "expR": -0.002,
        "pf": 1.0,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 161.0,
        "winnerMAE_p75": 57.5,
        "winnerMAE_p90": 482.9999999999998,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -53.0,
        "revAfterSL_rate": 81.2,
        "ci90": {
          "expR": -0.002,
          "ci90": [
            -0.355,
            0.36
          ],
          "p_mean_le_0": 0.515,
          "n": 47
        }
      },
      "1.3": {
        "n": 42,
        "wrTP1": 31.0,
        "nSL": 29,
        "nTO": 0,
        "expR": -0.03,
        "pf": 0.96,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 171.5,
        "winnerMAE_p75": 56.0,
        "winnerMAE_p90": 606.0000000000005,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -56.5,
        "revAfterSL_rate": 82.8,
        "ci90": {
          "expR": -0.03,
          "ci90": [
            -0.403,
            0.35
          ],
          "p_mean_le_0": 0.577,
          "n": 42
        }
      },
      "1.5": {
        "n": 29,
        "wrTP1": 34.5,
        "nSL": 19,
        "nTO": 0,
        "expR": 0.122,
        "pf": 1.19,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 257.0,
        "winnerMAE_p75": 99.5,
        "winnerMAE_p90": 1723.1999999999966,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -52.0,
        "revAfterSL_rate": 84.2,
        "ci90": {
          "expR": 0.122,
          "ci90": [
            -0.343,
            0.632
          ],
          "p_mean_le_0": 0.358,
          "n": 29
        }
      }
    }
  },
  "15/RETEST/SHORT": {
    "baseline": {
      "n": 231,
      "wrTP1": 52.8,
      "nSL": 109,
      "nTO": 0,
      "expR": 0.078,
      "pf": 1.17,
      "mfe_p25": 33.5,
      "mfe_p50": 128.0,
      "mfe_p75": 1697.0,
      "winnerMAE_p75": 451.5,
      "winnerMAE_p90": 4058.5000000000014,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -247.0,
      "revAfterSL_rate": 68.8,
      "ci90": {
        "expR": 0.078,
        "ci90": [
          -0.05,
          0.209
        ],
        "p_mean_le_0": 0.172,
        "n": 231
      }
    },
    "cuts": {
      "1.2": {
        "n": 62,
        "wrTP1": 40.3,
        "nSL": 37,
        "nTO": 0,
        "expR": 0.319,
        "pf": 1.53,
        "mfe_p25": 66.0,
        "mfe_p50": 182.5,
        "mfe_p75": 7566.0,
        "winnerMAE_p75": 2544.0,
        "winnerMAE_p90": 3694.6000000000004,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -326.0,
        "revAfterSL_rate": 54.1,
        "ci90": {
          "expR": 0.319,
          "ci90": [
            -0.045,
            0.667
          ],
          "p_mean_le_0": 0.07,
          "n": 62
        }
      },
      "1.3": {
        "n": 58,
        "wrTP1": 39.7,
        "nSL": 35,
        "nTO": 0,
        "expR": 0.297,
        "pf": 1.49,
        "mfe_p25": 66.0,
        "mfe_p50": 162.5,
        "mfe_p75": 7566.0,
        "winnerMAE_p75": 2460.0,
        "winnerMAE_p90": 3440.6000000000004,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -362.0,
        "revAfterSL_rate": 54.3,
        "ci90": {
          "expR": 0.297,
          "ci90": [
            -0.052,
            0.674
          ],
          "p_mean_le_0": 0.084,
          "n": 58
        }
      },
      "1.5": {
        "n": 45,
        "wrTP1": 33.3,
        "nSL": 30,
        "nTO": 0,
        "expR": 0.205,
        "pf": 1.31,
        "mfe_p25": 75.0,
        "mfe_p50": 228.0,
        "mfe_p75": 8134.0,
        "winnerMAE_p75": 2460.0,
        "winnerMAE_p90": 2740.6,
        "loserMFEbeforeSL_p50": 3.5,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -465.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.205,
          "ci90": [
            -0.212,
            0.666
          ],
          "p_mean_le_0": 0.234,
          "n": 45
        }
      },
      "2.0": {
        "n": 29,
        "wrTP1": 27.6,
        "nSL": 21,
        "nTO": 0,
        "expR": 0.107,
        "pf": 1.15,
        "mfe_p25": 74.0,
        "mfe_p50": 272.0,
        "mfe_p75": 16232.0,
        "winnerMAE_p75": 2445.25,
        "winnerMAE_p90": 3000.7,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 1.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -516.0,
        "revAfterSL_rate": 42.9,
        "ci90": {
          "expR": 0.107,
          "ci90": [
            -0.443,
            0.776
          ],
          "p_mean_le_0": 0.374,
          "n": 29
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 1650,
      "wrTP1": 47.4,
      "nSL": 818,
      "nTO": 50,
      "expR": -0.02,
      "pf": 0.96,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 41.2,
      "ci90": {
        "expR": -0.02,
        "ci90": [
          -0.066,
          0.026
        ],
        "p_mean_le_0": 0.756,
        "n": 1628
      }
    },
    "cuts": {
      "1.2": {
        "n": 608,
        "wrTP1": 27.5,
        "nSL": 409,
        "nTO": 32,
        "expR": -0.064,
        "pf": 0.91,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.400000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 35.5,
        "ci90": {
          "expR": -0.064,
          "ci90": [
            -0.163,
            0.045
          ],
          "p_mean_le_0": 0.844,
          "n": 597
        }
      },
      "1.3": {
        "n": 536,
        "wrTP1": 26.1,
        "nSL": 366,
        "nTO": 30,
        "expR": -0.057,
        "pf": 0.92,
        "mfe_p25": 13.0,
        "mfe_p50": 29.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 21.10000000000001,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 35.0,
        "ci90": {
          "expR": -0.057,
          "ci90": [
            -0.164,
            0.054
          ],
          "p_mean_le_0": 0.808,
          "n": 526
        }
      },
      "1.5": {
        "n": 444,
        "wrTP1": 24.1,
        "nSL": 310,
        "nTO": 27,
        "expR": -0.055,
        "pf": 0.92,
        "mfe_p25": 13.0,
        "mfe_p50": 29.0,
        "mfe_p75": 52.5,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 21.400000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 31.9,
        "ci90": {
          "expR": -0.055,
          "ci90": [
            -0.175,
            0.068
          ],
          "p_mean_le_0": 0.767,
          "n": 435
        }
      },
      "2.0": {
        "n": 282,
        "wrTP1": 17.0,
        "nSL": 210,
        "nTO": 24,
        "expR": -0.109,
        "pf": 0.86,
        "mfe_p25": 14.0,
        "mfe_p50": 30.0,
        "mfe_p75": 54.5,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 24.60000000000005,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 21.9,
        "ci90": {
          "expR": -0.109,
          "ci90": [
            -0.275,
            0.076
          ],
          "p_mean_le_0": 0.838,
          "n": 275
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 1278,
      "wrTP1": 50.0,
      "nSL": 609,
      "nTO": 30,
      "expR": 0.024,
      "pf": 1.05,
      "mfe_p25": 12.0,
      "mfe_p50": 25.0,
      "mfe_p75": 57.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 38.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -21.0,
      "revAfterSL_rate": 41.2,
      "ci90": {
        "expR": 0.024,
        "ci90": [
          -0.028,
          0.077
        ],
        "p_mean_le_0": 0.235,
        "n": 1258
      }
    },
    "cuts": {
      "1.2": {
        "n": 428,
        "wrTP1": 30.1,
        "nSL": 280,
        "nTO": 19,
        "expR": -0.027,
        "pf": 0.96,
        "mfe_p25": 19.0,
        "mfe_p50": 40.5,
        "mfe_p75": 80.75,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 34.2,
        "loserMFEbeforeSL_p50": 12.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -20.0,
        "revAfterSL_rate": 29.6,
        "ci90": {
          "expR": -0.027,
          "ci90": [
            -0.152,
            0.096
          ],
          "p_mean_le_0": 0.67,
          "n": 418
        }
      },
      "1.3": {
        "n": 376,
        "wrTP1": 28.5,
        "nSL": 251,
        "nTO": 18,
        "expR": -0.034,
        "pf": 0.95,
        "mfe_p25": 20.0,
        "mfe_p50": 42.5,
        "mfe_p75": 83.75,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 34.400000000000006,
        "loserMFEbeforeSL_p50": 14.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 27.9,
        "ci90": {
          "expR": -0.034,
          "ci90": [
            -0.165,
            0.101
          ],
          "p_mean_le_0": 0.662,
          "n": 366
        }
      },
      "1.5": {
        "n": 302,
        "wrTP1": 25.8,
        "nSL": 210,
        "nTO": 14,
        "expR": -0.046,
        "pf": 0.94,
        "mfe_p25": 20.0,
        "mfe_p50": 43.0,
        "mfe_p75": 86.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 35.89999999999999,
        "loserMFEbeforeSL_p50": 15.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 25.2,
        "ci90": {
          "expR": -0.046,
          "ci90": [
            -0.202,
            0.115
          ],
          "p_mean_le_0": 0.684,
          "n": 295
        }
      },
      "2.0": {
        "n": 187,
        "wrTP1": 20.9,
        "nSL": 137,
        "nTO": 11,
        "expR": -0.055,
        "pf": 0.93,
        "mfe_p25": 21.5,
        "mfe_p50": 42.0,
        "mfe_p75": 94.0,
        "winnerMAE_p75": 11.5,
        "winnerMAE_p90": 27.600000000000037,
        "loserMFEbeforeSL_p50": 15.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -22.0,
        "revAfterSL_rate": 19.0,
        "ci90": {
          "expR": -0.055,
          "ci90": [
            -0.27,
            0.187
          ],
          "p_mean_le_0": 0.653,
          "n": 183
        }
      }
    }
  },
  "29/RETEST/LONG": {
    "baseline": {
      "n": 76,
      "wrTP1": 61.8,
      "nSL": 29,
      "nTO": 0,
      "expR": 0.242,
      "pf": 1.63,
      "mfe_p25": 45.5,
      "mfe_p50": 113.5,
      "mfe_p75": 1455.5,
      "winnerMAE_p75": 399.0,
      "winnerMAE_p90": 8496.399999999994,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -74.0,
      "revAfterSL_rate": 65.5,
      "ci90": {
        "expR": 0.242,
        "ci90": [
          0.033,
          0.462
        ],
        "p_mean_le_0": 0.03,
        "n": 76
      }
    },
    "cuts": {
      "1.2": {
        "n": 20,
        "wrTP1": 40.0,
        "nSL": 12,
        "nTO": 0,
        "expR": 0.202,
        "pf": 1.34,
        "mfe_p25": 44.5,
        "mfe_p50": 73.0,
        "mfe_p75": 142.5,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 1103.3999999999994,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 75.0,
        "ci90": {
          "expR": 0.202,
          "ci90": [
            -0.37,
            0.768
          ],
          "p_mean_le_0": 0.284,
          "n": 20
        }
      }
    }
  },
  "29/RETEST/SHORT": {
    "baseline": {
      "n": 148,
      "wrTP1": 58.8,
      "nSL": 61,
      "nTO": 0,
      "expR": 0.19,
      "pf": 1.46,
      "mfe_p25": 30.0,
      "mfe_p50": 120.0,
      "mfe_p75": 652.75,
      "winnerMAE_p75": 195.5,
      "winnerMAE_p90": 1691.4000000000076,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -202.0,
      "revAfterSL_rate": 70.5,
      "ci90": {
        "expR": 0.19,
        "ci90": [
          0.037,
          0.34
        ],
        "p_mean_le_0": 0.019,
        "n": 148
      }
    },
    "cuts": {
      "1.2": {
        "n": 37,
        "wrTP1": 35.1,
        "nSL": 24,
        "nTO": 0,
        "expR": 0.154,
        "pf": 1.24,
        "mfe_p25": 47.0,
        "mfe_p50": 148.0,
        "mfe_p75": 1211.0,
        "winnerMAE_p75": 403.0,
        "winnerMAE_p90": 2221.800000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -281.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.154,
          "ci90": [
            -0.281,
            0.615
          ],
          "p_mean_le_0": 0.284,
          "n": 37
        }
      },
      "1.3": {
        "n": 34,
        "wrTP1": 32.4,
        "nSL": 23,
        "nTO": 0,
        "expR": 0.125,
        "pf": 1.19,
        "mfe_p25": 92.0,
        "mfe_p50": 178.0,
        "mfe_p75": 1229.75,
        "winnerMAE_p75": 782.0,
        "winnerMAE_p90": 2487.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -281.0,
        "revAfterSL_rate": 52.2,
        "ci90": {
          "expR": 0.125,
          "ci90": [
            -0.31,
            0.597
          ],
          "p_mean_le_0": 0.366,
          "n": 34
        }
      },
      "1.5": {
        "n": 26,
        "wrTP1": 34.6,
        "nSL": 17,
        "nTO": 0,
        "expR": 0.243,
        "pf": 1.37,
        "mfe_p25": 92.0,
        "mfe_p50": 130.5,
        "mfe_p75": 817.0,
        "winnerMAE_p75": 292.0,
        "winnerMAE_p90": 554.6000000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -218.0,
        "revAfterSL_rate": 41.2,
        "ci90": {
          "expR": 0.243,
          "ci90": [
            -0.313,
            0.788
          ],
          "p_mean_le_0": 0.271,
          "n": 26
        }
      }
    }
  },
  "3/RETEST/LONG": {
    "baseline": {
      "n": 633,
      "wrTP1": 56.1,
      "nSL": 272,
      "nTO": 6,
      "expR": 0.135,
      "pf": 1.31,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 50.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 32.60000000000002,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 56.6,
      "ci90": {
        "expR": 0.135,
        "ci90": [
          0.061,
          0.212
        ],
        "p_mean_le_0": 0.001,
        "n": 629
      }
    },
    "cuts": {
      "1.2": {
        "n": 165,
        "wrTP1": 39.4,
        "nSL": 98,
        "nTO": 2,
        "expR": 0.209,
        "pf": 1.35,
        "mfe_p25": 20.0,
        "mfe_p50": 38.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 38.400000000000006,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 52.0,
        "ci90": {
          "expR": 0.209,
          "ci90": [
            0.012,
            0.408
          ],
          "p_mean_le_0": 0.042,
          "n": 165
        }
      },
      "1.3": {
        "n": 142,
        "wrTP1": 39.4,
        "nSL": 84,
        "nTO": 2,
        "expR": 0.245,
        "pf": 1.41,
        "mfe_p25": 24.25,
        "mfe_p50": 40.0,
        "mfe_p75": 84.5,
        "winnerMAE_p75": 14.25,
        "winnerMAE_p90": 42.5,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.245,
          "ci90": [
            0.027,
            0.462
          ],
          "p_mean_le_0": 0.029,
          "n": 142
        }
      },
      "1.5": {
        "n": 106,
        "wrTP1": 39.6,
        "nSL": 62,
        "nTO": 2,
        "expR": 0.337,
        "pf": 1.58,
        "mfe_p25": 25.25,
        "mfe_p50": 43.5,
        "mfe_p75": 85.0,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 48.999999999999986,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -15.5,
        "revAfterSL_rate": 41.9,
        "ci90": {
          "expR": 0.337,
          "ci90": [
            0.07,
            0.614
          ],
          "p_mean_le_0": 0.02,
          "n": 106
        }
      },
      "2.0": {
        "n": 60,
        "wrTP1": 33.3,
        "nSL": 38,
        "nTO": 2,
        "expR": 0.339,
        "pf": 1.54,
        "mfe_p25": 31.0,
        "mfe_p50": 48.0,
        "mfe_p75": 88.25,
        "winnerMAE_p75": 11.25,
        "winnerMAE_p90": 29.300000000000033,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 39.5,
        "ci90": {
          "expR": 0.339,
          "ci90": [
            -0.036,
            0.728
          ],
          "p_mean_le_0": 0.07,
          "n": 60
        }
      }
    }
  },
  "3/RETEST/SHORT": {
    "baseline": {
      "n": 616,
      "wrTP1": 55.4,
      "nSL": 266,
      "nTO": 9,
      "expR": 0.135,
      "pf": 1.31,
      "mfe_p25": 11.75,
      "mfe_p50": 22.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 35.0,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -22.0,
      "revAfterSL_rate": 57.1,
      "ci90": {
        "expR": 0.135,
        "ci90": [
          0.061,
          0.208
        ],
        "p_mean_le_0": 0.001,
        "n": 612
      }
    },
    "cuts": {
      "1.2": {
        "n": 163,
        "wrTP1": 36.2,
        "nSL": 96,
        "nTO": 8,
        "expR": 0.212,
        "pf": 1.35,
        "mfe_p25": 16.75,
        "mfe_p50": 29.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 51.0,
        "ci90": {
          "expR": 0.212,
          "ci90": [
            0.005,
            0.414
          ],
          "p_mean_le_0": 0.045,
          "n": 160
        }
      },
      "1.3": {
        "n": 141,
        "wrTP1": 36.2,
        "nSL": 82,
        "nTO": 8,
        "expR": 0.262,
        "pf": 1.44,
        "mfe_p25": 17.25,
        "mfe_p50": 29.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 13.5,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 1.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -22.0,
        "revAfterSL_rate": 46.3,
        "ci90": {
          "expR": 0.262,
          "ci90": [
            0.037,
            0.495
          ],
          "p_mean_le_0": 0.025,
          "n": 138
        }
      },
      "1.5": {
        "n": 117,
        "wrTP1": 31.6,
        "nSL": 73,
        "nTO": 7,
        "expR": 0.2,
        "pf": 1.31,
        "mfe_p25": 17.5,
        "mfe_p50": 30.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 41.1,
        "ci90": {
          "expR": 0.2,
          "ci90": [
            -0.066,
            0.464
          ],
          "p_mean_le_0": 0.103,
          "n": 115
        }
      },
      "2.0": {
        "n": 62,
        "wrTP1": 32.3,
        "nSL": 37,
        "nTO": 5,
        "expR": 0.421,
        "pf": 1.69,
        "mfe_p25": 19.0,
        "mfe_p50": 33.0,
        "mfe_p75": 69.0,
        "winnerMAE_p75": 13.25,
        "winnerMAE_p90": 22.70000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.5,
        "revAfterSL_rate": 21.6,
        "ci90": {
          "expR": 0.421,
          "ci90": [
            0.025,
            0.844
          ],
          "p_mean_le_0": 0.042,
          "n": 61
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 825,
      "wrTP1": 52.6,
      "nSL": 368,
      "nTO": 23,
      "expR": 0.049,
      "pf": 1.11,
      "mfe_p25": 18.0,
      "mfe_p50": 41.0,
      "mfe_p75": 257.5,
      "winnerMAE_p75": 76.75,
      "winnerMAE_p90": 1286.699999999998,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -51.0,
      "revAfterSL_rate": 46.2,
      "ci90": {
        "expR": 0.049,
        "ci90": [
          -0.014,
          0.114
        ],
        "p_mean_le_0": 0.098,
        "n": 806
      }
    },
    "cuts": {
      "1.2": {
        "n": 251,
        "wrTP1": 31.5,
        "nSL": 158,
        "nTO": 14,
        "expR": -0.018,
        "pf": 0.97,
        "mfe_p25": 21.0,
        "mfe_p50": 49.0,
        "mfe_p75": 189.75,
        "winnerMAE_p75": 57.5,
        "winnerMAE_p90": 728.4000000000003,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.0,
        "revAfterSL_rate": 36.7,
        "ci90": {
          "expR": -0.018,
          "ci90": [
            -0.166,
            0.144
          ],
          "p_mean_le_0": 0.597,
          "n": 240
        }
      },
      "1.3": {
        "n": 224,
        "wrTP1": 27.7,
        "nSL": 148,
        "nTO": 14,
        "expR": -0.075,
        "pf": 0.89,
        "mfe_p25": 23.0,
        "mfe_p50": 53.0,
        "mfe_p75": 189.0,
        "winnerMAE_p75": 46.0,
        "winnerMAE_p90": 378.09999999999985,
        "loserMFEbeforeSL_p50": 3.5,
        "bars_win_p50": 2.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -34.5,
        "revAfterSL_rate": 37.2,
        "ci90": {
          "expR": -0.075,
          "ci90": [
            -0.241,
            0.092
          ],
          "p_mean_le_0": 0.774,
          "n": 213
        }
      },
      "1.5": {
        "n": 176,
        "wrTP1": 27.3,
        "nSL": 118,
        "nTO": 10,
        "expR": -0.044,
        "pf": 0.94,
        "mfe_p25": 23.0,
        "mfe_p50": 53.0,
        "mfe_p75": 189.0,
        "winnerMAE_p75": 40.75,
        "winnerMAE_p90": 517.5000000000018,
        "loserMFEbeforeSL_p50": 5.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 34.7,
        "ci90": {
          "expR": -0.044,
          "ci90": [
            -0.242,
            0.153
          ],
          "p_mean_le_0": 0.647,
          "n": 169
        }
      },
      "2.0": {
        "n": 101,
        "wrTP1": 19.8,
        "nSL": 76,
        "nTO": 5,
        "expR": -0.194,
        "pf": 0.75,
        "mfe_p25": 23.5,
        "mfe_p50": 53.5,
        "mfe_p75": 182.5,
        "winnerMAE_p75": 139.75,
        "winnerMAE_p90": 1595.6000000000006,
        "loserMFEbeforeSL_p50": 13.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 23.7,
        "ci90": {
          "expR": -0.194,
          "ci90": [
            -0.452,
            0.073
          ],
          "p_mean_le_0": 0.888,
          "n": 98
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 686,
      "wrTP1": 53.8,
      "nSL": 299,
      "nTO": 18,
      "expR": 0.063,
      "pf": 1.14,
      "mfe_p25": 18.0,
      "mfe_p50": 44.0,
      "mfe_p75": 231.0,
      "winnerMAE_p75": 50.0,
      "winnerMAE_p90": 336.4,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -65.5,
      "revAfterSL_rate": 54.8,
      "ci90": {
        "expR": 0.063,
        "ci90": [
          -0.007,
          0.137
        ],
        "p_mean_le_0": 0.072,
        "n": 669
      }
    },
    "cuts": {
      "1.2": {
        "n": 213,
        "wrTP1": 25.8,
        "nSL": 147,
        "nTO": 11,
        "expR": -0.132,
        "pf": 0.82,
        "mfe_p25": 25.0,
        "mfe_p50": 61.0,
        "mfe_p75": 223.0,
        "winnerMAE_p75": 37.0,
        "winnerMAE_p90": 149.00000000000006,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -55.0,
        "revAfterSL_rate": 43.5,
        "ci90": {
          "expR": -0.132,
          "ci90": [
            -0.303,
            0.048
          ],
          "p_mean_le_0": 0.897,
          "n": 203
        }
      },
      "1.3": {
        "n": 195,
        "wrTP1": 23.1,
        "nSL": 139,
        "nTO": 11,
        "expR": -0.182,
        "pf": 0.76,
        "mfe_p25": 24.0,
        "mfe_p50": 61.0,
        "mfe_p75": 247.0,
        "winnerMAE_p75": 44.0,
        "winnerMAE_p90": 149.00000000000006,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -55.0,
        "revAfterSL_rate": 43.2,
        "ci90": {
          "expR": -0.182,
          "ci90": [
            -0.361,
            -0.001
          ],
          "p_mean_le_0": 0.952,
          "n": 185
        }
      },
      "1.5": {
        "n": 165,
        "wrTP1": 23.0,
        "nSL": 118,
        "nTO": 9,
        "expR": -0.157,
        "pf": 0.79,
        "mfe_p25": 24.0,
        "mfe_p50": 60.0,
        "mfe_p75": 193.0,
        "winnerMAE_p75": 29.0,
        "winnerMAE_p90": 477.60000000000446,
        "loserMFEbeforeSL_p50": 10.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -53.0,
        "revAfterSL_rate": 39.0,
        "ci90": {
          "expR": -0.157,
          "ci90": [
            -0.346,
            0.054
          ],
          "p_mean_le_0": 0.88,
          "n": 157
        }
      },
      "2.0": {
        "n": 112,
        "wrTP1": 17.9,
        "nSL": 85,
        "nTO": 7,
        "expR": -0.243,
        "pf": 0.7,
        "mfe_p25": 27.25,
        "mfe_p50": 59.0,
        "mfe_p75": 161.5,
        "winnerMAE_p75": 18.5,
        "winnerMAE_p90": 160.30000000000166,
        "loserMFEbeforeSL_p50": 18.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -53.0,
        "revAfterSL_rate": 30.6,
        "ci90": {
          "expR": -0.243,
          "ci90": [
            -0.48,
            0.008
          ],
          "p_mean_le_0": 0.942,
          "n": 106
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
    "n": 8736,
    "wrTP1": 49.9,
    "expR": 0.033
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
      "n": 3,
      "wrTP1": 66.7,
      "expR": 0.18,
      "pf": 1.54
    },
    "15m/RETEST/LONG": {
      "n": 204,
      "wrTP1": 50.5,
      "expR": 0.031,
      "pf": 1.06
    },
    "15m/RETEST/SHORT": {
      "n": 234,
      "wrTP1": 52.1,
      "expR": 0.064,
      "pf": 1.13
    },
    "1m/INV/LONG": {
      "n": 42,
      "wrTP1": 59.5,
      "expR": 0.294,
      "pf": 1.93
    },
    "1m/INV/SHORT": {
      "n": 41,
      "wrTP1": 41.5,
      "expR": 0.057,
      "pf": 1.13
    },
    "1m/RETEST/LONG": {
      "n": 2187,
      "wrTP1": 47.1,
      "expR": 0.015,
      "pf": 1.03
    },
    "1m/RETEST/SHORT": {
      "n": 1691,
      "wrTP1": 47.6,
      "expR": -0.001,
      "pf": 1.0
    },
    "29m/RETEST/LONG": {
      "n": 82,
      "wrTP1": 57.3,
      "expR": 0.151,
      "pf": 1.35
    },
    "29m/RETEST/SHORT": {
      "n": 149,
      "wrTP1": 58.4,
      "expR": 0.182,
      "pf": 1.44
    },
    "2m/INV/LONG": {
      "n": 16,
      "wrTP1": 75.0,
      "expR": 0.192,
      "pf": 1.77
    },
    "2m/INV/SHORT": {
      "n": 18,
      "wrTP1": 66.7,
      "expR": 0.153,
      "pf": 1.51
    },
    "2m/RETEST/LONG": {
      "n": 945,
      "wrTP1": 48.5,
      "expR": -0.06,
      "pf": 0.88
    },
    "2m/RETEST/SHORT": {
      "n": 775,
      "wrTP1": 46.6,
      "expR": -0.021,
      "pf": 0.96
    },
    "3m/INV/LONG": {
      "n": 8,
      "wrTP1": 62.5,
      "expR": 0.02,
      "pf": 1.05
    },
    "3m/INV/SHORT": {
      "n": 4,
      "wrTP1": 100.0,
      "expR": 0.425,
      "pf": 99.0
    },
    "3m/RETEST/LONG": {
      "n": 642,
      "wrTP1": 55.3,
      "expR": 0.13,
      "pf": 1.3
    },
    "3m/RETEST/SHORT": {
      "n": 629,
      "wrTP1": 54.2,
      "expR": 0.119,
      "pf": 1.27
    },
    "5m/INV/LONG": {
      "n": 10,
      "wrTP1": 60.0,
      "expR": -0.15,
      "pf": 0.63
    },
    "5m/INV/SHORT": {
      "n": 7,
      "wrTP1": 28.6,
      "expR": 0.817,
      "pf": 2.91
    },
    "5m/RETEST/LONG": {
      "n": 562,
      "wrTP1": 53.4,
      "expR": 0.08,
      "pf": 1.18
    },
    "5m/RETEST/SHORT": {
      "n": 487,
      "wrTP1": 53.8,
      "expR": 0.078,
      "pf": 1.17
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 44843,
  "brier": 0.2215,
  "bias": -0.098,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.298
    },
    {
      "feature": "stretchAtr",
      "weight": -0.054
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.047
    },
    {
      "feature": "nearTk",
      "weight": -0.035
    },
    {
      "feature": "biasScore",
      "weight": -0.027
    },
    {
      "feature": "hourNY",
      "weight": 0.026
    },
    {
      "feature": "rvol",
      "weight": 0.02
    },
    {
      "feature": "emaStack",
      "weight": 0.019
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.015
    },
    {
      "feature": "chopIdx",
      "weight": -0.015
    },
    {
      "feature": "aligned",
      "weight": -0.013
    },
    {
      "feature": "structDir",
      "weight": -0.005
    },
    {
      "feature": "nearEdge",
      "weight": 0.002
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.169,
      "actual": 0.169,
      "n": 4484
    },
    {
      "bin": 1,
      "pred": 0.374,
      "actual": 0.31,
      "n": 4484
    },
    {
      "bin": 2,
      "pred": 0.451,
      "actual": 0.319,
      "n": 4484
    },
    {
      "bin": 3,
      "pred": 0.495,
      "actual": 0.426,
      "n": 4485
    },
    {
      "bin": 4,
      "pred": 0.531,
      "actual": 0.508,
      "n": 4484
    },
    {
      "bin": 5,
      "pred": 0.559,
      "actual": 0.562,
      "n": 4484
    },
    {
      "bin": 6,
      "pred": 0.58,
      "actual": 0.621,
      "n": 4485
    },
    {
      "bin": 7,
      "pred": 0.599,
      "actual": 0.643,
      "n": 4484
    },
    {
      "bin": 8,
      "pred": 0.617,
      "actual": 0.688,
      "n": 4484
    },
    {
      "bin": 9,
      "pred": 0.644,
      "actual": 0.753,
      "n": 4485
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
  "testN": 13447,
  "testWeeks": [
    "2026-W43",
    "2026-W44"
  ],
  "model_oos_brier": 0.2364,
  "model_oos_n": 13447,
  "best_scheme_in_sample": {
    "scheme": "fixed_2R",
    "trainExpR": 0.049
  },
  "best_scheme_oos_expR": 0.044
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "15m/RETEST/LONG": {
    "expR": 0.031,
    "ci90": [
      -0.097,
      0.167
    ],
    "p_mean_le_0": 0.35,
    "n": 204,
    "survives_fdr10": false
  },
  "15m/RETEST/SHORT": {
    "expR": 0.064,
    "ci90": [
      -0.054,
      0.196
    ],
    "p_mean_le_0": 0.211,
    "n": 234,
    "survives_fdr10": false
  },
  "1m/INV/LONG": {
    "expR": 0.138,
    "ci90": [
      0.042,
      0.248
    ],
    "p_mean_le_0": 0.011,
    "n": 426,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": 0.08,
    "ci90": [
      -0.026,
      0.181
    ],
    "p_mean_le_0": 0.11,
    "n": 300,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.027,
    "ci90": [
      0.012,
      0.043
    ],
    "p_mean_le_0": 0.002,
    "n": 16484,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.026,
    "ci90": [
      0.006,
      0.045
    ],
    "p_mean_le_0": 0.015,
    "n": 10428,
    "survives_fdr10": true
  },
  "29m/RETEST/LONG": {
    "expR": 0.151,
    "ci90": [
      -0.052,
      0.367
    ],
    "p_mean_le_0": 0.107,
    "n": 82,
    "survives_fdr10": false
  },
  "29m/RETEST/SHORT": {
    "expR": 0.182,
    "ci90": [
      0.033,
      0.332
    ],
    "p_mean_le_0": 0.021,
    "n": 149,
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
    "expR": 0.121,
    "ci90": [
      -0.067,
      0.327
    ],
    "p_mean_le_0": 0.16,
    "n": 115,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.032,
    "ci90": [
      0.008,
      0.054
    ],
    "p_mean_le_0": 0.011,
    "n": 7223,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.045,
    "ci90": [
      0.017,
      0.075
    ],
    "p_mean_le_0": 0.005,
    "n": 4593,
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
    "expR": 0.13,
    "ci90": [
      0.056,
      0.203
    ],
    "p_mean_le_0": 0.002,
    "n": 638,
    "survives_fdr10": true
  },
  "3m/RETEST/SHORT": {
    "expR": 0.119,
    "ci90": [
      0.044,
      0.192
    ],
    "p_mean_le_0": 0.003,
    "n": 625,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.154,
    "ci90": [
      -0.042,
      0.357
    ],
    "p_mean_le_0": 0.107,
    "n": 46,
    "survives_fdr10": false
  },
  "5m/INV/SHORT": {
    "expR": 0.287,
    "ci90": [
      -0.129,
      0.693
    ],
    "p_mean_le_0": 0.136,
    "n": 28,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.1,
    "ci90": [
      0.064,
      0.138
    ],
    "p_mean_le_0": 0.0,
    "n": 2783,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.067,
    "ci90": [
      0.02,
      0.115
    ],
    "p_mean_le_0": 0.008,
    "n": 1895,
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
      "n": 2431,
      "wrTP1": 54.0,
      "expR": 0.078,
      "pf": 1.17,
      "defining_features": {
        "aligned": -4.29,
        "atrPctUsed": -0.2,
        "rr1": -0.2,
        "rvol": -0.11
      }
    },
    {
      "id": 2,
      "n": 27246,
      "wrTP1": 46.5,
      "expR": 0.041,
      "pf": 1.08,
      "defining_features": {
        "biasScore": 0.74,
        "emaStack": 0.63,
        "nearEdge": 0.54,
        "structDir": 0.28
      }
    },
    {
      "id": 0,
      "n": 18260,
      "wrTP1": 45.9,
      "expR": 0.037,
      "pf": 1.08,
      "defining_features": {
        "biasScore": -1.11,
        "emaStack": -0.94,
        "nearEdge": -0.82,
        "structDir": -0.41
      }
    },
    {
      "id": 1,
      "n": 112,
      "wrTP1": 45.5,
      "expR": -0.027,
      "pf": 0.95,
      "defining_features": {
        "entryZoneTk": -15.54,
        "nearTk": 12.91,
        "aligned": -1.54,
        "atrPctUsed": 0.57
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
        "n": 30,
        "wrTP1": 56.7,
        "expR": 0.243
      },
      "NQ": {
        "n": 25,
        "wrTP1": 56.0,
        "expR": 0.112
      },
      "GC": {
        "n": 23,
        "wrTP1": 60.9,
        "expR": 0.348
      },
      "CL": {
        "n": 31,
        "wrTP1": 51.6,
        "expR": 0.012
      },
      "YM": {
        "n": 36,
        "wrTP1": 58.3,
        "expR": 0.256
      },
      "ETHUSDT": {
        "n": 29,
        "wrTP1": 51.7,
        "expR": -0.187
      },
      "BTCUSDT": {
        "n": 30,
        "wrTP1": 20.0,
        "expR": -0.528
      }
    },
    "expR_spread": 0.876,
    "verdict": "instrument-specific"
  },
  "15m/RETEST/SHORT": {
    "symbols": {
      "BTCUSDT": {
        "n": 54,
        "wrTP1": 59.3,
        "expR": 0.27
      },
      "ETHUSDT": {
        "n": 46,
        "wrTP1": 45.7,
        "expR": -0.194
      },
      "YM": {
        "n": 19,
        "wrTP1": 63.2,
        "expR": 0.281
      },
      "ES": {
        "n": 20,
        "wrTP1": 45.0,
        "expR": -0.238
      },
      "GC": {
        "n": 22,
        "wrTP1": 54.5,
        "expR": 0.177
      },
      "NQ": {
        "n": 33,
        "wrTP1": 48.5,
        "expR": 0.085
      },
      "CL": {
        "n": 40,
        "wrTP1": 50.0,
        "expR": 0.054
      }
    },
    "expR_spread": 0.519,
    "verdict": "instrument-specific"
  },
  "1m/INV/LONG": {
    "symbols": {
      "CL": {
        "n": 82,
        "wrTP1": 50.0,
        "expR": 0.333
      },
      "GC": {
        "n": 67,
        "wrTP1": 46.3,
        "expR": -0.031
      },
      "YM": {
        "n": 192,
        "wrTP1": 45.8,
        "expR": 0.163
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
    "expR_spread": 0.465,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "GC": {
        "n": 72,
        "wrTP1": 56.9,
        "expR": 0.18
      },
      "YM": {
        "n": 153,
        "wrTP1": 41.2,
        "expR": 0.067
      },
      "NQ": {
        "n": 36,
        "wrTP1": 61.1,
        "expR": 0.136
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
        "n": 3535,
        "wrTP1": 44.9,
        "expR": 0.036
      },
      "YM": {
        "n": 3884,
        "wrTP1": 45.8,
        "expR": 0.078
      }
    },
    "expR_spread": 0.077,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 1612,
        "wrTP1": 40.9,
        "expR": 0.018
      },
      "GC": {
        "n": 3209,
        "wrTP1": 46.6,
        "expR": 0.043
      },
      "YM": {
        "n": 2551,
        "wrTP1": 45.1,
        "expR": 0.045
      },
      "ES": {
        "n": 1946,
        "wrTP1": 46.1,
        "expR": 0.028
      },
      "CL": {
        "n": 1601,
        "wrTP1": 44.0,
        "expR": -0.035
      }
    },
    "expR_spread": 0.08,
    "verdict": "universal"
  },
  "29m/RETEST/LONG": {
    "symbols": {
      "YM": {
        "n": 14,
        "wrTP1": 50.0,
        "expR": 0.134
      },
      "NQ": {
        "n": 8,
        "wrTP1": 62.5,
        "expR": 0.48
      },
      "ES": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": -0.328
      },
      "CL": {
        "n": 19,
        "wrTP1": 52.6,
        "expR": 0.082
      },
      "BTCUSDT": {
        "n": 21,
        "wrTP1": 47.6,
        "expR": -0.159
      },
      "GC": {
        "n": 6,
        "wrTP1": 100.0,
        "expR": 0.997
      },
      "ETHUSDT": {
        "n": 10,
        "wrTP1": 70.0,
        "expR": 0.377
      }
    },
    "expR_spread": 1.325,
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
        "n": 20,
        "wrTP1": 50.0,
        "expR": -0.173
      },
      "YM": {
        "n": 18,
        "wrTP1": 66.7,
        "expR": 0.346
      },
      "NQ": {
        "n": 25,
        "wrTP1": 72.0,
        "expR": 0.586
      },
      "ETHUSDT": {
        "n": 32,
        "wrTP1": 56.2,
        "expR": 0.099
      },
      "GC": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.188
      },
      "BTCUSDT": {
        "n": 20,
        "wrTP1": 60.0,
        "expR": 0.271
      }
    },
    "expR_spread": 0.774,
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
        "n": 18,
        "wrTP1": 38.9,
        "expR": -0.301
      }
    },
    "expR_spread": 0.687,
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
        "n": 1578,
        "wrTP1": 48.7,
        "expR": 0.046
      },
      "ES": {
        "n": 1651,
        "wrTP1": 46.9,
        "expR": -0.017
      },
      "YM": {
        "n": 1603,
        "wrTP1": 48.8,
        "expR": 0.08
      }
    },
    "expR_spread": 0.097,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 866,
        "wrTP1": 48.4,
        "expR": 0.024
      },
      "YM": {
        "n": 1057,
        "wrTP1": 48.9,
        "expR": 0.099
      },
      "GC": {
        "n": 1335,
        "wrTP1": 48.9,
        "expR": 0.082
      },
      "NQ": {
        "n": 817,
        "wrTP1": 43.1,
        "expR": 0.0
      },
      "CL": {
        "n": 686,
        "wrTP1": 46.8,
        "expR": -0.025
      }
    },
    "expR_spread": 0.124,
    "verdict": "universal"
  },
  "3m/RETEST/LONG": {
    "symbols": {
      "YM": {
        "n": 143,
        "wrTP1": 55.9,
        "expR": 0.07
      },
      "ES": {
        "n": 164,
        "wrTP1": 52.4,
        "expR": 0.006
      },
      "NQ": {
        "n": 130,
        "wrTP1": 50.8,
        "expR": 0.024
      },
      "CL": {
        "n": 113,
        "wrTP1": 63.7,
        "expR": 0.406
      },
      "GC": {
        "n": 92,
        "wrTP1": 55.4,
        "expR": 0.252
      }
    },
    "expR_spread": 0.4,
    "verdict": "instrument-specific"
  },
  "3m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 126,
        "wrTP1": 53.2,
        "expR": 0.079
      },
      "ES": {
        "n": 110,
        "wrTP1": 51.8,
        "expR": -0.013
      },
      "GC": {
        "n": 126,
        "wrTP1": 54.8,
        "expR": 0.173
      },
      "CL": {
        "n": 154,
        "wrTP1": 56.5,
        "expR": 0.136
      },
      "YM": {
        "n": 113,
        "wrTP1": 54.0,
        "expR": 0.21
      }
    },
    "expR_spread": 0.223,
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
        "n": 12,
        "wrTP1": 83.3,
        "expR": 0.247
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
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.582
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
        "n": 572,
        "wrTP1": 51.4,
        "expR": 0.128
      },
      "CL": {
        "n": 556,
        "wrTP1": 55.2,
        "expR": 0.183
      },
      "NQ": {
        "n": 591,
        "wrTP1": 48.1,
        "expR": 0.03
      },
      "BTCUSDT": {
        "n": 138,
        "wrTP1": 50.7,
        "expR": 0.008
      },
      "ETHUSDT": {
        "n": 119,
        "wrTP1": 57.1,
        "expR": 0.141
      }
    },
    "expR_spread": 0.175,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 286,
        "wrTP1": 47.2,
        "expR": 0.046
      },
      "ES": {
        "n": 368,
        "wrTP1": 49.5,
        "expR": 0.139
      },
      "GC": {
        "n": 492,
        "wrTP1": 48.0,
        "expR": 0.025
      },
      "YM": {
        "n": 398,
        "wrTP1": 49.5,
        "expR": 0.126
      },
      "CL": {
        "n": 301,
        "wrTP1": 46.5,
        "expR": 0.028
      },
      "ETHUSDT": {
        "n": 72,
        "wrTP1": 62.5,
        "expR": 0.125
      },
      "BTCUSDT": {
        "n": 90,
        "wrTP1": 47.8,
        "expR": -0.086
      }
    },
    "expR_spread": 0.225,
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
    "n": 1018,
    "wrTP1": 50.0,
    "nSL": 485,
    "nTO": 24,
    "expR": 0.061,
    "pf": 1.13,
    "mfe_p25": 12.0,
    "mfe_p50": 32.0,
    "mfe_p75": 71.0,
    "winnerMAE_p75": 24.0,
    "winnerMAE_p90": 71.59999999999997,
    "loserMFEbeforeSL_p50": 3.0,
    "bars_win_p50": 1.0,
    "bars_loss_p50": 2.0,
    "entryZoneTk_p50": -19.0,
    "revAfterSL_rate": 47.8
  },
  "away_from_news": {
    "n": 47031,
    "wrTP1": 46.6,
    "nSL": 21938,
    "nTO": 3182,
    "expR": 0.04,
    "pf": 1.08,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 42.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 28.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 33.7
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 6,
  "mae_deltaER": 0.267,
  "hit_direction_rate": 0.0
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
    "afterN": 28573,
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
      "n": 28573,
      "wrTP1": 47.1,
      "nSL": 13540,
      "nTO": 1564,
      "expR": 0.031,
      "pf": 1.06,
      "mfe_p25": 9.0,
      "mfe_p50": 19.0,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 32.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 35.2
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
    "date": "2026-10-30",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-10-29T21:32:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "CL",
    "focus": {
      "sym": "CL",
      "verdict": "WAIT",
      "window": "17:00-00:00 CT",
      "setup": {
        "es": "pullback al cluster VAH/EMA50 101.9-102.3 para largo de continuacion",
        "en": "pullback to the VAH/EMA50 101.9-102.3 cluster for a long continuation"
      },
      "trigger": {
        "es": "reclamo con cierre 5m sobre 101.9 tras el pullback, o rechazo claro en el cluster",
        "en": "5m close reclaim above 101.9 after the pullback, or a clear rejection at the cluster"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 100.33",
        "en": "sustained 5m close below 100.33"
      },
      "note": {
        "es": "muy estirado (9.4 ATR): no se persigue el largo aqui, se espera el pullback",
        "en": "very stretched (9.4 ATR): don't chase the long here, wait for the pullback"
      }
    },
    "summary": {
      "es": [
        "!! rupturas de tesis confirmadas en NQ, GC e YM, y fisura real en ES tras la reversion de NY (GDP+PCE calientes); los 5 cierran MUY estirados",
        "NQ: corto revivido, dia 1, AVOID perseguir (5.9 ATR), vigila el cluster EMA20/EMA50 29306-29402",
        "ES: corto confirmado sin romper la invalidacion de 3 dias (7690), AVOID perseguir (5.8 ATR), vigila 7723-7750",
        "GC: corto revivido tras fallar el giro alcista, AVOID perseguir (2.8 ATR), vigila 4036-4051",
        "YM: corto revivido con conflicto de marcos (fondo aun mixto), AVOID perseguir (2.4 ATR), vigila 52588-52663",
        "CL: unico que sigue bien, ruptura alcista con los 4 marcos alineados, AVOID perseguir (9.4 ATR), vigila 101.9-102.3",
        "mas limpio: CL",
        "limite diario $1000 (bajo) deja maxContracts 0-1 en casi todas las zonas de hoy: piensa en micros",
        "ultimo dia habil de octubre (viernes): mas mechas por flujos de fin de mes"
      ],
      "en": [
        "!! thesis ruptures confirmed in NQ, GC and YM, and a real crack in ES after the NY reversal (hot GDP+PCE); all five close VERY stretched",
        "NQ: short revived, day 1, AVOID chasing (5.9 ATR), watch the EMA20/EMA50 cluster 29306-29402",
        "ES: short confirmed without breaking the 3-day invalidation (7690), AVOID chasing (5.8 ATR), watch 7723-7750",
        "GC: short revived after the bullish flip failed, AVOID chasing (2.8 ATR), watch 4036-4051",
        "YM: short revived with a frame conflict (underlying still mixed), AVOID chasing (2.4 ATR), watch 52588-52663",
        "CL: the only one still clean, bullish break with all 4 frames aligned, AVOID chasing (9.4 ATR), watch 101.9-102.3",
        "cleanest: CL",
        "the $1000 daily limit (low end) leaves maxContracts at 0-1 on almost every zone tonight: think micros",
        "last trading day of October (Friday): expect more wicks fr
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 24364,
  "by_verdict": {
    "AVOID": {
      "n": 2616,
      "wrTP1": 45.3,
      "nSL": 1246,
      "nTO": 184,
      "expR": 0.029,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 35.5
    },
    "GO": {
      "n": 4872,
      "wrTP1": 47.7,
      "nSL": 2298,
      "nTO": 251,
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
      "n": 16876,
      "wrTP1": 46.8,
      "nSL": 7954,
      "nTO": 1019,
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
      "expR": 0.029,
      "ci90": [
        -0.01,
        0.071
      ],
      "p_mean_le_0": 0.098,
      "n": 2495
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
      "n": 16400
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 2616,
      "wrTP1": 45.3,
      "nSL": 1246,
      "nTO": 184,
      "expR": 0.029,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 35.5
    },
    "GO_or_WAIT": {
      "n": 21748,
      "wrTP1": 47.0,
      "nSL": 10252,
      "nTO": 1270,
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
      "expR": 0.029,
      "ci90": [
        -0.01,
        0.071
      ],
      "p_mean_le_0": 0.098,
      "n": 2495
    },
    "GO_or_WAIT": {
      "expR": 0.035,
      "ci90": [
        0.021,
        0.048
      ],
      "p_mean_le_0": 0.0,
      "n": 21123
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
        "n": 33,
        "wrTP1": 36.4,
        "nSL": 16,
        "nTO": 5,
        "expR": -0.219,
        "pf": 0.6,
        "mfe_p25": 8.25,
        "mfe_p50": 16.5,
        "mfe_p75": 26.25,
        "winnerMAE_p75": 4.25,
        "winnerMAE_p90": 5.9,
        "loserMFEbeforeSL_p50": 13.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 7.5,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 12.5
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
        "n": 1600,
        "wrTP1": 44.1,
        "nSL": 794,
        "nTO": 100,
        "expR": -0.011,
        "pf": 0.98,
        "mfe_p25": 8.0,
        "mfe_p50": 16.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 33.6
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
        "n": 9433,
        "wrTP1": 47.1,
        "nSL": 4491,
        "nTO": 501,
        "expR": 0.041,
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
        "n": 941,
        "wrTP1": 47.7,
        "nSL": 417,
        "nTO": 75,
        "expR": 0.114,
        "pf": 1.24,
        "mfe_p25": 10.0,
        "mfe_p50": 22.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 40.5
      },
      "GO": {
        "n": 1662,
        "wrTP1": 48.4,
        "nSL": 753,
        "nTO": 105,
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
        "n": 6980,
        "wrTP1": 46.5,
        "nSL": 3268,
        "nTO": 468,
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
    "n": 42458,
    "wrTP1": 46.3,
    "nSL": 19908,
    "nTO": 2880,
    "expR": 0.036,
    "pf": 1.07,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 27.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 33.1
  },
  "shadow_ci90": {
    "expR": 0.036,
    "ci90": [
      0.027,
      0.046
    ],
    "p_mean_le_0": 0.0,
    "n": 41006
  },
  "raw_indicator": {
    "n": 46914,
    "wrTP1": 46.6,
    "nSL": 21976,
    "nTO": 3077,
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
    "revAfterSL_rate": 34.2
  },
  "raw_indicator_ci90": {
    "expR": 0.039,
    "ci90": [
      0.03,
      0.049
    ],
    "p_mean_le_0": 0.0,
    "n": 45338
  },
  "tier_ap_b_only": {
    "n": 23938,
    "wrTP1": 43.8,
    "nSL": 11748,
    "nTO": 1705,
    "expR": 0.028,
    "pf": 1.05,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.1
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.028,
    "ci90": [
      0.014,
      0.042
    ],
    "p_mean_le_0": 0.001,
    "n": 23149
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
    "shadow_n": 6559,
    "shadow_expR": 0.004,
    "raw_n": 8587,
    "raw_expR": 0.031,
    "shadow_beats_raw": false
  }
}
```
