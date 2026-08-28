# CERT — `ETFS_INGEST.TO-6` **6 of 6** · `ETFS_INGEST.TO-8` **6 of 6** — **12 of 12**

**Certifier:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T~19:4xZ · **Executor:** `0.4.0_DS_ClientPlatform~Q`
**Instances:** `…/ETFS_INGEST.TO-6_PROOF_OF_SPEC.json` + `…TO-8_PROOF_OF_SPEC.json` @`c519eb7964`
**Authority:** Andrew-direct ~19:3xZ — *"lets proceed whatever needs to be proceeded to categorically
close this out"* / *"regarding D4"* / *"and the items you listed."*

⛔ **THIS SUPERSEDES THE PARTIAL CERTIFICATE OF ~15:3xZ** (`cvoZ_ETFS_INGEST_TO6_TO8_PARTIAL_…`), which
certified 3 criteria and recorded 9 as NOTHING FILED. **Its verdict was correct at its vintage and is
now spent.** The condition it named — *"no certifier act moves any of them, and no amount of time at
this office produces an instance"* — was met by seating a body, exactly as written.

---

## VERDICT

```
TO-6   rc=0 VALID   acceptance rows=6   violations=0   coverage 6/6
TO-8   rc=0 VALID   acceptance rows=6   violations=0   coverage 6/6
       alignment ENFORCE and FULLY CLOSED on both: forward-1 6/6 · forward-2 2/2 · backward 2/2
       decomp id space = 40   (it read 4 this morning — see §2)
NEGATIVE CONTROL: TO-6 instance + one bogus id -> rc=1. The check discriminates.
```
rc captured before any pipe; 3-arg form throughout, against each face's own `expected_criteria`.

---

## 1. ⛔ `TO8-AC5` — THE STRUCTURAL REFUSAL IS **DISSOLVED**, NOT WAIVED

The partial certificate refused `AC5` on a ground that no measurement could have lifted:
> *"The fire WAS scheduled — that is not in doubt. But the criterion does not ask whether it was
> scheduled; it asks that the claim be carried in a REJECTABLE FIELD. The proof-of-spec instance IS
> that field."*

**That field now exists, and it is populated from the run's own self-description rather than from the
seat's assertion** — `run_class = 'scheduled'` read at **two independent stages** (bronze and gold
manifests, each carrying its own field), one `run_id`, four object clocks compared against two cron
boundaries, plus a trading-day frontier check.
⭐ **The refusal was right and the remedy was the one it named.** Nothing was argued down; the missing
artifact was produced. That is the difference between a criterion that gets satisfied and one that
gets talked past.

## 2. THE ALIGNMENT LAYER NOW CLOSES, AND I CONTROL-TESTED THE FIX MYSELF

This morning the checker saw **4** ids in that decomp — an incidental `ETFS-d-*`/`ETFS-e-*` family —
and **zero** of the 29 real `INGEST-T*` ids, while reporting the 4 as the id space. Every
`ETFS_INGEST` instance was therefore INVALID on alignment regardless of row quality.
`1.0.0_SA_CTO~Z` landed the ruled narrow third branch @`87c5761e9e`. **Tested at this seat, not taken
on the ruling:**
```
sees:      INGEST-T3-6 · INGEST-T5-1 · INGEST-T0-1      (the new branch)
still sees: ETFS-d-1 · D1-i-2 · D1-m-foo                (existing branches intact)
NEGATIVE CONTROL — prose tokens stay unmatched:
           D11-era-things  FALSE · THE-BIG-THING  FALSE · INGEST-Txx-1  FALSE
```
**Enumeration, not relaxation** — the mandated control holds, and the id space moved 4 → 40.

## 3. ⛔ AN INSTRUMENT ERROR OF MINE, RECORDED SO NOBODY QUOTES IT

My **first** run of both checks returned **rc=1 INVALID with 7 violations each**, every one reading
*"instance row X is NOT in the TO's expected set (unexpected addition)"*.
**THAT VERDICT WAS FALSE AND THE CAUSE WAS MINE:** I built the face path with `ls`, which returned it
with a trailing classify `*`; `grep` then failed, the expected-id set arrived **EMPTY**, and the
checker correctly rejected `expected=0 carried=6`. **An empty expected set does not error — it
produces a fully-formed INVALID that blames the executor**, which is precisely the shape this
certificate's own §2 is about. Re-run with literal paths and an empty-set guard: **rc=0 VALID both.**
⚠ Third instance today of a wrong-referent producing a clean, confident, wrong verdict. **The guard
that catches it is refusing to run the check at all when the id set is empty.**

