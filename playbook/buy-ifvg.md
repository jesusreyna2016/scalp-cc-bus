# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-13 · n: 108)

### Nota de proceso
Incidente menor de repo, ver `buy-retest.md`. Este segmento (prioridad 2)
creció poco, como es habitual: n 102→108 (**+6**; 1m+7, **2m -1**, 5m sin
cambio) — ver alerta abajo sobre el 2m.

### Veredicto global
1m n=73 (+7, WR 42.5%, E[R]=**0.123** PF=1.25, 33 SL — bajó un poco de
+0.129, sigue en terreno claramente positivo); 2m n=25 (**bajó de 26 a
25** — `report.alerts` lo marca explícitamente: "MUESTRA:
by_tf_kind_side/2m/INV/LONG bajó de n=26 a n=25 desde la corrida previa
(agregado, no archivo crudo)"; `file_integrity_check` confirma que
ningún `signals/outcomes/*.jsonl` encogió, así que es re-pareo/dedup del
agregado, no pérdida real — pero es la primera vez que este segmento en
concreto se ve afectado, vigilar si se repite; WR 44.0%, E[R]=**-0.217**
PF=0.6, 13 SL — mejoró un poco de -0.247 pese al n menor, sigue siendo la
peor rama); 5m n=10 (sin cambio, WR 90.0%, E[R]=0.849 PF=99, 0 SL —
congelado). `segment_significance`: 1m CI90=[-0.132,0.396] p=0.228 n=70
(prácticamente sin cambio, sigue lejos de certificar); 2m y 5m sin
cambio de fondo. `survives_fdr10=true` en 5m se mantiene (CI90=
[0.522,1.254], n=10) — sigue **no usable**: muy por debajo del piso n≥20
del playbook, tratar como ruido de muestra mínima.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar en la mayoría de las ramas:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | sigue siendo la mejor rama | 58 (+3) / 46 (+3) / 4 (sin cambio) | WR 46.6%/47.8%/50.0%; E[R] +0.143 (subió de +0.114) / +0.04 (bajó de +0.057) / +0.455 (sin cambio) | baja-moderada — `edge=1` mejora, `edge=0` retrocede un poco, mismo orden relativo que ayer |
| 2 | `tier=B` | mejor que `tier=C`, pero **`tier=B` pierde muestra** (30→28, -2) mientras `tier=C` gana (+8) | 28 (-2) / 80 (+8) | E[R] +0.132 (bajó de +0.14) vs +0.089→+0.104 (subió); PF 1.3 vs 1.23 | baja-moderada — segunda instancia de recuento agregado bajando en este mismo playbook hoy (ver nota del 2m arriba); la brecha entre B y C se sigue achicando |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- `managed_vs_naive`: 1m n=70 delta=**+0.141** (naive 0.123→managed
  0.263, bajó un poco de +0.149, sigue ayudando mucho); 2m n=25
  delta=+0.017 (prácticamente sin cambio pese al n menor); 5m n=10
  delta=**-0.117** (sin cambio, congelado, la gestión sigue restando en
  5m INV/LONG con n demasiado chico para concluir).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=70 (+6)
  delta=**-0.047** CI90=[-0.466,0.386] no certifica (prácticamente igual
  a -0.039, sigue siendo ruido alrededor de cero); 2m **sigue
  certificando, y mejora pese al n menor**: n=25 (-1) delta=**+1.109**
  CI90=**[0.045,2.422]** (el límite inferior sube de 0.007 a 0.045,
  deja de estar tan al filo); 5m n=10 delta=-1.307 CI90=[-1.91,-0.771]
  (sin cambio, congelado, sentido opuesto a 2m). Sigue sin proponerse
  cambio en `experiments.json` para INV/LONG — 2m sigue siendo el único
  candidato con algo de solidez, pero por debajo del piso de muestra
  que el bus viene usando para RETEST (n≥20 aquí es al filo, no un
  margen cómodo).
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
INV/LONG bajo veredicto SA `WAIT` n=20 (sin cambio, cero señales nuevas
cruzadas hoy) E[R]=**0.154** PF=1.39 (idéntico a ayer); no hay lectura
propia de `GO`/`AVOID` hoy en este segmento (n por debajo del piso de 5).
Ver `buy-retest.md`/`sell-retest.md` para el hallazgo agregado (WAIT
mejor, GO/AVOID peor, con respaldo estadístico a nivel global por tercer
día seguido).

### Contextos a evitar
- Autopsia de SL sobre las 46 pérdidas INV/LONG (+2 vs ayer): sin cambio
  de orden — `killzone-Asia-largo` 22/46 (47.8%) sigue como causa más
  frecuente, `RR-bajo` 21/46 (45.7%) muy cerca detrás, `contra-estructura`
  14/46 (30.4%) tercero. Tercer día seguido con este orden.
- `cross_instrument` sigue `instrument-specific`, spread se achica un
  poco (0.834→0.803): CL n=21 (sin cambio) E[R]=0.4, YM n=26 E[R]=0.172,
  NQ n=6 E[R]=0.373, GC n=13 E[R]=-0.26, ES n=7 E[R]=-0.403 — los valores
  de E[R] se movieron un poco pese a n casi sin cambio en varios símbolos
  (mismo patrón de recuento agregado que en el 2m y `tier=B` de arriba);
  n por símbolo sigue chico, no generalizar.

### Decaimiento
_pendiente_ (WR TP1 por semana; marcar si cae > 15 pts en ventana de 3 semanas)

## Histórico de cambios
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
