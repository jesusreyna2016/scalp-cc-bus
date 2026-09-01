# Escalera de ejecución · Scalp CC

Del asesor pasivo al bot en cuenta live personal, en peldaños. El agente puntúa
cada peldaño y NO recomienda subir al siguiente hasta que se cumplan sus gates.
Cada peldaño mantiene el logueo de todo (señal cruda + lo que se hizo + resultado).

| # | Peldaño | Qué hace | Gate para pasar al siguiente |
|---|---------|----------|------------------------------|
| 0 | **Asesor** (actual) | Loguea señales + outcomes, mide, autopsia de SL, playbook, propuestas semanales. Cero ejecución. | `analyze.py` corriendo a diario, >= 5 pares resueltos, pipeline sin huérfanos crecientes. |
| 1 | **Sombra** | El agente publica cada corrida qué señales habría tomado y con qué SL/objetivo (`state.json.shadowRules`), y compara ese conjunto contra el indicador crudo y contra tier A+/B. Nada se ejecuta. | El conjunto sombra bate al indicador crudo en E[R] durante 3 semanas seguidas, n >= 60 en el segmento objetivo. |
| 2 | **Semi-auto (ticket)** | En cada señal que pasa las reglas sombra, se deja un ticket listo (entrada, SL, TP1, tamaño) que Jesús confirma con un clic. Se loguea confirmado/rechazado y el fill real. | n >= 100, WR TP1 estable 3 semanas, E[R] > 0 con PF >= 1.3, causa de SL dominante mitigada por un experimento `confirmed`. Slippage real medido y dentro de tolerancia. |
| 3 | **Auto en demo** | El puente NinjaScript ejecuta solo en cuenta demo personal. El agente vigila: drawdown, racha de SL, desvío entre P(TP1) predicho y real. Kill-switch por reglas duras (N SL seguidos, DD diario). | 4 semanas en demo con E[R] y DD dentro de lo esperado por el modelo. Sin bug de ejecución. Reglas de riesgo probadas (kill-switch disparó y funcionó). |
| 4 | **Auto live micro** | Igual que el 3 pero en cuenta live personal de Jesús, tamaño mínimo (1 micro). Riesgo real acotado. | 4 semanas live micro con métricas consistentes con la demo. Sin sorpresas de slippage/latencia. |
| 5 | **Escalado** | Subir tamaño por pasos, cada paso con su propio período de verificación. | Cada escalón: 3-4 semanas estables antes del siguiente. |

## Reglas duras que aplican desde el peldaño 2 en adelante

- Máximo de trades por día (empezar conservador).
- Lockout tras N SL seguidos en el día.
- Kill-switch por drawdown diario en $ o en R.
- No operar en ventana de noticias de alto impacto.
- Coherencia con el veredicto del Session Analyst: si dice AVOID el instrumento,
  el peldaño 2+ no arma tickets en ese instrumento ese día (a menos que la data
  demuestre que la señal de scalp es indiferente a eso).
- Cualquier cambio de parámetro del indicador reinicia el contador de "semanas
  estables" del peldaño actual.

## Nota

Esto es infraestructura de decisión, no una promesa de rendimiento. Si un peldaño
no cumple su gate, se queda ahí o se baja uno. El objetivo del agente es que la
decisión de subir sea por evidencia, no por impaciencia.
