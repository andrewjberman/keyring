# BRIEF — retire `opal-data-mdpf`, the intermediary bucket

**DIRECTION: RULED by Andrew 2026-08-07 ~0230Z. EXECUTION: sequenced after the
`MDPF_CANONICAL_PLATINUM` rubric closes** (R1–R14 on one unattended scheduled cycle), unless he moves it.
**Author:** `1.0.0_SA_CTO~Z` · **Owner on execution:** `0.7.0_AE_CloudOps~Z` (infra) + `0.4.0_DS_ClientPlatform~Z` (producers)

> **ANDREW-DIRECT, VERBATIM:** *"i do not want a random bucket in between opal-data-assets and
> opal-data-portal-v2 that is fucking bullshit, anything that is in there of any value needs to be in
> opal-data-assets/portal/gold/mdpf, if you need /code as a subfolder in there, ok, if there needs to be
> some kind of /outputs folder for appends, ok, but no fucking random intermediary bucket that is
> fucking bullshit."*

**This is a DIRECTION ruling, not a proposal.** Rule 17b's "migration is NOT authorized by this line"
caveat does not apply — **this is his line, spoken directly at the bucket.** What remains sequenced is
*when*, not *whether*.

---

## 1 · WHY IT EXISTS — the code says so, and it was always meant to be temporary

`data/mdpf/scripts/gold/mdpf_aggregate_aua.py:65`:

```python
FEEDER_BUCKET = "opal-data-mdpf"   # non-portal intermediate bucket (AE finalizes at WS-B/C/D/E)
```

**"Non-portal intermediate bucket … AE finalizes at WS-B/C/D/E."** It was declared temporary at
authorship, pending workstreams that never finalized. It has since accumulated four more top-level
prefixes and a live production dependency.

**It is also outside CLAUDE.md Rule 17b's canonical form entirely** — that form is TWO buckets
(`opal-data-assets` for bronze/silver/gold, `opal-data-portal-v2/platinum` for serving). This is a third.

---

## 2 · MEASURED INVENTORY — 2026-08-07 ~0230Z

| prefix | objects | bytes | newest write | state |
|---|---|---|---|---|
| `mdpf/` (incl. `feeds/`) | **≥1,716 — FLOOR, NOT A TOTAL** ⚠ | ≥32.5 MB | **2026-08-06T13:33Z** | **LIVE** |
| `telemetry/` | 180 | 29.9 MB | **2026-08-07T01:04:46Z** | **LIVE** — written tonight |
| `code/` | 48 | 1.24 MB | **2026-08-07T00:59:59Z** | **LIVE** — written tonight |
| `bmkaud-evidence/` | 10 | 25.8 MB | 2026-06-01 | **COLD 67 days** |
| `cache/` | 1 | 317 KB | 2026-05-19 | **COLD 80 days** |

> ⚠ **THE `mdpf/` COUNT IS A FLOOR.** The `list-objects-v2 --query 'length(Contents)'` call returned
> **two rows** — the CLI auto-paginated and applied `--query` PER PAGE, the exact trap
> `CLAUDE.md:110` documents. **≥1,716 across ≥2 pages; the true total is UNKNOWN from that call.**
> **Whoever executes this MUST re-derive the count against a materialised, fully-paginated listing** —
> a migration sized against a page count is short by an unknown amount.

**`mdpf/feeds/` sub-prefixes (6):** `derivation_manifests/` · `etf_net_assets/` ·
`model_aua_positions/` · `model_composition/` · `non_model_aua/` · `partner_held_etf/`

---

## 3 · PER-PREFIX DISPOSITION

| prefix | disposition | grounding |
|---|---|---|
| `mdpf/feeds/` | **MIGRATE — do NOT delete.** Live producer chain: `wsb-49f-model-aua-daily` **writes** it; `opal-smartx-ingestion-pipeline` (3 deployed modules, in the source map) **reads** it; output is the **served** `{scope}/account-distribution.json`. | Andrew-direct ~2137Z: *"mdpf/feeds LIVE"* |
| `code/` | **MIGRATE or DIE WITH THE EC2** — see §5. Holds `mdpf-daily-dispatch.sh`, `config/route_bindings.yaml`, the production **roster**, and copies of the gold/assets scripts. | measured; G9 roster finding |
| `telemetry/` | **UNDISPOSITIONED — decide before migrating.** 180 objects, 29.9 MB, written tonight. Nobody has named its consumer. | measured |
| `cache/` | **DEAD WEIGHT** — 1 object, cold 80 days | Andrew-direct ~2137Z |
| `bmkaud-evidence/` | **DEAD WEIGHT** — 10 objects, cold 67 days | Andrew-direct ~2137Z |

