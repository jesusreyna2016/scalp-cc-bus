# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-28 (lunes) · n: 6924)

### Nota de proceso
`git pull` con "forced update" habitual en `origin/main", sin pérdida
(ver `buy-retest.md` para el detalle). Primer día hábil con trades
reales — resuelve la duda que quedó pendiente el fin de semana: la
debilidad del viernes en los tres TF SHORT (1m con CI90 cruzando cero
por primera vez) **se recuperó** con dato nuevo genuino, no era el
inicio de un decaimiento (ver Veredicto global).

### Veredicto global
1m n=4393 (+32) WR 44.2% E[R]=**0.034** PF=1.07; 2m n=1866 (+1) WR 48.3%
E[R]=**0.063** PF=1.13; 5m n=673 (+2) WR 47.4% E[R]=**0.086** PF=1.18.
`segment_significance`: **1m CI90=[0.004,0.066] p=0.032 n=4134 —
RECUPERA el criterio completo hoy** (ayer cruzaba cero por primera vez
en este playbook, CI90=[-0.001,0.062]); 2m CI90=[0.018,0.109] p=0.013
n=1790 (sin cambio real); 5m CI90=[0.005,0.165] p=0.043 n=622 (sin
cambio real). Los tres vuelven a `survives_fdr10=true` con CI90 fuera de
cero — la lectura de ayer era ruido de fin de semana con dato viejo, no
un cambio de régimen.
**⚠ Ver el hallazgo del día en "Gestión"**: primer chequeo real
antes/después del SL estructural (aplicado el sábado) y el resultado por
segmento es contradictorio — 1m SHORT sale sobre-reaccionando al alza,
no hay que leerlo como confirmación todavía.

### Reglas condicionales (IF contexto ENTONCES acción)

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tf=1m` (`survives_fdr10=true`) | TOMAR, edge real fuera de ruido — recupera el criterio completo hoy | 4134 (+32) | E[R]=**0.034** CI90=[0.004,0.066] | alta, vuelve tras el susto de ayer |
| 2 | `tf=2m` (`survives_fdr10=true`) | TOMAR, edge real fuera de ruido | 1790 (+1) | E[R]=**0.063** CI90=[0.018,0.109] | alta, sin cambio real |
| 3 | `tf=5m` (`survives_fdr10=true`) | TOMAR, edge real fuera de ruido | 622 (+2) | E[R]=**0.086** CI90=[0.005,0.165] | moderada, sin cambio real |
| 4 | `tier=A+` | sigue en zona alta | 452 (+6) | WR 25.4%, E[R]=**0.131** PF=1.2 | moderada |
| 5 | `tier=B` | sigue casi plano | 2952 (+9) | WR 46.1% E[R]=**-0.002** PF=1.0 | baja — sigue por debajo de A+ y C |
| 6 | símbolo (`cross_instrument`), 1m/2m/5m | los tres siguen `universal` | — | sin spread reportado hoy | moderada — sin cambio de veredicto |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara.

### Gestión
- **La escalera + parciales (`managed_vs_naive`)**: 1m n=4127
  delta=**+0.128**; 2m n=1790 delta=**+0.084**; 5m n=621 delta=**+0.019**
  — sin cambios de fondo, sigue ayudando en los tres TF.
- **SL estructural (`sl_origin_vs_layer`, medición paralela)**: 1m
  n=3498 delta=**+0.147** CI90=[0.08,0.22]; 2m n=1572 delta=**+0.152**
  CI90=[0.065,0.25]; 5m n=577 delta=**+0.362** CI90=[0.103,0.649] — sigue
  siendo el efecto más grande del experimento, sin cambio real.
- **⚠ HALLAZGO DEL DÍA (ver detalle completo en `buy-retest.md` →
  Gestión y en `experiments.json`)**: se arregló un bug en `analyze.py`
  que dejaba sin medición antes/después para siempre a los experimentos
  `applied` (sólo evaluaba `running`/`proposed`). Con el fix corrido hoy,
  el `prediction_scoreboard` por segmento da el primer resultado real del
  SL nuevo: **1m SHORT (n=33) sale con `realDeltaER=+0.567`, más de 4x lo
  predicho (+0.143)** — a favor en dirección, pero la magnitud es
  sospechosamente grande para n=33 en un solo día (mismo patrón que este
  experimento ya documentó: lecturas con n bajo sobrestiman el efecto).
  En paralelo, **1m LONG (n=37) salió en dirección CONTRARIA** a lo
  predicho (ver `buy-retest.md`) — el panorama agregado (`verdict`
  mecánico `confirmed`, n=89) no es confiable todavía con estos tamaños
  de muestra. NO se sube el estado a `confirmed`, se sigue vigilando
  día a día por segmento.
- **Modo sombra**: sin cambios de fondo para los 3 TF SHORT (ya estaban
  en v1 y v2). Racha de 3 semanas cerradas (W37-W39) intacta — ver
  `buy-retest.md` para el detalle completo.

### Contextos a evitar
- Autopsia de SL sobre las 3146 pérdidas SHORT: `RR-bajo` 1147/3146
  (36.5%), `stop-en-el-minimo` 1046/3146 (33.3%), `contra-estructura`
  1022/3146 (32.5%) — sin cambio de fondo. El SL estructural (arriba)
  sigue siendo el único ataque real a esta causa en SELL RETEST, pero su
  primer día de medición real es demasiado ruidoso para darlo por
  confirmado (ver Gestión).

### Cruce con Session Analyst
`AVOID` n=566 E[R]=**+0.044** PF=1.08; `GO` n=326 E[R]=**+0.223** (la
mejor rama por lejos) PF=1.57; `WAIT` n=1979 E[R]=**-0.018** PF=0.96 —
sin cambio real frente a ayer. El orden "GO mejor, WAIT peor" se
mantiene — patrón **opuesto** al de `buy-retest.md`, sigue sin
generalizarse la hipótesis AVOID-rinde-peor sin mirar el desglose por
side.

