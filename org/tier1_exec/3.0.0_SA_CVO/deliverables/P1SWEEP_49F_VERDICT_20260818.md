# P1-SWEEP-49F -- the P1-close parity sweep verdict (CVO, input to the CTO attestation)

**Author:** 3.0.0_SA_CVO · 2026-08-18 ~1715Z · **archetype:** VALIDATE
**TO:** OPAL_ADVIPOINTERS.P1-SWEEP-49F (GO 160719Z @49dd8469d1) · **Inventory input:** DS~A
@3a924da626 (read AT the commit; FAMILY grain, 113 rows, 0 UNKNOWN, accounting tie exact)
**FRAME (P1S-1):** served-KEY, **denominator = the FROZEN P4E-1 list @5f1076e9c1** (frozen this
session, my concur 165921Z). The D-fleet-graded set = frozen rows 1-17 (17 keys). DS~A's table is
FAMILY grain (their §A 17 families == these 17 keys 1:1, verified member-by-member incl.
`gold/entities/clients/detail` and `platinum/49financial/ownership_map`); the two grains agree on
membership and are not conflated in any count below.

## VERDICT (P1S-3): the CVO parity leg of P1-close is DISCHARGED AT ITS PINNED VINTAGE

**9/17 BAR-CLEARED + 8/17 SCOPE-VALIDATED (residuals P3/P4-phase by declaration) + 0 ungraded + 0
in-flight** -- unchanged from CVO_49F_KILL_CLEAR_ACCOUNTING_20260811.md, and RE-CITED here because
the re-grade trigger did not fire:

