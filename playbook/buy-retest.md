# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-01 · n: 3)

### Veredicto global
**MUESTRA INSUFICIENTE — no accionable todavía.** n=3 (2× 1m/RETEST/LONG,
1× 2m/RETEST/LONG), todas GC, mismo día. WR TP1 = 100%, E[R] = 0.645 (1m) /
0.7 (2m), 3/3 ganadoras. Resultado perfecto con n=3 no es señal, es azar
favorable — no lo trates como edge real. 5m: sin datos aún.

### Reglas condicionales (IF contexto ENTONCES acción)
Cada regla con: condición, n, WR/E[R] dentro vs fuera, confianza.

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | _pendiente_ (n<20 en todos los cortes) | _pendiente_ | 3 | ninguno fiable aún | muy baja |

### Entrada
- Óptima: _pendiente_ — datos insuficientes (`entryZoneTk` no disponible en n=3).

### Gestión
- SL óptimo: winnerMAE p75/p90 = 5.25/6.3 ticks (1m), 34.0 ticks (2m) — solo
  referencia descriptiva de esta muestra, no una regla.
- Objetivo: _pendiente_ (contrafactual n=0 todavía, sin outcomes v3).
- Parcial 1: mediana MFE 18.5 ticks (1m), 54.0 ticks (2m) — descriptivo, no regla.
- ¿Trailing tras +1R?: _pendiente_ (muestra insuficiente para ver curva de MFE).

### Contextos a evitar
_pendiente_ — 0 pérdidas en esta muestra, no hay causas de SL que analizar todavía.

### Decaimiento
_pendiente_ — solo una semana de datos (2026-W36), sin semana previa para comparar.

## Histórico de cambios
- 2026-09-01: primera escritura con datos reales (n=3, todas GC, mismo día,
  3/3 TP1). Marcado explícitamente como no accionable por tamaño de muestra.
