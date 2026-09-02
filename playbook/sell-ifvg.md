# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-02 · n: 9)

### Veredicto global
**MUESTRA MÍNIMA — primeros datos, no accionable.** n=9: 1m/INV/SHORT n=8
(WR 75.0%, E[R]=0.316, PF=2.27, 2 SL) + 5m/INV/SHORT n=1 (WR 100%,
E[R]=0.52, PF=99 — un solo trade, sin valor estadístico). El 1m mejoró
desde la lectura anterior (n=3, WR 66.7%, E[R]=-0.07) pero sigue muy lejos
de n=20 y de cualquier prueba de significancia — puro ruido de tamaño de
muestra por ahora. Prioridad 2 — seguir monitoreando, sin comprometer
tiempo de análisis mientras BUY/SELL RETEST tengan mejor muestra.

### Reglas condicionales (IF contexto ENTONCES acción)
Todavía sin ninguna con n suficiente. Con `by_kindside_edge`/`tier`
(agregado hoy a `analyze.py`) ya disponibles para este segmento cuando
crezca: por ahora, de las 8 señales 1m, 7 tienen `nearEdge=0` y `tier=C`
(las 2 SL están ahí también), 1 tiene `nearEdge=-1`/`tier=B` (fue SL) — sin
variación suficiente todavía para separar ramas.

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | _pendiente_ | _pendiente_ | 0 | | |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- SL óptimo (ticks / múltiplo de ATR5m): _pendiente_ (percentil 75-90 del `maeTk` de ganadores + colchón)
- Objetivo: _pendiente_ (siguiente nivel vs RR fijo 1.5/2/3 — ver contrafactual)
- Parcial 1: _pendiente_ (mediana del `mfeTk`; cruzar con `mfe5`/`mfe10`)
- ¿Trailing tras +1R?: _pendiente_ (curva MFE de ganadores que siguieron corriendo)

### Contextos a evitar
_pendiente_ (causas de SL dominantes para este tipo)

### Decaimiento
_pendiente_ (WR TP1 por semana; marcar si cae > 15 pts en ventana de 3 semanas)

## Histórico de cambios
- 2026-09-02 (corrida formal del agente): refresco n=4->9 (1m n=3->8, 5m
  se mantiene n=1). WR 1m sube de 66.7% a 75.0%, E[R] pasa de -0.07 a
  +0.316 - sigue siendo ruido de muestra chica (n=8), nada accionable
  todavía. Concentrado en YM/NQ, mayoría `tier=C`/`nearEdge=0`.
