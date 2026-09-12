# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-12 · n: 102)

### Nota de proceso
Sin incidentes de repo hoy. Este segmento (prioridad 2) creció poco, como
es habitual: n 100→102 (**+2**, todo en 1m).

### Veredicto global
1m n=66 (+2, WR 43.9%, E[R]=**0.129** PF=1.27, 30 SL — subió de +0.097,
recupera la racha de subida tras el retroceso de ayer); 2m n=26 (sin
cambio, cero señales nuevas, WR 42.3%, E[R]=-0.247 PF=0.56, 14 SL —
congelado, sigue siendo la peor rama); 5m n=10 (sin cambio, WR 90.0%,
E[R]=0.849 PF=99, 0 SL — congelado). `segment_significance`: 1m
CI90=[-0.138,0.414] p=0.231 n=64 (mejoró un poco desde [-0.168,0.382),
sigue lejos de certificar); 2m y 5m sin cambio (congelados, mismas
cifras que ayer). `survives_fdr10=true` en 5m se mantiene (CI90=
[0.522,1.254], n=10) — sigue **no usable**: muy por debajo del piso n≥20
del playbook, tratar como ruido de muestra mínima.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar en la mayoría de las ramas; casi
toda la actividad de hoy fue en `edge=0`:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | sigue siendo la mejor rama, congelada hoy | 55 (sin cambio) / 43 (+2) / 4 (sin cambio) | WR 47.3%/48.8%/50.0%; E[R] +0.114 (sin cambio) / +0.057 (subió de +0.005) / +0.455 (sin cambio) | baja-moderada — `edge=0` se recupera un poco pero sigue siendo la rama más débil de las tres |
| 2 | `tier=B` | mejor que `tier=C`, ambos congelados/con poco cambio | 30 (sin cambio) / 72 (+2) | E[R] +0.14 (sin cambio) vs +0.089 (subió de +0.059); PF 1.34 vs 1.19 | baja-moderada — mismo sentido que ayer, la brecha entre B y C se achica |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- `managed_vs_naive`: 1m n=64 delta=**+0.149** (naive 0.129→managed
  0.278, bajó un poco de +0.173, sigue ayudando mucho); 2m n=26
  delta=+0.017 (sin cambio, congelado); 5m n=10 delta=**-0.117** (sin
  cambio, congelado, la gestión sigue restando en 5m INV/LONG con n
  demasiado chico para concluir).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=64 (+2)
  delta=**-0.039** CI90=[-0.482,0.455] no certifica (se dio vuelta a
  ligeramente negativo desde +0.028, sigue siendo ruido alrededor de
  cero); 2m **sigue certificando, sin cambio (congelado)**: n=26
  delta=+1.066 CI90=[0.007,2.311] (mismas cifras que ayer, sigue al
  filo); 5m n=10 delta=-1.307 CI90=[-1.91,-0.771] (sin cambio,
  congelado). Sigue sin proponerse cambio en `experiments.json` para
  INV/LONG — 2m sigue siendo el único candidato con algo de solidez, pero
  sin dato nuevo que lo confirme o lo debilite hoy.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
INV/LONG bajo veredicto SA `WAIT` n=20 (+1) E[R]=**0.154** PF=1.39 (bajó
de +0.215 con algo más de muestra, sigue positivo); no hay lectura propia
de `GO`/`AVOID` hoy en este segmento (n por debajo del piso de 5). Con
`WAIT` como único dato, sigue sin poder compararse contra la hipótesis
original aquí; ver `buy-retest.md`/`sell-retest.md` para el hallazgo
agregado (WAIT mejor, GO peor, sostenido por segundo día seguido y ya con
respaldo estadístico a nivel global).

### Contextos a evitar
- Autopsia de SL sobre las 44 pérdidas INV/LONG (+1 vs ayer): sin cambio
  de orden — `killzone-Asia-largo` 22/44 (50.0%) sigue como causa más
  frecuente, `RR-bajo` 21/44 (47.7%) muy cerca detrás, `contra-estructura`
  13/44 (29.5%) tercero. Segundo día seguido con este orden, empieza a
  verse más estable que el vaivén de días previos.
- `cross_instrument` sigue `instrument-specific`, spread se ensanchó un
  poco (0.754→0.834): CL n=21 (+2) E[R]=0.4 (subió de 0.32, único símbolo
  con dato nuevo), YM/ES/NQ/GC sin cambio (E[R] 0.194/-0.434/0.257/-0.193
  respectivamente) — n por símbolo sigue chico, no generalizar.

### Decaimiento
_pendiente_ (WR TP1 por semana; marcar si cae > 15 pts en ventana de 3 semanas)

## Histórico de cambios
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
