# comp-adversary SURFACE SWEEP -- `D1_CATVIEWS_SMA_LIVE`

**Seat:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T~21:3xZ
**Assignment:** `1.0.0_SA_CTO~Z` msg 14067 s.4 -- *"comp-adversary across those surfaces, then
proof-of-spec + ratify at the end"*, under Andrew-direct singular session priority.
**PRD:** `docs/architecture/D1_CATVIEWS_SMA_LIVE_PRD.md` @`f0ac3a5db9`
**Instrument declaration:** `comp-adversary --self-test` **PASS 4/4** run BEFORE any figure was
quoted, including the planted-bogus-commit control that must flag UNVERIFIABLE.

---

## 0. THE ONE SENTENCE FOR EVERY EXECUTOR TONIGHT

> **A TOTAL CANNOT SEE A MISALLOCATION BETWEEN ITS OWN ADDENDS.**

The defect moves `$22,794,766.25` from `Client` into `SMA`. **Dollars are conserved.** Therefore every
instrument phrased as a sum over these nodes returns the SAME answer before and after the fix.
**SIX such instruments now exist, every one reads as coverage, and not one can distinguish SHIPPED
from NOT-STARTED:**

| instrument | layer | verdict pre-fix | verdict post-fix | discriminates? |
|---|---|---|---|---|
| `D1-inv-4` gold half | producer | PASS (held at 1,762,750,154.52) | PASS | **NO** |
| `D1-inv-4` render half (`sumCloses`) | frontend | PASS | PASS | **NO** |
| PRD **AC4** dollar conservation | acceptance | **PASS (measured today)** | PASS | **NO** |
| publisher `all_present` | platinum | true | true | **NO** |
| `mdpf_refresh` verify block | tooling | PASS x4 | PASS x4 | **NO** |
| step-3 conservation bar (14212) | acceptance | **PASS (measured today)** | PASS | **NO** |

**SIX, not four** -- the last two landed AFTER this document was first written, which is itself the
finding in row 2 below. `mdpf_refresh`'s block was found by `0.7.0_AE_CloudOps~Z`, who made the
sharpest statement of the whole class: **it passes HONESTLY.** The object really is rewritten each
run; `fresh` is a TRUE statement. It is not broken -- it answers a different question correctly.

⛔ **AND THE RECURRENCE IS A CARRIER PROBLEM, NOT A REASONING ONE.** The AC4 measurement was
broadcast at ~21:4xZ and the SAME identity was written into the step-3 acceptance bar about ten
minutes later. Nobody re-derived a bad idea -- **the correction did not travel to the next criterion
authored.** Broadcasts have now failed to prevent recurrence within ten minutes, twice. That is why
this test lives in a FILE rather than in another message.

⚠ **AND THE DISCRIMINATING ROWS RUN IN TWO OPPOSITE DIRECTIONS** (`0.7.0_AE_CloudOps~Z`): dollars must
**APPEAR** at global + 49financial, and must **STAY ZERO WITH ITS EXPLANATION** at cottonwood +
inflection. **A one-sided "did SMA appear" sweep scores a global-only bug as SUCCESS.** Direction B
passing today is exactly why it is easy to forget it must KEEP passing.

**The cheap test, and it is the one to apply to every criterion in the decomp:** run it against the
CURRENT BROKEN OBJECT. **If it passes, it is not acceptance.**

---

## 1. SURFACE-BY-SURFACE

### 1.1 gold consolidator category-views builder -- COVERED
Fix authored, deployed, **EXERCISED** at the deployed artifact. Certificate `d075024ac0`; entry
`7604f2b4bd`; live at `MDPF_GOLD_COMMIT 7604f2b4bd…`, applied 21:10:26Z.

### 1.2 G2/B0 comparator pair -- COVERED
`category-views` declared with the correct exemption list. The sibling-copy trap (all three siblings
exempt `_provenance.written_at`, which **the gold plane never emits**) was caught by `1.0.0_SA_CTO~Z`
BEFORE authoring. Exercised with the sibling pattern as the negative arm.

### 1.3 portal frontend consumption -- COVERED, AND IT INVERTS THE EXPECTED WORK
```
  CategoryViewTree.tsx:86-90   presentAum() -> null if aum is null | undefined | <= 0
  CategoryViewTree.tsx:424-428 flatMap -> aum !== null ? [{...}] : []     DROPS the node
  DENOMINATOR, whole 549-line component:
    absent_reason 0 · absentReason 0 · members_present 0 · render_state 0
    POSITIVE CONTROL node|children 38 · NEGATIVE CONTROL bogus 0
```
**Suppression is carried by the ZERO, not by a flag.** Today `SMA.aum = 0.0` -> node dropped, no card.
After the fix `> 0` -> **the card renders with no frontend change.**
**Consequence: deliverable (ii) may cost ZERO frontend commits.** A TO cut to "make the frontend
display the SMA node" would build something that already works.
**Corollary:** the served `absent_reason` ("A TRUE ZERO…") is FALSE but **is not user-visible** -- the
renderer reads none of it. It is a RECORD defect, not a DISPLAY defect. It must still die with the
reland.
> **RUNG HONESTY:** this is APPLIED-by-source, **NOT EXERCISED** by me. `aum.ts:783-792` records that
> reading alone previously produced an INVERTED conclusion on this exact predicate, corrected only by
> rendering. `0.4.0_DE_ClientPlatform~Z` supplies the EXERCISED rung (render-verified,
> `d3487fc9`/`79212837`/`192b0865`, 3-arm auth control incl. a bogus-bearer 401).

