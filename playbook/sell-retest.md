# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-02 · n: 123)

### Veredicto global
**TOMAR-FILTRADA — el segmento crudo es mediocre pero el corte por
`nearEdge` (y por `tier`) separa un subconjunto claramente rentable de uno
claramente perdedor, con muestra ya razonable en ambos lados.** n=123
(85× 1m, 28× 2m, 10× 5m). Crudo: 1m WR 51.8% E[R]=0.046 PF=1.11; 2m WR
57.1% E[R]=-0.046 PF=0.88; 5m WR 80% E[R]=0.245 PF=2.23 (n chico). Ninguno
de los tres sobrevive `segment_significance` todavía (`survives_fdr10=false`
en los tres, CI90 cruza 0) — **el número que cuenta para certificar sigue
sin llegar**, pero el filtro de contexto de abajo es el hallazgo más
accionable de hoy.

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna tiene `survives_fdr10=true` todavía (esa prueba corre por
tf/kind/side, no por estos cortes cruzados) — se tratan como candidatas
fuertes a vigilar 1-2 semanas más antes de proponer un cambio de Pine, no
como reglas certificadas.

| # | SI | ENTONCES | n (dentro/fuera) | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` (señal cerca del borde de la zona) | TOMAR | 49 / 61+13 | WR 69.4% vs 47.5% (edge=0) vs 38.5% (edge=-1); E[R] +0.326 vs -0.158 vs -0.095; PF 2.11 vs 0.66 vs 0.79 | **moderada** — n≥20 en las tres ramas, dirección consistente, misma dirección en 1m y 2m por separado |
| 2 | `nearEdge=0` | FILTRAR / no tomar | 61 | E[R]=-0.158, PF 0.66, WR 47.5% | moderada — es la rama mala y la más numerosa (49.6% de SELL RETEST) |
| 3 | `tier=B` | TOMAR, prioridad | 54 / 66 | WR 64.8% vs 48.5% (tier C); E[R] +0.269 vs -0.16; PF 1.88 vs 0.65 | moderada — n≥20 ambos lados, coherente con la regla de `nearEdge` (probable solape, no confirmado independiente) |
| 4 | símbolo (`cross_instrument`) | NO generalizar | ver detalle | 1m y 2m: `instrument-specific` (spread 0.70 y 0.43). 5m: `universal` (spread 0.25, n chico) | baja para usar como filtro — YM rinde mejor y ES peor en 1m, pero es observación por símbolo, no regla de contexto |

Antes de proponer esto como cambio de input de Pine (p.ej. un filtro de
proximidad tipo `3B` o ajustar `sc_min_rr`/umbral de zona) hace falta que
`nearEdge` o `tier` aparezcan con `survives_fdr10=true` en
`segment_significance` — ahora mismo esa prueba sólo corre sobre
tf/kind/side, no sobre estos cortes cruzados. Anotado para la próxima
revisión semanal: si `analyze.py` puede correr el bootstrap FDR también
sobre `by_kindside_edge`/`by_kindside_tier`, sería la mejora permanente que
cierra este gap.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente en la mayoría de outcomes.

### Gestión
- SL óptimo: `loserMFEbeforeSL_p50` global 2.0 ticks (away-from-news:
  cerca, n=157) — descriptivo. `revAfterSL_rate` global 62.9%: la mayoría
  de las pérdidas revierten después del SL, otra vez apuntando a SL
  ajustado más que a dirección equivocada.
- Objetivo: contrafactual `nextLevel` (0.276 E[R], n=8 — muestra chica,
  todavía no cortado por side) supera a RR fijo 1R (0.258) y empata con
  1.5/2/3R fijos (0.276 los tres); `altSL_0.5x_struct` (SL más ajustado)
  sube a 0.316 pero n=8 es demasiado chico para actuar.
