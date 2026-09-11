# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-11 · n: 94)

### Nota de proceso
Ver `buy-retest.md` para el incidente de repo de hoy (reset a
`origin/main`, sin pérdida de datos). Este segmento: n 82→94 (**+12**;
1m +8, 2m +4, 5m sin cambio).

### Veredicto global
1m n=62 (+8, WR 50.0%, E[R]=**+0.111** PF=1.25, 27 SL — bajó de +0.138,
la mayoría de los pares nuevos (6 de 8) fueron SL); 2m n=27 (+4, WR
33.3%, E[R]=**+0.019** PF=1.04 — **se da vuelta a positivo**, venía de
-0.14); 5m n=5 (sin cambio, WR 60%, E[R]=-0.186, PF=0.54). `segment_significance`:
1m CI90=[-0.151,0.382] p=0.255 n=60 (se alejó un poco de certificar,
venía de [-0.112,0.4] p=0.198); 2m CI90=[-0.408,0.503] p=0.496 n=27
(mejoró bastante junto con el E[R], sigue lejos de certificar).

### Reglas condicionales (IF contexto ENTONCES acción)
`edge=-1` n=57 (+5, WR 40.4%, E[R]=**+0.08** — **se da vuelta a
positivo**, venía de -0.043), `edge=0` n=35 (+7, WR 54.3%, E[R]=**+0.068**
— bajó fuerte de +0.218, deja de ser claramente la mejor rama), `edge=1`
n=2 (sin cambio, E[R]=-0.29). `tier=B` n=30 (+2, E[R]=**+0.163**, subió
de +0.104) y `tier=C` n=64 (+10, E[R]=**+0.021**, casi sin cambio de
+0.002).

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge` (en INV/SHORT) | **el gradiente se aplana** — `edge=-1` y `edge=0` casi convergen | 57/35/2 | E[R] +0.08/+0.068/-0.29 | baja — hasta ayer `edge=0` era claramente la mejor rama (+0.218 vs -0.043); hoy la diferencia entre las dos ramas grandes casi desaparece, tratar como no asentado |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: 1m n=60 delta=**+0.279** (prácticamente sin cambio,
  venía de +0.281 — sigue ayudando mucho); 2m n=27 delta=**-0.021**
  (naive 0.019→managed -0.002 — **cambia de signo**, ayer ayudaba
  +0.131, ahora resta ligeramente); 5m n=5 delta=+0.37 (sin cambio).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=50 (+9)
  delta=**+0.408** CI90=[-0.548,1.779] (bajó de +0.62, sigue sin
  certificar, CI muy ancho); 2m n=26 (+4) delta=+0.245 CI90=[-0.031,0.516]
  (subió un poco de +0.219, el límite inferior sigue justo debajo de
  cero — cerca pero sin certificar). Ninguno certifica todavía. No tocar
  el SL en INV/SHORT.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
**Reversión fuerte, en línea con lo que pasa en `sell-retest.md`**:
INV/SHORT bajo veredicto SA `AVOID` n=23 (+12) E[R]=**-0.151** PF=0.72
(**se da vuelta a negativo**, venía de +0.057) y `WAIT` n=19 (+6)
E[R]=**-0.222** PF=0.53 (**también se da vuelta a negativo**, venía de
+0.158) — las dos ramas con lectura propia en este segmento pasaron de
positivas a negativas a la vez. Coincide con la reversión general del
cruce SA↔resultado-scalp que hoy se ve en los cuatro playbooks (ver
`sell-retest.md` para el detalle agregado) — más evidencia de que esta
relación es inestable de una corrida a otra, no una regla explotable.

### Contextos a evitar
- Autopsia de SL sobre las 43 pérdidas INV/SHORT (+8 vs ayer): `RR-bajo`
  22/43 (51.2%) sigue siendo la causa dominante, sin cambio de posición;
  `contra-estructura` 14/43 (32.6%) y `stop-en-el-minimo` 13/43 (30.2%)
  se mantienen como segundo/tercer lugar en el mismo orden que ayer.
- `cross_instrument` **mejora de `instrument-specific` a `universal`**
  (spread 0.603→**0.328**, sólo 1m): YM n=46 (+6) E[R]=0.042 (casi sin
  cambio), NQ n=6 (+1) E[R]=0.37 (bajó de 0.644), ES n=4 (+1) E[R]=0.285
  (casi sin cambio), GC n=6 (sin cambio) E[R]=0.235 — primera vez que
  este corte deja de ser `instrument-specific`, aunque con n por símbolo
  todavía chico salvo YM.

### Decaimiento
`decay_weekly` (global): 2026-W36 n=3183 (bajó de n=3231, ver nota de
anomalía en `buy-retest.md`) y 2026-W37 n=3856 E[R]=+0.042 en el dataset
completo — este segmento sigue sin suficiente muestra propia por semana
para medir decaimiento aislado.

## Histórico de cambios
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
