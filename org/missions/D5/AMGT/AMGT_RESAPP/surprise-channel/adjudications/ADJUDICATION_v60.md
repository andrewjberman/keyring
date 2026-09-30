# AMGT_RESAPP ROUND 50 -- L8 COMPILE (no judgment criterion this round)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~02:5xZ
**Input:** `2.0.0_SA_COO~Z`'s `round50/DRAIN_END_PACKET.md` @`84424c5c98`, msg 26853. The packet was read to EOF (6,323 B).
**L7:** 6 of 6 terminal per the packet (yy-1..yy-6). 0 judgment criteria.

---

## 1. THE SERVED STATE, RE-READ BY THIS SEAT

- **Lambda:** `opal-amgt-scoped-api` returns CodeSha256 `pVa+sgzj8XNZ9u...`, LastModified 2026-09-30T01:46:54Z. This equals yy-5's close.
- **`/thesis` passes the dossier:** ML_FP_Equity returns 200 with **5 of 5 pillar leads**. This seat read 0 of 5 on the same route
  at AMGT_CORPUS round 14 (ADJUDICATION_v17), so **CORPUS's six render outcomes now have their served half.**
- **NEOs:** INTU_US_Equity `/thesis` carries `officer_set` = "named_executive_officers", with 5 officers: Sasan K. Goodarzi,
  Sandeep S. Aujla, Alex Balazs, Mark Notarainni, Marianna Tessel. That is the proxy's NEO set, labelled, not the whole roster,
  per CTO ruling 3.
- **The base case's owner:** "Opal's historical-multiple reference" is present in INTU's `/thesis` payload. This closes the
  observation this seat raised at DSGN_AMGTV1 v7.

## 2. ⭐ FWD-30 NOW GRADES VALUES -- THIS SEAT'S OWN ROUND-49 PLANTS, RE-RUN

v59 measured that a wrong figure on the page or in the export read EQUAL. The same plants, on ASML_NA_Equity's live capture,
against the round-50 grader (`round45/checks/sweep.py`, now with a `VALUES` class: FIGURES 206 / VALUES 206):

| plant | v59 (round 49) | now |
|---|---|---|
| **export** "3.66 PER SHARE" -> 999.99 | EQUAL, not caught | **NOT_OK "FIGURES(values) differ"**, naming "('FISCAL', 'IS_EPS', '2016') value differs: page=['3.66'] export=999.99 PER SHARE" |
| **page, visible cell text** 3.66 -> 999.99 | EQUAL, not caught | **NOT_OK "FIGURES(values) differ"**, naming "page=['999.99'] export=3.66 PER SHARE" |
| **page, `data-model-cell` attribute only** 3.66 -> 999.99, text unchanged | -- | OK |
| baseline | OK | OK |

**The blind spot v59 named is closed on both sides.**
- The page value graded is the **visible text a PM reads**, not u-5's `data-model-cell` attribute. That is the right object for
  "the export carries what the page shows".
- The attribute is simply not consulted for values. A page whose attribute disagreed with its text would pass, which is harmless
  because no one reads the attribute.
- The packet's "values equal 96 of 96" rests on this grader.
- `Z-W176-S1`'s 6 scale-unchecked names are a named exception, not a pass, and are carried.

## 3. ⭐ `Z-S308` MEASURED -- SIX STALE SENTINELS, NOT FOUR, AND WHY A BARE PER-WORKTREE UNION MISREADS THEM

The issuer's own error row says four AMGT sentinels sit on undrained worker branches. This seat swept **all 43 live worktrees**
(`git worktree list --porcelain`, then `ls-tree -r HEAD org/critical_paths/.open_deploys/` per tree):
- **6 distinct AMGT sentinel names across 20 worktrees; CLOUD HEAD holds 0.**
- **Every one is CLOSED on CLOUD** (`git log --diff-filter=D`):

  | sentinel | closed on CLOUD |
  |---|---|
  | `amgt-resapp-ww1-...-restart-20260929` | `4a5eeb4458` |
  | `amgt-harvst-i4-...-20260929` | `84548218ef` |
  | `amgt-resapp-xx4-...-20260929` | `fcef6211b2` |
  | `amgt-corpus-r17-hitachi-model-block` | `1d85152810` |
  | `amgt-resapp-yy5-one-build-20260930` | `67becd1b9f` |
  | `amgt-corpus-r10-dossier-rewrite` | `bc50ea89cf` |

  Each survives only on branches cut between its open and its close. A branch that never touched the file keeps CLOUD's deletion
  at its drain.
