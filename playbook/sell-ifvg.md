# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-10 · n: 82)

### Nota de proceso
Ver `buy-retest.md` para el detalle del salto de dato de hoy. Este
segmento sí participó del salto grande, a diferencia de `buy-ifvg.md`:
n 58→82 (**+24**; 1m +17, 2m +7, 5m sin cambio) — el mayor crecimiento
relativo de los cuatro playbooks (+41%).

### Veredicto global — **reversión de signo en 1m y 2m**
n=82 (antes 58, +24): 1m n=54 (+17, WR 53.7%, E[R]=**+0.138**, PF=1.34, 21
SL — sube de -0.054 a +0.138, con 5 SL nuevos de los 17 pares); 2m n=23
(+7, WR 34.8%, E[R]=**-0.14**, PF=0.73, 12 SL — sigue negativo pero mejoró
de -0.189, con 3 SL nuevos); 5m n=5 (sin cambio, WR 60%, E[R]=-0.186,
PF=0.54, 2 SL). Igual que en `sell-retest.md`, el 1m se dio vuelta de
negativo a positivo con la muestra nueva — **no tratar como veredicto
nuevo todavía**, es el mismo patrón de reversión por salto de muestra que
se repite hoy en varios segmentos del bus. `segment_significance`: 1m
CI90=[-0.112,0.4] p=0.198 (n=51, sigue sin certificar pero el CI se movió
hacia positivo); 2m CI90=[-0.475,0.18] p=0.776 (n=23).

### Reglas condicionales (IF contexto ENTONCES acción)
`edge=-1` n=52 (+16, WR 42.3%, E[R]=**-0.043**, PF=0.91 — mejoró mucho de
-0.284), `edge=0` n=28 (+8, WR 60.7%, E[R]=**+0.218**, PF=1.63 — se
mantiene la mejor rama, bajó un poco de +0.245), `edge=1` n=2 (sin cambio,
E[R]=-0.29). `tier=B` n=28 (+11, E[R]=**+0.104**, PF=1.25 — se dio vuelta
de -0.058) y `tier=C` n=54 (+13, E[R]=**+0.002**, PF=1.0 — se dio vuelta
de -0.123, quedó prácticamente plano).

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=0` (en INV/SHORT) | sigue siendo la mejor rama, con margen menor | 28/52/2 | E[R] +0.218/-0.043/-0.29 | baja — el gradiente se mantiene en el mismo orden que ayer (a diferencia de RETEST/SHORT, que se invirtió), pero `edge=-1` dejó de ser claramente negativo |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: 1m n=51 delta=**+0.281** (naive 0.138→managed 0.419,
  sigue ayudando mucho, en línea con el +0.278 de ayer); 2m n=23
  delta=+0.131 (naive -0.14→managed -0.009, casi neutraliza la pérdida
  cruda, subió de +0.018); 5m n=5 delta=+0.37 (sin cambio, n mínimo).
  Mismo patrón cualitativo: la gestión con parciales ayuda más en 1m que
  en 2m/5m de INV/SHORT.
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=41 (+16)
  delta=**+0.62** CI90=[-0.489,2.212] (cambio grande de signo vs ayer
  -0.018, pero el CI sigue siendo muy ancho y cruza cero — no certifica,
  no accionar); 2m n=22 (+7) delta=+0.219 CI90=[-0.04,0.439] (subió de
  +0.149, el límite inferior casi toca cero pero sigue sin certificar).
  Ninguno certifica todavía con el n de hoy. No tocar el SL en INV/SHORT.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
Sin cambio hoy en este corte pese al salto de +24 pares en el segmento
(ninguno de los pares nuevos matcheó con un plan SA): INV/SHORT bajo
veredicto SA `AVOID` n=11 E[R]=**+0.057** (mejoró de -0.036, pero sigue
sin ser fuerte), `WAIT` n=13 E[R]=+0.158 — **sigue siendo el segmento
donde `AVOID` NO se ve claramente mejor que el resto**, a diferencia del
hallazgo agregado que hoy es la alerta más fuerte de todo el bus (ver
`sell-retest.md`: AVOID +0.122 CI90 no cruza cero vs GO -0.196). n sigue
chico aquí para pesar contra el patrón agregado.

### Contextos a evitar
- Autopsia de SL sobre las 35 pérdidas INV/SHORT (+8 vs ayer): `RR-bajo`
  18/35 (51%) sigue siendo la causa dominante, pero `contra-estructura`
  12/35 (34%) se despegó de `stop-en-el-minimo` 10/35 (29%) — ya no es un
  empate de dos, ahora es un segundo lugar más claro.
- `cross_instrument` sigue `instrument-specific` (spread 0.603, bajó de
  1.0, sólo 1m): NQ n=5 (+1) E[R]=0.644, ES n=3 (nuevo con n útil)
  E[R]=0.307, GC n=6 (+2) E[R]=0.235 (bajó de 0.512), YM n=40 (+13)
  E[R]=**+0.041** (subió mucho de -0.205, arrastrando buena parte de la
  reversión del 1m) — n por símbolo sigue chico salvo YM, no generalizar
  todavía pero vigilar YM de cerca al ser el símbolo con más muestra de
  este segmento.

### Decaimiento
`decay_weekly` ahora reporta: 2026-W36 (n=3231) y 2026-W37 (n=2427,
E[R]=+0.069 en el dataset completo) pero este segmento sigue sin
suficiente muestra propia por semana para medir decaimiento aislado.

## Histórico de cambios
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
