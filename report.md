# Scalp CC · report 2026-11-13T02:14Z
- signals=64580 outcomes=62239 pares_resueltos=64311 pendientes=269 huerfanos=63

## ⚠ ALERTAS (llevar al frente del resumen)
- GATE: 29m/RETEST/LONG cumple el chequeo numerico agregado (n/PF/WR) pero NO el gate completo todavia -- weeklyStable3=False, slCauseMitigated=False. Es un near-miss a vigilar, no subir de peldano.
- SL: SL en la vela 1 del FVG (inversion) BATE al de 3 capas fuera de ruido (E[R] 1.912 vs 0.123, delta 1.789 CI90 [0.013, 5.168], n 1186). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.226 vs 0.063, delta 0.163 CI90 [0.127, 0.204], n 40017). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.066 vs 0.029, delta 0.036 CI90 [0.009, 0.063], n 10926). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=AVOID rinden MEJOR de forma no-random (E[R] 0.088 CI90 [0.056, 0.121], n 4542). Contrario a la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.068 CI90 [0.057, 0.08], n 31331). Consistente con la hipotesis original de agent-instructions.md.
- MODO SOMBRA: 3 semanas CERRADAS seguidas sin batir al indicador crudo (2026-W43, 2026-W44, 2026-W45) -- espejo inverso del gate de promocion del peldano 0->1. No implica bajar de peldano (ya promovido), pero revisar shadow_rules en la revision semanal.

- E[R] global: {"expR": 0.059, "ci90": [0.051, 0.067], "p_mean_le_0": 0.0, "n": 62176}
- gate ejecucion: {"readyForLive": true, "segment": "29m/RETEST/LONG", "weeklyStable3": false, "weeklyDetail": [{"week": "2026-W43", "wrTP1": null, "pf": null, "ok": false}, {"week": "2026-W44", "wrTP1": 54.5, "pf": 1.29, "ok": false}, {"week": "2026-W45", "wrTP1": 51.8, "pf": 2.04, "ok": true}], "slCauseMitigated": false, "fullyReady": false, "note": "readyForLive: n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side (solo agregado historico). fullyReady exige ademas weeklyStable3 (3 semanas CERRADAS seguidas con WR>=50 & PF>=1.3 en ese mismo segmento) y slCauseMitigated (experimento con verdict=confirmed dirigido a ese segmento). Solo fullyReady=true es luz verde real para subir de peldano; readyForLive=true con fullyReady=false es un near-miss a vigilar."}

## Integridad de sigId (colisiones, posible causa de alertas MUESTRA)
```json
{
  "signals": {
    "total_sigIds": 57626,
    "collided_sigIds": 6317,
    "collided_pct": 10.96,
    "delta_days_histogram": {
      "14": 1287,
      "7": 1190,
      "21": 555,
      "42": 540,
      "28": 534,
      "35": 510,
      "49": 379,
      "56": 320,
      "63": 144,
      "48": 118
    },
    "conflicting_result_n": 0,
    "conflicting_result_examples": []
  },
  "outcomes": {
    "total_sigIds": 55790,
    "collided_sigIds": 5887,
    "collided_pct": 10.55,
    "delta_days_histogram": {
      "14": 1245,
      "7": 1115,
      "21": 515,
      "28": 493,
      "42": 471,
      "35": 458,
      "49": 352,
      "56": 295,
      "63": 136,
      "48": 105
    },
    "conflicting_result_n": 3451,
    "conflicting_result_examples": [
      "NQ-2-22054-L",
      "GC-1-23394-S",
      "NQ-1-23427-L",
      "NQ-2-22070-L",
      "NQ-2-22078-L",
      "GC-1-23456-S",
      "GC-1-23459-S",
      "GC-1-23483-S"
    ]
  },
  "note": "colision = mismo sigId en >1 archivo diario con receivedAt distinto. 'last wins' en build_pairs() descarta una ocurrencia; si conflicting_result_n>0 confirma que son pares reales distintos, no un reenvio del mismo evento."
}
```

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 15m/INV/LONG | 4 | 50.0 | -0.115 | 0.77 | 2 | 92.0 | 155.75 | 0.0 |
| 15m/INV/SHORT | 4 | 75.0 | 0.667 | 3.67 | 1 | 91.5 | 1361.5 | 0.0 |
| 15m/RETEST/LONG | 837 | 49.5 | 0.12 | 1.25 | 388 | 120.0 | 227.25 | 57.5 |
| 15m/RETEST/SHORT | 792 | 51.0 | 0.169 | 1.36 | 358 | 141.0 | 254.75 | 63.4 |
| 1m/INV/LONG | 534 | 46.4 | 0.133 | 1.3 | 222 | 15.0 | 11.0 | 16.7 |
| 1m/INV/SHORT | 403 | 47.4 | 0.165 | 1.4 | 153 | 22.0 | 14.0 | 17.6 |
| 1m/RETEST/LONG | 19661 | 44.9 | 0.036 | 1.07 | 9399 | 15.0 | 10.0 | 28.7 |
| 1m/RETEST/SHORT | 13931 | 45.0 | 0.036 | 1.07 | 6531 | 19.0 | 12.0 | 29.3 |
| 29m/INV/LONG | 4 | 75.0 | 0.365 | 2.46 | 1 | 1251.0 | 1715.5 | 0.0 |
| 29m/INV/SHORT | 3 | 66.7 | 0.02 | 1.06 | 1 | 766.0 | 235.5 | 0.0 |
| 29m/RETEST/LONG | 404 | 55.0 | 0.344 | 1.84 | 157 | 140.5 | 216.25 | 56.7 |
| 29m/RETEST/SHORT | 455 | 51.6 | 0.187 | 1.41 | 198 | 167.5 | 284.0 | 74.7 |
| 2m/INV/LONG | 194 | 51.5 | 0.009 | 1.02 | 82 | 19.0 | 14.0 | 13.4 |
| 2m/INV/SHORT | 145 | 49.7 | 0.128 | 1.32 | 56 | 29.5 | 15.5 | 30.4 |
| 2m/RETEST/LONG | 8686 | 47.6 | 0.041 | 1.08 | 4091 | 19.0 | 13.0 | 39.1 |
| 2m/RETEST/SHORT | 5985 | 47.5 | 0.048 | 1.1 | 2809 | 25.0 | 15.0 | 38.6 |
| 3m/INV/LONG | 32 | 53.1 | -0.125 | 0.71 | 14 | 22.0 | 31.0 | 64.3 |
| 3m/INV/SHORT | 20 | 80.0 | 0.242 | 2.53 | 3 | 37.0 | 26.5 | 0.0 |
| 3m/RETEST/LONG | 2555 | 54.0 | 0.11 | 1.25 | 1105 | 25.5 | 18.0 | 51.5 |
| 3m/RETEST/SHORT | 2218 | 53.3 | 0.117 | 1.26 | 961 | 25.0 | 18.0 | 54.1 |
| 5m/INV/LONG | 64 | 65.6 | 0.097 | 1.33 | 18 | 31.0 | 32.75 | 55.6 |
| 5m/INV/SHORT | 45 | 51.1 | 0.125 | 1.3 | 18 | 82.0 | 63.5 | 38.9 |
| 5m/RETEST/LONG | 4263 | 51.6 | 0.112 | 1.25 | 1857 | 50.0 | 50.25 | 50.8 |
| 5m/RETEST/SHORT | 3072 | 49.8 | 0.094 | 1.2 | 1355 | 54.0 | 52.0 | 47.7 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 4177 | 23.6 | 0.058 | 1.09 | 2695 | 30.0 | 13.75 | 19.2 |
| B | 27620 | 47.8 | 0.044 | 1.09 | 12672 | 19.0 | 13.0 | 36.8 |
| C | 32514 | 49.8 | 0.072 | 1.16 | 14413 | 23.0 | 18.0 | 38.8 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 23144 | 49.3 | 0.076 | 1.16 | 10463 | 16.0 | 12.0 | 37.6 |
| London | 9516 | 47.0 | 0.041 | 1.08 | 4639 | 21.0 | 15.0 | 38.7 |
| NY | 11613 | 45.5 | 0.062 | 1.12 | 5499 | 31.0 | 22.0 | 39.3 |
| Sin KZ | 20038 | 45.9 | 0.046 | 1.09 | 9179 | 24.0 | 16.0 | 31.4 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 18041 | 45.9 | 0.05 | 1.1 | 8483 | 26.0 | 18.0 | 35.8 |
| edge=0 | 23722 | 49.2 | 0.066 | 1.14 | 10713 | 19.0 | 13.0 | 37.8 |
| edge=1 | 22548 | 46.1 | 0.059 | 1.12 | 10584 | 21.0 | 16.0 | 34.9 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 5781 | 53.6 | 0.119 | 1.26 | 2558 | 36.0 | 43.75 | 61.6 |
| aligned=1 | 58530 | 46.6 | 0.053 | 1.11 | 27222 | 21.0 | 14.0 | 33.8 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 39 | 48.7 | -0.008 | 0.98 | 19 | 23.0 | 32.0 | 31.6 |
| INV/LONG|edge=0 | 304 | 58.9 | 0.174 | 1.49 | 104 | 19.0 | 13.0 | 30.8 |
| INV/LONG|edge=1 | 489 | 43.8 | 0.046 | 1.1 | 216 | 17.0 | 13.0 | 13.4 |
| INV/SHORT|edge=-1 | 365 | 45.2 | 0.139 | 1.33 | 147 | 27.0 | 13.0 | 19.0 |
| INV/SHORT|edge=0 | 223 | 53.4 | 0.171 | 1.46 | 76 | 21.0 | 19.5 | 28.9 |
| INV/SHORT|edge=1 | 32 | 71.9 | 0.296 | 2.05 | 9 | 40.5 | 80.0 | 11.1 |
| RETEST/LONG|edge=-1 | 4645 | 51.6 | 0.111 | 1.24 | 2112 | 29.0 | 31.0 | 54.1 |
| RETEST/LONG|edge=0 | 14022 | 49.2 | 0.052 | 1.11 | 6423 | 17.0 | 13.0 | 38.0 |
| RETEST/LONG|edge=1 | 17739 | 44.5 | 0.046 | 1.09 | 8462 | 20.0 | 14.0 | 30.0 |
| RETEST/SHORT|edge=-1 | 12992 | 43.9 | 0.025 | 1.05 | 6205 | 25.0 | 16.0 | 30.0 |
| RETEST/SHORT|edge=0 | 9173 | 48.9 | 0.081 | 1.17 | 4110 | 21.0 | 14.0 | 37.9 |
| RETEST/SHORT|edge=1 | 4288 | 53.0 | 0.11 | 1.24 | 1897 | 29.0 | 30.0 | 59.1 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 307 | 41.4 | 0.039 | 1.08 | 143 | 17.0 | 13.0 | 11.2 |
| INV/LONG|tier=C | 525 | 54.3 | 0.121 | 1.31 | 196 | 19.0 | 14.0 | 26.0 |
| INV/SHORT|tier=B | 195 | 48.2 | 0.107 | 1.25 | 79 | 24.5 | 12.0 | 10.1 |
| INV/SHORT|tier=C | 425 | 50.1 | 0.183 | 1.47 | 153 | 26.0 | 23.0 | 28.1 |
| RETEST/LONG|tier=A+ | 2570 | 23.7 | 0.067 | 1.1 | 1671 | 25.0 | 12.0 | 17.4 |
| RETEST/LONG|tier=B | 15629 | 48.1 | 0.056 | 1.12 | 7147 | 18.0 | 13.0 | 38.1 |
| RETEST/LONG|tier=C | 18207 | 49.7 | 0.055 | 1.12 | 8179 | 21.0 | 17.0 | 37.9 |
| RETEST/SHORT|tier=A+ | 1607 | 23.5 | 0.043 | 1.06 | 1024 | 40.0 | 16.0 | 22.2 |
| RETEST/SHORT|tier=B | 11489 | 47.4 | 0.026 | 1.05 | 5303 | 21.0 | 14.0 | 36.2 |
| RETEST/SHORT|tier=C | 13357 | 49.7 | 0.089 | 1.19 | 5885 | 26.0 | 19.0 | 40.6 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=0 | 17 | 52.9 | -0.049 | 0.9 | 8 | 27.0 | 33.0 | 50.0 |
| INV/LONG|aligned=1 | 815 | 49.4 | 0.094 | 1.22 | 331 | 18.0 | 13.0 | 19.0 |
| INV/SHORT|aligned=0 | 19 | 73.7 | 0.122 | 1.46 | 5 | 45.0 | 98.25 | 20.0 |
| INV/SHORT|aligned=1 | 601 | 48.8 | 0.16 | 1.4 | 227 | 25.0 | 15.0 | 22.0 |
| RETEST/LONG|aligned=0 | 2624 | 53.0 | 0.116 | 1.25 | 1181 | 40.0 | 50.0 | 60.9 |
| RETEST/LONG|aligned=1 | 33782 | 46.7 | 0.052 | 1.11 | 15816 | 19.0 | 13.0 | 34.1 |
| RETEST/SHORT|aligned=0 | 3121 | 54.0 | 0.122 | 1.27 | 1364 | 33.0 | 38.0 | 62.5 |
| RETEST/SHORT|aligned=1 | 23332 | 46.2 | 0.05 | 1.1 | 10848 | 23.0 | 15.0 | 34.0 |

## Autopsia de SL
n_losses=29780  causas: RR-bajo×11626, contra-estructura×10777, stop-en-el-minimo×10775, killzone-Asia-largo×6179, estirado×5156, sin-nivel-detras×4628, chop×4440, SL-muy-pegado×3600, sin-causa-clara×2991, contra-sesgo×2558
- INV/LONG (n=339): killzone-Asia-largo×160, RR-bajo×130, contra-estructura×113, estirado×71, stop-en-el-minimo×67, chop×41, sin-nivel-detras×41, SL-muy-pegado×40, sin-causa-clara×22, contra-sesgo×8
- INV/SHORT (n=232): RR-bajo×103, contra-estructura×69, stop-en-el-minimo×51, estirado×48, sin-causa-clara×36, SL-muy-pegado×35, chop×32, sin-nivel-detras×19, contra-sesgo×5
- RETEST/LONG (n=16997): RR-bajo×6653, contra-estructura×6338, stop-en-el-minimo×6120, killzone-Asia-largo×6019, estirado×2950, sin-nivel-detras×2818, chop×2511, SL-muy-pegado×1966, sin-causa-clara×1382, contra-sesgo×1181
- RETEST/SHORT (n=12212): RR-bajo×4740, stop-en-el-minimo×4537, contra-estructura×4257, estirado×2087, chop×1856, sin-nivel-detras×1750, SL-muy-pegado×1559, sin-causa-clara×1551, contra-sesgo×1364

## Autopsia de SL · semana 2026-W46 (para revision semanal)
n_losses=2876  causas: stop-en-el-minimo×1241, contra-estructura×1178, RR-bajo×1168, killzone-Asia-largo×632, contra-sesgo×533, estirado×506, chop×471, sin-nivel-detras×410, SL-muy-pegado×310, sin-causa-clara×211
ejemplos por causa: {"stop-en-el-minimo": ["ES-5-21300-L", "YM-2-22619-L", "YM-1-23895-L", "YM-2-22745-L", "YM-2-22795-L"], "contra-estructura": ["YM-1-23718-L", "YM-1-23721-L", "NQ-1-24664-L", "ES-2-22682-L", "CL-1-24496-L"], "RR-bajo": ["YM-1-23721-L", "ES-1-24663-L", "CL-1-24496-L", "YM-1-23895-L", "YM-1-24083-L"]}

