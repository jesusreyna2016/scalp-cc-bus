# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-12 · n: 4314)

### Nota de proceso
Sin incidentes de repo hoy — `git pull` limpio, sin "forced update" ni
reescritura de historia. n 4128→4314 (**+186**; 1m+107, 2m+56, 5m+23).

### Veredicto global
1m n=2658 (+107) WR 44.5% E[R]=**0.026** PF=1.05 (subió de +0.005); 2m
n=1254 (+56) WR 47.0% E[R]=**-0.008** PF=0.98 (subió de -0.032, casi
breakeven); 5m n=402 (+23) WR 53.5% E[R]=**0.104** PF=1.23 (subió de
+0.09, sigue el mejor TF crudo). `segment_significance`: 1m
CI90=[-0.015,0.068] p=0.155 n=2615 (mejoró bastante desde
[-0.035,0.047], se acerca a certificar pero sigue cruzando cero); 2m
CI90=[-0.064,0.046] p=0.598 n=1237 (mejoró un poco desde [-0.088,0.021],
sigue sin certificar, prácticamente plano); **5m CI90=[0.006,0.202]
p=0.038 n=392 — el intervalo YA NO CRUZA CERO por primera vez** (venía de
[-0.007,0.191]), aunque `survives_fdr10` sigue en `false` (la corrección
FDR es más estricta que el CI90 crudo) — el TF más prometedor del
segmento sigue siendo 5m, ahora con una lectura cruda más sólida que
nunca. Veredicto: **1m mejorando pero sin señal dura, 2m vuelve a casi
breakeven, 5m sigue siendo el mejor TF y hoy da su primer CI90 positivo
en crudo — vigilar si se sostiene.**

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna certifica con `survives_fdr10`:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tier=A+` | **salto grande a positivo**, pasa a ser la mejor rama de tier | 330 (+29) | WR 26.7%, E[R]=**0.132** (venía de +0.002), PF=1.2 | baja — quinta lectura distinta en 5 días para esta rama (venía de vaivenes desde -0.705 hasta +0.055); ya está por encima del umbral n≥300 que el propio playbook fijó, pero el patrón sigue siendo demasiado inestable para fijarla como regla — esperar una segunda lectura en la misma dirección |
| 2 | `tier=B` | TOMAR, prioridad sobre A+ y C | 1766 (+73) vs 2218 (+84) tier C | WR 45.8% E[R]=0.061 PF=1.12 vs tier C WR 49.2% E[R]=-0.022 PF=0.95 | alta — sexto día seguido con B como la única rama de tier con E[R] positivo estable en LONG (C mejoró pero sigue negativo) |
| 3 | símbolo (`cross_instrument`), 1m | sigue `universal` | GC n=481 E[R]=0.108, NQ n=561 E[R]=-0.054, YM n=315 E[R]=0.101, ES n=477 E[R]=-0.01, CL n=824 (+104, único símbolo con dato nuevo) E[R]=0.027 (antes -0.052, se da vuelta a positivo) (spread 0.162) | moderada — spread bajó un poco (0.167→0.162), sigue lejos de `instrument-specific` |
| 4 | símbolo (`cross_instrument`), **5m** | **cambia de `universal` a `instrument-specific`** | spread 0.406 (antes 0.329) — YM n=63 E[R]=-0.016 (se da vuelta a negativo, antes +0.035), NQ n=126 E[R]=-0.097 (empeora), CL n=127 E[R]=0.309 (mejora) | baja — primera vez que este corte deja de ser `universal` en 5m LONG, pero con n por símbolo todavía chico (63-127); no generalizar todavía |
| 5 | `nearEdge` | sin gradiente limpio, pero mejora en general | edge=-1 n=212 (sin cambio, cero señales nuevas) E[R]=0.043; edge=0 n=1953 E[R]=-0.016 (mejoró de -0.038, sigue negativo); edge=1 n=2149 E[R]=0.058 (mejoró de 0.034, sigue la mejor rama) | baja — sin cambio de forma, `edge=1` sigue siendo consistentemente la mejor |
| 6 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1`, pero **la muestra sigue congelada en n=10** | 10 (sin cambio, segundo día seguido sin señales nuevas) vs 4304 | E[R] +0.433 vs +0.023, WR 50.0% vs 46.1%, PF 3.6 vs 1.05 | baja — n=10 sigue siendo demasiado chico para usar; `aligned=1` mejoró bastante (E[R] 0.001→0.023) |

