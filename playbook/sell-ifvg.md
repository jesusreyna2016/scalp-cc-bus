# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-14 · n: 121)

### Nota de proceso
`git pull` limpio hoy, sin incidentes. Este segmento: n 113→121
(**+8**; 1m +3, 2m +2, 5m +3 — el 5m INV/SHORT recibe señales nuevas por
primera vez en varios días).

### Veredicto global
1m n=76 (+3, WR 48.7%, E[R]=**+0.133** PF=1.29, 34 SL — subió fuerte de
+0.077, sigue positivo); 2m n=37 (+2, WR 37.8%, E[R]=**+0.072** PF=1.14 —
se mantiene positivo por segunda corrida seguida, subió de +0.044); 5m
n=8 (**+3, primera muestra nueva en días** — WR 75.0%, E[R]=**+0.615**
PF=3.46, subió mucho desde -0.186/n=5 — **con n=8 esto es ruido de
muestra mínima, no un giro real**, tres pares nuevos alcanzan para dar
vuelta el signo por completo). `segment_significance`: 1m
CI90=[-0.104,0.38] p=0.181 n=74 (se estrecha un poco, sigue lejos de
certificar); 2m CI90=[-0.301,0.467] p=0.382 n=37 (sigue muy ancho, lejos
de certificar en cualquier dirección); 5m no evaluable de forma
confiable con n=8.

### Reglas condicionales (IF contexto ENTONCES acción)
`nearEdge=1` **da un vuelco grande con apenas 5 pares nuevos** — tratar
como ruido, no como señal:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=-1` | sigue siendo la mejor rama grande, sube más | 70 (+3) | WR 41.4%, E[R]=**+0.176** (subió de +0.146) | baja-moderada — segunda corrida seguida sin cambiar de signo |
| 2 | `nearEdge=0` | sigue negativo, prácticamente sin cambio | 43 (sin cambio) | WR 51.2%, E[R]=**-0.051** (idéntico a ayer) | moderada — congelado, cero señales nuevas |
| 3 | `nearEdge=1` | **se da vuelta de golpe con +5 pares** | 8 (+5) | E[R] **+0.901** (venía de -0.527) | muy baja — n=8, un vuelco de este tamaño con tan poca muestra es ruido puro, no generalizar |
| 4 | `tier=C` | **se da vuelta a positivo**, tras varios días negativo | 83 (+8) | E[R]=**+0.125** (venía de -0.017) | baja — primera lectura positiva de esta rama en el histórico reciente, vigilar si se sostiene con más muestra antes de tratarla como señal |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: 1m n=74 delta=**+0.183** (bajó de +0.224, sigue
  ayudando bastante); 2m n=37 delta=**-0.064** (**se da vuelta a
  negativo**, venía de +0.022 — con n=37 todavía es una lectura frágil,
  vigilar); 5m n=8 delta=+0.042 (bajó mucho de +0.37 con la muestra
  nueva, mismo aviso de ruido que arriba).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=64 (+3)
  delta=**+0.252** CI90=[-0.505,1.245] (bajó de +0.337, sigue sin
  certificar, CI muy ancho); 2m n=36 (+2) delta=**+0.434** CI90=
  **[-0.071,1.114]** (prácticamente igual a +0.47, el límite inferior
  retrocede un poco de -0.05 a -0.071, sigue sin certificar); **5m
  aparece por primera vez con dato suficiente para calcularse**: n=7
  delta=-0.821 (sentido contrario a 1m/2m, muestra demasiado chica para
  concluir nada). Ninguno certifica todavía. No tocar el SL en INV/SHORT.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
INV/SHORT bajo veredicto SA `AVOID` n=23 (sin cambio, cero señales nuevas
cruzadas) E[R]=**-0.151** PF=0.72 y `WAIT` n=19 (sin cambio) E[R]=**-0.222**
PF=0.53 — ambas celdas congeladas, sin dato nuevo hoy por cuarto día
seguido. Sigue siendo el único playbook del bus que no muestra el patrón
agregado "WAIT/GO mejor que AVOID" de `buy-retest.md`/`sell-retest.md`.

### Contextos a evitar
- Autopsia de SL sobre las 55 pérdidas INV/SHORT (+1 vs ayer): `RR-bajo`
  27/55 (49.1%) sigue siendo la causa dominante, cuarto día con el mismo
  orden; `contra-estructura` 18/55 (32.7%) y `stop-en-el-minimo` 15/55
  (27.3%) se mantienen segundo/tercer lugar.
- `cross_instrument` **cambia de `universal` a `instrument-specific`**
  (spread 0.327→0.508) con apenas 2 pares nuevos: ES n=6 (+1) E[R]=0.57
  (subió de 0.354) y NQ n=9 (+1) E[R]=0.19 (subió de 0.027) — YM n=50
  (sin cambio) E[R]=0.062, GC n=11 (+1) E[R]=0.155. **Con n de 6-11 por
  símbolo, este cambio de veredicto es ruido de muestra mínima, no una
  divergencia real entre instrumentos** — mismo patrón de fragilidad que
  el `sl_origin_vs_layer` de `buy-ifvg.md` hoy.

### Decaimiento
`decay_weekly` (global): 2026-W36 n=3140 (sin cambio hoy, la racha de
corridas perdiendo muestra se detuvo — ver `buy-retest.md`) y 2026-W37
n=5389 E[R]=+0.072 en el dataset completo (subió de n=5331) — este
segmento sigue sin suficiente muestra propia por semana para medir
decaimiento aislado.

## Histórico de cambios
- 2026-09-14 (lunes): `git pull` limpio. n 113→121 (+8; 1m+3, 2m+2,
  5m+3 — primera muestra nueva en 5m INV/SHORT en varios días).
  **Lección de método del día**: con n tan chico en este playbook de
  prioridad 2, unos pocos pares nuevos bastan para dar vuelta señales por
  completo — `nearEdge=1` pasó de E[R]=-0.527 a +0.901 con sólo 5 pares
  nuevos, `tier=C` se dio vuelta a positivo con 8, y `cross_instrument`
  1m cambió de `universal` a `instrument-specific` con sólo 2. Ninguno de
  estos movimientos se trata como señal real; se anotan para que quede
  registro de la volatilidad de este segmento con muestra chica. Nada
  accionable nuevo.
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
