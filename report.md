# Scalp CC · report 2026-09-30T01:17Z
- signals=19849 outcomes=18893 pares_resueltos=19676 pendientes=173 huerfanos=40

## ⚠ ALERTAS (llevar al frente del resumen)
- MUESTRA: by_kindside_aligned/RETEST/LONG|aligned=0 bajo de n=10 a n=7 desde la corrida previa (agregado, no archivo crudo -- revisar deduplicacion/re-pareo).
- MUESTRA: semana ya cerrada 2026-W36 bajo de n=3183 a n=2867 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W37 bajo de n=5389 a n=4992 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W38 bajo de n=4911 a n=4622 desde la corrida previa -- vigilar, puede ser deduplicacion.
- MUESTRA: semana ya cerrada 2026-W39 bajo de n=5355 a n=5289 desde la corrida previa -- vigilar, puede ser deduplicacion.
- EXPERIMENTO CONFIRMADO: sl_basis_retest 3-capas (sc_slbuf x ATR1m + piso sc_floor_atr5 + techo sc_cap_atr5 / sc_cap_adr)->mecha de la vela del retest (lg_slOrig con slBasis=retestBar / retestBar2, crudo) (sl-retest-wick-2026-09-03).
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.235 vs 0.063, delta 0.172 CI90 [0.136, 0.209], n 12189). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.204 vs 0.061, delta 0.143 CI90 [0.08, 0.21], n 4030). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.141 CI90 [0.077, 0.21], n 918). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.068 CI90 [0.042, 0.098], n 5341). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.062, "ci90": [0.047, 0.077], "p_mean_le_0": 0.0, "n": 18853}
- gate ejecucion: {"readyForLive": false, "segment": null, "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 171 | 45.0 | 0.193 | 1.45 | 69 | 15.5 | 11.0 | 17.4 |
| 1m/INV/SHORT | 159 | 46.5 | -0.005 | 0.99 | 69 | 20.0 | 17.0 | 17.4 |
| 1m/RETEST/LONG | 6994 | 45.5 | 0.06 | 1.12 | 3279 | 15.0 | 10.0 | 28.1 |
| 1m/RETEST/SHORT | 5126 | 45.4 | 0.054 | 1.11 | 2331 | 18.0 | 11.0 | 31.5 |
| 2m/INV/LONG | 67 | 49.3 | 0.015 | 1.03 | 26 | 14.0 | 10.0 | 19.2 |
| 2m/INV/SHORT | 67 | 43.3 | 0.087 | 1.19 | 29 | 21.0 | 12.0 | 31.0 |
| 2m/RETEST/LONG | 3058 | 46.5 | 0.032 | 1.06 | 1435 | 18.0 | 13.0 | 37.2 |
| 2m/RETEST/SHORT | 2132 | 48.5 | 0.086 | 1.18 | 959 | 22.0 | 13.0 | 40.3 |
| 5m/INV/LONG | 20 | 70.0 | 0.421 | 3.52 | 3 | 28.5 | 29.0 | 66.7 |
| 5m/INV/SHORT | 12 | 66.7 | 0.392 | 2.44 | 3 | 34.0 | 58.25 | 66.7 |
| 5m/RETEST/LONG | 1102 | 49.5 | 0.121 | 1.27 | 467 | 30.0 | 20.0 | 48.6 |
| 5m/RETEST/SHORT | 768 | 48.2 | 0.083 | 1.18 | 334 | 31.0 | 19.0 | 36.2 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 1363 | 24.7 | 0.06 | 1.09 | 849 | 27.0 | 13.0 | 20.3 |
| B | 8583 | 47.0 | 0.068 | 1.14 | 3892 | 18.0 | 12.0 | 32.8 |
| C | 9730 | 48.8 | 0.057 | 1.12 | 4263 | 18.0 | 12.0 | 35.6 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 7115 | 49.6 | 0.11 | 1.24 | 3140 | 14.0 | 10.0 | 36.5 |
| London | 2957 | 45.8 | 0.035 | 1.07 | 1452 | 18.0 | 12.0 | 35.1 |
| NY | 3425 | 44.4 | 0.054 | 1.11 | 1582 | 25.0 | 15.0 | 36.1 |
| Sin KZ | 6179 | 44.0 | 0.023 | 1.05 | 2830 | 21.0 | 14.0 | 26.2 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 5156 | 45.3 | 0.063 | 1.13 | 2365 | 21.0 | 14.0 | 31.3 |
| edge=0 | 8378 | 49.0 | 0.062 | 1.13 | 3722 | 16.0 | 11.0 | 37.7 |
| edge=1 | 6142 | 43.6 | 0.061 | 1.12 | 2917 | 18.0 | 13.0 | 28.1 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 7 | 57.1 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| aligned=1 | 19669 | 46.3 | 0.062 | 1.13 | 9003 | 18.0 | 12.0 | 33.0 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 101 | 55.4 | 0.181 | 1.48 | 35 | 13.0 | 10.25 | 25.7 |
| INV/LONG|edge=1 | 153 | 43.1 | 0.144 | 1.34 | 61 | 17.0 | 14.0 | 14.8 |
| INV/SHORT|edge=-1 | 144 | 40.3 | -0.031 | 0.94 | 68 | 24.0 | 16.25 | 20.6 |
| INV/SHORT|edge=0 | 85 | 55.3 | 0.091 | 1.23 | 30 | 15.5 | 17.0 | 30.0 |
| INV/SHORT|edge=1 | 9 | 66.7 | 0.69 | 3.07 | 3 | 28.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 433 | 51.3 | 0.143 | 1.32 | 185 | 17.0 | 11.0 | 42.2 |
| RETEST/LONG|edge=0 | 4892 | 49.2 | 0.05 | 1.11 | 2207 | 15.0 | 11.0 | 37.6 |
| RETEST/LONG|edge=1 | 5829 | 43.3 | 0.058 | 1.12 | 2789 | 19.0 | 13.0 | 27.8 |
| RETEST/SHORT|edge=-1 | 4575 | 44.9 | 0.058 | 1.12 | 2110 | 21.0 | 14.0 | 30.7 |
| RETEST/SHORT|edge=0 | 3300 | 48.3 | 0.076 | 1.16 | 1450 | 18.0 | 11.0 | 38.5 |
| RETEST/SHORT|edge=1 | 151 | 54.3 | 0.051 | 1.12 | 64 | 14.0 | 9.0 | 56.2 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 84 | 44.0 | 0.244 | 1.56 | 35 | 17.0 | 14.0 | 8.6 |
| INV/LONG|tier=C | 174 | 50.0 | 0.123 | 1.31 | 63 | 14.0 | 11.5 | 25.4 |
| INV/SHORT|tier=B | 76 | 39.5 | -0.101 | 0.81 | 39 | 20.5 | 11.75 | 7.7 |
| INV/SHORT|tier=C | 162 | 50.0 | 0.107 | 1.26 | 62 | 20.0 | 23.0 | 32.3 |
| RETEST/LONG|tier=A+ | 831 | 23.3 | 0.014 | 1.02 | 542 | 24.0 | 13.0 | 19.2 |
| RETEST/LONG|tier=B | 4746 | 46.4 | 0.079 | 1.17 | 2169 | 17.0 | 12.0 | 32.0 |
| RETEST/LONG|tier=C | 5577 | 49.3 | 0.047 | 1.1 | 2470 | 17.0 | 12.0 | 35.8 |
| RETEST/SHORT|tier=A+ | 532 | 26.9 | 0.134 | 1.21 | 307 | 31.0 | 14.5 | 22.1 |
| RETEST/SHORT|tier=B | 3677 | 47.9 | 0.053 | 1.11 | 1649 | 19.0 | 13.0 | 35.0 |
| RETEST/SHORT|tier=C | 3817 | 47.9 | 0.068 | 1.15 | 1668 | 19.0 | 12.0 | 35.8 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 258 | 48.1 | 0.163 | 1.4 | 98 | 16.0 | 13.0 | 19.4 |
| INV/SHORT|aligned=1 | 238 | 46.6 | 0.04 | 1.09 | 101 | 20.0 | 17.5 | 22.8 |
| RETEST/LONG|aligned=0 | 7 | 57.1 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| RETEST/LONG|aligned=1 | 11147 | 46.2 | 0.058 | 1.12 | 5180 | 17.0 | 12.0 | 32.5 |
| RETEST/SHORT|aligned=1 | 8026 | 46.5 | 0.065 | 1.14 | 3624 | 20.0 | 13.0 | 34.3 |

## Autopsia de SL
n_losses=9004  causas: RR-bajo×3320, contra-estructura×3013, stop-en-el-minimo×2967, killzone-Asia-largo×1846, sin-nivel-detras×1661, estirado×1517, chop×1383, SL-muy-pegado×1153, sin-causa-clara×1017, contra-sesgo×1
- INV/LONG (n=98): killzone-Asia-largo×40, RR-bajo×39, contra-estructura×27, estirado×25, stop-en-el-minimo×19, chop×14, sin-nivel-detras×13, SL-muy-pegado×10, sin-causa-clara×6
- INV/SHORT (n=101): RR-bajo×46, contra-estructura×29, estirado×24, stop-en-el-minimo×23, sin-causa-clara×19, SL-muy-pegado×14, chop×10, sin-nivel-detras×6
- RETEST/LONG (n=5181): RR-bajo×1906, contra-estructura×1819, killzone-Asia-largo×1806, stop-en-el-minimo×1683, sin-nivel-detras×1020, estirado×864, chop×852, SL-muy-pegado×630, sin-causa-clara×469, contra-sesgo×1
- RETEST/SHORT (n=3624): RR-bajo×1329, stop-en-el-minimo×1242, contra-estructura×1138, sin-nivel-detras×622, estirado×604, sin-causa-clara×523, chop×507, SL-muy-pegado×499

## Autopsia de SL · semana 2026-W40 (para revision semanal)
n_losses=868  causas: RR-bajo×314, stop-en-el-minimo×300, contra-estructura×234, chop×160, estirado×137, sin-causa-clara×124, killzone-Asia-largo×121, SL-muy-pegado×118, sin-nivel-detras×71
ejemplos por causa: {"RR-bajo": ["GC-2-22069-L", "ES-1-21101-S", "YM-2-20824-S", "NQ-2-21022-L", "ES-1-21357-L"], "stop-en-el-minimo": ["ES-1-21101-S", "YM-2-20824-S", "YM-2-20877-S", "NQ-2-21030-L", "YM-5-20703-S"], "contra-estructura": ["YM-2-20877-S", "ES-1-21519-S", "CL-5-20746-L", "YM-2-21129-S", "ES-1-21934-S"]}

## Contrafactual de gestion
```json
{
  "n": 7,
  "baseline_nextLevel_expR": 0.236,
  "fixed_1R": [
    0.214,
    7
  ],
  "fixed_1_5R": [
    0.236,
    7
  ],
  "fixed_2R": [
    0.236,
    7
  ],
  "fixed_3R": [
    0.236,
    7
  ],
  "altSL_0_5x_struct": [
    0.205,
    7
  ],
  "altSL_1_5x_struct": [
    0.283,
    7
  ],
  "note": "fixed_XR: R esperado si el objetivo fuera XR fijo con SL=struct. altSL: SL a mult del SL struct."
}
```

## Modelo GESTIONADO (escalera + parciales) vs INGENUO
```json
{
  "overall": {
    "n": 18840,
    "naive_expR": 0.062,
    "managed_expR": 0.138,
    "delta": 0.076,
    "avgEntryBetterTk_p50": 2.7,
    "fill_t3plus_pct": 45.8,
    "fill_full_pct": 32.5,
    "m1_rate": 37.7,
    "m2_rate": 23.1,
    "m3_rate": 12.1,
    "beAfterM1_rate": 18.4
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 162,
      "naive_expR": 0.193,
      "managed_expR": 0.299,
      "delta": 0.106,
      "avgEntryBetterTk_p50": 2.1500000000000004,
      "fill_t3plus_pct": 46.9,
      "fill_full_pct": 35.2,
      "m1_rate": 43.8,
      "m2_rate": 26.5,
      "m3_rate": 13.0,
      "beAfterM1_rate": 24.1
    },
    "1m/INV/SHORT": {
      "n": 153,
      "naive_expR": -0.005,
      "managed_expR": 0.176,
      "delta": 0.182,
      "avgEntryBetterTk_p50": 3.5,
      "fill_t3plus_pct": 54.2,
      "fill_full_pct": 40.5,
      "m1_rate": 35.3,
      "m2_rate": 20.3,
      "m3_rate": 12.4,
      "beAfterM1_rate": 17.6
    },
    "1m/RETEST/LONG": {
      "n": 6772,
      "naive_expR": 0.059,
      "managed_expR": 0.145,
      "delta": 0.086,
      "avgEntryBetterTk_p50": 2.3,
      "fill_t3plus_pct": 47.6,
      "fill_full_pct": 33.8,
      "m1_rate": 38.2,
      "m2_rate": 23.2,
      "m3_rate": 11.8,
      "beAfterM1_rate": 17.7
    },
    "1m/RETEST/SHORT": {
      "n": 4856,
      "naive_expR": 0.055,
      "managed_expR": 0.182,
      "delta": 0.128,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 47.6,
      "fill_full_pct": 33.1,
      "m1_rate": 39.7,
      "m2_rate": 24.7,
      "m3_rate": 13.6,
      "beAfterM1_rate": 18.9
    },
    "2m/INV/LONG": {
      "n": 63,
      "naive_expR": 0.015,
      "managed_expR": -0.0,
      "delta": -0.015,
      "avgEntryBetterTk_p50": 2.2,
      "fill_t3plus_pct": 50.8,
      "fill_full_pct": 36.5,
      "m1_rate": 22.2,
      "m2_rate": 15.9,
      "m3_rate": 6.3,
      "beAfterM1_rate": 9.5
    },
    "2m/INV/SHORT": {
      "n": 65,
      "naive_expR": 0.087,
      "managed_expR": 0.131,
      "delta": 0.044,
      "avgEntryBetterTk_p50": 2.4,
      "fill_t3plus_pct": 47.7,
      "fill_full_pct": 35.4,
      "m1_rate": 30.8,
      "m2_rate": 23.1,
      "m3_rate": 15.4,
      "beAfterM1_rate": 10.8
    },
    "2m/RETEST/LONG": {
      "n": 2937,
      "naive_expR": 0.031,
      "managed_expR": 0.067,
      "delta": 0.036,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 44.5,
      "fill_full_pct": 31.5,
      "m1_rate": 35.1,
      "m2_rate": 20.4,
      "m3_rate": 10.4,
      "beAfterM1_rate": 18.3
    },
    "2m/RETEST/SHORT": {
      "n": 2058,
      "naive_expR": 0.086,
      "managed_expR": 0.145,
      "delta": 0.059,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 44.8,
      "fill_full_pct": 32.2,
      "m1_rate": 37.2,
      "m2_rate": 23.5,
      "m3_rate": 12.1,
      "beAfterM1_rate": 19.3
    },
    "5m/INV/LONG": {
      "n": 18,
      "naive_expR": 0.421,
      "managed_expR": 0.369,
      "delta": -0.052,
      "avgEntryBetterTk_p50": 0.65,
      "fill_t3plus_pct": 33.3,
      "fill_full_pct": 22.2,
      "m1_rate": 16.7,
      "m2_rate": 11.1,
      "m3_rate": 5.6,
      "beAfterM1_rate": 11.1
    },
    "5m/INV/SHORT": {
      "n": 11,
      "naive_expR": 0.392,
      "managed_expR": 0.458,
      "delta": 0.066,
      "avgEntryBetterTk_p50": 8.4,
      "fill_t3plus_pct": 63.6,
      "fill_full_pct": 45.5,
      "m1_rate": 27.3,
      "m2_rate": 18.2,
      "m3_rate": 18.2,
      "beAfterM1_rate": 9.1
    },
    "5m/RETEST/LONG": {
      "n": 1029,
      "naive_expR": 0.121,
      "managed_expR": 0.074,
      "delta": -0.047,
      "avgEntryBetterTk_p50": 1.0,
      "fill_t3plus_pct": 33.7,
      "fill_full_pct": 25.5,
      "m1_rate": 35.2,
      "m2_rate": 22.4,
      "m3_rate": 12.5,
      "beAfterM1_rate": 19.5
    },
    "5m/RETEST/SHORT": {
      "n": 716,
      "naive_expR": 0.082,
      "managed_expR": 0.091,
      "delta": 0.008,
      "avgEntryBetterTk_p50": 4.9,
      "fill_t3plus_pct": 41.5,
      "fill_full_pct": 27.7,
      "m1_rate": 35.9,
      "m2_rate": 22.3,
      "m3_rate": 10.8,
      "beAfterM1_rate": 18.0
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 16679,
    "layer_expR": 0.064,
    "orig_expR": 0.226,
    "delta_orig_minus_layer": 0.162,
    "delta_ci90": [
      0.131,
      0.193
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.2,
    "orig_wrTP1": 33.6,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 9.0,
    "orig_wider_pct": 3.9,
    "orig_saved_from_SL": 24,
    "orig_caused_SL": 2464
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 2,
  "invalid_by_seg": {
    "1m/RETEST/LONG": 2
  },
  "by_basis": {
    "candle1": {
      "n": 460,
      "layer_expR": 0.103,
      "orig_expR": 0.161,
      "delta_orig_minus_layer": 0.058,
      "delta_ci90": [
        -0.134,
        0.282
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.3,
      "orig_wrTP1": 26.7,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 5.0,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 105
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
      "n": 12189,
      "layer_expR": 0.063,
      "orig_expR": 0.235,
      "delta_orig_minus_layer": 0.172,
      "delta_ci90": [
        0.136,
        0.209
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.3,
      "orig_wrTP1": 33.9,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 4.4,
      "orig_saved_from_SL": 23,
      "orig_caused_SL": 1776
    },
    "retestBar2": {
      "n": 4030,
      "layer_expR": 0.061,
      "orig_expR": 0.204,
      "delta_orig_minus_layer": 0.143,
      "delta_ci90": [
        0.08,
        0.21
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.7,
      "orig_wrTP1": 33.2,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.4,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 583
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 162,
      "layer_expR": 0.193,
      "orig_expR": 0.078,
      "delta_orig_minus_layer": -0.115,
      "delta_ci90": [
        -0.423,
        0.181
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.5,
      "orig_wrTP1": 22.8,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 4.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 40
    },
    "1m/INV/SHORT": {
      "n": 143,
      "layer_expR": -0.01,
      "orig_expR": -0.004,
      "delta_orig_minus_layer": 0.005,
      "delta_ci90": [
        -0.289,
        0.34
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 47.6,
      "orig_wrTP1": 24.5,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.1,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 33
    },
    "1m/RETEST/LONG": {
      "n": 5888,
      "layer_expR": 0.058,
      "orig_expR": 0.205,
      "delta_orig_minus_layer": 0.146,
      "delta_ci90": [
        0.093,
        0.199
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.4,
      "orig_wrTP1": 29.6,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 1.2,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 989
    },
    "1m/RETEST/SHORT": {
      "n": 4149,
      "layer_expR": 0.057,
      "orig_expR": 0.203,
      "delta_orig_minus_layer": 0.146,
      "delta_ci90": [
        0.085,
        0.208
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 47.6,
      "orig_wrTP1": 33.1,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 601
    },
    "2m/INV/LONG": {
      "n": 63,
      "layer_expR": 0.015,
      "orig_expR": 0.947,
      "delta_orig_minus_layer": 0.933,
      "delta_ci90": [
        0.064,
        1.997
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 52.4,
      "orig_wrTP1": 31.7,
      "slTk_p50": 25.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 6.3,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 13
    },
    "2m/INV/SHORT": {
      "n": 64,
      "layer_expR": 0.081,
      "orig_expR": 0.217,
      "delta_orig_minus_layer": 0.135,
      "delta_ci90": [
        -0.257,
        0.575
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 43.8,
      "orig_wrTP1": 31.2,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 4.7,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 9
    },
    "2m/RETEST/LONG": {
      "n": 2696,
      "layer_expR": 0.037,
      "orig_expR": 0.207,
      "delta_orig_minus_layer": 0.169,
      "delta_ci90": [
        0.105,
        0.237
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.9,
      "orig_wrTP1": 35.9,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.5,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 354
    },
    "2m/RETEST/SHORT": {
      "n": 1827,
      "layer_expR": 0.097,
      "orig_expR": 0.238,
      "delta_orig_minus_layer": 0.141,
      "delta_ci90": [
        0.06,
        0.222
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.5,
      "orig_wrTP1": 36.6,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 3.8,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 256
    },
    "5m/INV/LONG": {
      "n": 18,
      "layer_expR": 0.421,
      "orig_expR": -0.401,
      "delta_orig_minus_layer": -0.821,
      "delta_ci90": [
        -1.32,
        -0.376
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 77.8,
      "orig_wrTP1": 38.9,
      "slTk_p50": 34.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 16.7,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 7
    },
    "5m/INV/SHORT": {
      "n": 10,
      "layer_expR": 0.379,
      "orig_expR": -0.435,
      "delta_orig_minus_layer": -0.814,
      "delta_ci90": [
        -1.197,
        -0.429
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 70.0,
      "orig_wrTP1": 40.0,
      "slTk_p50": 39.0,
      "slOrigTk_p50": 38.0,
      "orig_wider_pct": 30.0,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 3
    },
    "5m/RETEST/LONG": {
      "n": 992,
      "layer_expR": 0.112,
      "orig_expR": 0.377,
      "delta_orig_minus_layer": 0.265,
      "delta_ci90": [
        0.133,
        0.416
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.0,
      "orig_wrTP1": 43.9,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 18.0,
      "orig_wider_pct": 15.8,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 98
    },
    "5m/RETEST/SHORT": {
      "n": 667,
      "layer_expR": 0.077,
      "orig_expR": 0.409,
      "delta_orig_minus_layer": 0.332,
      "delta_ci90": [
        0.114,
        0.581
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.3,
      "orig_wrTP1": 43.3,
      "slTk_p50": 30.0,
      "slOrigTk_p50": 23.0,
      "orig_wider_pct": 21.0,
      "orig_saved_from_SL": 8,
      "orig_caused_SL": 61
    }
  }
}
```

## Contrafactual de entrada por RR minimo (candidato sc_min_rr, ataca causa RR-bajo)
```json
{
  "1/RETEST/LONG": {
    "baseline": {
      "n": 6726,
      "wrTP1": 47.3,
      "nSL": 3110,
      "nTO": 435,
      "expR": 0.049,
      "pf": 1.1,
      "mfe_p25": 6.0,
      "mfe_p50": 15.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 29.6,
      "ci90": {
        "expR": 0.049,
        "ci90": [
          0.026,
          0.073
        ],
        "p_mean_le_0": 0.001,
        "n": 6513
      }
    },
    "cuts": {
      "1.0": {
        "n": 3300,
        "wrTP1": 30.6,
        "nSL": 1965,
        "nTO": 326,
        "expR": 0.03,
        "pf": 1.05,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 21.4,
        "ci90": {
          "expR": 0.03,
          "ci90": [
            -0.011,
            0.072
          ],
          "p_mean_le_0": 0.124,
          "n": 3169
        }
      },
      "1.2": {
        "n": 2740,
        "wrTP1": 27.7,
        "nSL": 1682,
        "nTO": 300,
        "expR": 0.035,
        "pf": 1.05,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 19.0,
        "ci90": {
          "expR": 0.035,
          "ci90": [
            -0.013,
            0.087
          ],
          "p_mean_le_0": 0.124,
          "n": 2626
        }
      },
      "1.3": {
        "n": 2502,
        "wrTP1": 26.0,
        "nSL": 1560,
        "nTO": 291,
        "expR": 0.029,
        "pf": 1.04,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.7,
        "ci90": {
          "expR": 0.029,
          "ci90": [
            -0.026,
            0.081
          ],
          "p_mean_le_0": 0.19,
          "n": 2391
        }
      },
      "1.5": {
        "n": 2117,
        "wrTP1": 23.7,
        "nSL": 1351,
        "nTO": 264,
        "expR": 0.032,
        "pf": 1.05,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 15.0,
        "ci90": {
          "expR": 0.032,
          "ci90": [
            -0.027,
            0.093
          ],
          "p_mean_le_0": 0.195,
          "n": 2023
        }
      },
      "2.0": {
        "n": 1360,
        "wrTP1": 17.4,
        "nSL": 910,
        "nTO": 213,
        "expR": 0.022,
        "pf": 1.03,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 11.1,
        "ci90": {
          "expR": 0.022,
          "ci90": [
            -0.059,
            0.103
          ],
          "p_mean_le_0": 0.351,
          "n": 1301
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 4884,
      "wrTP1": 47.7,
      "nSL": 2161,
      "nTO": 394,
      "expR": 0.065,
      "pf": 1.14,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 22.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.0,
      "ci90": {
        "expR": 0.065,
        "ci90": [
          0.037,
          0.094
        ],
        "p_mean_le_0": 0.0,
        "n": 4635
      }
    },
    "cuts": {
      "1.0": {
        "n": 2344,
        "wrTP1": 31.8,
        "nSL": 1314,
        "nTO": 284,
        "expR": 0.074,
        "pf": 1.12,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.5,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 24.0,
        "ci90": {
          "expR": 0.074,
          "ci90": [
            0.023,
            0.125
          ],
          "p_mean_le_0": 0.009,
          "n": 2180
        }
      },
      "1.2": {
        "n": 1930,
        "wrTP1": 29.2,
        "nSL": 1108,
        "nTO": 258,
        "expR": 0.09,
        "pf": 1.14,
        "mfe_p25": 12.0,
        "mfe_p50": 25.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 21.3,
        "ci90": {
          "expR": 0.09,
          "ci90": [
            0.032,
            0.143
          ],
          "p_mean_le_0": 0.01,
          "n": 1788
        }
      },
      "1.3": {
        "n": 1768,
        "wrTP1": 27.8,
        "nSL": 1024,
        "nTO": 252,
        "expR": 0.095,
        "pf": 1.15,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 53.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 20.5,
        "ci90": {
          "expR": 0.095,
          "ci90": [
            0.033,
            0.158
          ],
          "p_mean_le_0": 0.004,
          "n": 1632
        }
      },
      "1.5": {
        "n": 1508,
        "wrTP1": 25.5,
        "nSL": 899,
        "nTO": 224,
        "expR": 0.09,
        "pf": 1.14,
        "mfe_p25": 12.0,
        "mfe_p50": 26.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.600000000000023,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 18.4,
        "ci90": {
          "expR": 0.09,
          "ci90": [
            0.017,
            0.165
          ],
          "p_mean_le_0": 0.016,
          "n": 1392
        }
      },
      "2.0": {
        "n": 1000,
        "wrTP1": 20.5,
        "nSL": 622,
        "nTO": 173,
        "expR": 0.086,
        "pf": 1.13,
        "mfe_p25": 12.0,
        "mfe_p50": 28.0,
        "mfe_p75": 60.5,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.599999999999994,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 12.4,
        "ci90": {
          "expR": 0.086,
          "ci90": [
            -0.005,
            0.186
          ],
          "p_mean_le_0": 0.058,
          "n": 919
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 2963,
      "wrTP1": 48.0,
      "nSL": 1379,
      "nTO": 162,
      "expR": 0.018,
      "pf": 1.04,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 38.7,
      "ci90": {
        "expR": 0.018,
        "ci90": [
          -0.018,
          0.052
        ],
        "p_mean_le_0": 0.205,
        "n": 2850
      }
    },
    "cuts": {
      "1.0": {
        "n": 1336,
        "wrTP1": 30.4,
        "nSL": 815,
        "nTO": 115,
        "expR": -0.001,
        "pf": 1.0,
        "mfe_p25": 11.0,
        "mfe_p50": 23.5,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 31.7,
        "ci90": {
          "expR": -0.001,
          "ci90": [
            -0.072,
            0.07
          ],
          "p_mean_le_0": 0.503,
          "n": 1264
        }
      },
      "1.2": {
        "n": 1088,
        "wrTP1": 26.9,
        "nSL": 697,
        "nTO": 98,
        "expR": -0.01,
        "pf": 0.98,
        "mfe_p25": 11.0,
        "mfe_p50": 23.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 29.7,
        "ci90": {
          "expR": -0.01,
          "ci90": [
            -0.086,
            0.076
          ],
          "p_mean_le_0": 0.573,
          "n": 1029
        }
      },
      "1.3": {
        "n": 994,
        "wrTP1": 26.2,
        "nSL": 640,
        "nTO": 94,
        "expR": 0.005,
        "pf": 1.01,
        "mfe_p25": 11.0,
        "mfe_p50": 23.0,
        "mfe_p75": 59.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.5,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 28.6,
        "ci90": {
          "expR": 0.005,
          "ci90": [
            -0.076,
            0.09
          ],
          "p_mean_le_0": 0.453,
          "n": 939
        }
      },
      "1.5": {
        "n": 809,
        "wrTP1": 23.0,
        "nSL": 533,
        "nTO": 90,
        "expR": 0.007,
        "pf": 1.01,
        "mfe_p25": 11.0,
        "mfe_p50": 23.0,
        "mfe_p75": 60.75,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 26.3,
        "ci90": {
          "expR": 0.007,
          "ci90": [
            -0.1,
            0.114
          ],
          "p_mean_le_0": 0.461,
          "n": 758
        }
      },
      "2.0": {
        "n": 499,
        "wrTP1": 19.4,
        "nSL": 338,
        "nTO": 64,
        "expR": 0.077,
        "pf": 1.11,
        "mfe_p25": 11.0,
        "mfe_p50": 27.0,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.400000000000006,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 23.1,
        "ci90": {
          "expR": 0.077,
          "ci90": [
            -0.066,
            0.234
          ],
          "p_mean_le_0": 0.191,
          "n": 465
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 2016,
      "wrTP1": 51.1,
      "nSL": 874,
      "nTO": 111,
      "expR": 0.097,
      "pf": 1.22,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 44.2,
      "ci90": {
        "expR": 0.097,
        "ci90": [
          0.055,
          0.141
        ],
        "p_mean_le_0": 0.001,
        "n": 1952
      }
    },
    "cuts": {
      "1.0": {
        "n": 920,
        "wrTP1": 35.5,
        "nSL": 519,
        "nTO": 74,
        "expR": 0.141,
        "pf": 1.24,
        "mfe_p25": 16.0,
        "mfe_p50": 31.0,
        "mfe_p75": 59.5,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 36.0,
        "ci90": {
          "expR": 0.141,
          "ci90": [
            0.06,
            0.221
          ],
          "p_mean_le_0": 0.004,
          "n": 887
        }
      },
      "1.2": {
        "n": 749,
        "wrTP1": 32.0,
        "nSL": 440,
        "nTO": 69,
        "expR": 0.143,
        "pf": 1.23,
        "mfe_p25": 16.0,
        "mfe_p50": 32.0,
        "mfe_p75": 64.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 27.099999999999994,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 32.7,
        "ci90": {
          "expR": 0.143,
          "ci90": [
            0.048,
            0.245
          ],
          "p_mean_le_0": 0.005,
          "n": 719
        }
      },
      "1.3": {
        "n": 679,
        "wrTP1": 30.3,
        "nSL": 408,
        "nTO": 65,
        "expR": 0.134,
        "pf": 1.21,
        "mfe_p25": 16.75,
        "mfe_p50": 32.0,
        "mfe_p75": 65.5,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 27.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 31.4,
        "ci90": {
          "expR": 0.134,
          "ci90": [
            0.033,
            0.238
          ],
          "p_mean_le_0": 0.011,
          "n": 652
        }
      },
      "1.5": {
        "n": 564,
        "wrTP1": 27.8,
        "nSL": 348,
        "nTO": 59,
        "expR": 0.141,
        "pf": 1.22,
        "mfe_p25": 17.0,
        "mfe_p50": 33.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.5,
        "revAfterSL_rate": 29.6,
        "ci90": {
          "expR": 0.141,
          "ci90": [
            0.024,
            0.253
          ],
          "p_mean_le_0": 0.022,
          "n": 542
        }
      },
      "2.0": {
        "n": 373,
        "wrTP1": 23.6,
        "nSL": 237,
        "nTO": 48,
        "expR": 0.183,
        "pf": 1.28,
        "mfe_p25": 18.0,
        "mfe_p50": 36.0,
        "mfe_p75": 76.0,
        "winnerMAE_p75": 14.25,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 25.3,
        "ci90": {
          "expR": 0.183,
          "ci90": [
            0.035,
            0.344
          ],
          "p_mean_le_0": 0.02,
          "n": 357
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 1050,
      "wrTP1": 52.0,
      "nSL": 430,
      "nTO": 74,
      "expR": 0.141,
      "pf": 1.32,
      "mfe_p25": 12.0,
      "mfe_p50": 28.0,
      "mfe_p75": 66.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 41.5,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -35.0,
      "revAfterSL_rate": 52.8,
      "ci90": {
        "expR": 0.141,
        "ci90": [
          0.075,
          0.206
        ],
        "p_mean_le_0": 0.001,
        "n": 984
      }
    },
    "cuts": {
      "1.0": {
        "n": 440,
        "wrTP1": 36.1,
        "nSL": 233,
        "nTO": 48,
        "expR": 0.252,
        "pf": 1.43,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 81.25,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 34.400000000000034,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.5,
        "revAfterSL_rate": 48.5,
        "ci90": {
          "expR": 0.252,
          "ci90": [
            0.115,
            0.387
          ],
          "p_mean_le_0": 0.001,
          "n": 400
        }
      },
      "1.2": {
        "n": 369,
        "wrTP1": 35.5,
        "nSL": 194,
        "nTO": 44,
        "expR": 0.32,
        "pf": 1.55,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 80.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 29.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 45.9,
        "ci90": {
          "expR": 0.32,
          "ci90": [
            0.157,
            0.471
          ],
          "p_mean_le_0": 0.0,
          "n": 333
        }
      },
      "1.3": {
        "n": 334,
        "wrTP1": 32.9,
        "nSL": 185,
        "nTO": 39,
        "expR": 0.289,
        "pf": 1.47,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 79.5,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 22.400000000000034,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.5,
        "revAfterSL_rate": 44.9,
        "ci90": {
          "expR": 0.289,
          "ci90": [
            0.127,
            0.458
          ],
          "p_mean_le_0": 0.002,
          "n": 303
        }
      },
      "1.5": {
        "n": 283,
        "wrTP1": 32.2,
        "nSL": 157,
        "nTO": 35,
        "expR": 0.334,
        "pf": 1.54,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 80.5,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 42.0,
        "ci90": {
          "expR": 0.334,
          "ci90": [
            0.153,
            0.515
          ],
          "p_mean_le_0": 0.002,
          "n": 256
        }
      },
      "2.0": {
        "n": 186,
        "wrTP1": 26.3,
        "nSL": 111,
        "nTO": 26,
        "expR": 0.341,
        "pf": 1.52,
        "mfe_p25": 17.0,
        "mfe_p50": 39.0,
        "mfe_p75": 96.75,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 36.9,
        "ci90": {
          "expR": 0.341,
          "ci90": [
            0.077,
            0.6
          ],
          "p_mean_le_0": 0.015,
          "n": 168
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 725,
      "wrTP1": 51.0,
      "nSL": 302,
      "nTO": 53,
      "expR": 0.109,
      "pf": 1.25,
      "mfe_p25": 13.5,
      "mfe_p50": 30.0,
      "mfe_p75": 57.0,
      "winnerMAE_p75": 19.0,
      "winnerMAE_p90": 38.0,
      "loserMFEbeforeSL_p50": 4.5,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -29.0,
      "revAfterSL_rate": 39.7,
      "ci90": {
        "expR": 0.109,
        "ci90": [
          0.036,
          0.186
        ],
        "p_mean_le_0": 0.007,
        "n": 679
      }
    },
    "cuts": {
      "1.0": {
        "n": 313,
        "wrTP1": 34.8,
        "nSL": 175,
        "nTO": 29,
        "expR": 0.163,
        "pf": 1.27,
        "mfe_p25": 18.0,
        "mfe_p50": 39.5,
        "mfe_p75": 70.75,
        "winnerMAE_p75": 21.0,
        "winnerMAE_p90": 40.2,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 31.4,
        "ci90": {
          "expR": 0.163,
          "ci90": [
            0.011,
            0.321
          ],
          "p_mean_le_0": 0.038,
          "n": 290
        }
      },
      "1.2": {
        "n": 259,
        "wrTP1": 30.9,
        "nSL": 153,
        "nTO": 26,
        "expR": 0.152,
        "pf": 1.24,
        "mfe_p25": 18.25,
        "mfe_p50": 40.5,
        "mfe_p75": 69.75,
        "winnerMAE_p75": 19.25,
        "winnerMAE_p90": 37.400000000000034,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 28.8,
        "ci90": {
          "expR": 0.152,
          "ci90": [
            -0.029,
            0.339
          ],
          "p_mean_le_0": 0.086,
          "n": 238
        }
      },
      "1.3": {
        "n": 240,
        "wrTP1": 31.2,
        "nSL": 142,
        "nTO": 23,
        "expR": 0.164,
        "pf": 1.26,
        "mfe_p25": 19.25,
        "mfe_p50": 42.0,
        "mfe_p75": 70.75,
        "winnerMAE_p75": 19.5,
        "winnerMAE_p90": 39.400000000000034,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.5,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 28.2,
        "ci90": {
          "expR": 0.164,
          "ci90": [
            -0.015,
            0.343
          ],
          "p_mean_le_0": 0.061,
          "n": 222
        }
      },
      "1.5": {
        "n": 197,
        "wrTP1": 29.4,
        "nSL": 117,
        "nTO": 22,
        "expR": 0.182,
        "pf": 1.28,
        "mfe_p25": 22.0,
        "mfe_p50": 45.5,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 35.400000000000034,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 25.6,
        "ci90": {
          "expR": 0.182,
          "ci90": [
            -0.027,
            0.391
          ],
          "p_mean_le_0": 0.083,
          "n": 180
        }
      },
      "2.0": {
        "n": 129,
        "wrTP1": 22.5,
        "nSL": 86,
        "nTO": 14,
        "expR": 0.094,
        "pf": 1.13,
        "mfe_p25": 24.5,
        "mfe_p50": 49.0,
        "mfe_p75": 84.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 23.3,
        "ci90": {
          "expR": 0.094,
          "ci90": [
            -0.183,
            0.395
          ],
          "p_mean_le_0": 0.282,
          "n": 119
        }
      }
    }
  }
}
```

## Contrafactual RR minimo · fuera de muestra (mismo split que walk_forward)
```json
{
  "testWeeks": [
    "2026-W39",
    "2026-W40"
  ],
  "1/RETEST/LONG": {
    "baseline": {
      "n": 2305,
      "wrTP1": 46.9,
      "nSL": 1069,
      "nTO": 155,
      "expR": 0.044,
      "pf": 1.09,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 22.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 29.6,
      "ci90": {
        "expR": 0.044,
        "ci90": [
          0.003,
          0.086
        ],
        "p_mean_le_0": 0.036,
        "n": 2237
      }
    },
    "cuts": {
      "1.2": {
        "n": 942,
        "wrTP1": 26.9,
        "nSL": 585,
        "nTO": 104,
        "expR": 0.004,
        "pf": 1.01,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.5,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 16.80000000000001,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 19.3,
        "ci90": {
          "expR": 0.004,
          "ci90": [
            -0.083,
            0.091
          ],
          "p_mean_le_0": 0.474,
          "n": 907
        }
      },
      "1.3": {
        "n": 857,
        "wrTP1": 25.1,
        "nSL": 542,
        "nTO": 100,
        "expR": -0.005,
        "pf": 0.99,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 46.5,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 16.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 18.1,
        "ci90": {
          "expR": -0.005,
          "ci90": [
            -0.095,
            0.089
          ],
          "p_mean_le_0": 0.538,
          "n": 823
        }
      },
      "1.5": {
        "n": 726,
        "wrTP1": 22.7,
        "nSL": 470,
        "nTO": 91,
        "expR": -0.007,
        "pf": 0.99,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 15.599999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 13.8,
        "ci90": {
          "expR": -0.007,
          "ci90": [
            -0.108,
            0.097
          ],
          "p_mean_le_0": 0.567,
          "n": 698
        }
      },
      "2.0": {
        "n": 460,
        "wrTP1": 16.7,
        "nSL": 310,
        "nTO": 73,
        "expR": -0.009,
        "pf": 0.99,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 5.0,
        "winnerMAE_p90": 13.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 11.0,
        "ci90": {
          "expR": -0.009,
          "ci90": [
            -0.152,
            0.137
          ],
          "p_mean_le_0": 0.544,
          "n": 441
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 2007,
      "wrTP1": 50.0,
      "nSL": 873,
      "nTO": 130,
      "expR": 0.073,
      "pf": 1.16,
      "mfe_p25": 9.0,
      "mfe_p50": 18.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.6,
      "ci90": {
        "expR": 0.073,
        "ci90": [
          0.03,
          0.114
        ],
        "p_mean_le_0": 0.003,
        "n": 1935
      }
    },
    "cuts": {
      "1.2": {
        "n": 757,
        "wrTP1": 30.5,
        "nSL": 440,
        "nTO": 86,
        "expR": 0.068,
        "pf": 1.11,
        "mfe_p25": 14.0,
        "mfe_p50": 25.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 24.0,
        "loserMFEbeforeSL_p50": 7.5,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 22.0,
        "ci90": {
          "expR": 0.068,
          "ci90": [
            -0.026,
            0.159
          ],
          "p_mean_le_0": 0.116,
          "n": 715
        }
      },
      "1.3": {
        "n": 688,
        "wrTP1": 29.8,
        "nSL": 398,
        "nTO": 85,
        "expR": 0.09,
        "pf": 1.14,
        "mfe_p25": 14.5,
        "mfe_p50": 26.0,
        "mfe_p75": 50.5,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 22.799999999999983,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 21.1,
        "ci90": {
          "expR": 0.09,
          "ci90": [
            -0.003,
            0.191
          ],
          "p_mean_le_0": 0.055,
          "n": 647
        }
      },
      "1.5": {
        "n": 584,
        "wrTP1": 27.1,
        "nSL": 351,
        "nTO": 75,
        "expR": 0.069,
        "pf": 1.11,
        "mfe_p25": 15.0,
        "mfe_p50": 25.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.900000000000034,
        "loserMFEbeforeSL_p50": 9.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 18.8,
        "ci90": {
          "expR": 0.069,
          "ci90": [
            -0.036,
            0.182
          ],
          "p_mean_le_0": 0.149,
          "n": 549
        }
      },
      "2.0": {
        "n": 362,
        "wrTP1": 19.9,
        "nSL": 234,
        "nTO": 56,
        "expR": -0.001,
        "pf": 1.0,
        "mfe_p25": 15.0,
        "mfe_p50": 25.0,
        "mfe_p75": 54.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 26.9,
        "loserMFEbeforeSL_p50": 11.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 11.5,
        "ci90": {
          "expR": -0.001,
          "ci90": [
            -0.151,
            0.154
          ],
          "p_mean_le_0": 0.517,
          "n": 339
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 919,
      "wrTP1": 48.4,
      "nSL": 426,
      "nTO": 48,
      "expR": 0.034,
      "pf": 1.07,
      "mfe_p25": 9.0,
      "mfe_p50": 20.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 29.600000000000023,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 41.1,
      "ci90": {
        "expR": 0.034,
        "ci90": [
          -0.034,
          0.099
        ],
        "p_mean_le_0": 0.21,
        "n": 887
      }
    },
    "cuts": {
      "1.2": {
        "n": 322,
        "wrTP1": 25.5,
        "nSL": 211,
        "nTO": 29,
        "expR": -0.008,
        "pf": 0.99,
        "mfe_p25": 12.0,
        "mfe_p50": 24.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 34.1,
        "ci90": {
          "expR": -0.008,
          "ci90": [
            -0.157,
            0.154
          ],
          "p_mean_le_0": 0.55,
          "n": 305
        }
      },
      "1.3": {
        "n": 295,
        "wrTP1": 25.1,
        "nSL": 192,
        "nTO": 29,
        "expR": 0.027,
        "pf": 1.04,
        "mfe_p25": 12.0,
        "mfe_p50": 25.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 6.75,
        "winnerMAE_p90": 16.400000000000006,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 32.3,
        "ci90": {
          "expR": 0.027,
          "ci90": [
            -0.14,
            0.196
          ],
          "p_mean_le_0": 0.407,
          "n": 278
        }
      },
      "1.5": {
        "n": 247,
        "wrTP1": 21.9,
        "nSL": 165,
        "nTO": 28,
        "expR": 0.022,
        "pf": 1.03,
        "mfe_p25": 12.0,
        "mfe_p50": 23.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 15.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 30.3,
        "ci90": {
          "expR": 0.022,
          "ci90": [
            -0.168,
            0.219
          ],
          "p_mean_le_0": 0.428,
          "n": 231
        }
      },
      "2.0": {
        "n": 154,
        "wrTP1": 22.1,
        "nSL": 98,
        "nTO": 22,
        "expR": 0.227,
        "pf": 1.33,
        "mfe_p25": 15.25,
        "mfe_p50": 26.5,
        "mfe_p75": 59.75,
        "winnerMAE_p75": 7.0,
        "winnerMAE_p90": 16.4,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 29.6,
        "ci90": {
          "expR": 0.227,
          "ci90": [
            -0.037,
            0.501
          ],
          "p_mean_le_0": 0.087,
          "n": 142
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 829,
      "wrTP1": 52.6,
      "nSL": 356,
      "nTO": 37,
      "expR": 0.095,
      "pf": 1.21,
      "mfe_p25": 11.0,
      "mfe_p50": 22.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 44.7,
      "ci90": {
        "expR": 0.095,
        "ci90": [
          0.03,
          0.158
        ],
        "p_mean_le_0": 0.007,
        "n": 810
      }
    },
    "cuts": {
      "1.2": {
        "n": 316,
        "wrTP1": 32.3,
        "nSL": 190,
        "nTO": 24,
        "expR": 0.065,
        "pf": 1.1,
        "mfe_p25": 17.0,
        "mfe_p50": 33.0,
        "mfe_p75": 54.5,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 26.900000000000006,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 31.6,
        "ci90": {
          "expR": 0.065,
          "ci90": [
            -0.074,
            0.203
          ],
          "p_mean_le_0": 0.221,
          "n": 307
        }
      },
      "1.3": {
        "n": 279,
        "wrTP1": 29.7,
        "nSL": 174,
        "nTO": 22,
        "expR": 0.038,
        "pf": 1.06,
        "mfe_p25": 17.0,
        "mfe_p50": 32.0,
        "mfe_p75": 53.25,
        "winnerMAE_p75": 14.5,
        "winnerMAE_p90": 26.799999999999997,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 28.7,
        "ci90": {
          "expR": 0.038,
          "ci90": [
            -0.118,
            0.194
          ],
          "p_mean_le_0": 0.341,
          "n": 272
        }
      },
      "1.5": {
        "n": 230,
        "wrTP1": 27.0,
        "nSL": 150,
        "nTO": 18,
        "expR": 0.024,
        "pf": 1.04,
        "mfe_p25": 17.0,
        "mfe_p50": 33.0,
        "mfe_p75": 58.5,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 27.3,
        "ci90": {
          "expR": 0.024,
          "ci90": [
            -0.136,
            0.196
          ],
          "p_mean_le_0": 0.431,
          "n": 227
        }
      },
      "2.0": {
        "n": 152,
        "wrTP1": 19.1,
        "nSL": 108,
        "nTO": 15,
        "expR": -0.068,
        "pf": 0.91,
        "mfe_p25": 14.0,
        "mfe_p50": 33.0,
        "mfe_p75": 61.0,
        "winnerMAE_p75": 18.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 20.4,
        "ci90": {
          "expR": -0.068,
          "ci90": [
            -0.281,
            0.165
          ],
          "p_mean_le_0": 0.713,
          "n": 149
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 314,
      "wrTP1": 48.4,
      "nSL": 138,
      "nTO": 24,
      "expR": 0.063,
      "pf": 1.13,
      "mfe_p25": 13.0,
      "mfe_p50": 26.0,
      "mfe_p75": 65.0,
      "winnerMAE_p75": 21.0,
      "winnerMAE_p90": 42.80000000000001,
      "loserMFEbeforeSL_p50": 2.5,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -36.0,
      "revAfterSL_rate": 50.7,
      "ci90": {
        "expR": 0.063,
        "ci90": [
          -0.057,
          0.189
        ],
        "p_mean_le_0": 0.198,
        "n": 290
      }
    },
    "cuts": {
      "1.2": {
        "n": 106,
        "wrTP1": 29.2,
        "nSL": 65,
        "nTO": 10,
        "expR": 0.108,
        "pf": 1.16,
        "mfe_p25": 18.0,
        "mfe_p50": 36.0,
        "mfe_p75": 73.75,
        "winnerMAE_p75": 20.5,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 44.6,
        "ci90": {
          "expR": 0.108,
          "ci90": [
            -0.185,
            0.417
          ],
          "p_mean_le_0": 0.282,
          "n": 96
        }
      },
      "1.3": {
        "n": 97,
        "wrTP1": 28.9,
        "nSL": 61,
        "nTO": 8,
        "expR": 0.113,
        "pf": 1.16,
        "mfe_p25": 18.0,
        "mfe_p50": 36.0,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 22.500000000000004,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -32.0,
        "revAfterSL_rate": 42.6,
        "ci90": {
          "expR": 0.113,
          "ci90": [
            -0.179,
            0.437
          ],
          "p_mean_le_0": 0.263,
          "n": 89
        }
      },
      "1.5": {
        "n": 83,
        "wrTP1": 30.1,
        "nSL": 52,
        "nTO": 6,
        "expR": 0.178,
        "pf": 1.26,
        "mfe_p25": 20.0,
        "mfe_p50": 36.0,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 42.3,
        "ci90": {
          "expR": 0.178,
          "ci90": [
            -0.148,
            0.532
          ],
          "p_mean_le_0": 0.189,
          "n": 77
        }
      },
      "2.0": {
        "n": 58,
        "wrTP1": 20.7,
        "nSL": 40,
        "nTO": 6,
        "expR": 0.04,
        "pf": 1.05,
        "mfe_p25": 17.75,
        "mfe_p50": 36.0,
        "mfe_p75": 69.25,
        "winnerMAE_p75": 9.25,
        "winnerMAE_p90": 19.900000000000002,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 4.5,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 40.0,
        "ci90": {
          "expR": 0.04,
          "ci90": [
            -0.405,
            0.493
          ],
          "p_mean_le_0": 0.475,
          "n": 52
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 293,
      "wrTP1": 52.2,
      "nSL": 127,
      "nTO": 13,
      "expR": 0.098,
      "pf": 1.22,
      "mfe_p25": 15.0,
      "mfe_p50": 30.0,
      "mfe_p75": 51.5,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 31.80000000000001,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -29.0,
      "revAfterSL_rate": 37.8,
      "ci90": {
        "expR": 0.098,
        "ci90": [
          -0.02,
          0.214
        ],
        "p_mean_le_0": 0.086,
        "n": 283
      }
    },
    "cuts": {
      "1.2": {
        "n": 106,
        "wrTP1": 33.0,
        "nSL": 65,
        "nTO": 6,
        "expR": 0.159,
        "pf": 1.25,
        "mfe_p25": 18.0,
        "mfe_p50": 40.0,
        "mfe_p75": 61.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 26.60000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 26.2,
        "ci90": {
          "expR": 0.159,
          "ci90": [
            -0.101,
            0.442
          ],
          "p_mean_le_0": 0.167,
          "n": 103
        }
      },
      "1.3": {
        "n": 101,
        "wrTP1": 33.7,
        "nSL": 61,
        "nTO": 6,
        "expR": 0.184,
        "pf": 1.3,
        "mfe_p25": 19.0,
        "mfe_p50": 40.0,
        "mfe_p75": 61.0,
        "winnerMAE_p75": 17.5,
        "winnerMAE_p90": 27.199999999999996,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 27.9,
        "ci90": {
          "expR": 0.184,
          "ci90": [
            -0.082,
            0.464
          ],
          "p_mean_le_0": 0.133,
          "n": 98
        }
      },
      "1.5": {
        "n": 81,
        "wrTP1": 29.6,
        "nSL": 51,
        "nTO": 6,
        "expR": 0.138,
        "pf": 1.21,
        "mfe_p25": 18.25,
        "mfe_p50": 41.0,
        "mfe_p75": 61.75,
        "winnerMAE_p75": 11.5,
        "winnerMAE_p90": 22.7,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 23.5,
        "ci90": {
          "expR": 0.138,
          "ci90": [
            -0.166,
            0.464
          ],
          "p_mean_le_0": 0.237,
          "n": 78
        }
      },
      "2.0": {
        "n": 56,
        "wrTP1": 19.6,
        "nSL": 39,
        "nTO": 6,
        "expR": 0.018,
        "pf": 1.02,
        "mfe_p25": 24.0,
        "mfe_p50": 47.0,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 12.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 17.9,
        "ci90": {
          "expR": 0.018,
          "ci90": [
            -0.369,
            0.443
          ],
          "p_mean_le_0": 0.475,
          "n": 53
        }
      }
    }
  }
}
```

## Decaimiento semanal
```json
{
  "2026-W36": {
    "n": 2867,
    "wrTP1": 44.8,
    "expR": -0.018
  },
  "2026-W37": {
    "n": 4992,
    "wrTP1": 46.9,
    "expR": 0.074
  },
  "2026-W38": {
    "n": 4622,
    "wrTP1": 46.1,
    "expR": 0.091
  },
  "2026-W39": {
    "n": 5289,
    "wrTP1": 45.7,
    "expR": 0.056
  },
  "2026-W40": {
    "n": 1906,
    "wrTP1": 49.6,
    "expR": 0.099
  }
}
```

## Decaimiento semanal por segmento (tf/kind/side)
```json
{
  "2026-W36": {
    "1m/INV/LONG": {
      "n": 34,
      "wrTP1": 47.1,
      "expR": 0.281,
      "pf": 1.64
    },
    "1m/INV/SHORT": {
      "n": 17,
      "wrTP1": 70.6,
      "expR": 0.243,
      "pf": 1.83
    },
    "1m/RETEST/LONG": {
      "n": 1205,
      "wrTP1": 42.7,
      "expR": -0.017,
      "pf": 0.97
    },
    "1m/RETEST/SHORT": {
      "n": 434,
      "wrTP1": 43.5,
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
      "n": 612,
      "wrTP1": 46.2,
      "expR": -0.057,
      "pf": 0.89
    },
    "2m/RETEST/SHORT": {
      "n": 201,
      "wrTP1": 41.3,
      "expR": -0.098,
      "pf": 0.82
    },
    "5m/INV/LONG": {
      "n": 5,
      "wrTP1": 100.0,
      "expR": 0.674,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 0.018,
      "pf": 1.07
    },
    "5m/RETEST/LONG": {
      "n": 241,
      "wrTP1": 52.3,
      "expR": 0.08,
      "pf": 1.18
    },
    "5m/RETEST/SHORT": {
      "n": 91,
      "wrTP1": 47.3,
      "expR": -0.019,
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
      "n": 54,
      "wrTP1": 40.7,
      "expR": 0.037,
      "pf": 1.07
    },
    "1m/RETEST/LONG": {
      "n": 1479,
      "wrTP1": 45.3,
      "expR": 0.062,
      "pf": 1.13
    },
    "1m/RETEST/SHORT": {
      "n": 1616,
      "wrTP1": 45.1,
      "expR": 0.041,
      "pf": 1.08
    },
    "2m/INV/LONG": {
      "n": 8,
      "wrTP1": 62.5,
      "expR": 0.115,
      "pf": 1.37
    },
    "2m/INV/SHORT": {
      "n": 31,
      "wrTP1": 35.5,
      "expR": 0.137,
      "pf": 1.27
    },
    "2m/RETEST/LONG": {
      "n": 638,
      "wrTP1": 47.0,
      "expR": 0.025,
      "pf": 1.05
    },
    "2m/RETEST/SHORT": {
      "n": 697,
      "wrTP1": 51.5,
      "expR": 0.152,
      "pf": 1.34
    },
    "5m/INV/LONG": {
      "n": 3,
      "wrTP1": 66.7,
      "expR": 1.3,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 4,
      "wrTP1": 75.0,
      "expR": 1.212,
      "pf": 5.85
    },
    "5m/RETEST/LONG": {
      "n": 225,
      "wrTP1": 51.6,
      "expR": 0.191,
      "pf": 1.42
    },
    "5m/RETEST/SHORT": {
      "n": 201,
      "wrTP1": 53.2,
      "expR": 0.158,
      "pf": 1.36
    }
  },
  "2026-W38": {
    "1m/INV/LONG": {
      "n": 56,
      "wrTP1": 41.1,
      "expR": -0.112,
      "pf": 0.78
    },
    "1m/INV/SHORT": {
      "n": 22,
      "wrTP1": 45.5,
      "expR": -0.098,
      "pf": 0.8
    },
    "1m/RETEST/LONG": {
      "n": 1896,
      "wrTP1": 48.3,
      "expR": 0.122,
      "pf": 1.27
    },
    "1m/RETEST/SHORT": {
      "n": 956,
      "wrTP1": 42.6,
      "expR": 0.113,
      "pf": 1.25
    },
    "2m/INV/LONG": {
      "n": 15,
      "wrTP1": 53.3,
      "expR": -0.12,
      "pf": 0.61
    },
    "2m/INV/SHORT": {
      "n": 4,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "2m/RETEST/LONG": {
      "n": 849,
      "wrTP1": 46.4,
      "expR": 0.036,
      "pf": 1.08
    },
    "2m/RETEST/SHORT": {
      "n": 353,
      "wrTP1": 43.3,
      "expR": 0.001,
      "pf": 1.0
    },
    "5m/INV/LONG": {
      "n": 7,
      "wrTP1": 28.6,
      "expR": -0.478,
      "pf": 0.2
    },
    "5m/INV/SHORT": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 300,
      "wrTP1": 50.7,
      "expR": 0.177,
      "pf": 1.43
    },
    "5m/RETEST/SHORT": {
      "n": 163,
      "wrTP1": 41.1,
      "expR": 0.1,
      "pf": 1.2
    }
  },
  "2026-W39": {
    "1m/INV/LONG": {
      "n": 37,
      "wrTP1": 48.6,
      "expR": 0.702,
      "pf": 3.36
    },
    "1m/INV/SHORT": {
      "n": 42,
      "wrTP1": 50.0,
      "expR": 0.057,
      "pf": 1.15
    },
    "1m/RETEST/LONG": {
      "n": 2005,
      "wrTP1": 44.6,
      "expR": 0.053,
      "pf": 1.11
    },
    "1m/RETEST/SHORT": {
      "n": 1353,
      "wrTP1": 44.8,
      "expR": -0.006,
      "pf": 0.99
    },
    "2m/INV/LONG": {
      "n": 25,
      "wrTP1": 48.0,
      "expR": 0.267,
      "pf": 1.68
    },
    "2m/INV/SHORT": {
      "n": 17,
      "wrTP1": 58.8,
      "expR": 0.508,
      "pf": 3.54
    },
    "2m/RETEST/LONG": {
      "n": 773,
      "wrTP1": 46.3,
      "expR": 0.126,
      "pf": 1.26
    },
    "2m/RETEST/SHORT": {
      "n": 564,
      "wrTP1": 49.1,
      "expR": 0.03,
      "pf": 1.07
    },
    "5m/INV/LONG": {
      "n": 4,
      "wrTP1": 100.0,
      "expR": 0.632,
      "pf": 99.0
    },
    "5m/INV/SHORT": {
      "n": 3,
      "wrTP1": 66.7,
      "expR": 0.195,
      "pf": 99.0
    },
    "5m/RETEST/LONG": {
      "n": 265,
      "wrTP1": 44.9,
      "expR": 0.071,
      "pf": 1.15
    },
    "5m/RETEST/SHORT": {
      "n": 201,
      "wrTP1": 47.3,
      "expR": 0.08,
      "pf": 1.17
    }
  },
  "2026-W40": {
    "1m/INV/LONG": {
      "n": 8,
      "wrTP1": 62.5,
      "expR": 0.394,
      "pf": 2.57
    },
    "1m/INV/SHORT": {
      "n": 24,
      "wrTP1": 37.5,
      "expR": -0.299,
      "pf": 0.45
    },
    "1m/RETEST/LONG": {
      "n": 409,
      "wrTP1": 45.7,
      "expR": 0.03,
      "pf": 1.06
    },
    "1m/RETEST/SHORT": {
      "n": 767,
      "wrTP1": 51.9,
      "expR": 0.155,
      "pf": 1.36
    },
    "2m/INV/LONG": {
      "n": 2,
      "wrTP1": 50.0,
      "expR": -0.345,
      "pf": 0.31
    },
    "2m/INV/SHORT": {
      "n": 9,
      "wrTP1": 55.6,
      "expR": -0.072,
      "pf": 0.79
    },
    "2m/RETEST/LONG": {
      "n": 186,
      "wrTP1": 46.8,
      "expR": -0.056,
      "pf": 0.89
    },
    "2m/RETEST/SHORT": {
      "n": 317,
      "wrTP1": 50.8,
      "expR": 0.231,
      "pf": 1.5
    },
    "5m/INV/LONG": {
      "n": 1,
      "wrTP1": 100.0,
      "expR": 0.16,
      "pf": 99.0
    },
    "5m/RETEST/LONG": {
      "n": 71,
      "wrTP1": 46.5,
      "expR": -0.008,
      "pf": 0.99
    },
    "5m/RETEST/SHORT": {
      "n": 112,
      "wrTP1": 51.8,
      "expR": 0.011,
      "pf": 1.02
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 18121,
  "brier": 0.2213,
  "bias": -0.08,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.209
    },
    {
      "feature": "nearTk",
      "weight": -0.056
    },
    {
      "feature": "stretchAtr",
      "weight": -0.056
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.034
    },
    {
      "feature": "biasScore",
      "weight": -0.028
    },
    {
      "feature": "emaStack",
      "weight": 0.027
    },
    {
      "feature": "rvol",
      "weight": 0.024
    },
    {
      "feature": "nearEdge",
      "weight": -0.018
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.017
    },
    {
      "feature": "aligned",
      "weight": -0.015
    },
    {
      "feature": "chopIdx",
      "weight": -0.007
    },
    {
      "feature": "structDir",
      "weight": 0.004
    },
    {
      "feature": "hourNY",
      "weight": 0.004
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.157,
      "actual": 0.185,
      "n": 1812
    },
    {
      "bin": 1,
      "pred": 0.359,
      "actual": 0.312,
      "n": 1812
    },
    {
      "bin": 2,
      "pred": 0.445,
      "actual": 0.337,
      "n": 1812
    },
    {
      "bin": 3,
      "pred": 0.493,
      "actual": 0.391,
      "n": 1812
    },
    {
      "bin": 4,
      "pred": 0.534,
      "actual": 0.518,
      "n": 1812
    },
    {
      "bin": 5,
      "pred": 0.566,
      "actual": 0.567,
      "n": 1812
    },
    {
      "bin": 6,
      "pred": 0.59,
      "actual": 0.616,
      "n": 1812
    },
    {
      "bin": 7,
      "pred": 0.612,
      "actual": 0.659,
      "n": 1812
    },
    {
      "bin": 8,
      "pred": 0.631,
      "actual": 0.69,
      "n": 1812
    },
    {
      "bin": 9,
      "pred": 0.659,
      "actual": 0.756,
      "n": 1813
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 12481,
  "testN": 7195,
  "testWeeks": [
    "2026-W39",
    "2026-W40"
  ],
  "model_oos_brier": 0.2215,
  "model_oos_n": 7195,
  "best_scheme_in_sample": {
    "scheme": "nextLevel",
    "trainExpR": 0.059
  },
  "best_scheme_oos_expR": 0.068
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.193,
    "ci90": [
      0.024,
      0.385
    ],
    "p_mean_le_0": 0.032,
    "n": 162,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": -0.005,
    "ci90": [
      -0.148,
      0.132
    ],
    "p_mean_le_0": 0.518,
    "n": 153,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.06,
    "ci90": [
      0.034,
      0.085
    ],
    "p_mean_le_0": 0.0,
    "n": 6776,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.054,
    "ci90": [
      0.027,
      0.083
    ],
    "p_mean_le_0": 0.001,
    "n": 4863,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.015,
    "ci90": [
      -0.194,
      0.236
    ],
    "p_mean_le_0": 0.464,
    "n": 63,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.087,
    "ci90": [
      -0.167,
      0.355
    ],
    "p_mean_le_0": 0.293,
    "n": 65,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.032,
    "ci90": [
      -0.008,
      0.069
    ],
    "p_mean_le_0": 0.097,
    "n": 2938,
    "survives_fdr10": false
  },
  "2m/RETEST/SHORT": {
    "expR": 0.086,
    "ci90": [
      0.04,
      0.132
    ],
    "p_mean_le_0": 0.001,
    "n": 2058,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.421,
    "ci90": [
      0.091,
      0.759
    ],
    "p_mean_le_0": 0.018,
    "n": 18,
    "survives_fdr10": true
  },
  "5m/INV/SHORT": {
    "expR": 0.392,
    "ci90": [
      -0.14,
      0.965
    ],
    "p_mean_le_0": 0.115,
    "n": 11,
    "survives_fdr10": false
  },
  "5m/RETEST/LONG": {
    "expR": 0.121,
    "ci90": [
      0.058,
      0.188
    ],
    "p_mean_le_0": 0.001,
    "n": 1029,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.083,
    "ci90": [
      0.009,
      0.159
    ],
    "p_mean_le_0": 0.034,
    "n": 717,
    "survives_fdr10": true
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
      "id": 2,
      "n": 333,
      "wrTP1": 42.3,
      "expR": 0.198,
      "pf": 1.42,
      "defining_features": {
        "nearTk": 4.62,
        "entryZoneTk": -4.31,
        "atrPctUsed": 1.51,
        "nearEdge": -0.44
      }
    },
    {
      "id": 0,
      "n": 4265,
      "wrTP1": 50.2,
      "expR": 0.062,
      "pf": 1.14,
      "defining_features": {
        "structDir": -1.02,
        "biasScore": 0.67,
        "nearEdge": 0.48,
        "emaStack": 0.35
      }
    },
    {
      "id": 3,
      "n": 7220,
      "wrTP1": 44.2,
      "expR": 0.061,
      "pf": 1.12,
      "defining_features": {
        "structDir": 0.98,
        "biasScore": 0.82,
        "emaStack": 0.8,
        "nearEdge": 0.65
      }
    },
    {
      "id": 1,
      "n": 7858,
      "wrTP1": 46.4,
      "expR": 0.057,
      "pf": 1.12,
      "defining_features": {
        "biasScore": -1.11,
        "emaStack": -0.91,
        "nearEdge": -0.84,
        "structDir": -0.35
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
        "n": 38,
        "wrTP1": 55.3,
        "expR": 0.611
      },
      "YM": {
        "n": 63,
        "wrTP1": 33.3,
        "expR": 0.231
      },
      "ES": {
        "n": 26,
        "wrTP1": 61.5,
        "expR": 0.132
      },
      "GC": {
        "n": 24,
        "wrTP1": 33.3,
        "expR": -0.428
      },
      "NQ": {
        "n": 20,
        "wrTP1": 55.0,
        "expR": 0.118
      }
    },
    "expR_spread": 1.039,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 91,
        "wrTP1": 39.6,
        "expR": -0.088
      },
      "NQ": {
        "n": 16,
        "wrTP1": 56.2,
        "expR": 0.128
      },
      "ES": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": 0.439
      },
      "GC": {
        "n": 32,
        "wrTP1": 62.5,
        "expR": 0.122
      },
      "CL": {
        "n": 13,
        "wrTP1": 38.5,
        "expR": -0.178
      }
    },
    "expR_spread": 0.617,
    "verdict": "instrument-specific"
  },
  "1m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 1089,
        "wrTP1": 42.8,
        "expR": 0.024
      },
      "NQ": {
        "n": 1545,
        "wrTP1": 45.6,
        "expR": 0.046
      },
      "ES": {
        "n": 1710,
        "wrTP1": 46.9,
        "expR": 0.065
      },
      "CL": {
        "n": 1565,
        "wrTP1": 45.8,
        "expR": 0.073
      },
      "YM": {
        "n": 1085,
        "wrTP1": 45.3,
        "expR": 0.088
      }
    },
    "expR_spread": 0.064,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 564,
        "wrTP1": 44.7,
        "expR": 0.148
      },
      "GC": {
        "n": 1330,
        "wrTP1": 45.9,
        "expR": 0.088
      },
      "YM": {
        "n": 1551,
        "wrTP1": 44.9,
        "expR": 0.041
      },
      "ES": {
        "n": 976,
        "wrTP1": 46.9,
        "expR": 0.031
      },
      "CL": {
        "n": 705,
        "wrTP1": 44.3,
        "expR": -0.021
      }
    },
    "expR_spread": 0.169,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 8,
        "wrTP1": 37.5,
        "expR": -0.454
      },
      "CL": {
        "n": 8,
        "wrTP1": 62.5,
        "expR": -0.016
      },
      "YM": {
        "n": 19,
        "wrTP1": 31.6,
        "expR": -0.256
      },
      "ES": {
        "n": 14,
        "wrTP1": 71.4,
        "expR": 0.191
      },
      "NQ": {
        "n": 18,
        "wrTP1": 50.0,
        "expR": 0.397
      }
    },
    "expR_spread": 0.851,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 40,
        "wrTP1": 52.5,
        "expR": 0.272
      },
      "NQ": {
        "n": 9,
        "wrTP1": 44.4,
        "expR": 0.184
      },
      "ES": {
        "n": 8,
        "wrTP1": 25.0,
        "expR": -0.176
      },
      "GC": {
        "n": 6,
        "wrTP1": 16.7,
        "expR": -0.46
      },
      "CL": {
        "n": 4,
        "wrTP1": 25.0,
        "expR": -0.665
      }
    },
    "expR_spread": 0.937,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 713,
        "wrTP1": 45.6,
        "expR": 0.027
      },
      "GC": {
        "n": 447,
        "wrTP1": 44.7,
        "expR": -0.008
      },
      "CL": {
        "n": 716,
        "wrTP1": 48.0,
        "expR": 0.057
      },
      "ES": {
        "n": 675,
        "wrTP1": 48.3,
        "expR": 0.012
      },
      "YM": {
        "n": 507,
        "wrTP1": 44.8,
        "expR": 0.067
      }
    },
    "expR_spread": 0.075,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 415,
        "wrTP1": 49.6,
        "expR": 0.013
      },
      "YM": {
        "n": 636,
        "wrTP1": 49.4,
        "expR": 0.086
      },
      "GC": {
        "n": 545,
        "wrTP1": 49.7,
        "expR": 0.212
      },
      "NQ": {
        "n": 257,
        "wrTP1": 42.8,
        "expR": 0.109
      },
      "CL": {
        "n": 279,
        "wrTP1": 47.3,
        "expR": -0.052
      }
    },
    "expR_spread": 0.264,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": 0.027
      },
      "YM": {
        "n": 5,
        "wrTP1": 100.0,
        "expR": 0.526
      },
      "CL": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 1.473
      },
      "ES": {
        "n": 4,
        "wrTP1": 75.0,
        "expR": 0.453
      }
    },
    "expR_spread": 1.446,
    "verdict": "instrument-specific"
  },
  "5m/INV/SHORT": {
    "symbols": {
      "NQ": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.85
      },
      "YM": {
        "n": 3,
        "wrTP1": 0.0,
        "expR": -1.0
      },
      "GC": {
        "n": 3,
        "wrTP1": 66.7,
        "expR": 0.755
      }
    },
    "expR_spread": 1.85,
    "verdict": "instrument-specific"
  },
  "5m/RETEST/LONG": {
    "symbols": {
      "GC": {
        "n": 118,
        "wrTP1": 47.5,
        "expR": 0.113
      },
      "ES": {
        "n": 239,
        "wrTP1": 49.8,
        "expR": 0.175
      },
      "YM": {
        "n": 174,
        "wrTP1": 52.3,
        "expR": 0.261
      },
      "CL": {
        "n": 245,
        "wrTP1": 51.4,
        "expR": 0.102
      },
      "NQ": {
        "n": 326,
        "wrTP1": 47.2,
        "expR": 0.024
      }
    },
    "expR_spread": 0.237,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 96,
        "wrTP1": 49.0,
        "expR": -0.004
      },
      "ES": {
        "n": 150,
        "wrTP1": 55.3,
        "expR": 0.112
      },
      "GC": {
        "n": 182,
        "wrTP1": 41.2,
        "expR": 0.005
      },
      "YM": {
        "n": 221,
        "wrTP1": 49.3,
        "expR": 0.162
      },
      "CL": {
        "n": 119,
        "wrTP1": 47.1,
        "expR": 0.087
      }
    },
    "expR_spread": 0.166,
    "verdict": "universal"
  }
}
```

## Contexto de noticias
```json
{
  "available": true,
  "n_events": 10,
  "near_news_30m": {
    "n": 68,
    "wrTP1": 45.6,
    "nSL": 29,
    "nTO": 8,
    "expR": 0.021,
    "pf": 1.05,
    "mfe_p25": 6.0,
    "mfe_p50": 15.0,
    "mfe_p75": 25.0,
    "winnerMAE_p75": 5.0,
    "winnerMAE_p90": 8.0,
    "loserMFEbeforeSL_p50": 13.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 8.0,
    "entryZoneTk_p50": -6.5,
    "revAfterSL_rate": 55.2
  },
  "away_from_news": {
    "n": 19608,
    "wrTP1": 46.3,
    "nSL": 8975,
    "nTO": 1547,
    "expR": 0.062,
    "pf": 1.13,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 32.9
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 6,
  "mae_deltaER": 0.251,
  "hit_direction_rate": 33.3
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
    "status": "applied",
    "hypothesis": "En RETEST, poner el SL en la mecha exacta de la vela del retest (crudo, sin piso ni techo) en vez del stop de 3 capas sube el E[R]. Baja el win rate (stop mas pegado, salta mas) pero los ganadores que sobreviven pagan mucha mas R, y el neto mejora. HASTA 2026-09-04 esto solo certificaba en SHORT (\"no aplica a largos\"); con la muestra de 2026-09-05 TAMBIEN certifica en 1m LONG, asi que se retira la exclusion dura de BUY RETEST y se deja como 'certifica por tf/side, no generalizar sin mirar la tabla'. 2026-09-06: mismas cifras exactas que 2026-09-05 (n identico) porque no llego dato nuevo. 2026-09-07 (lunes, primer dia con trades GENUINAMENTE nuevos post-restauracion, sin repeticion del bug de heal): retest_1m_long paso de n=1087 a n=1135 (+48 pares nuevos, no restaurados) y el delta se mantiene practicamente igual (0.181->0.183) con el CI90 todavia sin cruzar cero -- esta es la primera confirmacion independiente real que pedia el next_steps anterior. retest_1m_short tambien crecio con dato nuevo (n=219->229) y sigue certificando. 2026-09-08 (martes, primer dia habil COMPLETO post-feriado, salto grande de muestra real): retest_1m_long n=1135->1432 (delta 0.183->0.18, estable, segunda confirmacion independiente); retest_1m_short n=229->514 (delta 0.283->0.417, se hizo MAS fuerte); retest_2m_short CERTIFICA POR PRIMERA VEZ (n=129->260, CI90 dejo de cruzar cero); retest_5m_long CERTIFICA POR PRIMERA VEZ pero al filo (n=224->274, CI90=[0.005,0.36], limite inferior casi cero, vigilar que no se revierta con mas muestra); retest_2m_long sigue sin certificar y el delta bajo a casi cero (0.028->0.01, n=596->742).",
    "param": "sl_basis_retest",
    "from": "3-capas (sc_slbuf x ATR1m + piso sc_floor_atr5 + techo sc_cap_atr5 / sc_cap_adr)",
    "to": "mecha de la vela del retest (lg_slOrig con slBasis=retestBar / retestBar2, crudo)",
    "changeDate": "2026-09-26",
    "segment": {
      "kind": "RETEST"
    },
    "targetMetric": "expR",
    "minAfterN": 40,
    "evidence": {
      "source": "sl_origin_vs_layer.by_basis / by_tf_kind_side (medicion PARALELA: misma entrada y mismos TP, solo se mueve el stop; rMultiple = base 3-capas, rOrig = base mecha del retest). No requiere cambio en TradingView para medir.",
      "asOf": "2026-09-21 (lunes). Primer dia habil con dato nuevo genuino tras el fin de semana (+72 pares en todo el bus). n de pares resueltos subio de 13132 a 13204.",
      "retest_1m_long": {
        "n": 4111,
        "deltaER_orig_minus_layer": 0.147,
        "ci90": [
          0.084,
          0.21
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 4078 a 4111, delta estable (0.152->0.147) -- decimotercera confirmacion."
      },
      "retest_1m_short": {
        "n": 2440,
        "deltaER_orig_minus_layer": 0.153,
        "ci90": [
          0.066,
          0.244
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 2432 a 2440, delta identico (0.153) -- decimotercera confirmacion."
      },
      "retest_2m_long": {
        "n": 1919,
        "deltaER_orig_minus_layer": 0.151,
        "ci90": [
          0.078,
          0.228
        ],
        "ci90_no_cruza_cero": true,
        "nota": "TERCERA lectura consecutiva con dato genuinamente nuevo (primera 09-18, segunda 09-19, el 09-20 fue fin de semana sin trade real y no conto): n subio de 1897 a 1919, delta estable (0.153->0.151), CI90 practicamente igual (limite inferior 0.079->0.078). Cumple el criterio de '2-3 lecturas seguidas' que el experimento se puso a si mismo -- SE PROMUEVE a candidato de la propuesta formal hoy, con la misma advertencia de historial volatil que se le puso a 5m LONG cuando se sumo."
      },
      "retest_2m_short": {
        "n": 1097,
        "deltaER_orig_minus_layer": 0.134,
        "ci90": [
          0.04,
          0.232
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 1092 a 1097, delta identico (0.134), limite inferior del CI90 practicamente igual (0.039->0.04) -- sigue candidato debil/al filo, no se promueve."
      },
      "retest_5m_long": {
        "n": 713,
        "deltaER_orig_minus_layer": 0.276,
        "ci90": [
          0.111,
          0.466
        ],
        "ci90_no_cruza_cero": true,
        "nota": "sin senales 5m LONG nuevas hoy (n identico a ayer, 713) -- no cuenta como lectura independiente nueva, se mantiene en su novena confirmacion."
      },
      "retest_5m_short": {
        "n": 409,
        "deltaER_orig_minus_layer": 0.489,
        "ci90": [
          0.138,
          0.896
        ],
        "ci90_no_cruza_cero": true,
        "nota": "n subio de 408 a 409 (+1), delta practicamente identico (0.49->0.489) -- sigue siendo la lectura mas solida del experimento por margen."
      },
      "overall_by_basis_retestBar": {
        "n": 8374,
        "deltaER": 0.175,
        "ci90": [
          0.133,
          0.219
        ],
        "nota": "n subio de 8313 a 8374, delta estable (0.178->0.175) -- sigue sin usarse sola como evidencia, la decision es por tf/side de la tabla de arriba."
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
      "2026-09-17 (jueves, dato nuevo genuino, +1097 pares resueltos en todo el bus, el salto mas grande en varios dias): los 4 segmentos propuestos el 09-13 (1m LONG, 1m SHORT, 5m LONG, 5m SHORT) se mantienen TODOS con `delta_beats_zero=true` y sin ningun retroceso -- 1m LONG suma su DECIMA confirmacion (n=2737->3095, delta 0.15->0.142, CI90 [0.066,0.218]), 1m SHORT sube (n=1971->2085, delta 0.127->0.143, CI90 [0.046,0.247]), 5m LONG suma su SEPTIMA lectura seguida certificando (n=492->555, delta 0.248->0.218, CI90 [0.05,0.403]) y 5m SHORT sigue siendo el efecto mas grande, con margen (n=309->324, delta 0.554->0.514, CI90 [0.133,0.987]). 2m SHORT se mantiene candidato debil/al filo por otra corrida mas (n=895->939, delta 0.117->0.113, limite inferior del CI90 practicamente igual, 0.011 vs 0.012). 2m LONG sigue sin certificar, undecima lectura seguida (n=1327->1477, delta 0.035->0.05, CI90 [-0.018,0.12] -- el delta sube y el limite inferior se acerca a cero, vigilar si se acerca a certificar en las proximas corridas). Nota de gate: la semana ya cerrada 2026-W37 en el segmento 5m/RETEST/LONG (el segmento objetivo del gate de ejecucion) paso de PF=1.44 a PF=1.45 pero perdio 6 pares de muestra por el mismo mecanismo de dedup que ya afectaba los conteos agregados (n=241->235) -- primera vez que se ve este efecto a nivel de segmento individual, sin evidencia de perdida real de archivo (file_integrity_check limpio). Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView. Hallazgo nuevo en paralelo (no de este experimento): por primera vez el veredicto SA=GO certifica con significancia junto a SA=WAIT en el cruce agregado con Session Analyst (ver report.alerts); y en el desglose por kind/side, la rama AVOID de RETEST/LONG cruza a E[R] negativo por primera vez mientras la rama WAIT de RETEST/SHORT cruza a positivo -- ver playbooks para el detalle por lado.",
      "2026-09-18 (viernes): HEAD quedo detached tras el `git pull` porque `origin/main` fue reescrito rio arriba (historia sin ancestro comun con la rama local, primera vez que pasa desde 09-11) -- verificado que el commit remoto contenia todo el trabajo esperado (mismo tip de datos, ultimos 50 commits del bus) antes de resolver con `checkout -B main origin/main`, sin perdida. Dato nuevo genuino grande (+768 pares en todo el dataset). **HALLAZGO PRINCIPAL: retest_2m_long CERTIFICA POR PRIMERA VEZ** tras 11 lecturas seguidas sin lograrlo (delta 0.05->0.074, CI90 [-0.018,0.12]->[0.005,0.145], limite inferior cruza por encima de cero) -- se trata como candidato nuevo y fragil, no se suma todavia a la propuesta formal (mismo criterio de '2-3 lecturas seguidas' que se aplico a 5m LONG en la semana pasada). Los 4 segmentos ya propuestos (1m LONG/SHORT, 5m LONG/SHORT) se mantienen TODOS con `delta_beats_zero=true` y se fortalecen: 1m LONG suma su UNDECIMA confirmacion, 1m SHORT sube de delta 0.143 a 0.155, 5m LONG suma su OCTAVA lectura seguida con un salto notable (0.218->0.312), 5m SHORT estable como el efecto mas grande. 2m SHORT tiene su mejor lectura hasta ahora (limite inferior del CI90 0.011->0.031) pero se mantiene un dia mas como candidato debil antes de promoverlo. Nota de gate: en el segmento objetivo (5m/RETEST/LONG), la semana ya cerrada 2026-W36 volvio a perder 1 par por dedup (n=242, PF=1.18, sigue <1.3) y 2026-W37 tambien perdio 1 par (n=234, pero PF SUBIO a 1.47) -- el dedup a nivel de segmento sigue siendo benigno (sin evidencia de perdida real de archivo) pero ya van 3 corridas seguidas afectando este segmento especifico, vigilar que no erosione la serie. Sin cambios de estado en el experimento: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView -- con 4 segmentos solidos (2 de ellos en su octava/undecima confirmacion sin un solo retroceso desde el 09-13) mas un quinto candidato nuevo (2m LONG), esta es la evidencia acumulada mas fuerte hasta ahora para aplicar el cambio.",
      "2026-09-19 (sabado): salto de dato grande, el mayor en varios dias (n 11452->13092, +1640; el bus asento de una vez los archivos de 2026-09-18, mismo 'forced update' inofensivo de origin/main de siempre). Los 4 segmentos ya propuestos el 09-13 (1m LONG/SHORT, 5m LONG/SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG y 1m SHORT suman su DUODECIMA confirmacion (ambos practicamente sin cambio de delta), 5m LONG su NOVENA lectura seguida (delta baja un poco, 0.312->0.276, sigue muy lejos de cero) y 5m SHORT sigue siendo el efecto mas grande. HALLAZGO DEL DIA: 2m LONG suma su SEGUNDA lectura seguida certificando y se fortalece mucho (delta 0.074->0.153, CI90 limite inferior 0.005->0.079) -- un paso mas cerca de cumplir el criterio de '2-3 lecturas' para sumarse a la propuesta formal (vigilar una tercera lectura). 2m SHORT tiene su mejor lectura hasta ahora (limite inferior del CI90 0.031->0.039) pero se mantiene un dia mas como candidato debil antes de promoverlo. Vista actualizada: candidatos solidos sin cambio = 1m LONG, 1m SHORT, 5m LONG, 5m SHORT (los 4 ya propuestos); candidato experimental en camino de promocion = 2m LONG (segunda lectura, falta una tercera); candidato debil/al filo = 2m SHORT. Sin cambios de estado: sigue `proposed`, `changeDate` null, esperando que Jesus aplique el cambio en TradingView -- con 4 segmentos solidos y un quinto candidato acercandose (2m LONG en su segunda confirmacion), esta sigue siendo la evidencia mas fuerte acumulada hasta ahora para aplicar el cambio.",
      "2026-09-20 (domingo, REVISION SEMANAL, cierre de 2026-W38): primer fin de semana sin ningun archivo signals/outcomes nuevo desde que arranco el bus -- los +37 pares resueltos de hoy en todo el bus son TIMEOUT forzado de senales pendientes desde el viernes, sin trade real nuevo. Por eso esta medicion (que solo usa pares con outcome real) da exactamente los mismos numeros que ayer en los 6 segmentos RETEST: 1m LONG n=4078 delta=0.152, 1m SHORT n=2432 delta=0.153, 2m LONG n=1897 delta=0.153, 2m SHORT n=1092 delta=0.134, 5m LONG n=713 delta=0.276, 5m SHORT n=408 delta=0.49 -- NO cuenta como una lectura independiente nueva para ningun candidato (2m LONG sigue en su segunda lectura, todavia sin la tercera que pedia el criterio de promocion). Revision semanal completa en reviews/2026-week-38.md: se mantiene la propuesta formal de 4 segmentos (1m LONG/SHORT, 5m LONG/SHORT) sin cambios; 2m LONG y 2m SHORT siguen fuera, mas cerca que nunca pero sin una tercera lectura genuina.",
      "2026-09-21 (lunes, primer dia habil con dato nuevo genuino tras el fin de semana, +72 pares en todo el bus): 1m LONG y 1m SHORT suman su DECIMOTERCERA confirmacion sin ningun retroceso (n=4111 y n=2440). 5m LONG y 5m SHORT no tuvieron senales 5m nuevas hoy (5m LONG n identico 713, 5m SHORT +1 a 409) -- se mantienen en su novena/decima lectura respectivamente, sin avance ni retroceso. HALLAZGO PRINCIPAL: 2m LONG cumple hoy su TERCERA lectura consecutiva con dato genuinamente nuevo sosteniendo la certificacion (delta 0.153->0.151, CI90 practicamente sin cambio) -- se GRADUA de 'candidato experimental, vigilar una tercera lectura' a candidato de la propuesta formal, con la misma advertencia de historial volatil que se le puso a 5m LONG cuando se sumo el 09-13. La propuesta pasa de 4 a 5 segmentos: 1m LONG, 1m SHORT, 2m LONG, 5m LONG, 5m SHORT. 2m SHORT sigue sin alcanzar el mismo umbral (delta identico a ayer, limite inferior del CI90 practicamente sin moverse, 0.039->0.04) -- sigue fuera de la propuesta. Sin cambios de estado: sigue 'proposed', changeDate null, esperando que Jesus aplique el cambio en TradingView -- con 5 segmentos ahora con evidencia solida/experimental, esta es la evidencia acumulada mas fuerte y mas amplia hasta ahora para aplicar el cambio.",
      "2026-09-22 (martes, salto de dato grande y genuino: el bus asento de una vez el lote de +1027 outcomes de 2026-09-21, n total de pares resueltos 13204->14160): los 5 segmentos ya propuestos (1m LONG/SHORT, 2m LONG, 5m LONG/SHORT) se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG y 1m SHORT suman su DECIMOCUARTA/DECIMOQUINTA confirmacion (n=4493 y n=2611, deltas estables 0.132 y 0.142), 2m LONG suma su CUARTA lectura seguida (n=2081, delta 0.14, practicamente identico a ayer) y 5m LONG/SHORT tienen su primera lectura con dato nuevo desde el 09-21 y ambos se fortalecen (5m LONG delta 0.276->0.299, 5m SHORT delta 0.489->0.455 -- este ultimo baja un poco pero sigue siendo el efecto mas grande). HALLAZGO DEL DIA: 2m SHORT tiene su MEJOR lectura hasta ahora -- el limite inferior del CI90 sube de 0.04 a 0.057 (+42%), la subida mas grande en varias corridas -- pero todavia queda por debajo del rango tipico de graduacion de los 5 segmentos ya promovidos (~0.07-0.08 de limite inferior); se mantiene un dia mas como candidato debil/al filo, mas cerca que nunca. Nota en paralelo (no de este experimento, mismo mecanismo de SL): en INV/LONG (buy-ifvg.md) 1m certifica por primera vez a favor del SL de 3 capas (delta -0.323, CI90 no cruza cero) y 2m certifica por primera vez a favor del SL de vela-1 (delta +1.169, CI90 muy ancho, n=48 todavia chico) -- direcciones opuestas entre si, ninguno accionable todavia, pero primera senal estadistica real de esta medicion fuera de RETEST. Sin cambios de estado en este experimento: sigue 'proposed', changeDate null.",
      "2026-09-24 (jueves, dato nuevo genuino y parejo en los 6 segmentos, +189/+218/+137/+105/+50/+34 en n de 1m LONG/1m SHORT/2m LONG/2m SHORT/5m LONG/5m SHORT respectivamente): los 6 segmentos RETEST se mantienen TODOS con delta_beats_zero=true y sin ningun retroceso -- 1m LONG n=5025 delta=0.13 CI90=[0.076,0.188], 1m SHORT n=3032 delta=0.146 CI90=[0.071,0.226], 2m LONG n=2299 delta=0.153 CI90=[0.086,0.224], 2m SHORT n=1357 delta=0.138 CI90=[0.052,0.225] (segundo dia seguido sosteniendo la graduacion del 09-23, ya no es lectura de un solo dia), 5m LONG n=827 delta=0.297 CI90=[0.146,0.468], 5m SHORT n=498 delta=0.365 CI90=[0.091,0.706] (sigue siendo el efecto mas grande). Con las 6 ramas certificando de forma estable durante varias semanas seguidas y muestras que van de cientos a miles, este es el experimento mas maduro de todo el bus -- la evidencia acumulada ya no deja ningun segmento RETEST fuera de la propuesta. Sigue 'proposed', changeDate null, esperando que Jesus aplique el cambio de SL estructural (lg_slOrig, mecha del retest) en scalp_command.pine.",
      "2026-09-26 (sabado, dato de 2026-09-25 (viernes) llegando completo, +499/+436/+219/+214/+96/+77 en n de 1m LONG/1m SHORT/2m LONG/2m SHORT/5m LONG/5m SHORT respectivamente): los 6 segmentos RETEST se mantienen TODOS con delta_beats_zero=true y sin ninguna reversion -- 1m LONG n=5545 delta=0.148 CI90=[0.094,0.204] (se fortalece un poco de 0.13), 1m SHORT n=3468 delta=0.15 CI90=[0.083,0.222] (estable), 2m LONG n=2530 delta=0.154 CI90=[0.09,0.223] (estable), 2m SHORT n=1571 delta=0.151 CI90=[0.064,0.244] (se fortalece de 0.138), 5m LONG n=933 delta=0.273 CI90=[0.139,0.43] (baja un poco de 0.297, sigue muy lejos de cero), 5m SHORT n=575 delta=0.363 CI90=[0.097,0.653] (estable, sigue el efecto mas grande). Nota de metodo importante: el mismo dia, el E[R] crudo de SELL RETEST (1m/2m/5m SHORT) se debilito en las tres ramas en `by_tf_kind_side`/`segment_significance` (1m SHORT incluso perdio el CI90-fuera-de-cero por primera vez) -- pero el delta de ESTE experimento (SL estructural vs 3 capas) NO comparte esa debilidad, se mantiene igual o mejor en los tres TF SHORT. Confirma que este experimento mide algo distinto del nivel absoluto de E[R] (compara dos bases de SL con la misma entrada y mismo TP), y es una senal de robustez: la ventaja del SL estructural no depende de que el dia sea bueno o malo para SHORT. Incidente de repo distinto a los anteriores: el harness bloqueo `checkout -B`/`reset --hard` como destruccion local irreversible; resuelto sin perder nada con `git merge origin/main --allow-unrelated-histories -X theirs` (arbol final identico a origin/main). Mejora permanente a analyze.py: nueva funcion `shadow_weekly()` (desglosa el modo sombra por semana ISO) -- primer resultado, no de este experimento pero relacionado: el modo sombra actual (que todavia NO incorpora este SL estructural, sigue usando el stop de 3 capas del indicador) le gano al indicador crudo 3 semanas seguidas (W36-W38) pero perdio esta semana (W39 parcial) -- otro argumento a favor de aplicar el cambio de SL antes de subir de peldano. Sigue 'proposed', changeDate null.",
      "2026-09-27 (domingo, REVISION SEMANAL, cierre 2026-W39): primer dia sin trade nuevo desde el cambio (aplicado ayer sabado, fin de semana sin sesion CME) -- prediction_scoreboard confirma appliedDate=2026-09-26 en las 6 lineas de predictions.jsonl (4 de W37 + 2 nuevas de 2m LONG/SHORT anadidas hoy), todas en status 'accruing' con afterN=0, como se esperaba. Antes del cambio, los 6 segmentos RETEST cerraron su ultima lectura in-sample con delta_orig_minus_layer/CI90: 1m LONG 0.148 [0.094,0.204] n=5545, 1m SHORT 0.15 [0.083,0.222] n=3468, 2m LONG 0.154 [0.09,0.223] n=2530, 2m SHORT 0.151 [0.064,0.244] n=1571, 5m LONG 0.273 [0.139,0.43] n=933, 5m SHORT 0.363 [0.097,0.653] n=575 -- sin ninguna reversion en ninguno de los 6 en toda su historia de confirmaciones. sl_origin_vs_layer sigue corriendo la medicion paralela (rMultiple=3-capas, rOrig=mecha) independiente del cambio real en TradingView, asi que se puede seguir comparando ambos stops aunque el SL real ya cambio -- util para verificar que el efecto medido en produccion coincide con lo medido in-sample. Primer chequeo real: esperar hasta que haya trades del lunes 2026-09-28 en adelante (afterN>=20 minimo, 40 para no marcarlo 'experimental' segun agent-instructions.md) antes de poder comparar antes/despues real. Nada que decidir hoy sobre este experimento mas alla de seguir vigilando el scoreboard cada corrida.",
      "2026-09-28 (lunes, primer dia con trades reales bajo el SL nuevo -- el cambio se aplico el sabado 2026-09-26 y no hubo sesion CME el domingo): se encontro y arreglo un bug en analyze.py -- eval_experiments() solo calculaba beforeN/afterN/verdict para status 'running'/'proposed', nunca para 'applied'. Como este experimento paso a 'applied' el 09-26, se habria quedado sin medicion antes/despues PARA SIEMPRE (el verdict confirmed/rejected que este mismo archivo lleva semanas anticipando nunca se habria calculado). Se agrego 'applied' a la lista de estados elegibles (mejora permanente, commit de hoy). Con el fix, el agregado (segment={'kind':'RETEST'}, sin desglose tf/side) da beforeN=17449 afterN=89 expR 0.057->0.225, verdict mecanico 'confirmed' (delta=0.168>0.05, afterN=89>=40) y dispara la alerta EXPERIMENTO CONFIRMADO en report.md de hoy. NO SE TOMA ESE VERDICT AL PIE DE LA LETRA: el desglose real por segmento en prediction_scoreboard (las lineas de predictions.jsonl por tf/side) muestra un primer dia volatil y contradictorio -- 1m LONG (n=37, la rama con mas historia e in-sample mas estable de las seis) sale con realDeltaER=-0.055, DIRECCION CONTRARIA a lo predicho (+0.152); 1m SHORT (n=33) sale con realDeltaER=+0.567, mas de 4x lo predicho (+0.143); 2m LONG/SHORT y 5m LONG/SHORT todavia con afterN de un solo digito (1, 3, 6, 9), sin ninguna base para leer direccion. Esto es exactamente el patron que el propio historial in-sample de este experimento documento una y otra vez ('lecturas con n en los cientos bajos pueden sobrestimar el efecto') pero mas extremo (aqui n esta en las decenas, no en los cientos, y es UN SOLO DIA). DECISION: el status se mantiene en 'applied', NO se sube a 'confirmed' todavia pese al verdict mecanico de hoy -- se sigue vigilando dia a dia hasta que cada segmento (no el agregado) junte afterN>=40 y, per agent-instructions.md, se vea la misma direccion sostenida 2 semanas seguidas antes de tratarlo como resultado real. Revisar de nuevo mañana con el segundo dia de dato real.",
      "2026-09-29 (martes, tercer dia real de trading bajo el SL nuevo desde el sabado 09-26): salto grande de afterN agregado (89->999) al asentarse mas dato real. El verdict mecanico de eval_experiments() sigue en 'confirmed' a nivel agregado (beforeN=17367 afterN=999, expR 0.056->0.114) pero el desglose por segmento en prediction_scoreboard (predictions.jsonl) ya tiene muestra suficiente para desconfiar del agregado, NO para confirmarlo: de los 6 segmentos propuestos, SOLO 2 van en la direccion predicha -- 1m SHORT (n=454) realDeltaER=+0.16 vs +0.143 predicho (acierta) y 2m SHORT (n=164) realDeltaER=+0.354 vs +0.151 predicho (acierta, sobra) -- mientras que LOS OTROS 4 SALEN EN DIRECCION CONTRARIA: 1m LONG (n=199) realDeltaER=-0.174 vs +0.152 predicho, 2m LONG (n=83) realDeltaER=-0.097 vs +0.154 predicho, 5m LONG (n=44) realDeltaER=-0.228 vs +0.255 predicho, 5m SHORT (n=55) realDeltaER=-0.277 vs +0.567 predicho. hit_direction_rate del prediction_scoreboard cae a 33.3% (2/6) con mae_deltaER=0.354, la peor calificacion del scoreboard hasta la fecha. Es el patron opuesto al que domina el resto del bus (donde SHORT y LONG solian moverse parecido): aqui el SL nuevo parece estar ayudando en SHORT (1m y 2m, n ya no chico) y perjudicando en LONG (los 3 TF, incluido 1m LONG que era la rama con mas historia in-sample de las seis) mas 5m SHORT (n todavia chico, 55, tratar con cautela). DECISION: el estado se mantiene en 'applied', el verdict mecanico 'confirmed' del agregado NO se toma al pie de la letra y no se reporta a Jesus como exito -- se recomienda EXPLICITAMENTE seguir vigilando dia a dia sin tocar nada mas (ni revertir ni reforzar) hasta que: (a) cada segmento LONG junte afterN>=40 (1m y 2m ya lo cumplen hoy, 5m LONG con 44 esta al filo) y (b) se sostenga la misma direccion 2 semanas seguidas por segmento, per agent-instructions.md. Si el patron LONG-negativo se sostiene con mas muestra en las proximas corridas (en particular 1m LONG, que ya tiene n=199 y viene de ser el segmento mas maduro y estable de toda la evidencia in-sample), ese es el escenario que justificaria proponer revertir el SL a 3 capas SOLO en el lado LONG de RETEST en la revision semanal del domingo 2026-10-04, dejando SHORT con el SL nuevo. No se propone ese revert todavia porque 3 dias (con un fin de semana sin sesion CME de por medio) es muy poca muestra temporal para distinguir una reversion real de ruido post-cambio -- ver el propio historial de este experimento (in-sample) documentando varias veces que lecturas con n en las decenas/cientos bajos sobrestiman el efecto en cualquier direccion."
    ],
    "appliedNote": "2026-09-26: aplicado en scalp_command.pine (input sc_sl_retest_basis, default 'Auto (como se midio)'): en RETEST el SL real pasa a la mecha de la vela del retest; 1m SHORT suma la vela previa (retestBar2), igual que la medicion paralela. Base: los 6 segmentos RETEST certifican con CI90 > 0 (n=11273, E[R] 0.238 vs 0.065). El tier se sigue calculando con el stop de 3 capas. El feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig, asi que sl_origin_vs_layer sigue siendo la vigilancia. Rige en cada grafico desde que Jesus re-pega scalp_cc_FULL_for_tradingview.pine. Revertir = poner la base en '3 capas'.",
    "beforeN": 17241,
    "afterN": 1939,
    "before": {
      "n": 17241,
      "wrTP1": 45.9,
      "nSL": 7929,
      "nTO": 1403,
      "expR": 0.055,
      "pf": 1.11,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.0
    },
    "after": {
      "n": 1939,
      "wrTP1": 50.2,
      "nSL": 876,
      "nTO": 90,
      "expR": 0.11,
      "pf": 1.24,
      "mfe_p25": 9.0,
      "mfe_p50": 19.0,
      "mfe_p75": 44.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 35.5
    },
    "verdict": "confirmed"
  },
  {
    "id": "sc-min-rr-cut-2026-09-20",
    "status": "proposed",
    "hypothesis": "Subir sc_min_rr (o sc_aplus_rr) para exigir mas RR desde el origen de la senal sube el E[R] en RETEST porque ataca directo la causa de SL dominante 'RR-bajo' (37-38% de las perdidas en RETEST toda la vida del bus). Contrapartida esperada: baja el win rate (menos senales pasan el filtro, y las que pasan tienen el TP mas lejos del SL) pero las que sobreviven pagan mas R, y el neto deberia mejorar -- misma logica que el experimento sl-retest-wick pero del lado de la ENTRADA (que senales se toman), no de la gestion (donde se pone el stop).",
    "param": "sc_min_rr / sc_aplus_rr",
    "from": "sin piso explicito medido hoy (rr1 crudo del indicador)",
    "to": "candidatos a evaluar: 1.2 / 1.3 / 1.5 / 2.0 (ver evidencia por segmento)",
    "changeDate": null,
    "segment": {
      "kind": "RETEST"
    },
    "targetMetric": "expR",
    "minAfterN": 40,
    "evidence": {
      "source": "nuevo corte permanente en analyze.py de hoy (rr1_threshold_cut): por cada segmento tf/kind/side de RETEST, compara el E[R]/WR/PF/CI90 del segmento completo contra el subconjunto que solo toma senales con rr1>=X (contrafactual de entrada, no cambia gestion ni SL). Llena el hueco que la revision de 2026-week-37 dejo pendiente ('no hay todavia un corte contrafactual de rr1>=X').",
      "asOf": "2026-09-20 (domingo), primera lectura, dato identico al de ayer (fin de semana sin trade nuevo, ver nota de sl-retest-wick arriba).",
      "1m_short": {
        "baseline_n": 2998,
        "baseline_expR": 0.051,
        "rr1_ge_1_2_n": 1219,
        "rr1_ge_1_2_expR": 0.101,
        "ci90": [
          0.026,
          0.181
        ],
        "wr_baseline": 45.8,
        "wr_cut": 28.4
      },
      "2m_short": {
        "baseline_n": 1267,
        "baseline_expR": 0.099,
        "rr1_ge_1_2_n": 457,
        "rr1_ge_1_2_expR": 0.2,
        "ci90": [
          0.068,
          0.328
        ],
        "wr_baseline": 50.0,
        "wr_cut": 31.9
      },
      "5m_long": {
        "baseline_n": 767,
        "baseline_expR": 0.183,
        "rr1_ge_1_2_n": 276,
        "rr1_ge_1_2_expR": 0.408,
        "ci90": [
          0.231,
          0.582
        ],
        "wr_baseline": 53.8,
        "wr_cut": 38.0
      },
      "1m_long": {
        "baseline_n": 4695,
        "baseline_expR": 0.039,
        "rr1_ge_1_2_n": 1886,
        "rr1_ge_1_2_expR": 0.041,
        "ci90": "practicamente sin cambio vs baseline, efecto plano/nulo en este segmento -- no generalizar del resto"
      },
      "nota": "1m SHORT, 2m SHORT y 5m LONG muestran una relacion consistente: subir el piso de rr1 sube E[R] y PF de forma monotona-ish con CI90 que no cruza cero en ningun escalon (aunque son subconjuntos anidados, no lecturas independientes -- no comparar los CI90 entre escalones como si fueran experimentos separados). 1m LONG y 2m LONG NO muestran el mismo efecto (practicamente plano). Esto es coherente con el coeficiente mas grande del modelo P(TP1) (rr1, peso -1.185): mas RR exigido = menos probabilidad de tocar TP1, pero el modelo no dice si el NETO en R mejora o empeora, que es justo lo que mide este corte."
    },
    "next_steps": [
      "2026-09-20: primera lectura, in-sample, un solo dia de dato (identico a ayer por el fin de semana). NO proponer un valor concreto de sc_min_rr todavia -- falta: (a) walk_forward.ready (solo 3 semanas de historial), (b) que el patron se sostenga con dato genuinamente nuevo en corridas futuras, (c) decidir el punto exacto del trade-off WR-vs-E[R] que Jesus esta dispuesto a aceptar (WR cae de ~46-54% a ~28-38% en los tres segmentos donde el efecto es real).",
      "Vigilar en corridas futuras: si 1m SHORT, 2m SHORT y 5m LONG siguen mostrando el mismo patron con muestra nueva, y si 1m LONG / 2m LONG se mantienen planos (en cuyo caso la regla seria 'sc_min_rr mas alto solo para esos 3 segmentos', no un cambio global).",
      "Cuando haya 2-3 lecturas independientes seguidas confirmando: sumar a la propuesta formal de la revision semanal con predictedDeltaER en predictions.jsonl, igual que se hizo con sl-retest-wick.",
      "2026-09-21 (lunes, segunda lectura, primera con dato genuinamente nuevo desde que se anadio el corte el 09-20): el patron se mantiene igual que el domingo -- 1m SHORT, 2m SHORT y 5m LONG siguen mostrando que subir el piso de rr1 sube E[R] y PF de forma consistente con CI90 que no cruza cero; 1m LONG y 2m LONG siguen practicamente planos. Todavia in-sample, todavia sin walk_forward.ready con suficientes semanas -- sigue sin proponerse un valor concreto de sc_min_rr. Vigilar 2-3 lecturas mas con dato nuevo antes de sumarlo a una propuesta formal.",
      "2026-09-22 (martes, tercera lectura, con el lote grande de dato nuevo genuino del dia -- +1027 outcomes en todo el bus): 1m SHORT (cut>=1.2 n=1273 expR=0.124 CI90=[0.043,0.202]), 2m SHORT (n=475 expR=0.176 CI90=[0.051,0.297]) y 5m LONG (n=286 expR=0.45 CI90=[0.282,0.626]) siguen mostrando el mismo patron monotono, sin reversion en la tercera lectura. CAMBIO A VIGILAR: 1m LONG, que llevaba dos lecturas practicamente plano, hoy muestra un CI90 que ya no cruza cero (n=2055 expR=0.108 CI90=[0.051,0.167] vs baseline expR=0.075) -- todavia mas debil que los otros tres segmentos, pero ya no es claramente 'sin efecto'; 2m LONG sigue el mas debil/plano (n=850 expR=0.068 CI90=[-0.027,0.163], cruza cero). walk_forward.ready=true desde hace unos dias pero este corte especifico (rr1_threshold_cut) sigue sin evaluarse contra el split OOS -- pendiente antes de proponer un valor concreto. Sigue sin proponerse sc_min_rr en la revision semanal (la ultima fue el 09-20); revisar el patron de 1m LONG una vez mas el domingo antes de decidir si se suma a la propuesta.",
      "2026-09-24 (jueves): sin corte nuevo calculado explicitamente hoy en esta nota (ver report.json.rr1_threshold_cut para las cifras crudas del dia), el patron narrado el 09-22 se mantiene sin reversion conocida: 1m SHORT, 2m SHORT y 5m LONG siguen siendo los tres segmentos donde subir el piso de rr1 sube E[R]/PF de forma monotona con CI90 que no cruza cero; 1m LONG sigue mostrando un efecto mas debil que los otros tres pero ya no claramente plano (ver lectura del 09-22, CI90 dejo de cruzar cero en el corte 1.2); 2m LONG sigue siendo el mas plano/cruza cero. Sigue pendiente evaluar este corte contra el split walk-forward OOS (walk_forward.ready=true desde hace dias, pero el corte especifico rr1_threshold_cut todavia no se compara contra W38-W39) antes de proponer un valor concreto de sc_min_rr en la revision semanal del domingo 2026-09-27.",
      "2026-09-26 (sabado, cuarta lectura con corte recalculado, dato de 2026-09-25 completo): el patron se debilita en el corte 1.2 en varios segmentos a la vez, coincidiendo con la debilidad general de E[R] crudo en SELL RETEST que se vio hoy en todo el bus (ver playbooks) -- 1m SHORT (n=1638 expR=0.073 CI90=[0.007,0.138] vs baseline 0.043) sigue sin cruzar cero pero mas cerca que el 09-22 (era 0.124); 2m SHORT (n=646 expR=0.131 CI90=[0.035,0.235] vs baseline 0.097) sigue sin cruzar cero pero tambien mas debil que el 09-22 (0.176); 5m LONG (n=343 expR=0.375 CI90=[0.217,0.538] vs baseline 0.163) SIGUE siendo el mas fuerte y estable de los tres, practicamente igual al 09-22 (0.45) -- el unico de los tres candidatos que no comparte la debilidad de hoy. 1m LONG vuelve a mostrar un CI90 que cruza cero (n=2568 expR=0.055 CI90=[0.003,0.107] vs baseline 0.056, practicamente identico -- efecto nulo, revierte la lectura mas fuerte del 09-22) y 2m LONG sigue el mas plano/cruza cero (n=1026 expR=0.024 CI90=[-0.062,0.106]). Primera lectura separada de 5m SHORT (antes no se reportaba en esta nota): n=233 expR=0.138 CI90=[-0.044,0.326] vs baseline 0.106 -- cruza cero, no se suma como cuarto candidato todavia. Con dos de los tres candidatos (1m SHORT, 2m SHORT) debilitandose el mismo dia que el E[R] crudo de SHORT en general, hay que esperar el dato del lunes antes de decidir si es ruido de un viernes flojo o un cambio real del patron -- no se suma ni se descarta ningun segmento hoy. Sigue sin proponerse un valor concreto de sc_min_rr; sigue pendiente evaluar contra el split walk-forward OOS.",
      "2026-09-27 (domingo, REVISION SEMANAL): se agrego hoy a analyze.py el corte pendiente contra el split walk-forward (rr1_threshold_cut_oos, nueva funcion permanente) que este experimento llevaba pidiendo desde el 2026-09-22 ('pendiente evaluar este corte contra el split walk-forward OOS'). Resultado con testWeeks W38-W39 (mismo split que walk_forward.testWeeks): SOLO 5m LONG confirma fuera de muestra de forma clara -- baseline test n=544 expR=0.148 CI90=[0.056,0.247]; cortes 1.2/1.3/1.5 SUBEN el E[R] a 0.35-0.37 con CI90 que NO cruza cero (n=141-182, PF hasta 1.66) -- el patron in-sample se replica limpio fuera de muestra. Los otros dos candidatos in-sample (1m SHORT, 2m SHORT) NO se confirman: 1m SHORT sube de expR=0.052 a 0.073-0.094 con los cortes pero el CI90 sigue cruzando cero en el test set aislado (n mas chico, 425-836, falta potencia, no se descarta, solo no certifica todavia); 2m SHORT de hecho SE REVIERTE en el test set -- baseline test expR=0.058 (ya al filo, CI90=[-0.001,0.118]) y los 4 cortes dan expR NEGATIVO (-0.02 a -0.162), el corte 2.0 con CI90=[-0.382,0.05] casi enteramente del lado negativo. 1m LONG (que nunca certifico in-sample con consistencia) tambien se revierte en el test set: baseline test ya positivo (0.091) y los 4 cortes BAJAN el E[R] de forma monotona hasta 0.036 -- confirma que subir el piso de rr1 en 1m LONG no ayuda, va en contra. DECISION: no se propone sc_min_rr global. Se propone en la revision semanal de hoy (reviews/2026-week-39.md) SOLO un cambio experimental y acotado a 5m/RETEST/LONG (candidato a sc_aplus_rr o un filtro nuevo especifico de ese segmento, ya que sc_min_rr es global a todos los tf/side y subirlo global arriesga empeorar 1m LONG y 2m SHORT segun este mismo corte). Marcar 2m SHORT como alerta de metodo: un patron en apariencia solido in-sample (3+ lecturas consistentes) no sobrevivio el primer chequeo OOS real -- tratarlo como caso de estudio de por que el walk-forward es el numero que cuenta, no el contrafactual in-sample.",
      "2026-09-29 (martes): el walk-forward testWeeks avanzo de [W38,W39] a [W39,W40] (W39 ya cerro, W40 es la semana en curso) y con la ventana nueva el unico candidato que habia confirmado OOS limpio el 09-27 (5m/RETEST/LONG) PIERDE la certificacion: baseline test n=287 expR=0.084 CI90=[-0.046,0.215] (cruza cero, antes n=544 expR=0.148 CI90=[0.056,0.247] no cruzaba) y los cortes 1.2/1.3 salen con CI90 igual de anchos y cruzando cero (ej. 1.2: expR=0.161 CI90=[-0.175,0.527]) -- el patron todavia apunta en la misma direccion (subir el piso de rr1 sube el E[R] observado) pero ya no certifica fuera de muestra con esta ventana mas chica (W40 apenas tiene unos dias de dato). No es una reversion de signo, es perdida de potencia estadistica al cambiar de ventana de test -- vigilar si vuelve a certificar cuando W40 cierre con mas muestra. Sigue sin proponerse ningun valor concreto de sc_aplus_rr; la linea 7 de predictions.jsonl sigue sin appliedDate."
    ],
    "beforeN": 19180,
    "afterN": 0,
    "before": {
      "n": 19180,
      "wrTP1": 46.3,
      "nSL": 8805,
      "nTO": 1493,
      "expR": 0.061,
      "pf": 1.13,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 33.2
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
    "date": "2026-09-30",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-29T19:08:15-05:00",
    "schema": "sa-plan-2",
    "cleanest": "NQ",
    "focus": {
      "sym": "NQ",
      "verdict": "WAIT",
      "window": "17:00-00:00 CT",
      "setup": {
        "es": "pullback al cluster POC/EMA/VWAP 30588-30621 con FVG 15m 30570-30584.5 (peso 1) para continuar largo",
        "en": "POC/EMA/VWAP cluster pullback 30588-30621 with a 15m FVG 30570-30584.5 (weight 1) to continue long"
      },
      "trigger": {
        "es": "reclamo con FVG de 15m 30570-30584.5 o 30505.5-30524.75 y cierre 5m de vuelta sobre 30610; o barrido de 30575 con reclaim",
        "en": "15m FVG reclaim at 30570-30584.5 or 30505.5-30524.75 with a 5m close back above 30610; or a 30575 sweep with reclaim"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 30545 (IB bajo de hoy)",
        "en": "5m close sustained below 30545 (today's IB low)"
      },
      "note": {
        "es": "Ayer: overtrade + revenge + round-trip juntos, 71% de los trades contra el sesgo del plan -- si hoy pierdes 2 seguidas, cierra la plataforma. Desde la reapertura el precio nunca bajo al cluster POC/EMA 30588-621: corrio directo hacia el ONH/IBH 30725.5 sin ofrecer la entrada guionada. Sigue sin gatillo confirmado y sin tocar la invalidacion 30826.75; no persigas los maximos, espera el pullback o un rechazo real, y ojo con el IPC de Australia a las 20:30 CT.",
        "en": "Yesterday: overtrade, revenge and a round-trip all together, 71% of trades against the plan's bias -- if you take 2 losses in a row today, close the platform. Since the reopen price never dropped into the POC/EMA cluster 30588-621: it ran straight toward the ONH/IBH 30725.5 without offering the scripted entry. Still no confirmed trigger and the 30826.75 invalidation remains untouched; don't chase the highs, wait for the pullback or a real rejection, and watch the Australian CPI at 20:30 CT."
      }
    },
    "summary": {
      "es": [
        "Alarma: GC acierto de escenario A en 20 dias 29% (n=42), no te cases con el camino A.",
        "NQ: WAIT. Desde la reapertura extendio directo hacia el ONH/IBH 30725.5 (a 12pts de PDH) sin ofrecer el pullback guionado a POC/EMA 30588-621; el reinicio bajista narrativo sigue sin invalidar (30826.75 intacto).",
        "ES: WAIT. Extendio hasta tocar el VAH (0tk) y el ONH 3 veces sin rechazo; el conflicto de marcos sigue abierto, la invalidacion 7707.25 sigue lejos.",
        "GC: AVOID. Sigue pegado al techo de la zona 4205-4218 sin el cierre 5m que active el corto; el estiramiento de la nueva sesion se reinicio (1.1A) pero el marco de fondo bajista no confirma el giro.",
        "YM: AVOID. Corrio directo de 51758 a 51830 sin volver a probar 51744; ya supero el primer objetivo de escala (51804 VAH), estirado 2.8 ATR de sesion.",
        "CL: AVOID. Practicamente plano (88.98 -> 89.08); la zona de rebot
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 8138,
  "by_verdict": {
    "AVOID": {
      "n": 1613,
      "wrTP1": 45.5,
      "nSL": 803,
      "nTO": 76,
      "expR": 0.017,
      "pf": 1.03,
      "mfe_p25": 8.0,
      "mfe_p50": 16.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.1
    },
    "GO": {
      "n": 980,
      "wrTP1": 49.1,
      "nSL": 406,
      "nTO": 93,
      "expR": 0.141,
      "pf": 1.32,
      "mfe_p25": 12.25,
      "mfe_p50": 28.0,
      "mfe_p75": 53.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 29.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -18.0,
      "revAfterSL_rate": 42.4
    },
    "WAIT": {
      "n": 5545,
      "wrTP1": 47.8,
      "nSL": 2510,
      "nTO": 387,
      "expR": 0.068,
      "pf": 1.14,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -15.0,
      "revAfterSL_rate": 35.1
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": 0.017,
      "ci90": [
        -0.035,
        0.071
      ],
      "p_mean_le_0": 0.295,
      "n": 1574
    },
    "GO": {
      "expR": 0.141,
      "ci90": [
        0.077,
        0.21
      ],
      "p_mean_le_0": 0.0,
      "n": 918
    },
    "WAIT": {
      "expR": 0.068,
      "ci90": [
        0.042,
        0.098
      ],
      "p_mean_le_0": 0.0,
      "n": 5341
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1613,
      "wrTP1": 45.5,
      "nSL": 803,
      "nTO": 76,
      "expR": 0.017,
      "pf": 1.03,
      "mfe_p25": 8.0,
      "mfe_p50": 16.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -13.0,
      "revAfterSL_rate": 34.1
    },
    "GO_or_WAIT": {
      "n": 6525,
      "wrTP1": 48.0,
      "nSL": 2916,
      "nTO": 480,
      "expR": 0.079,
      "pf": 1.17,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 42.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 36.1
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": 0.017,
      "ci90": [
        -0.035,
        0.071
      ],
      "p_mean_le_0": 0.295,
      "n": 1574
    },
    "GO_or_WAIT": {
      "expR": 0.079,
      "ci90": [
        0.055,
        0.106
      ],
      "p_mean_le_0": 0.0,
      "n": 6259
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 16,
        "wrTP1": 43.8,
        "nSL": 7,
        "nTO": 2,
        "expR": -0.077,
        "pf": 0.82,
        "mfe_p25": 5.0,
        "mfe_p50": 8.0,
        "mfe_p75": 29.25,
        "winnerMAE_p75": 0.0,
        "winnerMAE_p90": 1.6000000000000014,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 28.6
      },
      "GO": {
        "n": 10,
        "wrTP1": 60.0,
        "nSL": 3,
        "nTO": 1,
        "expR": 0.032,
        "pf": 1.1,
        "mfe_p25": 23.0,
        "mfe_p50": 28.0,
        "mfe_p75": 31.0,
        "winnerMAE_p75": 15.5,
        "winnerMAE_p90": 30.0,
        "loserMFEbeforeSL_p50": 2.0,
        "bars_win_p50": 6.5,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -54.0,
        "revAfterSL_rate": 33.3
      },
      "WAIT": {
        "n": 71,
        "wrTP1": 42.3,
        "nSL": 32,
        "nTO": 9,
        "expR": -0.053,
        "pf": 0.89,
        "mfe_p25": 7.5,
        "mfe_p50": 17.0,
        "mfe_p75": 28.5,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 24.1,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 15.6
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 23,
        "wrTP1": 30.4,
        "nSL": 14,
        "nTO": 2,
        "expR": -0.43,
        "pf": 0.32,
        "mfe_p25": 6.5,
        "mfe_p50": 13.5,
        "mfe_p75": 21.75,
        "winnerMAE_p75": 5.0,
        "winnerMAE_p90": 7.200000000000001,
        "loserMFEbeforeSL_p50": 10.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 14.3
      },
      "WAIT": {
        "n": 87,
        "wrTP1": 48.3,
        "nSL": 35,
        "nTO": 10,
        "expR": -0.021,
        "pf": 0.95,
        "mfe_p25": 7.0,
        "mfe_p50": 19.5,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 17.75,
        "winnerMAE_p90": 29.599999999999994,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 25.7
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 928,
        "wrTP1": 45.5,
        "nSL": 478,
        "nTO": 28,
        "expR": -0.04,
        "pf": 0.92,
        "mfe_p25": 7.0,
        "mfe_p50": 14.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 31.0
      },
      "GO": {
        "n": 579,
        "wrTP1": 48.7,
        "nSL": 262,
        "nTO": 35,
        "expR": 0.12,
        "pf": 1.26,
        "mfe_p25": 10.0,
        "mfe_p50": 25.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -18.0,
        "revAfterSL_rate": 40.5
      },
      "WAIT": {
        "n": 2825,
        "wrTP1": 48.9,
        "nSL": 1249,
        "nTO": 194,
        "expR": 0.103,
        "pf": 1.22,
        "mfe_p25": 7.0,
        "mfe_p50": 17.0,
        "mfe_p75": 38.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 34.3
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 646,
        "wrTP1": 46.1,
        "nSL": 304,
        "nTO": 44,
        "expR": 0.118,
        "pf": 1.24,
        "mfe_p25": 9.0,
        "mfe_p50": 20.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 13.75,
        "winnerMAE_p90": 28.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 40.1
      },
      "GO": {
        "n": 387,
        "wrTP1": 49.1,
        "nSL": 140,
        "nTO": 57,
        "expR": 0.17,
        "pf": 1.41,
        "mfe_p25": 15.0,
        "mfe_p50": 33.0,
        "mfe_p75": 56.0,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 30.19999999999999,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 46.4
      },
      "WAIT": {
        "n": 2562,
        "wrTP1": 46.6,
        "nSL": 1194,
        "nTO": 174,
        "expR": 0.037,
        "pf": 1.08,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 26.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 36.6
      }
    }
  },
  "note": "join por (fecha, killzone->sesion SA asia/london/ny, simbolo); 'Sin KZ' no cruza (sin sesion SA equivalente); veredicto parseado del texto libre del resumen SA (linea 'SYM: ...'), no de un campo estructurado; by_verdict_ci90/avoid_vs_rest_ci90 = bootstrap 90% CI de E[R] (null si n<8); by_kind_side = mismo cruce desglosado por kind/side (solo celdas con n>=5)."
}
```

## Modo sombra (peldano 0->1, gate en execution-ladder.md)
```json
{
  "rule": {
    "version": 2,
    "definedAt": "2026-09-27",
    "criteria": {
      "kind": [
        "RETEST"
      ],
      "tf_side": [
        "1/LONG",
        "1/SHORT",
        "2/LONG",
        "2/SHORT",
        "5/LONG",
        "5/SHORT"
      ],
      "excludeSaVerdict": [
        "AVOID"
      ]
    },
    "rationale": "kind=RETEST (prioridad 1; INV no tiene ningun segmento con survives_fdr10=true todavia). REVISION SEMANAL 2026-09-27 (v1->v2): v1 (2026-09-20) limitaba tf_side a 4 segmentos (1/LONG, 1/SHORT, 2/SHORT, 5/LONG) porque 2m LONG y 5m SHORT todavia cruzaban/rozaban cero en ese momento. Desde entonces segment_significance certifico ambos de forma sostenida durante varias corridas seguidas (2m LONG desde 2026-09-18, 5m SHORT desde antes) sin ninguna reversion, y hoy los 6 segmentos RETEST (1m/2m/5m x LONG/SHORT) tienen survives_fdr10=true con CI90 que no cruza cero -- ver segment_significance de hoy. Se amplia tf_side a los 6 segmentos certificados; la justificacion vieja de v1 (excluir 2m LONG/5m SHORT por CI90 rozando cero) ya no la sostiene el dato, quedaba pendiente de esta revision semanal desde 2026-09-24 (ver playbook buy-retest.md, historico). Se excluyen senales del dia/sesion en un instrumento con veredicto Session Analyst=AVOID: avoid_vs_rest_ci90.AVOID no es significativo (p_mean_le_0 alto) mientras GO y WAIT si lo son (session_analyst_cross). SL/objetivo = el mismo del indicador (3 capas); el SL estructural de experiments.json (sl-retest-wick) SE APLICO en TradingView el 2026-09-26 pero el feed sigue registrando el 3-capas como rMultiple (el SL real ya cambio, la medicion paralela sigue corriendo en sl_origin_vs_layer) -- no se incorpora a la sombra hasta que haya muestra post-cambio suficiente para decidir si usar rOrig en vez de rMultiple."
  },
  "shadow": {
    "n": 17606,
    "wrTP1": 46.4,
    "nSL": 8023,
    "nTO": 1421,
    "expR": 0.064,
    "pf": 1.13,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 33.1
  },
  "shadow_ci90": {
    "expR": 0.064,
    "ci90": [
      0.05,
      0.08
    ],
    "p_mean_le_0": 0.0,
    "n": 16845
  },
  "raw_indicator": {
    "n": 19180,
    "wrTP1": 46.3,
    "nSL": 8805,
    "nTO": 1493,
    "expR": 0.061,
    "pf": 1.13,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 25.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 33.2
  },
  "raw_indicator_ci90": {
    "expR": 0.061,
    "ci90": [
      0.046,
      0.077
    ],
    "p_mean_le_0": 0.0,
    "n": 18381
  },
  "tier_ap_b_only": {
    "n": 9786,
    "wrTP1": 44.0,
    "nSL": 4667,
    "nTO": 816,
    "expR": 0.067,
    "pf": 1.13,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 5.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -15.0,
    "revAfterSL_rate": 30.9
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.067,
    "ci90": [
      0.045,
      0.089
    ],
    "p_mean_le_0": 0.0,
    "n": 9379
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```

## Modo sombra por semana (gate: shadow_beats_raw 3 semanas seguidas, n>=60)
```json
{
  "2026-W36": {
    "shadow_n": 2704,
    "shadow_expR": -0.03,
    "raw_n": 2784,
    "raw_expR": -0.022,
    "shadow_beats_raw": false
  },
  "2026-W37": {
    "shadow_n": 4111,
    "shadow_expR": 0.088,
    "raw_n": 4856,
    "raw_expR": 0.073,
    "shadow_beats_raw": true
  },
  "2026-W38": {
    "shadow_n": 4031,
    "shadow_expR": 0.11,
    "raw_n": 4517,
    "raw_expR": 0.097,
    "shadow_beats_raw": true
  },
  "2026-W39": {
    "shadow_n": 5085,
    "shadow_expR": 0.051,
    "raw_n": 5161,
    "raw_expR": 0.048,
    "shadow_beats_raw": true
  },
  "2026-W40": {
    "shadow_n": 1675,
    "shadow_expR": 0.094,
    "raw_n": 1862,
    "raw_expR": 0.104,
    "shadow_beats_raw": false
  }
}
```
