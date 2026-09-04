# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-04 · n: 1641)

### Veredicto global
**Salto de muestra ~5x (325→1641: 993×1m, 491×2m, 157×5m) y la anomalía
más citada de este playbook — `tier=A+` "catastrófico" — se corrige igual
que ya le pasó a SELL RETEST: era ruido de n chico, no un patrón real.**
Crudo: 1m WR 43.2% E[R]=-0.004 PF=0.99 (502 SL de 993, casi breakeven); 2m
WR 42.8% **E[R]=-0.13** PF=0.76 (264 SL de 491, el peor TF con muestra
grande); 5m WR 54.8% E[R]=+0.169 PF=1.4 (64 SL de 157) sigue siendo el
mejor. `segment_significance`: 1m CI90=[-0.075,0.071] p=0.531 (plano de
verdad); **2m CI90=[-0.208,-0.049] no cruza cero, p_mean_le_0=0.998 — esto
NO es "sin señal": es evidencia estadística sólida de que 2m/RETEST/LONG
pierde dinero en promedio** (`survives_fdr10=false` porque esa bandera solo
certifica edge *positivo*, no basta con "significativo" a secas — no leer
`false` como "ruido"); 5m CI90=[0.007,0.348] p=0.042, sigue sin certificar
por FDR pero es el más cercano de todo BUY RETEST. Veredicto: **1m sin
señal, 2m EVITAR con confianza estadística, 5m vigilar-no-confirmado.**

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna certifica con `survives_fdr10` (esa prueba corre por tf/kind/side,
no por estos cortes):

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tier=A+` | ya NO es "no tomar" — ver corrección abajo | 97 | WR 18.6%, E[R]=-0.021, PF=0.97 (57 SL de 97) | moderada — moderó de catastrófico a "peor tier por poco"; C es hoy el peor por E[R] |
| 2 | `tier=B` | TOMAR, prioridad | 635 / (909 tier C) | WR 43.0% E[R]=+0.022 PF=1.04 vs tier C WR 47.7% E[R]=-0.059 PF=0.88 | alta — n=635, B es la única rama de tier con E[R] positivo en LONG |
| 3 | símbolo (`cross_instrument`), 1m | CL rinde mal, resto mixto | GC n=181 E[R]=0.23, NQ n=123 E[R]=0.054, ES n=209 E[R]=-0.039, CL n=253 **E[R]=-0.232**, YM n=227 E[R]=0.067 (spread 0.462, `instrument-specific`) | moderada — CL sigue siendo el peor símbolo en 1m con n grande; YM ya no destaca tanto como antes (ver nota de dilución abajo) |
| 3b | símbolo (`cross_instrument`), 2m | **ya NO se puede filtrar por símbolo — verdict cambió a `universal`** | NQ n=73 -0.199, GC n=90 +0.04, CL n=109 -0.218, ES n=98 -0.048, YM n=121 **-0.201** (spread 0.258, `universal`) | alta como corrección — ver nota abajo, YM se volvió negativo en 2m |
| 4 | `nearEdge=1` | mejor que `edge=0`, similar a `edge=-1` | 759 / 785 / 97 | WR 41.0%/47.1%/45.4%; E[R] +0.016/-0.069/+0.007; PF 1.03/0.87/1.01 | moderada — ya no es un gradiente limpio como en SELL RETEST: `edge=0` es ahora la peor rama por E[R], no `edge=-1` |
| 5 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1` | 11 vs 1630 | E[R] +0.459 vs -0.027, WR 54.5% vs 44.1%, PF 4.21 vs 0.95 | baja — sigue en n=11, sin crecer desde la revisión anterior; anomalía de signo sin poder cuantificarse mejor |

**Corrección de la anomalía anterior — `tier=A+` en BUY RETEST.** La
revisión de ayer reportó A+ como el peor resultado del dataset (n=13, WR
7.7%, E[R]=-0.705, PF=0.24) y la marcó como el patrón sistemático que ya no
era "solo ruido de n chico". Con n=97 (×7.5) el resultado se normalizó
igual que ya le había pasado a SELL RETEST con su propio A+ (ver historial
en `sell-retest.md`): WR sube a 18.6%, E[R] a -0.021, PF a 0.97 — todavía
el peor WR del dataset, pero por E[R] hoy **`tier=C` es peor que A+**
(-0.059 vs -0.021). Lectura correcta: la lectura de ayer era mayormente
ruido de n=13, exactamente el tipo de conclusión prematura que este
playbook ya había señalado como riesgo con SELL RETEST. Se retira "NO
tomar A+" como regla dura; se mantiene como tier débil, no catastrófico.

