# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-10-10 (sábado) · n: 378)

### Nota de proceso
`git pull` encontró `HEAD` detached por un `main` local desactualizado,
sin incidente de fondo (ver `buy-retest.md`). Dato nuevo chico
(+15/+7/+2 en 1m/2m/5m) — INV sigue siendo mucho más esporádico que
RETEST. INV queda fuera de `shadowRules`, sin cambio.

`sl_origin_vs_layer.since_change` (`candle1`) confirma el mismo patrón
mixto de siempre con un poco más de muestra: **ayuda en 1m** (n=98,
delta=**+0.4** CI90=[0.003,0.821], confirma, al filo) pero **perjudica
en 2m** (n=41, delta=**-0.416** CI90=[-0.71,-0.1], confirma negativo);
5m sigue sin muestra suficiente (n=12, delta=+0.257 CI90=[-0.619,1.302],
no certifica). Sigue correcto que `sl-retest-wick` se limitara a
`kind=RETEST`. Único punto a vigilar sin alarmar: `2m/INV/LONG`
pierde significancia agregada esta corrida (E[R] pasa de +0.039 a
**-0.013**, CI90=[-0.175,0.167] ahora cruza cero, `survives_fdr10`
pasa a `false`) — con n=96 es ruido de muestra chica, no decaimiento,
pero ya no se puede citar como segmento confirmado.

### Veredicto global
1m n=248 (+15) WR 46.8% E[R]=**0.156** PF=1.36 (baja un poco vs 0.173,
dentro de ruido); 2m n=100 (+7) WR 50.0% E[R]=**-0.013** PF=0.97 (cruza
a negativo, ver Nota de proceso); 5m n=30 (+2) WR 73.3% E[R]=**0.374**
PF=3.53 (sigue siendo el mejor TF, n todavía muy chico para confiar).
`segment_significance`: 1m CI90=[0.013,0.308] n=237 sigue
`survives_fdr10=true` p=0.039; **2m CI90=[-0.175,0.167] n=96 YA NO
certifica** (antes sí); 5m CI90=[0.12,0.622] n=27 sostiene
`survives_fdr10=true` p=0.004 (n demasiado chico para confiar).

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar en más de una rama:

