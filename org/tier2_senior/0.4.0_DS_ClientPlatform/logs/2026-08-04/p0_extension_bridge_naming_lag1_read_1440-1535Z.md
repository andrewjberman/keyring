# P0 extension: global+inflection legs; bridge hop named + accepted; LAG=1 read (leak found)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-04 ~14:40Z -> ~15:35Z (delta since p0_49f_aum_metrics_leg log)

## Arc

1. **CTO accepted Leg-2 for 49f** (144951Z) on my + COO's dual evidence; my held roll-forward
   one-hunk AUTHORIZED post-Leg-4, normal reviewed path.
2. **P0 EXTENSION executed** (CTO 144858Z-c via COO 145157Z; 0.2.0_DS dark): fired GLOBAL
   (14:55:58Z, dual-emit portfolios/aum-metrics.json BY DESIGN) + INFLECTION (14:56:02Z) via
   `dim_mdpf_aum_metrics.py --firm X --upload`. Water-tested both: per-model tie 7/7 each TO
   THE CENT (global needed the LEGACY served label map — its rows use legacy display
   vocabulary by served-parity design; excluded universe = opal_growth_sma/opal_div_sma,
   F2-class); totals internally exact (global 1,963,658,339.15 / inflection 204,775,547.30);
   period=2026-07-30 both, INTERIM per the supersede ruling. Reported 151208Z/151315Z.
   **CONTENT FINDING: global's meta LACKS source_spine/as_of_basis/firm_id** (49f +
   inflection carry all three) — vintage still carried top-level; one-hunk meta extension
   proposed for the post-Leg-4 window.
3. **The 49f platinum seam -> BRIDGE HOP NAMED** (CTO ask 2 / COO 151326Z item 2 / AE
   151144Z): platinum had aum-metrics for global/inflection/cottonwood, NOT 49f. Named from
   source + live state, ACCEPTED by COO 152839Z as "the definitive mechanism record":
   - Mechanism: `build_portal_gold_accrual.py` = the single R1 rename boundary
     (gold/mdpf_revamp underscore -> portal/gold/mdpf/{scope}/{type}/{date}.json hyphen;
     date = the artifact's OWN period; R5 never-overwrite). Production step:
     `mdpf-accrual-trigger` Lambda, cron(45 15)Z + `--only DST_KEY` repair path.
   - Publisher `opal-assets-mdpf-portal-publisher` derives (scope,type) from the LISTING —
     never hand-lists — and carried 49f automatically once the dated file existed.
   - Negative attributions that pinned it: latest logged accrual run 13:40:21Z correctly
     R4-errored aum-metrics x3 (pre-fire); live get-bucket-notification-configuration on
     opal-data-assets = 8 configs ALL bronze->silver, NOTHING on gold/, EventBridge None.
   - My [INFERRED] per-key-repair attribution CONFIRMED by COO: 0.2.0's chain ran the
     accrual `--only` their two scopes at 14:56 (the 5-9s reaction I measured); 0.2.0 fired
     `--only` 49f at 15:24:24Z, dated key stage-confirmed byte-identical; my R5-skip
     prediction matched their written=1 errors=0 exactly. Event CLOSED; nothing further owed.
   - Guard note: one malformed send (placeholder body, wrong from_agent) was correctly
     REFUSED by the NFRA_IDENTITY G-A sender guard — the guard working as designed; the real
     message re-sent clean 152809Z.
4. **LAG=1 first-fire read (ADHOC lane, reported 153215Z):**
   - PRIMARIES PASS: all three snapshot tables landed T-1(=07-31) FULL at 02:06Z (holdings
     1,161,436B / allocations 346,228B / unrealized 4,726,152B); no T-day primaries.
   - **LEAK: the retry-net re-opened the partial hole.** Marker
     `_retry_net/2026-08-04.json` (02:06:36Z): sweep ran run_date=2026-08-04 (UTC basis)
     while primaries keyed off the ET run-day — so Monday 08-03 fell IN-window, read
     UNKNOWN-OR-ABSENT x3, was re-pulled; allocations (40,701B) + unrealized (36,177B)
     landed T-day PARTIALS passing the 0-data-row guard (:712) — the exact class LAG=1
     closed at the primary leg, re-entering via the sweep. Holdings: no 08-03 file
     (pricing-floor limb :733 presumably refused; marker says relanded — residual unknown,
     named).
   - **CLOCK: tonight's ~02Z run marks 08-03 INFERRED-PRESENT (">=1 data row" probe — the
     legend itself says "a partial landing also passes") and stops re-pulling — the partial
     FOSSILIZES.** Latest-snapshot consumers already select the 08-03 partials over the
     07-31 fulls (the A_00/A_01 near-empty class). Fix shape + interim
     delete-the-two-partials option surfaced to COO; deletion + code fix both HELD for word.

## Compiler Tools

| run | observed | verdict |
|---|---|---|
| water-test probes global+inflection (head+get+tie) | first global/inflection tie pass showed all-?? = MY probe's map gap (dm-dict harvest found no label dict; fallback dropped); re-run with spine display_name map -> inflection 7/7 TIE; global needed the LEGACY label map -> 7/7 TIE | probe corrected at the mapping, artifacts clean; universe/mapping errors are probe errors until proven otherwise (2nd instance this session) |
| `comp-grep "mdpf_revamp" infra/aws/terraform` + accrual/publisher source reads | publisher TF + Lambda located; derive-from-listing grammar confirmed at source (:88-108) | the naming's source base |
| live primitives: get-bucket-notification-configuration, accrual-bridge-runs logs, retry-net marker, platinum/portal-gold/bronze listings | per arc above | applied-truth layer per Rule 22a |
| `comp-pipescript deployed dim_mdpf_aum_metrics.py --pipeline mdpf` (pre-fire, prior window) | MATCH | carried from prior log; no re-run needed for the re-fires (same session, same tree) |

## Do NOT (successors)

- Do NOT treat the global aum_metrics meta-provenance gap as a serve blocker — CTO's
  vintage-carrier ruling stands; it is a one-hunk for the post-Leg-4 window.
- Do NOT delete the 08-03 cot partials without COO/Andrew word (data deletion).
- Do NOT re-derive the 14:56 dated-file writes as an event-driven bridge — CONFIRMED as
  0.2.0's per-key `--only` accrual fires; there is NO S3 notification on gold/.

## Blockers

None. Event-waits: Orion-fix supersede re-fire (all four scopes, mine to re-fire for
49f/global/inflection when the word lands); CTO fork rulings (CANRTE Phase B); post-Leg-4
window (two one-hunks: roll-forward resolver + global meta); COO word on the cot partial
fossilization clock (tonight ~02Z).

## Next Steps

- [0.4.0_DS_ClientPlatform] (me): 00:00Z bd-plane no-behavioral-delta read (last open
  scheduled-evidence item); then T4.A residue as fill; re-fires + one-hunks on their gates.
- [2.0.0_SA_COO]: cot partial-fossilization word before ~02Z; LAG-basis fix GO if wanted.
- [1.0.0_SA_CTO]: F-1/F-2/F-3 rulings when ready (design at your desk since 13:51Z).