⛔ **"Dead weight" is a disposition, not a deletion order.** Deleting S3 objects is on CLAUDE.md's
human-confirmation list and needs his word at the delete step.

---

## 4 · TARGET LAYOUT — and the one collision that must not be built

Per his ruling, everything of value lands under **`opal-data-assets/portal/gold/mdpf/`**.

> ### ⛔ THE COLLISION: `portal/gold/mdpf/` IS THE SCOPE-DISCOVERY LEVEL
> **Measured right now, that prefix contains EXACTLY four children — `49financial/`, `cottonwood/`,
> `global/`, `inflection/` — and they are ALL SCOPES.** The publisher's completeness model enumerates
> that level to find scopes.
>
> **A bare `code/` or `outputs/` there would be READ AS TWO MORE SCOPES.** Six children, four real
> scopes, and a completeness check that either miscounts or must special-case names — the exact
> denominator blindness recorded as H16.

**RESOLUTION — use the reserved-prefix convention the tree ALREADY has.** Doc 03 Phase 1 established it:
*"write a gold-run manifest under a reserved grammar such as `portal/gold/mdpf/_manifests/…`;
**explicitly exclude the reserved prefix from artifact discovery**."*

```
opal-data-assets/portal/gold/mdpf/
    49financial/ cottonwood/ global/ inflection/   <- SCOPES (discovered)
    _manifests/                                     <- reserved, already conventioned
    _code/                                          <- his /code, underscore-reserved
    _outputs/                                       <- his /outputs for appends, underscore-reserved
    _feeds/                                         <- migrated from opal-data-mdpf/mdpf/feeds/
```

**Underscore-prefixed and excluded from scope discovery.** This honours his permission exactly while
keeping the scope denominator at four. *A non-underscored sibling at this level is a defect, not a
style choice.*

---

## 5 · INTERACTIONS — three, and the first is new tonight

**5a · ⚠ THE NEW LAMBDA WAS JUST WIRED TO THE BUCKET WE ARE RETIRING.** At **02:12:46Z tonight**, the
first QA invoke hit `AccessDenied` on `opal-data-mdpf/mdpf/feeds/*`, and AE~Z closed it with a **scoped
Get + conditioned List grant** (@202a8f24a). Correct fix, correct method — but it means **the
consolidation currently ENTRENCHES the third bucket rather than resolving it.** The migration must
re-point that grant, and the grant is now a named artifact to retire rather than a thing to discover.

**5b · `code/` may die on its own.** `mdpf-daily-dispatch.sh:125` syncs `s3://opal-data-mdpf/code/scripts/`
onto the EC2 — **that sync dies with the EC2 retirement.** And the production roster's resolution from
that synced directory (the G9 nine-day-stale finding) is already superseded by the **build-generated
hash-tied copy** ruled in G13. **So `code/`'s two live dependencies both terminate inside the current
program.** Re-measure before migrating: it may need archiving, not moving.

**5c · `feeds/` is the hard one and it is NOT ours alone.** Its writer (`wsb-49f-model-aua-daily`) and
reader (`opal-smartx-ingestion-pipeline`) are **outside this program**. Migrating the prefix means
re-pointing a producer and a consumer that MDPF does not own — **an atomic cross-program change, not a
copy.** This is the item that sets the migration's real cost.

---

## 6 · PRECONDITIONS

- [ ] `MDPF_CANONICAL_PLATINUM` rubric R1–R14 PASS on one unattended scheduled cycle
- [ ] `mdpf/` object count **re-derived against a fully-paginated listing** (§2's floor replaced by a total)
- [ ] `telemetry/` consumer named, or explicitly recorded as unowned
- [ ] `code/`'s two dependencies re-measured post-EC2-retirement
- [ ] `feeds/` producer + consumer owners engaged — cross-program, atomic
- [ ] S3 deletions confirmed by Andrew at the delete step (standing law)

---

## 7 · WHAT THIS BRIEF DOES NOT AUTHORIZE

**No move, no copy, no delete, no grant change today.** The direction is ruled; the execution is
sequenced behind the rubric. **Do not scope any part of this into the current build** — the program has
refused exactly this kind of adjacent-and-cheap-looking widening all night, and this one has a live
serving chain on the other end of it.
