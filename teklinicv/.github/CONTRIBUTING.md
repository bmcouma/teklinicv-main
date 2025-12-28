# Contributing to TekliniCV

All contributions to TekliniCV are welcome!

## Development Setup

We use modern Python tooling to ensure a smooth development experience.

### Prerequisites

- [uv](https://github.com/astral-sh/uv) (for dependency management)
- [just](https://github.com/casey/just) (for command running)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/teklinicv/teklinicv.git
   cd teklinicv
   ```

2. Install dependencies:
   ```bash
   just sync
   ```

### Running Tests and Linting

We use `just` to run common tasks:

- **Format code**: `just format`
- **Lint code**: `just check`
- **Run tests**: `just test`
- **Build docs**: `just build-docs`

For more details, please see [the developer guide](https://docs.teklinicv.com/developer_guide).

