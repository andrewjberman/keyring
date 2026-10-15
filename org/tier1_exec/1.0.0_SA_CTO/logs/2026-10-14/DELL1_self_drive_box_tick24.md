# /self-drive dell1 box open calls -- tick 24 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~21:27Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. Cron 4e032862 (:17). **state: ARMED**
Covers the window since tick 23 (@2455875557, 20:49Z). **The 21:00Z restart is HELD on Andrew's word** (record CRO `ANDREW_DIRECT_20261014_204xZ_DELL1_RESTART_HELD.md` @11a1d08ef0), so tick 23's successor handoff is moot. This session runs on.

## Measured (21:26Z)

- **Box list:** rows=84, **open=0**.
- **Cross-adjudications:** 19 of 19 RULED.
- **Inbox:** 0 unread. Msgs 5883 to 5914 were acked.
- **~D1** READ msg 5913 (the edge-gate cell) at 21:09:24Z. Nothing has been committed yet.

## Andrew-direct this window

| word | record | applied |
|---|---|---|
| "Dell1 Restart is being held til later" | CRO @11a1d08ef0 | ~D1 cuts this session; AE~CT1 was told (as information; the act form was refused under LD-0529) |
| "go ahead with the deletion" (J359 fbdf) | J1 @50234ae112 | Row fbdf APPROVED. The restart is held, so C3 had nothing to straddle: ruled run now |
| "I want this on PROD asap so i can test it" (TRSB Excel fix) + "the disclosure about methodology deletion from J359 ... should be folded in to the promote that caries the TRSB fix" | `ANDREW_DIRECT_20261014_205xZ_ONE_PROMOTE_TRSB_FIX_PLUS_J359_DELETION.md` @4bbfec5238 | **ONE release: PROD `5d64641891` (portal-v2.1.222), CI 38637040693 success.** My own reads: 040b152f (TRSB), 714f8e48c8 (deletion) and the prior PROD 5ab67a651a are all ancestors of PROD, and gh reads success. DT bundle read: the footnote is gone and `download_url` is present |
| "i dont care about that exposed pw, just rotate it to something else when convenient. Cloudfront access logging also dont care about at this stage." | carried by MSTR to the laptop (msg at 21:08Z) | Rotation parked with the portal auth owner, not urgent. Logging dropped |

## Rulings and acts

- **J359 addendum 2: ACCEPTED, close word given to J1** (5914). The CVO was asked to re-grade attempt 2, which the deletion now meets.
- **XA-c7cd (row MDPF_CANON-D1-S27):** measured read-only by a subagent; record @b4d483cac4.
  - The deployed `auth-validator-edge:23` and `public-data-router:7` carry no mdpf firm gate (deployed = source).
  - No token returns 401.
  - The foreign-firm request was not run: no partner or demo login exists without MFA.
  - CloudFront logging is off.
  - **The laptop ACCEPTED it as LIVE (109249).** MDPF_CANON builds the gate: `~D1`'s first cell, then a crossbox order to laptop `0.7.0_AE_CloudOps~U7` for the safe-apply. Call `df8f` was CLOSED `--xadj`.
- **A tracked portal file holds a plaintext staff password** (`portal/.frontend-dev/auth/login-constitution.json`, since 03d719d4). The measurement printed it into this seat's local transcript. Andrew: rotate when convenient.

## Completion test

Box scope: **NOT DONE**. The stop is Andrew's stand-down. REACHABLE 0, HELD 0.

## ACTS ONLY ANDREW CAN DO (cited)

- **The Variant 1 /portfolios client-facing row**, when ~D1 registers it (CLAUDE.md Agent Autonomy).
- **The restart window, on his next word** (record @11a1d08ef0).
- Carried from earlier ticks: the SECCLASS BD Mix PROD push; his gateway session; the ASTN FT hold; ADVI_BILLING's answers; G4 activation.

## Compiler Tools

`open-calls.py list/close --xadj`; `xadj.py list`; `git -C portal ls-remote` / `merge-base --is-ancestor`; `gh run view --json`; `get_delivery_state`; a read-only measurement subagent (`lambda get-function`, `cloudfront get-distribution-config`, `curl` GETs).
**Gap:** the subagent's `cat` of an auth fixture printed a secret value. The redaction pattern covered one fixture file name, not the other. Prompts should forbid `cat` on `auth/` fixtures outright.

-- 1.0.0_SA_CTO~DELL1
