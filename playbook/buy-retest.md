# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-07 · n: 2366)

### Nota de proceso — primer día limpio, sin repetición del bug de "heal"
`file_integrity_check` (guardado permanente en `analyze.py` desde
2026-09-06) confirma que ningún `signals/outcomes/*.jsonl` encogió hoy —
todos los archivos crecieron o se mantuvieron respecto al máximo visto en
corridas previas. Llegó dato genuinamente nuevo: `signals/2026-09-06.jsonl`
(69) y `signals/2026-09-07.jsonl` (38) no estaban contados en la corrida
anterior (lunes, día festivo en EE.UU. — Globex operó con volumen reducido).
Ver `experiments.json` para el detalle de por qué esto importa: es la
primera confirmación independiente real (no solo dato restaurado) del
hallazgo de SL estructural en 1m LONG.

### Veredicto global
Con el dato completo (1m n=1412, 2m n=708, 5m n=246): 1m WR 43.0%
E[R]=-0.015 PF=0.97 (717 SL de 1412, casi breakeven, mejoró un poco vs
-0.025 de ayer con dato nuevo real); 2m WR 45.5% **E[R]=-0.072** PF=0.86
(364 SL de 708) sigue siendo el peor TF con muestra grande, prácticamente
sin cambio (-0.073→-0.072); 5m WR 52.8% E[R]=+0.086 PF=1.19 (104 SL de
246) sigue siendo el mejor, bajó un poco desde +0.098 pero en la misma
dirección. `segment_significance`: 1m CI90=[-0.073,0.044] p=0.672 (plano,
igual lectura); **2m CI90=[-0.139,-0.002] p_mean_le_0=0.956 — el CI ya no
roza cero, queda del lado negativo, sigue siendo la evidencia más sólida
de este playbook de que 2m/RETEST/LONG pierde dinero en promedio, y con
dato genuinamente nuevo hoy (no solo restaurado)** (`survives_fdr10=false`
porque esa bandera solo certifica edge *positivo*, no basta con
"significativo" a secas); 5m CI90=[-0.034,0.218] p=0.128, se alejó un poco
del borde de certificar (era p=0.102). Veredicto sin cambios: **1m sin
señal, 2m EVITAR con confianza estadística estable, 5m vigilar-no-confirmado.**

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna certifica con `survives_fdr10` (esa prueba corre por tf/kind/side,
no por estos cortes):

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tier=A+` | sigue siendo el peor tier por E[R], algo menos malo | 159 | WR 19.5%, E[R]=-0.11, PF=0.84 (103 SL de 159) | baja-moderada — prácticamente sin cambio vs ayer (-0.104→-0.11), n casi idéntico (158→159, apenas 1 señal nueva), no tratar como asentado |
| 2 | `tier=B` | TOMAR, prioridad sobre A+ | 872 vs 1335 tier C | WR 43.3% E[R]=0.011 PF=1.02 vs tier C WR 48.7% E[R]=-0.034 PF=0.93 | alta — n=872, B es la única rama de tier con E[R] positivo hoy en LONG |
| 3 | símbolo (`cross_instrument`), 1m | sigue `universal` — ya no hay excepción limpia por símbolo | GC n=225 E[R]=0.089, NQ n=256 E[R]=0.005, YM n=289 E[R]=0.034, ES n=333 E[R]=-0.058, CL **n=309 E[R]=-0.108** (spread 0.197, `universal`) | moderada — CL sigue siendo el peor símbolo en 1m pero mejoró (-0.201→-0.108 con dato nuevo), spread se redujo (0.29→0.197), confirma que no es un patrón sólido de símbolo |
| 3b | símbolo (`cross_instrument`), 2m | sigue sin poder filtrarse por símbolo (`universal`) | NQ n=129 -0.028, GC n=106 -0.012, ES n=155 -0.03, CL n=164 -0.061, YM **n=154 -0.206** (spread 0.194, `universal`) | alta — todos los símbolos negativos o planos, confirma la regla `tf=2m EVITAR` más que cualquier corte por símbolo |
| 4 | `nearEdge` | sin gradiente limpio, edge=-1 el menos malo | -1: n=143 E[R]=0.12; edge=0: n=1171 E[R]=-0.031; edge=1: n=1052 E[R]=-0.031 | baja-moderada — `edge=-1` se despega hoy como la única rama positiva (n=143), a vigilar si se sostiene 1-2 revisiones más antes de tratarlo como regla |
| 5 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1` | 11 vs 2355 | E[R] +0.459 vs -0.024, WR 54.5% vs 44.7%, PF 4.21 vs 0.95 | baja — sigue exactamente en n=11 (van 4 revisiones sin una sola señal nueva `aligned=0` en LONG, ni siquiera con el dato nuevo de hoy), anomalía de signo sin poder cuantificarse mejor |

