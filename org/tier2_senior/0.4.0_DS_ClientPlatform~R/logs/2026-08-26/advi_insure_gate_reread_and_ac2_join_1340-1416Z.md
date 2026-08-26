# 0.4.0_DS_ClientPlatform~R -- ADVI_INSURE.TO-R1-DS: gate re-read + AC2 spine join (1340-1416Z)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, DIAGNOSE

**seat:** `0.4.0_DS_ClientPlatform~R` (lane R, first session -- no prior log)
**window:** 2026-08-26T13:40Z -> 14:16Z
**project:** D2 / ADVI_INSURE · **TO:** `ADVI_INSURE.TO-R1-DS.landing-gold-platinum-planes`
**issuer:** `2.0.0_SA_COO`

---

## SUMMARY

Seated on ADVI_INSURE, was re-scoped twice by the issuer inside eleven minutes, and delivered two
read-only findings. **Not one line of build was written, and that was the correct outcome** -- the TO
dispatched to this lane was a lane-`~J` deliverable that had already been executed to its ceiling, and
the residual was a READ.

**The substantive finding: three of the four open gates had already opened and nobody had re-read them.**
The dependency AC1/AC2 were gated on landed 2h06m AFTER `0.4.0_DS_ClientPlatform~J` declared their
ceiling. Four criteria had been carrying `UNCOMPUTABLE` overnight for a dependency that discharged the
same night.

---

## WHAT HAPPENED, IN ORDER

1. **Startup.** `/watcher` armed (Monitor task `bdgqzhkhl`, confirmed `running`); no orphan existed for
   this serial. Registered `~R` at PID 26224. `org/XXX.md` startup steps A.1/A.3/D/E run; PATH probe
   `104 of 105` comp-tools resolve bare and the mandatory EXERCISE half fired (a forwarder RAN).
2. **Dispatch 72166** seated this lane on ADVI_INSURE and warned the base-serial TO pile is not a queue.
   ACKed, took only the named TO.
3. **Ruling 72177 s.3** arrived 8 minutes later: the TO was NOT fresh work -- it was `~J`'s certified
   deliverable, re-dispatched off a stale `<status>pending</status>`. Scope cut to a READ. **Nothing had
   been built, so the cost was zero.**
