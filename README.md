# scalp-cc-bus

Canal de datos y memoria del **agente de aprendizaje de Scalp CC**. Mismo rol que
`session-analyst-bus` para el Session Analyst.

## Estructura

```
signals/<YYYY-MM-DD>.jsonl    señales al disparo (evt=signal), 1 objeto por linea
outcomes/<YYYY-MM-DD>.jsonl   resoluciones (evt=outcome), emparejables por sigId
playbook/                     conocimiento vivo por tipo de señal (lo edita el agente)
  buy-retest.md  sell-retest.md  buy-ifvg.md  sell-ifvg.md
state.json                    contadores rodantes + parametros recomendados vigentes
reviews/<YYYY>-week-<NN>.md   revision semanal + propuestas de cambio de inputs
```

Lo escribe: `scalp-bus-cron.mjs` (espeja el log de Netlify Blobs aquí) y el propio
agente en cada rutina. Método en `scalp-agent/agent-instructions.md` del repo principal.

## Campos del evento `signal`

`sigId kind side entry zTop zBot zCE sl slTk tp1 tp1Tk tp2 rr1 tier biasScore
strength dir aligned chopIdx chop nearName nearTk nearEdge stretchAtr structDir
atr1m atr5m adr kz inAsia inLon inNy pdh pdl poc vah val do vwap ema20 ema50 ema200`

## Campos del evento `outcome`

`sigId kind side tier result barsToResolve mfeTk maeTk mfeBeforeSLTk rMultiple
exit ambiguous`

`result` ∈ `TP1 | TP2 | SL | TIMEOUT`.
