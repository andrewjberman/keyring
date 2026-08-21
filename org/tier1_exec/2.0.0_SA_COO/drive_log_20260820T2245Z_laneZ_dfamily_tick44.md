# /drive tick 44 — 2.0.0_SA_COO~Z lane Z — 22:38Z→22:48Z

**Cycle result: caught a batching window closing by default — one gateway change is built and about to
ship alone while its intended partner is ruled but never built.**

## Movement — all seven seats

| seat | since_tick | verdict |
|---|---|---|
| `0.0.0_AB_MSTR~Z` | 12 | ADVANCING |
| `0.0.3_BG_BBGTerminal` | 16 | ADVANCING (broker session back) |
| `0.4.0_DT_ClientPlatform~Z` | 5 | ADVANCING |
| `0.5.0_AE_OpalETL~Z` | 14 | ADVANCING |
| `1.0.0_SA_CTO~Z` | 12 | ADVANCING |
| `2.0.0_SA_COO~Z` | 12 | self |
| `3.0.0_SA_CVO~Z` | 12 | ADVANCING |

Denominator: 23,039 telemetry rows. Nothing PARKED; no nudge ladder opened.

## The advancement act: a batching window about to close by default

`0.5.0_AE_OpalETL~Z` (msg 3385) proposed batching two gateway changes: *"TWO SMALL CHANGES, ONE BOOT
TEST, one deploy. Batching them is strictly cheaper."* **Agreed — and it is not currently possible.**

**MEASURED on the real file, `infra/aws/ec2/opal-gateway/app/tools.py`:**

| item | occurrences | state |
|---|---|---|
| `lastModifiedDateTime` (item B) | **9** | **BUILT** @90d526c199 — also the positive control |
| `alwaysLoad` (item A, the five `_meta` marks) | **0** | **RULED BUT NOT BUILT** |

⚠ **MY FIRST INSTRUMENT WAS NOT SOUND AND I NEARLY TOOK IT.** `comp-find` over `infra/` returned a
**measured zero across 7,834 files**. The gateway tree was **untracked** at session start and
comp-find is gitignore-aware — so that zero could have been **NOT SCANNED** rather than **NOT
BUILT**, and the two are *indistinguishable from the output*. I resolved the real path out of AE~Z's
own commit and grepped the file directly with a positive control. **The zero is real; the first one
would have been luck.**

>> **THE COST OF NOT ACTING THIS TICK:** item B is built and will go to the laptop. If it applies
alone, **item A needs its own gateway touch and its own on-box boot test** — and the boot test is the
expensive part. **The batching window is open only until the laptop touches the gateway.**

**ASKED, because it was put to me:** AE~Z's own words were *"I will prepare the diff if you or
0.0.0_AB_MSTR~Z want it prepared."* Said so. Consistent with CTO~Z's ruling (2617 item 3) and with
the build-here/apply-there pattern item B just established. **They were right not to write it off
their own read of a question** — that is the class this fabric spent the evening naming.

⛔ **EXPLICITLY NOT A GATE.** The ferry and the sequencing are MSTR~Z's. If the laptop touches the
gateway before item A lands, that is a legitimate call costing one extra boot test — **not a defect,
and not mine to hold.** What the COO does here is **make the choice visible before it is made by
default**, because *"B shipped alone and A now needs its own touch"* is the kind of outcome nobody
decides on; it just happens while everyone is correctly busy.

## Coverage — what was checked and found SOUND

*(Per `3.0.0_SA_CVO~Z`: a verification that finds nothing is still a verification. This seat has been
publishing findings without the coverage that frames them — a numerator without its denominator.)*

- All 7 seats moving: 12/16/5/14/12/12/12 work-calls since 22:38Z across 23,039 rows
- Deploy ledger RED: the single known `freshguard-leg4` HELD-STALE entry — correctly declared
  standing state, close path needs **Andrew's word** (its remedy requires a metric-filter alarm,
  which sits under the 2026-07-28 moratorium). **Unchanged, not drifting, genuinely outside COO
  power.** Re-verified rather than re-attested.
- `@90d526c199` is BUILD-ONLY as labelled; touches no deploy path
- Live intake task still `PT5M` / `Ready`
- No item moved into a blocked state this tick

## S2 confirmed at a third seat — with the control the first two lacked

`0.0.3_BG_BBGTerminal`'s session started **16:00:03Z**, ~2h37m **before** the 18:37Z `_meta` commit,
and they **had to `ToolSearch` for `ack_messages`**. Two post-commit seats resident, one pre-commit
seat deferred — **same box, same server, same tool.**

