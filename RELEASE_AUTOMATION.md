# Release Automation Guide

This project uses GitHub Actions to automate the release process. Here's how it works:

## Automated Workflows

### 1. Testing (`test.yml`)
- **Trigger**: Push to main branch or pull requests
- **Purpose**: Run tests across Python 3.8-3.12
- **Actions**: 
  - Lint code with flake8
  - Test CLI functionality 
  - Build and test package installation

### 2. Version Bump (`version-bump.yml`)
- **Trigger**: Manual workflow dispatch
- **Purpose**: Bump version and prepare for release
- **Actions**:
  - Bumps version in `pyproject.toml` and `__init__.py`
  - Creates new CHANGELOG entry
  - Creates and pushes git tag
  - Opens PR for manual changelog editing

### 3. Release (`release.yml`)
- **Trigger**: When version tags (v*) are pushed
- **Purpose**: Create GitHub release and publish to PyPI
- **Actions**:
  - Build wheel and source distribution
  - Create GitHub release with assets
  - Publish to PyPI automatically

## Release Process

### Option 1: Automated Version Bump (Recommended)

1. **Start the release process**:
   - Go to GitHub Actions → "Version Bump and Release"
   - Click "Run workflow"
   - Choose version bump type (patch/minor/major)
   - Click "Run workflow"

2. **Update the changelog**:
   - The workflow will create a PR with a template changelog
   - Edit the CHANGELOG.md to add actual changes
   - Merge the PR

3. **Automatic release**:
   - When the tag is pushed, the release workflow automatically:
     - Builds the package
     - Creates GitHub release
     - Publishes to PyPI

### Option 2: Manual Release

1. **Update version manually**:
   ```bash
   # Edit pyproject.toml and src/displayctl/__init__.py
   # Update CHANGELOG.md
   git add .
   git commit -m "Bump version to X.Y.Z"
   git tag vX.Y.Z
   git push origin main
   git push origin vX.Y.Z
   ```

2. **Automatic publishing**:
   - The release workflow will trigger on the tag push
   - Everything else is automated

## Prerequisites

### GitHub Repository Settings

1. **PyPI Publishing**:
   
   ✅ **Trusted Publishing (Active)**
   - Configured on PyPI for this repository
   - No API tokens needed - more secure!
   - Uses GitHub's OIDC tokens for authentication

2. **Repository Permissions**:
   - Ensure Actions have write permissions to contents
   - Go to Settings → Actions → General → Workflow permissions
   - Select "Read and write permissions"

### Required Repository Secrets

✅ **None required!** - Trusted publishing handles authentication automatically.

## Workflow Features

- ✅ **Version consistency checking**: Ensures tag matches package version
- ✅ **Automatic changelog extraction**: Pulls release notes from CHANGELOG.md
- ✅ **Multi-format publishing**: Creates both wheel and source distributions
- ✅ **GitHub release creation**: With downloadable assets
- ✅ **PyPI publishing**: Automatic upload to PyPI
- ✅ **Python version testing**: Tests across Python 3.8-3.12
- ✅ **Dependency updates**: Dependabot keeps actions updated

## Troubleshooting

### Release workflow fails

- Verify version in `pyproject.toml` matches the git tag
- Ensure CHANGELOG.md has an entry for the version
- Check that trusted publishing is configured correctly on PyPI

### Version bump workflow fails  

- Check repository has write permissions for Actions
- Verify the current version format in `pyproject.toml`

### PyPI upload fails

- Verify trusted publishing is set up correctly on PyPI
- Check that version doesn't already exist on PyPI
- Ensure the repository name matches the PyPI trusted publishing config