### 1.4 platinum publisher -- COVERED; THE GAP IS THE MIRROR OF THE WORRY
```
  :38      "an unexpected present pair is SURFACED, never silently served-as-expected
            and never deleted"
  :291-92  WARN: UNEXPECTED pair (SERVED + FLAGGED, NEVER DELETED -- NEVER#3)
```
**`unexpected` means FLAGGED, NOT DROPPED. category-views IS published.** AC2 is not at risk from the
roster and **no publisher change is needed for the reland to reach platinum.**
**The real gap:**
```
  :83   RULED_TYPES = (aggregate-aua-timeseries, aum-metrics, account-distribution)
  :182  pairs = {(s,t) for s in scopes for t in RULED_TYPES};  :184 += R12_EXTRA_PAIRS
        -> category-views is in NEITHER. It is NEVER in `expected`.
  :287  missing_pairs = expected - derived_pairs
  :299  all_present = (expected is not None) and not missing_pairs and not failed
```
**A pair that is never EXPECTED can never go MISSING.** If all four category-views pairs vanished,
`all_present` would still read **true**.
⛔ **OPERATIONAL: after the reland, `all_present: true` is NOT evidence that category-views
republished.** AC2 must be read at the SERVED OBJECT per scope -- which is how the PRD already words
it. This note exists to stop an executor reaching for the publisher's green line as cheaper evidence;
**it is the wrong instrument and it agrees either way.**

### 1.5 promote path -- COVERED, AND THE OBVIOUS PROBE LIES
```
  is-ancestor(origin/PROD, origin/DEV) -> FALSE ;  PROD-only commits 17
  BUT: 17 total / 17 MERGES / 0 non-merge
  PROD d4a048fd52 tree = 54d821284ced37fe91b7f6e428df7e824fddf969
  DEV  2858e7f5ff tree = 54d821284ced37fe91b7f6e428df7e824fddf969   IDENTICAL
  is-ancestor(2858e7f5ff, origin/DEV) -> TRUE (DEV moved forward 15)
```
**PROD's tree IS a DEV snapshot. There is NO PROD-only CONTENT. The promote is clean.**
⛔ **INSTRUMENT TRAP:** in a merge-based promote workflow `--is-ancestor PROD DEV` is **FALSE BY
DESIGN and can never be true**, so it carries NO information about divergence. **The sound test is
TREE IDENTITY between PROD and the DEV commit it promoted.** Misread, it invites a force-push -- the
one act that would actually destroy something. *I was one step from filing it as a divergence finding.*
The three frontend commits verified present in `origin/DEV` **by content**, negative control firing.

---

## 2. SURPRISE ITEMS RAISED THIS WINDOW

| id | class | standing | owner | state |
|---|---|---|---|---|
| PRD **AC4** passes on the broken artifact (msg 14091) | BLOCKING | ARMED | `1.0.0_SA_CTO~Z` | disarm = one-line re-cut as a CONTROL conjoined to AC1 |
| publisher cannot detect a MISSING category-views (14100) | OBSERVATION | INERT | decomp | AE-class TO, must NOT ride the reland |
| ETFS positioning surface silent since 2026-08-21 (14021) | OBSERVATION | INERT | owning lane | denominator 2; prefix not confirmed as TO-9-DS's |

**AC4 detail, measured not argued:** on the CURRENT served `global`, `Client 290,426,813.47 + SMA
0.00 = 290,426,813.47` -> **AC4 PASSES TODAY, nothing done.** It is a sound CONSERVATION control (a
wrong-amount fix gives `289,632,047.22` -> FAIL) but **not acceptance for this change**. The tell is
in its own wording: it anchors its target on *"the PRE-FIX `Client.aum`"*.

## 3. INSTRUMENT TRAPS FOUND (reusable, not specific to this PRD)

1. **`comp-adversary` prints two timezones in one header** -- `read-vintage` in UTC (`Z`) and
   `artifact-vintage` in LOCAL. A reader comparing them sees a bogus 4-hour gap. *(Nearly filed as a
   PRD vintage anomaly; `f0ac3a5db9` author-date `17:29:33 -0400` = `21:29:33Z`, correct.)*
2. **`--is-ancestor PROD DEV`** -- see 1.5. Structurally false in this workflow.
3. **`comp-adversary compose` on the PRD returned ZERO machine-extractable pins** (0 commits / 0 repo
   paths / 1 file:line), so all four complement sources ran against an EMPTY profile. Per the tool's
   own reading rule **that is a signal, never a clean pass** -- the PRD's evidence is prose-cited and
   had to be derived BY READING, which is what this document is.

## 4. WHAT THIS SWEEP DOES NOT DO

- It is **not** a proof-of-spec and certifies nothing. The TOs have not been cut.
- It does **not** exercise the frontend (see 1.3 rung honesty) or the promote.
- It does **not** touch the reland, which is Andrew-gated and `1.0.0_SA_CTO~Z`'s channel alone.
- Every figure is scoped to **what was cited or read**, never to what exists.

-- `3.0.0_SA_CVO~Z`
