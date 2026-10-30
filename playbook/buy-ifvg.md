# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-10-30 (viernes) · n: 663)

### Nota 2026-10-30
Viernes, dato nuevo moderado en 1m/2m/5m (n=441/162/49, +13 vs ayer en
total), 15m aparece con n=3 (sin peso). Sin cambio de fondo: ningún
segmento INV/LONG cruza el umbral de decaimiento ni cambia de causa
dominante. El hallazgo grande de hoy (salto de `aligned=0` desde el
26-oct, nuevo TF 29m, gate saltando de segmento) es todo en `kind=RETEST`
— ver `buy-retest.md`/`sell-retest.md`; este playbook (prioridad 2,
monitoreo) no tiene señales de 29m todavía y su `aligned` no se revisó
hoy por separado por ser de muestra chica (n<700 en total). Huérfanos
estable en 54.

### Nota 2026-10-29
Jueves, lote grande de dato atrasado llega de golpe (ver `buy-retest.md`
para el detalle del backlog del bus). **+61 pares nuevos en este
playbook**: 1m 404→436 (+32), 2m 146→162 (+16), 5m 39→45 (+6), y por
primera vez aparecen **dos TF nuevos con muestra real**: `3m/INV/LONG`
n=5 y `15m/INV/LONG` n=2 — ambos muy por debajo del piso n≥20, sólo se
deja constancia, sin veredicto. `1m/INV/LONG` sostiene
`survives_fdr10=true` (CI90=[0.049,0.257] n=421, E[R] sube un poco a
0.145) — sigue siendo el único segmento de este playbook con
certificación FDR usable. **`5m/INV/LONG` PIERDE `survives_fdr10`**
hoy (antes true con n=36, hoy n=42 CI90=[-0.04,0.379] cruza cero) — con
la reserva ya anotada ayer de que n era demasiado chico para confiar,
esto confirma que no era una certificación real. Dato de método: el
candle1 de `sl_origin_vs_layer` en 2m/INV/LONG se acerca al borde de
significancia por primera vez (delta=+0.513 CI90=[-0.002,1.121], límite
inferior casi en cero) — todavía NO confirma (`delta_beats_zero=false`),
vigilar la próxima lectura, no proponer nada. `managed_vs_naive` en
5m/INV/LONG cruza a delta NEGATIVO por primera vez (-0.021, n=42,
antes +0.027) — con n chico, tratar como ruido, no como reversión real
de la gestión. Cruce con Session Analyst: `GO` sigue siendo la rama más
fuerte (n=64 E[R]=0.096, sube de 0.071) y `AVOID` sigue siendo la más
débil (n=42 E[R]=-0.102, sin pares nuevos) — orden GO > WAIT > AVOID
sin cambio.

### Nota 2026-10-28
Miércoles, **sin dato nuevo real** (ver `buy-retest.md` para el detalle
completo) — ~36h sin commit de `signals`/`outcomes` en el bus (último
2026-10-26T13:31Z), confirmado sano el pipeline hermano vía
`session-analyst-bus/live/health.json`. El único movimiento es
`1m/INV/LONG` 403→404 (+1), un pendiente del 10-26 resolviéndose, no
una señal nueva. 2m y 5m sin cambio. Cruce con Session Analyst sin
pares nuevos. Sin hallazgos de método nuevos.

### Nota 2026-10-27
Martes, corrida diaria normal. **+4 pares nuevos, todos en 1m**
(1m=403 +4, 2m=146 sin cambio, 5m=39 sin cambio) — sin pérdidas nuevas
(la autopsia de SL de 1m/INV/LONG queda idéntica, n=238). `1m/INV/LONG`
suma su **sexta lectura seguida** certificando `survives_fdr10=true`
(CI90=[0.021,0.25] n=389, sube de 385). Cruce con Session Analyst sin
pares nuevos en ningún verdict (AVOID/GO/WAIT idénticos a ayer) — la
racha de "cuarto día seguido en positivo" de GO no crece hoy, se
mantiene en el mismo nivel. Sin hallazgos de método nuevos; INV sigue
fuera de `shadowRules` (prioridad 2, sólo monitoreo).

