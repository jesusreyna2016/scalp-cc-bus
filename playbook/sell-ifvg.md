# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-12 · n: 109)

### Nota de proceso
Sin incidentes de repo hoy. Este segmento: n 94→109 (**+15**; 1m +9, 2m
+6, 5m sin cambio).

### Veredicto global
1m n=71 (+9, WR 47.9%, E[R]=**+0.109** PF=1.23, 32 SL — prácticamente sin
cambio de +0.111); 2m n=33 (+6, WR 33.3% sin cambio, E[R]=**-0.04**
PF=0.93 — **se da vuelta a negativo otra vez**, venía de +0.019, segundo
cambio de signo consecutivo); 5m n=5 (sin cambio, WR 60%, E[R]=-0.186,
PF=0.54). `segment_significance`: 1m CI90=[-0.141,0.377] p=0.244 n=69
(prácticamente sin cambio); 2m CI90=[-0.391,0.395] p=0.589 n=33 (el
intervalo se estrechó un poco pero el E[R] volvió a negativo, sigue lejos
de certificar).

### Reglas condicionales (IF contexto ENTONCES acción)
`edge=-1` n=65 (+8, WR 40.0%, E[R]=**+0.125**, subió de +0.08), `edge=0`
n=41 (+6, WR 51.2%, E[R]=**-0.033** — **se da vuelta a negativo**, venía
de +0.068), `edge=1` n=3 (+1, E[R]=**-0.527**, empeoró de -0.29). `tier=B`
n=36 (+6, E[R]=**+0.157**, prácticamente sin cambio de +0.163) y `tier=C`
n=73 (+9, E[R]=**-0.006** — se da vuelta a negativo, venía de +0.021).

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge` (en INV/SHORT) | **se invierte de nuevo** — ahora `edge=-1` es la mejor rama, `edge=0` cae a negativo | 65/41/3 | E[R] +0.125/-0.033/-0.527 | baja — tercer cambio de forma en 3 corridas para este corte, sigue sin asentarse |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: 1m n=69 delta=**+0.23** (bajó un poco de +0.279,
  sigue ayudando mucho); 2m n=33 delta=**+0.063** (**se da vuelta a
  positivo de nuevo**, venía de -0.021 — segundo cambio de signo
  consecutivo en esta rama); 5m n=5 delta=+0.37 (sin cambio).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=59 (+9)
  delta=**+0.349** CI90=[-0.547,1.441] (bajó de +0.408, sigue sin
  certificar, CI muy ancho); 2m n=32 (+6) delta=**+0.121**
  CI90=**[-0.142,0.372]** (bajó bastante de +0.245, el límite inferior
  se aleja de cero en vez de acercarse — pierde terreno respecto a la
  lectura "cerca de certificar" de ayer). Ninguno certifica todavía. No
  tocar el SL en INV/SHORT.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
INV/SHORT bajo veredicto SA `AVOID` n=23 (sin cambio, cero señales nuevas
cruzadas) E[R]=**-0.151** PF=0.72 y `WAIT` n=19 (sin cambio) E[R]=**-0.222**
PF=0.53 — ambas celdas congeladas, sin dato nuevo hoy. Segundo día
seguido con las dos ramas en negativo, mismo signo que ayer (a diferencia
de `sell-retest.md`/`buy-retest.md`, donde el cruce sí se movió con dato
nuevo) — sigue sin ser una regla explotable, sólo constancia de que no se
revirtió por falta de muestra nueva, no por confirmación real.

### Contextos a evitar
- Autopsia de SL sobre las 52 pérdidas INV/SHORT (+9 vs ayer): `RR-bajo`
  26/52 (50.0%) sigue siendo la causa dominante, sin cambio de posición
  (segundo día con el mismo orden); `contra-estructura` 17/52 (32.7%) y
  `stop-en-el-minimo` 14/52 (26.9%) se mantienen como segundo/tercer
  lugar.
- `cross_instrument` sigue `universal` (spread 0.328→0.327, prácticamente
  sin cambio): YM n=49 (+3) E[R]=0.085 (subió de 0.042), NQ n=8 (+2)
  E[R]=0.027 (bajó fuerte de 0.37, con muestra todavía chica), ES n=5
  (+1) E[R]=0.354 (subió de 0.285), GC n=9 (+3) E[R]=0.168 (bajó de
  0.235) — segundo día seguido como `universal`, aunque n por símbolo
  sigue chico salvo YM.

### Decaimiento
`decay_weekly` (global): 2026-W36 n=3179 (bajó de n=3183, tercera corrida
seguida perdiendo muestra pero desacelerando — ver `buy-retest.md`) y
2026-W37 n=4573 E[R]=+0.084 en el dataset completo (subió de +0.042) —
este segmento sigue sin suficiente muestra propia por semana para medir
decaimiento aislado.

## Histórico de cambios
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