**Tier A+ se estabiliza cerca de -0.11 por segunda revisión seguida.** Historial: n=13
E[R]=-0.705 (2026-09-03, "catastrófico") → n=97 E[R]=-0.021 (2026-09-04,
"ya no es el peor tier") → n=158 E[R]=-0.104 (2026-09-06) → n=159
E[R]=-0.11 (hoy). Primera vez que dos lecturas consecutivas coinciden de
cerca — sigue siendo el peor tier, con WR muy bajo (19.5%) y ganadores
grandes ocasionales que hacen su E[R] ruidoso. Esperar a n≥300 antes de
fijar una regla dura sobre A+.

**Símbolo en 1m se asienta como `universal`.** El spread entre símbolos
en 1m bajó de 0.29 a 0.197 con dato nuevo — CL sigue siendo el peor
símbolo pero cada vez más lejos del umbral de 0.4 que marca
`instrument-specific`. No usar "CL malo en 1m" como regla dura; sí sigue
sosteniéndose en 2m como corte `universal` de "todos mal", que es un
hallazgo distinto (régimen/TF, no símbolo).

**Anomalía a vigilar** (no accionar): el modelo P(TP1) in-sample sigue
ponderando `aligned` con signo negativo (-0.064 hoy) — alineado con el
sesgo/estructura predice *peor* resultado. La rama `aligned=0` de LONG
sigue exactamente en n=11 desde hace 4 revisiones, incluso con el dato
genuinamente nuevo de hoy. Sigue pendiente pedir a Jesús que confirme la
definición exacta de `aligned` en Pine.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara de calidad
  de entrada en este segmento.

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=1374 delta=**+0.061**
  (naive -0.017→managed 0.044, ayuda, casi sin cambio vs ayer +0.068); 2m
  n=690 delta=**+0.083** (naive -0.075→managed 0.008, rescata casi toda la
  pérdida cruda sin volverla positiva, idéntico a ayer); 5m n=235
  delta=**-0.127** (naive 0.086→managed -0.041, sigue siendo el único TF
  donde la gestión resta en LONG, tercera lectura consecutiva confirmando
  el patrón). Regla sin cambios: gestionar con escalera en 1m/2m, ir al
  mercado simple en 5m LONG.
- **SL estructural (`sl_origin_vs_layer`)**: 1m LONG sigue certificando
  positivo, n=1135 delta=**+0.183** CI90=**[0.057,0.324] no cruza cero** —
  **n subió de 1087 a 1135 (+48) con dato genuinamente nuevo, no
  restaurado** (primer día hábil desde la restauración sin repetición del
  bug de heal). Esta es la primera confirmación independiente real que se
  esperaba: el delta se mantiene prácticamente igual (0.181→0.183) con
  trades que no estaban en la muestra anterior. 2m n=596 delta=+0.028
  (CI90 [-0.069,0.136], sigue sin significar); 5m n=224 delta=+0.117
  (CI90 [-0.086,0.36], sigue sin significar). Registrado en
  `experiments.json` (`sl-retest-wick-2026-09-03`) con segmento ampliado a
  todo RETEST (ya no solo SHORT). Sigue sin aplicarse — es medición
  paralela; falta walk-forward (solo 2 semanas de datos) antes de tratarlo
  como asentado.
- Objetivo / Parcial 1 / trailing: _pendiente_ — el contrafactual global
  (`counterfactual`, n=9) no está cortado por side todavía.
- `revAfterSL_rate` por corte: `edge=-1` 47.5%, `edge=0` 41.7%, `edge=1`
  22.7% — mismo orden que ayer (edge=-1 revierte más tras el SL).

### Contextos a evitar
- **`tf=2m` completo**: CI90 de E[R] queda del lado negativo sin cruzar
  cero ([-0.139,-0.002]), n=693 en `segment_significance` — sigue siendo
  el hallazgo más sólido y ESTABLE de este playbook, ahora con dato
  genuinamente nuevo (no solo restaurado), más que cualquier corte por
  tier o símbolo.
- Ya no generalizar "símbolo malo" en 1m (regla #3, `universal`) — sí
  sigue aplicando en 2m como corte de régimen, no de símbolo (regla #3b).
- Autopsia de SL sobre las 1185 pérdidas LONG (desglose por kind/side
  permanente en `analyze.py`): `RR-bajo` 481/1185 (40.6%) sigue siendo la
  causa **dominante**, ahora seguida de cerca por `killzone-Asia-largo`
  460/1185 (38.8%) y `contra-estructura` 447/1185 (37.7%) — mismo reparto
  de siempre (los tres casi empatados), `RR-bajo` sigue siendo el
  candidato principal para `sc_min_rr`/`sc_aplus_rr` en la revisión semanal.

### Decaimiento
`decay_weekly` ya muestra 2 semanas: 2026-W36 (n=3231, WR 44.6%,
E[R]=-0.021) y 2026-W37 (n=26, WR 50.0%, E[R]=-0.193) — W37 todavía tiene
muestra minúscula (arrancó ayer), no comparar todavía semana contra
semana con esa n.

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