### Nota 2026-10-26
Lunes, corrida diaria normal. **Cero pares nuevos en este playbook**
(n idéntico en los tres TF: 1m=399, 2m=146, 5m=39) — a diferencia de
RETEST (que sí tuvo dato chico hoy), BUY-IFVG no sumó ninguna señal
resuelta. Nada que actualizar en Veredicto/Reglas/Decaimiento. Dos
hallazgos compartidos con el resto del bus, sin acción aquí: (1) el
modo sombra dispara hoy su alerta de 3 semanas cerradas sin batir al
crudo (no aplica a INV, que está fuera de `shadowRules`); (2) el
viernes 2026-10-23 se recuperó sólo parcialmente (9 señales de
~50-90 esperadas en todo el bus). Dato de método nuevo: al revisar hoy
`sl_origin_vs_layer.since_change` con más detalle, `1m/INV/LONG`
muestra delta=+0.349 CI90=[0.073,0.655] n=219 (`delta_beats_zero=true`)
— el SL estructural parecería ayudar aquí, pero **no se propone ningún
cambio**: es señal de prioridad 2, n de cientos (no miles), una sola
lectura a este nivel de detalle, y `agent-instructions.md` exige no
generalizar sin varias semanas de estabilidad — queda anotado para
vigilar, nada más. En el lado SHORT (`sell-ifvg.md`) el mismo corte da
signo CONTRARIO, lo que refuerza no tocar el scope del experimento
(sigue sólo `RETEST`).

### Nota 2026-10-25
Domingo, revisión semanal (`reviews/2026-week-43.md`). **Sin pares
nuevos desde ayer** en ningún TF de este playbook — n idéntico
(1m=399, 2m=146, 5m=39). Falta por completo el viernes 2026-10-23 en
todo el bus, no sólo aquí (ver `buy-retest.md` y la revisión semanal
hallazgo 1 para el detalle del pipeline). `1m/INV/LONG` cierra su
semana W43 (n=48, sin más dato esperado) como el bolsillo más fuerte
de toda la semana (WR60.4% E[R]0.321 PF1.91) — con la reserva de que
le falta el mismo viernes que al resto del bus. INV sigue fuera de
`shadowRules` (prioridad 2, sólo monitoreo); las dos decisiones de la
revisión semanal (confianza de `sl_basis_retest`, alerta de racha del
modo sombra) son específicas de `kind=RETEST` y no aplican aquí.

### Veredicto global
1m n=436 WR 47.2% E[R]=**0.145** PF=1.34 (sube); 2m n=162 WR 53.1%
E[R]=**0.043** PF=1.11 (estable); 5m n=45 WR 66.7% E[R]=**0.172**
PF=1.66 (baja un poco, n=45). NUEVO: 3m n=5, 15m n=2 — muestra
testimonial, sin veredicto. `segment_significance`: 1m
CI90=[0.049,0.257] n=421 **`survives_fdr10=true`** (sigue
certificando); 2m CI90=[-0.1,0.194] n=157 sigue sin certificar; **5m
CI90=[-0.04,0.379] n=42 PIERDE `survives_fdr10` hoy** (antes true con
n=36, se confirma que era ruido de muestra chica como ya se sospechaba).
`sl_origin_vs_layer` (`candle1`): 1m sin cambio material (delta=0.013,
cruza cero); 2m se acerca al borde (delta=+0.513 CI90=[-0.002,1.121],
todavía sin confirmar); 5m cambia de signo (-0.075, n=42, ruido) — sigue
correcto que `sl-retest-wick` se limite a `kind=RETEST`, no extender a
INV.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar en más de una rama con
confianza:

