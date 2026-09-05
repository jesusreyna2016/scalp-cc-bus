# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-05 · n: 2276)

### ⚠ Nota de proceso — data restaurada hoy
La corrida de hoy encontró que el commit `92917b8` ("heal 24 orphan
signal(s) 2026-09-03") en realidad **borró 1256 de las 1280 señales**
de `signals/2026-09-03.jsonl` (diff real: 1256 líneas eliminadas, 0
añadidas) en vez de repararlas — probablemente un bug del healer del
pipeline Netlify/Pine, no de este repo. Se restauró el archivo completo
desde el commit anterior (`f239309`, verificado línea por línea: las 24
que quedaban eran subconjunto exacto de las 1280 originales, cero
pérdida). Todas las cifras de esta revisión usan el dato restaurado
(n total del dataset pasó de 1884 a 3140 pares). **Los números de ayer
(2026-09-04, n=1641) estaban calculados sobre datos ya truncados** —
tratar el salto de hoy como corrección de un agujero, no como señales
nuevas genuinas de un solo día.

### Veredicto global
Con el dato completo (1m n=1355, 2m n=687, 5m n=234): 1m WR 43.0%
E[R]=-0.025 PF=0.95 (695 SL de 1355, casi breakeven, igual que ayer); 2m
WR 45.4% **E[R]=-0.073** PF=0.86 (354 SL de 687) sigue siendo el peor TF
con muestra grande, algo menos negativo que ayer (-0.13) pero en la misma
dirección; 5m WR 53.0% E[R]=+0.098 PF=1.22 (99 SL de 234) sigue siendo el
mejor, aunque bajó desde +0.169. `segment_significance`: 1m
CI90=[-0.082,0.034] p=0.773 (plano, igual lectura que ayer); **2m
CI90=[-0.142,0.0] p_mean_le_0=0.95 — roza cero por el lado de arriba,
sigue siendo la evidencia más sólida de este playbook de que 2m/RETEST/LONG
pierde dinero en promedio, y se mantiene estable tras restaurar el dato
(antes y después del arreglo da la misma dirección)**
(`survives_fdr10=false` porque esa bandera solo certifica edge *positivo*,
no basta con "significativo" a secas); 5m CI90=[-0.029,0.237] p=0.102, ya
no es el más cercano a certificar de todo BUY RETEST (ese honor hoy es de
la propuesta de SL de `sl_origin_vs_layer`, ver Gestión). Veredicto: **1m
sin señal, 2m EVITAR con confianza estadística estable, 5m vigilar-no-confirmado.**

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna certifica con `survives_fdr10` (esa prueba corre por tf/kind/side,
no por estos cortes):

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tier=A+` | vuelve a ser el peor tier por E[R] — ver nota de volatilidad abajo | 158 | WR 19.6%, E[R]=-0.104, PF=0.85 (102 SL de 158) | baja-moderada — se movió otra vez (-0.021 ayer → -0.104 hoy), sigue siendo n chico relativo al resto, no tratar como asentado |
| 2 | `tier=B` | TOMAR, prioridad sobre A+ | 844 vs 1274 tier C | WR 43.0% E[R]=-0.009 PF=0.98 vs tier C WR 49.1% E[R]=-0.03 PF=0.94 | alta — n=844, B sigue siendo la rama de tier menos mala en LONG (aunque hoy ninguna es positiva) |
| 3 | símbolo (`cross_instrument`), 1m | **verdict pasó a `universal`** — ya no hay excepción limpia por símbolo | GC n=? E[R]=0.089, NQ E[R]=0.024, YM E[R]=0.034, ES E[R]=-0.031, CL **E[R]=-0.201** (spread 0.29, `universal`) | moderada — CL sigue siendo el peor símbolo en 1m, pero el spread ya no basta para `instrument-specific` (era 0.462 ayer) |
| 3b | símbolo (`cross_instrument`), 2m | sigue sin poder filtrarse por símbolo (`universal`) | NQ -0.021, GC -0.012, ES -0.021, CL -0.075, YM **-0.206** (spread 0.194, `universal`) | alta — todos los símbolos negativos o planos, confirma la regla `tf=2m EVITAR` más que cualquier corte por símbolo |
| 4 | `nearEdge` | sin gradiente limpio, edge=-1 el menos malo | -1: n=133 E[R]=-0.004; edge=0: n=1113 E[R]=-0.028; edge=1: n=1030 E[R]=-0.028 | baja — los tres cortes casi empatados por E[R] hoy, no hay rama claramente mejor |
| 5 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1` | 11 vs 2265 | E[R] +0.459 vs -0.029, WR 54.5% vs 44.7%, PF 4.21 vs 0.95 | baja — sigue exactamente en n=11 (van 3 revisiones sin una sola señal nueva `aligned=0` en LONG), anomalía de signo sin poder cuantificarse mejor |

**Tier A+ vuelve a empeorar — no tratar como asentado.** Historial: n=13
E[R]=-0.705 (2026-09-03, "catastrófico") → n=97 E[R]=-0.021 (2026-09-04,
"ya no es el peor tier") → n=158 E[R]=-0.104 (hoy, otra vez el peor tier
por E[R]). El WR se mantiene bajo y estable (7.7%→18.6%→19.6%), pero el
E[R] ha oscilado en las 3 lecturas — la señal más consistente es que
`tier=A+` en BUY RETEST tiene WR muy bajo con ganadores grandes
ocasionales, lo que hace su E[R] ruidoso incluso con n=158. Esperar a
n≥300 antes de fijar una regla dura sobre A+.

**Símbolo en 1m pasa de `instrument-specific` a `universal`.** Con el
dato restaurado, CL sigue siendo el peor símbolo en 1m pero el spread
entre símbolos (0.29) ya no cruza el umbral de 0.4 que usa `analyze.py`
para marcar `instrument-specific` — la diferencia por símbolo se diluyó
al recuperar la muestra completa. No usar "CL malo en 1m" como regla dura
todavía; sí sigue sosteniéndose en 2m como corte `universal` de "todos
mal", que es un hallazgo distinto (régimen/TF, no símbolo).

**Anomalía a vigilar** (no accionar): el modelo P(TP1) in-sample sigue
ponderando `aligned` con signo negativo (-0.066 hoy) — alineado con el
sesgo/estructura predice *peor* resultado. La rama `aligned=0` de LONG
sigue exactamente en n=11 desde hace 3 revisiones. Sigue pendiente pedir
a Jesús que confirme la definición exacta de `aligned` en Pine.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara de calidad
  de entrada en este segmento.

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=1321 delta=**+0.068**
  (naive -0.026→managed 0.042, ayuda); 2m n=669 delta=**+0.083** (naive
  -0.076→managed 0.007, rescata casi toda la pérdida cruda sin volverla
  positiva); 5m n=224 delta=**-0.118** (naive 0.098→managed -0.02, sigue
  siendo el único TF donde la gestión resta en LONG, consistente con las
  2 revisiones previas — esto ya es un patrón estable, no ruido). Regla:
  gestionar con escalera en 1m/2m, ir al mercado simple en 5m LONG.
- **SL estructural (`sl_origin_vs_layer`) — CAMBIO IMPORTANTE HOY: 1m LONG
  pasa a certificar positivo**, algo que las 2 revisiones previas
  descartaban explícitamente ("no aplica a largos"). 1m n=1087
  delta=**+0.181** CI90=**[0.061,0.314] no cruza cero** (antes: n=802
  delta=+0.143 CI90 rozando cero, y n=171 delta=-0.128 negativo el día
  anterior a ese); 2m n=577 delta=+0.018 (CI90 [-0.078,0.124], sigue sin
  significar); 5m n=214 delta=+0.124 (CI90 [-0.093,0.37], sigue sin
  significar). **No confiar todavía en el giro de 1m**: coincide con el
  mismo día en que se restauró `signals/2026-09-03.jsonl` (ver nota de
  arriba), así que antes de tratarlo como hallazgo real hace falta
  confirmarlo el 2026-09-06 con datos que no dependan de la restauración.
  Registrado en `experiments.json` (`sl-retest-wick-2026-09-03`) con
  segmento ampliado a todo RETEST (ya no solo SHORT). Sigue sin aplicarse
  — es medición paralela.
- Objetivo / Parcial 1 / trailing: _pendiente_ — el contrafactual global
  (`counterfactual`, n=9) no está cortado por side todavía.
- `revAfterSL_rate` por corte: `edge=-1` 47.5%, `edge=0` 41.2%, `edge=1`
  22.8% — mismo orden que ayer (edge=-1 revierte más tras el SL).

### Contextos a evitar
- **`tf=2m` completo**: CI90 de E[R] roza cero por arriba
  ([-0.142, 0.0]), n=672 en `segment_significance` — sigue siendo el
  hallazgo más sólido y ESTABLE de este playbook (misma dirección antes y
  después de restaurar el dato de hoy), más que cualquier corte por tier
  o símbolo.
- Ya no generalizar "símbolo malo" en 1m (regla #3, pasó a `universal`) —
  sí sigue aplicando en 2m como corte de régimen, no de símbolo (regla #3b).
- Autopsia de SL sobre las 1148 pérdidas LONG (desglose por kind/side
  permanente en `analyze.py`): `RR-bajo` 467/1148 (40.7%) sigue siendo la
  causa **dominante**, casi empatada con `contra-estructura` 434/1148
  (37.8%) y `killzone-Asia-largo` 427/1148 (37.2%) — mismo reparto que
  ayer, sigue siendo el candidato principal para `sc_min_rr`/`sc_aplus_rr`
  en la revisión semanal.

### Decaimiento
Con solo 2026-W36 disponible (`decay_weekly` reporta una sola semana,
n=3140 en todo el dataset tras la restauración), sigue sin haber
comparación semana-contra-semana real.

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
