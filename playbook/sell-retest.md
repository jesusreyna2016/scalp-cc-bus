# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-04 · n: 687)

### Veredicto global
**Sigue sin certificar ningún TF, y el 5m se sigue moderando hacia el
ruido — confirma la lección de método de ayer.** n=687 (412×1m, 191×2m,
84×5m; +98 desde la revisión anterior). Crudo: 1m WR 44.4% E[R]=+0.015
PF=1.03 (188 SL de 412, casi breakeven); 2m WR 41.9% E[R]=**-0.08**
PF=0.85 (95 SL de 191, sigue negativo como ayer); 5m WR 50.0% E[R]=+0.03
PF=1.06 (36 SL de 84). El 5m — el que había certificado con n=18 y luego
perdió la certificación con n=68 — **sigue cayendo**: E[R] 0.687→0.088→
0.03, CI90=[-0.17,0.254] sigue cruzando cero, `survives_fdr10=false`.
Tres lecturas seguidas convergiendo hacia cero confirman que el
"TOMAR" original (n=18) era varianza de muestra chica, no un edge real que
se está diluyendo. Veredicto sin cambios: **NINGÚN TF certifica** — el
filtro de contexto (`nearEdge`, `tier`) sigue siendo el hallazgo más
accionable para el volumen grande (1m/2m).

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna tiene `survives_fdr10=true` (esa prueba corre por tf/kind/side, no
por estos cortes) — el gradiente de `nearEdge` se mantiene estable por
tercera revisión seguida:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | mejor que `edge=0` mejor que `edge=-1` | 65 / 298 / 324 | WR 55.4%/43.6%/42.9%; E[R] +0.11/+0.006/-0.048; PF 1.27/1.01/0.91 | **alta** — gradiente monótono estable por tercera revisión, prácticamente sin cambio en los números (era 62/260/267 ayer) |
| 2 | `nearEdge=-1` | FILTRAR / no tomar | 324 | E[R]=-0.048, PF 0.91, WR 42.9% | moderada — estable vs ayer (-0.036), sigue siendo la peor rama |
| 3 | símbolo (`cross_instrument`) | SÍ generalizar en 1m/2m | 1m spread 0.264 `universal` (NQ 116/0.104, GC 79/-0.16, YM 110/0.064, ES 107/0.003); 2m spread 0.185 `universal` (ES 40/-0.18, YM 56/-0.133, GC 33/-0.021, NQ 62/0.005) | ninguno se dispara fuera del resto | alta — se mantiene `universal` en ambos TF con n creciendo, mismo patrón que ayer |
| 3b | símbolo, 5m | **ya no se puede generalizar en 5m** | GC n=12 -0.489, YM n=15 -0.08, ES n=22 0.12, NQ n=35 0.181 (spread 0.67, `instrument-specific`) | nuevo corte — primera vez que 5m tiene n suficiente para evaluar `cross_instrument`; GC destaca muy negativo con n chico, vigilar sin generalizar todavía |
| 4 | `tier=B` | TOMAR, prioridad leve | 294 / 336 (tier C) | WR 49.3% vs 43.5%; E[R] +0.02 vs -0.038; PF 1.04 vs 0.92 | moderada — se mantiene como mejor rama de tier, márgenes estables vs ayer |
| 5 | `tier=A+` | ya normalizado, en línea con B/C | 57 (antes 54) | WR 24.6%, E[R]=+0.003, PF=1.0 | confirmado — segunda revisión seguida sin volver a ser anómalo, el caso ya se considera cerrado |

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara.

### Gestión
- **La escalera + parciales (`managed_vs_naive`) sigue ayudando en los
  tres TF de SELL RETEST**, con n mucho más grande: 1m n=380 delta=+0.146
  (naive 0.02→managed 0.165, un poco menor que ayer +0.16 pero
  consistente); 2m n=180 delta=+0.091 (naive -0.08→managed 0.011, sigue
  rescatando el segmento negativo, aunque el delta bajó de +0.111); 5m
  n=77 delta=+0.174 (naive 0.023→managed 0.197, subió desde +0.148). Se
  confirma el contraste con BUY RETEST, donde en 5m la escalera resta (ver
  `buy-retest.md`).
- **SL estructural (`sl_origin_vs_layer`) se debilita en 1m, sigue fuerte
  en 5m, no certifica en 2m** — cambio importante vs ayer: 1m n=169
  delta=+0.22 **CI90=[-0.056,0.55], ya NO bate cero** (ayer n=138
  delta=+0.328 sí certificaba); 5m n=52 delta=+1.386 CI90=[0.061,3.601]
  sigue batiendo cero (bajó desde +1.701 pero se mantiene el efecto más
  grande del dataset); 2m n=101 delta=+0.3 CI90=[-0.024,0.651] sigue sin
  certificar, muy cerca del borde. **La propuesta de `experiments.json`
  (`sl-retest-wick-2026-09-03`) sigue siendo válida en 5m, pero ya no en
  1m con la muestra de hoy — hay que actualizar la evidencia antes de la
  revisión semanal.** El agregado global por `basis` (`retestBar`, n=1639,
  ver alerta de hoy) sigue mezclando SHORT con LONG (donde el signo es
  plano) — no usar ese número agregado como evidencia, usar los cortes por
  side de aquí.
- `revAfterSL_rate`: sin cambio material vs ayer (62.9% away-from-news vs
  36.5% near-news, agregado global) — las pérdidas lejos de noticias
  revierten más.
- Parcial 1 / trailing: _pendiente_ de cortar por side en el contrafactual
  global.

### Contextos a evitar
- `nearEdge=-1` (regla #2). `tier=A+` sigue sin ser un contexto a evitar
  por sí solo (regla #5, confirmado normalizado).
- Autopsia de SL sobre las 319 pérdidas SHORT (desglose permanente por
  kind/side, sin cap de 60 filas): `contra-estructura` 127/319 (40%) se
  mantiene como causa **líder**, con `stop-en-el-minimo` 123/319 (39%) y
  `RR-bajo` 121/319 (38%) muy cerca — el mismo casi-empate de las dos
  revisiones anteriores, estable. Ninguna causa está mitigada todavía por
  un experimento `confirmed` — sigue bloqueando el gate de ejecución.
- Hipótesis de cruce con Session Analyst: sigue sin cuantificarse — los
  datos de `session_analyst` en el bus son narrativa de texto libre por
  día/símbolo, no un histórico estructurado de veredictos GO/WAIT/AVOID
  fácil de unir con los outcomes; requeriría una mejora dedicada en
  `analyze.py` para extraer y trackear el veredicto diario por símbolo.
  Pendiente para cuando haya presupuesto de tiempo para esa mejora.

### Decaimiento
Sólo 2026-W36 en `decay_weekly` (n=2400 en todo el dataset) — sin semana
previa para comparar decaimiento real todavía.

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
