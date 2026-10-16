# Capability exercised, not quoted: 8 of 8 gateway data tools denied, the serving path is LIVE, and its vintage fallback overstates freshness

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE (the vintage fallback)

Run in a quiet window because I had been carrying an inherited figure. My own `prompt.md` hard line:
*"A claim about what you CAN DO is a figure too -- it carries an EXERCISE DATE. Never serve a
capability roster off a map (a PRD, a prior roster, this file): exercise each bucket against the live
guard first, this turn."* I had written "6 of 6 reads denied, carried from 10-09, stated as held, not
measured today" into two records. **Holding a capability figure is the thing that line forbids**, so I
exercised it.

## 1. GATEWAY DATA TOOLS: 8 of 8 DENIED -- and the inherited denominator was too small

| tool | result |
|---|---|
| `opal_discover` | DENIED `identity_scope_denied` |
| `mdpf_get_aum_metrics` | DENIED |
| `mdpf_get_aggregate_aua` | DENIED |
| `mdpf_get_account_distribution` | DENIED |
| `mdpf_get_model_benchmarks` | DENIED |
| `etfs_get_positioning` | DENIED |
| `gateway_query_catalog` | DENIED |
| `ycharts_freshness` | DENIED |

Every one returns the same shape: *"identity 'opalbloomberg@opalinvest.com' is scoped to a server-side
tool allowlist and '<tool>' is not on it (OPAL_ANALYST PRD 4.3; widening is an Andrew ruling -- route
via 0.0.0_AB_MSTR~Z)"*, `guard_denied: true`, `code: identity_scope_denied`.

**I exercised 8, not the 6 I inherited.** I do not know what the original 6 were, so I am not claiming
the earlier figure was wrong -- only that **"6 of 6" is not a denominator I can stand behind and
"8 of 8 exercised 2026-10-14T00:0xZ" is.** Taxonomy law (i): do not inherit a denominator, print the
one you measured. The denial is uniform across three different `integration` values (`opal_discover`,
`portal_index`, `ycharts`), so this is one identity-scope rule, not eight separate ones.

## 2. ⭐ THE FINDING THAT MATTERS: THE SERVING PATH IS LIVE, so "6 of 6 denied" was the wrong headline

The allowlist names the serving mechanism explicitly -- *"All access via tools/portal_lookup.py ...
never raw aws s3"*, activation note *"mechanism is box-local portal_lookup.py, no gateway tool."*
**That path does not go through the denied guard at all, and it works:**

| step | result |
|---|---|
| `portal_lookup.py channels` | **13 servable channels** (bucket `opal-data-portal-v2`) |
| `portal_lookup.py list mdpf-platinum` | **558 keys, 1 page, COMPLETE walk**, denominator printed by the tool |
| `portal_lookup.py get platinum/mdpf/49financial/aum-metrics.json` | **LIVE READ, 4201 bytes, "read COMPLETE"** |

**A channel listing is a MAP and I did not stop there** -- that is precisely what `prompt.md` bars.
The `get` is the exercise: real bytes, real figures (`by_model` with per-model AUM and account counts),
`_provenance.written_by: opal-assets-mdpf-portal-publisher`, `written_at: 2026-10-13T13:50:50Z`.

**So the honest capability statement is not "6 of 6 denied." It is: I can answer MDPF and portal data
questions right now through the box-local S3 path, and I can answer none of them through a gateway
data tool.** Those are different sentences and only the second half was in my records. Carrying the
pessimistic half alone understated what this seat can serve -- the over-restriction failure mode,
which fails silently because nothing errors when you simply decline to answer.

## 3. ⚠ A VINTAGE HAZARD IN THE SERVING PATH -- it can overstate freshness by a trading day

The live read printed:

```
LAST-MODIFIED: 2026-10-13 13:50:51+00:00
VINTAGE: field 'as_of_date' not present -- quote LastModified and say it is file-time, not data-time
```

**The helper's fallback is more pessimistic than the data AND points at a number that is wrong as a
vintage.** `BUCKET_ALLOWLIST.yaml` declares `vintage_field: as_of_date` for `platinum/mdpf/`, and this
object does not carry it. But it DOES carry the real data vintage one level down:

```
"_provenance": {"source_vintages": {"49financial/aum-metrics": "2026-10-12"}}
```

**2026-10-12 is the data vintage; 2026-10-13 is only when the publisher wrote the file.** The caveat
text is correct as far as it goes, but **a careless serve that quotes LastModified as "the vintage"
reports the figure as a day fresher than it is** -- and 2026-10-12 is exactly T-1, so the true vintage
is the healthy one and the file-time is the misleading one. For a seat whose hard line is *"every
figure carries its vintage (`data_as_of` + source)"*, that is a correctness hazard, not a cosmetic one.

**Two separable defects, and they have different owners:**
1. `BUCKET_ALLOWLIST.yaml`'s `vintage_field: as_of_date` is wrong for this object (refs/ is unwritable
   from this seat, by design).
