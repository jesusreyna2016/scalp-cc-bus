# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-20 (domingo, revisión semanal) · n: 146)

### Nota de proceso
Sin archivo `signals/outcomes` nuevo hoy (fin de semana, ver
`buy-retest.md`); las 37 señales resueltas por TIMEOUT forzado en todo
el bus cayeron todas en RETEST — **este playbook queda con n y métricas
idénticas a ayer** (n=146, sin cambio en ningún TF). Ver
`reviews/2026-week-38.md` para el cierre de semana del bus completo.

### Veredicto global
1m n=96 (+8, WR 47.9%, E[R]=**+0.064** PF=1.14 — baja de +0.091); 2m
n=41 (+2, WR 34.1%, E[R]=**-0.033** PF=0.94 — **cruza a negativo**,
venía de +0.017); 5m n=9 (+1, primera señal nueva en 7 corridas, WR
66.7%, E[R]=+0.436 PF=2.31 — baja de +0.615, primer SL nuevo en esta
rama en varios días). `segment_significance`: 1m CI90=[-0.135,0.27]
p=0.29 n=92 (sigue lejos de certificar); 2m CI90=[-0.365,0.361] p=0.574
n=41 (sigue sin certificar, coherente con el cruce a negativo); 5m
CI90=[-0.218,1.126] p=0.138 n=9 (sigue sin certificar) — ningún TF de
este playbook certifica FDR hoy, igual que en `buy-ifvg.md` (que perdió
su única certificación ayer) — mismo recordatorio de que con n<20 la
bandera FDR no es señal real en ninguno de los dos playbooks INV.

