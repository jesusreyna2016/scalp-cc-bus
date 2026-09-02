# Playbook · SELL RETEST

Señal: un iFVG bajista ya formado (`kind=RETEST`, `side=SHORT`).
Prioridad 1. Lo reescribe el agente cada corrida; el histórico se acumula abajo.

## Sección viva  (última revisión: 2026-09-02 · n: 222)

### Veredicto global
**TOMAR-FILTRADA, y el 5m pasa a TOMAR (primer segmento certificado del
dataset).** n=222 (151× 1m, 53× 2m, 18× 5m). Crudo: 1m WR 49.0% E[R]=-0.015
PF=0.97 (básicamente breakeven); 2m WR 54.7% E[R]=0.087 PF=1.2; 5m WR 88.9%
E[R]=0.687 PF=7.19. **El 5m es el primer segmento de todo el dataset que
sobrevive `segment_significance` (`survives_fdr10=true`, CI90=[0.372,1.0],
no cruza 0, p_mean_le_0=0.0)** — sigue con n=18 (falta 2 para el piso de 20
del método antes de proponer un cambio de Pine), pero ya es un veredicto
TOMAR con confianza real, no una lectura de muestra chica. 1m y 2m siguen
sin certificar (`survives_fdr10=false`, CI90 cruza 0 en ambos). El filtro
de contexto (`nearEdge`, `tier`) sigue siendo el hallazgo más accionable
para el grueso del volumen (1m/2m).

### Reglas condicionales (IF contexto ENTONCES acción)
Ninguna tiene `survives_fdr10=true` todavía (esa prueba corre por
tf/kind/side, no por estos cortes cruzados) — se tratan como candidatas
fuertes a vigilar, no como reglas certificadas. **Mejora permanente de hoy:
`analyze.py` ahora calcula estos cortes cruzados directamente
(`by_kindside_edge`/`by_kindside_tier`/`by_kindside_aligned`), cerrando el
gap que pedía la revisión anterior — ya no se aproximan a mano.**

| # | SI | ENTONCES | n (dentro/fuera) | efecto | confianza |
|---|----|----------|---|--------|-----------|
| 1 | `nearEdge=1` (señal cerca del borde de la zona) | TOMAR | 49 / (125+48) | WR 69.4% vs 52.8% (edge=0) vs 39.6% (edge=-1); E[R] +0.326 vs +0.079 vs -0.233; PF 2.11 vs 1.18 vs 0.59 | **moderada-alta** — n≥48 en las tres ramas, gradiente monótono y consistente con la revisión anterior |
| 2 | `nearEdge=-1` | FILTRAR / no tomar | 48 | E[R]=-0.233, PF 0.59, WR 39.6% | moderada — rama claramente perdedora, n=48 |
| 3 | `tier=A+` | **ANOMALÍA — NO tratar como señal premium** | 16 | WR 6.2%, E[R]=-0.743, PF=0.21 — el peor resultado de *todo* el dataset, invertido respecto a lo que el nombre del tier sugiere | alta como alerta, moderada como regla — ver análisis abajo |
| 4 | `tier=B` | TOMAR, prioridad | 73 / 133 | WR 63.0% vs 54.1% (tier C); E[R] +0.216 vs +0.081; PF 1.65 vs 1.19 | moderada — n≥73 ambos lados, coherente con `nearEdge` (probable solape) |
| 5 | símbolo (`cross_instrument`) | NO generalizar por símbolo | ver detalle | 1m: `universal` (spread 0.265, NQ/GC/YM/ES todos dentro de rango). 2m: `universal` (spread 0.369). 5m: `instrument-specific` (spread 0.435, NQ 0.487 vs ES 0.922, n chico) | 1m/2m: el filtro `nearEdge`/`tier` sí generaliza entre símbolos — mejora la confianza de las reglas 1-4 |

**Anomalía a investigar — tier `A+` está invertido.** Con la muestra ya en
n=16 (sigue bajo el piso de 20 para proponer cambio de Pine, pero ya no es
ruido de 1-2 trades), el tier "A+" de SELL RETEST es el peor resultado de
todo el dataset: 15 de 16 SL, E[R]=-0.743. Mirando el detalle
(`dataset.jsonl`): las señales A+ tienen `rr1` sistemáticamente alto (1.6 a
10.4, varias >4) y en su mayoría `nearEdge=-1` (13/16). El modelo P(TP1)
in-sample pondera `rr1` con el coeficiente más fuerte de todos y signo
**negativo** (-0.757: a mayor distancia del objetivo en R, menor
probabilidad de tocarlo antes del SL) y `nearEdge` con signo positivo
(+0.447: `edge=-1` es la peor rama, confirmado también en la regla #2 de
arriba). Es decir: **el criterio que hoy califica una señal como "A+" en
Pine parece estar seleccionando precisamente las dos características que,
empíricamente, más *reducen* la probabilidad de éxito** (RR de entrada
alto/objetivo lejano + señal lejos del borde de la zona). Hipótesis: la
lógica de scoring de tier en `scalp_command.pine` puede estar tratando "RR
más generoso" como sinónimo de "mejor calidad" cuando en la práctica es lo
contrario para SELL RETEST. **No se propone cambio de Pine todavía (n=16 <
20)**, pero se recomienda a Jesús revisar la fórmula de tier A+ en el
indicador cuanto antes — no como resultado estadístico sino como posible
error de diseño con evidencia ya consistente. Vigilar de cerca: si con
n=20+ se sostiene, es "cambio del mes" candidato para la próxima revisión
semanal.

