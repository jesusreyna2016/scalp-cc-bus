# Scalp CC · report 2026-11-04T02:15Z
- signals=53220 outcomes=51568 pares_resueltos=53159 pendientes=61 huerfanos=61

## ⚠ ALERTAS (llevar al frente del resumen)
- ORFANOS: subieron a 61 (+4). Revisar pipeline Pine/ingest si sigue subiendo sin recompilar.
- GATE: 29m/RETEST/LONG cumple el chequeo numerico agregado (n/PF/WR) pero NO el gate completo todavia -- weeklyStable3=False, slCauseMitigated=False. Es un near-miss a vigilar, no subir de peldano.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.151 vs 0.043, delta 0.109 CI90 [0.091, 0.127], n 32083). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.059 vs 0.02, delta 0.04 CI90 [0.012, 0.067], n 9561). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=AVOID rinden MEJOR de forma no-random (E[R] 0.078 CI90 [0.035, 0.118], n 2983). Contrario a la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.051 CI90 [0.039, 0.063], n 26809). Consistente con la hipotesis original de agent-instructions.md.
- METODO: tus predicciones de direccion aciertan 0.0% (peor que un volado, n=6, MAE=0.265). Se mas conservador con 'cambio del mes' y marcar experimental mas tiempo antes de subir confianza.
- MODO SOMBRA: 3 semanas CERRADAS seguidas sin batir al indicador crudo (2026-W42, 2026-W43, 2026-W44) -- espejo inverso del gate de promocion del peldano 0->1. No implica bajar de peldano (ya promovido), pero revisar shadow_rules en la revision semanal.

- E[R] global: {"expR": 0.043, "ci90": [0.034, 0.052], "p_mean_le_0": 0.0, "n": 51507}
- gate ejecucion: {"readyForLive": true, "segment": "29m/RETEST/LONG", "weeklyStable3": false, "weeklyDetail": [{"week": "2026-W42", "wrTP1": null, "pf": null, "ok": false}, {"week": "2026-W43", "wrTP1": null, "pf": null, "ok": false}, {"week": "2026-W44", "wrTP1": 54.5, "pf": 1.29, "ok": false}], "slCauseMitigated": false, "fullyReady": false, "note": "readyForLive: n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side (solo agregado historico). fullyReady exige ademas weeklyStable3 (3 semanas CERRADAS seguidas con WR>=50 & PF>=1.3 en ese mismo segmento) y slCauseMitigated (experimento con verdict=confirmed dirigido a ese segmento). Solo fullyReady=true es luz verde real para subir de peldano; readyForLive=true con fullyReady=false es un near-miss a vigilar."}

