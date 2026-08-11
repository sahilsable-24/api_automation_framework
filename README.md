# API Test Automation Framework

![API Tests](https://github.com/sahilsable-24/api_automation_framework/actions/workflows/api-tests.yml/badge.svg)

A REST API test automation framework built with **Python, Requests, and Pytest**, targeting [reqres.in](https://reqres.in), a public REST API. Covers full CRUD coverage, JSON schema validation, negative/error-case testing, and a CI pipeline that runs automatically on every push.

## Why this project

Alongside a UI automation project, this framework demonstrates API-level testing — validating backend behavior directly, independent of any user interface. API tests run significantly faster than UI tests and catch a different class of bugs (data contracts, status codes, error handling), which is why most real testing pyramids rely heavily on this layer.

## Tech Stack

- **Requests** — HTTP client for sending GET/POST/PUT/DELETE calls
- **Pytest** — test runner, fixtures, parametrization
- **jsonschema** — validates full response structure, not just individual fields
- **python-dotenv** — keeps API keys out of source control
- **uv** — dependency and environment management
- **GitHub Actions** — CI pipeline with encrypted secrets for the API key

## Project Structure

```
api_automation_framework/
├── .github/workflows/api-tests.yml   # CI pipeline
├── data/
│   ├── config.py                # Base URL and API key (loaded from .env)
│   └── schemas.py                # JSON Schema definitions for response validation
├── tests/
│   ├── test_negative_cases.py            # Invalid input, missing auth, malformed requests
│   ├── test_users_delete.py             # Delete request test
│   ├── test_users_get.py             # Get request test
│   └── test_negative_post.py    # post request test
├── api_client.py               # Base API client (session, base URL, auth headers)
├── conftest.py                    # Shared pytest fixtures (api_client)
├── pyproject.toml                 # Project config and dependencies (managed by uv)
└── README.md
```

## Test Coverage — 16 tests

| Category | Count | What it covers |
|---|---|---|
| **Smoke** | 4 | Core happy-path checks across key endpoints — status codes, basic response shape |
| **Regression** | 7 | Full CRUD flows, JSON schema validation, parametrized coverage across paginated results |
| **Negative** | 5 | Invalid/non-numeric IDs, missing authentication, malformed JSON, missing required fields |

Tests are tagged with pytest markers so subsets can be run independently — e.g. a fast smoke check on every commit, full regression before a release.

## Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/sahilsable-24/api_automation_framework.git
cd api_automation_framework

# 2. Install dependencies with uv
uv sync

# 3. Add your API key
echo "API_KEY=your-key-here" > .env

# 4. Run the full suite
uv run pytest

# Run only smoke tests
uv run pytest -m smoke

# Run only negative/edge case tests
uv run pytest -m negative

# Run only regression tests
uv run pytest -m regression
```

After running, open `reports/report.html` for a full visual test report.

## CI/CD

Every push to `main` triggers the full suite via GitHub Actions on a fresh Ubuntu environment. The API key is injected securely via **GitHub Secrets** — never committed to source control or exposed in logs. Test reports are uploaded as workflow artifacts, downloadable from the **Actions** tab.

## Design Decisions

- **Base API client** — centralizes the base URL, session, and auth headers in one class, so a change to authentication or the target host only needs updating in one place.
- **Schema validation over field-by-field checks** — `jsonschema` validates the entire response structure (types, required fields) in one assertion, catching subtler bugs than checking individual fields would.
- **`.env` + GitHub Secrets** — the API key never touches source control locally or in CI, following standard secret-management practice.
- **Resource-based test organization** — tests are grouped by what they test (`users`, `auth`) rather than by HTTP method, mirroring how real API documentation and teams organize test coverage.
- **Honest negative testing** — several negative tests document actual observed API behavior (including cases where a public demo API is more lenient than a production system would be), rather than asserting an assumed "ideal" response.

## Possible Extensions

- Contract testing against an OpenAPI/Swagger spec
- Load/performance testing layer (e.g. Locust) alongside functional coverage
- Cross-checking API and UI state consistency (companion to the Playwright UI project)