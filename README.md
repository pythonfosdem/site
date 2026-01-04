# PythonFOSDEM 2026 - Website

Official website for the Python FOSDEM 2026 conference, built with [Lektor](https://www.getlektor.com/).

## Technology Stack

- **Static Site Generator**: Lektor 3.3.10 (Flask-based)
- **Python**: 3.12.12
- **Templates**: Jinja2 3.1.2
- **Frontend**: Bootstrap 3.3.7
- **Automation**: Taskfile
- **Deployment**: Netlify (self-hosted)

## Prerequisites

- Python 3.12.12 (recommended to use [pyenv](https://github.com/pyenv/pyenv) or [asdf](https://asdf-vm.com/))
- [Task](https://taskfile.dev/) (for command automation)

## Installation

### 1. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies

```bash
task dependencies:install
```

This will install Lektor and all necessary dependencies defined in `requirements.txt`.

## Usage

### Local Development

Start the development server with hot reload:

```bash
task serve
```

The site will be accessible at http://localhost:5000

### Build the Site

Generate static files in the `./output/` folder:

```bash
task build
```

### Clean Artifacts

Remove build files:

```bash
task clean
```

### Dependency Management

Compile dependencies from `requirements.in`:

```bash
task dependencies:build
```

Update all dependencies to latest versions:

```bash
task dependencies:update
```

## Project Structure

```
/
├── content/          # Content pages (.lr format)
│   ├── talks/       # Conference talks
│   ├── speakers/    # Speaker profiles
│   └── ...
├── templates/        # Jinja2 HTML templates
│   └── blocks/      # Flow block templates
├── models/          # Schema definitions (.ini)
├── flowblocks/      # Reusable content block types
├── databags/        # Static data collections
├── packages/        # Custom Lektor plugins
├── assets/          # Static files (CSS, images)
├── output/          # Generated static site (ignored by git)
└── .venv/           # Python virtual environment
```

## Content Format

Content files use the `.lr` (Lektor Record) format:

```yaml
_model: page
---
title: My Page
---
body:

#### md-section ####
title: Section Title
----
content: Markdown content here
```

- `---` separates fields
- `####` separates flow blocks
- Directory hierarchy = URL structure

## Direct Lektor Commands

If you need more control:

```bash
# Server with specific options
.venv/bin/lektor serve --verbose --prune

# Build to custom output directory
.venv/bin/lektor build --output-path=/path/to/output

# Clean cache
.venv/bin/lektor clean
```

## Deployment

The site is automatically deployed to **Netlify** when pushing to the main branch. Netlify:

1. Detects changes on the GitHub repository
2. Installs Python 3.12.12 and dependencies
3. Runs `lektor build`
4. Publishes the `output/` folder content

No manual action is required for deployment.

## Common Workflows

### Add a New Page

1. Create a folder in `/content/`, e.g., `/content/my-page/`
2. Add a `contents.lr` file with the `page` model
3. Add content using flow blocks (md-section, location, etc.)
4. Optional: add to navigation in `/databags/menu.ini`

### Add a Speaker/Talk

1. Create `/content/speakers/speaker-name/contents.lr` with the `speaker` model
2. Create `/content/talks/talk-title/contents.lr` with the `talk` model
3. Link the talk to the speaker via the `author` field

## Custom Plugins

- **humanize_date**: Jinja2 filter to format dates (e.g., "January 01, 2026")

## Additional Documentation

- [Lektor Documentation](https://www.getlektor.com/docs/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [CLAUDE.md](./CLAUDE.md) - Detailed guide for Claude Code

## Project Configuration

The `PythonFOSDEM.lektorproject` file contains site configuration:
- Project name and event date
- GitHub and Twitter URLs
- CFP (Call for Proposals) dates

## Contributing

To contribute to the site:

1. Fork the project
2. Create a branch for your feature
3. Test locally with `task serve`
4. Submit a Pull Request

## License

See the LICENSE file for more information.
