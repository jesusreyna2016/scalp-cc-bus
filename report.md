# Scalp CC · report 2026-09-18T01:14Z
- signals=11452 outcomes=10925 pares_resueltos=11452 pendientes=0 huerfanos=26

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: semana ya cerrada 2026-W36 bajo de n=3183 a n=3121 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W37 bajo de n=5389 a n=5315 desde la corrida previa -- vigilar, puede ser deduplicacion.
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.213 vs 0.05, delta 0.163 CI90 [0.113, 0.211], n 7109). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.217 vs 0.068, delta 0.149 CI90 [0.06, 0.253], n 2054). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.125 CI90 [0.046, 0.202], n 611). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.078 CI90 [0.041, 0.119], n 2447). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.049, "ci90": [0.029, 0.068], "p_mean_le_0": 0.0, "n": 10899}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 112 | 45.5 | 0.102 | 1.22 | 47 | 13.0 | 11.5 | 21.3 |
| 1m/INV/SHORT | 88 | 50.0 | 0.091 | 1.2 | 38 | 20.0 | 11.25 | 18.4 |
| 1m/RETEST/LONG | 4104 | 44.9 | 0.034 | 1.07 | 1952 | 14.0 | 10.0 | 29.2 |
| 1m/RETEST/SHORT | 2831 | 44.0 | 0.051 | 1.1 | 1297 | 18.0 | 12.0 | 31.8 |
| 2m/INV/LONG | 35 | 48.6 | -0.124 | 0.74 | 15 | 10.0 | 8.0 | 26.7 |
| 2m/INV/SHORT | 39 | 35.9 | 0.017 | 1.03 | 21 | 21.0 | 15.75 | 38.1 |
| 2m/RETEST/LONG | 1860 | 46.3 | -0.004 | 0.99 | 876 | 16.0 | 13.0 | 37.0 |
| 2m/RETEST/SHORT | 1220 | 48.0 | 0.088 | 1.19 | 538 | 22.0 | 13.0 | 40.1 |
| 5m/INV/LONG | 15 | 66.7 | 0.513 | 4.33 | 2 | 31.0 | 31.25 | 50.0 |
| 5m/INV/SHORT | 8 | 75.0 | 0.615 | 3.46 | 2 | 58.0 | 68.75 | 100.0 |
| 5m/RETEST/LONG | 693 | 51.4 | 0.157 | 1.36 | 287 | 27.0 | 19.25 | 50.5 |
| 5m/RETEST/SHORT | 447 | 47.4 | 0.089 | 1.19 | 188 | 34.0 | 23.0 | 36.7 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 798 | 25.3 | 0.092 | 1.14 | 487 | 28.0 | 15.0 | 19.3 |
| B | 4771 | 46.6 | 0.05 | 1.11 | 2170 | 17.0 | 13.0 | 33.3 |
| C | 5883 | 47.9 | 0.041 | 1.09 | 2606 | 16.0 | 12.0 | 36.6 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 4160 | 49.4 | 0.073 | 1.16 | 1847 | 13.0 | 9.0 | 39.1 |
| London | 1805 | 45.0 | -0.034 | 0.93 | 911 | 18.0 | 12.0 | 33.9 |
| NY | 2040 | 44.9 | 0.161 | 1.34 | 858 | 26.0 | 16.0 | 38.8 |
| Sin KZ | 3447 | 42.3 | -0.001 | 1.0 | 1647 | 19.0 | 14.0 | 24.5 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 2729 | 44.4 | 0.052 | 1.11 | 1258 | 21.0 | 14.0 | 31.9 |
| edge=0 | 5087 | 48.0 | 0.043 | 1.09 | 2278 | 15.0 | 11.0 | 38.6 |
| edge=1 | 3636 | 43.6 | 0.053 | 1.11 | 1727 | 18.0 | 14.0 | 28.3 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| aligned=1 | 11443 | 45.8 | 0.048 | 1.1 | 5262 | 17.0 | 13.0 | 33.6 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 70 | 54.3 | 0.145 | 1.36 | 25 | 10.5 | 10.75 | 28.0 |
| INV/LONG|edge=1 | 88 | 43.2 | 0.026 | 1.06 | 37 | 20.5 | 16.5 | 18.9 |
| INV/SHORT|edge=-1 | 78 | 41.0 | 0.098 | 1.2 | 38 | 22.0 | 12.5 | 26.3 |
| INV/SHORT|edge=0 | 49 | 53.1 | -0.03 | 0.93 | 21 | 16.0 | 15.5 | 33.3 |
| INV/SHORT|edge=1 | 8 | 75.0 | 0.901 | 4.6 | 2 | 32.5 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 264 | 53.4 | 0.172 | 1.41 | 106 | 12.0 | 7.0 | 50.9 |
| RETEST/LONG|edge=0 | 2989 | 48.5 | 0.005 | 1.01 | 1378 | 14.0 | 10.0 | 38.8 |
| RETEST/LONG|edge=1 | 3404 | 43.2 | 0.052 | 1.1 | 1631 | 18.0 | 14.0 | 27.6 |
| RETEST/SHORT|edge=-1 | 2383 | 43.6 | 0.036 | 1.07 | 1112 | 23.0 | 15.0 | 30.2 |
| RETEST/SHORT|edge=0 | 1979 | 47.0 | 0.101 | 1.22 | 854 | 18.0 | 11.0 | 38.8 |
| RETEST/SHORT|edge=1 | 136 | 54.4 | 0.047 | 1.11 | 57 | 14.0 | 10.0 | 54.4 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 40 | 37.5 | -0.076 | 0.86 | 20 | 16.5 | 15.5 | 15.0 |
| INV/LONG|tier=C | 122 | 51.6 | 0.144 | 1.36 | 44 | 14.0 | 12.5 | 27.3 |
| INV/SHORT|tier=B | 39 | 46.2 | 0.096 | 1.2 | 19 | 19.0 | 8.75 | 10.5 |
| INV/SHORT|tier=C | 96 | 47.9 | 0.103 | 1.23 | 42 | 24.0 | 28.0 | 35.7 |
| RETEST/LONG|tier=A+ | 502 | 24.5 | 0.064 | 1.1 | 313 | 23.0 | 14.0 | 17.3 |
| RETEST/LONG|tier=B | 2776 | 46.6 | 0.071 | 1.15 | 1264 | 16.0 | 12.0 | 32.8 |
| RETEST/LONG|tier=C | 3379 | 48.6 | 0.003 | 1.01 | 1538 | 15.0 | 11.0 | 37.1 |
| RETEST/SHORT|tier=A+ | 296 | 26.7 | 0.14 | 1.22 | 174 | 40.0 | 17.5 | 23.0 |
| RETEST/SHORT|tier=B | 1916 | 46.8 | 0.021 | 1.04 | 867 | 19.0 | 14.0 | 34.8 |
| RETEST/SHORT|tier=C | 2286 | 46.7 | 0.092 | 1.2 | 982 | 19.0 | 13.0 | 36.3 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 162 | 48.1 | 0.088 | 1.2 | 64 | 14.5 | 13.75 | 23.4 |
| INV/SHORT|aligned=1 | 135 | 47.4 | 0.101 | 1.22 | 61 | 21.0 | 17.75 | 27.9 |
| RETEST/LONG|aligned=0 | 9 | 55.6 | 0.433 | 3.6 | 1 | 18.5 | 7.0 | 0.0 |
| RETEST/LONG|aligned=1 | 6648 | 46.0 | 0.035 | 1.07 | 3114 | 16.0 | 12.0 | 33.4 |
| RETEST/SHORT|aligned=1 | 4498 | 45.4 | 0.065 | 1.13 | 2023 | 20.0 | 13.0 | 34.5 |

## Autopsia de SL
n_losses=5263  causas: RR-bajo×1998, contra-estructura×1848, stop-en-el-minimo×1769, killzone-Asia-largo×1100, sin-nivel-detras×1051, estirado×924, chop×737, SL-muy-pegado×647, sin-causa-clara×531, contra-sesgo×1
- INV/LONG (n=64): killzone-Asia-largo×32, RR-bajo×27, contra-estructura×19, stop-en-el-minimo×15, estirado×15, sin-nivel-detras×8, SL-muy-pegado×7, chop×5, sin-causa-clara×1
- INV/SHORT (n=61): RR-bajo×31, contra-estructura×18, stop-en-el-minimo×17, sin-causa-clara×12, estirado×12, SL-muy-pegado×8, chop×6, sin-nivel-detras×4
- RETEST/LONG (n=3115): RR-bajo×1184, contra-estructura×1182, killzone-Asia-largo×1068, stop-en-el-minimo×1039, sin-nivel-detras×655, estirado×526, chop×469, SL-muy-pegado×369, sin-causa-clara×245, contra-sesgo×1
- RETEST/SHORT (n=2023): RR-bajo×756, stop-en-el-minimo×698, contra-estructura×629, sin-nivel-detras×384, estirado×371, sin-causa-clara×273, SL-muy-pegado×263, chop×257

