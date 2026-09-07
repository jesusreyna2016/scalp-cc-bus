# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-07 · n: 796)

### Nota de proceso — primer día limpio, sin repetición del bug de "heal"
Ver el detalle completo en `buy-retest.md` (misma corrida). Resumen:
`file_integrity_check` confirma que ningún `signals/outcomes/*.jsonl`
encogió hoy — primer día desde la restauración del 2026-09-05/06 sin que
el bug de "heal" vuelva a truncar datos. Llegó dato genuinamente nuevo
(lunes festivo en EE.UU., Globex con volumen reducido).

### Veredicto global
n=796 (479×1m, 221×2m, 96×5m; +24 vs ayer, todo dato nuevo real). Crudo:
1m WR 43.2% E[R]=-0.013 PF=0.97 (226 SL de 479, casi breakeven, sin
cambio material vs ayer -0.004); 2m WR 40.7% E[R]=**-0.124** PF=0.77 (113
SL de 221, algo más negativo que ayer -0.106); 5m WR 47.9%
E[R]=**-0.018** PF=0.96 (42 SL de 96) — se mantiene negativo, cuarta
lectura consecutiva confirmando que el "TOMAR" original (n=18) era
varianza de muestra chica: el edge sigue sin reaparecer con dato nuevo.
`segment_significance`: 1m CI90=[-0.101,0.069] p=0.614, 2m
CI90=[-0.246,-0.001] p=0.953 (ya no roza cero, queda del lado negativo,
con dato genuinamente nuevo hoy), 5m CI90=[-0.209,0.194] p=0.561 —
ninguno certifica. Veredicto sin cambios: **NINGÚN TF certifica** — el
filtro de contexto (`nearEdge`) sigue siendo el hallazgo más accionable
para el volumen grande (1m/2m).

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna tiene `survives_fdr10=true` (esa prueba corre por tf/kind/side, no
por estos cortes) — el gradiente de `nearEdge` se mantiene estable por
cuarta revisión seguida, pero `tier=B` pierde su ventaja:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | mejor que `edge=0` mejor que `edge=-1` | 65 / 335 / 396 | WR 55.4%/42.4%/41.7%; E[R] +0.11/-0.025/-0.088; PF 1.27/0.95/0.84 | **alta** — gradiente monótono estable por quinta revisión seguida; `edge=1` sigue exactamente en n=65 (sin señales nuevas en esa rama, ni con el dato de hoy) |
| 2 | `nearEdge=-1` | FILTRAR / no tomar | 396 | E[R]=-0.088, PF 0.84, WR 41.7% | moderada — prácticamente sin cambio vs ayer (-0.08), sigue siendo la peor rama |
| 3 | símbolo (`cross_instrument`), 1m | sigue `instrument-specific` | spread 0.469 (NQ 0.104, YM 0.093, ES 0.003, GC -0.189, CL **-0.365**, n=26) | CL sigue destacando muy negativo, cifras idénticas a ayer | moderada — sin cambio (ni CL tuvo señales nuevas hoy, n=26 igual) — vigilar 1-2 corridas más antes de decidir si esto se asienta |
| 3b | símbolo, 2m | sigue `universal` | spread 0.339 (NQ 0.005, GC -0.012, YM -0.121, ES -0.18, CL -0.334) | ninguno se dispara, todos negativos o planos | alta — mismo veredicto y spread que ayer, sin señales nuevas en este corte |
| 3c | símbolo, 5m | sigue sin poder generalizarse | GC -0.568 (n=14), YM -0.08 (n=17), ES 0.022 (n=24), CL 0.015 (n=6), NQ 0.181 (n=35) (spread 0.749, `instrument-specific`) | GC sigue siendo el más negativo con diferencia, se puso un poco peor (-0.532→-0.568) | moderada — mismo veredicto que ayer, con dato nuevo real |
| 4 | `tier=B` | sigue sin ser TOMAR — negativo | 346 (antes 338) | WR 46.5% E[R]=**-0.04** PF=0.92 (antes -0.032) | baja — se mantiene negativo con dato nuevo, confirma que no era ruido de la restauración; sigue sin usarse como regla |
| 5 | `tier=A+` | prácticamente en línea con B/C, se movió un poco | 58 (antes 57, +1 señal nueva) | WR 24.1%, E[R]=**-0.015**, PF=0.98 (antes +0.003) | baja — primer cambio de signo en varias revisiones, sigue siendo n chico, el caso sigue considerándose normalizado (cerca de cero) |