### Decaimiento
`decay_weekly` (global, no por segmento, ver `buy-retest.md`). Por
segmento (`decay_weekly_by_segment`): **1m/RETEST/SHORT** — la reversión
de signo semanal que cerró 2026-W39 se revisa levemente al alza con el
dedup de siempre (n=1361, E[R]=**-0.005**, prácticamente en cero en vez
de claramente negativo como se leyó ayer, PF=0.99) — sigue siendo la
primera semana no-positiva de este segmento desde que existe el bus,
pero menos marcada de lo que parecía; **2m/RETEST/SHORT** W39 E[R]=0.033
PF=1.07 (sin cambio de fondo); **5m/RETEST/SHORT** W39 E[R]=0.059
PF=1.12 (sin cambio de fondo, primer par de 2026-W40 ya registrado hoy,
n=1, no leer todavía). Sin caída de WR > 15pts en ningún TF. Vigilar el
cierre de 2026-W40 antes de tratar la semana floja de 1m SHORT como algo
más que ruido.

## Histórico de cambios
- 2026-09-28 (lunes): primer día hábil con dato nuevo genuino — la
  debilidad del viernes en los tres TF SHORT (1m con CI90 cruzando cero
  por primera vez) se recupera del todo, era ruido de fin de semana con
  dato viejo, no un cambio de régimen. **Bug encontrado y arreglado en
  `analyze.py`** (mismo fix que `buy-retest.md`): `eval_experiments()`
  nunca evaluaba experimentos `applied`. Primer resultado real
  antes/después del SL estructural (aplicado el sábado): **1m SHORT
  (n=33) sale con `realDeltaER=+0.567`, 4x lo predicho** — a favor en
  dirección pero con una magnitud demasiado grande para confiar con
  n=33 en un solo día, mientras 1m LONG (ver `buy-retest.md`) salió en
  dirección contraria el mismo día — el verdict agregado `confirmed` no
  se toma como definitivo todavía, se sigue vigilando por segmento.
  1m/RETEST/SHORT revisa levemente al alza su E[R] de 2026-W39 (dedup
  habitual, de -0.021 a -0.005, sigue siendo la primera semana no
  positiva del segmento pero menos marcada). Resto sin cambios de fondo.
- 2026-09-27 (domingo, REVISIÓN SEMANAL): `git pull` limpio. Fin de
  semana sin sesión CME nueva (n 6896→6897, +1). Tres decisiones de la
  revisión semanal (detalle en `reviews/2026-week-39.md`): (1) **el SL
  estructural se aplicó ayer en TradingView**, incluidos los 3 TF SHORT
  de este playbook — deja de ser propuesta; (2) **mejora permanente
  `rr1_threshold_cut_oos`**: hallazgo específico de este playbook, **2m
  SHORT se revierte fuera de muestra** (el patrón in-sample de 3+
  lecturas consistentes no sobrevive el test set aislado — el corte de
  `rr1` da E[R] negativo en las 4 lecturas), se retira como candidato de
  `sc_min_rr`; 1m SHORT queda direccionalmente a favor pero sin
  certificar (CI90 cruza cero, falta potencia); (3) `SHADOW_RULES_V1`
  actualizado a v2 (sin cambio para los TF SHORT, ya estaban incluidos en
  v1). Hallazgo de decaimiento: **1m/RETEST/SHORT cerró su primera semana
  con E[R] negativo desde que existe el bus** (W39: E[R]=-0.021, PF=0.96)
  sin caída de WR correspondiente — primera reversión de signo semanal de
  un segmento RETEST certificado en todo el bus, vigilar el cierre de
  2026-W40. La debilidad de los tres TF SHORT notada ayer sigue sin
  poder confirmarse ni descartarse por falta de dato nuevo (fin de
  semana) — el chequeo real llega mañana lunes, junto con los primeros
  trades con el SL nuevo ya aplicado.
- 2026-09-26 (sábado): **hallazgo principal del playbook**: los tres TF
  de SELL RETEST se debilitaron a la vez con el dato completo de
  2026-09-25 — 1m SHORT es el más afectado: su CI90 de E[R] cruza cero
  por primera vez ([-0.001,0.062]) aunque el flag `survives_fdr10` siga
  en `true`; por la regla compuesta de `agent-instructions.md` (FDR Y
  CI90 fuera de cero) esto significa que 1m SHORT deja de tratarse como
  certificado hoy, primera vez que pasa en este playbook. 2m y 5m SHORT
  también se debilitan (límites inferiores del CI90 bajan bastante) pero
  siguen sosteniendo el criterio completo. Sin indicio de problema de
  pipeline (`orphan_outcomes` estable 36→37) — se lee como una sesión de
  viernes floja para SHORT, no un cambio de régimen, pero se marca para
  vigilar la próxima corrida antes de decidir. La gestión con escalera
  (`managed_vs_naive`) y el SL estructural (`sl_origin_vs_layer`) NO
  comparten la debilidad — ambos siguen intactos o mejor que ayer en los
  tres TF, lo cual sugiere que el movimiento es del E[R] crudo/gestión
  ingenua, no de la señal en sí. `WAIT` en el cruce con Session Analyst
  volvió a terreno negativo (tercer vaivén en pocos días) — tratarlo
  como ruidoso, no como tendencia. Mismo incidente de repo que
  `buy-retest.md` (merge en vez de reset, ver ahí el detalle). Sin
  cambios en la propuesta de SL estructural ni en el gate de ejecución.
  Pendiente para la revisión semanal de MAÑANA domingo 2026-09-27: el
  criterio desactualizado del modo sombra Y ahora también confirmar si
  la debilidad de hoy en 1m/2m/5m SHORT persiste con el dato del fin de
  semana/lunes antes de tratarla como algo más que ruido de un día.