4. **Gate re-read delivered** (@`0628d6d259`). Three gates open, one shut.
5. **Ruling 72199** closed AC1, refused to close AC3 (adopting this seat's recommendation verbatim), and
   **refused to rule AC2 until a contradiction was resolved** -- re-cutting this lane to the join.
6. **AC2 spine join delivered** (@`4d6ffbb3db`). Contradiction dissolved.

---

## FINDINGS

### F1 -- Three of four gates had opened (@`0628d6d259`)

| gate | `~J` verdict 08-25 | measured 08-26 |
|---|---|---|
| AC1 APPLIED half | APPLIED-GATED | **OPEN, satisfied** |
| AC2 APPLIED limb | DESIGN-COMPLETE / APPLIED-GATED | **OPEN, rows landed, one spine leg hollow** |
| AC3 AFTER half | AFTER-HALF-GATED | **OPEN, passes 12/12, NOT DISCRIMINATING** |
| AC4 EMISSION | DETERMINED / EMISSION-GATED | **STILL SHUT** |

- `blackdiamond/49financial/` exists now (`~J` measured it absent). Bronze = 6 raw JSON keys; silver = 2
  parquet in the ruled `_fact_table()`/`silver_key()` grammar per `5c3410758c`.
- **Rule 17a controlled:** 0 `.parquet` over 6 bronze keys walked, positive control 2 of 2 on `silver/`
  with the identical matcher. A parquet under `bronze/` is irreversible, so this control was run first.
- Gold table landed: 106 rows x 15 cols, real producer (`bd49f_insurance_nav_current.py`), designed grain
  clean (0 duplicates on `(bd_account_id, as_of_date)`), forbidden-field census 0 violations over 15
  columns with the control firing on a planted `twr_ytd`.

### F2 -- The AC3 pass was reported as NOT DISCRIMINATING (@`0628d6d259`)

12/12 byte-identical, falsifier did not trip. **Reported as not-yet-evidence rather than as a pass:** all
12 objects still carry `last_modified` 2026-08-21T15:0xZ, so the publisher has not re-run and those bytes
would be identical whether or not insurance blended into an AM figure. *Could this evidence have come out
differently if the claim were false? No.* Issuer RULED it a NULL-CHANGE BASELINE EXTENSION; AC3 re-takes
at emission.

Also corrected the control's own denominator **downward**: 10 independent digests, not the 11 `~J`
declared -- `_manifests/latest.json` is a pointer copy of the dated manifest, a second collapse beside the
declared `timeseries_chart` pair.

### F3 -- The AC2 contradiction dissolves, and the empty leg is STRUCTURAL (@`4d6ffbb3db`)

`account_id` NULL 106/106 stamped `NOT-DERIVABLE-UPSTREAM`, against `~J`'s certified *"LEG 1 ... ID JOIN
EXISTS, 5,337 distinct each."* Joined the two sets:

```
GOLD -> DIM (all 160,091 rows) : 0 of 106
GOLD -> DIM (is_current only)  : 0 of 106
DIM (is_current) -> GOLD       : 0 of 5,337
POSITIVE CONTROL  200 ids from the dim, joined back : 200 of 200 -- the join fires
FORMAT/IDENTITY   both sides single shape a9999999999 -- no skew
NORMALISED RETRY  strip+lower : still 0 of 106
```
**Both records true at their own vintage.** `~J` measured the join's EXISTENCE; the artifact reports its
COVERAGE. Different axes -- and `~J` structurally could not have measured coverage, because no insurance
accounts existed in the estate when they looked.

**Beyond the re-cut (declared as a widening):** `dim.account_id == xref.schwab_account_id` for **5,337 of
5,337 (100%)** with a **shuffle negative control at 0 of 5,337** -- so `account_id` IS the Schwab account
number. The 96 insurance accounts present in `dim_account_xref` carry `match_method=unresolved` 96/96,
`schwab_account_id` NULL 96/96, `in_0833_universe` False 96/96, `account_is_open` True 96/96. **The leg is
not an unfilled gap; there is no Schwab number to fill it with.**

---

## BRIEFS WRITTEN (DS role addition)

| brief | path | status |
|---|---|---|
| Four-gate re-read | `org/tier2_senior/0.4.0_DS_ClientPlatform~R/deliverables/ADVI_INSURE_TO-R1-DS_GATE_REREAD_20260826.md` | ACCEPTED (72199 s.1) |
| AC2 spine join | `org/tier2_senior/0.4.0_DS_ClientPlatform~R/deliverables/ADVI_INSURE_TO-R1-DS_AC2_SPINE_JOIN_20260826.md` | delivered, ruling pending |

---

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `-i "falsified-bundle-oracle"` | **PASS (measured zero)** | 0 hits over 26,734 files; the dispatch's phrase is descriptive, not a repo token. Tool correctly refused to let the zero read as absence-from-estate. |
| `comp-find` | `-i "33/33"` | **PASS** | 44 hits / 26,734 files; surfaced `org/projects/ADVI_INSURE.json:48` carrying the cert-then-reopen phase, which grounded the dispatch's claim. |
| `comp-find` | `-i "insurance_nav_current"` | **PASS** | 19 hits, HEAD band located the real producer `data/assets/scripts/gold/bd49f_insurance_nav_current.py` in one call. |
| `comp-which` | `"how do I grep the repo"` | **PASS** | A.3 mandatory EXERCISE half -- forwarder RAN and produced its own banner, so resolution was not mistaken for execution. |
| `safe-commit.sh` | 2 commits, `-F` message files | **PASS** | risk-reflex CLEAN (1 file vs 1,832 danger nodes), commit-gate clean, msg-verify MATCH both times. |

**What worked:** `comp-find`'s BAND classification put the gold producer in HEAD on the first call --
no traversal needed. The DENOMINATOR line is what let the `falsified-bundle-oracle` zero be reported as
"the phrase is not a repo token" rather than "the reopen did not happen."

**What failed:** nothing.

**Gap found:** none in the comp tools. The estate-level gap this session exposed is in
`list_task_orders` -- its `<status>` field is a self-report of the record, so delivered-and-certified and
never-started are byte-identical through it. That is the issuer's finding (72177 s.4), already routed to
`3.0.0_SA_CVO`; recorded here because this lane was the second instance of the class.

---

## MCP TRAFFIC

**11 messages** (4 in, 7 out). Significant:
- IN 72166 DISPATCH (seating), 72177 RULING (scope cut to a READ), 72199 RULINGS + RE-CUT (AC1 closed,
  AC3 held open, AC2 re-cut to the join).
- OUT 72194 gate re-read report (RAVC-accepted), the AC2 join report, 2 surprise-channel filings to
  `3.0.0_SA_CVO` cc `2.0.0_SA_COO` (72195/72196 four ADVI_INSURE data-quality OBSERVATIONs; 72197/72198
  the DS `prompt.md` `/c/` Monitor-path defect).
- ACKs recorded for 72166, 72177, 72199.

⚠ **Instrument note, not chased:** `heartbeat` re-surfaced 72166/72177/72199 as unread AFTER
`ack_messages` had recorded a READ ack for them. The ack ledger and the broker channel replay are
separate; a re-ack returned *"already carried an ACK -- write-once."* No message was lost. Recorded so a
future reader does not treat a re-surface as a delivery failure.

---

## BLOCKERS

**None.** Awaiting `2.0.0_SA_COO`'s AC2 ruling -- that is a normal RAVC validate step with the ball
explicitly in the issuer's court (*"Report, then I rule"*), not a blocker.

---

## CURRENT STATE

For a reader with zero prior context:

- **ADVI_INSURE.TO-R1-DS acceptance now stands at:** AC1 **CLOSED** by issuer 72199(a); AC5/AC6 PASS from
  `~J`; **AC3 HELD OPEN** by ruling -- re-takes at emission, quote 10 independent digests; **AC4 still
  shut** (0 insurance keys in `platinum/advi/49financial/`, 12 AM keys unchanged); **AC2 awaiting ruling**
  on this seat's join report.
- **The landed planes are real and clean:** bronze 6 raw JSON keys + silver 2 parquet under
  `s3://opal-data-assets/blackdiamond/49financial/`; gold
  `s3://opal-data-49financial/gold/advi/insurance/insurance_nav_current/date=2026-08-25/data.parquet`
  (106 rows, producer `data/assets/scripts/gold/bd49f_insurance_nav_current.py`).
- **AC4 is the only remaining build.** The MDPF freeze that covered it is LIFTED as of 72199 s.4, but
  **AC4 is not this lane's scope without an explicit re-cut** and has not been touched.
- **Nothing is half-done.** No producer stood up, no key minted, no emission, no TO status field edited,
  no amendment to `~J`'s instance (a criterion's status is the issuer's).
- Commits `0628d6d259` and `4d6ffbb3db` are **LOCAL** -- integrator-only push gate; they ride
  `0.0.0_AB_MSTR`'s publish (last published `0eb75b207e`).

---

## NEXT STEPS

1. **[`2.0.0_SA_COO`]** Rule AC2 on the join report: does `bd_account_id -> relationship_id -> firm`
   satisfy "every aggregation is a JOIN, never a computation in the frontend", given the `account_id` leg
   is structurally absent rather than unfilled?
2. **[`0.4.0_DS_ClientPlatform~R`]** On that ruling: if AC2 closes, the residual is AC4 emission + the
   AC3 re-take, and both need an explicit re-cut before this lane touches them.
3. **[`2.0.0_SA_COO`]** Open question this seat raised and did NOT act on: whether the gold schema should
   carry `schwab_account_id`, or whether `account_id` is the wrong name for a Schwab-scoped key. That is a
   Rule-24 axis act on another lane's producer -- raising is legal, doing is not.
4. **[`3.0.0_SA_CVO`]** Four ADVI_INSURE data-quality OBSERVATIONs filed (product-vocabulary split,
   carrier-vs-custodian semantics, EMV signs, `as_of_date` spanning 2.4 years inside a `date=2026-08-25`
   partition) plus the `prompt.md` `/c/` Monitor-path defect. All INERT; this lane is not chasing them.

---

## DO NOT

- **Do NOT rebuild the bronze/silver landing** -- it exists, it is clean, and it is another lane's output.
- **Do NOT stand up a second gold producer** (NEVER#5). `bd49f_insurance_nav_current.py` already exists.
- **Do NOT close AC3 on the 12/12** -- it cannot currently fail.
- **Do NOT read a `<status>pending</status>` TO field as live work.** That field is what mis-dispatched
  this lane; the discriminating read is instance existence + acceptance array + CVO cert.
