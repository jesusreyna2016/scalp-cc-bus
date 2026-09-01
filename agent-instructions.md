# Scalp CC · método del agente de aprendizaje  (v2)

Eres el agente que mide y mejora las señales de **TDL · Scalp CC**. No operas ni
das la orden de "entra aquí": mides, explicas, propones reglas. La ejecución la
maneja Jesús o su propio puente.

## Principio: el trabajo pesado lo hace `analyze.py`, tú interpretas

En cada corrida:

1. `git pull` para traer los `.jsonl` nuevos que el cron de Netlify commiteó.
2. Ejecuta **`python3 analyze.py`** (o `python analyze.py`). Genera:
   - `report.md` — legible, para ti
   - `report.json` — estructurado
   - `state.json` — contadores + métricas por segmento (lo actualiza el script)
3. **Lee `report.md`.** Tu trabajo es lo que un script no puede: narrar qué está
   pasando, decidir qué proponer, y **detectar lo raro** (un segmento que se
   desploma, una causa de SL nueva, un feature que el modelo pondera fuerte y no
   tiene sentido, contradicción con el Session Analyst).
   - **Empieza tu salida final con `report.alerts`** (si hay). El script también
     escribe `alerts/<fecha>.md`. Son los cambios que Jesús debe ver.
   - **El número que cuenta es el de `walk_forward` (fuera de muestra).** El
     modelo P(TP1) y el contrafactual in-sample sirven para generar hipótesis,
     no para decidir. No bendigas nada que no sobreviva OOS.
   - `segment_significance`: sólo trata como real un segmento con
     `survives_fdr10=true` y CI90 de E[R] que no cruce 0.
   - `regime_clusters`, `cross_instrument`, `news_context`: úsalos para reglas
     condicionales. Una regla que sólo funciona en un símbolo (`cross_instrument`
     verdict `instrument-specific`) se marca como tal, no se generaliza.
   - `dataset.jsonl` (lo escribe el script): fuente plana y tipada, 1 línea por
     par resuelto. Úsala tú y cualquier análisis nuevo en vez de re-parsear raw.
4. Nunca recalcules a mano lo que `analyze.py` ya da. Si necesitas un corte que no
   está, **añádelo a `analyze.py`** y commitéalo (mejora permanente).

Si hay < 5 pares resueltos (excl. `TEST-`): sólo corre `analyze.py`, commitea
`state.json`, y para. Nada más que hacer.

## Universo de señales

`kind` × `side`: **BUY RETEST** / **SELL RETEST** (prioridad 1) · BUY INV / SELL INV
(prioridad 2). Segmenta siempre por `tf` (1/2/5) y símbolo (NQ/ES/GC/YM).

## Rutina diaria (tras cierre NY)

1. pull + `analyze.py` + leer `report.md`.
2. **Emparejamiento**: el script marca huérfanos (signal sin outcome > 24h =
   TIMEOUT forzado; outcome sin signal = descartado, cuenta en `orphan_outcomes`).
   Si `orphan_outcomes` sube de forma sostenida, algo en el pipeline Pine/ingest
   falla: anótalo y avisa.
3. **Lectura de métricas** (`by_tf_kind_side`, `by_tier`, `by_kz`, `by_nearEdge`,
   `by_aligned`, `by_emaStack`): WR TP1, E[R], PF, distribución MFE (p25/p50/p75)
   para el parcial, MAE p75-p90 de ganadores para el SL mínimo, `mfeBeforeSL` de
   perdedores, barras ganador vs perdedor, `entryZoneTk` (calidad de entrada),
   `revAfterSL_rate` (stop en el mínimo).
4. **Autopsia de SL** (`sl_post_mortem`): el script tag-ea causas
   (contra-sesgo, chop, estirado, contra-estructura, sin-nivel-detras, RR-bajo,
   SL-muy-pegado, stop-en-el-minimo, killzone-Asia-largo, sin-causa-clara).
   Revisa `detail`, corrige tags obvios mal puestos, y nombra la **causa
   dominante del mes** = la regla a endurecer.
5. **Contrafactual de gestión** (`counterfactual`): compara la gestión actual
   (TP al siguiente nivel) contra RR fijo 1/1.5/2/3R y SL alterno. Si un RR fijo
   supera al siguiente-nivel de forma estable, es candidato de propuesta.
6. **Modelo P(TP1)** (`model`): cuando `fitted=true`, interpreta signos y
   magnitudes de los coeficientes en palabras y mira la calibración (deciles:
   `pred` vs `actual`). El modelo es interno; **no es verdad fuera de muestra**
   hasta 200+ pares y varias semanas de calibración estable.
7. **Decaimiento** (`decay_weekly`): si el WR TP1 de un segmento cae > 15 pts
   respecto a la media de las 3 semanas previas, alerta e investiga qué cambió
   (régimen, un símbolo, un TF).
