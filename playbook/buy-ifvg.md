# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-21 (lunes) · n: 191)

### Nota de proceso
Mismo incidente de repo inofensivo de siempre (ver `buy-retest.md`).
Hoy llegó poco dato INV/LONG nuevo (n 186→191, +5, repartido en los tres
TF) frente al volumen de RETEST.

### Veredicto global
1m n=131 (+1, WR 42.0%, E[R]=**0.002** PF=1.0, 60 SL — sigue casi plano
tras el retroceso de hace unos días); 2m n=43 (+3, WR 51.2%,
E[R]=**-0.102** PF=0.76, 17 SL — sigue siendo la peor rama por lejos);
5m n=17 (+1, WR 64.7%, E[R]=0.407 PF=3.03 — sube un poco, sigue con
muestra mínima).
`segment_significance`: 1m CI90=[-0.172,0.181] p=0.506 n=122 (sigue
lejos de certificar); 2m CI90=[-0.309,0.115] p=0.767 n=41 (sin cambio de
fondo); **5m CI90=[0.031,0.819] p=0.04 n=15 — vuelve a marcar
`survives_fdr10=true`** (lo había perdido y recuperado varias veces) —
con n=15, muy por debajo del piso n≥20 del playbook, se trata igual que
siempre: **no usable**, ejemplo de lo volátil que es esta bandera con
muestra tan chica.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar en ninguna rama:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | sigue negativo, estable | 108 (+4) | E[R]=**-0.05** (~idéntico a -0.052) | baja — se estabiliza en negativo, todavía sin asentarse del todo |
| 2 | `tier=B` vs `tier=C` | **B sigue peor, C sigue mejor** | 52 (+1) vs 139 (+4) | E[R] **-0.149** (B, mejora un poco de -0.164) vs +0.075 (C, baja de +0.091) | baja — la separación se mantiene direccionalmente, ambas ramas se mueven poco |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- `managed_vs_naive`: 1m n=122 delta=**+0.209** (~estable); 2m n=41
  delta=**+0.035** (baja un poco, casi sin edge); 5m n=15
  delta=**-0.132** (menos negativo que -0.168, sigue negativo con
  muestra mínima).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=122 (+1)
  delta=**-0.177** CI90=[-0.453,0.104] no certifica (sigue siendo
  ruido); 2m n=41 (+3) delta=**+0.673** CI90=[-0.075,1.516] (sube de
  +0.599, sigue sin certificar); 5m n=15 (+1) delta=**-0.809**
  CI90=[-1.327,-0.334] — sigue `delta_below_zero=true` (aquí el SL de 3
  capas gana, patrón contrario a RETEST, pero n=15 sigue sin ser lectura
  usable). Sin propuesta en `experiments.json` para INV/LONG.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
Sin dato SA nuevo que cruce hoy con INV/LONG — cifras idénticas a ayer:
`WAIT` n=47 E[R]=**-0.216**, `AVOID` n=13 E[R]=**-0.028**, `GO` n=10
E[R]=**-0.126**. Con n=10-47 sigue siendo muestra chica sin patrón
estable — no usar todavía para nada accionable.

### Contextos a evitar
- Autopsia de SL sobre las 80 pérdidas INV/LONG (+2 vs ayer): `RR-bajo`
  38/80 (47.5%) se mantiene como causa dominante (segunda corrida
  seguida, confirma que el cambio de orden del 09-20 no fue ruido de un
  día), `killzone-Asia-largo` 34/80 (42.5%) segundo,
  `contra-estructura` 23/80 (28.8%) tercero.
- `cross_instrument` (1m) sigue `instrument-specific`, spread baja a
  0.967 (desde 1.02): CL n=30 E[R]=0.411 (sigue el mejor), YM n=49
  (+0) E[R]=0.016, ES n=19 (+0) E[R]=-0.112, NQ n=12 (+0) E[R]=0.099,
  GC n=21 (+0) E[R]=**-0.556** (sigue el peor símbolo por lejos) — n por
  símbolo sigue chico, no generalizar.

### Decaimiento
_pendiente_ (WR TP1 por semana; marcar si cae > 15 pts en ventana de 3 semanas)

## Histórico de cambios
- 2026-09-21 (lunes): dato nuevo escaso (n 186→191, +5) frente al
  volumen de RETEST. `RR-bajo` se sostiene como causa dominante de SL
  por segunda corrida seguida (47.5% de 80 pérdidas), confirmando que el
  cambio de orden del 09-20 no fue ruido de un día. `segment_significance`
  en 5m vuelve a marcar `survives_fdr10=true` (n=15, todavía muy por
  debajo del piso n≥20 del playbook, no usable). Nada accionable nuevo:
  sigue siendo prioridad 2, ningún TF con n suficiente para proponer
  cambios.
