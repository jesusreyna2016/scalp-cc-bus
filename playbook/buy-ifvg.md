# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-11 · n: 100)

### Nota de proceso
Ver `buy-retest.md` para el incidente de repo de hoy (reset a
`origin/main`, superset verificado, sin pérdida de datos). Este segmento
(prioridad 2) sí participó del salto: n 82→100 (**+18**; 1m +11, 2m +4, 5m
+3) — la muestra más grande que ha sumado este playbook en un solo día.

### Veredicto global
1m n=64 (+11, WR 43.8%, E[R]=**0.097** PF=1.2, 29 SL — bajó de +0.225,
primer retroceso del 1m tras varios días subiendo); 2m n=26 (+4, WR
42.3%, E[R]=**-0.247** PF=0.56, 14 SL — mejoró de -0.32 pero sigue siendo
la peor rama del segmento); 5m n=10 (+3, WR 90.0%, E[R]=**0.849** PF=99,
0 SL). `segment_significance`: 1m CI90=[-0.168,0.382] p=0.285 n=62 (se
alejó de certificar, venía de [-0.084,0.531] p=0.127); 2m
CI90=[-0.537,0.051] p=0.904 n=26 (mejoró un poco, sigue lejos de
certificar); **5m aparece por primera vez con `survives_fdr10=true`**
(CI90=[0.522,1.254] p=0.0, n=10) — **no usable**: la regla del propio
playbook exige n≥20 para proponer cualquier cambio, y n=10 es awfully
small para un PF=99 (0 pérdidas); tratar como ruido de muestra mínima,
no como hallazgo.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar en la mayoría de las ramas:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | sigue siendo la mejor rama, aunque el efecto se moderó | 55 (+14) / 41 (+4) / 4 (sin cambio) | WR 47.3%/48.8%/50.0%; E[R] +0.114/+0.005/+0.455 (edge=0 casi colapsó de +0.161 a +0.005); PF 1.27/1.01/1.91 | baja-moderada — `edge=1` ahora tiene la muestra más grande de las tres, pero `edge=0` se diluyó fuerte |
| 2 | `tier=B` | mejor que `tier=C`, aunque ambos bajaron | 30 (+7) / 70 (+11) | E[R] +0.14 (venía de +0.293) vs +0.059 (venía de +0.047); PF 1.34 vs 1.13 | baja-moderada — mismo sentido que ayer pero B se moderó bastante, sin cambiar el orden |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- `managed_vs_naive`: 1m n=62 delta=**+0.173** (naive 0.097→managed 0.27,
  ayuda más que ayer, +0.142); 2m n=26 delta=+0.017 (naive
  -0.247→managed -0.231, casi sin cambio, sigue apenas positivo); 5m n=10
  delta=**-0.117** (naive 0.849→managed 0.732 — **cambia de signo**,
  ahora la gestión resta en 5m INV/LONG, aunque con n=10 no es
  concluyente).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=62
  delta=**+0.028** CI90=[-0.435,0.499] no certifica (bajó fuerte de
  +0.168, casi a cero); 2m **sigue certificando por cuarto día, pero al
  filo**: n=26 (+4) delta=**+1.066** CI90=**[0.007,2.311]** (bajó de
  +1.394, el límite inferior cayó de 0.185 a 0.007 — a un paso de perder
  la certificación); 5m n=10 (+3) delta=**-1.307** CI90=**[-1.91,-0.771]**
  (primera vez con CI calculable — confirma que el SL de 3 capas es
  MEJOR que el estructural en 5m INV/LONG, sentido opuesto a 2m, aunque
  n=10 sigue por debajo del piso de n≥20 del playbook). Sigue sin
  proponerse cambio en `experiments.json` para INV/LONG — 2m sigue siendo
  el único candidato con algo de solidez, pero está debilitándose.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Cruce con Session Analyst
INV/LONG bajo veredicto SA `WAIT` n=19 (+11) E[R]=**0.215** PF=1.58 (bajó
de +0.396 con más muestra, sigue positivo); la celda `GO` que ayer tenía
n=5 ya no aparece (cayó bajo el piso de n≥5 que usa este corte) — no hay
lectura propia de `GO` hoy en este segmento. Con `WAIT` como único dato,
no se puede comparar contra la hipótesis original aquí; ver
`buy-retest.md`/`sell-retest.md` para el hallazgo agregado, que hoy se
invirtió por completo (SA=WAIT pasa a ser la mejor rama en RETEST/LONG,
ya no SA=AVOID).

### Contextos a evitar
- Autopsia de SL sobre las 43 pérdidas INV/LONG (+9 vs ayer): **cambia el
  orden** — `killzone-Asia-largo` 21/43 (48.8%) pasa a ser la causa más
  frecuente, `RR-bajo` 20/43 (46.5%) muy cerca detrás (venía siendo
  dominante en solitario con 56%), `contra-estructura` 13/43 (30.2%)
  tercero. Ya no hay una causa claramente dominante en solitario.
- `cross_instrument` sigue `instrument-specific` pero el spread se
  estrechó bastante (0.935→0.754): CL n=19 (+5) E[R]=0.32 (bajó de
  0.428), YM n=21 (+3) E[R]=0.194 (bajó fuerte de 0.501), GC n=11 (+3)
  E[R]=-0.193 (empeoró de -0.141), ES n=7 (sin cambio) E[R]=-0.434, NQ
  n=6 (sin cambio) E[R]=0.257 — n por símbolo sigue chico, no
  generalizar.

### Decaimiento
_pendiente_ (WR TP1 por semana; marcar si cae > 15 pts en ventana de 3 semanas)

## Histórico de cambios
- 2026-09-11 (viernes): n 82→100 (+18; 1m+11, 2m+4, 5m+3), la muestra más
  grande sumada en un día en este playbook. Mismo incidente de repo que
  `buy-retest.md` (reset a `origin/main`, sin pérdida de datos). 1m
  retrocede de E[R]=+0.225 a +0.097 (primer retroceso tras varios días
  subiendo). `segment_significance` marca `survives_fdr10=true` en 5m por
  primera vez (n=10, PF=99) — explícitamente **no accionable**, muy por
  debajo del piso n≥20 del playbook. `sl_origin_vs_layer` en 2m sigue
  certificando pero al filo (límite inferior del CI90 cayó a 0.007); en
  5m aparece con CI calculable por primera vez y certifica en sentido
  CONTRARIO a 2m (el SL de 3 capas gana, no el estructural), con n=10.
  Autopsia de SL: `killzone-Asia-largo` desplaza a `RR-bajo` como causa
  más frecuente (48.8% vs 46.5%, antes RR-bajo dominaba solo con 56%).
- 2026-09-10 (jueves): a diferencia del resto del bus (salto grande de
  dato, ver `buy-retest.md`), este segmento apenas creció (+3, n 79→82) —
  sigue siendo el playbook con menos actividad. `sl_origin_vs_layer` en 2m
  sostiene su certificación por tercer día seguido (delta+1.394,
  CI90=[0.185,2.804]). Autopsia de SL sin cambios (cero SL nuevos).
- 2026-09-09 (miércoles): día de confirmación, sin dato fechado hoy —
  solo +2 pares en 1m (TO, sin SL nuevo), 2m/5m sin cambio. Todas las
  cifras coinciden con ayer salvo el cruce con Session Analyst, cuyo
  `n_matched` global creció mucho (ver `sell-retest.md`) y por primera vez
  muestra una celda `GO` en este segmento (n=5, E[R]=-0.212, mismo sentido
  que el hallazgo agregado AVOID>GO).
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
