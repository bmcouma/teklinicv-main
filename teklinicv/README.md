# TekliniCV

[![PyPI version](https://badge.fury.io/py/teklinicv.svg)](https://badge.fury.io/py/teklinicv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Formatted with Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

CV/Resume Generator by Teklini Technologies.

Transform structured CV input into professional PDFs with clean typography.

## Quick Start

1. Install:

```bash
pip install "teklinicv[full]"
```

2. Create a new CV:

```bash
teklinicv new "Your Name"
```

3. Render your CV:

```bash
teklinicv render "Your_Name_CV.yaml"
```

## Minimal Example YAML

```yaml
cv:
  name: "Your Name"
  email: "your.email@example.com"
  sections:
    Summary:
      - "This is a placeholder summary."
```

Powered by Teklini Technologies
