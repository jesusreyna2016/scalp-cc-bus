# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-05 · n: 772)

### ⚠ Nota de proceso — data restaurada hoy
Ver el detalle completo en `buy-retest.md` (misma corrida): el commit
`92917b8` había borrado 1256 de 1280 señales de `signals/2026-09-03.jsonl`
bajo el mensaje engañoso "heal 24 orphan signal(s)". Se restauró sin
pérdida desde `f239309`. El salto de n de hoy (687→772 en SHORT, todo el
dataset 1884→3140) es esa corrección, no señales nuevas — varias métricas
de abajo cambian de signo simplemente por volver a incluir un día entero
de datos legítimos que faltaban.

### Veredicto global
n=772 (465×1m, 214×2m, 93×5m; +85 vs la lectura de ayer, que estaba sobre
datos truncados). Crudo: 1m WR 43.7% E[R]=-0.004 PF=0.99 (219 SL de 465,
casi breakeven, igual lectura que ayer); 2m WR 41.6% E[R]=**-0.106**
PF=0.8 (108 SL de 214, más negativo que ayer -0.08); 5m WR 49.5%
E[R]=**-0.007** PF=0.99 (41 SL de 93) — **el 5m cruza a negativo por
primera vez** (venía de 0.687→0.088→0.03→-0.007), tres lecturas
consecutivas cayendo confirman que el "TOMAR" original (n=18) era
varianza de muestra chica: el edge se ha diluido hasta desaparecer del
todo, no solo perder significancia. `segment_significance`: 1m
CI90=[-0.097,0.08] p=0.542, 2m CI90=[-0.226,0.019] p=0.922 (roza
certificar en negativo), 5m CI90=[-0.191,0.21] p=0.53 — ninguno certifica.
Veredicto sin cambios: **NINGÚN TF certifica** — el filtro de contexto
(`nearEdge`) sigue siendo el hallazgo más accionable para el volumen
grande (1m/2m).

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna tiene `survives_fdr10=true` (esa prueba corre por tf/kind/side, no
por estos cortes) — el gradiente de `nearEdge` se mantiene estable por
cuarta revisión seguida, pero `tier=B` pierde su ventaja:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | mejor que `edge=0` mejor que `edge=-1` | 65 / 327 / 380 | WR 55.4%/43.1%/42.4%; E[R] +0.11/-0.005/-0.08; PF 1.27/0.99/0.85 | **alta** — gradiente monótono estable por cuarta revisión seguida; `edge=1` no cambió de n (sin señales nuevas en esa rama) |
| 2 | `nearEdge=-1` | FILTRAR / no tomar | 380 | E[R]=-0.08, PF 0.85, WR 42.4% | moderada — se puso más negativo que ayer (-0.048), sigue siendo la peor rama |
| 3 | símbolo (`cross_instrument`), 1m | **vuelve a `instrument-specific`** — ya no generalizar | spread 0.469 (NQ 0.104, YM 0.087, ES 0.003, GC -0.152, CL **-0.365**) | CL vuelve a destacar muy negativo | moderada — cambio de dirección vs ayer (`universal` con spread 0.264); vigilar 1-2 corridas más antes de decidir si esto se asienta |
| 3b | símbolo, 2m | sigue `universal` | spread 0.339 (NQ 0.005, GC -0.09, YM -0.121, ES -0.18, CL -0.334) | ninguno se dispara, todos negativos o planos | alta — mismo veredicto que ayer, spread creció un poco (0.185→0.339) pero sigue bajo el umbral de 0.4 |
| 3c | símbolo, 5m | sigue sin poder generalizarse | GC -0.532, YM -0.08, ES 0.022, CL 0.015, NQ 0.181 (spread 0.713, `instrument-specific`) | GC sigue siendo el más negativo con diferencia | moderada — mismo veredicto que ayer, GC se puso todavía más negativo |
| 4 | `tier=B` | **YA NO es TOMAR — se puso negativo** | 338 (antes 294) | WR 47.3% E[R]=**-0.032** PF=0.93 (antes E[R]=+0.02) | baja — se invirtió con la muestra restaurada, ver nota abajo, no usar como regla hasta que se estabilice |
| 5 | `tier=A+` | normalizado, en línea con B/C | 57 (sin cambio, sin señales A+ SHORT nuevas hoy) | WR 24.6%, E[R]=+0.003, PF=1.0 | confirmado — idéntico a ayer, el caso sigue cerrado |

