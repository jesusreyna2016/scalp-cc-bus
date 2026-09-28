# Scalp CC · report 2026-09-28T01:28Z
- signals=18000 outcomes=17200 pares_resueltos=17993 pendientes=7 huerfanos=39

## ⚠ ALERTAS (llevar al frente del resumen)
- EXPERIMENTO CONFIRMADO: sl_basis_retest 3-capas (sc_slbuf x ATR1m + piso sc_floor_atr5 + techo sc_cap_atr5 / sc_cap_adr)->mecha de la vela del retest (lg_slOrig con slBasis=retestBar / retestBar2, crudo) (sl-retest-wick-2026-09-03).
- GATE: el segmento objetivo cumple el gate de ejecucion. Revisar escalera.
- SL: SL en la mecha de la vela del retest BATE al de 3 capas fuera de ruido (E[R] 0.239 vs 0.065, delta 0.174 CI90 [0.135, 0.213], n 11325). Candidato para experiments.json + revision semanal.
- SL: SL en la mecha del retest + vela previa (1m short) BATE al de 3 capas fuera de ruido (E[R] 0.184 vs 0.041, delta 0.143 CI90 [0.078, 0.216], n 3379). Candidato para experiments.json + revision semanal.
- SESSION ANALYST: senales scalp con veredicto SA=GO rinden MEJOR de forma no-random (E[R] 0.187 CI90 [0.119, 0.258], n 841). Consistente con la hipotesis original de agent-instructions.md.
- SESSION ANALYST: senales scalp con veredicto SA=WAIT rinden MEJOR de forma no-random (E[R] 0.048 CI90 [0.02, 0.077], n 4391). Consistente con la hipotesis original de agent-instructions.md.

- E[R] global: {"expR": 0.059, "ci90": [0.044, 0.075], "p_mean_le_0": 0.0, "n": 17161}
- gate ejecucion: {"readyForLive": true, "segment": "5m/RETEST/LONG", "note": "n>=100 & E[R]>0 & PF>=1.3 & WR>=50 en un segmento tf/kind/side. Falta ademas: estabilidad 3 semanas + causa de SL dominante mitigada (lo valida el agente)."}

## Por tf / kind / side
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| 1m/INV/LONG | 163 | 44.2 | 0.182 | 1.41 | 67 | 14.0 | 12.0 | 17.9 |
| 1m/INV/SHORT | 136 | 47.8 | 0.046 | 1.1 | 56 | 20.0 | 13.0 | 17.9 |
| 1m/RETEST/LONG | 6655 | 45.6 | 0.063 | 1.13 | 3110 | 15.0 | 10.0 | 28.7 |
| 1m/RETEST/SHORT | 4393 | 44.2 | 0.034 | 1.07 | 2021 | 17.0 | 11.0 | 30.4 |
| 2m/INV/LONG | 66 | 48.5 | 0.01 | 1.02 | 26 | 14.0 | 10.0 | 19.2 |
| 2m/INV/SHORT | 58 | 41.4 | 0.112 | 1.24 | 26 | 22.5 | 12.5 | 34.6 |
| 2m/RETEST/LONG | 2900 | 46.5 | 0.04 | 1.08 | 1354 | 18.0 | 13.0 | 36.8 |
| 2m/RETEST/SHORT | 1866 | 48.3 | 0.063 | 1.13 | 834 | 23.0 | 12.0 | 39.4 |
| 5m/INV/LONG | 20 | 70.0 | 0.429 | 3.58 | 3 | 30.0 | 31.25 | 66.7 |
| 5m/INV/SHORT | 12 | 66.7 | 0.392 | 2.44 | 3 | 34.0 | 58.25 | 66.7 |
| 5m/RETEST/LONG | 1051 | 50.0 | 0.143 | 1.32 | 433 | 30.0 | 20.0 | 49.7 |
| 5m/RETEST/SHORT | 673 | 47.4 | 0.086 | 1.18 | 291 | 33.0 | 20.0 | 35.4 |

## Por tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| A+ | 1244 | 24.3 | 0.07 | 1.1 | 773 | 28.0 | 14.0 | 20.6 |
| B | 7575 | 46.4 | 0.056 | 1.12 | 3445 | 18.0 | 12.0 | 32.4 |
| C | 9174 | 48.7 | 0.061 | 1.13 | 4006 | 17.0 | 12.0 | 35.4 |

## Por killzone
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| Asia | 6435 | 49.2 | 0.1 | 1.22 | 2853 | 13.0 | 10.0 | 36.5 |
| London | 2696 | 46.2 | 0.041 | 1.08 | 1312 | 18.0 | 11.0 | 33.9 |
| NY | 3209 | 43.9 | 0.053 | 1.11 | 1475 | 25.0 | 15.0 | 36.0 |
| Sin KZ | 5653 | 43.6 | 0.025 | 1.05 | 2584 | 20.0 | 14.0 | 26.2 |

## Por nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| edge=-1 | 4246 | 44.2 | 0.035 | 1.07 | 1967 | 21.0 | 14.0 | 30.2 |
| edge=0 | 7924 | 48.8 | 0.063 | 1.13 | 3514 | 16.0 | 11.0 | 37.4 |
| edge=1 | 5823 | 43.7 | 0.072 | 1.15 | 2743 | 19.0 | 13.0 | 28.6 |

## Por aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| aligned=0 | 8 | 50.0 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| aligned=1 | 17985 | 46.0 | 0.059 | 1.12 | 8223 | 18.0 | 12.0 | 32.7 |

## Por kind/side x nearEdge
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|edge=-1 | 4 | 50.0 | 0.455 | 1.91 | 2 | 44.5 | 3.0 | 50.0 |
| INV/LONG|edge=0 | 98 | 55.1 | 0.184 | 1.49 | 34 | 12.0 | 11.75 | 26.5 |
| INV/LONG|edge=1 | 147 | 42.2 | 0.128 | 1.29 | 60 | 19.0 | 14.75 | 15.0 |
| INV/SHORT|edge=-1 | 115 | 40.9 | 0.032 | 1.07 | 53 | 24.0 | 12.0 | 22.6 |
| INV/SHORT|edge=0 | 82 | 53.7 | 0.088 | 1.22 | 29 | 16.0 | 17.0 | 31.0 |
| INV/SHORT|edge=1 | 9 | 66.7 | 0.69 | 3.07 | 3 | 28.0 | 32.0 | 0.0 |
| RETEST/LONG|edge=-1 | 395 | 53.9 | 0.205 | 1.49 | 157 | 16.0 | 11.0 | 44.6 |
| RETEST/LONG|edge=0 | 4693 | 49.0 | 0.046 | 1.1 | 2122 | 15.0 | 11.0 | 37.6 |
| RETEST/LONG|edge=1 | 5518 | 43.4 | 0.07 | 1.14 | 2618 | 19.0 | 13.0 | 28.2 |
| RETEST/SHORT|edge=-1 | 3732 | 43.2 | 0.016 | 1.03 | 1755 | 21.0 | 14.0 | 29.2 |
| RETEST/SHORT|edge=0 | 3051 | 48.0 | 0.084 | 1.18 | 1329 | 18.0 | 11.0 | 37.5 |
| RETEST/SHORT|edge=1 | 149 | 55.0 | 0.058 | 1.14 | 62 | 14.0 | 9.0 | 58.1 |

## Por kind/side x tier
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|tier=B | 80 | 43.8 | 0.221 | 1.49 | 34 | 17.0 | 15.5 | 8.8 |
| INV/LONG|tier=C | 169 | 49.1 | 0.124 | 1.31 | 62 | 15.0 | 12.5 | 25.8 |
| INV/SHORT|tier=B | 61 | 42.6 | -0.011 | 0.98 | 30 | 21.0 | 11.75 | 6.7 |
| INV/SHORT|tier=C | 145 | 49.0 | 0.125 | 1.31 | 55 | 20.0 | 19.5 | 34.5 |
| RETEST/LONG|tier=A+ | 792 | 23.6 | 0.036 | 1.05 | 510 | 25.0 | 13.0 | 19.0 |
| RETEST/LONG|tier=B | 4482 | 46.7 | 0.092 | 1.19 | 2023 | 17.0 | 12.0 | 32.6 |
| RETEST/LONG|tier=C | 5332 | 49.3 | 0.046 | 1.1 | 2364 | 16.0 | 12.0 | 36.0 |
| RETEST/SHORT|tier=A+ | 452 | 25.4 | 0.131 | 1.2 | 263 | 35.0 | 15.0 | 23.6 |
| RETEST/SHORT|tier=B | 2952 | 46.1 | -0.002 | 1.0 | 1358 | 18.0 | 13.0 | 33.4 |
| RETEST/SHORT|tier=C | 3528 | 47.8 | 0.078 | 1.17 | 1525 | 20.0 | 12.0 | 34.8 |

## Por kind/side x aligned
| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |
|---|--|--|--|--|--|--|--|--|
| INV/LONG|aligned=1 | 249 | 47.4 | 0.156 | 1.37 | 96 | 16.0 | 13.75 | 19.8 |
| INV/SHORT|aligned=1 | 206 | 47.1 | 0.084 | 1.19 | 85 | 20.0 | 17.0 | 24.7 |
| RETEST/LONG|aligned=0 | 8 | 50.0 | 0.408 | 3.04 | 1 | 17.0 | 13.75 | 0.0 |
| RETEST/LONG|aligned=1 | 10598 | 46.3 | 0.064 | 1.13 | 4896 | 17.0 | 12.0 | 32.8 |
| RETEST/SHORT|aligned=1 | 6932 | 45.6 | 0.047 | 1.1 | 3146 | 20.0 | 13.0 | 33.2 |

## Autopsia de SL
n_losses=8224  causas: RR-bajo×3038, contra-estructura×2815, stop-en-el-minimo×2693, killzone-Asia-largo×1742, sin-nivel-detras×1599, estirado×1396, chop×1235, SL-muy-pegado×1050, sin-causa-clara×905, contra-sesgo×1
- INV/LONG (n=96): RR-bajo×39, killzone-Asia-largo×38, contra-estructura×27, estirado×24, stop-en-el-minimo×19, chop×14, sin-nivel-detras×12, SL-muy-pegado×9, sin-causa-clara×6
- INV/SHORT (n=85): RR-bajo×42, contra-estructura×26, stop-en-el-minimo×21, estirado×21, sin-causa-clara×14, SL-muy-pegado×11, chop×8, sin-nivel-detras×6
- RETEST/LONG (n=4897): RR-bajo×1810, contra-estructura×1740, killzone-Asia-largo×1704, stop-en-el-minimo×1607, sin-nivel-detras×997, chop×809, estirado×801, SL-muy-pegado×600, sin-causa-clara×435, contra-sesgo×1
- RETEST/SHORT (n=3146): RR-bajo×1147, stop-en-el-minimo×1046, contra-estructura×1022, sin-nivel-detras×584, estirado×550, sin-causa-clara×450, SL-muy-pegado×430, chop×404

## Autopsia de SL · semana 2026-W40 (para revision semanal)
n_losses=6  causas: killzone-Asia-largo×6, contra-estructura×4, RR-bajo×3
ejemplos por causa: {"killzone-Asia-largo": ["CL-2-20674-L", "CL-1-20614-L", "CL-1-20631-L", "CL-1-20635-L", "CL-1-20639-L"], "contra-estructura": ["CL-2-20674-L", "CL-1-20631-L", "CL-1-20635-L", "CL-1-20639-L"], "RR-bajo": ["CL-2-20674-L", "CL-1-20614-L", "CL-1-20631-L"]}

## Contrafactual de gestion
```json
{
  "n": 8,
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
    0.18,
    8
  ],
  "altSL_1_5x_struct": [
    0.247,
    8
  ],
  "note": "fixed_XR: R esperado si el objetivo fuera XR fijo con SL=struct. altSL: SL a mult del SL struct."
}
```

