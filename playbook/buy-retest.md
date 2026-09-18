# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-18 · n: 6657)

### Nota de proceso
`git pull` dejó HEAD en detached: `origin/main` fue reescrito río arriba
(historia sin ancestro común con la rama local, primera vez desde
09-11) — verificado que el remoto contenía el mismo tip de datos y los
últimos 50 commits del bus (patrón "bus" con ventana fija de historia,
no pérdida), resuelto con `checkout -B main origin/main`. n 6102→6657
(**+555**; 1m+354, 2m+130, 5m+71). `file_integrity_check` limpio,
`orphan_outcomes` en 26 (sin cambio) — sin señal de problema de
pipeline.

### Veredicto global
1m n=4104 (+354) WR 44.9% E[R]=**0.034** PF=1.07 (~sin cambio de
+0.032); 2m n=1860 (+130) WR 46.3% E[R]=**-0.004** PF=0.99 (**vuelve a
terreno negativo**, la cruzada a positivo de ayer, +0.01, no se sostuvo
— lección de método: no fijar un giro con un solo día de dato); 5m
n=693 (+71) WR 51.4% E[R]=**0.157** PF=1.36 (prácticamente sin cambio de
+0.153). `segment_significance`: 1m CI90=**[0.0,0.066]** p=0.045 n=3965
(el límite inferior toca exactamente cero — a un pelo de certificar,
vigilar de cerca la próxima corrida); 2m CI90=[-0.048,0.043] p=0.569
n=1778 (se aleja de cero por el lado negativo, coherente con el E[R]
negativo de hoy); **5m CI90=[0.078,0.24] p=0.0 n=651 — sostiene
`survives_fdr10=true` por SEXTO día seguido**. `gate.readyForLive` del
sistema sigue en `true` con `segment=5m/RETEST/LONG`. **Sigue sin
recomendarse subir de peldaño**: de las dos semanas ya *cerradas*, W36
tiene PF=**1.18** en este segmento (bajo el umbral 1.3, bajó un poco de
1.19) y W37 da PF=**1.47** (sube de 1.45) — **ambas semanas volvieron a
perder 1 par de muestra por el mismo mecanismo de dedup ya conocido**
(W36 n=243→242, W37 n=235→234), tercera corrida seguida en que este
efecto toca el segmento objetivo del gate, sin evidencia de pérdida real
de archivo. Con sólo 2 semanas cerradas (una bajo el umbral) todavía no
se cumplen las "3 semanas estables" que pide la escalera, y el
experimento de SL estructural (abajo) sigue en estado `proposed`, sin
`changeDate`. Veredicto actualizado: **2m revierte a negativo (lección
de no fijar giros de un día); 5m en su sexta lectura de certificación
FDR — sigue asentado, pero el gate de ejecución pide más que la
certificación estadística sola.**

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna certifica con `survives_fdr10` a este nivel de corte:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tier=A+` | **retrocede fuerte tras 3 días subiendo** | 502 (+49) | WR 24.5%, E[R]=**0.064** (bajó de 0.114), PF=1.1 | baja — el "empieza a parecer tendencia" de ayer no se sostuvo, confirma que sigue siendo ruido con n mediano |
| 2 | `tier=B` | TOMAR, prioridad sobre A+ y C | 2776 (+222) vs 3379 (+284) tier C | WR 46.6% E[R]=0.071 (bajó de 0.08) PF=1.15 vs tier C WR 48.6% E[R]=**+0.003** (**cruza a positivo por primera vez en varias corridas**, venía de -0.007) PF=1.01 | alta-moderada — B sigue siendo la rama más fuerte, pero C deja de ser claramente negativo, vigilar si se sostiene |
| 3 | símbolo (`cross_instrument`), 1m | sigue `universal`, spread se achica | spread 0.074 (bajó de 0.104) | moderada-alta — sin cambio de fondo, cada vez más lejos de `instrument-specific` |
| 4 | símbolo (`cross_instrument`), **5m** | sigue `instrument-specific`, pero el spread se achica bastante | spread 0.432 (bajó de 0.626) — NQ sigue siendo el símbolo más débil pero menos negativo (n=226, E[R]=-0.048, antes -0.128), CL sigue el mejor (n=165, E[R]=0.286) | baja-moderada — no generalizar la certificación FDR de 5m a NQ, pero la brecha se está cerrando |
| 5 | `nearEdge=-1` | prácticamente sin cambio | 264 (-2, dedup fino) | E[R]=**0.172** (bajó un poco de 0.18) | moderada — sigue elevado, sin cambio de fondo |
| 6 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1`, muestra **estable en n=9** (sin señales nuevas) | 9 vs 6648 (+555) | E[R] +0.433 vs +0.035, WR 55.6% vs 46.0%, PF 3.6 vs 1.07 | baja — cifras idénticas a ayer, n sigue demasiado chico para usar |

**Símbolo en 1m sigue `universal`**, spread se estrecha más (~0.07).
**5m sigue `instrument-specific`** pero el spread se achica bastante
(NQ menos rezagado que ayer) — sigue sin generalizar la certificación
FDR de 5m a ese símbolo, pero la brecha entre símbolos se cierra.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara de calidad
  de entrada en este segmento.

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=3961 delta=**+0.087**
  (~sin cambio de +0.086); 2m n=1776 delta=**+0.067** (baja un poco de
  +0.074); 5m n=651 delta=**-0.068** (se hace un poco más negativo desde
  -0.065, sigue siendo el único TF donde la gestión resta en LONG). Regla
  sin cambios: escalera en 1m/2m, mercado simple en 5m LONG.