- 2026-09-25 (viernes): `git pull` con "forced update" habitual en
  `origin/main` (shallow clone, sin pérdida). Dato nuevo parejo
  (+302/+149/+45 en 1m/2m/5m). **5m SHORT suma su TERCERA lectura
  seguida con CI90 fuera de cero** (deja de tratarse como frágil, dos
  confirmaciones independientes desde el 09-23). 2m SHORT se fortalece
  bastante en `segment_significance` (límite inferior del CI90
  0.023→0.038) y en el SL estructural (delta 0.138→0.16, tercer día
  seguido sosteniendo su graduación del 09-23). El cruce con Session
  Analyst tiene un movimiento a vigilar: `WAIT` cruza a E[R] positivo
  (+0.013) por primera vez en varias corridas, aunque sigue muy por
  debajo de `GO` (+0.24) — no cambia el orden "GO mejor, WAIT peor" de
  este playbook. Sin cambios en la propuesta de SL estructural (6
  segmentos RETEST, sigue `proposed` sin `changeDate`) ni en el gate de
  ejecución (sigue en asesoría). El criterio del modo sombra que excluye
  `2m LONG`/`5m SHORT` sigue con la justificación desactualizada
  anotada ayer — pendiente para el domingo 2026-09-27.
- 2026-09-24 (jueves): dato nuevo parejo (+252/+109/+35 en 1m/2m/5m).
  Día de confirmación: los tres TF siguen certificando FDR sin
  reversiones, **5m SHORT suma su segunda lectura seguida con CI90
  fuera de cero** (deja de ser el hallazgo de un solo día del 09-23).
  El SL estructural se mantiene sólido en los tres TF, sin cambios en
  la propuesta de 6 segmentos. Hallazgo de método (ver detalle en
  `buy-retest.md`): el criterio del modo sombra que excluye a `2m LONG`
  y `5m SHORT` de la lista de segmentos elegibles quedó desactualizado
  frente a `segment_significance` de hoy — anotado para revisar en la
  revisión semanal del domingo 2026-09-27, no se cambia hoy. Autopsia
  de SL y cruce con Session Analyst sin cambios de orden. Sin cambios
  en el gate de ejecución (el segmento objetivo sigue siendo
  5m/RETEST/LONG, ver `buy-retest.md`).
- 2026-09-23 (miércoles): dato nuevo parejo (+228/+93/+43 en
  1m/2m/5m). **Hallazgo principal del playbook: `5m/RETEST/SHORT` deja
  de estar "al filo" y certifica de verdad** — el límite inferior del
  CI90 de E[R] cruza por encima de cero por primera vez (-0.001→0.012),
  cumpliendo el criterio compuesto completo (`survives_fdr10=true` Y
  CI90 que no cruza 0) que hasta ayer le faltaba. Tratar como lectura
  nueva y frágil (una sola confirmación) antes de generalizarla igual
  que 1m/2m. **Segundo hallazgo: el SL estructural en 2m SHORT también
  certifica con margen claro por primera vez** (CI90 límite inferior
  0.057→0.051 pero el delta se sostiene muy por encima del umbral de
  graduación) — se gradúa a la propuesta formal de `experiments.json`,
  que pasa de 5 a 6 segmentos junto con `buy-retest.md`. Con esto, los
  tres TF de SELL RETEST certifican FDR con CI90 fuera de cero
  simultáneamente por primera vez en este playbook. Autopsia de SL y
  cruce con Session Analyst sin cambios de orden. Sin cambios en el gate
  de ejecución (el segmento objetivo sigue siendo 5m/RETEST/LONG, ver
  `buy-retest.md`).
- 2026-09-23 (miércoles): dato nuevo parejo (+228/+93/+43 en
  1m/2m/5m). **Hallazgo principal del playbook: `5m/RETEST/SHORT` deja
  de estar "al filo" y certifica de verdad** — el límite inferior del
  CI90 de E[R] cruza por encima de cero por primera vez (-0.001→0.012),
  cumpliendo el criterio compuesto completo (`survives_fdr10=true` Y
  CI90 que no cruza 0) que hasta ayer le faltaba. Tratar como lectura
  nueva y frágil (una sola confirmación) antes de generalizarla igual
  que 1m/2m. **Segundo hallazgo: el SL estructural en 2m SHORT también
  certifica con margen claro por primera vez** (CI90 límite inferior
  0.057→0.051 pero el delta se sostiene muy por encima del umbral de
  graduación) — se gradúa a la propuesta formal de `experiments.json`,
  que pasa de 5 a 6 segmentos junto con `buy-retest.md`. Con esto, los
  tres TF de SELL RETEST certifican FDR con CI90 fuera de cero
  simultáneamente por primera vez en este playbook. Autopsia de SL y
  cruce con Session Analyst sin cambios de orden. Sin cambios en el gate
  de ejecución (el segmento objetivo sigue siendo 5m/RETEST/LONG, ver
  `buy-retest.md`).
- 2026-09-22 (martes): salto de dato grande y genuino (+1027 outcomes en
  todo el bus; +192/+74/+17 en 1m/2m/5m de este playbook). 1m y 2m
  siguen certificando FDR sin cambios de fondo (octava/undécima lectura).
  **5m marca `survives_fdr10=true` por primera vez pero con CI90 que
  todavía toca cero por abajo (-0.001)** — no se trata como certificación
  real hasta que el límite inferior quede claramente por encima de cero.
  El SL estructural en 2m SHORT tiene su mejor lectura hasta ahora
  (límite inferior del CI90 0.04→0.057) pero sigue sin alcanzar el
  umbral de graduación que ya cruzaron 1m LONG/SHORT, 2m LONG y 5m
  LONG/SHORT. Sin cambios en la propuesta formal de `experiments.json`.