## Modelo GESTIONADO (escalera + parciales) vs INGENUO
```json
{
  "overall": {
    "n": 17148,
    "naive_expR": 0.059,
    "managed_expR": 0.136,
    "delta": 0.076,
    "avgEntryBetterTk_p50": 2.7,
    "fill_t3plus_pct": 46.2,
    "fill_full_pct": 32.7,
    "m1_rate": 37.5,
    "m2_rate": 23.0,
    "m3_rate": 12.3,
    "beAfterM1_rate": 18.2
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 154,
      "naive_expR": 0.182,
      "managed_expR": 0.291,
      "delta": 0.109,
      "avgEntryBetterTk_p50": 2.45,
      "fill_t3plus_pct": 48.1,
      "fill_full_pct": 36.4,
      "m1_rate": 42.9,
      "m2_rate": 26.6,
      "m3_rate": 13.6,
      "beAfterM1_rate": 22.7
    },
    "1m/INV/SHORT": {
      "n": 130,
      "naive_expR": 0.046,
      "managed_expR": 0.181,
      "delta": 0.135,
      "avgEntryBetterTk_p50": 3.05,
      "fill_t3plus_pct": 53.1,
      "fill_full_pct": 40.0,
      "m1_rate": 34.6,
      "m2_rate": 20.0,
      "m3_rate": 12.3,
      "beAfterM1_rate": 17.7
    },
    "1m/RETEST/LONG": {
      "n": 6429,
      "naive_expR": 0.063,
      "managed_expR": 0.147,
      "delta": 0.084,
      "avgEntryBetterTk_p50": 2.1,
      "fill_t3plus_pct": 47.6,
      "fill_full_pct": 33.8,
      "m1_rate": 38.1,
      "m2_rate": 23.3,
      "m3_rate": 11.9,
      "beAfterM1_rate": 17.5
    },
    "1m/RETEST/SHORT": {
      "n": 4127,
      "naive_expR": 0.035,
      "managed_expR": 0.163,
      "delta": 0.128,
      "avgEntryBetterTk_p50": 2.8,
      "fill_t3plus_pct": 49.1,
      "fill_full_pct": 34.2,
      "m1_rate": 39.0,
      "m2_rate": 24.2,
      "m3_rate": 13.6,
      "beAfterM1_rate": 18.4
    },
    "2m/INV/LONG": {
      "n": 62,
      "naive_expR": 0.01,
      "managed_expR": -0.007,
      "delta": -0.017,
      "avgEntryBetterTk_p50": 2.4000000000000004,
      "fill_t3plus_pct": 51.6,
      "fill_full_pct": 37.1,
      "m1_rate": 22.6,
      "m2_rate": 16.1,
      "m3_rate": 6.5,
      "beAfterM1_rate": 9.7
    },
    "2m/INV/SHORT": {
      "n": 56,
      "naive_expR": 0.112,
      "managed_expR": 0.086,
      "delta": -0.026,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 48.2,
      "fill_full_pct": 35.7,
      "m1_rate": 32.1,
      "m2_rate": 23.2,
      "m3_rate": 16.1,
      "beAfterM1_rate": 10.7
    },
    "2m/RETEST/LONG": {
      "n": 2775,
      "naive_expR": 0.04,
      "managed_expR": 0.073,
      "delta": 0.033,
      "avgEntryBetterTk_p50": 2.7,
      "fill_t3plus_pct": 44.1,
      "fill_full_pct": 31.2,
      "m1_rate": 35.2,
      "m2_rate": 20.8,
      "m3_rate": 10.8,
      "beAfterM1_rate": 18.2
    },
    "2m/RETEST/SHORT": {
      "n": 1790,
      "naive_expR": 0.063,
      "managed_expR": 0.147,
      "delta": 0.084,
      "avgEntryBetterTk_p50": 2.9,
      "fill_t3plus_pct": 45.3,
      "fill_full_pct": 32.7,
      "m1_rate": 37.2,
      "m2_rate": 23.4,
      "m3_rate": 12.2,
      "beAfterM1_rate": 19.1
    },
    "5m/INV/LONG": {
      "n": 18,
      "naive_expR": 0.429,
      "managed_expR": 0.398,
      "delta": -0.031,
      "avgEntryBetterTk_p50": 2.65,
      "fill_t3plus_pct": 38.9,
      "fill_full_pct": 27.8,
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
      "n": 975,
      "naive_expR": 0.143,
      "managed_expR": 0.095,
      "delta": -0.048,
      "avgEntryBetterTk_p50": 0.7,
      "fill_t3plus_pct": 33.2,
      "fill_full_pct": 25.1,
      "m1_rate": 35.7,
      "m2_rate": 23.1,
      "m3_rate": 13.1,
      "beAfterM1_rate": 19.8
    },
    "5m/RETEST/SHORT": {
      "n": 621,
      "naive_expR": 0.086,
      "managed_expR": 0.105,
      "delta": 0.019,
      "avgEntryBetterTk_p50": 4.9,
      "fill_t3plus_pct": 42.5,
      "fill_full_pct": 28.0,
      "m1_rate": 36.4,
      "m2_rate": 22.4,
      "m3_rate": 11.6,
      "beAfterM1_rate": 18.5
    }
  }
}
```

## SL de 3 capas vs SL = vela 1 del FVG (medicion paralela, mismos TP)
```json
{
  "overall": {
    "n": 15123,
    "layer_expR": 0.061,
    "orig_expR": 0.225,
    "delta_orig_minus_layer": 0.163,
    "delta_ci90": [
      0.129,
      0.198
    ],
    "delta_beats_zero": true,
    "delta_below_zero": false,
    "layer_wrTP1": 48.1,
    "orig_wrTP1": 33.5,
    "slTk_p50": 20.0,
    "slOrigTk_p50": 9.0,
    "orig_wider_pct": 3.9,
    "orig_saved_from_SL": 23,
    "orig_caused_SL": 2242
  },
  "note": "overall/by_tf_kind_side = solo build retestBar (legacy excluido)",
  "invalid_geometry": 2,
  "invalid_by_seg": {
    "1m/RETEST/LONG": 2
  },
  "by_basis": {
    "candle1": {
      "n": 419,
      "layer_expR": 0.123,
      "orig_expR": 0.167,
      "delta_orig_minus_layer": 0.044,
      "delta_ci90": [
        -0.168,
        0.287
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.4,
      "orig_wrTP1": 26.7,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 5.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 96
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
      "n": 11325,
      "layer_expR": 0.065,
      "orig_expR": 0.239,
      "delta_orig_minus_layer": 0.174,
      "delta_ci90": [
        0.135,
        0.213
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 48.5,
      "orig_wrTP1": 34.0,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 4.3,
      "orig_saved_from_SL": 22,
      "orig_caused_SL": 1666
    },
    "retestBar2": {
      "n": 3379,
      "layer_expR": 0.041,
      "orig_expR": 0.184,
      "delta_orig_minus_layer": 0.143,
      "delta_ci90": [
        0.078,
        0.216
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.8,
      "orig_wrTP1": 32.6,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.6,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 480
    }
  },
  "by_tf_kind_side": {
    "1m/INV/LONG": {
      "n": 154,
      "layer_expR": 0.182,
      "orig_expR": -0.048,
      "delta_orig_minus_layer": -0.231,
      "delta_ci90": [
        -0.51,
        0.051
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 46.8,
      "orig_wrTP1": 21.4,
      "slTk_p50": 16.0,
      "slOrigTk_p50": 4.0,
      "orig_wider_pct": 4.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 39
    },
    "1m/INV/SHORT": {
      "n": 120,
      "layer_expR": 0.046,
      "orig_expR": 0.092,
      "delta_orig_minus_layer": 0.046,
      "delta_ci90": [
        -0.313,
        0.408
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 49.2,
      "orig_wrTP1": 25.8,
      "slTk_p50": 20.0,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 28
    },
    "1m/RETEST/LONG": {
      "n": 5580,
      "layer_expR": 0.063,
      "orig_expR": 0.214,
      "delta_orig_minus_layer": 0.151,
      "delta_ci90": [
        0.097,
        0.208
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.6,
      "orig_wrTP1": 29.7,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 7.0,
      "orig_wider_pct": 1.0,
      "orig_saved_from_SL": 2,
      "orig_caused_SL": 946
    },
    "1m/RETEST/SHORT": {
      "n": 3498,
      "layer_expR": 0.037,
      "orig_expR": 0.184,
      "delta_orig_minus_layer": 0.147,
      "delta_ci90": [
        0.08,
        0.22
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 46.6,
      "orig_wrTP1": 32.4,
      "slTk_p50": 19.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 2.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 498
    },
    "2m/INV/LONG": {
      "n": 62,
      "layer_expR": 0.01,
      "orig_expR": 0.942,
      "delta_orig_minus_layer": 0.932,
      "delta_ci90": [
        0.063,
        1.996
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.6,
      "orig_wrTP1": 30.6,
      "slTk_p50": 24.5,
      "slOrigTk_p50": 5.0,
      "orig_wider_pct": 6.5,
      "orig_saved_from_SL": 0,
      "orig_caused_SL": 13
    },
    "2m/INV/SHORT": {
      "n": 55,
      "layer_expR": 0.107,
      "orig_expR": 0.351,
      "delta_orig_minus_layer": 0.245,
      "delta_ci90": [
        -0.186,
        0.752
      ],
      "delta_beats_zero": false,
      "delta_below_zero": false,
      "layer_wrTP1": 41.8,
      "orig_wrTP1": 32.7,
      "slTk_p50": 24.0,
      "slOrigTk_p50": 8.0,
      "orig_wider_pct": 5.5,
      "orig_saved_from_SL": 1,
      "orig_caused_SL": 6
    },
    "2m/RETEST/LONG": {
      "n": 2539,
      "layer_expR": 0.045,
      "orig_expR": 0.199,
      "delta_orig_minus_layer": 0.154,
      "delta_ci90": [
        0.09,
        0.224
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 49.0,
      "orig_wrTP1": 36.0,
      "slTk_p50": 21.0,
      "slOrigTk_p50": 9.0,
      "orig_wider_pct": 3.4,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 335
    },
    "2m/RETEST/SHORT": {
      "n": 1572,
      "layer_expR": 0.074,
      "orig_expR": 0.226,
      "delta_orig_minus_layer": 0.152,
      "delta_ci90": [
        0.065,
        0.25
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 50.8,
      "orig_wrTP1": 37.1,
      "slTk_p50": 22.0,
      "slOrigTk_p50": 11.0,
      "orig_wider_pct": 4.0,
      "orig_saved_from_SL": 3,
      "orig_caused_SL": 219
    },
    "5m/INV/LONG": {
      "n": 18,
      "layer_expR": 0.429,
      "orig_expR": -0.389,
      "delta_orig_minus_layer": -0.818,
      "delta_ci90": [
        -1.274,
        -0.353
      ],
      "delta_beats_zero": false,
      "delta_below_zero": true,
      "layer_wrTP1": 77.8,
      "orig_wrTP1": 38.9,
      "slTk_p50": 43.0,
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
      "n": 938,
      "layer_expR": 0.126,
      "orig_expR": 0.398,
      "delta_orig_minus_layer": 0.272,
      "delta_ci90": [
        0.138,
        0.433
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 53.8,
      "orig_wrTP1": 44.3,
      "slTk_p50": 29.0,
      "slOrigTk_p50": 18.0,
      "orig_wider_pct": 16.2,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 96
    },
    "5m/RETEST/SHORT": {
      "n": 577,
      "layer_expR": 0.083,
      "orig_expR": 0.445,
      "delta_orig_minus_layer": 0.362,
      "delta_ci90": [
        0.103,
        0.649
      ],
      "delta_beats_zero": true,
      "delta_below_zero": false,
      "layer_wrTP1": 51.0,
      "orig_wrTP1": 43.2,
      "slTk_p50": 30.0,
      "slOrigTk_p50": 24.0,
      "orig_wider_pct": 22.0,
      "orig_saved_from_SL": 7,
      "orig_caused_SL": 52
    }
  }
}
```

