# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-02 · n: 39)

### Veredicto global
**EVITAR (1m) / MUESTRA DÉBIL, NO CONFIABLE (2m) — sigue sin ser
accionable.** n=39 (25× 1m/RETEST/LONG, 14× 2m/RETEST/LONG; creció desde
n=31). 1m: WR TP1 48.0%, E[R]=-0.224, PF=0.57 (13 SL de 25) — sigue
negativo, algo menos extremo que el -0.283 de la revisión anterior pero
todavía el peor o segundo peor segmento del dataset. 2m: WR TP1 64.3%,
E[R]=+0.178, PF=1.5 (5 SL de 14). `segment_significance` sigue sin
certificar ninguno de los dos (`survives_fdr10=false`, CI90 1m=[-0.497,
0.068] casi roza 0 por el lado positivo con p_mean_le_0=0.904 — muy
probablemente negativo en la práctica aunque no lo suficiente para pasar
FDR; CI90 2m=[-0.212, 0.585] cruza 0 con más margen). El aparente edge de
2m sigue sin sostenerse al cruzar símbolo: `cross_instrument` no vuelve a
listar 2m/RETEST/LONG este run — el corte por `nearEdge` (ver abajo) es
ahora el hallazgo más relevante en LONG. No tocar inputs de Pine por BUY
RETEST todavía; ninguno de los dos TF llega a n=20 con significancia real
(el 1m sí supera n=20 en volumen bruto, pero sigue sin `survives_fdr10`), y
5m sigue sin datos.

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna certificada (n<20 en la mayoría de los cortes, sin
`survives_fdr10`). Candidatas a vigilar, no a aplicar. **Mejora permanente
de hoy**: estos cortes ahora los calcula `analyze.py` directamente
(`by_kindside_edge`/`by_kindside_tier`/`by_kindside_aligned`), ya no se
aproximan a mano:

| # | SI | ENTONCES (hipótesis) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1` | 7 vs 32 | E[R] +0.459 vs -0.197, WR 85.7% vs 46.9% | baja — n=7 en la rama buena **sin crecer** desde la revisión anterior (todas las 8 señales nuevas fueron `aligned=1`), contraintuitivo (ver anomalía abajo) |
| 2 | `nearEdge=1` | mejor que `nearEdge=-1` mejor que `nearEdge=0` | 6 / 14 / 19 | WR 83.3% / 57.1% / 42.1%; E[R] +0.417 / +0.001 / -0.296; PF 3.5 / 1.0 / 0.49 | baja-moderada — forma NO monótona (edge=0 es la peor rama, no edge=-1 como en SELL RETEST); n=19 en `edge=0` ya razonable, `edge=1` sigue chico (n=6) |
| 3 | `tier` (B vs C) | no discrimina en LONG | 13 vs 26 | E[R] -0.055 vs -0.092, ambos negativos, WR 53.8% ambos | n/a — tier no separa nada aquí, a diferencia de SHORT donde `tier` sí discrimina fuerte (y donde `A+` resultó ser una anomalía invertida, ver `sell-retest.md`) — LONG no tiene ninguna señal `A+` todavía (n=0) |

**Anomalía a vigilar** (no accionar): el modelo P(TP1) in-sample sigue
ponderando `aligned` con signo **negativo** — "alineado con el
sesgo/estructura" predice *peor* resultado, lo mismo que refleja la regla
#1 de la tabla, y aparece también en SELL RETEST (aunque ahí no hay rama
`aligned=0` con la que comparar: 100% de SELL RETEST es `aligned=1`). Dos
hipótesis sin cambios desde la revisión anterior: (a) el campo `aligned`
puede estar capturando exhaustion — alineación tardía, ya extendida,
típica de killzone-Asia-largo; (b) hay un bug de signo en cómo Pine
calcula/envía `aligned`. Sigue en n=7 en la rama `aligned=0` de LONG (no
creció esta corrida) — pedir a Jesús que confirme la definición exacta de
`aligned` en el código sigue pendiente.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin llenarse en la mayoría de
  outcomes v1/v3 de este segmento; insuficiente para medir calidad de entrada.

### Gestión
- SL óptimo: `managed_vs_naive` no reporta 1m/2m RETEST/LONG por separado
  hoy (muestra v4 insuficiente en LONG) — sigue pendiente cortar el
  contrafactual de gestión por side.
- Objetivo: _pendiente_ (contrafactual global no está cortado por
  kind/side todavía).
