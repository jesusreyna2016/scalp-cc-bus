# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-23 (miércoles) · n: 8828)

### Nota de proceso
`git pull` limpio hoy (`Already up to date`, sin incidentes de repo).
Dato nuevo moderado: 1m LONG +413 (5334→5747), 2m LONG +146
(2388→2534), 5m LONG +52 (833→885).

### Veredicto global
1m n=5747 (+413) WR 46.1% E[R]=**0.075** PF=1.15 (baja de 0.088); 2m
n=2534 (+146) WR 48.3% E[R]=**0.077** PF=1.16 (sube de 0.072); 5m n=885
(+52) WR 52.5% E[R]=**0.189** PF=1.44 (sube de 0.181).
`segment_significance`: **1m CI90=[0.046,0.104] p=0.0 n=5584 —
sostiene `survives_fdr10=true`** (quinta lectura consecutiva); **2m
CI90=[0.036,0.12] p=0.001 n=2441 — segunda lectura consecutiva
certificando** (el límite inferior sube de 0.027 a 0.036, se aleja un
poco más de cero — un paso más para dejar de tratarlo como "frágil");
**5m CI90=[0.117,0.264] p=0.0 n=835 — sostiene `survives_fdr10=true`**,
décima confirmación. `gate.readyForLive` del sistema sigue en `true`
con `segment=5m/RETEST/LONG`. Las tres semanas cerradas no cambian hoy
(W36 PF=**1.18** bajo el umbral 1.3, W37 PF=**1.46**, W38 PF=**1.44**)
— sigue faltando la racha de "3 semanas con PF≥1.3" y el experimento de
SL estructural sigue `proposed`, sin `changeDate`. Walk-forward OOS
(`best_scheme_oos_expR`) da **0.091** positivo sobre W38-W39 (baja de
0.105 pero sigue claramente positivo) — coherente con que el edge
sobrevive fuera de muestra. Veredicto sin cambio de fondo: los tres TF
siguen certificando FDR en E[R] crudo; 2m suma su segunda confirmación
y empieza a dejar de ser la lectura más frágil.

### Reglas condicionales (IF contexto ENTONCES acción)

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tf=1m` (`survives_fdr10=true`) | TOMAR, edge real fuera de ruido | 5584 (+411) | E[R]=**0.075** CI90=[0.046,0.104] | alta — quinta lectura consecutiva certificando con FDR |
| 2 | `tf=5m` (`survives_fdr10=true`) | TOMAR, edge real fuera de ruido, el más grande de los tres TF | 835 (+53) | E[R]=**0.189** CI90=[0.117,0.264] | alta — décima confirmación |
| 3 | `tf=2m` (`survives_fdr10=true`) | TOMAR, edge real fuera de ruido | 2441 (+145) | E[R]=**0.077** CI90=[0.036,0.12] | moderada — segunda lectura seguida certificando, límite inferior sube |
| 4 | `tier=A+` | sigue positivo, baja un poco | 693 (+31) | WR 25.5%, E[R]=**0.129** (baja de 0.163), PF=1.2 | moderada — quinto día seguido sin revertir a negativo |
| 5 | `tier=B` | TOMAR, prioridad sobre A+ y C | 3851 (+193) vs 4622 (+387) tier C | WR 47.4% E[R]=0.108 (baja de 0.114) PF=1.23 vs tier C WR 50.6% E[R]=**0.062** (sube de 0.063→0.062, ~igual) PF=1.14 | alta — B sigue siendo la rama más fuerte |
| 6 | símbolo (`cross_instrument`), 1m | sigue `universal` | spread 0.086 (baja de 0.118) | moderada-alta — sin cambio de veredicto |
| 7 | símbolo (`cross_instrument`), **5m** | sigue `universal` | spread 0.273 (baja de 0.343) | moderada — sin cambio de veredicto |
| 8 | `nearEdge=-1` | baja bastante con el dato nuevo | 323 (+38) | E[R]=**0.149** (baja de 0.197) | moderada — sigue por encima del resto de las ramas de edge, pero el margen se reduce |
| 9 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1`, muestra **estable en n=9** (sin señales nuevas otra vez) | 9 vs 9157 (+611) | E[R] +0.433 vs +0.086, WR 55.6% vs 47.3%, PF 3.6 vs 1.18 | baja — n sigue demasiado chico para usar |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara de calidad
  de entrada en este segmento.

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=5580 delta=**+0.076**
  (sube un poco de 0.071); 2m n=2439 delta=**+0.022** (baja de 0.025);
  5m n=835 delta=**-0.061** (sigue negativo, sigue siendo el único TF
  donde la gestión resta en LONG). Regla sin cambios: escalera en
  1m/2m, mercado simple en 5m LONG.