## Autopsia de SL · tendencia semanal de causas (% de las perdidas de esa semana)
```json
{
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
    "n_losses": 4964,
    "causes_pct": {
      "RR-bajo": 45.9,
      "stop-en-el-minimo": 42.2,
      "contra-estructura": 41.7,
      "contra-sesgo": 26.0,
      "estirado": 18.2,
      "killzone-Asia-largo": 15.9,
      "chop": 12.8,
      "SL-muy-pegado": 11.1,
      "sin-nivel-detras": 8.5,
      "sin-causa-clara": 8.3
    }
  },
  "2026-W45": {
    "n_losses": 3612,
    "causes_pct": {
      "stop-en-el-minimo": 42.7,
      "RR-bajo": 40.6,
      "contra-estructura": 38.6,
      "contra-sesgo": 20.3,
      "estirado": 18.5,
      "chop": 15.7,
      "killzone-Asia-largo": 13.9,
      "sin-nivel-detras": 13.2,
      "SL-muy-pegado": 10.8,
      "sin-causa-clara": 9.6
    }
  },
  "2026-W46": {
    "n_losses": 2876,
    "causes_pct": {
      "stop-en-el-minimo": 43.2,
      "contra-estructura": 41.0,
      "RR-bajo": 40.6,
      "killzone-Asia-largo": 22.0,
      "contra-sesgo": 18.5,
      "estirado": 17.6,
      "chop": 16.4,
      "sin-nivel-detras": 14.3,
      "SL-muy-pegado": 10.8,
      "sin-causa-clara": 7.3
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
    "n": 62163,
    "naive_expR": 0.059,
    "managed_expR": 0.115,
    "delta": 0.056,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 44.8,
    "fill_full_pct": 31.7,
    "m1_rate": 37.2,
    "m2_rate": 22.6,
    "m3_rate": 11.7,
    "beAfterM1_rate": 18.5
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
    "15m/INV/SHORT": {
      "n": 4,
      "naive_expR": 0.667,
      "managed_expR": 0.459,
      "delta": -0.209,
      "avgEntryBetterTk_p50": 2.4,
      "fill_t3plus_pct": 0.0,
      "fill_full_pct": 0.0,
      "m1_rate": 50.0,
      "m2_rate": 50.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 25.0
    },
    "15m/RETEST/LONG": {
      "n": 807,
      "naive_expR": 0.12,
      "managed_expR": -0.101,
      "delta": -0.22,
      "avgEntryBetterTk_p50": 1.4,
      "fill_t3plus_pct": 31.7,
      "fill_full_pct": 22.3,
      "m1_rate": 33.8,
      "m2_rate": 19.2,
      "m3_rate": 10.3,
      "beAfterM1_rate": 18.1
    },
    "15m/RETEST/SHORT": {
      "n": 765,
      "naive_expR": 0.169,
      "managed_expR": 0.019,
      "delta": -0.15,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 29.4,
      "fill_full_pct": 18.4,
      "m1_rate": 37.3,
      "m2_rate": 21.2,
      "m3_rate": 12.7,
      "beAfterM1_rate": 20.3
    },
    "1m/INV/LONG": {
      "n": 512,
      "naive_expR": 0.133,
      "managed_expR": 0.268,
      "delta": 0.135,
      "avgEntryBetterTk_p50": 2.55,
      "fill_t3plus_pct": 51.2,
      "fill_full_pct": 37.3,
      "m1_rate": 41.4,
      "m2_rate": 24.8,
      "m3_rate": 12.1,
      "beAfterM1_rate": 18.8
    },
    "1m/INV/SHORT": {
      "n": 383,
      "naive_expR": 0.165,
      "managed_expR": 0.315,
      "delta": 0.15,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 48.0,
      "fill_full_pct": 36.6,
      "m1_rate": 41.5,
      "m2_rate": 26.4,
      "m3_rate": 13.3,
      "beAfterM1_rate": 17.2
    },
    "1m/RETEST/LONG": {
      "n": 19088,
      "naive_expR": 0.036,
      "managed_expR": 0.13,
      "delta": 0.094,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 47.8,
      "fill_full_pct": 34.1,
      "m1_rate": 37.2,
      "m2_rate": 22.9,
      "m3_rate": 12.1,
      "beAfterM1_rate": 17.5
    },
    "1m/RETEST/SHORT": {
      "n": 13348,
      "naive_expR": 0.036,
      "managed_expR": 0.156,
      "delta": 0.12,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 49.0,
      "fill_full_pct": 35.0,
      "m1_rate": 38.3,
      "m2_rate": 24.1,
      "m3_rate": 12.5,
      "beAfterM1_rate": 17.8
    },
    "29m/INV/LONG": {
      "n": 4,
      "naive_expR": 0.365,
      "managed_expR": 1.0,
      "delta": 0.635,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 25.0,
      "fill_full_pct": 25.0,
      "m1_rate": 100.0,
      "m2_rate": 50.0,
      "m3_rate": 25.0,
      "beAfterM1_rate": 50.0
    },
    "29m/INV/SHORT": {
      "n": 3,
      "naive_expR": 0.02,
      "managed_expR": 0.414,
      "delta": 0.394,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 0.0,
      "fill_full_pct": 0.0,
      "m1_rate": 33.3,
      "m2_rate": 33.3,
      "m3_rate": 33.3,
      "beAfterM1_rate": 0.0
    },
    "29m/RETEST/LONG": {
      "n": 382,
      "naive_expR": 0.344,
      "managed_expR": 0.061,
      "delta": -0.283,
      "avgEntryBetterTk_p50": 8.75,
      "fill_t3plus_pct": 36.4,
      "fill_full_pct": 26.7,
      "m1_rate": 39.5,
      "m2_rate": 26.4,
      "m3_rate": 15.4,
      "beAfterM1_rate": 15.4
    },
    "29m/RETEST/SHORT": {
      "n": 434,
      "naive_expR": 0.187,
      "managed_expR": -0.078,
      "delta": -0.265,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 23.7,
      "fill_full_pct": 12.4,
      "m1_rate": 37.1,
      "m2_rate": 19.8,
      "m3_rate": 11.3,
      "beAfterM1_rate": 19.8
    },
    "2m/INV/LONG": {
      "n": 189,
      "naive_expR": 0.009,
      "managed_expR": 0.111,
      "delta": 0.101,
      "avgEntryBetterTk_p50": 4.2,
      "fill_t3plus_pct": 55.0,
      "fill_full_pct": 40.7,
      "m1_rate": 29.6,
      "m2_rate": 18.0,
      "m3_rate": 6.9,
      "beAfterM1_rate": 12.7
    },
    "2m/INV/SHORT": {
      "n": 140,
      "naive_expR": 0.128,
      "managed_expR": 0.249,
      "delta": 0.122,
      "avgEntryBetterTk_p50": 4.1,
      "fill_t3plus_pct": 49.3,
      "fill_full_pct": 37.9,
      "m1_rate": 36.4,
      "m2_rate": 24.3,
      "m3_rate": 14.3,
      "beAfterM1_rate": 13.6
    },
    "2m/RETEST/LONG": {
      "n": 8437,
      "naive_expR": 0.04,
      "managed_expR": 0.086,
      "delta": 0.046,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 44.3,
      "fill_full_pct": 31.3,
      "m1_rate": 35.8,
      "m2_rate": 21.5,
      "m3_rate": 11.3,
      "beAfterM1_rate": 18.4
    },
    "2m/RETEST/SHORT": {
      "n": 5792,
      "naive_expR": 0.048,
      "managed_expR": 0.132,
      "delta": 0.084,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 45.6,
      "fill_full_pct": 32.0,
      "m1_rate": 38.2,
      "m2_rate": 23.2,
      "m3_rate": 12.1,
      "beAfterM1_rate": 20.0
    },
    "3m/INV/LONG": {
      "n": 32,
      "naive_expR": -0.125,
      "managed_expR": -0.121,
      "delta": 0.003,
      "avgEntryBetterTk_p50": 8.4,
      "fill_t3plus_pct": 53.1,
      "fill_full_pct": 40.6,
      "m1_rate": 18.8,
      "m2_rate": 3.1,
      "m3_rate": 3.1,
      "beAfterM1_rate": 12.5
    },
    "3m/INV/SHORT": {
      "n": 19,
      "naive_expR": 0.242,
      "managed_expR": 0.306,
      "delta": 0.065,
      "avgEntryBetterTk_p50": 3.6,
      "fill_t3plus_pct": 31.6,
      "fill_full_pct": 21.1,
      "m1_rate": 21.1,
      "m2_rate": 10.5,
      "m3_rate": 5.3,
      "beAfterM1_rate": 10.5
    },
    "3m/RETEST/LONG": {
      "n": 2510,
      "naive_expR": 0.11,
      "managed_expR": 0.041,
      "delta": -0.069,
      "avgEntryBetterTk_p50": 2.7,
      "fill_t3plus_pct": 40.1,
      "fill_full_pct": 27.9,
      "m1_rate": 35.3,
      "m2_rate": 18.9,
      "m3_rate": 8.2,
      "beAfterM1_rate": 20.1
    },
    "3m/RETEST/SHORT": {
      "n": 2162,
      "naive_expR": 0.117,
      "managed_expR": 0.079,
      "delta": -0.038,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 38.2,
      "fill_full_pct": 26.5,
      "m1_rate": 37.5,
      "m2_rate": 20.5,
      "m3_rate": 10.2,
      "beAfterM1_rate": 20.9
    },
    "5m/INV/LONG": {
      "n": 61,
      "naive_expR": 0.097,
      "managed_expR": 0.084,
      "delta": -0.012,
      "avgEntryBetterTk_p50": 3.8,
      "fill_t3plus_pct": 41.0,
      "fill_full_pct": 32.8,
      "m1_rate": 16.4,
      "m2_rate": 6.6,
      "m3_rate": 3.3,
      "beAfterM1_rate": 11.5
    },
    "5m/INV/SHORT": {
      "n": 43,
      "naive_expR": 0.125,
      "managed_expR": 0.218,
      "delta": 0.093,
      "avgEntryBetterTk_p50": 7.0,
      "fill_t3plus_pct": 53.5,
      "fill_full_pct": 37.2,
      "m1_rate": 30.2,
      "m2_rate": 20.9,
      "m3_rate": 14.0,
      "beAfterM1_rate": 14.0
    },
    "5m/RETEST/LONG": {
      "n": 4116,
      "naive_expR": 0.112,
      "managed_expR": 0.078,
      "delta": -0.034,
      "avgEntryBetterTk_p50": 1.7,
      "fill_t3plus_pct": 35.4,
      "fill_full_pct": 24.8,
      "m1_rate": 37.3,
      "m2_rate": 21.9,
      "m3_rate": 10.8,
      "beAfterM1_rate": 20.5
    },
    "5m/RETEST/SHORT": {
      "n": 2928,
      "naive_expR": 0.094,
      "managed_expR": 0.087,
      "delta": -0.006,
      "avgEntryBetterTk_p50": 3.6,
      "fill_t3plus_pct": 36.8,
      "fill_full_pct": 24.9,
      "m1_rate": 36.3,
      "m2_rate": 21.9,
      "m3_rate": 11.0,
      "beAfterM1_rate": 19.4
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 52129,
    "layer_expR": 0.058,
    "orig_expR": 0.231,
    "delta_orig_minus_layer": 0.173,
    "delta_ci90": [
      0.115,
      0.252
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.7,
    "orig_wrTP1": 35.9,
    "slTk_p50": 24.0,
    "slOrigTk_p50": 11.0,
    "orig_wider_pct": 5.5,
    "orig_saved_from_SL": 172,
    "orig_caused_SL": 6879
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 4477,
  "invalid_by_seg": {
    "2m/RETEST/LONG": 556,
    "1m/RETEST/SHORT": 905,
    "2m/RETEST/SHORT": 290,
    "1m/RETEST/LONG": 1945,
    "1m/INV/SHORT": 60,
    "5m/RETEST/LONG": 154,
    "1m/INV/LONG": 94,
    "2m/INV/LONG": 24,
    "5m/INV/LONG": 4,
    "2m/INV/SHORT": 9,
    "5m/RETEST/SHORT": 105,
    "5m/INV/SHORT": 3,
    "3m/RETEST/LONG": 150,
    "3m/RETEST/SHORT": 126,
    "15m/RETEST/LONG": 14,
    "29m/RETEST/SHORT": 7,
    "15m/RETEST/SHORT": 25,
    "29m/RETEST/LONG": 4,
    "3m/INV/LONG": 2
  },
  "by_basis": {
    "candle1": {
      "n": 1186,
      "layer_expR": 0.123,
      "orig_expR": 1.912,
      "delta_orig_minus_layer": 1.789,
      "delta_ci90": [
        0.013,
        5.168
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 52.3,
      "orig_wrTP1": 28.7,
      "slTk_p50": 24.5,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 3.6,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 283
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
      "n": 40017,
      "layer_expR": 0.063,
      "orig_expR": 0.226,
      "delta_orig_minus_layer": 0.163,
      "delta_ci90": [
        0.127,
        0.204
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.3,
      "orig_wrTP1": 36.8,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 6.4,
      "orig_saved_from_SL": 161,
      "orig_caused_SL": 5181
    },
    "retestBar2": {
      "n": 10926,
      "layer_expR": 0.029,
      "orig_expR": 0.066,
      "delta_orig_minus_layer": 0.036,
      "delta_ci90": [
        0.009,
        0.063
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.2,
      "orig_wrTP1": 33.4,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 8,
      "orig_caused_SL": 1415
    }
  },
  "by_tf_kind_side": {
    "15m/RETEST/LONG": {
      "n": 784,
      "layer_expR": 0.127,
      "orig_expR": 1.588,
      "delta_orig_minus_layer": 1.461,
      "delta_ci90": [
        0.634,
        2.535
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.8,
      "orig_wrTP1": 49.2,
      "slTk_p50": 79.5,
      "slOrigTk_p50": 81.5,
      "orig_wider_pct": 30.5,
      "orig_saved_from_SL": 23,
      "orig_caused_SL": 43
    },
    "15m/RETEST/SHORT": {
      "n": 718,
      "layer_expR": 0.181,
      "orig_expR": 0.301,
      "delta_orig_minus_layer": 0.12,
      "delta_ci90": [
        -0.015,
        0.28
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 53.6,
      "orig_wrTP1": 46.5,
      "slTk_p50": 90.5,
      "slOrigTk_p50": 81.0,
      "orig_wider_pct": 27.4,
      "orig_saved_from_SL": 17,
      "orig_caused_SL": 68
    },
    "1m/INV/LONG": {
      "n": 418,
      "layer_expR": 0.139,
      "orig_expR": 0.205,
      "delta_orig_minus_layer": 0.067,
      "delta_ci90": [
        -0.135,
        0.291
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.8,
      "orig_wrTP1": 25.4,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 98
    },
    "1m/INV/SHORT": {
      "n": 313,
      "layer_expR": 0.162,
      "orig_expR": 0.313,
      "delta_orig_minus_layer": 0.151,
      "delta_ci90": [
        -0.139,
        0.486
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.8,
      "orig_wrTP1": 26.8,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.9,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 74
    },
    "1m/RETEST/LONG": {
      "n": 14722,
      "layer_expR": 0.035,
      "orig_expR": 0.093,
      "delta_orig_minus_layer": 0.058,
      "delta_ci90": [
        0.034,
        0.082
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.4,
      "orig_wrTP1": 30.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 1.2,
      "orig_saved_from_SL": 5,
      "orig_caused_SL": 2218
    },
    "1m/RETEST/SHORT": {
      "n": 11049,
      "layer_expR": 0.029,
      "orig_expR": 0.067,
      "delta_orig_minus_layer": 0.038,
      "delta_ci90": [
        0.011,
        0.065
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.2,
      "orig_wrTP1": 33.4,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 8,
      "orig_caused_SL": 1431
    },
    "29m/RETEST/LONG": {
      "n": 375,
      "layer_expR": 0.336,
      "orig_expR": 0.819,
      "delta_orig_minus_layer": 0.483,
      "delta_ci90": [
        0.182,
        0.834
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 58.1,
      "orig_wrTP1": 58.9,
      "slTk_p50": 66.0,
      "slOrigTk_p50": 98.0,
      "orig_wider_pct": 49.6,
      "orig_saved_from_SL": 17,
      "orig_caused_SL": 14
    },
    "29m/RETEST/SHORT": {
      "n": 420,
      "layer_expR": 0.208,
      "orig_expR": 0.357,
      "delta_orig_minus_layer": 0.149,
      "delta_ci90": [
        0.034,
        0.276
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 55.2,
      "orig_wrTP1": 55.0,
      "slTk_p50": 80.5,
      "slOrigTk_p50": 96.5,
      "orig_wider_pct": 39.3,
      "orig_saved_from_SL": 20,
      "orig_caused_SL": 21
    },
    "2m/INV/LONG": {
      "n": 165,
      "layer_expR": 0.034,
      "orig_expR": 0.434,
      "delta_orig_minus_layer": 0.4,
      "delta_ci90": [
        -0.015,
        0.909
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 54.5,
      "orig_wrTP1": 29.7,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 41
    },
    "2m/INV/SHORT": {
      "n": 130,
      "layer_expR": 0.105,
      "orig_expR": 0.015,
      "delta_orig_minus_layer": -0.09,
      "delta_ci90": [
        -0.298,
        0.152
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 51.5,
      "orig_wrTP1": 31.5,
      "slTk_p50": 30.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 27
    },
    "2m/RETEST/LONG": {
      "n": 7236,
      "layer_expR": 0.039,
      "orig_expR": 0.119,
      "delta_orig_minus_layer": 0.08,
      "delta_ci90": [
        0.05,
        0.111
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.4,
      "orig_wrTP1": 36.7,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.7,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 922
    },
    "2m/RETEST/SHORT": {
      "n": 5048,
      "layer_expR": 0.049,
      "orig_expR": 0.135,
      "delta_orig_minus_layer": 0.085,
      "delta_ci90": [
        0.045,
        0.123
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.3,
      "orig_wrTP1": 36.2,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 13.0,
      "orig_wider_pct": 3.5,
      "orig_saved_from_SL": 9,
      "orig_caused_SL": 671
    },
    "3m/INV/LONG": {
      "n": 30,
      "layer_expR": -0.161,
      "orig_expR": -0.32,
      "delta_orig_minus_layer": -0.159,
      "delta_ci90": [
        -0.49,
        0.183
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.0,
      "orig_wrTP1": 26.7,
      "slTk_p50": 38.5,
      "slOrigTk_p50": 7.5,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 7
    },
    "3m/INV/SHORT": {
      "n": 19,
      "layer_expR": 0.242,
      "orig_expR": 1.362,
      "delta_orig_minus_layer": 1.121,
      "delta_ci90": [
        -0.442,
        3.498
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 84.2,
      "orig_wrTP1": 42.1,
      "slTk_p50": 55.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 8
    },
    "3m/RETEST/LONG": {
      "n": 2227,
      "layer_expR": 0.105,
      "orig_expR": 0.347,
      "delta_orig_minus_layer": 0.242,
      "delta_ci90": [
        0.172,
        0.31
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 55.3,
      "orig_wrTP1": 41.7,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 13.0,
      "orig_wider_pct": 4.9,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 309
    },
    "3m/RETEST/SHORT": {
      "n": 1917,
      "layer_expR": 0.123,
      "orig_expR": 0.255,
      "delta_orig_minus_layer": 0.131,
      "delta_ci90": [
        0.057,
        0.211
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 55.3,
      "orig_wrTP1": 38.7,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.0,
      "orig_saved_from_SL": 4,
      "orig_caused_SL": 323
    },
    "5m/INV/LONG": {
      "n": 57,
      "layer_expR": 0.117,
      "orig_expR": -0.009,
      "delta_orig_minus_layer": -0.126,
      "delta_ci90": [
        -0.442,
        0.204
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 70.2,
      "orig_wrTP1": 45.6,
      "slTk_p50": 38.0,
      "slOrigTk_p50": 13.0,
      "orig_wider_pct": 7.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 14
    },
    "5m/INV/SHORT": {
      "n": 39,
      "layer_expR": 0.202,
      "orig_expR": 51.063,
      "delta_orig_minus_layer": 50.861,
      "delta_ci90": [
        -0.654,
        153.446
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 56.4,
      "orig_wrTP1": 28.2,
      "slTk_p50": 72.0,
      "slOrigTk_p50": 19.0,
      "orig_wider_pct": 12.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 11
    },
    "5m/RETEST/LONG": {
      "n": 3761,
      "layer_expR": 0.098,
      "orig_expR": 0.48,
      "delta_orig_minus_layer": 0.382,
      "delta_ci90": [
        0.167,
        0.727
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.4,
      "orig_wrTP1": 45.6,
      "slTk_p50": 44.0,
      "slOrigTk_p50": 31.0,
      "orig_wider_pct": 14.5,
      "orig_saved_from_SL": 34,
      "orig_caused_SL": 329
    },
    "5m/RETEST/SHORT": {
      "n": 2686,
      "layer_expR": 0.079,
      "orig_expR": 0.429,
      "delta_orig_minus_layer": 0.35,
      "delta_ci90": [
        0.187,
        0.551
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.9,
      "orig_wrTP1": 43.4,
      "slTk_p50": 50.0,
      "slOrigTk_p50": 36.0,
      "orig_wider_pct": 15.5,
      "orig_saved_from_SL": 20,
      "orig_caused_SL": 247
    }
  },
  "since_change": {
    "changeDate": "2026-09-26",
    "n": 37810,
    "by_tf_kind_side": {
      "15m/RETEST/LONG": {
        "n": 784,
        "layer_expR": 0.127,
        "orig_expR": 1.588,
        "delta_orig_minus_layer": 1.461,
        "delta_ci90": [
          0.634,
          2.535
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 51.8,
        "orig_wrTP1": 49.2,
        "slTk_p50": 79.5,
        "slOrigTk_p50": 81.5,
        "orig_wider_pct": 30.5,
        "orig_saved_from_SL": 23,
        "orig_caused_SL": 43
      },
      "15m/RETEST/SHORT": {
        "n": 718,
        "layer_expR": 0.181,
        "orig_expR": 0.301,
        "delta_orig_minus_layer": 0.12,
        "delta_ci90": [
          -0.015,
          0.28
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 53.6,
        "orig_wrTP1": 46.5,
        "slTk_p50": 90.5,
        "slOrigTk_p50": 81.0,
        "orig_wider_pct": 27.4,
        "orig_saved_from_SL": 17,
        "orig_caused_SL": 68
      },
      "1m/INV/LONG": {
        "n": 286,
        "layer_expR": 0.132,
        "orig_expR": 0.316,
        "delta_orig_minus_layer": 0.183,
        "delta_ci90": [
          -0.061,
          0.481
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 50.0,
        "orig_wrTP1": 26.6,
        "slTk_p50": 18.0,
        "slOrigTk_p50": 5.0,
        "orig_wider_pct": 1.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 67
      },
      "1m/INV/SHORT": {
        "n": 209,
        "layer_expR": 0.226,
        "orig_expR": 0.485,
        "delta_orig_minus_layer": 0.259,
        "delta_ci90": [
          -0.149,
          0.734
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 49.8,
        "orig_wrTP1": 27.3,
        "slTk_p50": 26.0,
        "slOrigTk_p50": 6.0,
        "orig_wider_pct": 1.4,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 49
      },
      "1m/RETEST/LONG": {
        "n": 9541,
        "layer_expR": 0.023,
        "orig_expR": 0.061,
        "delta_orig_minus_layer": 0.038,
        "delta_ci90": [
          0.012,
          0.068
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 44.9,
        "orig_wrTP1": 29.9,
        "slTk_p50": 18.0,
        "slOrigTk_p50": 7.0,
        "orig_wider_pct": 1.3,
        "orig_saved_from_SL": 3,
        "orig_caused_SL": 1441
      },
      "1m/RETEST/SHORT": {
        "n": 7789,
        "layer_expR": 0.029,
        "orig_expR": 0.066,
        "delta_orig_minus_layer": 0.037,
        "delta_ci90": [
          0.006,
          0.068
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 46.3,
        "orig_wrTP1": 33.3,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 2.2,
        "orig_saved_from_SL": 7,
        "orig_caused_SL": 1024
      },
      "29m/RETEST/LONG": {
        "n": 375,
        "layer_expR": 0.336,
        "orig_expR": 0.819,
        "delta_orig_minus_layer": 0.483,
        "delta_ci90": [
          0.182,
          0.834
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 58.1,
        "orig_wrTP1": 58.9,
        "slTk_p50": 66.0,
        "slOrigTk_p50": 98.0,
        "orig_wider_pct": 49.6,
        "orig_saved_from_SL": 17,
        "orig_caused_SL": 14
      },
      "29m/RETEST/SHORT": {
        "n": 420,
        "layer_expR": 0.208,
        "orig_expR": 0.357,
        "delta_orig_minus_layer": 0.149,
        "delta_ci90": [
          0.034,
          0.276
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 55.2,
        "orig_wrTP1": 55.0,
        "slTk_p50": 80.5,
        "slOrigTk_p50": 96.5,
        "orig_wider_pct": 39.3,
        "orig_saved_from_SL": 20,
        "orig_caused_SL": 21
      },
      "2m/INV/LONG": {
        "n": 114,
        "layer_expR": 0.062,
        "orig_expR": 0.361,
        "delta_orig_minus_layer": 0.298,
        "delta_ci90": [
          -0.113,
          0.835
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 56.1,
        "orig_wrTP1": 30.7,
        "slTk_p50": 31.5,
        "slOrigTk_p50": 9.0,
        "orig_wider_pct": 0.9,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 29
      },
      "2m/INV/SHORT": {
        "n": 80,
        "layer_expR": 0.053,
        "orig_expR": -0.18,
        "delta_orig_minus_layer": -0.233,
        "delta_ci90": [
          -0.456,
          0.012
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 56.2,
        "orig_wrTP1": 30.0,
        "slTk_p50": 34.5,
        "slOrigTk_p50": 8.0,
        "orig_wider_pct": 5.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 21
      },
      "2m/RETEST/LONG": {
        "n": 4745,
        "layer_expR": 0.036,
        "orig_expR": 0.1,
        "delta_orig_minus_layer": 0.064,
        "delta_ci90": [
          0.028,
          0.101
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 49.4,
        "orig_wrTP1": 36.4,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 3.9,
        "orig_saved_from_SL": 3,
        "orig_caused_SL": 618
      },
      "2m/RETEST/SHORT": {
        "n": 3525,
        "layer_expR": 0.04,
        "orig_expR": 0.112,
        "delta_orig_minus_layer": 0.072,
        "delta_ci90": [
          0.026,
          0.12
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 48.6,
        "orig_wrTP1": 35.3,
        "slTk_p50": 25.0,
        "slOrigTk_p50": 13.0,
        "orig_wider_pct": 3.2,
        "orig_saved_from_SL": 7,
        "orig_caused_SL": 477
      },
      "3m/INV/LONG": {
        "n": 30,
        "layer_expR": -0.161,
        "orig_expR": -0.32,
        "delta_orig_minus_layer": -0.159,
        "delta_ci90": [
          -0.49,
          0.183
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 50.0,
        "orig_wrTP1": 26.7,
        "slTk_p50": 38.5,
        "slOrigTk_p50": 7.5,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 7
      },
      "3m/INV/SHORT": {
        "n": 19,
        "layer_expR": 0.242,
        "orig_expR": 1.362,
        "delta_orig_minus_layer": 1.121,
        "delta_ci90": [
          -0.442,
          3.498
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 84.2,
        "orig_wrTP1": 42.1,
        "slTk_p50": 55.0,
        "slOrigTk_p50": 7.0,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 8
      },
      "3m/RETEST/LONG": {
        "n": 2227,
        "layer_expR": 0.105,
        "orig_expR": 0.347,
        "delta_orig_minus_layer": 0.242,
        "delta_ci90": [
          0.172,
          0.31
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 55.3,
        "orig_wrTP1": 41.7,
        "slTk_p50": 25.0,
        "slOrigTk_p50": 13.0,
        "orig_wider_pct": 4.9,
        "orig_saved_from_SL": 6,
        "orig_caused_SL": 309
      },
      "3m/RETEST/SHORT": {
        "n": 1917,
        "layer_expR": 0.123,
        "orig_expR": 0.255,
        "delta_orig_minus_layer": 0.131,
        "delta_ci90": [
          0.057,
          0.211
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 55.3,
        "orig_wrTP1": 38.7,
        "slTk_p50": 24.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 3.0,
        "orig_saved_from_SL": 4,
        "orig_caused_SL": 323
      },
      "5m/INV/LONG": {
        "n": 39,
        "layer_expR": -0.03,
        "orig_expR": 0.167,
        "delta_orig_minus_layer": 0.197,
        "delta_ci90": [
          -0.198,
          0.601
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 66.7,
        "orig_wrTP1": 48.7,
        "slTk_p50": 38.0,
        "slOrigTk_p50": 14.0,
        "orig_wider_pct": 2.6,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 7
      },
      "5m/INV/SHORT": {
        "n": 29,
        "layer_expR": 0.14,
        "orig_expR": 68.82,
        "delta_orig_minus_layer": 68.68,
        "delta_ci90": [
          -0.607,
          206.621
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 51.7,
        "orig_wrTP1": 24.1,
        "slTk_p50": 182.0,
        "slOrigTk_p50": 19.0,
        "orig_wider_pct": 6.9,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 8
      },
      "5m/RETEST/LONG": {
        "n": 2838,
        "layer_expR": 0.09,
        "orig_expR": 0.546,
        "delta_orig_minus_layer": 0.456,
        "delta_ci90": [
          0.174,
          0.923
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 53.1,
        "orig_wrTP1": 45.6,
        "slTk_p50": 55.0,
        "slOrigTk_p50": 38.5,
        "orig_wider_pct": 13.7,
        "orig_saved_from_SL": 27,
        "orig_caused_SL": 240
      },
      "5m/RETEST/SHORT": {
        "n": 2110,
        "layer_expR": 0.088,
        "orig_expR": 0.496,
        "delta_orig_minus_layer": 0.408,
        "delta_ci90": [
          0.208,
          0.67
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 52.3,
        "orig_wrTP1": 43.4,
        "slTk_p50": 58.5,
        "slOrigTk_p50": 44.0,
        "orig_wider_pct": 13.6,
        "orig_saved_from_SL": 13,
        "orig_caused_SL": 200
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
      "n": 18978,
      "wrTP1": 46.5,
      "nSL": 8962,
      "nTO": 1192,
      "expR": 0.031,
      "pf": 1.06,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 33.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 30.1,
      "ci90": {
        "expR": 0.031,
        "ci90": [
          0.017,
          0.045
        ],
        "p_mean_le_0": 0.0,
        "n": 18421
      }
    },
    "cuts": {
      "1.0": {
        "n": 9176,
        "wrTP1": 30.6,
        "nSL": 5482,
        "nTO": 882,
        "expR": 0.032,
        "pf": 1.05,
        "mfe_p25": 9.0,
        "mfe_p50": 20.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.90000000000009,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 21.2,
        "ci90": {
          "expR": 0.032,
          "ci90": [
            0.007,
            0.059
          ],
          "p_mean_le_0": 0.014,
          "n": 8855
        }
      },
      "1.2": {
        "n": 7564,
        "wrTP1": 27.8,
        "nSL": 4650,
        "nTO": 812,
        "expR": 0.043,
        "pf": 1.07,
        "mfe_p25": 9.0,
        "mfe_p50": 21.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 18.8,
        "ci90": {
          "expR": 0.043,
          "ci90": [
            0.013,
            0.072
          ],
          "p_mean_le_0": 0.009,
          "n": 7287
        }
      },
      "1.3": {
        "n": 6896,
        "wrTP1": 26.3,
        "nSL": 4300,
        "nTO": 780,
        "expR": 0.043,
        "pf": 1.07,
        "mfe_p25": 9.0,
        "mfe_p50": 21.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.4,
        "ci90": {
          "expR": 0.043,
          "ci90": [
            0.012,
            0.075
          ],
          "p_mean_le_0": 0.009,
          "n": 6634
        }
      },
      "1.5": {
        "n": 5821,
        "wrTP1": 23.6,
        "nSL": 3735,
        "nTO": 715,
        "expR": 0.035,
        "pf": 1.05,
        "mfe_p25": 9.0,
        "mfe_p50": 21.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 15.5,
        "ci90": {
          "expR": 0.035,
          "ci90": [
            -0.0,
            0.071
          ],
          "p_mean_le_0": 0.053,
          "n": 5601
        }
      },
      "2.0": {
        "n": 3834,
        "wrTP1": 17.6,
        "nSL": 2580,
        "nTO": 579,
        "expR": 0.024,
        "pf": 1.03,
        "mfe_p25": 8.0,
        "mfe_p50": 22.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 11.4,
        "ci90": {
          "expR": 0.024,
          "ci90": [
            -0.023,
            0.072
          ],
          "p_mean_le_0": 0.2,
          "n": 3686
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 13333,
      "wrTP1": 47.0,
      "nSL": 6126,
      "nTO": 936,
      "expR": 0.039,
      "pf": 1.08,
      "mfe_p25": 9.0,
      "mfe_p50": 19.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 31.2,
      "ci90": {
        "expR": 0.039,
        "ci90": [
          0.022,
          0.055
        ],
        "p_mean_le_0": 0.0,
        "n": 12778
      }
    },
    "cuts": {
      "1.0": {
        "n": 6385,
        "wrTP1": 31.5,
        "nSL": 3690,
        "nTO": 684,
        "expR": 0.044,
        "pf": 1.07,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 22.0,
        "ci90": {
          "expR": 0.044,
          "ci90": [
            0.013,
            0.076
          ],
          "p_mean_le_0": 0.013,
          "n": 6040
        }
      },
      "1.2": {
        "n": 5214,
        "wrTP1": 28.0,
        "nSL": 3130,
        "nTO": 626,
        "expR": 0.041,
        "pf": 1.06,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.5,
        "ci90": {
          "expR": 0.041,
          "ci90": [
            0.004,
            0.075
          ],
          "p_mean_le_0": 0.036,
          "n": 4911
        }
      },
      "1.3": {
        "n": 4781,
        "wrTP1": 26.5,
        "nSL": 2906,
        "nTO": 607,
        "expR": 0.04,
        "pf": 1.06,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.4,
        "ci90": {
          "expR": 0.04,
          "ci90": [
            0.004,
            0.08
          ],
          "p_mean_le_0": 0.035,
          "n": 4494
        }
      },
      "1.5": {
        "n": 4027,
        "wrTP1": 23.9,
        "nSL": 2506,
        "nTO": 558,
        "expR": 0.037,
        "pf": 1.06,
        "mfe_p25": 12.0,
        "mfe_p50": 29.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 16.5,
        "ci90": {
          "expR": 0.037,
          "ci90": [
            -0.006,
            0.08
          ],
          "p_mean_le_0": 0.074,
          "n": 3778
        }
      },
      "2.0": {
        "n": 2705,
        "wrTP1": 18.5,
        "nSL": 1765,
        "nTO": 440,
        "expR": 0.024,
        "pf": 1.03,
        "mfe_p25": 12.0,
        "mfe_p50": 30.0,
        "mfe_p75": 64.0,
        "winnerMAE_p75": 13.25,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 11.8,
        "ci90": {
          "expR": 0.024,
          "ci90": [
            -0.034,
            0.08
          ],
          "p_mean_le_0": 0.233,
          "n": 2533
        }
      }
    }
  },
  "15/RETEST/LONG": {
    "baseline": {
      "n": 794,
      "wrTP1": 52.1,
      "nSL": 353,
      "nTO": 27,
      "expR": 0.112,
      "pf": 1.24,
      "mfe_p25": 39.0,
      "mfe_p50": 110.0,
      "mfe_p75": 640.5,
      "winnerMAE_p75": 227.25,
      "winnerMAE_p90": 2771.8999999999996,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -142.5,
      "revAfterSL_rate": 63.2,
      "ci90": {
        "expR": 0.112,
        "ci90": [
          0.045,
          0.181
        ],
        "p_mean_le_0": 0.005,
        "n": 767
      }
    },
    "cuts": {
      "1.0": {
        "n": 305,
        "wrTP1": 33.8,
        "nSL": 186,
        "nTO": 16,
        "expR": 0.089,
        "pf": 1.14,
        "mfe_p25": 50.0,
        "mfe_p50": 140.0,
        "mfe_p75": 882.0,
        "winnerMAE_p75": 320.5,
        "winnerMAE_p90": 2763.6,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -108.0,
        "revAfterSL_rate": 59.1,
        "ci90": {
          "expR": 0.089,
          "ci90": [
            -0.057,
            0.247
          ],
          "p_mean_le_0": 0.157,
          "n": 289
        }
      },
      "1.2": {
        "n": 248,
        "wrTP1": 29.8,
        "nSL": 161,
        "nTO": 13,
        "expR": 0.035,
        "pf": 1.05,
        "mfe_p25": 53.0,
        "mfe_p50": 132.0,
        "mfe_p75": 971.0,
        "winnerMAE_p75": 575.25,
        "winnerMAE_p90": 3608.7000000000025,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -107.5,
        "revAfterSL_rate": 59.0,
        "ci90": {
          "expR": 0.035,
          "ci90": [
            -0.134,
            0.206
          ],
          "p_mean_le_0": 0.371,
          "n": 235
        }
      },
      "1.3": {
        "n": 221,
        "wrTP1": 29.4,
        "nSL": 146,
        "nTO": 10,
        "expR": 0.033,
        "pf": 1.05,
        "mfe_p25": 53.0,
        "mfe_p50": 138.0,
        "mfe_p75": 970.0,
        "winnerMAE_p75": 729.0,
        "winnerMAE_p90": 3511.6000000000013,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -107.0,
        "revAfterSL_rate": 58.9,
        "ci90": {
          "expR": 0.033,
          "ci90": [
            -0.138,
            0.215
          ],
          "p_mean_le_0": 0.377,
          "n": 211
        }
      },
      "1.5": {
        "n": 171,
        "wrTP1": 29.2,
        "nSL": 112,
        "nTO": 9,
        "expR": 0.095,
        "pf": 1.14,
        "mfe_p25": 60.25,
        "mfe_p50": 153.0,
        "mfe_p75": 1050.75,
        "winnerMAE_p75": 697.25,
        "winnerMAE_p90": 2865.0000000000014,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -90.0,
        "revAfterSL_rate": 53.6,
        "ci90": {
          "expR": 0.095,
          "ci90": [
            -0.122,
            0.317
          ],
          "p_mean_le_0": 0.247,
          "n": 162
        }
      },
      "2.0": {
        "n": 100,
        "wrTP1": 25.0,
        "nSL": 69,
        "nTO": 6,
        "expR": 0.065,
        "pf": 1.09,
        "mfe_p25": 68.0,
        "mfe_p50": 279.5,
        "mfe_p75": 9559.0,
        "winnerMAE_p75": 1357.0,
        "winnerMAE_p90": 7430.200000000012,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -94.0,
        "revAfterSL_rate": 49.3,
        "ci90": {
          "expR": 0.065,
          "ci90": [
            -0.236,
            0.393
          ],
          "p_mean_le_0": 0.361,
          "n": 94
        }
      }
    }
  },
  "15/RETEST/SHORT": {
    "baseline": {
      "n": 768,
      "wrTP1": 52.6,
      "nSL": 338,
      "nTO": 26,
      "expR": 0.178,
      "pf": 1.39,
      "mfe_p25": 37.5,
      "mfe_p50": 139.0,
      "mfe_p75": 1116.5,
      "winnerMAE_p75": 254.75,
      "winnerMAE_p90": 4142.899999999999,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -210.0,
      "revAfterSL_rate": 67.2,
      "ci90": {
        "expR": 0.178,
        "ci90": [
          0.092,
          0.272
        ],
        "p_mean_le_0": 0.0,
        "n": 743
      }
    },
    "cuts": {
      "1.0": {
        "n": 286,
        "wrTP1": 39.2,
        "nSL": 161,
        "nTO": 13,
        "expR": 0.354,
        "pf": 1.6,
        "mfe_p25": 52.25,
        "mfe_p50": 164.0,
        "mfe_p75": 969.0,
        "winnerMAE_p75": 183.25,
        "winnerMAE_p90": 2791.6000000000004,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -229.5,
        "revAfterSL_rate": 60.2,
        "ci90": {
          "expR": 0.354,
          "ci90": [
            0.149,
            0.57
          ],
          "p_mean_le_0": 0.001,
          "n": 274
        }
      },
      "1.2": {
        "n": 234,
        "wrTP1": 38.0,
        "nSL": 135,
        "nTO": 10,
        "expR": 0.407,
        "pf": 1.68,
        "mfe_p25": 53.0,
        "mfe_p50": 154.0,
        "mfe_p75": 1001.0,
        "winnerMAE_p75": 166.0,
        "winnerMAE_p90": 2667.4,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -222.5,
        "revAfterSL_rate": 59.3,
        "ci90": {
          "expR": 0.407,
          "ci90": [
            0.19,
            0.647
          ],
          "p_mean_le_0": 0.002,
          "n": 225
        }
      },
      "1.3": {
        "n": 212,
        "wrTP1": 36.3,
        "nSL": 126,
        "nTO": 9,
        "expR": 0.4,
        "pf": 1.65,
        "mfe_p25": 55.25,
        "mfe_p50": 152.5,
        "mfe_p75": 1053.5,
        "winnerMAE_p75": 139.0,
        "winnerMAE_p90": 2587.6000000000004,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -221.0,
        "revAfterSL_rate": 58.7,
        "ci90": {
          "expR": 0.4,
          "ci90": [
            0.158,
            0.679
          ],
          "p_mean_le_0": 0.005,
          "n": 204
        }
      },
      "1.5": {
        "n": 172,
        "wrTP1": 32.0,
        "nSL": 109,
        "nTO": 8,
        "expR": 0.374,
        "pf": 1.56,
        "mfe_p25": 64.0,
        "mfe_p50": 155.0,
        "mfe_p75": 979.0,
        "winnerMAE_p75": 91.0,
        "winnerMAE_p90": 1256.2000000000003,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -221.0,
        "revAfterSL_rate": 56.9,
        "ci90": {
          "expR": 0.374,
          "ci90": [
            0.075,
            0.692
          ],
          "p_mean_le_0": 0.019,
          "n": 165
        }
      },
      "2.0": {
        "n": 105,
        "wrTP1": 29.5,
        "nSL": 68,
        "nTO": 6,
        "expR": 0.551,
        "pf": 1.81,
        "mfe_p25": 63.5,
        "mfe_p50": 173.0,
        "mfe_p75": 984.5,
        "winnerMAE_p75": 54.0,
        "winnerMAE_p90": 1333.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -230.0,
        "revAfterSL_rate": 47.1,
        "ci90": {
          "expR": 0.551,
          "ci90": [
            0.097,
            1.03
          ],
          "p_mean_le_0": 0.023,
          "n": 100
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 8433,
      "wrTP1": 49.0,
      "nSL": 3916,
      "nTO": 381,
      "expR": 0.038,
      "pf": 1.08,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 42.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 28.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 40.8,
      "ci90": {
        "expR": 0.038,
        "ci90": [
          0.016,
          0.059
        ],
        "p_mean_le_0": 0.004,
        "n": 8194
      }
    },
    "cuts": {
      "1.0": {
        "n": 3856,
        "wrTP1": 32.4,
        "nSL": 2329,
        "nTO": 276,
        "expR": 0.036,
        "pf": 1.06,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 33.8,
        "ci90": {
          "expR": 0.036,
          "ci90": [
            -0.003,
            0.075
          ],
          "p_mean_le_0": 0.064,
          "n": 3709
        }
      },
      "1.2": {
        "n": 3128,
        "wrTP1": 29.1,
        "nSL": 1967,
        "nTO": 251,
        "expR": 0.032,
        "pf": 1.05,
        "mfe_p25": 12.0,
        "mfe_p50": 26.5,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 31.4,
        "ci90": {
          "expR": 0.032,
          "ci90": [
            -0.015,
            0.078
          ],
          "p_mean_le_0": 0.133,
          "n": 3000
        }
      },
      "1.3": {
        "n": 2825,
        "wrTP1": 27.8,
        "nSL": 1800,
        "nTO": 239,
        "expR": 0.038,
        "pf": 1.06,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 30.5,
        "ci90": {
          "expR": 0.038,
          "ci90": [
            -0.01,
            0.088
          ],
          "p_mean_le_0": 0.101,
          "n": 2705
        }
      },
      "1.5": {
        "n": 2344,
        "wrTP1": 25.0,
        "nSL": 1533,
        "nTO": 225,
        "expR": 0.035,
        "pf": 1.05,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 27.9,
        "ci90": {
          "expR": 0.035,
          "ci90": [
            -0.022,
            0.096
          ],
          "p_mean_le_0": 0.151,
          "n": 2234
        }
      },
      "2.0": {
        "n": 1462,
        "wrTP1": 19.7,
        "nSL": 1000,
        "nTO": 174,
        "expR": 0.051,
        "pf": 1.07,
        "mfe_p25": 12.0,
        "mfe_p50": 29.0,
        "mfe_p75": 64.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.30000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 21.8,
        "ci90": {
          "expR": 0.051,
          "ci90": [
            -0.029,
            0.135
          ],
          "p_mean_le_0": 0.149,
          "n": 1382
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 5721,
      "wrTP1": 49.7,
      "nSL": 2617,
      "nTO": 263,
      "expR": 0.061,
      "pf": 1.13,
      "mfe_p25": 11.0,
      "mfe_p50": 24.0,
      "mfe_p75": 51.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 32.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 41.4,
      "ci90": {
        "expR": 0.061,
        "ci90": [
          0.035,
          0.087
        ],
        "p_mean_le_0": 0.0,
        "n": 5552
      }
    },
    "cuts": {
      "1.0": {
        "n": 2657,
        "wrTP1": 32.9,
        "nSL": 1601,
        "nTO": 182,
        "expR": 0.047,
        "pf": 1.07,
        "mfe_p25": 16.0,
        "mfe_p50": 33.5,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 32.700000000000045,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 33.5,
        "ci90": {
          "expR": 0.047,
          "ci90": [
            -0.003,
            0.094
          ],
          "p_mean_le_0": 0.059,
          "n": 2560
        }
      },
      "1.2": {
        "n": 2154,
        "wrTP1": 29.1,
        "nSL": 1363,
        "nTO": 165,
        "expR": 0.033,
        "pf": 1.05,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 31.0,
        "ci90": {
          "expR": 0.033,
          "ci90": [
            -0.025,
            0.092
          ],
          "p_mean_le_0": 0.172,
          "n": 2071
        }
      },
      "1.3": {
        "n": 1946,
        "wrTP1": 27.4,
        "nSL": 1257,
        "nTO": 155,
        "expR": 0.026,
        "pf": 1.04,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 74.0,
        "winnerMAE_p75": 15.75,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 29.5,
        "ci90": {
          "expR": 0.026,
          "ci90": [
            -0.037,
            0.086
          ],
          "p_mean_le_0": 0.258,
          "n": 1871
        }
      },
      "1.5": {
        "n": 1617,
        "wrTP1": 25.0,
        "nSL": 1076,
        "nTO": 137,
        "expR": 0.026,
        "pf": 1.04,
        "mfe_p25": 18.0,
        "mfe_p50": 39.0,
        "mfe_p75": 78.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 27.5,
        "ci90": {
          "expR": 0.026,
          "ci90": [
            -0.04,
            0.102
          ],
          "p_mean_le_0": 0.268,
          "n": 1557
        }
      },
      "2.0": {
        "n": 1053,
        "wrTP1": 20.4,
        "nSL": 729,
        "nTO": 109,
        "expR": 0.045,
        "pf": 1.06,
        "mfe_p25": 19.0,
        "mfe_p50": 41.0,
        "mfe_p75": 84.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 22.5,
        "ci90": {
          "expR": 0.045,
          "ci90": [
            -0.047,
            0.14
          ],
          "p_mean_le_0": 0.214,
          "n": 1011
        }
      }
    }
  },
  "29/RETEST/LONG": {
    "baseline": {
      "n": 376,
      "wrTP1": 59.0,
      "nSL": 137,
      "nTO": 17,
      "expR": 0.328,
      "pf": 1.86,
      "mfe_p25": 44.0,
      "mfe_p50": 120.0,
      "mfe_p75": 854.5,
      "winnerMAE_p75": 216.25,
      "winnerMAE_p90": 4453.900000000007,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -122.5,
      "revAfterSL_rate": 65.0,
      "ci90": {
        "expR": 0.328,
        "ci90": [
          0.219,
          0.445
        ],
        "p_mean_le_0": 0.0,
        "n": 359
      }
    },
    "cuts": {
      "1.0": {
        "n": 150,
        "wrTP1": 40.7,
        "nSL": 75,
        "nTO": 14,
        "expR": 0.408,
        "pf": 1.74,
        "mfe_p25": 55.0,
        "mfe_p50": 143.0,
        "mfe_p75": 1179.75,
        "winnerMAE_p75": 143.0,
        "winnerMAE_p90": 2002.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -92.0,
        "revAfterSL_rate": 60.0,
        "ci90": {
          "expR": 0.408,
          "ci90": [
            0.176,
            0.652
          ],
          "p_mean_le_0": 0.002,
          "n": 136
        }
      },
      "1.2": {
        "n": 124,
        "wrTP1": 34.7,
        "nSL": 68,
        "nTO": 13,
        "expR": 0.332,
        "pf": 1.54,
        "mfe_p25": 55.5,
        "mfe_p50": 142.0,
        "mfe_p75": 1095.0,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 1147.6000000000008,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -86.5,
        "revAfterSL_rate": 57.4,
        "ci90": {
          "expR": 0.332,
          "ci90": [
            0.037,
            0.613
          ],
          "p_mean_le_0": 0.036,
          "n": 111
        }
      },
      "1.3": {
        "n": 110,
        "wrTP1": 30.9,
        "nSL": 65,
        "nTO": 11,
        "expR": 0.278,
        "pf": 1.42,
        "mfe_p25": 55.5,
        "mfe_p50": 144.0,
        "mfe_p75": 1095.0,
        "winnerMAE_p75": 131.25,
        "winnerMAE_p90": 1124.3999999999999,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -86.5,
        "revAfterSL_rate": 55.4,
        "ci90": {
          "expR": 0.278,
          "ci90": [
            -0.036,
            0.591
          ],
          "p_mean_le_0": 0.072,
          "n": 99
        }
      },
      "1.5": {
        "n": 96,
        "wrTP1": 28.1,
        "nSL": 59,
        "nTO": 10,
        "expR": 0.262,
        "pf": 1.38,
        "mfe_p25": 56.25,
        "mfe_p50": 159.0,
        "mfe_p75": 1038.75,
        "winnerMAE_p75": 96.0,
        "winnerMAE_p90": 846.0000000000011,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -90.0,
        "revAfterSL_rate": 54.2,
        "ci90": {
          "expR": 0.262,
          "ci90": [
            -0.075,
            0.636
          ],
          "p_mean_le_0": 0.108,
          "n": 86
        }
      },
      "2.0": {
        "n": 67,
        "wrTP1": 25.4,
        "nSL": 42,
        "nTO": 8,
        "expR": 0.339,
        "pf": 1.48,
        "mfe_p25": 70.0,
        "mfe_p50": 208.0,
        "mfe_p75": 1394.0,
        "winnerMAE_p75": 90.0,
        "winnerMAE_p90": 486.20000000000005,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -85.0,
        "revAfterSL_rate": 64.3,
        "ci90": {
          "expR": 0.339,
          "ci90": [
            -0.106,
            0.8
          ],
          "p_mean_le_0": 0.113,
          "n": 59
        }
      }
    }
  },
  "29/RETEST/SHORT": {
    "baseline": {
      "n": 444,
      "wrTP1": 52.9,
      "nSL": 189,
      "nTO": 20,
      "expR": 0.191,
      "pf": 1.43,
      "mfe_p25": 41.5,
      "mfe_p50": 160.5,
      "mfe_p75": 1154.5,
      "winnerMAE_p75": 284.0,
      "winnerMAE_p90": 4437.399999999997,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -236.5,
      "revAfterSL_rate": 78.3,
      "ci90": {
        "expR": 0.191,
        "ci90": [
          0.088,
          0.296
        ],
        "p_mean_le_0": 0.001,
        "n": 424
      }
    },
    "cuts": {
      "1.0": {
        "n": 164,
        "wrTP1": 38.4,
        "nSL": 92,
        "nTO": 9,
        "expR": 0.309,
        "pf": 1.52,
        "mfe_p25": 51.5,
        "mfe_p50": 182.0,
        "mfe_p75": 1158.0,
        "winnerMAE_p75": 339.0,
        "winnerMAE_p90": 2370.6000000000026,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -197.0,
        "revAfterSL_rate": 69.6,
        "ci90": {
          "expR": 0.309,
          "ci90": [
            0.069,
            0.558
          ],
          "p_mean_le_0": 0.022,
          "n": 155
        }
      },
      "1.2": {
        "n": 128,
        "wrTP1": 34.4,
        "nSL": 79,
        "nTO": 5,
        "expR": 0.269,
        "pf": 1.42,
        "mfe_p25": 54.5,
        "mfe_p50": 182.0,
        "mfe_p75": 1188.0,
        "winnerMAE_p75": 255.25,
        "winnerMAE_p90": 1010.7000000000014,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -203.0,
        "revAfterSL_rate": 69.6,
        "ci90": {
          "expR": 0.269,
          "ci90": [
            0.001,
            0.556
          ],
          "p_mean_le_0": 0.049,
          "n": 123
        }
      },
      "1.3": {
        "n": 118,
        "wrTP1": 33.1,
        "nSL": 75,
        "nTO": 4,
        "expR": 0.245,
        "pf": 1.37,
        "mfe_p25": 61.0,
        "mfe_p50": 191.5,
        "mfe_p75": 1229.75,
        "winnerMAE_p75": 281.5,
        "winnerMAE_p90": 1426.2000000000037,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -237.0,
        "revAfterSL_rate": 70.7,
        "ci90": {
          "expR": 0.245,
          "ci90": [
            -0.032,
            0.563
          ],
          "p_mean_le_0": 0.078,
          "n": 114
        }
      },
      "1.5": {
        "n": 96,
        "wrTP1": 31.2,
        "nSL": 63,
        "nTO": 3,
        "expR": 0.28,
        "pf": 1.41,
        "mfe_p25": 71.0,
        "mfe_p50": 182.0,
        "mfe_p75": 1211.0,
        "winnerMAE_p75": 236.25,
        "winnerMAE_p90": 504.50000000000017,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -203.0,
        "revAfterSL_rate": 68.3,
        "ci90": {
          "expR": 0.28,
          "ci90": [
            -0.072,
            0.626
          ],
          "p_mean_le_0": 0.096,
          "n": 93
        }
      },
      "2.0": {
        "n": 70,
        "wrTP1": 27.1,
        "nSL": 48,
        "nTO": 3,
        "expR": 0.246,
        "pf": 1.34,
        "mfe_p25": 60.0,
        "mfe_p50": 182.0,
        "mfe_p75": 1021.5,
        "winnerMAE_p75": 141.5,
        "winnerMAE_p90": 331.79999999999984,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -186.5,
        "revAfterSL_rate": 66.7,
        "ci90": {
          "expR": 0.246,
          "ci90": [
            -0.156,
            0.711
          ],
          "p_mean_le_0": 0.173,
          "n": 67
        }
      }
    }
  },
  "3/RETEST/LONG": {
    "baseline": {
      "n": 2518,
      "wrTP1": 54.8,
      "nSL": 1081,
      "nTO": 57,
      "expR": 0.112,
      "pf": 1.26,
      "mfe_p25": 12.0,
      "mfe_p50": 25.0,
      "mfe_p75": 55.0,
      "winnerMAE_p75": 18.0,
      "winnerMAE_p90": 41.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -23.0,
      "revAfterSL_rate": 52.6,
      "ci90": {
        "expR": 0.112,
        "ci90": [
          0.075,
          0.147
        ],
        "p_mean_le_0": 0.0,
        "n": 2474
      }
    },
    "cuts": {
      "1.0": {
        "n": 933,
        "wrTP1": 40.6,
        "nSL": 519,
        "nTO": 35,
        "expR": 0.171,
        "pf": 1.3,
        "mfe_p25": 18.0,
        "mfe_p50": 35.0,
        "mfe_p75": 74.5,
        "winnerMAE_p75": 17.5,
        "winnerMAE_p90": 45.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 45.1,
        "ci90": {
          "expR": 0.171,
          "ci90": [
            0.093,
            0.25
          ],
          "p_mean_le_0": 0.0,
          "n": 911
        }
      },
      "1.2": {
        "n": 720,
        "wrTP1": 37.6,
        "nSL": 419,
        "nTO": 30,
        "expR": 0.173,
        "pf": 1.29,
        "mfe_p25": 20.0,
        "mfe_p50": 37.0,
        "mfe_p75": 83.0,
        "winnerMAE_p75": 16.5,
        "winnerMAE_p90": 45.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -22.0,
        "revAfterSL_rate": 43.4,
        "ci90": {
          "expR": 0.173,
          "ci90": [
            0.079,
            0.272
          ],
          "p_mean_le_0": 0.001,
          "n": 702
        }
      },
      "1.3": {
        "n": 620,
        "wrTP1": 36.0,
        "nSL": 368,
        "nTO": 29,
        "expR": 0.173,
        "pf": 1.28,
        "mfe_p25": 21.0,
        "mfe_p50": 39.0,
        "mfe_p75": 86.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 46.60000000000002,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -22.0,
        "revAfterSL_rate": 42.1,
        "ci90": {
          "expR": 0.173,
          "ci90": [
            0.067,
            0.279
          ],
          "p_mean_le_0": 0.003,
          "n": 603
        }
      },
      "1.5": {
        "n": 454,
        "wrTP1": 33.9,
        "nSL": 278,
        "nTO": 22,
        "expR": 0.213,
        "pf": 1.34,
        "mfe_p25": 22.0,
        "mfe_p50": 41.0,
        "mfe_p75": 85.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 48.70000000000002,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -20.0,
        "revAfterSL_rate": 38.8,
        "ci90": {
          "expR": 0.213,
          "ci90": [
            0.084,
            0.347
          ],
          "p_mean_le_0": 0.003,
          "n": 442
        }
      },
      "2.0": {
        "n": 236,
        "wrTP1": 31.8,
        "nSL": 144,
        "nTO": 17,
        "expR": 0.347,
        "pf": 1.55,
        "mfe_p25": 26.0,
        "mfe_p50": 44.5,
        "mfe_p75": 85.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 22.000000000000043,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 29.9,
        "ci90": {
          "expR": 0.347,
          "ci90": [
            0.139,
            0.568
          ],
          "p_mean_le_0": 0.001,
          "n": 228
        }
      }
    }
  },
  "3/RETEST/SHORT": {
    "baseline": {
      "n": 2183,
      "wrTP1": 54.2,
      "nSL": 933,
      "nTO": 67,
      "expR": 0.128,
      "pf": 1.29,
      "mfe_p25": 12.0,
      "mfe_p50": 24.0,
      "mfe_p75": 56.0,
      "winnerMAE_p75": 18.0,
      "winnerMAE_p90": 44.0,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -25.0,
      "revAfterSL_rate": 55.7,
      "ci90": {
        "expR": 0.128,
        "ci90": [
          0.088,
          0.17
        ],
        "p_mean_le_0": 0.0,
        "n": 2130
      }
    },
    "cuts": {
      "1.0": {
        "n": 839,
        "wrTP1": 40.4,
        "nSL": 451,
        "nTO": 49,
        "expR": 0.206,
        "pf": 1.37,
        "mfe_p25": 16.0,
        "mfe_p50": 33.0,
        "mfe_p75": 74.0,
        "winnerMAE_p75": 19.5,
        "winnerMAE_p90": 38.599999999999966,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 47.9,
        "ci90": {
          "expR": 0.206,
          "ci90": [
            0.12,
            0.289
          ],
          "p_mean_le_0": 0.0,
          "n": 804
        }
      },
      "1.2": {
        "n": 637,
        "wrTP1": 35.3,
        "nSL": 370,
        "nTO": 42,
        "expR": 0.169,
        "pf": 1.28,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 78.25,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 52.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 46.8,
        "ci90": {
          "expR": 0.169,
          "ci90": [
            0.065,
            0.275
          ],
          "p_mean_le_0": 0.003,
          "n": 608
        }
      },
      "1.3": {
        "n": 554,
        "wrTP1": 33.6,
        "nSL": 329,
        "nTO": 39,
        "expR": 0.166,
        "pf": 1.27,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 79.25,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 49.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 43.8,
        "ci90": {
          "expR": 0.166,
          "ci90": [
            0.062,
            0.279
          ],
          "p_mean_le_0": 0.004,
          "n": 528
        }
      },
      "1.5": {
        "n": 442,
        "wrTP1": 31.2,
        "nSL": 270,
        "nTO": 34,
        "expR": 0.171,
        "pf": 1.27,
        "mfe_p25": 19.0,
        "mfe_p50": 42.0,
        "mfe_p75": 86.0,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 54.599999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.5,
        "revAfterSL_rate": 41.5,
        "ci90": {
          "expR": 0.171,
          "ci90": [
            0.037,
            0.304
          ],
          "p_mean_le_0": 0.018,
          "n": 421
        }
      },
      "2.0": {
        "n": 210,
        "wrTP1": 24.3,
        "nSL": 139,
        "nTO": 20,
        "expR": 0.164,
        "pf": 1.24,
        "mfe_p25": 21.0,
        "mfe_p50": 47.0,
        "mfe_p75": 100.0,
        "winnerMAE_p75": 21.5,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 14.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -31.5,
        "revAfterSL_rate": 31.7,
        "ci90": {
          "expR": 0.164,
          "ci90": [
            -0.058,
            0.372
          ],
          "p_mean_le_0": 0.104,
          "n": 201
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 4115,
      "wrTP1": 53.5,
      "nSL": 1754,
      "nTO": 161,
      "expR": 0.119,
      "pf": 1.27,
      "mfe_p25": 18.0,
      "mfe_p50": 48.0,
      "mfe_p75": 225.0,
      "winnerMAE_p75": 50.25,
      "winnerMAE_p90": 600.3000000000004,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -52.0,
      "revAfterSL_rate": 53.8,
      "ci90": {
        "expR": 0.119,
        "ci90": [
          0.088,
          0.149
        ],
        "p_mean_le_0": 0.0,
        "n": 3981
      }
    },
    "cuts": {
      "1.0": {
        "n": 1696,
        "wrTP1": 37.0,
        "nSL": 959,
        "nTO": 110,
        "expR": 0.168,
        "pf": 1.28,
        "mfe_p25": 24.0,
        "mfe_p50": 59.0,
        "mfe_p75": 243.25,
        "winnerMAE_p75": 42.0,
        "winnerMAE_p90": 473.39999999999986,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -41.0,
        "revAfterSL_rate": 47.7,
        "ci90": {
          "expR": 0.168,
          "ci90": [
            0.102,
            0.232
          ],
          "p_mean_le_0": 0.0,
          "n": 1612
        }
      },
      "1.2": {
        "n": 1378,
        "wrTP1": 34.7,
        "nSL": 799,
        "nTO": 101,
        "expR": 0.19,
        "pf": 1.31,
        "mfe_p25": 24.0,
        "mfe_p50": 59.0,
        "mfe_p75": 243.0,
        "winnerMAE_p75": 35.75,
        "winnerMAE_p90": 353.40000000000055,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -39.5,
        "revAfterSL_rate": 45.3,
        "ci90": {
          "expR": 0.19,
          "ci90": [
            0.115,
            0.263
          ],
          "p_mean_le_0": 0.0,
          "n": 1303
        }
      },
      "1.3": {
        "n": 1258,
        "wrTP1": 32.6,
        "nSL": 754,
        "nTO": 94,
        "expR": 0.171,
        "pf": 1.27,
        "mfe_p25": 24.0,
        "mfe_p50": 60.5,
        "mfe_p75": 251.75,
        "winnerMAE_p75": 37.0,
        "winnerMAE_p90": 391.400000000001,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -39.0,
        "revAfterSL_rate": 44.2,
        "ci90": {
          "expR": 0.171,
          "ci90": [
            0.092,
            0.249
          ],
          "p_mean_le_0": 0.0,
          "n": 1190
        }
      },
      "1.5": {
        "n": 1019,
        "wrTP1": 30.5,
        "nSL": 630,
        "nTO": 78,
        "expR": 0.182,
        "pf": 1.28,
        "mfe_p25": 24.0,
        "mfe_p50": 61.0,
        "mfe_p75": 259.75,
        "winnerMAE_p75": 33.5,
        "winnerMAE_p90": 334.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -38.0,
        "revAfterSL_rate": 42.9,
        "ci90": {
          "expR": 0.182,
          "ci90": [
            0.092,
            0.272
          ],
          "p_mean_le_0": 0.0,
          "n": 966
        }
      },
      "2.0": {
        "n": 639,
        "wrTP1": 24.3,
        "nSL": 424,
        "nTO": 60,
        "expR": 0.15,
        "pf": 1.21,
        "mfe_p25": 26.0,
        "mfe_p50": 66.0,
        "mfe_p75": 243.0,
        "winnerMAE_p75": 30.0,
        "winnerMAE_p90": 337.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -38.0,
        "revAfterSL_rate": 35.1,
        "ci90": {
          "expR": 0.15,
          "ci90": [
            0.025,
            0.279
          ],
          "p_mean_le_0": 0.025,
          "n": 603
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 2929,
      "wrTP1": 52.2,
      "nSL": 1256,
      "nTO": 144,
      "expR": 0.1,
      "pf": 1.22,
      "mfe_p25": 20.0,
      "mfe_p50": 53.0,
      "mfe_p75": 274.25,
      "winnerMAE_p75": 52.0,
      "winnerMAE_p90": 751.6000000000017,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -53.5,
      "revAfterSL_rate": 51.5,
      "ci90": {
        "expR": 0.1,
        "ci90": [
          0.064,
          0.138
        ],
        "p_mean_le_0": 0.0,
        "n": 2804
      }
    },
    "cuts": {
      "1.0": {
        "n": 1238,
        "wrTP1": 34.2,
        "nSL": 724,
        "nTO": 91,
        "expR": 0.112,
        "pf": 1.18,
        "mfe_p25": 26.0,
        "mfe_p50": 64.0,
        "mfe_p75": 300.0,
        "winnerMAE_p75": 44.0,
        "winnerMAE_p90": 606.800000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -46.0,
        "revAfterSL_rate": 44.6,
        "ci90": {
          "expR": 0.112,
          "ci90": [
            0.033,
            0.188
          ],
          "p_mean_le_0": 0.008,
          "n": 1165
        }
      },
      "1.2": {
        "n": 1004,
        "wrTP1": 30.6,
        "nSL": 622,
        "nTO": 75,
        "expR": 0.095,
        "pf": 1.14,
        "mfe_p25": 27.0,
        "mfe_p50": 64.0,
        "mfe_p75": 299.75,
        "winnerMAE_p75": 46.0,
        "winnerMAE_p90": 642.8000000000015,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -46.5,
        "revAfterSL_rate": 41.6,
        "ci90": {
          "expR": 0.095,
          "ci90": [
            0.004,
            0.19
          ],
          "p_mean_le_0": 0.042,
          "n": 946
        }
      },
      "1.3": {
        "n": 911,
        "wrTP1": 28.8,
        "nSL": 579,
        "nTO": 70,
        "expR": 0.07,
        "pf": 1.1,
        "mfe_p25": 27.0,
        "mfe_p50": 63.5,
        "mfe_p75": 293.25,
        "winnerMAE_p75": 44.0,
        "winnerMAE_p90": 239.80000000000024,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -46.0,
        "revAfterSL_rate": 41.8,
        "ci90": {
          "expR": 0.07,
          "ci90": [
            -0.027,
            0.164
          ],
          "p_mean_le_0": 0.113,
          "n": 858
        }
      },
      "1.5": {
        "n": 747,
        "wrTP1": 26.8,
        "nSL": 481,
        "nTO": 66,
        "expR": 0.084,
        "pf": 1.12,
        "mfe_p25": 27.0,
        "mfe_p50": 64.0,
        "mfe_p75": 289.75,
        "winnerMAE_p75": 43.25,
        "winnerMAE_p90": 180.0999999999996,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -45.0,
        "revAfterSL_rate": 38.3,
        "ci90": {
          "expR": 0.084,
          "ci90": [
            -0.028,
            0.197
          ],
          "p_mean_le_0": 0.112,
          "n": 698
        }
      },
      "2.0": {
        "n": 481,
        "wrTP1": 20.2,
        "nSL": 334,
        "nTO": 50,
        "expR": 0.031,
        "pf": 1.04,
        "mfe_p25": 30.0,
        "mfe_p50": 67.0,
        "mfe_p75": 243.5,
        "winnerMAE_p75": 41.0,
        "winnerMAE_p90": 136.40000000000003,
        "loserMFEbeforeSL_p50": 13.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -48.0,
        "revAfterSL_rate": 34.1,
        "ci90": {
          "expR": 0.031,
          "ci90": [
            -0.121,
            0.184
          ],
          "p_mean_le_0": 0.383,
          "n": 447
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
    "2026-W45",
    "2026-W46"
  ],
  "1/RETEST/LONG": {
    "baseline": {
      "n": 2439,
      "wrTP1": 46.1,
      "nSL": 1126,
      "nTO": 189,
      "expR": 0.086,
      "pf": 1.18,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 50.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 31.0,
      "loserMFEbeforeSL_p50": 6.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 30.2,
      "ci90": {
        "expR": 0.086,
        "ci90": [
          0.044,
          0.13
        ],
        "p_mean_le_0": 0.0,
        "n": 2346
      }
    },
    "cuts": {
      "1.2": {
        "n": 1072,
        "wrTP1": 29.1,
        "nSL": 616,
        "nTO": 144,
        "expR": 0.16,
        "pf": 1.26,
        "mfe_p25": 13.25,
        "mfe_p50": 31.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 30.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 18.2,
        "ci90": {
          "expR": 0.16,
          "ci90": [
            0.078,
            0.246
          ],
          "p_mean_le_0": 0.001,
          "n": 1014
        }
      },
      "1.3": {
        "n": 980,
        "wrTP1": 27.7,
        "nSL": 571,
        "nTO": 138,
        "expR": 0.167,
        "pf": 1.27,
        "mfe_p25": 14.0,
        "mfe_p50": 32.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 16.8,
        "ci90": {
          "expR": 0.167,
          "ci90": [
            0.077,
            0.259
          ],
          "p_mean_le_0": 0.0,
          "n": 926
        }
      },
      "1.5": {
        "n": 808,
        "wrTP1": 24.8,
        "nSL": 483,
        "nTO": 125,
        "expR": 0.185,
        "pf": 1.29,
        "mfe_p25": 14.0,
        "mfe_p50": 32.0,
        "mfe_p75": 64.0,
        "winnerMAE_p75": 12.25,
        "winnerMAE_p90": 21.299999999999983,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 14.7,
        "ci90": {
          "expR": 0.185,
          "ci90": [
            0.083,
            0.294
          ],
          "p_mean_le_0": 0.002,
          "n": 763
        }
      },
      "2.0": {
        "n": 550,
        "wrTP1": 19.1,
        "nSL": 345,
        "nTO": 100,
        "expR": 0.208,
        "pf": 1.31,
        "mfe_p25": 12.0,
        "mfe_p50": 33.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 24.000000000000043,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 10.7,
        "ci90": {
          "expR": 0.208,
          "ci90": [
            0.074,
            0.346
          ],
          "p_mean_le_0": 0.001,
          "n": 522
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 2451,
      "wrTP1": 47.5,
      "nSL": 1125,
      "nTO": 162,
      "expR": 0.075,
      "pf": 1.16,
      "mfe_p25": 10.0,
      "mfe_p50": 20.0,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 26.700000000000045,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 32.6,
      "ci90": {
        "expR": 0.075,
        "ci90": [
          0.031,
          0.12
        ],
        "p_mean_le_0": 0.002,
        "n": 2373
      }
    },
    "cuts": {
      "1.2": {
        "n": 998,
        "wrTP1": 29.7,
        "nSL": 580,
        "nTO": 122,
        "expR": 0.154,
        "pf": 1.25,
        "mfe_p25": 14.0,
        "mfe_p50": 31.0,
        "mfe_p75": 65.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.5,
        "ci90": {
          "expR": 0.154,
          "ci90": [
            0.068,
            0.249
          ],
          "p_mean_le_0": 0.002,
          "n": 949
        }
      },
      "1.3": {
        "n": 925,
        "wrTP1": 28.8,
        "nSL": 539,
        "nTO": 120,
        "expR": 0.169,
        "pf": 1.27,
        "mfe_p25": 14.0,
        "mfe_p50": 31.5,
        "mfe_p75": 65.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 30.5,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.7,
        "ci90": {
          "expR": 0.169,
          "ci90": [
            0.075,
            0.27
          ],
          "p_mean_le_0": 0.001,
          "n": 878
        }
      },
      "1.5": {
        "n": 791,
        "wrTP1": 26.9,
        "nSL": 467,
        "nTO": 111,
        "expR": 0.193,
        "pf": 1.31,
        "mfe_p25": 14.0,
        "mfe_p50": 34.0,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 29.80000000000001,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.6,
        "ci90": {
          "expR": 0.193,
          "ci90": [
            0.082,
            0.298
          ],
          "p_mean_le_0": 0.001,
          "n": 751
        }
      },
      "2.0": {
        "n": 521,
        "wrTP1": 21.3,
        "nSL": 321,
        "nTO": 89,
        "expR": 0.217,
        "pf": 1.33,
        "mfe_p25": 13.75,
        "mfe_p50": 36.0,
        "mfe_p75": 69.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 13.4,
        "ci90": {
          "expR": 0.217,
          "ci90": [
            0.072,
            0.366
          ],
          "p_mean_le_0": 0.005,
          "n": 496
        }
      }
    }
  },
  "15/RETEST/LONG": {
    "baseline": {
      "n": 523,
      "wrTP1": 51.8,
      "nSL": 228,
      "nTO": 24,
      "expR": 0.124,
      "pf": 1.27,
      "mfe_p25": 44.5,
      "mfe_p50": 126.0,
      "mfe_p75": 849.5,
      "winnerMAE_p75": 316.0,
      "winnerMAE_p90": 4601.0,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -209.0,
      "revAfterSL_rate": 64.5,
      "ci90": {
        "expR": 0.124,
        "ci90": [
          0.034,
          0.213
        ],
        "p_mean_le_0": 0.011,
        "n": 499
      }
    },
    "cuts": {
      "1.2": {
        "n": 177,
        "wrTP1": 27.7,
        "nSL": 115,
        "nTO": 13,
        "expR": -0.003,
        "pf": 1.0,
        "mfe_p25": 57.25,
        "mfe_p50": 152.0,
        "mfe_p75": 961.5,
        "winnerMAE_p75": 602.0,
        "winnerMAE_p90": 4036.000000000002,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -138.0,
        "revAfterSL_rate": 52.2,
        "ci90": {
          "expR": -0.003,
          "ci90": [
            -0.209,
            0.201
          ],
          "p_mean_le_0": 0.527,
          "n": 164
        }
      },
      "1.3": {
        "n": 155,
        "wrTP1": 27.1,
        "nSL": 103,
        "nTO": 10,
        "expR": -0.004,
        "pf": 0.99,
        "mfe_p25": 55.0,
        "mfe_p50": 154.0,
        "mfe_p75": 950.0,
        "winnerMAE_p75": 1011.5,
        "winnerMAE_p90": 3766.8999999999983,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -139.0,
        "revAfterSL_rate": 51.5,
        "ci90": {
          "expR": -0.004,
          "ci90": [
            -0.218,
            0.209
          ],
          "p_mean_le_0": 0.526,
          "n": 145
        }
      },
      "1.5": {
        "n": 125,
        "wrTP1": 26.4,
        "nSL": 83,
        "nTO": 9,
        "expR": 0.031,
        "pf": 1.04,
        "mfe_p25": 68.0,
        "mfe_p50": 170.0,
        "mfe_p75": 938.25,
        "winnerMAE_p75": 1148.0,
        "winnerMAE_p90": 2559.7999999999997,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -118.0,
        "revAfterSL_rate": 47.0,
        "ci90": {
          "expR": 0.031,
          "ci90": [
            -0.226,
            0.316
          ],
          "p_mean_le_0": 0.427,
          "n": 116
        }
      },
      "2.0": {
        "n": 75,
        "wrTP1": 24.0,
        "nSL": 51,
        "nTO": 6,
        "expR": 0.063,
        "pf": 1.09,
        "mfe_p25": 69.0,
        "mfe_p50": 284.0,
        "mfe_p75": 6040.0,
        "winnerMAE_p75": 1168.25,
        "winnerMAE_p90": 2536.8,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -100.0,
        "revAfterSL_rate": 43.1,
        "ci90": {
          "expR": 0.063,
          "ci90": [
            -0.29,
            0.431
          ],
          "p_mean_le_0": 0.401,
          "n": 69
        }
      }
    }
  },
  "15/RETEST/SHORT": {
    "baseline": {
      "n": 473,
      "wrTP1": 52.4,
      "nSL": 201,
      "nTO": 24,
      "expR": 0.251,
      "pf": 1.56,
      "mfe_p25": 38.0,
      "mfe_p50": 122.0,
      "mfe_p75": 762.75,
      "winnerMAE_p75": 184.5,
      "winnerMAE_p90": 3721.0000000000014,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -165.0,
      "revAfterSL_rate": 62.7,
      "ci90": {
        "expR": 0.251,
        "ci90": [
          0.131,
          0.379
        ],
        "p_mean_le_0": 0.0,
        "n": 450
      }
    },
    "cuts": {
      "1.2": {
        "n": 158,
        "wrTP1": 38.6,
        "nSL": 87,
        "nTO": 10,
        "expR": 0.527,
        "pf": 1.9,
        "mfe_p25": 49.0,
        "mfe_p50": 139.0,
        "mfe_p75": 719.0,
        "winnerMAE_p75": 129.0,
        "winnerMAE_p90": 357.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -201.0,
        "revAfterSL_rate": 57.5,
        "ci90": {
          "expR": 0.527,
          "ci90": [
            0.224,
            0.88
          ],
          "p_mean_le_0": 0.002,
          "n": 149
        }
      },
      "1.3": {
        "n": 141,
        "wrTP1": 36.2,
        "nSL": 81,
        "nTO": 9,
        "expR": 0.526,
        "pf": 1.86,
        "mfe_p25": 52.0,
        "mfe_p50": 151.0,
        "mfe_p75": 719.0,
        "winnerMAE_p75": 91.0,
        "winnerMAE_p90": 186.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -200.0,
        "revAfterSL_rate": 56.8,
        "ci90": {
          "expR": 0.526,
          "ci90": [
            0.178,
            0.881
          ],
          "p_mean_le_0": 0.004,
          "n": 133
        }
      },
      "1.5": {
        "n": 115,
        "wrTP1": 33.0,
        "nSL": 69,
        "nTO": 8,
        "expR": 0.549,
        "pf": 1.86,
        "mfe_p25": 60.75,
        "mfe_p50": 152.5,
        "mfe_p75": 633.5,
        "winnerMAE_p75": 58.75,
        "winnerMAE_p90": 147.10000000000014,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -186.0,
        "revAfterSL_rate": 55.1,
        "ci90": {
          "expR": 0.549,
          "ci90": [
            0.14,
            0.997
          ],
          "p_mean_le_0": 0.01,
          "n": 108
        }
      },
      "2.0": {
        "n": 69,
        "wrTP1": 33.3,
        "nSL": 40,
        "nTO": 6,
        "expR": 0.923,
        "pf": 2.47,
        "mfe_p25": 52.75,
        "mfe_p50": 128.5,
        "mfe_p75": 633.5,
        "winnerMAE_p75": 39.5,
        "winnerMAE_p90": 80.60000000000002,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -170.0,
        "revAfterSL_rate": 42.5,
        "ci90": {
          "expR": 0.923,
          "ci90": [
            0.28,
            1.662
          ],
          "p_mean_le_0": 0.005,
          "n": 64
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 1175,
      "wrTP1": 50.0,
      "nSL": 532,
      "nTO": 56,
      "expR": 0.101,
      "pf": 1.21,
      "mfe_p25": 12.0,
      "mfe_p50": 25.0,
      "mfe_p75": 54.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 40.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -22.0,
      "revAfterSL_rate": 42.7,
      "ci90": {
        "expR": 0.101,
        "ci90": [
          0.04,
          0.166
        ],
        "p_mean_le_0": 0.002,
        "n": 1137
      }
    },
    "cuts": {
      "1.2": {
        "n": 445,
        "wrTP1": 32.1,
        "nSL": 261,
        "nTO": 41,
        "expR": 0.194,
        "pf": 1.31,
        "mfe_p25": 17.0,
        "mfe_p50": 33.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 33.0,
        "ci90": {
          "expR": 0.194,
          "ci90": [
            0.054,
            0.332
          ],
          "p_mean_le_0": 0.011,
          "n": 421
        }
      },
      "1.3": {
        "n": 409,
        "wrTP1": 31.1,
        "nSL": 243,
        "nTO": 39,
        "expR": 0.204,
        "pf": 1.32,
        "mfe_p25": 17.0,
        "mfe_p50": 34.0,
        "mfe_p75": 67.75,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 24.400000000000006,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 32.9,
        "ci90": {
          "expR": 0.204,
          "ci90": [
            0.065,
            0.354
          ],
          "p_mean_le_0": 0.007,
          "n": 386
        }
      },
      "1.5": {
        "n": 348,
        "wrTP1": 29.9,
        "nSL": 208,
        "nTO": 36,
        "expR": 0.246,
        "pf": 1.38,
        "mfe_p25": 19.0,
        "mfe_p50": 34.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 11.25,
        "winnerMAE_p90": 19.700000000000003,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 30.8,
        "ci90": {
          "expR": 0.246,
          "ci90": [
            0.086,
            0.411
          ],
          "p_mean_le_0": 0.005,
          "n": 327
        }
      },
      "2.0": {
        "n": 205,
        "wrTP1": 25.9,
        "nSL": 127,
        "nTO": 25,
        "expR": 0.362,
        "pf": 1.55,
        "mfe_p25": 19.75,
        "mfe_p50": 39.0,
        "mfe_p75": 74.25,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 16.800000000000004,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 24.4,
        "ci90": {
          "expR": 0.362,
          "ci90": [
            0.114,
            0.622
          ],
          "p_mean_le_0": 0.01,
          "n": 192
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 1010,
      "wrTP1": 50.0,
      "nSL": 464,
      "nTO": 41,
      "expR": 0.092,
      "pf": 1.2,
      "mfe_p25": 13.0,
      "mfe_p50": 26.0,
      "mfe_p75": 58.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 28.600000000000023,
      "loserMFEbeforeSL_p50": 7.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -20.0,
      "revAfterSL_rate": 39.7,
      "ci90": {
        "expR": 0.092,
        "ci90": [
          0.027,
          0.16
        ],
        "p_mean_le_0": 0.011,
        "n": 985
      }
    },
    "cuts": {
      "1.2": {
        "n": 421,
        "wrTP1": 27.1,
        "nSL": 278,
        "nTO": 29,
        "expR": 0.011,
        "pf": 1.02,
        "mfe_p25": 20.0,
        "mfe_p50": 42.0,
        "mfe_p75": 82.5,
        "winnerMAE_p75": 16.75,
        "winnerMAE_p90": 25.700000000000003,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 32.0,
        "ci90": {
          "expR": 0.011,
          "ci90": [
            -0.12,
            0.154
          ],
          "p_mean_le_0": 0.458,
          "n": 407
        }
      },
      "1.3": {
        "n": 388,
        "wrTP1": 26.3,
        "nSL": 259,
        "nTO": 27,
        "expR": 0.022,
        "pf": 1.03,
        "mfe_p25": 20.0,
        "mfe_p50": 43.0,
        "mfe_p75": 83.25,
        "winnerMAE_p75": 16.75,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 30.1,
        "ci90": {
          "expR": 0.022,
          "ci90": [
            -0.121,
            0.167
          ],
          "p_mean_le_0": 0.43,
          "n": 376
        }
      },
      "1.5": {
        "n": 331,
        "wrTP1": 25.4,
        "nSL": 221,
        "nTO": 26,
        "expR": 0.063,
        "pf": 1.09,
        "mfe_p25": 21.0,
        "mfe_p50": 47.0,
        "mfe_p75": 94.25,
        "winnerMAE_p75": 16.25,
        "winnerMAE_p90": 25.700000000000003,
        "loserMFEbeforeSL_p50": 11.0,
        "bars_win_p50": 5.5,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 27.6,
        "ci90": {
          "expR": 0.063,
          "ci90": [
            -0.104,
            0.232
          ],
          "p_mean_le_0": 0.286,
          "n": 320
        }
      },
      "2.0": {
        "n": 217,
        "wrTP1": 21.2,
        "nSL": 149,
        "nTO": 22,
        "expR": 0.112,
        "pf": 1.16,
        "mfe_p25": 23.0,
        "mfe_p50": 51.5,
        "mfe_p75": 104.75,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 12.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -24.0,
        "revAfterSL_rate": 22.1,
        "ci90": {
          "expR": 0.112,
          "ci90": [
            -0.11,
            0.341
          ],
          "p_mean_le_0": 0.199,
          "n": 208
        }
      }
    }
  },
  "29/RETEST/LONG": {
    "baseline": {
      "n": 262,
      "wrTP1": 59.5,
      "nSL": 89,
      "nTO": 17,
      "expR": 0.387,
      "pf": 2.06,
      "mfe_p25": 44.0,
      "mfe_p50": 117.0,
      "mfe_p75": 815.0,
      "winnerMAE_p75": 206.75,
      "winnerMAE_p90": 2283.0,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -154.0,
      "revAfterSL_rate": 64.0,
      "ci90": {
        "expR": 0.387,
        "ci90": [
          0.246,
          0.535
        ],
        "p_mean_le_0": 0.0,
        "n": 245
      }
    },
    "cuts": {
      "1.2": {
        "n": 90,
        "wrTP1": 35.6,
        "nSL": 45,
        "nTO": 13,
        "expR": 0.415,
        "pf": 1.71,
        "mfe_p25": 59.0,
        "mfe_p50": 165.0,
        "mfe_p75": 1287.0,
        "winnerMAE_p75": 207.5,
        "winnerMAE_p90": 1170.8000000000006,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -127.0,
        "revAfterSL_rate": 48.9,
        "ci90": {
          "expR": 0.415,
          "ci90": [
            0.063,
            0.78
          ],
          "p_mean_le_0": 0.024,
          "n": 77
        }
      },
      "1.3": {
        "n": 79,
        "wrTP1": 30.4,
        "nSL": 44,
        "nTO": 11,
        "expR": 0.322,
        "pf": 1.5,
        "mfe_p25": 58.5,
        "mfe_p50": 173.0,
        "mfe_p75": 1764.5,
        "winnerMAE_p75": 424.5,
        "winnerMAE_p90": 1124.3999999999999,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -141.0,
        "revAfterSL_rate": 47.7,
        "ci90": {
          "expR": 0.322,
          "ci90": [
            -0.065,
            0.703
          ],
          "p_mean_le_0": 0.087,
          "n": 68
        }
      },
      "1.5": {
        "n": 69,
        "wrTP1": 27.5,
        "nSL": 40,
        "nTO": 10,
        "expR": 0.298,
        "pf": 1.44,
        "mfe_p25": 58.0,
        "mfe_p50": 165.0,
        "mfe_p75": 1095.0,
        "winnerMAE_p75": 116.5,
        "winnerMAE_p90": 729.9999999999995,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -110.0,
        "revAfterSL_rate": 47.5,
        "ci90": {
          "expR": 0.298,
          "ci90": [
            -0.131,
            0.722
          ],
          "p_mean_le_0": 0.134,
          "n": 59
        }
      },
      "2.0": {
        "n": 50,
        "wrTP1": 22.0,
        "nSL": 31,
        "nTO": 8,
        "expR": 0.267,
        "pf": 1.36,
        "mfe_p25": 69.5,
        "mfe_p50": 221.5,
        "mfe_p75": 1923.25,
        "winnerMAE_p75": 116.5,
        "winnerMAE_p90": 401.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -125.5,
        "revAfterSL_rate": 58.1,
        "ci90": {
          "expR": 0.267,
          "ci90": [
            -0.263,
            0.892
          ],
          "p_mean_le_0": 0.21,
          "n": 42
        }
      }
    }
  },
  "29/RETEST/SHORT": {
    "baseline": {
      "n": 270,
      "wrTP1": 51.1,
      "nSL": 113,
      "nTO": 19,
      "expR": 0.225,
      "pf": 1.5,
      "mfe_p25": 48.5,
      "mfe_p50": 171.0,
      "mfe_p75": 1158.0,
      "winnerMAE_p75": 416.5,
      "winnerMAE_p90": 4809.799999999999,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -202.5,
      "revAfterSL_rate": 82.3,
      "ci90": {
        "expR": 0.225,
        "ci90": [
          0.082,
          0.374
        ],
        "p_mean_le_0": 0.002,
        "n": 251
      }
    },
    "cuts": {
      "1.2": {
        "n": 87,
        "wrTP1": 34.5,
        "nSL": 52,
        "nTO": 5,
        "expR": 0.331,
        "pf": 1.52,
        "mfe_p25": 61.0,
        "mfe_p50": 196.0,
        "mfe_p75": 1146.25,
        "winnerMAE_p75": 203.5,
        "winnerMAE_p90": 629.4,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -191.0,
        "revAfterSL_rate": 78.8,
        "ci90": {
          "expR": 0.331,
          "ci90": [
            -0.019,
            0.693
          ],
          "p_mean_le_0": 0.06,
          "n": 82
        }
      },
      "1.3": {
        "n": 81,
        "wrTP1": 33.3,
        "nSL": 50,
        "nTO": 4,
        "expR": 0.291,
        "pf": 1.45,
        "mfe_p25": 60.0,
        "mfe_p50": 205.0,
        "mfe_p75": 1165.0,
        "winnerMAE_p75": 246.0,
        "winnerMAE_p90": 639.6000000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -197.0,
        "revAfterSL_rate": 80.0,
        "ci90": {
          "expR": 0.291,
          "ci90": [
            -0.075,
            0.668
          ],
          "p_mean_le_0": 0.098,
          "n": 77
        }
      },
      "1.5": {
        "n": 67,
        "wrTP1": 29.9,
        "nSL": 44,
        "nTO": 3,
        "expR": 0.289,
        "pf": 1.42,
        "mfe_p25": 69.25,
        "mfe_p50": 218.0,
        "mfe_p75": 1545.0,
        "winnerMAE_p75": 128.5,
        "winnerMAE_p90": 504.50000000000017,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -197.0,
        "revAfterSL_rate": 79.5,
        "ci90": {
          "expR": 0.289,
          "ci90": [
            -0.13,
            0.727
          ],
          "p_mean_le_0": 0.131,
          "n": 64
        }
      },
      "2.0": {
        "n": 53,
        "wrTP1": 28.3,
        "nSL": 35,
        "nTO": 3,
        "expR": 0.333,
        "pf": 1.48,
        "mfe_p25": 65.75,
        "mfe_p50": 207.0,
        "mfe_p75": 1124.75,
        "winnerMAE_p75": 74.0,
        "winnerMAE_p90": 394.5999999999999,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -159.0,
        "revAfterSL_rate": 77.1,
        "ci90": {
          "expR": 0.333,
          "ci90": [
            -0.191,
            0.881
          ],
          "p_mean_le_0": 0.149,
          "n": 50
        }
      }
    }
  },
  "3/RETEST/LONG": {
    "baseline": {
      "n": 1740,
      "wrTP1": 55.2,
      "nSL": 729,
      "nTO": 50,
      "expR": 0.128,
      "pf": 1.3,
      "mfe_p25": 14.0,
      "mfe_p50": 26.0,
      "mfe_p75": 58.0,
      "winnerMAE_p75": 19.0,
      "winnerMAE_p90": 45.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -28.0,
      "revAfterSL_rate": 52.0,
      "ci90": {
        "expR": 0.128,
        "ci90": [
          0.082,
          0.172
        ],
        "p_mean_le_0": 0.0,
        "n": 1701
      }
    },
    "cuts": {
      "1.2": {
        "n": 516,
        "wrTP1": 38.2,
        "nSL": 292,
        "nTO": 27,
        "expR": 0.198,
        "pf": 1.34,
        "mfe_p25": 20.0,
        "mfe_p50": 37.0,
        "mfe_p75": 85.5,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 45.80000000000001,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -25.0,
        "revAfterSL_rate": 41.8,
        "ci90": {
          "expR": 0.198,
          "ci90": [
            0.083,
            0.316
          ],
          "p_mean_le_0": 0.002,
          "n": 499
        }
      },
      "1.3": {
        "n": 445,
        "wrTP1": 36.0,
        "nSL": 259,
        "nTO": 26,
        "expR": 0.188,
        "pf": 1.31,
        "mfe_p25": 21.0,
        "mfe_p50": 40.0,
        "mfe_p75": 88.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 47.099999999999994,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -25.0,
        "revAfterSL_rate": 40.2,
        "ci90": {
          "expR": 0.188,
          "ci90": [
            0.065,
            0.314
          ],
          "p_mean_le_0": 0.005,
          "n": 429
        }
      },
      "1.5": {
        "n": 324,
        "wrTP1": 32.7,
        "nSL": 198,
        "nTO": 20,
        "expR": 0.204,
        "pf": 1.32,
        "mfe_p25": 22.0,
        "mfe_p50": 40.0,
        "mfe_p75": 86.0,
        "winnerMAE_p75": 16.75,
        "winnerMAE_p90": 46.5,
        "loserMFEbeforeSL_p50": 6.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -22.5,
        "revAfterSL_rate": 37.9,
        "ci90": {
          "expR": 0.204,
          "ci90": [
            0.046,
            0.363
          ],
          "p_mean_le_0": 0.016,
          "n": 312
        }
      },
      "2.0": {
        "n": 164,
        "wrTP1": 31.7,
        "nSL": 97,
        "nTO": 15,
        "expR": 0.387,
        "pf": 1.62,
        "mfe_p25": 25.75,
        "mfe_p50": 43.0,
        "mfe_p75": 82.5,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 24.7,
        "ci90": {
          "expR": 0.387,
          "ci90": [
            0.132,
            0.638
          ],
          "p_mean_le_0": 0.005,
          "n": 156
        }
      }
    }
  },
  "3/RETEST/SHORT": {
    "baseline": {
      "n": 1445,
      "wrTP1": 53.7,
      "nSL": 615,
      "nTO": 54,
      "expR": 0.133,
      "pf": 1.3,
      "mfe_p25": 12.0,
      "mfe_p50": 26.0,
      "mfe_p75": 60.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 47.5,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -28.0,
      "revAfterSL_rate": 54.8,
      "ci90": {
        "expR": 0.133,
        "ci90": [
          0.085,
          0.183
        ],
        "p_mean_le_0": 0.0,
        "n": 1399
      }
    },
    "cuts": {
      "1.2": {
        "n": 448,
        "wrTP1": 35.0,
        "nSL": 260,
        "nTO": 31,
        "expR": 0.157,
        "pf": 1.26,
        "mfe_p25": 17.0,
        "mfe_p50": 40.0,
        "mfe_p75": 90.0,
        "winnerMAE_p75": 25.0,
        "winnerMAE_p90": 61.60000000000002,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 45.4,
        "ci90": {
          "expR": 0.157,
          "ci90": [
            0.037,
            0.285
          ],
          "p_mean_le_0": 0.018,
          "n": 424
        }
      },
      "1.3": {
        "n": 390,
        "wrTP1": 32.8,
        "nSL": 234,
        "nTO": 28,
        "expR": 0.139,
        "pf": 1.22,
        "mfe_p25": 18.0,
        "mfe_p50": 42.0,
        "mfe_p75": 95.0,
        "winnerMAE_p75": 23.75,
        "winnerMAE_p90": 59.3,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 42.7,
        "ci90": {
          "expR": 0.139,
          "ci90": [
            0.002,
            0.273
          ],
          "p_mean_le_0": 0.045,
          "n": 369
        }
      },
      "1.5": {
        "n": 306,
        "wrTP1": 31.7,
        "nSL": 185,
        "nTO": 24,
        "expR": 0.179,
        "pf": 1.28,
        "mfe_p25": 21.0,
        "mfe_p50": 47.0,
        "mfe_p75": 100.0,
        "winnerMAE_p75": 26.0,
        "winnerMAE_p90": 64.4,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -31.5,
        "revAfterSL_rate": 41.6,
        "ci90": {
          "expR": 0.179,
          "ci90": [
            0.015,
            0.337
          ],
          "p_mean_le_0": 0.034,
          "n": 289
        }
      },
      "2.0": {
        "n": 142,
        "wrTP1": 21.1,
        "nSL": 97,
        "nTO": 15,
        "expR": 0.065,
        "pf": 1.09,
        "mfe_p25": 26.0,
        "mfe_p50": 50.5,
        "mfe_p75": 121.75,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 62.500000000000036,
        "loserMFEbeforeSL_p50": 15.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.5,
        "revAfterSL_rate": 35.1,
        "ci90": {
          "expR": 0.065,
          "ci90": [
            -0.192,
            0.324
          ],
          "p_mean_le_0": 0.332,
          "n": 134
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 1098,
      "wrTP1": 53.1,
      "nSL": 480,
      "nTO": 35,
      "expR": 0.145,
      "pf": 1.32,
      "mfe_p25": 56.25,
      "mfe_p50": 324.0,
      "mfe_p75": 2698.25,
      "winnerMAE_p75": 398.5,
      "winnerMAE_p90": 4174.600000000009,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -450.0,
      "revAfterSL_rate": 59.2,
      "ci90": {
        "expR": 0.145,
        "ci90": [
          0.085,
          0.204
        ],
        "p_mean_le_0": 0.0,
        "n": 1074
      }
    },
    "cuts": {
      "1.2": {
        "n": 374,
        "wrTP1": 35.0,
        "nSL": 216,
        "nTO": 27,
        "expR": 0.239,
        "pf": 1.39,
        "mfe_p25": 54.25,
        "mfe_p50": 343.0,
        "mfe_p75": 1806.0,
        "winnerMAE_p75": 336.5,
        "winnerMAE_p90": 3161.0,
        "loserMFEbeforeSL_p50": 9.5,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -226.5,
        "revAfterSL_rate": 49.5,
        "ci90": {
          "expR": 0.239,
          "ci90": [
            0.086,
            0.39
          ],
          "p_mean_le_0": 0.004,
          "n": 358
        }
      },
      "1.3": {
        "n": 352,
        "wrTP1": 34.4,
        "nSL": 206,
        "nTO": 25,
        "expR": 0.245,
        "pf": 1.4,
        "mfe_p25": 53.25,
        "mfe_p50": 355.5,
        "mfe_p75": 1996.5,
        "winnerMAE_p75": 431.0,
        "winnerMAE_p90": 3199.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -215.0,
        "revAfterSL_rate": 47.6,
        "ci90": {
          "expR": 0.245,
          "ci90": [
            0.083,
            0.403
          ],
          "p_mean_le_0": 0.005,
          "n": 338
        }
      },
      "1.5": {
        "n": 281,
        "wrTP1": 30.2,
        "nSL": 173,
        "nTO": 23,
        "expR": 0.227,
        "pf": 1.35,
        "mfe_p25": 57.0,
        "mfe_p50": 385.0,
        "mfe_p75": 2307.0,
        "winnerMAE_p75": 339.0,
        "winnerMAE_p90": 3408.4,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -228.0,
        "revAfterSL_rate": 45.1,
        "ci90": {
          "expR": 0.227,
          "ci90": [
            0.043,
            0.409
          ],
          "p_mean_le_0": 0.02,
          "n": 269
        }
      },
      "2.0": {
        "n": 175,
        "wrTP1": 23.4,
        "nSL": 114,
        "nTO": 20,
        "expR": 0.235,
        "pf": 1.34,
        "mfe_p25": 59.0,
        "mfe_p50": 340.0,
        "mfe_p75": 1802.5,
        "winnerMAE_p75": 339.0,
        "winnerMAE_p90": 1499.0,
        "loserMFEbeforeSL_p50": 11.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -160.0,
        "revAfterSL_rate": 37.7,
        "ci90": {
          "expR": 0.235,
          "ci90": [
            -0.025,
            0.498
          ],
          "p_mean_le_0": 0.069,
          "n": 166
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 855,
      "wrTP1": 52.9,
      "nSL": 367,
      "nTO": 36,
      "expR": 0.143,
      "pf": 1.32,
      "mfe_p25": 49.25,
      "mfe_p50": 324.0,
      "mfe_p75": 5581.5,
      "winnerMAE_p75": 441.25,
      "winnerMAE_p90": 2972.4,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -409.0,
      "revAfterSL_rate": 59.7,
      "ci90": {
        "expR": 0.143,
        "ci90": [
          0.064,
          0.218
        ],
        "p_mean_le_0": 0.001,
        "n": 826
      }
    },
    "cuts": {
      "1.2": {
        "n": 297,
        "wrTP1": 34.0,
        "nSL": 178,
        "nTO": 18,
        "expR": 0.248,
        "pf": 1.4,
        "mfe_p25": 44.25,
        "mfe_p50": 294.5,
        "mfe_p75": 3007.0,
        "winnerMAE_p75": 140.0,
        "winnerMAE_p90": 2300.0,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -216.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.248,
          "ci90": [
            0.073,
            0.433
          ],
          "p_mean_le_0": 0.013,
          "n": 286
        }
      },
      "1.3": {
        "n": 265,
        "wrTP1": 30.6,
        "nSL": 166,
        "nTO": 18,
        "expR": 0.207,
        "pf": 1.32,
        "mfe_p25": 43.25,
        "mfe_p50": 270.5,
        "mfe_p75": 2402.0,
        "winnerMAE_p75": 134.0,
        "winnerMAE_p90": 1910.0,
        "loserMFEbeforeSL_p50": 9.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -203.0,
        "revAfterSL_rate": 51.2,
        "ci90": {
          "expR": 0.207,
          "ci90": [
            0.018,
            0.427
          ],
          "p_mean_le_0": 0.036,
          "n": 254
        }
      },
      "1.5": {
        "n": 217,
        "wrTP1": 26.7,
        "nSL": 141,
        "nTO": 18,
        "expR": 0.197,
        "pf": 1.29,
        "mfe_p25": 44.0,
        "mfe_p50": 275.5,
        "mfe_p75": 2099.0,
        "winnerMAE_p75": 127.25,
        "winnerMAE_p90": 638.1000000000001,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -164.0,
        "revAfterSL_rate": 48.9,
        "ci90": {
          "expR": 0.197,
          "ci90": [
            -0.031,
            0.45
          ],
          "p_mean_le_0": 0.076,
          "n": 206
        }
      },
      "2.0": {
        "n": 136,
        "wrTP1": 19.1,
        "nSL": 93,
        "nTO": 17,
        "expR": 0.202,
        "pf": 1.27,
        "mfe_p25": 50.5,
        "mfe_p50": 283.5,
        "mfe_p75": 1739.0,
        "winnerMAE_p75": 102.75,
        "winnerMAE_p90": 1027.0,
        "loserMFEbeforeSL_p50": 12.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -150.0,
        "revAfterSL_rate": 48.4,
        "ci90": {
          "expR": 0.202,
          "ci90": [
            -0.143,
            0.571
          ],
          "p_mean_le_0": 0.184,
          "n": 126
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
    "n": 10496,
    "wrTP1": 49.4,
    "expR": 0.028
  },
  "2026-W45": {
    "n": 8043,
    "wrTP1": 47.7,
    "expR": 0.121
  },
  "2026-W46": {
    "n": 6459,
    "wrTP1": 50.6,
    "expR": 0.129
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
      "n": 286,
      "wrTP1": 50.0,
      "expR": 0.036,
      "pf": 1.07
    },
    "15m/RETEST/SHORT": {
      "n": 303,
      "wrTP1": 51.5,
      "expR": 0.037,
      "pf": 1.08
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
      "n": 2137,
      "wrTP1": 47.1,
      "expR": 0.022,
      "pf": 1.04
    },
    "29m/INV/SHORT": {
      "n": 1,
      "wrTP1": 100.0,
      "expR": 0.14,
      "pf": 99.0
    },
    "29m/RETEST/LONG": {
      "n": 121,
      "wrTP1": 54.5,
      "expR": 0.133,
      "pf": 1.29
    },
    "29m/RETEST/SHORT": {
      "n": 179,
      "wrTP1": 54.2,
      "expR": 0.11,
      "pf": 1.24
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
      "n": 992,
      "wrTP1": 48.1,
      "expR": -0.069,
      "pf": 0.86
    },
    "2m/RETEST/SHORT": {
      "n": 949,
      "wrTP1": 45.8,
      "expR": -0.022,
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
      "n": 789,
      "wrTP1": 53.1,
      "expR": 0.069,
      "pf": 1.15
    },
    "3m/RETEST/SHORT": {
      "n": 755,
      "wrTP1": 53.9,
      "expR": 0.109,
      "pf": 1.25
    },
    "5m/INV/LONG": {
      "n": 16,
      "wrTP1": 68.8,
      "expR": -0.087,
      "pf": 0.72
    },
    "5m/INV/SHORT": {
      "n": 10,
      "wrTP1": 20.0,
      "expR": 0.272,
      "pf": 1.45
    },
    "5m/RETEST/LONG": {
      "n": 796,
      "wrTP1": 53.1,
      "expR": 0.075,
      "pf": 1.17
    },
    "5m/RETEST/SHORT": {
      "n": 675,
      "wrTP1": 53.5,
      "expR": 0.089,
      "pf": 1.2
    }
  },
  "2026-W45": {
    "15m/INV/SHORT": {
      "n": 1,
      "wrTP1": 100.0,
      "expR": 0.51,
      "pf": 99.0
    },
    "15m/RETEST/LONG": {
      "n": 336,
      "wrTP1": 46.1,
      "expR": 0.137,
      "pf": 1.28
    },
    "15m/RETEST/SHORT": {
      "n": 285,
      "wrTP1": 53.3,
      "expR": 0.36,
      "pf": 1.83
    },
    "1m/INV/LONG": {
      "n": 32,
      "wrTP1": 43.8,
      "expR": 0.149,
      "pf": 1.35
    },
    "1m/INV/SHORT": {
      "n": 44,
      "wrTP1": 47.7,
      "expR": 0.438,
      "pf": 2.28
    },
    "1m/RETEST/LONG": {
      "n": 1035,
      "wrTP1": 40.4,
      "expR": 0.071,
      "pf": 1.14
    },
    "1m/RETEST/SHORT": {
      "n": 1754,
      "wrTP1": 44.0,
      "expR": 0.046,
      "pf": 1.09
    },
    "29m/INV/LONG": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 0.365,
      "pf": 2.46
    },
    "29m/INV/SHORT": {
      "n": 1,
      "wrTP1": 100.0,
      "expR": 0.92,
      "pf": 99.0
    },
    "29m/RETEST/LONG": {
      "n": 168,
      "wrTP1": 51.8,
      "expR": 0.44,
      "pf": 2.04
    },
    "29m/RETEST/SHORT": {
      "n": 151,
      "wrTP1": 51.7,
      "expR": 0.313,
      "pf": 1.73
    },
    "2m/INV/LONG": {
      "n": 12,
      "wrTP1": 50.0,
      "expR": -0.033,
      "pf": 0.93
    },
    "2m/INV/SHORT": {
      "n": 16,
      "wrTP1": 43.8,
      "expR": -0.105,
      "pf": 0.77
    },
    "2m/RETEST/LONG": {
      "n": 502,
      "wrTP1": 43.0,
      "expR": 0.051,
      "pf": 1.1
    },
    "2m/RETEST/SHORT": {
      "n": 694,
      "wrTP1": 46.5,
      "expR": 0.097,
      "pf": 1.2
    },
    "3m/INV/LONG": {
      "n": 11,
      "wrTP1": 36.4,
      "expR": -0.293,
      "pf": 0.46
    },
    "3m/INV/SHORT": {
      "n": 11,
      "wrTP1": 72.7,
      "expR": 0.054,
      "pf": 1.2
    },
    "3m/RETEST/LONG": {
      "n": 1011,
      "wrTP1": 52.1,
      "expR": 0.105,
      "pf": 1.23
    },
    "3m/RETEST/SHORT": {
      "n": 831,
      "wrTP1": 55.4,
      "expR": 0.204,
      "pf": 1.49
    },
    "5m/INV/LONG": {
      "n": 2,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/INV/SHORT": {
      "n": 10,
      "wrTP1": 60.0,
      "expR": -0.067,
      "pf": 0.83
    },
    "5m/RETEST/LONG": {
      "n": 563,
      "wrTP1": 49.6,
      "expR": 0.087,
      "pf": 1.18
    },
    "5m/RETEST/SHORT": {
      "n": 569,
      "wrTP1": 53.1,
      "expR": 0.207,
      "pf": 1.47
    }
  },
  "2026-W46": {
    "15m/INV/SHORT": {
      "n": 2,
      "wrTP1": 50.0,
      "expR": 0.405,
      "pf": 1.81
    },
    "15m/RETEST/LONG": {
      "n": 215,
      "wrTP1": 54.0,
      "expR": 0.206,
      "pf": 1.46
    },
    "15m/RETEST/SHORT": {
      "n": 204,
      "wrTP1": 47.1,
      "expR": 0.106,
      "pf": 1.22
    },
    "1m/INV/LONG": {
      "n": 50,
      "wrTP1": 48.0,
      "expR": 0.281,
      "pf": 1.73
    },
    "1m/INV/SHORT": {
      "n": 30,
      "wrTP1": 56.7,
      "expR": 0.62,
      "pf": 3.08
    },
    "1m/RETEST/LONG": {
      "n": 1529,
      "wrTP1": 46.2,
      "expR": 0.131,
      "pf": 1.28
    },
    "1m/RETEST/SHORT": {
      "n": 812,
      "wrTP1": 48.3,
      "expR": 0.108,
      "pf": 1.23
    },
    "29m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "29m/RETEST/LONG": {
      "n": 115,
      "wrTP1": 60.0,
      "expR": 0.442,
      "pf": 2.28
    },
    "29m/RETEST/SHORT": {
      "n": 125,
      "wrTP1": 48.0,
      "expR": 0.154,
      "pf": 1.32
    },
    "2m/INV/LONG": {
      "n": 20,
      "wrTP1": 40.0,
      "expR": -0.23,
      "pf": 0.62
    },
    "2m/INV/SHORT": {
      "n": 9,
      "wrTP1": 66.7,
      "expR": 0.646,
      "pf": 3.58
    },
    "2m/RETEST/LONG": {
      "n": 706,
      "wrTP1": 52.5,
      "expR": 0.147,
      "pf": 1.33
    },
    "2m/RETEST/SHORT": {
      "n": 356,
      "wrTP1": 51.1,
      "expR": 0.024,
      "pf": 1.05
    },
    "3m/INV/LONG": {
      "n": 13,
      "wrTP1": 61.5,
      "expR": -0.072,
      "pf": 0.81
    },
    "3m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 0.533,
      "pf": 99.0
    },
    "3m/RETEST/LONG": {
      "n": 755,
      "wrTP1": 57.5,
      "expR": 0.158,
      "pf": 1.39
    },
    "3m/RETEST/SHORT": {
      "n": 632,
      "wrTP1": 50.0,
      "expR": 0.017,
      "pf": 1.04
    },
    "5m/INV/LONG": {
      "n": 7,
      "wrTP1": 57.1,
      "expR": 0.1,
      "pf": 1.23
    },
    "5m/INV/SHORT": {
      "n": 2,
      "wrTP1": 100.0,
      "expR": 0.505,
      "pf": 99.0
    },
    "5m/RETEST/LONG": {
      "n": 564,
      "wrTP1": 53.9,
      "expR": 0.217,
      "pf": 1.49
    },
    "5m/RETEST/SHORT": {
      "n": 308,
      "wrTP1": 48.7,
      "expR": 0.038,
      "pf": 1.08
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 60138,
  "brier": 0.2224,
  "bias": -0.071,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.238
    },
    {
      "feature": "stretchAtr",
      "weight": -0.058
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.048
    },
    {
      "feature": "nearTk",
      "weight": -0.038
    },
    {
      "feature": "hourNY",
      "weight": 0.027
    },
    {
      "feature": "aligned",
      "weight": -0.022
    },
    {
      "feature": "chopIdx",
      "weight": -0.021
    },
    {
      "feature": "biasScore",
      "weight": -0.019
    },
    {
      "feature": "rvol",
      "weight": 0.01
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.01
    },
    {
      "feature": "nearEdge",
      "weight": 0.006
    },
    {
      "feature": "structDir",
      "weight": 0.004
    },
    {
      "feature": "emaStack",
      "weight": 0.004
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.173,
      "actual": 0.179,
      "n": 6013
    },
    {
      "bin": 1,
      "pred": 0.376,
      "actual": 0.324,
      "n": 6014
    },
    {
      "bin": 2,
      "pred": 0.453,
      "actual": 0.329,
      "n": 6014
    },
    {
      "bin": 3,
      "pred": 0.498,
      "actual": 0.426,
      "n": 6014
    },
    {
      "bin": 4,
      "pred": 0.535,
      "actual": 0.516,
      "n": 6014
    },
    {
      "bin": 5,
      "pred": 0.563,
      "actual": 0.575,
      "n": 6013
    },
    {
      "bin": 6,
      "pred": 0.586,
      "actual": 0.608,
      "n": 6014
    },
    {
      "bin": 7,
      "pred": 0.605,
      "actual": 0.642,
      "n": 6014
    },
    {
      "bin": 8,
      "pred": 0.623,
      "actual": 0.693,
      "n": 6014
    },
    {
      "bin": 9,
      "pred": 0.65,
      "actual": 0.755,
      "n": 6014
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 49809,
  "testN": 14502,
  "testWeeks": [
    "2026-W45",
    "2026-W46"
  ],
  "model_oos_brier": 0.2236,
  "model_oos_n": 14502,
  "best_scheme_in_sample": {
    "scheme": "fixed_1_5R",
    "trainExpR": 0.047
  },
  "best_scheme_oos_expR": 0.095
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "15m/RETEST/LONG": {
    "expR": 0.12,
    "ci90": [
      0.039,
      0.21
    ],
    "p_mean_le_0": 0.011,
    "n": 807,
    "survives_fdr10": true
  },
  "15m/RETEST/SHORT": {
    "expR": 0.169,
    "ci90": [
      0.079,
      0.261
    ],
    "p_mean_le_0": 0.001,
    "n": 765,
    "survives_fdr10": true
  },
  "1m/INV/LONG": {
    "expR": 0.133,
    "ci90": [
      0.045,
      0.23
    ],
    "p_mean_le_0": 0.006,
    "n": 512,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": 0.165,
    "ci90": [
      0.068,
      0.263
    ],
    "p_mean_le_0": 0.003,
    "n": 383,
    "survives_fdr10": true
  },
  "1m/RETEST/LONG": {
    "expR": 0.036,
    "ci90": [
      0.022,
      0.05
    ],
    "p_mean_le_0": 0.0,
    "n": 19091,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.036,
    "ci90": [
      0.018,
      0.053
    ],
    "p_mean_le_0": 0.001,
    "n": 13354,
    "survives_fdr10": true
  },
  "29m/RETEST/LONG": {
    "expR": 0.344,
    "ci90": [
      0.207,
      0.492
    ],
    "p_mean_le_0": 0.0,
    "n": 382,
    "survives_fdr10": true
  },
  "29m/RETEST/SHORT": {
    "expR": 0.187,
    "ci90": [
      0.077,
      0.302
    ],
    "p_mean_le_0": 0.002,
    "n": 434,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.009,
    "ci90": [
      -0.12,
      0.139
    ],
    "p_mean_le_0": 0.475,
    "n": 189,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.128,
    "ci90": [
      -0.044,
      0.301
    ],
    "p_mean_le_0": 0.109,
    "n": 140,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.041,
    "ci90": [
      0.019,
      0.063
    ],
    "p_mean_le_0": 0.002,
    "n": 8440,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.048,
    "ci90": [
      0.022,
      0.074
    ],
    "p_mean_le_0": 0.002,
    "n": 5792,
    "survives_fdr10": true
  },
  "3m/INV/LONG": {
    "expR": -0.125,
    "ci90": [
      -0.372,
      0.116
    ],
    "p_mean_le_0": 0.799,
    "n": 32,
    "survives_fdr10": false
  },
  "3m/INV/SHORT": {
    "expR": 0.242,
    "ci90": [
      0.014,
      0.449
    ],
    "p_mean_le_0": 0.04,
    "n": 19,
    "survives_fdr10": true
  },
  "3m/RETEST/LONG": {
    "expR": 0.11,
    "ci90": [
      0.073,
      0.147
    ],
    "p_mean_le_0": 0.0,
    "n": 2510,
    "survives_fdr10": true
  },
  "3m/RETEST/SHORT": {
    "expR": 0.117,
    "ci90": [
      0.079,
      0.156
    ],
    "p_mean_le_0": 0.0,
    "n": 2162,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.097,
    "ci90": [
      -0.082,
      0.28
    ],
    "p_mean_le_0": 0.199,
    "n": 61,
    "survives_fdr10": false
  },
  "5m/INV/SHORT": {
    "expR": 0.125,
    "ci90": [
      -0.151,
      0.428
    ],
    "p_mean_le_0": 0.248,
    "n": 43,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.112,
    "ci90": [
      0.082,
      0.144
    ],
    "p_mean_le_0": 0.0,
    "n": 4116,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.094,
    "ci90": [
      0.055,
      0.136
    ],
    "p_mean_le_0": 0.0,
    "n": 2929,
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
      "n": 7917,
      "wrTP1": 50.4,
      "expR": 0.086,
      "pf": 1.19,
      "defining_features": {
        "hourNY": 1.32,
        "biasScore": -0.94,
        "emaStack": -0.84,
        "nearEdge": -0.7
      }
    },
    {
      "id": 1,
      "n": 13017,
      "wrTP1": 51.2,
      "expR": 0.062,
      "pf": 1.14,
      "defining_features": {
        "structDir": -1.02,
        "biasScore": 0.68,
        "nearEdge": 0.51,
        "emaStack": 0.37
      }
    },
    {
      "id": 3,
      "n": 24445,
      "wrTP1": 45.5,
      "expR": 0.06,
      "pf": 1.12,
      "defining_features": {
        "structDir": 0.98,
        "biasScore": 0.82,
        "emaStack": 0.77,
        "nearEdge": 0.63
      }
    },
    {
      "id": 0,
      "n": 18932,
      "wrTP1": 45.4,
      "expR": 0.044,
      "pf": 1.09,
      "defining_features": {
        "biasScore": -1.12,
        "emaStack": -0.89,
        "nearEdge": -0.87,
        "hourNY": -0.5
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
        "n": 82,
        "wrTP1": 43.9,
        "expR": 0.076
      },
      "NQ": {
        "n": 97,
        "wrTP1": 44.3,
        "expR": -0.105
      },
      "GC": {
        "n": 101,
        "wrTP1": 48.5,
        "expR": 0.172
      },
      "CL": {
        "n": 116,
        "wrTP1": 52.6,
        "expR": 0.019
      },
      "YM": {
        "n": 130,
        "wrTP1": 50.0,
        "expR": 0.485
      },
      "ETHUSDT": {
        "n": 153,
        "wrTP1": 56.2,
        "expR": 0.135
      },
      "BTCUSDT": {
        "n": 158,
        "wrTP1": 46.8,
        "expR": 0.021
      }
    },
    "expR_spread": 0.59,
    "verdict": "instrument-specific"
  },
  "15m/RETEST/SHORT": {
    "symbols": {
      "BTCUSDT": {
        "n": 186,
        "wrTP1": 53.8,
        "expR": 0.089
      },
      "ETHUSDT": {
        "n": 137,
        "wrTP1": 48.2,
        "expR": -0.036
      },
      "YM": {
        "n": 92,
        "wrTP1": 56.5,
        "expR": 0.368
      },
      "ES": {
        "n": 87,
        "wrTP1": 44.8,
        "expR": 0.249
      },
      "GC": {
        "n": 98,
        "wrTP1": 51.0,
        "expR": 0.257
      },
      "NQ": {
        "n": 98,
        "wrTP1": 49.0,
        "expR": 0.141
      },
      "CL": {
        "n": 94,
        "wrTP1": 52.1,
        "expR": 0.298
      }
    },
    "expR_spread": 0.404,
    "verdict": "instrument-specific"
  },
  "1m/INV/LONG": {
    "symbols": {
      "CL": {
        "n": 99,
        "wrTP1": 45.5,
        "expR": 0.212
      },
      "GC": {
        "n": 77,
        "wrTP1": 48.1,
        "expR": 0.064
      },
      "YM": {
        "n": 243,
        "wrTP1": 46.1,
        "expR": 0.172
      },
      "ES": {
        "n": 67,
        "wrTP1": 40.3,
        "expR": -0.1
      },
      "NQ": {
        "n": 48,
        "wrTP1": 56.2,
        "expR": 0.192
      }
    },
    "expR_spread": 0.312,
    "verdict": "universal"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "GC": {
        "n": 90,
        "wrTP1": 54.4,
        "expR": 0.276
      },
      "YM": {
        "n": 174,
        "wrTP1": 43.7,
        "expR": 0.11
      },
      "NQ": {
        "n": 48,
        "wrTP1": 56.2,
        "expR": 0.04
      },
      "ES": {
        "n": 28,
        "wrTP1": 53.6,
        "expR": 0.437
      },
      "CL": {
        "n": 63,
        "wrTP1": 38.1,
        "expR": 0.127
      }
    },
    "expR_spread": 0.397,
    "verdict": "universal"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 3236,
        "wrTP1": 44.0,
        "expR": 0.03
      },
      "NQ": {
        "n": 3452,
        "wrTP1": 44.9,
        "expR": 0.023
      },
      "ES": {
        "n": 4402,
        "wrTP1": 44.9,
        "expR": 0.008
      },
      "CL": {
        "n": 3862,
        "wrTP1": 44.6,
        "expR": 0.033
      },
      "YM": {
        "n": 4709,
        "wrTP1": 45.7,
        "expR": 0.079
      }
    },
    "expR_spread": 0.071,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 2078,
        "wrTP1": 41.2,
        "expR": 0.047
      },
      "GC": {
        "n": 3830,
        "wrTP1": 45.6,
        "expR": 0.039
      },
      "YM": {
        "n": 3123,
        "wrTP1": 44.7,
        "expR": 0.05
      },
      "ES": {
        "n": 2420,
        "wrTP1": 46.5,
        "expR": 0.026
      },
      "CL": {
        "n": 2480,
        "wrTP1": 46.2,
        "expR": 0.012
      }
    },
    "expR_spread": 0.038,
    "verdict": "universal"
  },
  "29m/RETEST/LONG": {
    "symbols": {
      "YM": {
        "n": 68,
        "wrTP1": 51.5,
        "expR": 0.747
      },
      "NQ": {
        "n": 42,
        "wrTP1": 54.8,
        "expR": 0.186
      },
      "ES": {
        "n": 41,
        "wrTP1": 53.7,
        "expR": 0.301
      },
      "CL": {
        "n": 66,
        "wrTP1": 60.6,
        "expR": 0.301
      },
      "BTCUSDT": {
        "n": 73,
        "wrTP1": 56.2,
        "expR": 0.24
      },
      "GC": {
        "n": 57,
        "wrTP1": 50.9,
        "expR": 0.275
      },
      "ETHUSDT": {
        "n": 57,
        "wrTP1": 56.1,
        "expR": 0.281
      }
    },
    "expR_spread": 0.561,
    "verdict": "instrument-specific"
  },
  "29m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 75,
        "wrTP1": 46.7,
        "expR": 0.081
      },
      "CL": {
        "n": 50,
        "wrTP1": 46.0,
        "expR": 0.104
      },
      "YM": {
        "n": 65,
        "wrTP1": 52.3,
        "expR": 0.482
      },
      "NQ": {
        "n": 62,
        "wrTP1": 59.7,
        "expR": 0.483
      },
      "ETHUSDT": {
        "n": 75,
        "wrTP1": 56.0,
        "expR": 0.078
      },
      "GC": {
        "n": 35,
        "wrTP1": 48.6,
        "expR": 0.187
      },
      "BTCUSDT": {
        "n": 93,
        "wrTP1": 50.5,
        "expR": 0.02
      }
    },
    "expR_spread": 0.463,
    "verdict": "instrument-specific"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 28,
        "wrTP1": 42.9,
        "expR": -0.281
      },
      "CL": {
        "n": 21,
        "wrTP1": 61.9,
        "expR": 0.118
      },
      "YM": {
        "n": 75,
        "wrTP1": 42.7,
        "expR": -0.057
      },
      "ES": {
        "n": 36,
        "wrTP1": 63.9,
        "expR": 0.005
      },
      "NQ": {
        "n": 34,
        "wrTP1": 58.8,
        "expR": 0.347
      }
    },
    "expR_spread": 0.628,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 62,
        "wrTP1": 54.8,
        "expR": 0.353
      },
      "NQ": {
        "n": 20,
        "wrTP1": 45.0,
        "expR": -0.032
      },
      "ES": {
        "n": 17,
        "wrTP1": 29.4,
        "expR": -0.146
      },
      "CL": {
        "n": 21,
        "wrTP1": 57.1,
        "expR": -0.006
      },
      "GC": {
        "n": 25,
        "wrTP1": 48.0,
        "expR": -0.007
      }
    },
    "expR_spread": 0.499,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 1655,
        "wrTP1": 47.3,
        "expR": 0.048
      },
      "GC": {
        "n": 1379,
        "wrTP1": 45.1,
        "expR": 0.011
      },
      "CL": {
        "n": 1677,
        "wrTP1": 48.7,
        "expR": 0.052
      },
      "ES": {
        "n": 1963,
        "wrTP1": 47.4,
        "expR": 0.003
      },
      "YM": {
        "n": 2012,
        "wrTP1": 49.0,
        "expR": 0.083
      }
    },
    "expR_spread": 0.08,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 1056,
        "wrTP1": 47.2,
        "expR": 0.005
      },
      "YM": {
        "n": 1294,
        "wrTP1": 47.6,
        "expR": 0.066
      },
      "GC": {
        "n": 1574,
        "wrTP1": 48.0,
        "expR": 0.072
      },
      "NQ": {
        "n": 1005,
        "wrTP1": 43.7,
        "expR": 0.023
      },
      "CL": {
        "n": 1056,
        "wrTP1": 50.4,
        "expR": 0.057
      }
    },
    "expR_spread": 0.067,
    "verdict": "universal"
  },
  "3m/INV/LONG": {
    "symbols": {
      "CL": {
        "n": 4,
        "wrTP1": 25.0,
        "expR": -0.645
      },
      "YM": {
        "n": 12,
        "wrTP1": 58.3,
        "expR": -0.064
      },
      "NQ": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.183
      },
      "ES": {
        "n": 7,
        "wrTP1": 71.4,
        "expR": 0.18
      },
      "GC": {
        "n": 3,
        "wrTP1": 0.0,
        "expR": -1.0
      }
    },
    "expR_spread": 1.183,
    "verdict": "instrument-specific"
  },
  "3m/INV/SHORT": {
    "symbols": {
      "GC": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.22
      },
      "YM": {
        "n": 6,
        "wrTP1": 100.0,
        "expR": 0.507
      },
      "CL": {
        "n": 3,
        "wrTP1": 100.0,
        "expR": 0.4
      },
      "NQ": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.57
      }
    },
    "expR_spread": 0.79,
    "verdict": "instrument-specific"
  },
  "3m/RETEST/LONG": {
    "symbols": {
      "YM": {
        "n": 516,
        "wrTP1": 57.2,
        "expR": 0.146
      },
      "ES": {
        "n": 571,
        "wrTP1": 52.7,
        "expR": 0.056
      },
      "NQ": {
        "n": 498,
        "wrTP1": 52.6,
        "expR": 0.052
      },
      "CL": {
        "n": 481,
        "wrTP1": 55.1,
        "expR": 0.12
      },
      "GC": {
        "n": 489,
        "wrTP1": 52.6,
        "expR": 0.183
      }
    },
    "expR_spread": 0.131,
    "verdict": "universal"
  },
  "3m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 439,
        "wrTP1": 53.5,
        "expR": 0.123
      },
      "ES": {
        "n": 407,
        "wrTP1": 49.4,
        "expR": 0.013
      },
      "GC": {
        "n": 394,
        "wrTP1": 52.8,
        "expR": 0.151
      },
      "CL": {
        "n": 506,
        "wrTP1": 54.5,
        "expR": 0.097
      },
      "YM": {
        "n": 472,
        "wrTP1": 55.7,
        "expR": 0.194
      }
    },
    "expR_spread": 0.181,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 13,
        "wrTP1": 61.5,
        "expR": 0.251
      },
      "YM": {
        "n": 15,
        "wrTP1": 66.7,
        "expR": -0.002
      },
      "ES": {
        "n": 13,
        "wrTP1": 69.2,
        "expR": 0.023
      },
      "CL": {
        "n": 9,
        "wrTP1": 66.7,
        "expR": 0.472
      },
      "GC": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.088
      },
      "BTCUSDT": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": -0.36
      },
      "ETHUSDT": {
        "n": 4,
        "wrTP1": 75.0,
        "expR": -0.115
      }
    },
    "expR_spread": 0.832,
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
        "n": 7,
        "wrTP1": 14.3,
        "expR": -0.791
      },
      "ES": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": 0.677
      },
      "GC": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": 0.318
      },
      "CL": {
        "n": 4,
        "wrTP1": 75.0,
        "expR": 0.213
      },
      "BTCUSDT": {
        "n": 8,
        "wrTP1": 62.5,
        "expR": -0.018
      },
      "ETHUSDT": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": -0.148
      }
    },
    "expR_spread": 1.468,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 460,
        "wrTP1": 50.0,
        "expR": 0.159
      },
      "ES": {
        "n": 669,
        "wrTP1": 51.1,
        "expR": 0.115
      },
      "YM": {
        "n": 693,
        "wrTP1": 50.9,
        "expR": 0.117
      },
      "CL": {
        "n": 598,
        "wrTP1": 54.2,
        "expR": 0.167
      },
      "NQ": {
        "n": 661,
        "wrTP1": 48.6,
        "expR": 0.068
      },
      "BTCUSDT": {
        "n": 582,
        "wrTP1": 53.3,
        "expR": 0.103
      },
      "ETHUSDT": {
        "n": 600,
        "wrTP1": 53.3,
        "expR": 0.07
      }
    },
    "expR_spread": 0.099,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 348,
        "wrTP1": 46.6,
        "expR": 0.038
      },
      "ES": {
        "n": 419,
        "wrTP1": 48.9,
        "expR": 0.193
      },
      "GC": {
        "n": 575,
        "wrTP1": 47.7,
        "expR": 0.043
      },
      "YM": {
        "n": 473,
        "wrTP1": 48.8,
        "expR": 0.127
      },
      "CL": {
        "n": 414,
        "wrTP1": 49.0,
        "expR": 0.056
      },
      "ETHUSDT": {
        "n": 387,
        "wrTP1": 55.0,
        "expR": 0.138
      },
      "BTCUSDT": {
        "n": 456,
        "wrTP1": 52.9,
        "expR": 0.074
      }
    },
    "expR_spread": 0.155,
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
    "n": 137,
    "wrTP1": 49.6,
    "nSL": 53,
    "nTO": 16,
    "expR": 0.297,
    "pf": 1.7,
    "mfe_p25": 24.0,
    "mfe_p50": 67.0,
    "mfe_p75": 288.0,
    "winnerMAE_p75": 23.75,
    "winnerMAE_p90": 94.90000000000023,
    "loserMFEbeforeSL_p50": 1.0,
    "bars_win_p50": 1.0,
    "bars_loss_p50": 2.0,
    "entryZoneTk_p50": -47.0,
    "revAfterSL_rate": 47.2
  },
  "away_from_news": {
    "n": 64174,
    "wrTP1": 47.2,
    "nSL": 29727,
    "nTO": 4157,
    "expR": 0.058,
    "pf": 1.12,
    "mfe_p25": 9.0,
    "mfe_p50": 21.0,
    "mfe_p75": 51.0,
    "winnerMAE_p75": 15.0,
    "winnerMAE_p90": 40.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -17.0,
    "revAfterSL_rate": 36.2
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 6,
  "mae_deltaER": 0.247,
  "hit_direction_rate": 50.0
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
    "hypothesis": "En RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. HASTA 2026-09-04 esto solo certificaba en SHORT (\"no aplica a largos\"); con la muestra de 2026-09-05 TAMBIEN certifica en 1m LONG, asi que se retira la exclusion dura de BUY RETEST y se deja como 'certifica por tf/side, no generalizar sin mirar la tabla'. 2026-09-06: mismas cifras exactas que 2026-09-05 (n identico) porque no llego dato nuevo. 2026-09-07 (lunes, primer dia con trades GENUINAMENTE nuevos post-restauracion, sin repeticion del bug de heal): retest_1m_long paso de n=1087 a n=1135 (+48 pares nuevos, no restaurados) y el delta se mantiene practicamente igual (0.181->0.183) con el CI90 todavia sin cruzar cero -- esta es la primera confirmacion independiente real que pedia el next_steps anterior. retest_1m_short tambien crecio con dato nuevo (n=219->229) y sigue certificando. 2026-09-08 (martes, primer dia habil COMPLETO post-feriado, salto grande de muestra real): retest_1m_long n=1135->1432 (delta 0.183->0.18, estable, segunda confirmacion independiente); retest_1m_short n=229->514 (delta 0.283->0.417, se hizo MAS fuerte); retest_2m_short CERTIFICA POR PRIMERA VEZ (n=129->260, CI90 dejo de cruzar cero); retest_5m_long CERTIFICA POR PRIMERA VEZ pero al filo (n=224->274, CI90=[0.005,0.36], limite inferior casi cero, vigilar que no se revierta con mas muestra); retest_2m_long sigue sin certificar y el delta bajo a casi cero (0.028->0.01, n=596->742). 2026-10-20: hito nuevo -- `since_change` certifica limpio ahora en los 6 de 6 segmentos RETEST del bus (el que faltaba, 5m SHORT, cruzo hoy su CI90 a positivo: [-0.005,0.299] -> [0.004,0.286], n=541->586, limite inferior apenas sobre cero pero real). Documentado en detalle en playbook/buy-retest.md y playbook/sell-retest.md (seccion Gestion). El verdict agregado formal de este experimento sigue en 'flat' por la limitacion de metrica ya conocida (mide con rMultiple, no con rOrig) -- no es evidencia de que el cambio no funcione, es la evidencia real viviendo fuera de ese campo. A evaluar en la revision semanal del domingo (2026-week-43): si corresponde subir la confianza documentada de 'aplicado, parcial' a 'aplicado, 6/6 certifican' y si shadow_rules deberia empezar a razonar sobre rOrig en el segmento del gate (5m LONG). No se decide hoy. 2026-10-31: muestra mucho mayor y delta estable -- retestBar (RETEST 2m/5m) E[R] 0.131 vs 0.036 de 3-capas, delta 0.095 CI90 [0.077,0.114] n=29603; retestBar2 (RETEST 1m SHORT) E[R] 0.063 vs 0.022, delta 0.041 CI90 [0.012,0.069] n=8744. Ambos CI90 siguen sin cruzar cero con n mucho mas grande que en octubre. candle1 (INVERSION) sigue sin certificar (CI90 cruza cero, n=936, bajo volumen). El verdict agregado formal sigue 'flat' por el mismo mismatch de metrica ya documentado (mide rMultiple, no rOrig); la evidencia real sigue viviendo en sl_origin_vs_layer. 2026-11-02: lunes, dato nuevo chico y parejo en todo el bus (+282 pares). retestBar (RETEST 2m/5m/15m/29m) sube a n=29983 (de 29603), E[R] 0.138 vs 0.037 de 3-capas, delta 0.101 CI90=[0.083,0.12] -- delta un poco mas fuerte que el 31-oct (0.095), CI90 sin cruzar cero con una confirmacion mas. retestBar2 (RETEST 1m SHORT) n=8758 (de 8744), E[R] 0.061 vs 0.021, delta 0.041 CI90=[0.012,0.07], practicamente igual a ayer. candle1 (INVERSION) sigue sin certificar (CI90 cruza cero, n=942). Nada cambia la conclusion: sigue siendo el candidato mas fuerte del bus, aun sin aplicarse en Pine. 2026-11-04: miercoles, dato nuevo chico y parejo en todo el bus. retestBar (RETEST 2m/3m/5m/15m/29m) sube a n=32083 (de 29983), E[R] 0.151 vs 0.043 de 3-capas, delta 0.109 CI90=[0.091,0.127] -- delta mas fuerte que el 11-02 (0.101), sigue sin cruzar cero con una confirmacion mas y la muestra mas grande hasta ahora. retestBar2 (RETEST 1m SHORT) n=9561 (de 8758), E[R] 0.059 vs 0.02, delta 0.04 CI90=[0.012,0.067], practicamente igual a antes. candle1 (INVERSION) hoy mostro una lectura ruidosa: orig_expR salta a 2.128 (de ordenes de magnitud mas chicos en lecturas previas) con CI90=[-0.073,6.075] n=995 -- es varianza de cola gorda por SL estructural muy ajustado (slOrigTk mediana=6 ticks) combinada con n todavia chico, no un cambio real ni un bug de pipeline (el filtro invalid_geometry de analyze.py ya excluye slOrigTk<=1; esto es ruido dentro del rango valido). Sigue sin certificar, no cambia el tratamiento de candle1 como no-propuesta. Conclusion sin cambio: retestBar/retestBar2 siguen siendo el candidato mas fuerte del bus, aun sin aplicarse en Pine -- con n=32083+9561=41644 ya se acerca al umbral n>=100 por overall varias veces sobre, listo para formalizarse como propuesta concreta en la revision semanal del domingo 2026-11-08. 2026-11-05: jueves, dato nuevo chico y parejo en todo el bus (+1512 pares). sl_origin_vs_layer.by_basis.retestBar (RETEST 2m/3m/5m/15m/29m) sube a n=33281 (de 32083), E[R] 0.158 vs 0.048 de 3-capas, delta 0.11 CI90=[0.091,0.129] -- estable, una confirmacion mas. retestBar2 (RETEST 1m SHORT) n=9714 (de 9561), E[R] 0.062 vs 0.021, delta 0.041 CI90=[0.014,0.068], practicamente igual. Hallazgo del dia en since_change (medicion desde que el cambio se aplico el 2026-09-26, distinta de by_basis que es paralela sin fecha): 1m/RETEST/LONG, el unico de los 6 segmentos RETEST que seguia al filo cruzando cero, vuelve a cruzar a positivo (delta 0.034 CI90=[0.003,0.065], n=7660->8003) -- con esto los 6 de 6 segmentos RETEST tienen delta_beats_zero=true en since_change de forma simultanea, algo que ya paso una vez (2026-10-20) y se revirtio en este mismo segmento. Dado ese historial de vaiven justo en el limite, se trata como una recuperacion a vigilar 2-3 lecturas mas, no como confirmacion definitiva del 6/6. Conclusion sin cambio de fondo: retestBar/retestBar2 siguen siendo el candidato mas fuerte del bus para la propuesta formal de la revision semanal del domingo 2026-11-08, aun sin aplicarse en Pine. 2026-11-06: viernes, dato nuevo chico y parejo en todo el bus (+1337 pares). sl_origin_vs_layer.by_basis.retestBar (RETEST 2m/3m/5m/15m/29m) sube a n=34155 (de 33281), E[R] 0.166 vs 0.052 de 3-capas, delta 0.115 CI90=[0.096,0.134] -- un poco mas fuerte que ayer (0.11), sigue sin cruzar cero con una confirmacion mas. retestBar2 (RETEST 1m SHORT) n=9972 (de 9714), E[R] 0.065 vs 0.023, delta 0.042 CI90=[0.015,0.07], practicamente igual. since_change (desde 2026-09-26): 1m/RETEST/LONG mantiene por segundo dia consecutivo delta_beats_zero=true tras el cruce de ayer (delta=0.034 CI90=[0.004,0.064], n=8003->8193, practicamente plano) -- los 6 de 6 segmentos RETEST siguen con delta_beats_zero=true de forma simultanea por segunda lectura seguida; se mantiene la cautela (ya se revirtio una vez el 2026-10-20 justo despues de certificar), vigilar 1-2 lecturas mas antes de llamarlo estable. Conclusion sin cambio de fondo: retestBar/retestBar2 siguen siendo el candidato mas fuerte del bus para la propuesta formal de la revision semanal del domingo 2026-11-08, aun sin aplicarse en Pine. 2026-11-08 (domingo, REVISION SEMANAL 2026-week-45): se formaliza el estado de este experimento -- sl_origin_vs_layer.since_change (n=31991) confirma los 6 segmentos clasicos (1m/2m/5m x LONG/SHORT) sin ninguna reversion en 44 dias (1m LONG, el mas fragil, delta=0.032 CI90=[0.003,0.061] n=8288; 5m SHORT el efecto mas grande, delta=0.407 CI90=[0.184,0.711] n=1784) y SUMA dos TF nuevos que certifican limpio por primera vez con muestra post-cambio ya grande: 3m LONG delta=0.242 CI90=[0.162,0.323] n=1536 y 15m LONG delta=0.724 CI90=[0.34,1.174] n=567 (ambos TF heredan el mismo SL del Pine desde que existen, no requieren un cambio nuevo). Quedan sin certificar por edad/muestra (ningun delta negativo, solo CI90 cruzando cero): 3m SHORT (0.079 [-0.013,0.178] n=1370), 15m SHORT (0.161 [-0.025,0.37] n=505), 29m LONG (0.378 [-0.012,0.864] n=257), 29m SHORT (0.037 [-0.104,0.207] n=296). DECISION FORMAL: se trata este experimento como confirmado en la practica para 8/12 segmentos RETEST, aunque el verdict mecanico de eval_experiments() (beforeN=18341, afterN=37917) siga en 'flat' por el mismatch de metrica ya documentado desde 2026-09-27 (mide rMultiple, la base que el propio cambio reemplazo, no rOrig). Esta limitacion se declara PERMANENTE desde hoy: no se recalcula ni se replantea cada corrida -- la medicion que manda para este experimento especifico es sl_origin_vs_layer.since_change, el verdict generico de eval_experiments() queda documentado como no aplicable a un experimento que redefine la base de medicion de si mismo. No se modifica eval_experiments() para crear un caso especial (riesgo de romper la evaluacion generica de otros experimentos). Ningun cambio de input nuevo en scalp_command.pine: el cambio real sigue aplicado desde 2026-09-26, sin ajustes. Detalle completo en reviews/2026-week-45.md. 2026-11-10: martes, dato nuevo chico y parejo en todo el bus (+942 pares LONG, +552 SHORT). sl_origin_vs_layer.by_basis.retestBar (RETEST 2m/3m/5m/15m/29m) sube a n=36470 (de 34155), E[R] 0.201 vs 0.058 de 3-capas, delta 0.143 CI90=[0.11,0.183] -- mas fuerte que el 11-06 (0.115), sigue sin cruzar cero con una confirmacion mas. retestBar2 (RETEST 1m SHORT) n=10470 (de 9972), E[R] 0.064 vs 0.027, delta 0.037 CI90=[0.011,0.065], practicamente igual. HALLAZGO DEL DIA en since_change: 29m/RETEST/LONG -- el segmento exacto del gate de ejecucion -- certifica por PRIMERA VEZ (delta=0.351 CI90=[0.009,0.783] n=291, ayer [-0.005,0.828] n=271 al filo negativo). Con esto 9/12 segmentos RETEST certifican de forma limpia (antes 8/12). El limite inferior (0.009) es muy ajustado y el n todavia chico (291) -- mismo patron de 'cruce justo en el filo' que ya se revirtio una vez en 1m/RETEST/LONG el 2026-10-20, asi que se trata como hallazgo a confirmar 2-3 lecturas mas, NO como slCauseMitigated=true del gate (ese campo depende del verdict formal de eval_experiments(), que sigue flat por el mismatch de metrica ya documentado como PERMANENTE desde 2026-11-08). Quedan sin certificar: 3m SHORT (0.072 [-0.012,0.167] n=1490), 15m SHORT (0.158 [-0.008,0.354] n=596, el mas cerca de certificar), 29m SHORT (0.08 [-0.052,0.236] n=329) -- ninguno con delta negativo, los tres mejoran su limite inferior frente a ayer. Ningun cambio de input nuevo en scalp_command.pine: el cambio real sigue aplicado desde 2026-09-26, sin ajustes. 2026-11-11: miercoles, dato nuevo moderado y parejo en todo el bus (+625 pares LONG, +695 SHORT). sl_origin_vs_layer.by_basis.retestBar (RETEST 2m/3m/5m/15m/29m) sube a n=37429 (de 36470), E[R] 0.203 vs 0.058 de 3-capas, delta 0.145 CI90=[0.114,0.186] -- mas fuerte que el 11-10 (0.143), sigue sin cruzar cero con una confirmacion mas. retestBar2 (RETEST 1m SHORT) n=10643 (de 10470), E[R] 0.064 vs 0.028, delta 0.036 CI90=[0.008,0.063], practicamente igual. HALLAZGO DEL DIA en since_change: dos cambios de estado simultaneos -- (1) 3m/RETEST/SHORT certifica por PRIMERA VEZ (delta=0.086 CI90=[0.012,0.174] n=1670, ayer [-0.012,0.167] n=1490, al filo negativo); (2) 29m/RETEST/LONG -- el segmento exacto del gate de ejecucion -- tiene su SEGUNDA lectura consecutiva confirmando (delta=0.36 CI90=[0.041,0.764] n=318, ayer [0.009,0.783] n=291) y el limite inferior mejora de 0.009 a 0.041, mas comodo que la primera lectura. Con esto 10/12 segmentos RETEST certifican de forma limpia (antes 9/12). Quedan sin certificar: 15m SHORT (0.135 [-0.013,0.311] n=647) y 29m SHORT (0.121 [-0.003,0.274] n=361, el mas cerca de certificar) -- ninguno con delta negativo. Politica sin cambio: 29m/RETEST/LONG necesita 2-3 lecturas seguidas antes de tratarse como estable (esta es la #2, criterio de reversion ya visto una vez en 1m/RETEST/LONG el 2026-10-20); no se marca slCauseMitigated=true del gate todavia (ese campo depende del verdict formal de eval_experiments(), que sigue flat por el mismatch de metrica ya documentado como PERMANENTE desde 2026-11-08). Ningun cambio de input nuevo en scalp_command.pine: el cambio real sigue aplicado desde 2026-09-26, sin ajustes. 2026-11-12: jueves, dato nuevo moderado (+1222 pares LONG, +520 SHORT). sl_origin_vs_layer.by_basis.retestBar n=38805 (de 37429), E[R] 0.208 vs 0.061, delta 0.147 CI90=[0.118,0.187], estable/ligeramente mas fuerte. retestBar2 (1m SHORT) n=10755, delta 0.035 CI90=[0.007,0.062] -- positivo pero limite inferior estrechandose lectura a lectura (0.012->0.008->0.007), vigilar. HALLAZGO DEL DIA en since_change: (1) 29m/RETEST/LONG -- segmento del gate -- TERCERA lectura consecutiva confirmando (delta=0.402 CI90=[0.106,0.771] n=344), limite inferior subiendo tres dias seguidos (0.009->0.041->0.106): cumple la politica de 2-3 lecturas, se trata como estable en la medicion paralela; (2) 29m/RETEST/SHORT certifica por PRIMERA VEZ (delta=0.134 CI90=[0.019,0.265] n=407). 11/12 segmentos RETEST certifican; solo falta 15m SHORT (0.114 [-0.023,0.277] n=697). slCauseMitigated del gate sigue false (verdict mecanico flat, mismatch permanente desde 2026-11-08). Ningun cambio de input nuevo en scalp_command.pine.",
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
      "2026-10-29 (jueves): CORRECCION DE METODO, no reversion de senal. analyze.py tenia un piso demasiado bajo en invalid_geometry (excluia solo slOrigTk<=0); con slOrigTk=1 (SL estructural a 1 tick de la entrada, denominador casi cero) rOrig explotaba a valores absurdos (hasta 3403R en BTCUSDT, tambien visto en NQ/GC/YM, no es exclusivo de un simbolo). Eso inflaba by_basis y since_change: antes de hoy by_basis.retestBar reportaba delta=0.397 (n=30186) y since_change decia 6/6 segmentos RETEST certificando limpio un mes completo sin reversion. Se subio el piso a slOrigTk<=1 (excluye ~2723 filas degeneradas de retestBar y ~716 de retestBar2) y se recalculo: by_basis.retestBar delta bajo a 0.087 CI90=[0.068,0.105] (n=27463, sigue sin cruzar cero, la direccion del edge es real, la magnitud previa era ficticia) y retestBar2 a delta=0.033 CI90=[0.004,0.061] (n=8046, al filo). since_change con el piso corregido: de los 6 segmentos RETEST, SOLO 3 certifican limpio hoy (2m/RETEST/LONG delta=0.061 CI90=[0.018,0.103] n=3515; 5m/RETEST/LONG delta=0.138 CI90=[0.065,0.233] n=1547; 5m/RETEST/SHORT delta=0.077 CI90=[0.002,0.168] n=1070); 1m/RETEST/LONG (delta=0.032 CI90=[0.0,0.065] n=7130), 1m/RETEST/SHORT (delta=0.031 CI90=[-0.005,0.065] n=4909) y 2m/RETEST/SHORT (delta=0.054 CI90=[0.0,0.111] n=2266) ya NO certifican (CI90 toca o cruza cero). La narrativa previa de \"6/6 certifican, un mes sin reversion\" era optimismo inflado por la geometria degenerada, no evidencia real de ese alcance. No se revierte el cambio aplicado en TradingView (la direccion sigue siendo real donde certifica, y no hay evidencia de que haga dano en 1m/2m SHORT, solo que no esta confirmado ahi). Se baja la confianza documentada de \"aplicado, 6/6 certifican de forma sostenida\" a \"aplicado, 3/6 certifican tras corregir geometria degenerada (2m LONG, 5m LONG, 5m SHORT); 1m LONG, 1m SHORT y 2m SHORT sin confirmar, vigilar si recuperan CI90>0 con mas muestra o si se mantienen al filo\". Vigilar en corridas futuras si 1m/2m SHORT recuperan certificacion con mas dato limpio.",
      "2026-11-01 (domingo, REVISION SEMANAL 2026-week-44): since_change (geometria corregida del 10-29) se recupera con mas dato limpio -- los 6 segmentos clasicos vuelven a certificar (delta_beats_zero=true en los 6), aunque 1m/RETEST/LONG sigue al filo (delta=0.033 CI90=[0.001,0.066] n=7475, limite inferior casi en cero, el mas debil de los 6, sin cambio desde ayer por falta de dato nuevo de domingo). 2m/RETEST/LONG delta=0.06 CI90=[0.019,0.102] n=3684; 1m/RETEST/SHORT delta=0.043 CI90=[0.008,0.077] n=5607; 2m/RETEST/SHORT delta=0.052 CI90=[0.005,0.1] n=2582; 5m/RETEST/LONG delta=0.183 CI90=[0.107,0.275] n=1770; 5m/RETEST/SHORT delta=0.172 CI90=[0.062,0.3] n=1304 -- los 6 recuperan la certificacion limpia que se habia perdido parcialmente el 10-29 (entonces 3/6). Primera lectura de since_change para los TF nuevos (medicion paralela, no requiere que el cambio se 'aplicara' a ellos): 3m/RETEST/LONG delta=0.331 CI90=[0.205,0.465] n=657 certifica fuerte; 3m/RETEST/SHORT delta=0.102 CI90=[-0.002,0.213] n=653 al filo (no certifica); 5m->15m/RETEST/LONG delta=0.577 CI90=[0.245,0.996] n=255 certifica; 15m/RETEST/SHORT delta=0.175 CI90=[-0.007,0.38] n=268 no certifica; 29m/RETEST/LONG delta=0.925 CI90=[0.08,2.114] n=106 certifica (CI90 muy ancho, muestra chica); 29m/RETEST/SHORT delta=0.237 CI90=[0.045,0.494] n=163 certifica. Se sube la confianza documentada de 'aplicado, 3/6 certifican tras corregir geometria degenerada' a 'aplicado, 6/6 clasicos vuelven a certificar (1m LONG al filo), mas evidencia nueva favorable en 3/4 TF nuevos (3m LONG, 15m LONG, 29m LONG/SHORT; 3m SHORT y 15m SHORT todavia al filo)'. Hallazgo de la revision semanal de hoy (no de este experimento): se diagnostico y corrigio un artefacto de alcance en shadow_rules (v3->v4, ver reviews/2026-week-44.md) -- no cambia nada de este experimento, se anota por el cruce de ambos temas (shadow_rules segui pendiente de pasar de rMultiple a rOrig, sin cambio hoy).",
      "2026-11-03 (martes): since_change (post-2026-09-26) con mas dato, n total sube a 26784. 1m/RETEST/LONG, el mas fragil de los 6 clasicos, CRUZA hoy a NO certificar: delta=0.03 CI90=[-0.001,0.061] n=7619 (limite inferior pasa a ligeramente negativo, de [0.001,0.066] el 2026-11-01) -- primera vez que el limite inferior toca negativo desde que se viene vigilando 'al filo'; no amerita revertir (delta sigue positivo, n grande, solo un cruce marginal de CI90). Los otros 5 clasicos se mantienen o mejoran: 1m/RETEST/SHORT delta=0.038 CI90=[0.005,0.07] n=5966; 2m/RETEST/LONG delta=0.062 CI90=[0.023,0.104] n=3757; 2m/RETEST/SHORT delta=0.056 CI90=[0.006,0.11] n=2751; 5m/RETEST/LONG delta=0.182 CI90=[0.11,0.263] n=1926; 5m/RETEST/SHORT delta=0.227 CI90=[0.096,0.387] n=1422. TF nuevos: 3m/RETEST/LONG delta=0.281 CI90=[0.173,0.401] n=881 fuerte; 3m/RETEST/SHORT delta=0.064 CI90=[-0.033,0.167] n=814 al filo (no certifica, bajo frente a ayer); 15m/RETEST/LONG delta=0.746 CI90=[0.337,1.249] n=351 fuerte; 15m/RETEST/SHORT delta=0.296 CI90=[0.061,0.589] n=340 certifica; 29m/RETEST/LONG delta=0.62 CI90=[0.026,1.428] n=152 certifica (recupera FDR agregado tambien hoy, ver segment_significance); 29m/RETEST/SHORT delta=0.149 CI90=[-0.027,0.375] n=193 al filo (no certifica). A nivel de bus (ALERTAS de hoy): by_basis.retestBar (incluye pre-cambio) n=31023 E[R] 0.147 vs 0.042 delta 0.105 CI90=[0.086,0.123]; by_basis.retestBar2 (1m SHORT + vela previa) n=9103 delta 0.037 CI90=[0.009,0.066]. Sin cambio de decision: ningun segmento desarrolla delta_below_zero=true, no se revierte nada; se vigila de cerca 1m/RETEST/LONG, ahora el unico de los 6 clasicos sin certificar limpio en since_change."
    ],
    "appliedNote": "2026-09-26: aplicado en scalp_command.pine (input sc_sl_retest_basis, default 'Auto (como se midio)'): en RETEST el SL real pasa a la mecha de la vela del retest; 1m SHORT suma la vela previa (retestBar2), igual que la medicion paralela. Base: los 6 segmentos RETEST certifican con CI90 > 0 (n=11273, E[R] 0.238 vs 0.065). El tier se sigue calculando con el stop de 3 capas. El feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig, asi que sl_origin_vs_layer sigue siendo la vigilancia. Rige en cada grafico desde que Jesus re-pega scalp_cc_FULL_for_tradingview.pine. Revertir = poner la base en '3 capas'.",
    "beforeN": 18341,
    "afterN": 44518,
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
      "n": 44518,
      "wrTP1": 47.7,
      "nSL": 20773,
      "nTO": 2498,
      "expR": 0.06,
      "pf": 1.12,
      "mfe_p25": 10.0,
      "mfe_p50": 23.0,
      "mfe_p75": 57.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 51.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 38.0
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
    "hypothesis": "No es un experimento propuesto por el agente, es un cambio detectado en el DATO que agent-instructions.md pide registrar como posible cambio de input de Jesus: el campo aligned (que define la causa de SL contra-sesgo) paso de ser casi siempre 1 (aligned=0 en ~0.0-0.1% de las perdidas, W36-W43) a aligned=0 en 20-46% de las senales desde 2026-10-26, visible en TODOS los simbolos (YM 20.9%, GC 23.5%, NQ 29.4%, ES 30.3%, CL 32.1% desde esa fecha), no solo en los simbolos nuevos BTCUSDT/ETHUSDT (42-46%, mas alto pero no categoricamente distinto). El campo ver se mantiene en v4 todo el tiempo, por lo que si hubo un cambio de input no quedo registrado ahi. Contraintuitivo: aligned=0 NO rinde peor -- by_aligned de hoy da aligned=0 E[R]=0.084 PF=1.19 WR=54.3% (n=2471) vs aligned=1 E[R]=0.039 PF=1.08 WR=46.2% (n=45549), es decir el grupo contra-sesgo rinde MEJOR. El salto de causas_pct contra-sesgo a 27% en sl_post_mortem_weekly_trend (W44) es un efecto de que crecio mucho de muestra, no evidencia de que el bias filter se haya roto o deba endurecerse. 2026-10-31: se mantiene el patron contraintuitivo con mas muestra -- by_aligned de hoy: aligned=0 n=2660 E[R]=0.066 PF=1.14 WR=53.3% vs aligned=1 n=46734 E[R]=0.038 PF=1.08 WR=46.3%. El salto de la causa 'contra-sesgo' a 25.4% de las perdidas en sl_post_mortem_weekly_trend W44 (vs 0.0% en W41-43) es, de nuevo, crecimiento de muestra del grupo aligned=0, no un problema nuevo -- ese grupo sigue rindiendo mejor que aligned=1, no peor. Confirmacion repetida, no se toca el filtro de sesgo. 2026-11-01 (REVISION SEMANAL 2026-week-44): CUARTA confirmacion consecutiva del patron contraintuitivo, con mas muestra -- by_aligned de hoy: aligned=0 n=2745 E[R]=0.071 PF=1.16 WR=53.4% vs aligned=1 n=46836 E[R]=0.038 PF=1.08 WR=46.2%. El salto de la causa 'contra-sesgo' en sl_post_mortem_weekly_trend (25.6% en W44) sigue siendo el mismo efecto de muestra ya diagnosticado, no un problema nuevo. Dato adicional de esta revision (sin resolver la pregunta pendiente): la aparicion de BTCUSDT/ETHUSDT y de los TF 3m/15m/29m se confirmo hoy como un cambio real y deliberado de alcance del indicador (no artefacto de dato), con primera aparicion el 2026-10-26/27 en signals/*.jsonl -- coincide con la fecha de este cambio de 'aligned', reforzando la hipotesis de que ambos cambios vinieron juntos en la misma actualizacion de Jesus, pero sigue sin confirmacion directa de el. Sigue pendiente la pregunta a Jesus. 2026-11-03: QUINTA confirmacion consecutiva del patron contraintuitivo, con mas muestra -- by_aligned de hoy: aligned=0 n=3182 E[R]=0.093 PF=1.21 WR=54.1% vs aligned=1 n=48259 E[R]=0.04 PF=1.08 WR=46.3%. Sigue pendiente la pregunta a Jesus sobre el origen del cambio del 2026-10-26; mientras no se confirme, no se toca el filtro de sesgo. 2026-11-04: SEXTA confirmacion consecutiva del patron contraintuitivo, con mas muestra -- by_aligned de hoy: aligned=0 n=3540 E[R]=0.096 PF=1.21 WR=53.9% vs aligned=1 n=49619 E[R]=0.039 PF=1.08 WR=46.3%, la brecha a favor de aligned=0 sigue ampliandose (de 0.093 vs 0.04 el 11-03 a 0.096 vs 0.039 hoy). Dato adicional: el modelo P(TP1) de hoy (model.coefficients, n=49776) pesa `aligned` en -0.017 (negativo) -- el modelo in-sample corrobora la misma direccion que el corte empirico (aligned=1 resta probabilidad de TP1), consistente entre dos metodos independientes. Sigue sin confirmacion directa de Jesus sobre el origen del cambio del 2026-10-26; mientras no se confirme, no se toca el filtro de sesgo. 2026-11-05: se mantiene el patron contraintuitivo con mas muestra -- by_aligned de hoy: aligned=0 n=3805 E[R]=0.087 PF=1.19 WR=53.5% vs aligned=1 n=50871 E[R]=0.044 PF=1.09 WR=46.4%. Sin cambio de conclusion: el grupo contra-sesgo sigue rindiendo mejor, no peor; no se toca el filtro. Aun sin confirmar con Jesus que cambio exactamente el 2026-10-26 en el calculo de aligned/biasScore. 2026-11-06: se mantiene el patron contraintuitivo con mas muestra -- by_aligned de hoy: aligned=0 n=4052 E[R]=0.083 PF=1.18 WR=53.1% vs aligned=1 n=51961 E[R]=0.047 PF=1.1 WR=46.4%. Sin cambio de conclusion: el grupo contra-sesgo sigue rindiendo mejor, no peor; no se toca el filtro. Aun sin confirmar con Jesus que cambio exactamente el 2026-10-26 en el calculo de aligned/biasScore. 2026-11-08 (REVISION SEMANAL 2026-week-45): SEPTIMA confirmacion consecutiva del patron contraintuitivo, con mas muestra -- by_aligned de hoy: aligned=0 n=4439 E[R]=0.101 PF=1.22 WR=53.2% vs aligned=1 n=53129 E[R]=0.047 PF=1.1 WR=46.3%, la brecha sigue ampliandose (0.096 el 11-06 -> 0.101 hoy). El salto de la causa 'contra-sesgo' en sl_post_mortem_weekly_trend baja de 26.0% (W44) a 19.6% (W45) a medida que crece el denominador de perdidas de la semana -- mismo efecto de muestra ya diagnosticado, no un problema nuevo. Sigue sin confirmacion directa de Jesus sobre el origen del cambio del 2026-10-26; mientras no se confirme, no se toca el filtro de sesgo. Detalle en reviews/2026-week-45.md.",
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
    "date": "2026-11-13",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-11-12T16:07:39-06:00",
    "schema": "sa-plan-2",
    "cleanest": "NQ",
    "focus": {
      "sym": "NQ",
      "verdict": "WAIT",
      "window": "20:00-23:30 CT",
      "setup": {
        "es": "rebote del cluster TDO+VAL+FVG 15m 28169-28212 (confluencia 10, A+ del metodo) tras el round-trip del dia",
        "en": "a bounce off the TDO+VAL+15m FVG cluster 28169-28212 (confluence 10, A+ by the method) after today's round-trip"
      },
      "trigger": {
        "es": "cierre 5m de vuelta sobre 28212 tras testear el cluster; sin ese cierre es anticipar un nivel que todavia no rechazo",
        "en": "a 5m close back above 28212 after testing the cluster; without that close it's front-running a level that hasn't rejected yet"
      },
      "invalid": {
        "es": "cierre 1h sostenido bajo 28093.75 perdiendo el EMA200 28339.75",
        "en": "a sustained 1h close below 28093.75, also losing the EMA200 28339.75"
      },
      "note": {
        "es": "hoy fue el dia mas chopeado de la racha (4 flips, round-trip completo) -- si entras, respeta el stop del libro y no promedies; no es dia para subir tamaño tras un ganador o una perdida",
        "en": "today was the choppiest day of the run (4 flips, a full round-trip) -- if you're in, respect the resting stop and don't average in; not a day to size up after a winner or a loser"
      }
    },
    "summary": {
      "es": [
        "!! cron descalzado por DST, ajustar: hubo un disparo a las 15:31 CT (antes del cierre de 16:00) y otro a las 16:06 CT",
        "NQ: largo revivido tras romperse el corto de la mañana en la misma sesion (shock Nvidia); A+ rebote VAL 28169-28212, WAIT a la espera del gatillo.",
        "ES: sin sesgo medido (24h plano, checklist con 8 flips); cluster 7559.25-7596 es B (fade IB paga solo 28% aqui), WAIT.",
        "GC: el mas estirado de los 5 (15.71 ATR) tras dolar/rendimientos fuertes; sin borde a tiro, AVOID, cluster 3919-3927.2 solo de watch.",
        "YM: dentro de la zona dorada tras barrer el IB a la baja, pero con conflicto de marcos activo (1h vs 4h); WAIT, A+ a tiro pero sin GO por regla dura.",
        "CL: ruptura alcista por titular de Iran, 2o mas estirado (12.15 ATR) en maximos; AVOID, el fade de 89.15-89.35 va contra el checklist, tope B.",
        "mas limpio: NQ",
        "limite $1000 por cuenta (extremo bajo) ⇒ en la mejor A+ (NQ, stop ~$1020/contrato full) sale 0 contratos en full: considera micros (MNQ, stop ~$102) o pasa la zona.",
        "contexto fuera del grafico ALTO: renuncia del CEO de Nvidia sacudio el Nasdaq sin evento de calendario (NQ/ES, risk-off); Trump sobre Iran ('tenemos su Estrecho') empujo el petroleo (CL). VIX +8% rompiendo maximo previo, US10Y +2.1% rompiendo maximo previo, DXY +0.26% rompiendo maximo previo, BTC -3.46% rompiendo minimo previo -- tono risk-off real, no solo ruido.",
  
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 41237,
  "by_verdict": {
    "AVOID": {
      "n": 4732,
      "wrTP1": 46.5,
      "nSL": 2215,
      "nTO": 317,
      "expR": 0.088,
      "pf": 1.18,
      "mfe_p25": 10.0,
      "mfe_p50": 23.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 31.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 38.6
    },
    "GO": {
      "n": 4289,
      "wrTP1": 47.2,
      "nSL": 2048,
      "nTO": 218,
      "expR": -0.003,
      "pf": 0.99,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.799999999999955,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 40.2
    },
    "WAIT": {
      "n": 32216,
      "wrTP1": 47.6,
      "nSL": 14996,
      "nTO": 1870,
      "expR": 0.068,
      "pf": 1.14,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 29.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 36.6
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.088,
      "ci90": [
        0.056,
        0.121
      ],
      "p_mean_le_0": 0.0,
      "n": 4542
    },
    "GO": {
      "expR": -0.003,
      "ci90": [
        -0.032,
        0.026
      ],
      "p_mean_le_0": 0.572,
      "n": 4169
    },
    "WAIT": {
      "expR": 0.068,
      "ci90": [
        0.057,
        0.08
      ],
      "p_mean_le_0": 0.0,
      "n": 31331
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 4732,
      "wrTP1": 46.5,
      "nSL": 2215,
      "nTO": 317,
      "expR": 0.088,
      "pf": 1.18,
      "mfe_p25": 10.0,
      "mfe_p50": 23.0,
      "mfe_p75": 48.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 31.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 38.6
    },
    "GO_or_WAIT": {
      "n": 36505,
      "wrTP1": 47.6,
      "nSL": 17044,
      "nTO": 2088,
      "expR": 0.06,
      "pf": 1.12,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 28.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 37.0
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.088,
      "ci90": [
        0.056,
        0.121
      ],
      "p_mean_le_0": 0.0,
      "n": 4542
    },
    "GO_or_WAIT": {
      "expR": 0.06,
      "ci90": [
        0.049,
        0.071
      ],
      "p_mean_le_0": 0.0,
      "n": 35500
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 65,
        "wrTP1": 49.2,
        "nSL": 27,
        "nTO": 6,
        "expR": -0.036,
        "pf": 0.92,
        "mfe_p25": 8.25,
        "mfe_p50": 21.0,
        "mfe_p75": 33.25,
        "winnerMAE_p75": 17.5,
        "winnerMAE_p90": 24.700000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 33.3
      },
      "GO": {
        "n": 68,
        "wrTP1": 57.4,
        "nSL": 24,
        "nTO": 5,
        "expR": 0.247,
        "pf": 1.68,
        "mfe_p25": 7.0,
        "mfe_p50": 19.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 13.5,
        "winnerMAE_p90": 39.60000000000001,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -9.0,
        "revAfterSL_rate": 33.3
      },
      "WAIT": {
        "n": 481,
        "wrTP1": 48.2,
        "nSL": 205,
        "nTO": 44,
        "expR": 0.075,
        "pf": 1.17,
        "mfe_p25": 6.0,
        "mfe_p50": 15.0,
        "mfe_p75": 34.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 25.900000000000006,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 16.1
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 50,
        "wrTP1": 46.0,
        "nSL": 20,
        "nTO": 7,
        "expR": 0.036,
        "pf": 1.08,
        "mfe_p25": 9.0,
        "mfe_p50": 20.0,
        "mfe_p75": 34.5,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 23.800000000000004,
        "loserMFEbeforeSL_p50": 13.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -14.5,
        "revAfterSL_rate": 10.0
      },
      "GO": {
        "n": 30,
        "wrTP1": 60.0,
        "nSL": 9,
        "nTO": 3,
        "expR": 0.123,
        "pf": 1.4,
        "mfe_p25": 12.75,
        "mfe_p50": 25.0,
        "mfe_p75": 59.75,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 60.50000000000006,
        "loserMFEbeforeSL_p50": 25.0,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 9.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 11.1
      },
      "WAIT": {
        "n": 346,
        "wrTP1": 50.9,
        "nSL": 132,
        "nTO": 38,
        "expR": 0.161,
        "pf": 1.41,
        "mfe_p25": 8.0,
        "mfe_p50": 25.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 29.5,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 25.0
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 2865,
        "wrTP1": 46.0,
        "nSL": 1358,
        "nTO": 189,
        "expR": 0.082,
        "pf": 1.17,
        "mfe_p25": 10.0,
        "mfe_p50": 22.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 37.3
      },
      "GO": {
        "n": 2886,
        "wrTP1": 47.4,
        "nSL": 1381,
        "nTO": 137,
        "expR": 0.008,
        "pf": 1.02,
        "mfe_p25": 6.0,
        "mfe_p50": 16.0,
        "mfe_p75": 34.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 39.5
      },
      "WAIT": {
        "n": 17512,
        "wrTP1": 47.5,
        "nSL": 8205,
        "nTO": 989,
        "expR": 0.069,
        "pf": 1.14,
        "mfe_p25": 7.0,
        "mfe_p50": 17.0,
        "mfe_p75": 40.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 36.8
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 1752,
        "wrTP1": 47.2,
        "nSL": 810,
        "nTO": 115,
        "expR": 0.104,
        "pf": 1.21,
        "mfe_p25": 11.5,
        "mfe_p50": 25.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 35.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 41.6
      },
      "GO": {
        "n": 1305,
        "wrTP1": 45.8,
        "nSL": 634,
        "nTO": 73,
        "expR": -0.043,
        "pf": 0.91,
        "mfe_p25": 9.0,
        "mfe_p50": 19.0,
        "mfe_p75": 38.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.5,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 42.4
      },
      "WAIT": {
        "n": 13877,
        "wrTP1": 47.7,
        "nSL": 6454,
        "nTO": 799,
        "expR": 0.065,
        "pf": 1.13,
        "mfe_p25": 10.0,
        "mfe_p50": 22.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 37.2
      }
    }
  },
  "by_kind_side_ci90": {
    "INV/LONG": {
      "AVOID": {
        "expR": -0.036,
        "ci90": [
          -0.236,
          0.161
        ],
        "p_mean_le_0": 0.608,
        "n": 62
      },
      "GO": {
        "expR": 0.247,
        "ci90": [
          0.02,
          0.48
        ],
        "p_mean_le_0": 0.034,
        "n": 67
      },
      "WAIT": {
        "expR": 0.075,
        "ci90": [
          -0.02,
          0.174
        ],
        "p_mean_le_0": 0.102,
        "n": 467
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "expR": 0.036,
        "ci90": [
          -0.21,
          0.296
        ],
        "p_mean_le_0": 0.427,
        "n": 47
      },
      "GO": {
        "expR": 0.123,
        "ci90": [
          -0.122,
          0.362
        ],
        "p_mean_le_0": 0.209,
        "n": 30
      },
      "WAIT": {
        "expR": 0.161,
        "ci90": [
          0.057,
          0.266
        ],
        "p_mean_le_0": 0.005,
        "n": 337
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "expR": 0.082,
        "ci90": [
          0.04,
          0.123
        ],
        "p_mean_le_0": 0.001,
        "n": 2754
      },
      "GO": {
        "expR": 0.008,
        "ci90": [
          -0.029,
          0.042
        ],
        "p_mean_le_0": 0.374,
        "n": 2815
      },
      "WAIT": {
        "expR": 0.069,
        "ci90": [
          0.053,
          0.085
        ],
        "p_mean_le_0": 0.0,
        "n": 17097
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "expR": 0.104,
        "ci90": [
          0.051,
          0.158
        ],
        "p_mean_le_0": 0.001,
        "n": 1679
      },
      "GO": {
        "expR": -0.043,
        "ci90": [
          -0.096,
          0.006
        ],
        "p_mean_le_0": 0.927,
        "n": 1257
      },
      "WAIT": {
        "expR": 0.065,
        "ci90": [
          0.047,
          0.083
        ],
        "p_mean_le_0": 0.0,
        "n": 13430
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5); by_kind_side_ci90 = bootstrap 90% CI de E[R] por celda kind/side x veredicto (solo celdas con n>=8, null si bootstrap_er_ci no puede calcular) -- agregado 2026-11-08 porque los playbooks venian recalculando esto a mano cada corrida sin poder citar un CI90 propio del corte cruzado."
}
```

