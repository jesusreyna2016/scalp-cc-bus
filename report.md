# Scalp CC · report 2026-09-02T03:14Z
- signals=304 outcomes=287 pares_resueltos=270 pendientes=34 huerfanos=17

- E[R] global: {"expR": 0.054, "ci90": [-0.056, 0.163], "p_mean_le_0": 0.22, "n": 270}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/SHORT | 8 | 75.0 | 0.316 | 2.27 | 2 | 18.5 | 59.0 | 50.0 |
| 1m/RETEST/LONG | 25 | 48.0 | -0.224 | 0.57 | 13 | 10.0 | 1.25 | 92.3 |
| 1m/RETEST/SHORT | 151 | 49.0 | -0.015 | 0.97 | 70 | 13.0 | 7.75 | 40.0 |
| 2m/RETEST/LONG | 14 | 64.3 | 0.178 | 1.5 | 5 | 11.5 | 13.0 | 100.0 |
| 2m/RETEST/SHORT | 53 | 54.7 | 0.087 | 1.2 | 22 | 10.0 | 9.0 | 45.5 |
| 5m/INV/SHORT | 1 | 100.0 | 0.52 | 99.0 | 0 | 79.0 | 74.0 | None |
| 5m/RETEST/SHORT | 18 | 88.9 | 0.687 | 7.19 | 2 | 46.0 | 44.75 | 100.0 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 16 | 6.2 | -0.743 | 0.21 | 15 | 7.0 | 3.0 | 6.7 |
| B | 87 | 60.9 | 0.162 | 1.45 | 31 | 13.0 | 9.0 | 54.8 |
| C | 167 | 55.7 | 0.074 | 1.18 | 68 | 12.0 | 11.0 | 58.8 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 249 | 53.4 | 0.046 | 1.1 | 108 | 12.0 | 10.0 | 51.9 |
| Sin KZ | 21 | 66.7 | 0.146 | 1.46 | 6 | 20.0 | 20.75 | 33.3 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 63 | 42.9 | -0.193 | 0.64 | 34 | 13.0 | 15.0 | 32.4 |
| edge=0 | 152 | 53.3 | 0.055 | 1.12 | 65 | 11.5 | 10.0 | 61.5 |
| edge=1 | 55 | 70.9 | 0.336 | 2.2 | 15 | 13.0 | 8.0 | 46.7 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 7 | 85.7 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| aligned=1 | 263 | 53.6 | 0.043 | 1.1 | 113 | 12.0 | 10.0 | 51.3 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/SHORT|edge=-1 | 1 | 0.0 | -1.0 | 0.0 | 1 | 5.0 | None | 0.0 |
| INV/SHORT|edge=0 | 8 | 87.5 | 0.506 | 5.05 | 1 | 26.5 | 74.5 | 100.0 |
| RETEST/LONG|edge=-1 | 14 | 57.1 | 0.001 | 1.0 | 6 | 12.5 | 8.75 | 83.3 |
| RETEST/LONG|edge=0 | 19 | 42.1 | -0.296 | 0.49 | 11 | 10.0 | 7.75 | 100.0 |
| RETEST/LONG|edge=1 | 6 | 83.3 | 0.417 | 3.5 | 1 | 10.0 | 3.0 | 100.0 |
| RETEST/SHORT|edge=-1 | 48 | 39.6 | -0.233 | 0.59 | 27 | 15.5 | 17.5 | 22.2 |
| RETEST/SHORT|edge=0 | 125 | 52.8 | 0.079 | 1.18 | 53 | 13.0 | 9.0 | 52.8 |
| RETEST/SHORT|edge=1 | 49 | 69.4 | 0.326 | 2.11 | 14 | 13.0 | 9.0 | 42.9 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/SHORT|tier=B | 1 | 0.0 | -1.0 | 0.0 | 1 | 5.0 | None | 0.0 |
| INV/SHORT|tier=C | 8 | 87.5 | 0.506 | 5.05 | 1 | 26.5 | 74.5 | 100.0 |
| RETEST/LONG|tier=B | 13 | 53.8 | -0.055 | 0.88 | 6 | 11.0 | 3.0 | 100.0 |
| RETEST/LONG|tier=C | 26 | 53.8 | -0.092 | 0.8 | 12 | 10.0 | 11.5 | 91.7 |
| RETEST/SHORT|tier=A+ | 16 | 6.2 | -0.743 | 0.21 | 15 | 7.0 | 3.0 | 6.7 |
| RETEST/SHORT|tier=B | 73 | 63.0 | 0.216 | 1.65 | 24 | 17.0 | 9.0 | 45.8 |
| RETEST/SHORT|tier=C | 133 | 54.1 | 0.081 | 1.19 | 55 | 13.0 | 10.25 | 50.9 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/SHORT|aligned=1 | 9 | 77.8 | 0.339 | 2.52 | 2 | 26.0 | 74.5 | 50.0 |
| RETEST/LONG|aligned=0 | 7 | 85.7 | 0.459 | 4.21 | 1 | 20.0 | 12.25 | 0.0 |
| RETEST/LONG|aligned=1 | 32 | 46.9 | -0.197 | 0.63 | 17 | 10.0 | 3.5 | 100.0 |
| RETEST/SHORT|aligned=1 | 222 | 53.6 | 0.066 | 1.15 | 94 | 13.0 | 10.0 | 42.6 |

