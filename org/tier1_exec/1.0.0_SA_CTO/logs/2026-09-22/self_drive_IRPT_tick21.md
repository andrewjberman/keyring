# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 21 (~02:1xZ 2026-09-22)

- **Arming record:** carrier `c9ccd9f4e3`
- **Cron:** `46e545b7`
- **State:** ARMED
- **Scope:** 2 projects, both `active` / EXECUTING. Sequence: no flags.
- **Inbox:** 0 unread. Read and acked: 99356, 99360, 99363, 99364, 99368, 99369, 99373.

## Events since tick 20

### L4 fence probe (IB-rtj-2): PASS, and the role is gone

`0.7.0_AE_CloudOps~V` recorded the probe at `87a4e03a70`. All arms ran in one assumed session at 01:59:48Z.

| Arm | Target | Result |
|---|---|---|
| Positive control | lambda-artifacts | lists, KeyCount 5 |
| Negative | opal-data-inflection | AccessDenied, "explicit deny in a resource-based policy" |
| Negative | opal-data-cottonwood | AccessDenied, "explicit deny in a resource-based policy" |
| Attribution control | opal-data-assets | AccessDenied, "no identity-based policy allows" |

- Both negatives are attributed to the resource policy (2 of 2). The attribution control's different wording shows the Deny wording discriminates between the two causes.
- **Role deletion, verified independently by this seat:** `iam get-role irpt-fence-probe-l4-role` returns NoSuchEntity. The declaration was removed at `d1fa987b2d`, and the ledger is closed.
- **Signatures:** there are three halves, from CTO, CRO and COO~F. The CRO recovered from its 529s and signed at `dba9199222`, which made COO~F's in-stead half redundant.
- **Relay:** my first relay to CloudOps~V was refused by LD-0529, because a Tier-2 message must cite a task-order id. I resent it as information citing `IRPT_BCKEND.TO-IB-rtj-2`, and it was delivered.

### Capture tool: still HELD

`3.0.0_SA_CVO~B` graded R101-AC3 early as **FAIL** (`33c5b593ef`, `ADJUDICATION_v6.md`). The initial-hop repair works, but two lifecycle counterexamples remain, reproduced on `c5a18898`:

1. **Interactive interval.** A portal -> foreign -> portal navigation that happens while the human is logging in is never observed. The run shows intervalChainReads=0 and no listeners installed, and it ends writes=1 / success=true.
2. **Retry after a foreign hop.** A foreign verification hop is detected but treated as retryable (`:255-259`). A clean retry then succeeds and writes the session.

This correction applies to this seat's supplementary run (msg 99370). That run used only the round-9 diagnostic, and it discriminated only the initial-hop case. **It could not see either residual.** The L9 gate is what caught them, which is exactly what the gate is for.

- The ask to Andrew stays HELD.
- The remedy belongs to `2.0.0_SA_COO~B` through normal repair issuance.
- Design direction for this seat's round-10 analysis:
  - a session-lifetime main-frame navigation observer, installed before the first `goto`;
  - any foreign origin at any point is TERMINAL, with no retry;
  - acceptance is CVO~B's R10 lifecycle diagnostic plus its interval pair plus a positive control.

### Other movement

- **IRPT_FNTEND round 11:** wave 1 has drained. `2.0.0_SA_COO~F` corrected its own F65-AC16 invocation at `6100a2fc06`.

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

- `git log` / `git show`
- `.tools/aws iam get-role` (rail-checked; one existence probe)
- `sequence-check.py`
