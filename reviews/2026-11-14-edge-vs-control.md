# Scalp CC · ventaja frente a control (2026-11-14)

## Diseño
- Datos: 59 483 pares señal/resultado (dataset.jsonl, 1 sep a 14 nov, 65 días) con barras de 5m de Yahoo (bus del Session Analyst) para NQ, ES, GC, YM, CL, BTC, ETH. Fuera 6 515 sin barras, sin geometría o sin R.
- Re-simulación igual para señal y control, sobre barras de 5m: entrada a la apertura de la primera vela de 5m tras la señal, mismo SL y TP1 en ticks que la señal, timeout = 40 velas del TF de la señal, SL y TP en la misma vela = SL (conservador, 5 % de los casos), sin TP2.
- Control: por cada señal, 5 entradas al azar del mismo símbolo, mismo lado, misma hora de NY (sesión), otro día en ± 10 días, mismo SL / TP / timeout. Segundo control: espejo (misma hora, lado contrario).
- IC 95 % de E[R] con bootstrap por días (las señales de un mismo día no son independientes; el bootstrap por señal de analyze.py da IC demasiado estrechos). WR con Wilson 95 %.
- Coste: 2 ticks ida y vuelta, en R (= 2 / slTk). Mediana del SL: 20 ticks, así que el coste medio es 0.13 R.
- Script: `reviews/2026-11-14-edge_ctrl.py`.

## Resultado global
| | n | WR | E[R] |
|---|---|---|---|
| Pine (lo que mide el agente) | 59 483 | 50.5 % [50.1, 50.9] | +0.057 [+0.034, +0.081] |
| Pine menos 2 ticks de coste | | | **-0.073** |
| Señal re-simulada en 5m | | 47.4 % | -0.038 |
| Control al azar (misma hora y lado) | | 44.7 % | -0.083 |
| Espejo (lado contrario) | | | -0.058 |
| **Señal menos control** | | +2.7 pts | **+0.045 [+0.022, +0.070]** |

Lectura:
1. A diferencia de TDL Key Levels, **sí hay una ventaja medible sobre el azar: +0.045 R por señal**, con IC por días que no toca 0. Es pequeña.
2. **No cubre los costes.** Con 2 ticks por trade el E[R] de Pine pasa de +0.057 a -0.073. Solo los segmentos con SL grande en ticks (5m, 15m, 29m, NQ, crypto) quedan cerca de 0 o encima.
3. El +0.057 de Pine está inflado: si la vela toca TP1 y TP2 a la vez cobra TP2 (aporta +0.041 R por señal de media), y si toca SL y TP en la misma vela decide por la apertura. Con la regla conservadora la señal da -0.038.
4. El WR de 50 % está por debajo del WR que daría el azar con ese R:R (51.1 %): el WR solo no dice nada; manda E[R].

## Por tier (lo más importante)
| tier | n | WR Pine | E[R] Pine | señal menos control |
|---|---|---|---|---|
| A+ | 3 914 | 24.5 % [23.2, 25.8] | +0.049 [-0.048, +0.159] | +0.060 [-0.047, +0.168] |
| B | 24 909 | 52.0 % | +0.040 | +0.033 [+0.007, +0.056] |
| C | 30 660 | 52.5 % | +0.072 | +0.053 [+0.027, +0.079] |

**El tier no ordena la calidad.** A+ no se separa del control, y C (las que no se pintan) rinde igual o mejor que B. B SHORT: +0.000 frente al control.

## Por TF, tipo, símbolo y sesión (señal menos control, IC 95 % por días)
- TF: 1m +0.042 [+0.018, +0.069] · 2m +0.043 [+0.010, +0.074] · 3m +0.046 · 5m +0.054 [+0.012, +0.098] · 15m +0.055 [-0.013, +0.127] · 29m +0.130 [+0.044, +0.217] (n 790, solo 18 días).
- INV LONG +0.138 [+0.049, +0.233] (n 745) · INV SHORT +0.148 [+0.059, +0.247] (n 514) · RETEST LONG +0.050 · RETEST SHORT +0.034.
- Símbolo: YM +0.082 [+0.040, +0.125] · GC +0.047 [+0.004, +0.091] · NQ +0.025 [-0.023, +0.072] · ES +0.025 [-0.015, +0.062] · CL +0.025 [-0.019, +0.068] · BTC +0.103 y ETH +0.083 (20 días).
- Sesión: Asia +0.056 [+0.025, +0.086] · NY +0.049 [+0.000, +0.100] · Londres +0.041 [-0.008, +0.091] · sin KZ +0.032 [-0.008, +0.072].
- NQ, el símbolo que opera Jesús, no se separa del control.

## Ruido
- 65 días en total; 3m, 15m, 29m y crypto solo 16-20 días. Con tantos cortes (unos 40 aquí) alguno saldrá "significativo" por azar; tratar como hipótesis todo lo que no sea el resultado global.
- La re-simulación en 5m coincide con Pine en el 73 % de los casos (granularidad distinta); la comparación justa es señal frente a control con la misma mecánica, no los valores absolutos.

## Auditoría del método (agent-instructions.md, README, execution-ladder.md)
Arreglado (texto inequívoco):
- README apuntaba al método en `scalp-agent/agent-instructions.md` del repo principal: es una copia v1 vieja que la rutina no clona. El método vigente es `agent-instructions.md` de este repo.

Propuestas (cambian lógica, decide Jesús):
1. Meter costes en `analyze.py` (2 ticks por defecto, por símbolo) y que todo E[R], gate y sombra sea neto. Hoy el gate dice `readyForLive` con E[R] bruto.
2. Arreglar la resolución en Pine: misma vela TP1 + TP2 debe cobrar TP1 (primer toque), y misma vela SL + TP contar SL. Infla el E[R] unos 0.04-0.06 R.
3. Bootstrap por días en `bootstrap_er_ci` (hoy por señal, IC demasiado estrechos con señales simultáneas en 6 TF y 7 símbolos).
4. Añadir este control al azar a `analyze.py` como línea base fija de cada segmento; una regla solo vale si supera al control.
5. Revisar el tier: A+ no supera al control y C rinde más que B. O se recalcula o deja de usarse como filtro.
6. Gate 29m/RETEST/LONG: n 359 en 17 días, demasiado poco para hablar de live.
7. execution-ladder.md aún pide coherencia con el veredicto AVOID del Session Analyst, que el método dio por refutado el 2026-10-31 (paso 8): quitar esa regla.
8. Paso 10b (narrativa de 150-250 palabras por idioma cada día) y las reglas de semanas: valorar si recortar para ahorrar tokens.
