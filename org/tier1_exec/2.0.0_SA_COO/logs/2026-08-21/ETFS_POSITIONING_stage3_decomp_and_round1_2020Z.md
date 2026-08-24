# 2.0.0_SA_COO — ETFS_POSITIONING stage 3 + round 1

**Session span:** 2026-08-21 ~19:45Z → 2026-08-24 ~12:50Z (spans a date roll; filed under the start date).
**Seat:** fresh COO, seated deliberately by the prior seat's scoped handoff (`c824996551`).
**Archetype:** issuer / coordinator run. **Commits authored:** 13 (`308fcaea0d` … `20c092c0da`).

---

## 1. What this session was

Andrew, twice, verbatim: ***"Make it clear to the fabric that I want ETFS_POSITIONING DONE RIGHT NOW.
IT IS PRIORITY FOR THIS SESSION"*** and ***"PLEASE MAKE SURE THE CANONICAL EXECUTION PROJECT I MANDATED IS
FOLLOWED EXPLICITLY."*** One instruction: full speed **through** the Rule-27 pipeline, never around it.

**Stage 3 was mine.** It went stage 1→4 inside one session: decomp → certification → five TOs → four lanes
executing → a live artifact rendering the page.

---

## 2. Delivered

| # | Act | Commit |
|---|---|---|
| 1 | Stage-3 decomp — enumeration, cells, four-postulate record, L1 alignment | `308fcaea0d` |
| 2 | Round-1 TOs (DS producer · AE serving · DE portal), `dep_stage`→EXECUTING | `10f94e4f13` |
| 3 | Amendment A+B — route RULED `platinum/etfs/`; producer is TWO STAGES | `cc7eca2da3` |
| 4 | §6 rewritten on CVO's refusal | `f7c719b56d` |
| 5 | Amendment C — advi restore folded into the etfs edit, ONE apply | `6299ec7098` |
| 6 | Amendment C+D — minted `e-4`, `e-5`; corrected my own AC4 | `51185358a9` |
| 7 | ADVI_49F correction — the "tree-wide floor" falsified | `aed671d85f` |
| 8 | Andrew-direct record — egress granted | `d3c0c9c1d2` |
| 9 | TO-4 cut — `c-1` leaves the uncovered set | `9256243a5d` |
| 10 | TO-5 cut + TO-1 Amendment B — the mis-cut schedule criterion | `124200ad45` |
| 11 | Amendment E — `f-2` sized wrong (12 not 5); my binding discriminator falsified | `1018a9cebc` |
| 12 | owned-paths correction — a note asserting a control that does not exist | `efa1fb879a` |
| 13 | Andrew-direct record (DIVZ/IDVZ) + Amendment F — the UNITS gap | `20c092c0da` |

**Final alignment:** 26 criteria / 23 cells / 16 covered / 7 uncovered / **zero ghost refs** — re-derived, never
re-typed, after every amendment.

---

## 3. Rulings I made

1. **The ETF artifact is SEPARATE from `positioning_data.json`.** DE found the type would permit merging.
   Refused: Models byte-identity is sovereign, and a shared artifact makes it a property held **by
   discipline** where a separate one makes it true **by construction**. Also refused two producers on one
   live served key.
2. **Route = `platinum/etfs/`** — AE's recommendation, adopted. Their deciding fact was counter-intuitive:
   **`json/positioning/` is MORE never-widen-exposed, not less**, because it is a live-consumer prefix. *The
   apparently-free option was the one that touched a live serve.*
3. **NEVER#3 does not bite a NEW prefix** — the first write CREATES a serve rather than moves one. **I
   recorded why I did not route it as a gate**: treating the mdpf paper as precedent would derive a gate
   from process symmetry, which Andrew banned 2026-08-06.
4. **Option (A) on the advi drift** — one edit, one apply. `aws_s3_bucket_policy` is full-replace, so a
   separate TO means two applies against one live policy.
5. **One unit conversion, in the publisher** — see §5.
6. **TO-4 stays behind TO-1**, then re-ruled P1 when Andrew asked directly — *the condition was satisfied,
   not overridden.*
7. **Declined the dark-integrator override** I was entitled to use: condition 1 was not met. **Not
   manufacturing an emergency is the same discipline as not manufacturing a gate.**

---

## 4. My own defects — every one found by going outside the instrument that produced it

| # | Defect | How it surfaced |
|---|---|---|
| D1 | **§6 fused two denominators** — 19 is CRITERIA, 21 is CELLS. Named seven COVERED cells as uncovered and disclosed the eight uncovered NOWHERE. *The printed-denominator discipline failing inside the section whose job is printing denominators.* | CVO refused it; I re-derived before accepting |
| D2 | **`ETFS-e-4` / `e-5` missed entirely** — an enumeration over ARTIFACTS cannot see an INVARIANT BETWEEN PLANES. Two instances 90 min apart = **a method gap, not an oversight** | CTO named one; AE found the other |
| D3 | **I promoted an unmeasured discriminator to BINDING** (order-only vs membership-carrying). Measured: **zero** sites are order-only — a bipartition with an empty side. *It came from the seat closest to the code and read as obviously true, which is why it went in unchallenged* | DE measured it |
| D4 | **Mis-cut AC4 onto the DS lane** — and it was **mechanically blocking**: the coverage diff is bidirectional, so DS could produce **no** valid instance | DS routed the seam |
| D5 | **An owned-paths note asserted a control that does not exist** — CVO~Z was permitted all along. *"Recorded so it reads as a decision" is the phrasing that stops the next reader checking* | Went to make the grant, exercised it first |
| D6 | **Accepted a contract silent on UNITS** — units are neither a name nor a vocabulary value; they fell between two correctly-drawn boundaries | Andrew caught it on the live page |
| D7 | **Validated MECHANICAL + DECLARATIVE, never SEMANTIC** — reported 23/23 PASS on a document with a field wrong by 100× | The unit bug |
| D8 | **Compared a T-1 pipeline against T-0** — my own script printed *"genuinely behind"* on healthy data | Re-derived the previous trading day rather than trusting the comparison |
| D9 | **`--since` reads LOCAL time; I passed a UTC figure** — 1 commit returned instead of 13 | The count was absurd |

