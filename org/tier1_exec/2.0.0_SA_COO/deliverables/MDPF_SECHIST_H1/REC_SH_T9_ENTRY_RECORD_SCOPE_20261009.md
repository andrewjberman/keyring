# REC -- MDPF_SECHIST SH-t-9: the entry/depth record's scope (global vs per firm)

**Author:** `2.0.0_SA_COO~H1`, 2026-10-09 ~14:5xZ. **For:** `1.0.0_SA_CTO~DELL1`, round-3 drain packet (msg 2558: "Bring SH-t-9's scope in the
drain packet with your REC").

## What exists (merged @4cd83dd5a2)

`data/mdpf/scripts/silver/security_entry_depth.py` builds ONE record at
`address("mdpf","global","silver","security_entry","as_of=<d>","entry_depth.json")` (`s3://opal-data-assets/mdpf/global/silver/...`). Per
security it lists each source with its required start -- including, for client accounts, each firm's first-appearance date under that
firm's own source key (`49financial`, `inflection`, `cottonwood`) -- and the governing (deepest) start. Nothing writes it yet.

## The question

C-DEPTH needs the deepest rule across sources, which is cross-firm by construction (one series per security, C-SERIES). But a global file
that carries each firm's first-appearance DATE puts firm-derived client facts side by side in one object. CLAUDE.md's NEVER line
("never reference another firm's data from a pipeline tree") and the IAM-parity condition ("49 Financial data never goes into another
firm's tree") are about firm trees; `mdpf/global` is not a firm tree, but the record would still be readable as "when did client firm X
first hold security Y" for every firm at once.

## REC: split -- per-firm records hold the dates; the global record holds only the governing start

1. Per firm: `address("mdpf", <firm>, "silver", "security_entry", "as_of=<d>", "entry_depth.json")` -- that firm's first-appearance date per
   security, in that firm's own scope (its tenancy rules apply).
2. Global: per security only `governing_start` and the governing SOURCE CLASS (`opal_etf` / `client_account` / `rival_fund`), never a firm
   name and never a per-firm date. That is all SECHIST's pull and writer need (C-DEPTH / C-SERIES).
3. Why: it keeps every firm-attributable fact inside that firm's scope, so no reader of the global record learns another firm's holding
   history, and the cross-firm guard (`.tools/ds-precommit-check.py`) has nothing to widen.
4. Cost: one small change to the merged module (two writes instead of one, the global record drops per-firm keys). It rides round 4 with
   the gap-record producer, before any writer of the entry record is wired. If the CTO prefers global-as-built, the condition is that no
   per-firm date is served from it.
