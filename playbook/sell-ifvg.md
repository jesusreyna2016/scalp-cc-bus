# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-08 · n: 57)

### Nota de proceso
Segundo día sin repetición del bug de "heal" (ver `buy-retest.md`, incluye
la nota de `git pull "forced update"` resuelta con `git reset --hard`).
**La racha de "cero señales nuevas" se rompió hoy**: llegaron 28 señales
nuevas de golpe (n 29→57) — ver veredicto abajo, ya no hace falta
preguntarle a Jesús sobre un posible bloqueo en Pine para este lado, al
menos por ahora.

### Veredicto global
**Se rompe la racha de 3 revisiones sin señales nuevas — llegaron 28 de
golpe con el primer día hábil completo post-feriado.** n=57 (antes 29):
1m n=36 (WR 52.8%, E[R]=**-0.054**, PF=0.88, 16 SL — se invirtió de
positivo a negativo con las 17 señales nuevas); 2m n=16 (WR 31.2%,
E[R]=**-0.189**, PF=0.66, 9 SL, empeoró bastante con 10 señales nuevas);
5m n=5 (WR 60%, E[R]=-0.186, PF=0.54, 2 SL, solo 1 señal nueva, cambió de
signo pero n mínimo). **El 1m se revierte de "TOMAR" a negativo apenas
llega dato nuevo real** — la lectura de +0.264 con n=19 era en buena
parte ruido/sesgo de muestra chica y de pocos días concretos, lección de
método igual que se vio hoy en `buy-retest.md`/`sell-retest.md` con 2m
RETEST. Prioridad 2 se mantiene; ya no hay lectura claramente accionable
en ningún TF de este playbook.

### Reglas condicionales (IF contexto ENTONCES acción)
Con el salto de dato de hoy el cuadro se invierte por completo: `edge=-1`
n=35 (WR 37.1%, E[R]=**-0.284**, PF=0.5), `edge=0` n=20 (WR 65%,
E[R]=**+0.245**, PF=1.77), `edge=1` n=2 (WR 50%, E[R]=-0.29) — **`edge=-1`
pasó de ser la mejor rama (n=12, ayer) a la peor (n=35, hoy)**, y
`edge=0` pasó de neutral a la mejor rama. Lección de método: con n<20 este
corte no era confiable, tal como advierte `agent-instructions.md`; ya no
se puede decir "INV va al revés de RETEST en `nearEdge`" con esta
muestra. `by_kindside_tier`: `tier=B` n=16 (E[R]=**-0.058**, PF=0.87) y
`tier=C` n=41 (E[R]=**-0.123**, PF=0.75) — **ambos se volvieron
negativos** con el dato nuevo (ayer B=+0.201, C=+0.086); mismo tipo de
reversión.

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=0` (en INV/SHORT) | mejor que `edge=-1`/`edge=1`, orden invertido vs ayer | 20/35/2 | E[R] +0.245/-0.284/-0.29 | baja — n recién cruzó 20 en una rama, el giro completo de signo en 24h muestra que era ruido de muestra chica, no generalizar todavía |

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
Primera lectura con algo de muestra en este segmento
(`session_analyst_cross.by_kind_side`, mejora de `analyze.py` de hoy):
INV/SHORT bajo veredicto SA `AVOID` n=8 E[R]=**-0.036** (casi plano),
`WAIT` n=13 E[R]=+0.158 — **es el único segmento donde `AVOID` NO se ve
claramente mejor que el resto**, a diferencia del hallazgo agregado fuerte
de `sell-retest.md` (AVOID +0.183 vs GO -0.273, con CI90 real). n=8 es
demasiado chico para pesar contra el patrón agregado — anotado para
vigilar si se sostiene con más muestra, no como excepción confirmada.

### Contextos a evitar
- Autopsia de SL sobre las 27 pérdidas INV/SHORT (desglose permanente por
  kind/side en `analyze.py`): `RR-bajo` 16/27 (59%) pasa a ser la causa
  dominante clara, seguida de `stop-en-el-minimo` 10/27 (37%) y
  `contra-estructura` 10/27 (37%) — con más muestra `RR-bajo` se despega
  del empate que había ayer.
- `cross_instrument` sigue `instrument-specific` (spread 1.0, subió de
  0.597, sólo 1m): NQ n=4 WR 100% E[R]=0.795, GC n=4 WR 75% E[R]=0.512,
  **YM n=26 (creció de 14) WR 46.2% E[R]=-0.205 (se invirtió de
  +0.198 a negativo con las señales nuevas)** — n por símbolo sigue chico
  en NQ/GC, no generalizar; YM ya tiene algo más de muestra y su giro es
  la lectura más confiable de las tres.

### Decaimiento
`decay_weekly` ya reporta 2 semanas con muestra sustancial en el dataset
completo (2026-W36 n=3231, 2026-W37 n=1155) pero este segmento sigue sin
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
