# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-10 · n: 2100)

### Nota de proceso — salto grande de dato nuevo, ver `buy-retest.md`
Mismo pull/analyze que `buy-retest.md`: el bus terminó de asentar
`signals/outcomes/2026-09-08.jsonl`. En este playbook: n 1368→2100
(**+732**; 1m 847→1295, 2m 385→612, 5m 136→193). SL nuevos: 631-422=209 en
1m, 301-192=109 en 2m, 94-59=35 en 5m — a diferencia del día de calma de
ayer, hoy sí llegaron pérdidas nuevas en volumen.

### Veredicto global — **reversión de signo en los tres TF**
1m WR 42.8% E[R]=**+0.051** PF=1.1 (ayer -0.048); 2m WR 45.6% E[R]=**+0.057**
PF=1.11 (ayer -0.068); 5m WR 46.1% E[R]=**+0.02** PF=1.04 (ayer -0.027).
Los tres TF pasaron de negativo a positivo con el salto de muestra de hoy
— revierte la lectura estable de las últimas 5-6 corridas ("sexta lectura
consecutiva confirmando que el TOMAR original era ruido"). `segment_significance`
también se movió hacia positivo sin certificar: 1m CI90=[-0.008,0.111]
p=0.083 n=1245 (el límite inferior casi toca cero, la más cerca de
certificar de los tres); 2m CI90=[-0.026,0.142] p=0.138 n=599; 5m
CI90=[-0.139,0.188] p=0.408 n=184. **No tratar este giro como un nuevo
veredicto** — es exactamente el mismo patrón de reversión con salto de
muestra ya visto varias veces en este dataset (ej. `tier=A+` en
`buy-retest.md`, `2m/RETEST/LONG` el 09-08): vigilar 1-2 corridas más
antes de cambiar el veredicto de "ningún TF certifica".

### Reglas condicionales (IF contexto ENTONCES acción)
**El gradiente de `nearEdge` que estaba estable hace 4 revisiones se
invirtió con la muestra de hoy** — tratar como no confiable hasta que se
re-asiente:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=0` | ahora la MEJOR rama (antes era "FILTRAR/no tomar") | 783 (+351) | WR 43.6%, E[R]=**+0.113**, PF=1.22 | **baja — reversión completa de la regla #2 anterior (E[R] pasó de -0.087 a +0.113 con +351 pares); no accionar todavía, vigilar 1-2 corridas** |
| 2 | `nearEdge=-1` | pasó de negativo a levemente positivo | 1238 (+367) | E[R] +0.012 (antes -0.046), WR 43.5%, PF 1.02 | baja — mismo patrón de reversión que la regla #1 |
| 3 | `nearEdge=1` | ya no es la mejor rama (lo era hace 4 corridas) | 79 (+14) | WR 53.2%, E[R]=+0.022 (antes +0.11), PF 1.05 | baja — sigue siendo la rama con mejor WR pero el E[R] se diluyó mucho |
| 4 | símbolo (`cross_instrument`), 1m | sigue `instrument-specific` | spread 0.677 (NQ 0.116, YM 0.13, ES 0.037, GC -0.001, CL -0.547, n=43) | CL se sostiene como el peor símbolo, spread se ensanchó un poco (0.632→0.677) | moderada — segunda corrida seguida con CL claramente peor |
| 5 | `tier=A+` | **se dio vuelta a fuertemente positivo** | 151 (+59) | WR 27.2%, E[R]=**+0.185**, PF=1.29 (antes E[R]=-0.001) | baja — mismo patrón de reversión con muestra nueva, no tratar como asentado; WR sigue muy bajo |
| 6 | `tier=B` | sigue sin ser TOMAR — casi plano | 1015 (+277) | WR 46.4% E[R]=**-0.001** PF=1.0 (antes -0.039) | baja — se acercó a cero pero sigue sin ser una ventaja clara |

**Lectura de método del día**: prácticamente todos los cortes de este
playbook (nearEdge, tier, el TF crudo) cambiaron de signo o se movieron
mucho hoy con el salto de +732 pares. Es la muestra más grande y volátil
de una sola corrida desde el 09-08 — tratar TODAS las lecturas de hoy como
provisionales y esperar 1-2 corridas más antes de fijar cualquier regla
nueva o retirar una vieja.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara.

### Gestión
- **La escalera + parciales (`managed_vs_naive`) sigue ayudando en los
  tres TF de SELL RETEST**, aunque el margen se redujo con la muestra
  nueva: 1m n=1238 delta=**+0.123** (antes +0.172), 2m n=599 delta=**+0.116**
  (antes +0.137), 5m n=183 delta=**+0.084** (antes +0.181) — sigue siendo
  positivo en los tres, pero conviene vigilar si sigue bajando. Se
  confirma el contraste con BUY RETEST, donde en 5m la escalera resta (ver
  `buy-retest.md`).
- **SL estructural (`sl_origin_vs_layer`)**: las tres combinaciones de TF
  con muestra útil en SHORT **siguen certificando positivo**, pero con
  deltas más chicos que ayer al crecer la muestra: 1m n=898 (+384)
  delta=**+0.181** CI90=[0.027,0.33] (antes +0.417, bajó bastante pero
  sigue sin cruzar cero); 2m n=462 (+202) delta=**+0.149**
  CI90=**[0.001,0.313]** (antes +0.245, el límite inferior quedó casi en
  cero — certifica al filo, vigilar); 5m n=149 (+54) delta=**+0.734**
  CI90=[0.034,1.63] (antes +0.784, sigue siendo el efecto más grande del
  dataset). La propuesta de `experiments.json`
  (`sl-retest-wick-2026-09-03`) sigue siendo la más sólida en SHORT, pero
  hoy es la primera vez que se ve el delta contraerse en las tres TF a la
  vez con muestra nueva — ver `experiments.json.next_steps` (actualizado
  hoy).
- `revAfterSL_rate` por corte: `edge=-1` 27.4%, `edge=0` 34.2%, `edge=1`
  57.6% — patrón sin gradiente limpio, igual que el resto de los cortes
  hoy.
- Parcial 1 / trailing: _pendiente_ de cortar por side en el contrafactual
  global.

### Contextos a evitar
- Con la reversión de `nearEdge` de hoy (ver Reglas condicionales), no hay
  un contexto claro a evitar en este corte por ahora — esperar a que se
  re-asiente. `tier=A+` sigue sin ser un contexto a evitar por sí solo
  (regla #5, WR bajo pero E[R] ahora positivo).
- Autopsia de SL sobre las 1026 pérdidas SHORT (+353 vs ayer):
  `contra-estructura` 339/1026 (33.0%) y `RR-bajo` 338/1026 (33.0%) quedan
  prácticamente empatados en primer lugar, `stop-en-el-minimo` 317/1026
  (30.9%) muy cerca detrás — se sostiene el casi-empate de tres causas ya
  visto ayer, mismo orden aproximado. Ninguna causa está mitigada todavía
  por un experimento `confirmed` — sigue bloqueando el gate de ejecución.
- **Cruce con Session Analyst — este es el hallazgo más fuerte de todo el
  bus hoy, y ya sale en `report.alerts`.** Agregado de todo `kind/side`
  (n_matched creció con la muestra): `AVOID` **E[R]=+0.122
  CI90=[0.045,0.193] (n=637, no cruza cero)** — se moderó un poco desde
  +0.175 pero sigue certificando con más muestra; `GO` **E[R]=-0.196
  CI90=[-0.301,-0.08] (n=219, no cruza cero) — cifra IDÉNTICA a ayer, cero
  señales nuevas bajo veredicto GO en todo el bus hoy pese al salto de
  +1203 pares totales**, algo a notar: casi todo el dato nuevo de hoy cayó
  bajo AVOID o WAIT, no GO; `WAIT` E[R]=+0.011 (n=958, sin certificar). La
  hipótesis original de `agent-instructions.md` ("AVOID rinde peor") sigue
  **refutada, con muestra más grande y CI90 más angosto**: AVOID rinde
  mejor, GO rinde peor, de forma no-random. Desglose por kind/side en
  RETEST/SHORT (`by_kind_side`): `AVOID` n=354 (+150) E[R]=+0.067 PF=1.14
  (WR 47.5%, bajó de 51.0% pero se mantiene positivo); `GO` n=40 (sin
  cambio) E[R]=**-0.221** PF=0.61 (WR 32.5%) — mismo sentido que el
  agregado, sin pares GO nuevos en este segmento tampoco; `WAIT` n=549
  (+42) E[R]=-0.025 (WR 45.9%). **Sigue sin usarse para filtrar señales en
  vivo** — es una correlación cruzada, no causalidad probada — pero al
  tercer día consecutivo de certificar con CI90 que no cruza cero es
  candidato serio a formalizarse en `experiments.json` en la próxima
  revisión semanal (domingo 2026-09-13) si se sostiene.

### Decaimiento
`decay_weekly` ahora reporta: 2026-W36 (n=3231, WR 44.6%, E[R]=-0.021) y
2026-W37 (n=2427, WR 46.6%, E[R]=**+0.069**, antes +0.016 con n=1224) —
mismo giro a positivo que se ve en `buy-retest.md`, sin señal de
decaimiento (no hay caída de WR > 15 pts). Con la volatilidad de hoy en
casi todos los cortes, tratar la semana en curso como no asentada todavía.

## Histórico de cambios
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