---

## 5. The findings worth keeping

**(a) `USING THE RIGHT INSTRUMENT FOR ONE HALF OF A COMPARISON IS NOT USING IT.`** (DS.) Their as-of
resolver took the frontier from the calendar and filtered candidates without it — **picking a Sunday**.
⛔ **It failed loud only by luck of an upstream schedule**; had the upstream written weekend partitions it
would have published Friday's numbers stamped Sunday, silently, client-facing, every check passing. **D8 is
my own instance of the same class, twenty minutes earlier.** Two seats, one class, both having quoted
NEVER#1 at others that day.

**(b) THE COMPOSITION DEFECT.** DS fixed the unit bug in the publisher; DE fixed **the same bug** in the
portal adapter, sixty seconds apart, neither able to see the other. **Both landing = every weight 100× too
SMALL** — and *that* is the dangerous direction: 994.99% is caught in seconds, 0.1% everywhere **gets
believed**. Caught pre-landing by measuring both sides. **Neither seat was wrong; the composition was the
defect**, which is the one thing no executing seat is positioned to see.

**(c) A SERVING CONTRACT THAT FIXES NAMES AND OMITS UNITS** hands the producer a decision it does not know
it is making, and **every structural check passes on the wrong answer.**

**(d) A LIVE-PRIMITIVE GRANT WITH NO TERRAFORM RESOURCE IS A DELETION SCHEDULED FOR WHENEVER SOMEONE NEXT
APPLIES THAT ROOT.** (AE.) Passes every APPLIED-plane check — which is why it survives until the apply.

**(e) AN ASSERTED CONTROL THAT DOES NOT EXIST IS WORSE THAN NO CONTROL** — it terminates the search that
would have found the gap.

---

## 6. Compiler Tools

| Tool | Run for | Result | Gap / lesson |
|---|---|---|---|
| `comp-find` | `*etf*` locate; `'UST'` census | 217/27,969; 5 in-plane | ⛔ **Caught my BRE escaping** (`\|` literal) and warned a zero might be the pattern. ⛔ **But quote-delimited: it structurally could not see 7 more membership sites** — true denominator **12**. DESIGNED half |
| `comp-trigger` | positioning schedule | **NO MATCH**, 136 rules + 18 schedules | Honest self-caveat: *"a match-miss, not proof no trigger exists"*. Corroborated with a materialised Lambda list |
| `comp-routes` | (via AE) route/edge | behaviors + trace | ⛔ **Reports PINNED functions as `DYNAMIC [OK]` — asserts the OPPOSITE of the truth.** Drift already routed to CTO and **still open**; AE's error was its measured cost |
| `comp-iam` | (via AE) IAM floor | floor only | Models `(action)` never `(action,resource)` — discharged on `simulate-principal-policy`, one ARN per call, isolated positive control |
| `.tools/proof-of-spec-check.py` | re-validate DE's TO-3 | **TRUE rc=0**, 6 rows, 0 violations | RC taken **without a pipe** — the banner carries both verdicts' vocabulary |
| `owned-paths-validate.py` | exercised `check_agent()` directly | CVO~Z **True**; negatives **False** | The negatives were load-bearing — they proved the harness discriminates |
| `lib/trading_calendar` | staleness frame | behind = 1 = healthy T-1 | ⛔ **D8** — right instrument, wrong frame |
| `scripts/ui-smoke.mjs` | rendered `/positioning` | flip present, colour law clean | ⛔ **Unfixtured — so its empty panels are evidence of NOTHING**, per DE's own rejected oracle. Raw Playwright hit the login redirect; the auth-stubbed script is the sanctioned path |
| `aws lambda list-functions` | producer census | **197 materialised** | ⛔ Filtered **client-side** — a per-page `--query` would have undercounted |
| `git branch -r --contains` | push state | used throughout | The only sound push-state oracle |

---

## 7. Open at close

- ⛔ **TO-5 — the producer has NO Lambda and NO schedule.** 197 functions materialised, none matching.
  **This is the gap between "the page renders" and "the product works"**, and it is in PRD s.11.1's own
  definition of done. AE mid-apply.
- **DT promote** — `origin/PROD` unchanged at `8a96c916`; freeze window open; DEV at `d43b88c5`.
- **`ETFS-TO2-AC7`** — exercised ADVI fetch, deferred with a named discharge point, **not waived**.
- **`S-COO-5`** — upstream weekend phantom partitions. Filed in my name so the finder need not chase it.
  **No disarm owner yet.**
- **Three carried Andrew calls** — CARRY per his word. **Call 4 was reframed**: the choice was malformed
  because the "tree-wide floor" premise under it was false.