## Contrafactual de entrada por RR minimo (candidato sc_min_rr, ataca causa RR-bajo)
```json
{
  "1/RETEST/LONG": {
    "baseline": {
      "n": 6392,
      "wrTP1": 47.4,
      "nSL": 2940,
      "nTO": 419,
      "expR": 0.055,
      "pf": 1.12,
      "mfe_p25": 6.0,
      "mfe_p50": 15.0,
      "mfe_p75": 34.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 30.4,
      "ci90": {
        "expR": 0.055,
        "ci90": [
          0.031,
          0.08
        ],
        "p_mean_le_0": 0.0,
        "n": 6175
      }
    },
    "cuts": {
      "1.0": {
        "n": 3129,
        "wrTP1": 30.9,
        "nSL": 1849,
        "nTO": 312,
        "expR": 0.044,
        "pf": 1.07,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 21.7,
        "ci90": {
          "expR": 0.044,
          "ci90": [
            -0.001,
            0.09
          ],
          "p_mean_le_0": 0.054,
          "n": 2996
        }
      },
      "1.2": {
        "n": 2592,
        "wrTP1": 28.0,
        "nSL": 1578,
        "nTO": 287,
        "expR": 0.052,
        "pf": 1.08,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 19.1,
        "ci90": {
          "expR": 0.052,
          "ci90": [
            -0.0,
            0.105
          ],
          "p_mean_le_0": 0.051,
          "n": 2476
        }
      },
      "1.3": {
        "n": 2371,
        "wrTP1": 26.4,
        "nSL": 1467,
        "nTO": 279,
        "expR": 0.046,
        "pf": 1.07,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.9,
        "ci90": {
          "expR": 0.046,
          "ci90": [
            -0.008,
            0.103
          ],
          "p_mean_le_0": 0.085,
          "n": 2258
        }
      },
      "1.5": {
        "n": 2005,
        "wrTP1": 24.1,
        "nSL": 1269,
        "nTO": 252,
        "expR": 0.051,
        "pf": 1.08,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 15.3,
        "ci90": {
          "expR": 0.051,
          "ci90": [
            -0.012,
            0.11
          ],
          "p_mean_le_0": 0.087,
          "n": 1909
        }
      },
      "2.0": {
        "n": 1291,
        "wrTP1": 18.0,
        "nSL": 854,
        "nTO": 205,
        "expR": 0.048,
        "pf": 1.07,
        "mfe_p25": 8.0,
        "mfe_p50": 20.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 9.0,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 11.4,
        "ci90": {
          "expR": 0.048,
          "ci90": [
            -0.033,
            0.13
          ],
          "p_mean_le_0": 0.161,
          "n": 1230
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 4183,
      "wrTP1": 46.4,
      "nSL": 1871,
      "nTO": 370,
      "expR": 0.047,
      "pf": 1.1,
      "mfe_p25": 8.0,
      "mfe_p50": 17.0,
      "mfe_p75": 36.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 32.8,
      "ci90": {
        "expR": 0.047,
        "ci90": [
          0.018,
          0.078
        ],
        "p_mean_le_0": 0.004,
        "n": 3939
      }
    },
    "cuts": {
      "1.0": {
        "n": 2009,
        "wrTP1": 30.6,
        "nSL": 1133,
        "nTO": 261,
        "expR": 0.059,
        "pf": 1.1,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.600000000000023,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 22.8,
        "ci90": {
          "expR": 0.059,
          "ci90": [
            0.004,
            0.115
          ],
          "p_mean_le_0": 0.039,
          "n": 1850
        }
      },
      "1.2": {
        "n": 1650,
        "wrTP1": 28.2,
        "nSL": 950,
        "nTO": 235,
        "expR": 0.081,
        "pf": 1.13,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 20.1,
        "ci90": {
          "expR": 0.081,
          "ci90": [
            0.016,
            0.145
          ],
          "p_mean_le_0": 0.024,
          "n": 1513
        }
      },
      "1.3": {
        "n": 1508,
        "wrTP1": 26.6,
        "nSL": 878,
        "nTO": 229,
        "expR": 0.083,
        "pf": 1.13,
        "mfe_p25": 11.0,
        "mfe_p50": 25.0,
        "mfe_p75": 51.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 19.2,
        "ci90": {
          "expR": 0.083,
          "ci90": [
            0.014,
            0.15
          ],
          "p_mean_le_0": 0.027,
          "n": 1377
        }
      },
      "1.5": {
        "n": 1283,
        "wrTP1": 24.3,
        "nSL": 768,
        "nTO": 203,
        "expR": 0.082,
        "pf": 1.12,
        "mfe_p25": 11.0,
        "mfe_p50": 27.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -12.5,
        "revAfterSL_rate": 17.3,
        "ci90": {
          "expR": 0.082,
          "ci90": [
            -0.001,
            0.162
          ],
          "p_mean_le_0": 0.052,
          "n": 1171
        }
      },
      "2.0": {
        "n": 863,
        "wrTP1": 20.0,
        "nSL": 535,
        "nTO": 155,
        "expR": 0.098,
        "pf": 1.14,
        "mfe_p25": 11.0,
        "mfe_p50": 28.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.80000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 13.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 12.7,
        "ci90": {
          "expR": 0.098,
          "ci90": [
            -0.002,
            0.206
          ],
          "p_mean_le_0": 0.055,
          "n": 786
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 2806,
      "wrTP1": 48.0,
      "nSL": 1296,
      "nTO": 162,
      "expR": 0.03,
      "pf": 1.06,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 26.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 38.4,
      "ci90": {
        "expR": 0.03,
        "ci90": [
          -0.008,
          0.068
        ],
        "p_mean_le_0": 0.098,
        "n": 2689
      }
    },
    "cuts": {
      "1.0": {
        "n": 1270,
        "wrTP1": 30.9,
        "nSL": 764,
        "nTO": 114,
        "expR": 0.028,
        "pf": 1.04,
        "mfe_p25": 10.0,
        "mfe_p50": 24.0,
        "mfe_p75": 55.0,
        "winnerMAE_p75": 11.25,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 30.9,
        "ci90": {
          "expR": 0.028,
          "ci90": [
            -0.044,
            0.103
          ],
          "p_mean_le_0": 0.271,
          "n": 1196
        }
      },
      "1.2": {
        "n": 1036,
        "wrTP1": 27.5,
        "nSL": 653,
        "nTO": 98,
        "expR": 0.024,
        "pf": 1.04,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 56.5,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 28.8,
        "ci90": {
          "expR": 0.024,
          "ci90": [
            -0.062,
            0.106
          ],
          "p_mean_le_0": 0.33,
          "n": 975
        }
      },
      "1.3": {
        "n": 946,
        "wrTP1": 27.0,
        "nSL": 597,
        "nTO": 94,
        "expR": 0.047,
        "pf": 1.07,
        "mfe_p25": 11.0,
        "mfe_p50": 23.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.5,
        "revAfterSL_rate": 27.5,
        "ci90": {
          "expR": 0.047,
          "ci90": [
            -0.043,
            0.139
          ],
          "p_mean_le_0": 0.203,
          "n": 889
        }
      },
      "1.5": {
        "n": 768,
        "wrTP1": 24.2,
        "nSL": 492,
        "nTO": 90,
        "expR": 0.067,
        "pf": 1.1,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 22.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 25.0,
        "ci90": {
          "expR": 0.067,
          "ci90": [
            -0.043,
            0.179
          ],
          "p_mean_le_0": 0.166,
          "n": 715
        }
      },
      "2.0": {
        "n": 477,
        "wrTP1": 20.3,
        "nSL": 316,
        "nTO": 64,
        "expR": 0.135,
        "pf": 1.19,
        "mfe_p25": 12.0,
        "mfe_p50": 27.0,
        "mfe_p75": 67.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 20.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 21.8,
        "ci90": {
          "expR": 0.135,
          "ci90": [
            -0.017,
            0.283
          ],
          "p_mean_le_0": 0.07,
          "n": 441
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 1765,
      "wrTP1": 51.0,
      "nSL": 757,
      "nTO": 107,
      "expR": 0.096,
      "pf": 1.22,
      "mfe_p25": 10.0,
      "mfe_p50": 22.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 27.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 43.5,
      "ci90": {
        "expR": 0.096,
        "ci90": [
          0.048,
          0.142
        ],
        "p_mean_le_0": 0.0,
        "n": 1699
      }
    },
    "cuts": {
      "1.0": {
        "n": 800,
        "wrTP1": 34.6,
        "nSL": 454,
        "nTO": 69,
        "expR": 0.12,
        "pf": 1.2,
        "mfe_p25": 16.0,
        "mfe_p50": 31.0,
        "mfe_p75": 58.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 26.400000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.5,
        "revAfterSL_rate": 36.3,
        "ci90": {
          "expR": 0.12,
          "ci90": [
            0.032,
            0.21
          ],
          "p_mean_le_0": 0.006,
          "n": 766
        }
      },
      "1.2": {
        "n": 646,
        "wrTP1": 31.3,
        "nSL": 380,
        "nTO": 64,
        "expR": 0.131,
        "pf": 1.21,
        "mfe_p25": 17.0,
        "mfe_p50": 31.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 25.900000000000006,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.5,
        "revAfterSL_rate": 32.6,
        "ci90": {
          "expR": 0.131,
          "ci90": [
            0.035,
            0.235
          ],
          "p_mean_le_0": 0.018,
          "n": 615
        }
      },
      "1.3": {
        "n": 583,
        "wrTP1": 29.3,
        "nSL": 352,
        "nTO": 60,
        "expR": 0.116,
        "pf": 1.18,
        "mfe_p25": 17.0,
        "mfe_p50": 31.0,
        "mfe_p75": 61.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 27.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 31.2,
        "ci90": {
          "expR": 0.116,
          "ci90": [
            -0.001,
            0.232
          ],
          "p_mean_le_0": 0.052,
          "n": 555
        }
      },
      "1.5": {
        "n": 487,
        "wrTP1": 27.3,
        "nSL": 300,
        "nTO": 54,
        "expR": 0.13,
        "pf": 1.2,
        "mfe_p25": 18.0,
        "mfe_p50": 33.0,
        "mfe_p75": 68.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 26.799999999999997,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 29.7,
        "ci90": {
          "expR": 0.13,
          "ci90": [
            0.004,
            0.268
          ],
          "p_mean_le_0": 0.045,
          "n": 464
        }
      },
      "2.0": {
        "n": 316,
        "wrTP1": 24.1,
        "nSL": 198,
        "nTO": 42,
        "expR": 0.201,
        "pf": 1.3,
        "mfe_p25": 20.0,
        "mfe_p50": 34.5,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 10.25,
        "winnerMAE_p90": 22.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 26.3,
        "ci90": {
          "expR": 0.201,
          "ci90": [
            0.032,
            0.371
          ],
          "p_mean_le_0": 0.024,
          "n": 300
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 1000,
      "wrTP1": 52.6,
      "nSL": 397,
      "nTO": 77,
      "expR": 0.164,
      "pf": 1.38,
      "mfe_p25": 12.0,
      "mfe_p50": 28.0,
      "mfe_p75": 66.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 41.0,
      "loserMFEbeforeSL_p50": 2.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -35.0,
      "revAfterSL_rate": 54.2,
      "ci90": {
        "expR": 0.164,
        "ci90": [
          0.099,
          0.231
        ],
        "p_mean_le_0": 0.0,
        "n": 931
      }
    },
    "cuts": {
      "1.0": {
        "n": 414,
        "wrTP1": 37.2,
        "nSL": 210,
        "nTO": 50,
        "expR": 0.302,
        "pf": 1.54,
        "mfe_p25": 16.75,
        "mfe_p50": 37.5,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 34.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.302,
          "ci90": [
            0.167,
            0.446
          ],
          "p_mean_le_0": 0.0,
          "n": 372
        }
      },
      "1.2": {
        "n": 347,
        "wrTP1": 36.6,
        "nSL": 174,
        "nTO": 46,
        "expR": 0.376,
        "pf": 1.67,
        "mfe_p25": 16.0,
        "mfe_p50": 37.0,
        "mfe_p75": 82.0,
        "winnerMAE_p75": 17.0,
        "winnerMAE_p90": 27.200000000000017,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 47.1,
        "ci90": {
          "expR": 0.376,
          "ci90": [
            0.214,
            0.538
          ],
          "p_mean_le_0": 0.001,
          "n": 309
        }
      },
      "1.3": {
        "n": 312,
        "wrTP1": 34.0,
        "nSL": 165,
        "nTO": 41,
        "expR": 0.348,
        "pf": 1.59,
        "mfe_p25": 16.5,
        "mfe_p50": 36.0,
        "mfe_p75": 81.0,
        "winnerMAE_p75": 15.0,
        "winnerMAE_p90": 21.5,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 46.1,
        "ci90": {
          "expR": 0.348,
          "ci90": [
            0.173,
            0.528
          ],
          "p_mean_le_0": 0.001,
          "n": 279
        }
      },
      "1.5": {
        "n": 263,
        "wrTP1": 33.1,
        "nSL": 139,
        "nTO": 37,
        "expR": 0.404,
        "pf": 1.68,
        "mfe_p25": 17.0,
        "mfe_p50": 36.0,
        "mfe_p75": 81.5,
        "winnerMAE_p75": 14.5,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -30.0,
        "revAfterSL_rate": 43.2,
        "ci90": {
          "expR": 0.404,
          "ci90": [
            0.205,
            0.602
          ],
          "p_mean_le_0": 0.001,
          "n": 234
        }
      },
      "2.0": {
        "n": 175,
        "wrTP1": 28.6,
        "nSL": 97,
        "nTO": 28,
        "expR": 0.467,
        "pf": 1.75,
        "mfe_p25": 17.5,
        "mfe_p50": 42.0,
        "mfe_p75": 109.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -33.0,
        "revAfterSL_rate": 37.1,
        "ci90": {
          "expR": 0.467,
          "ci90": [
            0.206,
            0.751
          ],
          "p_mean_le_0": 0.002,
          "n": 155
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 636,
      "wrTP1": 50.2,
      "nSL": 264,
      "nTO": 53,
      "expR": 0.109,
      "pf": 1.24,
      "mfe_p25": 14.0,
      "mfe_p50": 32.0,
      "mfe_p75": 61.0,
      "winnerMAE_p75": 20.0,
      "winnerMAE_p90": 38.19999999999999,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -30.0,
      "revAfterSL_rate": 38.6,
      "ci90": {
        "expR": 0.109,
        "ci90": [
          0.03,
          0.188
        ],
        "p_mean_le_0": 0.011,
        "n": 590
      }
    },
    "cuts": {
      "1.0": {
        "n": 283,
        "wrTP1": 33.9,
        "nSL": 158,
        "nTO": 29,
        "expR": 0.147,
        "pf": 1.24,
        "mfe_p25": 19.75,
        "mfe_p50": 41.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 19.5,
        "winnerMAE_p90": 38.5,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 30.4,
        "ci90": {
          "expR": 0.147,
          "ci90": [
            -0.014,
            0.311
          ],
          "p_mean_le_0": 0.066,
          "n": 260
        }
      },
      "1.2": {
        "n": 233,
        "wrTP1": 30.0,
        "nSL": 137,
        "nTO": 26,
        "expR": 0.138,
        "pf": 1.21,
        "mfe_p25": 22.0,
        "mfe_p50": 43.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 37.400000000000006,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 27.7,
        "ci90": {
          "expR": 0.138,
          "ci90": [
            -0.044,
            0.326
          ],
          "p_mean_le_0": 0.112,
          "n": 212
        }
      },
      "1.3": {
        "n": 215,
        "wrTP1": 29.8,
        "nSL": 128,
        "nTO": 23,
        "expR": 0.133,
        "pf": 1.2,
        "mfe_p25": 22.0,
        "mfe_p50": 43.0,
        "mfe_p75": 71.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 39.80000000000001,
        "loserMFEbeforeSL_p50": 7.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 26.6,
        "ci90": {
          "expR": 0.133,
          "ci90": [
            -0.058,
            0.346
          ],
          "p_mean_le_0": 0.13,
          "n": 197
        }
      },
      "1.5": {
        "n": 178,
        "wrTP1": 28.1,
        "nSL": 106,
        "nTO": 22,
        "expR": 0.151,
        "pf": 1.23,
        "mfe_p25": 25.0,
        "mfe_p50": 48.0,
        "mfe_p75": 75.0,
        "winnerMAE_p75": 19.0,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 3.5,
        "bars_loss_p50": 2.5,
        "entryZoneTk_p50": -28.5,
        "revAfterSL_rate": 25.5,
        "ci90": {
          "expR": 0.151,
          "ci90": [
            -0.065,
            0.372
          ],
          "p_mean_le_0": 0.133,
          "n": 161
        }
      },
      "2.0": {
        "n": 116,
        "wrTP1": 21.6,
        "nSL": 77,
        "nTO": 14,
        "expR": 0.075,
        "pf": 1.1,
        "mfe_p25": 28.25,
        "mfe_p50": 52.5,
        "mfe_p75": 84.5,
        "winnerMAE_p75": 25.0,
        "winnerMAE_p90": 41.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -30.5,
        "revAfterSL_rate": 24.7,
        "ci90": {
          "expR": 0.075,
          "ci90": [
            -0.21,
            0.388
          ],
          "p_mean_le_0": 0.344,
          "n": 106
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
      "n": 1940,
      "wrTP1": 47.3,
      "nSL": 887,
      "nTO": 135,
      "expR": 0.064,
      "pf": 1.14,
      "mfe_p25": 6.0,
      "mfe_p50": 14.0,
      "mfe_p75": 33.0,
      "winnerMAE_p75": 9.0,
      "winnerMAE_p90": 21.0,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 31.8,
      "ci90": {
        "expR": 0.064,
        "ci90": [
          0.021,
          0.111
        ],
        "p_mean_le_0": 0.008,
        "n": 1872
      }
    },
    "cuts": {
      "1.2": {
        "n": 783,
        "wrTP1": 28.0,
        "nSL": 475,
        "nTO": 89,
        "expR": 0.055,
        "pf": 1.09,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 44.0,
        "winnerMAE_p75": 7.5,
        "winnerMAE_p90": 16.200000000000017,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 19.8,
        "ci90": {
          "expR": 0.055,
          "ci90": [
            -0.04,
            0.152
          ],
          "p_mean_le_0": 0.183,
          "n": 748
        }
      },
      "1.3": {
        "n": 715,
        "wrTP1": 26.0,
        "nSL": 443,
        "nTO": 86,
        "expR": 0.043,
        "pf": 1.07,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 44.0,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 15.5,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 18.5,
        "ci90": {
          "expR": 0.043,
          "ci90": [
            -0.058,
            0.15
          ],
          "p_mean_le_0": 0.233,
          "n": 681
        }
      },
      "1.5": {
        "n": 603,
        "wrTP1": 23.9,
        "nSL": 382,
        "nTO": 77,
        "expR": 0.049,
        "pf": 1.07,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 14.400000000000034,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 9.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 14.1,
        "ci90": {
          "expR": 0.049,
          "ci90": [
            -0.065,
            0.162
          ],
          "p_mean_le_0": 0.257,
          "n": 575
        }
      },
      "2.0": {
        "n": 384,
        "wrTP1": 18.8,
        "nSL": 249,
        "nTO": 63,
        "expR": 0.089,
        "pf": 1.13,
        "mfe_p25": 8.0,
        "mfe_p50": 19.0,
        "mfe_p75": 48.0,
        "winnerMAE_p75": 5.0,
        "winnerMAE_p90": 13.0,
        "loserMFEbeforeSL_p50": 5.0,
        "bars_win_p50": 12.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 11.6,
        "ci90": {
          "expR": 0.089,
          "ci90": [
            -0.064,
            0.238
          ],
          "p_mean_le_0": 0.176,
          "n": 365
        }
      }
    }
  },
  "1/RETEST/SHORT": {
    "baseline": {
      "n": 1283,
      "wrTP1": 47.5,
      "nSL": 570,
      "nTO": 103,
      "expR": 0.028,
      "pf": 1.06,
      "mfe_p25": 9.0,
      "mfe_p50": 17.0,
      "mfe_p75": 33.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 18.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -11.0,
      "revAfterSL_rate": 31.4,
      "ci90": {
        "expR": 0.028,
        "ci90": [
          -0.024,
          0.081
        ],
        "p_mean_le_0": 0.183,
        "n": 1217
      }
    },
    "cuts": {
      "1.2": {
        "n": 465,
        "wrTP1": 28.4,
        "nSL": 273,
        "nTO": 60,
        "expR": 0.04,
        "pf": 1.06,
        "mfe_p25": 13.0,
        "mfe_p50": 25.0,
        "mfe_p75": 44.0,
        "winnerMAE_p75": 12.0,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 19.0,
        "ci90": {
          "expR": 0.04,
          "ci90": [
            -0.083,
            0.169
          ],
          "p_mean_le_0": 0.299,
          "n": 429
        }
      },
      "1.3": {
        "n": 417,
        "wrTP1": 27.3,
        "nSL": 244,
        "nTO": 59,
        "expR": 0.062,
        "pf": 1.1,
        "mfe_p25": 15.0,
        "mfe_p50": 27.0,
        "mfe_p75": 45.0,
        "winnerMAE_p75": 12.75,
        "winnerMAE_p90": 18.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 17.6,
        "ci90": {
          "expR": 0.062,
          "ci90": [
            -0.067,
            0.199
          ],
          "p_mean_le_0": 0.222,
          "n": 382
        }
      },
      "1.5": {
        "n": 349,
        "wrTP1": 24.4,
        "nSL": 213,
        "nTO": 51,
        "expR": 0.041,
        "pf": 1.06,
        "mfe_p25": 15.0,
        "mfe_p50": 27.0,
        "mfe_p75": 43.5,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 8.0,
        "bars_loss_p50": 6.0,
        "entryZoneTk_p50": -10.0,
        "revAfterSL_rate": 16.0,
        "ci90": {
          "expR": 0.041,
          "ci90": [
            -0.107,
            0.193
          ],
          "p_mean_le_0": 0.35,
          "n": 319
        }
      },
      "2.0": {
        "n": 216,
        "wrTP1": 18.5,
        "nSL": 141,
        "nTO": 35,
        "expR": 0.006,
        "pf": 1.01,
        "mfe_p25": 15.0,
        "mfe_p50": 27.0,
        "mfe_p75": 46.75,
        "winnerMAE_p75": 9.25,
        "winnerMAE_p90": 18.200000000000003,
        "loserMFEbeforeSL_p50": 11.0,
        "bars_win_p50": 11.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -11.0,
        "revAfterSL_rate": 12.8,
        "ci90": {
          "expR": 0.006,
          "ci90": [
            -0.191,
            0.214
          ],
          "p_mean_le_0": 0.505,
          "n": 198
        }
      }
    }
  },
  "2/RETEST/LONG": {
    "baseline": {
      "n": 745,
      "wrTP1": 48.5,
      "nSL": 340,
      "nTO": 44,
      "expR": 0.07,
      "pf": 1.15,
      "mfe_p25": 8.0,
      "mfe_p50": 20.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 28.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 40.3,
      "ci90": {
        "expR": 0.07,
        "ci90": [
          -0.005,
          0.147
        ],
        "p_mean_le_0": 0.062,
        "n": 713
      }
    },
    "cuts": {
      "1.2": {
        "n": 265,
        "wrTP1": 26.8,
        "nSL": 167,
        "nTO": 27,
        "expR": 0.099,
        "pf": 1.15,
        "mfe_p25": 11.0,
        "mfe_p50": 24.0,
        "mfe_p75": 49.0,
        "winnerMAE_p75": 6.5,
        "winnerMAE_p90": 17.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 31.7,
        "ci90": {
          "expR": 0.099,
          "ci90": [
            -0.08,
            0.279
          ],
          "p_mean_le_0": 0.193,
          "n": 248
        }
      },
      "1.3": {
        "n": 242,
        "wrTP1": 27.3,
        "nSL": 149,
        "nTO": 27,
        "expR": 0.165,
        "pf": 1.25,
        "mfe_p25": 12.0,
        "mfe_p50": 25.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 16.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 28.9,
        "ci90": {
          "expR": 0.165,
          "ci90": [
            -0.031,
            0.362
          ],
          "p_mean_le_0": 0.087,
          "n": 225
        }
      },
      "1.5": {
        "n": 201,
        "wrTP1": 25.4,
        "nSL": 124,
        "nTO": 26,
        "expR": 0.219,
        "pf": 1.33,
        "mfe_p25": 12.0,
        "mfe_p50": 25.0,
        "mfe_p75": 50.0,
        "winnerMAE_p75": 6.0,
        "winnerMAE_p90": 15.0,
        "loserMFEbeforeSL_p50": 7.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -17.0,
        "revAfterSL_rate": 26.6,
        "ci90": {
          "expR": 0.219,
          "ci90": [
            -0.007,
            0.453
          ],
          "p_mean_le_0": 0.056,
          "n": 185
        }
      },
      "2.0": {
        "n": 128,
        "wrTP1": 25.0,
        "nSL": 76,
        "nTO": 20,
        "expR": 0.435,
        "pf": 1.66,
        "mfe_p25": 16.75,
        "mfe_p50": 27.5,
        "mfe_p75": 51.25,
        "winnerMAE_p75": 6.25,
        "winnerMAE_p90": 14.800000000000004,
        "loserMFEbeforeSL_p50": 7.5,
        "bars_win_p50": 7.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 26.3,
        "ci90": {
          "expR": 0.435,
          "ci90": [
            0.107,
            0.752
          ],
          "p_mean_le_0": 0.01,
          "n": 116
        }
      }
    }
  },
  "2/RETEST/SHORT": {
    "baseline": {
      "n": 535,
      "wrTP1": 52.5,
      "nSL": 223,
      "nTO": 31,
      "expR": 0.081,
      "pf": 1.19,
      "mfe_p25": 13.0,
      "mfe_p50": 24.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 23.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 43.5,
      "ci90": {
        "expR": 0.081,
        "ci90": [
          0.006,
          0.159
        ],
        "p_mean_le_0": 0.04,
        "n": 516
      }
    },
    "cuts": {
      "1.2": {
        "n": 200,
        "wrTP1": 30.0,
        "nSL": 122,
        "nTO": 18,
        "expR": -0.014,
        "pf": 0.98,
        "mfe_p25": 18.0,
        "mfe_p50": 31.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 11.25,
        "winnerMAE_p90": 18.1,
        "loserMFEbeforeSL_p50": 6.5,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 32.0,
        "ci90": {
          "expR": -0.014,
          "ci90": [
            -0.183,
            0.157
          ],
          "p_mean_le_0": 0.556,
          "n": 191
        }
      },
      "1.3": {
        "n": 172,
        "wrTP1": 26.7,
        "nSL": 110,
        "nTO": 16,
        "expR": -0.062,
        "pf": 0.91,
        "mfe_p25": 18.0,
        "mfe_p50": 30.0,
        "mfe_p75": 46.0,
        "winnerMAE_p75": 10.75,
        "winnerMAE_p90": 16.5,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 28.2,
        "ci90": {
          "expR": -0.062,
          "ci90": [
            -0.25,
            0.116
          ],
          "p_mean_le_0": 0.71,
          "n": 165
        }
      },
      "1.5": {
        "n": 142,
        "wrTP1": 25.4,
        "nSL": 94,
        "nTO": 12,
        "expR": -0.06,
        "pf": 0.91,
        "mfe_p25": 18.0,
        "mfe_p50": 31.0,
        "mfe_p75": 47.0,
        "winnerMAE_p75": 10.0,
        "winnerMAE_p90": 16.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -13.0,
        "revAfterSL_rate": 27.7,
        "ci90": {
          "expR": -0.06,
          "ci90": [
            -0.25,
            0.141
          ],
          "p_mean_le_0": 0.699,
          "n": 139
        }
      },
      "2.0": {
        "n": 87,
        "wrTP1": 17.2,
        "nSL": 63,
        "nTO": 9,
        "expR": -0.177,
        "pf": 0.76,
        "mfe_p25": 17.0,
        "mfe_p50": 30.0,
        "mfe_p75": 47.25,
        "winnerMAE_p75": 8.0,
        "winnerMAE_p90": 12.799999999999999,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 7.0,
        "bars_loss_p50": 4.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 20.6,
        "ci90": {
          "expR": -0.177,
          "ci90": [
            -0.447,
            0.109
          ],
          "p_mean_le_0": 0.862,
          "n": 84
        }
      }
    }
  },
  "5/RETEST/LONG": {
    "baseline": {
      "n": 251,
      "wrTP1": 49.8,
      "nSL": 102,
      "nTO": 24,
      "expR": 0.117,
      "pf": 1.26,
      "mfe_p25": 12.5,
      "mfe_p50": 27.0,
      "mfe_p75": 69.0,
      "winnerMAE_p75": 21.0,
      "winnerMAE_p90": 42.20000000000002,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -33.5,
      "revAfterSL_rate": 55.9,
      "ci90": {
        "expR": 0.117,
        "ci90": [
          -0.023,
          0.255
        ],
        "p_mean_le_0": 0.083,
        "n": 227
      }
    },
    "cuts": {
      "1.2": {
        "n": 78,
        "wrTP1": 32.1,
        "nSL": 43,
        "nTO": 10,
        "expR": 0.255,
        "pf": 1.4,
        "mfe_p25": 17.0,
        "mfe_p50": 39.0,
        "mfe_p75": 77.25,
        "winnerMAE_p75": 20.0,
        "winnerMAE_p90": 21.6,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -26.5,
        "revAfterSL_rate": 51.2,
        "ci90": {
          "expR": 0.255,
          "ci90": [
            -0.11,
            0.639
          ],
          "p_mean_le_0": 0.132,
          "n": 68
        }
      },
      "1.3": {
        "n": 69,
        "wrTP1": 31.9,
        "nSL": 39,
        "nTO": 8,
        "expR": 0.279,
        "pf": 1.44,
        "mfe_p25": 17.0,
        "mfe_p50": 37.0,
        "mfe_p75": 73.0,
        "winnerMAE_p75": 13.0,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 48.7,
        "ci90": {
          "expR": 0.279,
          "ci90": [
            -0.114,
            0.678
          ],
          "p_mean_le_0": 0.127,
          "n": 61
        }
      },
      "1.5": {
        "n": 57,
        "wrTP1": 33.3,
        "nSL": 32,
        "nTO": 6,
        "expR": 0.39,
        "pf": 1.62,
        "mfe_p25": 23.5,
        "mfe_p50": 38.0,
        "mfe_p75": 70.5,
        "winnerMAE_p75": 9.5,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -29.0,
        "revAfterSL_rate": 50.0,
        "ci90": {
          "expR": 0.39,
          "ci90": [
            -0.063,
            0.854
          ],
          "p_mean_le_0": 0.074,
          "n": 51
        }
      },
      "2.0": {
        "n": 42,
        "wrTP1": 26.2,
        "nSL": 25,
        "nTO": 6,
        "expR": 0.374,
        "pf": 1.54,
        "mfe_p25": 21.25,
        "mfe_p50": 43.0,
        "mfe_p75": 76.25,
        "winnerMAE_p75": 9.5,
        "winnerMAE_p90": 21.0,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 6.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -23.0,
        "revAfterSL_rate": 44.0,
        "ci90": {
          "expR": 0.374,
          "ci90": [
            -0.2,
            1.004
          ],
          "p_mean_le_0": 0.145,
          "n": 36
        }
      }
    }
  },
  "5/RETEST/SHORT": {
    "baseline": {
      "n": 194,
      "wrTP1": 50.0,
      "nSL": 84,
      "nTO": 13,
      "expR": 0.098,
      "pf": 1.21,
      "mfe_p25": 17.0,
      "mfe_p50": 35.0,
      "mfe_p75": 56.0,
      "winnerMAE_p75": 16.0,
      "winnerMAE_p90": 32.60000000000002,
      "loserMFEbeforeSL_p50": 8.0,
      "bars_win_p50": 1.0,
      "bars_loss_p50": 2.0,
      "entryZoneTk_p50": -31.0,
      "revAfterSL_rate": 33.3,
      "ci90": {
        "expR": 0.098,
        "ci90": [
          -0.054,
          0.246
        ],
        "p_mean_le_0": 0.136,
        "n": 184
      }
    },
    "cuts": {
      "1.2": {
        "n": 77,
        "wrTP1": 31.2,
        "nSL": 47,
        "nTO": 6,
        "expR": 0.138,
        "pf": 1.22,
        "mfe_p25": 25.5,
        "mfe_p50": 43.0,
        "mfe_p75": 61.75,
        "winnerMAE_p75": 11.25,
        "winnerMAE_p90": 21.099999999999998,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 2.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -27.0,
        "revAfterSL_rate": 23.4,
        "ci90": {
          "expR": 0.138,
          "ci90": [
            -0.162,
            0.471
          ],
          "p_mean_le_0": 0.245,
          "n": 74
        }
      },
      "1.3": {
        "n": 74,
        "wrTP1": 31.1,
        "nSL": 45,
        "nTO": 6,
        "expR": 0.139,
        "pf": 1.22,
        "mfe_p25": 27.0,
        "mfe_p50": 43.0,
        "mfe_p75": 61.5,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 21.400000000000002,
        "loserMFEbeforeSL_p50": 10.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -26.5,
        "revAfterSL_rate": 24.4,
        "ci90": {
          "expR": 0.139,
          "ci90": [
            -0.166,
            0.462
          ],
          "p_mean_le_0": 0.241,
          "n": 71
        }
      },
      "1.5": {
        "n": 61,
        "wrTP1": 26.2,
        "nSL": 39,
        "nTO": 6,
        "expR": 0.057,
        "pf": 1.08,
        "mfe_p25": 29.0,
        "mfe_p50": 45.0,
        "mfe_p75": 64.25,
        "winnerMAE_p75": 9.25,
        "winnerMAE_p90": 20.5,
        "loserMFEbeforeSL_p50": 12.0,
        "bars_win_p50": 2.5,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -26.0,
        "revAfterSL_rate": 23.1,
        "ci90": {
          "expR": 0.057,
          "ci90": [
            -0.286,
            0.421
          ],
          "p_mean_le_0": 0.418,
          "n": 58
        }
      },
      "2.0": {
        "n": 42,
        "wrTP1": 16.7,
        "nSL": 29,
        "nTO": 6,
        "expR": -0.033,
        "pf": 0.96,
        "mfe_p25": 29.0,
        "mfe_p50": 52.0,
        "mfe_p75": 85.0,
        "winnerMAE_p75": 14.5,
        "winnerMAE_p90": 41.00000000000002,
        "loserMFEbeforeSL_p50": 12.0,
        "bars_win_p50": 5.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -28.0,
        "revAfterSL_rate": 20.7,
        "ci90": {
          "expR": -0.033,
          "ci90": [
            -0.461,
            0.437
          ],
          "p_mean_le_0": 0.55,
          "n": 39
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
    "n": 2868,
    "wrTP1": 44.8,
    "expR": -0.018
  },
  "2026-W37": {
    "n": 5073,
    "wrTP1": 46.9,
    "expR": 0.075
  },
  "2026-W38": {
    "n": 4684,
    "wrTP1": 46.1,
    "expR": 0.092
  },
  "2026-W39": {
    "n": 5355,
    "wrTP1": 45.8,
    "expR": 0.059
  },
  "2026-W40": {
    "n": 13,
    "wrTP1": 53.8,
    "expR": -0.133
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
      "n": 613,
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
      "n": 1490,
      "wrTP1": 45.4,
      "expR": 0.061,
      "pf": 1.13
    },
    "1m/RETEST/SHORT": {
      "n": 1636,
      "wrTP1": 44.8,
      "expR": 0.037,
      "pf": 1.07
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
      "n": 645,
      "wrTP1": 47.4,
      "expR": 0.039,
      "pf": 1.08
    },
    "2m/RETEST/SHORT": {
      "n": 730,
      "wrTP1": 51.6,
      "expR": 0.15,
      "pf": 1.33
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
      "n": 229,
      "wrTP1": 52.4,
      "expR": 0.213,
      "pf": 1.48
    },
    "5m/RETEST/SHORT": {
      "n": 205,
      "wrTP1": 52.7,
      "expR": 0.146,
      "pf": 1.33
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
      "n": 1916,
      "wrTP1": 48.2,
      "expR": 0.122,
      "pf": 1.27
    },
    "1m/RETEST/SHORT": {
      "n": 962,
      "wrTP1": 42.6,
      "expR": 0.114,
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
      "n": 858,
      "wrTP1": 46.4,
      "expR": 0.036,
      "pf": 1.08
    },
    "2m/RETEST/SHORT": {
      "n": 364,
      "wrTP1": 44.0,
      "expR": 0.013,
      "pf": 1.03
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
      "n": 309,
      "wrTP1": 50.2,
      "expR": 0.172,
      "pf": 1.42
    },
    "5m/RETEST/SHORT": {
      "n": 170,
      "wrTP1": 41.8,
      "expR": 0.096,
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
      "n": 43,
      "wrTP1": 48.8,
      "expR": 0.047,
      "pf": 1.12
    },
    "1m/RETEST/LONG": {
      "n": 2035,
      "wrTP1": 45.0,
      "expR": 0.06,
      "pf": 1.12
    },
    "1m/RETEST/SHORT": {
      "n": 1361,
      "wrTP1": 44.8,
      "expR": -0.005,
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
      "n": 783,
      "wrTP1": 46.1,
      "expR": 0.124,
      "pf": 1.26
    },
    "2m/RETEST/SHORT": {
      "n": 571,
      "wrTP1": 49.2,
      "expR": 0.033,
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
      "n": 270,
      "wrTP1": 45.6,
      "expR": 0.102,
      "pf": 1.22
    },
    "5m/RETEST/SHORT": {
      "n": 206,
      "wrTP1": 46.6,
      "expR": 0.059,
      "pf": 1.12
    }
  },
  "2026-W40": {
    "1m/RETEST/LONG": {
      "n": 9,
      "wrTP1": 44.4,
      "expR": -0.221,
      "pf": 0.6
    },
    "2m/RETEST/LONG": {
      "n": 1,
      "wrTP1": 0.0,
      "expR": -1.0,
      "pf": 0.0
    },
    "5m/RETEST/LONG": {
      "n": 2,
      "wrTP1": 100.0,
      "expR": 0.335,
      "pf": 99.0
    },
    "5m/RETEST/SHORT": {
      "n": 1,
      "wrTP1": 100.0,
      "expR": 0.59,
      "pf": 99.0
    }
  }
}
```

