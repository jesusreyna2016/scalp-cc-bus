# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-03 · n: 589)

### Veredicto global
**El 5m se DES-certifica — lección de método, no de mercado.** n=589
(356× 1m, 165× 2m, 68× 5m; +367 desde la revisión anterior). Crudo: 1m WR
47.8% E[R]=+0.026 PF=1.05 (básicamente breakeven); 2m WR 43.6%
E[R]=**-0.087** PF=0.84 (se pone negativo, antes era +0.087); 5m WR 55.9%
E[R]=+0.088 PF=1.2. **El 5m — el único segmento que había certificado en
`segment_significance` la revisión anterior (`survives_fdr10=true` con
n=18, WR 88.9%, E[R]=0.687)** ya no certifica con n=68: E[R] cayó a 0.088,
CI90=[-0.139,0.332] vuelve a cruzar cero, `survives_fdr10=false`. Esto **no
es necesariamente que el edge haya desaparecido** — es la prueba de que la
regla del método (no declarar TOMAR hasta que sobreviva FDR con muestra
seria) estaba bien puesta: n=18 con WR 88.9% era, en retrospectiva,
mayormente varianza de muestra chica. Veredicto revisado: **NINGÚN TF de
SELL RETEST certifica hoy** — bajar 5m de TOMAR a "vigilar, no confirmado".
2m pasa a ser el TF con peor lectura cruda (-0.087, antes positivo) aunque
tampoco certifica (CI90=[-0.225,0.052], p_mean_le_0=0.856, roza el lado
negativo). El filtro de contexto (`nearEdge`, `tier`) sigue siendo el
hallazgo más accionable para el volumen grande (1m/2m), y ahora con
`cross_instrument` en `universal` para ambos — mejor confianza que antes.

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna tiene `survives_fdr10=true` (esa prueba corre por tf/kind/side, no
por estos cortes) — pero con n ya en cientos, el gradiente de `nearEdge` es
un patrón práctico fuerte:

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | mejor que `edge=0` mejor que `edge=-1` | 62 / 260 / 267 | WR 58.1%/46.9%/45.7%; E[R] +0.11/+0.015/-0.036; PF 1.27/1.03/0.93 | **alta** — n≥62 en las tres ramas (antes 48-125), gradiente monótono estable desde hace 2 revisiones, y `cross_instrument` marca 1m y 2m `universal` (ver regla #3) |
| 2 | `nearEdge=-1` | FILTRAR / no tomar | 267 | E[R]=-0.036, PF 0.93, WR 45.7% | moderada — ya no tan negativo como antes (-0.233 con n=48), se moderó con más muestra pero se mantiene la peor rama |
| 3 | símbolo (`cross_instrument`) | SÍ generalizar en 1m/2m | 1m spread 0.335 `universal` (NQ 78/0.175, GC 77/-0.16, YM 102/0.064, ES 99/0.013); 2m spread 0.194 `universal` (ES 40/-0.18, YM 52/-0.133, GC 31/-0.021, NQ 42/0.014) | ninguno se dispara fuera del resto | alta — a diferencia de BUY RETEST (donde CL/YM sí divergen fuerte), en SELL RETEST el filtro por `nearEdge`/`tier` no necesita cortarse por símbolo en 1m/2m |
| 4 | `tier=B` | TOMAR, prioridad leve | 242 / 293 (tier C) | WR 52.9% vs 47.1%; E[R] +0.019 vs -0.02; PF 1.04 vs 0.96 | moderada — sigue siendo la mejor rama de tier, aunque el margen se redujo mucho vs la revisión anterior (era +0.216 vs +0.081) |
| 5 | `tier=A+` | **la "anomalía" se moderó fuerte — ya NO es catastrófica** | 54 (antes 16) | WR 25.9%, E[R]=+0.04, PF=1.06 | ver corrección abajo — con n×3.4 el resultado dejó de ser el peor del dataset y pasó a estar en línea con B/C |

**Corrección de la anomalía anterior — `tier=A+` en SELL RETEST.** La
revisión anterior reportó A+ como el peor resultado de todo el dataset
(n=16, WR 6.2%, E[R]=-0.743) y lo marcó como posible error de diseño en
Pine. Con n=54 (×3.4) el resultado se normalizó: WR 25.9%, E[R]=+0.04 — en
línea con tier B (+0.019) y C (-0.02), ya no invertido ni catastrófico.
**Lectura correcta: el hallazgo de la revisión anterior era en gran parte
ruido de n=16**, exactamente el tipo de lectura prematura que
`survives_fdr10` está diseñado para filtrar (nunca certificó). Se retira
la recomendación urgente de auditar la fórmula de tier A+ en Pine — sigue
mereciendo una mirada porque A+ no es "premium" tampoco aquí (no bate a
B), pero ya no es una alarma. **Distinto es el caso de BUY RETEST**, donde
`tier=A+` con n=13 muestra el mismo patrón invertido con la magnitud
extrema de antes (E[R]=-0.705) — ver `buy-retest.md`; se vigila por
separado, sin mezclar el diagnóstico de ambos sides.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin dar señal clara.

### Gestión
- **La escalera + parciales (`managed_vs_naive`) ayuda en los tres TF de
  SELL RETEST, incluido 2m** (se corrige lo de la revisión anterior: el
  delta negativo en 2m era también muestra chica): 1m n=349 delta=+0.16
  (naive 0.031→managed 0.191), 2m n=162 delta=+0.111 (naive -0.087→managed
  0.024, la escalera rescata un segmento que en crudo es negativo), 5m
  n=67 delta=+0.148 (naive 0.081→managed 0.23). Contraste claro con BUY
  RETEST, donde la escalera no ayuda o perjudica (ver `buy-retest.md`).
- **SL estructural (`sl_origin_vs_layer`) gana en 1m y 5m, no en 2m**: 1m
  n=138 delta=+0.328 CI90=[0.009,0.722] bate cero; 5m n=42 delta=+1.701
  CI90=[0.076,4.452] bate cero (el efecto más grande del dataset, aunque
  con n moderado); 2m n=83 delta=+0.289 CI90=[-0.021,0.632] casi bate cero
  pero no formalmente. El agregado por `basis` (`retestBar`, n=517) que
  dispara la alerta de hoy mezcla estos tres TF con LONG — el efecto real
  y significativo está en SHORT/1m y SHORT/5m, no generalizar a LONG (ver
  `buy-retest.md`, donde el signo es plano/contrario).
- `revAfterSL_rate`: 62.9% away-from-news vs 36.5% near-news (agregado
  global) — las pérdidas lejos de noticias revierten más, apunta a SL
  ajustado más que a dirección equivocada.
- Parcial 1 / trailing: _pendiente_ de cortar por side en el contrafactual
  global.

### Contextos a evitar
- `nearEdge=-1` (regla #2). `tier=A+` ya no clasifica aquí (ver
  corrección arriba) — sigue sin ser la mejor rama, pero no es un contexto
  a evitar por sí solo.
- Autopsia de SL sobre las 286 pérdidas SHORT (desglose permanente por
  kind/side, sin cap de 60 filas — mejora de hoy en `analyze.py`):
  `contra-estructura` 126/286 (44%) pasa a ser la causa **líder**, muy
  cerca de `stop-en-el-minimo` 118/286 (41%) y `RR-bajo` 107/286 (37%) —
  el empate exacto de la revisión anterior (40/94 y 40/94) se rompió
  ligeramente a favor de contra-estructura con la muestra más grande.
  `estirado` 60/286 (21%) y `sin-nivel-detras` 55/286 (19%) crecen en
  proporción relativa. Ninguna causa está mitigada todavía por un
  experimento `confirmed` — sigue bloqueando el gate de ejecución.
- Hipótesis de cruce con Session Analyst: sigue sin cuantificarse —
  mejora permanente pendiente para la próxima revisión semanal.

### Decaimiento
Sólo 2026-W36 en `decay_weekly` (n=943 en todo el dataset) — sin semana
previa para comparar decaimiento real todavía. La caída de 5m dentro de la
misma semana (n=18→68) es un recordatorio de que "decaimiento" real
necesita comparar semanas completas, no cortes parciales del mismo run.

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
