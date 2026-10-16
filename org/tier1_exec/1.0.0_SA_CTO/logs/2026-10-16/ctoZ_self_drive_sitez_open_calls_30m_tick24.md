# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 24 (2026-10-16 ~13:31Z to 13:57Z)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Rulings and acts (the 49F Black Diamond chain, in order)

All four sections are in `CTO_RULING_NFRA_MCPINDEX_R18_RESEARCH_32_OUT_OF_LINE_20261016_Z.md`.

| input | ruling | record |
|---|---|---|
| COO~MI 35027: re-keying `prefix` would list an empty S3 path (`typed_scope.py:79` uses it verbatim) | (a) an `address` lookup field; `prefix` stays the true path; `address` unique; the read goes to the row's own bucket. (b), an adapter-built path, refused | @ed33f552ae |
| CVO 35029, Z-S292 BLOCKING: `role_key` drops `-live`, and the `blackdiamond49f` role explicitly denies `opal-data-bd` | `-live` routes to a DEDICATED read-only role on exactly the four `opal-data-bd/silver/` prefixes (v3.6 item 2), never-widen with three halves; the old role keeps its Deny. The Deny's origin is this seat's A2 (msg 34134), overtaken by v3.6 | @8b2865e461 |
| COO~MI 35036: the 8 legacy rows describe the FROZEN `opal-data-assets` copy, not the live bd tables | REC ratified: four NEW live rows (`opal-data-bd`, `silver/<t>/`, `address`, `read_tool`, live freshness); the 8 re-bucketed to their real frozen prefix, still OUT. Rewrite-in-place refused | @96ea4ac3da |
| MSTR~Z 35033: the XB-95c2 follow-up was sent (bus ed9a8524); the to-side is closed by COO~C | from-side close HELD until COO~C answers the follow-up and a re-run reads Z-C-S79 MET | msg to MSTR~Z |
| MSTR~Z 35040: relay of Andrew-direct (dell2 CTO record @c2b2f1e950), "you can delete synthetic and test files any time, i do not need an open call or reserved call for that kind of behavior" | noted. No site Z call is of that class (ae72 is already CLOSED). Applied here once the record syncs and is read | -- |

**Release order:** `~MI`'s field and four rows, and `~O`'s address code, `-live` role, its ask and its test, ride ONE batched gateway release. OG-en-11
re-runs on the served host, and Z-S292 closes on that run.

## Scope state

7 open on site Z (54 rows), all `act`, all only Andrew can do; 0 forks: 21c5, f0d2, 8ed7, 21d9, def4, bd68 and 5b35 (as tick 23).

Waiting:
- COO~MP's MP-pf-9 half;
- the batched release (49F, OG-en-10's 429 audit, E9);
- COO~C on 95c2.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| safe-commit.sh | 3 ruling commits | OK |
| send_message / ack_messages | 4 sends, 4 acks | DELIVERED / READ |
| Monitor (inbox-watch.sh) | re-armed at 13:42Z | task b5l746bxg |

- **What failed:** the 49F chain took four rulings in 30 minutes, because each fix met the next layer (catalog key, S3 path, IAM Deny, frozen-vs-live rows). Each was caught by a seat measuring before cutting, which is the intended shape. The root is my ~13:1xZ ruling, made off the slug without reading the adapter, its lookup or its role.