## Modelo P(TP1) (in-sample)
```json
{
  "fitted": true,
  "n": 16509,
  "brier": 0.2218,
  "bias": -0.082,
  "coefficients": [
    {
      "feature": "rr1",
      "weight": -1.193
    },
    {
      "feature": "nearTk",
      "weight": -0.1
    },
    {
      "feature": "stretchAtr",
      "weight": -0.051
    },
    {
      "feature": "emaStack",
      "weight": 0.038
    },
    {
      "feature": "rvol",
      "weight": 0.032
    },
    {
      "feature": "atrPctUsed",
      "weight": -0.031
    },
    {
      "feature": "biasScore",
      "weight": -0.03
    },
    {
      "feature": "entryZoneTk",
      "weight": -0.023
    },
    {
      "feature": "aligned",
      "weight": -0.016
    },
    {
      "feature": "chopIdx",
      "weight": -0.016
    },
    {
      "feature": "hourNY",
      "weight": -0.005
    },
    {
      "feature": "nearEdge",
      "weight": 0.003
    },
    {
      "feature": "structDir",
      "weight": -0.001
    }
  ],
  "calibration_deciles": [
    {
      "bin": 0,
      "pred": 0.16,
      "actual": 0.187,
      "n": 1650
    },
    {
      "bin": 1,
      "pred": 0.36,
      "actual": 0.308,
      "n": 1651
    },
    {
      "bin": 2,
      "pred": 0.445,
      "actual": 0.354,
      "n": 1651
    },
    {
      "bin": 3,
      "pred": 0.492,
      "actual": 0.38,
      "n": 1651
    },
    {
      "bin": 4,
      "pred": 0.531,
      "actual": 0.511,
      "n": 1651
    },
    {
      "bin": 5,
      "pred": 0.563,
      "actual": 0.565,
      "n": 1651
    },
    {
      "bin": 6,
      "pred": 0.587,
      "actual": 0.614,
      "n": 1651
    },
    {
      "bin": 7,
      "pred": 0.609,
      "actual": 0.652,
      "n": 1651
    },
    {
      "bin": 8,
      "pred": 0.628,
      "actual": 0.694,
      "n": 1651
    },
    {
      "bin": 9,
      "pred": 0.657,
      "actual": 0.755,
      "n": 1651
    }
  ],
  "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"
}
```