**Símbolo en 1m sigue `universal`.** Spread bajó un poco (0.167→0.162).
No usar "símbolo malo" como regla dura en 1m LONG. En **5m sí cambió de
forma** hoy (ver regla #4) — vigilar sin generalizar todavía, la muestra
por símbolo es chica.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara de calidad
  de entrada en este segmento.

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=2611 delta=**+0.078**
  (bajó un poco de +0.088, sigue sólido); 2m n=1235 delta=**+0.078**
  (bajó un poco de +0.083, estable); 5m n=392 delta=**-0.047** (mejoró de
  -0.064, sigue siendo el único TF donde la gestión resta en LONG, pero
  el hueco se achica). Regla sin cambios: gestionar con escalera en
  1m/2m, ir al mercado simple en 5m LONG.
- **SL estructural (`sl_origin_vs_layer`)**: 1m LONG sigue certificando
  positivo, n=2231 (+96) delta=**+0.152** CI90=[0.069,0.238] (no cruza
  cero, bajó un poco de +0.163) — quinta confirmación independiente,
  sigue siendo la lectura más estable del experimento. **5m LONG
  certifica por SEGUNDA lectura seguida** (09-11 y hoy): n=378 (+23)
  delta=**+0.187** CI90=**[0.028,0.363]** (mejoró desde [0.007,0.314]) —
  primera vez que cumple la barra de "2 lecturas seguidas del mismo lado"
  que el propio experimento se puso tras tres vaivenes; pasa a candidato
  **experimental** para la revisión semanal de mañana, con la salvedad
  explícita de su historial volátil. 2m sigue sin certificar, n=1116
  (+53) delta=+0.019 CI90=[-0.057,0.104] — sexta lectura seguida sin
  certificar, sigue fuera de cualquier propuesta. Detalle completo en
  `experiments.json` (`sl-retest-wick-2026-09-03`). Sigue sin aplicarse —
  falta walk-forward (solo 2 semanas de datos).
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- **`tf=2m`**: E[R] casi en breakeven (-0.008), CI90 sigue cruzando cero
  ([-0.064,0.046], n=1237) — ya no se ve claramente negativo, pero
  tampoco hay señal positiva; se degrada de "negativo, vigilar" a
  "neutro, sin edge claro".
- Autopsia de SL sobre las 2105 pérdidas LONG (+77 vs ayer): el
  casi-empate de tres causas se sostiene y **`RR-bajo` retoma el primer
  lugar** (816/2105, 38.8%) por delante de `killzone-Asia-largo`
  (805/2105, 38.2%) y `contra-estructura` (786/2105, 37.3%) — tercer
  cambio de orden en 3 días, rango de apenas 1.5pp entre las tres, sigue
  siendo un empate de fondo. El SL estructural (arriba) sigue siendo el
  candidato que mejor ataca `RR-bajo` de las tres.

### Cruce con Session Analyst
Bajo veredicto SA `WAIT` el E[R] se mantiene como la mejor rama:
**+0.191** (n=780, +22 vs ayer, bajó un poco de +0.202 pero sigue
claramente primero), por delante de `AVOID` **+0.069** (n=429, sin
cambio — cero señales nuevas cruzadas hoy) y de `GO` **-0.066** (n=184,
sin cambio, sigue siendo la peor rama). El orden "WAIT mejor, GO peor"
que apareció ayer **se sostiene por segundo día seguido** — primera vez
que esta relación no cambia de dirección de una corrida a otra. A nivel
global (`session_analyst_cross.by_verdict_ci90`, todo kind/side) esto
ahora tiene respaldo estadístico: WAIT E[R]=0.081 CI90=[0.029,0.133]
(no cruza cero, n=1490) y AVOID rinde peor que GO+WAIT juntos
(E[R]=0.012 vs 0.072, CI90 de la diferencia [0.026,0.122] no cruza
cero) — la lectura más creíble hasta ahora a favor de la hipótesis
original de `agent-instructions.md`, aunque con solo 2 días sosteniéndose
sigue sin ser un filtro para usar en vivo.

### Decaimiento
`decay_weekly` (global, no por segmento): 2026-W36 n=3179 WR 44.7%
E[R]=-0.018 (bajó de n=3183 — **tercera corrida seguida en que esta
semana ya cerrada pierde muestra**: 3231→3183→3179, aunque la caída se
desacelera fuerte, 48 y luego 4; `file_integrity_check` sigue sin
alertar ningún archivo encogido, así que sigue leyéndose como
re-pareo/deduplicación del agregado, no pérdida real de datos — vigilar
que se estabilice); 2026-W37 n=4573 WR 47.4% E[R]=**0.084** (subió de
n=3856, sigue positivo y mejoró bastante de +0.042). Sin señal de
decaimiento (no hay caída de WR > 15 pts).

## Histórico de cambios
- 2026-09-12 (sábado, última corrida antes de la revisión semanal de
  mañana): n 4128→4314 (+186; 1m+107, 2m+56, 5m+23), sin incidentes de
  repo. Hallazgos del día: `tier=A+` da un salto grande a positivo
  (E[R] 0.002→0.132, quinta lectura distinta en 5 días, todavía no fijar
  como regla); `cross_instrument` en 5m cambia de `universal` a
  `instrument-specific` por primera vez; `segment_significance` en 5m
  tiene su primer CI90 que no cruza cero en crudo ([0.006,0.202]), aunque
  `survives_fdr10` sigue en falso. El hallazgo más importante:
  `sl_origin_vs_layer` en **5m LONG certifica por segunda lectura
  seguida** (delta 0.154→0.187), cumpliendo por primera vez la barra de
  estabilidad que el propio experimento se puso — pasa a candidato
  experimental para la revisión semanal de mañana domingo 2026-09-13
  (junto a 1m LONG/SHORT y 5m SHORT, ver `experiments.json`). El cruce
  con Session Analyst (WAIT mejor, GO peor) se sostiene por segundo día
  seguido y ahora tiene respaldo estadístico a nivel global — primera vez
  que esta relación no se revierte de una corrida a otra. La semana ya
  cerrada 2026-W36 volvió a perder muestra (3183→3179) pero la caída se
  desacelera fuerte frente a la de ayer (-48 → -4).
- 2026-09-11 (viernes): n 3394→4128 (+734; 1m+486, 2m+210, 5m+38).
  **Incidente de repo**: `origin/main` fue reescrito río arriba (historia
  sin ancestro común con la local) — verificado como superset sin pérdida
  de datos, resuelto con `git reset --hard origin/main` (ver Nota de
  proceso arriba). `tier=A+` corta su racha de 3 días subiendo (E[R]
  +0.055→+0.002 con n 252→301, cruzando el umbral n≥300 sin confirmar la
  mejora). `sl_origin_vs_layer` en 5m LONG recupera la certificación que
  había perdido ayer (tercer vaivén en 3 días, tratar como inestable). El
  cruce con Session Analyst se invierte: ahora SA=WAIT rinde mejor
  (E[R]+0.202, antes +0.045) y SA=AVOID deja de ser la mejor rama
  (+0.069, antes +0.193) — tercer cambio de dirección de este cruce en 4
  días, ver `report.alerts`. Dos anomalías de conteo menores (`aligned=0`
  bajó de n=11 a n=10; la semana ya cerrada 2026-W36 perdió muestra de
  n=3231 a n=3183) probablemente ligadas al reset de historia, sin
  evidencia de pérdida real de datos (`file_integrity_check` limpio).
- 2026-09-11 (viernes): n 3394→4128 (+734; 1m+486, 2m+210, 5m+38).
  **Incidente de repo**: `origin/main` fue reescrito río arriba (historia
  sin ancestro común con la local) — verificado como superset sin pérdida
  de datos, resuelto con `git reset --hard origin/main` (ver Nota de
  proceso arriba). `tier=A+` corta su racha de 3 días subiendo (E[R]
  +0.055→+0.002 con n 252→301, cruzando el umbral n≥300 sin confirmar la
  mejora). `sl_origin_vs_layer` en 5m LONG recupera la certificación que
  había perdido ayer (tercer vaivén en 3 días, tratar como inestable). El
  cruce con Session Analyst se invierte: ahora SA=WAIT rinde mejor
  (E[R]+0.202, antes +0.045) y SA=AVOID deja de ser la mejor rama
  (+0.069, antes +0.193) — tercer cambio de dirección de este cruce en 4
  días, ver `report.alerts`. Dos anomalías de conteo menores (`aligned=0`
  bajó de n=11 a n=10; la semana ya cerrada 2026-W36 perdió muestra de
  n=3231 a n=3183) probablemente ligadas al reset de historia, sin
  evidencia de pérdida real de datos (`file_integrity_check` limpio).
- 2026-09-10 (jueves): salto grande de dato nuevo (+444, n 2950→3394) —
  el bus terminó de asentar `signals/outcomes/2026-09-08.jsonl`. **5m LONG
  pierde la certificación de `sl_origin_vs_layer` que había ganado "al
  filo" ayer** (CI90 volvió a cruzar cero) — se cumplió la advertencia de
  tratarlo como débil. 1m LONG sostiene su tercera confirmación
  independiente (delta+0.178, estable). La autopsia de SL cambia de una
  causa dominante clara (`RR-bajo`) a un empate de tres causas
  (`contra-estructura`/`killzone-Asia-largo`/`RR-bajo`, dentro de 0.7pp).
  `tier=A+` sube a E[R]=+0.055 (n=252) por tercer día positivo seguido,
  acercándose al umbral n≥300 fijado para tratarlo como regla. El cruce
  con Session Analyst (AVOID mejor que GO) se sostiene con más muestra en
  este segmento (ver `sell-retest.md` para el hallazgo agregado, que se
  fortaleció y ahora se reporta en `report.alerts`). `2026-W37` pasó a
  E[R] positivo (+0.069) con casi el doble de muestra que ayer.
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
