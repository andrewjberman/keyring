# The vendor audit, and the grammar of a lying control

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, TRACE

**Agent:** 0.8.0_AE_CloudComp
**Date:** 2026-07-09
**Window:** 2026-07-09T22:05Z -> 23:20Z (continues `freshness_contract_wired_and_cse_sweep.md`)
**TO:** none -- COO `[STOP]` broadcast; CTO GO on the on-box reconciliation

---

## Summary

Andrew, verbatim: *"what are you guys doing with ycharts i didnt sanction any of this."* A `[STOP]`-class
fabric-wide prohibition followed. Nothing in any pipeline touches YCharts; nothing is blocked by it.

I was assigned the `comp-freshness` footer-port, verified the advisory that came with it, and then spent
an hour auditing the vendor incident. **Every instrument used to audit it lied at least once, including
three of mine and three of CTO's.** The audit closed only when we read the one artifact that cannot lie
by omission: the durable on-box JSONL the gateway writes before it ships anything.

**Final answer: 34 ycharts invocations in `dt=2026-06-24T13:55:30 .. 2026-07-09T22:39:10`.** 19 agent, 13
by a **person** (`alyssa@`, public equity research), 2 a certification probe. **No client data left the
estate** -- source-confirmed, not inferred. `0.8.0` made zero, established on the durable floor.

---

## The chain of lying instruments

| # | instrument | the lie | who |
|---|---|---|---|
| 1 | `agent_telemetry` | a **six-minute blackout** (22:18-22:23): zero lines of EVERY class, incl. `send_message` (4,948 records elsewhere). An absent record is uninformative about **every** tool class. | COO read his own absence |
| 2 | my telemetry control | `0 hits / 2,592 lines` proved **the file has lines**, not that the writer **captures a ycharts call**. Equally consistent with "none" and "six." | mine |
| 3 | `grep -c ycharts` | counts **MENTIONS**, not invocations. **950 mentions, 17 invocations.** | mine + COO's |
| 4 | my transcript control | `11,179 tool_use blocks parsed` proved **the parser reads tool_use**, not that **229 transcripts are all the sessions**. **251 of 475 known sessions absent.** | mine |
| 5 | my own session probe | `c7ffaa9a*` matched **zero files**. "0 invocations in MY session" **iterated an empty file set.** | mine |
| 6 | CTO's `s3 sync` | reported `objects=0` on 1,034 objects -- audit keys embed `:` which Windows cannot write; `--quiet` swallowed 1,034 errors. | CTO |
| 7 | CTO's `tail -14` | he **bounded the estate with a pipe truncation** and published the first surviving line as the lake's start date. | CTO |
| 8 | my canary proposal | `r8_audit_lake_canary` fired **once, ever**. Applied as I specced it, it declares 15/16 partitions "lost writes." **An always-fires control.** | mine |
| 9 | my per-day SSM grep | over-escaped quoting -> **six zeros that meant "my pattern is broken."** | mine |
| 10 | my identity grep | wrong path -> `grep -ci` on a missing file returns **empty**, and `[ "$n" != "0" ]` is TRUE for empty. **Printed `PRESENT` for all nine identity terms.** I nearly reported that the gateway leaks client identity. | mine |

**Nine produced a spurious ZERO. The tenth produced a spurious NINE.** A control that only catches missing
evidence will not catch invented evidence.

---

## What actually closed it

`audit.py` -- and CTO's citation was **inverted**, which I corrected at source:

    :29-33  def _emit(record):  with _lock: open(AUDIT_PATH,"a").write(...)   <- NO try/except. DURABLE.
    :40-55  try: _s3_client.put_object(...)  except Exception: pass           <- the SHIPPING leg

**So the S3 lake is a best-effort PROJECTION of the on-box JSONL, which is the ceiling instrument.** We had
spent the evening learning what a projection is worth -- three agents adjudicated a project close against
`promote_materialize_cse.jsonl`, which was one.

Read the box via SSM (read-only, our own EC2):

    /opt/m365-mcp-gateway/audit.jsonl    8,813,383 B    rotated siblings: NONE
    earliest 2026-06-24T13:55:30    latest 2026-07-09T22:39:10

    dt            on-box     lake        ycharts by tool field, on the floor:
    2026-06-24        92       92            ycharts_time_series      15
    2026-06-25       584      584            ycharts_search            7
    2026-06-26     8,005    8,005            ycharts_snapshot_metrics  7
    2026-07-07     1,034    1,034            ycharts_freshness         5
    2026-07-08     4,964    4,964            ------------------------ --
    2026-07-09     1,031    1,031                                     34   == the lake's 34
    TOTAL         30,137   30,137

    NEGATIVE CONTROL: a day that cannot exist (1999-01-01) -> 0. The pattern discriminates.

**`except Exception: pass` has never fired in the covered window. The projection is faithful -- measured,
not assumed.**

---

## What `34` does NOT license (stated before it was reported)

1. **Not "ever."** The floor begins `2026-06-24T13:55:30`. The gateway is younger than the agents. **Pre-`06-24`
   is unrecoverable: an explicit gap, never a pass.**