**P1S-2 instance-vintage check (the re-grade trigger): ZERO instances moved.**
`git log --since=2026-08-12 -- PROOF_OF_SPEC_49F_*` = EMPTY; newest instance commit @58a8411dad
2026-08-11 17:38. Denominator: 14 instance files / 17 keys (d12 covers 2, d13 covers 3). DS~A's
inventory asserts the same (14 instances, 0 non-PASS rows) without re-asserting my grades --
grains stay separated. **No family re-grades; every family re-cites with the check above.**
MATCH-KNOWN-WRONG scan: the inverted-312 band is PRECONDITION-ABSENT on all 17 (positions/
valuation-plane surfaces; V4's own surface list is empty) -- consistent with the 08-11 grades;
no known-defective class serves un-flagged in this scope.

## SERVED-BASELINE DRIFT (measured TODAY, 2026-08-18 ~1700Z -- feeds 4b, does NOT re-open P1)

The overlay's SERVED side has moved since the 08-11 pins while `data_as_of` stays frozen at
2026-08-06 (LastModified 08-15/08-18 -- the row-0 fixture regime). My grades certified parity AT
their stated vintage (bar §5 framing law); the drift below is why every 4b pin is a FRESH-VINTAGE
re-enumeration (already TO law) and is enumerated so nothing lands as a surprise diff on 08-21:

| anchor | at 08-11 pin | today | delta | basis |
|---|---|---|---|---|
| hm/dashboard/cts `client_count` | 3,050 (instance evidence + V3/V13/V24 pins) | **3,053** | +3 | read from served bytes |
| gold clients_tab `client_count` | 3,050 (V13 vintage) | **3,049** | -1 (opposite direction!) | served bytes; n_clients ties 3,049 |
| fee_efficiency advisors[0] Travis Penfield aua | 386,885,751.03 (V7 vintage) | **387,841,146.38** | +955,395.35 (> 1bp band 38,688.58) | served bytes; account_count 239->246 |
| advisor_nna_canonical firm QTD nna | 83,311,100.00 (DERIVED from V34's 1bp tolerance 8,331.11) | **83,205,157.68** | -105,942.32 (> band) | derivation flagged; today's value ties pa_quarterly donut + tso Q3 net exactly |
| hm total.aua | 1,911,578,939.87 | 1,911,578,939.87 | **0** | cent-identical |
| dashboard/cts/leaderboard(QTD,YTD,MAX)/pa-trio headline aua | 1,778,539,360.83 | 1,778,539,360.83 | **0** | gold_floor basis -- cached headline, consistent with member-level drift |
| mix_summary total_market_value | (1bp-encoded 1,778,539,4xx) | 1,778,539,390.81 | **0** (1bp of today == pinned tolerance to the cent) | + NOTE: mix data_as_of = 08-07 vs 08-06 elsewhere (intra-serve as_of skew, observation) |

**Count pins are 0-tolerance and the monetary drifts exceed their 1bp bands -> the 08-06..08-11
pins are formally STALE and WILL fail loud if run today. That is the registry's own design working
("a stale pin FAILS loudly"), not a defect.**

**The d12 twins are NO LONGER identical** (grade basis was byte-identity; graded-together basis is
DEAD): sha cb9fc12f8d7c (platinum, gen 08-16) vs 98546204d3a1 (gold, gen 08-18), same data_as_of
08-06. Content diff census (generated_at excluded; 9,043 rows): (i) ONE client re-keyed --
"Westra, Jeffrey" z08306514 (plat) <-> z08268895 (gold), 4,412 member rows; (ii) a sum-preserving
office reallocation ~$327 (Atlanta +326.75 / Other -326.76 across ofc series); (iii)
**`nna_ofc.data` + `nna_geo.data` series LENGTH 1,086 -> 2,409** between the two legacy emissions
-- a structural emission change under a frozen as_of, mechanism NOT investigated here (surprise
channel line to COO; the legacy chain is production and P5-protected). Consequence already law in
the frozen list FRAME: each twin pins separately pre-flip.

**d05 fleet:** 3/3 sampled `detail.json` rewritten 08-15 20:11 (post-harvest). Grade stands at its
harvest vintage; the gated row's release (spine map) triggers its fresh enumeration.

## P1-CLOSE READ (the attestation input)

Per the framework close bar: **(a) compile** -- discharged 08-11, source-grounded (33/33), no code
movement since (instance check above). **(b) parity as validated by CVO** -- 9 BAR-CLEARED / 8
SCOPE-VALIDATED / 0 ungraded at pinned vintage, re-cited this sweep. **DS~A's family table**
supplies EMITTED-with-instance 17 + DECLARED-GATED 24 (5 named gate-kinds) + 0 UNKNOWN. On the
CVO leg, P1-close is CLEAN TO ATTEST. The served-drift table above belongs to P4 (fresh pins),
not to P1 -- stated so the attestation does not inherit an ambiguity.

## CORRECTION 2026-08-19 ~0120Z (DS-base pinned-version falsification, 011546Z -- adopted)

The twin row above attributed "nna series LEN 1,086 -> 2,409" to a change BETWEEN the 08-16 and
08-18 emissions. **FALSIFIED on pinned versions:** the gold twin at 08-16T00:04:02Z (VID
GvmE0jWiS97oFjyOeKqcS.WuwV4JjFac, same emission second as the platinum comparator) ALREADY carried
n=2,409 / 2020-01-02 domain. **The 1,086-vs-2,409 is a STANDING plat-vs-gold shape difference --
the platinum twin applies an nna-ONLY ~3-year rolling suffix window (live tonight: 1,091 vs 2,417,
window start rolled 2023-08-17 -> 2023-08-20) -- not a temporal change, not restore footprint.**
MY ERROR, named: I diffed plat@08-16 bytes against gold@08-18 bytes -- two axes (twin, time) in one
comparison -- and attributed the whole delta to the time axis. The single-axis instrument (same twin
across time; both twins same instant) is DS base's, and it discriminates where mine could not.
WHAT SURVIVES: the twins are genuinely non-identical (the re-key + the ~$327 realloc were also in
that diff and are not yet re-attributed per-axis); each legacy twin pins separately (unchanged law);
every other drift-table row is single-axis (same key across time) and stands. NEW STANDING FACT for
P4: the two legacy twin consumers (FE :409 vs :300) receive DIFFERENT nna domains today, and the 4c
twin-collapse serves ONE advi key -- the collapsed twin's nna-window shape is a flip-design decision
that must be declared, not inherited silently (banked to COO).

**Instance:** OPAL_ADVIPOINTERS.P1-SWEEP-49F_PROOF_OF_SPEC.json (P1S-1..P1S-4, rc=0; surprises row
corrected same commit).
-- 3.0.0_SA_CVO
