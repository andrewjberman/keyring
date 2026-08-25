# 2.0.0_SA_COO — SESSION LOG, 2026-08-24 22:26Z → 2026-08-25 01:00Z

**archetype:** COORDINATE

**Continues** `2026-08-24/SESSION_2226Z_STAGE3_DECOMPS_AND_ROUND1_DISPATCH.md` (19:26Z→22:2xZ). This log carries the
delta only. **Commits this window: 9** (24 across the session, anchored count — see §5).

---

## 1. ⛔ CURRENT STATE — the handoff

| project | `dep_stage` | where it stands |
|---|---|---|
| **D1_CATVIEWS** | EXECUTING | 28 certified cells in flight (`DS~F`, `DE~C`); **scope RE-OPENED to 31**, v2.1 re-certified by **CTO as alternate signer** @5eaa41585f; both re-cert P1s + the P2 landed @d82b3d55ec; SMA separability SUPERSEDED by Andrew @ce04a311eb |
| **ADVI_PERFRP** | EXECUTING | `DS~G` / `DE~D` / `AE~G` all delivering; contract at **0.3.0-skeleton**, 11 RATIFIED / 1 PROPOSED |
| **ADVI_STITCH** | EXECUTING | Phase-A TOs cut @0c337e4fbb; **seating deliberately not requested** (§3) |
| **ADVI_INSURE** | DECOMP | certified @7397dfd83e, then **RE-OPENED 33→36** @2f5d1411f4; awaiting CTO's alternate-signer re-cert |

**Nothing at this seat is half-landed.** Every ruling is either in a decomp/TO on disk or routed with its owner named.

---

## 2. Three re-opens, and why only two were mine to call

**A DECOMP-INVALIDATING item is an UNENUMERATED OPERATIVE SURFACE — not a bad oracle on an enumerated one.** I held that
line in both directions this window, and the distinction did real work:

| item | call | why |
|---|---|---|
| `PRF-inv-1`'s unrunnable bundle oracle | **AMEND, no re-cert** | the cell existed, its intent was right; only the ORACLE was unrunnable |
| D1's missing path-to-live | **RE-OPEN** (28→31) | a surface nobody enumerated — postulate (i) |
| INSURE's missing path-to-live | **RE-OPEN** (33→36) | same class, second project, answered CVO's own question on the cert's face |

**Both re-certs go to base CTO, not CVO** — the pipeline's self-certification break, and the CRO class is off-limits.
**Neither CVO cert is impeached:** each was true of what it read, and CVO named the INSURE gap themselves.

⛔ **THE INSURE (h) SURFACE CARRIES AN EXPLICIT ANTI-INHERITANCE CLAUSE, which is the reusable part:** D1's producer sits in
`mdpf-gold-lambda` behind a PINNED package across two code channels; INSURE's is a new script in the **49F runner chain — a
different execution vehicle whose pinning is UNMEASURED.** `INS-h-1`'s first act is to MEASURE it. Reasoning from the
neighbour would be the wrong-plane error one project over.

---

## 3. Rulings issued this window (13) — the ones a successor must not re-litigate

**Serving shape:** round 1 emits ONE OBJECT PER FAMILY (entity-keyed map); **the publisher is NOT extended** — a fan-out mode
on the estate's single serving producer is CTO-arch territory and would be a standing-second-channel by accident inside a
round-1 cell · N is TWO NUMBERS (11 families FIXED, objects DATA-DEPENDENT; criteria measure families) · `PRF-c-3` runs
**after the c04 battery** — a c04 abort must BLOCK a client-facing performance projection.
**Data semantics:** UNRESOLVED is a fifth flow class, propagated as its own state, **excluded from all four netting
buckets** · the shallow-history THIRD STATE is carried per-column and **never merged into declared-absent** (no source vs
no history — different remedy, different owner) · measure RECOVERABLE-vs-STRUCTURALLY-ABSENT **before** planning any
remedy · BD-plane Custom members go in a registry-side table, never the crosswalk · the crosswalk→member_id map is
authorized as DATA with both id families named; **display-name matching REFUSED**.
**Process:** executing seats SURFACE surprises by MCP, **CVO files** (no registry widening) · **evidence at a NAMED REF,
never the shared working tree** (§4) · seating-lint refusals reach MSTR as a BATCH; a lane is reapable when its last cell
flips AND its proof instance is checker-VALID, **not when it goes quiet**.
**Routed, not decided:** the Transactions spec collision · the Allocation card · the `a4_expected` contract edit · the
Moderate Income stored-class question · the twr_daily mechanism · the never-rules-gate false positive.

---

## 4. ⛔ My own defects this window — four, and one is the sharpest of the night

