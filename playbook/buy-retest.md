# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-09 · n: 2950)

### Nota de proceso — día de "calma": sin fecha nueva, solo resolución de pendientes
`git pull` esta vez no mostró "forced update" (ya estaba al día).
`file_integrity_check` sin alertas (ningún archivo encogió). **No llegó
ningún `signals/*.jsonl` ni `outcomes/*.jsonl` fechado 2026-09-09** — lo
único que cambió fue que `signals/2026-09-08.jsonl` creció de 47 a 408
líneas (más señales del mismo día ya conocido llegando tarde al bus) y
`outcomes/2026-09-08.jsonl` se mantuvo en 55. Resultado: +39 pares nuevos
en este playbook (n 2911→2950; 1m 1754→1776, 2m 861→872, 5m 296→302), y
**los tres TF tienen exactamente el mismo número de SL que ayer** (873/1m,
433/2m, 127/5m) — los 39 pares nuevos fueron todos TP o TIMEOUT, cero SL
nuevos. Por eso casi todas las métricas de abajo coinciden a 2-3 decimales
con la corrida de ayer: es una corrida de **confirmación de estabilidad**,
no de datos genuinamente nuevos de una nueva sesión.

### Veredicto global
1m n=1776 (+22) WR 43.9% (bajó de 44.5% solo por dilución de TO/TP nuevos)
E[R]=**-0.005** PF=0.99 (sin cambio); 2m n=872 (+11) WR 45.8% E[R]=**-0.04**
PF=0.92 (sin cambio); 5m n=302 (+6) WR 52.0% E[R]=+0.081 PF=1.18 (sin
cambio) sigue siendo el mejor TF crudo. `segment_significance` idéntico a
ayer en los tres TF: 1m CI90=[-0.055,0.045] p=0.577 n=1720; 2m
CI90=[-0.102,0.023] p=0.843 n=846; 5m CI90=[-0.03,0.194] p=0.114 n=285 —
la muestra que usa el bootstrap de significancia no creció con los 39
pares nuevos (mismo patrón ya visto ayer, parece haber un rezago antes de
que un par entre a este cálculo; no tratar como anomalía todavía, vigilar
si se mantiene rezagado varios días más). Veredicto sin cambios: **1m sin
señal, 2m negativo sin certificar (vigilar), 5m mejor TF sin confirmar
estadísticamente.**

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna certifica con `survives_fdr10` (esa prueba corre por tf/kind/side,
no por estos cortes):

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tier=A+` | sigue siendo el peor tier por WR, E[R] se mantiene positivo | 223 (+5) | WR 22.9%, E[R]=0.02, PF=1.03 (137 SL, sin cambio — los 5 nuevos fueron TP/TO) | baja-moderada — segundo día seguido con E[R] positivo tras el giro de ayer, pero WR sigue bajísimo (22.9%), no tratar como asentado |
| 2 | `tier=B` | TOMAR, prioridad sobre A+ y C | 1140 (+17) vs 1587 (+17) tier C | WR 43.9% E[R]=0.011 PF=1.02 vs tier C WR 49.4% E[R]=-0.023 PF=0.95 | alta — sin cambio de sentido, B sigue siendo la única rama de tier con E[R] positivo estable en LONG |
| 3 | símbolo (`cross_instrument`), 1m | sigue `universal` | GC n=262 E[R]=0.096, NQ n=391 E[R]=0.015, YM n=291 E[R]=0.032, ES n=373 E[R]=-0.068, CL n=459 E[R]=-0.051 (spread 0.164, `universal`) | moderada — spread y E[R] por símbolo idénticos a ayer a 3 decimales (solo CL sumó 10 pares neutros) |
| 4 | `nearEdge` | sin gradiente limpio | -1: n=176 E[R]=0.044 (sin cambio); edge=0: n=1391 (+15) E[R]=-0.017; edge=1: n=1383 (+24) E[R]=-0.003 | baja — E[R] por rama idéntico a ayer, sin gradiente monótono limpio como en SELL RETEST |
| 5 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1` | 11 vs 2939 (+39) | E[R] +0.459 vs -0.008, WR 54.5% vs 45.3%, PF 4.21 vs 0.98 | baja — sigue exactamente en n=11 (van 6 revisiones sin una sola señal nueva `aligned=0` en LONG), anomalía de signo sin poder cuantificarse mejor |