- **SL estructural (`sl_origin_vs_layer`)**: 1m LONG n=4836 (+343)
  delta=**+0.126** CI90=[0.072,0.184] — decimoquinta confirmación, sin
  reversión (baja un poco de 0.132, sigue sólido); **5m LONG** n=797
  (+50) delta=**+0.272** CI90=[0.117,0.439] — undécima lectura seguida
  (baja de 0.299, sigue siendo el efecto más grande de los tres TF LONG);
  **2m LONG** n=2218 (+137) delta=**+0.151** CI90=[0.087,0.221] — quinta
  lectura consecutiva sosteniendo la certificación, sube de 0.14. Propuesta
  sin cambios: **1m LONG, 1m SHORT, 2m LONG, 5m LONG, 5m SHORT** — ver
  `sell-retest.md`: hoy **2m SHORT certifica por primera vez** con margen
  claro (antes al filo), así que la propuesta pasa a **6 segmentos**. Ver
  `experiments.json` (`sl-retest-wick-2026-09-03`) y
  `reviews/2026-week-38.md`. Sigue sin aplicarse en TradingView
  (`changeDate` null).
- **Modo sombra (`shadow_rules`)**: cuarta lectura desde que se definió
  el 09-20. Hoy: shadow E[R]=**0.078** (n=10622) sigue batiendo al
  indicador crudo E[R]=**0.075** (n=14775), pero el margen se redujo a
  casi nada (+0.003, antes +0.007) y **tier A+/B solo (E[R]=0.084,
  n=7223) vuelve a ser el mejor de los tres conjuntos** — anotar como
  algo a vigilar: el conjunto de reglas condicionales de la sombra ya no
  bate claramente al filtro simple de tier; los CI90 de los tres se
  solapan casi por completo ([0.055,0.097] shadow vs [0.055,0.111] tier),
  así que no hay diferencia estadística todavía, pero el reloj de 3
  semanas seguidas batiendo al crudo para el gate de peldaño 0→1 no debe
  darse por cumplido con este margen. Ver `execution-ladder.md` y
  `report.md` sección "Modo sombra".
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL sobre las 4196 pérdidas LONG (+301 vs ayer): `RR-bajo`
  1569/4196 (37.4%) sigue como causa dominante, `killzone-Asia-largo`
  1501/4196 (35.8%) sube al segundo puesto (antes tercero),
  `contra-estructura` 1495/4196 (35.6%) baja al tercero (antes segundo,
  diferencia de 0.2pp — prácticamente empatadas, no tratar el cambio de
  orden como señal real), `stop-en-el-minimo` 1408/4196 (33.6%) cuarto,
  sin cambio. El SL estructural (arriba) sigue siendo el candidato que
  mejor ataca `RR-bajo` de las cuatro.

### Cruce con Session Analyst
`WAIT` n=2316 (+369) E[R]=**+0.115** (baja de 0.143, sigue sólido);
`GO` n=557 (+25) E[R]=**+0.177** (baja un poco de 0.187, **segundo día
seguido por encima de WAIT** en este playbook — ya no es un evento de
un solo día); `AVOID` n=803 (-13, dedup de agregado) sigue en terreno
negativo: **-0.018**. **A nivel global (todo kind/side)**: la hipótesis
original de `agent-instructions.md` era "AVOID rinde peor" — sigue SIN
confirmarse con significancia (`by_verdict_ci90` AVOID E[R]=0.005
CI90=[-0.05,0.06] p=0.434, cruza cero, n=1354); pero **WAIT y GO siguen
certificando ambos con significancia**: WAIT (E[R]=0.063
CI90=[0.033,0.096] p=0.001, n=3656) y GO (E[R]=0.192 CI90=[0.113,0.268]
p=0.0, n=764) — ver `report.alerts`. No generalizar la hipótesis sin
mirar el desglose por side (**SELL RETEST el orden histórico es GO
mejor, WAIT peor**, ver `sell-retest.md`).

