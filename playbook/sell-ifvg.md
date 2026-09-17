# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-17 · n: 131)

### Nota de proceso
Mismo incidente inofensivo de repo que `buy-retest.md` (HEAD detached,
resuelto sin pérdida). Este segmento apenas se movió: n 129→131
(**+2**; todo en 1m — sigue siendo el playbook con menos actividad del
bus hoy, junto a `buy-ifvg.md` 2m/5m).

### Veredicto global
1m n=84 (+2, WR 50.0% idéntico, E[R]=**+0.096** PF=1.22, sin SL nuevos
— baja un poco de +0.124); 2m n=39 (sin cambio, cero pares nuevos, WR
35.9%, E[R]=+0.017 PF=1.03, idéntico); 5m n=8 (sin cambio, congelado por
QUINTO día, WR 75.0%, E[R]=+0.615 PF=3.46). `segment_significance`: 1m
CI90=[-0.116,0.328] p=0.237 n=81 (prácticamente sin cambio, sigue lejos
de certificar); 2m CI90=[-0.335,0.412] p=0.477 n=39 (idéntico, sin dato
nuevo); 5m CI90=[-0.057,1.309] p=0.072 n=8 — **sigue sin certificar** (a
diferencia del 5m INV/LONG de `buy-ifvg.md`, que sigue certificando con
un tamaño de muestra similar — mismo recordatorio de que "certifica FDR"
con n<20 puede ir en cualquier dirección, no es señal real en ninguno de
los dos casos).

### Reglas condicionales (IF contexto ENTONCES acción)

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=-1` | sigue siendo la mejor rama grande, sin cambio (cero pares nuevos) | 75 (+0) | E[R]=**+0.133** (idéntico) | baja-moderada — mismo signo por quinta corrida |
| 2 | `nearEdge=0` | sin cambio (los 2 pares nuevos cayeron en otras ramas) | 46 (+0) | E[R]=**-0.038** (idéntico) | moderada — sigue negativo, sin dato nuevo hoy |
| 3 | `tier=B` | **cruza a positivo, se acerca a tier=C** | 39 (+0 en conteo, sube igual por recálculo interno) | E[R]=**+0.096** (bajó de +0.162, el par nuevo repartió peso) | baja — un solo par nuevo mueve bastante con n=39, no fijar todavía |
| 4 | `tier=C` | **sostiene la vuelta a positivo por cuarta lectura seguida** | 92 (+2) | E[R]=**+0.108** (subió de +0.104) | baja-moderada — cuarta lectura positiva seguida, empieza a parecer más que ruido pero todavía sin confirmar |

`nearEdge=1` se mantiene congelado en n=8 (sin señales nuevas) — sigue
siendo ruido de muestra mínima, no generalizar.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: 1m n=81 delta=**+0.2** (sube de +0.188, sigue
  ayudando bastante, cada vez más); 2m n=39 delta=**-0.061** (idéntico,
  cero pares nuevos); 5m n=8 delta=+0.042 (sin cambio, congelado).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): **1m se da
  vuelta de signo con un solo par nuevo**: n=71 (+1) delta=**-0.193**
  CI90=[-0.551,0.194] (antes +0.243, orig_expR pasó de +0.377 a -0.091)
  — sigue sin certificar (CI90 cruza cero en ambos sentidos), pero es un
  recordatorio explícito de método: con n=70-71 un solo par nuevo puede
  invertir el signo del delta, no tratar esta rama como lectura estable
  en ninguna dirección; 2m n=38 (sin cambio) delta=**+0.411** CI90=
  [-0.059,1.034] (idéntico, cero pares nuevos, sigue sin certificar); 5m
  n=7 (sin cambio) delta=-0.821 (sin cambio, muestra demasiado chica
  para concluir nada). Ninguno certifica todavía. No tocar el SL en
  INV/SHORT.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
INV/SHORT bajo veredicto SA `AVOID` n=23 (-1, re-pareo, `file_integrity_check`
limpio) E[R]=**-0.333** (empeora bastante desde -0.188) PF=0.44 y `WAIT`
n=22 (+2) E[R]=**-0.12** (mejora desde -0.174 con los pares nuevos)
PF=0.71 — sigue siendo el único playbook del bus que no muestra el
patrón agregado "WAIT/GO mejor que AVOID" de
`buy-retest.md`/`sell-retest.md`; aquí las dos ramas con muestra
utilizable siguen rindiendo negativo.

### Contextos a evitar
- Autopsia de SL sobre las 59 pérdidas INV/SHORT (sin cambio, ningún par
  nuevo del día fue SL): `RR-bajo` 30/59 (50.8%) sigue siendo la causa
  dominante, séptimo+ día con el mismo orden; `contra-estructura` 18/59
  (30.5%) y `stop-en-el-minimo` 17/59 (28.8%) se mantienen
  segundo/tercer lugar.
- `cross_instrument` (1m) sigue `instrument-specific` (spread sube de
  0.522 a 0.582): YM n=51 (-1) E[R]=**-0.012** (**cruza a negativo**,
  antes +0.048 — primer símbolo negativo de esta tabla en varios días),
  GC n=18 (+3) E[R]=0.188 (sube de 0.157), NQ n=9 E[R]=0.19 (sin
  cambio), ES n=6 E[R]=0.57 (sin cambio) — n por símbolo sigue chico
  (6-51), no generalizar; vigilar si YM se sostiene en negativo.

### Decaimiento
`decay_weekly` (global): 2026-W36 n=3135 (bajó de 3140 por dedup, ver
`buy-retest.md`); 2026-W37 n=5338 (bajó de n=5375 por -37, la caída más
grande vista hasta ahora) E[R]=+0.07; 2026-W38 n=2211 (subió fuerte de
1072) E[R]=+0.123 — este segmento sigue sin suficiente muestra propia
por semana para medir decaimiento aislado.

## Histórico de cambios
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