## Walk-forward (fuera de muestra = el numero que cuenta)
```json
{
  "ready": true,
  "trainN": 12625,
  "testN": 5368,
  "testWeeks": [
    "2026-W39",
    "2026-W40"
  ],
  "model_oos_brier": 0.2229,
  "model_oos_n": 5368,
  "best_scheme_in_sample": {
    "scheme": "nextLevel",
    "trainExpR": 0.06
  },
  "best_scheme_oos_expR": 0.059
}
```

## Significancia por segmento (bootstrap + FDR 10%)
```json
{
  "1m/INV/LONG": {
    "expR": 0.182,
    "ci90": [
      -0.007,
      0.393
    ],
    "p_mean_le_0": 0.057,
    "n": 154,
    "survives_fdr10": true
  },
  "1m/INV/SHORT": {
    "expR": 0.046,
    "ci90": [
      -0.103,
      0.208
    ],
    "p_mean_le_0": 0.317,
    "n": 130,
    "survives_fdr10": false
  },
  "1m/RETEST/LONG": {
    "expR": 0.063,
    "ci90": [
      0.037,
      0.089
    ],
    "p_mean_le_0": 0.001,
    "n": 6433,
    "survives_fdr10": true
  },
  "1m/RETEST/SHORT": {
    "expR": 0.034,
    "ci90": [
      0.004,
      0.066
    ],
    "p_mean_le_0": 0.032,
    "n": 4134,
    "survives_fdr10": true
  },
  "2m/INV/LONG": {
    "expR": 0.01,
    "ci90": [
      -0.205,
      0.232
    ],
    "p_mean_le_0": 0.475,
    "n": 62,
    "survives_fdr10": false
  },
  "2m/INV/SHORT": {
    "expR": 0.112,
    "ci90": [
      -0.166,
      0.427
    ],
    "p_mean_le_0": 0.27,
    "n": 56,
    "survives_fdr10": false
  },
  "2m/RETEST/LONG": {
    "expR": 0.04,
    "ci90": [
      0.0,
      0.08
    ],
    "p_mean_le_0": 0.048,
    "n": 2776,
    "survives_fdr10": true
  },
  "2m/RETEST/SHORT": {
    "expR": 0.063,
    "ci90": [
      0.018,
      0.109
    ],
    "p_mean_le_0": 0.013,
    "n": 1790,
    "survives_fdr10": true
  },
  "5m/INV/LONG": {
    "expR": 0.429,
    "ci90": [
      0.099,
      0.756
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
    "expR": 0.143,
    "ci90": [
      0.077,
      0.211
    ],
    "p_mean_le_0": 0.0,
    "n": 975,
    "survives_fdr10": true
  },
  "5m/RETEST/SHORT": {
    "expR": 0.086,
    "ci90": [
      0.005,
      0.165
    ],
    "p_mean_le_0": 0.043,
    "n": 622,
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
      "n": 625,
      "wrTP1": 49.4,
      "expR": 0.105,
      "pf": 1.25,
      "defining_features": {
        "rvol": 3.89,
        "stretchAtr": 1.52,
        "chopIdx": -1.22,
        "biasScore": -0.21
      }
    },
    {
      "id": 0,
      "n": 7760,
      "wrTP1": 47.6,
      "expR": 0.065,
      "pf": 1.14,
      "defining_features": {
        "biasScore": 0.77,
        "emaStack": 0.69,
        "nearEdge": 0.55,
        "chopIdx": 0.43
      }
    },
    {
      "id": 3,
      "n": 2971,
      "wrTP1": 41.9,
      "expR": 0.065,
      "pf": 1.13,
      "defining_features": {
        "stretchAtr": 1.18,
        "chopIdx": -1.08,
        "nearEdge": 0.5,
        "biasScore": 0.49
      }
    },
    {
      "id": 1,
      "n": 6637,
      "wrTP1": 45.8,
      "expR": 0.046,
      "pf": 1.09,
      "defining_features": {
        "biasScore": -1.1,
        "emaStack": -0.97,
        "nearEdge": -0.85,
        "structDir": -0.42
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
        "n": 34,
        "wrTP1": 52.9,
        "expR": 0.549
      },
      "YM": {
        "n": 63,
        "wrTP1": 33.3,
        "expR": 0.231
      },
      "ES": {
        "n": 25,
        "wrTP1": 60.0,
        "expR": 0.13
      },
      "GC": {
        "n": 23,
        "wrTP1": 34.8,
        "expR": -0.402
      },
      "NQ": {
        "n": 18,
        "wrTP1": 55.6,
        "expR": 0.157
      }
    },
    "expR_spread": 0.951,
    "verdict": "instrument-specific"
  },
  "1m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 76,
        "wrTP1": 39.5,
        "expR": -0.04
      },
      "NQ": {
        "n": 11,
        "wrTP1": 54.5,
        "expR": 0.092
      },
      "ES": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": 0.439
      },
      "GC": {
        "n": 29,
        "wrTP1": 69.0,
        "expR": 0.242
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
        "n": 1064,
        "wrTP1": 42.9,
        "expR": 0.032
      },
      "NQ": {
        "n": 1464,
        "wrTP1": 45.7,
        "expR": 0.044
      },
      "ES": {
        "n": 1655,
        "wrTP1": 47.2,
        "expR": 0.075
      },
      "CL": {
        "n": 1442,
        "wrTP1": 45.7,
        "expR": 0.059
      },
      "YM": {
        "n": 1030,
        "wrTP1": 45.5,
        "expR": 0.111
      }
    },
    "expR_spread": 0.079,
    "verdict": "universal"
  },
  "1m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 462,
        "wrTP1": 42.0,
        "expR": 0.051
      },
      "GC": {
        "n": 1202,
        "wrTP1": 46.0,
        "expR": 0.069
      },
      "YM": {
        "n": 1306,
        "wrTP1": 43.3,
        "expR": 0.039
      },
      "ES": {
        "n": 777,
        "wrTP1": 44.5,
        "expR": 0.007
      },
      "CL": {
        "n": 646,
        "wrTP1": 44.0,
        "expR": -0.015
      }
    },
    "expR_spread": 0.084,
    "verdict": "universal"
  },
  "2m/INV/LONG": {
    "symbols": {
      "GC": {
        "n": 7,
        "wrTP1": 42.9,
        "expR": -0.376
      },
      "CL": {
        "n": 7,
        "wrTP1": 57.1,
        "expR": -0.063
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
        "n": 19,
        "wrTP1": 47.4,
        "expR": 0.315
      }
    },
    "expR_spread": 0.691,
    "verdict": "instrument-specific"
  },
  "2m/INV/SHORT": {
    "symbols": {
      "YM": {
        "n": 33,
        "wrTP1": 48.5,
        "expR": 0.29
      },
      "NQ": {
        "n": 8,
        "wrTP1": 50.0,
        "expR": 0.333
      },
      "ES": {
        "n": 7,
        "wrTP1": 28.6,
        "expR": -0.038
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
    "expR_spread": 0.998,
    "verdict": "instrument-specific"
  },
  "2m/RETEST/LONG": {
    "symbols": {
      "NQ": {
        "n": 670,
        "wrTP1": 45.4,
        "expR": 0.048
      },
      "GC": {
        "n": 435,
        "wrTP1": 45.3,
        "expR": 0.014
      },
      "CL": {
        "n": 654,
        "wrTP1": 47.6,
        "expR": 0.034
      },
      "ES": {
        "n": 651,
        "wrTP1": 48.7,
        "expR": 0.028
      },
      "YM": {
        "n": 490,
        "wrTP1": 44.7,
        "expR": 0.077
      }
    },
    "expR_spread": 0.063,
    "verdict": "universal"
  },
  "2m/RETEST/SHORT": {
    "symbols": {
      "ES": {
        "n": 320,
        "wrTP1": 50.3,
        "expR": 0.062
      },
      "YM": {
        "n": 588,
        "wrTP1": 49.3,
        "expR": 0.102
      },
      "GC": {
        "n": 479,
        "wrTP1": 49.3,
        "expR": 0.099
      },
      "NQ": {
        "n": 217,
        "wrTP1": 41.9,
        "expR": 0.042
      },
      "CL": {
        "n": 262,
        "wrTP1": 46.9,
        "expR": -0.066
      }
    },
    "expR_spread": 0.168,
    "verdict": "universal"
  },
  "5m/INV/LONG": {
    "symbols": {
      "NQ": {
        "n": 8,
        "wrTP1": 62.5,
        "expR": 0.069
      },
      "YM": {
        "n": 4,
        "wrTP1": 100.0,
        "expR": 0.617
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
    "expR_spread": 1.404,
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
        "n": 115,
        "wrTP1": 48.7,
        "expR": 0.144
      },
      "ES": {
        "n": 235,
        "wrTP1": 49.8,
        "expR": 0.178
      },
      "YM": {
        "n": 170,
        "wrTP1": 51.8,
        "expR": 0.215
      },
      "CL": {
        "n": 215,
        "wrTP1": 54.4,
        "expR": 0.242
      },
      "NQ": {
        "n": 316,
        "wrTP1": 46.8,
        "expR": 0.012
      }
    },
    "expR_spread": 0.23,
    "verdict": "universal"
  },
  "5m/RETEST/SHORT": {
    "symbols": {
      "NQ": {
        "n": 87,
        "wrTP1": 51.7,
        "expR": 0.05
      },
      "ES": {
        "n": 113,
        "wrTP1": 54.0,
        "expR": 0.107
      },
      "GC": {
        "n": 168,
        "wrTP1": 41.7,
        "expR": 0.022
      },
      "YM": {
        "n": 195,
        "wrTP1": 47.2,
        "expR": 0.163
      },
      "CL": {
        "n": 110,
        "wrTP1": 46.4,
        "expR": 0.056
      }
    },
    "expR_spread": 0.141,
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
    "n": 0
  },
  "away_from_news": {
    "n": 17993,
    "wrTP1": 46.0,
    "nSL": 8224,
    "nTO": 1484,
    "expR": 0.059,
    "pf": 1.12,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 40.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 32.7
  }
}
```

