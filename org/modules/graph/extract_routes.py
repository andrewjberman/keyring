"""
Route extractor -- maps the full serving path from S3 artifact to frontend component.

Authoritative sources:
  1. cloudfront-distribution.tf  -- behaviors, origins, Lambda@Edge associations
  2. shared-advisor-router/index.mjs -- URL->S3 key rewrite rules
  3. api-gateway.tf files -- API GW route_key -> Lambda mapping
  4. advisor-intelligence.ts (+ other endpoint files) -- frontend function -> URL
  5. *.tsx components -- component -> function imports + calls

Builds a route table where each entry is:
  path_pattern -> origin -> [edge_functions] -> auth_layers -> s3_key_or_lambda -> endpoint_fn -> component

Zero API calls. Pure static analysis from Terraform + source.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class CloudFrontOrigin:
    """A CloudFront origin."""
    origin_id: str           # e.g., S3-opal-data-bd
    domain_name: str         # e.g., opal-data-bd.s3.us-east-1.amazonaws.com
    origin_type: str         # "s3" or "api_gateway"
    origin_path: str = ""    # e.g., /prod for API GW
    bucket_name: str = ""    # for S3 origins: opal-data-bd
    oai_or_oac: str = ""     # OAI or OAC identifier


@dataclass
class EdgeFunction:
    """A Lambda@Edge association on a behavior."""
    event_type: str          # viewer-request, origin-request, origin-response
    function_name: str       # e.g., auth-validator-edge
    arn: str = ""


@dataclass
class CloudFrontBehavior:
    """A CloudFront cache behavior (ordered or default)."""
    path_pattern: str        # e.g., /api/scoped/advisor-intelligence/artifacts/*/*
    origin_id: str           # target origin
    edge_functions: list[EdgeFunction] = field(default_factory=list)
    has_auth: bool = False   # True if auth-validator-edge is attached
    has_router: bool = False # True if shared-advisor-router is attached
    order: int = 0           # position in behavior list
    comment: str = ""        # from TF comments


@dataclass
class EdgeVersionBinding:
    """A Lambda@Edge version binding from the locals block."""
    local_name: str          # e.g., auth_validator_edge_arn
    function_name: str       # e.g., auth-validator-edge
    pinned_version: int | None = None   # e.g., 9 (None if dynamic)
    is_dynamic: bool = False             # True if uses qualified_arn
    tf_resource: str = ""                # e.g., aws_lambda_function.auth_validator_edge
    raw_value: str = ""                  # full RHS from locals block


@dataclass
class CustomErrorResponse:
    """A CloudFront custom error response rule."""
    error_code: int              # e.g., 403, 404, 500
    response_code: int           # e.g., 200 (CF substitutes this)
    response_page_path: str      # e.g., /index.html
    ttl_seconds: int = 0         # error_caching_min_ttl


@dataclass
class RewriteRule:
    """A URL->S3 key rewrite rule from Lambda@Edge router."""
    url_prefix: str          # matched URL prefix
    s3_prefix: str           # rewritten S3 key prefix
    condition: str = ""      # e.g., "suffix.startsWith('advisors/')"


@dataclass
class ApiGatewayRoute:
    """An API Gateway route."""
    route_key: str           # e.g., GET /api/scoped/advisor-intelligence/timeseries/{dimension}
    method: str = ""         # GET, POST, etc.
    path: str = ""           # /api/scoped/advisor-intelligence/timeseries/{dimension}
    lambda_name: str = ""    # target Lambda
    tf_file: str = ""        # source Terraform file
    pipeline: str = ""       # pipeline name


@dataclass
class EndpointFunction:
    """A frontend API endpoint function."""
    name: str                # e.g., getPartnerAnalytics
    url_template: str = ""   # URL pattern this function calls
    source_file: str = ""    # e.g., portal/src/api/endpoints/advisor-intelligence.ts


@dataclass
class ComponentBinding:
    """A React component that calls endpoint functions."""
    name: str                # e.g., PartnerAnalytics
    file_path: str = ""
    endpoint_calls: list[str] = field(default_factory=list)  # function names called


@dataclass
class Route:
    """A complete route from S3 artifact to frontend component."""
    # Request path
    url_pattern: str = ""              # what the browser requests
    # CloudFront layer
    cf_behavior: str = ""              # matching behavior path_pattern
    cf_origin: str = ""                # origin ID
    cf_origin_type: str = ""           # s3 or api_gateway
    # Auth layer
    auth_edge: bool = False            # auth-validator-edge present
    auth_api_gw: bool = False          # API GW authorizer present
    auth_lambda: str = ""              # Lambda-level auth check
    # Routing layer
    edge_router: str = ""              # shared-advisor-router, public-data-router, etc.
    s3_rewrite: str = ""               # rewritten S3 key (if S3 origin)
    api_gw_route: str = ""             # API GW route_key (if API GW origin)
    # Backend
    lambda_handler: str = ""           # Lambda that handles the request
    s3_key: str = ""                   # final S3 key read (by router or Lambda)
    # Frontend
    endpoint_function: str = ""        # JS function that makes the call
    components: list[str] = field(default_factory=list)  # React components


@dataclass
class RoutingTable:
    """Complete routing table for the portal."""
    origins: dict[str, CloudFrontOrigin] = field(default_factory=dict)
    behaviors: list[CloudFrontBehavior] = field(default_factory=list)
    custom_error_responses: list[CustomErrorResponse] = field(default_factory=list)
    rewrite_rules: list[RewriteRule] = field(default_factory=list)
    api_gw_routes: list[ApiGatewayRoute] = field(default_factory=list)
    endpoints: dict[str, EndpointFunction] = field(default_factory=dict)
    components: list[ComponentBinding] = field(default_factory=list)
    routes: list[Route] = field(default_factory=list)

    def match_behavior(self, url: str) -> CloudFrontBehavior | None:
        """Match a URL to the most specific CloudFront behavior.
        CloudFront evaluates ordered behaviors first (most specific wins),
        then falls back to the default behavior."""
        # Check ordered behaviors first (order > 0), then default (order == 0)
        ordered = [b for b in self.behaviors if b.order > 0]
        default = [b for b in self.behaviors if b.order == 0]
        # Within ordered behaviors, more specific patterns (longer, more segments) win.
        # CloudFront checks them in declared order, so we preserve that.
        for b in ordered:
            if _cf_pattern_matches(b.path_pattern, url):
                return b
        for b in default:
            if _cf_pattern_matches(b.path_pattern, url):
                return b
        return None

    def match_api_route(self, url: str) -> ApiGatewayRoute | None:
        """Match a URL to an API Gateway route."""
        for r in self.api_gw_routes:
            if _api_route_matches(r.path, url):
                return r
        return None

    def resolve_s3_key(self, url: str) -> str:
        """Apply rewrite rules to resolve a URL to an S3 key."""
        for rule in self.rewrite_rules:
            if url.startswith(rule.url_prefix):
                suffix = url[len(rule.url_prefix):]
                return rule.s3_prefix + suffix
        return ""


def _cf_pattern_matches(pattern: str, url: str) -> bool:
    """CloudFront pattern matching. * matches any characters including /."""
    # Strip query params from URL before matching
    url_path = url.split('?')[0]
    # CloudFront * matches everything (including slashes), unlike nginx
    regex = re.escape(pattern).replace(r'\*', '.*')
    regex = '^' + regex + '$'
    return bool(re.match(regex, url_path))


def _api_route_matches(route_path: str, url: str) -> bool:
    """API Gateway route matching. {param} matches one path segment."""
    regex = re.sub(r'\{[^}]+\}', '[^/]+', re.escape(route_path))
    regex = '^' + regex.replace(r'\*', '.*') + '(?:\\?.*)?$'
    return bool(re.match(regex, url))


# ---------------------------------------------------------------------------
# Step 1: Parse CloudFront distribution Terraform
# ---------------------------------------------------------------------------

def _parse_cloudfront(workspace_root: Path) -> tuple[dict[str, CloudFrontOrigin], list[CloudFrontBehavior], list[CustomErrorResponse]]:
    """Parse cloudfront-distribution.tf for origins and behaviors."""
    cf_file = workspace_root / "infra" / "aws" / "terraform" / "portal-auth" / "cloudfront-distribution.tf"
    if not cf_file.exists():
        return {}, [], []

    content = cf_file.read_text(encoding="utf-8", errors="replace")

    # Parse edge function name from ARN locals (handles both hardcoded and qualified_arn)
    edge_name_map: dict[str, str] = {}  # local var -> function name
    # Hardcoded: "${local.edge_arn_prefix}:auth-validator-edge:9"
    for m in re.finditer(r'(\w+_arn)\s*=\s*"\$\{local\.edge_arn_prefix\}:([^:]+):\d+"', content):
        edge_name_map[m.group(1)] = m.group(2)
    # Dynamic/ternary: ...qualified_arn : "${...}:shared-advisor-router:13"
    for m in re.finditer(r'(\w+_arn)\s*=.*?:([a-z][a-z0-9_-]+):\d+"', content):
        if m.group(1) not in edge_name_map:
            edge_name_map[m.group(1)] = m.group(2)

    # Parse origins
    origins: dict[str, CloudFrontOrigin] = {}
    for m in re.finditer(r'origin\s*\{', content):
        block = _extract_tf_block(content, m.start())
        origin_id_m = re.search(r'origin_id\s*=\s*"([^"]+)"', block)
        domain_m = re.search(r'domain_name\s*=\s*"([^"]+)"', block)
        if not origin_id_m or not domain_m:
            continue

        origin_id = origin_id_m.group(1)
        domain = domain_m.group(1)
        origin_path_m = re.search(r'origin_path\s*=\s*"([^"]+)"', block)

        is_s3 = 's3_origin_config' in block
        bucket_name = domain.split('.')[0] if is_s3 else ""

        oai_m = re.search(r'origin_access_identity\s*=\s*"([^"]*)"', block)
        oac_m = re.search(r'origin_access_control_id\s*=\s*"([^"]*)"', block)
        oai_or_oac = ""
        if oac_m and oac_m.group(1):
            oai_or_oac = f"OAC:{oac_m.group(1)}"
        elif oai_m and oai_m.group(1):
            oai_or_oac = f"OAI:{oai_m.group(1)}"

        origins[origin_id] = CloudFrontOrigin(
            origin_id=origin_id,
            domain_name=domain,
            origin_type="s3" if is_s3 else "api_gateway",
            origin_path=origin_path_m.group(1) if origin_path_m else "",
            bucket_name=bucket_name,
            oai_or_oac=oai_or_oac,
        )

    # Parse behaviors
    behaviors: list[CloudFrontBehavior] = []

    # Default behavior
    default_m = re.search(r'default_cache_behavior\s*\{', content)
    if default_m:
        block = _extract_tf_block(content, default_m.start())
        origin_m = re.search(r'target_origin_id\s*=\s*"([^"]+)"', block)
        behaviors.append(CloudFrontBehavior(
            path_pattern="/*",
            origin_id=origin_m.group(1) if origin_m else "",
            order=0,
            comment="default (SPA)",
        ))

    # Ordered behaviors
    order = 1
    for m in re.finditer(r'ordered_cache_behavior\s*\{', content):
        block = _extract_tf_block(content, m.start())
        pattern_m = re.search(r'path_pattern\s*=\s*"([^"]+)"', block)
        origin_m = re.search(r'target_origin_id\s*=\s*"([^"]+)"', block)
        if not pattern_m or not origin_m:
            continue

        # Extract edge functions
        edge_fns: list[EdgeFunction] = []
        for ef_m in re.finditer(r'lambda_function_association\s*\{([^}]+)\}', block):
            ef_block = ef_m.group(1)
            event_m = re.search(r'event_type\s*=\s*"([^"]+)"', ef_block)
            arn_m = re.search(r'lambda_arn\s*=\s*local\.(\w+)', ef_block)
            if event_m and arn_m:
                fn_name = edge_name_map.get(arn_m.group(1), arn_m.group(1))
                edge_fns.append(EdgeFunction(
                    event_type=event_m.group(1),
                    function_name=fn_name,
                ))

        has_auth = any(ef.function_name == 'auth-validator-edge' for ef in edge_fns)
        has_router = any(ef.function_name in ('shared-advisor-router', 'public-data-router')
                         for ef in edge_fns)

        # Extract comment above behavior (look for # N. comment)
        block_start = m.start()
        preceding = content[max(0, block_start - 200):block_start]
        comment_m = re.search(r'#\s*\d+[a-z]?\.\s*(.+)', preceding)
        comment = comment_m.group(1).strip() if comment_m else ""

        behaviors.append(CloudFrontBehavior(
            path_pattern=pattern_m.group(1),
            origin_id=origin_m.group(1),
            edge_functions=edge_fns,
            has_auth=has_auth,
            has_router=has_router,
            order=order,
            comment=comment,
        ))
        order += 1

    # Parse custom_error_response blocks
    custom_error_responses: list[CustomErrorResponse] = []
    for m in re.finditer(r'custom_error_response\s*\{', content):
        block = _extract_tf_block(content, m.start())

        error_code_m = re.search(r'error_code\s*=\s*(\d+)', block)
        response_code_m = re.search(r'response_code\s*=\s*(\d+)', block)
        response_page_m = re.search(r'response_page_path\s*=\s*"([^"]+)"', block)
        ttl_m = re.search(r'error_caching_min_ttl\s*=\s*(\d+)', block)

        if error_code_m and response_code_m and response_page_m:
            custom_error_responses.append(CustomErrorResponse(
                error_code=int(error_code_m.group(1)),
                response_code=int(response_code_m.group(1)),
                response_page_path=response_page_m.group(1),
                ttl_seconds=int(ttl_m.group(1)) if ttl_m else 0,
            ))

    return origins, behaviors, custom_error_responses


def parse_edge_versions(workspace_root: Path) -> list[EdgeVersionBinding]:
    """Parse the locals block in cloudfront-distribution.tf for Lambda@Edge version bindings.

    Detects hardcoded version numbers (`:9`) vs dynamic references (`qualified_arn`).
    Cross-references against aws_lambda_function resources in lambda-edge.tf.
    """
    cf_file = workspace_root / "infra" / "aws" / "terraform" / "portal-auth" / "cloudfront-distribution.tf"
    edge_tf = workspace_root / "infra" / "aws" / "terraform" / "portal-auth" / "lambda-edge.tf"

    if not cf_file.exists():
        return []

    content = cf_file.read_text(encoding="utf-8", errors="replace")

    # Build map of Lambda resource names -> tf resource identifiers from lambda-edge.tf
    resource_map: dict[str, str] = {}  # function-name -> aws_lambda_function.X
    if edge_tf.exists():
        edge_content = edge_tf.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(
            r'resource\s+"aws_lambda_function"\s+"(\w+)"\s*\{', edge_content
        ):
            tf_name = m.group(1)
            block = _extract_tf_block(edge_content, m.start())
            fn_m = re.search(r'function_name\s*=\s*"([^"]+)"', block)
            if fn_m:
                resource_map[fn_m.group(1)] = f"aws_lambda_function.{tf_name}"

    # Parse the locals block for _arn assignments
    locals_m = re.search(r'locals\s*\{', content)
    if not locals_m:
        return []

    locals_block = _extract_tf_block(content, locals_m.start())

    bindings: list[EdgeVersionBinding] = []
    for m in re.finditer(
        r'(\w+_arn)\s*=\s*(.+)', locals_block
    ):
        local_name = m.group(1)
        raw_value = m.group(2).strip().rstrip(',')

        # Skip the prefix definition itself
        if local_name == "edge_arn_prefix":
            continue

        # Detect dynamic (qualified_arn) vs hardcoded
        is_dynamic = "qualified_arn" in raw_value

        # Extract function name from either pattern
        fn_name = ""
        pinned_version = None

        # Hardcoded: "${local.edge_arn_prefix}:auth-validator-edge:9"
        hardcoded_m = re.search(r':([a-z][a-z0-9_-]+):(\d+)', raw_value)
        if hardcoded_m:
            fn_name = hardcoded_m.group(1)
            if not is_dynamic:
                pinned_version = int(hardcoded_m.group(2))

        # Dynamic: aws_lambda_function.shared_advisor_router[0].qualified_arn
        dynamic_m = re.search(r'aws_lambda_function\.(\w+)\[?\d*\]?\.qualified_arn', raw_value)
        if dynamic_m:
            tf_name = dynamic_m.group(1)
            # Resolve function name from resource if available
            for fname, res in resource_map.items():
                if res == f"aws_lambda_function.{tf_name}":
                    fn_name = fname
                    break
            if not fn_name:
                fn_name = tf_name.replace('_', '-')

        # Ternary: may have both dynamic and hardcoded (fallback)
        # e.g., var.enable_lambda_edge ? ...qualified_arn : "${...}:shared-advisor-router:13"
        if "?" in raw_value and is_dynamic and hardcoded_m:
            # Ternary with qualified_arn on true branch and hardcoded fallback
            fallback_m = re.search(r':\s*"[^"]*:([a-z][a-z0-9_-]+):(\d+)"', raw_value)
            if fallback_m and not fn_name:
                fn_name = fallback_m.group(1)

        if not fn_name:
            continue

        tf_resource = resource_map.get(fn_name, "")

        bindings.append(EdgeVersionBinding(
            local_name=local_name,
            function_name=fn_name,
            pinned_version=pinned_version,
            is_dynamic=is_dynamic,
            tf_resource=tf_resource,
            raw_value=raw_value,
        ))

    return bindings


def _extract_tf_block(content: str, start: int) -> str:
    """Extract a Terraform {} block starting from a position."""
    brace_pos = content.find('{', start)
    if brace_pos == -1:
        return ""
    depth = 1
    i = brace_pos + 1
    while i < len(content) and depth > 0:
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
        i += 1
    return content[brace_pos:i]


# ---------------------------------------------------------------------------
# Step 2: Parse shared-advisor-router rewrite rules
# ---------------------------------------------------------------------------

def _parse_rewrite_rules(workspace_root: Path) -> list[RewriteRule]:
    """Parse Lambda@Edge routers for URL->S3 rewrite rules."""
    rules: list[RewriteRule] = []

    # shared-advisor-router
    router_file = workspace_root / "infra" / "aws" / "lambda-edge" / "shared-advisor-router" / "index.mjs"
    if router_file.exists():
        content = router_file.read_text(encoding="utf-8", errors="replace")

        # Parse the if/else chain in the router (order matters -- more specific first)
        # suffix.startsWith("advisors/") -> /gold/entities/ + suffix
        rules.append(RewriteRule(
            url_prefix="/api/scoped/advisor-intelligence/advisors/",
            s3_prefix="gold/entities/advisors/",
            condition="advisors/* entities",
        ))
        rules.append(RewriteRule(
            url_prefix="/api/scoped/advisor-intelligence/views/",
            s3_prefix="gold/views/",
            condition="views/* passthrough",
        ))
        rules.append(RewriteRule(
            url_prefix="/api/scoped/advisor-intelligence/timeseries/",
            s3_prefix="gold/timeseries/",
            condition="timeseries/* passthrough",
        ))
        rules.append(RewriteRule(
            url_prefix="/api/scoped/advisor-intelligence/artifacts/",
            s3_prefix="gold/artifacts/",
            condition="artifacts/* passthrough",
        ))
        rules.append(RewriteRule(
            url_prefix="/api/scoped/advisor-intelligence/entities/",
            s3_prefix="gold/entities/",
            condition="entities/* passthrough",
        ))
        # ADVI_49PUSH: platinum/ paths route directly to platinum/ (no gold/ prefix)
        # Router index.mjs L116-120: suffix.startsWith("platinum/") -> "/" + suffix
        rules.append(RewriteRule(
            url_prefix="/api/scoped/advisor-intelligence/platinum/",
            s3_prefix="platinum/",
            condition="platinum/* passthrough (ADVI_49PUSH)",
        ))
        # Default: everything else -> gold/artifacts/
        rules.append(RewriteRule(
            url_prefix="/api/scoped/advisor-intelligence/",
            s3_prefix="gold/artifacts/",
            condition="default (legacy flat paths)",
        ))

    # public-data-router (for /api/general/ paths)
    public_router = workspace_root / "infra" / "aws" / "lambda-edge" / "public-data-router" / "index.mjs"
    if public_router.exists():
        # /api/general/json/... -> /json/...
        rules.append(RewriteRule(
            url_prefix="/api/general/json/",
            s3_prefix="json/",
            condition="general json passthrough",
        ))
        rules.append(RewriteRule(
            url_prefix="/api/general/json-tiered/",
            s3_prefix="json-tiered/",
            condition="general json-tiered passthrough",
        ))

    return rules


# ---------------------------------------------------------------------------
# Step 3: Parse API Gateway routes
# ---------------------------------------------------------------------------

def _parse_api_gw_routes(workspace_root: Path) -> list[ApiGatewayRoute]:
    """Parse API Gateway route_key definitions from Terraform."""
    routes: list[ApiGatewayRoute] = []
    tf_base = workspace_root / "infra" / "aws" / "terraform"

    for pipeline_dir in sorted(tf_base.iterdir()):
        if not pipeline_dir.is_dir():
            continue

        for tf_file in pipeline_dir.glob("api-gateway*.tf"):
            try:
                content = tf_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            rel_path = str(tf_file.relative_to(workspace_root)).replace("\\", "/")

            for m in re.finditer(r'route_key\s*=\s*"([^"]+)"', content):
                route_key = m.group(1)
                parts = route_key.split(' ', 1)
                method = parts[0] if len(parts) == 2 else "ANY"
                path = parts[1] if len(parts) == 2 else parts[0]

                # Try to find target Lambda from integration in same block
                block_start = content.rfind('resource ', 0, m.start())
                if block_start >= 0:
                    block = _extract_tf_block(content, block_start)
                    # integration_uri pattern
                    int_m = re.search(r'integration_uri\s*=\s*(?:module\.(\w+)\.invoke_arn|aws_lambda_function\.(\w+)\.invoke_arn|"([^"]+)")', block)
                    lambda_name = ""
                    if int_m:
                        lambda_name = int_m.group(1) or int_m.group(2) or int_m.group(3) or ""

                routes.append(ApiGatewayRoute(
                    route_key=route_key,
                    method=method,
                    path=path,
                    lambda_name=lambda_name,
                    tf_file=rel_path,
                    pipeline=pipeline_dir.name,
                ))

    return routes


# ---------------------------------------------------------------------------
# Step 4: Parse frontend endpoint functions
# ---------------------------------------------------------------------------

def _parse_frontend_endpoints(workspace_root: Path) -> dict[str, EndpointFunction]:
    """Parse portal/src/api/endpoints/*.ts for function->URL mappings."""
    endpoints: dict[str, EndpointFunction] = {}
    api_dir = workspace_root / "portal" / "src" / "api" / "endpoints"
    if not api_dir.exists():
        return endpoints

    # Pattern: export async function getFoo(...) { ... apiRequest<T>(`/api/...`) }
    fn_pattern = re.compile(r'export\s+(?:async\s+)?function\s+(\w+)\s*\(')

    # Pre-scan: extract file-level URL constants (e.g., PLATINUM_BASE, API_BASE_URL)
    # These are used in template literals: `${PLATINUM_BASE}/firm/dashboard.json`
    file_constants: dict[str, dict[str, str]] = {}  # filename -> {const_name: value}

    for ts_file in sorted(api_dir.glob("*.ts")):
        try:
            content = ts_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        consts: dict[str, str] = {}
        for cm in re.finditer(r"(?:const|let)\s+(\w+)\s*=\s*['\"]([^'\"]+)['\"]", content):
            name, value = cm.group(1), cm.group(2)
            if '/' in value:  # only URL-like constants
                consts[name] = value
        file_constants[ts_file.name] = consts

    for ts_file in sorted(api_dir.glob("*.ts")):
        try:
            content = ts_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        rel_path = str(ts_file.relative_to(workspace_root)).replace("\\", "/")
        consts = file_constants.get(ts_file.name, {})
        fn_starts = list(fn_pattern.finditer(content))

        for i, fm in enumerate(fn_starts):
            fn_name = fm.group(1)
            start = fm.start()
            end = fn_starts[i + 1].start() if i + 1 < len(fn_starts) else len(content)
            chunk = content[start:end]

            # Extract URL from apiRequest, fetch, or template literal
            url = ""
            # apiRequest<T>('/api/...')  or  apiRequest<T>(`/api/...`)
            url_m = re.search(r'apiRequest\s*<[^>]*>\s*\(\s*[`\'"]([^`\'"]+)[`\'"]', chunk)
            if url_m:
                url = url_m.group(1)
            else:
                # apiRequest<T>(`${base}...`) where base is defined earlier
                url_m = re.search(r'apiRequest\s*<[^>]*>\s*\(\s*`([^`]+)`', chunk)
                if url_m:
                    url = url_m.group(1)
                else:
                    # fetch(url, ...) where url is built from a const
                    url_m = re.search(r"const\s+(?:url|base|endpoint)\s*=\s*[`'\"](/[^`'\"]+)[`'\"]", chunk)
                    if url_m:
                        url = url_m.group(1)
                    else:
                        # const base = `${CONST}/path`; ... apiRequest(base) or fetch(url)
                        url_m = re.search(r"const\s+(?:url|base)\s*=\s*`([^`]+)`", chunk)
                        if url_m:
                            url = url_m.group(1)

            # Resolve file-level constants in template literals: ${PLATINUM_BASE} -> /api/scoped/...
            for const_name, const_value in consts.items():
                url = url.replace(f'${{{const_name}}}', const_value)

            # Clean remaining template literal interpolations (dynamic params)
            url = re.sub(r'\$\{[^}]+\}', '{param}', url)

            endpoints[fn_name] = EndpointFunction(
                name=fn_name,
                url_template=url,
                source_file=rel_path,
            )

    return endpoints


# ---------------------------------------------------------------------------
# Step 5: Parse component -> endpoint bindings
# ---------------------------------------------------------------------------

def _parse_component_bindings(workspace_root: Path, endpoints: dict[str, EndpointFunction]) -> list[ComponentBinding]:
    """Parse .tsx files for which endpoint functions they import and call."""
    bindings: list[ComponentBinding] = []
    pages_dir = workspace_root / "portal" / "src" / "pages"
    if not pages_dir.exists():
        return bindings

    import_pattern = re.compile(r'import\s*\{([^}]+)\}\s*from\s*[\'"]([^\'"]+)[\'"]')

    for tsx_file in sorted(pages_dir.rglob("*.tsx")):
        try:
            content = tsx_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        rel_path = str(tsx_file.relative_to(workspace_root)).replace("\\", "/")

        # Find endpoint imports
        imported_fns: set[str] = set()
        for m in import_pattern.finditer(content):
            source = m.group(2)
            if 'api/' in source or 'endpoints/' in source:
                names = [n.strip().split(' as ')[0].strip()
                         for n in m.group(1).split(',')]
                for name in names:
                    if name in endpoints:
                        imported_fns.add(name)

        if not imported_fns:
            continue

        # Check which are actually called
        called_fns = []
        for fn_name in imported_fns:
            if re.search(rf'\b{re.escape(fn_name)}\s*\(', content):
                called_fns.append(fn_name)

        if called_fns:
            bindings.append(ComponentBinding(
                name=tsx_file.stem,
                file_path=rel_path,
                endpoint_calls=sorted(called_fns),
            ))

    return bindings


# ---------------------------------------------------------------------------
# Main: build the complete routing table
# ---------------------------------------------------------------------------

def build_routing_table(workspace_root: Path) -> RoutingTable:
    """Build the complete routing table from all authoritative sources."""
    rt = RoutingTable()

    # Step 1: CloudFront
    origins, behaviors, custom_error_responses = _parse_cloudfront(workspace_root)
    rt.origins = origins
    rt.behaviors = behaviors
    rt.custom_error_responses = custom_error_responses

    # Step 2: Rewrite rules
    rt.rewrite_rules = _parse_rewrite_rules(workspace_root)

    # Step 3: API Gateway
    rt.api_gw_routes = _parse_api_gw_routes(workspace_root)

    # Step 4: Frontend endpoints
    rt.endpoints = _parse_frontend_endpoints(workspace_root)

    # Step 5: Component bindings
    rt.components = _parse_component_bindings(workspace_root, rt.endpoints)

    # Step 6: Build resolved routes (connect endpoint URLs through the full chain)
    for fn_name, ep in rt.endpoints.items():
        if not ep.url_template:
            continue

        url = ep.url_template
        route = Route(url_pattern=url, endpoint_function=fn_name)

        # Match CloudFront behavior
        behavior = rt.match_behavior(url)
        if behavior:
            route.cf_behavior = behavior.path_pattern
            route.cf_origin = behavior.origin_id
            route.auth_edge = behavior.has_auth
            route.edge_router = next(
                (ef.function_name for ef in behavior.edge_functions
                 if ef.event_type == "origin-request"), ""
            )

            origin = rt.origins.get(behavior.origin_id)
            if origin:
                route.cf_origin_type = origin.origin_type

                if origin.origin_type == "s3":
                    # Resolve S3 key via rewrite rules
                    s3_key = rt.resolve_s3_key(url)
                    route.s3_key = s3_key
                    route.s3_rewrite = s3_key

                elif origin.origin_type == "api_gateway":
                    route.auth_api_gw = True
                    # Match API GW route
                    api_route = rt.match_api_route(url)
                    if api_route:
                        route.api_gw_route = api_route.route_key
                        route.lambda_handler = api_route.lambda_name

        # Find components that call this endpoint
        for comp in rt.components:
            if fn_name in comp.endpoint_calls:
                route.components.append(comp.name)

        rt.routes.append(route)

    return rt
