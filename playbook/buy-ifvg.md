# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-05 · n: 63)

### ⚠ Nota de proceso — data restaurada hoy
Ver el detalle en `buy-retest.md`: se restauró `signals/2026-09-03.jsonl`
(un commit anterior había borrado 1256 de 1280 líneas por error). Parte
del salto de n de hoy (48→63) viene de esa corrección, no de señales
nuevas.

### Veredicto global
1m n=40 (WR 47.5%, E[R]=+0.307, PF=1.72, 16 SL); 2m n=18 (WR 38.9%,
E[R]=-0.271, PF=0.56, 11 SL); 5m n=5 (100% TP1, todavía sin valor
estadístico). `segment_significance`: 1m CI90=[-0.088,0.695]
p_mean_le_0=0.101, se alejó un poco del borde de significancia respecto a
ayer (era p=0.059) pero sigue en la misma dirección positiva; 2m
CI90=[-0.638,0.119] p=0.879, sigue negativo sin certificar. Prioridad 2 se
mantiene; el 1m sigue siendo el único con algo de lectura útil.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar, pero ya hay lectura por corte:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | mejor que `edge=0` | 32 / 30 | WR 46.9%/50.0%; E[R] +0.175/+0.082; PF 1.4/1.17 | baja-moderada — n creció (24/20→32/30) pero el efecto se moderó, mismo sentido que RETEST |
| 2 | `tier=B` | mejor que `tier=C` | 18 / 45 | E[R] +0.352 vs +0.1; PF 1.91 vs 1.21 | baja-moderada — n de B creció (13→18), efecto se moderó (+0.577→+0.352) pero se mantiene la misma dirección |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- `managed_vs_naive`: 2m n=18 delta=+0.03 (naive -0.271→managed -0.241,
  sigue negativo, la escalera resta menos que ayer +0.014→+0.03). 1m no
  tiene fila propia en este corte con la muestra de hoy (ver
  `report.json.managed_vs_naive.by_tf_kind_side` para el detalle crudo).
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=39
  delta=+0.257 CI90=[-0.43,1.011] no certifica; 2m n=18 delta=**+1.708**
  CI90=[0.256,3.449] **bate cero** — se mantiene el efecto grande (bajó de
  +2.472 con n=12 a +1.708 con n=18), n sigue justo debajo del piso de 20
  del método; no proponer cambio todavía, un solo par más de muestra lo
  pondría en condición de evaluarse.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL sobre las 27 pérdidas INV/LONG (desglose permanente por
  kind/side en `analyze.py`): `killzone-Asia-largo` 15/27 (56%) sigue
  siendo la causa dominante, con `RR-bajo` 14/27 (52%) y
  `contra-estructura` 11/27 (41%) cerca detrás — mismo patrón que ayer
  (58%/47%/37%), estable.

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
