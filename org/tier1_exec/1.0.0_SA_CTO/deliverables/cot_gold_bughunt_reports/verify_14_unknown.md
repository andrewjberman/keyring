# VERIFY #14 -- target: unknown

- is_real: **False**
- confidence: **refuted**
- corrected_severity: low

## Reasoning
The producer half of the flag is accurate: C_01b:104 (`.where(notna() & != '', pd.NA)`) and :117 (`notna() & != ''`) only treat NaN/'' as no-advisor and pass the literal 'Unassigned' through, and A_00:495-496 does stamp 'Unassigned' when architect is populated-but-blank. So IF architect were populated, C_01b would compute a phantom (advisor='Unassigned', role='architect', aua=firm total) row. However, the flag's STATED harm is refuted at the consumer, and no concrete trigger to wrong served output exists today.

(1) Cited-scenario refutation (D_02 advisor timeseries). role_ts_lookup is populated from canonical role_aua (D_02:2020-2033) as a dict keyed by (date, advisor, role) and is only READ at D_02:2094 for advisor_name values iterated from ts.groupby('advisor_name') (D_02:2062). ts (D_02:1871) is built from `melted`, which is filtered at D_02:1805 by EXCLUDE_NAMES={'', 'Unassigned', 'unassigned', 'UNASSIGNED', 'None', 'nan'}. So advisor_name is never 'Unassigned' and the phantom canonical entry is an unused dict key. The other D_02 consumer (role_aua_snap_lookup, D_02:1164) is driven by advisors_sorted, itself EXCLUDE_NAMES-filtered at D_02:1148. The phantom is inert in BOTH D_02 paths, including under the RA-P2b canonical cutover the flag hypothesizes.

(2) By-design producer behavior. C_01b:104/117 is an exact mirror of the daily shadow writer _emit_role_aua_shadow (D_02:3038-3039, 3061). The system deliberately filters 'Unassigned' at the consumer (EXCLUDE_NAMES/_EXCL appears in every consumer: D_02:1142/1784, D_00c:199; D_00b:803-811 explicitly folds 'Unassigned' into 'Other', and its canonical role_aua path is hard-disabled `if False` at D_00b:791). Not filtering at the producer is the intended pattern, not a defect unique to C_01b.

(3) Dormant + no concrete current trigger (flag concedes, verified). cot architect is all-NaN (A_00:495 empty-series assign yields NaN), so C_01b's fallback (line 213) reads an all-NaN architect -> _n_roles=0 for every account -> every partition returns empty (line 107-108). No phantom row is even written today. The trigger requires ADVI_COTPPLADVFIX to first populate architect (a future state), not a current input.

(4) Honest caveat (does not rescue the flag). D_01:1046 (RA-P4 override) iterates role_aua_snap.items() directly rather than keyed-lookup, and WOULD carry an 'Unassigned' phantom into the architect donut (line 1049-1064) if it fired. But that is a DIFFERENT consumer than the flag cited, and is triple-gated: architect must populate (dormant), role_aua_snap must be non-empty for cot, and the advisor/role-AUA donut must be a rendered cot-v1 surface (deferred -- cot v1 is Distribution-GEO-only per C_01b:209-211). It is also not caused by C_01b uniquely (the daily D_02 shadow writer produces the same latest-date partition identically).

Verdict: the specific cited harm (D_02 timeseries surfacing a fake 'Unassigned' advisor at 100% firm AUA) is concretely refuted by the EXCLUDE_NAMES filter at D_02:1805 + keyed-lookup consumption; the compute path today produces correct (empty) output; the residual same-class exposure (D_01 RA-P4) is dormant and multiply-gated. Corrected severity low (latent consumer-guard fragility worth a producer-side 'Unassigned' filter for robustness, but not a currently-fireable served-number defect).