- 2026-09-21 (lunes, primer día hábil con dato nuevo genuino tras el fin
  de semana, +10 pares en este playbook — volumen SHORT bajo hoy frente
  a LONG): mismo incidente de repo inofensivo de siempre. 1m suma su
  séptima lectura FDR seguida (n=2949, CI90=[0.021,0.098]) y 2m su
- 2026-09-22 (martes): salto de dato grande y genuino (+1027 outcomes en
  todo el bus; +192/+74/+17 en 1m/2m/5m de este playbook). 1m y 2m
  siguen certificando FDR sin cambios de fondo (octava/undécima lectura).
  **5m marca `survives_fdr10=true` por primera vez pero con CI90 que
  todavía toca cero por abajo (-0.001)** — no se trata como certificación
  real hasta que el límite inferior quede claramente por encima de cero.
  El SL estructural en 2m SHORT tiene su mejor lectura hasta ahora
  (límite inferior del CI90 0.04→0.057) pero sigue sin alcanzar el
  umbral de graduación que ya cruzaron 1m LONG/SHORT, 2m LONG y 5m
  LONG/SHORT. Sin cambios en la propuesta formal de `experiments.json`.
- 2026-09-21 (lunes, primer día hábil con dato nuevo genuino tras el fin
  de semana, +10 pares en este playbook — volumen SHORT bajo hoy frente
  a LONG): mismo incidente de repo inofensivo de siempre. 1m suma su
  séptima lectura FDR seguida (n=2949, CI90=[0.021,0.098]) y 2m su
  décima (n=1277, CI90=[0.016,0.128]), ambos sin sobresaltos. El SL
  estructural en los tres TF SHORT se mantiene sin reversión pero sin
  ningún ascenso de estado: **2m SHORT sigue sin alcanzar el umbral
  para promoverse** (delta 0.134, CI90 límite inferior prácticamente
  igual, 0.039→0.04) — a diferencia de **2m LONG, que sí se graduó hoy a
  candidato de la propuesta formal tras su tercera lectura consecutiva**
  (ver `buy-retest.md`); la asimetría LONG/SHORT en este experimento se
  mantiene. El patrón "CL se diluye en 1m SHORT" sigue mejorando cuarto
  día seguido (E[R] -0.517→-0.122→-0.029). Autopsia de SL y cruce con
  Session Analyst sin cambios de orden. Modo sombra suma su segundo día
  seguido batiendo al indicador crudo. Sin cambios de estado en el gate
  de ejecución ni en el experimento de SL (`proposed`, sin
  `changeDate`).
- 2026-09-20 (domingo, REVISIÓN SEMANAL, cierre de 2026-W38): primer fin
  de semana sin ningún archivo `signals/outcomes` nuevo (ver
  `buy-retest.md` para el detalle) — los +15 pares de este playbook son
  TIMEOUT forzado, sin trade real nuevo. Todas las métricas de outcome
  real quedan idénticas a ayer. Mejora permanente en `analyze.py`:
  primer borrador de `shadow_rules` (ver `buy-retest.md` y
  `reviews/2026-week-38.md`), que incluye los dos segmentos SHORT de
  este playbook que certifican FDR (1m y 2m). Revisión semanal completa
  de 2026-W38 en `reviews/2026-week-38.md`: sin cambios de dirección en
  ninguna regla condicional de este playbook.
- 2026-09-19 (sábado): mismo patrón de "forced update" en `origin/main`
  (verificado sin pérdida). Salto de dato grande (n 4498→4937, +439; el
  bus asentó de una vez los archivos de 2026-09-18). **Hallazgo más
  importante: el patrón "CL rinde mal en SELL RETEST 1m" que se venía
  endureciendo desde el 09-11 queda revertido** — con n casi
  cuatriplicado (96→271) el efecto se diluyó del todo (E[R]
  -0.517→-0.122) y `cross_instrument` pasa de `instrument-specific` a
  `universal` por primera vez; se retira la regla condicional candidata
  "evitar CL en 1m SHORT". El SL estructural en 2m SHORT tiene su mejor
  lectura hasta ahora (CI90 límite inferior 0.031→0.039) pero se
  mantiene un día más antes de promoverlo. 1m y 2m siguen certificando
  FDR sin sobresaltos (quinta y octava lectura seguida). En el cruce con
  Session Analyst, `WAIT` cruza a E[R] negativo por primera vez
  (+0.021→-0.009) — el patrón "GO mejor, WAIT peor" de SELL RETEST se
  acentúa, en contraste directo con `buy-retest.md` donde `WAIT` sigue
  siendo la mejor rama. Sin cambios de estado en el experimento de SL
  (`proposed`, sin `changeDate`).
- 2026-09-18 (viernes): mismo incidente de repo que `buy-retest.md`
  (`origin/main` reescrito río arriba, verificado sin pérdida). n
  4294→4498 (+204; 1m+109, 2m+49, 5m+46). **1m suma su cuarta
  confirmación FDR seguida** y 2m su séptima; 5m retrocede un paso en
  vez de acercarse a certificar (CI90 límite inferior -0.009→-0.013). El
  SL estructural sube en los tres TF: 1m a su undécima confirmación
  (delta 0.143→0.155), 2m a su mejor lectura hasta ahora (límite
  inferior del CI90 0.012→0.031, sigue sin promoverse) y 5m estable como
  el efecto más grande. **Hallazgo del día**: el patrón "CL rinde mal en
  SELL RETEST" se confirma con más fuerza en 1m (n casi se duplica,
  E[R] empeora a -0.517) pero se diluye en 2m/5m al crecer la muestra
  (ambos pasan a verdict `universal`) — la regla condicional candidata
  debe restringirse a 1m, no generalizarse a los tres TF como se venía
  sugiriendo. En el cruce con Session Analyst, `WAIT` retrocede de
  +0.038 a +0.021 mientras en `buy-retest.md` su rama `WAIT` vuelve a
  ser claramente la mejor — el patrón opuesto entre LONG y SHORT se
  reafirma tras el acercamiento pasajero de ayer. Sin cambios de estado
  en el experimento de SL (`proposed`, sin `changeDate`).