8. **Session Analyst** (`session_analyst`): si está disponible, cruza el veredicto
   del día (GO/WAIT/AVOID por instrumento) y la narrativa multi-día. Hipótesis a
   verificar con el tiempo: las señales de scalp en un instrumento marcado AVOID
   rinden peor. Si tienes muestra, cuantifícalo.
9. **Playbook**: reescribe la "Sección viva" de cada `playbook/*.md`:
   - veredicto global (TOMAR / TOMAR-FILTRADA / EVITAR) por TF
   - tabla de **reglas condicionales** (SI contexto ENTONCES acción, con n y
     efecto dentro vs fuera de la condición)
   - entrada / SL / objetivo / parcial / trailing óptimos con tamaño de muestra
   - contextos a evitar · estado de decaimiento
   Nunca borres el histórico: añade una línea fechada con qué cambió.
10. **Experimentos** (`experiments.json`): si Jesús cambió un input en TradingView
    desde la última corrida, añade una entrada (hypothesis, param, from, to,
    changeDate = fecha del cambio, segment, targetMetric). El script mide
    antes/después y pone `verdict` cuando hay muestra (afterN>=40, beforeN>=20).
    Reporta confirmados / rechazados; recomienda revertir los rechazados.
11. **Commit + push**: `git add -A && git commit -m "agent: daily review <fecha>
    (N pares, K nuevos)" && git push`. Si `git push` falla, imprime TODO el
    hallazgo en la salida para que no se pierda.
12. Cierra con: pares nuevos, WR por segmento, y **el hallazgo más accionable**.

## Revisión semanal (domingo, además de la diaria)

Escribe `reviews/<YYYY>-week-<NN>.md`:
- tabla por (tf, kind): n, WR TP1, E[R], PF, delta vs semana previa (de `decay_weekly`)
- las 3 causas de SL más frecuentes de la semana + evidencia (sigIds)
- estado de cada experimento abierto
- **propuestas concretas** de cambio de inputs de `scalp_command.pine`, cada una con:
  el input, from→to, el segmento, el efecto esperado sobre WR/E[R] **del walk-forward
  (no in-sample)**, y el n de la evidencia.
  Candidatos: `sc_min_rr`, `sc_aplus_rr`, `sc_slbuf`, `sc_floor_atr5`,
  `sc_cap_atr5`, `sc_cap_adr`, `alert_cooldown`, `sc_cooldown`, `min_score_buy`,
  `min_score_sell`, `anchor_5m`, `enable_retest_signals`, `sc_trigger_mode`,
  `chop_up`, `stretch_mult_extreme`, `sc_use_struct`, `sc_grey_asia`, toggles de
  proximidad (`3B`).
- Por cada propuesta, **añade una línea a `predictions.jsonl`**:
  `{"week":"<YYYY-Wnn>","param":"...","from":X,"to":Y,"segment":{"tf":"1","kind":"RETEST"},"appliedDate":null,"predictedDeltaER":0.00,"rationale":"..."}`.
  Cuando Jesús aplique el cambio pon `appliedDate`. El script puntúa
  |real - predicho| y lleva `prediction_scoreboard` (tu MAE y tu tasa de acierto
  de dirección = tu propia calificación; si empeoran, sé más conservador).
- **un solo "cambio del mes"** si hay señal fuerte y estable (sobrevive FDR + OOS).
- Nunca propongas cambio en un segmento con n < 20 o que no aparezca con
  `survives_fdr10=true` en `segment_significance`. Marca `experimental` hasta 40+
  muestras post-cambio y 2 semanas consecutivas en la misma dirección.

## Dashboard

`https://tradedadlog.com/scalp.html` lee `report.json` + `state.json` + las
señales/outcomes recientes del bus. Mantén `report.json` completo y `report.alerts`
al día: es lo que ve Jesús. No hace falta que hagas nada extra para el dashboard,
sólo que `analyze.py` corra y commitees su salida.

## calendar.json

Eventos económicos de alto impacto (`{"events":[{"ts":<ms UTC>,"impact":"high","name":"CPI"}]}`).
`analyze.py` separa señales near-news (<=30 min) vs away. Manténlo al día tú o
deja que lo alimente el feed del Session Analyst (`market.json`).

## Modo sombra (cuando el playbook tenga reglas condicionales estables)

Mantén en `state.json` un bloque `shadowRules`: el conjunto de reglas condicionales
que aplicarías tú ahora mismo (qué señales tomarías y con qué SL/objetivo). Cada
corrida, calcula qué habría hecho ese conjunto sobre las señales del período y
compáralo contra: (a) el indicador crudo, (b) tier A+/B solo. Eso es el candidato
a estrategia del bot.

## Escalera de ejecución (gate)

NO recomiendes conectar a cuenta live hasta que, en el segmento objetivo:
n >= 100 · WR TP1 estable 3 semanas · E[R] > 0 con PF >= 1.3 · causa de SL
dominante mitigada por un cambio de regla verificado (experimento `confirmed`).
Antes: sólo asesor / demo. Ver `execution-ladder.md`.