**Tier A+ sostiene el giro a positivo por segundo día.** Historial: n=13
E[R]=-0.705 (09-03) → n=97 E[R]=-0.021 (09-04) → n=158 E[R]=-0.104 (09-06)
→ n=159 E[R]=-0.11 (09-07) → n=218 E[R]=+0.02 (09-08) → n=223
**E[R]=+0.02** (hoy, idéntico — los 5 pares nuevos no movieron la cifra).
Con WR 22.9% sigue siendo por lejos el peor tier en tasa de acierto
(ganadores grandes ocasionales inflando el E[R]) — no leer este giro como
"A+ ya funciona". Esperar a n≥300 antes de fijar una regla dura.

**Símbolo en 1m sigue asentándose como `universal`.** Spread y E[R] por
símbolo sin cambio hoy — CL sigue siendo el peor símbolo pero lejos del
umbral de 0.4 (`instrument-specific`). No usar "CL malo en 1m" como regla
dura.

**Anomalía a vigilar** (no accionar): el modelo P(TP1) in-sample sigue
ponderando `aligned` con signo negativo (-0.06, estable) — alineado con
el sesgo/estructura predice *peor* resultado. La rama `aligned=0` de LONG
sigue exactamente en n=11 desde hace 6 revisiones. Sigue pendiente pedir
a Jesús que confirme la definición exacta de `aligned` en Pine.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara de calidad
  de entrada en este segmento.

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=1716 delta=+0.07
  (sin cambio vs ayer); 2m n=843 delta=+0.071 (sin cambio); 5m n=285
  delta=-0.068 (sin cambio) — sigue siendo el único TF donde la gestión
  resta en LONG. Regla sin cambios: gestionar con escalera en 1m/2m, ir al
  mercado simple en 5m LONG.
- **SL estructural (`sl_origin_vs_layer`)**: sin pares nuevos hoy en este
  corte (misma n que ayer en los tres TF). 1m LONG sigue certificando
  positivo, n=1432 delta=+0.18 CI90=[0.074,0.296] (no cruza cero) —
  segunda confirmación independiente real, sostenida por segundo día. 5m
  LONG n=274 delta=+0.178 CI90=[0.005,0.38] sigue al filo del cero, sin
  nueva muestra que la refuerce o la debilite — sigue como "débil,
  vigilar". 2m n=742 delta=+0.01 (CI90 [-0.079,0.1], sigue sin
  significar). Registrado en `experiments.json`
  (`sl-retest-wick-2026-09-03`). Sigue sin aplicarse — es medición
  paralela; falta walk-forward (solo 2 semanas de datos) antes de tratarlo
  como asentado.
- Objetivo / Parcial 1 / trailing: _pendiente_ — el contrafactual global
  (`counterfactual`, n=9) no está cortado por side todavía.
- `revAfterSL_rate` por corte: `edge=-1` 46.3%, `edge=0` 41.7%, `edge=1`
  24.5% — sin cambio.

### Contextos a evitar
- **`tf=2m`**: E[R] sigue negativo (-0.04), CI90 de `segment_significance`
  sigue cruzando cero ([-0.102,0.023], n=846 sin cambio hoy) — se mantiene
  como "negativo, vigilar", todavía no "EVITAR con confianza estadística".