- 2026-09-17 (jueves): mismo incidente inofensivo de repo que
  `buy-retest.md` (HEAD detached, resuelto sin pérdida). Salto de dato
  grande (n 4022→4294, +272). **1m/RETEST/SHORT suma su TERCERA
  confirmación FDR seguida** y 2m su SEXTA; 5m mejora y se acerca a
  certificar por primera vez (CI90 límite inferior -0.033→-0.009). El SL
  estructural en 1m sube a su décima confirmación (delta 0.127→0.143).
  **Hallazgo del día**: la rama `WAIT` del cruce con Session Analyst
  cruza a E[R] positivo por primera vez (-0.023→+0.038, con +207 pares
  nuevos) — el patrón "GO mejor, WAIT peor" de SELL RETEST se mantiene en
  orden relativo pero se modera en términos absolutos, en paralelo a que
  `buy-retest.md` reporta hoy que su rama `AVOID` cruza a negativo por
  primera vez. A nivel global, `GO` certifica con significancia por
  primera vez junto a `WAIT` (ver `report.alerts` y `buy-retest.md`).
  `nearEdge=1` deja de estar congelado y sube fuerte con 6 señales
  nuevas. Sin cambios de estado en el experimento de SL (`proposed`, sin
  `changeDate`).
- 2026-09-16 (miércoles): "forced update" habitual de `origin/main`
  (shallow clone, sin pérdida). Dato nuevo moderado (n 3889→4022, +133).
  **1m/RETEST/SHORT sostiene `survives_fdr10=true` por SEGUNDO día
  seguido** — primera confirmación independiente de la certificación
  fresca de ayer; 2m suma su quinto día seguido certificando. El SL
  estructural en 2m SHORT sostiene su certificación "al filo" por segundo
  día (delta 0.117, límite inferior 0.011) sin fortalecerse todavía.
  Curiosidad de dato: CL tuvo CERO trades nuevos hoy en los tres TF de
  este playbook (cifras de `cross_instrument` idénticas a ayer) —
  probablemente solo ausencia de señales ese día, no un problema de
  pipeline (otros símbolos sí crecieron). Nada más accionable nuevo: día
  de confirmación, sin sorpresas de signo en ninguna métrica.
- 2026-09-15 (martes): otro "forced update" de `origin/main` al inicio
  (mismo patrón inofensivo de otras corridas). Salto de dato grande y
  genuino (n 3484→3889, +405). **Hallazgo más accionable del bus hoy:
  1m/RETEST/SHORT certifica `survives_fdr10=true` por primera vez**
  (CI90=[0.014,0.101]), a la vez que 2m sostiene su cuarta certificación
  seguida — primera vez que dos TF de este playbook certifican FDR
  simultáneamente. El SL estructural en 2m SHORT certifica por primera
  vez también (CI90=[0.014,0.223]) pero al filo, se trata como candidato
  débil, no se suma a la propuesta formal todavía. Nuevo patrón
  documentado: CL rinde mal en SELL RETEST en 1m, 2m y 5m a la vez
  (candidato a regla condicional cuando crezca la muestra en 2m/5m). Se
  confirma que el cruce con Session Analyst en SHORT es opuesto al de
  LONG (GO mejor, WAIT peor) — ver nota global en `buy-retest.md`.
- 2026-09-14 (lunes): `git pull` limpio. Salto de muestra chico (n
  3419→3484, +65), como en `buy-retest.md`. **`2m/RETEST/SHORT` sostiene
  `survives_fdr10=true` por TERCER día seguido** — sigue siendo la
  certificación FDR más duradera del bus. El SL estructural en 1m y 5m
  SHORT (propuestos ayer en la revisión semanal) se mantienen estables
  sin retroceso. Único movimiento de dato nuevo relevante del día: el
  cruce con Session Analyst en la rama `GO` de este segmento creció de
  n=76 a n=101 (+25) con E[R] subiendo de +0.193 a +0.304 — es el único
  lugar del cruce SA↔scalp de todo el bus (LONG y SHORT) que recibió
  señales nuevas hoy.

- 2026-09-13 (domingo, REVISIÓN SEMANAL): n 3227→3419 (+192; 1m+125,
  2m+53, 5m+14). Incidente menor de repo, ver `buy-retest.md`.
  **2m/RETEST/SHORT sostiene `survives_fdr10=true` por segundo día
  seguido** (CI90=[0.037,0.173]) — sigue siendo el segmento SHORT más
  confiable del bus. 1m pierde el "casi certifica" de ayer (CI90 vuelve a
  cruzar cero, [-0.008,0.087]). El SL estructural en 1m SHORT mejora de
  nuevo (delta 0.139→0.143, límite inferior del CI90 sube a 0.037) y se
  incluye en la propuesta formal de la revisión semanal de hoy (junto a
  1m LONG y 5m LONG/SHORT, ver `experiments.json` y
  `reviews/2026-week-37.md`); 2m SHORT queda fuera. `nearEdge=-1` deja de
  cambiar de signo por primera vez en 7 corridas. La autopsia de SL
  mantiene el mismo orden de causas por primera vez en varios días
  (RR-bajo > stop-en-el-mínimo > contra-estructura).
