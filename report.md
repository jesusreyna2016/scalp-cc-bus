# Scalp CC · report 2026-09-01T20:56Z
- signals=18 outcomes=12 pares_resueltos=11 pendientes=7 huerfanos=1

- E[R] global: {"expR": -0.001, "ci90": [-0.444, 0.423], "p_mean_le_0": 0.513, "n": 11}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/RETEST/LONG | 4 | 75.0 | 0.335 | 2.34 | 1 | 15.5 | 4.0 | 0.0 |
| 1m/RETEST/SHORT | 5 | 20.0 | -0.532 | 0.26 | 3 | 13.0 | 6.0 | 0.0 |
| 2m/RETEST/LONG | 2 | 100.0 | 0.655 | 99.0 | 0 | 70.0 | 29.0 | None |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| B | 2 | 50.0 | -0.025 | 0.95 | 1 | 11.0 | 6.0 | 0.0 |
| C | 9 | 55.6 | 0.004 | 1.01 | 3 | 20.0 | 14.0 | 0.0 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Sin KZ | 11 | 54.5 | -0.001 | 1.0 | 4 | 17.0 | 12.25 | 0.0 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 7 | 71.4 | 0.236 | 1.82 | 2 | 17.0 | 14.0 | 0.0 |
| edge=0 | 3 | 0.0 | -0.87 | 0.0 | 2 | 22.0 | None | 0.0 |
| edge=1 | 1 | 100.0 | 0.95 | 99.0 | 0 | 13.0 | 6.0 | None |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 6 | 83.3 | 0.442 | 3.65 | 1 | 18.5 | 14.0 | 0.0 |
| aligned=1 | 5 | 20.0 | -0.532 | 0.26 | 3 | 13.0 | 6.0 | 0.0 |

## Autopsia de SL
n_losses=4  causas: RR-bajo×2, chop×1, sin-causa-clara×1, contra-sesgo×1

## Contrafactual de gestion
```json
{
  "n": 0,
  "note": "sin outcomes v3 todavia (curva/flags nuevos)"
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 11,
    "wrTP1": 54.5,
    "expR": -0.001
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": false,
  "n": 10,
  "need": 120
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": false,
  "n": 11,
  "need": 60
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{}
```

## Clusters de regimen
```json
{
  "ready": false,
  "n": 11,
  "need": 60
}
```

## Consistencia entre instrumentos
```json
{}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 16,
  "near_news_30m": {
    "n": 0
  },
  "away_from_news": {
    "n": 11,
    "wrTP1": 54.5,
    "nSL": 4,
    "nTO": 1,
    "expR": -0.001,
    "pf": 1.0,
    "mfe_p25": 11.0,
    "mfe_p50": 17.0,
    "mfe_p75": 25.5,
    "winnerMAE_p75": 12.25,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 7.0,
    "bars_win_p50": 0.5,
    "bars_loss_p50": 6.5,
    "entryZoneTk_p50": null,
    "revAfterSL_rate": 0.0
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
    "date": "2026-09-01",
    "session": "ny",
    "runType": "pre-ny",
    "generatedAt": "2026-09-01T08:20:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "GC",
    "focus": {
      "sym": "GC",
      "verdict": "WAIT",
      "window": "09:15-11:30 CT",
      "setup": {
        "es": "posible pullback a la zona 4402-4423 (POC/EMA20/EMA50/eq/golden) para reanudar el corto de tendencia",
        "en": "possible pullback into the 4402-4423 zone (POC/EMA20/EMA50/eq/golden) to resume the trend short"
      },
      "trigger": {
        "es": "rebote con cierre 5m dentro de 4402-4423 y rechazo (mecha superior o CHoCH bajista) de vuelta abajo; evita el ISM 08:45-09:10",
        "en": "a bounce with a 5m close inside 4402-4423 and a rejection (upper wick or bearish CHoCH) back down; avoid the 08:45-09:10 ISM window"
      },
      "invalid": {
        "es": "cierre 5m sostenido sobre 4423 mata el rebote corto; aceptación sobre 4521.50 mata la tesis bajista de fondo",
        "en": "a sustained 5m close above 4423 kills the short bounce; acceptance above 4521.50 kills the underlying bearish thesis"
      },
      "note": {
        "es": "el día ya gastó su presupuesto (130% del ATR), no persigas el corto aquí abajo; espera el rebote y el rechazo confirmado, no lo anticipes",
        "en": "the day already spent its budget (130% of ATR), don't chase the short down here; wait for the bounce and the confirmed rejection, don't front-run it"
      }
    },
    "summary": {
      "es": [
        "!! NQ: la tesis alcista de 1 día se rompió esta corrida (cierre muy bajo la invalidación 29352.50), narrativa reescrita a bajista",
        "datos OK, snapshot <1 min",
        "NQ: corto, AVOID (estirado 11.7A, no perseguir), espera rebote a 29142-29220 para vender",
        "ES: corto, AVOID (estirado 6.9A, rompió VAL/IBL/mínimo semanal sin rebote), espera rebote a 7649-7677",
        "GC: corto, AVOID (estirado 7.2A, 130% del ATR usado), espera rebote a 4402-4423 -- la lectura más limpia de los tres",
        "más limpio: GC (ALIGN sin conflictos internos, guion bajista cumplido 3 veces)",
        "ISM Manufacturing PMI 09:00 CT (+ISM Prices/JOLTS) = riesgo de noticias ALTA, manos fuera 08:45-09:10 CT en los tres",
        "límite $1000/día ⇒ 0 contratos full en las 3 A+ mapeadas (stops de $375-1300); solo micros o pasa el día",
        "recordatorio anti-fuga: si ya estás dentro de un corto, no promedies ni subas tamaño con el estiramiento actual; y no compres el rebote contra el sesgo dominante"
      ],
      "en": [
        "!! NQ: the 1-day bullish thesis broke this run (close far below the 29352.50 invalidation), narrative rewritten bearish",
        "data OK, snapshot <1 min old",
        "NQ: short, AVOID (stretched 11.7A, don't chase), wait for a bounce to 29142-29220 to sell",
        "ES: short, AVOID (stretched 6.9A, broke VAL/IBL/weekly low with no bounce), wait for a bounce to 7649-7677",
        "GC: s
```