- 2026-09-20 (domingo, revisión semanal): sin archivo de datos nuevo
  (fin de semana) y las 37 señales resueltas por TIMEOUT forzado en todo
  el bus cayeron todas en RETEST — este playbook queda con n=186 y todas
  sus métricas idénticas a ayer, sin excepción. Ver `reviews/2026-week-38.md`
  para el cierre de semana del bus completo.
- 2026-09-19 (sábado): mismo incidente de repo que `buy-retest.md`
  (`origin/main` reescrito río arriba, sin pérdida). n 162→186 (+24;
  1m+18, 2m+5, 5m+1) — salto algo mayor a lo habitual para este
  playbook de prioridad 2. **1m retrocede fuerte** (E[R] 0.102→0.011,
  primer retroceso marcado tras varias corridas estables). **Hallazgo
  del día: la autopsia de SL invierte su causa dominante** —
  `RR-bajo` (46.2%) adelanta a `killzone-Asia-largo` (41.0%, venía
  siendo dominante con 50.0%) — rompe el patrón "INV/LONG es distinto de
  RETEST" que se reportaba como estable desde hace días; con n=78
  todavía chico, tratar como cambio a confirmar. En el cruce con Session
  Analyst las tres ramas (GO/WAIT/AVOID) dan negativo por primera vez
  simultáneamente, con `WAIT` empeorando fuerte (-0.106→-0.216). Nada
  accionable nuevo: sigue siendo prioridad 2, ningún TF con n suficiente
  para proponer cambios.
- 2026-09-18 (viernes): mismo incidente de repo que `buy-retest.md`
  (`origin/main` reescrito río arriba, sin pérdida). n 157→162 (+5;
  1m+2, 2m+2, 5m+1) — vuelve al ritmo mínimo habitual. El 5m pierde la
  certificación FDR que sostenía desde hacía varias corridas (n=13,
  sigue muy por debajo del piso n≥20, sin impacto práctico). `tier=B`
  sigue negativo, `tier=C` estable arriba. En el cruce con Session
  Analyst, `AVOID` vuelve a negativo (-0.072, venía de +0.013) y `WAIT`
  se mantiene negativo por segunda corrida — sigue sin patrón usable con
  n=9-36. Nada accionable nuevo: sigue siendo prioridad 2, ningún TF con
  n suficiente para proponer cambios.
- 2026-09-17 (jueves): mismo incidente inofensivo de repo que
  `buy-retest.md`. Salto de dato el más grande en varios días para este
  playbook (n 131→157, +26; 1m+22, 2m+3, 5m+1). **2m mejora bastante**
  (E[R] -0.159→-0.111) aunque sigue siendo la peor rama. `tier=B` cruza
  a negativo por primera vez mientras `tier=C` sigue subiendo — primera
  vez que se separan con claridad. En el cruce con Session Analyst, la
  rama `WAIT` cruza a negativo por primera vez (+0.14→-0.078) el mismo
  día que `buy-retest.md` reporta su rama `AVOID` cruzando a negativo —
  ambos playbooks LONG se mueven hoy, sin patrón consistente todavía
  entre INV y RETEST. Nada accionable nuevo: sigue siendo prioridad 2,
  ningún TF con n suficiente para proponer cambios.
- 2026-09-16 (miércoles): "forced update" habitual de `origin/main`
  (shallow clone, sin pérdida). n 123→131 (+8; 1m+4, 2m+1, 5m+3).
  **5m rompe su congelamiento de 3 días** con 3 señales nuevas (WR
  90%→76.9%, E[R] 0.849→0.788) — primer movimiento real en esa rama
  desde el 09-13, sigue siendo `survives_fdr10=true` pero todavía muy
  por debajo del piso n≥20, no accionable. Sin hallazgos fuertes nuevos:
  `tier=C` sostiene su ventaja sobre `tier=B` por segunda lectura
  seguida (brecha se achica un poco). Causa dominante de SL sin cambios
  (`killzone-Asia-largo`).
- 2026-09-15 (martes): otro "forced update" de `origin/main` al inicio
  (mismo patrón inofensivo de otras corridas). n 111→123 (+12; 1m+9,
  2m+3, 5m sin cambio, congelado por tercer día). Sin hallazgo nuevo
  fuerte: `tier=C` adelanta a `tier=B` por primera vez (muestra todavía
  chica en ambos), y por primera vez `GO`/`AVOID` del cruce con Session
  Analyst alcanzan el piso mínimo de reporte (n=5, ambos anecdóticos).
  La causa dominante de SL sigue siendo `killzone-Asia-largo`, distinta
  a la de RETEST (`RR-bajo`) — patrón estable desde hace varios días.
