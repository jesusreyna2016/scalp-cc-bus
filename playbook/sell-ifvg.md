# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-05 · n: 29)

### Veredicto global
**Crecimiento casi nulo de nuevo (+1) — sin cambio de lectura, este
playbook no se vio afectado por la restauración de datos de hoy (ver
`buy-retest.md`).** n=29 (antes 28): 1m n=19 (WR 68.4%, E[R]=+0.264,
PF=1.95, 5 SL); 2m n=6 (sin cambio, WR 50%, E[R]=-0.267, PF=0.47, 3 SL);
5m n=4 (sin cambio, WR 75%, E[R]=+0.018, PF=1.07, 1 SL). El 1m sigue
siendo el más cerca de ser accionable; el ritmo de crecimiento lento se
mantiene por segunda revisión — vigilar si es un patrón de baja frecuencia
o un problema de detección en Pine. Prioridad 2 se mantiene.

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
- 2026-09-04: crecimiento mínimo n=26→28 (1m 17→18, 2m sin cambio en 6,
  5m 3→4). Sin cambios de lectura material — se deja constancia del
  estancamiento momentáneo, nada accionable nuevo.
- 2026-09-05: crecimiento mínimo otra vez n=28→29 (1m 18→19, 2m/5m sin
  cambio). A diferencia de BUY/SELL RETEST (ver sus historiales), este
  playbook no se movió con la restauración de `signals/2026-09-03.jsonl`
  de hoy — su muestra de ese día ya era chica y no dependía del archivo
  dañado. Sin cambios de lectura material.
