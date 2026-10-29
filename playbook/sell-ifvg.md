# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-10-29 (jueves) · n: 449)

### Nota 2026-10-29
Jueves, lote grande de dato atrasado llega de golpe (ver `buy-retest.md`
para el detalle del backlog del bus). **+41 pares nuevos en este
playbook**: 1m 281→309 (+28), 2m 104→113 (+9), 5m 23→26 (+3), y
aparece por primera vez `3m/INV/SHORT` con n=1 (testimonial, sin
veredicto). **Hallazgo del día — reversión del `since_change` de
`sl_basis_retest` en `1m/INV/SHORT`**: tras tres lecturas seguidas
confirmando NEGATIVO (mover el SL a la mecha perjudicaría en este
segmento), con el dato nuevo de hoy el CI90 VUELVE A CRUZAR CERO
(delta -0.288→**-0.173**, CI90=[-0.513,-0.065]→**[-0.435,0.087]**,
n132→160) — PIERDE la certificación negativa que sostenía desde el
2026-10-26. No se trata como una reversión real todavía (una sola
lectura tras tres confirmando, n sigue moderado): se baja de "confirma
negativo" a "vigilar, perdió significancia con el lote grande de hoy",
sin cambiar la recomendación de no extender `sl-retest-wick` a INV
(sigue sin evidencia de que ayude tampoco). Ningún TF de este playbook
certifica FDR hoy (1m CI90=[-0.034,0.184] n=292; antes CI90=[-0.034,0.196]
n=264 — prácticamente sin cambio). Cruce con Session Analyst: orden
GO > WAIT >> AVOID se mantiene (GO n=30 E[R]=0.208, WAIT n=197
E[R]=0.137, AVOID n=32 E[R]=-0.247, todos con pares nuevos hoy).

### Nota 2026-10-28
Miércoles, **cero pares nuevos en este playbook, y cero en todo el bus**
(ver `buy-retest.md` para el detalle completo) — ~36h sin commit de
`signals`/`outcomes` (último 2026-10-26T13:31Z), confirmado sano el
pipeline hermano. 1m/2m/5m sin cambio de n (281/104/23). Todas las
cifras idénticas a ayer porque no hay muestra que las mueva.

### Nota 2026-10-27
Martes, corrida diaria normal. +5 pares nuevos, chico y normal
(1m=281 +3, 2m=104 +2, 5m=23 sin cambio). `since_change` de
`sl_basis_retest` en `1m/INV/SHORT` sigue confirmando NEGATIVO con el
dato nuevo (delta -0.305→**-0.288** CI90=[-0.538,-0.08]→**[-0.513,-0.065]**,
n129→132) — tercera lectura seguida reforzando que el cambio de SL
estructural NO debe extenderse a INV (sigue sólo `kind=RETEST`).
Cruce con Session Analyst sin pares nuevos en ningún verdict
(AVOID/GO/WAIT idénticos a ayer).

### Nota 2026-10-26
Lunes, corrida diaria normal. +2 pares nuevos, chico y normal
(1m=278 +1, 2m=102 +1, 5m=23 sin cambio). Dos hallazgos compartidos con
el resto del bus, sin acción específica aquí: (1) el modo sombra
dispara hoy su alerta de 3 semanas cerradas sin batir al crudo (no
aplica a INV, fuera de `shadowRules`); (2) el viernes 2026-10-23 se
recuperó sólo parcialmente (9 señales de ~50-90 esperadas). Dato de
método: `since_change` de `sl_basis_retest` en `1m/INV/SHORT` sigue
confirmando NEGATIVO con el par nuevo (delta -0.284→**-0.305**
CI90=[-0.51,-0.06]→**[-0.538,-0.08]**, n128→129) — refuerza, con una
lectura más, que el cambio de SL estructural NO debe extenderse a INV
(el scope de `sl-retest-wick-2026-09-03` sigue siendo sólo
`kind=RETEST`, documentado hoy en `experiments.json`). Contraste con
`buy-ifvg.md`, donde el mismo corte en INV/LONG da signo positivo —
confirma que el efecto es específico de lado, no generalizable.