### Entrada
- Óptima: _pendiente_ — `entryZoneTk` insuficiente en la mayoría de outcomes.

### Gestión
- SL óptimo: `loserMFEbeforeSL_p50` global (away-from-news) 2.0 ticks —
  descriptivo. `revAfterSL_rate` away-from-news 62.9% vs near-news 36.5%:
  la mayoría de las pérdidas revierten después del SL, otra vez apuntando a
  SL ajustado más que a dirección equivocada, y más marcado lejos de
  noticias.
- Objetivo: contrafactual `nextLevel` (0.276 E[R], n=8 global — todavía no
  cortado por side) supera a RR fijo 1R (0.258) y empata con 1.5/2/3R fijos
  (0.276 los tres); `altSL_0.5x_struct` (SL más ajustado) sube a 0.316 pero
  n=8 es demasiado chico para actuar.
- Parcial 1 / modelo GESTIONADO vs INGENUO (`managed_vs_naive`): en SELL
  RETEST el gestionado bate al ingenuo en 1m y 5m, pero **pierde por
  primera vez en 2m** — 1m delta +0.165 (n=144, naive -0.004 → managed
  0.16, el salto más grande en volumen), 2m delta **-0.015** (n=53, naive
  0.087 → managed 0.072), 5m delta +0.169 (n=17, naive 0.695 → managed
  0.864). El global (todos los kind/side) es delta +0.119 (n=255,
  naive 0.049 → managed 0.168) — la escalera sigue aportando en conjunto,
  pero en 2m/SELL específicamente NO conviene la gestión con parciales
  sobre el ingenuo con la muestra actual; vigilar si se sostiene.
- ¿Trailing tras +1R?: `beAfterM1_rate` 18.8% global — descriptivo, sin
  contrafactual propio todavía.

### Contextos a evitar
- `nearEdge=-1` (ver regla #2) y `tier=A+` (ver anomalía arriba) — ambos
  con E[R] muy negativo y muestra ya razonable (n=48 y n=16).
- Autopsia de SL sobre las 94 pérdidas SHORT (recalculado hoy sin el cap de
  60 filas que trunca el detalle mostrado en `report.md`): `RR-bajo` 40/94
  (43%) y `stop-en-el-minimo` 40/94 (43%) **siguen empatadas como causa
  dominante**, `contra-estructura` 32/94 (34%), `sin-nivel-detras` 21/94
  (22%), `chop` 16/94 (17%), `sin-causa-clara` 14/94, `SL-muy-pegado` 11/94,
  `estirado` 5/94. El empate RR-bajo/stop-en-el-mínimo se mantiene estable
  desde la revisión anterior (era 22/44 y 22/44) — **sigue siendo la causa
  de SL dominante del mes, doble**: RR de entrada demasiado bajo Y el SL
  colocado justo donde el precio hace mínimo/máximo antes de revertir.
  Ninguna de las dos está mitigada todavía por un experimento `confirmed` —
  sigue bloqueando el gate de ejecución.
- Hipótesis de cruce con Session Analyst (§8 de `agent-instructions.md`):
  sigue sin cuantificarse — `analyze.py` no tiene todavía un cruce
  histórico fecha+símbolo entre el veredicto GO/WAIT/AVOID del SA y el
  resultado del par. Sigue siendo la mejora permanente pendiente más
  valiosa para la próxima revisión semanal.

### Decaimiento
Sólo 2026-W36 en `decay_weekly` (n=270 en todo el dataset, WR 54.4%, E[R]
0.054) — sin semana previa para comparar decaimiento real todavía.

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
- 2026-09-02 (corrida formal del agente): salto de muestra n=123→222 (151×
  1m, 53× 2m, 18× 5m). **El 5m certifica por primera vez**
  (`survives_fdr10=true`, CI90=[0.372,1.0], WR 88.9%, E[R]=0.687, PF=7.19,
  n=18) — primer segmento del dataset con confianza estadística real,
  veredicto TOMAR. Se detecta y documenta una **anomalía fuerte**:
  `tier=A+` es el peor resultado del dataset (n=16, WR 6.2%, E[R]=-0.743,
  PF=0.21), aparentemente invertido — selecciona `rr1` alto y
  `nearEdge=-1`, ambos con signo negativo para P(TP1) según el modelo. Se
  recomienda a Jesús auditar la fórmula de tier A+ en Pine; no se propone
  cambio todavía (n<20). `managed_vs_naive` en 2m/SELL pasa a negativo por
  primera vez (delta -0.015, n=53) — vigilar. Autopsia de SL recalculada
  sin el cap de 60 filas que trunca `report.md` (RR-bajo y
  stop-en-el-mínimo empatados 40/94, estable vs revisión previa). Mejora
  permanente en `analyze.py`: se agregan los cortes cruzados
  `by_kindside_edge`/`by_kindside_tier`/`by_kindside_aligned` (pedido
  explícito de la nota anterior) — ya no se aproximan a mano. Además, se
  encontró y corrigió *de nuevo* el bug de `news_context` (el fix de la
  entrada anterior se había perdido: el histórico de git muestra que un
  `git pull` con "forced update" sobre `origin/main` reescribió la rama y
  un commit posterior reintrodujo el código viejo sin querer). Recordatorio
  para corridas futuras: no forzar push sobre `main`; si `git pull` reporta
  "forced update", revisar con cuidado que no se haya perdido trabajo antes
  de continuar.
