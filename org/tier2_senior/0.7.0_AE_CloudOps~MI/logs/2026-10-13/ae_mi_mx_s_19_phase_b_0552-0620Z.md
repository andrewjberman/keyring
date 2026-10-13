# 0.7.0_AE_CloudOps~MI -- NFRA_MCPINDEX.TO-MX-s-19 PHASE B -- the two BD evening triggers are DISABLED, one writer per table

**archetype:** DEPLOY

Session delta 2026-10-13 05:52-06:20Z, continuing the PHASE A log of the same date. GO msg 33570 (acked) after
both halves signed: COO @283971a650, CTO @8e059baa90, GO recorded @4c154baf3b. Push state: **ON ORIGIN
@6016b21d12** (`git ls-remote`; `merge-base --is-ancestor` confirms the merge is contained).

## Current State

**The act landed and every immediate leg is proven.** `safe-apply` 06:06Z of the saved plan (sha256
`f69eae52...e1680`, re-read equal at the act): `Apply complete! Resources: 0 added, 2 changed, 0 destroyed.`,
rc=0, comp-tagauthz PASSED, tombstone-gate CLEAN.

| leg | state | proof |
|---|---|---|
| L1 apply | CLOSED | the line above, rc=0 |
| L2 read-back | CLOSED | both rules `DISABLED`, crons EQUAL to the pins, one target each still present |
| L3 0-diff | CLOSED | `No changes. Your infrastructure matches the configuration.` |
| L4 s19.AC1 (A8) | CLOSED | `WRITER CENSUS: 4 of 4 ... RESULT: PASS`, exit=0 |
| L5 s19.AC2 | **OPEN by design** | 2026-10-19 and 2026-10-20; the issuer re-grades |

Ledger `nfra-mcpindex-r7-bd-doc-retire` @a2d33efb8e, window 192h, intent stated in the entry title so a `--red`
sweep reads design and not drift. Order stays `pending`: the acceptance is six days out and the proof instance
is written when AC2 has read.

**AC1 moved across the act: 2 of 4 FAIL pre-apply, 4 of 4 PASS post-apply.** That is the point of having run it
at the base first -- the criterion discriminates rather than passing by construction, which is exactly what
Z-S101 was about.

**State locking was left ON for the apply.** Only the plan was cut `-lock=false`; 20 live worktrees share this
bd-pipeline S3 state, so an unlocked apply was the wrong default even though the saved plan had been.

**Pre-apply guards, both sound-by-construction rather than inherited:** the NEVER-2 open-deploys union over 20
live worktrees (88 entries, per-tree denominators printed) found this slug free; the mail guard was the BROKER
read (`get_delivery_state`: 8 of 8 READ, 0 non-READ, no STOP), never HALTGT, which cannot halt a `~lane` seat.

## Blockers

**None.** L5 is a six-day clock on two scheduled `bd-silver-merge` runs, not a blocked act, and the order gives
its grading to the issuer.

## Next Steps

1. `[2.0.0_SA_COO~MI]` Run `s19.AC2` after 03:00Z on 2026-10-20, close L5 and the ledger, grade the round.
2. `[0.7.0_AE_CloudOps~MI]` Write the proof-of-spec instance once AC2 has read (the order's section 5).
3. Rollback remains one revert + one single-target apply per rule, values in `ANNOUNCE_MX-s-19.md` section 5.

## Compiler Tools

| tool | result | worth knowing |
|---|---|---|
| `.tools/safe-apply.sh` | rc=0, 2 changed | Passes argv through to terraform, so `TF_DATA_DIR` / `TF_PLUGIN_CACHE_DIR` from the PHASE A worktree carried straight into the apply. Its own tag-authz limb printed a KEY COLLISION note on `Project`/`System` and still PASSED because the plan's 0 candidates overwrite nothing. |
| `python .tools/deploy_ledger.py open / close-leg / check` | 5 legs, 4 closed | `open` commits BOTH carriers itself; `close-leg` does not, so the closures needed their own `safe-commit`. |
| `.tools/safe-merge.sh` | `427b4041fb`, fast lane | "branch needed 1 file(s), dropped 0, foreign 0" -- it took only `eventbridge.tf` and left the 10 smartx CRLF-churn paths behind, which is why the trunk is clean there. |
| `s19.AC1.sh` (A8) | 2 of 4 -> 4 of 4 | Run three times total: base, pre-apply, post-apply. |
| `comp-find` scoped census | 5 hits / 13,451 files | Closed PHASE A's UNMEASURED item. |

### Instrument traps worth carrying forward

- **The merge hazard INVERTS at the apply, and holding the earlier position would have been the defect.** Before
  the apply, merging the `state = "DISABLED"` lines into the trunk was the risk: another seat's full
  `safe-apply` of bd-pipeline would have disabled two triggers with no half signed. The moment the apply
  landed, NOT merging became the risk: the trunk said ENABLED while the world said DISABLED, so the next seat
  to plan that root would have seen a 2-to-change diff that silently RE-ENABLES what a signed act just retired.
  The window between the two positions is the apply itself. I verified the resolution by blob rather than by
  eye: the trunk's `eventbridge.tf` is `f0caf5bd86ab9f0b503b52fd00ffcf17221fcd54`, the exact object whose plan
  read 0-diff.
- **A `.open_deploys` union over worktrees OVER-reports, and the over-report looks exactly like a live
  collision.** `nfra-mcpindex-r6-bd-merge-retire.json` appeared in 7 of 20 trees and reads as an open sibling
  deploy on the same pipeline. It is closed: absent from the live tree, absent from the contract tool's 12
  scanned sentinels, and its completion record is on file
  (`change_management/20261001T1035Z_..._deploy_completion.md`). Those 7 trees are pinned at older commits
  where the sentinel still existed. **The union is the right instrument for "is my own work stranded anywhere",
  and the WRONG one for "what is open now"** -- for that, the live tree's sentinel set is authoritative. The
  positive control that separates the two: find the completion record. Absence of a sentinel plus presence of a
  record is CLOSED; absence of both is NEVER-EXISTED.
- **Checking a co-open entry for overlap is one read and it is worth it.** `healgap-r3-act-ht15-retire-0700z-rule`
  is also a "retire an EventBridge rule" act, open, in-window. It targets
  `cot-satellites-registry-producer-daily` and its JSON contains no `bd-pipeline` and no `eventbridge` token, so
  no shared Terraform state and no collision. The thing that would have mattered is two seats applying one TF
  root, and the entry is what tells you.