- 2026-09-12 (sábado, última corrida antes de la revisión semanal de
  mañana): n 2717→3227 (+510; 1m+337, 2m+119, 5m+54), sin incidentes de
  repo. **Hallazgo más accionable del bus hoy**: `segment_significance`
  de **2m/RETEST/SHORT certifica con `survives_fdr10=true`** por primera
  vez (CI90=[0.04,0.18], n=893) — segundo segmento de todo el dataset en
  lograrlo y el primero con muestra grande y usable (el otro, 5m/INV/LONG,
  tiene n=10). 1m queda al borde (CI90=[0.001,0.095], no cruza cero mas
  no sobrevive FDR). `sl_origin_vs_layer` en 1m SHORT deja de estar "al
  filo" (límite inferior del CI90 sube de 0.003 a 0.022); `tier=B` se da
  vuelta a positivo por primera vez en varios días. El cruce con Session
  Analyst (GO mejor, AVOID negativo) se sostiene por segundo día seguido
  sin revertirse — primera vez que no cambia de dirección de una corrida
  a otra.
- 2026-09-11 (viernes): n 2100→2717 (+617; 1m+389, 2m+177, 5m+51). Mismo
  incidente de repo que `buy-retest.md` (historia de `origin/main`
  reescrita, resuelto sin pérdida de datos). **`sl_origin_vs_layer` en 2m
  SHORT pierde la certificación "al filo" de ayer** (CI90 vuelve a cruzar
  cero) mientras 1m SHORT queda a un paso de perderla también (límite
  inferior baja a 0.003); 5m SHORT sigue siendo la lectura más sólida. El
  hallazgo más fuerte del bus de ayer (`AVOID` mejor que `GO` en Session
  Analyst) **se revierte casi por completo** en este segmento: `GO` pasa
  de E[R]=-0.221 a +0.193 y `AVOID` de +0.067 a -0.034 — la relación
  SA↔resultado-scalp queda oficialmente marcada como inestable, no como
  regla explotable (ver Cruce con Session Analyst arriba). `nearEdge=-1`
  cambia de signo por tercera vez en 5 corridas.
- 2026-09-11 (viernes): n 2100→2717 (+617; 1m+389, 2m+177, 5m+51). Mismo
  incidente de repo que `buy-retest.md` (historia de `origin/main`
  reescrita, resuelto sin pérdida de datos). **`sl_origin_vs_layer` en 2m
  SHORT pierde la certificación "al filo" de ayer** (CI90 vuelve a cruzar
  cero) mientras 1m SHORT queda a un paso de perderla también (límite
  inferior baja a 0.003); 5m SHORT sigue siendo la lectura más sólida. El
  hallazgo más fuerte del bus de ayer (`AVOID` mejor que `GO` en Session
  Analyst) **se revierte casi por completo** en este segmento: `GO` pasa
  de E[R]=-0.221 a +0.193 y `AVOID` de +0.067 a -0.034 — la relación
  SA↔resultado-scalp queda oficialmente marcada como inestable, no como
  regla explotable (ver Cruce con Session Analyst arriba). `nearEdge=-1`
  cambia de signo por tercera vez en 5 corridas.
- 2026-09-10 (jueves): salto grande de dato nuevo (+732, n 1368→2100).
  **Reversión de signo simultánea en casi todos los cortes**: los tres TF
  crudos pasaron de negativo a positivo; el gradiente de `nearEdge` que
  llevaba 4 revisiones estable se invirtió por completo (`edge=0` pasó de
  "peor rama, filtrar" a "mejor rama"); `tier=A+` se dio vuelta de
  E[R]≈0 a +0.185. Tratado explícitamente como volatilidad de muestra
  nueva, no como veredicto nuevo — vigilar 1-2 corridas más. En paralelo,
  el SL estructural (`sl_origin_vs_layer`) siguió certificando en los tres
  TF pero con deltas más chicos (2m quedó "al filo" con CI90 límite
  inferior 0.001). El cruce con Session Analyst (AVOID>GO) se mantiene
  fuerte por tercer día y ahora sale en `report.alerts` — candidato a
  formalizar en la revisión semanal del domingo si se sostiene; notable
  que la celda `GO` global quedó con cifras IDÉNTICAS a ayer (cero señales
  nuevas bajo GO en todo el bus pese al salto de +1203 pares totales).
- 2026-09-01: primera escritura con datos reales (n=3, todas GC 1m SHORT
  mismo día, 3/3 SL). Marcado explícitamente como no accionable por tamaño
  de muestra; se deja constancia de la posible correlación con el veredicto
  del Session Analyst para verificar cuando crezca la muestra.
- 2026-09-01 (tarde): refresco a n=5 (WR sube de 0% a 20%, sigue siendo el
  peor segmento). Coincide con el corte `aligned=1` — anotado como posible
  confusión de variables, a revisar cuando la muestra crezca. Hipótesis de
  cruce con Session Analyst se mantiene, sigue sin ser cuantificable.
- 2026-09-02: salto grande de muestra, n=5→123 (85× 1m, 28× 2m, 10× 5m).
  El segmento crudo por TF sigue sin significancia (`survives_fdr10=false`
  en los tres), pero aparece el primer hallazgo accionable real: el corte
  `nearEdge=1` vs `nearEdge=0` separa un E[R]=+0.326 (n=49) de un
  E[R]=-0.158 (n=61) — candidato fuerte para la revisión semanal si se
  sostiene 1-2 semanas más. `tier B` vs `tier C` muestra el mismo patrón
  (probable solape con `nearEdge`, sin confirmar independencia). Autopsia
  de SL: `RR-bajo` y `stop-en-el-minimo` empatados 22/44 como causa
  dominante — ninguna mitigada aún. Se descarta generalizar por símbolo:
  `cross_instrument` marca 1m y 2m como `instrument-specific`. Fix de bug
  en `analyze.py` (`news_context` crasheaba leyendo `market.json` del
  Session Analyst) aplicado hoy, sin impacto en estas métricas.
