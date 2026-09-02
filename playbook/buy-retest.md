# Playbook · BUY RETEST

Señal: el precio vuelve a tocar un iFVG alcista ya formado (`kind=RETEST`, `side=LONG`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-02 · n: 31)

### Veredicto global
**EVITAR (1m) / MUESTRA DÉBIL, NO CONFIABLE (2m) — sigue sin ser
accionable, y el 1m se deterioró fuerte.** n=31 (18× 1m/RETEST/LONG,
13× 2m/RETEST/LONG). 1m: WR TP1 44.4%, E[R]=-0.283, PF=0.49 (10 SL de 18).
2m: WR TP1 61.5%, E[R]=+0.159, PF=1.41 (5 SL de 13). **Confirma la
advertencia de la revisión anterior**: el 100% de WR que se veía con n=3-6
era ruido — con n=18 el 1m/LONG pasó de aparentar el mejor segmento del
dataset a ser claramente negativo (E[R] -0.283, el peor de los seis
segmentos con datos hoy). `segment_significance` no certifica ninguno de
los dos (`survives_fdr10=false`, CI90 1m=[-0.606, 0.043] cruza 0, CI90
2m=[-0.28, 0.602] cruza 0 y es aún más ancho). El aparente edge positivo de
2m tampoco se sostiene al cruzar símbolo: `cross_instrument` lo marca
`instrument-specific` (spread 0.603) — está inflado por NQ (n=3, 100% WR,
E[R]=0.623, tamaño de muestra irrisorio) mientras CL (n=10, la mayoría del
segmento) apenas empata (WR 50%, E[R]=0.02). No toques inputs de Pine por
BUY RETEST todavía; ninguno de los dos TF llega a n=20 con significancia
real, y 5m sigue sin datos.

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna certificada (n<20 por corte, sin `survives_fdr10`). Candidatas a
vigilar, no a aplicar:

| # | SI | ENTONCES (hipótesis) | n | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `aligned=0` (contra-tendencia HTF) | mejor que `aligned=1` | 7 vs 24 | E[R] +0.459 vs -0.26, WR 85.7% vs 41.7% | baja — n=7 en la rama buena, contraintuitivo (ver anomalía abajo) |
| 2 | `nearEdge=-1` | mejor que `nearEdge=0` | 13 vs 16 | E[R] +0.078 vs -0.345, WR 61.5% vs 37.5% | baja — ambos cortes <20, y el signo es opuesto al de SELL RETEST (ahí `edge=1` es el bueno) |
| 3 | `tier` (B vs C) | no discrimina en LONG | 8 vs 23 | E[R] -0.091 vs -0.10, ambos negativos | n/a — tier no separa nada aquí, a diferencia de SHORT |

**Anomalía a vigilar** (no accionar): el modelo P(TP1) in-sample pondera
`aligned` con signo **negativo** (-0.459, el tercer coeficiente más fuerte)
— es decir, "alineado con el sesgo/estructura" predice *peor* resultado, lo
mismo que refleja la regla #1 de la tabla. Esto es contraintuitivo (uno
esperaría que ir con el sesgo ayude) y aparece también en SELL RETEST. Dos
hipótesis: (a) el campo `aligned` puede estar capturando exhaustion —
alineación tardía, ya extendida, típica de killzone-Asia-largo; (b) hay un
bug de signo en cómo Pine calcula/envía `aligned`. Con solo n=7 en la rama
`aligned=0` de LONG no es cuantificable — pedir a Jesús que confirme la
definición exacta de `aligned` en el código y vigilar si el signo se
sostiene cuando la muestra crezca.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` sigue sin llenarse en la mayoría de
  outcomes v1/v3 de este segmento; insuficiente para medir calidad de entrada.

### Gestión
- SL óptimo: winnerMAE p75/p90 = 1.25/3.5 ticks (1m, n=18), 13.25/20.0
  ticks (2m, n=13) — descriptivo, no regla (muestra chica y ruidosa; el
  salto del 1m entre esta y la revisión previa —4.0→1.25— confirma que
  no era estable).
- Objetivo: _pendiente_ (contrafactual global no está cortado por
  kind/side todavía).
- Parcial 1: mediana MFE 9.0 ticks (1m), 12.0 ticks (2m) — descriptivo.
- `revAfterSL_rate`: 90% (1m), 100% (2m) — casi todas las pérdidas
  revierten después del SL. Sugiere SL demasiado ajustado / mal ubicado
  más que dirección equivocada, consistente con la causa `stop-en-el-minimo`
  (14 de 15 pérdidas la llevan, ver autopsia abajo). Aún no hay contrafactual
  cortado por side para cuantificar cuánto ganaríamos con SL más holgado.
- ¿Trailing tras +1R?: _pendiente_.

### Contextos a evitar
- 1m/RETEST/LONG en general: E[R] negativo (-0.283) con la muestra más
  grande que hemos tenido, ya no es solo "insuficiente", es la peor lectura
  del dataset hoy. Tratar como EVITAR mientras no cambie.
- Autopsia de SL sobre las 15 pérdidas LONG: `RR-bajo` 15/15 (100%),
  `contra-estructura` 14/15, `stop-en-el-minimo` 14/15,
  `killzone-Asia-largo` 14/15 (pero 24/31 de toda la muestra LONG ya es
  Asia, así que esta última no discrimina mucho por sí sola),
  `sin-nivel-detras` 9/15. **`RR-bajo` es la causa dominante y virtualmente
  universal** en las pérdidas LONG — casi cualquier pérdida 1m/LONG tenía
  el TP1 demasiado cerca del SL desde el origen de la señal. Candidato
  fuerte para revisión semanal (`sc_min_rr` o `sc_aplus_rr`) en cuanto
  aligned=0 / edge=-1 crezcan lo suficiente para aislar la señal real de la
  confusión con RR bajo.

### Decaimiento
Con solo 2026-W36 disponible (`decay_weekly` reporta una sola semana),
sigue sin haber comparación semana-contra-semana real. Lo que sí es
observable dentro de la semana: el WR 1m/LONG cayó de 75-100% (n=3-6, días
previos) a 44.4% (n=18, acumulado) — más una corrección de tamaño de
muestra que "decaimiento" en el sentido de `decay_weekly`, pero el efecto
práctico (la señal ya no parece buena) es el mismo.

## Histórico de cambios
- 2026-09-01: primera escritura con datos reales (n=3, todas GC, mismo día,
  3/3 TP1). Marcado explícitamente como no accionable por tamaño de muestra.
- 2026-09-01 (tarde): refresco a n=6 (1m n=4, 2m n=2). Primera pérdida 1m
  registrada (WR baja de 100% a 75%), confirma que el 100% inicial era
  ruido. Sigue sin ser accionable (n<20).
- 2026-09-02: refresco a n=31 (1m n=18, 2m n=13). El 1m se da vuelta del
  todo: pasa de aparentar el mejor segmento a ser el peor (E[R] -0.283,
  10 SL de 18). El 2m sigue positivo pero `cross_instrument` lo marca
  instrument-specific e inflado por 3 muestras de NQ — no confiable
  todavía. `RR-bajo` sale como causa casi universal (15/15) de las
  pérdidas LONG: candidato a revisar en la próxima revisión semanal si la
  muestra aguanta. Fix de bug en `analyze.py`: `news_context` crasheaba al
  leer `market.json` del Session Analyst (trataba el dict `news.events`
  como lista de eventos y iteraba sobre sus claves) — corregido hoy, sin
  impacto en las métricas de este playbook.