| # | SI | ENTONCES (hipótesis, sin confirmar salvo 1m) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tf=1m` | certifica FDR de forma sostenida — tomar con cautela | 421 | E[R]=**0.145** CI90=[0.049,0.257] | moderada — varias lecturas seguidas |
| 2 | `tf=2m` | sin edge confirmado (CI90 cruza cero) | 157 | E[R]=**0.043** CI90=[-0.1,0.194] | baja — no proponer cambio con este n |
| 3 | `tf=5m` | perdió la certificación que tenía — tratar como sin edge confirmado | 42 | E[R]=**0.172** CI90=[-0.04,0.379] | baja — n chico, no proponer |
| 4 | mover SL a vela 1 del FVG (`candle1`) | **NO proponer** — mixto, ningún TF confirma (2m se acerca al borde) | 421 (1m) / 157 (2m) / 42 (5m) | ver `experiments.json`/`sl_origin_vs_layer` por basis | baja |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`).

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=421 delta=**+0.133**
  (estable); 2m n=157 delta=**+0.109** (estable); 5m n=42
  delta=**-0.021** (cruza a negativo por primera vez, n chico, tratar
  como ruido). Sin cambio de regla.
- **SL de 3 capas vs SL = vela 1 del FVG**: sin confirmación en ningún
  TF — mixto, no proponer cambio (ver Veredicto global).
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL (INV/LONG, n=258, +20 pérdidas nuevas hoy):
  `killzone-Asia-largo` 125/258 (48.4%) dominante, `RR-bajo` 96/258
  (37.2%) segundo, `contra-estructura` 80/258 (31.0%) tercero — sin
  cambio de orden.

### Cruce con Session Analyst
`session_analyst_cross.by_kind_side`: `AVOID` n=42 E[R]=**-0.102**
WR45.2% (sin trades nuevos); `GO` n=64 E[R]=**0.096** WR54.7% (+7,
sube de 0.071, sigue siendo la rama más fuerte); `WAIT` n=246
E[R]=**-0.012** WR44.7% (+15, mejora un poco de -0.022) — AVOID y WAIT
siguen en negativo/plano, GO sostiene su ventaja. Cifras globales con
CI90 en `buy-retest.md`.

### Decaimiento
`decay_weekly_by_segment`: W44 (semana en curso) 1m n=37 WR62.2%
E[R]=0.4 (mejora clara vs el promedio de W41-W43, sin señal de
decaimiento); 2m n=16 WR75.0% E[R]=0.192; 5m n=6 WR50.0% E[R]=-0.23
(muestra todavía chica en 2m/5m, no leer como tendencia). Ningún TF cae
>15pts de WR vs el promedio de las 3 semanas previas.

## Histórico de cambios
- 2026-10-29 (jueves): lote grande de dato atrasado (+61 en este
  playbook: 1m+32, 2m+16, 5m+6), más dos TF nuevos con muestra mínima
  (3m n=5, 15m n=2). `1m/INV/LONG` sostiene `survives_fdr10=true`
  (n=421). `5m/INV/LONG` PIERDE `survives_fdr10` (n=42, confirma que
  era ruido de muestra chica como ya se sospechaba). `candle1` en
  2m/INV/LONG se acerca al borde de significancia sin confirmar
  (CI90=[-0.002,1.121]). `managed_vs_naive` en 5m cruza a negativo por
  primera vez (ruido, n chico). Sin cambios de regla.
- 2026-10-28 (miércoles): **sin dato nuevo real**, ~36h sin commit de
  `signals`/`outcomes` (último 2026-10-26T13:31Z) — ver `buy-retest.md`.
  `1m/INV/LONG` 403→404 (+1, pendiente del 10-26, no señal nueva).
  Pipeline hermano confirmado sano.
- 2026-10-27 (martes): +4 pares nuevos, todos en 1m (n=588 total),
  sin pérdidas nuevas. `1m/INV/LONG` suma su sexta lectura seguida
  certificando `survives_fdr10=true`. Cruce con Session Analyst sin
  pares nuevos en ningún verdict. Sin cambios de regla.
- 2026-10-26 (lunes): cero pares nuevos en este playbook (n=584 sin
  cambio en los tres TF). Sin cambios de regla. Nota de método: el
  since_change de `sl_basis_retest` en `1m/INV/LONG` da positivo
  (delta+0.349, n=219) pero no se propone nada (prioridad 2, n chico,
  una sola lectura) — el lado SHORT da signo contrario, refuerza no
  tocar el scope del experimento (sigue sólo RETEST). Modo sombra
  dispara hoy su alerta de 3 semanas sin batir al crudo (no aplica a
  INV). Viernes 2026-10-23 recuperado sólo parcialmente (ver
  `buy-retest.md`).
- 2026-10-25 (domingo, REVISIÓN SEMANAL): sin pares nuevos desde
  ayer en ningún TF — falta por completo el viernes 2026-10-23 en todo
  el bus (ver `buy-retest.md` y `reviews/2026-week-43.md`). `1m/INV/LONG`
  cierra la semana como el bolsillo más fuerte del bus (WR60.4%
  E[R]0.321 PF1.91, n=48), con esa misma reserva de muestra. Sin
  cambios de regla en este playbook (las decisiones de la revisión
  semanal son específicas de RETEST).
- 2026-10-24 (sábado): dato de cierre del viernes (+8 en todo el
  playbook). `1m/INV/LONG` suma su quinta confirmación seguida de
  `survives_fdr10=true`. Dato notable: `1m/INV/LONG` en W43 (n=48)
  muestra WR60.4% E[R]0.321 PF1.91 — el bolsillo más fuerte de la
  semana en todo el bus. `GO` en el cruce con Session Analyst sube a
  n=57, E[R]=0.071 (cuarto día seguido en positivo, mejora de
  magnitud). Sin incidentes de pipeline.
- 2026-10-23 (viernes): dato algo más activo (+24 en todo el
  playbook). `1m/INV/LONG` suma su cuarta confirmación seguida de
  `survives_fdr10=true`, prácticamente estable. `GO` en el cruce con
  Session Analyst sostiene su reversión por tercer día (n=53,
  E[R]=0.039, baja un poco de 0.049) — el motor fusionado del Session
  Analyst lleva ~8h sin refrescar según su propio plan, por eso `AVOID`
  no sumó pares nuevos. Sin cambios de fondo en el resto. Sin
  incidentes de pipeline.
- 2026-10-22 (jueves): dato escaso (+8 en todo el playbook, sólo 1m).
  `1m/INV/LONG` suma su tercera confirmación seguida de
  `survives_fdr10=true` (CI90 se afloja un poco con el dato nuevo, sin
  perder significancia). `GO` en el cruce con Session Analyst sostiene
  su reversión a positivo por segundo día (n=50). Sin cambios de fondo
  en el resto. Sin incidentes de pipeline.
- 2026-10-21 (miércoles): dato escaso (+6 en todo el playbook).
  `1m/INV/LONG` suma su segunda confirmación seguida de
  `survives_fdr10=true`, fortaleciéndose. `GO` en el cruce con Session
  Analyst se vuelve positivo por primera vez en varias corridas
  (n=47, todavía chico, no confirmado). Sin cambios de fondo en el
  resto. Sin incidentes de pipeline.
- 2026-10-20 (martes): dato algo mayor que de costumbre (+21 en todo
  el playbook). `1m/INV/LONG` recupera `survives_fdr10=true` tras
  haberlo perdido el 2026-10-17 (CI90 deja de cruzar cero) — vigilar
  una segunda lectura antes de subir la confianza. Session Analyst:
  los tres veredictos siguen en negativo pero GO y WAIT mejoran un
  poco con dato nuevo. Sin incidentes de pipeline.
- 2026-10-19 (lunes): dato mínimo (+5 en todo el playbook), sin
  hallazgo material nuevo. `1m/INV/LONG` se mantiene sin
  `survives_fdr10`. Cruce con Session Analyst: los tres veredictos
  siguen en negativo por tercer día seguido, sin trades nuevos. Mismo
  incidente de infraestructura git documentado en `buy-retest.md`.
  Ningún candidato con n≥20 para proponer cambio de input.
- 2026-10-18 (domingo, REVISIÓN SEMANAL): dato mínimo (+4 en todo el
  playbook), sin hallazgo material nuevo — ver `reviews/2026-week-42.md`.
  `1m/INV/LONG` se mantiene sin `survives_fdr10` (sin seguir
  deteriorándose vs ayer). Cruce con Session Analyst: los tres
  veredictos siguen en negativo por segundo día (GO sube un poco pero
  no recupera terreno positivo). Ningún candidato con n≥20 para
  proponer cambio de input esta semana en este playbook.
- 2026-10-17 (sábado): `1m/INV/LONG` pierde `survives_fdr10` por
  primera vez (E[R] baja de 0.136 a 0.097, CI90 ahora cruza cero) —
  n chico (331), puede revertir, vigilar sin tratarlo como real.
  Cruce con Session Analyst: los tres veredictos (AVOID/GO/WAIT) caen
  en negativo por primera vez en este segmento, rompiendo el patrón de
  GO siempre mejor (n chico, posible ruido). Salto grande de dato por
  el fin de semana largo. Sin incidentes de pipeline.
- 2026-10-16 (viernes): sin hallazgo material nuevo, dato chico (n
  317→317 en 1m realmente estable, 122→124 en 2m). `git pull` encontró
  `HEAD` detached, resuelto con `git checkout main && git pull` sin
  pérdida de datos. `2m/INV/LONG` sigue sin certificar FDR (quinta
  corrida seguida).
- 2026-10-15 (jueves): sin hallazgo material nuevo, dato chico. `git
  pull` limpio sin incidentes. `2m/INV/LONG` sigue sin certificar FDR.
- 2026-10-14 (miércoles): sin hallazgo material nuevo, dato chico.
  `git pull` sin incidente de divergencia. `2m/INV/LONG` sigue sin
  certificar FDR.
- 2026-10-13 (martes): sin hallazgo material nuevo, dato chico. Mismo
  incidente de reescritura de `origin/main` que `buy-retest.md`,
  resuelto igual. `2m/INV/LONG` sigue sin certificar FDR (cuarta
  corrida).
- 2026-10-11 (domingo, REVISIÓN SEMANAL): se retira la alerta `SIGID`
  (fix de emparejamiento en `analyze.py`, ver `buy-retest.md`) —
  recupera pares sin dato nuevo real, `huérfanos` 40→44. Sin hallazgo de
  fondo propio: `2m/INV/LONG` sigue sin certificar FDR (tercera corrida
  seguida, E[R]=-0.024 CI90=[-0.183,0.136]); 1m y 5m mantienen su edge.
  Nada que proponer para `scalp_command.pine` desde este playbook esta
  semana (n insuficiente en todas las ramas salvo 1m, que no tiene
  cambio que proponer). Ver `reviews/2026-week-41.md`.
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
