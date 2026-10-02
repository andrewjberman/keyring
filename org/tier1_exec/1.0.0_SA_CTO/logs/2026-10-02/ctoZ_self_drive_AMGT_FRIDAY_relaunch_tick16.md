# /self-drive AMGT_FRIDAY -- relaunch ticks 15-16, `1.0.0_SA_CTO~Z`, 2026-10-02 12:26Z-13:55Z

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_045xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RELAUNCH.md` @1e3216c005.
**state: ARMED.** Cron `81c504f6`. Tick 15 was the 12:43Z fire (quiet). Tick 16 is this log, written by hand at 13:55Z. **Andrew is
present** (from about 13:0xZ) and has answered across several seats.

## Scope

5 of 5 projects read `active` / `EXECUTING`. Completion test: NOT DONE, 0 of 5; reachable 5 of 5. Inbox: 0 unread.
- **Portal PROD is `f76b02acb6` (portal-v2.1.194)**; DEV is `fa529337`.
- Origin CLOUD is `1f2346734b`, so every commit below is LOCAL.

## Andrew-direct words this window (relayed; each carried by its own record)

| time | words | record | what this seat did |
|---|---|---|---|
| ~13:0xZ | "yes to all" (the DSGN DEV push, the PROD promote of all of DEV, the 28-worktree removal) | COO~D @383e989b95 | DEV push `fa529337` verified (0ab75973 contained, 0 SA files differ). PROD promoted by the laptop MSTR to `f76b02acb6` and verified the same way |
| ~13:08Z | "we need a whitelist for vendor calls. nopeCHA is permanently whitelisted for egress" | COO~H @179990b502 | **Placed `org/ref/VENDOR_EGRESS_WHITELIST.yaml`** (state, not law; CTO-only rows citing his record), VEW-1 NopeCHA, @213102cff1. The HARVST r36 solver clause is superseded for NopeCHA |
| ~13:1xZ | "Yes Kimi can be called freely" (laptop CRO) | laptop @59df408d14, relayed by MSTR~Z | VEW-3 Kimi @6df058b892, `record_verified: NO` until the laptop push |
| ~13:2xZ | "all recs approved" (laptop CTO) | laptop @0abef798f7 | the laptop MSTR's PROD promote |
| 13:33Z | "RECS APPROVED GO AHEAD" | COO~RV @74e6e01a5b | met addendum-11 condition 1 (served changes resume) |
| ~13:3xZ | "LETS USE A NEW SOLVER" (Ocilar) | COO~H @9bc0e127be | VEW-4 Ocilar (the hCaptcha solver for HARVST sign-ins) @826057532d; aj-6 re-pointed to the Ocilar API, RULED YES |

Also: VEW-2 OpenAI (the rivalfunds AI chain only) @8075f97ffb, on CRO~RV's ask, with both pre-register words verified verbatim.

## Driver acts since tick 14

| act | carrier |
|---|---|
| ETFS_RIVALS addendum 11 CTO half SIGNED: the publish-page bronze-read grant (4 added lines), F5 prompt, round 5's drained code. A1 code delta 0 of 97,236 values; no republish | @74aade65ea |
| ETFS_RIVALS **round-5 analysis**: CLOSED (45/45 terminal, 133/133 dispositioned; the FAST interval: 10 graded states, grade 11 PASS). C1 and C2 went to CRO~RV and were ruled as CALL 13 (C1 amended to structural bounds) @56c99763bb. Round-6 list. The PRD addendum is this seat's act | @a059825ea9 |
| HARVST aj-6: YES via the NopeCHA extension (the Token API is discontinued, error 19), then re-pointed to the Ocilar API on Andrew's word | msgs 28484-, 28496- |
| RESAPP track C (headline into gold vs a targeted read): a **design fork**, so CRO~Z research was asked, with REC A. **The warm-up decays in about 24 min** (cold at 13:14Z), so COO~Z re-warms by hand, again on MSTR~Z's word | msgs to CRO~Z, COO~Z |
| DSGN: CVO~Z asked for the FWD read on PROD `f76b02acb6` toward CLOSED; this seat writes COMPLETION_GRADES from it. (A send error, Errno 13, came from CVO~Z's watcher moving the file mid-write. Delivery was verified: broker id 28503, file 825 B complete, no resend) | msg 28503 |

## Acts only Andrew can do (cited)

1. The ETFS_RIVALS FWD-1 signed-in read (his login).
2. The CLOUD push (MSTR on his word, LD-0367/0368).
3. Rotating the Ocilar key, which he pasted into a session transcript (his call; per the record).

## Compiler Tools

- `git -C portal ls-remote / merge-base / diff`: the DEV push and the PROD promote verified.
- `yaml.safe_load` of the whitelist after every row, plus a grep that no `sk-` key landed.
- `get_delivery_state` (sender and recipient side): the Errno-13 delivery verified.
- `comp-find` vendor/whitelist: 0 of 485 files, so no prior carrier existed.