### Nota 2026-10-25
Domingo, revisión semanal (`reviews/2026-week-43.md`). **Sin pares
nuevos desde ayer** en ningún TF (1m=277, 2m=101, 5m=23, sin cambio).
Falta por completo el viernes 2026-10-23 en todo el bus — ver
`buy-retest.md` y la revisión semanal hallazgo 1 para el detalle del
pipeline; no es específico de este playbook. Gate de ejecución sin
cambio: INV sigue fuera de `shadowRules`. Las decisiones de la revisión
semanal (confianza de `sl_basis_retest`, alerta de racha del modo
sombra) son específicas de `kind=RETEST` y no aplican a este playbook.
Ningún candidato con n≥20 para proponer cambio de input.

### Veredicto global
1m n=309 WR 46.3% E[R]=**0.078** PF=1.18 (estable); 2m n=113 WR 47.8%
E[R]=**0.126** PF=1.3 (sube); 5m n=26 WR 53.8% E[R]=**0.031** PF=1.07
(baja, +3 pares). NUEVO: 3m n=1 — testimonial. `segment_significance`:
1m CI90=[-0.034,0.184] n=292 (sigue sin certificar); 2m
CI90=[-0.072,0.345] n=109 (sin certificar); 5m CI90=[-0.31,0.366] n=24
(sin certificar) — ningún TF de este playbook certifica FDR, sin
cambio de fondo. `sl_origin_vs_layer.since_change` (ventana
post-2026-09-26 del experimento `sl_basis_retest`, medición paralela,
no aplicado en INV): **1m INV/SHORT PIERDE hoy la certificación
negativa que sostenía desde el 10-26** (delta -0.288→**-0.173**,
CI90=[-0.513,-0.065]→**[-0.435,0.087]**, n132→160, ahora cruza cero) —
una sola lectura, no se trata como reversión confirmada, se vigila.
Sigue sin evidencia de que el SL-mecha ayude en INV tampoco, así que la
recomendación de no extender `sl-retest-wick` a `kind=INV` no cambia.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar en ninguna rama:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tf=1m`/`2m`/`5m` | ninguno certifica FDR hoy | 292/109/24 | E[R] 0.078/0.126/0.031, todos CI90 cruzan cero | baja |
| 2 | símbolo (`cross_instrument`) | los tres TF `instrument-specific` — NO generalizar | — | sin veredicto único | baja |
| 3 | mover SL a mecha del retest en INV (`sl_basis_retest`, medición paralela) | **NO proponer** — perdió hoy la certificación negativa que tenía, vigilar antes de recalificar | 160 (1m) | delta -0.173 CI90=[-0.435,0.087] (cruza cero) | baja — una sola lectura de la reversión |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=292 delta=**+0.199**
  (la gestión sigue ayudando mucho más que en cualquier otro segmento del
  bus, sobre E[R] base cercano a cero); 2m n=109 delta=**+0.167**; 5m
  n=24 delta=**+0.1** (sube con los pares nuevos, sigue chico). Sin
  cambio de regla.
- **SL de 3 capas vs SL = vela 1 del FVG**: ver Veredicto global — ya
  no confirma en ninguna dirección en 1m, no proponer.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL (n=178, INV/SHORT, +16 pérdidas nuevas hoy): `RR-bajo`
  75/178 (42.1%) causa dominante, `contra-estructura` 54/178 (30.3%)
  segundo, `estirado` 39/178 (21.9%) tercero — sin cambio de orden.
- **Decaimiento a vigilar (sigue sin ser formal)**: W44 (semana en
  curso) 1m n=31 WR38.7% E[R]=0.031 (más débil que el promedio de
  W41-W43 ~WR45-58%, pero la caída no llega a 15pts, no es alerta
  formal); 2m n=12 WR66.7% E[R]=0.213; 5m n=3 WR33.3% E[R]=-0.527
  (2m/5m siguen con muestra demasiado chica para leer).

### Cruce con Session Analyst
`session_analyst_cross.by_kind_side`: `AVOID` n=32 E[R]=**-0.247**
WR34.4% (sin pares nuevos hoy; sigue siendo la caída más fuerte de los
cuatro playbooks de este bus, confirma la hipótesis "AVOID rinde peor"
de forma muy clara para este lado específico); `GO` n=30 E[R]=**0.208**
WR60.0% (+7, baja un poco de 0.22 pero sigue el más alto); `WAIT`
n=197 E[R]=**0.137** WR49.7% (+18, sube de 0.112). Orden
GO > WAIT >> AVOID sin cambio — sigue siendo la lectura por side más
alineada con la hipótesis original de todo el bus (contraste directo
con `sell-retest.md`, donde el bus completo ahora muestra a WAIT como
el único verdict significativo — ver `buy-retest.md`/`sell-retest.md`
para esa lectura agregada).

### Decaimiento
Ver "Contextos a evitar" arriba — 1m/INV/SHORT algo más débil en W44
que el promedio reciente (sin llegar al umbral de 15pts), 2m/5m con
muestra todavía insuficiente para leer.

## Histórico de cambios
- 2026-10-29 (jueves): lote grande de dato atrasado (+41 en este
  playbook: 1m+28, 2m+9, 5m+3), más `3m/INV/SHORT` nuevo (n=1,
  testimonial). **`since_change` de `sl_basis_retest` en 1m/INV/SHORT
  PIERDE la certificación negativa que sostenía desde el 10-26**
  (delta -0.288→-0.173, CI90 vuelve a cruzar cero, n132→160) — una
  sola lectura, se vigila, no se recalifica todavía. Ningún TF certifica
  FDR. Orden GO > WAIT >> AVOID en Session Analyst sin cambio. Sin
  cambios de regla.
- 2026-10-28 (miércoles): **cero pares nuevos**, ~36h sin commit de
  `signals`/`outcomes` en el bus (último 2026-10-26T13:31Z) — ver
  `buy-retest.md`. Pipeline hermano confirmado sano. Todas las cifras
  idénticas a ayer.
- 2026-10-27 (martes): +5 pares nuevos (1m+3, 2m+2), chico y normal,
  +3 pérdidas nuevas (n=162). `since_change` de `sl_basis_retest` en
  `1m/INV/SHORT` suma su TERCERA lectura seguida confirmando negativo
  (delta-0.288, n=132) — refuerza no extender el cambio de SL a INV.
  Cruce con Session Analyst sin pares nuevos en ningún verdict.
- 2026-10-26 (lunes): +2 pares nuevos (1m+1, 2m+1), chico y normal.
  `since_change` de `sl_basis_retest` en `1m/INV/SHORT` se afirma un
  poco en negativo con el par nuevo (delta-0.305, n=129) — refuerza no
  extender el cambio de SL a INV, documentado hoy en
  `experiments.json`. Contraste con `buy-ifvg.md` (INV/LONG da signo
  positivo) — el efecto es específico de lado. Modo sombra dispara hoy
  su alerta de 3 semanas sin batir al crudo (no aplica a INV).
- 2026-10-25 (domingo, REVISIÓN SEMANAL): sin pares nuevos desde
  ayer en ningún TF — falta por completo el viernes 2026-10-23 en todo
  el bus (ver `buy-retest.md` y `reviews/2026-week-43.md`). Sin
  cambios de regla en este playbook (las decisiones de la revisión
  semanal son específicas de RETEST).
- 2026-10-24 (sábado): dato de cierre del viernes (+11 en todo el
  playbook, el más activo en días para 5m con +3). Sin hallazgo
  material nuevo de fondo; ningún TF certifica FDR todavía. `since_change`
  de `sl_basis_retest` en 1m INV/SHORT sigue confirmando negativo pero
  se afloja un poco (delta -0.352→-0.284) — sigue correcto no extender
  el cambio de SL a INV. Orden GO > WAIT >> AVOID sin cambio, sigue
  siendo la lectura más alineada con la hipótesis Session Analyst de
  todo el bus. Sin incidentes de pipeline.
- 2026-10-23 (viernes): dato mínimo (+2 en todo el playbook), sin
  hallazgo material nuevo. `GO` se mantiene el más alto del cruce con
  Session Analyst, sube un poco (n=21, E[R]=0.26). `AVOID` sin pares
  nuevos — el motor fusionado del Session Analyst lleva ~8h sin
  refrescar según su propio plan (ver `buy-retest.md`). Sin incidentes
  de pipeline.
- 2026-10-22 (jueves): dato mínimo (+14 en todo el playbook), sin
  hallazgo material nuevo. `GO` se mantiene el más alto del cruce con
  Session Analyst aunque baja un poco (n=20, E[R]=0.248). Orden
  GO>WAIT>>AVOID sin cambio — contraste notable con la inversión de
  orden de hoy en `sell-retest.md`. Sin incidentes de pipeline.
- 2026-10-21 (miércoles): dato mínimo (+6 en todo el playbook), sin
  hallazgo material nuevo. `GO` se fortalece un poco (n=18,
  E[R]=0.387). Orden GO>WAIT>>AVOID sin cambio. Sin incidentes de
  pipeline.
- 2026-10-20 (martes): dato mínimo (+3 en todo el playbook), sin
  hallazgo material nuevo. Orden GO>WAIT>>AVOID se mantiene (en
  contraste con `sell-retest.md`, donde se invirtió hoy). Sin
  incidentes de pipeline.
- 2026-10-19 (lunes): dato mínimo (+1 en 1m), sin hallazgo material
  nuevo. Session Analyst sin señales nuevas en ningún veredicto, orden
  GO>WAIT>>AVOID sin cambio. Mismo incidente de infraestructura git
  documentado en `buy-retest.md`.
- 2026-10-18 (domingo, REVISIÓN SEMANAL): dato mínimo (+1), sin
  hallazgo material nuevo — ver `reviews/2026-week-42.md`. La reversión
  de `1m/INV/SHORT` se confirma y se fortalece con W42 cerrada
  (n=23, E[R]=0.183, sube de 0.174). Sin incidentes de pipeline.
- 2026-10-17 (sábado): sin hallazgo material nuevo en este playbook,
  dato mínimo (segmento de prioridad 2). La reversión de `1m/INV/SHORT`
  en W41→W42 se confirma con la semana ya cerrada (n=22, E[R]=0.174,
  sin caer). Salto grande de dato en el resto del bus por el fin de
  semana largo. Sin incidentes de pipeline.
- 2026-10-16 (viernes): sin hallazgo material nuevo, dato mínimo. `git
  pull` encontró `HEAD` detached, resuelto con `git checkout main &&
  git pull` sin pérdida de datos. La reversión de `1m/INV/SHORT` en
  W42 que empezaba a verse ayer **se confirma con el doble de muestra**
  (n=10→21, E[R] -0.007→+0.23, ya claramente positivo). `GO` en
  `session_analyst_cross` baja de 0.476 a 0.377 con un par nuevo pero
  sigue siendo el mejor de los tres veredictos. `sl_origin_vs_layer.
  since_change` en 1m INV/SHORT sin cambio de fondo (n=103,
  delta=-0.37, prácticamente igual a ayer) — confirma que está bien no
  extender el SL de mecha del retest a INV.
- 2026-10-15 (jueves): sin hallazgo material nuevo, dato mínimo. `git
  pull` limpio sin incidentes. `sl_origin_vs_layer.since_change` en 1m
  INV/SHORT sigue empeorando con significancia (n=98, delta=-0.373,
  ayer -0.331 n=92) — confirma que está bien no extender el SL de mecha
  del retest a INV.
- 2026-10-14 (miércoles): sin hallazgo material nuevo, dato mínimo.
  `git pull` sin incidente de divergencia. 1m/INV/SHORT W42 parcial
  mejora levemente (n=5→10, E[R] -0.122→-0.007) pero sigue sin cruzar a
  positivo.
- 2026-10-13 (martes): sin hallazgo material nuevo, dato mínimo. Mismo
  incidente de reescritura de `origin/main` que `buy-retest.md`,
  resuelto igual.
- 2026-10-11 (domingo, REVISIÓN SEMANAL): se retira la alerta `SIGID`
  (fix de emparejamiento en `analyze.py`, ver `buy-retest.md`) —
  recupera pares sin dato nuevo real, `huérfanos` 40→44. Sin hallazgo de
  fondo propio: ningún TF certifica FDR todavía, patrón de SL
  (`candle1` perjudica en 1m) y de Session Analyst (AVOID muy negativo,
  la lectura más alineada con la hipótesis de todo el bus) sin cambio.
  Nota cruzada: `sell-retest.md` (RETEST/SHORT) muestra hoy el patrón
  inverso de Session Analyst (AVOID > WAIT) — este playbook (INV/SHORT)
  sigue siendo el más alineado con "AVOID rinde peor", confirma que es
  un efecto de `kind`/side combinado, no sólo de side. Nada que proponer
  para `scalp_command.pine` desde este playbook esta semana (n
  insuficiente en las tres ramas). Ver `reviews/2026-week-41.md`.
- 2026-10-10 (sábado): sin hallazgo nuevo material. 1m/INV/SHORT y
  2m/INV/SHORT confirman la recuperación de W41 que se veía parcial
  ayer (W41 ya con n=39/9, E[R]=+0.133/+0.377). Dato nuevo mínimo
  +4/+1/+0 (1m/2m/5m).
- 2026-10-09 (viernes): `origin/main` llegó con el historial git
  reescrito — ver nota completa en `buy-retest.md`, sin pérdida de
  contenido. Dato +11/+1/+2 en 1m/2m/5m. 1m INV/SHORT vuelve a positivo
  (E[R]=0.028, vs -0.009 ayer) confirmando que el cruce a negativo de
  ayer era ruido de n chico, no tendencia. `decay_weekly_by_segment`
  de 1m también se recupera (W41 E[R]=+0.165 vs W40 -0.059) — ya no hay
  racha negativa de dos semanas en este TF. Sin hallazgo nuevo en
  `sl_origin_vs_layer` (mismo patrón, 1m sigue perjudicado con
  significancia). Nota menor: el conteo absoluto de la causa de SL
  `RR-bajo` bajó de 57 a 56 pese a que n subió — consistente con el
  reordenamiento de pares por la colisión de `sigId` que señala
  `report.alerts`, no una mejora real.
- 2026-10-08 (jueves): `git pull` sin incidente real (ver
  `buy-retest.md`). Dato +8/+2/+0 en 1m/2m/5m. **Hallazgo nuevo
  (compartido con `buy-ifvg.md`): primera lectura con muestra real de
  `sl_origin_vs_layer.since_change` para INV/SHORT — mover el SL a la
  vela 1 del FVG perjudicaría con significancia en 1m** (delta=-0.341,
  CI90=[-0.61,-0.066], `delta_below_zero=true`); 2m inconcluso (CI muy
  ancho). Entre los dos playbooks INV, el cambio sólo ayudaría en 1m
  INV/LONG — conclusión cruzada: no extender el cambio de SL aplicado en
  RETEST a ningún segmento INV. Primera lectura propia del cruce con
  Session Analyst por `kind/side`: `AVOID` sale muy negativo aquí
  (E[R]=-0.447, PF=0.3, n=28) — la confirmación más clara de la
  hipótesis "AVOID rinde peor" de los cuatro playbooks, aunque con n
  todavía chico. 1m INV/SHORT cruza a E[R] ligeramente negativo
  (-0.009), sin significancia, dentro del ruido habitual.
- 2026-10-07 (miércoles): `git pull` limpio. Dato mínimo (+2/+0/+0 en
  1m/2m/5m), normal para INV. 1m cruza de vuelta a E[R]≈0 (-0.002→0.004),
  ruido de n chico, sin cambio de fondo — ningún TF certifica FDR.
  `rr1_threshold_cut_oos` (hallazgo del día en RETEST, ver
  `buy-retest.md`/`sell-retest.md`) no aplica a INV. Sin hallazgos
  propios nuevos hoy.
- 2026-10-06 (martes): incidente de repo del día (ver `buy-retest.md`),
  sin pérdida. Dato nuevo chico (+9/+3/+1 en 1m/2m/5m). 1m vuelve a
  cruzar a E[R] ligeramente negativo (-0.002), dentro del ruido habitual
  de este playbook (sigue sin certificar FDR en ningún TF). Sin cambios
  de fondo ni relación clara con el deterioro de RETEST reportado en
  `buy-retest.md` — muestra demasiado chica para una lectura propia.
- 2026-10-05 (lunes): `git pull` trajo jsonl nuevo real al bus pero cero
  trades nuevos en INV/SHORT (n sin cambio en los tres TF). Sin alerta
  `MUESTRA` en este playbook hoy (sí la tiene `buy-ifvg.md`, ver ahí).
  Sin cambios de fondo.
- 2026-10-04 (domingo, REVISIÓN SEMANAL): sin jsonl nuevo del cron, n sin
  cambio en los tres TF. Sin cambios de fondo en este playbook; foco de la
  revisión semanal en RETEST (ver `buy-retest.md` y
  `reviews/2026-week-40.md`) — gate 0→1 de modo sombra y baja de confianza
  del "cambio del mes" `sl_basis_retest`, ninguno aplica a INV.
- 2026-10-03 (sábado): dato nuevo mínimo (+3/+4/+0 en 1m/2m/5m). Ningún TF
  certifica FDR, sin cambio de fondo. El punto a vigilar (1m/2m INV/SHORT
  negativos en W40) se recupera en ambos TF hoy — se corrige la nota de
  ayer que decía que 2m empeoraba. Ver `buy-retest.md` → Histórico de hoy
  para el hallazgo metodológico del día (no aplica a este playbook).
- 2026-10-02 (viernes): `git pull` limpio (fast-forward). Dato nuevo
  minimo (+7/+5/+1 en 1m/2m/5m). Sigue siendo el playbook con menos edge
  estadistico confirmado de los cuatro. El punto a vigilar de ayer
  (1m/INV/SHORT cayendo en W40) se recupera un poco (WR 32.4%->37.0%,
  E[R] -0.229->-0.112) pero 2m/INV/SHORT empeora (E[R] -0.165->-0.193) --
  2 corridas seguidas con el mismo signo en ambos TF, todavia sin n
  suficiente para tratarlo como decaimiento confirmado. Ver
  `buy-retest.md` para el hallazgo de pipeline (colision de sigId sigue
  creciendo).
- 2026-10-01 (jueves): `git pull` limpio. Dato nuevo minimo (+12/+1/+2 en
  1m/2m/5m). Sigue siendo el playbook con menos edge estadistico
  confirmado de los cuatro (ningun TF certifica FDR hoy). Hallazgo a
  vigilar: `decay_weekly_by_segment` muestra 1m/INV/SHORT cayendo de WR
  50.0% (W39, n=42) a WR 32.4% (W40, n=37, parcial) -- por encima del
  umbral de 15pts, pero n chico y semana sin cerrar, no se trata como
  decaimiento confirmado todavia. Ver `buy-retest.md` para el hallazgo de
  pipeline del dia (colisiones de sigId).
- 2026-09-30 (miércoles): +19 señales INV/SHORT nuevas (13 en 1m, 6 en
  2m), el mayor salto de dato de este playbook en varios días. Sin
  cambios de fondo en las conclusiones: ningún TF certifica FDR,
  `RR-bajo` sigue causa dominante de SL, `AVOID` sigue siendo la peor
  rama de Session Analyst (patrón opuesto al resto del bus, ya
  documentado). 1m cruza a E[R] ligeramente negativo (+0.005→-0.005),
  tercer valor distinto en tres corridas seguidas (+0.046→+0.005→-0.005)
  — sigue dentro del rango de ruido de su CI90 ancho ([-0.148,0.132]),
  no se lee como decaimiento real. El hallazgo grande del día (reversión
  del SL estructural en LONG de RETEST) es de `kind=RETEST` y no aplica
  aquí — ver `buy-retest.md`.
- 2026-09-29 (martes): +13 señales INV/SHORT nuevas (la mayoría en 1m),
  el mayor salto de dato de este playbook en varios días. Sin cambios de
  fondo en las conclusiones: ningún TF certifica FDR, `RR-bajo` sigue
  causa dominante de SL, `AVOID` sigue siendo la peor rama de Session
  Analyst (patrón opuesto al resto del bus, ya documentado). E[R] crudo
  de 1m/2m cae bastante (1m +0.046→+0.005, 2m +0.112→+0.08) pero dentro
  del rango de ruido que ya mostraban sus CI90 anchos — no se lee como
  decaimiento real. `nearEdge=-1` cambia de signo (+0.032→-0.019) con
  n=127, todavía poco fiable. El hallazgo grande del día (reversión del
  SL estructural en el lado LONG y en 5m SHORT de RETEST) no aplica a
  INV — ver `buy-retest.md`/`sell-retest.md`.
- 2026-09-28 (lunes): +2 señales INV/SHORT nuevas (1m). Sin cambios de
  fondo: ningún TF certifica FDR, `tier=B` cruza a E[R] levemente
  negativo (-0.011) mientras `tier=C` se mantiene positivo. El fix de
  `analyze.py` y el hallazgo del SL estructural de hoy (ver
  `buy-retest.md`) son de `kind=RETEST`, no tocan este playbook.
- 2026-09-27 (domingo, REVISIÓN SEMANAL): sin dato nuevo (fin de semana,
  n idéntico a ayer en los tres TF: 134/58/12). La revisión semanal de
  hoy no afecta a este playbook (las tres decisiones — SL estructural
  aplicado, `rr1_threshold_cut_oos`, `SHADOW_RULES_V1` v2 — son todas de
  `kind=RETEST`, ver `buy-retest.md`). Sin cambios de veredicto: ningún
  TF certifica FDR, INV/SHORT sigue siendo el único playbook donde
  "WAIT/GO mejor que AVOID" no se sostiene. Nada accionable nuevo.
- 2026-09-26 (sábado): **confirma la cautela de ayer**: tanto 1m
  INV/SHORT (E[R] +0.072→+0.036) como el cruce con Session Analyst
  (`WAIT` +0.052→-0.01) revirtieron casi por completo el salto positivo
  de la corrida anterior, que ya se había anotado como "una sola
  lectura, no cambio de régimen" — buen ejemplo de método funcionando
  como debería. 2m INV/SHORT sí sostiene su cruce a positivo de ayer
  (E[R] 0.118→0.112, casi sin cambio). Ningún TF certifica FDR. Mismo
  incidente de repo que `buy-retest.md` (merge en vez de reset, sin
  pérdida). Sin propuestas nuevas — n sigue muy por debajo del piso de
  20 en 5m y sin patrón estable en el resto.
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
