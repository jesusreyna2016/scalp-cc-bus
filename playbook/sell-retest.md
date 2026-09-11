# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-11 · n: 2717)

### Nota de proceso — ver `buy-retest.md`
Mismo incidente de repo que `buy-retest.md`: `origin/main` fue reescrito
río arriba (historia sin ancestro común con la rama local), verificado
como superset sin pérdida de datos y resuelto con
`git reset --hard origin/main`. En este playbook: n 2100→2717 (**+617**;
1m 1295→1684, 2m 612→789, 5m 193→244).

### Veredicto global
1m n=1684 (+389) WR 43.4% E[R]=**+0.017** PF=1.03 (bajó de +0.051); 2m
n=789 (+177) WR 48.2% E[R]=**+0.074** PF=1.15 (subió de +0.057); 5m n=244
(+51) WR 47.5% E[R]=**-0.005** PF=0.99 (bajó de +0.02, vuelve a rozar
negativo). `segment_significance`: 1m CI90=[-0.033,0.072] p=0.293 n=1639
— **retrocedió** respecto a ayer ([-0.008,0.111] p=0.083), se aleja de
certificar; 2m CI90=**[-0.002,0.145]** p=0.056 n=777 — **mejoró y es
ahora el más cerca de certificar de los tres** (límite inferior a solo
0.002 de cruzar cero, venía de [-0.026,0.142] p=0.138); 5m
CI90=[-0.133,0.14] p=0.521 n=235 (sin cambio material). Ningún TF
certifica todavía — 2m es el que hay que vigilar de cerca para la próxima
corrida.

