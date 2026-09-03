# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-03 · n: 325)

### Veredicto global
**Salto de muestra ~8x (39→325: 217×1m, 78×2m, 30×5m) y el cuadro cambia
de fondo: 1m deja de ser EVITAR.** 1m WR TP1 47.5%, E[R]=+0.034, PF=1.07
(106 SL de 217) — ya no es negativo como en las dos revisiones anteriores
(-0.283, -0.224); con n multiplicado por 8 esto es una lectura más
confiable que las anteriores, no ruido nuevo. 2m WR 52.6%, E[R]=+0.098,
PF=1.21 (36 SL de 78). 5m WR 66.7%, E[R]=+0.401, PF=2.2 (10 SL de 30) sigue
siendo el mejor TF. Ninguno de los tres certifica todavía en
`segment_significance`: 1m CI90=[-0.106,0.183] p=0.359; 2m CI90=[-0.128,
0.352] p=0.251; **5m CI90=[0.025,0.784] p=0.04 no cruza cero pero
`survives_fdr10=false`** — la corrección por multiplicidad (7 segmentos
probados a la vez) todavía lo rechaza aunque el punto estimado es bueno;
es el más cercano a certificar de todo BUY RETEST. Veredicto: **MUESTRA
GRANDE PERO SIN CERTIFICAR — ya no EVITAR, tampoco TOMAR.** El hallazgo
más accionable de esta corrida no es el TF sino el símbolo y el tier (ver
abajo).

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna certifica con `survives_fdr10` (esa prueba corre por tf/kind/side,
no por estos cortes). Con n ya grande en varias ramas, se tratan como
candidatas fuertes a vigilar 1-2 semanas más antes de tocar Pine:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tier=A+` | **NO tomar — peor resultado del dataset** | 13 | WR 7.7%, E[R]=-0.705, PF=0.24 (12 SL de 13) | alta como alerta — ver anomalía cruzada abajo (mismo patrón que SELL RETEST) |
| 2 | `tier=B` | TOMAR, prioridad | 153 / (159 tier C) | WR 51.6% E[R]=+0.225 PF=1.47 vs tier C WR 52.8% E[R]=+0.011 PF=1.02 | moderada-alta — n=153, tier B es con diferencia la mejor rama de todo LONG, tier C es casi breakeven |
| 3 | símbolo (`cross_instrument`) | **CL rinde mal, YM rinde muy bien, en 1m Y 2m** | 1m: CL n=88 E[R]=-0.172 vs YM n=33 E[R]=+0.622 (spread 0.794, `instrument-specific`). 2m: CL n=29 E[R]=-0.323 vs YM n=10 E[R]=+1.037 (spread 1.36, `instrument-specific`) | moderada-alta — mismo patrón (CL malo / YM bueno) repetido en dos TF con n razonable en CL; candidato a filtro por símbolo antes que por TF |
| 4 | `nearEdge=1` | mejor que `edge=-1`/`edge=0` | 152 / 49 / 124 | WR 48.0%/55.1%/51.6%; E[R] +0.169/+0.016/+0.004; PF 1.33/1.04/1.01 | moderada — E[R] y PF sí son monótonos hacia `edge=1` (igual que en SELL RETEST), aunque el WR no lo es (edge=-1 tiene el WR más alto con el peor PF: ganancias más chicas) |
| 5 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1` | 11 vs 314 | E[R] +0.459 vs +0.076, WR 54.5% vs 50.3%, PF 4.21 vs 1.16 | baja-moderada — creció de n=7 a n=11 pero sigue chico; anomalía de signo, ver nota abajo |

**Anomalía cruzada — `tier=A+` sigue invertido, y ahora con muestra real
en LONG.** La revisión anterior no tenía ninguna señal LONG `A+` (n=0);
ahora n=13 y es el peor resultado de *todo* el dataset (peor incluso que
el A+ de SELL RETEST, que se moderó — ver `sell-retest.md`). En ambos
lados `tier=B` bate a `tier=A+`, nunca al revés. Esto ya no es un patrón
de un solo side con muestra chica: es sistemático en LONG y SHORT. Se
mantiene la hipótesis de la revisión anterior (la fórmula de scoring de
tier en `scalp_command.pine` puede estar premiando RR de entrada alto /
señal lejos del borde, que empíricamente predicen peor resultado) —
todavía no se propone cambio de Pine (esperando `survives_fdr10` real),
pero con n=13+54=67 señales A+ combinadas peor que B en ambos lados, es
candidato fuerte a "cambio del mes" en la próxima revisión semanal si se
sostiene.

**Anomalía a vigilar** (no accionar): el modelo P(TP1) in-sample sigue
ponderando `aligned` con signo negativo (-0.109) — alineado con el
sesgo/estructura predice *peor* resultado. La rama `aligned=0` de LONG
creció de n=7 a n=11 sin cambiar de signo. Sigue pendiente pedir a Jesús
que confirme la definición exacta de `aligned` en Pine.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara de calidad
  de entrada en este segmento.

### Gestión
- **Escalera + parciales (`managed_vs_naive`) NO ayuda en LONG, al revés
  que en SHORT**: 1m n=210 delta=+0.008 (casi nulo), 2m n=74
  delta=**-0.039** (la gestión pierde contra 1 contrato a mercado), 5m
  n=30 delta=**-0.11** (pierde más). Contraste fuerte con SELL RETEST
  donde la escalera aporta en 1m y 5m. No aplicar la config de escalera
  como si fuera universal — en LONG el ingenuo (mercado, 1 contrato) hoy
  rinde igual o mejor.
- **SL estructural (`sl_origin_vs_layer`) tampoco mejora en LONG** (al
  revés que en SHORT, ver `sell-retest.md`): 1m n=171 delta=-0.128 (CI90
  [-0.344,0.092], no significativo), 2m n=53 delta=+0.171 (CI90 muy ancho,
  no significativo), 5m n=30 delta=-0.283 (CI90 [-0.634,0.027], roza
  significativo por el lado malo). No mover el SL a la mecha estructural
  en LONG con la evidencia actual.
- Objetivo / Parcial 1 / trailing: _pendiente_ — el contrafactual global
  (`counterfactual`, n=9) no está cortado por side todavía.
- `revAfterSL_rate` por corte: `edge=-1` 72.2%, `edge=0` 32.8%,
  `aligned=1` 34.4% — la rama `edge=-1` (la de peor PF, ver regla #4)
  también es la que más revierte tras el SL: apunta a SL mal ubicado ahí
  más que a dirección equivocada.

### Contextos a evitar
- `tier=A+` (regla #1) y símbolo `CL` en 1m/2m (regla #3).
- Autopsia de SL sobre las 152 pérdidas LONG (desglose por kind/side ya
  permanente en `analyze.py`, sin cap de 60 filas): `RR-bajo` 71/152
  (47%) es ahora la causa **dominante única** (ya no un triple empate como
  en la revisión anterior con n=18) — `contra-estructura` 56/152 (37%),
  `stop-en-el-minimo` 52/152 (34%), `killzone-Asia-largo` 29/152 (19%),
  `chop` 28/152, `sin-nivel-detras` 27/152, resto menor. Con esta muestra
  (n=152 pérdidas) `RR-bajo` ya es candidato serio para `sc_min_rr` o
  `sc_aplus_rr` en la próxima revisión semanal, cruzado con la anomalía de
  tier A+ (que también viene con `rr1` alto — mismo mecanismo posible).

### Decaimiento
Con solo 2026-W36 disponible (`decay_weekly` reporta una sola semana,
n=943 en todo el dataset), sigue sin haber comparación semana-contra-semana
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
