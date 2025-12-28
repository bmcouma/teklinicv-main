# Get Started

## Installation

1. Install [Python](https://www.python.org/downloads/) (3.12 or newer).

2. Run the command below to install TekliniCV.

    === "pip"

        ```
        pip install "teklinicv[full]"
        ```

    === "pipx"

        ```
        pipx install "teklinicv[full]"
        ```

    === "uv"

        ```
        uv tool install "teklinicv[full]"
        ```

    === "Docker"

        Docker image is available at [ghcr.io/teklinicv/teklinicv](https://github.com/teklinicv/teklinicv/pkgs/container/teklinicv).

        ```bash
        docker run -v "$PWD":/work -w /work ghcr.io/teklinicv/teklinicv new "Your Name"
        ```

## Quick Start

1. Create a new CV YAML input file

    ```bash
    teklinicv new "Your Name"
    ```

    This creates a YAML input file called `Your_Name_CV.yaml`. This file contains the content, design options, translations and settings for TekliniCV. See [YAML Input Structure](yaml_input_structure/index.md) for the full reference.

    See the [CLI Reference](cli_reference.md#teklinicv-new) for the complete list of options available for the `new` command.

    !!! tip
        To get started with another language or theme, you can use the `--locale` and `--theme` options:

        ```bash
        teklinicv new "Your Name" --locale "turkish" --theme "engineeringresumes"
        ```


2. Render the YAML input file with

    ```bash
    teklinicv render "Your_Name_CV.yaml"
    ```

    This generates a `teklinicv_output/` directory containing:

    - `John_Doe_CV.pdf`: Your CV as PDF
    - `John_Doe_CV.typ`: [Typst](https://typst.app) source code of the PDF
    - `John_Doe_CV_1.png`, `..._2.png`, ...: PNG images of each page of the PDF
    - `John_Doe_CV.md`: Your CV as Markdown
    - `John_Doe_CV.html`: Your CV as HTML (generated from the Markdown)

    See the [CLI Reference](cli_reference.md#teklinicv-render) for the complete list of options available for the `render` command.

    !!! tip
        To re-render automatically whenever you save changes, use the `--watch` option:

        ```bash
        teklinicv render --watch "Your_Name_CV.yaml"
        ```