| # | SI | ENTONCES (hipótesis, sin confirmar salvo 1m) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tf=1m` (`survives_fdr10=true`) | TOMAR, único segmento de este playbook con n usable | 237 | E[R]=**0.156** CI90=[0.013,0.308] | moderada-alta |
| 2 | `tf=2m` | **dejó de certificar hoy** (CI90 cruza cero) — tratar como sin edge confirmado, n=96 sigue siendo chico | 96 | E[R]=**-0.013** CI90=[-0.175,0.167] | baja — vigilar, no proponer cambio con este n |
| 3 | mover SL a vela 1 del FVG (`candle1`) | **NO proponer** — ayuda en 1m (al filo) pero perjudica con significancia en 2m | 98 (1m) / 41 (2m) | delta +0.4 (1m, al filo) / -0.416 (2m, confirma negativo) | moderada |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`).

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=237 delta=**+0.082**;
  2m n=96 delta=**+0.08**; 5m n=27 delta=**+0.012** (débil en 5m, sin
  cambio de fondo). Sin cambio de regla.
- **SL de 3 capas vs SL = vela 1 del FVG**: ver Nota de proceso — mixto,
  no proponer cambio.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL (INV/LONG, n=148): `killzone-Asia-largo` 68/148 (45.9%)
  dominante, `RR-bajo` 54/148 (36.5%) segundo, `contra-estructura` 46/148
  (31.1%) tercero — sin cambio de fondo.

### Cruce con Session Analyst
`session_analyst_cross.by_kind_side` (muestra todavía chica): `AVOID`
n=33 E[R]=**-0.025**; `GO` n=24 E[R]=**0.18**; `WAIT` n=134
E[R]=**-0.044** — GO sigue el mejor, consistente con la hipótesis
general, pero AVOID y WAIT siguen chicos para una lectura propia
confiable. Cifras globales con CI90 en `buy-retest.md`.

### Decaimiento
`decay_weekly_by_segment`: ningún TF de este playbook tiene todavía
muestra semanal suficiente para separar señal de ruido. El cambio de
signo de `2m/INV/LONG` en agregado (ver Nota de proceso) es el único
punto a vigilar, sin tratarlo como decaimiento real todavía (n chico).

## Histórico de cambios
- 2026-10-10 (sábado): `2m/INV/LONG` pierde significancia agregada
  (E[R] +0.039→-0.013, `survives_fdr10` true→false) — con n=96 se
  trata como ruido de muestra chica, no como decaimiento, pero deja de
  poder citarse como segmento confirmado. Resto sin cambio de fondo;
  dato nuevo chico +15/+7/+2 (1m/2m/5m).
- 2026-10-09 (viernes): `origin/main` llegó con el historial git
  reescrito — ver nota completa en `buy-retest.md`, sin pérdida de
  contenido. Dato nuevo chico +5/+6/+1 (1m/2m/5m). Sin hallazgo nuevo
  material: `sl_origin_vs_layer` confirma el mismo patrón mixto de ayer
  con un poco más de muestra (1m ayuda, 2m perjudica, 5m sin dato nuevo).
  GC sigue siendo el único símbolo negativo en 1m INV LONG, mejora algo
  (-0.275→-0.192).
- 2026-10-08 (jueves): `git pull` sin incidente real (ver
  `buy-retest.md`). Dato nuevo +18/+10/+2 en 1m/2m/5m. **Hallazgo nuevo:
  primera lectura con muestra real de `sl_origin_vs_layer.since_change`
  para INV (candle1) — mixta y con significancia en contra en 2 de 3
  TF** (1m ayudaría, delta=+0.518 confirma; 2m y 5m perjudicarían,
  delta=-0.538 y -0.607, ambos `delta_below_zero=true`). Confirma que
  fue correcto no extender `sl-retest-wick` a `kind=INV` — no proponer
  ese cambio aquí. Primera lectura propia del cruce con Session Analyst
  por `kind/side` (antes sólo se citaban cifras globales): GO mejor que
  AVOID/WAIT, consistente con la hipótesis general, pero muestra (n=20
  GO, 33 AVOID, 104 WAIT) todavía chica para confiar. 2m y 5m INV/LONG
  caen a E[R] negativo en W41 pero con n=12 y n=4 respectivamente —
  ruido, no decaimiento real.
- 2026-10-07 (miércoles): `git pull` limpio. Dato nuevo chico
  (+5/+1/+2 en 1m/2m/5m). Sin hallazgos propios nuevos — el deterioro de
  RETEST/LONG y el hallazgo de `rr1_threshold_cut_oos` (ver
  `buy-retest.md`) no tienen equivalente medible aquí. Sin cambios de
  regla.
- 2026-10-06 (martes): incidente de repo del día (ver `buy-retest.md`),
  sin pérdida. Dato nuevo chico (+7/+1/+0 en 1m/2m/5m). Sin hallazgos
  propios nuevos — el deterioro semanal reportado en `buy-retest.md`
  (RETEST/LONG) no tiene equivalente medible aquí por falta de muestra
  semanal (INV es demasiado esporádico para `decay_weekly_by_segment`
  confiable). Sin cambios de regla.
- 2026-10-05 (lunes): cero trades reales nuevos en INV/LONG hoy. Único
  punto de interés: la alerta `MUESTRA` de `by_tf_kind_side/1m/INV/LONG`
  (n 199→198) del bug de `sigId` aterriza justo en este playbook — ver
  "Nota de proceso". Sin cambios de regla.
- 2026-10-04 (domingo, REVISIÓN SEMANAL): sin jsonl nuevo del cron (+1/+0/+0
  en 1m/2m/5m, timeout resuelto). Sin cambios de fondo en este playbook; el
  foco de la revisión semanal fue RETEST (ver `buy-retest.md` y
  `reviews/2026-week-40.md`): gate 0→1 de modo sombra cumplido a nivel de
  todo el bus (no aplica a INV, fuera de `shadowRules`) y baja de confianza
  del "cambio del mes" `sl_basis_retest` (tampoco aplica aquí, INV usa
  `slBasis=candle1`, sin experimento abierto). `sl_origin_vs_layer`
  `by_basis=candle1` sigue inconcluso (ver "Gestión", sin revisión fina
  hoy por foco en RETEST).
- 2026-10-03 (sábado): dato nuevo chico (+10/+0/+3 en 1m/2m/5m). 1m mejora
  de "al filo" a certificación limpia (CI90=[0.03,0.388], p=0.028 vs 0.052
  ayer). 5m cruza por primera vez el piso n≥20 (n=21) aunque sigue siendo
  el TF más ruidoso de los tres. Ver `buy-retest.md` → Histórico de hoy
  para el hallazgo metodológico del día (`sl_origin_vs_layer.since_change`),
  que no aplica a este playbook (INV usa slBasis=`candle1`, sin experimento
  abierto ahí). Filas 2-3 de la tabla de reglas no se revisaron hoy a fondo
  por foco en RETEST (prioridad 1); sin motivo para pensar que cambiaron.
- 2026-10-02 (viernes): `git pull` limpio (fast-forward). Dato nuevo
  mínimo (+5/+2/+0 en 1m/2m/5m), típico de INV. 1m sigue siendo el único
  segmento de este playbook con n usable, pero `survives_fdr10=true` hoy
  está más al filo (p=0.052, CI90 roza cero) que en corridas previas —
  vigilar si se cae a `false`. Sin cambios de fondo en el resto.
- 2026-10-01 (jueves): `git pull` limpio. Dato nuevo minimo (+12/+5/+0 en
  1m/2m/5m), tipico de INV. 1m sigue siendo el unico segmento de este
  playbook con n usable y `survives_fdr10=true`. `sl_origin_vs_layer`
  (`by_basis=candle1`, n=485) sigue sin certificar en ninguna direccion
  (delta=-0.006, CI90 cruza cero) -- a diferencia de RETEST, el SL
  estructural no tiene evidencia clara en INV todavia. Ver `buy-retest.md`
  para el hallazgo de pipeline del dia (colisiones de sigId).
- 2026-09-30 (miércoles): +8 señales INV/LONG nuevas (7 en 1m, 1 en 2m),
  volumen bajo como de costumbre. **1m/INV/LONG RECUPERA
  `survives_fdr10=true`** hoy (mismo efecto de ranking FDR que ayer, en
  sentido contrario). Sin cambios de fondo en el resto: 2m sigue sin
  certificar, 5m sigue con n=18 insuficiente. El hallazgo grande del día
  (reversión del SL estructural en el lado LONG de RETEST, cuarto día
  seguido) es de `kind=RETEST` y no aplica aquí — ver `buy-retest.md`.
- 2026-09-29 (martes): +1 señal INV/LONG nueva (1m), volumen mínimo como
  de costumbre en este playbook. **1m/INV/LONG PIERDE `survives_fdr10`
  hoy** (la corrección FDR ya no lo deja pasar pese a que su propio CI90
  casi no cambió — es un efecto del ranking de p-valores de todos los
  segmentos del día, no un cambio real de este segmento; nota de método
  para no sobre-interpretarlo). 2m/INV/LONG sigue mejorando (E[R]
  0.01→0.031). El hallazgo grande del día (reversión del SL estructural
  en el lado LONG de RETEST) es de `kind=RETEST` y no aplica aquí — ver
  `buy-retest.md`. Resto sin cambios de fondo.
- 2026-09-28 (lunes): primer día hábil, sólo +1 señal INV/LONG nueva (2m).
  Sin cambios de fondo: sigue sin ningún segmento con el criterio
  compuesto completo. 2m/INV/LONG vuelve a E[R] positivo (-0.01→0.01) y
  su SL alternativo (`candle1` vs vela-1) recupera `delta_beats_zero`.
  El fix de `analyze.py` y el hallazgo del SL estructural de hoy (ver
  `buy-retest.md`) son de `kind=RETEST`, no tocan este playbook.
- 2026-09-27 (domingo, REVISIÓN SEMANAL): sin dato nuevo (fin de semana,
  n idéntico a ayer en los tres TF). La revisión semanal de hoy no afecta
  a este playbook (las tres decisiones — SL estructural aplicado,
  `rr1_threshold_cut_oos`, `SHADOW_RULES_V1` v2 — son todas de
  `kind=RETEST`, ver `buy-retest.md`). Sin cambios en el veredicto: 1m
  sigue con `survives_fdr10=true` pero CI90 rozando cero
  ([-0.007,0.393]), 2m sigue sin certificar y en negativo, 5m certifica
  pero bajo el piso n≥20 de este playbook. Nada accionable nuevo — a
  vigilar el lunes si llega dato genuinamente nuevo.
- 2026-09-26 (sábado): dato de 2026-09-25 llegando completo (+10/+6/+2
  en 1m/2m/5m). **1m INV/LONG certifica FDR por primera vez**
  (CI90=[-0.007,0.393], p=0.057) aunque el límite inferior todavía
  cruza cero por un margen mínimo — no tratar como certificado completo
  todavía. **2m INV/LONG cruza a E[R] negativo** (-0.01, primera vez en
  varias corridas) y su SL estructural (`sl_origin_vs_layer`) pierde
  `delta_beats_zero` el mismo día (CI90 límite inferior 0.042→-0.003) —
  ambos movimientos coinciden, vigilar si 2m INV/LONG entra en un
  régimen más débil o es ruido de muestra chica (n=61-65). NQ en
  `cross_instrument` volvió a cruzar a positivo (tercer vaivén en pocos
  días) — seguir tratando el desglose por símbolo de este segmento como
  ruidoso con esta muestra. Mismo incidente de repo que `buy-retest.md`
  (merge en vez de reset, sin pérdida). Sin propuestas nuevas — n sigue
  bajo el piso de 20 para el gate en 5m y sin patrón estable en el resto.
- 2026-09-25 (viernes): **sin ningún par INV/LONG nuevo hoy** (n
  idéntico a ayer en los tres TF, 153/59/18) — todas las métricas de
  esta sección son idénticas a la corrida del 09-24 porque no hay
  outcome nuevo que mueva el número. `git pull` con el mismo "forced
  update" habitual de `origin/main` (shallow clone, sin pérdida). Nada
  accionable nuevo; ver `sell-ifvg.md` para el contraste del mismo día
  (ahí sí llegó dato nuevo en INV/SHORT).
- 2026-09-24 (jueves): dato nuevo chico (+9, sin señales 5m nuevas).
  Sin hallazgos de fondo: `sl_origin_vs_layer` en 1m INV/LONG sigue sin
  certificar (mismo estado que ayer), 2m INV/LONG sigue certificando en
  sentido contrario pero el límite inferior de su CI90 se acerca un
  poco más a cero (0.118→0.042). Único cambio de orden: en la autopsia
  de SL, `killzone-Asia-largo` empata con `RR-bajo` como causa más
  frecuente (38/89 cada una) por primera vez en este playbook — con
  n=89 todavía moderado, no tratar como señal firme. `cross_instrument`
  en NQ cruza a E[R] negativo (-0.033) por primera vez, n=15 sigue
  chico. Sigue sin n suficiente (todo <20 salvo 1m/2m) para proponer
  nada en `experiments.json`.
- 2026-09-23 (miércoles): dato nuevo chico (+13). Único hallazgo
  reseñable: `sl_origin_vs_layer` en **1m INV/LONG pierde la
  certificación de ayer** (CI90 vuelve a cruzar cero, -0.515 a 0.101) —
  tratado como reversión de muestra todavía moderada (n=140), no como
  giro real; vigilar la próxima lectura. Resto de métricas sin cambios
  de fondo, sigue sin n suficiente (todo <20 salvo 1m/2m) para proponer
  nada en `experiments.json`.
- 2026-09-22 (martes): dato nuevo notable para este playbook (+17, n
  186→208 vía el lote grande de outcomes de 2026-09-21). E[R] mejora
  fuerte en 1m (0.002→0.121) y 2m sale de negativo (-0.102→0.02).
  **Hallazgo principal: `sl_origin_vs_layer` certifica por primera vez
  en 1m (favorece SL 3-capas) y en 2m (favorece SL vela-1), en
  direcciones opuestas entre sí** — ninguno es accionable todavía (n
  moderado, 2m con CI90 muy ancho), pero es la primera señal estadística
  real de este experimento en INV/LONG. Sigue siendo prioridad 2, ningún
  TF con n suficiente para proponer cambio de reglas.
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