- 2026-09-02 (corrida formal del agente): salto de muestra n=123→222 (151×
  1m, 53× 2m, 18× 5m). **El 5m certifica por primera vez**
  (`survives_fdr10=true`, CI90=[0.372,1.0], WR 88.9%, E[R]=0.687, PF=7.19,
  n=18) — primer segmento del dataset con confianza estadística real,
  veredicto TOMAR. Se detecta y documenta una **anomalía fuerte**:
  `tier=A+` es el peor resultado del dataset (n=16, WR 6.2%, E[R]=-0.743,
  PF=0.21), aparentemente invertido — selecciona `rr1` alto y
  `nearEdge=-1`, ambos con signo negativo para P(TP1) según el modelo. Se
  recomienda a Jesús auditar la fórmula de tier A+ en Pine; no se propone
  cambio todavía (n<20). `managed_vs_naive` en 2m/SELL pasa a negativo por
  primera vez (delta -0.015, n=53) — vigilar. Autopsia de SL recalculada
  sin el cap de 60 filas que trunca `report.md` (RR-bajo y
  stop-en-el-mínimo empatados 40/94, estable vs revisión previa). Mejora
  permanente en `analyze.py`: se agregan los cortes cruzados
  `by_kindside_edge`/`by_kindside_tier`/`by_kindside_aligned` (pedido
  explícito de la nota anterior) — ya no se aproximan a mano. Además, se
  encontró y corrigió *de nuevo* el bug de `news_context` (el fix de la
  entrada anterior se había perdido: el histórico de git muestra que un
  `git pull` con "forced update" sobre `origin/main` reescribió la rama y
  un commit posterior reintrodujo el código viejo sin querer). Recordatorio
  para corridas futuras: no forzar push sobre `main`; si `git pull` reporta
  "forced update", revisar con cuidado que no se haya perdido trabajo antes
  de continuar.
- 2026-09-04: refresco n=589→687 (1m 356→412, 2m 165→191, 5m 68→84). El
  5m sigue perdiendo E[R] por tercera lectura seguida (0.687→0.088→0.03),
  confirmando que la certificación original (n=18) era varianza de muestra
  chica, no un edge que se está diluyendo con el tiempo. `sl_origin_vs_layer`
  en 1m pierde la certificación que tenía ayer (delta +0.328 CI90 no cruzaba
  cero → hoy delta +0.22 CI90=[-0.056,0.55] sí la cruza) — la propuesta en
  `experiments.json` sigue siendo válida solo para 5m con la muestra de hoy,
  hay que actualizarla antes de la revisión semanal. Primer corte de
  `cross_instrument` en 5m con n suficiente: `instrument-specific`
  (GC muy negativo con n=12, vigilar sin generalizar). Nota de proceso:
  `git pull` volvió a reportar "forced update" sobre `origin/main` al
  inicio de esta corrida — mismo problema recurrente que el 2026-09-02.
  Se verificó que `origin/main` traía todo el trabajo esperado antes de
  resetear la rama local `main` a `origin/main`; sin pérdida de trabajo,
  pero conviene que Jesús revise por qué el bus sigue reescribiendo la
  rama en vez de hacer fast-forward.
- 2026-09-03: salto de muestra fuerte n=222→589 (1m 151→356, 2m 53→165, 5m
  18→68). **El 5m pierde la certificación FDR que tenía** (E[R] 0.687→0.088,
  `survives_fdr10` true→false) — se documenta como lección de método: la
  certificación anterior con n=18 no sobrevivió al crecer la muestra,
  confirma que el piso de n y el FDR están bien calibrados y no hay que
  bajar la guardia con muestras chicas aunque el p-valor parezca bueno. La
  anomalía de `tier=A+` también se corrige: pasó de E[R]=-0.743 (n=16,
  "peor del dataset") a E[R]=+0.04 (n=54, en línea con B/C) — era en buena
  parte ruido de muestra chica; el mismo patrón SÍ persiste con fuerza en
  BUY RETEST (n=13, E[R]=-0.705), que se sigue vigilando por separado. 2m
  se pone negativo en crudo por primera vez (E[R] +0.087→-0.087) pero
  `managed_vs_naive` muestra que la escalera con parciales lo rescata
  (delta +0.111) — se corrige también el dato de la revisión anterior que
  decía que la gestión perdía en 2m (n=53 chico entonces). `cross_instrument`
  confirma `universal` en 1m y 2m — el filtro `nearEdge` generaliza bien
  por símbolo. Mejora permanente en `analyze.py`:
  `sl_post_mortem.causes_by_kind_side` (autopsia de SL por segmento sin cap
  de 60 filas, ya no se recalcula a mano) y corrección del label de alerta
  de `sl_origin_vs_layer` (decía "(2m/5m)" para el basis `retestBar` pero
  el Pine todavía no separa 1m SHORT en `retestBar2`, así que el agregado
  mezclaba los tres TF — el label ahora es neutral y el matiz por TF va en
  la alerta).
