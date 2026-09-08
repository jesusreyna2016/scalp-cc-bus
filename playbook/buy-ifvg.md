# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-08 · n: 77)

### Nota de proceso
Segundo día sin repetición del bug de "heal" (ver `buy-retest.md` para el
detalle completo, incluida la nota de `git pull "forced update"` resuelta
con `git reset --hard origin/main`). Llegó dato nuevo genuino del primer
día hábil completo post-feriado, aunque este segmento sigue creciendo
lento por ser prioridad 2.

### Veredicto global
1m n=50 (WR 46.0%, E[R]=+0.212, PF=1.48, 21 SL); 2m n=20 (WR 35.0%,
E[R]=-0.344, PF=0.47, 13 SL, empeoró vs -0.271 con 2 señales nuevas); 5m
n=7 (WR 100%, E[R]=+0.646, PF=99, todavía sin valor estadístico, n creció
de 6 a 7). `segment_significance`: 1m CI90=[-0.103,0.534] p_mean_le_0=0.162
(n=49), se alejó más del borde de significancia (era p=0.116 ayer) pero
sigue en la misma dirección positiva; 2m CI90=[-0.675,0.027] p=0.942, el
límite superior se acerca a cero por primera vez pero sigue sin certificar
sobre el lado negativo. Prioridad 2 se mantiene; el 1m sigue siendo el
único con algo de lectura útil.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar, pero ya hay lectura por corte:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | mejor que `edge=0`; `edge=-1` creció de n=1 a n=4 | 38 / 35 / 4 | WR 47.4%/48.6%/50.0%; E[R] +0.141/+0.028/+0.455; PF 1.34/1.06/1.91 | baja-moderada — orden edge=1 vs edge=0 se invirtió levemente (antes edge=1 mejor con más margen), n sigue chico en todas las ramas |
| 2 | `tier=B` | mejor que `tier=C` | 20 / 57 | E[R] +0.268 vs +0.051; PF 1.67 vs 1.11 | baja-moderada — mismo sentido que ayer, ambas ramas crecieron un poco (18→20, 48→57) |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- `managed_vs_naive`: 1m n=49 delta=**+0.139** (naive 0.212→managed 0.35,
  ayuda, en línea con ayer +0.113); 2m n=20 delta=+0.027 (naive
  -0.344→managed -0.317, sigue negativo, casi sin cambio); 5m n=7
  delta=+0.141 (naive 0.646→managed 0.787, ayuda, n todavía mínimo).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=49
  delta=+0.19 CI90=[-0.38,0.816] no certifica, casi sin cambio; 2m
  **n llegó a 20 (el piso mínimo del método) y AHORA CERTIFICA**:
  delta=**+1.538** CI90=**[0.243,3.13]**, no cruza cero — primera vez que
  esta rama entra en territorio "tratable como real" según el criterio de
  `agent-instructions.md` (n>=20 + CI90 no cruza cero), aunque sigue
  siendo prioridad 2 y el efecto es enorme para un n tan chico (vigilar
  que no colapse con más muestra, como pasó con `tier=A+` en RETEST); 5m
  n=7 delta=**-1.254** (sentido contrario a 2m — el SL de 3 capas gana
  ahí, CI no calculable con n tan chico, anotar sin accionar). Sigue sin
  proponerse cambio en `experiments.json` para INV/LONG — esperar a que
  2m crezca más allá del piso justo antes de tratarlo como candidato.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
Primera celda con lectura en este segmento (`session_analyst_cross.by_kind_side`,
mejora de `analyze.py` de hoy): INV/LONG bajo veredicto SA `WAIT` n=7
E[R]=+0.437 — n insuficiente para comparar contra AVOID/GO todavía. Ver
`sell-retest.md` para el hallazgo agregado (AVOID rinde mejor que GO,
ahora con CI90 real).

### Contextos a evitar
- Autopsia de SL sobre las 34 pérdidas INV/LONG (desglose permanente por
  kind/side en `analyze.py`): `RR-bajo` 19/34 (56%) pasa a ser la causa
  más frecuente, con `killzone-Asia-largo` 18/34 (53%) muy cerca detrás y
  `contra-estructura` 12/34 (35%) — mismo casi-empate de siempre, orden
  entre las dos primeras se invirtió levemente con dato nuevo.
