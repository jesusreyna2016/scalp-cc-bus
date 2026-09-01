# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-01 (tarde) · n: 5)

### Veredicto global
**MUESTRA INSUFICIENTE — no accionable todavía, pero el patrón se sostiene
y empeora.** n=5, todas 1m/RETEST/SHORT (4 GC + 1 nuevo símbolo desde la
corrida anterior). WR TP1 = 20% (1/5), E[R] = -0.532, PF = 0.26 (3 SL, 1
TIMEOUT, 1 TP1). Sigue siendo n<20 — no toques inputs de Pine por esto —
pero es el peor segmento del dataset hoy y coincide exactamente con el
segmento `aligned=1` (WR 20%, n=5), lo que sugiere una confusión: el corte
que de verdad importa podría ser símbolo/TF/side, no "aligned" en sí.
Reportar, vigilar, no accionar. 2m y 5m: sin datos aún.

### Reglas condicionales (IF contexto ENTONCES acción)
Cada regla con: condición, n, WR/E[R] dentro vs fuera, confianza.

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | _pendiente_ (n<20 en todos los cortes; ver nota abajo) | _pendiente_ | 5 | ninguno fiable aún | muy baja |

Nota: 3 de las 4 pérdidas/timeout de GC ocurrieron el día que el Session
Analyst marcó GC en `WAIT`/`AVOID` para el corto (esperando rechazo
confirmado en 4402-4423, sin perseguir). Es la hipótesis de cruce del §8 de
`agent-instructions.md` (señal de scalp contra veredicto SA rinde peor) —
consistente con n=5, pero **no cuantificable con esta muestra**. Vigilar.

### Entrada
- Óptima: _pendiente_ — datos insuficientes (`entryZoneTk` no disponible aún).

### Gestión
- SL óptimo: _pendiente_ — `loserMFEbeforeSL_p50`=9.0 ticks (referencia, no regla).
- Objetivo: _pendiente_ (contrafactual n=0 todavía, sin outcomes v3).
- Parcial 1: mediana MFE 13.0 ticks — descriptivo, no regla (n=1 ganador).
- ¿Trailing tras +1R?: _pendiente_ (1 solo ganador en esta muestra).

### Contextos a evitar
Provisional, solo como hipótesis a verificar (n=5): 1m/RETEST/SHORT cuando
el Session Analyst tiene el símbolo en AVOID/WAIT para el corto sin rechazo
confirmado. Autopsia de SL sobre las 4 pérdidas totales del dataset (no solo
este segmento): `RR-bajo`×2, `chop`×1, `sin-causa-clara`×1,
`contra-sesgo`×1 — `RR-bajo` es la causa más repetida hoy, pero n=4 pérdidas
totales es demasiado bajo para llamarla "causa dominante" en el sentido del
gate de ejecución.

### Decaimiento
_pendiente_ — solo una semana de datos (2026-W36), sin semana previa para comparar.

## Histórico de cambios
- 2026-09-01: primera escritura con datos reales (n=3, todas GC 1m SHORT
  mismo día, 3/3 SL). Marcado explícitamente como no accionable por tamaño
  de muestra; se deja constancia de la posible correlación con el veredicto
  del Session Analyst para verificar cuando crezca la muestra.
- 2026-09-01 (tarde): refresco a n=5 (WR sube de 0% a 20%, sigue siendo el
  peor segmento). Coincide con el corte `aligned=1` — anotado como posible
  confusión de variables, a revisar cuando la muestra crezca. Hipótesis de
  cruce con Session Analyst se mantiene, sigue sin ser cuantificable.