- **So the NEVER-2 rule "read every worktree" must be read as a DIFFERENCE, not a union.** An entry is open only if it is present
  on some tree AND not deleted on CLOUD after that tree's base. A bare union reports 6 closed entries as open. That is the
  opposite error to the shared-tree-only read `Z-S308` names. The issuer's gate proposal (packet section 5 item 5) should carry this.
- **The disposable worktrees the COOs have listed hold most of these copies.** Removing them on Andrew's go clears the false opens.

## 4. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W173-S1..S4` (facts with no page attribute, graded on identity alone; the value blind spot) | **GRADUATED** | section 2: this seat's value plants are caught on both sides |
| `Z-W173-S5` (Hitachi identified; the export refused it for want of a model block) | **GRADUATED** | the block landed (AMGT_CORPUS v20), and FWD-30 reads 96 of 96 identified |
| `Z-S308` (the issuer's sentinel read was shared-tree only) | **CARRIED**, corrected | section 3: 6 names in 20 trees, all closed on CLOUD; the right read is the difference |
| `Z-S307` (the half read packaging from code comments, not the build manifest) | **CARRIED** -> the gate proposal | the issuer's own error, named |
| `Z-W176-S1` (the export's UNRESOLVED unit on 6 names) | **CARRIED** -> a RESAPP export fix | a counted exception, not a pass |
| `Z-S306` (the REGISTRY_HASH stamp is RED on HEAD) | **CARRIED** -> the analysis | whose restamp |
| `Z-W175-S1` (the NEO label) | **GRADUATED** | "named_executive_officers" is served (section 1) |
| `Z-W177-S1..S5`, `Z-W179-S1` | **CARRIED**, INERT or ruled | as the packet |
| the older ARMED set (`Z-S237`, `Z-S238`, `Z-S248`, `Z-S255`, `Z-W158-S1`, `Z-S276`) | **CARRIED**, unchanged | |

## 5. L10 PRECONDITION

1. **Every task order terminal:** 6 of 6. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** as above. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S430",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T02:55:00Z",
    "one_line": "L8 round 50: live pVa+sgzj... serves ML_FP's 5 of 5 pillars (0 of 5 at CORPUS r14), INTU's 5 named executive officers labelled, and 'Opal's historical-multiple reference'; this seat's v59 value plants are now caught on page text and export (FIGURES(values) differ); Z-S308 measured as 6 stale sentinels in 20 of 43 worktrees, all closed on CLOUD -- a per-worktree union misreads them as open.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Lambda opal-amgt-scoped-api CodeSha256 pVa+sgzj8XNZ9u..., LastModified 2026-09-30T01:46:54Z.",
        "Deployed /thesis ML_FP_Equity -> 200, pillar leads 5 of 5; INTU_US_Equity -> officer_set 'named_executive_officers', 5 officers (Goodarzi, Aujla, Balazs, Notarainni, Tessel); payload contains \"Opal's historical-multiple reference\".",
        "sweep.py (round-50) on ASML_NA_Equity live capture: page facts {FIGURES 206, VALUES 206}; export plant 3.66->999.99 -> verdict NOT_OK reason 'FIGURES(values) differ' val_differ 1; page visible-text plant -> NOT_OK val_differ 1; page data-model-cell attribute-only plant -> OK.",
        "Sentinel sweep: 43 worktrees; 6 AMGT names in 20 trees; CLOUD HEAD 0; git log --diff-filter=D: 4a5eeb4458, 84548218ef, fcef6211b2, 1d85152810, 67becd1b9f, bc50ea89cf."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W173-S1",
      "AMGT_RESAPP-Z-W173-S2",
      "AMGT_RESAPP-Z-W173-S3",
      "AMGT_RESAPP-Z-W173-S4",
      "AMGT_RESAPP-Z-W173-S5",
      "AMGT_RESAPP-Z-W175-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @84424c5c98 asserts 6 of 6 terminal, yy-5 served @pVa+sgzj, FWD-30 values equal 96 of 96 before and after the deploy, and names the issuer's errors Z-S307 and Z-S308.",
    "world_is": "True as read on the deployed function and on this seat's own plants. Z-S308's count is 6 names in 20 worktrees, all closed on CLOUD; the correct NEVER-2 read is a difference against CLOUD's deletions, not a union.",
    "notes": "FOR THE ROUND-50 ANALYSIS: the per-worktree sentinel read must subtract CLOUD's deletions (else 6 closed entries read open); the value grader reads visible text, not the data-model-cell attribute; Z-W176-S1's 6 unscaled names stay an exception; Z-S306 restamp owner."
  }
]
```
