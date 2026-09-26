# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-25 (viernes) · n: 193)

### Nota de proceso
`git pull` con "forced update" habitual de `origin/main` (shallow
clone, sin pérdida, ver `buy-retest.md`). Dato nuevo notable para este
playbook: n 166→193 (+27: 1m+15, 2m+11, 5m+1) — el salto más grande en
varias corridas para INV/SHORT, contrasta con `buy-ifvg.md` que no tuvo
ningún par nuevo hoy.

### Veredicto global
1m n=125 (+15, WR 50.4%, E[R]=**+0.072** PF=1.17 — sube bastante de
+0.025); 2m n=56 (+11, WR 41.1%, E[R]=**+0.118** PF=1.25 — **cruza a
positivo**, sube fuerte de -0.029); 5m n=12 (+1, WR 66.7%, E[R]=+0.392
PF=2.44 — prácticamente sin cambio de fondo vs +0.413).
`segment_significance`: 1m CI90=[-0.095,0.25] p=0.247 n=120 (mejora
pero sigue lejos de certificar); 2m CI90=[-0.185,0.437] p=0.264 n=54
(mejora bastante el rango pero sigue cruzando cero); 5m
CI90=[-0.14,0.965] p=0.115 n=11 (sigue sin certificar) — ningún TF de
este playbook certifica FDR hoy, mismo recordatorio de que con n<20 la
bandera FDR no es señal real en ninguno de los dos playbooks INV. **El
salto de 1m y 2m a E[R] más positivo con +26 pares nuevos combinados es
la primera mejora de este tamaño en varias corridas — tratar como una
sola lectura, no como cambio de régimen, hasta 2-3 confirmaciones
más.**

