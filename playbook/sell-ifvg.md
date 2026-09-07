# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-07 · n: 29)

### Nota de proceso
Primer día sin repetición del bug de "heal" (ver `buy-retest.md`). Este
playbook en particular tuvo **cero señales nuevas hoy** pese a que otros
segmentos sí recibieron dato genuino — ver veredicto abajo.

### Veredicto global
**Tercera revisión seguida sin ninguna señal nueva — vigilar si es baja
frecuencia real o un problema de detección en Pine.** n=29 (sin cambio
desde 2026-09-05): 1m n=19 (WR 68.4%, E[R]=+0.264, PF=1.95, 5 SL); 2m n=6
(WR 50%, E[R]=-0.267, PF=0.47, 3 SL); 5m n=4 (WR 75%, E[R]=+0.018,
PF=1.07, 1 SL) — cifras idénticas a las 3 últimas corridas. El 1m sigue
siendo el más cerca de ser accionable. A diferencia de INV/LONG (que sí
recibió 2 señales nuevas hoy en `buy-ifvg.md`), este lado (SHORT) lleva ya
3 revisiones (2026-09-05, 09-06, 09-07) sin una sola señal nueva — si se
mantiene 1-2 corridas más, vale la pena preguntarle a Jesús si `kind=INV
side=SHORT` tiene algún filtro o condición en Pine que lo esté bloqueando
más de lo esperado. Prioridad 2 se mantiene.

### Reglas condicionales (IF contexto ENTONCES acción)
Todavía por debajo del piso de n=20 para cualquier corte cruzado, sin
cambios materiales vs ayer: `edge=-1` n=12 (WR 75%, E[R]=+0.262, PF=2.05),
`edge=0` n=15 (WR 60%, E[R]=+0.047, PF=1.13), `edge=1` n=2 (WR 50%,
E[R]=-0.29) — **sigue al revés que en RETEST** (`edge=-1` la mejor rama,
no la peor). No mezclar el filtro de `nearEdge` entre RETEST e INV: son
geometrías de señal distintas. `by_kindside_tier`: `tier=B` n=7
(E[R]=+0.201, PF=1.71, sin cambio) sigue por delante de `tier=C` n=22
(E[R]=+0.086, PF=1.26) — mismo sentido que en RETEST, sin señales `A+` en
INV todavía.

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=-1` (en INV) | mejor que `edge=0`/`edge=1` | 12/15/2 | E[R] +0.262/+0.047/-0.29 | baja — n aún chico, dirección opuesta a RETEST, vigilar sin generalizar |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: la escalera sigue ayudando en los tres TF — 1m n=18
  delta=+0.39 (naive 0.264→managed 0.653, el salto más grande del dataset
  en proporción, mayor incluso que ayer +0.352), 2m n=6 delta=+0.064
  (sigue negativo pero menos: -0.267→-0.203, sin cambio), 5m n=4
  delta=+0.463 (naive 0.018→managed 0.481). Mismo patrón que ayer: la
  gestión con parciales parece más importante en INV/SHORT que en
  RETEST/SHORT, pero con n todavía chico en los tres TF.
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=8
  delta=-0.318 (el SL de 3 capas actual sigue batiendo al estructural
  aquí, al revés que en RETEST/SHORT), 2m n=5 delta=+0.344 (sin cambio) —
  ninguno con CI90 calculable de forma fiable (n<10). No tocar el SL en
  INV todavía.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL sobre las 9 pérdidas INV/SHORT (desglose permanente por
  kind/side en `analyze.py`): `contra-estructura` 6/9 (67%) y `RR-bajo`
  6/9 (67%) empatadas como causa dominante, `stop-en-el-minimo` 4/9 (44%)
  — sin cambio vs ayer. Mismo patrón cualitativo que RETEST/SHORT, con
  menos muestra.
- `cross_instrument` (primera vez con lectura en este segmento,
  `instrument-specific`, spread 0.597, sólo 1m): YM n=14 WR 64.3%
  E[R]=0.198, NQ n=4 WR 100% E[R]=0.795 — n por símbolo demasiado chico
  para generalizar.

### Decaimiento
`decay_weekly` ya reporta 2 semanas en todo el dataset (2026-W36 n=3231,
2026-W37 n=26) pero este segmento no tuvo señales en la semana nueva —
sin decaimiento propio que medir todavía.

## Histórico de cambios
- 2026-09-02 (corrida formal del agente): refresco n=4->9 (1m n=3->8, 5m
  se mantiene n=1). WR 1m sube de 66.7% a 75.0%, E[R] pasa de -0.07 a
  +0.316 - sigue siendo ruido de muestra chica (n=8), nada accionable
  todavía. Concentrado en YM/NQ, mayoría `tier=C`/`nearEdge=0`.
- 2026-09-03: salto de muestra n=9→26 (1m 8→17, 2m 0→6, 5m 1→3 — primeros
  datos 2m). El 1m se mantiene fuerte (E[R]=+0.222, WR 70.6%) y ya casi
  alcanza el piso de n=20 total (por TF sigue chico para `nearEdge`/`tier`
  cruzado). Primer dato de `nearEdge` en INV: el orden es opuesto al de
  RETEST (`edge=-1` es la mejor rama aquí, no la peor) — anotado para no
  confundir los dos playbooks al generalizar. `managed_vs_naive` muestra a
  la escalera ayudando fuerte en 1m (+0.352). Mejora permanente en
  `analyze.py`: `sl_post_mortem.causes_by_kind_side` ya cubre este
  segmento sin necesidad de recalcular a mano.
- 2026-09-04: crecimiento mínimo n=26→28 (1m 17→18, 2m sin cambio en 6,
  5m 3→4). Sin cambios de lectura material — se deja constancia del
  estancamiento momentáneo, nada accionable nuevo.
- 2026-09-05: crecimiento mínimo otra vez n=28→29 (1m 18→19, 2m/5m sin
  cambio). A diferencia de BUY/SELL RETEST (ver sus historiales), este
  playbook no se movió con la restauración de `signals/2026-09-03.jsonl`
  de hoy — su muestra de ese día ya era chica y no dependía del archivo
  dañado. Sin cambios de lectura material.
- 2026-09-06 (revisión semanal, domingo): n sin cambios (29) — sin dato de
  mercado nuevo (fin de semana). El bug de `heal` de `signals/2026-09-03.jsonl`
  se repitió una segunda vez y se restauró de nuevo; se añadió guarda
  permanente en `analyze.py` (`file_integrity_check`). Ver
  `reviews/2026-week-36.md`.
- 2026-09-07 (lunes, festivo EE.UU.): n sin cambios (29) — tercera revisión
  seguida sin ninguna señal INV/SHORT nueva, pese a que otros segmentos
  (INV/LONG, RETEST) sí recibieron dato genuino hoy. Primera lectura de
  `cross_instrument` en este segmento (`instrument-specific`, spread
  0.597, sólo 1m, n por símbolo muy chico). Se deja anotado para preguntar
  a Jesús si hay algo en Pine bloqueando la detección de este lado si el
  estancamiento sigue 1-2 corridas más.