## Autopsia de SL · semana 2026-W38 (para revision semanal)
n_losses=1187  causas: RR-bajo×446, contra-estructura×418, stop-en-el-minimo×412, killzone-Asia-largo×263, sin-nivel-detras×246, estirado×221, chop×152, SL-muy-pegado×136, sin-causa-clara×135
ejemplos por causa: {"RR-bajo": ["CL-1-23392-L", "YM-1-23338-S", "NQ-5-20749-L", "CL-5-20795-L", "YM-2-21454-S"], "contra-estructura": ["NQ-1-21696-L", "CL-5-20795-L", "NQ-2-22258-L", "NQ-2-22261-L", "NQ-2-22262-L"], "stop-en-el-minimo": ["YM-1-23338-S", "NQ-5-20749-L", "NQ-1-23388-L", "NQ-1-23634-L", "YM-2-22115-S"]}

## Contrafactual de gestion
```json
{
  "n": 9,
  "baseline_nextLevel_expR": 0.276,
  "fixed_1R": [
    0.258,
    8
  ],
  "fixed_1_5R": [
    0.276,
    8
  ],
  "fixed_2R": [
    0.276,
    8
  ],
  "fixed_3R": [
    0.276,
    8
  ],
  "altSL_0_5x_struct": [
    0.281,
    9
  ],
  "altSL_1_5x_struct": [
    0.26,
    9
  ],
  "note": "fixed_XR: R esperado si el objetivo fuera XR fijo con SL=struct. altSL: SL a mult del SL struct."
}
```

