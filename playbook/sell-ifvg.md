# Playbook · SELL (iFVG invertido)

Señal: un FVG alcista que se invierte a la baja (`kind=INV`, `side=SHORT`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-02 · n: 4)

### Veredicto global
**MUESTRA MÍNIMA — primeros datos, no accionable.** n=4: 1m/INV/SHORT n=3
(WR 66.7%, E[R]=-0.07, PF=0.79, 1 SL) + 5m/INV/SHORT n=1 (WR 100%,
E[R]=0.52, PF=99 — un solo trade, sin valor estadístico). Muy lejos de
n=20. Prioridad 2 — seguir monitoreando, sin comprometer tiempo de análisis
mientras BUY/SELL RETEST tengan mejor muestra.

### Reglas condicionales (IF contexto ENTONCES acción)
Cada regla con: condición, n, WR/E[R] dentro vs fuera, confianza.

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
_(vacío)_