- 2026-09-05: **hallazgo de pipeline, no de trading**: se detectó y
  corrigió una pérdida real de datos — el commit `92917b8` había borrado
  1256 de 1280 señales de `signals/2026-09-03.jsonl` bajo el mensaje
  engañoso "heal 24 orphan signal(s)"; restaurado desde `f239309` sin
  pérdida (verificado línea por línea). n saltó de 687 a 772 en SHORT por
  esa restauración, no por señales nuevas. El 5m cruza a negativo por
  primera vez (E[R] 0.687→0.088→0.03→-0.007), confirmando que el "TOMAR"
  original con n=18 era ruido puro. `tier=B` se invirtió
  (E[R]=+0.02→-0.032) al restaurar el día que faltaba — se retira como
  regla activa. `cross_instrument` en 1m volvió de `universal` a
  `instrument-specific` (CL otra vez el peor símbolo). `sl_origin_vs_layer`
  en 1m RECUPERÓ la certificación que había perdido ayer (delta
  +0.22→+0.296, CI90 vuelve a batir cero) — y por primera vez también
  certificó en 1m LONG (ver `buy-retest.md`), así que el experimento
  `sl-retest-wick-2026-09-03` en `experiments.json` se amplió de "solo
  SHORT" a todo RETEST, marcado para confirmar el 2026-09-06 antes de
  tratarlo como asentado. Mejora permanente en `analyze.py`:
  `session_analyst_cross` — primera cuantificación real de la hipótesis
  "AVOID rinde peor" de `agent-instructions.md` (parsea GO/WAIT/AVOID de
  los planes pre-asia/pre-london/pre-ny por símbolo, cruza contra el
  resultado real por fecha+killzone+símbolo). Resultado, con n=885
  agregado de todo kind/side: AVOID rindió MEJOR que GO (E[R] +0.204 vs
  -0.273) — lo opuesto a la hipótesis original. Todavía sin desglose por
  segmento ni prueba de significancia; queda para la próxima revisión
  afinarlo antes de sacar conclusiones.
- 2026-09-06 (revisión semanal, domingo): **el mismo bug de "heal" volvió a
  borrar `signals/2026-09-03.jsonl` una segunda vez** (commit `0cf0a30`,
  deshaciendo el arreglo de ayer); restaurado de nuevo. Sin dato de mercado
  nuevo (CME cerrado el fin de semana) — n=772 y todas las cifras idénticas
  a 2026-09-05, lo que confirma que la recuperación de `sl_origin_vs_layer`
  en 1m/5m SHORT de ayer no era artefacto de la restauración (al restaurar
  hoy de nuevo el mismo archivo, el número no cambió). Mejora permanente en
  `analyze.py`: `file_integrity_check` — detecta automáticamente si algún
  `signals/outcomes/*.jsonl` encoge respecto al máximo visto antes. Ver
  `reviews/2026-week-36.md` para la revisión semanal completa (primera del
  bus).
- 2026-09-07 (lunes, festivo EE.UU. — Globex con volumen reducido):
  **primer día sin repetición del bug de "heal"**, dato genuinamente nuevo.
  n subió de 772 a 796 (465→479 en 1m, 214→221 en 2m, 93→96 en 5m).
  `sl_origin_vs_layer` en 1m SHORT creció de n=219 a n=229 con trades
  nuevos y el delta se mantuvo (+0.296→+0.283, CI90 sigue sin cruzar
  cero) — primera confirmación independiente real, igual que en
  `buy-retest.md`. `tier=B` se mantiene negativo con dato nuevo
  (-0.032→-0.04), confirma que la corrección de ayer no era ruido de la
  restauración. `tier=A+` tuvo su primer cambio de signo en varias
  revisiones (+0.003→-0.015, n=57→58) pero sigue siendo lectura de n
  chico. `decay_weekly` ya reporta una segunda semana (2026-W37, n=26
  todavía chico).
- 2026-09-08 (martes, primer día hábil completo post-feriado): salto de
  muestra grande n=796->1341 (1m 479->831, 2m 221->378, 5m 96->132).
  `sl_origin_vs_layer` en 1m SHORT se hizo MÁS fuerte con dato nuevo
  (delta 0.283->0.417, CI90 [0.2,0.644]); **2m SHORT certifica por
  primera vez** (delta 0.245, CI90 [0.035,0.466], ayer cruzaba cero) — ya
  las tres TF de SHORT certifican el SL estructural. `segment_significance`
  de 2m se revirtió (CI90 pasó de [-0.246,-0.001] a [-0.157,0.029], vuelve
  a cruzar cero) — mismo patrón de reversión por salto de muestra que en
  `buy-retest.md` 2m LONG, ver nota de método ahí. **Hallazgo mayor del
  día**: `session_analyst_cross` gana bootstrap CI90 por veredicto y
  desglose por kind/side (mejora permanente en `analyze.py`) — la
  hipótesis "AVOID rinde peor" de `agent-instructions.md` queda refutada
  con confianza estadística por primera vez (AVOID E[R]=+0.183 CI90 no
  cruza cero n=350; GO E[R]=-0.273 CI90 no cruza cero n=121); nuevo
  chequeo en `material_alerts` para que salga en `report.alerts`. Nota de
  proceso: `git pull` mostró "forced update" de nuevo (rama local vieja);
  resuelto con `git reset --hard origin/main` sin pérdida de trabajo.
- 2026-09-09 (miércoles): día de confirmación, no de dato nuevo (ver
  `buy-retest.md` para el detalle del pipeline) — +27 pares, todos
  TP/TIMEOUT, cero SL nuevos (422/1m, 192/2m, 59/5m idénticos a ayer). La
  mayoría de las métricas coinciden a 2-3 decimales con ayer. La excepción
  es `session_analyst_cross`: el `n_matched` saltó de ~1306 a 1551
  (+245, mucho más que los 69 pares nuevos de todo el bus — el join por
  fecha+killzone+símbolo recuperó cruces de días previos que antes no
  encontraban plan de Session Analyst). Con más muestra el hallazgo se
  sostiene y se afina: `AVOID` E[R]=+0.175 CI90=[0.085,0.267] n=452, `GO`
  E[R]=-0.196 CI90=[-0.301,-0.08] n=219 (CI mucho más angosto que ayer). En
  RETEST/SHORT la celda `GO` pasó de n<5 (no reportable) a n=40
  E[R]=-0.221 — primera vez con muestra útil, mismo sentido que el
  agregado.
