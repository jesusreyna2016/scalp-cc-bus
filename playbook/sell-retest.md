# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: _pendiente_ · n: 0)

### Veredicto global
_pendiente_ — TOMAR / TOMAR-FILTRADA / EVITAR, con WR TP1, E[R], PF por TF (1m / 2m / 5m).

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