- Ya no generalizar "símbolo malo" en 1m (regla #3, `universal`).
- Autopsia de SL sobre las 1433 pérdidas LONG (sin cambio hoy: cero SL
  nuevos): `RR-bajo` 569/1433 (39.7%) sigue siendo la causa **dominante**,
  seguida de `contra-estructura` 549/1433 (38.3%) y `killzone-Asia-largo`
  537/1433 (37.5%) — `RR-bajo` sigue siendo el candidato principal para
  `sc_min_rr`/`sc_aplus_rr` en la revisión semanal, y es exactamente el
  tipo de pérdida que el SL estructural más ajustado (`sl_origin_vs_layer`
  arriba) ataca directamente al mejorar el R:R de cada operación.

### Cruce con Session Analyst
Sin cambio hoy (mismos n que ayer en este corte). En RETEST/LONG: bajo
veredicto SA `AVOID` el E[R] es +0.211 (n=245), bajo `GO` es -0.18
(n=173), bajo `WAIT` es +0.073 (n=346) — mismo sentido contrario a la
hipótesis de `agent-instructions.md` que ya se veía en `sell-retest.md`.
El agregado de todo kind/side sigue certificando con CI90 que no cruza
cero (ver `report.md` / `sell-retest.md` para el detalle numérico
completo).

### Decaimiento
`decay_weekly` ya reporta 2 semanas con muestra sustancial: 2026-W36
(n=3231, WR 44.6%, E[R]=-0.021) y 2026-W37 (n=1224, WR 43.7%,
E[R]=-0.016) — semana en curso sigue en la misma dirección, sin señal de
decaimiento (no hay caída de WR > 15 pts).

## Histórico de cambios
- 2026-09-01: primera escritura con datos reales (n=3, todas GC, mismo día,
  3/3 TP1). Marcado explícitamente como no accionable por tamaño de muestra.
- 2026-09-01 (tarde): refresco a n=6 (1m n=4, 2m n=2). Primera pérdida 1m
  registrada (WR baja de 100% a 75%), confirma que el 100% inicial era
  ruido. Sigue sin ser accionable (n<20).
- 2026-09-02: refresco a n=31 (1m n=18, 2m n=13). El 1m se da vuelta del
  todo: pasa de aparentar el mejor segmento a ser el peor (E[R] -0.283,
  10 SL de 18). El 2m sigue positivo pero `cross_instrument` lo marca
  instrument-specific e inflado por 3 muestras de NQ — no confiable
  todavía. `RR-bajo` sale como causa casi universal (15/15) de las
  pérdidas LONG: candidato a revisar en la próxima revisión semanal si la
  muestra aguanta. Fix de bug en `analyze.py`: `news_context` crasheaba al
  leer `market.json` del Session Analyst (trataba el dict `news.events`
  como lista de eventos y iteraba sobre sus claves) — corregido hoy, sin
  impacto en las métricas de este playbook.
- 2026-09-02 (corrida formal del agente): refresco n=31->39 (1m n=18->25, 2m
  n=13->14). El 1m se mantiene negativo (-0.283->-0.224), ya no es un salto
  raro sino la lectura estable. El corte `nearEdge` cambia de forma: ahora
  es `edge=0` la peor rama (no `edge=-1` como parecía con n chico) -
  patrón no-monótono y distinto al de SELL RETEST, donde `edge=1` es
  siempre el mejor. La rama `aligned=0` (la buena, E[R]=+0.459) se quedó
  exactamente en n=7 - las 8 señales LONG nuevas fueron todas `aligned=1`,
  así que la anomalía de signo en `aligned` sigue sin poder cuantificarse
  mejor. Autopsia de SL recalculada sin cap de 60 filas: las tres causas
  `contra-estructura`/`stop-en-el-mínimo`/`RR-bajo` siguen casi universales
  (16-17 de 18 pérdidas). Mejora permanente en `analyze.py`: cortes
  cruzados `by_kindside_edge`/`by_kindside_tier`/`by_kindside_aligned`
  agregados (ver detalle en `sell-retest.md`).
- 2026-09-03: salto de muestra fuerte n=39→325 (1m 25→217, 2m 14→78, 5m
  0→30 — primeros datos 5m). El 1m se revierte de EVITAR a casi breakeven
  (E[R] -0.224→+0.034): confirma que la lectura negativa previa era
  todavía ruido de muestra chica, no un patrón real. `tier=A+` aparece por
  primera vez en LONG (n=13) y es el peor resultado de todo el dataset
  (E[R]=-0.705) — mismo signo invertido que en SELL RETEST, ahora
  confirmado en ambos lados. Nuevo hallazgo con n grande: por símbolo, CL
  rinde mal y YM muy bien en 1m y 2m simultáneamente (`cross_instrument`).
  Nuevo contraste con SELL RETEST: ni la escalera gestionada
  (`managed_vs_naive`) ni el SL estructural (`sl_origin_vs_layer`) ayudan
  en LONG — en 2m/5m la gestión con parciales pierde contra el ingenuo, y
  el SL estructural no mejora en ningún TF. Autopsia de SL con el nuevo
  desglose permanente por kind/side de `analyze.py` (n=152 pérdidas):
  `RR-bajo` pasa a ser causa dominante única (47%), ya no empatada a tres.
  Mejora permanente en `analyze.py`: `sl_post_mortem.causes_by_kind_side`
  (autopsia de SL sin cap de 60 filas, por segmento) — ya no hace falta
  recalcularlo a mano cada corrida como en las dos revisiones anteriores.
- 2026-09-04: salto de muestra n=325→1641 (1m 217→993, 2m 78→491, 5m
  30→157). **Se corrigen dos anomalías de la revisión anterior, ambas por
  el mismo mecanismo (n chico haciéndose pasar por patrón real):**
  `tier=A+` pasó de "peor resultado del dataset" (n=13, E[R]=-0.705) a
  resultado moderado (n=97, E[R]=-0.021, ya no el peor tier por E[R] — hoy
  lo es `tier=C`); y "YM rinde muy bien" en 2m se invirtió del todo
  (n=10 E[R]=+1.037 → n=121 E[R]=-0.201), llevando ese corte de
  `instrument-specific` a `universal`. **Hallazgo nuevo y más sólido:**
  2m/RETEST/LONG certifica como negativo en `segment_significance`
  (CI90=[-0.208,-0.049], no cruza cero) — primer segmento de todo el
  dataset con evidencia estadística de E[R]<0, útil recordar que
  `survives_fdr10=false` no significa "sin señal" cuando el CI no cruza
  cero por el lado malo (esa bandera solo certifica edge positivo).
  `managed_vs_naive` y `sl_origin_vs_layer` cambian de signo en 1m y 2m
  (ambos pasan de negativo/nulo a positivo, aunque sin certificar) —
  contradice la conclusión de ayer de que ninguno ayuda en LONG; sigue
  siendo cierto solo para 5m. Nota de proceso: `git pull` volvió a
  reportar "forced update" sobre `origin/main` al inicio de esta corrida
  (rama local `main` apuntaba a un commit viejo y divergente); se verificó
  que el commit remoto (`origin/main`) contenía todo el trabajo esperado
  (`analyze.py`, playbooks, experiments.json) antes de resetear la rama
  local — sin pérdida de trabajo, pero es la segunda vez que pasa (ver
  nota del 2026-09-02 en `sell-retest.md`).
- 2026-09-05: **hallazgo de pipeline, no de trading**: se detectó y
  corrigió una pérdida real de datos (commit `92917b8` había borrado 1256
  de 1280 señales de `signals/2026-09-03.jsonl` bajo el mensaje engañoso
  "heal 24 orphan signal(s)"; restaurado desde `f239309` sin pérdida, ver
  nota al inicio de la Sección viva). n saltó de 1641 a 2276 en LONG (todo
  el dataset 1884→3140) por esa restauración, no por señales nuevas.
  `tier=A+` volvió a empeorar (E[R] -0.021→-0.104, n=97→158), tercera
  lectura distinta en 3 días — confirma que sigue sin ser confiable como
  regla dura. `cross_instrument` en 1m pasó de `instrument-specific` a
  `universal` (el spread por símbolo se diluyó al restaurar la muestra).
  Hallazgo más importante: `sl_origin_vs_layer` en 1m LONG **certificó
  positivo por primera vez** (delta=+0.181, CI90 no cruza cero) — hasta
  ayer esta rama se consideraba plana/opuesta y el experimento
  `sl-retest-wick-2026-09-03` excluía explícitamente a BUY RETEST; se
  amplió el segmento del experimento y se marcó el giro como pendiente de
  confirmar el 2026-09-06 (coincide con el mismo día de la restauración,
  podría ser artefacto). Mejora permanente en `analyze.py`:
  `session_analyst_cross` — cruza el veredicto GO/WAIT/AVOID del Session
  Analyst (parseado de sus planes `pre-asia/pre-london/pre-ny`) contra el
  resultado real de las señales scalp del mismo símbolo+sesión+día; ver
  `report.md` para el resultado agregado (todo-kind), sorprendentemente
  contrario a la hipótesis original de agent-instructions.md.
- 2026-09-06 (revisión semanal, domingo): **el mismo bug de "heal" volvió a
  borrar `signals/2026-09-03.jsonl` una segunda vez** (commit `0cf0a30`,
  deshaciendo el arreglo de ayer); restaurado de nuevo desde `945c337`. Sin
  dato de mercado nuevo (CME cerrado el fin de semana) — todas las cifras
  de esta revisión son idénticas a 2026-09-05, lo que SÍ confirma que el
  giro de `sl_origin_vs_layer` en 1m LONG no era artefacto de la
  restauración de ayer (ver Gestión). Mejora permanente en `analyze.py`:
  `file_integrity_check` — alerta si algún `signals/outcomes/*.jsonl`
  encoge respecto al máximo visto en corridas previas, para detectar este
  tipo de borrado automáticamente sin depender de que el agente note el
  tamaño del diff a mano. Ver `reviews/2026-week-36.md` para la revisión
  semanal completa (primera del bus).
- 2026-09-07 (lunes, festivo EE.UU. — Globex con volumen reducido):
  **primer día sin repetición del bug de "heal"** — `file_integrity_check`
  confirma que ningún archivo encogió. n subió de 2292 a 2366 en LONG
  (1355→1412 en 1m, 687→708 en 2m, 234→246 en 5m) con dato genuinamente
  nuevo, no restaurado. Hallazgo más importante: `sl_origin_vs_layer` en
  1m LONG creció de n=1087 a n=1135 con trades nuevos y el delta se
  mantuvo (+0.181→+0.183, CI90 sigue sin cruzar cero) — es la primera
  confirmación independiente real de este hallazgo (hasta ayer todo el
  crecimiento venía de restaurar datos truncados, no de trades nuevos).
  `tf=2m EVITAR` se sostiene con dato nuevo (CI90 pasa de rozar cero
  [-0.142,0.0] a quedar del lado negativo [-0.139,-0.002]). `tier=A+`
  tiene su segunda lectura consecutiva cerca de -0.11 (antes -0.104),
  primera señal de estabilización tras 3 lecturas dispares. `decay_weekly`
  ya reporta una segunda semana (2026-W37, n=26 todavía chico) — primera
  vez que hay más de una semana para comparar decaimiento.
- 2026-09-08 (martes, primer día hábil completo post-feriado): salto de
  muestra grande n=2366->2911 (1m 1412->1754, 2m 708->861, 5m 246->296).
  **Reversión importante**: la certificación de `2m/RETEST/LONG` como
  negativo que se veía "estadísticamente estable" ayer (CI90
  [-0.139,-0.002]) se revirtió al crecer la muestra (CI90 hoy
  [-0.102,0.023], vuelve a cruzar cero) — se degrada la regla de EVITAR a
  "negativo sin certificar", lección de método sobre no fijar una
  conclusión con muestra todavía mediana. `sl_origin_vs_layer` en 1m LONG
  creció de n=1135 a 1432 con el delta estable (+0.183->+0.18, sigue
  certificando) — segunda confirmación independiente; **5m LONG certifica
  por primera vez** (n=274, delta+0.178, CI90 [0.005,0.38], al filo del
  cero). `tier=A+` da su primer giro a E[R] positivo (+0.02, n=218) tras
  tres lecturas cerca de -0.11, aunque con WR todavía muy bajo (23.4%).
  Mejora permanente en `analyze.py`: `session_analyst_cross` ahora calcula
  `by_verdict_ci90` (bootstrap 90% CI de E[R] por veredicto GO/WAIT/AVOID)
  y `by_kind_side` (mismo cruce desglosado por kind/side) — con esto la
  hipótesis "AVOID rinde peor" de `agent-instructions.md` queda
  **refutada con confianza estadística por primera vez**: AVOID rinde
  MEJOR (E[R]=+0.183, CI90 [0.08,0.285], n=350, no cruza cero) y GO rinde
  PEOR (E[R]=-0.273, CI90 [-0.423,-0.118], n=121, no cruza cero); nuevo
  chequeo en `material_alerts` de `analyze.py` para que esto salga en
  `report.alerts` cuando el CI no cruce cero. Nota de proceso: `git pull`
  volvió a mostrar "forced update" (rama local vieja / clon superficial);
  se verificó `origin/main` y se hizo `git reset --hard` sin pérdida de
  trabajo, mismo patrón que 2026-09-02/09-04.
- 2026-09-09 (miércoles): **día de confirmación, no de dato nuevo** — no
  llegó ningún archivo `signals/outcomes` fechado 2026-09-09; solo
  terminaron de resolverse pendientes de 2026-09-08 (+39 pares en este
  playbook). Cero SL nuevos en los tres TF (873/1m, 433/2m, 127/5m
  idénticos a ayer) — todos los pares nuevos cerraron en TP o TIMEOUT. Casi
  todas las métricas (E[R], PF, `segment_significance`, `sl_origin_vs_layer`,
  `session_analyst_cross`, `cross_instrument`) coinciden a 2-3 decimales
  con la corrida de 2026-09-08, lo que sirve como confirmación de
  estabilidad de las lecturas de ayer más que como información nueva.
  Curiosidad de método: la n usada por `segment_significance` no creció
  con los 39 pares nuevos (se mantuvo en 1720/846/285 para 1m/2m/5m) —
  puede ser un rezago de una corrida antes de que el bootstrap incorpore
  pares muy recientes; vigilar si esto se sostiene, no se trata como bug
  todavía porque no hay evidencia de pérdida de datos
  (`file_integrity_check` limpio).