### Decaimiento
`decay_weekly` (global, no por segmento): 2026-W36 n=2991 WR 44.6%
E[R]=**-0.02**; 2026-W37 n=5199 WR 46.8% E[R]=**0.072**; 2026-W38
n=4847 WR 46.3% E[R]=**0.089** (W37/W38 siguen bajando 1-2 pares por
corrida por el mismo mecanismo de dedup benigno, ver alerta MUESTRA en
`report.alerts` — sin evidencia de pérdida real de archivo, ya son
~12-14 corridas seguidas del mismo goteo pequeño, vigilar que no sea un
problema real de re-pareo si sigue sin estabilizarse); **2026-W39
n=2120 WR 50.5% E[R]=0.187 — la semana en curso ya tiene muestra real,
sigue siendo prematuro leerla como estable**. Por segmento
(`decay_weekly_by_segment`), 5m/RETEST/LONG, las tres semanas cerradas
sin cambio: W36 n=242 E[R]=0.082 PF=**1.18** (bajo el umbral 1.3 — la
que hoy frena el gate de ejecución); W37 n=231 E[R]=0.208 PF=**1.46**;
W38 n=319 WR 50.8% E[R]=0.177 PF=**1.44**. W39 ya suma n=93 (WR 59.1%,
E[R]=0.449, PF=2.16 — muestra parcial de la semana en curso, sube
fuerte pero no cuenta como semana cerrada). WR TP1 estable en las tres
semanas cerradas (52.5/52.4/50.8%) y E[R]>0 en las tres, pero sólo 2 de
3 con PF≥1.3 — no se cumplen todavía las "3 semanas estables" del gate.
Sin caída de WR > 15 pts en ninguna semana cerrada, en ningún TF de este
playbook — sin señal de decaimiento real.

## Histórico de cambios
- 2026-09-23 (miércoles): `git pull` limpio, sin incidentes de repo.
  Dato nuevo moderado y parejo en los tres TF (+413/+146/+52 en
  1m/2m/5m). **2m/RETEST/LONG suma su segunda confirmación FDR seguida**
  (límite inferior del CI90 sube de 0.027 a 0.036) — empieza a dejar de
  tratarse como lectura única y frágil. El SL estructural en **2m SHORT
  certifica por primera vez con margen claro** (ver `sell-retest.md`), así
  que la propuesta formal de SL pasa de 5 a **6 segmentos**. Hallazgo a
  vigilar, no a actuar: el modo sombra (`shadow_rules`) redujo su ventaja
  sobre el indicador crudo a casi nada (+0.003) y **tier A+/B solo volvió
  a ser el mejor de los tres conjuntos comparados** — los CI90 se solapan
  por completo, así que no hay reversión estadística todavía, pero el
  reloj de 3 semanas del gate de peldaño 0→1 no debe leerse como "shadow
  gana con claridad" mientras el margen siga tan chico. Autopsia de SL:
  `killzone-Asia-largo` y `contra-estructura` intercambian el 2°/3° puesto
  por una diferencia de 0.2pp (ruido, no señal). Cruce con Session
  Analyst: `GO` por encima de `WAIT` por **segundo día seguido** — ya no
  es un evento de un solo día, empieza a parecer un cambio de régimen a
  vigilar (sigue siendo la primera vez que se ve sostenido en este
  playbook). Sin cambios en el gate de ejecución (sigue en asesoría,
  W36 PF=1.18<1.3, experimento de SL sigue `proposed` sin `changeDate`).
  La alerta MUESTRA de W37/W38 lleva ya varias corridas seguidas sin
  estabilizarse del todo (goteo de 1-2 pares por corrida) — sigue sin
  evidencia de pérdida real de archivo, pero se anota como algo a seguir
  vigilando si no converge pronto.
- 2026-09-22 (martes): salto de dato grande y genuino (+1027 outcomes en
  todo el bus, el lote de 2026-09-21 asentándose de una vez; +439/+174/+37
  en 1m/2m/5m de este playbook). **Hallazgo principal: `2m/RETEST/LONG`
  CERTIFICA `survives_fdr10` en E[R] crudo por primera vez**
  (CI90=[0.027,0.114], n=2296) — junto con 1m y 5m ya certificados, es la
  primera vez que los tres TF de este playbook certifican FDR
  simultáneamente; tratar 2m como lectura frágil hasta 2-3 confirmaciones
  más. El SL estructural en 2m LONG suma su cuarta lectura sosteniendo la
  certificación (delta 0.14, casi idéntico a ayer). `sl_origin_vs_layer`
  en 1m INV/LONG (ver `buy-ifvg.md`) certifica por primera vez en sentido
  contrario (favorece el SL de 3 capas). Gate de ejecución sigue
  bloqueado en el peldaño "asesor": W36 PF=1.18 < 1.3 y el experimento
  `sl-retest-wick` sigue `proposed` sin `changeDate` — ningún cambio de
  fondo en la decisión del gate pese a `readyForLive=true` del sistema.