## Modelo GESTIONADO (escalera + parciales) vs INGENUO
```json
{
  "overall": {
    "n": 10885,
    "naive_expR": 0.048,
    "managed_expR": 0.124,
    "delta": 0.076,
    "avgEntryBetterTk_p50": 2.5,
    "fill_t3plus_pct": 46.1,
    "fill_full_pct": 32.6,
    "m1_rate": 36.7,
    "m2_rate": 22.8,
    "m3_rate": 12.3,
    "beAfterM1_rate": 17.7
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 104,
      "naive_expR": 0.102,
      "managed_expR": 0.285,
      "delta": 0.183,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 48.1,
      "fill_full_pct": 33.7,
      "m1_rate": 42.3,
      "m2_rate": 27.9,
      "m3_rate": 14.4,
      "beAfterM1_rate": 21.2
    },
    "1m/INV/SHORT": {
      "n": 85,
      "naive_expR": 0.091,
      "managed_expR": 0.289,
      "delta": 0.198,
      "avgEntryBetterTk_p50": 3.2,
      "fill_t3plus_pct": 50.6,
      "fill_full_pct": 38.8,
      "m1_rate": 37.6,
      "m2_rate": 23.5,
      "m3_rate": 14.1,
      "beAfterM1_rate": 17.6
    },
    "1m/RETEST/LONG": {
      "n": 3961,
      "naive_expR": 0.033,
      "managed_expR": 0.121,
      "delta": 0.087,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 48.1,
      "fill_full_pct": 34.5,
      "m1_rate": 35.9,
      "m2_rate": 22.5,
      "m3_rate": 11.8,
      "beAfterM1_rate": 16.6
    },
    "1m/RETEST/SHORT": {
      "n": 2649,
      "naive_expR": 0.052,
      "managed_expR": 0.157,
      "delta": 0.106,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 48.1,
      "fill_full_pct": 33.5,
      "m1_rate": 40.0,
      "m2_rate": 24.7,
      "m3_rate": 13.7,
      "beAfterM1_rate": 19.1
    },
    "2m/INV/LONG": {
      "n": 33,
      "naive_expR": -0.124,
      "managed_expR": -0.081,
      "delta": 0.043,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 54.5,
      "fill_full_pct": 36.4,
      "m1_rate": 18.2,
      "m2_rate": 18.2,
      "m3_rate": 0.0,
      "beAfterM1_rate": 3.0
    },
    "2m/INV/SHORT": {
      "n": 39,
      "naive_expR": 0.017,
      "managed_expR": -0.044,
      "delta": -0.061,
      "avgEntryBetterTk_p50": 3.4,
      "fill_t3plus_pct": 46.2,
      "fill_full_pct": 38.5,
      "m1_rate": 25.6,
      "m2_rate": 23.1,
      "m3_rate": 12.8,
      "beAfterM1_rate": 5.1
    },
    "2m/RETEST/LONG": {
      "n": 1776,
      "naive_expR": -0.005,
      "managed_expR": 0.063,
      "delta": 0.067,
      "avgEntryBetterTk_p50": 2.5,
      "fill_t3plus_pct": 44.1,
      "fill_full_pct": 30.1,
      "m1_rate": 34.3,
      "m2_rate": 20.3,
      "m3_rate": 10.8,
      "beAfterM1_rate": 17.6
    },
    "2m/RETEST/SHORT": {
      "n": 1160,
      "naive_expR": 0.088,
      "managed_expR": 0.146,
      "delta": 0.058,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 46.3,
      "fill_full_pct": 33.8,
      "m1_rate": 36.9,
      "m2_rate": 23.6,
      "m3_rate": 12.2,
      "beAfterM1_rate": 17.8
    },
    "5m/INV/LONG": {
      "n": 13,
      "naive_expR": 0.513,
      "managed_expR": 0.332,
      "delta": -0.181,
      "avgEntryBetterTk_p50": 4.0,
      "fill_t3plus_pct": 38.5,
      "fill_full_pct": 23.1,
      "m1_rate": 30.8,
      "m2_rate": 23.1,
      "m3_rate": 7.7,
      "beAfterM1_rate": 15.4
    },
    "5m/INV/SHORT": {
      "n": 8,
      "naive_expR": 0.615,
      "managed_expR": 0.657,
      "delta": 0.042,
      "avgEntryBetterTk_p50": 8.4,
      "fill_t3plus_pct": 62.5,
      "fill_full_pct": 37.5,
      "m1_rate": 37.5,
      "m2_rate": 25.0,
      "m3_rate": 25.0,
      "beAfterM1_rate": 12.5
    },
    "5m/RETEST/LONG": {
      "n": 651,
      "naive_expR": 0.157,
      "managed_expR": 0.089,
      "delta": -0.068,
      "avgEntryBetterTk_p50": 0.7,
      "fill_t3plus_pct": 32.6,
      "fill_full_pct": 23.8,
      "m1_rate": 34.3,
      "m2_rate": 22.6,
      "m3_rate": 12.9,
      "beAfterM1_rate": 18.9
    },
    "5m/RETEST/SHORT": {
      "n": 406,
      "naive_expR": 0.088,
      "managed_expR": 0.146,
      "delta": 0.059,
      "avgEntryBetterTk_p50": 4.35,
      "fill_t3plus_pct": 42.1,
      "fill_full_pct": 26.6,
      "m1_rate": 37.2,
      "m2_rate": 22.9,
      "m3_rate": 12.6,
      "beAfterM1_rate": 18.7
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 9433,
    "layer_expR": 0.055,
    "orig_expR": 0.21,
    "delta_orig_minus_layer": 0.155,
    "delta_ci90": [
      0.112,
      0.196
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 47.9,
    "orig_wrTP1": 33.5,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 9.0,
    "orig_wider_pct": 4.1,
    "orig_saved_from_SL": 19,
    "orig_caused_SL": 1385
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 0,
  "invalid_by_seg": {},
  "by_basis": {
    "candle1": {
      "n": 270,
      "layer_expR": 0.093,
      "orig_expR": 0.063,
      "delta_orig_minus_layer": -0.029,
      "delta_ci90": [
        -0.24,
        0.205
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.6,
      "orig_wrTP1": 28.1,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 7.8,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 59
    },
    "legacy": {
      "n": 7,
      "layer_expR": 0.339,
      "orig_expR": 1.227,
      "delta_orig_minus_layer": 0.889,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 85.7,
      "orig_wrTP1": 85.7,
      "slTk_p50": 6.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 42.9,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 1
    },
    "retestBar": {
      "n": 7109,
      "layer_expR": 0.05,
      "orig_expR": 0.213,
      "delta_orig_minus_layer": 0.163,
      "delta_ci90": [
        0.113,
        0.211
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.3,
      "orig_wrTP1": 34.0,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.3,
      "orig_saved_from_SL": 17,
      "orig_caused_SL": 1035
    },
    "retestBar2": {
      "n": 2054,
      "layer_expR": 0.068,
      "orig_expR": 0.217,
      "delta_orig_minus_layer": 0.149,
      "delta_ci90": [
        0.06,
        0.253
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.5,
      "orig_wrTP1": 32.4,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.7,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 291
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 104,
      "layer_expR": 0.102,
      "orig_expR": -0.074,
      "delta_orig_minus_layer": -0.176,
      "delta_ci90": [
        -0.476,
        0.136
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.0,
      "orig_wrTP1": 23.1,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 3.0,
      "orig_wider_pct": 5.8,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 27
    },
    "1m/INV/SHORT": {
      "n": 75,
      "layer_expR": 0.096,
      "orig_expR": -0.055,
      "delta_orig_minus_layer": -0.151,
      "delta_ci90": [
        -0.525,
        0.243
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 50.7,
      "orig_wrTP1": 26.7,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 18
    },
    "1m/RETEST/LONG": {
      "n": 3410,
      "layer_expR": 0.037,
      "orig_expR": 0.182,
      "delta_orig_minus_layer": 0.145,
      "delta_ci90": [
        0.076,
        0.214
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.0,
      "orig_wrTP1": 29.7,
      "slTk_p50": 18.0,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 1.3,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 555
    },
    "1m/RETEST/SHORT": {
      "n": 2179,
      "layer_expR": 0.059,
      "orig_expR": 0.214,
      "delta_orig_minus_layer": 0.155,
      "delta_ci90": [
        0.064,
        0.249
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.3,
      "orig_wrTP1": 32.2,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.6,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 309
    },
    "2m/INV/LONG": {
      "n": 33,
      "layer_expR": -0.124,
      "orig_expR": 0.635,
      "delta_orig_minus_layer": 0.759,
      "delta_ci90": [
        -0.072,
        1.728
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 51.5,
      "orig_wrTP1": 33.3,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 12.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 6
    },
    "2m/INV/SHORT": {
      "n": 38,
      "layer_expR": 0.006,
      "orig_expR": 0.417,
      "delta_orig_minus_layer": 0.411,
      "delta_ci90": [
        -0.059,
        1.034
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 34.2,
      "orig_wrTP1": 31.6,
      "slTk_p50": 23.5,
      "slOrigTk_p50": 6.0,
      "orig_wider_pct": 5.3,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 2
    },
    "2m/RETEST/LONG": {
      "n": 1599,
      "layer_expR": 0.012,
      "orig_expR": 0.085,
      "delta_orig_minus_layer": 0.074,
      "delta_ci90": [
        0.005,
        0.145
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.0,
      "orig_wrTP1": 35.4,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 219
    },
    "2m/RETEST/SHORT": {
      "n": 984,
      "layer_expR": 0.103,
      "orig_expR": 0.226,
      "delta_orig_minus_layer": 0.123,
      "delta_ci90": [
        0.031,
        0.223
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.9,
      "orig_wrTP1": 36.9,
      "slTk_p50": 23.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.8,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 140
    },
    "5m/INV/LONG": {
      "n": 13,
      "layer_expR": 0.513,
      "orig_expR": -0.505,
      "delta_orig_minus_layer": -1.018,
      "delta_ci90": [
        -1.554,
        -0.546
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 76.9,
      "orig_wrTP1": 38.5,
      "slTk_p50": 49.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 23.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 5
    },
    "5m/INV/SHORT": {
      "n": 7,
      "layer_expR": 0.629,
      "orig_expR": -0.193,
      "delta_orig_minus_layer": -0.821,
      "delta_ci90": [
        null,
        null
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 71.4,
      "orig_wrTP1": 57.1,
      "slTk_p50": 46.0,
      "slOrigTk_p50": 88.0,
      "orig_wider_pct": 42.9,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 1
    },
    "5m/RETEST/LONG": {
      "n": 622,
      "layer_expR": 0.149,
      "orig_expR": 0.461,
      "delta_orig_minus_layer": 0.312,
      "delta_ci90": [
        0.123,
        0.525
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 54.7,
      "orig_wrTP1": 44.7,
      "slTk_p50": 28.0,
      "slOrigTk_p50": 16.0,
      "orig_wider_pct": 15.8,
      "orig_saved_from_SL": 5,
      "orig_caused_SL": 67
    },
    "5m/RETEST/SHORT": {
      "n": 369,
      "layer_expR": 0.07,
      "orig_expR": 0.616,
      "delta_orig_minus_layer": 0.546,
      "delta_ci90": [
        0.184,
        0.976
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.9,
      "orig_wrTP1": 43.1,
      "slTk_p50": 32.0,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 20.1,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 36
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 3121,
    "wrTP1": 44.7,
    "expR": -0.019
  },
  "2026-W37": {
    "n": 5315,
    "wrTP1": 46.8,
    "expR": 0.071
  },
  "2026-W38": {
    "n": 3016,
    "wrTP1": 45.1,
    "expR": 0.081
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 38,
      "wrTP1": 44.7,
      "expR": 0.278,
      "pf": 1.59
    },
    "1m/INV/SHORT": {
      "n": 19,
      "wrTP1": 68.4,
      "expR": 0.264,
      "pf": 1.95
    },
    "1m/RETEST/LONG": {
      "n": 1363,
      "wrTP1": 42.9,
      "expR": -0.012,
      "pf": 0.98
    },
    "1m/RETEST/SHORT": {
      "n": 442,
      "wrTP1": 43.4,
      "expR": -0.012,
      "pf": 0.98
    },
    "2m/INV/LONG": {
      "n": 17,
      "wrTP1": 41.2,
      "expR": -0.228,
      "pf": 0.61
    },
    "2m/INV/SHORT": {
      "n": 6,
      "wrTP1": 50.0,
      "expR": -0.267,
      "pf": 0.47
    },
    "2m/RETEST/LONG": {
      "n": 681,
      "wrTP1": 46.0,
      "expR": -0.065,
      "pf": 0.87
    },
    "2m/RETEST/SHORT": {
      "n": 210,
      "wrTP1": 40.5,
      "expR": -0.114,
      "pf": 0.79
    },
    "5m/INV/LONG": {
      "n": 6,
      "wrTP1": 100.0,
      "expR": 0.712,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 0.018,
      "pf": 1.07
    },
    "5m/RETEST/LONG": {
      "n": 242,
      "wrTP1": 52.5,
      "expR": 0.082,
      "pf": 1.18
    },
    "5m/RETEST/SHORT": {
      "n": 93,
      "wrTP1": 47.3,
      "expR": -0.021,
      "pf": 0.96
    }
  },
  "2026-W37": {
    "1m/INV/LONG": {
      "n": 36,
      "wrTP1": 41.7,
      "expR": -0.046,
      "pf": 0.9
    },
    "1m/INV/SHORT": {
      "n": 56,
      "wrTP1": 41.1,
      "expR": 0.038,
      "pf": 1.07
    },
    "1m/RETEST/LONG": {
      "n": 1596,
      "wrTP1": 45.2,
      "expR": 0.048,
      "pf": 1.1
    },
    "1m/RETEST/SHORT": {
      "n": 1708,
      "wrTP1": 44.9,
      "expR": 0.043,
      "pf": 1.09
    },
    "2m/INV/LONG": {
      "n": 9,
      "wrTP1": 55.6,
      "expR": -0.009,
      "pf": 0.98
    },
    "2m/INV/SHORT": {
      "n": 31,
      "wrTP1": 35.5,
      "expR": 0.137,
      "pf": 1.27
    },
    "2m/RETEST/LONG": {
      "n": 673,
      "wrTP1": 47.7,
      "expR": 0.045,
      "pf": 1.09
    },
    "2m/RETEST/SHORT": {
      "n": 747,
      "wrTP1": 51.4,
      "expR": 0.147,
      "pf": 1.32
    },
    "5m/INV/LONG": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 1.055,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 1.212,
      "pf": 5.85
    },
    "5m/RETEST/LONG": {
      "n": 234,
      "wrTP1": 52.6,
      "expR": 0.208,
      "pf": 1.47
    },
    "5m/RETEST/SHORT": {
      "n": 217,
      "wrTP1": 51.6,
      "expR": 0.111,
      "pf": 1.24
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 38,
      "wrTP1": 50.0,
      "expR": 0.056,
      "pf": 1.13
    },
    "1m/INV/SHORT": {
      "n": 13,
      "wrTP1": 61.5,
      "expR": 0.074,
      "pf": 1.22
    },
    "1m/RETEST/LONG": {
      "n": 1145,
      "wrTP1": 46.9,
      "expR": 0.071,
      "pf": 1.15
    },
    "1m/RETEST/SHORT": {
      "n": 681,
      "wrTP1": 42.0,
      "expR": 0.121,
      "pf": 1.27
    },
    "2m/INV/LONG": {
      "n": 9,
      "wrTP1": 55.6,
      "expR": -0.019,
      "pf": 0.94
    },
    "2m/INV/SHORT": {
      "n": 2,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 506,
      "wrTP1": 44.9,
      "expR": 0.015,
      "pf": 1.03
    },
    "2m/RETEST/SHORT": {
      "n": 263,
      "wrTP1": 44.1,
      "expR": 0.072,
      "pf": 1.16
    },
    "5m/INV/LONG": {
      "n": 5,
      "wrTP1": 20.0,
      "expR": -0.607,
      "pf": 0.09
    },
    "5m/RETEST/LONG": {
      "n": 217,
      "wrTP1": 48.8,
      "expR": 0.188,
      "pf": 1.44
    },
    "5m/RETEST/SHORT": {
      "n": 137,
      "wrTP1": 40.9,
      "expR": 0.132,
      "pf": 1.29
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 10507,
  "brier": 0.2209,
  "bias": -0.094,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.213
    },
    {
      "feature": "stretchAtr",
      "weight": -0.109
    },
    {
      "feature": "nearTk",
      "weight": -0.076
    },
    {
      "feature": "biasScore",
      "weight": -0.061
    },
    {
      "feature": "structDir",
      "weight": 0.051
    },
    {
      "feature": "rvol",
      "weight": 0.051
    },
    {
      "feature": "nearEdge",
      "weight": 0.035
    },
    {
      "feature": "aligned",
      "weight": -0.027
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.021
    },
    {
      "feature": "hourNY",
      "weight": 0.009
    },
    {
      "feature": "chopIdx",
      "weight": -0.005
    },
    {
      "feature": "emaStack",
      "weight": 0.002
    },
    {
      "feature": "entryZoneTk",
      "weight": 0.001
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.154,
      "actual": 0.168,
      "n": 1050
    },
    {
      "bin": 1,
      "pred": 0.348,
      "actual": 0.3,
      "n": 1051
    },
    {
      "bin": 2,
      "pred": 0.436,
      "actual": 0.352,
      "n": 1051
    },
    {
      "bin": 3,
      "pred": 0.487,
      "actual": 0.409,
      "n": 1050
    },
    {
      "bin": 4,
      "pred": 0.528,
      "actual": 0.516,
      "n": 1051
    },
    {
      "bin": 5,
      "pred": 0.561,
      "actual": 0.546,
      "n": 1051
    },
    {
      "bin": 6,
      "pred": 0.586,
      "actual": 0.604,
      "n": 1050
    },
    {
      "bin": 7,
      "pred": 0.609,
      "actual": 0.663,
      "n": 1051
    },
    {
      "bin": 8,
      "pred": 0.631,
      "actual": 0.696,
      "n": 1051
    },
    {
      "bin": 9,
      "pred": 0.665,
      "actual": 0.737,
      "n": 1051
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": false,
  "reason": "pocas semanas",
  "weeks": 3
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.102,
    "ci90": [
      -0.104,
      0.305
    ],
    "p_mean_le_0": 0.21,
    "n": 104,
    "survives_fdr10": false
  },
  "1m/INV/SHORT": {
    "expR": 0.091,
    "ci90": [
      -0.11,
      0.322
    ],
    "p_mean_le_0": 0.242,
    "n": 85,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.034,
    "ci90": [
      0.0,
      0.066
    ],
    "p_mean_le_0": 0.045,
    "n": 3965,
    "survives_fdr10": false
  },
  "1m/RETEST/SHORT": {
    "expR": 0.051,
    "ci90": [
      0.01,
      0.09
    ],
    "p_mean_le_0": 0.024,
    "n": 2656,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": -0.124,
    "ci90": [
      -0.361,
      0.147
    ],
    "p_mean_le_0": 0.777,
    "n": 33,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.017,
    "ci90": [
      -0.335,
      0.412
    ],
    "p_mean_le_0": 0.477,
    "n": 39,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": -0.004,
    "ci90": [
      -0.048,
      0.043
    ],
    "p_mean_le_0": 0.569,
    "n": 1778,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.088,
    "ci90": [
      0.031,
      0.147
    ],
    "p_mean_le_0": 0.007,
    "n": 1160,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.513,
    "ci90": [
      0.108,
      0.935
    ],
    "p_mean_le_0": 0.018,
    "n": 13,
    "survives_fdr10": true
  },
  "5m/INV/SHORT": {
    "expR": 0.615,
    "ci90": [
      -0.057,
      1.309
    ],
    "p_mean_le_0": 0.072,
    "n": 8,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.157,
    "ci90": [
      0.078,
      0.24
    ],
    "p_mean_le_0": 0.0,
    "n": 651,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.089,
    "ci90": [
      -0.013,
      0.193
    ],
    "p_mean_le_0": 0.074,
    "n": 407,
    "survives_fdr10": false
  }
}
```