### Reglas condicionales (IF contexto ENTONCES acción)
El gradiente de `nearEdge` que se había invertido ayer **se invierte de
nuevo hoy** — cuarto cambio de forma en 5 revisiones, tratar como no
confiable:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=-1` | **se da vuelta a negativo otra vez** | 1489 (+251) | E[R] **-0.023** (ayer +0.012), WR 43.3%, PF 0.96 | baja — tercer cambio de signo de esta rama en 5 corridas |
| 2 | `nearEdge=0` | se mantiene como la mejor rama, estable | 1143 (+360) | WR 46.8%, E[R]=**+0.103** (ayer +0.113), PF 1.21 | moderada — es la única rama que no cambió de signo hoy, aunque el ranking relativo entre ramas sigue sin asentarse |
| 3 | `nearEdge=1` | sigue siendo la rama con mejor WR | 85 (+6) | WR 55.3%, E[R]=+0.028 (ayer +0.022) | baja — n todavía chico para esta rama |
| 4 | símbolo (`cross_instrument`), 1m | sigue `instrument-specific` | spread 0.637 (NQ 0.032, YM 0.09, ES -0.025, GC -0.002, **CL n=43 E[R]=-0.547, cifras idénticas a ayer**) | CL sigue siendo el peor símbolo; **cero señales nuevas de CL en 1m SHORT hoy** pese al salto de +389 pares del TF | moderada — tercera corrida con CL como el peor símbolo, pero congelado en n=43 |
| 5 | `tier=A+` | sigue positivo pero **se moderó bastante** | 172 (+21) | WR 27.3%, E[R]=**+0.107** (ayer +0.185), PF=1.16 | baja — mismo patrón de vaivén que `tier=A+` en `buy-retest.md`, no tratar como asentado |
| 6 | `tier=B` | se va más al lado negativo | 1213 (+198) | WR 45.6% E[R]=**-0.031** (ayer -0.001), PF=0.94 | baja — se aleja de breakeven en sentido negativo, sigue sin ser TOMAR |

**Lectura de método**: `nearEdge=-1` cambió de signo por tercera vez en 5
corridas y `tier=A+`/`tier=B` se movieron de nuevo con muestra grande —
seguir tratando estos cortes como no asentados, no fijar reglas nuevas.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara.

### Gestión
- **La escalera + parciales (`managed_vs_naive`) sigue ayudando en los
  tres TF**, pero el margen sigue reduciéndose con más muestra: 1m
  n=1632 delta=**+0.12** (estable, venía de +0.123); 2m n=777
  delta=**+0.074** (bajó de +0.116, tercera corrida seguida a la baja); 5m
  n=234 delta=**+0.039** (bajó a la mitad de +0.084) — sigue siendo
  positivo en los tres, pero 2m y 5m vienen bajando de forma sostenida,
  vigilar si siguen cayendo.
- **SL estructural (`sl_origin_vs_layer`)**: **el debilitamiento
  advertido ayer se confirma** — 1m n=1252 (+354) delta=**+0.133**
  CI90=**[0.003,0.271]** (certifica al filo, el límite inferior bajó de
  0.027 a 0.003 — a un paso de perder la certificación); **2m PIERDE la
  certificación**: n=625 (+163) delta=+0.096 CI90=**[-0.009,0.243]**
  (vuelve a cruzar cero; ayer certificaba al filo con [0.001,0.313], se
  cumplió la advertencia de tratarlo como débil); 5m sigue siendo el más
  sólido: n=198 (+49) delta=**+0.687** CI90=[0.13,1.418] (bajó un poco de
  +0.734 pero el CI se estrechó — la lectura más estable de las tres).
  **Cambio de foco para la propuesta de la revisión semanal**: de las tres
  TF de SHORT, hoy solo 5m SHORT (y 1m, al filo) siguen siendo candidatos
  sólidos; 2m SHORT queda fuera igual que 2m LONG (ver
  `experiments.json.next_steps`, a actualizar).
- `revAfterSL_rate` por corte: sin desglose nuevo relevante hoy.

### Contextos a evitar
- `nearEdge=-1` vuelve a verse negativo (regla #1) pero con 3 reversiones
  en 5 días no es todavía un contexto a evitar con confianza.
- Autopsia de SL sobre las 1334 pérdidas SHORT (+308 vs ayer): tres causas
  siguen prácticamente empatadas — `RR-bajo` 463/1334 (34.7%) edita
  ligeramente al frente, `contra-estructura` 459/1334 (34.4%),
  `stop-en-el-minimo` 441/1334 (33.1%) — rango de 1.6pp, mismo empate de
  fondo que ayer con el orden barajado otra vez. Ninguna causa mitigada
  todavía por un experimento `confirmed`.
- **Cruce con Session Analyst — reversión completa, la más fuerte de todo
  el bus hoy.** Desglose por kind/side en RETEST/SHORT (`by_kind_side`):
  `AVOID` n=454 (+100) E[R]=**-0.034** PF=0.94 (**ayer +0.067 — se da
  vuelta a negativo**); `GO` n=76 (+36) E[R]=**+0.193** PF=1.44 (**ayer
  -0.221 — se da vuelta a fuertemente positivo, el cambio más grande de
  todo el playbook hoy**); `WAIT` n=646 (+97) E[R]=-0.055 (ayer -0.025,
  se mantiene negativo). El orden pasó de "AVOID mejor, GO peor"
  (contrario a la hipótesis, sostenido 3+ días) a **"GO mejor, AVOID
  negativo"** — casi el opuesto exacto de lo que se reportaba ayer como
  el hallazgo más fuerte del bus. Esto, junto con el mismo tipo de
  reversión en `buy-retest.md` (ver ahí: SA=WAIT pasa a ser la mejor
  rama), confirma que el cruce SA↔resultado-scalp **no es una relación
  estable** de una corrida a otra con el n actual — es una correlación
  ruidosa, no una regla para filtrar señales en vivo. Bajar la prioridad
  de formalizar esto en `experiments.json` hasta que se sostenga en la
  misma dirección 3+ corridas seguidas (todavía no ha pasado ni una vez).

### Decaimiento
`decay_weekly` (global, no por segmento): 2026-W36 n=3183 WR 44.7%
E[R]=-0.018 (bajó de n=3231, ver nota de anomalía en `buy-retest.md`);
2026-W37 n=3856 WR 46.4% E[R]=**+0.042** (subió de n=2427, sigue positivo,
bajó un poco de +0.069). Sin señal de decaimiento.

## Histórico de cambios
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