- 2026-09-14 (lunes): `git pull` limpio, sin incidentes. n 108→111 (+3;
  1m+2, 2m+1, 5m sin cambio). **`2m/INV/LONG` se recupera de n=25 a
  n=26**, confirmando que la baja de ayer era re-pareo/dedup y no pérdida
  real — pero al mismo tiempo **pierde la certificación de
  `sl_origin_vs_layer`** que tenía ayer (CI90 vuelve a cruzar cero pese a
  que el delta apenas cambió), ilustrando lo frágil que es esta rama con
  n=26: un solo par nuevo mueve el límite del CI90 de un lado a otro de
  cero. Nada más accionable: día de muestra mínima en este segmento de
  prioridad 2.
- 2026-09-13 (domingo, REVISIÓN SEMANAL): n 102→108 (+6; 1m+7, 2m-1,
  5m sin cambio). Incidente menor de repo, ver `buy-retest.md`.
  **Primera alerta de muestra propia de este playbook**: `2m/INV/LONG`
  bajó de n=26 a n=25 (aparece en `report.alerts`); `file_integrity_check`
  confirma que ningún archivo crudo encogió, así que es re-pareo/dedup
  del agregado, no pérdida real — la misma corrida también mostró
  `tier=B` bajando de n=30 a 28, mismo tipo de ruido de recuento. El SL
  estructural en 2m sigue certificando y mejora pese al n menor (delta
  1.066→1.109, límite inferior del CI90 sube de 0.007 a 0.045). Sin
  propuesta nueva para `experiments.json` en este segmento (prioridad 2,
  n por debajo del piso cómodo de evidencia).
- 2026-09-12 (sábado): n 100→102 (+2, todo en 1m), sin incidentes de
  repo. Segmento casi congelado hoy: 2m y 5m sin señales nuevas (idénticas
  a ayer en todas las métricas). 1m recupera la racha de subida
  (E[R] 0.097→0.129). Autopsia de SL sostiene el mismo orden por segundo
  día (`killzone-Asia-largo` > `RR-bajo` > `contra-estructura`).
- 2026-09-11 (viernes): n 82→100 (+18; 1m+11, 2m+4, 5m+3), la muestra más
  grande sumada en un día en este playbook. Mismo incidente de repo que
  `buy-retest.md` (reset a `origin/main`, sin pérdida de datos). 1m
  retrocede de E[R]=+0.225 a +0.097 (primer retroceso tras varios días
  subiendo). `segment_significance` marca `survives_fdr10=true` en 5m por
  primera vez (n=10, PF=99) — explícitamente **no accionable**, muy por
  debajo del piso n≥20 del playbook. `sl_origin_vs_layer` en 2m sigue
  certificando pero al filo (límite inferior del CI90 cayó a 0.007); en
  5m aparece con CI calculable por primera vez y certifica en sentido
  CONTRARIO a 2m (el SL de 3 capas gana, no el estructural), con n=10.
  Autopsia de SL: `killzone-Asia-largo` desplaza a `RR-bajo` como causa
  más frecuente (48.8% vs 46.5%, antes RR-bajo dominaba solo con 56%).
- 2026-09-11 (viernes): n 82→100 (+18; 1m+11, 2m+4, 5m+3), la muestra más
  grande sumada en un día en este playbook. Mismo incidente de repo que
  `buy-retest.md` (reset a `origin/main`, sin pérdida de datos). 1m
  retrocede de E[R]=+0.225 a +0.097 (primer retroceso tras varios días
  subiendo). `segment_significance` marca `survives_fdr10=true` en 5m por
  primera vez (n=10, PF=99) — explícitamente **no accionable**, muy por
  debajo del piso n≥20 del playbook. `sl_origin_vs_layer` en 2m sigue
  certificando pero al filo (límite inferior del CI90 cayó a 0.007); en
  5m aparece con CI calculable por primera vez y certifica en sentido
  CONTRARIO a 2m (el SL de 3 capas gana, no el estructural), con n=10.
  Autopsia de SL: `killzone-Asia-largo` desplaza a `RR-bajo` como causa
  más frecuente (48.8% vs 46.5%, antes RR-bajo dominaba solo con 56%).
- 2026-09-10 (jueves): a diferencia del resto del bus (salto grande de
  dato, ver `buy-retest.md`), este segmento apenas creció (+3, n 79→82) —
  sigue siendo el playbook con menos actividad. `sl_origin_vs_layer` en 2m
  sostiene su certificación por tercer día seguido (delta+1.394,
  CI90=[0.185,2.804]). Autopsia de SL sin cambios (cero SL nuevos).
