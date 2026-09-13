# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-13 · n: 113)

### Nota de proceso
Incidente menor de repo, ver `buy-retest.md`. Este segmento: n 109→113
(**+4**; 1m +2, 2m +2, 5m sin cambio).

### Veredicto global
1m n=73 (+2, WR 46.6%, E[R]=**+0.077** PF=1.16, 34 SL — bajó de +0.109,
sigue positivo pero se modera); 2m n=35 (+2, WR 37.1%, E[R]=**+0.044**
PF=1.08 — **se da vuelta a positivo de nuevo**, venía de -0.04, tercer
cambio de signo consecutivo en 3 corridas); 5m n=5 (sin cambio, WR 60%,
E[R]=-0.186, PF=0.54). `segment_significance`: 1m CI90=[-0.168,0.332]
p=0.315 n=71 (se ensanchó un poco, sigue lejos de certificar); 2m
CI90=[-0.331,0.458] p=0.444 n=35 (el intervalo se ensanchó bastante y el
E[R] volvió a positivo, sigue lejos de certificar en cualquier
dirección).

### Reglas condicionales (IF contexto ENTONCES acción)
`nearEdge` **por primera vez en varias corridas NO cambia de forma**:
`edge=-1` n=67 (+2, WR 40.3%, E[R]=**+0.146**, subió de +0.125), `edge=0`
n=43 (+2, WR 51.2%, E[R]=**-0.051** — sigue negativo, bajó un poco de
-0.033), `edge=1` n=3 (sin cambio, congelado, E[R]=**-0.527**). `tier=B`
n=38 (+2, E[R]=**+0.192**, subió de +0.157) y `tier=C` n=75 (+2,
E[R]=**-0.017**, sigue negativo, prácticamente igual a -0.006).

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge` (en INV/SHORT) | **mantiene la forma de ayer por primera vez** — `edge=-1` mejor rama, `edge=0`/`edge=1` negativos | 67/43/3 | E[R] +0.146/-0.051/-0.527 | baja-moderada — primera vez sin cambio de forma tras 3 corridas seguidas invirtiéndose; aún insuficiente para tratarlo como regla |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: 1m n=71 delta=**+0.224** (prácticamente igual a
  +0.23, sigue ayudando mucho); 2m n=35 delta=**+0.022** (bajó de +0.063,
  sigue positivo, tercera corrida en positivo tras el vaivén); 5m n=5
  delta=+0.37 (sin cambio, congelado).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=61 (+2)
  delta=**+0.337** CI90=[-0.514,1.429] (prácticamente igual a +0.349,
  sigue sin certificar, CI muy ancho); 2m n=34 (+2) delta=**+0.47**
  CI90=**[-0.05,1.155]** (**salto grande** desde +0.121, el límite
  inferior se acerca a cero desde -0.142 a -0.05) — movimiento grande con
  apenas +2 de muestra, tratar como ruido de n chico, no como mejora
  real; sigue sin certificar. Ninguno certifica todavía. No tocar el SL
  en INV/SHORT.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
INV/SHORT bajo veredicto SA `AVOID` n=23 (sin cambio, cero señales nuevas
cruzadas) E[R]=**-0.151** PF=0.72 y `WAIT` n=19 (sin cambio) E[R]=**-0.222**
PF=0.53 — ambas celdas congeladas, sin dato nuevo hoy por tercer día
seguido. Sigue sin ser una regla explotable, sólo constancia de que no se
revirtió por falta de muestra nueva, no por confirmación real. Este
sigue siendo el único playbook del bus que no muestra el patrón agregado
"WAIT/GO mejor que AVOID" de `buy-retest.md`/`sell-retest.md`.

### Contextos a evitar
- Autopsia de SL sobre las 54 pérdidas INV/SHORT (+2 vs ayer): `RR-bajo`
  26/54 (48.1%, conteo sin cambio, baja de % por el denominador mayor)
  sigue siendo la causa dominante, tercer día con el mismo orden;
  `contra-estructura` 18/54 (33.3%) y `stop-en-el-minimo` 14/54 (25.9%,
  conteo sin cambio) se mantienen segundo/tercer lugar.
- `cross_instrument` sigue `universal` (spread 0.327, prácticamente sin
  cambio): YM n=50 (+1) E[R]=0.062 (bajó de 0.085), NQ n=8 (sin cambio)
  E[R]=0.027, ES n=5 (sin cambio) E[R]=0.354, GC n=10 (+1) E[R]=0.051
  (bajó de 0.168) — tercer día seguido como `universal`, n por símbolo
  sigue chico salvo YM.

### Decaimiento
`decay_weekly` (global): 2026-W36 n=3140 (bajó de n=3179, cuarta corrida
seguida perdiendo muestra — ver `buy-retest.md`) y 2026-W37 n=5331
E[R]=+0.072 en el dataset completo (bajó un poco de +0.084) — este
segmento sigue sin suficiente muestra propia por semana para medir
decaimiento aislado.

## Histórico de cambios
- 2026-09-13 (domingo, REVISIÓN SEMANAL): n 109→113 (+4; 1m+2, 2m+2).
  Incidente menor de repo, ver `buy-retest.md`. 2m se da vuelta a
  positivo por tercera vez consecutiva (E[R] -0.04→+0.044) — sigue sin
  asentarse, n=35 todavía chico. `nearEdge` deja de invertirse por
  primera vez en 3 corridas (misma forma que ayer). `sl_origin_vs_layer`
  en 2m da un salto grande (delta 0.121→0.47) con apenas +2 de muestra —
  tratado como ruido, no como mejora real. Sigue siendo el único playbook
  del bus sin el patrón agregado "AVOID rinde peor" (cruce con Session
  Analyst congelado por tercer día).
- 2026-09-12 (sábado): n 94→109 (+15; 1m+9, 2m+6), sin incidentes de
  repo. 2m se da vuelta a negativo por segunda vez consecutiva (E[R]
  +0.019→-0.04) y `managed_vs_naive` en 2m se da vuelta a positivo
  también por segunda vez consecutiva (-0.021→+0.063) — ambas ramas
  siguen sin asentarse con n todavía chico (33). El cruce con Session
  Analyst queda congelado (cero señales nuevas cruzadas), a diferencia
  del resto del bus donde sí hubo movimiento.
- 2026-09-11 (viernes): n 82→94 (+12; 1m+8, 2m+4). Mismo incidente de
  repo que `buy-retest.md`. 2m se da vuelta a positivo (E[R] -0.14→+0.019)
  y `managed_vs_naive` en 2m cambia de signo (+0.131→-0.021). El cruce con
  Session Analyst se revierte con fuerza: `AVOID` pasa de +0.057 a -0.151
  y `WAIT` de +0.158 a -0.222 — misma reversión que se ve en
  `sell-retest.md`/`buy-retest.md` hoy, confirma que el cruce SA no es
  estable corrida a corrida. `cross_instrument` en 1m pasa de
  `instrument-specific` a `universal` (spread 0.603→0.328), primera vez
  para este segmento.
- 2026-09-10 (jueves): salto de dato mayor que `buy-ifvg.md` (+24 vs +3,
  n 58→82). **Reversión de signo en 1m y 2m** (1m E[R] -0.054→+0.138, 2m
  -0.189→-0.14), mismo patrón de volatilidad por muestra nueva que se ve
  en `sell-retest.md` hoy — no tratar como veredicto nuevo. `tier=B` y
  `tier=C` también se dieron vuelta a positivo. YM concentró buena parte
  del crecimiento en 1m (n 27→40) y lideró la reversión (E[R]
  -0.205→+0.041). Cruce con Session Analyst sigue plano en este segmento
  (AVOID apenas +0.057), a diferencia del hallazgo agregado fuerte del
  resto del bus.
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