### Reglas condicionales (IF contexto ENTONCES acción)

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=-1` | positivo, se fortalece | 107 (+12) | E[R]=**+0.065** (sube de +0.024) | baja — sigue chico, quinto vaivén distinto en pocas corridas |
| 2 | `nearEdge=0` | **cruza a positivo** | 77 (+15) | E[R]=**+0.088** (sube de -0.049) | baja — vaivén, n todavía chico |
| 3 | `nearEdge=1` | positivo fuerte, n mínimo, sin dato nuevo | 9 (+0) | E[R]=**+0.69** | muy baja — n=9, no usable |
| 4 | `tier=B` | **cruza a positivo** | 55 (+9) | E[R]=**+0.038** (sube de -0.037) | baja |
| 5 | `tier=C` | se fortalece | 138 (+18) | E[R]=**+0.132** (sube de +0.062) | baja-moderada |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- `managed_vs_naive`: 1m n=120 delta=**+0.14** (sube de +0.126, sigue
  ayudando bastante); 2m n=54 delta=**-0.016** (mejora hacia cero desde
  -0.039, sigue negativo); 5m n=11 delta=+0.066 (baja un poco de
  +0.072, sin dato robusto todavía).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=110 (+13)
  delta=**+0.051** CI90=[-0.327,0.478] — baja de +0.091, sigue
  cruzando cero en ambos sentidos, sigue siendo ruido de muestra
  chica, no cambio real; 2m n=53 (+9) delta=**+0.244** CI90=[-0.219,0.794] (baja
  de +0.445, el límite inferior se aleja un poco de cero sin
  cruzarlo, vigilar); 5m n=10 (+1) delta=**-0.814** CI90=[-1.197,-0.429]
  — sigue siendo la única lectura de este playbook con CI90 que no
  cruza cero, pero n=10 sigue muy por debajo del piso n≥20 del playbook.
  Ninguno certifica de forma usable todavía. No tocar el SL en
  INV/SHORT.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
`AVOID` n=22 (+0, sin señales nuevas en el join de hoy) E[R]=**-0.403**
PF=0.35 (sin cambio) y `WAIT` n=57 (+19) E[R]=**+0.052** PF=1.13 —
**cruza a positivo por primera vez en este playbook** tras varias
corridas negativo (-0.232), rompiendo por primera vez el patrón de que
INV/SHORT no mostraba el orden "WAIT/GO mejor que AVOID" de
`buy-retest.md`/`sell-retest.md`; con n=57 y una sola lectura, tratar
como candidato a confirmar, no como hallazgo firme todavía.

### Contextos a evitar
- Autopsia de SL sobre las 79 pérdidas INV/SHORT (+3 vs ayer): mismo
  orden — `RR-bajo` 37/79 (46.8%) sigue siendo la causa dominante (baja
  el % sólo por el denominador, cuenta idéntica); `contra-estructura`
  22/79 (27.8%) sin cambio de cuenta, `stop-en-el-minimo` 20/79 (25.3%,
  +1) se mantienen segundo/tercer lugar.
- `cross_instrument` (1m) sigue spread 0.748 (sin cambio) y sigue
  `instrument-specific`: CL n=13 (+1) E[R]=-0.178 (sin cambio), YM n=68
  (+9) E[R]=**-0.019** (mejora bastante de -0.073),
  GC n=27 (+4) E[R]=**0.285** (sube de 0.216), NQ n=11 (+1) E[R]=0.092
  (sube un poco de 0.071), ES n=6 (+0) E[R]=0.57 (sin cambio) — n por
  símbolo sigue chico (6-68), no generalizar.

### Decaimiento
`decay_weekly` (global): 2026-W36 n=2963 (sigue bajando por dedup, ver
`buy-retest.md`); 2026-W37 n=5131 E[R]=+0.074; 2026-W38 n=4763
E[R]=+0.093; 2026-W39 n=3708 E[R]=+0.14 — este segmento sigue sin
suficiente muestra propia por semana para medir decaimiento aislado.

## Histórico de cambios
- 2026-09-25 (viernes): `git pull` con "forced update" habitual de
  `origin/main` (shallow clone, sin pérdida). **Dato nuevo notable para
  este playbook** (+27, el salto más grande en varias corridas: 1m+15,
  2m+11, 5m+1). 1m y 2m mejoran fuerte en E[R] (1m +0.025→+0.072, 2m
  **cruza a positivo** -0.029→+0.118), y en el cruce con Session
  Analyst **`WAIT` cruza a positivo por primera vez en este playbook**
  (-0.232→+0.052, n=38→57) — hasta ahora este era el único playbook del
  bus sin el patrón "WAIT/GO mejor que AVOID". Con una sola lectura de
  este tamaño, tratar ambos movimientos como candidatos a confirmar, no
  como cambio de régimen todavía — vigilar las próximas 2-3 corridas
  antes de actualizar el veredicto de este playbook. Ningún TF certifica
  FDR todavía (`survives_fdr10=false` en los tres). Sin n suficiente
  para proponer nada en `experiments.json`.
- 2026-09-24 (jueves): dato nuevo mínimo (+5, 1m+3/2m+1/5m+1). Sin
  hallazgos accionables: `sl_origin_vs_layer` en 1m INV/SHORT cambia de
  signo (-0.084→+0.091) con sólo 4 pares nuevos — ruido de muestra
  chica, ambos CI90 cruzan cero, no tratar como giro real. `nearEdge=1`
  aparece por primera vez con n≥5 (n=9, E[R]=+0.69) pero sigue muy por
  debajo de cualquier umbral usable. Cruce con Session Analyst sin dato
  nuevo (AVOID/WAIT idénticos a ayer). Autopsia de SL sin pérdidas
  nuevas en ninguna de las tres causas principales. Sigue sin n
  suficiente en ningún TF para proponer nada en `experiments.json`.
- 2026-09-23 (miércoles): dato nuevo chico otra vez (+9: 1m+4, 2m+0,
  5m+1). Sin hallazgos de fondo nuevos: ninguna rama certifica FDR,
  `sl_origin_vs_layer` sigue sin certificar de forma usable en ningún
  TF (5m es la única con CI90 fuera de cero pero n=8, bajo el piso del
  playbook). Nota menor de método: `AVOID` en el cruce con Session
  Analyst bajó de n=23 a n=22 pese a ser agregado — probablemente
  re-pareo de fecha/sesión, no pérdida de archivo
  (`file_integrity_check` limpio); vigilar si se repite.

## Histórico de cambios
- 2026-09-23 (miércoles): dato nuevo chico (+9), sin hallazgos nuevos
  de fondo. Todas las ramas de Session Analyst empeoran un poco (AVOID
  y WAIT ambas más negativas) pero sin significancia — sigue siendo el
  único playbook sin el patrón "WAIT/GO mejor que AVOID". Nota de método:
  el agregado `AVOID` del cruce con Session Analyst bajó de n=23 a n=22
  (un agregado normalmente no encoge) — probablemente re-pareo de
  fecha/sesión, `file_integrity_check` sigue limpio, vigilar si se
  repite. Sin n suficiente en ningún TF para proponer nada en
  `experiments.json`.
- 2026-09-22 (martes): dato nuevo escaso otra vez (n 146→152, +6) pese
  al lote grande que asentó el resto del bus (+1027 outcomes, ver
  `buy-retest.md`) — INV/SHORT sigue siendo la señal de menor volumen
  del indicador. `tier=B` cruza a negativo por primera vez (E[R]
  +0.015→-0.007). `cross_instrument` en 1m se normaliza (spread
  1.126→0.756): el salto de CL de ayer (n=6, E[R]=-0.556) era ruido de
  muestra mínima, confirmado con las 4 señales nuevas (E[R]→-0.186).
  Nada accionable nuevo: sigue siendo prioridad 2, ningún TF certifica
  FDR de forma usable.
- 2026-09-21 (lunes): primer día hábil completo con dato nuevo genuino
  en el resto del bus (+72 pares, ver `buy-retest.md`) que deja este
  playbook exactamente plano (n=146, 96/41/9 por TF, cero señales
  INV/SHORT nuevas) — sin fallo de pipeline, simplemente no hubo señales
  de este tipo hoy. Nada accionable nuevo.
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
