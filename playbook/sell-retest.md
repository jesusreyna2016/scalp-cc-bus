# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-08 · n: 1341)

### Nota de proceso — segundo día limpio, sin repetición del bug de "heal"
Ver el detalle completo en `buy-retest.md` (misma corrida). Resumen:
`file_integrity_check` sin alertas por segundo día seguido; `git pull`
mostró "forced update" de nuevo (clon superficial), resuelto con
`git reset --hard origin/main` sin pérdida de trabajo. Salto grande de
dato genuinamente nuevo: martes 2026-09-07 fue el primer día hábil
COMPLETO post-feriado.

### Veredicto global
n=1341 (831×1m, 378×2m, 132×5m ; +545 vs ayer, todo dato nuevo real, casi
duplicó la muestra). Crudo: 1m WR 41.8% E[R]=**-0.048** PF=0.91 (422 SL
de 831, algo peor que ayer -0.013); 2m WR 43.4% E[R]=**-0.068** PF=0.87
(192 SL de 378, mejoró bastante vs ayer -0.124); 5m WR 49.2%
E[R]=**-0.027** PF=0.94 (59 SL de 132) — se mantiene negativo, quinta
lectura consecutiva confirmando que el "TOMAR" original (n=18) era
varianza de muestra chica. `segment_significance`: 1m CI90=[-0.116,0.018]
p=0.887, 2m CI90=[-0.157,0.029] p=0.874 (**el CI volvió a cruzar cero
hoy** — ayer estaba del lado negativo [-0.246,-0.001] — mismo patrón de
reversión que en `buy-retest.md` 2m LONG con el salto de muestra de hoy),
5m CI90=[-0.187,0.145] p=0.605 — ninguno certifica. Veredicto: **NINGÚN
TF certifica** (2m pierde la lectura negativa que tenía ayer, ver nota de
método en `buy-retest.md`) — el filtro de contexto (`nearEdge`) sigue
siendo el hallazgo más accionable para el volumen grande (1m/2m).

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna tiene `survives_fdr10=true` (esa prueba corre por tf/kind/side, no
por estos cortes) — el gradiente de `nearEdge` se mantiene estable por
cuarta revisión seguida, pero `tier=B` pierde su ventaja:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | mejor que `edge=0` mejor que `edge=-1` | 65 / 426 / 850 | WR 55.4%/40.8%/43.1%; E[R] +0.11/-0.087/-0.046; PF 1.27/0.84/0.91 | **alta** — `edge=1` sigue exactamente en n=65 (sexta revisión sin señales nuevas en esa rama); el orden edge=-1 vs edge=0 se invirtió levemente (edge=-1 ahora un poco mejor que edge=0) con el salto de dato, vigilar si se sostiene |
| 2 | `nearEdge=0` | FILTRAR / no tomar (peor rama hoy) | 426 | E[R]=-0.087, PF 0.84, WR 40.8% | moderada — con el salto de dato de hoy `edge=0` pasa a ser la peor rama (antes era `edge=-1`); no generalizar todavía, vigilar 1-2 corridas |
| 3 | símbolo (`cross_instrument`), 1m | sigue `instrument-specific` | spread 0.632 (NQ 0.104, YM 0.011, ES -0.02, GC -0.156, CL **-0.528**, n=35) | CL se puso mucho más negativo (-0.365→-0.528) con dato nuevo real | moderada — CL se sostiene como el peor símbolo en 1m, vigilar si se sostiene 1-2 corridas más |
| 4 | `tier=B` | sigue sin ser TOMAR — negativo | 724 (antes 346) | WR 45.6% E[R]=**-0.039** PF=0.92 (antes -0.04) | baja — prácticamente sin cambio con el salto de dato, confirma que retirar "TOMAR tier B" fue correcto |
| 5 | `tier=A+` | prácticamente en línea con B/C | 90 (antes 58) | WR 21.1%, E[R]=**-0.001**, PF=1.0 (antes -0.015) | baja — se mantiene cerca de cero con más muestra, WR muy bajo (21.1%) sigue siendo la señal más fuerte de este tier (ganadores grandes ocasionales) |

**`tier=B` se mantiene negativo y estable con el gran salto de dato de
hoy.** E[R] prácticamente sin cambio (-0.04→-0.039) pese a que n más que
se duplicó (346→724) — confirma con fuerza que retirar "TOMAR tier B"
como regla activa fue correcto, no era ruido de la restauración.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara.

