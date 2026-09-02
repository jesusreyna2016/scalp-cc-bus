# Scalp CC · report 2026-09-02T01:21Z
- signals=178 outcomes=172 pares_resueltos=158 pendientes=20 huerfanos=14

## ⚠ ALERTAS (llevar al frente del resumen)
- ORFANOS: 14 outcomes sin señal. Revisar pipeline Pine/ingest.

- E[R] global: {"expR": 0.015, "ci90": [-0.107, 0.145], "p_mean_le_0": 0.416, "n": 158}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/SHORT | 3 | 66.7 | -0.07 | 0.79 | 1 | 10.0 | 3.75 | 100.0 |
| 1m/RETEST/LONG | 18 | 44.4 | -0.283 | 0.49 | 10 | 9.0 | 1.25 | 90.0 |
| 1m/RETEST/SHORT | 85 | 51.8 | 0.046 | 1.11 | 34 | 14.0 | 9.0 | 50.0 |
| 2m/RETEST/LONG | 13 | 61.5 | 0.159 | 1.41 | 5 | 12.0 | 13.25 | 100.0 |
| 2m/RETEST/SHORT | 28 | 57.1 | -0.046 | 0.88 | 10 | 11.0 | 12.25 | 50.0 |
| 5m/INV/SHORT | 1 | 100.0 | 0.52 | 99.0 | 0 | 79.0 | 74.0 | None |
| 5m/RETEST/SHORT | 10 | 80.0 | 0.245 | 2.23 | 2 | 36.0 | 85.0 | 100.0 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 3 | 33.3 | 0.37 | 1.55 | 2 | 13.0 | 3.0 | 0.0 |
| B | 62 | 62.9 | 0.222 | 1.67 | 20 | 14.0 | 9.0 | 65.0 |
| C | 93 | 50.5 | -0.135 | 0.7 | 40 | 11.0 | 13.5 | 65.0 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 137 | 53.3 | -0.005 | 0.99 | 56 | 12.0 | 9.0 | 66.1 |
| Sin KZ | 21 | 66.7 | 0.146 | 1.46 | 6 | 20.0 | 20.75 | 33.3 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 26 | 50.0 | -0.008 | 0.98 | 11 | 17.0 | 14.0 | 63.6 |
| edge=0 | 81 | 46.9 | -0.183 | 0.62 | 37 | 11.0 | 12.75 | 70.3 |
| edge=1 | 51 | 70.6 | 0.342 | 2.21 | 14 | 13.0 | 9.0 | 42.9 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 7 | 85.7 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| aligned=1 | 151 | 53.6 | -0.006 | 0.99 | 61 | 12.0 | 10.0 | 63.9 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/SHORT|edge=0 | 4 | 75.0 | 0.077 | 1.31 | 1 | 10.5 | 39.5 | 100.0 |
| RETEST/LONG|edge=-1 | 13 | 61.5 | 0.078 | 1.2 | 5 | 12.0 | 8.75 | 80.0 |
| RETEST/LONG|edge=0 | 16 | 37.5 | -0.345 | 0.45 | 10 | 10.0 | 5.0 | 100.0 |
| RETEST/LONG|edge=1 | 2 | 100.0 | 0.74 | 99.0 | 0 | 22.5 | 2.5 | None |
| RETEST/SHORT|edge=-1 | 13 | 38.5 | -0.095 | 0.79 | 6 | 26.0 | 23.0 | 50.0 |
| RETEST/SHORT|edge=0 | 61 | 47.5 | -0.158 | 0.66 | 26 | 13.0 | 20.0 | 57.7 |
| RETEST/SHORT|edge=1 | 49 | 69.4 | 0.326 | 2.11 | 14 | 13.0 | 9.0 | 42.9 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/SHORT|aligned=1 | 4 | 75.0 | 0.077 | 1.31 | 1 | 10.5 | 39.5 | 100.0 |
| RETEST/LONG|aligned=0 | 7 | 85.7 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| RETEST/LONG|aligned=1 | 24 | 41.7 | -0.26 | 0.56 | 14 | 10.0 | 3.0 | 100.0 |
| RETEST/SHORT|aligned=1 | 123 | 55.3 | 0.041 | 1.1 | 46 | 14.0 | 12.25 | 52.2 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/SHORT|tier=C | 4 | 75.0 | 0.077 | 1.31 | 1 | 10.5 | 39.5 | 100.0 |
| RETEST/LONG|tier=B | 8 | 50.0 | -0.091 | 0.82 | 4 | 11.0 | 3.0 | 100.0 |
| RETEST/LONG|tier=C | 23 | 52.2 | -0.1 | 0.79 | 11 | 10.0 | 8.5 | 90.9 |
| RETEST/SHORT|tier=A+ | 3 | 33.3 | 0.37 | 1.55 | 2 | 13.0 | 3.0 | 0.0 |
| RETEST/SHORT|tier=B | 54 | 64.8 | 0.269 | 1.88 | 16 | 17.5 | 9.0 | 56.2 |
| RETEST/SHORT|tier=C | 66 | 48.5 | -0.16 | 0.65 | 28 | 13.0 | 20.0 | 53.6 |