## Clusters de regimen
```json
{
  "ready": true,
  "k": 4,
  "clusters": [
    {
      "id": 0,
      "n": 3175,
      "wrTP1": 44.0,
      "expR": 0.083,
      "pf": 1.17,
      "defining_features": {
        "structDir": 0.99,
        "biasScore": 0.79,
        "emaStack": 0.75,
        "nearEdge": 0.69
      }
    },
    {
      "id": 2,
      "n": 4168,
      "wrTP1": 44.9,
      "expR": 0.072,
      "pf": 1.15,
      "defining_features": {
        "biasScore": -1.16,
        "emaStack": -0.99,
        "nearEdge": -0.9,
        "structDir": -0.44
      }
    },
    {
      "id": 1,
      "n": 2038,
      "wrTP1": 49.7,
      "expR": 0.019,
      "pf": 1.04,
      "defining_features": {
        "hourNY": 1.36,
        "atrPctUsed": -0.87,
        "emaStack": 0.57,
        "biasScore": 0.51
      }
    },
    {
      "id": 3,
      "n": 2071,
      "wrTP1": 46.5,
      "expR": -0.021,
      "pf": 0.96,
      "defining_features": {
        "structDir": -1.01,
        "biasScore": 0.64,
        "nearEdge": 0.52,
        "hourNY": -0.51
      }
    }
  ]
}
```

