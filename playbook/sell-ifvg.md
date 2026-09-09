# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-09 · n: 58)

### Nota de proceso
Día de confirmación, no de dato nuevo (ver `buy-retest.md` para el detalle
del pipeline) — solo +1 par nuevo, en 1m (2m/5m sin cambio).

### Veredicto global
n=58 (antes 57, +1): 1m n=37 (WR 51.4%, E[R]=**-0.054**, PF=0.88, 16 SL —
sin cambio, el nuevo par fue TO); 2m n=16 (sin cambio, WR 31.2%,
E[R]=**-0.189**, PF=0.66, 9 SL); 5m n=5 (sin cambio, WR 60%, E[R]=-0.186,
PF=0.54, 2 SL). Sin cambio de lectura: prioridad 2 se mantiene, sin señal
claramente accionable en ningún TF de este playbook.

### Reglas condicionales (IF contexto ENTONCES acción)
`edge=-1` n=36 (+1, WR 36.1%, E[R]=**-0.284**, PF=0.5), `edge=0` n=20
(sin cambio, WR 65%, E[R]=**+0.245**, PF=1.77), `edge=1` n=2 (sin cambio,
E[R]=-0.29). `by_kindside_tier`: `tier=B` n=17 (+1, E[R]=**-0.058**,
PF=0.87) y `tier=C` n=41 (sin cambio, E[R]=**-0.123**, PF=0.75) — sin
cambio de sentido vs ayer.

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=0` (en INV/SHORT) | mejor que `edge=-1`/`edge=1` | 20/36/2 | E[R] +0.245/-0.284/-0.29 | baja — n sigue chico en todas las ramas, sin cambio vs ayer |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: 1m n=35 delta=**+0.278** (naive -0.054→managed
  0.224, la escalera rescata toda la pérdida cruda y la vuelve positiva,
  menor que el +0.39 de ayer pero sigue siendo un delta grande); 2m n=16
  delta=+0.018 (naive -0.189→managed -0.171, sigue negativo, casi sin
  ayudar, mucho menor que ayer +0.064); 5m n=5 delta=+0.37 (naive
  -0.186→managed 0.184, ayuda, n mínimo). Mismo patrón cualitativo: la
  gestión con parciales ayuda más en 1m que en 2m/5m de INV/SHORT.
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=25
  delta=-0.018 CI90=[-0.385,0.358] (se acercó mucho a cero, ayer era
  -0.318 con n=8 — otra reversión por muestra chica), 2m n=15 delta=+0.149
  CI90=[-0.179,0.452] (bajó de +0.344, sigue sin certificar). Ninguno
  certifica con el n de hoy. No tocar el SL en INV/SHORT todavía.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
Sin cambio hoy en este corte (el nuevo par no matcheó con un plan SA):
INV/SHORT bajo veredicto SA `AVOID` n=8 E[R]=**-0.036** (casi plano),
`WAIT` n=13 E[R]=+0.158 — **sigue siendo el único segmento donde `AVOID`
NO se ve claramente mejor que el resto**, a diferencia del hallazgo
agregado fuerte de `sell-retest.md` (AVOID +0.175 vs GO -0.196, con CI90
real y muestra mucho mayor hoy). n=8 sigue siendo demasiado chico para
pesar contra el patrón agregado.

### Contextos a evitar
- Autopsia de SL sobre las 27 pérdidas INV/SHORT (sin cambio hoy, cero SL
  nuevos): `RR-bajo` 16/27 (59%) sigue siendo la causa dominante clara,
  seguida de `stop-en-el-minimo` 10/27 (37%) y `contra-estructura` 10/27
  (37%).
- `cross_instrument` sigue `instrument-specific` (spread 1.0, sin cambio,
  sólo 1m): NQ n=4 WR 100% E[R]=0.795, GC n=4 WR 75% E[R]=0.512, YM n=27
  (+1) WR 44.4% E[R]=-0.205 (sin cambio de cifra) — n por símbolo sigue
  chico en NQ/GC, no generalizar.

### Decaimiento
`decay_weekly` ya reporta 2 semanas con muestra sustancial en el dataset
completo (2026-W36 n=3231, 2026-W37 n=1224) pero este segmento sigue sin
suficiente muestra propia por semana para medir decaimiento aislado.

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
- 2026-09-08 (martes, primer día hábil completo post-feriado): **se rompe
  la racha de 3 revisiones sin señales nuevas** — llegaron 28 de golpe
  (n=29→57: 1m 19→36, 2m 6→16, 5m 4→5); ya no hace falta preguntar a
  Jesús por un posible bloqueo de Pine, al menos por ahora. Casi todas las
  lecturas se invirtieron de signo con el dato nuevo: 1m E[R]
  +0.264→-0.054, `nearEdge` pasó de `edge=-1` mejor a `edge=0` mejor,
  `tier=B`/`tier=C` pasaron de positivos a negativos, `sl_origin_vs_layer`
  1m de -0.318 a -0.018. Lección de método explícita: todas las lecturas
  de este playbook tenían n<20 y eran ruido de muestra chica, igual que
  ya se documentó para `tier=A+` en `buy-retest.md`/`sell-retest.md`.
  Mejora permanente en `analyze.py`: `session_analyst_cross.by_kind_side`
  da su primera lectura aquí (AVOID n=8 E[R]=-0.036, casi plano) — es el
  único segmento que por ahora NO muestra el patrón "AVOID rinde mejor"
  confirmado hoy en `sell-retest.md`, pero n=8 es insuficiente para
  pesar contra el hallazgo agregado.
- 2026-09-09 (miércoles): día de confirmación, sin dato fechado hoy — solo
  +1 par en 1m (TO, sin SL nuevo), 2m/5m sin cambio. Todas las cifras
  coinciden con ayer, incluido el cruce con Session Analyst (el nuevo par
  no matcheó con un plan SA) — este playbook sigue siendo el único que no
  muestra el patrón agregado "AVOID rinde mejor que GO" (ver
  `sell-retest.md`, cuya muestra del cruce sí creció mucho hoy).