## Autopsia de SL
n_losses=62  causas: RR-bajo×39, stop-en-el-minimo×39, contra-estructura×27, chop×18, sin-nivel-detras×17, killzone-Asia-largo×14, sin-causa-clara×8, estirado×2, SL-muy-pegado×2, contra-sesgo×1

## Contrafactual de gestion
```json
{
  "n": 8,
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
    0.316,
    8
  ],
  "altSL_1_5x_struct": [
    0.293,
    8
  ],
  "note": "fixed_XR: R esperado si el objetivo fuera XR fijo con SL=struct. altSL: SL a mult del SL struct."
}
```

## Modelo GESTIONADO (escalera + parciales) vs INGENUO
```json
{
  "overall": {
    "n": 143,
    "naive_expR": 0.002,
    "managed_expR": 0.076,
    "delta": 0.074,
    "avgEntryBetterTk_p50": 2.8,
    "fill_t3plus_pct": 51.7,
    "fill_full_pct": 30.8,
    "m1_rate": 31.5,
    "m2_rate": 14.0,
    "m3_rate": 9.1,
    "beAfterM1_rate": 18.9
  },
  "by_tf_kind_side": {
    "1m/INV/SHORT": {
      "n": 3,
      "naive_expR": -0.07,
      "managed_expR": 0.109,
      "delta": 0.179,
      "avgEntryBetterTk_p50": 2.5,
      "fill_t3plus_pct": 33.3,
      "fill_full_pct": 33.3,
      "m1_rate": 0.0,
      "m2_rate": 0.0,
      "m3_rate": 0.0,
      "beAfterM1_rate": 0.0
    },
    "1m/RETEST/LONG": {
      "n": 14,
      "naive_expR": -0.459,
      "managed_expR": -0.358,
      "delta": 0.102,
      "avgEntryBetterTk_p50": 2.0,
      "fill_t3plus_pct": 57.1,
      "fill_full_pct": 50.0,
      "m1_rate": 14.3,
      "m2_rate": 7.1,
      "m3_rate": 7.1,
      "beAfterM1_rate": 14.3
    },
    "1m/RETEST/SHORT": {
      "n": 78,
      "naive_expR": 0.072,
      "managed_expR": 0.112,
      "delta": 0.04,
      "avgEntryBetterTk_p50": 3.45,
      "fill_t3plus_pct": 51.3,
      "fill_full_pct": 26.9,
      "m1_rate": 35.9,
      "m2_rate": 17.9,
      "m3_rate": 11.5,
      "beAfterM1_rate": 19.2
    },
    "2m/RETEST/LONG": {
      "n": 10,
      "naive_expR": 0.02,
      "managed_expR": 0.1,
      "delta": 0.08,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 80.0,
      "fill_full_pct": 70.0,
      "m1_rate": 50.0,
      "m2_rate": 30.0,
      "m3_rate": 20.0,
      "beAfterM1_rate": 20.0
    },
    "2m/RETEST/SHORT": {
      "n": 28,
      "naive_expR": -0.046,
      "managed_expR": -0.011,
      "delta": 0.035,
      "avgEntryBetterTk_p50": 3.8499999999999996,
      "fill_t3plus_pct": 42.9,
      "fill_full_pct": 21.4,
      "m1_rate": 21.4,
      "m2_rate": 3.6,
      "m3_rate": 3.6,
      "beAfterM1_rate": 17.9
    },
    "5m/RETEST/SHORT": {
      "n": 9,
      "naive_expR": 0.211,
      "managed_expR": 0.515,
      "delta": 0.304,
      "avgEntryBetterTk_p50": 2.6,
      "fill_t3plus_pct": 44.4,
      "fill_full_pct": 11.1,
      "m1_rate": 44.4,
      "m2_rate": 11.1,
      "m3_rate": 0.0,
      "beAfterM1_rate": 33.3
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 158,
    "wrTP1": 55.1,
    "expR": 0.015
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 149,
  "brier": 0.1715,
  "bias": 0.382,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -0.889
    },
    {
      "feature": "nearEdge",
      "weight": 0.476
    },
    {
      "feature": "aligned",
      "weight": -0.459
    },
    {
      "feature": "structDir",
      "weight": 0.453
    },
    {
      "feature": "nearTk",
      "weight": -0.396
    },
    {
      "feature": "chopIdx",
      "weight": -0.393
    },
    {
      "feature": "emaStack",
      "weight": -0.247
    },
    {
      "feature": "stretchAtr",
      "weight": 0.228
    },
    {
      "feature": "biasScore",
      "weight": -0.134
    },
    {
      "feature": "atrPctUsed",
      "weight": 0.107
    },
    {
      "feature": "hourNY",
      "weight": 0.099
    },
    {
      "feature": "rvol",
      "weight": -0.019
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.008
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.097,
      "actual": 0.143,
      "n": 14
    },
    {
      "bin": 1,
      "pred": 0.227,
      "actual": 0.267,
      "n": 15
    },
    {
      "bin": 2,
      "pred": 0.408,
      "actual": 0.267,
      "n": 15
    },
    {
      "bin": 3,
      "pred": 0.502,
      "actual": 0.4,
      "n": 15
    },
    {
      "bin": 4,
      "pred": 0.592,
      "actual": 0.6,
      "n": 15
    },
    {
      "bin": 5,
      "pred": 0.654,
      "actual": 0.733,
      "n": 15
    },
    {
      "bin": 6,
      "pred": 0.744,
      "actual": 0.8,
      "n": 15
    },
    {
      "bin": 7,
      "pred": 0.814,
      "actual": 0.867,
      "n": 15
    },
    {
      "bin": 8,
      "pred": 0.851,
      "actual": 0.8,
      "n": 15
    },
    {
      "bin": 9,
      "pred": 0.921,
      "actual": 0.933,
      "n": 15
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
  "weeks": 1
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/RETEST/LONG": {
    "expR": -0.283,
    "ci90": [
      -0.606,
      0.043
    ],
    "p_mean_le_0": 0.921,
    "n": 18,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.046,
    "ci90": [
      -0.131,
      0.236
    ],
    "p_mean_le_0": 0.353,
    "n": 85,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.159,
    "ci90": [
      -0.28,
      0.602
    ],
    "p_mean_le_0": 0.246,
    "n": 13,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": -0.046,
    "ci90": [
      -0.276,
      0.192
    ],
    "p_mean_le_0": 0.622,
    "n": 28,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": 0.245,
    "ci90": [
      -0.128,
      0.602
    ],
    "p_mean_le_0": 0.137,
    "n": 10,
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
      "id": 3,
      "n": 51,
      "wrTP1": 68.6,
      "expR": 0.277,
      "pf": 2.17,
      "defining_features": {
        "structDir": 0.73,
        "stretchAtr": 0.68,
        "hourNY": -0.58,
        "nearEdge": 0.52
      }
    },
    {
      "id": 1,
      "n": 29,
      "wrTP1": 55.2,
      "expR": -0.027,
      "pf": 0.93,
      "defining_features": {
        "entryZoneTk": -1.19,
        "nearTk": 0.88,
        "emaStack": -0.65,
        "chopIdx": 0.47
      }
    },
    {
      "id": 2,
      "n": 49,
      "wrTP1": 46.9,
      "expR": -0.088,
      "pf": 0.83,
      "defining_features": {
        "structDir": -0.78,
        "hourNY": 0.65,
        "biasScore": -0.58,
        "emaStack": -0.58
      }
    },
    {
      "id": 0,
      "n": 29,
      "wrTP1": 44.8,
      "expR": -0.231,
      "pf": 0.58,
      "defining_features": {
        "biasScore": 1.79,
        "emaStack": 0.91,
        "nearEdge": -0.64,
        "entryZoneTk": 0.56
      }
    }
  ]
}
```