- 2026-09-09 (miércoles): día de confirmación, sin dato fechado hoy —
  solo +2 pares en 1m (TO, sin SL nuevo), 2m/5m sin cambio. Todas las
  cifras coinciden con ayer salvo el cruce con Session Analyst, cuyo
  `n_matched` global creció mucho (ver `sell-retest.md`) y por primera vez
  muestra una celda `GO` en este segmento (n=5, E[R]=-0.212, mismo sentido
  que el hallazgo agregado AVOID>GO).
- 2026-09-03: primeros datos reales, n=0→3 (1m n=2, 2m n=1). Sin valor
  estadístico todavía; se deja constancia. Sigue siendo el segmento con
  menos muestra de los cuatro playbooks — prioridad 2 confirmada.
- 2026-09-04: salto grande n=3→48 (1m 2→30, 2m 1→12, 5m 0→2, primeros
  datos 5m). Primera lectura con algo de valor: 1m E[R]=+0.428, cerca del
  borde de significancia (p=0.059) pero sin certificar FDR todavía. Nuevo
  hallazgo a vigilar sin accionar: `sl_origin_vs_layer` en 2m bate cero
  con un efecto grande (+2.472) pero n=12, muy por debajo del piso de
  n=20 — no se propone nada, solo se deja constancia. Autopsia de SL:
  `killzone-Asia-largo` domina (58% de las pérdidas), distinto al patrón
  de RETEST donde `RR-bajo`/`contra-estructura` lideran.
- 2026-09-05: refresco n=48→63 (1m 30→40, 2m 12→18, 5m 2→5), en parte por
  la restauración de `signals/2026-09-03.jsonl` (ver nota al inicio de la
  Sección viva y detalle completo en `buy-retest.md`). Todas las lecturas
  se mantienen en la misma dirección que ayer, sin sorpresas: 1m sigue
  positivo pero se alejó un poco del borde de significancia (p=0.059→0.101),
  `sl_origin_vs_layer` en 2m sigue batiendo cero con efecto grande
  (+2.472→+1.708, n=12→18, todavía bajo el piso de n=20). A diferencia de
  BUY/SELL RETEST, aquí la restauración de datos no cambió ningún signo —
  este playbook ya tenía muestra chica y por lo tanto poco que corregir.
- 2026-09-06 (revisión semanal, domingo): n sin cambios (63) — CME cerrado
  el fin de semana, cero signals/outcomes nuevos. El bug de `heal` que
  truncó `signals/2026-09-03.jsonl` se repitió una segunda vez (commit
  `0cf0a30`) y se restauró de nuevo; ver nota de proceso arriba y
  `experiments.json`/`analyze.py` (guarda `file_integrity_check` nueva).
  Ver `reviews/2026-week-36.md` para la revisión semanal completa.
- 2026-09-07 (lunes, festivo EE.UU.): primer día sin repetición del bug de
  "heal", con algo de dato nuevo genuino (n=63→66: 1m 40→42, 5m 5→6, 2m
  sin cambio en 18). Primera vez con fila propia de `managed_vs_naive` en
  1m (delta+0.113) y 5m (delta+0.191), ambas ayudan. Primera lectura de
  `sl_origin_vs_layer` en 5m: delta negativo (-1.255, n=6 mínimo, sentido
  opuesto al de 2m) — anotado sin accionar. Primera lectura de
  `cross_instrument` en este segmento (`instrument-specific`, spread
  1.109, YM/CL positivos, ES/GC negativos, n por símbolo muy chico).
- 2026-09-08 (martes, primer día hábil completo post-feriado): n=66->77
  (1m 42->50, 2m 18->20, 5m 6->7). **`sl_origin_vs_layer` en 2m llegó al
  piso de n=20 del método y certifica** (delta+1.538, CI90 [0.243,3.13],
  no cruza cero) — primera vez que esta rama de INV/LONG entra en
  territorio "tratable como real"; efecto muy grande para un n tan chico,
  vigilar que no se diluya como pasó con otras lecturas de n justo en el
  piso en este bus. Mejora permanente en `analyze.py`:
  `session_analyst_cross.by_kind_side` da su primera celda para este
  segmento (WAIT n=7, E[R]=+0.437, insuficiente para comparar contra
  AVOID/GO). Ver `sell-retest.md` para el hallazgo mayor del día (SA
  AVOID rinde mejor que GO, ahora con CI90 estadístico real).