- 2026-09-21 (lunes, primer día hábil con dato nuevo genuino tras el fin
  de semana, +72 pares en todo el bus / +57 en este playbook): `HEAD`
  detached tras el `git pull` (mismo patrón de "forced update" de
  `origin/main` de siempre) pero ya apuntaba al mismo commit remoto, sin
  pérdida. **Hallazgo más importante: el SL estructural en 2m LONG suma
  su TERCERA lectura consecutiva con dato genuinamente nuevo**
  (0.153→0.151, CI90 prácticamente sin cambio) — cumple el criterio de
  "2-3 lecturas seguidas" y se gradúa a candidato de la propuesta
  formal (con la misma advertencia de historial volátil que se le puso
  a 5m LONG en su momento); la propuesta pasa de 4 a 5 segmentos: 1m
  LONG, 1m SHORT, 2m LONG, 5m LONG, 5m SHORT. 1m LONG certifica su
  tercera lectura FDR seguida (n=4738, CI90=[0.028,0.086]). **5m no tuvo
  ninguna señal LONG nueva hoy** (n=796, idéntico a ayer) — todo lo que
  depende de 5m (FDR, SL estructural, decay) se mantiene congelado en su
  lectura anterior, no cuenta como confirmación nueva. Autopsia de SL
  sin cambios de orden (RR-bajo sigue dominante, 38.0%). Cruce con
  Session Analyst sin dato nuevo que caiga en el join de hoy, cifras
  idénticas a ayer. Sin cambios de estado en el gate de ejecución (sigue
  en asesoría, `readyForLive=true` pero W36 todavía con PF<1.3) ni en el
  experimento de SL (`proposed`, sin `changeDate`). Modo sombra
  (`shadow_rules`) suma su segundo día seguido batiendo al indicador
  crudo (E[R] 0.07 vs 0.059, n=9077).
- 2026-09-20 (domingo, REVISIÓN SEMANAL, cierre de 2026-W38): **primer
  fin de semana sin ningún archivo `signals/outcomes` nuevo** desde que
  arrancó el bus (último commit sigue siendo `outcomes 2026-09-18`) — los
  únicos pares que cambiaron de estado (+25 en este playbook, +37 en todo
  el bus) fueron señales pendientes desde el viernes que cruzaron 24h sin
  outcome y se resolvieron como TIMEOUT forzado; todas las métricas que
  requieren outcome real (`segment_significance`, `sl_origin_vs_layer`,
  `managed_vs_naive`) dan cifras idénticas a ayer — no es un fallo de
  pipeline, es la ausencia esperada de sesión NY en fin de semana.
  **Mejora permanente en `analyze.py`: primer borrador de `shadow_rules`**
  (modo sombra, gate de peldaño 0→1) — el conjunto de reglas
  condicionales más robusto de hoy (RETEST + los 4 segmentos
  `survives_fdr10=true` + excluir SA=AVOID) bate al indicador crudo en
  E[R] (0.066 vs 0.056, n=9032) desde su primera lectura; arranca el
  reloj de 3 semanas seguidas que pide `execution-ladder.md`. **Cierre de
  2026-W38** (revisión semanal completa en `reviews/2026-week-38.md`):
  con las 3 semanas que ya existen en todo el bus, WR TP1 de
  5m/RETEST/LONG estable (52.5/52.2/51.2%) y E[R]>0 las tres, pero W36
  (PF=1.18) sigue siendo la única que no llega a PF≥1.3 — el gate de
  ejecución sigue sin las "3 semanas estables" que exige, y el
  experimento de SL estructural sigue `proposed` sin `changeDate`. Sin
  cambios de dirección en ninguna regla condicional de este playbook.