## Consistencia entre instrumentos
```json
{
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 14,
        "wrTP1": 50.0,
        "expR": 0.063
      },
      "GC": {
        "n": 34,
        "wrTP1": 50.0,
        "expR": -0.038
      },
      "YM": {
        "n": 27,
        "wrTP1": 59.3,
        "expR": 0.307
      },
      "ES": {
        "n": 10,
        "wrTP1": 40.0,
        "expR": -0.398
      }
    },
    "expR_spread": 0.705,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 3,
        "wrTP1": 100.0,
        "expR": 0.623
      },
      "CL": {
        "n": 10,
        "wrTP1": 50.0,
        "expR": 0.02
      }
    },
    "expR_spread": 0.603,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 5,
        "wrTP1": 40.0,
        "expR": -0.22
      },
      "YM": {
        "n": 11,
        "wrTP1": 54.5,
        "expR": -0.026
      },
      "GC": {
        "n": 8,
        "wrTP1": 75.0,
        "expR": 0.154
      },
      "NQ": {
        "n": 4,
        "wrTP1": 50.0,
        "expR": -0.28
      }
    },
    "expR_spread": 0.434,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 7,
        "wrTP1": 85.7,
        "expR": 0.321
      },
      "ES": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.067
      }
    },
    "expR_spread": 0.254,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 15,
  "near_news_30m": {
    "n": 1,
    "wrTP1": 100.0,
    "nSL": 0,
    "nTO": 0,
    "expR": 0.62,
    "pf": 99.0,
    "mfe_p25": 5.0,
    "mfe_p50": 5.0,
    "mfe_p75": 5.0,
    "winnerMAE_p75": 0.0,
    "winnerMAE_p90": 0.0,
    "loserMFEbeforeSL_p50": null,
    "bars_win_p50": 1.0,
    "bars_loss_p50": null,
    "entryZoneTk_p50": -3.0,
    "revAfterSL_rate": null
  },
  "away_from_news": {
    "n": 157,
    "wrTP1": 54.8,
    "nSL": 62,
    "nTO": 9,
    "expR": 0.011,
    "pf": 1.03,
    "mfe_p25": 8.0,
    "mfe_p50": 13.0,
    "mfe_p75": 27.0,
    "winnerMAE_p75": 11.5,
    "winnerMAE_p90": 29.0,
    "loserMFEbeforeSL_p50": 2.0,
    "bars_win_p50": 1.0,
    "bars_loss_p50": 3.5,
    "entryZoneTk_p50": -10.0,
    "revAfterSL_rate": 62.9
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 0,
  "note": "sin predictions.jsonl todavia"
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
  }
]
```

