# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-01 (tarde) · n: 6)

### Veredicto global
**MUESTRA INSUFICIENTE — no accionable todavía.** n=6 (4× 1m/RETEST/LONG,
2× 2m/RETEST/LONG). WR TP1 = 75% (1m, n=4) / 100% (2m, n=2). E[R] = 0.335
(1m) / 0.655 (2m), PF = 2.34 (1m) / 99 (2m, sin perdedoras). Sube de n=3 a
n=6 desde la última corrida y ya aparece la primera pérdida en 1m (antes
3/3 ganadoras, ahora 3/4): el 100% inicial era ruido, como se advirtió.
Sigue muy por debajo de n=20 — no toques inputs de Pine por esto. 5m: sin
datos aún.

### Reglas condicionales (IF contexto ENTONCES acción)
Cada regla con: condición, n, WR/E[R] dentro vs fuera, confianza.

| # | SI | ENTONCES | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | _pendiente_ (n<20 en todos los cortes) | _pendiente_ | 6 | ninguno fiable aún | muy baja |

Observación a vigilar (no regla): la única pérdida 1m/LONG (`NQ-1-23427-L`)
está tageada `contra-sesgo` + `RR-bajo` en la autopsia de SL — coincide con
el patrón que también se ve en SELL RETEST (señal a favor del scalp pero
contra el sesgo dominante de la sesión). Con n=1 no es cuantificable, solo
un candidato a regla para cuando crezca la muestra.

### Entrada
- Óptima: _pendiente_ — datos insuficientes (`entryZoneTk` no disponible aún).

### Gestión
- SL óptimo: winnerMAE p75/p90 = 4.0/5.8 ticks (1m), 29.0/32.0 ticks (2m) —
  solo referencia descriptiva de esta muestra, no una regla.
- Objetivo: _pendiente_ (contrafactual n=0 todavía, sin outcomes v3).
- Parcial 1: mediana MFE 15.5 ticks (1m), 70.0 ticks (2m) — descriptivo, no regla.
- ¿Trailing tras +1R?: _pendiente_ (muestra insuficiente para ver curva de MFE).

### Contextos a evitar
Provisional (n=1, no cuantificable): 1m/RETEST/LONG contra el sesgo
dominante de sesión (ver observación arriba).

### Decaimiento
_pendiente_ — solo una semana de datos (2026-W36), sin semana previa para comparar.

## Histórico de cambios
- 2026-09-01: primera escritura con datos reales (n=3, todas GC, mismo día,
  3/3 TP1). Marcado explícitamente como no accionable por tamaño de muestra.
- 2026-09-01 (tarde): refresco a n=6 (1m n=4, 2m n=2). Primera pérdida 1m
  registrada (WR baja de 100% a 75%), confirma que el 100% inicial era
  ruido. Sigue sin ser accionable (n<20).