## Autopsia de SL
n_losses=114  causas: stop-en-el-minimo×58, RR-bajo×56, contra-estructura×49, sin-nivel-detras×31, chop×22, killzone-Asia-largo×17, sin-causa-clara×15, SL-muy-pegado×11, estirado×6, contra-sesgo×1

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
    "n": 255,
    "naive_expR": 0.049,
    "managed_expR": 0.168,
    "delta": 0.119,
    "avgEntryBetterTk_p50": 2.4,
    "fill_t3plus_pct": 49.8,
    "fill_full_pct": 27.8,
    "m1_rate": 37.3,
    "m2_rate": 20.4,
    "m3_rate": 11.8,
    "beAfterM1_rate": 18.8
  },
  "by_tf_kind_side": {
    "1m/INV/SHORT": {
      "n": 8,
      "naive_expR": 0.316,
      "managed_expR": 0.611,
      "delta": 0.295,
      "avgEntryBetterTk_p50": 4.05,
      "fill_t3plus_pct": 50.0,
      "fill_full_pct": 50.0,
      "m1_rate": 37.5,
      "m2_rate": 37.5,
      "m3_rate": 0.0,
      "beAfterM1_rate": 0.0
    },
    "1m/RETEST/LONG": {
      "n": 21,
      "naive_expR": -0.33,
      "managed_expR": -0.285,
      "delta": 0.045,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 52.4,
      "fill_full_pct": 47.6,
      "m1_rate": 14.3,
      "m2_rate": 4.8,
      "m3_rate": 4.8,
      "beAfterM1_rate": 14.3
    },
    "1m/RETEST/SHORT": {
      "n": 144,
      "naive_expR": -0.004,
      "managed_expR": 0.16,
      "delta": 0.165,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 51.4,
      "fill_full_pct": 23.6,
      "m1_rate": 38.9,
      "m2_rate": 21.5,
      "m3_rate": 13.9,
      "beAfterM1_rate": 20.1
    },
    "2m/RETEST/LONG": {
      "n": 11,
      "naive_expR": 0.056,
      "managed_expR": 0.076,
      "delta": 0.019,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 81.8,
      "fill_full_pct": 63.6,
      "m1_rate": 45.5,
      "m2_rate": 27.3,
      "m3_rate": 18.2,
      "beAfterM1_rate": 18.2
    },
    "2m/RETEST/SHORT": {
      "n": 53,
      "naive_expR": 0.087,
      "managed_expR": 0.072,
      "delta": -0.015,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 39.6,
      "fill_full_pct": 26.4,
      "m1_rate": 32.1,
      "m2_rate": 13.2,
      "m3_rate": 9.4,
      "beAfterM1_rate": 18.9
    },
    "5m/RETEST/SHORT": {
      "n": 17,
      "naive_expR": 0.695,
      "managed_expR": 0.864,
      "delta": 0.169,
      "avgEntryBetterTk_p50": 3.3,
      "fill_t3plus_pct": 41.2,
      "fill_full_pct": 5.9,
      "m1_rate": 64.7,
      "m2_rate": 41.2,
      "m3_rate": 11.8,
      "beAfterM1_rate": 23.5
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 270,
    "wrTP1": 54.4,
    "expR": 0.054
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 261,
  "brier": 0.1984,
  "bias": 0.262,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -0.757
    },
    {
      "feature": "nearEdge",
      "weight": 0.447
    },
    {
      "feature": "chopIdx",
      "weight": -0.367
    },
    {
      "feature": "aligned",
      "weight": -0.33
    },
    {
      "feature": "structDir",
      "weight": 0.224
    },
    {
      "feature": "nearTk",
      "weight": -0.215
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.215
    },
    {
      "feature": "stretchAtr",
      "weight": 0.135
    },
    {
      "feature": "emaStack",
      "weight": -0.135
    },
    {
      "feature": "atrPctUsed",
      "weight": 0.129
    },
    {
      "feature": "rvol",
      "weight": -0.061
    },
    {
      "feature": "biasScore",
      "weight": -0.059
    },
    {
      "feature": "hourNY",
      "weight": -0.01
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.167,
      "actual": 0.231,
      "n": 26
    },
    {
      "bin": 1,
      "pred": 0.292,
      "actual": 0.308,
      "n": 26
    },
    {
      "bin": 2,
      "pred": 0.411,
      "actual": 0.308,
      "n": 26
    },
    {
      "bin": 3,
      "pred": 0.491,
      "actual": 0.5,
      "n": 26
    },
    {
      "bin": 4,
      "pred": 0.552,
      "actual": 0.577,
      "n": 26
    },
    {
      "bin": 5,
      "pred": 0.616,
      "actual": 0.577,
      "n": 26
    },
    {
      "bin": 6,
      "pred": 0.685,
      "actual": 0.654,
      "n": 26
    },
    {
      "bin": 7,
      "pred": 0.744,
      "actual": 0.692,
      "n": 26
    },
    {
      "bin": 8,
      "pred": 0.799,
      "actual": 0.846,
      "n": 26
    },
    {
      "bin": 9,
      "pred": 0.865,
      "actual": 0.926,
      "n": 27
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
  "1m/INV/SHORT": {
    "expR": 0.316,
    "ci90": [
      -0.2,
      0.864
    ],
    "p_mean_le_0": 0.162,
    "n": 8,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": -0.224,
    "ci90": [
      -0.497,
      0.068
    ],
    "p_mean_le_0": 0.904,
    "n": 25,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": -0.015,
    "ci90": [
      -0.158,
      0.127
    ],
    "p_mean_le_0": 0.574,
    "n": 151,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.178,
    "ci90": [
      -0.212,
      0.585
    ],
    "p_mean_le_0": 0.216,
    "n": 14,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.087,
    "ci90": [
      -0.157,
      0.348
    ],
    "p_mean_le_0": 0.281,
    "n": 53,
    "survives_fdr10": false
  },
  "5m/RETEST/SHORT": {
    "expR": 0.687,
    "ci90": [
      0.372,
      1.0
    ],
    "p_mean_le_0": 0.0,
    "n": 18,
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
      "n": 18,
      "wrTP1": 72.2,
      "expR": 0.126,
      "pf": 1.45,
      "defining_features": {
        "entryZoneTk": -2.73,
        "rr1": -0.51,
        "chopIdx": 0.46,
        "biasScore": -0.37
      }
    },
    {
      "id": 0,
      "n": 23,
      "wrTP1": 52.2,
      "expR": 0.123,
      "pf": 1.31,
      "defining_features": {
        "nearTk": 2.83,
        "hourNY": 1.01,
        "nearEdge": -0.75,
        "structDir": 0.66
      }
    },
    {
      "id": 1,
      "n": 109,
      "wrTP1": 59.6,
      "expR": 0.101,
      "pf": 1.27,
      "defining_features": {
        "emaStack": 0.77,
        "biasScore": 0.63,
        "hourNY": -0.6,
        "nearEdge": 0.48
      }
    },
    {
      "id": 3,
      "n": 120,
      "wrTP1": 47.5,
      "expR": -0.012,
      "pf": 0.98,
      "defining_features": {
        "emaStack": -0.6,
        "structDir": -0.47,
        "biasScore": -0.42,
        "hourNY": 0.38
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
        "n": 25,
        "wrTP1": 48.0,
        "expR": -0.026
      },
      "GC": {
        "n": 42,
        "wrTP1": 47.6,
        "expR": -0.099
      },
      "YM": {
        "n": 48,
        "wrTP1": 52.1,
        "expR": 0.143
      },
      "ES": {
        "n": 36,
        "wrTP1": 47.2,
        "expR": -0.122
      }
    },
    "expR_spread": 0.265,
    "verdict": "universal"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 3,
        "wrTP1": 100.0,
        "expR": 0.623
      },
      "CL": {
        "n": 11,
        "wrTP1": 54.5,
        "expR": 0.056
      }
    },
    "expR_spread": 0.567,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 16,
        "wrTP1": 43.8,
        "expR": -0.03
      },
      "YM": {
        "n": 22,
        "wrTP1": 54.5,
        "expR": 0.195
      },
      "GC": {
        "n": 9,
        "wrTP1": 77.8,
        "expR": 0.201
      },
      "NQ": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.168
      }
    },
    "expR_spread": 0.369,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 10,
        "wrTP1": 90.0,
        "expR": 0.487
      },
      "ES": {
        "n": 6,
        "wrTP1": 83.3,
        "expR": 0.922
      }
    },
    "expR_spread": 0.435,
    "verdict": "instrument-specific"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 15,
  "near_news_30m": {
    "n": 107,
    "wrTP1": 51.4,
    "nSL": 52,
    "nTO": 0,
    "expR": -0.002,
    "pf": 1.0,
    "mfe_p25": 5.0,
    "mfe_p50": 11.0,
    "mfe_p75": 25.5,
    "winnerMAE_p75": 8.5,
    "winnerMAE_p90": 20.200000000000003,
    "loserMFEbeforeSL_p50": 2.5,
    "bars_win_p50": 4.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -8.0,
    "revAfterSL_rate": 36.5
  },
  "away_from_news": {
    "n": 163,
    "wrTP1": 56.4,
    "nSL": 62,
    "nTO": 9,
    "expR": 0.091,
    "pf": 1.23,
    "mfe_p25": 8.0,
    "mfe_p50": 13.0,
    "mfe_p75": 28.0,
    "winnerMAE_p75": 11.25,
    "winnerMAE_p90": 30.600000000000023,
    "loserMFEbeforeSL_p50": 2.0,
    "bars_win_p50": 2.0,
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