- 2026-09-19 (sábado): mismo patrón de "forced update" en `origin/main`
  (verificado sin pérdida). Salto de dato grande, el mayor en varios
  días (n 6657→7823, +1166; el bus asentó de una vez los archivos de
  2026-09-18). **Hallazgo más importante: 1m/RETEST/LONG certifica con
  FDR por primera vez** (`segment_significance` CI90=[0.023,0.082],
  antes el límite inferior tocaba cero exacto) — se convierte en el
  tercer segmento LONG con edge estadísticamente real, junto a 5m. El SL
  estructural en 2m LONG suma su segunda lectura seguida certificando y
  se fortalece mucho (delta 0.074→0.153, CI90 deja de rozar cero) — un
  paso más cerca de sumarse a la propuesta formal. `cross_instrument` en
  5m cambia de `instrument-specific` a `universal` por primera vez
  (spread 0.432→0.334). La autopsia de SL despeja el casi-empate de
  varias corridas: `RR-bajo` se separa como causa dominante clara. El
  cruce con Session Analyst tiene su cuarto vaivén de signo en `AVOID`
  (vuelve a negativo) — seguir tratándolo como ruido, no como señal. El
  gate de ejecución sigue bloqueado por el PF de W36 (1.18, bajo 1.3,
  esta vez sin perder más muestra); W37 perdió 2 pares más por dedup
  (cuarta corrida seguida) sin evidencia de pérdida real de archivo. Sin
  cambios de estado en el experimento de SL (`proposed`, sin
  `changeDate`).
- 2026-09-18 (viernes): `origin/main` fue reescrito río arriba (historia
  sin ancestro común, primera vez desde 09-11) — verificado como el
  mismo tip de datos, sin pérdida, resuelto con `checkout -B main
  origin/main`. n 6102→6657 (+555; 1m+354, 2m+130, 5m+71). **Hallazgo más
  importante: el SL estructural en 2m LONG certifica por primera vez**
  (`sl_origin_vs_layer`, delta 0.05→0.074, CI90 deja de cruzar cero) tras
  11 lecturas sin lograrlo — tratado como candidato nuevo y frágil, no se
  suma aún a la propuesta formal. 5m LONG da un salto fuerte en su octava
  confirmación (delta 0.218→0.312). **Dos giros de ayer resultaron ser
  ruido de un día**: 2m/RETEST/LONG vuelve a E[R] negativo (+0.01→-0.004)
  y en el cruce con Session Analyst el orden "WAIT mejor, GO peor" se
  reafirma (AVOID vuelve a positivo, GO baja) — lección de método
  explícita sobre no fijar conclusiones con un solo día de dato. La
  autopsia de SL reordena sus causas: `killzone-Asia-largo` cae al
  tercer puesto por primera vez en varios días. El gate de ejecución
  sigue bloqueado por el PF de la semana cerrada W36 (1.18, bajo 1.3);
  W36 y W37 volvieron a perder 1 par cada una por dedup a nivel de
  segmento (tercera corrida seguida). Sin cambios de estado en el
  experimento de SL (sigue `proposed`, sin `changeDate`).
- 2026-09-17 (jueves): HEAD quedó detached tras el `git pull` (fetch al
  día pero rama local sin mover), resuelto con `checkout -B main
  origin/main`, sin pérdida. **Salto de dato grande, el mayor en varios
  días** (n 5305→6102, +797). **2m/RETEST/LONG cruza a E[R] positivo por
  primera vez en varios días** (-0.017→+0.01) y el CI90 de 1m se acerca
  a certificar (límite inferior -0.011→-0.002). **5m suma su QUINTA
  lectura FDR seguida** y el SL estructural en 5m LONG llega a su
  SÉPTIMA confirmación. **Hallazgo nuevo más importante**: en el cruce
  con Session Analyst, la rama `GO` en LONG mejora fuerte (E[R]
  -0.06→+0.12, n casi se duplica) y `AVOID` cruza a negativo por primera
  vez (+0.014→-0.019) — el orden "WAIT mejor, GO peor" que llevaba
  varios días empieza a cambiar; a nivel global, `GO` certifica con
  significancia por primera vez junto a `WAIT` (ver `report.alerts`).
  Nota de método: la semana ya cerrada 2026-W37 pierde muestra por dedup
  también **a nivel del segmento 5m/RETEST/LONG** (n 241→235), primera
  vez que se ve este efecto fuera de los conteos agregados — el PF de esa
  semana en el segmento sigue por encima de 1.3 (1.44→1.45) así que no
  cambia la conclusión del gate, pero vigilar que el dedup no erosione
  series por segmento. Sin cambios de estado en el gate (sigue en
  asesoría) ni en el experimento de SL (sigue `proposed`, sin
  `changeDate`).
