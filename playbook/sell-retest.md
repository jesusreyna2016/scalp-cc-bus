# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-01 · n: 3)

### Veredicto global
**MUESTRA INSUFICIENTE — no accionable todavía.** n=3, todas GC 1m/RETEST/SHORT,
todas mismo día. WR TP1 = 0%, E[R] = -1.0, PF = 0.0 (3/3 SL). No se puede
distinguir señal de ruido con n=3; no toques inputs de Pine por esto. Se
reporta para dejar rastro, no como veredicto real. 2m y 5m: sin datos aún.

### Reglas condicionales (IF contexto ENTONCES acción)
Cada regla con: condición, n, WR/E[R] dentro vs fuera, confianza.

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | _pendiente_ (n<20 en todos los cortes; ver nota abajo) | _pendiente_ | 3 | ninguno fiable aún | muy baja |

Nota: las 3 pérdidas ocurrieron en GC el mismo día que el Session Analyst
marcó GC en `WAIT`/`AVOID` para el corto (esperando rechazo confirmado en
4402-4423, sin perseguir). Es la hipótesis de cruce del §8 de
`agent-instructions.md` (señal de scalp contra veredicto SA rinde peor) —
consistente con n=3, pero **no cuantificable con esta muestra**. Vigilar.

### Entrada
- Óptima: _pendiente_ — datos insuficientes (`entryZoneTk` no disponible en n=3).

### Gestión
- SL óptimo: _pendiente_ — todas las 3 tocaron SL, `loserMFEbeforeSL_p50`=9.0 ticks (referencia, no regla).
- Objetivo: _pendiente_ (contrafactual n=0 todavía, sin outcomes v3).
- Parcial 1: _pendiente_.
- ¿Trailing tras +1R?: _pendiente_ (0 ganadores en esta muestra).

### Contextos a evitar
Provisional, solo como hipótesis a verificar (n=3): 1m/RETEST/SHORT en GC
cuando el Session Analyst tiene el símbolo en AVOID/WAIT para el corto sin
rechazo confirmado. Causas de SL vistas: chop×1, RR-bajo×1, sin-causa-clara×1
— sin causa dominante clara con n=3.

### Decaimiento
_pendiente_ — solo una semana de datos (2026-W36), sin semana previa para comparar.

## Histórico de cambios
- 2026-09-01: primera escritura con datos reales (n=3, todas GC 1m SHORT
  mismo día, 3/3 SL). Marcado explícitamente como no accionable por tamaño
  de muestra; se deja constancia de la posible correlación con el veredicto
  del Session Analyst para verificar cuando crezca la muestra.