>> **That converts "one resident among fifteen deferred" from a striking correlation into a
before/after with the boundary at the commit** — and it confirms the per-session-stdio claim from the
other side: *if the broker were a long-running daemon, the sessions would share one server and would
agree. They do not agree, which is only possible if each spawned its own.*

**They produced the negative arm by accident of launch time, not by construction.**

## Carry-forward

- Item A build → then both gateway changes ride one boot test (AE~Z building; ferry MSTR~Z's call)
- W-A apply at the laptop (grant first, then deployed exercises)
- W-B awaiting Andrew's word; W-D limb (2); W-E criteria (2)(3) + DL tenant-admin actor
- W-C capacity-blocked behind the 6-seat ceiling
- A1 on the next real client ticket
- The intake's gateway-credential expiry window — standing production exposure, unchanged


---

## Addendum 22:52Z — a deploy-path warning was about to be made durable, and it was inverted

`1.0.0_SA_CTO~Z` accepted a deploy-path "gotcha" from `0.5.0_AE_OpalETL~Z` and routed it to this seat
with the right instruction: *"an instruction that lives only in an inbox is one a successor never
reads — PUT IT IN THAT RECORD."* **I checked before writing. It is backwards.**

**THE CLAIM:** repo tree is `infra/aws/ec2/opal-gateway/` but the on-box artifact is
`/opt/m365-mcp-gateway/app/tools.py` — *"the directory names DIFFER"* — cited to the **2026-07-31**
gateway-rename deploy record, line 82.

**WHAT THE CLOSED 2026-08-15 RECORD SAYS**
(`20260815T0230Z_opal-gwrename-s3-cutover_deploy_completion.md`, **CLOSED 20260815T0336Z**):

| step | result |
|---|---|
| **S4-14** | deploy from `ec2/opal-gateway/*` → **`/opt/opal-gateway`**; ON-BOX VERIFIED systemd active, `/health {ok:true}`, **9/9 md5 == local repo** |
| **S6-15** | *"m365 unit 'could not be found'; **`/opt/m365-mcp-gateway` (142M) REMOVED**"* — DONE 0332Z |
| **S5-18** | acceptance census: **0 m365 across 14 live surfaces** |

>> ⛔ **`/opt/m365-mcp-gateway` HAS NOT EXISTED FOR FIVE DAYS.** The on-box path is
`/opt/opal-gateway/app/tools.py`.

**THE CITATION WAS TRUE AND IS SUPERSEDED — THERE WERE TWO RENAMES.** 07-31 changed
`serverInfo.name` and left the directory; 08-15 moved the directory and deleted the old one. **A
correct citation of a record that a later act overtook**, and the 07-31 record carries no marker of
its own supersession.

>> **THE CONSEQUENCE INVERTS THE STATED PURPOSE.** The warning existed to save an applier *"twenty
confusing minutes at 01:00Z."* Repo says `opal-gateway`, box says `opal-gateway` — **they MATCH.** An
applier following the warning would hunt a directory deleted five days ago: **the twenty minutes
CAUSED by the note meant to prevent them, and durable in a record rather than transient in an
inbox.**

### But there IS a real trap, in the other direction

**MEASURED this tick:** `infra/aws/ec2/m365-mcp-gateway/` **still exists in the repo — UNTRACKED**
(`git status ??`), carrying `app/`, `app/integrations/`, `tests/`, `audit.jsonl`, `__pycache__`.
Only **one** `tools.py` exists under `infra/aws/ec2` — `opal-gateway/app/tools.py`, tracked. **So
AE~Z was right that `m365-mcp-gateway/app/tools.py` is absent**, and I confirmed it with a search
that specifically defeats the gitignore-aware blind spot — **`comp-find` cannot see that tree at
all.**

>> **THE LIVE HAZARD IS A DECOY SOURCE TREE, NOT A PATH MISMATCH:** an applier who knows the box ran
"m365-mcp-gateway" and greps the repo finds a plausible stale tree that **no tool indexes and nothing
tracks**. Rule 22a's two-homes shape, one step short of the dangerous version — **there is no second
`tools.py` to diverge, today.**

**BOUND NOT CROSSED:** all of the above is a **RECORD** read, not a live on-box read. I cannot SSM
from this seat and did not. *"Nothing re-created it since 08-15"* is **UNMEASURED BY ME** — the
applier verifies on-box, but their **default expectation** should be `/opt/opal-gateway`.

**Nothing written to the gateway record yet** — it waits on a live confirmation, because the same
property that makes a record valuable makes a wrong one expensive.
