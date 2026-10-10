# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-10-10 (sábado) · n: 317)

### Nota de proceso
`git pull` encontró `HEAD` detached por un `main` local desactualizado,
sin incidente de fondo (ver `buy-retest.md`). Dato nuevo mínimo (+4/+1/+0
en 1m/2m/5m) — normal, INV sigue siendo mucho más esporádico que RETEST.
Gate de ejecución sin cambio: INV sigue fuera de `shadowRules`.

Sin hallazgo nuevo material — `sl_origin_vs_layer.since_change`
(`candle1`) confirma el mismo patrón de siempre: 1m INV/SHORT sigue
perjudicado con significancia (n=82, delta=**-0.396**
CI90=[-0.634,-0.15]); 2m sigue inconcluso (n=27, delta=-0.116
CI90=[-0.9,0.827], CI90 demasiado ancho); 5m (n=5) sigue sin muestra
para bootstrap. Sin cambio en la conclusión cruzada: no extender
`sl-retest-wick`/`candle1` a ningún segmento INV.

### Veredicto global
1m n=215 (+4) WR 44.7% E[R]=**0.024** PF=1.05 (baja un poco vs 0.028,
dentro de ruido); 2m n=84 (+1) WR 42.9% E[R]=**0.093** PF=1.2 (sube un
poco); 5m n=18 (sin dato nuevo) WR 55.6% E[R]=**0.128** PF=1.34 (sin
cambio). `segment_significance`: 1m CI90=[-0.107,0.158] n=202 (sigue sin
certificar); 2m CI90=[-0.142,0.356] n=81 (sin certificar); 5m
CI90=[-0.304,0.572] n=16 (sin certificar) — ningún TF de este playbook
certifica FDR, sin cambio de fondo.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar en ninguna rama:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tf=1m`/`2m`/`5m` | ninguno certifica FDR hoy | 202/81/16 | E[R] 0.024/0.093/0.128, todos CI90 cruzan cero | baja |
| 2 | `tier=B` | sigue negativo | 105 | E[R]=**-0.016** PF=0.97 | baja |
| 3 | `tier=C` | positivo, sigue mejor que B | 212 | E[R]=**+0.082** PF=1.19 | baja-moderada |
| 4 | símbolo (`cross_instrument`) | los tres TF `instrument-specific` — NO generalizar | — | sin veredicto único | baja |
| 5 | mover SL a vela 1 del FVG (`candle1`) | **NO proponer** — perjudica con significancia en 1m, inconcluso en 2m/5m | 82 (1m) / 27 (2m) / 5 (5m) | delta -0.396 (1m, confirma negativo) / -0.116 (2m, CI90 ancho) / -0.214 (5m, n mínimo) | moderada |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente todavía.

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=202 delta=**+0.213**
  (la gestión sigue ayudando mucho más que en cualquier otro segmento del
  bus, sobre E[R] base cercano a cero); 2m n=81 delta=**+0.086**; 5m
  n=16 delta=**+0.08**. Sin cambio de regla.
- **SL de 3 capas vs SL = vela 1 del FVG**: ver Nota de proceso arriba —
  perjudica en 1m, no proponer.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL (n=134, INV/SHORT): `RR-bajo` 57/134 (42.5%) causa
  dominante, `contra-estructura` 41/134 (30.6%) segundo, `estirado`
  31/134 (23.1%) tercero — sin cambio de fondo.
- **Decaimiento a vigilar (sigue sin ser formal)**: `decay_weekly_by_segment`
  1m/INV/SHORT W40 (cerrada) E[R]=**-0.059** → W41 (n=39)
  E[R]=**+0.133** — se confirma la recuperación, W41 cierra cerca de
  WR estable (41.0%). 2m/INV/SHORT W40 E[R]=-0.018 → W41 (n=9)
  E[R]=**+0.377** — sigue siendo n chico, no leer como tendencia. 5m
  sigue negativo ambas semanas (W40 -0.36, W41 -0.513) con n=3 cada
  una — ruido puro, sin muestra para decidir.

### Cruce con Session Analyst
`session_analyst_cross.by_kind_side`: `AVOID` n=28 E[R]=**-0.447** PF=0.3
— la caída más fuerte de los cuatro playbooks, confirma la hipótesis
"AVOID rinde peor" de forma muy clara para este lado específico; `GO`
n=10 E[R]=**0.502** (n mínimo); `WAIT` n=137 E[R]=**0.05**. Orden
GO > WAIT >> AVOID, con AVOID muy por debajo — aunque el n de AVOID (28)
y GO (10) siguen chicos para certificar con CI90 propio, es la lectura
por side más alineada con la hipótesis original de todo el bus.

### Decaimiento
Ver "Contextos a evitar" arriba — 1m y 2m se recuperan en W41, sin
racha negativa clara en este playbook salvo 5m (n demasiado chico).

## Histórico de cambios
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
