# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-03 · n: 26)

### Veredicto global
**Crece rápido y empieza a verse interesante, pero todavía no toca el
piso de n=20 por TF.** n=26 (antes 9): 1m n=17 (WR 70.6%, E[R]=+0.222,
PF=1.75, 5 SL) — el más cerca de ser accionable, ya pasó n=20 en total de
señales pero conviene esperar `segment_significance` (no listado todavía,
probablemente por debajo del piso interno del método); 2m n=6 (WR 50%,
E[R]=-0.267, PF=0.47, 3 SL); 5m n=3 (WR 66.7%, E[R]=-0.04, PF=0.88).
Prioridad 2 se mantiene, pero el 1m ya merece que se le preste atención en
la próxima revisión semanal si sigue creciendo al ritmo de hoy.

### Reglas condicionales (IF contexto ENTONCES acción)
Todavía por debajo del piso de n=20 para cualquier corte cruzado, pero ya
hay gradiente visible en `by_kindside_edge` (INV/SHORT): `edge=-1` n=10
(WR 70%, E[R]=+0.197, PF=1.66), `edge=0` n=14 (WR 64.3%, E[R]=+0.047,
PF=1.13), `edge=1` n=2 (WR 50%, E[R]=-0.29) — **nótese que aquí el orden es
al revés que en RETEST** (`edge=-1` es la mejor rama, no la peor). No
mezclar el filtro de `nearEdge` entre RETEST e INV: son geometrías de señal
distintas. `by_kindside_tier`: `tier=B` n=7 (E[R]=+0.201, PF=1.71) sigue
por delante de `tier=C` n=19 (E[R]=+0.034, PF=1.09) — mismo sentido que en
RETEST, sin señales `A+` en INV todavía.

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=-1` (en INV) | mejor que `edge=0`/`edge=1` | 10/14/2 | E[R] +0.197/+0.047/-0.29 | baja — n aún chico, dirección opuesta a RETEST, vigilar sin generalizar |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: la escalera ayuda en los tres TF — 1m n=17
  delta=+0.352 (naive 0.222→managed 0.574, el salto más grande del
  dataset en proporción), 2m n=6 delta=+0.064 (sigue negativo pero menos:
  -0.267→-0.203), 5m n=3 delta=+0.551 (n muy chico). Vigilar si se
  sostiene al crecer la muestra — de confirmarse, la gestión con parciales
  sería aún más importante en INV/SHORT que en RETEST/SHORT.
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=7
  delta=-0.813 (el SL de 3 capas actual bate al estructural aquí, al revés
  que en RETEST/SHORT), 2m n=5 delta=+0.344 — ninguno con CI90 calculable
  de forma fiable (n<10). No tocar el SL en INV todavía.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL sobre las 9 pérdidas INV/SHORT (desglose permanente por
  kind/side, nuevo en `analyze.py`): `contra-estructura` 6/9 (67%) y
  `RR-bajo` 6/9 (67%) empatadas como causa dominante, `stop-en-el-minimo`
  4/9 (44%). Mismo patrón cualitativo que RETEST/SHORT, con menos muestra.

### Decaimiento
_pendiente_ — sólo 2026-W36 disponible en todo el dataset.

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