- 2026-09-16 (miércoles): "forced update" habitual de `origin/main`
  (shallow clone, mismo tip, sin pérdida), resuelto igual que siempre.
  Dato nuevo moderado (n 5163→5305, +142). **5m RETEST/LONG suma su
  CUARTA lectura seguida certificando FDR** y el SL estructural en 5m
  LONG llega a su SEXTA confirmación seguida (delta 0.246→0.248,
  CI90=[0.063,0.479]) — el candidato antes más frágil de la propuesta ya
  acumula tanta evidencia como el más sólido (1m LONG, novena
  confirmación). El gate de ejecución sigue sin cumplirse por el mismo
  motivo de siempre: la semana cerrada W36 tiene PF=1.19 (<1.3) y el
  experimento de SL sigue sin `changeDate`. `2026-W37` (semana cerrada)
  perdió 1 par más de muestra por dedup (5376→5375) — segundo día
  seguido bajando, vigilar que no sea el inicio de una tendencia real en
  vez de ruido de dedup. Nada más accionable nuevo: día de confirmación,
  no de sorpresas.
- 2026-09-15 (martes): otro "forced update" de `origin/main` al inicio
  (mismo patrón que corridas anteriores, resuelto sin pérdida). Salto de
  dato grande y genuino (n 4851→5163, +312) tras el mínimo de ayer.
  **5m RETEST/LONG suma su TERCERA lectura seguida certificando FDR**,
  pero el gate de ejecución sigue sin cumplirse: la semana cerrada W36
  tuvo PF=1.19 en este segmento (< 1.3 exigido), así que "3 semanas
  estables" todavía no se cumple aunque `gate.readyForLive` crudo diga
  `true`. Los 4 segmentos de la propuesta de SL estructural se mantienen
  estables (5m LONG llega a su quinta confirmación). Hallazgo más
  importante del día: la hipótesis "SA=AVOID rinde peor" sigue sin
  confirmarse (CI90 cruza cero), pero "SA=WAIT rinde mejor" sí certifica
  a nivel global — y ese efecto es en realidad una mezcla de dos patrones
  opuestos por lado (WAIT mejor en LONG, GO mejor en SHORT, ver
  `sell-retest.md`). Se corrigió un bug de `analyze.py`: la alerta de
  caída de muestra en semanas ya cerradas se repetía idéntica cada
  corrida en vez de solo cuando la cifra seguía empeorando (ver Nota de
  proceso).
- 2026-09-14 (lunes): primer día hábil tras la revisión semanal, `git
  pull` limpio (sin incidentes de repo por primera vez en varias
  corridas). Salto de muestra mínimo, como se esperaba (n 4831→4851,
  +20) — reapertura de Globex del domingo por la noche. **5m RETEST/LONG
  sostiene su certificación FDR por segundo día seguido**
  (CI90=[0.058,0.242]), primera confirmación independiente del hito de
  ayer, aunque con muestra nueva mínima (+4). Los 4 segmentos de la
  propuesta formal de SL estructural de la revisión semanal (1m
  LONG/SHORT, 5m LONG/SHORT) se mantienen estables sin ningún
  retroceso — primer día de confirmación post-propuesta. La racha de 4
  días de la semana 2026-W36 perdiendo muestra agregada se detuvo (se
  mantuvo en n=3140). Nada accionable nuevo: día de muestra demasiado
  chica para mover ninguna conclusión de fondo.
- 2026-09-13 (domingo, REVISIÓN SEMANAL): n 4314→4831 (+517; 1m+312,
  2m+123, 5m+82). Incidente menor de repo (`git pull` "forced update",
  verificado como superset sin pérdida real — ver Nota de proceso
  arriba). **Hallazgo más importante del bus hasta la fecha**: 5m
  RETEST/LONG certifica con `survives_fdr10=true` por primera vez
  (E[R]=0.154, CI90=[0.061,0.248]), lo que dispara `gate.readyForLive`
  del sistema — pero la escalera de ejecución exige además 3 semanas de
  estabilidad (sólo hay 2, una sin cerrar) y un experimento de SL
  aplicado y confirmado, así que se mantiene en asesoría, sin subir de
  peldaño. El SL estructural (`sl_origin_vs_layer`) en 5m LONG certifica
  por TERCERA lectura seguida (delta 0.187→0.255) y se gradúa a
  candidato sólido para la propuesta formal de la revisión semanal
  (junto a 1m LONG/SHORT y 5m SHORT; ver `reviews/2026-week-37.md` y
  `experiments.json`). La autopsia de SL separa `RR-bajo` como causa
  dominante clara por primera vez en varios días (38.3% vs 37.0% de
  `contra-estructura`, antes casi empatadas). La semana ya cerrada
  2026-W36 pierde muestra por cuarta corrida seguida (3179→3140) sin
  evidencia de pérdida real de archivos — vigilar si no se estabiliza.
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