### Gestión
- **La escalera + parciales (`managed_vs_naive`) sigue ayudando en los
  tres TF de SELL RETEST**: 1m n=796 delta=+0.172 (naive -0.046→managed
  0.126, mejoró vs ayer +0.139); 2m n=366 delta=+0.137 (naive
  -0.068→managed 0.069, rescata casi toda la pérdida cruda, sin cambio de
  sentido vs ayer +0.116); 5m n=123 delta=+0.181 (naive -0.032→managed
  0.149, sigue siendo de los deltas más grandes, algo menor que ayer
  +0.237). Se confirma el contraste con BUY RETEST, donde en 5m la
  escalera resta (ver `buy-retest.md`).
- **SL estructural (`sl_origin_vs_layer`)**: 1m sigue certificando, n=514
  delta=**+0.417** **CI90=[0.2,0.644]** — n subió de 229 a 514 con el
  salto grande de dato de hoy, delta se hizo MÁS fuerte (0.283→0.417),
  tercera confirmación independiente y la más sólida hasta ahora; 5m n=95
  delta=+0.784 CI90=[0.064,1.975] sigue batiendo cero (efecto grande del
  dataset, CI sigue ancho pero se redujo bastante); 2m n=260 delta=+0.245
  CI90=[0.035,0.466] **certifica por primera vez** (ayer CI90=[-0.044,0.487]
  cruzaba cero) — con esto las 4 combinaciones tf con muestra útil en
  SHORT (1m, 2m, 5m) certifican positivo. **La propuesta de
  `experiments.json` (`sl-retest-wick-2026-09-03`) queda hoy más sólida
  que nunca en SHORT** — ver `experiments.json.next_steps`.
- `revAfterSL_rate`: sin cambio material (agregado global) — las pérdidas
  lejos de noticias siguen revirtiendo más.
- Parcial 1 / trailing: _pendiente_ de cortar por side en el contrafactual
  global.

### Contextos a evitar
- `nearEdge=0` es hoy la peor rama (regla #2, ver nota de que el orden con
  `edge=-1` se invirtió levemente). `tier=A+` sigue sin ser un contexto a
  evitar por sí solo (regla #5, WR bajo pero E[R]≈0). `tier=B` sigue sin
  ser un contexto a favor (confirmado negativo con el gran salto de dato)
  pero tampoco es peor que C — neutral.
- Autopsia de SL sobre las 673 pérdidas SHORT (desglose permanente por
  kind/side, sin cap de 60 filas): `RR-bajo` 235/673 (34.9%) pasa a ser la
  causa individual más frecuente, muy cerca de `stop-en-el-minimo`
  228/673 (33.9%) y `contra-estructura` 226/673 (33.6%) — sigue siendo un
  casi-empate de tres causas, mismo patrón cualitativo con casi el doble
  de muestra. Ninguna causa está mitigada todavía por un experimento
  `confirmed` — sigue bloqueando el gate de ejecución.
- **Cruce con Session Analyst — hallazgo confirmado hoy con prueba
  estadística real** (mejora permanente en `analyze.py`:
  `session_analyst_cross.by_verdict_ci90` + `by_kind_side`, bootstrap 90%
  CI de E[R]). Agregado de todo `kind/side` (n=1306 cruces, join por
  fecha+killzone+símbolo): `AVOID` **E[R]=+0.183 CI90=[0.08,0.285]
  (n=350, no cruza cero)**, `GO` **E[R]=-0.273 CI90=[-0.423,-0.118]
  (n=121, no cruza cero)**, `WAIT` E[R]=-0.006 (n=834, sin certificar).
  **Esto REFUTA con confianza estadística, por primera vez, la hipótesis
  original de `agent-instructions.md`** ("las señales en un instrumento
  AVOID rinden peor") — es justo lo contrario: AVOID rinde mejor y GO
  rinde peor, de forma no-random. Desglose por kind/side en RETEST/SHORT
  (`by_kind_side`): `AVOID` n=187 E[R]=+0.212 PF=1.49 (WR 55.6%), `WAIT`
  n=507 E[R]=-0.049 (WR 45.4%) — sin celda `GO` con n>=5 en SHORT
  todavía, pero el mismo sentido que el agregado y que RETEST/LONG (ver
  `buy-retest.md`). **Sigue sin usarse para filtrar señales en vivo** —
  es una correlación cruzada, no causalidad probada, y falta ver si es
  estable fuera de muestra — pero es el hallazgo cualitativamente más
  importante de hoy: contradice de forma medible la intuición de partida
  del propio sistema de aprendizaje.

### Decaimiento
`decay_weekly` ya reporta 2 semanas con muestra sustancial: 2026-W36
(n=3231, WR 44.6%, E[R]=-0.021) y 2026-W37 (n=1155, WR 46.3%,
E[R]=-0.016) — mejora leve, sin señal de decaimiento.

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