- Parcial 1: _pendiente_ esta corrida (ver `by_tf_kind_side` en
  `report.md` para MFE descriptivo por TF).
- `revAfterSL_rate` (`by_kindside_edge`/aligned, agregados): sigue alto en
  las ramas perdedoras (`edge=0` 100% en la revisión anterior) — apunta a
  SL demasiado ajustado / mal ubicado más que a dirección equivocada,
  consistente con `stop-en-el-minimo` como una de las causas dominantes
  (ver abajo).
- ¿Trailing tras +1R?: _pendiente_.

### Contextos a evitar
- 1m/RETEST/LONG en general: E[R] sigue negativo (-0.224) con n=25, ya no
  se recupera con más muestra. Tratar como EVITAR mientras no cambie.
- Autopsia de SL sobre las 18 pérdidas LONG (recalculado hoy sin el cap de
  60 filas que trunca `report.md`): `contra-estructura` 17/18 (94%),
  `stop-en-el-minimo` 17/18 (94%), `killzone-Asia-largo` 17/18 (94% —
  pero 32/39 de toda la muestra LONG ya es Asia, así que esta causa por sí
  sola discrimina poco: 82% base rate vs 94% en pérdidas), `RR-bajo` 16/18
  (89%), `sin-nivel-detras` 10/18 (56%), `chop` 5/18. **Tres causas casi
  universales y empatadas** (contra-estructura, stop-en-el-mínimo,
  RR-bajo) — prácticamente cualquier pérdida LONG las tiene las tres a la
  vez, más que en la revisión anterior (14-15/15 → 16-17/18, proporción
  estable). Candidato fuerte para revisión semanal (`sc_min_rr` o
  `sc_aplus_rr`) en cuanto `aligned=0` / `edge=1` crezcan lo suficiente
  para aislar la señal real de la confusión con RR bajo.

### Decaimiento
Con solo 2026-W36 disponible (`decay_weekly` reporta una sola semana, n=270
en todo el dataset), sigue sin haber comparación semana-contra-semana real.

## Histórico de cambios
- 2026-09-01: primera escritura con datos reales (n=3, todas GC, mismo día,
  3/3 TP1). Marcado explícitamente como no accionable por tamaño de muestra.
- 2026-09-01 (tarde): refresco a n=6 (1m n=4, 2m n=2). Primera pérdida 1m
  registrada (WR baja de 100% a 75%), confirma que el 100% inicial era
  ruido. Sigue sin ser accionable (n<20).
- 2026-09-02: refresco a n=31 (1m n=18, 2m n=13). El 1m se da vuelta del
  todo: pasa de aparentar el mejor segmento a ser el peor (E[R] -0.283,
  10 SL de 18). El 2m sigue positivo pero `cross_instrument` lo marca
  instrument-specific e inflado por 3 muestras de NQ — no confiable
  todavía. `RR-bajo` sale como causa casi universal (15/15) de las
  pérdidas LONG: candidato a revisar en la próxima revisión semanal si la
  muestra aguanta. Fix de bug en `analyze.py`: `news_context` crasheaba al
  leer `market.json` del Session Analyst (trataba el dict `news.events`
  como lista de eventos y iteraba sobre sus claves) — corregido hoy, sin
  impacto en las métricas de este playbook.
- 2026-09-02 (corrida formal del agente): refresco n=31->39 (1m n=18->25, 2m
  n=13->14). El 1m se mantiene negativo (-0.283->-0.224), ya no es un salto
  raro sino la lectura estable. El corte `nearEdge` cambia de forma: ahora
  es `edge=0` la peor rama (no `edge=-1` como parecía con n chico) -
  patrón no-monótono y distinto al de SELL RETEST, donde `edge=1` es
  siempre el mejor. La rama `aligned=0` (la buena, E[R]=+0.459) se quedó
  exactamente en n=7 - las 8 señales LONG nuevas fueron todas `aligned=1`,
  así que la anomalía de signo en `aligned` sigue sin poder cuantificarse
  mejor. Autopsia de SL recalculada sin cap de 60 filas: las tres causas
  `contra-estructura`/`stop-en-el-mínimo`/`RR-bajo` siguen casi universales
  (16-17 de 18 pérdidas). Mejora permanente en `analyze.py`: cortes
  cruzados `by_kindside_edge`/`by_kindside_tier`/`by_kindside_aligned`
  agregados (ver detalle en `sell-retest.md`).