## Scoreboard de predicciones
```json
{
  "n": 7,
  "scored": 2,
  "mae_deltaER": 0.316,
  "hit_direction_rate": 50.0
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
      "2026-09-28 (lunes, primer dia con trades reales bajo el SL nuevo -- el cambio se aplico el sabado 2026-09-26 y no hubo sesion CME el domingo): se encontro y arreglo un bug en analyze.py -- eval_experiments() solo calculaba beforeN/afterN/verdict para status 'running'/'proposed', nunca para 'applied'. Como este experimento paso a 'applied' el 09-26, se habria quedado sin medicion antes/despues PARA SIEMPRE (el verdict confirmed/rejected que este mismo archivo lleva semanas anticipando nunca se habria calculado). Se agrego 'applied' a la lista de estados elegibles (mejora permanente, commit de hoy). Con el fix, el agregado (segment={'kind':'RETEST'}, sin desglose tf/side) da beforeN=17449 afterN=89 expR 0.057->0.225, verdict mecanico 'confirmed' (delta=0.168>0.05, afterN=89>=40) y dispara la alerta EXPERIMENTO CONFIRMADO en report.md de hoy. NO SE TOMA ESE VERDICT AL PIE DE LA LETRA: el desglose real por segmento en prediction_scoreboard (las lineas de predictions.jsonl por tf/side) muestra un primer dia volatil y contradictorio -- 1m LONG (n=37, la rama con mas historia e in-sample mas estable de las seis) sale con realDeltaER=-0.055, DIRECCION CONTRARIA a lo predicho (+0.152); 1m SHORT (n=33) sale con realDeltaER=+0.567, mas de 4x lo predicho (+0.143); 2m LONG/SHORT y 5m LONG/SHORT todavia con afterN de un solo digito (1, 3, 6, 9), sin ninguna base para leer direccion. Esto es exactamente el patron que el propio historial in-sample de este experimento documento una y otra vez ('lecturas con n en los cientos bajos pueden sobrestimar el efecto') pero mas extremo (aqui n esta en las decenas, no en los cientos, y es UN SOLO DIA). DECISION: el status se mantiene en 'applied', NO se sube a 'confirmed' todavia pese al verdict mecanico de hoy -- se sigue vigilando dia a dia hasta que cada segmento (no el agregado) junte afterN>=40 y, per agent-instructions.md, se vea la misma direccion sostenida 2 semanas seguidas antes de tratarlo como resultado real. Revisar de nuevo mañana con el segundo dia de dato real."
    ],
    "appliedNote": "2026-09-26: aplicado en scalp_command.pine (input sc_sl_retest_basis, default 'Auto (como se midio)'): en RETEST el SL real pasa a la mecha de la vela del retest; 1m SHORT suma la vela previa (retestBar2), igual que la medicion paralela. Base: los 6 segmentos RETEST certifican con CI90 > 0 (n=11273, E[R] 0.238 vs 0.065). El tier se sigue calculando con el stop de 3 capas. El feed NO cambia: sigue registrando el 3 capas como rMultiple y la mecha como rOrig, asi que sl_origin_vs_layer sigue siendo la vigilancia. Rige en cada grafico desde que Jesus re-pega scalp_cc_FULL_for_tradingview.pine. Revertir = poner la base en '3 capas'.",
    "beforeN": 17449,
    "afterN": 89,
    "before": {
      "n": 17449,
      "wrTP1": 45.9,
      "nSL": 8012,
      "nTO": 1424,
      "expR": 0.057,
      "pf": 1.12,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.0
    },
    "after": {
      "n": 89,
      "wrTP1": 64.0,
      "nSL": 31,
      "nTO": 1,
      "expR": 0.225,
      "pf": 1.64,
      "mfe_p25": 8.0,
      "mfe_p50": 14.0,
      "mfe_p75": 41.0,
      "winnerMAE_p75": 10.0,
      "winnerMAE_p90": 18.799999999999997,
      "loserMFEbeforeSL_p50": 3.0,
      "bars_win_p50": 3.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 38.7
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
      "2026-09-27 (domingo, REVISION SEMANAL): se agrego hoy a analyze.py el corte pendiente contra el split walk-forward (rr1_threshold_cut_oos, nueva funcion permanente) que este experimento llevaba pidiendo desde el 2026-09-22 ('pendiente evaluar este corte contra el split walk-forward OOS'). Resultado con testWeeks W38-W39 (mismo split que walk_forward.testWeeks): SOLO 5m LONG confirma fuera de muestra de forma clara -- baseline test n=544 expR=0.148 CI90=[0.056,0.247]; cortes 1.2/1.3/1.5 SUBEN el E[R] a 0.35-0.37 con CI90 que NO cruza cero (n=141-182, PF hasta 1.66) -- el patron in-sample se replica limpio fuera de muestra. Los otros dos candidatos in-sample (1m SHORT, 2m SHORT) NO se confirman: 1m SHORT sube de expR=0.052 a 0.073-0.094 con los cortes pero el CI90 sigue cruzando cero en el test set aislado (n mas chico, 425-836, falta potencia, no se descarta, solo no certifica todavia); 2m SHORT de hecho SE REVIERTE en el test set -- baseline test expR=0.058 (ya al filo, CI90=[-0.001,0.118]) y los 4 cortes dan expR NEGATIVO (-0.02 a -0.162), el corte 2.0 con CI90=[-0.382,0.05] casi enteramente del lado negativo. 1m LONG (que nunca certifico in-sample con consistencia) tambien se revierte en el test set: baseline test ya positivo (0.091) y los 4 cortes BAJAN el E[R] de forma monotona hasta 0.036 -- confirma que subir el piso de rr1 en 1m LONG no ayuda, va en contra. DECISION: no se propone sc_min_rr global. Se propone en la revision semanal de hoy (reviews/2026-week-39.md) SOLO un cambio experimental y acotado a 5m/RETEST/LONG (candidato a sc_aplus_rr o un filtro nuevo especifico de ese segmento, ya que sc_min_rr es global a todos los tf/side y subirlo global arriesga empeorar 1m LONG y 2m SHORT segun este mismo corte). Marcar 2m SHORT como alerta de metodo: un patron en apariencia solido in-sample (3+ lecturas consistentes) no sobrevivio el primer chequeo OOS real -- tratarlo como caso de estudio de por que el walk-forward es el numero que cuenta, no el contrafactual in-sample."
    ],
    "beforeN": 17538,
    "afterN": 0,
    "before": {
      "n": 17538,
      "wrTP1": 46.0,
      "nSL": 8043,
      "nTO": 1425,
      "expR": 0.058,
      "pf": 1.12,
      "mfe_p25": 8.0,
      "mfe_p50": 18.0,
      "mfe_p75": 40.75,
      "winnerMAE_p75": 12.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 4.0,
      "entryZoneTk_p50": -14.0,
      "revAfterSL_rate": 33.0
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
    "date": "2026-09-28",
    "session": "asia",
    "runType": "asia-2",
    "generatedAt": "2026-09-27T19:06:00-05:00",
    "schema": "sa-plan-2",
    "cleanest": "NQ",
    "focus": {
      "sym": "NQ",
      "verdict": "WAIT",
      "window": "17:00-01:00 CT",
      "setup": {
        "es": "retroceso a VWAP/EMA50/descuento 30845-30885.5, YA TOCADO en la reapertura (min ~30783)",
        "en": "pullback to the VWAP/EMA50 discount 30845-30885.5, NOW TAGGED on the reopen (low ~30783)"
      },
      "trigger": {
        "es": "cierre 5m de vuelta sobre 30885.5 tras el toque; sin eso, no hay entrada",
        "en": "5m close back above 30885.5 after the tag; without that, no entry"
      },
      "invalid": {
        "es": "cierre 5m sostenido bajo 30679.00 (minimo mejor defendido del viernes)",
        "en": "sustained 5m close below 30679.00 (Friday's best-defended low)"
      },
      "note": {
        "es": "la zona finalmente se toco (no paso en Asia ni Londres el viernes) -- ahora exige el cierre de reclamo, no compres solo por estar cerca",
        "en": "the zone finally got tagged (it didn't happen in Asia or London Friday) -- it now needs the reclaim close, don't buy just for being close"
      }
    },
    "summary": {
      "es": [
        "Asia-2 19:00 CT: Tokio ya abrio, feed fresco (~5 min), reapertura normal sin caidas.",
        "NQ: WAIT, el retroceso 30845-30885.5 SI se toco en la reapertura (min ~30783); ahora dentro de la zona, esperando el cierre sobre 30885.5.",
        "ES: WAIT, el retest del area rota 7783.5-7797 esta en curso, precio en el borde bajo (7784), comando lee chop/debil, sin reclamo aun.",
        "GC: WAIT, salto la resistencia fallida y ataco el equilibrio por abajo, a 2.7pts del minimo del viernes 4289.2.",
        "YM: WAIT, cayo al area POC/VAL de no-trade (51958-51991), sin tocar aun el retroceso 51844-51940.",
        "CL: WAIT, el weekend gap alcista se desvanecio casi entero, precio a 0.06pts del cluster de fade 92.79-93.25.",
        "Nada disparo entrada todavia -- focus sigue en NQ, la zona mas cerca de reaccionar.",
        "Calendario: semana de NFP (viernes 02-oct) y PCE/fin de trimestre miercoles 30-sep -- sin cambio, no afecta Asia.",
        "Limite diario $1000 (extremo bajo): con 3 stops seguidos se acaba el dia, es la cuenta completa para Jesus."
      ],
      "en": [
        "Asia-2 19:00 CT: Tokyo has opened, feed fresh (~5 min), normal reopen, no outages.",
        "NQ: WAIT, the 30845-30885.5 pullback DID get tagged on the reopen (low ~30783); now inside the zone, waiting for a close above 30885.5.",
        "ES: WAIT, the retest of the broken 7783.5-7797 area is in progress, price at the low edge (7784), command reads chop/weak, no reclaim yet.",
        "GC: WAIT, it skipped the failed resistance and attacked the equilibrium from below, 2.7pts off Friday's low 4289.2.",
        "YM: WAIT, dropped into the POC/VAL no-trade area (51958-51991)
```