**(a) `sma_separable: false` — A CONTROL THAT COMMITTED THE EXACT ERROR IT WAS BUILT TO PREVENT, IN THE SAME RULING.** I
mandated the marker so a renderer could not infer something false; Andrew's word (*"only 49 has 'SMAs' category items"*)
makes it **a positive claim about money that does not exist** — it tells the renderer SMA dollars hide inside Client for
firms that have none. Strictly worse than the omission it replaced, **and I mandated it in the same ruling where I refused
to let an absent predicate render as a zero.** The two-edged law, now carried by every lane: *a MISSING PREDICATE rendered
as ZERO claims a measurement nobody took; a TRUE ABSENCE rendered as UNAVAILABLE claims there is something to measure.*
**(b) I declared INSURE uncertified NINE MINUTES AFTER it was certified and on origin** — and did it in the message where I
told CVO there was no pressure, so the error cost time while sounding considerate. *(CVO's correction accepted: the
ORDERING was right — holding TOs against a cert I could not see is the correct default, and cutting on an unconfirmed cert
is what their earlier false-closure sentence invited.)*
**(c) I FIXED THE INSTANCE AND NOT THE CLASS.** INSURE's `inv-2` carried the same falsified oracle I had corrected on
PERFRP an hour earlier. Caught by CVO's check 7 — its first real catch, on a night whose entire lesson was the class.
**(d) `R-p4` double-counted Transactions** (a card-level pair AND its own paged key) — found by a seat trying to USE the
enumeration rather than read it.

**AND ONE NEAR-MISS WORTH MORE THAN THE DEFECTS:** a python step exited 1, `&&` short-circuited before its heredoc, and
`safe-commit -F` ran anyway. **It failed LOUDLY only because that filename did not yet exist.** Had I reused a name from
earlier in the same session it would have committed silently under a stale subject. **The discriminator was the accident of
a path, not any discipline of mine** — and I wrote eleven message files that session under a predictable scheme.

---

## 5. Compiler Tools

| Tool | Result | Gap / lesson |
|---|---|---|
| `git log --author='<serial>'` | **18 loose == 18 anchored**, 1 distinct author | ⛔ **`--author` SUBSTRING-MATCHES ITS OWN LANES.** Mine came back clean ONLY because my lanes were dark — `2.0.0_SA_COO~*` has 15 commits in history. AE~G measured a **906-commit / 29% inflation** on their base. Anchored form (`^serial <` + `--perl-regexp`) adopted permanently |
| `git log --since` | **returned 0 on 17 real commits** | ⛔ reads LOCAL time; I passed UTC. Re-counted with `%aI`, which carries its own offset |
| message-integrity check (4 forms) | form 4 works: **rstrip both, report first differing index** | ⛔ **ROOT CAUSE REPRODUCED HERE: `--format=%B` and `--pretty=format:%B` give +1 and 0 for the SAME file and commit** — the byte arithmetic tested exactly the byte the two spellings disagree about. **Now moot: Andrew ruled it into `safe-commit`, and `[msg-verify] MATCH` fires on my commits** |
| `aws s3 ls` (rail-checked) | 30 bd prefixes vs a 4-prefix territory; `canonical_positions` **4 partitions floor 2026-08-18** vs `canonical_valuation` **530 floor 2024-07-08** | The contrast control is what made the shallow finding legible; a floor read without one proves nothing |
| `aws s3 ls` on the SILVER inputs | `dim_position` **535 partitions to the SI floor** | Handed to DS~G as a LEAD, not a conclusion — it became the recoverable-vs-absent discriminator |
| `grep -o` cell-id control | 28 / 36 / 33 / 32 / 31 / 36, run **before every commit** | Caught my own 20-of-28 shortfall on D1 v2 before CVO could; the count closed only when PRINTED, three times |
| bidirectional `cell_refs` control | 0 unresolved on all 7 TOs | Caught a real defect: TO-1's decomp_ref claimed `ETFS-a-1`, which no criterion discharged |
| `proof-of-spec-check.py` | 3/3 ETFS instances VALID with the join computed | ⛔ its harvest reads EVERY id in `<decomp_ref>` as a CLAIM — **an exclusion clause is INVERTED into a claim.** Fixed by RELOCATION into a sibling element, never deletion |
| `safe-commit.sh` | 9 commits; 2 audited lane overrides (singular, never `--force`) | ⛔ the never-rules gate **denied a correctly-`-F` commit** because the flag token sat in the document's own PROSE — restructured, did not override |
| `comp-find` / `--name` | every PRD, TO and source located | No gap this window |

---

## 6. For the next seat

1. **INSURE's second re-cert is at CTO**; its TOs stay uncut until it lands. STITCH's TOs are cut and **unseated by choice**.
2. **Five lanes are live and disciplined** — every one verified its own start condition rather than trusting a message, and
   four filed findings against their own prior reports. Read what they send; they are more reliable than my rulings were.
3. **Four calls are at Andrew** (per-Partner rulesets · the ~$7M referent · IDVZ/PFDE at SMA L1 · the third bucket's label).
   CTO holds two more; do not double-list them.
4. **Nothing is pushed by this seat.** Say "LOCAL @hash, rides integration" — and cite the commit's own stat, never
   `git log -1`, which in a shared worktree is another seat's clock.
