# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-04 · n: 48)

### Veredicto global
**Salto grande de muestra (3→48) y las primeras lecturas útiles.** 1m
n=30 (WR 50.0%, E[R]=+0.428, PF=2.02, 12 SL); 2m n=12 (WR 41.7%,
E[R]=-0.233, PF=0.6, 7 SL); 5m n=2 (100% TP1, todavía sin valor). El 1m ya
tiene n=30 en `segment_significance`: CI90=[-0.02,0.94], p_mean_le_0=0.059
— cerca del borde de significativo por el lado bueno, pero
`survives_fdr10=false`. Prioridad 2 se mantiene, pero el 1m ya merece
seguimiento semanal cercano.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente todavía para certificar, pero ya hay lectura por corte:

| # | SI | ENTONCES (hipótesis, sin confirmar) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` | mejor que `edge=0` | 24 / 20 | WR 50.0%/50.0%; E[R] +0.346/+0.137; PF 1.87/1.27 | baja-moderada — n todavía chico, mismo sentido que RETEST (edge alto ayuda) |
| 2 | `tier=B` | mejor que `tier=C` | 13 / 31 | E[R] +0.577 vs +0.114; PF 2.65 vs 1.24 | baja — n=13 en B, mismo sentido que RETEST pero muestra chica |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- `managed_vs_naive`: 1m n=30 delta=+0.108 (naive 0.428→managed 0.535, la
  escalera ayuda); 2m n=12 delta=+0.014 (naive -0.233→managed -0.219,
  sigue negativo pero la escalera resta menos). Mismo sentido que
  RETEST/LONG: ayuda o es neutra, nunca perjudica fuerte.
- `sl_origin_vs_layer` (basis `candle1`, vela 1 del FVG): 1m n=30
  delta=+0.443 CI90=[-0.362,1.327] no certifica; 2m n=12 delta=**+2.472**
  CI90=[0.456,5.001] **bate cero** — efecto grande pero n=12, muy por
  debajo del piso de n=20 del método; no proponer cambio todavía, solo
  vigilar si se sostiene al crecer.
- Objetivo / Parcial 1 / trailing: _pendiente_.

### Contextos a evitar
- Autopsia de SL sobre las 19 pérdidas INV/LONG (desglose permanente por
  kind/side en `analyze.py`): `killzone-Asia-largo` 11/19 (58%) es la
  causa dominante, seguida de `RR-bajo` 9/19 (47%) y `contra-estructura`
  7/19 (37%).

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
