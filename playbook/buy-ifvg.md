# Playbook · BUY (iFVG invertido)

Señal: un FVG bajista que se invierte al alza (`kind=INV`, `side=LONG`).
Prioridad 2 (monitoreo). Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-03 · n: 3)

### Veredicto global
**Primeros datos reales, todavía sin valor estadístico.** n=3 (2× 1m: WR
50%, E[R]=-0.21, PF=0.58, 1 SL; 1× 2m: único trade, TP1, E[R]=+0.74).
Prioridad 2 (monitoreo) — no compite en atención con BUY/SELL RETEST hasta
que crezca. Nada accionable con n=3; se deja constancia de los primeros
signos y se sigue observando.

### Reglas condicionales (IF contexto ENTONCES acción)
Sin n suficiente para ninguna rama (`by_kindside_edge`/`tier`/`aligned` ya
disponibles en `analyze.py` para cuando este segmento crezca).

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | _pendiente_ | _pendiente_ | 3 | | ninguna |

### Entrada
- Óptima: _pendiente_ (mercado al cierre vs límite en `zBot`/`zCE`; ver `entryZoneTk` de ganadores vs perdedores)

### Gestión
- SL óptimo (ticks / múltiplo de ATR5m): _pendiente_ (percentil 75-90 del `maeTk` de ganadores + colchón)
- Objetivo: _pendiente_ (siguiente nivel vs RR fijo 1.5/2/3 — ver contrafactual)
- Parcial 1: _pendiente_ (mediana del `mfeTk`; cruzar con `mfe5`/`mfe10`)
- ¿Trailing tras +1R?: _pendiente_ (curva MFE de ganadores que siguieron corriendo)

### Contextos a evitar
- Única pérdida (1m, n=1): causas `chop`, `RR-bajo`, `stop-en-el-minimo` —
  un solo caso, no generaliza.

### Decaimiento
_pendiente_ (WR TP1 por semana; marcar si cae > 15 pts en ventana de 3 semanas)

## Histórico de cambios
- 2026-09-03: primeros datos reales, n=0→3 (1m n=2, 2m n=1). Sin valor
  estadístico todavía; se deja constancia. Sigue siendo el segmento con
  menos muestra de los cuatro playbooks — prioridad 2 confirmada.