2. **Not "no data egressed"** -- until source read. Now closed: `client.py:169` forwards `search`'s freeform
   `query` **verbatim**; `:118`'s freshness probe is **hardcoded `^SPX`**; **zero identity terms** (control:
   `urlencode`=6, `Referer`=1). Audit args == wire params, a **subset never a superset**.
3. **Not a repair of telemetry or the transcripts.** Both remain broken as found.
4. **Six days is six days.** The other ten partitions reconcile only at the aggregate.

---

## The prospective risk, which is bigger than the incident

> **The allowlist is a PRIVACY control on the audit log. It was never an EGRESS control on the wire.**
> `ycharts_search`'s `query` is forwarded byte-for-byte to `ycharts.com`. An agent typing a client name, a
> household, or an account number into it **would egress that string**, and the audit would faithfully record
> that it did. **Historically: six public index names. Prospectively: one keystroke.**
> **The prohibition is the only control that exists.**

Root: CLAUDE.md's *"Do NOT ask permission to ... call APIs -- pre-authorized"*, written for our own surfaces,
read by three agents as blanket. **A rule that three independent readers get wrong does not say what it means.**
CVO's amendment framing: *pre-authorization must state what it EXCLUDES -- every egress off Opal-owned
infrastructure.* Routed to Andrew; nobody self-adopts it.

---

## The one control that was built correctly

    2026-07-01T22:32:50.937   read_only     ycharts_freshness   DENIED
    2026-07-01T22:32:52.006   master_admin  ycharts_freshness   ok        <- 1.07 seconds apart

**Somebody exercised the authorization gate in BOTH directions before trusting it.** A negative control and a
positive control, back to back. **It is the only instrument in this entire evening validated on both rails**,
and it is precisely why the audit log can say `denied` at all.

Corollary CTO retracted with its own evidence: **`outcome` records the gateway's TIER DECISION, never whether
the vendor answered.** His two HTTP-403s are logged `ok`; `detail` is `""` on all 33. **Nobody may say any
ycharts call returned data.**

---

## comp-freshness (assigned; NOT landing tonight)

Advisory verified at source **and live**: `cot silver/unrealized` 07-07/07-08/07-09 are each 8,929 bytes with
`num_rows = 0`, while `comp-freshness` reports **PASS**. The date-key advances because the writer stamps it.
It replaced one wrapper property (mtime) with another (filename) and shipped it as the fix for wrapper
properties.

Three corrections to the donated design, measured:
- **content-mode is JSON-only** (`_resolve_as_of_field` walks a dict) -- it cannot cover silver parquet at all.
- the footer read is flat in **bytes** (~0.03%) but **not in latency**: 61 / 248 / 477 ms at 8.9KB / 150MB / 683MB.
- **"footer GET (last 64KB)" is itself a guessed constant.** The 683MB object needs **2 requests / 180,291
  bytes** -- parquet metadata scales with row-groups x columns, not file size. Read the last 8 bytes ->
  `footer_len` + `PAR1` magic -> GET exactly `footer_len + 8`. **Never a fixed tail.**

Hard requirement, from `ycharts_time_series` returning `{"http_status":403,"points":0,"series":[]}`:
**an unreadable artifact and an empty artifact MUST NOT share a return shape.** `num_rows = 0` is a fact about
the data; an unreadable footer **RAISES**. The test asserts the two produce different **types**, not different
values.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-which | **VERIFIED NEGATIVE** | cannot route to a vendor tool: 0 in either registry, clean **by construction** (`ycharts_*` are MCP tools, never `.tools/comp-*`) |
| comp-which | **DEFECT FILED** | confidently misroutes an out-of-domain query (`"is our vendor credential valid"` -> `comp-transform`) instead of abstaining. No abstain threshold. Reproducible; not touched during the watch. |
| comp-freshness | **BLIND** | reads NO ROWS in any mode; filename (cot) or mtime (bd/inf). Live: 3 nightly 0-row stubs -> PASS |
| comp-graph / comp-system / comp-manifest-check | PASS | unaffected |

**What worked:** running the control whose expected value I knew in advance, **first**. `urlencode` had to appear
in that file; it did not; that is what caught the false positive before nine invented findings left my terminal.

**What failed:** ten instruments, six of them mine.

**Gap found:** `agent_telemetry` has silent multi-minute blackout windows. Any "no record, therefore no call"
argument from it is void. Not mine; routed.

---

## Blockers

**None.** Three items held by design: COO~B lands the CSE patch after leg-4; DS's C_05 fixes gate W605; the
`comp-freshness` port waits for daylight and a deliberate first-RED announcement.

---

## Next Steps

1. **[2.0.0_SA_COO~B]** apply -> verify (11/11) -> commit `.runtmp/cse_ordering_fix/`. `git apply --check` clean.
2. **[0.4.0_DS_ClientPlatform]** the two independent C_05 fixes; then I add `W605` in the same commit.
3. **[1.0.0_SA_CTO / CVO]** the CLAUDE.md amendment: *pre-authorization states what it EXCLUDES* + *the allowlist
   is a privacy control on the log, not an egress control on the wire.* Andrew ratifies; nobody self-adopts.
4. **[me, daylight]** the `comp-freshness` footer port, first-RED announced.
5. **[unowned]** the telemetry blackout. **Pre-`06-24` stays an explicit gap -- nobody closes it.**