**Corrección de la anomalía anterior — símbolo en 2m.** La revisión de
ayer generalizó "CL rinde mal, YM rinde muy bien, en 1m Y 2m" con YM en 2m
en n=10 (E[R]=+1.037). Con n=121 hoy, YM en 2m **se volvió negativo**
(E[R]=-0.201) y el corte pasó de `instrument-specific` a `universal`: ya
no hay una excepción positiva por símbolo en 2m, todos los símbolos rondan
negativo o plano. En 1m el patrón CL-malo se mantiene (n=253) pero el
YM-bueno se diluyó fuerte (de E[R]=+0.622 con n=33 a +0.067 con n=227).
**No usar más "YM bueno" como regla — era la misma trampa de n chico que
el tier A+.**

**Anomalía a vigilar** (no accionar): el modelo P(TP1) in-sample sigue
ponderando `aligned` con signo negativo (-0.078 hoy, era -0.109) —
alineado con el sesgo/estructura predice *peor* resultado, aunque el
coeficiente se moderó un poco. La rama `aligned=0` de LONG sigue en n=11.
Sigue pendiente pedir a Jesús que confirme la definición exacta de
`aligned` en Pine.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara de calidad
  de entrada en este segmento.

### Gestión
- **Escalera + parciales (`managed_vs_naive`) SE REVIERTE en 1m y 2m — ya
  no es "no ayuda en LONG" sin matices.** 1m n=971 delta=**+0.057** (naive
  -0.005→managed 0.052, pasó de casi nulo a ayudar); 2m n=475
  delta=**+0.113** (naive -0.135→managed -0.021, **cambió de signo**
  respecto a la revisión anterior que decía delta=-0.039; la escalera
  rescata buena parte de la pérdida cruda aunque no la vuelve positiva);
  5m n=151 delta=**-0.103** (naive 0.169→managed 0.065, sigue siendo el
  único TF donde la gestión resta, consistente con ayer). Ya no se puede
  decir "en LONG el ingenuo rinde igual o mejor" en general — depende del
  TF, y en 5m específicamente sí conviene el ingenuo.
- **SL estructural (`sl_origin_vs_layer`) también cambia de signo en 1m,
  y se aplana en 5m** (comparar con la lectura de ayer): 1m n=802
  delta=**+0.143** (CI90=[-0.0,0.297], roza significativo por el lado
  bueno — ayer era n=171 delta=-0.128, negativo); 2m n=403 delta=+0.069
  (CI90 [-0.053,0.19], no significativo, mismo sentido que ayer); 5m n=143
  delta=+0.003 (CI90 [-0.216,0.25], neutral — ayer rozaba significativo
  por el lado malo con delta=-0.283). **Ninguno certifica todavía, pero la
  dirección ya no apoya "el SL estructural nunca ayuda en LONG"**; vigilar
  1m de cerca, es el más cerca de cruzar a significativo por el lado
  bueno. Sigue sin aplicarse — es medición paralela.
- Objetivo / Parcial 1 / trailing: _pendiente_ — el contrafactual global
  (`counterfactual`, n=9) no está cortado por side todavía.
- `revAfterSL_rate` por corte: `edge=-1` 50.0%, `edge=0` 38.7%, `edge=1`
  23.7% — moderó fuerte desde el 72.2% de `edge=-1` reportado ayer, pero
  sigue siendo la rama que más revierte tras el SL.

### Contextos a evitar
- **`tf=2m` completo** (regla nueva, reemplaza a `tier=A+`): CI90 de E[R]
  no cruza cero por el lado negativo, n=478 en `segment_significance` —
  es hoy el hallazgo más sólido de este playbook, más que cualquier corte
  por tier o símbolo.
- Símbolo `CL` en 1m (regla #3) — ya no generalizar a 2m (regla #3b).
- Autopsia de SL sobre las 830 pérdidas LONG (desglose por kind/side
  permanente en `analyze.py`): `RR-bajo` 338/830 (40.7%) sigue siendo la
  causa **dominante**, seguida de cerca por `contra-estructura` 316/830
  (38.1%) y `killzone-Asia-largo` 303/830 (36.5%) — más repartido que ayer
  (RR-bajo 47% en solitario), pero sigue siendo el candidato principal
  para `sc_min_rr`/`sc_aplus_rr` en la revisión semanal.

### Decaimiento
Con solo 2026-W36 disponible (`decay_weekly` reporta una sola semana,
n=2400 en todo el dataset), sigue sin haber comparación semana-contra-semana
real.

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