## Modo sombra (peldano 0->1, gate en execution-ladder.md)
```json
{
  "rule": {
    "version": 4,
    "definedAt": "2026-11-01",
    "criteria": {
      "kind": [
        "RETEST"
      ],
      "tf_side": [
        "1/LONG",
        "1/SHORT",
        "2/LONG",
        "2/SHORT",
        "3/LONG",
        "3/SHORT",
        "5/LONG",
        "5/SHORT"
      ],
      "excludeSaVerdict": []
    },
    "rationale": "REVISION SEMANAL 2026-11-01 (v3->v4): se agrega 3/LONG y 3/SHORT a tf_side. shadow_weekly venia marcando shadow_beats_raw=false de forma sostenida (W41-W44) porque desde que aparecieron TF nuevos en el bus (3m/15m/29m, ~2026-10-29) raw_indicator los incluye pero shadow (criterio v3) no, asi que shadow dejo de ser un subconjunto distinto de raw -- en las semanas donde el criterio v3 cubre todo el universo clasico (W36-W43, antes de que 3m/15m/29m tuvieran muestra) shadow_n era literalmente igual a raw_n (comparacion trivial, nunca puede batir a algo idéntico a si mismo); en W44 (con los TF nuevos ya con muestra) raw_expR=0.027 > shadow_expR=0.01 porque las senales nuevas que shadow excluye rinden bien y raw si las cuenta. De los tres TF nuevos, 3m/RETEST/LONG (n=764, survives_fdr10=true, CI90=[0.008,0.141]) y 3m/RETEST/SHORT (n=738, survives_fdr10=true, CI90=[0.04,0.177]) cumplen HOY el mismo estandar que uso la revision v1->v2 para sumar 2m LONG/5m SHORT (FDR 10% + cross_instrument verdict=universal, spread 0.323 y 0.327 respectivamente) -- se agregan. 15m (survives_fdr10=false en ambos lados) y 29m (survives_fdr10=true en SHORT pero cross_instrument=instrument-specific, spread 0.916, y sin una sola semana ISO cerrada de historial, todo su n vive en W44) NO cumplen el estandar todavia -- quedan fuera de v4, igual que 2m LONG/5m SHORT se quedaron fuera de v1 hasta madurar. Ver reviews/2026-week-44.md para el detalle. Historia v1/v2/v3 abajo. REVISION 2026-10-31 (v2->v3): se quita el filtro por veredicto Session Analyst. Con n=24k cruzados, AVOID rinde E[R] +0.022 (mejor que GO +0.005) y WAIT es el mejor (+0.043, CI90 limpio, estable desde 2026-09-11); excluir AVOID dejaba la sombra en +0.036 contra +0.038 del indicador crudo, o sea el filtro restaba. El veredicto SA es un plan de sesion para el trader, no un filtro de senales scalp: no volver a excluir por SA salvo que session_analyst_cross muestre AVOID con CI90 negativo durante 3 semanas. Historia v1/v2 abajo. kind=RETEST (prioridad 1; INV no tiene ningun segmento con survives_fdr10=true todavia). REVISION SEMANAL 2026-09-27 (v1->v2): v1 (2026-09-20) limitaba tf_side a 4 segmentos (1/LONG, 1/SHORT, 2/SHORT, 5/LONG) porque 2m LONG y 5m SHORT todavia cruzaban/rozaban cero en ese momento. Desde entonces segment_significance certifico ambos de forma sostenida durante varias corridas seguidas (2m LONG desde 2026-09-18, 5m SHORT desde antes) sin ninguna reversion, y hoy los 6 segmentos RETEST (1m/2m/5m x LONG/SHORT) tienen survives_fdr10=true con CI90 que no cruza cero -- ver segment_significance de hoy. Se amplia tf_side a los 6 segmentos certificados; la justificacion vieja de v1 (excluir 2m LONG/5m SHORT por CI90 rozando cero) ya no la sostiene el dato, quedaba pendiente de esta revision semanal desde 2026-09-24 (ver playbook buy-retest.md, historico). Se excluyen senales del dia/sesion en un instrumento con veredicto Session Analyst=AVOID: avoid_vs_rest_ci90.AVOID no es significativo (p_mean_le_0 alto) mientras GO y WAIT si lo son (session_analyst_cross). SL/objetivo = el mismo del indicador (3 capas); el SL estructural de experiments.json (sl-retest-wick) SE APLICO en TradingView el 2026-09-26 pero el feed sigue registrando el 3-capas como rMultiple (el SL real ya cambio, la medicion paralela sigue corriendo en sl_origin_vs_layer) -- no se incorpora a la sombra hasta que haya muestra post-cambio suficiente para decidir si usar rOrig en vez de rMultiple."
  },
  "shadow": {
    "n": 60371,
    "wrTP1": 47.0,
    "nSL": 28108,
    "nTO": 3899,
    "expR": 0.052,
    "pf": 1.11,
    "mfe_p25": 9.0,
    "mfe_p50": 21.0,
    "mfe_p75": 48.0,
    "winnerMAE_p75": 14.0,
    "winnerMAE_p90": 33.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -16.0,
    "revAfterSL_rate": 35.5
  },
  "shadow_ci90": {
    "expR": 0.052,
    "ci90": [
      0.044,
      0.061
    ],
    "p_mean_le_0": 0.0,
    "n": 58394
  },
  "raw_indicator": {
    "n": 62859,
    "wrTP1": 47.2,
    "nSL": 29209,
    "nTO": 4011,
    "expR": 0.057,
    "pf": 1.12,
    "mfe_p25": 9.0,
    "mfe_p50": 22.0,
    "mfe_p75": 51.0,
    "winnerMAE_p75": 15.0,
    "winnerMAE_p90": 40.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -17.0,
    "revAfterSL_rate": 36.5
  },
  "raw_indicator_ci90": {
    "expR": 0.057,
    "ci90": [
      0.049,
      0.066
    ],
    "p_mean_le_0": 0.0,
    "n": 60782
  },
  "tier_ap_b_only": {
    "n": 31295,
    "wrTP1": 44.6,
    "nSL": 15145,
    "nTO": 2195,
    "expR": 0.045,
    "pf": 1.09,
    "mfe_p25": 9.0,
    "mfe_p50": 20.0,
    "mfe_p75": 46.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 30.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -16.0,
    "revAfterSL_rate": 34.1
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.045,
    "ci90": [
      0.033,
      0.057
    ],
    "p_mean_le_0": 0.0,
    "n": 30271
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```