- Parcial 1 / modelo GESTIONADO vs INGENUO (`managed_vs_naive`, n=143
  global): en SELL RETEST el gestionado bate al ingenuo en los tres TF —
  1m delta +0.04 (n=78), 2m delta +0.035 (n=28), 5m delta +0.304 (n=9,
  chico pero el salto más grande). La escalera de entrada consigue el
  primer parcial (`m1Hit`) 31.5-44% de las veces según TF; fill completo de
  las 3 franjas sólo 11-31%. Es la config fija del sistema, no se toca a
  ojo — sólo referencia de cuánto aporta la gestión vs 1 contrato a mercado.
- ¿Trailing tras +1R?: `beAfterM1_rate` 17.9-33.3% según TF — descriptivo,
  sin contrafactual propio todavía.

### Contextos a evitar
- `nearEdge=0` (ver regla #2) y `tier=C` (ver regla #3) — ambos con E[R]
  negativo y muestra ya razonable (n=61 y n=66).
- Autopsia de SL sobre las 44 pérdidas SHORT: `RR-bajo` 22/44 (50%) y
  `stop-en-el-minimo` 22/44 (50%) **empatadas como causa dominante** —
  coincide con el empate a nivel global del dataset (39/39). `chop` 13/44,
  `contra-estructura` 12/44, `sin-nivel-detras` 8/44, `sin-causa-clara`
  8/44. Con dos causas empatadas y cada una en la mitad de las pérdidas,
  **la causa de SL dominante del mes es doble**: RR de entrada demasiado
  bajo Y el SL colocado justo donde el precio hace mínimo/máximo antes de
  revertir. Ninguna de las dos está mitigada todavía por un experimento
  `confirmed` — sigue bloqueando el gate de ejecución (criterio "causa de
  SL dominante mitigada").
- Hipótesis de cruce con Session Analyst (§8 de `agent-instructions.md`):
  sigue sin cuantificarse — `analyze.py` no tiene todavía un cruce
  histórico fecha+símbolo entre el veredicto GO/WAIT/AVOID del SA y el
  resultado del par. Sería la mejora permanente más valiosa a construir en
  la revisión semanal (unir `dataset.jsonl.recvDate`+símbolo contra los
  `plans/*.json` archivados del SA) — hoy no se improvisa a mano para no
  reportar un número no verificado.

### Decaimiento
Sólo 2026-W36 en `decay_weekly` (n=158, WR 55.1%, E[R] 0.015) — sin semana
previa para comparar decaimiento real todavía.

## Histórico de cambios
- 2026-09-01: primera escritura con datos reales (n=3, todas GC 1m SHORT
  mismo día, 3/3 SL). Marcado explícitamente como no accionable por tamaño
  de muestra; se deja constancia de la posible correlación con el veredicto
  del Session Analyst para verificar cuando crezca la muestra.
- 2026-09-01 (tarde): refresco a n=5 (WR sube de 0% a 20%, sigue siendo el
  peor segmento). Coincide con el corte `aligned=1` — anotado como posible
  confusión de variables, a revisar cuando la muestra crezca. Hipótesis de
  cruce con Session Analyst se mantiene, sigue sin ser cuantificable.
- 2026-09-02: salto grande de muestra, n=5→123 (85× 1m, 28× 2m, 10× 5m).
  El segmento crudo por TF sigue sin significancia (`survives_fdr10=false`
  en los tres), pero aparece el primer hallazgo accionable real: el corte
  `nearEdge=1` vs `nearEdge=0` separa un E[R]=+0.326 (n=49) de un
  E[R]=-0.158 (n=61) — candidato fuerte para la revisión semanal si se
  sostiene 1-2 semanas más. `tier B` vs `tier C` muestra el mismo patrón
  (probable solape con `nearEdge`, sin confirmar independencia). Autopsia
  de SL: `RR-bajo` y `stop-en-el-minimo` empatados 22/44 como causa
  dominante — ninguna mitigada aún. Se descarta generalizar por símbolo:
  `cross_instrument` marca 1m y 2m como `instrument-specific`. Fix de bug
  en `analyze.py` (`news_context` crasheaba leyendo `market.json` del
  Session Analyst) aplicado hoy, sin impacto en estas métricas.