- **SL estructural (`sl_origin_vs_layer`)**: 1m LONG sigue certificando,
  n=3410 (+315) delta=**+0.145** CI90=[0.076,0.214] (prácticamente
  idéntico a ayer, +0.142) — UNDÉCIMA confirmación independiente. **5m
  LONG suma su OCTAVA lectura seguida certificando** con un salto
  notable: n=622 (+67) delta=**+0.312** CI90=**[0.123,0.525]** (sube
  fuerte de +0.218, CI90 se aleja mucho más de cero) — sigue siendo
  candidato sólido de la propuesta formal (junto a 1m LONG/SHORT y 5m
  SHORT). **2m CERTIFICA POR PRIMERA VEZ** tras 11 lecturas sin
  lograrlo: n=1599 (+122) delta=**+0.074** CI90=**[0.005,0.145]** (el
  límite inferior cruzó por encima de cero, antes [-0.018,0.12]) — se
  trata como candidato NUEVO y frágil, no se suma todavía a la propuesta
  formal (mismo criterio de "2-3 lecturas seguidas" con el que se
  promovió 5m LONG en la semana pasada). Los 4 segmentos propuestos el
  09-13 (1m LONG/SHORT, 5m LONG/SHORT) se mantienen todos con
  `delta_beats_zero=true`, sin ningún retroceso desde la propuesta. Ver
  `reviews/2026-week-37.md` y `experiments.json`
  (`sl-retest-wick-2026-09-03`). Sigue sin aplicarse en TradingView
  (`changeDate` null).
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- **`tf=2m`**: E[R] vuelve a terreno negativo (-0.004) tras un solo día
  positivo — el CI90 ([-0.048,0.043], n=1778) sigue cruzando cero,
  "neutro, sin edge claro", no "leve positivo" como se leyó ayer.
- Autopsia de SL sobre las 3115 pérdidas LONG (+273 vs ayer): el orden
  cambia — `RR-bajo` 1184/3115 (38.0%) y `contra-estructura` 1182/3115
  (37.9%) quedan prácticamente empatados en el primer lugar,
  `killzone-Asia-largo` 1068/3115 (34.3%) **cae al tercer puesto** (bajó
  de 37.5%, la caída más marcada de las cuatro causas top),
  `stop-en-el-minimo` 1039/3115 (33.4%) se mantiene cuarto. Sigue sin
  causa dominante única y clara, pero `killzone-Asia-largo` pierde peso
  relativo por primera vez en varios días — vigilar si es tendencia o
  ruido. El SL estructural (arriba) sigue siendo el candidato que mejor
  ataca `RR-bajo` de las cuatro.

### Cruce con Session Analyst
Bajo veredicto SA `WAIT` el E[R] **vuelve a ser claramente la mejor
rama**: **+0.124** (n=1524, +173), por delante de `GO` **+0.078**
(n=446, +80, baja de +0.12); `AVOID` **vuelve a terreno positivo**:
**+0.015** (n=644, +61, venía de -0.019 ayer). **El giro de ayer no se
sostuvo**: el orden "WAIT mejor, GO peor" — el patrón histórico de este
playbook — se reafirma hoy; la lectura de ayer (GO acercándose a WAIT,
AVOID cruzando a negativo) queda confirmada como ruido de un día, tal
como se advirtió ("vigilar 1-2 corridas más antes de dar el giro por
asentado"). **A nivel global (todo kind/side)**: la hipótesis original
de `agent-instructions.md` era "AVOID rinde peor" — sigue SIN
confirmarse con significancia (`by_verdict_ci90` AVOID E[R]=0.013
CI90=[-0.049,0.073] p=0.356, cruza cero, n=1166); pero **WAIT y GO
siguen certificando ambos con significancia**: WAIT (E[R]=0.078
CI90=[0.041,0.119] p=0.001, n=2447) y GO (E[R]=0.125 CI90=[0.046,0.202]
p=0.004, n=611) — segunda corrida seguida con los dos certificando, ver
`report.alerts`. Esa lectura global sigue escondiendo la asimetría por
lado: en LONG (esta tabla) WAIT es claramente la mejor rama; en **SELL
RETEST el orden histórico es GO mejor, WAIT peor** (ver
`sell-retest.md`). No generalizar la hipótesis sin mirar el desglose por
side.

### Decaimiento
`decay_weekly` (global, no por segmento): 2026-W36 n=3121 WR 44.7%
E[R]=**-0.019** (bajó de n=3183 por -62, la caída agregada más grande
vista hasta ahora en esta semana — mismo mecanismo de dedup, sin
evidencia de pérdida real de archivo, ver Nota de proceso); 2026-W37
n=5315 WR 46.8% E[R]=**0.071** (bajó de n=5389 por -74, también la caída
más grande vista hasta ahora — vigilar que el mecanismo de dedup no se
esté acelerando); 2026-W38 n=3016 (subió fuerte de 2211) WR 45.1%
E[R]=**0.081** — semana en curso, todavía sin cerrar. Por segmento
(`decay_weekly_by_segment`), 5m/RETEST/LONG: W36 n=242 (bajó 1 par)
E[R]=0.082 PF=**1.18** (el PF que hoy frena el gate de ejecución, ver
Veredicto global); W37 n=234 (bajó 1 par, tercera corrida seguida
perdiendo muestra en este segmento) E[R]=0.208 PF=**1.47** (sube de
1.45, ya por encima del umbral 1.3); W38 n=217 (subió fuerte de 144) WR
48.8% E[R]=0.188 PF=1.44 (semana en curso, normal que se mueva al sumar
muestra, no es señal de decaimiento). Sin señal de decaimiento real (no
hay caída de WR > 15 pts en una semana ya cerrada) en ningún TF de este
playbook.

## Histórico de cambios
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