## Consistencia entre instrumentos
```json
{
  "1m/INV/LONG": {
    "symbols": {
      "CL": {
        "n": 29,
        "wrTP1": 58.6,
        "expR": 0.464
      },
      "YM": {
        "n": 44,
        "wrTP1": 38.6,
        "expR": 0.124
      },
      "ES": {
        "n": 14,
        "wrTP1": 50.0,
        "expR": -0.245
      },
      "NQ": {
        "n": 9,
        "wrTP1": 55.6,
        "expR": 0.31
      },
      "GC": {
        "n": 16,
        "wrTP1": 31.2,
        "expR": -0.408
      }
    },
    "expR_spread": 0.872,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 53,
        "wrTP1": 45.3,
        "expR": 0.027
      },
      "NQ": {
        "n": 10,
        "wrTP1": 50.0,
        "expR": 0.071
      },
      "ES": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.57
      },
      "GC": {
        "n": 19,
        "wrTP1": 57.9,
        "expR": 0.122
      }
    },
    "expR_spread": 0.543,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 663,
        "wrTP1": 44.5,
        "expR": 0.063
      },
      "NQ": {
        "n": 819,
        "wrTP1": 45.7,
        "expR": -0.008
      },
      "ES": {
        "n": 819,
        "wrTP1": 46.9,
        "expR": 0.066
      },
      "CL": {
        "n": 1207,
        "wrTP1": 45.2,
        "expR": 0.031
      },
      "YM": {
        "n": 596,
        "wrTP1": 41.1,
        "expR": 0.02
      }
    },
    "expR_spread": 0.074,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 415,
        "wrTP1": 41.7,
        "expR": 0.088
      },
      "GC": {
        "n": 764,
        "wrTP1": 45.5,
        "expR": 0.069
      },
      "YM": {
        "n": 880,
        "wrTP1": 45.2,
        "expR": 0.112
      },
      "ES": {
        "n": 676,
        "wrTP1": 44.5,
        "expR": 0.009
      },
      "CL": {
        "n": 96,
        "wrTP1": 26.0,
        "expR": -0.517
      }
    },
    "expR_spread": 0.629,
    "verdict": "instrument-specific"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 5,
        "wrTP1": 40.0,
        "expR": -0.37
      },
      "CL": {
        "n": 6,
        "wrTP1": 50.0,
        "expR": -0.137
      },
      "YM": {
        "n": 9,
        "wrTP1": 33.3,
        "expR": -0.379
      },
      "ES": {
        "n": 6,
        "wrTP1": 83.3,
        "expR": 0.442
      },
      "NQ": {
        "n": 9,
        "wrTP1": 44.4,
        "expR": -0.13
      }
    },
    "expR_spread": 0.821,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 21,
        "wrTP1": 33.3,
        "expR": 0.072
      },
      "NQ": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": 0.324
      },
      "ES": {
        "n": 5,
        "wrTP1": 40.0,
        "expR": -0.072
      },
      "GC": {
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.46
      }
    },
    "expR_spread": 0.784,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 390,
        "wrTP1": 48.5,
        "expR": 0.038
      },
      "GC": {
        "n": 248,
        "wrTP1": 45.2,
        "expR": -0.012
      },
      "CL": {
        "n": 544,
        "wrTP1": 48.2,
        "expR": 0.044
      },
      "ES": {
        "n": 379,
        "wrTP1": 48.0,
        "expR": -0.037
      },
      "YM": {
        "n": 299,
        "wrTP1": 38.8,
        "expR": -0.098
      }
    },
    "expR_spread": 0.142,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 275,
        "wrTP1": 49.8,
        "expR": 0.05
      },
      "YM": {
        "n": 417,
        "wrTP1": 50.6,
        "expR": 0.142
      },
      "GC": {
        "n": 290,
        "wrTP1": 46.9,
        "expR": 0.102
      },
      "NQ": {
        "n": 201,
        "wrTP1": 42.3,
        "expR": 0.075
      },
      "CL": {
        "n": 37,
        "wrTP1": 43.2,
        "expR": -0.246
      }
    },
    "expR_spread": 0.388,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 6,
        "wrTP1": 66.7,
        "expR": 0.13
      },
      "YM": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.617
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 1.517
      }
    },
    "expR_spread": 1.387,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 40,
        "wrTP1": 60.0,
        "expR": 0.384
      },
      "ES": {
        "n": 149,
        "wrTP1": 51.7,
        "expR": 0.227
      },
      "YM": {
        "n": 113,
        "wrTP1": 49.6,
        "expR": 0.198
      },
      "CL": {
        "n": 165,
        "wrTP1": 58.2,
        "expR": 0.286
      },
      "NQ": {
        "n": 226,
        "wrTP1": 45.6,
        "expR": -0.048
      }
    },
    "expR_spread": 0.432,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 81,
        "wrTP1": 48.1,
        "expR": -0.017
      },
      "ES": {
        "n": 99,
        "wrTP1": 55.6,
        "expR": 0.118
      },
      "GC": {
        "n": 100,
        "wrTP1": 37.0,
        "expR": 0.054
      },
      "YM": {
        "n": 144,
        "wrTP1": 49.3,
        "expR": 0.176
      },
      "CL": {
        "n": 23,
        "wrTP1": 43.5,
        "expR": -0.036
      }
    },
    "expR_spread": 0.212,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 16,
  "near_news_30m": {
    "n": 353,
    "wrTP1": 48.4,
    "nSL": 128,
    "nTO": 54,
    "expR": 0.319,
    "pf": 1.76,
    "mfe_p25": 13.0,
    "mfe_p50": 29.0,
    "mfe_p75": 70.0,
    "winnerMAE_p75": 19.0,
    "winnerMAE_p90": 44.0,
    "loserMFEbeforeSL_p50": 3.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 3.0,
    "entryZoneTk_p50": -19.0,
    "revAfterSL_rate": 46.9
  },
  "away_from_news": {
    "n": 11099,
    "wrTP1": 45.7,
    "nSL": 5135,
    "nTO": 891,
    "expR": 0.041,
    "pf": 1.08,
    "mfe_p25": 7.0,
    "mfe_p50": 17.0,
    "mfe_p75": 39.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 33.3
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 4,
  "scored": 0,
  "mae_deltaER": null,
  "hit_direction_rate": null
}
```

