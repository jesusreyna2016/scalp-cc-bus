# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-07 · n: 66)

### Nota de proceso
Primer día sin repetición del bug de "heal" (ver `buy-retest.md` para el
detalle completo) — llegó algo de dato nuevo genuino (lunes festivo
EE.UU., Globex con volumen reducido), aunque este segmento sigue teniendo
muestra chica y crece lento.

### Veredicto global
1m n=42 (WR 47.6%, E[R]=+0.276, PF=1.64, 17 SL); 2m n=18 (sin cambio, WR
38.9%, E[R]=-0.271, PF=0.56, 11 SL); 5m n=6 (100% TP1, E[R]=+0.712, PF=99,
todavía sin valor estadístico, n creció de 5 a 6). `segment_significance`:
1m CI90=[-0.102,0.653] p_mean_le_0=0.116 (n=41), se alejó un poco más del
borde de significancia (era p=0.101 ayer, p=0.059 hace 2 días) pero sigue
en la misma dirección positiva; 2m CI90=[-0.638,0.119] p=0.879, idéntico a
ayer (sin señales 2m nuevas), sigue negativo sin certificar. Prioridad 2
se mantiene; el 1m sigue siendo el único con algo de lectura útil.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar, pero ya hay lectura por corte:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | mejor que `edge=0`; primera señal `edge=-1` hoy | 34 / 31 / 1 | WR 50.0%/48.4%/100%; E[R] +0.201/+0.047/+2.59; PF 1.49/1.1/99 | baja-moderada — mismo sentido que antes en `edge=1` vs `edge=0`, pero `edge=-1` es una sola señal nueva (n=1), no generalizar |
| 2 | `tier=B` | mejor que `tier=C` | 18 / 48 | E[R] +0.352 vs +0.098; PF 1.91 vs 1.21 | baja-moderada — tier B sin señales nuevas (n=18 igual que ayer), tier C creció poco (45→48), misma dirección |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- `managed_vs_naive`: **1m tiene fila propia por primera vez hoy**, n=41
  delta=**+0.113** (naive 0.276→managed 0.389, ayuda); 2m n=18 delta=+0.03
  (naive -0.271→managed -0.241, sigue negativo, sin cambio); 5m n=6
  delta=+0.191 (naive 0.712→managed 0.903, primera lectura con fila
  propia, ayuda, pero n mínimo).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=41
  delta=+0.24 CI90=[-0.431,0.958] no certifica, casi sin cambio; 2m n=18
  delta=**+1.708** CI90=[0.256,3.449] **sigue batiendo cero** — idéntico a
  ayer (sin señales 2m nuevas), n sigue justo debajo del piso de 20 del
  método; 5m n=6 delta=**-1.255** (primera lectura, va en sentido
  contrario a 2m — el SL de 3 capas gana ahí, CI no calculable con n=6,
  anotar sin accionar). No proponer cambio todavía en INV/LONG.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL sobre las 28 pérdidas INV/LONG (desglose permanente por
  kind/side en `analyze.py`): `killzone-Asia-largo` 16/28 (57%) sigue
  siendo la causa dominante, con `RR-bajo` 15/28 (54%) y
  `contra-estructura` 11/28 (39%) cerca detrás — mismo patrón de siempre,
  estable.
- `cross_instrument` (primera vez con lectura, sigue `instrument-specific`,
  spread 1.109): YM n=18 E[R]=0.501, CL n=13 E[R]=0.428, ES n=5
  E[R]=-0.5, GC n=4 E[R]=-0.608 — n por símbolo todavía muy chico, no
  generalizar.

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