**`tier=B` se mantiene negativo con dato nuevo.** La lectura de ayer
(E[R]=-0.032) ya había corregido la lectura previa de "B es la mejor
rama". Hoy, con trades genuinamente nuevos, B sigue negativo (-0.04) y
sigue casi empatado con C (-0.054) — confirma que retirar "TOMAR tier B"
como regla activa fue correcto, no era ruido de la restauración.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara.

### Gestión
- **La escalera + parciales (`managed_vs_naive`) sigue ayudando en los
  tres TF de SELL RETEST**: 1m n=444 delta=+0.139 (naive -0.01→managed
  0.129, casi sin cambio vs ayer +0.142); 2m n=209 delta=+0.116 (naive
  -0.124→managed -0.008, rescata casi toda la pérdida cruda, sin cambio
  vs ayer +0.121); 5m n=87 delta=+0.237 (naive -0.025→managed 0.213, el
  delta más grande de los tres TF, sin cambio vs ayer +0.24). Se confirma
  el contraste con BUY RETEST, donde en 5m la escalera resta (ver
  `buy-retest.md`).
- **SL estructural (`sl_origin_vs_layer`)**: 1m sigue certificando, n=229
  delta=+0.283 **CI90=[0.011,0.609]** — n subió de 219 a 229 con dato
  genuinamente nuevo, delta prácticamente igual (0.296→0.283); 5m n=62
  delta=+1.127 CI90=[0.012,3.025] sigue batiendo cero (efecto más grande
  del dataset, CI muy ancho, casi sin cambio); 2m n=129 delta=+0.215
  CI90=[-0.044,0.487] sigue sin certificar. **La propuesta de
  `experiments.json` (`sl-retest-wick-2026-09-03`) sigue soportada en 1m y
  5m SHORT, y también en 1m LONG** (ver `buy-retest.md`) — el agregado
  global por `basis` (`retestBar`, n=2284) creció con dato nuevo real y
  sigue sin mezclar una rama plana con una real. Hoy es el primer día que
  cuenta como confirmación independiente genuina (no solo dataset
  restaurado recalculado) — ver `experiments.json.next_steps`.
- `revAfterSL_rate`: sin cambio material (agregado global) — las pérdidas
  lejos de noticias siguen revirtiendo más.
- Parcial 1 / trailing: _pendiente_ de cortar por side en el contrafactual
  global.

### Contextos a evitar
- `nearEdge=-1` (regla #2). `tier=A+` sigue sin ser un contexto a evitar
  por sí solo (regla #5). `tier=B` sigue sin ser un contexto a favor (ver
  nota arriba, confirmado negativo con dato nuevo) pero tampoco es peor
  que C — neutral.
- Autopsia de SL sobre las 381 pérdidas SHORT (desglose permanente por
  kind/side, sin cap de 60 filas): `stop-en-el-minimo` 149/381 (39.1%)
  edge ligeramente por delante de `RR-bajo` 144/381 (37.8%) y
  `contra-estructura` 144/381 (37.8%) — sigue siendo un casi-empate de
  tres causas, estable con dato genuinamente nuevo. Ninguna causa está
  mitigada todavía por un experimento `confirmed` — sigue bloqueando el
  gate de ejecución.
- **Cruce con Session Analyst**: `session_analyst_cross` (n=885 pares
  cruzados de todo `kind/side`, sin cambio de n hoy — no hubo cruces
  nuevos que emparejar) sigue mostrando el resultado sorprendente,
  CONTRARIO a la hipótesis de `agent-instructions.md`: las señales en un
  instrumento marcado `AVOID` rindieron MEJOR (n=92, E[R]=+0.204, WR
  56.5%, PF 1.47) que las marcadas `GO` (n=122, E[R]=**-0.273**, WR 37.7%,
  PF 0.56) o `WAIT` (n=671, E[R]=-0.014). Sin prueba de significancia
  todavía y sin desglose por kind/side/tf — no generalizar ni usarlo para
  filtrar señales todavía, pero es exactamente el tipo de contradicción
  con el Session Analyst que `agent-instructions.md` pide vigilar.
  Próximo paso: bootstrap CI por veredicto y desglose por kind/side antes
  de proponer nada.

### Decaimiento
`decay_weekly` ya reporta 2 semanas: 2026-W36 (n=3231, WR 44.6%,
E[R]=-0.021) y 2026-W37 (n=26, WR 50.0%, E[R]=-0.193) — W37 arrancó ayer,
muestra todavía minúscula para comparar decaimiento real.

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