## Modo sombra por semana (gate: shadow_beats_raw 3 semanas seguidas, n>=60)
```json
{
  "2026-W36": {
    "shadow_n": 3136,
    "shadow_expR": -0.027,
    "raw_n": 3136,
    "raw_expR": -0.027,
    "shadow_beats_raw": false
  },
  "2026-W37": {
    "shadow_n": 5248,
    "shadow_expR": 0.07,
    "raw_n": 5248,
    "raw_expR": 0.07,
    "shadow_beats_raw": false
  },
  "2026-W38": {
    "shadow_n": 4807,
    "shadow_expR": 0.091,
    "raw_n": 4807,
    "raw_expR": 0.091,
    "shadow_beats_raw": false
  },
  "2026-W39": {
    "shadow_n": 5227,
    "shadow_expR": 0.051,
    "raw_n": 5227,
    "raw_expR": 0.051,
    "shadow_beats_raw": false
  },
  "2026-W40": {
    "shadow_n": 5223,
    "shadow_expR": 0.016,
    "raw_n": 5223,
    "raw_expR": 0.016,
    "shadow_beats_raw": false
  },
  "2026-W41": {
    "shadow_n": 5084,
    "shadow_expR": 0.057,
    "raw_n": 5084,
    "raw_expR": 0.057,
    "shadow_beats_raw": false
  },
  "2026-W42": {
    "shadow_n": 4993,
    "shadow_expR": 0.05,
    "raw_n": 4993,
    "raw_expR": 0.05,
    "shadow_beats_raw": false
  },
  "2026-W43": {
    "shadow_n": 4609,
    "shadow_expR": -0.005,
    "raw_n": 4609,
    "raw_expR": -0.005,
    "shadow_beats_raw": false
  },
  "2026-W44": {
    "shadow_n": 9423,
    "shadow_expR": 0.023,
    "raw_n": 10312,
    "raw_expR": 0.027,
    "shadow_beats_raw": false
  },
  "2026-W45": {
    "shadow_n": 6959,
    "shadow_expR": 0.099,
    "raw_n": 7899,
    "raw_expR": 0.121,
    "shadow_beats_raw": false
  },
  "2026-W46": {
    "shadow_n": 5662,
    "shadow_expR": 0.118,
    "raw_n": 6321,
    "raw_expR": 0.127,
    "shadow_beats_raw": false
  }
}
```