## Experimentos
```json
[
  {
    "id": "example-0000",
    "status": "template",
    "hypothesis": "Ejemplo. Subir sc_min_rr de 1.0 a 1.3 sube E[R] en 1m/RETEST porque elimina las señales con TP1 mas cerca que el SL.",
    "param": "sc_min_rr",
    "from": 1.0,
    "to": 1.3,
    "changeDate": null,
    "segment": {
      "tf": "1",
      "kind": "RETEST"
    },
    "targetMetric": "expR",
    "minAfterN": 40
  },
  {
    "id": "sl-retest-wick-2026-09-03",
    "status": "proposed",
    "hypothesis": "En RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. HASTA 2026-09-04 esto solo certificaba en SHORT (\"no aplica a largos\"); con la muestra de 2026-09-05 TAMBIEN certifica en 1m LONG, asi que se retira la exclusion dura de BUY RETEST y se deja como 'certifica por tf/side, no generalizar sin mirar la tabla'. 2026-09-06: mismas cifras exactas que 2026-09-05 (n identico) porque no llego dato nuevo. 2026-09-07 (lunes, primer dia con trades GENUINAMENTE nuevos post-restauracion, sin repeticion del bug de heal): retest_1m_long paso de n=1087 a n=1135 (+48 pares nuevos, no restaurados) y el delta se mantiene practicamente igual (0.181->0.183) con el CI90 todavia sin cruzar cero -- esta es la primera confirmacion independiente real que pedia el next_steps anterior. retest_1m_short tambien crecio con dato nuevo (n=219->229) y sigue certificando. 2026-09-08 (martes, primer dia habil COMPLETO post-feriado, salto grande de muestra real): retest_1m_long n=1135->1432 (delta 0.183->0.18, estable, segunda confirmacion independiente); retest_1m_short n=229->514 (delta 0.283->0.417, se hizo MAS fuerte); retest_2m_short CERTIFICA POR PRIMERA VEZ (n=129->260, CI90 dejo de cruzar cero); retest_5m_long CERTIFICA POR PRIMERA VEZ pero al filo (n=224->274, CI90=[0.005,0.36], limite inferior casi cero, vigilar que no se revierta con mas muestra); retest_2m_long sigue sin certificar y el delta bajo a casi cero (0.028->0.01, n=596->742).",
    "param": "sl_basis_retest",
    "from": "3-capas (sc_slbuf x ATR1m + piso sc_floor_atr5 + techo sc_cap_atr5 / sc_cap_adr)",
    "to": "mecha de la vela del retest (lg_slOrig con slBasis=retestBar / retestBar2, crudo)",
    "changeDate": null,
    "segment": {
      "kind": "RETEST"
    },
    "targetMetric": "expR",
    "minAfterN": 40,
    "evidence": {
      "source": "sl_origin_vs_layer.by_basis / by_tf_kind_side (medicion PARALELA: misma entrada y mismos TP, solo se mueve el stop; rMultiple = base 3-capas, rOrig = base mecha del retest). No requiere cambio en TradingView para medir.",
      "asOf": "2026-09-16 (miercoles). Dato nuevo genuino, sin incidentes de repo salvo el 'forced update' habitual sobre origin/main (shallow clone, mismo tip, resuelto con checkout -B main origin/main). n de pares resueltos subio de 9303 a 9587.",
      "retest_1m_long": {
        "n": 2737,
        "deltaER_orig_minus_layer": 0.15,
        "ci90": [
          0.072,
          0.231
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 2676 a 2737, delta practicamente identico (0.141->0.15) -- novena confirmacion independiente, sigue siendo la lectura mas estable del experimento."
      },
      "retest_1m_short": {
        "n": 1971,
        "deltaER_orig_minus_layer": 0.127,
        "ci90": [
          0.036,
          0.226
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 1955 a 1971, delta se mantiene sin cruzar cero (0.126->0.127), limite inferior del CI90 estable en 0.036."
      },
      "retest_2m_long": {
        "n": 1327,
        "deltaER_orig_minus_layer": 0.035,
        "ci90": [
          -0.039,
          0.109
        ],
        "ci90_no_cruza_cero": false,
        "nota": "n subio de 1306 a 1327, delta subio un poco (0.032->0.035) pero el CI90 sigue cruzando cero -- decima lectura seguida sin certificar, se mantiene fuera de la propuesta."
      },
      "retest_2m_short": {
        "n": 895,
        "deltaER_orig_minus_layer": 0.117,
        "ci90": [
          0.011,
          0.221
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 890 a 895, delta identico (0.117), el limite inferior del CI90 se mantiene muy pegado a cero (0.014->0.011) -- sigue como candidato debil/al filo, no promoverlo a la lista solida todavia."
      },
      "retest_5m_long": {
        "n": 492,
        "deltaER_orig_minus_layer": 0.248,
        "ci90": [
          0.063,
          0.479
        ],
        "ci90_no_cruza_cero": true,
        "nota": "SEXTA LECTURA SEGUIDA CERTIFICANDO: n subio de 489 a 492, delta practicamente identico (0.246->0.248) -- sigue estable, sin retroceso, desde que se incluyo en la propuesta de la revision semanal."
      },
      "retest_5m_short": {
        "n": 309,
        "deltaER_orig_minus_layer": 0.554,
        "ci90": [
          0.148,
          1.067
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 305 a 309, delta practicamente sin cambio (0.561->0.554) -- sigue siendo la lectura mas solida del experimento."
      },
      "overall_by_basis_retestBar": {
        "n": 5888,
        "deltaER": 0.15,
        "ci90": [
          0.101,
          0.205
        ],
        "nota": "n subio de 5794 a 5888, delta estable (0.146->0.15) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba."
      }
    },
    "next_steps": [
      "2026-09-05: se recupero signals/2026-09-03.jsonl (ver nota de la corrida en state.json/narrative y en el historico de los playbooks) -- estaba truncado de 1280 a 24 lineas por un commit 'heal' que en realidad BORRO datos en vez de repararlos.",
      "2026-09-06: EL MISMO BUG SE REPITIO -- un segundo commit 'heal 24 orphan signal(s) 2026-09-03' (0cf0a30, autor jesusreyna2016, ts commit 2026-09-04 20:31 -0500) volvio a truncar signals/2026-09-03.jsonl de 1280 a 24 lineas, DESPUES de que el agente ya lo habia arreglado el dia anterior (commit 945c337). Se restauro de nuevo desde 945c337. Se anadio una guarda permanente en analyze.py (file_integrity_check: compara lineas de cada signals/outcomes/*.jsonl contra el maximo visto en corridas previas via state.json.file_line_counts, y alerta si algun archivo ENCOGIO). Jesus debe revisar/desactivar el job externo de 'heal' de huerfanos -- esta confundiendo señales legitimas con duplicados y borrando datos reales dos veces en 3 dias.",
      "2026-09-07 (lunes): PRIMER DIA SIN REPETICION DEL BUG -- file_line_counts confirma que ningun signals/outcomes/*.jsonl encogio; todos los archivos crecieron o se mantuvieron. La guarda de analyze.py sigue activa por si vuelve a pasar. Llego dato genuinamente nuevo (38 signals, 44 outcomes de 2026-09-07 + 69/62 de 2026-09-06 que no estaban contados en la corrida anterior) -- retest_1m_long y retest_1m_short subieron de n con delta estable, primera confirmacion independiente real (ver evidence arriba).",
      "2026-09-08 (martes): SEGUNDO DIA SIN REPETICION DEL BUG, salto grande de dato genuinamente nuevo (primer dia habil completo post-feriado). retest_1m_long/short mejoran o se mantienen (segunda confirmacion independiente); retest_2m_short y retest_5m_long CERTIFICAN POR PRIMERA VEZ (este ultimo al filo del cero, tratar como debil). Nota de metodo importante: en el mismo dia, segment_significance de 2m/RETEST (ambos lados) REVIRTIO su certificacion negativa de ayer al cruzar el CI90 de nuevo por cero con mas muestra -- prueba de que hay que seguir siendo conservador incluso con lecturas que 'parecian asentadas' con n mediano (cientos, no miles). Aplicar el mismo escepticismo a las certificaciones nuevas de hoy (2m short, 5m long) hasta que se sostengan 2-3 corridas mas.",
      "Revision semanal del domingo: confirmar sobre walk-forward + segment_significance (FDR 10%), no solo in-sample (walk_forward todavia no esta listo, solo 2 semanas de datos).",
      "Anadir linea a predictions.jsonl con predictedDeltaER antes de aplicar.",
      "Cuando se confirme con datos nuevos genuinos (no solo restaurados) durante varios dias mas y walk-forward este listo: cambio en Pine = para RETEST usar lg_slOrig (mecha de la vela del retest) como SL de trabajo en 1m (long y short) y 5m/2m SHORT; en 2m LONG y 5m LONG esperar mas confirmacion (5m LONG certifica pero al filo). Poner changeDate el dia que se aplique en los 12 graficos.",
      "Vigilar: retestBar2 (1m SHORT = mecha vela retest + vela previa) sigue siendo una fraccion chica de la muestra 1m short -- puede mover el numero cuando crezca.",
      "2026-09-10 (jueves): salto grande de dato nuevo (bus asento signals/outcomes/2026-09-08.jsonl completos, +1203 pares en todo el dataset). Patron de metodo importante que se repite: 1m SHORT paso de un delta que parecia muy fuerte (n=514, delta=0.417) a uno mas moderado pero todavia solido (n=898, delta=0.181) -- confirma otra vez que las lecturas con n en los cientos bajos pueden sobrestimar el efecto, tratar el numero mas reciente (mayor n) como el mas representativo, no promediar con lecturas viejas de n mas chico. 5m LONG PERDIO la certificacion 'al filo' de ayer (CI90 volvio a cruzar cero) -- se cumplio la advertencia de tratarlo como debil; sacarlo de cualquier propuesta hasta que vuelva a certificar sostenido. 2m SHORT tambien se debilito (certifica al filo, limite inferior del CI90 en 0.001). El unico segmento que se fortalecio con mas confianza fue 1m LONG (tercera confirmacion, delta estable) y 5m SHORT (sigue siendo el efecto mas grande, con margen). Vista global: SOLO 1m LONG, 1m SHORT y 5m SHORT siguen siendo candidatos solidos para la propuesta de la revision semanal del domingo 2026-09-13; 2m SHORT es candidato debil; 2m LONG y 5m LONG quedan fuera por ahora.",
      "2026-09-11 (viernes): incidente de repo (origin/main reescrito rio arriba, sin ancestro comun con la rama local; verificado como superset sin perdida de datos, resuelto con git reset --hard origin/main -- ver playbooks para el detalle). Dato nuevo genuino post-reset. Vista actualizada de candidatos: 1m LONG sigue solido (cuarta confirmacion, delta 0.163); 1m SHORT certifica pero a un paso de perder la certificacion (limite inferior del CI90 bajo a 0.003, vigilar de cerca); 5m SHORT sigue siendo el efecto mas grande y ahora la lectura mas solida (CI90 se estrecho); 5m LONG RECUPERA la certificacion que habia perdido ayer (tercer vaiven en 3 dias, seguir tratando como inestable). 2m SHORT PIERDE la certificacion 'al filo' de ayer (CI90 volvio a cruzar cero) -- se une a 2m LONG como no-candidato. Vista para la revision semanal del domingo 2026-09-13: candidatos solidos = 1m LONG y 5m SHORT; candidato debil/al filo = 1m SHORT; inestable (no incluir todavia) = 5m LONG; fuera = 2m LONG y 2m SHORT.",
      "2026-09-12 (sabado, ultima corrida antes de la revision semanal de manana domingo 2026-09-13): dato nuevo genuino sin incidentes de repo (+713 pares). Dos movimientos favorables: 1m SHORT deja de estar 'al filo' -- el limite inferior de su CI90 subio de 0.003 a 0.022, ya no es el candidato mas fragil de los tres solidos. Y sobre todo: **5m LONG certifica por SEGUNDA lectura seguida** (09-11 y hoy, delta 0.154->0.187, CI90 cada vez mas lejos de cero) -- es la primera vez que cumple la barra de '2 lecturas seguidas del mismo lado' que el propio experimento se puso el 09-08 tras tres vaivenes en 3 dias; pasa de 'inestable, no incluir' a candidato EXPERIMENTAL para la propuesta de manana, con la advertencia explicita de su historial volatil (no tratarlo al mismo nivel de confianza que 1m LONG/SHORT o 5m SHORT hasta una tercera lectura). 1m LONG (quinta confirmacion) y 5m SHORT (sigue siendo el efecto mas grande, CI90 mas angosto) se mantienen como los dos candidatos mas solidos sin cambios de fondo. 2m LONG (sexta lectura sin certificar) sigue fuera; 2m SHORT sigue sin certificar pero ahora es el no-candidato mas cerca de cero (limite inferior del CI90 = -0.001). PARA LA REVISION SEMANAL DE MANANA: candidatos solidos = 1m LONG, 1m SHORT (ya no al filo), 5m SHORT; candidato experimental (2 lecturas, vigilar una tercera) = 5m LONG; fuera = 2m LONG y 2m SHORT (este ultimo el mas cerca de flipear, seguir vigilando aunque no se proponga todavia).",
      "2026-09-13 (domingo, REVISION SEMANAL): dato nuevo genuino (+719 pares, sin incidentes de perdida real -- ver nota de proceso en `asOf`, hubo un `git pull` con 'forced update' al iniciar la corrida por una reescritura upstream de `origin/main`, verificada como superset y resuelta sin perder trabajo local). **5m LONG cumple hoy su TERCERA lectura seguida certificando** (delta 0.187->0.255, CI90 cada vez mas lejos de cero) -- se gradua de 'candidato experimental' a candidato SOLIDO, aunque se mantiene la nota de historial volatil (3 vaivenes entre 09-08 y 09-11) como diferencia frente a 1m LONG (sexta confirmacion sin un solo vaiven en su historia). DECISION DE LA REVISION SEMANAL: se propone formalmente a Jesus aplicar el cambio de SL en `scalp_command.pine` (usar `lg_slOrig`/mecha del retest en vez del stop de 3 capas) en los 4 segmentos que certifican de forma estable con n>=20 post-cambio exigido: **1m LONG, 1m SHORT, 5m LONG, 5m SHORT**. 2m LONG y 2m SHORT quedan explicitamente fuera de la propuesta (septima y octava lectura sin certificar de forma estable). Se anadieron 4 lineas a `predictions.jsonl` (una por segmento, `predictedDeltaER` = delta medido hoy) para poder puntuar el acierto una vez Jesus aplique el cambio y se junte muestra post-cambio (afterN>=40, marcar `experimental` hasta 40+ muestras y 2 semanas consecutivas en la misma direccion, per agent-instructions.md). Ver `reviews/2026-week-37.md` para el detalle completo de la revision. Status del experimento se mantiene en `proposed` (no aplicado todavia en TradingView, `changeDate` sigue null) -- pasara a medirse antes/despues (y potencialmente a `confirmed`) recien cuando Jesus ponga fecha de cambio en los graficos.",
      "2026-09-14 (lunes, primer dia habil tras la revision semanal): dato nuevo minimo (+96 pares en todo el dataset, reapertura de Globex del domingo). **Los 4 segmentos propuestos ayer (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen todos con `delta_beats_zero=true` sin ningun retroceso** -- primer dia de confirmacion post-propuesta, deltas practicamente identicos a ayer en los cuatro. 5m LONG suma su CUARTA lectura seguida certificando. 2m LONG y 2m SHORT siguen fuera (octava y novena lectura sin certificar). Sin cambios a la propuesta: sigue en estado `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView.",
      "2026-09-15 (martes, primer dia habil despues de la reapertura de Globex del domingo, dato genuino): los 4 segmentos propuestos en la revision semanal del 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG suma su octava confirmacion, 1m SHORT y 5m SHORT se mantienen estables, 5m LONG suma su QUINTA lectura seguida certificando (ya el doble del umbral de '2 lecturas seguidas' que se puso el propio experimento el 09-08). Movimiento notable: 2m SHORT se fortalecio (delta 0.093->0.117, CI90 ya no cruza cero) pero su limite inferior (0.014) sigue demasiado pegado a cero para promoverlo -- se mantiene como candidato debil/al filo, fuera de la propuesta hasta una segunda lectura consecutiva lejos de cero. 2m LONG sigue sin certificar (novena lectura). Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView. Nota de mantenimiento (no de dato): se corrigio hoy un bug de analyze.py que hacia que la alerta MUESTRA de 2026-W36/W37 (caida de n ya explicada por dedup, sin perdida de archivo real) se repitiera identica cada corrida para siempre en vez de solo mientras la cifra siguiera empeorando; el efecto se vera desde la proxima corrida.",
      "2026-09-16 (miercoles, dato nuevo genuino, +284 pares resueltos en todo el bus): los 4 segmentos propuestos el 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con `delta_beats_zero=true` y sin ningun retroceso -- 1m LONG suma su NOVENA confirmacion, 1m SHORT y 5m SHORT estables, **5m LONG suma su SEXTA lectura seguida certificando**. 2m SHORT se mantiene exactamente igual (delta 0.117, limite inferior del CI90 baja un poco de 0.014 a 0.011 -- sigue candidato debil/al filo, todavia sin una segunda lectura clara lejos de cero). 2m LONG sigue sin certificar, decima lectura seguida (delta 0.035, CI90 cruza cero). Sin cambios de estado: sigue `proposed`, `changeDate` null. La escalera de ejecucion sigue bloqueada en el peldano 0 (asesor) porque, aun con `gate.readyForLive=true` en 5m/RETEST/LONG (n>=100, E[R]>0, PF>=1.3, WR>=50), este mismo experimento -- la causa de SL dominante en RETEST -- sigue sin un `changeDate` ni muestra post-cambio; ese es exactamente el requisito que falta segun `execution-ladder.md` peldano 2. Nada accionable nuevo para Jesus hoy mas alla de: si va a aplicar el cambio de SL estructural en los 12 graficos, este es el dia con la evidencia mas solida acumulada hasta ahora (6 confirmaciones seguidas en el candidato mas fragil, 5m LONG).",
      "2026-09-17 (jueves, dato nuevo genuino, +1097 pares resueltos en todo el bus, el salto mas grande en varios dias): los 4 segmentos propuestos el 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con `delta_beats_zero=true` y sin ningun retroceso -- 1m LONG suma su DECIMA confirmacion (n=2737->3095, delta 0.15->0.142, CI90 [0.066,0.218]), 1m SHORT sube (n=1971->2085, delta 0.127->0.143, CI90 [0.046,0.247]), 5m LONG suma su SEPTIMA lectura seguida certificando (n=492->555, delta 0.248->0.218, CI90 [0.05,0.403]) y 5m SHORT sigue siendo el efecto mas grande, con margen (n=309->324, delta 0.554->0.514, CI90 [0.133,0.987]). 2m SHORT se mantiene candidato debil/al filo por otra corrida mas (n=895->939, delta 0.117->0.113, limite inferior del CI90 practicamente igual, 0.011 vs 0.012). 2m LONG sigue sin certificar, undecima lectura seguida (n=1327->1477, delta 0.035->0.05, CI90 [-0.018,0.12] -- el delta sube y el limite inferior se acerca a cero, vigilar si se acerca a certificar en las proximas corridas). Nota de gate: la semana ya cerrada 2026-W37 en el segmento 5m/RETEST/LONG (el segmento objetivo del gate de ejecucion) paso de PF=1.44 a PF=1.45 pero perdio 6 pares de muestra por el mismo mecanismo de dedup que ya afectaba los conteos agregados (n=241->235) -- primera vez que se ve este efecto a nivel de segmento individual, sin evidencia de perdida real de archivo (file_integrity_check limpio). Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView. Hallazgo nuevo en paralelo (no de este experimento): por primera vez el veredicto SA=GO certifica con significancia junto a SA=WAIT en el cruce agregado con Session Analyst (ver report.alerts); y en el desglose por kind/side, la rama AVOID de RETEST/LONG cruza a E[R] negativo por primera vez mientras la rama WAIT de RETEST/SHORT cruza a positivo -- ver playbooks para el detalle por lado."
    ],
    "beforeN": 11155,
    "afterN": 0,
    "before": {
      "n": 11155,
      "wrTP1": 45.7,
      "nSL": 5138,
      "nTO": 915,
      "expR": 0.047,
      "pf": 1.1,
      "mfe_p25": 7.0,
      "mfe_p50": 17.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.8
    },
    "after": {
      "n": 0
    }
  }
]
```

## Session Analyst
```json
{
  "available": true,
  "latest_plan": {
    "date": "2026-09-18",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-17T19:24:36-05:00",
    "schema": "sa-plan-2",
    "cleanest": "NQ",
    "focus": {
      "sym": "NQ",
      "verdict": "WAIT",
      "window": "19:00-21:15 CT",
      "setup": {
        "es": "fade del máximo de ayer 29751.25-29762.50: VAH + máximo del día + zona premium + barrida de liquidez, confluencia 7",
        "en": "fading yesterday's 29751.25-29762.50 high: VAH + day high + premium zone + liquidity sweep, confluence 7"
      },
      "trigger": {
        "es": "barrido de 29762.50 y cierre de 5m de vuelta bajo el VAH 29751.22; si no hay barrido y cierre de vuelta, no hay trade",
        "en": "a sweep of 29762.50 and a 5m close back below the 29751.22 VAH; with no sweep and close back inside there is no trade"
      },
      "invalid": {
        "es": "cierre de 5m sostenido sobre 29775",
        "en": "a sustained 5m close above 29775"
      },
      "note": {
        "es": "es un corto contra un marco de fondo alcista, así que solo existe como reacción a un nivel que ya rechazó: nada de entrar al toque ni de decidir el giro antes de que el precio lo enseñe. Manos fuera entre 21:15 y 21:40 por el Banco de Japón, y el veredicto es esperar, no hay permiso de entrada.",
        "en": "it's a short against a bullish underlying frame, so it only exists as a reaction to a level that has already rejected: no entry on the touch, no deciding the turn before price shows it. Hands off between 21:15 and 21:40 for the Bank of Japan, and the verdict is wait, there is no entry permission."
      }
    },
    "summary": {
      "es": [
        "!! 2 fuentes siguen muertas (NQ 57h, ES 9h); tesis de YM sigue rota; CL con el feed desplazado ~4.53 $ por un rolo de contrato, sus niveles no son fiables esta sesión.",
        "NQ: el cierre real llegó a 29793.25 antes de asentar en 29720.50, por encima de los 29762.50 provisionales. Ya en Asia el rango es de solo 54.5 pts (29674-29728.50): el precio recorrió las dos puntas del hueco alcista de 15m 29691-29708 y ahora cotiza justo en su piso, 29691. Sigue en espera: sin GO mientras la voz fusionada del sesgo siga muerta.",
        "ES: sesión clavada en apenas 7.25 pts (7697-7704.25) sobre el cluster POC/EMA50/VAH. Sigue evitar: el único borde que compraría está 14 pts abajo, ya casi en el límite del presupuesto de la noche.",
        "GC: subió de la mano del hueco alcista de 4h y ya reclamó el techo 4391.80 (ahora en 4393.30); a solo 3.2 pts del retest corto 4396.50-4400.10. Sigue esperar: marcos opuestos y sin tamaño posible en ninguna de las dos zonas por el límite diario.",
        "YM: rango de reapertura de solo 60 pts (52147-52207). Su única zona mapeada (fade 52279-52334) se estiró al 57% del presupuesto de la sesión sin alternativa táctica en tabla; sigue bloqueada por marcos opuestos.",
        "CL: aviso de datos, no de mercado. El feed bajó unos 4.53 $ de
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 4480,
  "by_verdict": {
    "AVOID": {
      "n": 1212,
      "wrTP1": 44.8,
      "nSL": 597,
      "nTO": 72,
      "expR": 0.013,
      "pf": 1.02,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 28.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 33.7
    },
    "GO": {
      "n": 653,
      "wrTP1": 51.6,
      "nSL": 261,
      "nTO": 55,
      "expR": 0.125,
      "pf": 1.29,
      "mfe_p25": 10.0,
      "mfe_p50": 26.0,
      "mfe_p75": 53.0,
      "winnerMAE_p75": 18.0,
      "winnerMAE_p90": 32.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 39.1
    },
    "WAIT": {
      "n": 2615,
      "wrTP1": 47.8,
      "nSL": 1118,
      "nTO": 248,
      "expR": 0.078,
      "pf": 1.17,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 39.5
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.013,
      "ci90": [
        -0.049,
        0.073
      ],
      "p_mean_le_0": 0.356,
      "n": 1166
    },
    "GO": {
      "expR": 0.125,
      "ci90": [
        0.046,
        0.202
      ],
      "p_mean_le_0": 0.004,
      "n": 611
    },
    "WAIT": {
      "expR": 0.078,
      "ci90": [
        0.041,
        0.119
      ],
      "p_mean_le_0": 0.001,
      "n": 2447
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1212,
      "wrTP1": 44.8,
      "nSL": 597,
      "nTO": 72,
      "expR": 0.013,
      "pf": 1.02,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 28.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 19.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 33.7
    },
    "GO_or_WAIT": {
      "n": 3268,
      "wrTP1": 48.5,
      "nSL": 1379,
      "nTO": 303,
      "expR": 0.087,
      "pf": 1.19,
      "mfe_p25": 8.0,
      "mfe_p50": 20.0,
      "mfe_p75": 46.0,
      "winnerMAE_p75": 14.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 39.4
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.013,
      "ci90": [
        -0.049,
        0.073
      ],
      "p_mean_le_0": 0.356,
      "n": 1166
    },
    "GO_or_WAIT": {
      "expR": 0.087,
      "ci90": [
        0.054,
        0.122
      ],
      "p_mean_le_0": 0.0,
      "n": 3058
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 12,
        "wrTP1": 50.0,
        "nSL": 5,
        "nTO": 1,
        "expR": -0.072,
        "pf": 0.83,
        "mfe_p25": 5.0,
        "mfe_p50": 6.0,
        "mfe_p75": 29.25,
        "winnerMAE_p75": 0.0,
        "winnerMAE_p90": 2.0,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 40.0
      },
      "GO": {
        "n": 9,
        "wrTP1": 55.6,
        "nSL": 3,
        "nTO": 1,
        "expR": -0.016,
        "pf": 0.96,
        "mfe_p25": 19.75,
        "mfe_p50": 26.0,
        "mfe_p75": 33.25,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 28.400000000000002,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -60.0,
        "revAfterSL_rate": 33.3
      },
      "WAIT": {
        "n": 36,
        "wrTP1": 44.4,
        "nSL": 17,
        "nTO": 3,
        "expR": -0.106,
        "pf": 0.79,
        "mfe_p25": 7.5,
        "mfe_p50": 19.5,
        "mfe_p75": 46.75,
        "winnerMAE_p75": 19.5,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 23.5
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 23,
        "wrTP1": 34.8,
        "nSL": 13,
        "nTO": 2,
        "expR": -0.333,
        "pf": 0.44,
        "mfe_p25": 6.5,
        "mfe_p50": 13.5,
        "mfe_p75": 21.75,
        "winnerMAE_p75": 4.5,
        "winnerMAE_p90": 6.8999999999999995,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 15.4
      },
      "WAIT": {
        "n": 23,
        "wrTP1": 52.2,
        "nSL": 10,
        "nTO": 1,
        "expR": -0.158,
        "pf": 0.64,
        "mfe_p25": 8.5,
        "mfe_p50": 20.0,
        "mfe_p75": 38.5,
        "winnerMAE_p75": 33.25,
        "winnerMAE_p90": 73.9,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 5.5,
        "entryZoneTk_p50": -22.0,
        "revAfterSL_rate": 40.0
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 644,
        "wrTP1": 46.9,
        "nSL": 314,
        "nTO": 28,
        "expR": 0.015,
        "pf": 1.03,
        "mfe_p25": 6.0,
        "mfe_p50": 12.0,
        "mfe_p75": 25.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 29.9
      },
      "GO": {
        "n": 446,
        "wrTP1": 50.7,
        "nSL": 189,
        "nTO": 31,
        "expR": 0.078,
        "pf": 1.18,
        "mfe_p25": 9.0,
        "mfe_p50": 25.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 31.5,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.5,
        "revAfterSL_rate": 39.7
      },
      "WAIT": {
        "n": 1524,
        "wrTP1": 49.4,
        "nSL": 635,
        "nTO": 136,
        "expR": 0.124,
        "pf": 1.28,
        "mfe_p25": 8.0,
        "mfe_p50": 18.0,
        "mfe_p75": 42.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 42.7
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 533,
        "wrTP1": 42.6,
        "nSL": 265,
        "nTO": 41,
        "expR": 0.026,
        "pf": 1.05,
        "mfe_p25": 7.0,
        "mfe_p50": 15.5,
        "mfe_p75": 30.0,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 20.80000000000001,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 38.9
      },
      "GO": {
        "n": 196,
        "wrTP1": 53.6,
        "nSL": 68,
        "nTO": 23,
        "expR": 0.231,
        "pf": 1.6,
        "mfe_p25": 13.0,
        "mfe_p50": 27.0,
        "mfe_p75": 57.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 30.800000000000026,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 38.2
      },
      "WAIT": {
        "n": 1032,
        "wrTP1": 45.3,
        "nSL": 456,
        "nTO": 108,
        "expR": 0.021,
        "pf": 1.04,
        "mfe_p25": 9.0,
        "mfe_p50": 21.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 15.25,
        "winnerMAE_p90": 28.30000000000001,
        "loserMFEbeforeSL_p50": 3.5,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 35.7
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```