## Session Analyst
```json
{
  "available": true,
  "latest_plan": {
    "date": "2026-09-02",
    "session": "asia",
    "runType": "pre-asia",
    "generatedAt": "2026-09-01T16:20:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "GC",
    "focus": {
      "sym": "GC",
      "verdict": "WAIT",
      "window": "17:00-21:00 CT",
      "setup": {
        "es": "pullback a POC/EMA50/VWAP/IB/zona dorada 4383-4424 para vender de nuevo",
        "en": "pullback into the POC/EMA50/VWAP/IB/golden-zone cluster 4383-4424 to sell again"
      },
      "trigger": {
        "es": "cierre 5m dentro de 4383-4424 con rechazo (mecha superior o CHoCH bajista); evita RBNZ 21:00-22:15 CT",
        "en": "5m close inside 4383-4424 with a rejection (upper wick or bearish CHoCH); avoid the 21:00-22:15 CT RBNZ window"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 4424 mata el rebote corto; aceptacion sobre 4510.50 mata la tesis bajista de fondo",
        "en": "a sustained 5m close above 4424 kills the short bounce; acceptance above 4510.50 kills the underlying bearish thesis"
      },
      "note": {
        "es": "la lectura mas limpia de las tres por tercer dia seguido; no lo anticipes, espera el rechazo confirmado, no el toque",
        "en": "the cleanest read of the three for a third day running; don't front-run it, wait for the confirmed rejection, not just the touch"
      }
    },
    "summary": {
      "es": [
        "Corrida antes de la reapertura (16:20 CT, mercado en pausa hasta 17:00) -- niveles de hoy ya cerrados, sin gap medido aun, se confirma en pre-london.",
        "NQ: tesis bajista dia 2 confirmada, cierre en tercio bajo de un rango de 569pts -- WAIT, espera el pullback a 29125-29222 para vender, full contract intocable con el limite diario.",
        "ES: el conflicto de dos dias se resolvio bajista esta noche -- WAIT, pullback a 29659-7667 (EMA200/VAH/IBH), tambien intocable en full.",
        "GC: tercer rechazo confirmado seguido, la lectura mas limpia -- WAIT, pullback a 4383-4424, intocable en full tambien.",
        "Los 3 stops estructurales superan el limite diario de $1000 en full contract; solo micros (/10) tienen sentido esta noche.",
        "RBNZ (OCR + conferencia) 21:00-22:15 CT y PIB de Australia 20:30 CT caen en Asia -- no son USD directo pero ensanchan el no-trade por precaucion.",
        "mas limpio: GC."
      ],
      "en": [
        "This run happened before the 17:00 CT reopen (market halted) -- today's levels already closed, no gap measured yet, confirmed at pre-london.",
        "NQ: day-2 bearish thesis confirmed, closed in the lower third of a 569pt range -- WAIT, wait for the 29125-29222 pullback to sell, full contract untouchable under the daily limit.",
        "ES: the two-day conflict resolved bearish tonight -- WAIT, pullback to 7659-7667 (EMA200/VAH/IBH), also untouchable in full size.",
        "GC: third confirmed rejection in a row, the cleanest read -- WAIT, pullback to 4383-4424, also untouchable in full s
```