## Integridad de sigId (colisiones, posible causa de alertas MUESTRA)
```json
{
  "signals": {
    "total_sigIds": 48207,
    "collided_sigIds": 4636,
    "collided_pct": 9.62,
    "delta_days_histogram": {
      "14": 964,
      "7": 887,
      "21": 524,
      "28": 490,
      "35": 439,
      "42": 402,
      "56": 184,
      "49": 179,
      "48": 67,
      "34": 63
    },
    "conflicting_result_n": 0,
    "conflicting_result_examples": []
  },
  "outcomes": {
    "total_sigIds": 46884,
    "collided_sigIds": 4342,
    "collided_pct": 9.26,
    "delta_days_histogram": {
      "14": 920,
      "7": 832,
      "21": 488,
      "28": 459,
      "35": 405,
      "42": 357,
      "49": 172,
      "56": 171,
      "34": 63,
      "48": 60
    },
    "conflicting_result_n": 2506,
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
| 15m/RETEST/LONG | 403 | 50.1 | 0.051 | 1.1 | 197 | 75.5 | 109.0 | 51.8 |
| 15m/RETEST/SHORT | 431 | 52.9 | 0.116 | 1.25 | 199 | 158.0 | 556.25 | 67.8 |
| 1m/INV/LONG | 462 | 47.0 | 0.12 | 1.27 | 195 | 15.0 | 11.0 | 18.5 |
| 1m/INV/SHORT | 353 | 46.2 | 0.106 | 1.25 | 140 | 21.0 | 14.0 | 16.4 |
| 1m/RETEST/LONG | 17320 | 45.0 | 0.024 | 1.05 | 8329 | 15.0 | 10.0 | 28.7 |
| 1m/RETEST/SHORT | 12292 | 44.7 | 0.027 | 1.05 | 5801 | 19.0 | 12.0 | 29.3 |
| 29m/INV/SHORT | 1 | 100.0 | 0.14 | 99.0 | 0 | 57.0 | 287.0 | None |
| 29m/RETEST/LONG | 172 | 55.2 | 0.227 | 1.51 | 77 | 100.0 | 133.5 | 54.5 |
| 29m/RETEST/SHORT | 241 | 54.8 | 0.17 | 1.38 | 107 | 153.0 | 265.25 | 71.0 |
| 2m/INV/LONG | 168 | 53.0 | 0.043 | 1.1 | 67 | 17.0 | 14.0 | 14.9 |
| 2m/INV/SHORT | 130 | 46.9 | 0.065 | 1.15 | 54 | 28.0 | 14.0 | 29.6 |
| 2m/RETEST/LONG | 7595 | 47.3 | 0.028 | 1.06 | 3607 | 19.0 | 12.0 | 38.4 |
| 2m/RETEST/SHORT | 5341 | 47.4 | 0.05 | 1.1 | 2508 | 25.0 | 15.0 | 38.4 |
| 3m/INV/LONG | 11 | 54.5 | -0.124 | 0.73 | 5 | 22.0 | 26.25 | 20.0 |
| 3m/INV/SHORT | 8 | 100.0 | 0.455 | 99.0 | 0 | 30.5 | 13.0 | None |
| 3m/RETEST/LONG | 1249 | 53.1 | 0.087 | 1.19 | 571 | 23.0 | 16.0 | 51.7 |
| 3m/RETEST/SHORT | 1140 | 55.9 | 0.146 | 1.34 | 486 | 23.0 | 18.0 | 53.9 |
| 5m/INV/LONG | 57 | 66.7 | 0.096 | 1.35 | 15 | 31.0 | 31.25 | 53.3 |
| 5m/INV/SHORT | 38 | 52.6 | 0.221 | 1.57 | 14 | 56.5 | 39.5 | 28.6 |
| 5m/RETEST/LONG | 3313 | 51.5 | 0.1 | 1.22 | 1442 | 39.0 | 33.0 | 48.8 |
| 5m/RETEST/SHORT | 2429 | 48.9 | 0.069 | 1.15 | 1091 | 42.0 | 33.0 | 44.6 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 3543 | 22.7 | 0.023 | 1.03 | 2321 | 28.0 | 13.25 | 17.8 |
| B | 22935 | 47.2 | 0.033 | 1.07 | 10670 | 18.0 | 12.0 | 35.5 |
| C | 26681 | 49.6 | 0.054 | 1.12 | 11916 | 20.0 | 15.0 | 37.2 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 19251 | 48.8 | 0.073 | 1.16 | 8731 | 15.0 | 10.0 | 36.3 |
| London | 8041 | 46.2 | 0.014 | 1.03 | 4003 | 19.0 | 13.0 | 37.5 |
| NY | 9478 | 45.0 | 0.024 | 1.05 | 4578 | 28.0 | 20.0 | 37.1 |
| Sin KZ | 16389 | 45.8 | 0.033 | 1.07 | 7595 | 22.0 | 15.0 | 29.9 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 14540 | 45.1 | 0.034 | 1.07 | 6937 | 24.0 | 16.0 | 33.3 |
| edge=0 | 20425 | 49.0 | 0.055 | 1.12 | 9272 | 18.0 | 12.0 | 37.3 |
| edge=1 | 18194 | 45.6 | 0.038 | 1.08 | 8698 | 19.0 | 14.0 | 33.0 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 3540 | 53.9 | 0.096 | 1.21 | 1599 | 26.0 | 30.0 | 59.2 |
| aligned=1 | 49619 | 46.3 | 0.039 | 1.08 | 23308 | 19.0 | 13.0 | 33.0 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 28 | 50.0 | -0.042 | 0.92 | 14 | 20.0 | 18.0 | 14.3 |
| INV/LONG|edge=0 | 264 | 58.7 | 0.186 | 1.52 | 90 | 17.0 | 11.5 | 30.0 |
| INV/LONG|edge=1 | 410 | 44.6 | 0.045 | 1.1 | 180 | 16.0 | 14.0 | 14.4 |
| INV/SHORT|edge=-1 | 312 | 43.6 | 0.084 | 1.19 | 133 | 26.0 | 12.25 | 17.3 |
| INV/SHORT|edge=0 | 197 | 52.3 | 0.136 | 1.36 | 68 | 20.0 | 18.5 | 27.9 |
| INV/SHORT|edge=1 | 22 | 68.2 | 0.303 | 1.95 | 7 | 30.0 | 50.0 | 14.3 |
| RETEST/LONG|edge=-1 | 3131 | 51.3 | 0.082 | 1.17 | 1456 | 22.0 | 19.0 | 50.2 |
| RETEST/LONG|edge=0 | 11942 | 49.1 | 0.044 | 1.09 | 5480 | 16.0 | 11.0 | 37.3 |
| RETEST/LONG|edge=1 | 14979 | 44.0 | 0.024 | 1.05 | 7287 | 19.0 | 13.0 | 29.4 |
| RETEST/SHORT|edge=-1 | 11069 | 43.3 | 0.019 | 1.04 | 5334 | 24.0 | 16.0 | 29.1 |
| RETEST/SHORT|edge=0 | 8022 | 48.6 | 0.065 | 1.14 | 3634 | 21.0 | 13.0 | 37.7 |
| RETEST/SHORT|edge=1 | 2783 | 54.4 | 0.108 | 1.24 | 1224 | 24.0 | 24.0 | 57.0 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 254 | 41.7 | 0.035 | 1.07 | 119 | 17.0 | 13.75 | 10.9 |
| INV/LONG|tier=C | 448 | 54.9 | 0.129 | 1.33 | 165 | 17.0 | 12.75 | 25.5 |
| INV/SHORT|tier=B | 166 | 45.2 | 0.036 | 1.08 | 73 | 25.0 | 12.0 | 9.6 |
| INV/SHORT|tier=C | 365 | 49.0 | 0.148 | 1.37 | 135 | 24.5 | 21.0 | 26.7 |
| RETEST/LONG|tier=A+ | 2191 | 22.1 | 0.007 | 1.01 | 1462 | 23.0 | 11.0 | 15.6 |
| RETEST/LONG|tier=B | 12972 | 47.6 | 0.042 | 1.09 | 6043 | 17.0 | 12.0 | 36.9 |
| RETEST/LONG|tier=C | 14889 | 49.6 | 0.038 | 1.08 | 6718 | 18.0 | 14.0 | 36.6 |
| RETEST/SHORT|tier=A+ | 1352 | 23.7 | 0.049 | 1.07 | 859 | 39.0 | 16.0 | 21.5 |
| RETEST/SHORT|tier=B | 9543 | 46.9 | 0.021 | 1.04 | 4435 | 20.0 | 14.0 | 34.7 |
| RETEST/SHORT|tier=C | 10979 | 49.3 | 0.07 | 1.15 | 4898 | 24.0 | 17.0 | 38.8 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=0 | 11 | 63.6 | 0.003 | 1.01 | 4 | 25.0 | 40.5 | 0.0 |
| INV/LONG|aligned=1 | 691 | 49.9 | 0.096 | 1.23 | 280 | 16.0 | 13.0 | 19.6 |
| INV/SHORT|aligned=0 | 10 | 70.0 | 0.03 | 1.1 | 3 | 38.5 | 119.0 | 33.3 |
| INV/SHORT|aligned=1 | 521 | 47.4 | 0.114 | 1.27 | 205 | 24.5 | 14.0 | 20.5 |
| RETEST/LONG|aligned=0 | 1590 | 51.9 | 0.067 | 1.14 | 743 | 27.0 | 29.0 | 57.7 |
| RETEST/LONG|aligned=1 | 28462 | 46.5 | 0.036 | 1.07 | 13480 | 17.0 | 12.0 | 33.3 |
| RETEST/SHORT|aligned=0 | 1929 | 55.4 | 0.121 | 1.27 | 849 | 26.0 | 30.0 | 60.8 |
| RETEST/SHORT|aligned=1 | 19945 | 45.8 | 0.04 | 1.08 | 9343 | 22.0 | 15.0 | 33.3 |

## Autopsia de SL
n_losses=24907  causas: RR-bajo×9630, contra-estructura×8797, stop-en-el-minimo×8640, killzone-Asia-largo×5247, estirado×4285, sin-nivel-detras×3959, chop×3661, SL-muy-pegado×3077, sin-causa-clara×2599, contra-sesgo×1599
- INV/LONG (n=284): killzone-Asia-largo×132, RR-bajo×109, contra-estructura×88, estirado×56, stop-en-el-minimo×55, chop×34, sin-nivel-detras×33, SL-muy-pegado×31, sin-causa-clara×19, contra-sesgo×4
- INV/SHORT (n=208): RR-bajo×86, contra-estructura×60, stop-en-el-minimo×43, estirado×42, SL-muy-pegado×35, sin-causa-clara×34, chop×29, sin-nivel-detras×17, contra-sesgo×3
- RETEST/LONG (n=14223): RR-bajo×5531, contra-estructura×5178, killzone-Asia-largo×5115, stop-en-el-minimo×4919, estirado×2477, sin-nivel-detras×2354, chop×2086, SL-muy-pegado×1680, sin-causa-clara×1197, contra-sesgo×743
- RETEST/SHORT (n=10192): RR-bajo×3904, stop-en-el-minimo×3623, contra-estructura×3471, estirado×1710, sin-nivel-detras×1555, chop×1512, sin-causa-clara×1349, SL-muy-pegado×1331, contra-sesgo×849

## Autopsia de SL · semana 2026-W45 (para revision semanal)
n_losses=1615  causas: stop-en-el-minimo×649, RR-bajo×637, contra-estructura×593, contra-sesgo×307, estirado×302, chop×258, sin-nivel-detras×218, killzone-Asia-largo×202, SL-muy-pegado×177, sin-causa-clara×164
ejemplos por causa: {"stop-en-el-minimo": ["GC-1-28130-S", "GC-2-25059-S", "GC-2-25062-S", "YM-1-22509-S", "YM-1-22546-S"], "RR-bajo": ["GC-1-28130-S", "GC-2-25059-S", "GC-1-29773-S", "YM-1-22532-S", "YM-1-22546-S"], "contra-estructura": ["YM-1-22700-S", "YM-1-22850-S", "YM-1-22851-S", "YM-1-22866-S", "GC-1-29089-L"]}

## Autopsia de SL · tendencia semanal de causas (% de las perdidas de esa semana)
```json
{
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
    "n_losses": 1615,
    "causes_pct": {
      "stop-en-el-minimo": 40.2,
      "RR-bajo": 39.4,
      "contra-estructura": 36.7,
      "contra-sesgo": 19.0,
      "estirado": 18.7,
      "chop": 16.0,
      "sin-nivel-detras": 13.5,
      "killzone-Asia-largo": 12.5,
      "SL-muy-pegado": 11.0,
      "sin-causa-clara": 10.2
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
    "n": 51494,
    "naive_expR": 0.043,
    "managed_expR": 0.114,
    "delta": 0.071,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 45.5,
    "fill_full_pct": 32.1,
    "m1_rate": 37.1,
    "m2_rate": 22.5,
    "m3_rate": 11.6,
    "beAfterM1_rate": 18.4
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
      "n": 400,
      "naive_expR": 0.051,
      "managed_expR": -0.121,
      "delta": -0.172,
      "avgEntryBetterTk_p50": 8.4,
      "fill_t3plus_pct": 37.2,
      "fill_full_pct": 26.8,
      "m1_rate": 34.8,
      "m2_rate": 19.5,
      "m3_rate": 10.0,
      "beAfterM1_rate": 19.0
    },
    "15m/RETEST/SHORT": {
      "n": 428,
      "naive_expR": 0.116,
      "managed_expR": 0.003,
      "delta": -0.114,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 29.4,
      "fill_full_pct": 18.0,
      "m1_rate": 34.6,
      "m2_rate": 20.1,
      "m3_rate": 12.1,
      "beAfterM1_rate": 19.4
    },
    "1m/INV/LONG": {
      "n": 447,
      "naive_expR": 0.12,
      "managed_expR": 0.255,
      "delta": 0.135,
      "avgEntryBetterTk_p50": 2.7,
      "fill_t3plus_pct": 50.8,
      "fill_full_pct": 37.4,
      "m1_rate": 41.4,
      "m2_rate": 24.6,
      "m3_rate": 11.9,
      "beAfterM1_rate": 19.7
    },
    "1m/INV/SHORT": {
      "n": 334,
      "naive_expR": 0.106,
      "managed_expR": 0.285,
      "delta": 0.179,
      "avgEntryBetterTk_p50": 3.1,
      "fill_t3plus_pct": 49.7,
      "fill_full_pct": 37.7,
      "m1_rate": 41.3,
      "m2_rate": 25.4,
      "m3_rate": 12.6,
      "beAfterM1_rate": 17.7
    },
    "1m/RETEST/LONG": {
      "n": 16847,
      "naive_expR": 0.024,
      "managed_expR": 0.119,
      "delta": 0.094,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.6,
      "fill_full_pct": 33.9,
      "m1_rate": 36.8,
      "m2_rate": 22.3,
      "m3_rate": 11.8,
      "beAfterM1_rate": 17.5
    },
    "1m/RETEST/SHORT": {
      "n": 11781,
      "naive_expR": 0.027,
      "managed_expR": 0.152,
      "delta": 0.125,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 48.8,
      "fill_full_pct": 34.5,
      "m1_rate": 38.4,
      "m2_rate": 24.1,
      "m3_rate": 12.4,
      "beAfterM1_rate": 18.0
    },
    "29m/RETEST/LONG": {
      "n": 172,
      "naive_expR": 0.227,
      "managed_expR": -0.037,
      "delta": -0.264,
      "avgEntryBetterTk_p50": 10.649999999999999,
      "fill_t3plus_pct": 40.1,
      "fill_full_pct": 30.2,
      "m1_rate": 36.6,
      "m2_rate": 24.4,
      "m3_rate": 11.6,
      "beAfterM1_rate": 14.5
    },
    "29m/RETEST/SHORT": {
      "n": 240,
      "naive_expR": 0.17,
      "managed_expR": -0.086,
      "delta": -0.256,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 23.3,
      "fill_full_pct": 12.5,
      "m1_rate": 37.5,
      "m2_rate": 19.6,
      "m3_rate": 10.8,
      "beAfterM1_rate": 20.8
    },
    "2m/INV/LONG": {
      "n": 163,
      "naive_expR": 0.043,
      "managed_expR": 0.152,
      "delta": 0.11,
      "avgEntryBetterTk_p50": 4.0,
      "fill_t3plus_pct": 54.6,
      "fill_full_pct": 39.9,
      "m1_rate": 28.8,
      "m2_rate": 19.0,
      "m3_rate": 8.0,
      "beAfterM1_rate": 12.3
    },
    "2m/INV/SHORT": {
      "n": 126,
      "naive_expR": 0.065,
      "managed_expR": 0.223,
      "delta": 0.158,
      "avgEntryBetterTk_p50": 4.2,
      "fill_t3plus_pct": 51.6,
      "fill_full_pct": 40.5,
      "m1_rate": 34.9,
      "m2_rate": 23.8,
      "m3_rate": 13.5,
      "beAfterM1_rate": 12.7
    },
    "2m/RETEST/LONG": {
      "n": 7384,
      "naive_expR": 0.027,
      "managed_expR": 0.084,
      "delta": 0.057,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 44.6,
      "fill_full_pct": 31.6,
      "m1_rate": 35.7,
      "m2_rate": 21.5,
      "m3_rate": 11.2,
      "beAfterM1_rate": 18.3
    },
    "2m/RETEST/SHORT": {
      "n": 5173,
      "naive_expR": 0.05,
      "managed_expR": 0.127,
      "delta": 0.077,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 45.4,
      "fill_full_pct": 32.0,
      "m1_rate": 38.1,
      "m2_rate": 23.0,
      "m3_rate": 12.0,
      "beAfterM1_rate": 19.9
    },
    "3m/INV/LONG": {
      "n": 11,
      "naive_expR": -0.124,
      "managed_expR": -0.035,
      "delta": 0.089,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 36.4,
      "fill_full_pct": 18.2,
      "m1_rate": 27.3,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 27.3
    },
    "3m/INV/SHORT": {
      "n": 8,
      "naive_expR": 0.455,
      "managed_expR": 0.336,
      "delta": -0.119,
      "avgEntryBetterTk_p50": 0.0,
      "fill_t3plus_pct": 25.0,
      "fill_full_pct": 12.5,
      "m1_rate": 25.0,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 25.0
    },
    "3m/RETEST/LONG": {
      "n": 1242,
      "naive_expR": 0.087,
      "managed_expR": -0.001,
      "delta": -0.088,
      "avgEntryBetterTk_p50": 2.8499999999999996,
      "fill_t3plus_pct": 41.7,
      "fill_full_pct": 28.7,
      "m1_rate": 34.1,
      "m2_rate": 17.8,
      "m3_rate": 8.5,
      "beAfterM1_rate": 19.6
    },
    "3m/RETEST/SHORT": {
      "n": 1133,
      "naive_expR": 0.146,
      "managed_expR": 0.102,
      "delta": -0.044,
      "avgEntryBetterTk_p50": 2.5,
      "fill_t3plus_pct": 37.0,
      "fill_full_pct": 26.7,
      "m1_rate": 38.2,
      "m2_rate": 21.0,
      "m3_rate": 10.3,
      "beAfterM1_rate": 21.0
    },
    "5m/INV/LONG": {
      "n": 54,
      "naive_expR": 0.096,
      "managed_expR": 0.09,
      "delta": -0.006,
      "avgEntryBetterTk_p50": 3.65,
      "fill_t3plus_pct": 38.9,
      "fill_full_pct": 31.5,
      "m1_rate": 16.7,
      "m2_rate": 5.6,
      "m3_rate": 1.9,
      "beAfterM1_rate": 13.0
    },
    "5m/INV/SHORT": {
      "n": 36,
      "naive_expR": 0.221,
      "managed_expR": 0.291,
      "delta": 0.07,
      "avgEntryBetterTk_p50": 5.3,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 36.1,
      "m1_rate": 33.3,
      "m2_rate": 22.2,
      "m3_rate": 16.7,
      "beAfterM1_rate": 16.7
    },
    "5m/RETEST/LONG": {
      "n": 3194,
      "naive_expR": 0.1,
      "managed_expR": 0.083,
      "delta": -0.017,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 37.0,
      "fill_full_pct": 26.0,
      "m1_rate": 36.9,
      "m2_rate": 22.2,
      "m3_rate": 10.9,
      "beAfterM1_rate": 20.1
    },
    "5m/RETEST/SHORT": {
      "n": 2315,
      "naive_expR": 0.068,
      "managed_expR": 0.084,
      "delta": 0.016,
      "avgEntryBetterTk_p50": 4.2,
      "fill_t3plus_pct": 38.1,
      "fill_full_pct": 25.4,
      "m1_rate": 36.3,
      "m2_rate": 22.3,
      "m3_rate": 11.3,
      "beAfterM1_rate": 19.3
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 42639,
    "layer_expR": 0.039,
    "orig_expR": 0.177,
    "delta_orig_minus_layer": 0.138,
    "delta_ci90": [
      0.08,
      0.234
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.1,
    "orig_wrTP1": 35.2,
    "slTk_p50": 22.0,
    "slOrigTk_p50": 11.0,
    "orig_wider_pct": 5.0,
    "orig_saved_from_SL": 111,
    "orig_caused_SL": 5616
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 3923,
  "invalid_by_seg": {
    "2m/RETEST/LONG": 512,
    "1m/RETEST/SHORT": 817,
    "2m/RETEST/SHORT": 260,
    "1m/RETEST/LONG": 1787,
    "1m/INV/SHORT": 54,
    "5m/RETEST/LONG": 112,
    "1m/INV/LONG": 85,
    "2m/INV/LONG": 23,
    "5m/INV/LONG": 4,
    "2m/INV/SHORT": 9,
    "5m/RETEST/SHORT": 77,
    "5m/INV/SHORT": 3,
    "3m/RETEST/LONG": 88,
    "3m/RETEST/SHORT": 66,
    "15m/RETEST/LONG": 6,
    "29m/RETEST/SHORT": 4,
    "15m/RETEST/SHORT": 14,
    "29m/RETEST/LONG": 2
  },
  "by_basis": {
    "candle1": {
      "n": 995,
      "layer_expR": 0.106,
      "orig_expR": 2.128,
      "delta_orig_minus_layer": 2.022,
      "delta_ci90": [
        -0.073,
        6.075
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 52.0,
      "orig_wrTP1": 28.8,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 3.6,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 232
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
      "n": 32083,
      "layer_expR": 0.043,
      "orig_expR": 0.151,
      "delta_orig_minus_layer": 0.109,
      "delta_ci90": [
        0.091,
        0.127
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.6,
      "orig_wrTP1": 36.0,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 5.8,
      "orig_saved_from_SL": 104,
      "orig_caused_SL": 4151
    },
    "retestBar2": {
      "n": 9561,
      "layer_expR": 0.02,
      "orig_expR": 0.059,
      "delta_orig_minus_layer": 0.04,
      "delta_ci90": [
        0.012,
        0.067
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.9,
      "orig_wrTP1": 33.0,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 5,
      "orig_caused_SL": 1233
    }
  },
  "by_tf_kind_side": {
    "15m/RETEST/LONG": {
      "n": 391,
      "layer_expR": 0.063,
      "orig_expR": 0.769,
      "delta_orig_minus_layer": 0.706,
      "delta_ci90": [
        0.328,
        1.164
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.2,
      "orig_wrTP1": 49.9,
      "slTk_p50": 56.0,
      "slOrigTk_p50": 56.0,
      "orig_wider_pct": 31.5,
      "orig_saved_from_SL": 10,
      "orig_caused_SL": 15
    },
    "15m/RETEST/SHORT": {
      "n": 401,
      "layer_expR": 0.113,
      "orig_expR": 0.362,
      "delta_orig_minus_layer": 0.248,
      "delta_ci90": [
        0.04,
        0.503
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.6,
      "orig_wrTP1": 48.4,
      "slTk_p50": 116.0,
      "slOrigTk_p50": 101.0,
      "orig_wider_pct": 27.9,
      "orig_saved_from_SL": 12,
      "orig_caused_SL": 33
    },
    "1m/INV/LONG": {
      "n": 362,
      "layer_expR": 0.117,
      "orig_expR": 0.114,
      "delta_orig_minus_layer": -0.003,
      "delta_ci90": [
        -0.184,
        0.176
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.2,
      "orig_wrTP1": 26.0,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 84
    },
    "1m/INV/SHORT": {
      "n": 270,
      "layer_expR": 0.109,
      "orig_expR": 0.048,
      "delta_orig_minus_layer": -0.061,
      "delta_ci90": [
        -0.289,
        0.193
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.5,
      "orig_wrTP1": 25.6,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.9,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 63
    },
    "1m/RETEST/LONG": {
      "n": 12841,
      "layer_expR": 0.019,
      "orig_expR": 0.075,
      "delta_orig_minus_layer": 0.056,
      "delta_ci90": [
        0.03,
        0.082
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.4,
      "orig_wrTP1": 30.3,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 1.2,
      "orig_saved_from_SL": 4,
      "orig_caused_SL": 1936
    },
    "1m/RETEST/SHORT": {
      "n": 9684,
      "layer_expR": 0.019,
      "orig_expR": 0.061,
      "delta_orig_minus_layer": 0.041,
      "delta_ci90": [
        0.014,
        0.07
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 45.9,
      "orig_wrTP1": 33.0,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 5,
      "orig_caused_SL": 1249
    },
    "29m/RETEST/LONG": {
      "n": 169,
      "layer_expR": 0.238,
      "orig_expR": 0.753,
      "delta_orig_minus_layer": 0.515,
      "delta_ci90": [
        -0.019,
        1.258
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 55.6,
      "orig_wrTP1": 58.6,
      "slTk_p50": 51.0,
      "slOrigTk_p50": 69.0,
      "orig_wider_pct": 52.7,
      "orig_saved_from_SL": 10,
      "orig_caused_SL": 5
    },
    "29m/RETEST/SHORT": {
      "n": 235,
      "layer_expR": 0.195,
      "orig_expR": 0.305,
      "delta_orig_minus_layer": 0.11,
      "delta_ci90": [
        -0.042,
        0.296
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 56.2,
      "orig_wrTP1": 55.7,
      "slTk_p50": 119.0,
      "slOrigTk_p50": 145.0,
      "orig_wider_pct": 43.4,
      "orig_saved_from_SL": 9,
      "orig_caused_SL": 10
    },
    "2m/INV/LONG": {
      "n": 140,
      "layer_expR": 0.07,
      "orig_expR": 0.381,
      "delta_orig_minus_layer": 0.311,
      "delta_ci90": [
        -0.173,
        0.896
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 56.4,
      "orig_wrTP1": 29.3,
      "slTk_p50": 27.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 3.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 38
    },
    "2m/INV/SHORT": {
      "n": 116,
      "layer_expR": 0.034,
      "orig_expR": -0.031,
      "delta_orig_minus_layer": -0.065,
      "delta_ci90": [
        -0.3,
        0.205
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 48.3,
      "orig_wrTP1": 31.0,
      "slTk_p50": 29.5,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 5.2,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 21
    },
    "2m/RETEST/LONG": {
      "n": 6284,
      "layer_expR": 0.025,
      "orig_expR": 0.105,
      "delta_orig_minus_layer": 0.08,
      "delta_ci90": [
        0.048,
        0.112
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.0,
      "orig_wrTP1": 36.5,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 10.0,
      "orig_wider_pct": 3.9,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 788
    },
    "2m/RETEST/SHORT": {
      "n": 4487,
      "layer_expR": 0.052,
      "orig_expR": 0.136,
      "delta_orig_minus_layer": 0.084,
      "delta_ci90": [
        0.045,
        0.125
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.2,
      "orig_wrTP1": 36.2,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 3.6,
      "orig_saved_from_SL": 6,
      "orig_caused_SL": 590
    },
    "3m/INV/LONG": {
      "n": 11,
      "layer_expR": -0.124,
      "orig_expR": 0.242,
      "delta_orig_minus_layer": 0.365,
      "delta_ci90": [
        -0.227,
        0.975
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 54.5,
      "orig_wrTP1": 36.4,
      "slTk_p50": 36.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 2
    },
    "3m/INV/SHORT": {
      "n": 8,
      "layer_expR": 0.455,
      "orig_expR": 0.95,
      "delta_orig_minus_layer": 0.495,
      "delta_ci90": [
        -0.459,
        1.449
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 100.0,
      "orig_wrTP1": 62.5,
      "slTk_p50": 52.5,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 0.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 3
    },
    "3m/RETEST/LONG": {
      "n": 1081,
      "layer_expR": 0.073,
      "orig_expR": 0.357,
      "delta_orig_minus_layer": 0.284,
      "delta_ci90": [
        0.186,
        0.382
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.3,
      "orig_wrTP1": 40.3,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 12.0,
      "orig_wider_pct": 5.2,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 143
    },
    "3m/RETEST/SHORT": {
      "n": 1006,
      "layer_expR": 0.148,
      "orig_expR": 0.194,
      "delta_orig_minus_layer": 0.046,
      "delta_ci90": [
        -0.042,
        0.13
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 56.6,
      "orig_wrTP1": 39.1,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 177
    },
    "5m/INV/LONG": {
      "n": 50,
      "layer_expR": 0.12,
      "orig_expR": 0.098,
      "delta_orig_minus_layer": -0.022,
      "delta_ci90": [
        -0.358,
        0.327
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 72.0,
      "orig_wrTP1": 50.0,
      "slTk_p50": 37.5,
      "slOrigTk_p50": 13.0,
      "orig_wider_pct": 8.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 11
    },
    "5m/INV/SHORT": {
      "n": 32,
      "layer_expR": 0.326,
      "orig_expR": 62.451,
      "delta_orig_minus_layer": 62.125,
      "delta_ci90": [
        -0.663,
        187.069
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 59.4,
      "orig_wrTP1": 34.4,
      "slTk_p50": 57.5,
      "slOrigTk_p50": 14.0,
      "orig_wider_pct": 15.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 8
    },
    "5m/RETEST/LONG": {
      "n": 2932,
      "layer_expR": 0.082,
      "orig_expR": 0.28,
      "delta_orig_minus_layer": 0.198,
      "delta_ci90": [
        0.131,
        0.271
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.3,
      "orig_wrTP1": 45.8,
      "slTk_p50": 37.0,
      "slOrigTk_p50": 25.0,
      "orig_wider_pct": 14.9,
      "orig_saved_from_SL": 27,
      "orig_caused_SL": 246
    },
    "5m/RETEST/SHORT": {
      "n": 2133,
      "layer_expR": 0.05,
      "orig_expR": 0.255,
      "delta_orig_minus_layer": 0.205,
      "delta_ci90": [
        0.1,
        0.32
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.8,
      "orig_wrTP1": 42.6,
      "slTk_p50": 39.0,
      "slOrigTk_p50": 29.0,
      "orig_wider_pct": 16.6,
      "orig_saved_from_SL": 16,
      "orig_caused_SL": 192
    }
  },
  "since_change": {
    "changeDate": "2026-09-26",
    "n": 28320,
    "by_tf_kind_side": {
      "15m/RETEST/LONG": {
        "n": 391,
        "layer_expR": 0.063,
        "orig_expR": 0.769,
        "delta_orig_minus_layer": 0.706,
        "delta_ci90": [
          0.328,
          1.164
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 51.2,
        "orig_wrTP1": 49.9,
        "slTk_p50": 56.0,
        "slOrigTk_p50": 56.0,
        "orig_wider_pct": 31.5,
        "orig_saved_from_SL": 10,
        "orig_caused_SL": 15
      },
      "15m/RETEST/SHORT": {
        "n": 401,
        "layer_expR": 0.113,
        "orig_expR": 0.362,
        "delta_orig_minus_layer": 0.248,
        "delta_ci90": [
          0.04,
          0.503
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 53.6,
        "orig_wrTP1": 48.4,
        "slTk_p50": 116.0,
        "slOrigTk_p50": 101.0,
        "orig_wider_pct": 27.9,
        "orig_saved_from_SL": 12,
        "orig_caused_SL": 33
      },
      "1m/INV/LONG": {
        "n": 230,
        "layer_expR": 0.096,
        "orig_expR": 0.198,
        "delta_orig_minus_layer": 0.101,
        "delta_ci90": [
          -0.102,
          0.321
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 50.9,
        "orig_wrTP1": 27.8,
        "slTk_p50": 18.0,
        "slOrigTk_p50": 5.0,
        "orig_wider_pct": 0.9,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 53
      },
      "1m/INV/SHORT": {
        "n": 166,
        "layer_expR": 0.156,
        "orig_expR": 0.099,
        "delta_orig_minus_layer": -0.058,
        "delta_ci90": [
          -0.368,
          0.277
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 47.6,
        "orig_wrTP1": 25.3,
        "slTk_p50": 25.5,
        "slOrigTk_p50": 6.0,
        "orig_wider_pct": 1.2,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 38
      },
      "1m/RETEST/LONG": {
        "n": 7660,
        "layer_expR": -0.006,
        "orig_expR": 0.024,
        "delta_orig_minus_layer": 0.03,
        "delta_ci90": [
          -0.002,
          0.061
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 44.7,
        "orig_wrTP1": 29.6,
        "slTk_p50": 17.0,
        "slOrigTk_p50": 7.0,
        "orig_wider_pct": 1.3,
        "orig_saved_from_SL": 2,
        "orig_caused_SL": 1159
      },
      "1m/RETEST/SHORT": {
        "n": 6424,
        "layer_expR": 0.015,
        "orig_expR": 0.056,
        "delta_orig_minus_layer": 0.041,
        "delta_ci90": [
          0.007,
          0.075
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 45.8,
        "orig_wrTP1": 32.8,
        "slTk_p50": 21.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 2.2,
        "orig_saved_from_SL": 4,
        "orig_caused_SL": 842
      },
      "29m/RETEST/LONG": {
        "n": 169,
        "layer_expR": 0.238,
        "orig_expR": 0.753,
        "delta_orig_minus_layer": 0.515,
        "delta_ci90": [
          -0.019,
          1.258
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 55.6,
        "orig_wrTP1": 58.6,
        "slTk_p50": 51.0,
        "slOrigTk_p50": 69.0,
        "orig_wider_pct": 52.7,
        "orig_saved_from_SL": 10,
        "orig_caused_SL": 5
      },
      "29m/RETEST/SHORT": {
        "n": 235,
        "layer_expR": 0.195,
        "orig_expR": 0.305,
        "delta_orig_minus_layer": 0.11,
        "delta_ci90": [
          -0.042,
          0.296
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 56.2,
        "orig_wrTP1": 55.7,
        "slTk_p50": 119.0,
        "slOrigTk_p50": 145.0,
        "orig_wider_pct": 43.4,
        "orig_saved_from_SL": 9,
        "orig_caused_SL": 10
      },
      "2m/INV/LONG": {
        "n": 89,
        "layer_expR": 0.127,
        "orig_expR": 0.255,
        "delta_orig_minus_layer": 0.128,
        "delta_ci90": [
          -0.377,
          0.789
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 59.6,
        "orig_wrTP1": 30.3,
        "slTk_p50": 28.0,
        "slOrigTk_p50": 9.0,
        "orig_wider_pct": 1.1,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 26
      },
      "2m/INV/SHORT": {
        "n": 66,
        "layer_expR": -0.082,
        "orig_expR": -0.302,
        "delta_orig_minus_layer": -0.219,
        "delta_ci90": [
          -0.459,
          0.025
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 51.5,
        "orig_wrTP1": 28.8,
        "slTk_p50": 34.5,
        "slOrigTk_p50": 8.0,
        "orig_wider_pct": 6.1,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 15
      },
      "2m/RETEST/LONG": {
        "n": 3793,
        "layer_expR": 0.012,
        "orig_expR": 0.073,
        "delta_orig_minus_layer": 0.061,
        "delta_ci90": [
          0.023,
          0.101
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 48.7,
        "orig_wrTP1": 36.0,
        "slTk_p50": 20.0,
        "slOrigTk_p50": 10.0,
        "orig_wider_pct": 4.2,
        "orig_saved_from_SL": 3,
        "orig_caused_SL": 484
      },
      "2m/RETEST/SHORT": {
        "n": 2964,
        "layer_expR": 0.042,
        "orig_expR": 0.109,
        "delta_orig_minus_layer": 0.068,
        "delta_ci90": [
          0.02,
          0.114
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 48.4,
        "orig_wrTP1": 35.2,
        "slTk_p50": 26.0,
        "slOrigTk_p50": 13.0,
        "orig_wider_pct": 3.3,
        "orig_saved_from_SL": 4,
        "orig_caused_SL": 396
      },
      "3m/INV/LONG": {
        "n": 11,
        "layer_expR": -0.124,
        "orig_expR": 0.242,
        "delta_orig_minus_layer": 0.365,
        "delta_ci90": [
          -0.227,
          0.975
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 54.5,
        "orig_wrTP1": 36.4,
        "slTk_p50": 36.0,
        "slOrigTk_p50": 7.0,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 2
      },
      "3m/INV/SHORT": {
        "n": 8,
        "layer_expR": 0.455,
        "orig_expR": 0.95,
        "delta_orig_minus_layer": 0.495,
        "delta_ci90": [
          -0.459,
          1.449
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 100.0,
        "orig_wrTP1": 62.5,
        "slTk_p50": 52.5,
        "slOrigTk_p50": 8.0,
        "orig_wider_pct": 0.0,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 3
      },
      "3m/RETEST/LONG": {
        "n": 1081,
        "layer_expR": 0.073,
        "orig_expR": 0.357,
        "delta_orig_minus_layer": 0.284,
        "delta_ci90": [
          0.186,
          0.382
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 53.3,
        "orig_wrTP1": 40.3,
        "slTk_p50": 23.0,
        "slOrigTk_p50": 12.0,
        "orig_wider_pct": 5.2,
        "orig_saved_from_SL": 3,
        "orig_caused_SL": 143
      },
      "3m/RETEST/SHORT": {
        "n": 1006,
        "layer_expR": 0.148,
        "orig_expR": 0.194,
        "delta_orig_minus_layer": 0.046,
        "delta_ci90": [
          -0.042,
          0.13
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 56.6,
        "orig_wrTP1": 39.1,
        "slTk_p50": 22.0,
        "slOrigTk_p50": 11.0,
        "orig_wider_pct": 3.0,
        "orig_saved_from_SL": 1,
        "orig_caused_SL": 177
      },
      "5m/INV/LONG": {
        "n": 32,
        "layer_expR": -0.058,
        "orig_expR": 0.373,
        "delta_orig_minus_layer": 0.431,
        "delta_ci90": [
          0.049,
          0.858
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 68.8,
        "orig_wrTP1": 56.2,
        "slTk_p50": 37.5,
        "slOrigTk_p50": 13.0,
        "orig_wider_pct": 3.1,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 4
      },
      "5m/INV/SHORT": {
        "n": 22,
        "layer_expR": 0.302,
        "orig_expR": 91.036,
        "delta_orig_minus_layer": 90.734,
        "delta_ci90": [
          -0.537,
          272.488
        ],
        "delta_beats_zero": false,
        "delta_below_zero": false,
        "layer_wrTP1": 54.5,
        "orig_wrTP1": 31.8,
        "slTk_p50": 68.5,
        "slOrigTk_p50": 11.5,
        "orig_wider_pct": 9.1,
        "orig_saved_from_SL": 0,
        "orig_caused_SL": 5
      },
      "5m/RETEST/LONG": {
        "n": 2009,
        "layer_expR": 0.065,
        "orig_expR": 0.282,
        "delta_orig_minus_layer": 0.218,
        "delta_ci90": [
          0.134,
          0.316
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 52.9,
        "orig_wrTP1": 46.0,
        "slTk_p50": 39.0,
        "slOrigTk_p50": 28.0,
        "orig_wider_pct": 14.0,
        "orig_saved_from_SL": 20,
        "orig_caused_SL": 157
      },
      "5m/RETEST/SHORT": {
        "n": 1557,
        "layer_expR": 0.051,
        "orig_expR": 0.281,
        "delta_orig_minus_layer": 0.231,
        "delta_ci90": [
          0.104,
          0.368
        ],
        "delta_beats_zero": true,
        "delta_below_zero": false,
        "layer_wrTP1": 51.0,
        "orig_wrTP1": 42.3,
        "slTk_p50": 45.0,
        "slOrigTk_p50": 32.0,
        "orig_wider_pct": 14.5,
        "orig_saved_from_SL": 9,
        "orig_caused_SL": 145
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
      "n": 16762,
      "wrTP1": 46.5,
      "nSL": 7955,
      "nTO": 1015,
      "expR": 0.022,
      "pf": 1.04,
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
        "expR": 0.022,
        "ci90": [
          0.007,
          0.036
        ],
        "p_mean_le_0": 0.006,
        "n": 16298
      }
    },
    "cuts": {
      "1.0": {
        "n": 8020,
        "wrTP1": 30.4,
        "nSL": 4843,
        "nTO": 741,
        "expR": 0.014,
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
          "expR": 0.014,
          "ci90": [
            -0.014,
            0.04
          ],
          "p_mean_le_0": 0.209,
          "n": 7762
        }
      },
      "1.2": {
        "n": 6593,
        "wrTP1": 27.5,
        "nSL": 4101,
        "nTO": 679,
        "expR": 0.022,
        "pf": 1.03,
        "mfe_p25": 8.0,
        "mfe_p50": 19.5,
        "mfe_p75": 42.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 18.7,
        "ci90": {
          "expR": 0.022,
          "ci90": [
            -0.01,
            0.052
          ],
          "p_mean_le_0": 0.127,
          "n": 6374
        }
      },
      "1.3": {
        "n": 6008,
        "wrTP1": 26.0,
        "nSL": 3791,
        "nTO": 653,
        "expR": 0.021,
        "pf": 1.03,
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
          "expR": 0.021,
          "ci90": [
            -0.013,
            0.055
          ],
          "p_mean_le_0": 0.159,
          "n": 5800
        }
      },
      "1.5": {
        "n": 5089,
        "wrTP1": 23.2,
        "nSL": 3306,
        "nTO": 601,
        "expR": 0.009,
        "pf": 1.01,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 18.90000000000009,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 15.5,
        "ci90": {
          "expR": 0.009,
          "ci90": [
            -0.029,
            0.048
          ],
          "p_mean_le_0": 0.342,
          "n": 4914
        }
      },
      "2.0": {
        "n": 3338,
        "wrTP1": 17.2,
        "nSL": 2274,
        "nTO": 489,
        "expR": -0.008,
        "pf": 0.99,
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
          "expR": -0.008,
          "ci90": [
            -0.058,
            0.04
          ],
          "p_mean_le_0": 0.619,
          "n": 3218
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 11759,
      "wrTP1": 46.7,
      "nSL": 5447,
      "nTO": 818,
      "expR": 0.029,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 38.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 31.2,
      "ci90": {
        "expR": 0.029,
        "ci90": [
          0.012,
          0.046
        ],
        "p_mean_le_0": 0.003,
        "n": 11276
      }
    },
    "cuts": {
      "1.0": {
        "n": 5613,
        "wrTP1": 31.0,
        "nSL": 3282,
        "nTO": 591,
        "expR": 0.024,
        "pf": 1.04,
        "mfe_p25": 11.0,
        "mfe_p50": 26.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 22.3,
        "ci90": {
          "expR": 0.024,
          "ci90": [
            -0.008,
            0.055
          ],
          "p_mean_le_0": 0.11,
          "n": 5319
        }
      },
      "1.2": {
        "n": 4570,
        "wrTP1": 27.5,
        "nSL": 2777,
        "nTO": 538,
        "expR": 0.019,
        "pf": 1.03,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 13.5,
        "winnerMAE_p90": 24.600000000000136,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 19.6,
        "ci90": {
          "expR": 0.019,
          "ci90": [
            -0.018,
            0.057
          ],
          "p_mean_le_0": 0.202,
          "n": 4314
        }
      },
      "1.3": {
        "n": 4189,
        "wrTP1": 25.9,
        "nSL": 2581,
        "nTO": 521,
        "expR": 0.015,
        "pf": 1.02,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.4,
        "ci90": {
          "expR": 0.015,
          "ci90": [
            -0.026,
            0.056
          ],
          "p_mean_le_0": 0.268,
          "n": 3947
        }
      },
      "1.5": {
        "n": 3526,
        "wrTP1": 23.2,
        "nSL": 2228,
        "nTO": 479,
        "expR": 0.008,
        "pf": 1.01,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 16.4,
        "ci90": {
          "expR": 0.008,
          "ci90": [
            -0.038,
            0.053
          ],
          "p_mean_le_0": 0.384,
          "n": 3315
        }
      },
      "2.0": {
        "n": 2396,
        "wrTP1": 18.0,
        "nSL": 1585,
        "nTO": 380,
        "expR": -0.009,
        "pf": 0.99,
        "mfe_p25": 12.0,
        "mfe_p50": 29.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 11.6,
        "ci90": {
          "expR": -0.009,
          "ci90": [
            -0.067,
            0.052
          ],
          "p_mean_le_0": 0.596,
          "n": 2248
        }
      }
    }
  },
  "15/RETEST/LONG": {
    "baseline": {
      "n": 388,
      "wrTP1": 52.1,
      "nSL": 183,
      "nTO": 3,
      "expR": 0.087,
      "pf": 1.18,
      "mfe_p25": 31.0,
      "mfe_p50": 70.0,
      "mfe_p75": 334.0,
      "winnerMAE_p75": 109.0,
      "winnerMAE_p90": 2366.900000000002,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -79.5,
      "revAfterSL_rate": 55.7,
      "ci90": {
        "expR": 0.087,
        "ci90": [
          -0.013,
          0.188
        ],
        "p_mean_le_0": 0.08,
        "n": 385
      }
    },
    "cuts": {
      "1.0": {
        "n": 146,
        "wrTP1": 34.2,
        "nSL": 95,
        "nTO": 1,
        "expR": 0.057,
        "pf": 1.09,
        "mfe_p25": 38.0,
        "mfe_p50": 70.0,
        "mfe_p75": 291.0,
        "winnerMAE_p75": 83.5,
        "winnerMAE_p90": 2545.7000000000007,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -66.0,
        "revAfterSL_rate": 54.7,
        "ci90": {
          "expR": 0.057,
          "ci90": [
            -0.144,
            0.274
          ],
          "p_mean_le_0": 0.336,
          "n": 145
        }
      },
      "1.2": {
        "n": 113,
        "wrTP1": 30.1,
        "nSL": 79,
        "nTO": 0,
        "expR": 0.011,
        "pf": 1.02,
        "mfe_p25": 42.0,
        "mfe_p50": 75.0,
        "mfe_p75": 257.0,
        "winnerMAE_p75": 79.25,
        "winnerMAE_p90": 2681.8999999999996,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -61.0,
        "revAfterSL_rate": 55.7,
        "ci90": {
          "expR": 0.011,
          "ci90": [
            -0.232,
            0.28
          ],
          "p_mean_le_0": 0.486,
          "n": 113
        }
      },
      "1.3": {
        "n": 106,
        "wrTP1": 29.2,
        "nSL": 75,
        "nTO": 0,
        "expR": -0.008,
        "pf": 0.99,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 270.5,
        "winnerMAE_p75": 99.5,
        "winnerMAE_p90": 2750.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -69.0,
        "revAfterSL_rate": 56.0,
        "ci90": {
          "expR": -0.008,
          "ci90": [
            -0.26,
            0.257
          ],
          "p_mean_le_0": 0.511,
          "n": 106
        }
      },
      "1.5": {
        "n": 79,
        "wrTP1": 29.1,
        "nSL": 56,
        "nTO": 0,
        "expR": 0.055,
        "pf": 1.08,
        "mfe_p25": 43.5,
        "mfe_p50": 76.0,
        "mfe_p75": 266.0,
        "winnerMAE_p75": 99.5,
        "winnerMAE_p90": 2704.6,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -56.0,
        "revAfterSL_rate": 51.8,
        "ci90": {
          "expR": 0.055,
          "ci90": [
            -0.251,
            0.374
          ],
          "p_mean_le_0": 0.394,
          "n": 79
        }
      },
      "2.0": {
        "n": 46,
        "wrTP1": 21.7,
        "nSL": 36,
        "nTO": 0,
        "expR": -0.098,
        "pf": 0.88,
        "mfe_p25": 44.25,
        "mfe_p50": 82.5,
        "mfe_p75": 8053.25,
        "winnerMAE_p75": 2074.5,
        "winnerMAE_p90": 11698.799999999996,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -57.5,
        "revAfterSL_rate": 38.9,
        "ci90": {
          "expR": -0.098,
          "ci90": [
            -0.513,
            0.337
          ],
          "p_mean_le_0": 0.644,
          "n": 46
        }
      }
    }
  },
  "15/RETEST/SHORT": {
    "baseline": {
      "n": 416,
      "wrTP1": 54.8,
      "nSL": 185,
      "nTO": 3,
      "expR": 0.126,
      "pf": 1.28,
      "mfe_p25": 38.0,
      "mfe_p50": 153.0,
      "mfe_p75": 2509.0,
      "winnerMAE_p75": 556.25,
      "winnerMAE_p90": 5180.400000000002,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -291.5,
      "revAfterSL_rate": 73.0,
      "ci90": {
        "expR": 0.126,
        "ci90": [
          0.025,
          0.226
        ],
        "p_mean_le_0": 0.015,
        "n": 413
      }
    },
    "cuts": {
      "1.0": {
        "n": 133,
        "wrTP1": 41.4,
        "nSL": 78,
        "nTO": 0,
        "expR": 0.303,
        "pf": 1.52,
        "mfe_p25": 54.0,
        "mfe_p50": 180.0,
        "mfe_p75": 2331.0,
        "winnerMAE_p75": 890.0,
        "winnerMAE_p90": 3790.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -230.0,
        "revAfterSL_rate": 65.4,
        "ci90": {
          "expR": 0.303,
          "ci90": [
            0.067,
            0.544
          ],
          "p_mean_le_0": 0.017,
          "n": 133
        }
      },
      "1.2": {
        "n": 109,
        "wrTP1": 41.3,
        "nSL": 64,
        "nTO": 0,
        "expR": 0.356,
        "pf": 1.61,
        "mfe_p25": 53.0,
        "mfe_p50": 155.0,
        "mfe_p75": 2092.0,
        "winnerMAE_p75": 447.0,
        "winnerMAE_p90": 3653.2,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -229.0,
        "revAfterSL_rate": 62.5,
        "ci90": {
          "expR": 0.356,
          "ci90": [
            0.072,
            0.646
          ],
          "p_mean_le_0": 0.02,
          "n": 109
        }
      },
      "1.3": {
        "n": 100,
        "wrTP1": 40.0,
        "nSL": 60,
        "nTO": 0,
        "expR": 0.341,
        "pf": 1.57,
        "mfe_p25": 52.75,
        "mfe_p50": 130.5,
        "mfe_p75": 3088.5,
        "winnerMAE_p75": 668.5,
        "winnerMAE_p90": 3609.7000000000003,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -229.5,
        "revAfterSL_rate": 63.3,
        "ci90": {
          "expR": 0.341,
          "ci90": [
            0.031,
            0.654
          ],
          "p_mean_le_0": 0.035,
          "n": 100
        }
      },
      "1.5": {
        "n": 77,
        "wrTP1": 32.5,
        "nSL": 52,
        "nTO": 0,
        "expR": 0.234,
        "pf": 1.35,
        "mfe_p25": 58.0,
        "mfe_p50": 134.0,
        "mfe_p75": 5361.0,
        "winnerMAE_p75": 447.0,
        "winnerMAE_p90": 2609.4,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -190.0,
        "revAfterSL_rate": 61.5,
        "ci90": {
          "expR": 0.234,
          "ci90": [
            -0.129,
            0.616
          ],
          "p_mean_le_0": 0.162,
          "n": 77
        }
      },
      "2.0": {
        "n": 47,
        "wrTP1": 29.8,
        "nSL": 33,
        "nTO": 0,
        "expR": 0.306,
        "pf": 1.44,
        "mfe_p25": 62.5,
        "mfe_p50": 180.0,
        "mfe_p75": 9065.0,
        "winnerMAE_p75": 1004.75,
        "winnerMAE_p90": 2569.9000000000005,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -360.0,
        "revAfterSL_rate": 54.5,
        "ci90": {
          "expR": 0.306,
          "ci90": [
            -0.207,
            0.843
          ],
          "p_mean_le_0": 0.173,
          "n": 47
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 7375,
      "wrTP1": 48.7,
      "nSL": 3453,
      "nTO": 328,
      "expR": 0.026,
      "pf": 1.05,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 40.1,
      "ci90": {
        "expR": 0.026,
        "ci90": [
          0.004,
          0.05
        ],
        "p_mean_le_0": 0.029,
        "n": 7174
      }
    },
    "cuts": {
      "1.0": {
        "n": 3355,
        "wrTP1": 31.7,
        "nSL": 2057,
        "nTO": 236,
        "expR": 0.009,
        "pf": 1.01,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 33.1,
        "ci90": {
          "expR": 0.009,
          "ci90": [
            -0.033,
            0.052
          ],
          "p_mean_le_0": 0.343,
          "n": 3234
        }
      },
      "1.2": {
        "n": 2742,
        "wrTP1": 28.3,
        "nSL": 1754,
        "nTO": 213,
        "expR": -0.002,
        "pf": 1.0,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 30.8,
        "ci90": {
          "expR": -0.002,
          "ci90": [
            -0.049,
            0.046
          ],
          "p_mean_le_0": 0.527,
          "n": 2638
        }
      },
      "1.3": {
        "n": 2472,
        "wrTP1": 26.9,
        "nSL": 1603,
        "nTO": 203,
        "expR": 0.003,
        "pf": 1.0,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 29.8,
        "ci90": {
          "expR": 0.003,
          "ci90": [
            -0.051,
            0.057
          ],
          "p_mean_le_0": 0.476,
          "n": 2375
        }
      },
      "1.5": {
        "n": 2044,
        "wrTP1": 23.7,
        "nSL": 1367,
        "nTO": 192,
        "expR": -0.011,
        "pf": 0.98,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.600000000000023,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 27.0,
        "ci90": {
          "expR": -0.011,
          "ci90": [
            -0.069,
            0.053
          ],
          "p_mean_le_0": 0.599,
          "n": 1955
        }
      },
      "2.0": {
        "n": 1290,
        "wrTP1": 18.4,
        "nSL": 901,
        "nTO": 152,
        "expR": -0.004,
        "pf": 0.99,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 21.1,
        "ci90": {
          "expR": -0.004,
          "ci90": [
            -0.091,
            0.078
          ],
          "p_mean_le_0": 0.519,
          "n": 1223
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 5096,
      "wrTP1": 49.7,
      "nSL": 2332,
      "nTO": 231,
      "expR": 0.062,
      "pf": 1.13,
      "mfe_p25": 11.0,
      "mfe_p50": 24.0,
      "mfe_p75": 51.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 33.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 41.3,
      "ci90": {
        "expR": 0.062,
        "ci90": [
          0.034,
          0.088
        ],
        "p_mean_le_0": 0.0,
        "n": 4952
      }
    },
    "cuts": {
      "1.0": {
        "n": 2357,
        "wrTP1": 33.1,
        "nSL": 1418,
        "nTO": 159,
        "expR": 0.055,
        "pf": 1.09,
        "mfe_p25": 16.0,
        "mfe_p50": 33.0,
        "mfe_p75": 66.25,
        "winnerMAE_p75": 15.25,
        "winnerMAE_p90": 33.10000000000002,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 33.7,
        "ci90": {
          "expR": 0.055,
          "ci90": [
            0.004,
            0.108
          ],
          "p_mean_le_0": 0.037,
          "n": 2276
        }
      },
      "1.2": {
        "n": 1907,
        "wrTP1": 29.6,
        "nSL": 1197,
        "nTO": 145,
        "expR": 0.051,
        "pf": 1.08,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 33.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 30.9,
        "ci90": {
          "expR": 0.051,
          "ci90": [
            -0.012,
            0.11
          ],
          "p_mean_le_0": 0.096,
          "n": 1838
        }
      },
      "1.3": {
        "n": 1718,
        "wrTP1": 27.9,
        "nSL": 1102,
        "nTO": 137,
        "expR": 0.042,
        "pf": 1.06,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 33.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 29.4,
        "ci90": {
          "expR": 0.042,
          "ci90": [
            -0.024,
            0.109
          ],
          "p_mean_le_0": 0.151,
          "n": 1655
        }
      },
      "1.5": {
        "n": 1423,
        "wrTP1": 25.2,
        "nSL": 944,
        "nTO": 120,
        "expR": 0.039,
        "pf": 1.06,
        "mfe_p25": 17.25,
        "mfe_p50": 38.0,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 33.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 27.2,
        "ci90": {
          "expR": 0.039,
          "ci90": [
            -0.038,
            0.119
          ],
          "p_mean_le_0": 0.207,
          "n": 1374
        }
      },
      "2.0": {
        "n": 920,
        "wrTP1": 20.7,
        "nSL": 636,
        "nTO": 94,
        "expR": 0.062,
        "pf": 1.09,
        "mfe_p25": 18.0,
        "mfe_p50": 40.0,
        "mfe_p75": 79.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 22.0,
        "ci90": {
          "expR": 0.062,
          "ci90": [
            -0.038,
            0.171
          ],
          "p_mean_le_0": 0.158,
          "n": 887
        }
      }
    }
  },
  "29/RETEST/LONG": {
    "baseline": {
      "n": 165,
      "wrTP1": 57.6,
      "nSL": 70,
      "nTO": 0,
      "expR": 0.279,
      "pf": 1.66,
      "mfe_p25": 42.0,
      "mfe_p50": 94.0,
      "mfe_p75": 303.0,
      "winnerMAE_p75": 133.5,
      "winnerMAE_p90": 6753.200000000012,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -76.0,
      "revAfterSL_rate": 60.0,
      "ci90": {
        "expR": 0.279,
        "ci90": [
          0.114,
          0.455
        ],
        "p_mean_le_0": 0.004,
        "n": 165
      }
    },
    "cuts": {
      "1.0": {
        "n": 65,
        "wrTP1": 43.1,
        "nSL": 37,
        "nTO": 0,
        "expR": 0.394,
        "pf": 1.69,
        "mfe_p25": 42.0,
        "mfe_p50": 89.0,
        "mfe_p75": 235.0,
        "winnerMAE_p75": 63.75,
        "winnerMAE_p90": 369.80000000000064,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -44.0,
        "revAfterSL_rate": 62.2,
        "ci90": {
          "expR": 0.394,
          "ci90": [
            0.055,
            0.773
          ],
          "p_mean_le_0": 0.03,
          "n": 65
        }
      },
      "1.2": {
        "n": 52,
        "wrTP1": 38.5,
        "nSL": 32,
        "nTO": 0,
        "expR": 0.364,
        "pf": 1.59,
        "mfe_p25": 46.75,
        "mfe_p50": 89.5,
        "mfe_p75": 238.25,
        "winnerMAE_p75": 35.25,
        "winnerMAE_p90": 182.60000000000122,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -45.0,
        "revAfterSL_rate": 59.4,
        "ci90": {
          "expR": 0.364,
          "ci90": [
            -0.068,
            0.798
          ],
          "p_mean_le_0": 0.085,
          "n": 52
        }
      },
      "1.3": {
        "n": 47,
        "wrTP1": 36.2,
        "nSL": 30,
        "nTO": 0,
        "expR": 0.355,
        "pf": 1.56,
        "mfe_p25": 44.5,
        "mfe_p50": 75.0,
        "mfe_p75": 236.5,
        "winnerMAE_p75": 36.0,
        "winnerMAE_p90": 442.4000000000003,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -46.0,
        "revAfterSL_rate": 56.7,
        "ci90": {
          "expR": 0.355,
          "ci90": [
            -0.116,
            0.857
          ],
          "p_mean_le_0": 0.107,
          "n": 47
        }
      },
      "1.5": {
        "n": 40,
        "wrTP1": 30.0,
        "nSL": 28,
        "nTO": 0,
        "expR": 0.261,
        "pf": 1.37,
        "mfe_p25": 45.25,
        "mfe_p50": 89.5,
        "mfe_p75": 252.75,
        "winnerMAE_p75": 51.0,
        "winnerMAE_p90": 96.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -55.5,
        "revAfterSL_rate": 53.6,
        "ci90": {
          "expR": 0.261,
          "ci90": [
            -0.265,
            0.79
          ],
          "p_mean_le_0": 0.226,
          "n": 40
        }
      },
      "2.0": {
        "n": 26,
        "wrTP1": 34.6,
        "nSL": 17,
        "nTO": 0,
        "expR": 0.599,
        "pf": 1.92,
        "mfe_p25": 56.75,
        "mfe_p50": 96.5,
        "mfe_p75": 282.25,
        "winnerMAE_p75": 35.0,
        "winnerMAE_p90": 719.6000000000006,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -49.5,
        "revAfterSL_rate": 64.7,
        "ci90": {
          "expR": 0.599,
          "ci90": [
            -0.119,
            1.377
          ],
          "p_mean_le_0": 0.086,
          "n": 26
        }
      }
    }
  },
  "29/RETEST/SHORT": {
    "baseline": {
      "n": 233,
      "wrTP1": 56.7,
      "nSL": 100,
      "nTO": 1,
      "expR": 0.168,
      "pf": 1.39,
      "mfe_p25": 44.75,
      "mfe_p50": 147.0,
      "mfe_p75": 1235.25,
      "winnerMAE_p75": 265.25,
      "winnerMAE_p90": 4568.400000000005,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -304.0,
      "revAfterSL_rate": 76.0,
      "ci90": {
        "expR": 0.168,
        "ci90": [
          0.041,
          0.288
        ],
        "p_mean_le_0": 0.012,
        "n": 232
      }
    },
    "cuts": {
      "1.0": {
        "n": 75,
        "wrTP1": 44.0,
        "nSL": 42,
        "nTO": 0,
        "expR": 0.319,
        "pf": 1.57,
        "mfe_p25": 58.0,
        "mfe_p50": 158.0,
        "mfe_p75": 1188.0,
        "winnerMAE_p75": 331.0,
        "winnerMAE_p90": 1062.8000000000004,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -281.0,
        "revAfterSL_rate": 61.9,
        "ci90": {
          "expR": 0.319,
          "ci90": [
            0.025,
            0.64
          ],
          "p_mean_le_0": 0.036,
          "n": 75
        }
      },
      "1.2": {
        "n": 59,
        "wrTP1": 37.3,
        "nSL": 37,
        "nTO": 0,
        "expR": 0.245,
        "pf": 1.39,
        "mfe_p25": 58.0,
        "mfe_p50": 147.0,
        "mfe_p75": 1223.5,
        "winnerMAE_p75": 279.5,
        "winnerMAE_p90": 1110.900000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -286.0,
        "revAfterSL_rate": 59.5,
        "ci90": {
          "expR": 0.245,
          "ci90": [
            -0.108,
            0.622
          ],
          "p_mean_le_0": 0.131,
          "n": 59
        }
      },
      "1.3": {
        "n": 54,
        "wrTP1": 35.2,
        "nSL": 35,
        "nTO": 0,
        "expR": 0.228,
        "pf": 1.35,
        "mfe_p25": 72.75,
        "mfe_p50": 162.5,
        "mfe_p75": 1229.75,
        "winnerMAE_p75": 347.5,
        "winnerMAE_p90": 1426.1999999999991,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -300.0,
        "revAfterSL_rate": 60.0,
        "ci90": {
          "expR": 0.228,
          "ci90": [
            -0.175,
            0.619
          ],
          "p_mean_le_0": 0.182,
          "n": 54
        }
      },
      "1.5": {
        "n": 42,
        "wrTP1": 33.3,
        "nSL": 28,
        "nTO": 0,
        "expR": 0.266,
        "pf": 1.4,
        "mfe_p25": 81.0,
        "mfe_p50": 134.5,
        "mfe_p75": 1157.5,
        "winnerMAE_p75": 190.0,
        "winnerMAE_p90": 369.7000000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -259.5,
        "revAfterSL_rate": 57.1,
        "ci90": {
          "expR": 0.266,
          "ci90": [
            -0.177,
            0.753
          ],
          "p_mean_le_0": 0.176,
          "n": 42
        }
      },
      "2.0": {
        "n": 27,
        "wrTP1": 29.6,
        "nSL": 19,
        "nTO": 0,
        "expR": 0.236,
        "pf": 1.34,
        "mfe_p25": 63.5,
        "mfe_p50": 102.0,
        "mfe_p75": 754.0,
        "winnerMAE_p75": 79.5,
        "winnerMAE_p90": 224.09999999999997,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.5,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -238.0,
        "revAfterSL_rate": 52.6,
        "ci90": {
          "expR": 0.236,
          "ci90": [
            -0.346,
            0.858
          ],
          "p_mean_le_0": 0.261,
          "n": 27
        }
      }
    }
  },
  "3/RETEST/LONG": {
    "baseline": {
      "n": 1237,
      "wrTP1": 53.6,
      "nSL": 562,
      "nTO": 12,
      "expR": 0.093,
      "pf": 1.2,
      "mfe_p25": 11.0,
      "mfe_p50": 23.0,
      "mfe_p75": 51.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 33.80000000000007,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -20.0,
      "revAfterSL_rate": 52.5,
      "ci90": {
        "expR": 0.093,
        "ci90": [
          0.039,
          0.149
        ],
        "p_mean_le_0": 0.003,
        "n": 1230
      }
    },
    "cuts": {
      "1.0": {
        "n": 451,
        "wrTP1": 39.7,
        "nSL": 265,
        "nTO": 7,
        "expR": 0.152,
        "pf": 1.26,
        "mfe_p25": 15.0,
        "mfe_p50": 32.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 36.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -20.0,
        "revAfterSL_rate": 44.5,
        "ci90": {
          "expR": 0.152,
          "ci90": [
            0.035,
            0.272
          ],
          "p_mean_le_0": 0.018,
          "n": 449
        }
      },
      "1.2": {
        "n": 343,
        "wrTP1": 37.3,
        "nSL": 209,
        "nTO": 6,
        "expR": 0.177,
        "pf": 1.29,
        "mfe_p25": 17.0,
        "mfe_p50": 35.0,
        "mfe_p75": 72.5,
        "winnerMAE_p75": 14.25,
        "winnerMAE_p90": 29.699999999999974,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 42.6,
        "ci90": {
          "expR": 0.177,
          "ci90": [
            0.04,
            0.319
          ],
          "p_mean_le_0": 0.015,
          "n": 342
        }
      },
      "1.3": {
        "n": 296,
        "wrTP1": 35.5,
        "nSL": 185,
        "nTO": 6,
        "expR": 0.173,
        "pf": 1.27,
        "mfe_p25": 18.5,
        "mfe_p50": 36.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 38.400000000000034,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -20.0,
        "revAfterSL_rate": 41.6,
        "ci90": {
          "expR": 0.173,
          "ci90": [
            0.012,
            0.328
          ],
          "p_mean_le_0": 0.038,
          "n": 295
        }
      },
      "1.5": {
        "n": 224,
        "wrTP1": 35.3,
        "nSL": 140,
        "nTO": 5,
        "expR": 0.259,
        "pf": 1.41,
        "mfe_p25": 21.75,
        "mfe_p50": 41.0,
        "mfe_p75": 78.5,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 46.000000000000014,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -19.5,
        "revAfterSL_rate": 36.4,
        "ci90": {
          "expR": 0.259,
          "ci90": [
            0.064,
            0.452
          ],
          "p_mean_le_0": 0.013,
          "n": 224
        }
      },
      "2.0": {
        "n": 124,
        "wrTP1": 35.5,
        "nSL": 75,
        "nTO": 5,
        "expR": 0.458,
        "pf": 1.75,
        "mfe_p25": 30.5,
        "mfe_p50": 48.5,
        "mfe_p75": 88.25,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 26.10000000000001,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 33.3,
        "ci90": {
          "expR": 0.458,
          "ci90": [
            0.178,
            0.739
          ],
          "p_mean_le_0": 0.004,
          "n": 124
        }
      }
    }
  },
  "3/RETEST/SHORT": {
    "baseline": {
      "n": 1116,
      "wrTP1": 57.1,
      "nSL": 466,
      "nTO": 13,
      "expR": 0.16,
      "pf": 1.38,
      "mfe_p25": 12.0,
      "mfe_p50": 22.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 18.0,
      "winnerMAE_p90": 39.0,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -24.0,
      "revAfterSL_rate": 56.2,
      "ci90": {
        "expR": 0.16,
        "ci90": [
          0.103,
          0.215
        ],
        "p_mean_le_0": 0.0,
        "n": 1109
      }
    },
    "cuts": {
      "1.0": {
        "n": 417,
        "wrTP1": 43.9,
        "nSL": 223,
        "nTO": 11,
        "expR": 0.25,
        "pf": 1.46,
        "mfe_p25": 15.0,
        "mfe_p50": 29.0,
        "mfe_p75": 60.25,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 32.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 50.2,
        "ci90": {
          "expR": 0.25,
          "ci90": [
            0.128,
            0.367
          ],
          "p_mean_le_0": 0.0,
          "n": 412
        }
      },
      "1.2": {
        "n": 309,
        "wrTP1": 39.2,
        "nSL": 177,
        "nTO": 11,
        "expR": 0.238,
        "pf": 1.41,
        "mfe_p25": 16.75,
        "mfe_p50": 32.0,
        "mfe_p75": 64.25,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 48.0,
        "ci90": {
          "expR": 0.238,
          "ci90": [
            0.087,
            0.386
          ],
          "p_mean_le_0": 0.003,
          "n": 304
        }
      },
      "1.3": {
        "n": 268,
        "wrTP1": 37.3,
        "nSL": 157,
        "nTO": 11,
        "expR": 0.235,
        "pf": 1.39,
        "mfe_p25": 17.0,
        "mfe_p50": 32.0,
        "mfe_p75": 63.5,
        "winnerMAE_p75": 16.75,
        "winnerMAE_p90": 34.30000000000011,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 45.2,
        "ci90": {
          "expR": 0.235,
          "ci90": [
            0.069,
            0.397
          ],
          "p_mean_le_0": 0.009,
          "n": 263
        }
      },
      "1.5": {
        "n": 213,
        "wrTP1": 32.9,
        "nSL": 133,
        "nTO": 10,
        "expR": 0.183,
        "pf": 1.29,
        "mfe_p25": 18.0,
        "mfe_p50": 33.0,
        "mfe_p75": 72.0,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 54.2,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 42.9,
        "ci90": {
          "expR": 0.183,
          "ci90": [
            -0.001,
            0.377
          ],
          "p_mean_le_0": 0.051,
          "n": 209
        }
      },
      "2.0": {
        "n": 101,
        "wrTP1": 30.7,
        "nSL": 65,
        "nTO": 5,
        "expR": 0.293,
        "pf": 1.45,
        "mfe_p25": 19.0,
        "mfe_p50": 33.5,
        "mfe_p75": 73.25,
        "winnerMAE_p75": 14.5,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 23.1,
        "ci90": {
          "expR": 0.293,
          "ci90": [
            -0.016,
            0.615
          ],
          "p_mean_le_0": 0.058,
          "n": 100
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 3192,
      "wrTP1": 53.4,
      "nSL": 1354,
      "nTO": 132,
      "expR": 0.113,
      "pf": 1.26,
      "mfe_p25": 16.0,
      "mfe_p50": 38.0,
      "mfe_p75": 112.75,
      "winnerMAE_p75": 33.0,
      "winnerMAE_p90": 169.5,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -40.0,
      "revAfterSL_rate": 51.9,
      "ci90": {
        "expR": 0.113,
        "ci90": [
          0.078,
          0.146
        ],
        "p_mean_le_0": 0.0,
        "n": 3082
      }
    },
    "cuts": {
      "1.0": {
        "n": 1317,
        "wrTP1": 36.5,
        "nSL": 749,
        "nTO": 87,
        "expR": 0.153,
        "pf": 1.25,
        "mfe_p25": 20.0,
        "mfe_p50": 47.0,
        "mfe_p75": 134.5,
        "winnerMAE_p75": 27.0,
        "winnerMAE_p90": 97.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -35.0,
        "revAfterSL_rate": 46.2,
        "ci90": {
          "expR": 0.153,
          "ci90": [
            0.083,
            0.225
          ],
          "p_mean_le_0": 0.0,
          "n": 1251
        }
      },
      "1.2": {
        "n": 1071,
        "wrTP1": 34.3,
        "nSL": 624,
        "nTO": 80,
        "expR": 0.175,
        "pf": 1.28,
        "mfe_p25": 20.0,
        "mfe_p50": 47.0,
        "mfe_p75": 134.25,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 89.80000000000024,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 43.8,
        "ci90": {
          "expR": 0.175,
          "ci90": [
            0.091,
            0.257
          ],
          "p_mean_le_0": 0.001,
          "n": 1012
        }
      },
      "1.3": {
        "n": 970,
        "wrTP1": 31.8,
        "nSL": 587,
        "nTO": 75,
        "expR": 0.149,
        "pf": 1.23,
        "mfe_p25": 21.0,
        "mfe_p50": 47.0,
        "mfe_p75": 141.25,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 85.60000000000002,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 42.8,
        "ci90": {
          "expR": 0.149,
          "ci90": [
            0.06,
            0.235
          ],
          "p_mean_le_0": 0.003,
          "n": 916
        }
      },
      "1.5": {
        "n": 795,
        "wrTP1": 30.3,
        "nSL": 493,
        "nTO": 61,
        "expR": 0.171,
        "pf": 1.26,
        "mfe_p25": 21.0,
        "mfe_p50": 48.0,
        "mfe_p75": 144.75,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 77.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 42.0,
        "ci90": {
          "expR": 0.171,
          "ci90": [
            0.068,
            0.276
          ],
          "p_mean_le_0": 0.004,
          "n": 754
        }
      },
      "2.0": {
        "n": 498,
        "wrTP1": 24.1,
        "nSL": 332,
        "nTO": 46,
        "expR": 0.132,
        "pf": 1.19,
        "mfe_p25": 22.0,
        "mfe_p50": 53.0,
        "mfe_p75": 155.5,
        "winnerMAE_p75": 19.25,
        "winnerMAE_p90": 88.00000000000009,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.0,
        "revAfterSL_rate": 33.7,
        "ci90": {
          "expR": 0.132,
          "ci90": [
            -0.007,
            0.275
          ],
          "p_mean_le_0": 0.059,
          "n": 471
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 2297,
      "wrTP1": 51.7,
      "nSL": 999,
      "nTO": 111,
      "expR": 0.078,
      "pf": 1.17,
      "mfe_p25": 17.0,
      "mfe_p50": 40.0,
      "mfe_p75": 113.0,
      "winnerMAE_p75": 33.0,
      "winnerMAE_p90": 145.20000000000027,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -42.0,
      "revAfterSL_rate": 48.7,
      "ci90": {
        "expR": 0.078,
        "ci90": [
          0.038,
          0.119
        ],
        "p_mean_le_0": 0.001,
        "n": 2201
      }
    },
    "cuts": {
      "1.0": {
        "n": 985,
        "wrTP1": 33.9,
        "nSL": 582,
        "nTO": 69,
        "expR": 0.067,
        "pf": 1.11,
        "mfe_p25": 24.0,
        "mfe_p50": 52.0,
        "mfe_p75": 146.0,
        "winnerMAE_p75": 30.0,
        "winnerMAE_p90": 119.89999999999992,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -37.0,
        "revAfterSL_rate": 42.4,
        "ci90": {
          "expR": 0.067,
          "ci90": [
            -0.012,
            0.147
          ],
          "p_mean_le_0": 0.082,
          "n": 930
        }
      },
      "1.2": {
        "n": 794,
        "wrTP1": 29.8,
        "nSL": 497,
        "nTO": 60,
        "expR": 0.043,
        "pf": 1.06,
        "mfe_p25": 24.5,
        "mfe_p50": 53.0,
        "mfe_p75": 149.5,
        "winnerMAE_p75": 28.0,
        "winnerMAE_p90": 133.8000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -37.5,
        "revAfterSL_rate": 39.2,
        "ci90": {
          "expR": 0.043,
          "ci90": [
            -0.049,
            0.137
          ],
          "p_mean_le_0": 0.234,
          "n": 747
        }
      },
      "1.3": {
        "n": 725,
        "wrTP1": 28.6,
        "nSL": 463,
        "nTO": 55,
        "expR": 0.024,
        "pf": 1.04,
        "mfe_p25": 25.0,
        "mfe_p50": 54.0,
        "mfe_p75": 157.0,
        "winnerMAE_p75": 28.5,
        "winnerMAE_p90": 125.80000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -38.0,
        "revAfterSL_rate": 39.1,
        "ci90": {
          "expR": 0.024,
          "ci90": [
            -0.073,
            0.124
          ],
          "p_mean_le_0": 0.355,
          "n": 683
        }
      },
      "1.5": {
        "n": 592,
        "wrTP1": 27.4,
        "nSL": 379,
        "nTO": 51,
        "expR": 0.053,
        "pf": 1.08,
        "mfe_p25": 25.25,
        "mfe_p50": 57.0,
        "mfe_p75": 157.0,
        "winnerMAE_p75": 26.75,
        "winnerMAE_p90": 141.80000000000013,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -37.0,
        "revAfterSL_rate": 34.8,
        "ci90": {
          "expR": 0.053,
          "ci90": [
            -0.066,
            0.174
          ],
          "p_mean_le_0": 0.233,
          "n": 554
        }
      },
      "2.0": {
        "n": 383,
        "wrTP1": 20.4,
        "nSL": 269,
        "nTO": 36,
        "expR": -0.041,
        "pf": 0.95,
        "mfe_p25": 29.0,
        "mfe_p50": 59.0,
        "mfe_p75": 146.5,
        "winnerMAE_p75": 24.25,
        "winnerMAE_p90": 65.09999999999998,
        "loserMFEbeforeSL_p50": 14.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -38.0,
        "revAfterSL_rate": 30.5,
        "ci90": {
          "expR": -0.041,
          "ci90": [
            -0.192,
            0.104
          ],
          "p_mean_le_0": 0.673,
          "n": 359
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
    "2026-W44",
    "2026-W45"
  ],
  "1/RETEST/LONG": {
    "baseline": {
      "n": 2504,
      "wrTP1": 47.3,
      "nSL": 1195,
      "nTO": 124,
      "expR": 0.006,
      "pf": 1.01,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 32.9,
      "ci90": {
        "expR": 0.006,
        "ci90": [
          -0.031,
          0.043
        ],
        "p_mean_le_0": 0.405,
        "n": 2453
      }
    },
    "cuts": {
      "1.2": {
        "n": 871,
        "wrTP1": 27.7,
        "nSL": 550,
        "nTO": 80,
        "expR": -0.001,
        "pf": 1.0,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 43.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 20.9,
        "ci90": {
          "expR": -0.001,
          "ci90": [
            -0.086,
            0.085
          ],
          "p_mean_le_0": 0.514,
          "n": 853
        }
      },
      "1.3": {
        "n": 786,
        "wrTP1": 25.7,
        "nSL": 505,
        "nTO": 79,
        "expR": -0.012,
        "pf": 0.98,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 42.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 19.900000000000006,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 19.8,
        "ci90": {
          "expR": -0.012,
          "ci90": [
            -0.103,
            0.079
          ],
          "p_mean_le_0": 0.591,
          "n": 768
        }
      },
      "1.5": {
        "n": 664,
        "wrTP1": 22.0,
        "nSL": 443,
        "nTO": 75,
        "expR": -0.046,
        "pf": 0.93,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 42.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 18.7,
        "ci90": {
          "expR": -0.046,
          "ci90": [
            -0.14,
            0.058
          ],
          "p_mean_le_0": 0.779,
          "n": 650
        }
      },
      "2.0": {
        "n": 432,
        "wrTP1": 16.7,
        "nSL": 302,
        "nTO": 58,
        "expR": -0.064,
        "pf": 0.91,
        "mfe_p25": 10.0,
        "mfe_p50": 27.0,
        "mfe_p75": 44.25,
        "winnerMAE_p75": 7.25,
        "winnerMAE_p90": 11.899999999999999,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 13.2,
        "ci90": {
          "expR": -0.064,
          "ci90": [
            -0.196,
            0.072
          ],
          "p_mean_le_0": 0.787,
          "n": 420
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 2939,
      "wrTP1": 47.4,
      "nSL": 1426,
      "nTO": 119,
      "expR": 0.01,
      "pf": 1.02,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 38.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 32.4,
      "ci90": {
        "expR": 0.01,
        "ci90": [
          -0.024,
          0.045
        ],
        "p_mean_le_0": 0.308,
        "n": 2894
      }
    },
    "cuts": {
      "1.2": {
        "n": 1038,
        "wrTP1": 27.6,
        "nSL": 667,
        "nTO": 84,
        "expR": 0.011,
        "pf": 1.02,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 32.2000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 20.1,
        "ci90": {
          "expR": 0.011,
          "ci90": [
            -0.066,
            0.088
          ],
          "p_mean_le_0": 0.412,
          "n": 1019
        }
      },
      "1.3": {
        "n": 947,
        "wrTP1": 26.0,
        "nSL": 620,
        "nTO": 81,
        "expR": 0.004,
        "pf": 1.01,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 18.1,
        "ci90": {
          "expR": 0.004,
          "ci90": [
            -0.077,
            0.086
          ],
          "p_mean_le_0": 0.48,
          "n": 930
        }
      },
      "1.5": {
        "n": 794,
        "wrTP1": 23.6,
        "nSL": 528,
        "nTO": 79,
        "expR": 0.013,
        "pf": 1.02,
        "mfe_p25": 13.0,
        "mfe_p50": 29.0,
        "mfe_p75": 62.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 34.400000000000006,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 10.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 15.7,
        "ci90": {
          "expR": 0.013,
          "ci90": [
            -0.08,
            0.109
          ],
          "p_mean_le_0": 0.414,
          "n": 777
        }
      },
      "2.0": {
        "n": 536,
        "wrTP1": 18.1,
        "nSL": 370,
        "nTO": 69,
        "expR": 0.014,
        "pf": 1.02,
        "mfe_p25": 13.5,
        "mfe_p50": 31.0,
        "mfe_p75": 63.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 26.00000000000003,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 10.3,
        "ci90": {
          "expR": 0.014,
          "ci90": [
            -0.106,
            0.143
          ],
          "p_mean_le_0": 0.42,
          "n": 523
        }
      }
    }
  },
  "15/RETEST/LONG": {
    "baseline": {
      "n": 388,
      "wrTP1": 52.1,
      "nSL": 183,
      "nTO": 3,
      "expR": 0.087,
      "pf": 1.18,
      "mfe_p25": 31.0,
      "mfe_p50": 70.0,
      "mfe_p75": 334.0,
      "winnerMAE_p75": 109.0,
      "winnerMAE_p90": 2366.900000000002,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -79.5,
      "revAfterSL_rate": 55.7,
      "ci90": {
        "expR": 0.087,
        "ci90": [
          -0.013,
          0.188
        ],
        "p_mean_le_0": 0.08,
        "n": 385
      }
    },
    "cuts": {
      "1.2": {
        "n": 113,
        "wrTP1": 30.1,
        "nSL": 79,
        "nTO": 0,
        "expR": 0.011,
        "pf": 1.02,
        "mfe_p25": 42.0,
        "mfe_p50": 75.0,
        "mfe_p75": 257.0,
        "winnerMAE_p75": 79.25,
        "winnerMAE_p90": 2681.8999999999996,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -61.0,
        "revAfterSL_rate": 55.7,
        "ci90": {
          "expR": 0.011,
          "ci90": [
            -0.232,
            0.28
          ],
          "p_mean_le_0": 0.486,
          "n": 113
        }
      },
      "1.3": {
        "n": 106,
        "wrTP1": 29.2,
        "nSL": 75,
        "nTO": 0,
        "expR": -0.008,
        "pf": 0.99,
        "mfe_p25": 42.0,
        "mfe_p50": 76.0,
        "mfe_p75": 270.5,
        "winnerMAE_p75": 99.5,
        "winnerMAE_p90": 2750.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -69.0,
        "revAfterSL_rate": 56.0,
        "ci90": {
          "expR": -0.008,
          "ci90": [
            -0.26,
            0.257
          ],
          "p_mean_le_0": 0.511,
          "n": 106
        }
      },
      "1.5": {
        "n": 79,
        "wrTP1": 29.1,
        "nSL": 56,
        "nTO": 0,
        "expR": 0.055,
        "pf": 1.08,
        "mfe_p25": 43.5,
        "mfe_p50": 76.0,
        "mfe_p75": 266.0,
        "winnerMAE_p75": 99.5,
        "winnerMAE_p90": 2704.6,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -56.0,
        "revAfterSL_rate": 51.8,
        "ci90": {
          "expR": 0.055,
          "ci90": [
            -0.251,
            0.374
          ],
          "p_mean_le_0": 0.394,
          "n": 79
        }
      },
      "2.0": {
        "n": 46,
        "wrTP1": 21.7,
        "nSL": 36,
        "nTO": 0,
        "expR": -0.098,
        "pf": 0.88,
        "mfe_p25": 44.25,
        "mfe_p50": 82.5,
        "mfe_p75": 8053.25,
        "winnerMAE_p75": 2074.5,
        "winnerMAE_p90": 11698.799999999996,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -57.5,
        "revAfterSL_rate": 38.9,
        "ci90": {
          "expR": -0.098,
          "ci90": [
            -0.513,
            0.337
          ],
          "p_mean_le_0": 0.644,
          "n": 46
        }
      }
    }
  },
  "15/RETEST/SHORT": {
    "baseline": {
      "n": 416,
      "wrTP1": 54.8,
      "nSL": 185,
      "nTO": 3,
      "expR": 0.126,
      "pf": 1.28,
      "mfe_p25": 38.0,
      "mfe_p50": 153.0,
      "mfe_p75": 2509.0,
      "winnerMAE_p75": 556.25,
      "winnerMAE_p90": 5180.400000000002,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -291.5,
      "revAfterSL_rate": 73.0,
      "ci90": {
        "expR": 0.126,
        "ci90": [
          0.025,
          0.226
        ],
        "p_mean_le_0": 0.015,
        "n": 413
      }
    },
    "cuts": {
      "1.2": {
        "n": 109,
        "wrTP1": 41.3,
        "nSL": 64,
        "nTO": 0,
        "expR": 0.356,
        "pf": 1.61,
        "mfe_p25": 53.0,
        "mfe_p50": 155.0,
        "mfe_p75": 2092.0,
        "winnerMAE_p75": 447.0,
        "winnerMAE_p90": 3653.2,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -229.0,
        "revAfterSL_rate": 62.5,
        "ci90": {
          "expR": 0.356,
          "ci90": [
            0.072,
            0.646
          ],
          "p_mean_le_0": 0.02,
          "n": 109
        }
      },
      "1.3": {
        "n": 100,
        "wrTP1": 40.0,
        "nSL": 60,
        "nTO": 0,
        "expR": 0.341,
        "pf": 1.57,
        "mfe_p25": 52.75,
        "mfe_p50": 130.5,
        "mfe_p75": 3088.5,
        "winnerMAE_p75": 668.5,
        "winnerMAE_p90": 3609.7000000000003,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -229.5,
        "revAfterSL_rate": 63.3,
        "ci90": {
          "expR": 0.341,
          "ci90": [
            0.031,
            0.654
          ],
          "p_mean_le_0": 0.035,
          "n": 100
        }
      },
      "1.5": {
        "n": 77,
        "wrTP1": 32.5,
        "nSL": 52,
        "nTO": 0,
        "expR": 0.234,
        "pf": 1.35,
        "mfe_p25": 58.0,
        "mfe_p50": 134.0,
        "mfe_p75": 5361.0,
        "winnerMAE_p75": 447.0,
        "winnerMAE_p90": 2609.4,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -190.0,
        "revAfterSL_rate": 61.5,
        "ci90": {
          "expR": 0.234,
          "ci90": [
            -0.129,
            0.616
          ],
          "p_mean_le_0": 0.162,
          "n": 77
        }
      },
      "2.0": {
        "n": 47,
        "wrTP1": 29.8,
        "nSL": 33,
        "nTO": 0,
        "expR": 0.306,
        "pf": 1.44,
        "mfe_p25": 62.5,
        "mfe_p50": 180.0,
        "mfe_p75": 9065.0,
        "winnerMAE_p75": 1004.75,
        "winnerMAE_p90": 2569.9000000000005,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -360.0,
        "revAfterSL_rate": 54.5,
        "ci90": {
          "expR": 0.306,
          "ci90": [
            -0.207,
            0.843
          ],
          "p_mean_le_0": 0.173,
          "n": 47
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 1081,
      "wrTP1": 48.3,
      "nSL": 542,
      "nTO": 17,
      "expR": -0.054,
      "pf": 0.89,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 44.25,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 32.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 46.5,
      "ci90": {
        "expR": -0.054,
        "ci90": [
          -0.106,
          0.005
        ],
        "p_mean_le_0": 0.933,
        "n": 1076
      }
    },
    "cuts": {
      "1.2": {
        "n": 353,
        "wrTP1": 24.9,
        "nSL": 252,
        "nTO": 13,
        "expR": -0.166,
        "pf": 0.77,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 55.75,
        "winnerMAE_p75": 10.5,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 40.1,
        "ci90": {
          "expR": -0.166,
          "ci90": [
            -0.294,
            -0.028
          ],
          "p_mean_le_0": 0.978,
          "n": 350
        }
      },
      "1.3": {
        "n": 315,
        "wrTP1": 23.5,
        "nSL": 229,
        "nTO": 12,
        "expR": -0.17,
        "pf": 0.77,
        "mfe_p25": 13.0,
        "mfe_p50": 28.0,
        "mfe_p75": 57.25,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 22.80000000000001,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 38.9,
        "ci90": {
          "expR": -0.17,
          "ci90": [
            -0.308,
            -0.027
          ],
          "p_mean_le_0": 0.976,
          "n": 312
        }
      },
      "1.5": {
        "n": 262,
        "wrTP1": 21.4,
        "nSL": 194,
        "nTO": 12,
        "expR": -0.176,
        "pf": 0.76,
        "mfe_p25": 13.0,
        "mfe_p50": 28.0,
        "mfe_p75": 55.5,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 35.6,
        "ci90": {
          "expR": -0.176,
          "ci90": [
            -0.332,
            -0.01
          ],
          "p_mean_le_0": 0.959,
          "n": 259
        }
      },
      "2.0": {
        "n": 149,
        "wrTP1": 15.4,
        "nSL": 114,
        "nTO": 12,
        "expR": -0.191,
        "pf": 0.76,
        "mfe_p25": 14.0,
        "mfe_p50": 30.0,
        "mfe_p75": 66.75,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 44.00000000000002,
        "loserMFEbeforeSL_p50": 11.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -20.0,
        "revAfterSL_rate": 21.9,
        "ci90": {
          "expR": -0.191,
          "ci90": [
            -0.422,
            0.054
          ],
          "p_mean_le_0": 0.905,
          "n": 146
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 1310,
      "wrTP1": 48.2,
      "nSL": 649,
      "nTO": 29,
      "expR": 0.025,
      "pf": 1.05,
      "mfe_p25": 10.0,
      "mfe_p50": 25.0,
      "mfe_p75": 57.0,
      "winnerMAE_p75": 16.25,
      "winnerMAE_p90": 40.89999999999998,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -20.0,
      "revAfterSL_rate": 40.2,
      "ci90": {
        "expR": 0.025,
        "ci90": [
          -0.03,
          0.081
        ],
        "p_mean_le_0": 0.236,
        "n": 1300
      }
    },
    "cuts": {
      "1.2": {
        "n": 482,
        "wrTP1": 29.7,
        "nSL": 315,
        "nTO": 24,
        "expR": 0.026,
        "pf": 1.04,
        "mfe_p25": 18.0,
        "mfe_p50": 42.0,
        "mfe_p75": 79.0,
        "winnerMAE_p75": 16.5,
        "winnerMAE_p90": 38.599999999999994,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 30.2,
        "ci90": {
          "expR": 0.026,
          "ci90": [
            -0.1,
            0.143
          ],
          "p_mean_le_0": 0.369,
          "n": 477
        }
      },
      "1.3": {
        "n": 428,
        "wrTP1": 27.6,
        "nSL": 286,
        "nTO": 24,
        "expR": 0.018,
        "pf": 1.03,
        "mfe_p25": 18.0,
        "mfe_p50": 42.0,
        "mfe_p75": 81.5,
        "winnerMAE_p75": 18.5,
        "winnerMAE_p90": 39.0,
        "loserMFEbeforeSL_p50": 8.5,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 28.0,
        "ci90": {
          "expR": 0.018,
          "ci90": [
            -0.11,
            0.163
          ],
          "p_mean_le_0": 0.404,
          "n": 423
        }
      },
      "1.5": {
        "n": 350,
        "wrTP1": 25.7,
        "nSL": 239,
        "nTO": 21,
        "expR": 0.038,
        "pf": 1.05,
        "mfe_p25": 18.0,
        "mfe_p50": 43.0,
        "mfe_p75": 83.25,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 39.10000000000001,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -20.5,
        "revAfterSL_rate": 23.4,
        "ci90": {
          "expR": 0.038,
          "ci90": [
            -0.111,
            0.192
          ],
          "p_mean_le_0": 0.356,
          "n": 348
        }
      },
      "2.0": {
        "n": 215,
        "wrTP1": 20.5,
        "nSL": 153,
        "nTO": 18,
        "expR": 0.076,
        "pf": 1.11,
        "mfe_p25": 19.0,
        "mfe_p50": 44.0,
        "mfe_p75": 85.5,
        "winnerMAE_p75": 10.25,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 15.7,
        "ci90": {
          "expR": 0.076,
          "ci90": [
            -0.137,
            0.305
          ],
          "p_mean_le_0": 0.289,
          "n": 214
        }
      }
    }
  },
  "29/RETEST/LONG": {
    "baseline": {
      "n": 165,
      "wrTP1": 57.6,
      "nSL": 70,
      "nTO": 0,
      "expR": 0.279,
      "pf": 1.66,
      "mfe_p25": 42.0,
      "mfe_p50": 94.0,
      "mfe_p75": 303.0,
      "winnerMAE_p75": 133.5,
      "winnerMAE_p90": 6753.200000000012,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -76.0,
      "revAfterSL_rate": 60.0,
      "ci90": {
        "expR": 0.279,
        "ci90": [
          0.114,
          0.455
        ],
        "p_mean_le_0": 0.004,
        "n": 165
      }
    },
    "cuts": {
      "1.2": {
        "n": 52,
        "wrTP1": 38.5,
        "nSL": 32,
        "nTO": 0,
        "expR": 0.364,
        "pf": 1.59,
        "mfe_p25": 46.75,
        "mfe_p50": 89.5,
        "mfe_p75": 238.25,
        "winnerMAE_p75": 35.25,
        "winnerMAE_p90": 182.60000000000122,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -45.0,
        "revAfterSL_rate": 59.4,
        "ci90": {
          "expR": 0.364,
          "ci90": [
            -0.068,
            0.798
          ],
          "p_mean_le_0": 0.085,
          "n": 52
        }
      },
      "1.3": {
        "n": 47,
        "wrTP1": 36.2,
        "nSL": 30,
        "nTO": 0,
        "expR": 0.355,
        "pf": 1.56,
        "mfe_p25": 44.5,
        "mfe_p50": 75.0,
        "mfe_p75": 236.5,
        "winnerMAE_p75": 36.0,
        "winnerMAE_p90": 442.4000000000003,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -46.0,
        "revAfterSL_rate": 56.7,
        "ci90": {
          "expR": 0.355,
          "ci90": [
            -0.116,
            0.857
          ],
          "p_mean_le_0": 0.107,
          "n": 47
        }
      },
      "1.5": {
        "n": 40,
        "wrTP1": 30.0,
        "nSL": 28,
        "nTO": 0,
        "expR": 0.261,
        "pf": 1.37,
        "mfe_p25": 45.25,
        "mfe_p50": 89.5,
        "mfe_p75": 252.75,
        "winnerMAE_p75": 51.0,
        "winnerMAE_p90": 96.0,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -55.5,
        "revAfterSL_rate": 53.6,
        "ci90": {
          "expR": 0.261,
          "ci90": [
            -0.265,
            0.79
          ],
          "p_mean_le_0": 0.226,
          "n": 40
        }
      },
      "2.0": {
        "n": 26,
        "wrTP1": 34.6,
        "nSL": 17,
        "nTO": 0,
        "expR": 0.599,
        "pf": 1.92,
        "mfe_p25": 56.75,
        "mfe_p50": 96.5,
        "mfe_p75": 282.25,
        "winnerMAE_p75": 35.0,
        "winnerMAE_p90": 719.6000000000006,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -49.5,
        "revAfterSL_rate": 64.7,
        "ci90": {
          "expR": 0.599,
          "ci90": [
            -0.119,
            1.377
          ],
          "p_mean_le_0": 0.086,
          "n": 26
        }
      }
    }
  },
  "29/RETEST/SHORT": {
    "baseline": {
      "n": 233,
      "wrTP1": 56.7,
      "nSL": 100,
      "nTO": 1,
      "expR": 0.168,
      "pf": 1.39,
      "mfe_p25": 44.75,
      "mfe_p50": 147.0,
      "mfe_p75": 1235.25,
      "winnerMAE_p75": 265.25,
      "winnerMAE_p90": 4568.400000000005,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 1.0,
      "entryZoneTk_p50": -304.0,
      "revAfterSL_rate": 76.0,
      "ci90": {
        "expR": 0.168,
        "ci90": [
          0.041,
          0.288
        ],
        "p_mean_le_0": 0.012,
        "n": 232
      }
    },
    "cuts": {
      "1.2": {
        "n": 59,
        "wrTP1": 37.3,
        "nSL": 37,
        "nTO": 0,
        "expR": 0.245,
        "pf": 1.39,
        "mfe_p25": 58.0,
        "mfe_p50": 147.0,
        "mfe_p75": 1223.5,
        "winnerMAE_p75": 279.5,
        "winnerMAE_p90": 1110.900000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -286.0,
        "revAfterSL_rate": 59.5,
        "ci90": {
          "expR": 0.245,
          "ci90": [
            -0.108,
            0.622
          ],
          "p_mean_le_0": 0.131,
          "n": 59
        }
      },
      "1.3": {
        "n": 54,
        "wrTP1": 35.2,
        "nSL": 35,
        "nTO": 0,
        "expR": 0.228,
        "pf": 1.35,
        "mfe_p25": 72.75,
        "mfe_p50": 162.5,
        "mfe_p75": 1229.75,
        "winnerMAE_p75": 347.5,
        "winnerMAE_p90": 1426.1999999999991,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -300.0,
        "revAfterSL_rate": 60.0,
        "ci90": {
          "expR": 0.228,
          "ci90": [
            -0.175,
            0.619
          ],
          "p_mean_le_0": 0.182,
          "n": 54
        }
      },
      "1.5": {
        "n": 42,
        "wrTP1": 33.3,
        "nSL": 28,
        "nTO": 0,
        "expR": 0.266,
        "pf": 1.4,
        "mfe_p25": 81.0,
        "mfe_p50": 134.5,
        "mfe_p75": 1157.5,
        "winnerMAE_p75": 190.0,
        "winnerMAE_p90": 369.7000000000001,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -259.5,
        "revAfterSL_rate": 57.1,
        "ci90": {
          "expR": 0.266,
          "ci90": [
            -0.177,
            0.753
          ],
          "p_mean_le_0": 0.176,
          "n": 42
        }
      },
      "2.0": {
        "n": 27,
        "wrTP1": 29.6,
        "nSL": 19,
        "nTO": 0,
        "expR": 0.236,
        "pf": 1.34,
        "mfe_p25": 63.5,
        "mfe_p50": 102.0,
        "mfe_p75": 754.0,
        "winnerMAE_p75": 79.5,
        "winnerMAE_p90": 224.09999999999997,
        "loserMFEbeforeSL_p50": 0.0,
        "bars_win_p50": 1.5,
        "bars_loss_p50": 1.0,
        "entryZoneTk_p50": -238.0,
        "revAfterSL_rate": 52.6,
        "ci90": {
          "expR": 0.236,
          "ci90": [
            -0.346,
            0.858
          ],
          "p_mean_le_0": 0.261,
          "n": 27
        }
      }
    }
  },
  "3/RETEST/LONG": {
    "baseline": {
      "n": 1237,
      "wrTP1": 53.6,
      "nSL": 562,
      "nTO": 12,
      "expR": 0.093,
      "pf": 1.2,
      "mfe_p25": 11.0,
      "mfe_p50": 23.0,
      "mfe_p75": 51.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 33.80000000000007,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -20.0,
      "revAfterSL_rate": 52.5,
      "ci90": {
        "expR": 0.093,
        "ci90": [
          0.04,
          0.146
        ],
        "p_mean_le_0": 0.003,
        "n": 1230
      }
    },
    "cuts": {
      "1.2": {
        "n": 343,
        "wrTP1": 37.3,
        "nSL": 209,
        "nTO": 6,
        "expR": 0.177,
        "pf": 1.29,
        "mfe_p25": 17.0,
        "mfe_p50": 35.0,
        "mfe_p75": 72.5,
        "winnerMAE_p75": 14.25,
        "winnerMAE_p90": 29.699999999999974,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 42.6,
        "ci90": {
          "expR": 0.177,
          "ci90": [
            0.034,
            0.318
          ],
          "p_mean_le_0": 0.013,
          "n": 342
        }
      },
      "1.3": {
        "n": 296,
        "wrTP1": 35.5,
        "nSL": 185,
        "nTO": 6,
        "expR": 0.173,
        "pf": 1.27,
        "mfe_p25": 18.5,
        "mfe_p50": 36.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 38.400000000000034,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -20.0,
        "revAfterSL_rate": 41.6,
        "ci90": {
          "expR": 0.173,
          "ci90": [
            0.018,
            0.338
          ],
          "p_mean_le_0": 0.034,
          "n": 295
        }
      },
      "1.5": {
        "n": 224,
        "wrTP1": 35.3,
        "nSL": 140,
        "nTO": 5,
        "expR": 0.259,
        "pf": 1.41,
        "mfe_p25": 21.75,
        "mfe_p50": 41.0,
        "mfe_p75": 78.5,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 46.000000000000014,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -19.5,
        "revAfterSL_rate": 36.4,
        "ci90": {
          "expR": 0.259,
          "ci90": [
            0.066,
            0.451
          ],
          "p_mean_le_0": 0.016,
          "n": 224
        }
      },
      "2.0": {
        "n": 124,
        "wrTP1": 35.5,
        "nSL": 75,
        "nTO": 5,
        "expR": 0.458,
        "pf": 1.75,
        "mfe_p25": 30.5,
        "mfe_p50": 48.5,
        "mfe_p75": 88.25,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 26.10000000000001,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -21.0,
        "revAfterSL_rate": 33.3,
        "ci90": {
          "expR": 0.458,
          "ci90": [
            0.182,
            0.748
          ],
          "p_mean_le_0": 0.003,
          "n": 124
        }
      }
    }
  },
  "3/RETEST/SHORT": {
    "baseline": {
      "n": 1116,
      "wrTP1": 57.1,
      "nSL": 466,
      "nTO": 13,
      "expR": 0.16,
      "pf": 1.38,
      "mfe_p25": 12.0,
      "mfe_p50": 22.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 18.0,
      "winnerMAE_p90": 39.0,
      "loserMFEbeforeSL_p50": 1.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -24.0,
      "revAfterSL_rate": 56.2,
      "ci90": {
        "expR": 0.16,
        "ci90": [
          0.103,
          0.217
        ],
        "p_mean_le_0": 0.0,
        "n": 1109
      }
    },
    "cuts": {
      "1.2": {
        "n": 309,
        "wrTP1": 39.2,
        "nSL": 177,
        "nTO": 11,
        "expR": 0.238,
        "pf": 1.41,
        "mfe_p25": 16.75,
        "mfe_p50": 32.0,
        "mfe_p75": 64.25,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 48.0,
        "ci90": {
          "expR": 0.238,
          "ci90": [
            0.094,
            0.385
          ],
          "p_mean_le_0": 0.005,
          "n": 304
        }
      },
      "1.3": {
        "n": 268,
        "wrTP1": 37.3,
        "nSL": 157,
        "nTO": 11,
        "expR": 0.235,
        "pf": 1.39,
        "mfe_p25": 17.0,
        "mfe_p50": 32.0,
        "mfe_p75": 63.5,
        "winnerMAE_p75": 16.75,
        "winnerMAE_p90": 34.30000000000011,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 45.2,
        "ci90": {
          "expR": 0.235,
          "ci90": [
            0.077,
            0.4
          ],
          "p_mean_le_0": 0.007,
          "n": 263
        }
      },
      "1.5": {
        "n": 213,
        "wrTP1": 32.9,
        "nSL": 133,
        "nTO": 10,
        "expR": 0.183,
        "pf": 1.29,
        "mfe_p25": 18.0,
        "mfe_p50": 33.0,
        "mfe_p75": 72.0,
        "winnerMAE_p75": 22.0,
        "winnerMAE_p90": 54.2,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 42.9,
        "ci90": {
          "expR": 0.183,
          "ci90": [
            0.005,
            0.371
          ],
          "p_mean_le_0": 0.048,
          "n": 209
        }
      },
      "2.0": {
        "n": 101,
        "wrTP1": 30.7,
        "nSL": 65,
        "nTO": 5,
        "expR": 0.293,
        "pf": 1.45,
        "mfe_p25": 19.0,
        "mfe_p50": 33.5,
        "mfe_p75": 73.25,
        "winnerMAE_p75": 14.5,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 23.1,
        "ci90": {
          "expR": 0.293,
          "ci90": [
            0.007,
            0.603
          ],
          "p_mean_le_0": 0.047,
          "n": 100
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 946,
      "wrTP1": 54.1,
      "nSL": 416,
      "nTO": 18,
      "expR": 0.107,
      "pf": 1.24,
      "mfe_p25": 33.5,
      "mfe_p50": 234.0,
      "mfe_p75": 3562.0,
      "winnerMAE_p75": 397.75,
      "winnerMAE_p90": 3192.700000000007,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -253.0,
      "revAfterSL_rate": 53.1,
      "ci90": {
        "expR": 0.107,
        "ci90": [
          0.047,
          0.168
        ],
        "p_mean_le_0": 0.004,
        "n": 939
      }
    },
    "cuts": {
      "1.2": {
        "n": 288,
        "wrTP1": 33.0,
        "nSL": 180,
        "nTO": 13,
        "expR": 0.124,
        "pf": 1.2,
        "mfe_p25": 39.0,
        "mfe_p50": 345.0,
        "mfe_p75": 4670.0,
        "winnerMAE_p75": 276.5,
        "winnerMAE_p90": 1861.600000000002,
        "loserMFEbeforeSL_p50": 1.5,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -132.0,
        "revAfterSL_rate": 42.2,
        "ci90": {
          "expR": 0.124,
          "ci90": [
            -0.03,
            0.28
          ],
          "p_mean_le_0": 0.093,
          "n": 285
        }
      },
      "1.3": {
        "n": 263,
        "wrTP1": 31.9,
        "nSL": 166,
        "nTO": 13,
        "expR": 0.135,
        "pf": 1.21,
        "mfe_p25": 41.75,
        "mfe_p50": 333.5,
        "mfe_p75": 4564.0,
        "winnerMAE_p75": 206.5,
        "winnerMAE_p90": 1675.0000000000005,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -123.0,
        "revAfterSL_rate": 42.2,
        "ci90": {
          "expR": 0.135,
          "ci90": [
            -0.032,
            0.313
          ],
          "p_mean_le_0": 0.092,
          "n": 260
        }
      },
      "1.5": {
        "n": 205,
        "wrTP1": 31.2,
        "nSL": 129,
        "nTO": 12,
        "expR": 0.2,
        "pf": 1.31,
        "mfe_p25": 56.0,
        "mfe_p50": 402.0,
        "mfe_p75": 7330.0,
        "winnerMAE_p75": 184.0,
        "winnerMAE_p90": 1833.2000000000012,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -146.0,
        "revAfterSL_rate": 43.4,
        "ci90": {
          "expR": 0.2,
          "ci90": [
            -0.002,
            0.408
          ],
          "p_mean_le_0": 0.051,
          "n": 203
        }
      },
      "2.0": {
        "n": 114,
        "wrTP1": 24.6,
        "nSL": 75,
        "nTO": 11,
        "expR": 0.216,
        "pf": 1.32,
        "mfe_p25": 73.0,
        "mfe_p50": 527.5,
        "mfe_p75": 9403.25,
        "winnerMAE_p75": 413.25,
        "winnerMAE_p90": 2330.6000000000013,
        "loserMFEbeforeSL_p50": 17.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -199.0,
        "revAfterSL_rate": 29.3,
        "ci90": {
          "expR": 0.216,
          "ci90": [
            -0.075,
            0.51
          ],
          "p_mean_le_0": 0.115,
          "n": 112
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 877,
      "wrTP1": 53.7,
      "nSL": 397,
      "nTO": 9,
      "expR": 0.085,
      "pf": 1.19,
      "mfe_p25": 22.75,
      "mfe_p50": 85.0,
      "mfe_p75": 853.5,
      "winnerMAE_p75": 145.5,
      "winnerMAE_p90": 1960.0,
      "loserMFEbeforeSL_p50": 0.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -88.0,
      "revAfterSL_rate": 56.4,
      "ci90": {
        "expR": 0.085,
        "ci90": [
          0.021,
          0.148
        ],
        "p_mean_le_0": 0.013,
        "n": 872
      }
    },
    "cuts": {
      "1.2": {
        "n": 287,
        "wrTP1": 33.1,
        "nSL": 184,
        "nTO": 8,
        "expR": 0.067,
        "pf": 1.1,
        "mfe_p25": 33.5,
        "mfe_p50": 97.0,
        "mfe_p75": 1008.5,
        "winnerMAE_p75": 135.5,
        "winnerMAE_p90": 2213.4000000000024,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -68.0,
        "revAfterSL_rate": 48.9,
        "ci90": {
          "expR": 0.067,
          "ci90": [
            -0.082,
            0.225
          ],
          "p_mean_le_0": 0.224,
          "n": 283
        }
      },
      "1.3": {
        "n": 257,
        "wrTP1": 31.5,
        "nSL": 169,
        "nTO": 7,
        "expR": 0.044,
        "pf": 1.07,
        "mfe_p25": 33.25,
        "mfe_p50": 104.0,
        "mfe_p75": 1124.75,
        "winnerMAE_p75": 127.0,
        "winnerMAE_p90": 2321.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -68.0,
        "revAfterSL_rate": 49.1,
        "ci90": {
          "expR": 0.044,
          "ci90": [
            -0.118,
            0.211
          ],
          "p_mean_le_0": 0.337,
          "n": 254
        }
      },
      "1.5": {
        "n": 205,
        "wrTP1": 30.7,
        "nSL": 136,
        "nTO": 6,
        "expR": 0.087,
        "pf": 1.13,
        "mfe_p25": 33.5,
        "mfe_p50": 97.0,
        "mfe_p75": 1008.5,
        "winnerMAE_p75": 146.5,
        "winnerMAE_p90": 2488.8000000000025,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -65.0,
        "revAfterSL_rate": 44.9,
        "ci90": {
          "expR": 0.087,
          "ci90": [
            -0.113,
            0.277
          ],
          "p_mean_le_0": 0.24,
          "n": 203
        }
      },
      "2.0": {
        "n": 125,
        "wrTP1": 21.6,
        "nSL": 92,
        "nTO": 6,
        "expR": -0.055,
        "pf": 0.93,
        "mfe_p25": 36.0,
        "mfe_p50": 82.0,
        "mfe_p75": 726.5,
        "winnerMAE_p75": 50.0,
        "winnerMAE_p90": 1408.6000000000004,
        "loserMFEbeforeSL_p50": 19.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -58.0,
        "revAfterSL_rate": 39.1,
        "ci90": {
          "expR": -0.055,
          "ci90": [
            -0.306,
            0.208
          ],
          "p_mean_le_0": 0.626,
          "n": 123
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
    "n": 3350,
    "wrTP1": 48.4,
    "expR": 0.093
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
    "15m/RETEST/LONG": {
      "n": 117,
      "wrTP1": 50.4,
      "expR": 0.086,
      "pf": 1.17
    },
    "15m/RETEST/SHORT": {
      "n": 128,
      "wrTP1": 56.2,
      "expR": 0.304,
      "pf": 1.71
    },
    "1m/INV/LONG": {
      "n": 10,
      "wrTP1": 70.0,
      "expR": 0.313,
      "pf": 2.04
    },
    "1m/INV/SHORT": {
      "n": 24,
      "wrTP1": 41.7,
      "expR": 0.401,
      "pf": 1.96
    },
    "1m/RETEST/LONG": {
      "n": 223,
      "wrTP1": 41.3,
      "expR": -0.069,
      "pf": 0.87
    },
    "1m/RETEST/SHORT": {
      "n": 927,
      "wrTP1": 41.7,
      "expR": 0.007,
      "pf": 1.01
    },
    "29m/RETEST/LONG": {
      "n": 51,
      "wrTP1": 56.9,
      "expR": 0.449,
      "pf": 2.04
    },
    "29m/RETEST/SHORT": {
      "n": 62,
      "wrTP1": 56.5,
      "expR": 0.344,
      "pf": 1.82
    },
    "2m/INV/LONG": {
      "n": 6,
      "wrTP1": 50.0,
      "expR": 0.028,
      "pf": 1.06
    },
    "2m/INV/SHORT": {
      "n": 10,
      "wrTP1": 20.0,
      "expR": -0.62,
      "pf": 0.13
    },
    "2m/RETEST/LONG": {
      "n": 117,
      "wrTP1": 38.5,
      "expR": -0.105,
      "pf": 0.82
    },
    "2m/RETEST/SHORT": {
      "n": 406,
      "wrTP1": 48.5,
      "expR": 0.137,
      "pf": 1.28
    },
    "3m/INV/LONG": {
      "n": 3,
      "wrTP1": 33.3,
      "expR": -0.507,
      "pf": 0.24
    },
    "3m/INV/SHORT": {
      "n": 3,
      "wrTP1": 100.0,
      "expR": 0.413,
      "pf": 99.0
    },
    "3m/RETEST/LONG": {
      "n": 460,
      "wrTP1": 53.0,
      "expR": 0.118,
      "pf": 1.26
    },
    "3m/RETEST/SHORT": {
      "n": 385,
      "wrTP1": 59.7,
      "expR": 0.218,
      "pf": 1.54
    },
    "5m/INV/LONG": {
      "n": 2,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/INV/SHORT": {
      "n": 5,
      "wrTP1": 100.0,
      "expR": 0.584,
      "pf": 99.0
    },
    "5m/RETEST/LONG": {
      "n": 177,
      "wrTP1": 50.3,
      "expR": 0.152,
      "pf": 1.33
    },
    "5m/RETEST/SHORT": {
      "n": 234,
      "wrTP1": 47.0,
      "expR": 0.043,
      "pf": 1.09
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 49776,
  "brier": 0.2218,
  "bias": -0.097,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.279
    },
    {
      "feature": "stretchAtr",
      "weight": -0.055
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.049
    },
    {
      "feature": "nearTk",
      "weight": -0.04
    },
    {
      "feature": "hourNY",
      "weight": 0.029
    },
    {
      "feature": "biasScore",
      "weight": -0.026
    },
    {
      "feature": "rvol",
      "weight": 0.019
    },
    {
      "feature": "aligned",
      "weight": -0.017
    },
    {
      "feature": "emaStack",
      "weight": 0.016
    },
    {
      "feature": "chopIdx",
      "weight": -0.016
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.012
    },
    {
      "feature": "nearEdge",
      "weight": 0.005
    },
    {
      "feature": "structDir",
      "weight": 0.002
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.168,
      "actual": 0.171,
      "n": 4977
    },
    {
      "bin": 1,
      "pred": 0.371,
      "actual": 0.31,
      "n": 4978
    },
    {
      "bin": 2,
      "pred": 0.449,
      "actual": 0.317,
      "n": 4977
    },
    {
      "bin": 3,
      "pred": 0.493,
      "actual": 0.428,
      "n": 4978
    },
    {
      "bin": 4,
      "pred": 0.53,
      "actual": 0.51,
      "n": 4978
    },
    {
      "bin": 5,
      "pred": 0.558,
      "actual": 0.571,
      "n": 4977
    },
    {
      "bin": 6,
      "pred": 0.58,
      "actual": 0.613,
      "n": 4978
    },
    {
      "bin": 7,
      "pred": 0.599,
      "actual": 0.64,
      "n": 4977
    },
    {
      "bin": 8,
      "pred": 0.618,
      "actual": 0.689,
      "n": 4978
    },
    {
      "bin": 9,
      "pred": 0.645,
      "actual": 0.747,
      "n": 4978
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 39313,
  "testN": 13846,
  "testWeeks": [
    "2026-W44",
    "2026-W45"
  ],
  "model_oos_brier": 0.2464,
  "model_oos_n": 13846,
  "best_scheme_in_sample": {
    "scheme": "fixed_2R",
    "trainExpR": 0.046
  },
  "best_scheme_oos_expR": 0.057
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "15m/RETEST/LONG": {
    "expR": 0.051,
    "ci90": [
      -0.046,
      0.15
    ],
    "p_mean_le_0": 0.21,
    "n": 400,
    "survives_fdr10": false
  },
  "15m/RETEST/SHORT": {
    "expR": 0.116,
    "ci90": [
      0.01,
      0.228
    ],
    "p_mean_le_0": 0.037,
    "n": 428,
    "survives_fdr10": true
  },
  "1m/INV/LONG": {
    "expR": 0.12,
    "ci90": [
      0.025,
      0.225
    ],
    "p_mean_le_0": 0.017,
    "n": 447,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": 0.106,
    "ci90": [
      0.003,
      0.208
    ],
    "p_mean_le_0": 0.043,
    "n": 334,
    "survives_fdr10": true
  },
  "1m/RETEST/LONG": {
    "expR": 0.024,
    "ci90": [
      0.01,
      0.04
    ],
    "p_mean_le_0": 0.006,
    "n": 16850,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.027,
    "ci90": [
      0.009,
      0.046
    ],
    "p_mean_le_0": 0.009,
    "n": 11787,
    "survives_fdr10": true
  },
  "29m/RETEST/LONG": {
    "expR": 0.227,
    "ci90": [
      0.054,
      0.395
    ],
    "p_mean_le_0": 0.015,
    "n": 172,
    "survives_fdr10": true
  },
  "29m/RETEST/SHORT": {
    "expR": 0.17,
    "ci90": [
      0.034,
      0.313
    ],
    "p_mean_le_0": 0.019,
    "n": 240,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.043,
    "ci90": [
      -0.098,
      0.187
    ],
    "p_mean_le_0": 0.331,
    "n": 163,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.065,
    "ci90": [
      -0.106,
      0.258
    ],
    "p_mean_le_0": 0.288,
    "n": 126,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.028,
    "ci90": [
      0.005,
      0.05
    ],
    "p_mean_le_0": 0.019,
    "n": 7387,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.05,
    "ci90": [
      0.02,
      0.079
    ],
    "p_mean_le_0": 0.001,
    "n": 5173,
    "survives_fdr10": true
  },
  "3m/INV/LONG": {
    "expR": -0.124,
    "ci90": [
      -0.543,
      0.267
    ],
    "p_mean_le_0": 0.683,
    "n": 11,
    "survives_fdr10": false
  },
  "3m/INV/SHORT": {
    "expR": 0.455,
    "ci90": [
      0.348,
      0.556
    ],
    "p_mean_le_0": 0.0,
    "n": 8,
    "survives_fdr10": true
  },
  "3m/RETEST/LONG": {
    "expR": 0.087,
    "ci90": [
      0.036,
      0.141
    ],
    "p_mean_le_0": 0.004,
    "n": 1242,
    "survives_fdr10": true
  },
  "3m/RETEST/SHORT": {
    "expR": 0.146,
    "ci90": [
      0.09,
      0.202
    ],
    "p_mean_le_0": 0.001,
    "n": 1133,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.096,
    "ci90": [
      -0.084,
      0.273
    ],
    "p_mean_le_0": 0.195,
    "n": 54,
    "survives_fdr10": false
  },
  "5m/INV/SHORT": {
    "expR": 0.221,
    "ci90": [
      -0.092,
      0.571
    ],
    "p_mean_le_0": 0.137,
    "n": 36,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.1,
    "ci90": [
      0.066,
      0.135
    ],
    "p_mean_le_0": 0.0,
    "n": 3194,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.069,
    "ci90": [
      0.029,
      0.114
    ],
    "p_mean_le_0": 0.003,
    "n": 2316,
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
      "n": 8683,
      "wrTP1": 50.2,
      "expR": 0.048,
      "pf": 1.1,
      "defining_features": {
        "hourNY": 1.34,
        "atrPctUsed": -0.91,
        "emaStack": 0.64,
        "biasScore": 0.61
      }
    },
    {
      "id": 1,
      "n": 19522,
      "wrTP1": 46.7,
      "expR": 0.046,
      "pf": 1.09,
      "defining_features": {
        "biasScore": 0.78,
        "emaStack": 0.66,
        "nearEdge": 0.65,
        "hourNY": -0.49
      }
    },
    {
      "id": 3,
      "n": 6015,
      "wrTP1": 44.4,
      "expR": 0.045,
      "pf": 1.09,
      "defining_features": {
        "stretchAtr": 1.8,
        "rvol": 1.5,
        "chopIdx": -1.38,
        "hourNY": -0.16
      }
    },
    {
      "id": 0,
      "n": 18939,
      "wrTP1": 46.0,
      "expR": 0.037,
      "pf": 1.08,
      "defining_features": {
        "biasScore": -1.09,
        "emaStack": -0.97,
        "nearEdge": -0.84,
        "structDir": -0.46
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
        "n": 52,
        "wrTP1": 48.1,
        "expR": -0.021
      },
      "NQ": {
        "n": 34,
        "wrTP1": 50.0,
        "expR": -0.015
      },
      "GC": {
        "n": 57,
        "wrTP1": 57.9,
        "expR": 0.298
      },
      "CL": {
        "n": 49,
        "wrTP1": 44.9,
        "expR": -0.111
      },
      "YM": {
        "n": 81,
        "wrTP1": 54.3,
        "expR": 0.18
      },
      "ETHUSDT": {
        "n": 61,
        "wrTP1": 54.1,
        "expR": 0.045
      },
      "BTCUSDT": {
        "n": 69,
        "wrTP1": 40.6,
        "expR": -0.102
      }
    },
    "expR_spread": 0.409,
    "verdict": "instrument-specific"
  },
  "15m/RETEST/SHORT": {
    "symbols": {
      "BTCUSDT": {
        "n": 115,
        "wrTP1": 56.5,
        "expR": 0.114
      },
      "ETHUSDT": {
        "n": 84,
        "wrTP1": 47.6,
        "expR": -0.117
      },
      "YM": {
        "n": 47,
        "wrTP1": 55.3,
        "expR": 0.085
      },
      "ES": {
        "n": 40,
        "wrTP1": 55.0,
        "expR": 0.318
      },
      "GC": {
        "n": 44,
        "wrTP1": 59.1,
        "expR": 0.282
      },
      "NQ": {
        "n": 45,
        "wrTP1": 48.9,
        "expR": 0.054
      },
      "CL": {
        "n": 56,
        "wrTP1": 48.2,
        "expR": 0.263
      }
    },
    "expR_spread": 0.435,
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
        "n": 68,
        "wrTP1": 47.1,
        "expR": -0.028
      },
      "YM": {
        "n": 202,
        "wrTP1": 46.5,
        "expR": 0.165
      },
      "ES": {
        "n": 59,
        "wrTP1": 39.0,
        "expR": -0.132
      },
      "NQ": {
        "n": 43,
        "wrTP1": 60.5,
        "expR": 0.257
      }
    },
    "expR_spread": 0.389,
    "verdict": "universal"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "GC": {
        "n": 80,
        "wrTP1": 55.0,
        "expR": 0.165
      },
      "YM": {
        "n": 164,
        "wrTP1": 41.5,
        "expR": 0.091
      },
      "NQ": {
        "n": 40,
        "wrTP1": 57.5,
        "expR": 0.067
      },
      "ES": {
        "n": 26,
        "wrTP1": 50.0,
        "expR": 0.344
      },
      "CL": {
        "n": 43,
        "wrTP1": 34.9,
        "expR": -0.071
      }
    },
    "expR_spread": 0.415,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 2743,
        "wrTP1": 44.1,
        "expR": 0.0
      },
      "NQ": {
        "n": 3048,
        "wrTP1": 44.8,
        "expR": 0.005
      },
      "ES": {
        "n": 3868,
        "wrTP1": 45.0,
        "expR": 0.001
      },
      "CL": {
        "n": 3665,
        "wrTP1": 44.9,
        "expR": 0.033
      },
      "YM": {
        "n": 3996,
        "wrTP1": 45.7,
        "expR": 0.071
      }
    },
    "expR_spread": 0.071,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 1847,
        "wrTP1": 42.1,
        "expR": 0.047
      },
      "GC": {
        "n": 3506,
        "wrTP1": 46.0,
        "expR": 0.039
      },
      "YM": {
        "n": 2904,
        "wrTP1": 44.7,
        "expR": 0.048
      },
      "ES": {
        "n": 2254,
        "wrTP1": 45.7,
        "expR": 0.02
      },
      "CL": {
        "n": 1781,
        "wrTP1": 43.5,
        "expR": -0.041
      }
    },
    "expR_spread": 0.089,
    "verdict": "universal"
  },
  "29m/RETEST/LONG": {
    "symbols": {
      "YM": {
        "n": 37,
        "wrTP1": 54.1,
        "expR": 0.434
      },
      "NQ": {
        "n": 13,
        "wrTP1": 53.8,
        "expR": 0.148
      },
      "ES": {
        "n": 15,
        "wrTP1": 46.7,
        "expR": 0.096
      },
      "CL": {
        "n": 37,
        "wrTP1": 56.8,
        "expR": 0.332
      },
      "BTCUSDT": {
        "n": 34,
        "wrTP1": 52.9,
        "expR": -0.017
      },
      "GC": {
        "n": 20,
        "wrTP1": 60.0,
        "expR": 0.29
      },
      "ETHUSDT": {
        "n": 16,
        "wrTP1": 62.5,
        "expR": 0.134
      }
    },
    "expR_spread": 0.451,
    "verdict": "instrument-specific"
  },
  "29m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 36,
        "wrTP1": 55.6,
        "expR": 0.109
      },
      "CL": {
        "n": 28,
        "wrTP1": 46.4,
        "expR": 0.266
      },
      "YM": {
        "n": 32,
        "wrTP1": 59.4,
        "expR": 0.359
      },
      "NQ": {
        "n": 31,
        "wrTP1": 64.5,
        "expR": 0.482
      },
      "ETHUSDT": {
        "n": 45,
        "wrTP1": 55.6,
        "expR": 0.059
      },
      "GC": {
        "n": 16,
        "wrTP1": 50.0,
        "expR": -0.059
      },
      "BTCUSDT": {
        "n": 53,
        "wrTP1": 50.9,
        "expR": 0.027
      }
    },
    "expR_spread": 0.541,
    "verdict": "instrument-specific"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 23,
        "wrTP1": 43.5,
        "expR": -0.309
      },
      "CL": {
        "n": 21,
        "wrTP1": 61.9,
        "expR": 0.118
      },
      "YM": {
        "n": 64,
        "wrTP1": 40.6,
        "expR": -0.066
      },
      "ES": {
        "n": 29,
        "wrTP1": 69.0,
        "expR": 0.053
      },
      "NQ": {
        "n": 31,
        "wrTP1": 64.5,
        "expR": 0.486
      }
    },
    "expR_spread": 0.795,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 58,
        "wrTP1": 53.4,
        "expR": 0.317
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
        "n": 14,
        "wrTP1": 50.0,
        "expR": -0.132
      },
      "GC": {
        "n": 21,
        "wrTP1": 42.9,
        "expR": -0.23
      }
    },
    "expR_spread": 0.547,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 1484,
        "wrTP1": 46.6,
        "expR": 0.04
      },
      "GC": {
        "n": 1155,
        "wrTP1": 45.8,
        "expR": 0.001
      },
      "CL": {
        "n": 1617,
        "wrTP1": 48.6,
        "expR": 0.049
      },
      "ES": {
        "n": 1680,
        "wrTP1": 46.8,
        "expR": -0.021
      },
      "YM": {
        "n": 1659,
        "wrTP1": 48.3,
        "expR": 0.063
      }
    },
    "expR_spread": 0.084,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 1001,
        "wrTP1": 47.4,
        "expR": 0.011
      },
      "YM": {
        "n": 1204,
        "wrTP1": 48.6,
        "expR": 0.08
      },
      "GC": {
        "n": 1452,
        "wrTP1": 48.8,
        "expR": 0.085
      },
      "NQ": {
        "n": 931,
        "wrTP1": 44.4,
        "expR": 0.049
      },
      "CL": {
        "n": 753,
        "wrTP1": 46.7,
        "expR": -0.009
      }
    },
    "expR_spread": 0.094,
    "verdict": "universal"
  },
  "3m/RETEST/LONG": {
    "symbols": {
      "YM": {
        "n": 293,
        "wrTP1": 54.6,
        "expR": 0.074
      },
      "ES": {
        "n": 271,
        "wrTP1": 50.2,
        "expR": -0.028
      },
      "NQ": {
        "n": 229,
        "wrTP1": 50.2,
        "expR": -0.019
      },
      "CL": {
        "n": 208,
        "wrTP1": 59.1,
        "expR": 0.243
      },
      "GC": {
        "n": 248,
        "wrTP1": 52.0,
        "expR": 0.195
      }
    },
    "expR_spread": 0.271,
    "verdict": "universal"
  },
  "3m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 210,
        "wrTP1": 56.2,
        "expR": 0.14
      },
      "ES": {
        "n": 190,
        "wrTP1": 51.1,
        "expR": 0.013
      },
      "GC": {
        "n": 221,
        "wrTP1": 57.0,
        "expR": 0.238
      },
      "CL": {
        "n": 274,
        "wrTP1": 55.1,
        "expR": 0.086
      },
      "YM": {
        "n": 245,
        "wrTP1": 59.2,
        "expR": 0.238
      }
    },
    "expR_spread": 0.225,
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
    "expR_spread": 0.852,
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
        "n": 4,
        "wrTP1": 75.0,
        "expR": 0.212
      }
    },
    "expR_spread": 1.468,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 387,
        "wrTP1": 51.7,
        "expR": 0.138
      },
      "ES": {
        "n": 560,
        "wrTP1": 50.0,
        "expR": 0.059
      },
      "YM": {
        "n": 593,
        "wrTP1": 50.8,
        "expR": 0.121
      },
      "CL": {
        "n": 574,
        "wrTP1": 54.9,
        "expR": 0.172
      },
      "NQ": {
        "n": 592,
        "wrTP1": 48.1,
        "expR": 0.031
      },
      "BTCUSDT": {
        "n": 314,
        "wrTP1": 51.0,
        "expR": 0.044
      },
      "ETHUSDT": {
        "n": 293,
        "wrTP1": 56.3,
        "expR": 0.144
      }
    },
    "expR_spread": 0.141,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 322,
        "wrTP1": 47.2,
        "expR": 0.032
      },
      "ES": {
        "n": 406,
        "wrTP1": 49.3,
        "expR": 0.151
      },
      "GC": {
        "n": 522,
        "wrTP1": 47.7,
        "expR": 0.027
      },
      "YM": {
        "n": 450,
        "wrTP1": 50.2,
        "expR": 0.145
      },
      "CL": {
        "n": 341,
        "wrTP1": 46.0,
        "expR": 0.02
      },
      "ETHUSDT": {
        "n": 176,
        "wrTP1": 56.8,
        "expR": 0.1
      },
      "BTCUSDT": {
        "n": 212,
        "wrTP1": 48.6,
        "expR": -0.029
      }
    },
    "expR_spread": 0.18,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 21,
  "near_news_30m": {
    "n": 336,
    "wrTP1": 45.2,
    "nSL": 163,
    "nTO": 21,
    "expR": 0.032,
    "pf": 1.06,
    "mfe_p25": 12.5,
    "mfe_p50": 27.0,
    "mfe_p75": 113.5,
    "winnerMAE_p75": 21.5,
    "winnerMAE_p90": 93.90000000000012,
    "loserMFEbeforeSL_p50": 7.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -28.0,
    "revAfterSL_rate": 32.5
  },
  "away_from_news": {
    "n": 52823,
    "wrTP1": 46.8,
    "nSL": 24744,
    "nTO": 3362,
    "expR": 0.043,
    "pf": 1.09,
    "mfe_p25": 8.0,
    "mfe_p50": 20.0,
    "mfe_p75": 45.0,
    "winnerMAE_p75": 14.0,
    "winnerMAE_p90": 32.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 34.7
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 6,
  "mae_deltaER": 0.265,
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
    "hypothesis": "En RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. HASTA 2026-09-04 esto solo certificaba en SHORT (\"no aplica a largos\"); con la muestra de 2026-09-05 TAMBIEN certifica en 1m LONG, asi que se retira la exclusion dura de BUY RETEST y se deja como 'certifica por tf/side, no generalizar sin mirar la tabla'. 2026-09-06: mismas cifras exactas que 2026-09-05 (n identico) porque no llego dato nuevo. 2026-09-07 (lunes, primer dia con trades GENUINAMENTE nuevos post-restauracion, sin repeticion del bug de heal): retest_1m_long paso de n=1087 a n=1135 (+48 pares nuevos, no restaurados) y el delta se mantiene practicamente igual (0.181->0.183) con el CI90 todavia sin cruzar cero -- esta es la primera confirmacion independiente real que pedia el next_steps anterior. retest_1m_short tambien crecio con dato nuevo (n=219->229) y sigue certificando. 2026-09-08 (martes, primer dia habil COMPLETO post-feriado, salto grande de muestra real): retest_1m_long n=1135->1432 (delta 0.183->0.18, estable, segunda confirmacion independiente); retest_1m_short n=229->514 (delta 0.283->0.417, se hizo MAS fuerte); retest_2m_short CERTIFICA POR PRIMERA VEZ (n=129->260, CI90 dejo de cruzar cero); retest_5m_long CERTIFICA POR PRIMERA VEZ pero al filo (n=224->274, CI90=[0.005,0.36], limite inferior casi cero, vigilar que no se revierta con mas muestra); retest_2m_long sigue sin certificar y el delta bajo a casi cero (0.028->0.01, n=596->742). 2026-10-20: hito nuevo -- `since_change` certifica limpio ahora en los 6 de 6 segmentos RETEST del bus (el que faltaba, 5m SHORT, cruzo hoy su CI90 a positivo: [-0.005,0.299] -> [0.004,0.286], n=541->586, limite inferior apenas sobre cero pero real). Documentado en detalle en playbook/buy-retest.md y playbook/sell-retest.md (seccion Gestion). El verdict agregado formal de este experimento sigue en 'flat' por la limitacion de metrica ya conocida (mide con rMultiple, no con rOrig) -- no es evidencia de que el cambio no funcione, es la evidencia real viviendo fuera de ese campo. A evaluar en la revision semanal del domingo (2026-week-43): si corresponde subir la confianza documentada de 'aplicado, parcial' a 'aplicado, 6/6 certifican' y si shadow_rules deberia empezar a razonar sobre rOrig en el segmento del gate (5m LONG). No se decide hoy. 2026-10-31: muestra mucho mayor y delta estable -- retestBar (RETEST 2m/5m) E[R] 0.131 vs 0.036 de 3-capas, delta 0.095 CI90 [0.077,0.114] n=29603; retestBar2 (RETEST 1m SHORT) E[R] 0.063 vs 0.022, delta 0.041 CI90 [0.012,0.069] n=8744. Ambos CI90 siguen sin cruzar cero con n mucho mas grande que en octubre. candle1 (INVERSION) sigue sin certificar (CI90 cruza cero, n=936, bajo volumen). El verdict agregado formal sigue 'flat' por el mismo mismatch de metrica ya documentado (mide rMultiple, no rOrig); la evidencia real sigue viviendo en sl_origin_vs_layer. 2026-11-02: lunes, dato nuevo chico y parejo en todo el bus (+282 pares). retestBar (RETEST 2m/5m/15m/29m) sube a n=29983 (de 29603), E[R] 0.138 vs 0.037 de 3-capas, delta 0.101 CI90=[0.083,0.12] -- delta un poco mas fuerte que el 31-oct (0.095), CI90 sin cruzar cero con una confirmacion mas. retestBar2 (RETEST 1m SHORT) n=8758 (de 8744), E[R] 0.061 vs 0.021, delta 0.041 CI90=[0.012,0.07], practicamente igual a ayer. candle1 (INVERSION) sigue sin certificar (CI90 cruza cero, n=942). Nada cambia la conclusion: sigue siendo el candidato mas fuerte del bus, aun sin aplicarse en Pine.",
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
    "afterN": 33585,
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
      "n": 33585,
      "wrTP1": 47.3,
      "nSL": 15979,
      "nTO": 1735,
      "expR": 0.036,
      "pf": 1.07,
      "mfe_p25": 9.0,
      "mfe_p50": 21.0,
      "mfe_p75": 49.0,
      "winnerMAE_p75": 15.0,
      "winnerMAE_p90": 38.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 36.2
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
    "hypothesis": "No es un experimento propuesto por el agente, es un cambio detectado en el DATO que agent-instructions.md pide registrar como posible cambio de input de Jesus: el campo aligned (que define la causa de SL contra-sesgo) paso de ser casi siempre 1 (aligned=0 en ~0.0-0.1% de las perdidas, W36-W43) a aligned=0 en 20-46% de las senales desde 2026-10-26, visible en TODOS los simbolos (YM 20.9%, GC 23.5%, NQ 29.4%, ES 30.3%, CL 32.1% desde esa fecha), no solo en los simbolos nuevos BTCUSDT/ETHUSDT (42-46%, mas alto pero no categoricamente distinto). El campo ver se mantiene en v4 todo el tiempo, por lo que si hubo un cambio de input no quedo registrado ahi. Contraintuitivo: aligned=0 NO rinde peor -- by_aligned de hoy da aligned=0 E[R]=0.084 PF=1.19 WR=54.3% (n=2471) vs aligned=1 E[R]=0.039 PF=1.08 WR=46.2% (n=45549), es decir el grupo contra-sesgo rinde MEJOR. El salto de causas_pct contra-sesgo a 27% en sl_post_mortem_weekly_trend (W44) es un efecto de que crecio mucho de muestra, no evidencia de que el bias filter se haya roto o deba endurecerse. 2026-10-31: se mantiene el patron contraintuitivo con mas muestra -- by_aligned de hoy: aligned=0 n=2660 E[R]=0.066 PF=1.14 WR=53.3% vs aligned=1 n=46734 E[R]=0.038 PF=1.08 WR=46.3%. El salto de la causa 'contra-sesgo' a 25.4% de las perdidas en sl_post_mortem_weekly_trend W44 (vs 0.0% en W41-43) es, de nuevo, crecimiento de muestra del grupo aligned=0, no un problema nuevo -- ese grupo sigue rindiendo mejor que aligned=1, no peor. Confirmacion repetida, no se toca el filtro de sesgo. 2026-11-01 (REVISION SEMANAL 2026-week-44): CUARTA confirmacion consecutiva del patron contraintuitivo, con mas muestra -- by_aligned de hoy: aligned=0 n=2745 E[R]=0.071 PF=1.16 WR=53.4% vs aligned=1 n=46836 E[R]=0.038 PF=1.08 WR=46.2%. El salto de la causa 'contra-sesgo' en sl_post_mortem_weekly_trend (25.6% en W44) sigue siendo el mismo efecto de muestra ya diagnosticado, no un problema nuevo. Dato adicional de esta revision (sin resolver la pregunta pendiente): la aparicion de BTCUSDT/ETHUSDT y de los TF 3m/15m/29m se confirmo hoy como un cambio real y deliberado de alcance del indicador (no artefacto de dato), con primera aparicion el 2026-10-26/27 en signals/*.jsonl -- coincide con la fecha de este cambio de 'aligned', reforzando la hipotesis de que ambos cambios vinieron juntos en la misma actualizacion de Jesus, pero sigue sin confirmacion directa de el. Sigue pendiente la pregunta a Jesus. 2026-11-03: QUINTA confirmacion consecutiva del patron contraintuitivo, con mas muestra -- by_aligned de hoy: aligned=0 n=3182 E[R]=0.093 PF=1.21 WR=54.1% vs aligned=1 n=48259 E[R]=0.04 PF=1.08 WR=46.3%. Sigue pendiente la pregunta a Jesus sobre el origen del cambio del 2026-10-26; mientras no se confirme, no se toca el filtro de sesgo.",
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
    "date": "2026-11-04",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-11-03T16:30:00-06:00",
    "schema": "sa-plan-2",
    "cleanest": "GC",
    "focus": {
      "sym": "GC",
      "verdict": "GO",
      "window": "17:30-21:00 CT",
      "setup": {
        "es": "A+ barrida+reclamo, barrida del IBL 3933.0 + reclamo en el cluster EMA20/FVG invertido 3932.9-3936.7",
        "en": "A+ sweep+reclaim, IBL 3933.0 sweep + reclaim at the EMA20/inverse-FVG cluster 3932.9-3936.7"
      },
      "trigger": {
        "es": "cierre 5m de vuelta sobre 3934.1 (borde del iFVG) tras barrer el IBL 3933.0",
        "en": "5m close back above 3934.1 (iFVG edge) after sweeping the 3933.0 IBL"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 3929 (bajo el swing 3929.4)",
        "en": "sustained 5m close below 3929 (below the 3929.4 swing)"
      },
      "note": {
        "es": "edge real (confluencia 8, alta conviccion), pero el stop estructural (5.9pts) deja los contratos maximos en 0 bajo tu limite de $1000/3 stops: no fuerces tamano completo, es un patron overtrade-chop si lo haces en micro sin medir.",
        "en": "real edge (confluence 8, high conviction), but the structural stop (5.9pts) leaves max contracts at 0 under your $1000/3-stop limit: don't force full size, that's an overtrade-chop pattern if you do it in micros without measuring."
      }
    },
    "summary": {
      "es": [
        "!! Alarma de precision 45d: sesgo ES 44% (n=94), NQ-direccion 40% (n=34) y GC-rango 36% (n=49) bajo umbral.",
        "NQ: WAIT, squeeze de NY se quedo a 70pts de la invalidacion dura (28513.75) y cerro devolviendo parte; golden zone 28565-28590 confluencia 8 pero precision historica 32% (n=22), no es GO.",
        "ES: WAIT, mismo patron que NQ (squeeze sin romper 7617.25); zona FVG 7619-7624.5 solo B (confluencia 5).",
        "GC: GO, barrida+reclamo en el IBL 3933 + EMA20/FVG invertido, confluencia 8, alta conviccion -- pero tamano maximo 0 contratos al stop mostrado, mide el tamano.",
        "YM: AVOID, conflicto de marcos activo + 2 sesiones sin resolver + estirado 3.07A; el unico setup a tiro seria un LARGO contra el sesgo bajista de fondo (fuga #2 de Jesus).",
        "CL: AVOID, 3er dia de whipsaw por titulares de Iran, conflicto de marcos activo, EIA real recien manana 09:30 CT.",
        "AMD +7% after-hours: riesgo de noticias de NQ ALTA (manos fuera 17:00-17:30 CT), EM NQ +12%; ES/YM MEDIA por contagio.",
        "Semana de NFP (viernes); sin FOMC/CPI hoy. Mas limpio: GC."
      ],
      "en": [
        "!! 45d precision alarm: ES bias 44% (n=94), NQ-direction 40% (n=34) and GC-range 36% (n=49) under threshold.",
        "NQ: WAIT, NY's squeeze stopped 70pts short of the hard invalidation (28513.75) and closed giving part of it back; golden zone 28565-28590 confluence 8 but historical accuracy 32% (n=22), not a GO.",
        "ES: WAIT, same pattern as NQ (squeeze
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 34820,
  "by_verdict": {
    "AVOID": {
      "n": 3122,
      "wrTP1": 44.8,
      "nSL": 1486,
      "nTO": 236,
      "expR": 0.078,
      "pf": 1.16,
      "mfe_p25": 9.0,
      "mfe_p50": 19.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.7
    },
    "GO": {
      "n": 4174,
      "wrTP1": 47.0,
      "nSL": 2007,
      "nTO": 204,
      "expR": -0.016,
      "pf": 0.97,
      "mfe_p25": 7.0,
      "mfe_p50": 16.0,
      "mfe_p75": 35.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 40.1
    },
    "WAIT": {
      "n": 27524,
      "wrTP1": 47.2,
      "nSL": 12968,
      "nTO": 1571,
      "expR": 0.051,
      "pf": 1.11,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 42.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 35.7
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.078,
      "ci90": [
        0.035,
        0.118
      ],
      "p_mean_le_0": 0.0,
      "n": 2983
    },
    "GO": {
      "expR": -0.016,
      "ci90": [
        -0.045,
        0.012
      ],
      "p_mean_le_0": 0.818,
      "n": 4061
    },
    "WAIT": {
      "expR": 0.051,
      "ci90": [
        0.039,
        0.063
      ],
      "p_mean_le_0": 0.0,
      "n": 26809
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 3122,
      "wrTP1": 44.8,
      "nSL": 1486,
      "nTO": 236,
      "expR": 0.078,
      "pf": 1.16,
      "mfe_p25": 9.0,
      "mfe_p50": 19.0,
      "mfe_p75": 39.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.7
    },
    "GO_or_WAIT": {
      "n": 31698,
      "wrTP1": 47.2,
      "nSL": 14975,
      "nTO": 1775,
      "expR": 0.042,
      "pf": 1.09,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 36.3
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.078,
      "ci90": [
        0.035,
        0.118
      ],
      "p_mean_le_0": 0.0,
      "n": 2983
    },
    "GO_or_WAIT": {
      "expR": 0.042,
      "ci90": [
        0.031,
        0.054
      ],
      "p_mean_le_0": 0.0,
      "n": 30870
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 49,
        "wrTP1": 46.9,
        "nSL": 20,
        "nTO": 6,
        "expR": 0.01,
        "pf": 1.02,
        "mfe_p25": 6.25,
        "mfe_p50": 14.5,
        "mfe_p75": 33.25,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 18.6,
        "loserMFEbeforeSL_p50": 6.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 20.0
      },
      "GO": {
        "n": 66,
        "wrTP1": 57.6,
        "nSL": 24,
        "nTO": 4,
        "expR": 0.175,
        "pf": 1.47,
        "mfe_p25": 7.0,
        "mfe_p50": 18.0,
        "mfe_p75": 34.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 39.90000000000001,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -9.0,
        "revAfterSL_rate": 33.3
      },
      "WAIT": {
        "n": 407,
        "wrTP1": 48.9,
        "nSL": 171,
        "nTO": 37,
        "expR": 0.087,
        "pf": 1.2,
        "mfe_p25": 6.0,
        "mfe_p50": 15.0,
        "mfe_p75": 33.0,
        "winnerMAE_p75": 12.5,
        "winnerMAE_p90": 26.200000000000017,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 16.4
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 37,
        "wrTP1": 37.8,
        "nSL": 17,
        "nTO": 6,
        "expR": -0.094,
        "pf": 0.82,
        "mfe_p25": 9.0,
        "mfe_p50": 18.0,
        "mfe_p75": 27.0,
        "winnerMAE_p75": 4.75,
        "winnerMAE_p90": 8.100000000000003,
        "loserMFEbeforeSL_p50": 13.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 11.8
      },
      "GO": {
        "n": 29,
        "wrTP1": 62.1,
        "nSL": 8,
        "nTO": 3,
        "expR": 0.161,
        "pf": 1.58,
        "mfe_p25": 12.0,
        "mfe_p50": 25.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 60.50000000000006,
        "loserMFEbeforeSL_p50": 25.0,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 10.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 12.5
      },
      "WAIT": {
        "n": 303,
        "wrTP1": 48.8,
        "nSL": 120,
        "nTO": 35,
        "expR": 0.122,
        "pf": 1.3,
        "mfe_p25": 8.0,
        "mfe_p50": 24.0,
        "mfe_p75": 50.5,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 29.30000000000001,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 24.2
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 1933,
        "wrTP1": 44.5,
        "nSL": 935,
        "nTO": 137,
        "expR": 0.07,
        "pf": 1.14,
        "mfe_p25": 9.0,
        "mfe_p50": 18.0,
        "mfe_p75": 38.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 32.8
      },
      "GO": {
        "n": 2800,
        "wrTP1": 47.0,
        "nSL": 1357,
        "nTO": 128,
        "expR": -0.014,
        "pf": 0.97,
        "mfe_p25": 6.0,
        "mfe_p50": 15.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 39.1
      },
      "WAIT": {
        "n": 14903,
        "wrTP1": 47.0,
        "nSL": 7110,
        "nTO": 795,
        "expR": 0.045,
        "pf": 1.09,
        "mfe_p25": 7.0,
        "mfe_p50": 16.0,
        "mfe_p75": 38.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 35.8
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 1103,
        "wrTP1": 45.5,
        "nSL": 514,
        "nTO": 87,
        "expR": 0.101,
        "pf": 1.21,
        "mfe_p25": 10.0,
        "mfe_p50": 21.0,
        "mfe_p75": 42.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 39.5
      },
      "GO": {
        "n": 1279,
        "wrTP1": 46.3,
        "nSL": 618,
        "nTO": 69,
        "expR": -0.036,
        "pf": 0.93,
        "mfe_p25": 9.0,
        "mfe_p50": 19.0,
        "mfe_p75": 38.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 42.7
      },
      "WAIT": {
        "n": 11911,
        "wrTP1": 47.4,
        "nSL": 5567,
        "nTO": 704,
        "expR": 0.056,
        "pf": 1.11,
        "mfe_p25": 9.0,
        "mfe_p50": 21.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 31.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 36.4
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
    "n": 50679,
    "wrTP1": 46.6,
    "nSL": 23835,
    "nTO": 3238,
    "expR": 0.04,
    "pf": 1.08,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 44.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 29.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 34.3
  },
  "shadow_ci90": {
    "expR": 0.04,
    "ci90": [
      0.031,
      0.048
    ],
    "p_mean_le_0": 0.0,
    "n": 49082
  },
  "raw_indicator": {
    "n": 51926,
    "wrTP1": 46.7,
    "nSL": 24415,
    "nTO": 3248,
    "expR": 0.042,
    "pf": 1.09,
    "mfe_p25": 9.0,
    "mfe_p50": 20.0,
    "mfe_p75": 46.0,
    "winnerMAE_p75": 14.0,
    "winnerMAE_p90": 32.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -16.0,
    "revAfterSL_rate": 35.0
  },
  "raw_indicator_ci90": {
    "expR": 0.042,
    "ci90": [
      0.033,
      0.05
    ],
    "p_mean_le_0": 0.0,
    "n": 50322
  },
  "tier_ap_b_only": {
    "n": 26058,
    "wrTP1": 44.0,
    "nSL": 12799,
    "nTO": 1800,
    "expR": 0.032,
    "pf": 1.06,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 43.0,
    "winnerMAE_p75": 13.0,
    "winnerMAE_p90": 27.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.7
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.032,
    "ci90": [
      0.019,
      0.045
    ],
    "p_mean_le_0": 0.0,
    "n": 25259
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
    "shadow_n": 2929,
    "shadow_expR": 0.072,
    "raw_n": 3287,
    "raw_expR": 0.092,
    "shadow_beats_raw": false
  }
}
```
