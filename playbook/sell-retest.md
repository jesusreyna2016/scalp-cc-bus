# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-16 · n: 4022)

### Nota de proceso — ver `buy-retest.md`
Mismo "forced update" inofensivo de `origin/main` al inicio (shallow
clone), resuelto igual que siempre. n 3889→4022 (**+133**; 1m
2460→2559, 2m 1078→1098, 5m 351→365) — dato genuino, más moderado que
ayer.

### Veredicto global
1m n=2559 (+99) WR 44.8% E[R]=**+0.054** PF=1.11 (prácticamente sin
cambio de +0.055); 2m n=1098 (+20) WR 49.3% E[R]=**+0.088** PF=1.19
(prácticamente sin cambio de +0.089); 5m n=365 (+14) WR 50.1% E[R]=**+0.075**
PF=1.16 (prácticamente sin cambio de +0.077). `segment_significance`:
**1m CI90=[0.013,0.099] p=0.015 n=2432 — sostiene `survives_fdr10=true`
por SEGUNDO día seguido** (ayer certificó por primera vez) — primera
confirmación independiente de esa certificación fresca; **2m
CI90=[0.028,0.149] p=0.009 n=1068 — sostiene `survives_fdr10=true` por
QUINTO día seguido**, sigue siendo la lectura SHORT más duradera del bus;
5m CI90=[-0.033,0.195] p=0.127 n=346 (sigue sin certificar, sin cambio de
fondo). Veredicto actualizado: **1m y 2m siguen certificando FDR
simultáneamente por segundo día** — 1m empieza a verse menos frágil pero
todavía se trata como reciente; 2m sigue siendo la más confiable por
antigüedad; 5m estable, sin señal dura.

### Reglas condicionales (IF contexto ENTONCES acción)

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=-1` | prácticamente sin cambio | 2183 (+95) | E[R] **+0.043** (idéntico a ayer) | moderada — cuarto día seguido sin cambiar de signo |
| 2 | `nearEdge=0` | sigue como la mejor rama en magnitud, baja un poco | 1713 (+38) | WR 48.0%, E[R]=**+0.098** (ayer +0.101) | alta — sexta corrida seguida como el corte más estable de esta tabla |
| 3 | `nearEdge=1` | sigue congelado, casi en breakeven | 126 (+0) | WR 53.2%, E[R]=+0.005 (idéntico a ayer, cero señales nuevas) | baja — n todavía chico, sin movimiento |
| 4 | símbolo (`cross_instrument`), los 3 TF | **CL sigue siendo sistemáticamente el peor símbolo en SELL RETEST en 1m, 2m Y 5m** | 1m CL n=49 E[R]=-0.441; 2m CL n=20 E[R]=-0.422; 5m CL n=9 E[R]=-0.323 (idéntico a ayer, cero trades CL nuevos hoy en ningún TF; `instrument-specific`, spreads 0.545/0.556/0.507) | moderada en 1m (n=49, patrón sostenido varios días) — baja en 2m/5m (n<20, no proponer cambio de regla todavía) |
| 5 | `tier=A+` | sigue subiendo, más moderado | 277 (+22) | WR 27.1%, E[R]=**+0.127** (ayer +0.13, prácticamente igual) | baja — segunda lectura seguida cerca de +0.13, empieza a asentarse pero todavía sin confirmar |
| 6 | `tier=B` | se mantiene positivo | 1773 (+62) | WR 47.9% E[R]=**+0.044** (ayer +0.045), PF=1.09 | moderada — quinto día seguido en positivo |

**Lectura de método**: `nearEdge=0` lleva 6 corridas seguidas como la
rama más estable de toda la tabla. El patrón de `cross_instrument`
(fila 4) se sostiene sin ningún cambio: CL sigue rindiendo mal en SELL
RETEST en las tres temporalidades a la vez — candidato a regla
condicional ("evitar CL en SELL RETEST") una vez que la muestra en
2m/5m crezca de n<20 a n≥20.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara.

### Gestión
- **La escalera + parciales (`managed_vs_naive`) sigue ayudando en los
  tres TF**: 1m n=2425 delta=**+0.112** (sin cambio de fondo); 2m n=1068
  delta=**+0.065** (sin cambio); 5m n=345 delta=**+0.056** (baja un poco
  de +0.061, sin cambio de fondo). Sigue positivo y estable en los tres TF.
- **SL estructural (`sl_origin_vs_layer`)**: 1m sigue certificando,
  n=1971 (+16) delta=**+0.127** CI90=**[0.036,0.226]** (prácticamente
  idéntico a +0.126); **2m sostiene la certificación por segundo día**,
  n=895 (+5) delta=+0.117 CI90=**[0.011,0.221]** (idéntico a ayer en
  delta, el límite inferior sigue muy pegado a cero, 0.011 vs 0.014) —
  se mantiene como candidato débil/al filo, no promoverlo a la propuesta
  formal todavía; 5m sigue siendo el más sólido, casi sin cambio: n=309
  (+4) delta=**+0.554** CI90=[0.148,1.067] (casi idéntico a +0.561). Los
  2 segmentos SHORT propuestos el 09-13 (1m y 5m) se mantienen ambos con
  `delta_beats_zero=true`, sin retroceso; 2m SHORT sigue fuera de la
  propuesta por ahora. Ver `experiments.json` (`sl-retest-wick-2026-09-03`)
  y `reviews/2026-week-37.md`.
- `revAfterSL_rate` por corte: sin desglose nuevo relevante hoy.

### Contextos a evitar
- Autopsia de SL sobre las 1832 pérdidas SHORT (+13 vs ayer): mismo
  orden por cuarto/quinto día seguido — `RR-bajo` 693/1832 (37.8%),
  `stop-en-el-minimo` 655/1832 (35.8%), `contra-estructura` 593/1832
  (32.4%). Ninguna causa mitigada todavía por un experimento `confirmed`.
- **Cruce con Session Analyst**. Desglose por kind/side en RETEST/SHORT
  (`by_kind_side`): `AVOID` n=533 (+17) E[R]=**+0.026** (idéntico a
  ayer) PF=1.05; **`GO` n=196 (+17) E[R]=**+0.231** (idéntico a ayer,
  sigue siendo la mejor rama por lejos)**; `WAIT` n=749 (+28) E[R]=**-0.023**
  (sigue negativo, la peor rama). Sexto+ día seguido con "GO mejor, WAIT
  peor" — patrón **opuesto** al de `buy-retest.md` (donde WAIT es la
  mejor rama y GO la peor). Ver la nota global en `buy-retest.md`: el
  hallazgo agregado "WAIT rinde mejor" de `agent-instructions.md`
  esconde esta asimetría por lado y no debe generalizarse a SELL RETEST
  sin mirar esta tabla.

### Decaimiento
`decay_weekly` (global, no por segmento): 2026-W36 n=3140 WR 44.8%
E[R]=-0.016 (sin cambio, ya no perdió muestra — ver `buy-retest.md`);
2026-W37 n=5375 WR 46.9% E[R]=**+0.071** (bajó de n=5376 por -1, dedup
ya conocido, vigilar si sigue bajando); 2026-W38 n=1072 (subió fuerte de
787) WR 46.5% E[R]=**+0.096** — semana en curso.

## Histórico de cambios
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