## Session Analyst x resultado scalp (hipotesis AVOID rinde peor)
```json
{
  "available": true,
  "n_matched": 6953,
  "by_verdict": {
    "AVOID": {
      "n": 1454,
      "wrTP1": 44.7,
      "nSL": 727,
      "nTO": 77,
      "expR": -0.0,
      "pf": 1.0,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 32.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 33.8
    },
    "GO": {
      "n": 904,
      "wrTP1": 50.2,
      "nSL": 359,
      "nTO": 91,
      "expR": 0.187,
      "pf": 1.44,
      "mfe_p25": 12.0,
      "mfe_p50": 29.0,
      "mfe_p75": 56.0,
      "winnerMAE_p75": 17.0,
      "winnerMAE_p90": 30.0,
      "loserMFEbeforeSL_p50": 5.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -17.0,
      "revAfterSL_rate": 42.3
    },
    "WAIT": {
      "n": 4595,
      "wrTP1": 47.0,
      "nSL": 2089,
      "nTO": 345,
      "expR": 0.048,
      "pf": 1.1,
      "mfe_p25": 8.0,
      "mfe_p50": 19.0,
      "mfe_p75": 40.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 24.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 34.2
    }
  },
  "by_verdict_ci90": {
    "AVOID": {
      "expR": -0.0,
      "ci90": [
        -0.054,
        0.054
      ],
      "p_mean_le_0": 0.509,
      "n": 1408
    },
    "GO": {
      "expR": 0.187,
      "ci90": [
        0.119,
        0.258
      ],
      "p_mean_le_0": 0.0,
      "n": 841
    },
    "WAIT": {
      "expR": 0.048,
      "ci90": [
        0.02,
        0.077
      ],
      "p_mean_le_0": 0.004,
      "n": 4391
    }
  },
  "avoid_vs_rest": {
    "AVOID": {
      "n": 1454,
      "wrTP1": 44.7,
      "nSL": 727,
      "nTO": 77,
      "expR": -0.0,
      "pf": 1.0,
      "mfe_p25": 7.0,
      "mfe_p50": 15.0,
      "mfe_p75": 32.0,
      "winnerMAE_p75": 11.0,
      "winnerMAE_p90": 20.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -12.0,
      "revAfterSL_rate": 33.8
    },
    "GO_or_WAIT": {
      "n": 5499,
      "wrTP1": 47.6,
      "nSL": 2448,
      "nTO": 436,
      "expR": 0.07,
      "pf": 1.15,
      "mfe_p25": 8.0,
      "mfe_p50": 20.0,
      "mfe_p75": 43.0,
      "winnerMAE_p75": 13.0,
      "winnerMAE_p90": 25.0,
      "loserMFEbeforeSL_p50": 4.0,
      "bars_win_p50": 2.0,
      "bars_loss_p50": 3.0,
      "entryZoneTk_p50": -16.0,
      "revAfterSL_rate": 35.4
    }
  },
  "avoid_vs_rest_ci90": {
    "AVOID": {
      "expR": -0.0,
      "ci90": [
        -0.054,
        0.054
      ],
      "p_mean_le_0": 0.509,
      "n": 1408
    },
    "GO_or_WAIT": {
      "expR": 0.07,
      "ci90": [
        0.044,
        0.097
      ],
      "p_mean_le_0": 0.0,
      "n": 5232
    }
  },
  "by_kind_side": {
    "INV/LONG": {
      "AVOID": {
        "n": 14,
        "wrTP1": 50.0,
        "nSL": 5,
        "nTO": 2,
        "expR": 0.055,
        "pf": 1.15,
        "mfe_p25": 5.0,
        "mfe_p50": 7.5,
        "mfe_p75": 29.75,
        "winnerMAE_p75": 0.0,
        "winnerMAE_p90": 1.6000000000000014,
        "loserMFEbeforeSL_p50": 1.0,
        "bars_win_p50": 1.0,
        "bars_loss_p50": 2.0,
        "entryZoneTk_p50": -11.5,
        "revAfterSL_rate": 40.0
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
        "n": 63,
        "wrTP1": 38.1,
        "nSL": 31,
        "nTO": 8,
        "expR": -0.129,
        "pf": 0.75,
        "mfe_p25": 7.5,
        "mfe_p50": 17.0,
        "mfe_p75": 28.5,
        "winnerMAE_p75": 17.5,
        "winnerMAE_p90": 24.7,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 5.0,
        "entryZoneTk_p50": -14.0,
        "revAfterSL_rate": 16.1
      }
    },
    "INV/SHORT": {
      "AVOID": {
        "n": 22,
        "wrTP1": 31.8,
        "nSL": 13,
        "nTO": 2,
        "expR": -0.403,
        "pf": 0.35,
        "mfe_p25": 6.0,
        "mfe_p50": 13.0,
        "mfe_p75": 21.0,
        "winnerMAE_p75": 5.0,
        "winnerMAE_p90": 7.200000000000001,
        "loserMFEbeforeSL_p50": 8.0,
        "bars_win_p50": 4.0,
        "bars_loss_p50": 7.0,
        "entryZoneTk_p50": -10.5,
        "revAfterSL_rate": 15.4
      },
      "WAIT": {
        "n": 64,
        "wrTP1": 46.9,
        "nSL": 26,
        "nTO": 8,
        "expR": -0.01,
        "pf": 0.98,
        "mfe_p25": 6.0,
        "mfe_p50": 20.0,
        "mfe_p75": 44.5,
        "winnerMAE_p75": 16.25,
        "winnerMAE_p90": 28.900000000000055,
        "loserMFEbeforeSL_p50": 4.5,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 7.5,
        "entryZoneTk_p50": -13.5,
        "revAfterSL_rate": 26.9
      }
    },
    "RETEST/LONG": {
      "AVOID": {
        "n": 852,
        "wrTP1": 45.9,
        "nSL": 429,
        "nTO": 32,
        "expR": -0.02,
        "pf": 0.96,
        "mfe_p25": 7.0,
        "mfe_p50": 14.5,
        "mfe_p75": 33.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 19.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 3.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -12.5,
        "revAfterSL_rate": 30.8
      },
      "GO": {
        "n": 564,
        "wrTP1": 50.5,
        "nSL": 245,
        "nTO": 34,
        "expR": 0.165,
        "pf": 1.37,
        "mfe_p25": 10.0,
        "mfe_p50": 26.0,
        "mfe_p75": 52.0,
        "winnerMAE_p75": 16.0,
        "winnerMAE_p90": 27.599999999999994,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -19.0,
        "revAfterSL_rate": 40.4
      },
      "WAIT": {
        "n": 2489,
        "wrTP1": 48.6,
        "nSL": 1102,
        "nTO": 178,
        "expR": 0.105,
        "pf": 1.23,
        "mfe_p25": 7.0,
        "mfe_p50": 18.0,
        "mfe_p75": 39.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 23.0,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 35.6
      }
    },
    "RETEST/SHORT": {
      "AVOID": {
        "n": 566,
        "wrTP1": 43.3,
        "nSL": 280,
        "nTO": 41,
        "expR": 0.044,
        "pf": 1.08,
        "mfe_p25": 8.0,
        "mfe_p50": 16.0,
        "mfe_p75": 32.0,
        "winnerMAE_p75": 11.0,
        "winnerMAE_p90": 23.599999999999994,
        "loserMFEbeforeSL_p50": 3.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.5,
        "entryZoneTk_p50": -12.0,
        "revAfterSL_rate": 39.3
      },
      "GO": {
        "n": 326,
        "wrTP1": 49.1,
        "nSL": 110,
        "nTO": 56,
        "expR": 0.223,
        "pf": 1.57,
        "mfe_p25": 15.0,
        "mfe_p50": 34.0,
        "mfe_p75": 60.0,
        "winnerMAE_p75": 20.25,
        "winnerMAE_p90": 32.099999999999994,
        "loserMFEbeforeSL_p50": 6.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -15.0,
        "revAfterSL_rate": 47.3
      },
      "WAIT": {
        "n": 1979,
        "wrTP1": 45.4,
        "nSL": 930,
        "nTO": 151,
        "expR": -0.018,
        "pf": 0.96,
        "mfe_p25": 9.0,
        "mfe_p50": 20.0,
        "mfe_p75": 41.0,
        "winnerMAE_p75": 14.0,
        "winnerMAE_p90": 25.0,
        "loserMFEbeforeSL_p50": 4.0,
        "bars_win_p50": 2.0,
        "bars_loss_p50": 3.0,
        "entryZoneTk_p50": -16.0,
        "revAfterSL_rate": 33.4
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
    "n": 16120,
    "wrTP1": 46.1,
    "nSL": 7334,
    "nTO": 1352,
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
  },
  "shadow_ci90": {
    "expR": 0.062,
    "ci90": [
      0.047,
      0.08
    ],
    "p_mean_le_0": 0.0,
    "n": 15357
  },
  "raw_indicator": {
    "n": 17538,
    "wrTP1": 46.0,
    "nSL": 8043,
    "nTO": 1425,
    "expR": 0.058,
    "pf": 1.12,
    "mfe_p25": 8.0,
    "mfe_p50": 18.0,
    "mfe_p75": 40.75,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 24.0,
    "loserMFEbeforeSL_p50": 4.0,
    "bars_win_p50": 2.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 33.0
  },
  "raw_indicator_ci90": {
    "expR": 0.058,
    "ci90": [
      0.043,
      0.074
    ],
    "p_mean_le_0": 0.0,
    "n": 16730
  },
  "tier_ap_b_only": {
    "n": 8678,
    "wrTP1": 43.3,
    "nSL": 4154,
    "nTO": 767,
    "expR": 0.057,
    "pf": 1.11,
    "mfe_p25": 8.0,
    "mfe_p50": 19.0,
    "mfe_p75": 41.0,
    "winnerMAE_p75": 12.0,
    "winnerMAE_p90": 23.0,
    "loserMFEbeforeSL_p50": 5.0,
    "bars_win_p50": 3.0,
    "bars_loss_p50": 4.0,
    "entryZoneTk_p50": -14.0,
    "revAfterSL_rate": 30.6
  },
  "tier_ap_b_only_ci90": {
    "expR": 0.057,
    "ci90": [
      0.034,
      0.08
    ],
    "p_mean_le_0": 0.0,
    "n": 8271
  },
  "note": "compara el conjunto de reglas condicionales (shadow) contra (a) el indicador crudo (todo RETEST) y (b) RETEST tier A+/B solo. Gate peldano 0->1 de execution-ladder.md: shadow debe batir a raw_indicator en E[R] durante 3 semanas seguidas, n>=60 en el segmento objetivo. bootstrap_er_ci requiere n>=8, si no devuelve null."
}
```

## Modo sombra por semana (gate: shadow_beats_raw 3 semanas seguidas, n>=60)
```json
{
  "2026-W36": {
    "shadow_n": 2705,
    "shadow_expR": -0.03,
    "raw_n": 2785,
    "raw_expR": -0.022,
    "shadow_beats_raw": false
  },
  "2026-W37": {
    "shadow_n": 4173,
    "shadow_expR": 0.088,
    "raw_n": 4935,
    "raw_expR": 0.074,
    "shadow_beats_raw": true
  },
  "2026-W38": {
    "shadow_n": 4079,
    "shadow_expR": 0.11,
    "raw_n": 4579,
    "raw_expR": 0.098,
    "shadow_beats_raw": true
  },
  "2026-W39": {
    "shadow_n": 5150,
    "shadow_expR": 0.055,
    "raw_n": 5226,
    "raw_expR": 0.052,
    "shadow_beats_raw": true
  },
  "2026-W40": {
    "shadow_n": 13,
    "shadow_expR": -0.133,
    "raw_n": 13,
    "raw_expR": -0.133,
    "shadow_beats_raw": false
  }
}
```