### Reglas condicionales (IF contexto ENTONCES acción)

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=-1` | **cede fuerte** | 87 (+9) | E[R]=**+0.043** (bajó mucho de +0.125) | baja — primer retroceso marcado tras varias corridas estable, vigilar si se sostiene |
| 2 | `nearEdge=0` | **retrocede, vuelve a negativo** | 50 (+3) | E[R]=**-0.03** (empeora de -0.014) | baja — vaivén, n todavía chico |
| 3 | `tier=B` | **cede fuerte** | 45 (+6) | E[R]=**+0.015** (bajó mucho de +0.096) | baja — primer retroceso marcado |
| 4 | `tier=C` | se mantiene positivo, pero cede un poco | 101 (+5) | E[R]=**+0.08** (bajó un poco de +0.103) | baja-moderada — sexta lectura positiva seguida, pero ya no clara la separación de `tier=B` |

`nearEdge=1` sale de su congelamiento con 1 señal nueva (n=9, +1):
E[R]=**+0.69** — sigue siendo ruido de muestra mínima, no generalizar.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: 1m n=92 delta=**+0.207** (sube de +0.198, sigue
  ayudando bastante); 2m n=41 delta=**-0.058** (idéntico, sigue
  negativo); 5m n=9 delta=+0.037 (baja un poco de +0.042).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=82 (+7)
  delta=**-0.154** CI90=[-0.498,0.201] (prácticamente idéntico a
  -0.151, sigue sin certificar); 2m n=40 (+2) delta=**+0.39**
  CI90=[-0.055,0.993] (baja un poco de +0.411, sigue sin certificar); 5m
  n=8 (+1) delta=**-0.719** CI90=**[-1.204,-0.241]** — **primera lectura
  con CI90 que no cruza cero** (`delta_below_zero=true`), mismo signo
  que 5m INV/LONG (el SL de 3 capas gana, no el estructural) — pero con
  n=8 sigue siendo ruido de muestra mínima, no tratar como hallazgo real
  todavía (muy por debajo del piso n≥20 del playbook, y del n≥30 que
  pide `agent-instructions.md` para esta medición). Ninguno certifica de
  forma usable todavía. No tocar el SL en INV/SHORT.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
INV/SHORT bajo veredicto SA `AVOID` n=23 (sin cambio, cero pares nuevos
por segunda corrida) E[R]=**-0.333** (idéntico) PF=0.44 y `WAIT` n=31
(+8) E[R]=**-0.183** (empeora desde -0.158) PF=0.63 — sigue siendo el
único playbook del bus que no muestra el patrón agregado "WAIT/GO mejor
que AVOID" de `buy-retest.md`/`sell-retest.md`; aquí las dos ramas con
muestra utilizable siguen rindiendo negativo, `WAIT` cada vez peor.

### Contextos a evitar
- Autopsia de SL sobre las 69 pérdidas INV/SHORT (+8 vs ayer): mismo
  orden — `RR-bajo` 34/69 (49.3%) sigue siendo la causa dominante,
  prácticamente igual a ayer (50.8%); `contra-estructura` 19/69 (27.5%)
  y `stop-en-el-minimo` 18/69 (26.1%) se mantienen segundo/tercer lugar.
- `cross_instrument` (1m) **sube a spread 1.126** (desde 0.543) y sigue
  `instrument-specific`: **aparece CL por primera vez** con n=6,
  E[R]=**-0.556** (nuevo peor símbolo, empuja el spread hacia arriba,
  pero n=6 es ruido puro); YM n=55 (+2) E[R]=0.044 (sube un poco de
  0.027), GC n=19 (sin cambio) E[R]=0.122 (idéntico), NQ n=10 (sin
  cambio) E[R]=0.071 (idéntico), ES n=6 (sin cambio) E[R]=0.57 (idéntico)
  — n por símbolo sigue chico (6-55), no generalizar; el salto de spread
  es un artefacto de n=6 en CL, no un patrón nuevo real.

### Decaimiento
`decay_weekly` (global): 2026-W36 n=3121 (bajó de 3183 por dedup, ver
`buy-retest.md`); 2026-W37 n=5315 (bajó de n=5389 por -74, la caída más
grande vista hasta ahora) E[R]=+0.071; 2026-W38 n=3016 (subió fuerte de
2211) E[R]=+0.081 — este segmento sigue sin suficiente muestra propia
por semana para medir decaimiento aislado.

## Histórico de cambios
- 2026-09-20 (domingo, revisión semanal): sin archivo de datos nuevo
  (fin de semana); los 37 TIMEOUT forzados de todo el bus cayeron todos
  en RETEST — este playbook queda con n=146 y todas sus métricas
  idénticas a ayer. Ver `reviews/2026-week-38.md` para el cierre de
  semana del bus completo.
- 2026-09-19 (sábado): mismo incidente de repo que `buy-retest.md`
  (`origin/main` reescrito río arriba, sin pérdida). n 135→146 (+11;
  1m+8, 2m+2, 5m+1) — algo más de actividad que el mínimo habitual.
  **2m cruza a negativo** (E[R] +0.017→-0.033) y `tier=B`/`nearEdge=-1`
  ceden fuerte tras varias corridas estables, sin certificar en ningún
  caso (n todavía chico). El SL estructural en 5m tiene su primera
  lectura con CI90 que no cruza cero (`delta_below_zero=true`,
  n=8) — mismo signo que 5m INV/LONG, pero con n=8 sigue siendo ruido,
  no un hallazgo real todavía. `cross_instrument` en 1m sube de spread
  por la aparición de CL con n=6 (artefacto de muestra mínima, no un
  patrón nuevo). Nada accionable nuevo: sigue siendo prioridad 2, ningún
  TF con n suficiente para proponer cambios.
- 2026-09-18 (viernes): mismo incidente de repo que `buy-retest.md`
  (`origin/main` reescrito río arriba, sin pérdida). Día casi sin
  actividad otra vez: n 131→135 (+4, todo en 1m). El vuelco de signo de
  ayer en `sl_origin_vs_layer` 1m se modera (delta -0.193→-0.151, vuelve
  a incluir positivos en el CI90) y el símbolo YM en `cross_instrument`
  también revierte su cruce a negativo de ayer (E[R] -0.012→+0.027) —
  dos lecciones de método el mismo día sobre no fijar giros de una sola
  corrida con n~50-75. Nada accionable nuevo: sigue siendo prioridad 2,
  ningún TF con n suficiente para proponer cambios.
- 2026-09-17 (jueves): mismo incidente inofensivo de repo que
  `buy-retest.md`. Día casi sin actividad otra vez: n 129→131 (+2, todo
  en 1m). **Lección de método del día**: `sl_origin_vs_layer` en 1m se
  dio vuelta de signo completo con un solo par nuevo (delta
  +0.243→-0.193, n=70→71) — con n tan chico un solo trade puede invertir
  la lectura, no tratarla como señal en ninguna dirección. El cruce con
  Session Analyst empeora en ambas ramas (`AVOID` -0.188→-0.333, aunque
  `WAIT` mejora de -0.174 a -0.12) — sigue siendo el único playbook sin
  el patrón agregado "WAIT/GO mejor que AVOID". `cross_instrument` en 1m
  ve a YM cruzar a E[R] negativo por primera vez en varios días. `tier=B`
  cruza a positivo, `tier=C` sostiene su cuarta lectura positiva
  seguida. Nada accionable nuevo.
- 2026-09-16 (miércoles): "forced update" habitual de `origin/main`
  (shallow clone, sin pérdida). Día casi sin actividad: n 128→129 (+1,
  todo en 1m, un solo par ganador/TO). Sin hallazgos nuevos: todas las
  ramas con cero pares nuevos hoy (2m, 5m, `cross_instrument`, SL
  estructural en 2m/5m) quedan exactamente iguales a ayer. `tier=C`
  suma su tercera lectura positiva seguida. Sigue siendo el playbook con
  menos actividad del bus.
- 2026-09-15 (martes): otro "forced update" de `origin/main` al inicio
  (mismo patrón inofensivo de otras corridas). n 121→128 (+7; 1m+5,
  2m+2, 5m sin cambio). Nada fuerte nuevo: `tier=C` sostiene su segunda
  lectura positiva seguida (moderándose un poco), 2m se debilita hacia
  breakeven. Nota de método: el 5m INV/SHORT (n=8) NO certifica FDR hoy,
  a diferencia del 5m INV/LONG de `buy-ifvg.md` que sí lo hace con un
  tamaño de muestra igual de pequeño — ilustra que "certifica" con n<20
  es ruido en cualquier dirección, no tratar ninguno de los dos como
  señal real.
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