**`tier=B` pierde su ventaja al restaurar el dato.** Las 3 revisiones
previas mostraban a B como la mejor rama de tier con E[R] positivo
(+0.02 ayer). Con las señales de 2026-09-03 restauradas, B pasa a
E[R]=-0.032 — casi empatado con C (-0.038). Esto es evidencia de que la
lectura anterior dependía en parte de un día de datos que faltaba, no de
una ventaja estructural real. Se retira "TOMAR tier B" como regla activa
hasta que se sostenga 1-2 revisiones más con dato completo.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara.

### Gestión
- **La escalera + parciales (`managed_vs_naive`) sigue ayudando en los
  tres TF de SELL RETEST**: 1m n=433 delta=+0.142 (naive 0.0→managed
  0.142); 2m n=203 delta=+0.121 (naive -0.106→managed 0.015, rescata casi
  toda la pérdida cruda); 5m n=86 delta=+0.24 (naive -0.013→managed 0.227,
  el delta más grande de los tres TF). Se confirma el contraste con BUY
  RETEST, donde en 5m la escalera resta (ver `buy-retest.md`).
- **SL estructural (`sl_origin_vs_layer`) RECUPERA la certificación en 1m
  que había perdido ayer** — con el dato restaurado: 1m n=219 delta=+0.296
  **CI90=[0.013,0.633], vuelve a batir cero** (ayer, con datos truncados:
  n=169 delta=+0.22 CI90 cruzaba cero); 5m n=61 delta=+1.145
  CI90=[0.013,3.032] sigue batiendo cero (efecto más grande del dataset,
  aunque CI muy ancho); 2m n=123 delta=+0.226 CI90=[-0.046,0.505] sigue
  sin certificar, muy cerca del borde. **La propuesta de `experiments.json`
  (`sl-retest-wick-2026-09-03`) vuelve a estar soportada en 1m y 5m SHORT.**
  Novedad importante: con el dato restaurado, **1m LONG también certificó
  hoy por primera vez** (ver `buy-retest.md`) — el experimento ya no se
  limita a SHORT, se amplió el segmento en `experiments.json` a todo
  RETEST. El agregado global por `basis` (`retestBar`, n=2200) ya no
  mezcla una rama plana con una real: LONG y SHORT certifican ambos en 1m
  hoy, aunque se pide un día más de confirmación (ver nota de arriba).
- `revAfterSL_rate`: sin cambio material (agregado global) — las pérdidas
  lejos de noticias siguen revirtiendo más.
- Parcial 1 / trailing: _pendiente_ de cortar por side en el contrafactual
  global.

### Contextos a evitar
- `nearEdge=-1` (regla #2). `tier=A+` sigue sin ser un contexto a evitar
  por sí solo (regla #5, confirmado normalizado). `tier=B` ya NO es un
  contexto a favor (ver nota arriba) pero tampoco es peor que C — neutral.
- Autopsia de SL sobre las 368 pérdidas SHORT (desglose permanente por
  kind/side, sin cap de 60 filas): `contra-estructura` 143/368 (39%) y
  `stop-en-el-minimo` 143/368 (39%) empatados en el liderazgo, con
  `RR-bajo` 137/368 (37%) muy cerca — mismo casi-empate de las revisiones
  anteriores, estable pese a la restauración de datos. Ninguna causa está
  mitigada todavía por un experimento `confirmed` — sigue bloqueando el
  gate de ejecución.
- **Cruce con Session Analyst — cuantificado por primera vez hoy.** Mejora
  permanente en `analyze.py`: `session_analyst_cross` parsea el veredicto
  GO/WAIT/AVOID de cada plan (`pre-asia/pre-london/pre-ny`) por símbolo y
  lo cruza con el resultado real de las señales scalp de ese
  símbolo+sesión+día (join por fecha+killzone, n=885 pares cruzados de
  todo `kind/side`, todavía sin desglosar por SELL RETEST específicamente).
  **Resultado sorprendente, CONTRARIO a la hipótesis de
  `agent-instructions.md`**: las señales en un instrumento marcado `AVOID`
  rindieron MEJOR (n=92, E[R]=+0.204, WR 56.5%, PF 1.47) que las marcadas
  `GO` (n=122, E[R]=**-0.273**, WR 37.7%, PF 0.56) o `WAIT` (n=671,
  E[R]=-0.014). Sin prueba de significancia todavía y sin desglose por
  kind/side/tf — no generalizar ni usarlo para filtrar señales todavía,
  pero es exactamente el tipo de contradicción con el Session Analyst que
  `agent-instructions.md` pide vigilar. Próximo paso: bootstrap CI por
  veredicto y desglose por kind/side antes de proponer nada.

### Decaimiento
Sólo 2026-W36 en `decay_weekly` (n=3140 en todo el dataset tras la
restauración) — sin semana previa para comparar decaimiento real todavía.

## Histórico de cambios
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
