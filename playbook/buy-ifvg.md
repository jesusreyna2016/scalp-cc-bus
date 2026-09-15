# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-15 · n: 123)

### Nota de proceso
Otro "forced update" de `origin/main` al inicio de la corrida (ver
`buy-retest.md`), resuelto sin pérdida. Segmento de prioridad 2, crece
poco como es habitual: n 111→123 (**+12**; 1m+9, 2m+3, 5m sin cambio).

### Veredicto global
1m n=84 (+9, WR 45.2%, E[R]=**0.133** PF=1.28, 37 SL — prácticamente
igual a ayer +0.139); 2m n=29 (+3, WR 48.3%, E[R]=**-0.159** PF=0.68, 14
SL — bajó un poco de -0.152, sigue siendo la peor rama por lejos); 5m
n=10 (sin cambio, congelado por TERCER día, WR 90.0%, E[R]=0.849 PF=99,
0 SL). `segment_significance`: 1m CI90=[-0.096,0.376] p=0.177 n=81
(prácticamente sin cambio, sigue lejos de certificar); 2m CI90=
[-0.447,0.129] p=0.818 n=29 (sin cambio de fondo); 5m
`survives_fdr10=true` se mantiene (n=10) — sigue **no usable**, muy por
debajo del piso n≥20 del playbook; es el mismo tipo de "estadísticamente
significativo pero con n de juguete" que hay que ignorar para decisiones.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar en la mayoría de las ramas:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | sigue siendo la mejor rama | 65 | E[R]=**+0.146** | baja-moderada — orden relativo estable, n todavía chico |
| 2 | `tier=B` vs `tier=C` | **C adelanta a B por primera vez** | 31 (+3) vs 92 (+9) | E[R] +0.106 (bajó de +0.132) vs +0.127 (subió de +0.104/0.135) | baja — la brecha se invierte con muestra todavía chica en ambos lados, no fijar como regla |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- `managed_vs_naive`: 1m n=81 delta=**+0.18** (subió de +0.14, la
  gestión ayuda cada vez más en este TF); 2m n=29 delta=+0.006 (bajó de
  +0.011, casi neutro); 5m n=10 delta=**-0.117** (sin cambio, congelado).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=81 (+9)
  delta=**-0.164** CI90=[-0.529,0.227] no certifica (se aleja un poco más
  hacia el lado negativo desde -0.078, sigue siendo ruido, n todavía
  chico); 2m n=29 (+3) delta=**+0.909** CI90=[-0.027,2.134] sigue sin
  certificar (cruza cero, límite inferior casi tocando cero — la misma
  fragilidad de los últimos días con n<30); 5m n=10 delta=-1.307
  CI90=[-1.91,-0.771] (sin cambio, congelado, `delta_below_zero=true` —
  aquí es el SL de 3 capas el que gana, no el estructural, pero con n=10
  no es una lectura usable). Sin propuesta en `experiments.json` para
  INV/LONG — ningún TF tiene todavía una lectura estable con n suficiente.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
INV/LONG bajo veredicto SA `WAIT` n=21 (+1) E[R]=**0.18** (subió de
0.154); por primera vez `GO` y `AVOID` alcanzan el piso mínimo de n=5
para reportarse: `AVOID` n=5 E[R]=**-0.52** (muy negativo, muestra
mínima) y `GO` n=5 E[R]=**-0.01**. Con n=5 en ambas ramas nuevas esto es
apenas anecdótico — no usar todavía para nada accionable, sólo vigilar
si el patrón "WAIT mejor" (que domina en `buy-retest.md`) también se
sostiene aquí con más muestra.

### Contextos a evitar
- Autopsia de SL sobre las 51 pérdidas INV/LONG (+5 vs ayer): mismo
  orden por quinto día seguido — `killzone-Asia-largo` 25/51 (49.0%),
  `RR-bajo` 22/51 (43.1%), `contra-estructura` 14/51 (27.5%). A
  diferencia de RETEST (donde domina `RR-bajo`), en INV/LONG la causa
  dominante sigue siendo `killzone-Asia-largo` — patrón distinto y
  estable, vale la pena mantenerlo como regla separada en el playbook.
- `cross_instrument` sigue `instrument-specific`, spread se achica un
  poco (0.831→0.803): CL n=27 (+4) E[R]=0.473 (subió, sigue el mejor), YM
  n=30 (+4) E[R]=0.101 (bajó bastante de 0.172), ES n=8 (+1) E[R]=-0.33
  (sigue negativo), NQ n=6 E[R]=0.212, GC n=13 (sin cambio) E[R]=-0.26 —
  n por símbolo sigue chico, no generalizar.

### Decaimiento
_pendiente_ (WR TP1 por semana; marcar si cae > 15 pts en ventana de 3 semanas)

## Histórico de cambios
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
