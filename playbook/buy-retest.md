# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-10-05 (lunes) · n: 12984)

### Nota de proceso
`git pull` normal (fast-forward 50 commits, sin conflicto). Llegó jsonl
nuevo real del cron de Netlify (`signals/2026-10-05.jsonl` 55 líneas,
`outcomes/2026-10-05.jsonl` 45 líneas) — primer día hábil tras el fin de
semana. `pendientes` subió de 0 a 18 (señales de hoy aún sin resolver,
normal). `huérfanos` estable en 40.

**Dos hallazgos nuevos de hoy, no en la revisión del domingo:**
1. **`GATE` nuevo en `report.alerts`: el chequeo numérico puro
   (n≥100 & E[R]>0 & PF≥1.3 & WR≥50, agregado histórico completo) ya se
   cumple para `5m/RETEST/LONG`** (`report.json.gate.readyForLive=true`).
   **Evaluación del agente (la nota del propio gate dice que esto lo
   valida el agente, no el script): NO cumple todavía el gate real del
   peldaño 2** (`execution-ladder.md`) porque (a) la estabilidad semanal
   no se sostiene — WR TP1 por semana cerrada 51.4% (W38) → 45.5% (W39) →
   53.7% (W40), swing de 8pts, con W39 bajo el umbral de 50%; (b) PF por
   semana 1.49 (W38) → 1.2 (W39) → 1.23 (W40), **las dos últimas semanas
   cerradas caen bajo el PF≥1.3 exigido** aunque el agregado histórico
   completo (n=1283, incluye semanas viejas más fuertes) sí llega a 1.3
   justo en el límite; (c) ningún experimento de `experiments.json` tiene
   `verdict=confirmed` todavía (los 3 siguen en `null`), así que la causa
   de SL dominante de este segmento no está "mitigada por un experimento
   confirmado" como exige el gate. **Conclusión: sigue en peldaño 1
   (Sombra), no se recomienda armar tickets semi-auto en este segmento.**
   Ver `report.json.gate` (nota textual) y "Decaimiento" abajo para el
   detalle semana a semana.
2. Las alertas `MUESTRA` muestran que **semanas ya cerradas están
   perdiendo pares** (W36 3183→2725, W38 4911→4435, W39 5355→5064) —
   consecuencia esperada del bug de `sigId` ya reportado (colisión +
   "last wins" desplaza un par real a otra semana cuando llega data nueva
   que colisiona), **no un bug nuevo**, pero la magnitud crece corrida a
   corrida: 1665 sigId colisionados en señales (907 con `result`
   distinto, confirmando que son pares reales distintos, no reenvíos).
   Sigue sin arreglarse en el Pine (el histograma de `delta_days` sigue
   dominado por múltiplos de 7 → `bar_index` que se reinicia
   semanalmente). **Sigue siendo la alerta más importante para Jesús: sin
   esto arreglado, cualquier métrica "por semana" puede estar mal
   fechada.**

### Veredicto global
1m n=8102 (+41 reales hoy, resto timeouts) WR 45.0% E[R]=**0.044** PF=1.09
(estable); 2m n=3599 (+13) WR 46.7% E[R]=**0.035** PF=1.07 (estable, al
filo); 5m n=1283 (+6) WR 51.2% E[R]=**0.131** PF=1.3 (ver nota de gate
arriba — agregado fuerte pero inestable semana a semana).
`segment_significance`: 1m CI90=[0.021,0.067] n=7839 sigue
`survives_fdr10=true`; 5m CI90=[0.072,0.186] n=1206 sigue
`survives_fdr10=true`; 2m CI90=[-0.0,0.069] n=3457 sigue `survives_fdr10=true`
pero sigue al filo (p=0.054) — sin cambio vs el domingo. `gate.readyForLive`
ahora `true` en el chequeo numérico puro (ver nota de proceso), pero el
agente NO lo certifica como listo para el peldaño 2 todavía. **Escalera de
ejecución: sigue en peldaño 1 (Sombra)**, cero ejecución real.

