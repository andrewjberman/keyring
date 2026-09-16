# POSN_ASTTAX round 7 - L9 judgment completion

The X1 proof instance is structurally valid. X1-AC7 is graded against the measured guard/write-surface comparison.

```json
[
{"id":"POSN_ASTTAX-Z-C-S181","project":"POSN_ASTTAX","fabric":"site-z","surfaced_by":"3.0.0_SA_CVO~Z","surfaced_at":"2026-09-15T14:20:00Z","one_line":"X1-AC7 confirms the guard owns exactly the seeder's three data fields; management_style is outside that seeder write and requires a separate R1 guard act.","class":"OBSERVATION","hazard_standing":"INERT","grounding":{"status":"GROUNDED","evidence":["org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~27/POSN_ASTTAX.TO-X1-1.seeder-guard-reconciled-with-the-retag-write-surface.proof_of_spec.json@2cdca2a27d04469f69cabda2f62044938c739f0a"]},"disposition":"GRADUATED","spec_asserts":"X1-AC7 asks whether guard-owned fields equal the seeder write surface and whether R1's management_style write needs its own guard.","world_is":"The SET clause and YANG_OWNED_FIELDS agree on asset_class, sub_asset_class, and name; management_style is in neither. Mutant and live scratch controls discriminate the separate R1 case.","notes":"PASS for the seeder guard; the separate R1 management_style guard remains an explicit follow-on cell.","grades":[{"criterion":"X1-AC7","instance":"org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~27/POSN_ASTTAX.TO-X1-1.seeder-guard-reconciled-with-the-retag-write-surface.proof_of_spec.json@2cdca2a27d04469f69cabda2f62044938c739f0a","verdict":"PASS","reason":"Three of three seeder-owned fields match; management_style is correctly identified as outside this writer."}]}
]
```