- `cross_instrument` sigue `instrument-specific` (spread 0.935, bajó de
  1.109): YM n=18 E[R]=0.501, CL n=13 E[R]=0.428, NQ n=6 E[R]=0.257, ES
  n=7 E[R]=-0.434, GC n=6 E[R]=-0.367 — n por símbolo todavía muy chico,
  no generalizar.

### Decaimiento
_pendiente_ (WR TP1 por semana; marcar si cae > 15 pts en ventana de 3 semanas)

## Histórico de cambios
- 2026-09-03: primeros datos reales, n=0→3 (1m n=2, 2m n=1). Sin valor
  estadístico todavía; se deja constancia. Sigue siendo el segmento con
  menos muestra de los cuatro playbooks — prioridad 2 confirmada.
- 2026-09-04: salto grande n=3→48 (1m 2→30, 2m 1→12, 5m 0→2, primeros
  datos 5m). Primera lectura con algo de valor: 1m E[R]=+0.428, cerca del
  borde de significancia (p=0.059) pero sin certificar FDR todavía. Nuevo
  hallazgo a vigilar sin accionar: `sl_origin_vs_layer` en 2m bate cero
  con un efecto grande (+2.472) pero n=12, muy por debajo del piso de
  n=20 — no se propone nada, solo se deja constancia. Autopsia de SL:
  `killzone-Asia-largo` domina (58% de las pérdidas), distinto al patrón
  de RETEST donde `RR-bajo`/`contra-estructura` lideran.
- 2026-09-05: refresco n=48→63 (1m 30→40, 2m 12→18, 5m 2→5), en parte por
  la restauración de `signals/2026-09-03.jsonl` (ver nota al inicio de la
  Sección viva y detalle completo en `buy-retest.md`). Todas las lecturas
  se mantienen en la misma dirección que ayer, sin sorpresas: 1m sigue
  positivo pero se alejó un poco del borde de significancia (p=0.059→0.101),
  `sl_origin_vs_layer` en 2m sigue batiendo cero con efecto grande
  (+2.472→+1.708, n=12→18, todavía bajo el piso de n=20). A diferencia de
  BUY/SELL RETEST, aquí la restauración de datos no cambió ningún signo —
  este playbook ya tenía muestra chica y por lo tanto poco que corregir.
- 2026-09-06 (revisión semanal, domingo): n sin cambios (63) — CME cerrado
  el fin de semana, cero signals/outcomes nuevos. El bug de `heal` que
  truncó `signals/2026-09-03.jsonl` se repitió una segunda vez (commit
  `0cf0a30`) y se restauró de nuevo; ver nota de proceso arriba y
  `experiments.json`/`analyze.py` (guarda `file_integrity_check` nueva).
  Ver `reviews/2026-week-36.md` para la revisión semanal completa.
- 2026-09-07 (lunes, festivo EE.UU.): primer día sin repetición del bug de
  "heal", con algo de dato nuevo genuino (n=63→66: 1m 40→42, 5m 5→6, 2m
  sin cambio en 18). Primera vez con fila propia de `managed_vs_naive` en
  1m (delta+0.113) y 5m (delta+0.191), ambas ayudan. Primera lectura de
  `sl_origin_vs_layer` en 5m: delta negativo (-1.255, n=6 mínimo, sentido
  opuesto al de 2m) — anotado sin accionar. Primera lectura de
  `cross_instrument` en este segmento (`instrument-specific`, spread
  1.109, YM/CL positivos, ES/GC negativos, n por símbolo muy chico).
- 2026-09-08 (martes, primer día hábil completo post-feriado): n=66->77
  (1m 42->50, 2m 18->20, 5m 6->7). **`sl_origin_vs_layer` en 2m llegó al
  piso de n=20 del método y certifica** (delta+1.538, CI90 [0.243,3.13],
  no cruza cero) — primera vez que esta rama de INV/LONG entra en
  territorio "tratable como real"; efecto muy grande para un n tan chico,
  vigilar que no se diluya como pasó con otras lecturas de n justo en el
  piso en este bus. Mejora permanente en `analyze.py`:
  `session_analyst_cross.by_kind_side` da su primera celda para este
  segmento (WAIT n=7, E[R]=+0.437, insuficiente para comparar contra
  AVOID/GO). Ver `sell-retest.md` para el hallazgo mayor del día (SA
  AVOID rinde mejor que GO, ahora con CI90 estadístico real).