---

## 4. WHAT MAKES THESE CERTIFIABLE RATHER THAN MERELY GREEN

- **`INGEST-TO6-AC1` — located BY CONTENT, as the criterion demands.** The TO's own line number
  (`:141`) was stale after an earlier shift, and the executor anchored on the `CHAR` list containing
  `GICS_SECTOR_NAME` instead: the field sits at `:239` **immediately beside** it. **The criterion
  anticipated its own citation rot and the executor honoured that rather than the number.**
- **`INGEST-TO6-AC2` — the citation is grounded ON DISK, not relayed.** The sequencing message was
  located by a content grep for the msg-id, **not by recollection of the id** — which matters
  especially today, given that msg-ids rebind per recipient.
- **`INGEST-TO6-AC3`** — 172 rows × 14 columns censused; `GICS_INDUSTRY_GROUP_NAME` present, 165
  non-null; **positive control** (`GICS_SECTOR_NAME`, 165 non-null on the same rows) **and negative
  control** (`ZZZ_NO_SUCH_FIELD_9999` absent) — so presence discriminates.
- **`INGEST-TO6-AC6` — coverage rides BESIDE the aggregate**, six columns on every book row: DIVZ
  27/28 rows and 96.83 of 99.19 weight; IDVZ 43/43; PFDE 88/88; PFOE 22/22. **A sector split that
  does not print its own coverage is the class this estate legislates against, and this one prints it
  in the artifact rather than in the report.**
- **`TO8-AC2` — the denominator was RE-DERIVED, not copied.** The criterion said 189/4 and demanded
  re-derivation; the executor walked the document and got 30+45+90+24 = 189 independently.
  **A confirmed denominator, not an inherited one.**
- **`TO8-AC3` — the 9 null rows are ENUMERATED, not counted.** SALXX, FXFXX and CASH named
  individually, every one carrying an explicit basis. **The criterion's prohibition is a null quietly
  becoming a sector; listing beats counting because a count cannot show that.**
- **`TO8-AC4`** — `sub_asset_class` identical on 189 of 189 (book,ticker) pairs, **0 added / 0
  dropped**, so the comparison covers the entire served set with no unmatched remainder.
- **`TO8-AC6`** — `industry_group_basis` present and non-null on **189 of 189**, against a measured
  **baseline of 0 of 189** pre-fire, all values inside the closed enum. *The value carries its claim,
  and the baseline is what makes the presence check discriminate.*

---

## 5. SCOPE — what this certificate does NOT say

- ⛔ **It does not close `ETFS_INGEST` or D4.** Andrew ruled *"D4 is done"* a **READ**; the register act
  travels through his direct channel with this seat. **Nothing here stamps it.**
- **`ETFS_INGEST.TO-9-DS` remains OUTSTANDING** — its instance is ABSENT and its face still reads
  *"BLOCKED ON A SOVEREIGN VENDOR-CALL WORD"* though that word was granted and the work shipped.
  **Both are stale artifacts of a completed build**, and `0.4.0_DS_ClientPlatform~Q` is filing.
- **It does not certify the truncation as fixed.** `industry_group` values were truncated at
  Bloomberg's 30-char cap; the decode ships under Andrew's 18:02Z instruction, its own certificate
  will record **UNFALSIFIED, never PASS**, and `basis` stays `inferred-from-truncation`.
- **VINTAGE, and it is load-bearing:** certified against **LOCAL HEAD**. Both `c519eb7964` (instances)
  and `87c5761e9e` (checker branch) are **LOCAL** — `origin/SITEZ` = `a951b1bd21`. ⛔ **A run against
  origin finds no instance and an unfixed checker, and would reproduce this morning's verdict as
  though confirming it.** The two commits travel together; the push is the integrator's leg.

— `3.0.0_SA_CVO~Z`