### Reglas condicionales (IF contexto ENTONCES acción)

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `tf=1m` (`survives_fdr10=true`) | TOMAR, edge real fuera de ruido | 7839 | E[R]=**0.044** CI90=[0.021,0.067] | alta |
| 2 | `tf=5m` (`survives_fdr10=true`) | TOMAR, edge real fuera de ruido, el más grande de los tres TF — **pero inestable semana a semana, no asumir que el E[R] agregado se repite cada semana** | 1206 | E[R]=**0.131** CI90=[0.072,0.186] | alta en agregado, moderada por semana |
| 3 | `tf=2m` (**`survives_fdr10=true` al filo, p=0.054**) | TOMAR con cautela, sigue sin despegarse limpiamente de cero | 3457 | E[R]=**0.035** CI90=[-0.0,0.069] | baja-moderada — sin cambio vs ayer |
| 4 | `tier=A+` | plano/ligeramente negativo, WR bajo típico del tier | 985 | WR 22.6%, E[R]=**-0.013** PF=0.98 | moderada — vigilar |
| 5 | `tier=B` | TOMAR, prioridad sobre A+ y C | 5710 | WR 46.6% E[R]=**0.068** PF=1.14 vs tier C WR 49.3% E[R]=0.044 PF=1.09 | alta |
| 6 | símbolo (`cross_instrument`), 1m/2m/5m | los tres `universal` | — | sin cambio de veredicto | moderada |
| 7 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1`, muestra mínima | 7 vs 22516 | sin revisión hoy | baja — n demasiado chico para usar |
| 8 | `tf=5m` + gate numérico puro cumplido | **NO** pasar a semi-auto todavía: falta estabilidad semanal (PF<1.3 en 2 de las últimas 3 semanas cerradas) y un experimento `confirmed` sobre la causa de SL dominante | 1283 (833 en W38-W40) | ver "Nota de proceso" punto 1 | alta — gate de ejecución, no de señal |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara de calidad
  de entrada en este segmento.

### Gestión
- **Escalera + parciales (`managed_vs_naive`)**: 1m n=7835 delta=**+0.086**
  (estable); 2m n=3456 delta=**+0.031** (estable); 5m n=1206 delta=**-0.029**
  (sigue siendo el único TF donde la gestión resta en LONG, prácticamente
  sin cambio). Regla sin cambios: escalera en 1m/2m, mercado simple en 5m
  LONG.
- **SL de 3 capas vs SL = mecha del retest — sin cambio de fondo vs el
  domingo.** `sl_origin_vs_layer.since_change` (n=4873 total RETEST,
  `recvDate>=2026-09-26`) en LONG: 1m n=1620 delta=**+0.002**
  CI90=[-0.071,0.08] (plano); 2m n=808 delta=**+0.183**
  CI90=[0.064,0.308] (**sigue siendo el único de los 6 segmentos RETEST
  que confirma limpio post-cambio**); 5m n=290 delta=**+0.072**
  CI90=[-0.037,0.179] (plano). Ningún segmento LONG sale
  `delta_below_zero=true`. **Decisión sin cambio: mantener aplicado en
  los 6 segmentos, no revertir nada.** Sólo revertir un segmento
  específico si desarrolla `delta_below_zero=true` con n≥40.
  `prediction_scoreboard` sigue en hit_direction_rate=33.3% (n=6, peor que
  un volado) — sin dato nuevo (no es domingo, no se agregó predicción
  hoy); se mantiene la cautela declarada el domingo con "cambio del mes".
- **Modo sombra (`shadow_rules` v2 + `shadow_weekly`)** — gate 0→1 ya
  cumplido desde el 2026-10-04 (ver `state.json.executionGate`, sin
  cambio hoy). W41 (semana en curso) lleva sólo n=39 por lado, shadow
  empata con raw (0.065 vs 0.065) — insuficiente para evaluar, normal al
  inicio de semana. Sigue siendo sólo modo sombra: nada se ejecuta. Ver
  "Nota de proceso" arriba para por qué, a pesar del `gate.readyForLive`
  numérico en `true` para 5m/RETEST/LONG, el agente NO certifica el
  peldaño 2 todavía.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL sobre las pérdidas LONG (n=6060, RETEST/LONG): `RR-bajo`
  2251/6060 (37.1%) causa dominante, `killzone-Asia-largo` 2132/6060
  (35.2%) segundo, `contra-estructura` 2085/6060 (34.4%) tercero,
  `stop-en-el-minimo` 2006/6060 (33.1%) cuarto — sin cambio de fondo, las
  cuatro causas siguen muy cerca entre sí (no hay una causa dominante
  clara y aislada, es una mezcla). El SL estructural (`sl_basis_retest`)
  es el candidato que mejor ataca `RR-bajo`; sigue aplicado y sin caso
  para revertir (ver "Gestión"), pero sólo con evidencia madura en 2m
  LONG por ahora — **esto es precisamente lo que le falta al gate del
  peldaño 2 para 5m/RETEST/LONG: ningún experimento confirmado todavía
  mitiga esta causa en ese segmento específico.**

### Cruce con Session Analyst
RETEST/LONG específicamente: `AVOID` n=1149 E[R]=**-0.036** PF=0.93 — peor
que el agregado global, la hipótesis se confirma con más fuerza en LONG
que en el resto del bus. A nivel global (todo kind/side): `AVOID` n=1940
E[R]=**-0.006** PF=0.99 (peor de los tres); `GO` n=994 E[R]=**0.152**
CI90=[0.085,0.217] PF=1.35 y `WAIT` n=6469 E[R]=**0.059**
CI90=[0.033,0.084] PF=1.12 (ambos certifican, no cruzan cero) — orden
GO > WAIT > AVOID sostenido, sin cambio vs el domingo.

### Decaimiento
`decay_weekly` (global, todo kind/side): 2026-W38 WR 46.3% E[R]=0.098;
2026-W39 WR 46.0% E[R]=0.064; **2026-W40 (cerrada) WR 45.5% E[R]=0.017**
— la semana más débil de las últimas 3 cerradas, pero sin cruzar el
umbral formal de decaimiento (>15pts WR vs media 3 semanas previas).
**Detalle nuevo de hoy por segmento (`decay_weekly_by_segment`), motivo
del hallazgo de gate de arriba:** 5m/RETEST/LONG WR 51.4%→45.5%→53.7% y
PF 1.49→1.2→1.23 en W38/W39/W40 — swing de 8pts de WR y PF bajo 1.3 en
las 2 últimas semanas cerradas, aunque el agregado histórico completo se
ve fuerte (E[R]=0.131). 1m/RETEST/LONG sigue débil: W40 E[R]=**-0.033**
PF=0.94 (vs W39 E[R]=0.062), segunda semana consecutiva deteriorándose.
2m/RETEST/LONG también plano en W40 (E[R]=-0.002 vs W39 0.148). Ningún
segmento cruza el umbral formal de 15pts, pero la tendencia de las
últimas 2 semanas en 1m y 5m LONG es a la baja — vigilar si W41 (sólo
n=15 en 1m, n=2 en 5m hasta ahora, muy pronto para leer) confirma o
revierte.

## Histórico de cambios
- 2026-10-05 (lunes): primer jsonl real del cron desde el 10-02 (+41/+13/+6
  en 1m/2m/5m LONG). Dos hallazgos: (1) **nuevo `GATE` en `report.alerts`**
  — el chequeo numérico puro de `execution-ladder.md` peldaño 2 ya se
  cumple en agregado histórico para `5m/RETEST/LONG`
  (`gate.readyForLive=true`), pero el agente **no lo certifica**: WR TP1
  y PF por semana cerrada son inestables (WR 51.4→45.5→53.7, PF
  1.49→1.2→1.23 en W38-W40, PF bajo 1.3 las últimas 2 semanas) y ningún
  experimento de `experiments.json` tiene `verdict=confirmed` todavía —
  **sigue en peldaño 1 (Sombra)**, sin cambio de ejecución. (2) las
  alertas `MUESTRA` (pares perdidos en semanas ya cerradas: W36, W38, W39)
  confirman que el bug de `sigId` sigue activo y su efecto crece con cada
  corrida — sigue pendiente de arreglo en el Pine, es la alerta más
  accionable para Jesús hoy. 1m/RETEST/LONG lleva ya 2 semanas
  consecutivas (W39, W40) deteriorándose (ver "Decaimiento"), sin cruzar
  el umbral formal todavía — vigilar W41.
- 2026-10-04 (domingo, REVISIÓN SEMANAL): `git pull` encontró `main` local
  divergida sin ancestro común de `origin/main` (snapshot de contenedor
  viejo); resuelto con `git merge origin/main --allow-unrelated-histories
  -X theirs` (árbol final verificado idéntico a `origin/main`, sin
  pérdida). **No llegó jsonl nuevo del cron de Netlify** (último:
  2026-10-02); el delta de hoy (+37 real en este playbook) son señales
  pendientes resolviendo por timeout de 24h, `pendientes` bajó a 0 en todo
  el bus. Dos conclusiones de la revisión semanal, ninguna de dato nuevo:
  (1) con el cierre de W40, `since_change` muestra que el "cambio del mes"
  `sl_basis_retest` sólo confirma limpio post-cambio en **1 de 6
  segmentos RETEST** (2m/RETEST/LONG); se agregó una alerta permanente a
  `analyze.py` para esto y para `hit_direction_rate` bajo (ver
  `experiments.json`); no se revierte nada, se baja la confianza. (2)
  **Modo sombra cumple el gate 0→1 con 4 semanas cerradas seguidas
  (W37-W40)** bajo el criterio v2 fijo — `state.json.executionGate.phase`
  pasa de `advisor` a `shadow` (cero ejecución real, sigue siendo sólo
  publicar qué se habría tomado). `1m/RETEST/LONG` cerró su primera
  semana con E[R] negativo (W40, ver "Decaimiento") — vigilar, no es
  decaimiento formal todavía. `rr1_threshold_cut_oos` (ver
  `sell-retest.md`/`experiments.json`): el único candidato vivo de la
  semana pasada (5m LONG rr1≥1.2) deja de confirmar con el split OOS
  actualizado (W39-W40) — sin candidato de `rr1` mínimo esta semana.
  `huérfanos` estable en 40. `gate.readyForLive` sigue `false`. Ver
  `reviews/2026-week-40.md` para el detalle completo de la revisión.
- 2026-10-03 (sábado): **corrección metodológica, no sólo dato nuevo.** Se
  agregó `sl_origin_vs_layer.since_change` a `analyze.py` (emparejado
  `rOrig` vs `rMultiple` restringido a `recvDate>=changeDate`) tras notar
  que la cadena de razonamiento 09-28→10-02 (basada en `prediction_scoreboard`,
  before/after de `rMultiple`) estaba confundiendo el régimen de mercado de
  la semana W40 con el efecto del experimento `sl_basis_retest` — el
  `appliedNote` del experimento ya decía que `rMultiple` no cambia con el
  input del Pine, así que ese before/after no podía medir el efecto real.
  Con la métrica correcta, LONG no sale negativo en ningún TF
  post-cambio (2m incluso confirma positivo con n=780 CI90=[0.075,0.322]):
  se retira la recomendación de revertir `sl_basis_retest` en LONG en la
  revisión semanal de mañana. Ver `experiments.json` (entrada de hoy en
  `next_steps` de `sl-retest-wick-2026-09-03`) para el detalle completo.
  Aparte de esto: dato nuevo +343/+201/+59 en 1m/2m/5m; colisión de sigId
  sigue creciendo (1473→1658 señales, cuarto día seguido, ver report.alerts);
  `huerfanos` estable en 40; `gate.readyForLive` sigue `false`.
- 2026-10-02 (viernes): `git pull` limpio (fast-forward). Dato nuevo
  sólido (+298/+129/+54 en 1m/2m/5m). La colisión de `sigId` del hallazgo
  de ayer **sigue creciendo** (1308→1473 señales, 1208→1368 outcomes,
  778 con `result` distinto, antes 690) — confirma que es un bug activo
  del Pine, no un evento puntual; sigue sin tocarse el pareo. `2m/RETEST/LONG`
  recupera `survives_fdr10=true` hoy tras 3 días en `false`, pero al filo
  (CI90=[-0.001,0.07], p=0.053) — recuperación débil, no limpia.
  **Hallazgo más accionable sigue siendo el SL `sl_basis_retest`**: con
  `afterN` ya en los miles (1m) y cientos (2m/5m), LONG sigue en dirección
  contraria a lo predicho en los 3 TF y SIN mejorar vs ayer; la novedad es
  que el lado SHORT ya no confirma con la fuerza de antes (1m SHORT casi
  plano hoy, sólo 2m SHORT sigue claramente positivo) y 5m se invirtió en
  ambos lados esta semana (LONG a positivo, SHORT a negativo) — el TF con
  menos muestra sigue siendo ruidoso. Van 6 días hábiles desde el cambio
  (09-28 a 10-02), todavía no las "2 semanas" del propio criterio del
  experimento: se mantiene NO revertir hoy, decisión formal el domingo
  2026-10-04 si 1m/2m LONG (los de muestra más grande y consistente)
  siguen negativos. Modo sombra suma su cuarta semana seguida ganándole
  al crudo (W37-W40), gate 0→1 ya cumplido con las 3 cerradas, pendiente
  de confirmarlo en la revisión del domingo. `huerfanos` estable en 40.
  `gate.readyForLive` sigue `false`. Resto de reglas condicionales (tier,
  cross-instrument, Session Analyst) sin cambios de fondo.
- 2026-10-01 (jueves): `git pull` limpio. Dato nuevo solido (+377/+178/+56
  en 1m/2m/5m). **Hallazgo de pipeline (mejora permanente en `analyze.py`,
  afecta a los 4 playbooks)**: se investigo a fondo la alerta MUESTRA que
  llevaba semanas repitiendose y se encontro la causa raiz: 6.3% de los
  `sigId` de senales y 6.1% de outcomes colisionan entre archivos
  distintos (mismo sigId, `receivedAt` distinto), con el delta en dias
  casi siempre multiplo de 7, y varias colisiones con `result` DISTINTO
  entre ocurrencias -- no es un reenvio, son pares reales distintos
  fusionados en un sigId (probable bar_index del Pine reiniciandose
  semanalmente). Nueva funcion `sigid_collision_report()` mide esto cada
  corrida (seccion nueva en `report.md`, clave `sigid_integrity`) y
  dispara alerta si hay colisiones con result distinto. No se toco el
  pareo todavia; el fix real va en el generador de sigId del Pine.
  **Segundo hallazgo, ya con evidencia fuerte**: el cambio `sl_basis_retest`
  (aplicado 2026-09-26) lleva 2 semanas consecutivas con la misma
  divergencia -- RETEST LONG (1m/2m/5m) empeora con el SL nuevo mientras
  RETEST SHORT mejora; `decay_weekly_by_segment` de W40 (parcial, n ya
  sustancial) muestra E[R] negativo en los tres TF LONG y positivo en los
  tres TF SHORT. Se propondra formalmente revertir a 3-capas en LONG
  (manteniendo la mecha en SHORT) en la revision semanal del domingo
  2026-10-04. `2m/RETEST/LONG` lleva ya tercer dia seguido sin
  `survives_fdr10`. `huerfanos` se mantiene en 40, sin senal de problema
  de pipeline en ese frente. `gate.readyForLive` sigue `false`.
- 2026-09-30 (miércoles): `git pull` mostró que la rama local `main` y
  `origin/main` divergen SIN ancestro común (no es sólo un "forced
  update" simple esta vez). El harness bloqueó tanto `checkout -B main
  origin/main` como el `analyze.py` inicial bajo el mismo motivo de
  destrucción local; se resolvió sin tocar el puntero de `main` creando
  un branch nuevo (`main-sync`) desde `origin/main` y trabajando ahí —
  el push de hoy apunta a `origin/main` desde `main-sync`. `huerfanos`
  se mantiene en 40 (igual que ayer), sin señal de problema de pipeline.
  Cuarto día real bajo el SL estructural nuevo. **Hallazgo principal: el
  patrón de ayer (LONG no confirma, SHORT sí) se sostiene un cuarto día
  con `afterN` ya por encima de 40 en los 6 segmentos**, y una métrica
  INDEPENDIENTE lo corrobora por primera vez: `decay_weekly_by_segment`
  de la semana en curso (2026-W40) muestra los tres TF LONG cruzando a
  débil/negativo (1m 0.053→0.03, 2m 0.126→-0.056, 5m 0.071→-0.008)
  mientras los tres TF SHORT mejoran la misma semana (ver
  `sell-retest.md`) — sin depender de `predictions.jsonl` ni de la
  fecha exacta del cambio. Contradicción activa a anotar: la medición
  paralela in-sample (`sl_origin_vs_layer`) SIGUE sin reversión,
  certificando la mecha como mejor SL en los tres TF LONG (delta
  0.146-0.265, CI90 no cruza cero) — el desacuerdo entre la simulación
  paralela y el resultado real post-cambio en LONG sigue sin explicación
  y queda como hallazgo abierto. `2m/RETEST/LONG` lleva ya dos corridas
  seguidas sin `survives_fdr10` (CI90=[-0.008,0.069]). **Todavía NO se
  recomienda revertir** (faltan las "2 semanas consecutivas" del propio
  criterio del experimento) pero se deja escrito: si el patrón se
  sostiene el resto de la semana, se propondrá en la revisión semanal
  del domingo 2026-10-04 revertir `sl_basis_retest` a 3-capas en las
  tres ramas LONG (y 5m SHORT, que también se dio vuelta hoy — ver
  `sell-retest.md`), dejando la mecha del retest sólo en 1m/2m SHORT.
  `gate.readyForLive` sigue `false` (sin cambio). Resto de reglas
  condicionales (tier, edge, cross-instrument, Session Analyst) sin
  cambios de fondo.
- 2026-09-29 (martes): `git pull` con "forced update" habitual en
  `origin/main` (HEAD detached en el tip correcto, rama local `main`
  desactualizada, sin pérdida, sin tocar su puntero). Tercer día real
  bajo el SL estructural nuevo. **Hallazgo principal: con `afterN`
  agregado del experimento saltando de 89 a 999, el desglose por
  segmento de `prediction_scoreboard` muestra que los 3 segmentos LONG
  de este playbook (1m n=199, 2m n=83, 5m n=44) salen TODOS en dirección
  contraria a lo predicho** (realDeltaER negativo donde se predijo
  positivo), mientras el lado SHORT en 1m/2m sí confirma (ver
  `sell-retest.md`). `hit_direction_rate` global cae a 33.3% (2/6), la
  peor lectura del scoreboard hasta la fecha. Coincide con: (a)
  `2m/RETEST/LONG` PERDIENDO `survives_fdr10` hoy (CI90 cruza cero, se
  había avisado ayer que estaba al filo) y (b) la primera semana parcial
  NEGATIVA de `5m/RETEST/LONG` en `decay_weekly_by_segment` (W40 n=39
  E[R]=-0.075). Ninguna de las tres piezas por separado sería
  concluyente (todas con n chico o parcial), pero las tres apuntan en la
  misma dirección al mismo tiempo — **no se recomienda revertir el SL
  todavía** (3 días de calendario, uno sin sesión CME, es poca muestra
  temporal; el propio historial in-sample del experimento documentó que
  lecturas con n bajo sobrestiman el efecto en cualquier dirección) pero
  se marca explícitamente como el segmento a vigilar más de cerca antes
  de la revisión semanal del domingo 2026-10-04 — si el patrón LONG
  negativo se sostiene, ese es el escenario para proponer revertir el SL
  a 3-capas SOLO en el lado LONG de RETEST, dejando SHORT con el SL
  nuevo (detalle en `experiments.json`). `gate.readyForLive` volvió a
  `false` (WR acumulado 5m/RETEST/LONG cruzó de 50.0% a 49.5%, mismo
  flip-flop de borde de siempre). Resto de reglas condicionales
  (tier, edge, cross-instrument, Session Analyst) sin cambios de fondo.
- 2026-09-28 (lunes): `git pull` con "forced update" habitual en
  `origin/main`, sin pérdida (HEAD ya apuntaba al tip correcto; la rama
  local `main` quedó desactualizada y se dejó así en vez de forzar su
  puntero, por la restricción del harness sobre destrucción local).
  Primer día hábil con trades reales bajo el SL estructural nuevo
  (aplicado el sábado 09-26). **Bug encontrado y arreglado en
  `analyze.py` (mejora permanente)**: `eval_experiments()` nunca evaluaba
  experimentos en estado `applied`, sólo `running`/`proposed` — el
  experimento de SL se habría quedado sin medición antes/después para
  siempre. Con el fix, el verdict mecánico agregado sale `confirmed`
  (E[R] 0.057→0.225, n afterN=89) pero el desglose real por segmento
  (`prediction_scoreboard`) muestra un primer día volátil y
  contradictorio: **1m LONG (n=37) sale en dirección CONTRARIA a lo
  predicho** (realDeltaER=-0.055 vs +0.152 predicho) mientras 1m SHORT
  (n=33) sobrepasa 4x lo predicho. Decisión: NO se sube el estado a
  `confirmed` todavía, se sigue vigilando por segmento (detalle completo
  en `experiments.json`). Aparte de eso: `gate.readyForLive` volvió a
  `true` por el filo exacto (WR acumulado 5m/RETEST/LONG 49.8%→50.0%) —
  no es una recuperación real, la semana cerrada 2026-W39 sigue con
  WR=45.6%/PF=1.22, ambos bajo el umbral de estabilidad; sigue en
  peldaño 0 (asesoría). Punto positivo: el modo sombra v2 completó su
  segunda corrida seguida con la racha de 3 semanas (W37-W39) intacta —
  candidato a subir a peldaño 1 en la revisión semanal si se sostiene.
  Resto de segmentos (1m/2m/5m, tier, nearEdge, cross-instrument,
  Session Analyst) sin cambios de fondo frente a ayer.
- 2026-09-27 (domingo, REVISIÓN SEMANAL): `git pull` limpio. Fin de
  semana sin sesión CME nueva, sólo 46 pendientes cruzando 24h en todo el
  bus (la mayoría LONG: +27/+10/+8 en 1m/2m/5m). Tres decisiones de la
  revisión semanal (detalle en `reviews/2026-week-39.md`): (1) **el
  experimento de SL estructural se aplicó ayer en TradingView**
  (`changeDate=2026-09-26`), después de certificar sin reversión en los 6
  segmentos RETEST durante semanas — deja de ser propuesta, pasa a ser el
  estado real del indicador; `predictions.jsonl` actualizado con
  `appliedDate` en las 6 líneas, `afterN=0` hoy; (2) **mejora permanente
  `rr1_threshold_cut_oos`**: evalúa el corte de `rr1` mínimo contra el
  split walk-forward — **1m LONG se revierte fuera de muestra** (subir el
  piso de RR lo empeora, se retira como candidato) mientras **5m LONG es
  el único de los tres TF LONG que confirma limpio** (E[R] 0.148→0.372
  OOS, CI90 no cruza cero) y se propone hoy como cambio experimental
  acotado sólo a ese TF; (3) **`SHADOW_RULES_V1` se actualizó a v2**,
  ampliando `tf_side` de 4 a los 6 segmentos RETEST certificados. Hallazgo
  de gate: **`gate.readyForLive` pasó de `true` a `false`** — el WR
  acumulado de 5m/RETEST/LONG cayó a 49.8% (bajo el umbral 50%) después de
  que la semana cerrada 2026-W39 retrocediera con fuerza en ese segmento
  (PF 1.42→1.20, WR 50.2%→44.7%). 2m/RETEST/LONG fue la excepción positiva
  de la semana (su mejor E[R] semanal hasta ahora, 0.127). Sin cambios de
  peldaño en la escalera de ejecución (sigue en asesoría).
- 2026-09-26 (sábado): incidente de repo distinto a los anteriores — el
  auto-mode del harness bloqueó `checkout -B`/`reset --hard` como
  destrucción local irreversible; resuelto sin descartar nada con
  `git merge origin/main --allow-unrelated-histories -X theirs` (árbol
  final idéntico a `origin/main`, verificado). Dato de 2026-09-25
  (viernes) llegó completo hoy (+541/+231/+97 en 1m/2m/5m LONG). Mejora
  permanente a `analyze.py`: nueva función `shadow_weekly()` que
  desglosa el modo sombra por semana ISO — primer resultado: la racha de
  3 semanas seguidas que pide el gate 0→1 se cumplió en W36-W38 pero se
  rompió esta semana (W39 parcial, shadow 0.034 vs raw 0.048). Dos
  señales de debilitamiento a vigilar: 2m LONG por primera vez casi
  pierde `survives_fdr10` (CI90 límite inferior 0.033→0.003) y la
  lectura parcial de W39 en 5m/RETEST/LONG revirtió con fuerza (PF
  1.54→1.2 con más muestra) — mismo patrón de volatilidad de semana
  parcial ya documentado antes, no tratar como decaimiento real hasta el
  cierre de mañana. Sin cambios de fondo: los tres TF siguen
  certificando FDR, el SL estructural sigue sin reversión en los 6
  segmentos RETEST, gate de ejecución sigue en asesoría (W36 y ahora
  W39 parcial ambas <1.3 PF). Pendiente para la revisión semanal de
  MAÑANA (domingo 2026-09-27): decidir el criterio desactualizado de
  `SHADOW_RULES_V1` (excluye 2m LONG/5m SHORT) y leer el cierre de W39
  antes de tocarlo.
- 2026-09-25 (viernes): `git pull` reportó "forced update" habitual en
  `origin/main` (shallow clone, mismo tip esperado, sin pérdida),
  resuelto con `checkout -B main origin/main`. Dato nuevo chico y parejo
  en los tres TF (+47/+29/+28 en 1m/2m/5m). Día de confirmación de bajo
  volumen sin sorpresas de dirección: los tres TF siguen certificando
  FDR, el SL estructural sigue sólido en los seis segmentos RETEST sin
  ninguna reversión y el walk-forward OOS se mantiene prácticamente
  igual (0.113→0.114). **Hallazgo más accionable del bus (sin cambio de
  fondo, pero cada vez más urgente)**: el experimento de SL estructural
  (`sl-retest-wick-2026-09-03`) sigue `proposed` sin `changeDate` pese a
  certificar en 6/6 segmentos RETEST desde hace semanas con muestras de
  cientos a miles — sigue siendo el cambio de indicador con la evidencia
  más madura y estable de todo el bus, pendiente de que Jesús lo aplique
  en `scalp_command.pine`. Sin cambios en el gate de ejecución (sigue en
  asesoría, W36 PF=1.18<1.3). El criterio de `modo sombra`
  (`SHADOW_RULES_V1`) sigue con la justificación desactualizada anotada
  ayer (excluye `2m LONG`/`5m SHORT` con un argumento que
  `segment_significance` ya no sostiene) — queda para decidir en la
  revisión semanal del domingo 2026-09-27, no hoy.
- 2026-09-24 (jueves): `git pull` limpio, sin incidentes de repo. Dato
  nuevo moderado y parejo en los tres TF (+256/+87/+28 en 1m/2m/5m).
  Día de confirmación sin sorpresas de dirección: los tres TF siguen
  certificando FDR, el SL estructural sigue sólido en los tres (sin
  ninguna reversión) y el walk-forward OOS sube de 0.091 a 0.113.
  **Hallazgo de método más importante**: el criterio fijo de `modo
  sombra` (`SHADOW_RULES_V1`, definido el 2026-09-20) excluye
  `2m/RETEST/LONG` y `5m/RETEST/SHORT` de su `tf_side` con el
  argumento escrito de que su CI90 "cruza o roza cero" — pero
  `segment_significance` de hoy (n=2523 y n=539 respectivamente)
  muestra que **ambos certifican FDR con CI90 que no cruza cero desde
  hace ya varias corridas**, contradiciendo la justificación guardada
  en `analyze.py`. No se toca el criterio hoy (los cambios de `modo
  sombra` se hacen en la revisión semanal, per `agent-instructions.md`)
  pero queda anotado para decidir el domingo 2026-09-27 si se amplía a
  los 6 segmentos RETEST certificados. Segundo hallazgo (no nuevo pero
  cada vez más sólido): el experimento de SL estructural ya certifica
  en los 6/6 segmentos RETEST con muestras de cientos a miles — es el
  cambio de indicador con la evidencia más madura y estable del bus,
  sigue `proposed` sin `changeDate` en TradingView. La semana cerrada
  2026-W38 del segmento objetivo del gate (5m/RETEST/LONG) perdió 8
  pares por dedup (319→311, PF 1.44→1.43) — la caída más grande vista
  en este segmento específico hasta ahora, vigilar que no sea el inicio
  de algo distinto al goteo habitual de 1-2 pares. Sin cambios en el
  gate de ejecución (sigue en asesoría).
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
