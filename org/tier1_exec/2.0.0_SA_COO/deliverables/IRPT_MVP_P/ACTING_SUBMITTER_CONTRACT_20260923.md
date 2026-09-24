# Actual submitter and retained input attribution

Under5ad99c7d30 and CTO8b7d43d5eb, verified Opal may create a new analysis/report using another creator's retained input. This is required capability, not an unresolved permission choice. Implement source only under current owners; no deployment follows this contract.

## Exact roles and additive wire

- The current viewer is InteractiveAccess.current() from trusted request headers, never from stored owner metadata. Entry scope.current_owner is this actor. scope.prospect_owner is the server-loaded original prospect owner for an existing input, or the actual actor's new prospect owner for upload creation.
- For new submission, resolved.owner and the accepted request owner describe the real acting submitter, with real principal_id/home_firm_id/principal_class and the concrete storage firm. Retain exact input/account/snapshot attribution in that request owner; do not synthesize advisor identity. Request identity/idempotency remain keyed by concrete request firm + actual submitter + browser idempotency request_id.
- Add resolved.input_owner as the server-loaded original owner of the retained normalized input. It must exactly equal the normalized document owner and bind the immutable artifact/retention owner (allow only existing documented owner projections where the formats differ). Retain the original document, artifact reference, version, hash, creator, source firm, accounts and snapshot unchanged. Do not reupload or relabel the input.
- Compatibility: absent input_owner on legacy accepted compositions means resolved.owner, preserving existing same-owner documents. A new foreign-input composition must include input_owner explicitly. Closed schema/admission validation must recognize this field deliberately, not relax unknown-field rejection. The server resolves it; browser owner/viewer/placement claims cannot populate it.
- Current tranche remains one concrete input storage firm per request. Actual viewer may be Global or have another selected filter. Placement follows the server-resolved retained input, not an arbitrary first firm. Multiple-firm composite inputs need an attributed recipe and per-input placement; this contract does not invent one.

## Authorization and immutable replay

Before accepting a new request and before final dispatch, reauthorize the actual viewer against both the new request owner and original input owner, using the trusted current predicate. Verify the immutable input/receipt/retention binding under input_owner's data_firm. Preserve ordinary same-owner/same-firm behavior and forged/service-identity refusal. Stored creator identity is attribution, never an impersonated acting principal.

Artifact get/head and retention checks receive actual viewer plus explicit data_firm. Composition publication is owned by actual submitter; its dependencies keep original input retention refs. P's same-firm dependency DAG supports different creators without changing ownership. Every dependency must remain live; owner/identity/expiry changes during I/O refuse before release/dispatch.

Replay loads the accepted frozen composition; it does not re-resolve maintained sources, rewrite its original input owner, or refreeze another creator's profile. The original acceptance/idempotency owner stays the submitter of that accepted request. Another viewer reading/reopening it does not change that identity. A new submission by another Opal actor has its own request identity and separately records the unchanged input owner.

## Owned implementation and acceptance controls

Y owns submission/composition/admission/request schema wiring, dual-owner validation and exact byte retention/replay; return source pin and any concrete schema-owner dependency. M provides maintained-profile source semantics: input-derived descriptors use original input attribution; actor-specific configuration may name the actual submitter explicitly. Existing authorize_input(owner,input_ref) remains original-owner semantics unless a separately named current-viewer port is installed. Frozen profiles never change merely because their viewer changes.

P owns shared Entry/current viewer and repository/retention ports; source4ec461a2e9 and dd6edfc3aa are ready. Pair real implementations with offline storage, then submit exact source/runtime changes for CTO review. Required controls: Opal new submission of partner-created and Opal-created prospect input; actual submitter request identity; original normalized bytes/owner unchanged; stable retry; current authorization revoked before acceptance/dispatch; ordinary other-creator refusal; forged Opal/service role refusal; no reupload; immutable replay after maintained source changes.