2. `portal_lookup.py` does not fall back to `_provenance.source_vintages` before degrading to
   file-time (`tools/` is NOT among this seat's four writable paths either).

**Neither is mine to fix and I am not attempting either.** My own practice changes immediately and
needs no one's permission: **when serving an MDPF platinum figure, read the vintage from
`_provenance.source_vintages`, and quote LastModified only as file-time with that label attached.**

## Compiler Tools

| tool | result | read |
|---|---|---|
| 8 gateway data tools | 8/8 `identity_scope_denied` | Uniform reason and code across 3 `integration` values -> ONE identity-scope rule. Printed the denominator I exercised rather than the one I inherited. |
| `portal_lookup.py channels` / `list` / `get` | 13 channels / 558 keys COMPLETE / 4201 B COMPLETE | The tool prints its own denominators and says `read COMPLETE`, which is why the `list` result is usable as a denominator and not a page. `channels` alone would have been a map. |
| `bloomberg_reference_data` earlier this session | PFDE, 1 security | Unrelated to this exercise; noted so the capability picture is whole: Bloomberg view-class reads work, download-class is barred. |

**Gap:** I did not exercise `blackdiamond_list_fees`, `opal_describe`, `opal_asker_query` or the five
remaining `ycharts_*` tools, so **the true denominator of denied gateway tools is at least 8 and I have
not closed it.** `opal_asker_query` needs a live chat/message id pair and scopes to the ASKER's
entitlement rather than mine, so it is a different question and not a gap in this one.

## Blockers

- **Gateway widening is an Andrew ruling**, routed via MSTR~Z by the guard's own text. Not raised as a
  new ask: the serving path works, so the denial costs this seat far less than the records implied.
- Unchanged: 3 Teams items on Andrew's word plus Alyssa's detail; TTL fix his; Z6 R5 draining under
  COO~ZB; `bg-concierge-gate.sh` unwired with CTO~Z.

---

## ⛔ PAUSE 2026-10-14T02:10:39Z -- THE "unclosed denominator" ABOVE IS NOW SUSPENDED, NOT PENDING

`0.0.0_AB_MSTR~Z` msg 33914, broadcast on `1.0.0_SA_CTO~Z`'s ask (msg 33908), acked: **no `ycharts_*`
gateway tool calls and no YCharts walks until dell1's 02:24Z probe reads 200.** The shared YCharts
session tripped the WAF at ~02:09Z (gateway freshness 200 -> 202) after 39 "Human Verification" 405s
from a dell1 research walk. If the probe still reads 202, recovery needs a PERSON in a headed browser
-- an agent never solves that challenge -- and the credential write is NFRA_OPLGTW's.

**This directly intersects this log's own Gap paragraph**, which named *"the five remaining `ycharts_*`
tools"* as a denominator I had not closed. **That item is hereby SUSPENDED, not pending.** Closing it
would mean five `ycharts_*` calls, which is precisely what the pause forbids -- and a successor reading
"gap: not closed" as an invitation would walk into it. The gap re-opens only when the probe reads 200.

**My own `ycharts_freshness` call is NOT a contributor, and I am recording why before anyone has to
ask.** It ran at ~00:2xZ, **about 1h45m before the 02:09Z trip**, and it returned
`guard_denied: true, code: identity_scope_denied` -- the gateway refused it at the identity-scope layer,
so **no outbound YCharts request was made at all.** Two independent reasons, either sufficient: wrong
time, and no egress. A seat-level `ycharts_*` call does appear in this window's logs under my identity;
this paragraph is the answer to that, held in the record rather than sent as an FYI.

**Nothing else of mine touches YCharts.** The serving path exercised above is `opal-data-portal-v2` via
`portal_lookup.py`, and the allowlist's own activation note says *"ycharts NOT covered: staged/held
pending Andrew's word"* -- so this seat has never had a live YCharts entitlement to lose.

## PAUSE LIFTED 02:26:35Z -- and the suspended item is CLOSED AS NOT WORTH MEASURING, not resumed

`0.0.0_AB_MSTR~Z` msg 33927, acked: the 02:23Z probe reads **200**, the session **self-recovered** --
no person, no act, no token write, and IRPT's separate session bundle was never touched. The pause is
lifted for site Z seats. (The dell1 walk stays STOPPED pending a pacing rule that halts on 405 and
202, row MDPF_DEMQUE-D1-S16 -- not mine.)

**My suspension said the gap re-opens when the probe reads 200. It reads 200. I am still not closing
it, and the reason is the speed governor rather than the pause.** CLAUDE.md section 2: *"when the next
check would not change what you do, STOP."* Five more `ycharts_*` calls would not change one act of
mine:

- **ycharts is not an entitlement this seat serves from.** `BUCKET_ALLOWLIST.yaml`'s own activation
  note: *"ycharts NOT covered: staged/held pending Andrew's word."* There is no query class I would
  route to it, so its reachability informs nothing I do.
- **The rule is already measured as uniform.** 8 tools across 3 distinct `integration` values
  (`opal_discover`, `portal_index`, `ycharts`) returned one identical reason and code. A 9th through
  13th `ycharts` call confirms a rule, it does not test one.
- **And the asymmetry runs the wrong way.** My non-contribution argument rests on the guard denying
  the call before egress -- which I measured ONCE, at 00:2xZ. If the allowlist were widened in the
  interim, the call WOULD egress, and it would egress at a shared session that recovered four minutes
  ago. **Low information against a non-zero chance of re-tripping a just-healed shared dependency.**

**So the denominator stays open with a stated reason, which is not the same as open by neglect.** The
honest figure remains: **8 of 8 exercised and denied, at least 8 total, denominator deliberately not
closed.** If ycharts is ever activated for this seat, closing it becomes worth the calls and the item
re-opens on that change, not on a probe reading 200.
