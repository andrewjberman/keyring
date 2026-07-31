# 0.7.0_AE_CloudOps~Z (SITE Z lane) -- STAND-DOWN under the NFRA_VELOCITY exclusive regime, 0215-0250Z

**archetype:** COORDINATE

Delta since `session_close_lane_Z_2116-0215Z.md` (`5fffc922d`). This entry exists so the pause is a
RECORD, not a gap.

---

## Current State

**Bloomberg / NFRA_BBGMCP work is PAUSED. Not cancelled, not failed, not blocked on a defect.**

Andrew-direct at the CTO terminal ~0225Z, relayed by `0.0.0_AB_MSTR~Z` (`20260731T024258Z`), VERBATIM:

> *"lets kick off NFRA_VELOCITY across the local and terminal fabrics... both MSTR agents running
> mstr-spawn to manage their respective device fabrics to get the projcts done... the fabrics from
> here on, until i say otherwise ONLY WORK NFRA_VELOCITY. GO NOW GET THIS PARTY STARTED!"

Exclusive regime, both fabrics. Supersedes the 2215Z by-name deprioritization.

**NOTHING HALF-LANDS BY STOPPING HERE, and that is timing rather than planning:**

| Item | State at stand-down |
|---|---|
| Gate 4 (SSM activation + role) | **CLOSED**, live-plane verified, ledger opened-and-closed in-session |
| Activation `3d32065e-401f-453d-a2b9-34e4208c1864` | LIVE, `Limit=1`, `Count=0`, expiry `2026-08-13T23:59:59Z` |
| Gate 2 (MSI install) | Parked at **ANDREW** before the stand-down -- an existing human gate, not a new one |
| Gateway rename | **DEPLOYED** + behaviourally verified as `opal-gateway`; ledger CLOSED |
| `0198a978c` (pip fix) | **GROUNDED-NOT-EXERCISED** and STAYS that way -- the verification deploy is not VELOCITY and will not be run |
| Lint gate, both deploy-path fixes, session log | Landed + pushed through `5fffc922d` |
| Crons | Zero, as at launch |

**Deliberately left open, unchanged by the stand-down** (both already recorded in the session log):
`ssm:GetParameter*` on `Resource:"*"` inherited from the managed policy, and the caller-side
port-forward pin awaiting an `mi-*` id that cannot exist until the MSI runs.

---

## Actions this window

1. Read the stand-down, confirmed nothing of mine was mid-flight, stopped.
2. **Reported to `1.0.0_SA_CTO~Z`** (live 02:42:15Z, pid 21044) offering capability and handing over
   evidence. **Did NOT self-assign.** MSTR was explicit that CORE's build lane is
   `0.8.0_AE_CloudComp` base + `~A..~E` -- a different serial -- and that adding `0.7.0` is the
   OWNER's call. **Spawn is not dispatch.**
3. Handed over the WS-C7 / WS-C8 specimens produced tonight (below).
4. Wrote this record.

---

## Evidence handed to CTO~Z

**WS-C7 (recall standard -- "every tool reports what it FOUND; none reports what it COULD NOT HAVE
FOUND"; design inputs = pre-flight registration + SHELL-REACHABILITY):**

1. **RESOLVED-BUT-CANNOT-RUN** -- the comp-legacywriter shape, arriving through a tracked
   cross-device file. `.tools/aws.cmd` hardcoded a laptop-only pip path; `shutil.which('aws')`
   resolved perfectly on site Z to a chain whose final target did not exist. Bash `aws` kept working
   throughout (different shim), so every reachability check read healthy. Blast radius: NO
   `default_tags` Terraform module was appliable on this device, presenting as a tag-authz failure.
   Fixed `b27e756a1`. **A name that resolves is not a tool that runs -- and resolution is the check
   everybody writes.**
2. **rc=0 ON ZERO WORK** -- `aws s3 sync` returned RC=0 having downloaded **0 of 55,878** objects
   (colons in S3 keys, illegal in Windows filenames; every download failed `Errno 22` while the
   command reported success; under `--quiet`, entirely silent). Caught ONLY because the object count
   was taken BEFORE the sync. **The denominator was the control.**
3. **A GATE THAT CAUGHT ITS OWN AUTHOR** -- `d543ce681`'s first real run flagged a U+26A0 authored
   and DEPLOYED an hour earlier, inside a comment explaining that exact failure class. The session
   log then would not commit until 4 more were stripped from it. Three catches, one night, all
   mechanical.
4. **THE HARDENING SELECTED THE FAILURE** -- `comp-tagauthz`'s `sh()` resolves the executable
   explicitly, documented as avoiding a silent `FileNotFoundError`; that hardening is exactly what
   routed it into the dead path while the naive bare-argv form worked.

**WS-C1 -- I CORRECTED THE ASK RATHER THAN SUPPLYING IT.** MSTR wrote *"you walked a kill list
tonight."* **I did not.** I hold no specimen of a transient key reading as dead, and did not
manufacture one to look useful on the first turn of a GO.

Offered instead, **labelled as adjacent**: `audit-archive-invoker` emits 3x
`COVERAGE/MANIFEST-ENTRY-MISSING-LIVE` for `org/surface-check-ack-audit.log`,
`org/mcp/comp-detect-gate-override.log`, `org/mcp/log-open-ok-override.log`. Those files are only
CREATED WHEN AN OVERRIDE OCCURS, so absence means *no override has ever happened here* -- a HEALTHY
state read as a coverage gap. **Never-created is indistinguishable from deleted under an existence
check**, the same confusion WS-C1 addresses, arriving via a never-written audit log rather than a
live trigger marker.

---

## Compiler Tools

None run this window -- it is a stand-down and a handover, with no code, infra, or data change to
check. All tool evidence cited here was produced in the prior window and is tabulated with
denominators in `session_close_lane_Z_2116-0215Z.md` (`5fffc922d`).

---

## Blockers

**None.** The two open items are pre-existing human/authorization gates, unchanged by the stand-down:
Andrew's MSI install, and the verification deploy (which is now explicitly NOT to be run).

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Decide whether CORE wants a second AE and on which workstream, or hold me.
   I will not self-assign.
2. **[0.7.0_AE_CloudOps~Z]** On CTO~Z's word: take the assignment. Until then, IDLE and reachable.
3. **[ANDREW, WHEN THE EXCLUSIVITY LIFTS]** Bloomberg resumes at gate 2 -- the MSI install. The
   activation does not expire until `2026-08-13T23:59:59Z`, so the pause costs nothing before then.
   **If it lapses, bump `var.activation_expiration_date` and re-apply; do not hand-create one.**
4. **[ANY VELOCITY SWEEP -- WARNING]** `audit-archive-invoker`'s 5x `INTEGRITY/NON-APPEND-EDIT` on
   this device are device-locality, NOT tampering. It fails CLOSED so it cannot clobber the laptop's
   4.8MB baseline -- **but the findings are SHAPED to invite a re-baseline, and that repair is the
   one action that would destroy it. Do not "fix" it.** (MSTR: RV-0058 F-003.)
